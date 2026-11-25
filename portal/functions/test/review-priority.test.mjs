import test from 'node:test';
import assert from 'node:assert/strict';
import { paperPriority, paperTopics, rankPapers } from '../../web/review-priority.js';
import { selectDrafts } from '../../web/draft-queue.js';
const finding = { target: 'sentence_comprehension', target_kind: 'impairment', source_kind: 'region', method: 'VLSM', evidence_quality: 'cohort', population: 'Patients after stroke', claim: 'No association detected.' };
const title = 'Lesion correlates of sentence comprehension after stroke';
test('topics overlap and relevance follows the reviewer choice', () => {
  assert.deepEqual(paperTopics([finding], title), ['mapping', 'language']);
  assert.equal(paperPriority([finding], title, 'mapping').tier, 1);
  assert.equal(paperPriority([finding], 'Cognitive impairment following stroke', 'mapping').tier, 2);
  const therapy = { ...finding, source_kind: 'therapy', method: 'behavioral_only', relationship: 'treatment_response' };
  assert.equal(paperPriority([therapy], 'Aphasia therapy after stroke', 'treatment').tier, 1);
  assert.equal(paperPriority([therapy], 'Aphasia therapy after stroke', 'mapping').tier, 5);
  const recovery = { ...finding, source_kind: 'predictor', method: 'MVPA', target: 'naming_recovery', claim: 'Baseline severity predicted follow-up naming.' };
  assert.ok(paperTopics([recovery], 'Predicting aphasia recovery').includes('recovery'));
});
test('imaging, synthesis and clinical trials are not mislabeled as primary mapping', () => {
  assert.ok(!paperTopics([{ ...finding, target: 'language_activation' }], title).includes('mapping'));
  assert.ok(paperTopics([{ ...finding, target: 'language_activation' }], title).includes('methods'));
  assert.ok(!paperTopics([{ ...finding, evidence_quality: 'meta-analysis' }], title).includes('mapping'));
  assert.ok(!paperTopics([finding], 'Randomised controlled trial of aphasia therapy after stroke').includes('mapping'));
  assert.ok(paperTopics([{ ...finding, target: 'working_memory' }], 'Cognitive outcomes').includes('cognition'));
});
test('mixed samples and unknown populations remain accessible with a caveat', () => {
  assert.equal(paperPriority([{ ...finding, population: 'Stroke and temporal lobectomy patients with epilepsy' }], title, 'mapping').tier, 3);
  assert.equal(paperPriority([{ ...finding, population: 'Stroke patients without epilepsy' }], title, 'mapping').tier, 1);
  assert.equal(paperPriority([{ ...finding, population: 'not_reported' }], 'Sentence comprehension', 'mapping').tier, 4);
});
test('confidence, sample size, direction and duplicates do not invent impact or change inputs', () => {
  const before = JSON.stringify(finding);
  assert.deepEqual(paperPriority([finding], title, 'mapping'), paperPriority(Array(20).fill({ ...finding, confidence: 'high', sample: { n: 9000, population: finding.population }, claim: 'Strong positive association.' }), title, 'mapping'));
  assert.equal(JSON.stringify(finding), before);
});
test('topic filtering keeps whole papers, all-papers escape, alphabetical order and exact drilldown', () => {
  const drafts = [
    { path: 'a', citation: '@A', findings: [finding] },
    { path: 'b', citation: '@B', findings: [finding] },
    { path: 'c', citation: '@B', findings: [{ ...finding, target: 'brain_activation' }] },
    { path: 'd', citation: '@C', findings: [{ target: 'unspecified', target_kind: 'prognosis' }] },
  ];
  const citations = { '@A': 'Cognition following stroke', '@B': title, '@C': 'Outcome study' };
  const ranked = rankPapers(drafts, citations, 'priority', 'mapping');
  assert.deepEqual(ranked.map(p => p.citation), ['@B', '@A']);
  assert.deepEqual(ranked[0].drafts.map(d => d.path), ['b', 'c']);
  assert.equal(rankPapers(drafts, citations).flatMap(p => p.drafts).length, 4);
  assert.equal(rankPapers(drafts, citations, 'az', 'mapping')[0].citation, '@A');
  assert.deepEqual(selectDrafts(ranked.flatMap(p => p.drafts), { paper: '@B' }).items.map(d => d.path), ['b', 'c']);
  assert.equal(rankPapers(drafts, citations, 'priority', 'treatment').length, 0);
  assert.equal(rankPapers([], citations).length, 0);
});

test('missing structured titles never claim that the topic is central to the title', () => {
  assert.equal(paperPriority([finding], '', 'mapping').tier, 2);
  assert.ok(!paperPriority([finding], '', 'mapping').reason.includes('title'));
});
