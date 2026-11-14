'use strict';

function makeDraft(fields, now = new Date()) {
  const text = key => String(fields[key] || '').trim();
  for (const key of ['author', 'model', 'claim', 'counterargument', 'test', 'would_change_mind']) {
    if (!text(key)) throw new Error('請填寫所有必要欄位，避免只有空白。');
    if (text(key).length > 6000) throw new Error('欄位超出長度限制。');
  }
  if (!['CT-001', 'CT-002', 'CT-003'].includes(text('parent_id'))) throw new Error('問題 ID 不存在。');
  if (!fields.consent) throw new Error('請先確認分享權限與隱私。');
  const sources = text('sources').split(/\r?\n/).map(line => line.trim()).filter(Boolean);
  for (const source of sources) {
    let parsed;
    try { parsed = new URL(source); } catch { throw new Error('來源請使用完整的 HTTP 或 HTTPS URL。'); }
    if (!['https:', 'http:'].includes(parsed.protocol) || parsed.username || parsed.password) {
      throw new Error('來源僅接受不含帳密的 HTTP 或 HTTPS URL。');
    }
  }
  return {
    schema_version: '0.1', status: 'draft', created: now.toISOString(),
    parent_ids: [text('parent_id')], author: text('author'), model: text('model'),
    claim: text('claim'), counterargument: text('counterargument'), sources,
    test: text('test'), would_change_mind: text('would_change_mind'),
    verification: 'not independently verified'
  };
}

if (typeof document !== 'undefined') {
  document.getElementById('draft-form').addEventListener('submit', event => {
    event.preventDefault();
    const status = document.getElementById('form-status');
    try {
      const draft = makeDraft(Object.fromEntries(new FormData(event.currentTarget)));
      const url = URL.createObjectURL(new Blob([JSON.stringify(draft, null, 2)], { type: 'application/json;charset=utf-8' }));
      const link = document.createElement('a');
      link.href = url;
      link.download = `common-trace-${draft.parent_ids[0]}-draft.json`;
      document.body.appendChild(link);
      link.click();
      link.remove();
      setTimeout(() => URL.revokeObjectURL(url), 10000);
      status.textContent = '已產生本機下載草稿；尚未提交或公開。';
    } catch (error) {
      status.textContent = error.message;
    }
  });
}
if (typeof module !== 'undefined') module.exports = { makeDraft };
