// Suggested reading order, not evidence quality, approval readiness or clinical advice.
// Use binary relevance signals: duplicates, confidence and positive/null results cannot add priority.
const words = value => String(value || '').replace(/[_–—-]/g, ' ').toLowerCase();
const LANGUAGE = /aphasi|language|speech|comprehension|naming|repetition|semantic|phonolog|reading|writing|fluency|agrammati|dysarthri|apraxia of speech|communication|prosody|paraphasi|alexia|anomia/;
const IMAGING = /activation|connectivity|lateralization|lesion location|lesion distribution|fa values|white matter|neural|brain|tissue|imaging|cluster/;
const MAPPING = new Set(['LSM', 'VLSM', 'RLSM', 'VBCM', 'VBM', 'DTI', 'tractography', 'disconnectome']);
const SYNTHESIS = /meta.analysis|narrative.review|synthesis/;

export function paperPriority(findings, citationText = '') {
  const title = words(citationText);
  const synthesis = SYNTHESIS.test(title) || findings.some(f => SYNTHESIS.test(words(f.evidence_quality)));
  const treatmentTrial = /randomi[sz]ed.*trial/.test(title);
  let mapping = false, prediction = false, stroke = false, language = false, otherCohort = false;
  for (const f of findings) {
    const target = words(f.target);
    const population = words(f.sample?.population || f.population);
    // Exclusion lists must not turn a stroke-only sample into a mixed clinical cohort.
    const included = population.split(/excluding|excluded|without|no history|no evidence/)[0];
    stroke ||= /stroke|infarct|cerebrovascular/.test(included);
    otherCohort ||= /lobectom|epilep|tumou?r|traumatic brain|primary progressive|healthy participants only|healthy adults only/.test(included);
    const behaviour = !['region', 'predictor'].includes(f.target_kind) &&
      f.target_audit?.category !== 'non_behaviour_or_methodological' && !IMAGING.test(target);
    const relevant = behaviour && LANGUAGE.test(target);
    language ||= relevant;
    const primary = !synthesis && !treatmentTrial && !SYNTHESIS.test(words([f.evidence_quality, f.method, f.relationship].join(' ')));
    const neuralOrPredictor = ['region', 'predictor'].includes(f.source_kind);
    mapping ||= primary && relevant && neuralOrPredictor && MAPPING.has(f.method);
    const context = words([f.target, f.claim, citationText].join(' '));
    prediction ||= primary && relevant && neuralOrPredictor &&
      /recover|prognos|follow up|longitudinal|outcome/.test(context) && /predict|prognos/.test(context);
  }
  stroke ||= /post ?stroke|after stroke|stroke patients|stroke survivors/.test(title);
  const focus = [mapping && 'Lesion–behaviour mapping', prediction && 'Recovery / outcome prediction'].filter(Boolean).join(' · ');
  if (focus && stroke && !otherCohort && LANGUAGE.test(title)) return { tier: 1, label: 'Start here', reason: `${focus} · Stroke population recorded` };
  if (focus && stroke && !otherCohort) return { tier: 2, label: 'Broader mapping / prediction', reason: `${focus} · Broader stroke or cognitive study` };
  if (focus) return { tier: 3, label: 'Check applicability', reason: `${focus} · ${otherCohort ? 'Mixed or non-stroke population recorded' : 'Stroke population needs confirmation'}` };
  if (language) return { tier: 4, label: 'Related language evidence', reason: 'Language, communication or treatment outcomes; outside the first mapping / prediction group' };
  return { tier: 5, label: 'Broader supporting evidence', reason: 'Other cognitive, imaging or methodological outcomes' };
}

export function rankPapers(drafts, citations = {}, order = 'priority') {
  const groups = new Map();
  for (const d of drafts) {
    if (!groups.has(d.citation)) groups.set(d.citation, { citation: d.citation, drafts: [] });
    groups.get(d.citation).drafts.push(d);
  }
  return [...groups.values()].map(p => ({ ...p, priority: paperPriority(p.drafts.flatMap(d => d.findings), citations[p.citation]) }))
    .sort((a, b) => (order === 'az' ? 0 : a.priority.tier - b.priority.tier) || String(a.citation).localeCompare(String(b.citation)));
}
