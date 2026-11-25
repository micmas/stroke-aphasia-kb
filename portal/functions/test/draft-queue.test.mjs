import test from 'node:test';
import assert from 'node:assert/strict';
import { selectDrafts, measurementLabel } from '../../web/draft-queue.js';

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
