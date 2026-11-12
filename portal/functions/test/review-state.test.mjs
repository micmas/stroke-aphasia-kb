// A review saved in the browser is carried over only to the same version of the draft; the files
// the page loaded must come from one build. Run: node --test portal/functions/test/
import test from 'node:test';
import assert from 'node:assert/strict';
import { carryOver, freshReview, sameBuild } from '../../web/review-state.js';

const A = `sha256:${'a'.repeat(64)}`; const B = `sha256:${'b'.repeat(64)}`;
const decided = (digest) => ({ ...freshReview(digest), verdict: 'approve', rationale: 'checked', findings: { f1: { verdict: 'agree', concern: '', edits: {}, passages: {}, added: [] } } });

test('same version: the saved decisions are kept', () => {
  const saved = decided(A);
  assert.deepEqual(carryOver(saved, A), { review: saved, setAside: false });
  assert.deepEqual(carryOver(null, A).review, freshReview(A));
});

test('changed draft: decisions reset, the old ones kept for reference only (REVIEW.md finding 10)', () => {
  const { review, setAside } = carryOver(decided(A), B, new Date('2026-11-11T00:00:00Z'));
  assert.equal(setAside, true);
  assert.equal(review.digest, B);
  assert.equal(review.verdict, ''); assert.deepEqual(review.findings, {});
  assert.equal(review.previous.verdict, 'approve'); assert.equal(review.previous.digest, A);
  // set aside twice: only the latest earlier state is kept, never nested
  const again = carryOver({ ...decided(B), previous: review.previous }, `sha256:${'c'.repeat(64)}`).review;
  assert.equal(again.previous.digest, B); assert.equal(again.previous.previous, undefined);
});

test('state saved before the binding existed counts as another version', () => {
  const legacy = { verdict: 'approve', rationale: '', findings: { f1: { verdict: 'agree' } }, marks: [], comments: {} };
  const { review, setAside } = carryOver(legacy, A);
  assert.equal(setAside, true); assert.equal(review.verdict, ''); assert.equal(review.digest, A);
  // an untouched legacy state just adopts the current version
  assert.deepEqual(carryOver({ verdict: '', rationale: '', findings: {}, marks: [], comments: {} }, A), { review: { ...freshReview(A) }, setAside: false });
});

test('the page refuses mixed builds', () => {
  const kb = { version: { contentDigest: 'd1' } };
  const manifest = { buildId: 'b1', exportDigest: 'd1', exportSha256: 's1' };
  const bindings = { buildId: 'b1', exportDigest: 'd1', exportSha256: 's1', drafts: {} };
  assert.equal(sameBuild(manifest, bindings, kb, 's1'), true);
  assert.equal(sameBuild(manifest, { ...bindings, buildId: 'b0' }, kb, 's1'), false);            // drafts.json from another build
  assert.equal(sameBuild(manifest, bindings, { version: { contentDigest: 'd0' } }, 's1'), false); // a cached export
  assert.equal(sameBuild(manifest, bindings, kb, 's0'), false);                                  // other bytes
  assert.equal(sameBuild(manifest, { ...bindings, exportDigest: null }, kb, 's1'), false);       // build found the export stale
  assert.equal(sameBuild(manifest, null, kb, 's1'), false);
  assert.equal(sameBuild({ ...manifest, buildId: '' }, { ...bindings, buildId: '' }, kb, 's1'), false);
});
