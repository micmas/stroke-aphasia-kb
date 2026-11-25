import test from 'node:test';
import assert from 'node:assert/strict';
import { paperPriority, rankPapers } from '../../web/review-priority.js';
import { selectDrafts } from '../../web/draft-queue.js';
const finding = { target: 'sentence_comprehension', target_kind: 'impairment', source_kind: 'region', method: 'VLSM', evidence_quality: 'cohort', population: 'Patients after stroke', claim: 'No association detected.' };
const title = 'Lesion correlates of sentence comprehension after stroke';
test('direct stroke-language mapping and recovery prediction lead the queue', () => {
  assert.equal(paperPriority([finding], title).tier, 1);
  const prediction = { ...finding, source_kind: 'predictor', method: 'MVPA', target: 'naming_recovery', claim: 'Baseline severity predicted follow-up naming.' };
  assert.equal(paperPriority([prediction], 'Predicting aphasia recovery after stroke').tier, 1);
  assert.equal(paperPriority([finding], 'Cognitive impairment following stroke').tier, 2);
});
test('synthesis, trial metadata and imaging outcomes do not masquerade as primary mapping', () => {
  assert.equal(paperPriority([{ ...finding, evidence_quality: 'meta-analysis' }], title).tier, 4);
  assert.equal(paperPriority([finding, { ...finding, evidence_quality: 'meta-analysis' }], title).tier, 4);
  assert.equal(paperPriority([finding], 'Randomised controlled trial of aphasia therapy after stroke').tier, 4);
  assert.equal(paperPriority([{ ...finding, target: 'language_activation' }], title).tier, 5);
});
test('mixed samples and missing population evidence remain visible with an applicability caveat', () => {
  const mixed = paperPriority([{ ...finding, population: 'Stroke patients and temporal lobectomy patients with epilepsy' }], title);
  assert.equal(mixed.tier, 3); assert.match(mixed.reason, /Mixed/);
  assert.equal(paperPriority([{ ...finding, population: 'Stroke patients without epilepsy' }], title).tier, 1);
  assert.equal(paperPriority([{ ...finding, population: 'not_reported' }], 'Sentence comprehension').tier, 3);
});
test('confidence, result direction and duplicated records do not raise priority; inputs unchanged', () => {
  const before = JSON.stringify(finding);
  assert.deepEqual(paperPriority([finding], title), paperPriority(Array(20).fill({ ...finding, confidence: 'high', claim: 'Strong positive association.' }), title));
  assert.equal(JSON.stringify(finding), before);
});
test('paper groups preserve every draft, alphabetic override and exact paper drilldown', () => {
  const drafts = [
    { path: 'a', citation: '@A', findings: [{ ...finding, target: 'brain_activation' }] },
    { path: 'b', citation: '@B', findings: [finding] },
    { path: 'c', citation: '@B', findings: [finding] },
    { path: 'd', citation: '@B2', findings: [finding] },
  ];
  const citations = { '@A': 'Imaging', '@B': title, '@B2': title };
  const ranked = rankPapers(drafts, citations);
  assert.deepEqual(ranked.map(p => p.citation), ['@B', '@B2', '@A']);
  assert.equal(ranked.flatMap(p => p.drafts).length, 4);
  assert.equal(rankPapers(drafts, citations, 'az')[0].citation, '@A');
  assert.deepEqual(selectDrafts(drafts, { paper: '@B' }).items.map(d => d.path), ['b', 'c']);
  assert.equal(selectDrafts(drafts, { query: 'lesion correlates', citations }).total, 3);
  assert.equal(rankPapers([], citations).length, 0);
});
