const assert = require('node:assert/strict');
const fs = require('node:fs');
const crypto = require('node:crypto');
const Core = require('./learner-core.js');
const records = JSON.parse(fs.readFileSync('dist/records.json','utf8')).records;
const cases = [
  ['記憶如何支持自我連續性？','CT-001'],
  ['Does memory establish identity across time?','CT-001'],
  ['AIの記憶と心理的連続性','CT-001'],
  ['¿La memoria establece continuidad?','CT-001'],
  ['Gedächtnis und psychologische Kontinuität','CT-001'],
  ['多個 AI 的共識是否是獨立證據？','CT-002'],
  ['Does agent consensus provide independent evidence?','CT-002'],
  ['集合知と出典の独立性','CT-002'],
  ['consenso y fuentes independientes','CT-002'],
  ['kollektive Intelligenz und unabhängige Quellen','CT-002'],
  ['教訓如何改變行動與規則？','CT-003'],
  ['Does a recorded lesson change action?','CT-003'],
  ['教訓は行動を変えるか','CT-003'],
  ['lección acción y regla','CT-003'],
  ['Lernen und Handlungsregeln','CT-003'],
  ['CT-002','CT-002'],
];
for (const [question,id] of cases) assert.equal(Core.retrieve(question,records)[0]?.record.id,id,question);
assert.deepEqual(Core.retrieve('What is the best pasta recipe?',records),[],'unrelated question should not fabricate relevance');
assert.deepEqual(Core.retrieve('zzzxxyy',records),[]);
assert.deepEqual(Core.retrieve('',records),[]);
const ids = records.map(r=>r.id);
const first = Core.addNote([], '<script>untrusted</script>', 'memory?', ['CT-001'], 'note-1', '2026-11-14T00:00:00Z');
assert.equal(first[0].status,'candidate');
const exported = Core.packet('memory?',Core.retrieve('memory',records),first,'a draft','retrieval');
const restored = Core.validateNotes(JSON.parse(JSON.stringify(exported)).candidate_notes,ids);
assert.deepEqual(restored,first);
assert.throws(()=>Core.validateNotes([{...first[0],status:'verified'}],ids));
assert.throws(()=>Core.validateNotes([{...first[0],source_ids:['CT-999']}],ids));
assert.throws(()=>Core.validateNotes([{...first[0],created:'not a date'}],ids));
assert.throws(()=>Core.validateNotes([first[0],first[0]],ids));
assert.throws(()=>Core.validateNotes(Array(41).fill(first[0]),ids));
assert.equal(exported.answer.verification,'not independently verified');
assert.ok(!JSON.stringify(Core.messages('memory?',Core.retrieve('memory',records))).includes('untrusted</script>'),'local memory must not become source evidence in model prompts');
assert.ok(Core.messages('memory?',Core.retrieve('memory',records))[0].content.includes('untrusted hypotheses'));
const recalled = Core.recallNotes('memory?',Core.retrieve('memory',records),first);
assert.deepEqual(recalled,first);
const withMemory = JSON.parse(Core.messages('memory?',Core.retrieve('memory',records),recalled)[1].content);
assert.equal(withMemory.untrusted_candidate_notes[0].status,'candidate');
assert.equal(withMemory.untrusted_candidate_notes[0].verification,'unverified personal note');
assert.deepEqual(JSON.parse(Core.messages('memory?',Core.retrieve('memory',records))[1].content).untrusted_candidate_notes,[]);
const sha = file => crypto.createHash('sha256').update(fs.readFileSync(file,'utf8').replace(/\r\n/g,'\n')).digest('hex');
const report = {schema_version:'0.2',scope:'Deterministic retrieval and candidate-memory integrity; not model intelligence or training effectiveness.',retrieval_cases:cases.length+3,retrieval_passed:cases.length+3,memory_integrity:'passed',hash_encoding:'UTF-8 with LF newlines',core_sha256:sha('learner-core.js'),corpus_sha256:sha('dist/records.json'),model_inference_smoke:'not yet verified',model_answer_quality:'not evaluated'};
fs.writeFileSync('evaluation-results.json',JSON.stringify(report,null,2)+'\n');
console.log(`PASS: ${cases.length+3} retrieval cases; memory round-trip, false-verification rejection, unknown source rejection, duplicate rejection, capacity and prompt provenance.`);
