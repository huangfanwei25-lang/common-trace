(function(root, factory) {
  const api = factory();
  if (typeof module === 'object' && module.exports) module.exports = api;
  else root.TracePractice = api;
})(globalThis, function() {
  'use strict';
  const text = value => typeof value === 'string' ? value.trim() : '';
  function freezeBefore(caseRecord, answer, created = new Date().toISOString()) {
    if (!caseRecord || !/^PR-\d{3}$/.test(caseRecord.id)) throw new Error('練習題 ID 無效。');
    if (!text(answer) || answer.length > 4000) throw new Error('第一次回答需為 1–4000 字。');
    // Clone the complete public scenario so future corpus revisions cannot change this attempt.
    const snapshot = JSON.parse(JSON.stringify(caseRecord));
    return {schema_version:'0.1', kind:'public-practice-attempt', created, case_snapshot:snapshot,
      before:{text:text(answer), recorded_before_ui_reference_reveal:true},
      evidence_status:'self-reported practice; not independently evaluated',
      limits:['References and criteria are publicly accessible; this is not a blind test.', 'A changed answer is not proof of learning.', 'No causal effect, model training or collective consciousness is established.', 'Export is local, not a public submission.']};
  }
  function finish(attempt, answer, reason, judgment) {
    if (!attempt || attempt.kind !== 'public-practice-attempt' || !attempt.before?.text) throw new Error('請先固定第一次回答。');
    if (!text(answer) || answer.length > 4000 || !text(reason) || reason.length > 4000) throw new Error('請填寫後續回答與理由，各限 1–4000 字。');
    if (!['revised','retained','uncertain'].includes(judgment)) throw new Error('請選擇本次判斷狀態。');
    return {...JSON.parse(JSON.stringify(attempt)), after:{text:text(answer),reason:text(reason),self_judgment:judgment},
      comparison:{text_changed:text(answer)!==attempt.before.text, independently_scored:false, learning_effect:'not estimated'}};
  }
  return {freezeBefore,finish};
});
