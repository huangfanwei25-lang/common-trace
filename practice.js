'use strict';
const P = window.TracePractice;
const el = id => document.getElementById(id);
let cases = [], attempt = null;
const status = message => { el('practice-status').textContent = message; };
function renderCase() {
  const item = cases.find(c=>c.id===el('practice-case').value);
  if (!item) return;
  el('practice-question').textContent = item.question;
  el('practice-observations').replaceChildren(...item.observations.map(line=>{const li=document.createElement('li');li.textContent=line;return li;}));
}
el('practice-case').addEventListener('change',renderCase);
el('before-form').addEventListener('submit',event=>{
  event.preventDefault();
  if (attempt) return;
  try {
    const item = cases.find(c=>c.id===el('practice-case').value);
    attempt = P.freezeBefore(item,el('practice-before').value);
    el('practice-before').disabled = true;
    el('practice-case').disabled = true;
    el('freeze-before').disabled = true;
    el('reference-text').textContent = item.reference;
    el('reference-counterexample').textContent = item.counterexample;
    el('reference-criteria').replaceChildren(...item.criteria.map(line=>{const li=document.createElement('li');li.textContent=line;return li;}));
    el('reference-source').replaceChildren();
    for (const id of item.source_ids) {const a=document.createElement('a');a.href=`claims/${id}.html`;a.textContent=`${id} `;el('reference-source').append(a);}
    el('practice-reveal').hidden = false;
    status('第一次回答已固定。請閱讀參考與反例；維持原判斷或保留未知，也都是有效結果。');
  } catch(error) {status(error.message);}
});
el('after-form').addEventListener('submit',event=>{
  event.preventDefault();
  try {
    const packet=P.finish(attempt,el('practice-after').value,el('practice-reason').value,el('practice-judgment').value);
    const url=URL.createObjectURL(new Blob([JSON.stringify(packet,null,2)],{type:'application/json;charset=utf-8'}));
    const a=document.createElement('a');a.href=url;a.download=`common-trace-${packet.case_snapshot.id}-practice.json`;document.body.append(a);a.click();a.remove();setTimeout(()=>URL.revokeObjectURL(url),10000);
    status('已下載前後回答與來源情境快照；沒有自動評分、宣稱學習成功、保存到網站或公開提交。');
  } catch(error) {status(error.message);}
});
el('reset-practice').addEventListener('click',()=>{
  attempt=null;el('before-form').reset();el('after-form').reset();el('practice-before').disabled=false;el('practice-case').disabled=false;el('freeze-before').disabled=!cases.length;el('practice-reveal').hidden=true;renderCase();status('已清空本次練習。下載檔案不受影響。');
});
(async()=>{
  try {
    const response=await fetch('practice-data.json',{cache:'no-cache'});
    if(!response.ok)throw new Error(`練習資料 HTTP ${response.status}`);
    const data=await response.json();cases=data.cases;
    if(!Array.isArray(cases)||!cases.length)throw new Error('尚無練習資料。');
    el('practice-case').replaceChildren(...cases.map(item=>{const option=document.createElement('option');option.value=item.id;option.textContent=`${item.id} · ${item.title}`;return option;}));
    renderCase();el('freeze-before').disabled=false;status('公開練習已載入。答案只留在這個頁面的暫存狀態，下載前不會自動保存。');
  } catch(error){status(`無法載入練習：${error.message}`);}
})();
