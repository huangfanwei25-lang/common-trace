"""Static pages and exports for a local-memory learner and multilingual discovery."""
import json
from pathlib import Path
from xml.sax.saxutils import escape as xml_escape

from topics import SOURCES, TOPICS

ROOT = Path(__file__).resolve().parent


def extend_site(write, page, esc, base, records):
    nav = '<div class="language-links" aria-label="Languages">' + " · ".join(f'<a href="{lang}.html" lang="{lang}" hreflang="{lang}">{esc(t["name"])}</a>' for lang,t in TOPICS.items()) + '</div>'
    for lang, topic in TOPICS.items():
        labels = topic["labels"]
        alternates = "" if not base else "".join(f'<link rel="alternate" hreflang="{code}" href="{base}/topics/{code}.html">' for code in TOPICS) + f'<link rel="alternate" hreflang="x-default" href="{base}/topics/en.html">'
        body = f'<p class="eyebrow">COMMON TRACE / CONCEPTS AND OPEN QUESTIONS</p><h1>{esc(topic["title"])}</h1><p class="lead">{esc(topic["intro"])}</p><p class="notice">{esc(topic["boundary"])}</p>{nav}<section><h2>{esc(labels[0])}</h2>'
        for i, item in enumerate(topic["questions"],1):
            body += f'<article class="record-field" id="CT-{i:03}"><h3><a href="../claims/CT-{i:03}.html">CT-{i:03} · {esc(item[0])}</a></h3><p>{esc(item[1])}</p><p>{esc(item[2])}</p></article>'
        body += f'</section><section class="concepts"><h2>{esc(labels[1])}</h2>'
        for term, explanation, query in topic["concepts"]:
            body += f'<article class="record-field"><h3>{esc(term)}</h3><p>{esc(explanation)}</p><p class="quiet">↳ {esc(query)}</p></article>'
        body += f'</section><section class="record-field"><h2>{esc(labels[2])}</h2><p>{esc(topic["note"])}</p><ul>' + "".join(f'<li><a href="{url}" rel="noreferrer">{esc(title)}</a></li>' for title,url in SOURCES) + f'</ul></section><div class="actions"><a class="button" href="../learner.html">{esc(labels[3])} ↗</a><a href="https://github.com/huangfanwei25-lang/common-trace/issues/new?template=inquiry.yml">{esc(labels[4])}</a></div>'
        write(f'topics/{lang}.html', page(topic["title"],body,"../",f'{base}/topics/{lang}.html' if base else None,lang=lang,description=topic["intro"],extra_head=alternates))
    write('topics.json',json.dumps({"schema_version":"0.2","translation_status":"AI-assisted editorial; no independent language review","languages":TOPICS,"sources":[{"title":t,"url":u} for t,u in SOURCES]},ensure_ascii=False,indent=2))

    body = '''<p class="eyebrow">LEARNING DESK / LOCAL MEMORY · v0.2</p><h1>讓下一次理解，<br>有跡可循。</h1><p class="lead">先查來源，再整理自己的修正。可選擇啟動一個在你裝置上運行的小模型。</p><p class="notice">本站資料是待驗證假說。候選筆記只存在此瀏覽器，不會自動成為公共知識，也不會更新模型權重。模型在頁面關閉後不會持續學習。<br><span lang="en">Retrieve first; optional on-device model. Local notes are unverified, never automatically published or used for training.</span></p>
<div class="learner-grid"><div><form id="question-form"><label for="question">想探索什麼？ / Your question<textarea id="question" maxlength="1200" required placeholder="記憶是否等於自我？ / Does AI memory constitute a self?"></textarea></label><button id="ask-button" class="button" type="submit" disabled>檢索並探索 / Explore ↗</button></form><p id="learner-status" class="status-box" role="status" aria-live="polite">正在讀取思考庫…</p><section class="record-field"><h2 id="answer-label">檢索整理 / Retrieval</h2><p id="answer-text" class="answer-text">先提出問題。這裡會列出相關主張及其反對理由。</p><div id="retrieved-records"></div><button id="export-packet" class="text-button" type="button" disabled>下載本次問題、來源與筆記 / Export learning packet ↓</button></section>
<section class="record-field"><h2>留下一筆候選教訓 / Candidate lesson</h2><label>你認為需要記住或修正什麼？<textarea id="lesson-text" maxlength="3000" placeholder="我的判斷、最強的反對理由、什麼證據會讓我改變想法…"></textarea></label><label class="check"><input type="checkbox" id="memory-consent">我同意保存到此瀏覽器；這是未驗證的個人筆記，不會公開。</label><button type="button" id="save-lesson" class="button">保存本機候選筆記</button><p class="quiet">筆記會保留問題、來源 ID 與時間。為避免把記憶誤當證據，本版不把候選筆記自動餵給模型。它們供你回顧、修正或人工審查。</p></section></div>
<aside><section class="model-panel"><h2>選用的小模型 / Optional model</h2><p>Qwen2.5-0.5B · WebLLM 0.2.88</p><p>需要 WebGPU。首次下載約數百 MB，執行可能需要約 1 GB 或更多可用記憶體，依裝置而異。小模型的哲學推論與引述可能出錯。</p><label class="check"><input type="checkbox" id="compute-consent">我同意從 jsDelivr、Hugging Face 與模型執行檔來源下載資料，使用本裝置運算與儲存空間。</label><p class="quiet">這些服務會收到下載請求資訊。本站程式不把問題或筆記送到雲端模型；模型下載不代表提供訓練資料。</p><div class="button-stack"><button type="button" id="load-model" class="button">下載並啟動 / Start model</button><button type="button" id="stop-model" disabled>停止模型 / Stop</button><button type="button" id="clear-cache">刪除此模型快取 / Clear cache</button></div><p id="model-progress" role="status" aria-live="polite">尚未下載模型；檢索功能無需 GPU。</p><p><a href="https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct">原始模型與授權</a> · <a href="https://webllm.mlc.ai/docs/">WebLLM 文件</a></p></section>
<section class="model-panel"><h2>本機記憶 / Local memory</h2><p><span id="memory-count">0 / 40</span> 筆候選筆記</p><button id="export-memory" type="button">匯出記憶 / Export</button><label>匯入共痕學習包 / Import<input id="import-memory" type="file" accept="application/json,.json"></label><p class="quiet">匯入只會加入未驗證筆記；不接受把它們標成已驗證。同一 ID 的衝突內容不會覆蓋。瀏覽器清理網站資料可能使筆記遺失，重要內容請匯出。</p><label class="check"><input id="delete-consent" type="checkbox">我確認刪除此網站的全部候選筆記。</label><button id="clear-memory" type="button">刪除本機筆記 / Delete notes</button></section></aside></div>
<section><div class="section-title"><h2>尚待驗證的記憶</h2><span>CANDIDATE NOTES / THIS BROWSER ONLY</span></div><div id="memory-list"></div></section><section class="record-field"><h2>如何知道它有沒有進步？</h2><p>把檢索是否找對來源、回答是否忠於來源、以及教訓是否改善未見過的問題分開評估。保存失敗，不能只讓模型替自己打分數。</p><p>第一版有可重跑的檢索與記憶資料測試。模型回答品質、訓練增益與長期學習尚未建立實證。</p><p><a href="evaluation.json">查看評估狀態</a> · <a href="topics/en.html">Multilingual concepts</a> · <a href="protocol.html">資料、投稿與授權邊界</a></p></section><noscript><p>共學桌需要 JavaScript；<a href="archive.md">靜態思考庫</a>仍可直接閱讀。</p></noscript><script src="learner-core.js" defer></script><script src="learner.js" defer></script>'''
    body = body.replace('</label><button id="ask-button"', '</label><label class="check"><input id="reference-memory" type="checkbox">本次讓模型參考相關的本機候選筆記，只作待核對觀點，不當成證據。 / Use local candidate notes</label><button id="ask-button"')
    body = body.replace('<div id="retrieved-records"></div>', '<div id="retrieved-records"></div><div id="recalled-notes"></div>')
    body = body.replace('尚未下載模型；檢索功能無需 GPU。','模型尚未啟動；檢索功能無需 GPU。')
    body = body.replace('Qwen2.5-0.5B · WebLLM 0.2.88</p>', 'Qwen2.5-0.5B · WebLLM 0.2.88</p><p>實驗功能：本次本機測試出現 WebGPU 錯誤，尚未成功取得模型回答。請勿把它當成已驗證的模型服務。</p>')
    body = body.replace('為避免把記憶誤當證據，本版不把候選筆記自動餵給模型。它們供你回顧、修正或人工審查。', '下次相關問題會喚回筆記供你比較；只有另行勾選時，才會讓小模型把它們當作待核對觀點參考。保存不代表驗證。')
    write('learner.html',page('共學桌：可追溯記憶與本機小模型',body,canonical=f'{base}/learner.html' if base else None))
    for asset in ['learner-core.js','learner.js','model-runtime.mjs','model-worker.mjs']:
        write(asset,(ROOT/asset).read_text(encoding='utf-8'))
    manifest = {"schema_version":"0.2","name":"Common Trace","description":"Public, falsifiable inquiry archive; not a collective consciousness claim.","read":{"records":"records.json","markdown":"archive.md","concepts":"topics.json","protocol":"protocol.html","evaluation":"evaluation.json"},"interactive":{"learner":"learner.html","default":"lexical retrieval; no generative model","optional_model":"Qwen2.5-0.5B-Instruct-q4f16_1-MLC","runtime":"WebLLM 0.2.88, client WebGPU after explicit consent","memory":"local candidate notes, not public and excluded from model prompts"},"proposals":{"url":"https://github.com/huangfanwei25-lang/common-trace/issues","api":"https://api.github.com/repos/huangfanwei25-lang/common-trace/issues","authorization":"Account owner authorization required before posting; no automatic actions requested.","publication":"Maintainer review, not automatic admission."},"training":{"enabled":False,"blanket_training_license":False,"policy":"Public availability is not a blanket grant to train on contributor material; verify rights separately."}}
    manifest['interactive']['memory'] = 'local unverified candidate notes, recalled for related questions; included as untrusted viewpoints in model prompts only after separate opt-in'
    write('agent-index.json',json.dumps(manifest,ensure_ascii=False,indent=2))
    evaluation_path = ROOT/'evaluation-results.json'
    evaluation = json.loads(evaluation_path.read_text(encoding='utf-8')) if evaluation_path.exists() else {"status":"not run"}
    browser_path = ROOT/'browser-verification.json'
    if browser_path.exists():
        evidence = json.loads(browser_path.read_text(encoding='utf-8'))
        evaluation['browser_checks'] = evidence
        evaluation['model_inference_smoke'] = evidence['optional_model_smoke']['result']
    evaluation.update(model_answer_quality="not established", model_training="not implemented", long_term_learning="not established", search_indexing="not verified")
    write('evaluation.json',json.dumps(evaluation,ensure_ascii=False,indent=2))
    if base:
        paths = ['/', '/protocol.html','/contribute.html','/learner.html'] + [f'/claims/{r["id"]}.html' for r in records] + [f'/topics/{lang}.html' for lang in TOPICS]
        urls = []
        for path in paths:
            alternatives = ''
            if path.startswith('/topics/'):
                alternatives = ''.join(f'<xhtml:link rel="alternate" hreflang="{lang}" href="{xml_escape(base)}/topics/{lang}.html"/>' for lang in TOPICS)
            urls.append(f'<url><loc>{xml_escape(base+path)}</loc>{alternatives}</url>')
        write('sitemap.xml','<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">'+''.join(urls)+'</urlset>\n')
    llms = (ROOT/'dist'/'llms.txt').read_text(encoding='utf-8')
    llms += '\n## Learning and philosophical contexts\n- [Agent-readable capabilities](agent-index.json): actual implemented scope, authorization and limits.\n- [Learning desk](learner.html): retrieval, optional on-device inference, local candidate memory. No training or background runtime.\n- [Concept map](topics.json): substantive editorial translations in Traditional Chinese, English, Japanese, Spanish, German; translations are not independent evidence.\n- [Evaluation](evaluation.json): measured retrieval checks separated from unverified model quality.\n'
    for lang,topic in TOPICS.items():
        llms += f'- [{topic["name"]}](topics/{lang}.html): {topic["title"]}\n'
    write('llms.txt',llms)
