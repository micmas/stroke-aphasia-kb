import test from 'node:test';
import assert from 'node:assert/strict';
import {DATABASES,queryFor,parseRIS,csv,SCREEN_COLUMNS} from '../../explorer/dysphagia-search/data.js';
test('both Cochrane collections use NEXT for all truncated phrases',()=>{
 for(const id of ['central','cdsr']) {
  const query=queryFor(DATABASES.find(db=>db.id===id),'2026-11-23');
  const quoted=[...query.matchAll(/"([^"]*)"/g)].map(match=>match[1]);
  assert.ok(quoted.every(phrase=>!/[?*]/.test(phrase)));
  for(const phrase of ['cerebral NEXT infarct*','brain NEXT infarct*',
   'cerebral NEXT hemorrhag*','cerebral NEXT haemorrhag*',
   'intracerebral NEXT hemorrhag*','intracerebral NEXT haemorrhag*']) {
   assert.ok(query.includes(`(${phrase})`));
  }
  assert.ok(query.includes('"post-stroke"'));
 }
 assert.ok(DATABASES.find(db=>db.id==='scopus').query.includes('"cerebral infarct*"'));
});
test('all eight databases remain independently identifiable',()=>{assert.equal(DATABASES.length,8);assert.equal(new Set(DATABASES.map(x=>x.id)).size,8);assert.ok(DATABASES.find(x=>x.id==='central'));assert.ok(DATABASES.find(x=>x.id==='cdsr'));});
test('date-bound queries use the selected date without changing stored templates',()=>{const p=DATABASES[0];assert.match(queryFor(p,'2026-11-17'),/2026\/11\/17/);assert.doesNotMatch(p.query,/2026/);assert.match(queryFor(DATABASES[1],'2026-11-17'),/PUBYEAR < 2027/);assert.throws(()=>queryFor(p,''));});
test('RIS conversion preserves multiline abstracts, source identity and blank decisions',()=>{const rows=parseRIS('TY  - JOUR\r\nTI  - A title\r\nAB  - First line\r\n continuation\r\nAU  - Smith\r\nAU  - Jones\r\nDO  - 10.1/test\r\nER  - \r\n','dedup.ris');assert.equal(rows.length,1);assert.equal(rows[0].length,SCREEN_COLUMNS.length);assert.equal(rows[0][3],'First line continuation');assert.equal(rows[0][4],'Smith; Jones');assert.equal(rows[0][7],'dedup.ris');assert.equal(rows[0][11],'');});
test('incomplete or non-RIS exports fail instead of silently dropping records',()=>{assert.throws(()=>parseRIS('TY  - JOUR\nTI  - Lost','x.ris'));assert.throws(()=>parseRIS('PMID- 123','x.nbib'));assert.throws(()=>parseRIS('TY  - JOUR\nTY  - JOUR\nER  -','x.ris'));});
test('CSV downloads preserve quotes and newlines without spreadsheet formulas',()=>{const out=csv([['=HYPERLINK("x")','a\nb','quote"']]);assert.ok(out.includes("'="));assert.ok(out.includes('"a\nb"'));assert.ok(out.includes('"quote"""'));});
