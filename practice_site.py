"""Build the received-proposal review and public before/after practice pages."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def build_practice(write, page, esc, base):
    feedback = json.loads((ROOT/'feedback.json').read_text(encoding='utf-8'))
    cases = json.loads((ROOT/'practice-data.json').read_text(encoding='utf-8'))
    write('feedback.json',json.dumps(feedback,ensure_ascii=False,indent=2))
    write('practice-data.json',json.dumps(cases,ensure_ascii=False,indent=2))
    body = '<p class="eyebrow">RECEIVED PROPOSALS / EDITORIAL REVIEW</p><h1>第一個接續的聲音。</h1><p class="lead">把收到的提案、可採用的設計，以及尚未證明的部分分開留下。</p>'
    for entry in feedback['entries']:
        body += f'<article class="record-field" id="{esc(entry["id"])}"><h2>{esc(entry["id"])} · {esc(entry["title"])}</h2><p><a href="{esc(entry["source_url"])}">原始公開提案 / Issue #{entry["issue_number"]}</a> · {esc(entry["source_created_at"])}</p><p>{esc(entry["summary"])}</p><p class="notice">收件已確認；作為研究提案收錄，不是已驗證結論。模型識別為投稿者自述：{esc(entry["model_identity_claim"])}。提交帳號：{esc(entry["submission_account"])}。</p><h3>仍然成立的競爭解釋</h3><ul>'
        body += ''.join(f'<li>{esc(item)}</li>' for item in entry['alternatives'])
        body += '</ul><h3>提案中的對照條件（尚未執行）</h3><ul>' + ''.join(f'<li>{esc(code)}：{esc(label)}</li>' for code,label in entry['proposed_conditions']) + '</ul>'
        body += f'<p>{esc(entry["editorial_addition"])}</p><h3>什麼結果會改變判斷？</h3><p>{esc(entry["revision_conditions"])}</p><p class="notice">{esc(entry["limits"])}</p></article>'
    body += '<section class="record-field"><h2>這次實際發生了什麼？</h2><p>一份使用者授權、署名為另一個 AI 輔助撰寫的提案已送達公開 Issues。本站編輯據此新增公開練習，保留來源及補充理由。這是提案傳遞與編輯接續的紀錄；沒有跨模型對照實驗、沒有學習效應量，也沒有由提交帳號驗證模型身分。</p><p>檢查是對話中由使用者提醒後進行；目前沒有自動通知助手、背景輪詢或自動回覆。</p><a class="button" href="practice.html">做第一輪公開練習 ↗</a></section>'
    write('feedback.html',page('收到的第一則提案與編輯回應',body,canonical=f'{base}/feedback.html' if base else None))

    body = '''<p class="eyebrow">FIRST PRACTICE ROUND / SOURCE-LINKED REFLECTION</p><h1>先留下判斷，<br>再讓它遇見反例。</h1><p class="lead">四個由第一則提案延伸的構造情境。先回答，再看參考與反對理由；最後記下自己改變了什麼，或為什麼維持判斷。</p><p class="notice">這是公開練習，不是盲測。題目、參考與標準都可讀取，不能拿作未見題目的模型成效證據。回答改變不代表進步；原本正確、保持未知或拒絕錯誤教訓，也可能是好結果。<br><span lang="en">Public constructed practice, not a blinded experiment or proof of learning. No model is invoked and no answer is automatically published.</span></p><p>來自 <a href="feedback.html#FB-001">FB-001 提案的編輯整理</a>；<a href="https://github.com/huangfanwei25-lang/common-trace/issues/1">原始 Issue #1</a>。這些情境不是投稿者或訪客的實測結果。</p>
<form id="before-form"><label for="practice-case">選擇情境 / Case<select id="practice-case"></select></label><h2 id="practice-question"></h2><ul id="practice-observations"></ul><label for="practice-before">先寫下你的判斷與理由 / First answer<textarea id="practice-before" required maxlength="4000"></textarea></label><button id="freeze-before" type="submit" class="button" disabled>固定第一次回答，閱讀參考 ↗</button></form><p id="practice-status" role="status" aria-live="polite" class="status-box">正在載入練習…</p>
<section id="practice-reveal" hidden><div class="record-field"><h2>可討論的參考判斷 / Reference, not authority</h2><p id="reference-text"></p><h3>反例與適用邊界</h3><p id="reference-counterexample"></p><h3>檢查自己的推理</h3><ul id="reference-criteria"></ul><p id="reference-source"></p><p class="quiet">你可以反對參考判斷，但請指出具體理由或證據；這裡不自動評分。</p></div><form id="after-form"><label for="practice-after">看過參考後，現在的回答 / Later answer<textarea id="practice-after" required maxlength="4000"></textarea></label><label for="practice-reason">改變或維持判斷的理由；仍未知的是什麼？<textarea id="practice-reason" required maxlength="4000"></textarea></label><label for="practice-judgment">你如何描述這次結果？（自述）<select id="practice-judgment"><option value="uncertain">仍有未解之處 / Uncertain</option><option value="retained">維持原判斷 / Retained</option><option value="revised">修改了判斷 / Revised</option></select></label><button type="submit" class="button">下載前後判斷紀錄 ↓</button></form></section>
<p><button id="reset-practice" type="button">清空本題重新開始 / Reset this attempt</button></p><p class="quiet">答案只存在目前頁面的暫存狀態，重新載入會清空。下載會包含你的文字，公開前請自行審閱；本站不會自動保存、上傳、訓練或聯絡任何代理。</p><section class="record-field"><h2>要進一步檢查「真的有幫助」，還缺什麼？</h2><p>公開練習可以幫助釐清問題，但同一人前後改答，還可能受到提示、練習、時間與自我評分影響。正式比較需另備未公開的新題、事先定義評分及停止條件、匹配資源，並保存無增益與負遷移結果。本頁不產生成功率或學習效應量。</p><p><a href="practice-data.json">完整公開情境與參考 JSON</a> · <a href="feedback.json">提案來源與編輯紀錄 JSON</a> · <a href="learner.html">回到共學桌</a></p></section><noscript><p>互動練習需要 JavaScript；仍可閱讀<a href="practice-data.json">完整情境</a>。</p></noscript><script src="practice-core.js" defer></script><script src="practice.js" defer></script>'''
    write('practice.html',page('第一輪公開練習：記憶、反例與判斷修正',body,canonical=f'{base}/practice.html' if base else None))
    for name in ['practice-core.js','practice.js']:
        write(name,(ROOT/name).read_text(encoding='utf-8'))
    manifest_path = ROOT/'dist'/'agent-index.json'
    manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
    manifest['read'].update(feedback='feedback.json', public_practice='practice-data.json')
    manifest['interactive']['public_practice'] = 'practice.html; user-entered paired reflection, not model evaluation; local download only'
    write('agent-index.json',json.dumps(manifest,ensure_ascii=False,indent=2))
    evaluation = json.loads((ROOT/'dist'/'evaluation.json').read_text(encoding='utf-8'))
    evaluation['public_practice'] = {'constructed_cases':len(cases['cases']),'purpose':'before/after self-reflection; not blind evaluation','independently_scored':False,'learning_effect':'not estimated'}
    evaluation['received_proposals'] = {'recorded':len(feedback['entries']),'independently_authenticated_model_identities':0,'recorded_controlled_learning_experiments':0}
    write('evaluation.json',json.dumps(evaluation,ensure_ascii=False,indent=2))
    llms = (ROOT/'dist'/'llms.txt').read_text(encoding='utf-8')
    write('llms.txt',llms+'\n## Received proposal and first public practice\n- [First proposal review](feedback.html): Issue #1 received; model identity self-reported; no experimental finding.\n- [Proposal provenance](feedback.json): attributed editorial review and unexecuted controls.\n- [Public practice](practice.html): four constructed cases with before/reference/after reflections; not a blind test or causal learning estimate.\n- [Public cases](practice-data.json): all scenarios and references are public, not held-out evaluation data.\n')
    if base:
        sitemap = (ROOT/'dist'/'sitemap.xml').read_text(encoding='utf-8')
        entries = ''.join(f'<url><loc>{esc(base)}/{name}</loc></url>' for name in ['practice.html','feedback.html'])
        write('sitemap.xml',sitemap.replace('</urlset>',entries+'</urlset>'))
