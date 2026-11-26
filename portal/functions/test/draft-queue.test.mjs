import test from 'node:test';
import assert from 'node:assert/strict';
import { selectDrafts, measurementLabel, reviewProgress, pendingFirst, nextPaperDraft } from '../../web/draft-queue.js';

const drafts = Array.from({ length: 31 }, (_, i) => ({ citation: `@Paper${i}`, entry: 'connectivity', findings: [{
  target: 'auditory_sentence_comprehension', claim: 'No association detected.', confidence: i === 0 ? 'high' : 'medium',
  outcome_measurement: i === 0 ? { status: 'identified', instruments: [{ name: 'Token Test' }] } : { status: 'needs_source_review', instruments: [] },
  target_audit: { status: i === 1 ? 'needs_source_review' : 'behaviour_label_present' },
}] }));
test('queue limits long lists and clamps page after filtering', () => {
  assert.equal(selectDrafts(drafts).items.length, 25);
  assert.equal(selectDrafts(drafts, { page: 1 }).items.length, 6);
  const one = selectDrafts(drafts, { page: 10, query: 'Token sentence' });
  assert.equal(one.total, 1); assert.equal(one.page, 0);
  assert.equal(selectDrafts(drafts, { query: 'nonexistent' }).items.length, 0);
});
test('definition, measurement and confidence filters remain distinct', () => {
  assert.equal(selectDrafts(drafts, { filter: 'target' }).total, 1);
  assert.equal(selectDrafts(drafts, { filter: 'measurement' }).total, 30);
  assert.equal(selectDrafts(drafts, { filter: 'high' }).total, 1);
  assert.equal(drafts[0].findings[0].source_status, undefined); // no promotion or mutation
});
test('missing measures never masquerade as verified assessments', () => {
  assert.match(measurementLabel({}), /Not yet verified/);
  assert.equal(measurementLabel(drafts[0].findings[0]), 'Token Test');
});

test('current-version decisions count per finding; stale, partial and other-draft receipts stay pending', () => {
  const d = { path: 'drafts/x-long-shared-prefix-a.md', findings: [{id:'f1'}, {id:'f2'}] };
  const b = { digest: 'v1' };
  const receipt = { id: d.path, draft_digest: 'v1', by: 'Reviewer', per_finding: [{id:'f1',verdict:'agree'}] };
  assert.equal(reviewProgress(d,b,[receipt]).complete,false);
  assert.equal(reviewProgress(d,b,[receipt]).decided,1);
  assert.equal(reviewProgress(d,b,[{...receipt,id:'drafts/x-long-shared-prefix-b.md'}]).decided,0);
  assert.equal(reviewProgress(d,b,[{...receipt,draft_digest:'old'}]).decided,0);
  assert.equal(reviewProgress(d,b,[{...receipt,per_finding:[{id:'f1',verdict:null}]}]).decided,0);
  assert.equal(reviewProgress(d,{...b,reviews:[{reviewed_digest:'v1',findings:[{id:'f2',verdict:'unsure'}],by:'Other'}]},[receipt]).complete,true);
  assert.equal(reviewProgress(d,{...b,reviews:[{reviewed_digest:'v1',stale:'changed',findings:[{id:'f2',verdict:'agree'}]}]},[receipt]).complete,false);
});

test('pending drafts precede submitted drafts before pagination and advancement stays in the paper', () => {
  const list = ['a','b','c','d'].map(path=>({path,citation:path==='d'?'@Other':'@Paper',findings:[{id:'f1'}]}));
  const done = d=>d.path==='b';
  assert.deepEqual(pendingFirst(list.slice(0,3),done).map(d=>d.path),['a','c','b']);
  assert.equal(nextPaperDraft(list,list[0],done).path,'c');
  assert.equal(nextPaperDraft(list,list[2],done).path,'a');
  assert.equal(nextPaperDraft(list,list[2],d=>['a','b'].includes(d.path)),null);
  assert.deepEqual(list.map(d=>d.path),['a','b','c','d']);
});
