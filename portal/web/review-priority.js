// Reviewer-selected topics and transparent relevance ordering, never approval or certainty.
const words = value => String(value || '').replace(/[_–—-]/g, ' ').toLowerCase();
const LANGUAGE = /aphasi|language|speech|comprehension|naming|repetition|semantic|phonolog|reading|writing|fluency|agrammati|dysarthri|apraxia of speech|communication|prosody|paraphasi|alexia|anomia/;
const COGNITION = /cogniti|attention|memory|executive|neglect|praxis|apraxia|visuospatial|dementia|reasoning|orientation|calculation/;
const IMAGING = /activation|connectivity|lateralization|lesion location|lesion distribution|fa values|white matter|neural|brain|tissue|imaging|cluster/;
const MAPPING = new Set(['LSM', 'VLSM', 'RLSM', 'VBCM', 'VBM', 'DTI', 'tractography', 'disconnectome']);
const SYNTHESIS = /meta.analysis|narrative.review|synthesis/;
const TITLE = {
  mapping: /lesion|mapping|neural correlates|neuroanatom|white matter|tract|disconnection|structural/,
  recovery: /recover|predict|prognos|longitudinal|outcome/,
  treatment: /therap|treatment|rehabilit|stimulation|intervention|training|trial/,
  language: LANGUAGE,
  cognition: COGNITION,
  methods: /network|connect|imaging|functional|method|atlas|meta.analysis|review|synthesis/,
};
export const REVIEW_TOPICS = [
  { id: 'mapping', label: 'Lesion–behaviour mapping', description: 'How damage to brain regions and pathways relates to behaviour.' },
  { id: 'recovery', label: 'Recovery and prediction', description: 'Recovery over time and predictors of later outcomes.' },
  { id: 'treatment', label: 'Treatment and rehabilitation', description: 'Therapies, stimulation, dose and treatment response.' },
  { id: 'language', label: 'Language and communication', description: 'Speaking, comprehension, naming, reading and writing.' },
  { id: 'cognition', label: 'Other cognitive functions', description: 'Attention, memory, executive function, praxis and neglect.' },
  { id: 'methods', label: 'Brain networks and methods', description: 'Imaging endpoints, networks, methods and evidence synthesis.' },
];

function signals(findings, paperTitle) {
  const title = words(paperTitle);
  const topics = new Set();
  const synthesis = SYNTHESIS.test(title) || findings.some(f => SYNTHESIS.test(words(f.evidence_quality)));
  const treatmentTrial = /randomi[sz]ed.*trial/.test(title);
  let stroke = false, otherCohort = false;
  for (const f of findings) {
    const target = words(f.target);
    const included = words(f.sample?.population || f.population).split(/excluding|excluded|without|no history|no evidence/)[0];
    stroke ||= /stroke|infarct|cerebrovascular/.test(included);
    otherCohort ||= /lobectom|epilep|tumou?r|traumatic brain|primary progressive|healthy participants only|healthy adults only/.test(included);
    const behaviour = !['region', 'predictor'].includes(f.target_kind) &&
      f.target_audit?.category !== 'non_behaviour_or_methodological' && !IMAGING.test(target);
    const neuralOrPredictor = ['region', 'predictor'].includes(f.source_kind);
    if (!synthesis && !treatmentTrial && behaviour && neuralOrPredictor && MAPPING.has(f.method)) topics.add('mapping');
    const context = words([f.target, f.claim].join(' '));
    if ((behaviour && neuralOrPredictor && /recover|prognos|follow up|longitudinal|outcome/.test(context) && /predict|prognos/.test(context)) ||
        f.target_kind === 'prognosis' || (behaviour && /recover|longitudinal/.test(title) && !TITLE.treatment.test(title))) topics.add('recovery');
    if (f.source_kind === 'therapy' || ['responder', 'treatment_response'].includes(f.relationship) || TITLE.treatment.test(title)) topics.add('treatment');
    if (behaviour && LANGUAGE.test(target)) topics.add('language');
    if (behaviour && !LANGUAGE.test(target) && COGNITION.test(target)) topics.add('cognition');
    if (IMAGING.test(target) || SYNTHESIS.test(words(f.evidence_quality)) || f.target_audit?.category === 'non_behaviour_or_methodological') topics.add('methods');
  }
  stroke ||= /post ?stroke|after stroke|stroke patients|stroke survivors/.test(title);
  return { title, topics: [...topics], stroke, otherCohort };
}

export function paperTopics(findings, paperTitle = '') {
  return signals(findings, paperTitle).topics;
}

export function paperPriority(findings, paperTitle = '', topic = 'all') {
  const s = signals(findings, paperTitle);
  if (topic === 'all') return { tier: 0, label: 'All topics', reason: 'Choose a topic for relevance ordering' };
  if (!s.topics.includes(topic)) return { tier: 5, label: 'Outside this topic', reason: 'No matching recorded finding' };
  if (s.otherCohort) return { tier: 3, label: 'Check applicability', reason: 'Topic match · Mixed or non-stroke population recorded' };
  if (!s.stroke) return { tier: 4, label: 'Check population', reason: 'Topic match · Stroke population needs confirmation' };
  if (TITLE[topic]?.test(s.title)) return { tier: 1, label: 'Closest match', reason: 'Topic is central to the paper title · Stroke population recorded' };
  return { tier: 2, label: 'Relevant findings', reason: 'Matching findings in a broader paper · Stroke population recorded' };
}

export function rankPapers(drafts, titles = {}, order = 'priority', topic = 'all') {
  const groups = new Map();
  for (const d of drafts) {
    if (!groups.has(d.citation)) groups.set(d.citation, { citation: d.citation, drafts: [] });
    groups.get(d.citation).drafts.push(d);
  }
  return [...groups.values()].map(p => {
    const findings = p.drafts.flatMap(d => d.findings);
    return { ...p, topics: paperTopics(findings, titles[p.citation]), priority: paperPriority(findings, titles[p.citation], topic) };
  }).filter(p => topic === 'all' || p.topics.includes(topic))
    .sort((a, b) => (order === 'az' ? 0 : a.priority.tier - b.priority.tier) || String(a.citation).localeCompare(String(b.citation)));
}
