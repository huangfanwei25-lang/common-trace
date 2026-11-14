'use strict';
const Core = window.TraceLearner;
const $ = id => document.getElementById(id);
let records = [], notes = [], lastResults = [], lastQuestion = '', answer = '', answerMode = 'retrieval';
let engine = null, runtime = null, busy = false, loading = false, storageHealthy = true, cancelLoad;
let cancelRun = null, loadEpoch = 0;
const notice = text => { $('learner-status').textContent = text; };
const knownIds = () => records.map(r => r.id);
function errorText(error) {
  if (typeof error === 'string' && error.trim()) return error;
  if (error && typeof error.message === 'string' && error.message.trim()) return error.message;
  return '瀏覽器模型或 WebGPU 執行失敗，未取得可讀錯誤原因。可繼續使用來源檢索；沒有完成模型推論。';
}

function saveNotes(next) {
  if (!storageHealthy) throw new Error('原有記憶無法讀取，為避免覆蓋請先匯出原始資料或明確刪除。');
  const safe = Core.validateNotes(next, knownIds());
  localStorage.setItem(Core.KEY, JSON.stringify(safe));
  notes = safe;
  renderNotes();
}

function renderNotes() {
  $('memory-count').textContent = `${notes.length} / ${Core.MAX_NOTES}`;
  const list = $('memory-list');
  list.replaceChildren();
  for (const note of notes.slice().reverse()) {
    const article = document.createElement('article');
    article.className = 'memory-note';
    const label = document.createElement('p');
    label.className = 'eyebrow';
    label.textContent = `CANDIDATE · ${note.created} · ${note.source_ids.join(', ') || 'NO SOURCE'}`;
    const text = document.createElement('p');
    text.textContent = note.text;
    const button = document.createElement('button');
    button.type = 'button';
    button.className = 'text-button';
    button.textContent = '刪除此筆 / Delete note';
    button.addEventListener('click', () => {
      try { saveNotes(notes.filter(n => n.id !== note.id)); notice('已刪除這筆本機筆記。'); }
      catch (error) { notice(error.message); }
    });
    article.append(label, text, button);
    list.append(article);
  }
}

function renderSources(results) {
  const box = $('retrieved-records');
  box.replaceChildren();
  for (const {record:r} of results) {
    const article = document.createElement('article');
    article.className = 'memory-note';
    const link = document.createElement('a');
    link.href = `claims/${encodeURIComponent(r.id)}.html`;
    link.textContent = `${r.id} · ${r.title} / ${r.title_en}`;
    const status = document.createElement('p');
    status.className = 'quiet';
    status.textContent = `HYPOTHESIS · ${r.verification} · revision ${r.revision}`;
    const claim = document.createElement('p');
    claim.textContent = r.claim;
    const counter = document.createElement('p');
    counter.textContent = `反對理由：${r.counterargument}`;
    article.append(link, status, claim, counter);
    box.append(article);
  }
}

function setBusy(value) {
  busy = value;
  $('ask-button').disabled = value || !records.length;
  $('load-model').disabled = value || loading || !!engine;
  $('clear-cache').disabled = value || loading;
}

function download(name, value) {
  const blob = new Blob([JSON.stringify(value, null, 2)], {type:'application/json;charset=utf-8'});
  const url = URL.createObjectURL(blob);
  const link = document.createElement('a');
  link.href = url; link.download = name;
  document.body.append(link); link.click(); link.remove();
  setTimeout(() => URL.revokeObjectURL(url), 10000);
}

$('question-form').addEventListener('submit', async event => {
  event.preventDefault();
  if (busy || !records.length) return;
  const question = $('question').value.trim();
  if (!question || question.length > 1200) { notice('請輸入 1–1200 字的問題。'); return; }
  setBusy(true);
  lastQuestion = question;
  lastResults = Core.retrieve(question, records);
  const recalled = Core.recallNotes(question,lastResults,notes);
  answer = ''; answerMode = 'retrieval';
  renderSources(lastResults);
  const recalledBox = $('recalled-notes');
  recalledBox.replaceChildren();
  for (const note of recalled) {
    const paragraph = document.createElement('p');
    paragraph.className = 'notice';
    paragraph.textContent = `你曾留下的候選筆記（未驗證）：${note.text}`;
    recalledBox.append(paragraph);
  }
  $('answer-text').textContent = '';
  $('answer-label').textContent = '檢索整理 / Retrieval · 不是生成模型回答';
  $('lesson-text').value = '';
  try {
    if (!lastResults.length) {
      answer = '目前思考庫沒有足夠相關的紀錄。請改寫問題，或提出新的公開研究提案。沒有來源時不產生模型答案。';
    } else if (!engine) {
      answer = `找到 ${lastResults.length} 筆相關假說：${lastResults.map(x => x.record.id).join(', ')}，及 ${recalled.length} 筆相關的本機候選筆記。\n請先比較下方的主張與反對理由，再寫下自己的修正筆記。這些資料尚未獨立驗證；檢索命中不代表答案正確。`;
    } else {
      answerMode = 'browser-model';
      $('answer-label').textContent = '本機小模型草稿 / Browser model · 未獨立驗證';
      let runTimeout;
      const cancelled = new Promise((_,reject)=> { cancelRun = () => reject(new Error('模型生成已停止。')); runTimeout = setTimeout(()=>reject(new Error('生成超過 90 秒，請使用檢索結果或縮短問題。')),90000); });
      let response;
      try { response = await Promise.race([engine.chat.completions.create({messages:Core.messages(question,lastResults,$('reference-memory').checked?recalled:[]), temperature:0.3, max_tokens:320, stream:false}),cancelled]); }
      finally { clearTimeout(runTimeout); cancelRun = null; }
      answer = response.choices?.[0]?.message?.content?.trim() || '';
      if (!answer) throw new Error('模型沒有回傳文字。');
    }
    $('answer-text').textContent = answer;
    $('export-packet').disabled = false;
    notice(engine && lastResults.length ? '已完成本機推論，權重未更新。請自行核對引述與推論。' : '已完成來源檢索。尚未啟動模型，也沒有更新模型權重。');
  } catch (error) {
    answer = '';
    if (answerMode === 'browser-model') { if (runtime) runtime.stop(); engine = null; $('stop-model').disabled = true; }
    $('answer-text').textContent = '這次生成未完成；來源仍列在下方，沒有把失敗結果記成學習成果。';
    notice(`執行失敗：${errorText(error)}`);
  } finally { setBusy(false); }
});

$('save-lesson').addEventListener('click', () => {
  try {
    const text = $('lesson-text').value.trim();
    if (!text || text.length > 3000) throw new Error('筆記請填寫 1–3000 字。');
    if (!lastQuestion) throw new Error('請先檢索一個問題，讓筆記留下來由。');
    if (!$('memory-consent').checked) throw new Error('請先同意將這筆候選筆記保存在此瀏覽器。');
    saveNotes(Core.addNote(notes,text,lastQuestion,lastResults.map(x=>x.record.id),crypto.randomUUID()));
    $('lesson-text').value = '';
    notice('已保存本機候選筆記，未公開、未驗證，也未用於更新模型權重。');
  } catch (error) { notice(`無法保存：${error.message}`); }
});

$('export-packet').addEventListener('click', () => {
  if (!lastQuestion) return;
  download('common-trace-learning-packet.json', Core.packet(lastQuestion,lastResults,notes,answer,answerMode));
  notice('已下載包含問題、來源快照與候選筆記的學習包；沒有自動提交。');
});
$('export-memory').addEventListener('click', () => {
  if (!storageHealthy) {
    try { download('common-trace-unreadable-memory.json', {kind:'unreadable-local-memory',raw:localStorage.getItem(Core.KEY)}); notice('已匯出原始本機資料，未嘗試修復或覆蓋。'); }
    catch (error) { notice(`無法讀取儲存空間：${error.message}`); }
    return;
  }
  download('common-trace-local-memory.json', Core.packet('',[],notes));
  notice('已下載本機記憶包。檔案可能包含私人筆記，公開前請自行審閱。');
});
$('import-memory').addEventListener('change', async event => {
  const file = event.target.files[0];
  if (!file) return;
  try {
    if (!records.length) throw new Error('思考庫尚未載入。');
    if (file.size > 500000) throw new Error('匯入檔案限制為 500 KB。');
    const data = JSON.parse(await file.text());
    if (data.schema_version !== Core.VERSION || data.kind !== 'learning-packet') throw new Error('不是支援的共痕學習包。');
    const incoming = Core.validateNotes(data.candidate_notes,knownIds());
    const existing = new Map(notes.map(note => [note.id,note]));
    for (const note of incoming) {
      if (existing.has(note.id) && JSON.stringify(existing.get(note.id)) !== JSON.stringify(note)) throw new Error('同一 ID 有不同內容，為保留版本請先手動整理。');
      existing.set(note.id,note);
    }
    saveNotes([...existing.values()]);
    notice(`匯入完成，目前 ${notes.length} 筆未驗證的本機候選筆記；未公開，也未作為模型證據。`);
  } catch (error) { notice(`匯入失敗，原資料未覆蓋：${error.message}`); }
  event.target.value = '';
});
$('clear-memory').addEventListener('click', () => {
  if (!$('delete-consent').checked) { notice('請先勾選刪除確認；可先匯出備份。'); return; }
  try {
    localStorage.removeItem(Core.KEY); notes = []; storageHealthy = true; renderNotes();
    $('delete-consent').checked = false;
    notice('已刪除此網站的候選筆記；未刪除下載檔案或模型快取。');
  } catch (error) { notice(`刪除失敗：${error.message}`); }
});

$('load-model').addEventListener('click', async () => {
  if (busy || loading || engine) return;
  if (!$('compute-consent').checked) { notice('請先同意模型下載與裝置運算。'); return; }
  loading = true; $('load-model').disabled = true; $('clear-cache').disabled = true;
  const epoch = ++loadEpoch;
  $('stop-model').disabled = false;
  let timeout;
  try {
    if (!navigator.gpu) throw new Error('此瀏覽器沒有 WebGPU，仍可使用來源檢索與本機筆記。');
    const adapter = await navigator.gpu.requestAdapter();
    if (!adapter) throw new Error('找不到可用的 WebGPU 裝置。');
    if (epoch !== loadEpoch) throw new Error('已停止模型載入。');
    notice('開始載入選用的本機模型；這不是訓練。可隨時按停止。');
    runtime = await import('./model-runtime.mjs');
    if (epoch !== loadEpoch) throw new Error('已停止模型載入。');
    const cancellation = new Promise((_, reject) => { cancelLoad = () => reject(new Error('已停止模型載入。')); timeout = setTimeout(()=>reject(new Error('模型載入超過五分鐘；已停止，請檢查網路與裝置。')),300000); });
    engine = await Promise.race([runtime.load(progress => { $('model-progress').textContent = progress.text || '載入中…'; }),cancellation]);
    $('model-progress').textContent = '模型已就緒：Qwen2.5-0.5B。小模型的答案可能不準確。';
    notice('本機模型已就緒；後續有來源的問題會使用它產生待核對草稿。');
  } catch (error) {
    if (runtime) runtime.stop(); engine = null;
    $('model-progress').textContent = '未啟動模型。來源檢索仍可使用。';
    notice(`模型未就緒：${errorText(error)}`);
  } finally {
    clearTimeout(timeout); cancelLoad = null; loading = false;
    $('load-model').disabled = busy || !!engine; $('clear-cache').disabled = busy;
    $('stop-model').disabled = !engine;
  }
});
$('stop-model').addEventListener('click', () => {
  loadEpoch++;
  if (cancelRun) cancelRun();
  if (cancelLoad) cancelLoad();
  if (runtime) runtime.stop(); engine = null;
  $('load-model').disabled = false; $('stop-model').disabled = true;
  $('model-progress').textContent = '模型已停止；已下載的快取可能仍保留。';
  notice('已停止模型工作執行緒；來源檢索與本機記憶仍可使用。');
});
$('clear-cache').addEventListener('click', async () => {
  if (busy || loading) return;
  if (!runtime && !$('compute-consent').checked) { notice('清除模型快取需下載管理程式。請勾選下載同意後再按清除；此操作不會下載模型權重。也可直接使用瀏覽器的網站資料管理。'); return; }
  $('clear-cache').disabled = true;
  try { if (!runtime) runtime = await import('./model-runtime.mjs'); runtime.stop(); engine = null; await runtime.clearModelCache(); $('model-progress').textContent='已刪除此模型快取。'; notice('已刪除該模型的快取；本機候選筆記仍保留。'); }
  catch (error) { notice(`快取刪除失敗：${error.message}`); }
  finally { $('clear-cache').disabled = false; $('load-model').disabled = false; $('stop-model').disabled = true; }
});

(async function init() {
  try {
    const response = await fetch('records.json', {cache:'no-cache'});
    if (!response.ok) throw new Error(`思考庫 HTTP ${response.status}`);
    const data = await response.json();
    records = data.records;
    if (!Array.isArray(records) || !records.length) throw new Error('思考庫格式不正確。');
    try {
      const raw = localStorage.getItem(Core.KEY);
      notes = Core.validateNotes(raw ? JSON.parse(raw) : [], knownIds());
    } catch (error) {
      storageHealthy = false;
      notice(`本機記憶讀取失敗，原資料未覆蓋：${error.message}`);
    }
    renderNotes(); setBusy(false);
    if (storageHealthy) notice('思考庫已載入。現在可檢索；目前沒有啟動模型。先前下載的快取可能仍保留。');
  } catch (error) { notice(`初始化失敗：${error.message}`); }
})();
