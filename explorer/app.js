import { overviewTopics } from './overview-topics.js';
import { atlasCoverage, mappingStatus } from './atlas-coverage.js';
import { ANATOMY, FACTORS } from './topic-categories.js';
import { groupedMatrix } from './evidence-groups.js';
import { loadExportText } from './load-export.js';
// Stroke aphasia KB explorer — views and routing.
//
// A static page: it loads export/stroke-aphasia-kb.json (approved findings), or
// with ?kb=drafts export/stroke-aphasia-kb-drafts.json (approved + drafts; the
// "Findings" switch in the header), or the file named by ?kb=<url>, or one
// chosen with the "Open a local export" control, indexes
// it with kb-index.js and renders one view per hash route:
//   #/                       overview
//   #/findings?facet=value   faceted finding browser (query string = filters)
//   #/matrix?kind=…          evidence matrices
//   #/papers · #/paper/<Key> bibliography and one paper's findings in page order
//   #/licences?c=category    every bibliography entry with its licence (screen.py licences)
//   #/coverage?facet=value  the screening register: PRISMA flow, gap coverage, candidates
//   #/entry/<id>             one region / impairment / therapy / predictor
//   #/finding/<source>/<id>  one finding, permalinked
// Every string from the KB is inserted as text, never as HTML.
import {
  buildIndex, FACETS, facetCounts, matches, matrixOf, provenanceCounts, yearOf, paperLabel,
  RELATIONSHIP_TEXT, DIRECTION_LABEL, REVIEW_LABEL,
  SCREENING_FACETS, STAGE_TEXT, KB_STATE_TEXT, ARM_TEXT,
} from './kb-index.js';

const KB_VERSIONS = { approved: '../export/stroke-aphasia-kb.json', drafts: '../export/stroke-aphasia-kb-drafts.json' };
const DEFAULT_KB = KB_VERSIONS.drafts;
const PAGE = 60;
const state = { index: null, source: null, sourceLabel: '', shown: PAGE };

// ---------------------------------------------------------------------------
// DOM helpers
// ---------------------------------------------------------------------------
function h(tag, attrs = {}, ...children) {
  const el = document.createElement(tag);
  for (const [k, v] of Object.entries(attrs)) {
    if (v === null || v === undefined || v === false) continue;
    if (k === 'class') el.className = v;
    else if (k === 'text') el.textContent = v;
    else if (k.startsWith('on') && typeof v === 'function') el.addEventListener(k.slice(2), v);
    else if (k === 'dataset') Object.assign(el.dataset, v);
    else el.setAttribute(k, v === true ? '' : v);
  }
  for (const c of children.flat(Infinity)) {
    if (c === null || c === undefined || c === false) continue;
    el.append(c instanceof Node ? c : document.createTextNode(String(c)));
  }
  return el;
}
const frag = (...children) => { const f = document.createDocumentFragment(); for (const c of children.flat(Infinity)) if (c !== null && c !== undefined && c !== false) f.append(c instanceof Node ? c : document.createTextNode(String(c))); return f; };
const plural = (n, word, words = `${word}s`) => `${n} ${n === 1 ? word : words}`;
const pct = (n, d) => (d ? `${Math.round((100 * n) / d)}%` : '—');
const esc = encodeURIComponent;

function href(path, params = {}) {
  const q = new URLSearchParams();
  for (const [k, v] of Object.entries(params)) {
    for (const item of Array.isArray(v) ? v : [v]) if (item !== undefined && item !== null && item !== '') q.append(k, item);
  }
  const qs = q.toString();
  return `#${path}${qs ? `?${qs}` : ''}`;
}
const entryHref = (id) => `#/entry/${esc(id)}`;
const paperHref = (key) => `#/paper/${esc(String(key).replace(/^@/, ''))}`;
const findingHref = (f) => `#/finding/${esc(f.source_path || f.source_id)}/${esc(f.id)}`;

function parseRoute() {
  const raw = location.hash.replace(/^#/, '') || '/';
  const [path, qs = ''] = raw.split('?');
  const params = new URLSearchParams(qs);
  const filters = {};
  for (const [k, v] of params) { if (k === 'q' || k === 'sort' || k === 'kind' || k === 'min' || k === 'entries' || k === 'find' || k === 'box') continue; (filters[k] ||= []).push(v); }
  return { path: decodeURI(path), params, filters, segments: path.split('/').filter(Boolean).map(decodeURIComponent) };
}

// ---------------------------------------------------------------------------
// Get involved — the five levels at which a person can take part (#/involve)
// ---------------------------------------------------------------------------
const sv = (tag, attrs = {}, ...children) => s(tag, attrs, ...children);   // the SVG helper defined with the Coverage view
/** The levels, from reading to building. `needs` is the only thing that changes between them. */
const LEVELS = [
  { n: 1, name: 'Use', verb: 'Read the evidence', who: 'Anyone: clinicians, students, researchers', time: 'minutes', needs: 'nothing — this site is public', colour: 'var(--cyan)',
    does: ['Browse findings by region, impairment or therapy; follow each claim to the exact passage and page of its paper.', 'Use the evidence matrix and the coverage view to see what is known, how well, and where the gaps are.'],
    gives: 'Questions, teaching material, a check on your own clinical reasoning.', link: '#/matrix', linkText: 'Evidence matrix' },
  { n: 2, name: 'Screen', verb: 'Sort the literature', who: 'Clinicians and students, 10 minutes at a time', time: '10 min per 20 abstracts', needs: 'an email address the maintainer has approved; no account to create', colour: 'var(--blue)',
    does: ['In the review portal, read a title and abstract and say include / exclude (with a reason) / unsure against the eligibility criteria.', 'At the full-text stage, read the paper itself; upload its PDF if the project does not have it.'],
    gives: 'The PRISMA flow: which of the 20 000+ candidate papers deserve extraction.', link: 'portal', linkText: 'Review portal' },
  { n: 3, name: 'Review', verb: 'Check the extraction', who: 'Researchers, students, clinicians with 30 minutes', time: '20–40 min per paper', needs: 'an email address the maintainer has approved; no account to create', colour: 'var(--grape)',
    does: ['Open a draft beside the annotated PDF: for each finding say agree / disagree / unsure, fix a wrong field, flag a passage that does not support the claim.', 'Select words in the paper to add a passage, or mark something the extractor missed so it is re-read.'],
    gives: 'Verified findings: every claim read by a person against the paper before it enters the KB.', link: 'portal', linkText: 'Review portal → Drafts' },
  { n: 4, name: 'Approve', verb: 'Take responsibility', who: 'Named approvers (senior researchers, clinician-scientists)', time: 'a review + the verdict', needs: 'to be listed in the Reviewer team', colour: 'var(--pink)',
    does: ['Give the overall verdict that moves a draft into the knowledge base — or rejects it — under your name.', 'Take part in the 20 % quote audit and the re-review of pre-policy entries.'],
    gives: 'Accountability: nothing enters the KB without a named person.', link: 'reviewers', linkText: 'The Reviewer team (portal/reviewers.yaml)' },
  { n: 5, name: 'Build', verb: 'Extend the system', who: 'Developers, students with a laptop and a local model', time: 'hours to weeks', needs: 'a copy of the repository', colour: 'var(--ink-2)',
    does: ['Run independent extraction and source review on screened papers with local models; add atlas mappings so lesions can reach new regions; improve the schema.', 'Work on this explorer, the review portal, the screening tools or the CALMaR / Neurodesk integration.'],
    gives: 'New papers, new regions, new tools — and the pipeline that keeps the KB honest.', link: 'contributing', linkText: 'CONTRIBUTING.md' },
];
const REPO_DOCS = { reviewers: 'https://github.com/micmas/stroke-aphasia-kb/blob/main/portal/reviewers.yaml', governance: 'https://github.com/micmas/stroke-aphasia-kb/blob/main/docs/GOVERNANCE.md', contributing: 'https://github.com/micmas/stroke-aphasia-kb/blob/main/CONTRIBUTING.md', screening: 'https://github.com/micmas/stroke-aphasia-kb/blob/main/docs/SCREENING.md', portalDoc: 'https://github.com/micmas/stroke-aphasia-kb/blob/main/docs/PORTAL.md', models: 'https://github.com/micmas/stroke-aphasia-kb/blob/main/docs/MODELS.md' };
function levelHref(index, lv) { if (lv.link === 'portal') return index.kb.portal?.url || REPO_DOCS.portalDoc; return REPO_DOCS[lv.link] || lv.link; }

/** The figure: five rising steps; each names the level, who it is for and what it needs. */
function involvementFigure(index) {
  const W = 960; const H = 500; const n = LEVELS.length; const colW = (W - 40) / n; const stepH = 46; const base = H - 130;
  const svg = sv('svg', { viewBox: `0 0 ${W} ${H}`, role: 'img', 'aria-labelledby': 'invTitle invDesc', class: 'involve-figure' },
    sv('title', { id: 'invTitle', text: 'Five levels of involvement in the stroke aphasia knowledge base' }),
    sv('desc', { id: 'invDesc', text: LEVELS.map((l) => `${l.n}. ${l.name}: ${l.verb}; for ${l.who}; needs ${l.needs}.`).join(' ') }));
  // the rising floor
  const floor = LEVELS.map((_, i) => `${20 + i * colW},${base - i * stepH} ${20 + (i + 1) * colW},${base - i * stepH}`).join(' ');
  svg.append(sv('polyline', { points: `20,${H - 60} 20,${base} ${floor} ${W - 20},${H - 60}`, fill: 'var(--panel)', stroke: 'var(--line-strong)', 'stroke-width': 1.5, 'stroke-linejoin': 'round' }));
  // the accountability line: from level 4 on, a named person answers for the decision
  const ax = 20 + 3 * colW;
  svg.append(sv('line', { x1: ax, y1: 24, x2: ax, y2: base - 3 * stepH, stroke: 'var(--pink)', 'stroke-width': 1.5, 'stroke-dasharray': '5 4' }),
    sv('text', { x: ax - 8, y: 36, 'text-anchor': 'end', class: 'inv-note', fill: 'var(--pink)', text: 'from here, a named person answers for each decision →' }));
  LEVELS.forEach((lv, i) => {
    const x = 20 + i * colW; const y = base - i * stepH;
    const whoLines = wrapWords(lv.who, 24);
    const cardH = 96 + whoLines.length * 14 + 14;
    const top = y - cardH - 10;
    const g = sv('g', { class: 'inv-level' });
    g.append(sv('rect', { x: x + 10, y: top, width: colW - 20, height: cardH, rx: 8, fill: 'var(--surface)', stroke: lv.colour, 'stroke-width': 2 }));
    g.append(sv('circle', { cx: x + 32, cy: top + 24, r: 14, fill: lv.colour }), sv('text', { x: x + 32, y: top + 29, 'text-anchor': 'middle', class: 'inv-num', fill: '#fff', text: String(lv.n) }));
    g.append(sv('text', { x: x + 54, y: top + 30, class: 'inv-name', fill: 'var(--ink)', text: lv.name }));
    g.append(sv('text', { x: x + 22, y: top + 56, class: 'inv-verb', fill: 'var(--ink)', text: lv.verb }));
    const who = sv('text', { x: x + 22, y: top + 76, class: 'inv-small', fill: 'var(--ink-2)' });
    whoLines.forEach((t, k) => who.append(sv('tspan', { x: x + 22, dy: k ? 14 : 0, text: t }))); g.append(who);
    g.append(sv('text', { x: x + 22, y: top + 76 + whoLines.length * 14 + 6, class: 'inv-small', fill: 'var(--ink-2)', text: `~ ${lv.time}` }));
    // under the floor: what this level needs
    const needs = sv('text', { x: x + colW / 2, y: H - 42, 'text-anchor': 'middle', class: 'inv-needs', fill: 'var(--ink)' });
    needs.append(sv('tspan', { x: x + colW / 2, dy: 0, class: 'inv-needs-head', fill: lv.colour, text: 'needs' }));
    wrapWords(lv.needs, 24).forEach((t) => needs.append(sv('tspan', { x: x + colW / 2, dy: 13, text: t })));
    g.append(needs);
    g.append(sv('line', { x1: x + colW / 2, y1: y, x2: x + colW / 2, y2: H - 60, stroke: 'var(--line-strong)', 'stroke-width': 1, 'stroke-dasharray': '2 3' }));
    svg.append(g);
  });
  svg.append(sv('text', { x: 24, y: H - 68, class: 'inv-note', fill: 'var(--ink-2)', text: 'more time and responsibility →' }));
  return svg;
}
function wrapWords(text, width) { const out = []; let cur = ''; for (const w of String(text).split(' ')) { if ((cur + ' ' + w).trim().length > width && cur) { out.push(cur); cur = w; } else cur = (cur + ' ' + w).trim(); } if (cur) out.push(cur); return out; }
function wrapText(textEl, text, width, x, lineH) { wrapWords(text, width).forEach((t, i) => textEl.append(sv('tspan', { x, dy: i ? lineH : 0, text: t }))); }

function involve(index) {
  return h('div', { class: 'editorial-page' },
    h('p', { class: 'eyebrow', text: 'Open research · shared work' }),
    h('h1', { text: 'Help make the evidence useful.' }),
    h('p', { class: 'lead', text: 'We welcome clinicians, researchers and students interested in aphasia, brain imaging and recovery. You can contribute a paper, check a finding or help develop the tools.' }),
    h('div', { class: 'ways-to-help' },
      h('section', {}, h('h2', { text: 'Screen papers' }), h('p', { text: 'Read titles and abstracts, then full texts, to decide which studies belong in the knowledge base. Record a reason so others can follow the decision.' })),
      h('section', {}, h('h2', { text: 'Check findings' }), h('p', { text: 'Compare a proposed finding with its source paper. Correct errors, flag missing context and check who the result applies to.' })),
      h('section', {}, h('h2', { text: 'Build and test' }), h('p', {}, 'Help improve extraction, atlas mapping or reports. Start with the ', h('a', { href: REPO_DOCS.contributing, text: 'contribution guide' }), '.'))),
    h('h2', { text: 'Join the review team' }),
    h('p', { text: 'Tell us a little about your background. Once invited, you can sign in by email and choose a task in the portal. Your decisions are recorded under your name.' }),
    h('a', { class: 'editorial-button', href: 'https://review.aphasia-kb.app/welcome/', text: 'Ask to join' }),
    h('h2', { text: 'Who is responsible?' }),
    h('p', {}, 'Michele Masson-Trottier leads the project. People set its research questions, screening criteria and approval policy. AI assists with coding and extracting evidence; it can miss or misread a result. Each finding keeps its source and review history.'),
    h('p', {}, 'Final approval is a separate role, agreed with the maintainer. See the ', h('a', { href: REPO_DOCS.reviewers, text: 'reviewer team' }), ' and ', h('a', { href: REPO_DOCS.governance, text: 'review and approval policy' }), '.'),
    h('p', { class: 'small muted', text: 'The knowledge base and code are public. Access to paper PDFs depends on their licences and reviewer permissions.' }));
}

// ---------------------------------------------------------------------------
// Shared renderers
// ---------------------------------------------------------------------------
// ---------------------------------------------------------------------------
// Models — which local model reads the papers, and how it was chosen (#/models)
// The numbers come from export/model-benchmark.json, written by
// `scripts/benchmark_models.py --publish`: counts and ids only, no paper text.
// ---------------------------------------------------------------------------
const BENCH_URL = '../export/model-benchmark.json';
const ROLE_TEXT = {
  extract: ['Extractor', 'reads a whole paper and drafts its findings, each with verbatim passages'],
  review: ['Reviewer', 'a different model that re-reads the paper and checks routine findings; anything else waits for a person'],
  rag: ['Report writer', 'turns cited findings into the prose of a CALMaR report'],
  screen: ['Screening helper', 'suggests include / exclude on titles and abstracts; a person decides'],
};
const secs = (x) => { if (!x) return '—'; const m = Math.round(x / 60); return m >= 60 ? `${Math.floor(m / 60)} h ${String(m % 60).padStart(2, '0')} min` : `${m} min`; };
const share = (x) => (x === null || x === undefined ? '—' : `${Math.round(100 * x)}%`);
function meter(n, d, { alt = false } = {}) {
  return h('span', { class: 'meter', title: `${n} of ${d}` },
    h('span', { class: 'meter-track' }, h('span', { class: `meter-fill${alt ? ' alt' : ''}`, style: `width:${d ? Math.max(n ? 3 : 0, (100 * n) / d) : 0}%` })),
    h('span', { class: 'meter-n', text: `${n} / ${d}` }));
}
function linkLabel(index, text) {
  // "left_angular_gyrus ↔ semantics": show entry names, linked when the KB has the entry
  const parts = String(text).split(' ↔ ');
  return frag(parts.map((id, i) => [i ? ' ↔ ' : '', index.kb.entries?.[id] ? h('a', { href: entryHref(id), text: index.name(id) }) : String(id).replace(/_/g, ' ')]));
}
function loadBench() {
  if (state.bench !== undefined) return;
  state.bench = 'loading';
  fetch(BENCH_URL, { cache: 'no-cache' }).then((r) => (r.ok ? r.json() : null)).catch(() => null)
    .then((d) => { state.bench = d && d.schema === 1 ? d : null; if (parseRoute().segments[0] === 'models') render(); });
}
function models(index) {
  loadBench();
  const b = state.bench;
  const head = h('div', { class: 'page-head' }, h('h1', { text: 'Models' }), h('span', { class: 'muted small', text: 'How AI assists the research' }));
  const intro = h('p', { class: 'lead' }, 'AI helps us find and organise evidence in papers. We test what it gets right and what it misses. Agreement between models is not proof that a finding is correct.');
  if (b === 'loading' || b === undefined) return frag(head, intro, h('p', { class: 'loading', text: 'Loading the latest comparison…' }));
  if (!b) return frag(head, intro, h('p', { class: 'notice' }, 'No comparison has been published yet. The method and the decision log are in ', h('a', { href: REPO_DOCS.models, target: '_blank', rel: 'noopener', text: 'MODELS.md' }), '.'));
  const current = b.current_method;
  const currentPanel = current ? h('details', { class: 'editorial-details' }, h('summary', { text: 'Current method, test results and limitations' }),
    h('h2', { text: `Current source-evidence workflow · ${current.updated}` }),
    h('p', { class: 'notice', text: current.status }),
    h('div', { class: 'tiles' }, current.extractors.map((model, i) => h('div', { class: 'tile' },
      h('div', { class: 'label', text: `Independent extractor ${i + 1}` }), h('div', { class: 'value model-tag', text: model })))),
    h('p', { text: current.method }),
    h('p', {}, h('code', { text: '--profile relationships' }),
      ' selects this source-evidence method and is already the default. The older analyses profile is retained for earlier runs. ',
      h('a', { href: 'https://github.com/micmas/stroke-aphasia-kb/blob/main/docs/COMMANDS.md#extraction-options', target: '_blank', rel: 'noopener', text: 'Command options and progress counters' }),
      ' · ', h('a', { href: 'https://github.com/micmas/stroke-aphasia-kb/blob/main/docs/HOWTO.md', target: '_blank', rel: 'noopener', text: 'Step-by-step workflow and human review' })),
    h('p', { class: 'small', text: current.auditing }),
    h('div', { class: 'table-wrap' }, h('table', { class: 'models' },
      h('thead', {}, h('tr', {}, h('th', { text: 'Fresh-source validation paper' }), h('th', { text: 'Reference evidence groups located' }), h('th', { text: 'Both models: call time' }), h('th', { text: 'Qualification' }))),
      h('tbody', {}, current.papers.map(p => h('tr', {}, h('td', { text: paperLabel(p.key) }),
        h('td', { text: `${p.families_located} / ${p.reference_families}` }), h('td', { text: `About ${Math.round(p.paired_component_minutes)} min` }), h('td', { text: p.qualification })))))),
    h('p', { class: 'small', text: current.timing_note }), h('p', { class: 'small', text: current.coverage_note }),
    h('h3', { text: 'Review step' }), h('p', { text: current.review_status }),
    current.source_check ? h('div', {}, h('h3', { text: 'Source checking and draft recovery' }), h('p', { text: current.source_check.process }), h('p', { class: 'small', text: current.source_check.pilot })) : null,
    current.review_validation ? h('div', {},
      h('p', { class: 'small', text: current.review_validation.scope }),
      h('div', { class: 'table-wrap' }, h('table', { class: 'models' },
        h('thead', {}, h('tr', {}, h('th', { text: 'Review paper' }), h('th', { text: 'Time' }), h('th', { text: 'Independent source audit' }))),
        h('tbody', {}, current.review_validation.papers.map(p => h('tr', {},
          h('td', {}, h('a', { href: paperHref(p.key), text: paperLabel(p.key) })), h('td', { text: `${p.seconds} sec` }), h('td', { text: p.result })))))),
      h('p', { class: 'notice', text: current.review_validation.decision }),
      h('ul', {}, current.review_validation.caveats.map(text => h('li', { text })))) : null,
    current.review_comparison ? h('div', {},
      h('p', { class: 'small', text: current.review_comparison.scope }),
      h('div', { class: 'table-wrap' }, h('table', { class: 'models' },
        h('thead', {}, h('tr', {}, h('th', { text: 'Reviewer tested' }), h('th', { text: 'Call time' }), h('th', { text: 'Observed result' }))),
        h('tbody', {}, current.review_comparison.models.map(m => h('tr', {},
          h('td', { text: m.model }), h('td', { text: `${m.seconds} sec` }), h('td', { text: m.finding })))))),
      h('p', { class: 'small', text: current.review_comparison.caveat })) : null,
    current.additional_trials ? h('details', {}, h('summary', { text: 'Other tested settings and failed attempts' }),
      h('ul', {}, current.additional_trials.map(text => h('li', { text })))) : null,
    h('ul', {}, current.limitations.map(text => h('li', { text })))) : null;
  const roles = Object.entries(b.roles || {}).filter(([k]) => ROLE_TEXT[k]);
  const ms = [...(b.models || [])].sort((x, y) => (y.incumbent - x.incumbent) || (y.eligible - x.eligible) || ((y.link_recall || 0) - (x.link_recall || 0)));
  const thin = (b.papers || []).filter((p) => (p.findings || 0) < 5);
  const graded = (m) => (m.rows || []).some((r) => !r.ungraded && !r.failed);
  const verdict = (m) => (m.incumbent ? h('span', { class: 'badge badge-model', text: current ? 'used then' : 'in use' })
    : m.eligible ? h('span', { class: 'badge badge-human', title: 'Passes the rule on these papers; adopting it is still a person\'s decision', text: 'eligible' })
      : h('span', { class: 'badge badge-legacy', text: 'not eligible' }));
  const row = (m) => h('tr', {},
    h('td', {}, h('code', { text: m.model }), ' ', verdict(m), m.reasons?.length ? h('div', { class: 'small muted', text: m.reasons.join('; ') }) : null),
    h('td', { class: 'num' }, graded(m) ? h('span', { class: m.absent ? 'bad' : 'good', title: 'Quoted passages that are nowhere in the paper', text: `${m.absent} of ${m.quotes}` }) : h('span', { class: 'muted', text: 'not graded' })),
    h('td', { class: 'num', text: String(m.schema_issues ?? '—') }),
    h('td', {}, meter(m.shared_links || 0, m.ref_links || 0)),
    h('td', { class: 'num', title: `${m.shared_links || 0} of the ${m.links || 0} links it drafted are in the reference`, text: share(m.link_precision) }),
    h('td', { class: 'num', title: 'Mean strength of its findings minus the reference\'s (weak 1, moderate 2, strong 3). Positive = claims more strongly than the curated findings.', text: m.calibration_delta === null || m.calibration_delta === undefined ? '—' : `${m.calibration_delta > 0 ? '+' : ''}${m.calibration_delta.toFixed(2)}` }),
    h('td', { class: 'num', text: secs(m.mean_elapsed_s) }));
  const table = h('table', { class: 'models' }, h('thead', {}, h('tr', {},
    h('th', { text: 'Model' }), h('th', { class: 'num', text: 'Fabricated quotes' }), h('th', { class: 'num', text: 'Schema issues' }),
    h('th', { text: 'Known links found' }), h('th', { class: 'num', text: 'Precision' }), h('th', { class: 'num', text: 'Over-claiming' }), h('th', { class: 'num', text: 'Time per paper' }))),
    h('tbody', {}, ms.map(row)));
  const detail = (m) => h('details', { class: 'model-detail' }, h('summary', {}, h('code', { text: m.model }),
    h('span', { class: 'muted small', text: ` — ${[m.source?.developer?.replace(/\s*\(.*\)$/, ''), m.source?.licence?.split(/[;,:]/)[0], m.ram_class ? `needs about ${m.ram_class} GB of memory` : null].filter(Boolean).concat(['where it comes from, paper by paper']).join(' · ')}` })),
    provenance(m),
    m.note ? h('p', { class: 'small muted' }, h('b', { text: 'Caveat noted before testing: ' }), m.note) : null,
    (m.rows || []).length ? h('h4', { class: 'model-sub', text: 'Paper by paper' }) : null,
    (m.rows || []).map((r) => h('div', { class: 'model-paper' },
      h('p', {}, h('a', { href: paperHref(r.paper), text: r.paper }), ' · ',
        r.failed ? h('span', { class: 'bad', text: 'no drafts produced' })
          : `${plural(r.findings, 'finding')} in ${plural(r.drafts, 'draft')} (the reference has ${r.ref_findings}) · ${r.ungraded ? 'quotes not graded' : `${r.absent} of ${r.quotes} quotes absent, ${r.verified} verified verbatim`} · ${plural(r.schema_issues || 0, 'schema issue')} · ${secs(r.elapsed_s)}${r.processor ? ` (${r.processor})` : ''}`),
      r.failed ? null : h('p', { class: 'small' }, h('b', { text: `Found ${r.shared_links} of ${r.ref_links} known links` }),
        r.relationship_agreement !== undefined ? `, same relationship on ${share(r.relationship_agreement)} of them. ` : '. ',
        r.missed_links?.length ? ['Missed, among others: ', r.missed_links.map((x, i) => [i ? '; ' : '', linkLabel(index, x)]), '. '] : null,
        r.new_links?.length ? ['Links the reference does not have: ', r.new_links.map((x, i) => [i ? '; ' : '', linkLabel(index, x)]), '.'] : null))));
  const previousPanel = frag(
    current ? h('p', { class: 'notice', text: 'The comparison below used the previous drafting method. Its scores cannot be compared directly with the source-evidence pilot above.' }) : h('div', { class: 'tiles' }, roles.map(([k, r]) => h('div', { class: 'tile' }, h('div', { class: 'label', text: ROLE_TEXT[k][0] }), h('div', { class: 'value model-tag', text: r.model || '—' }), h('div', { class: 'detail', text: ROLE_TEXT[k][1] })))),
    h('h2', { text: `${current ? 'Earlier method comparison' : 'Latest comparison'} · ${b.date}` }),
    h('p', { class: 'small' }, `${plural(ms.length, 'model')} each extracted the same ${plural((b.papers || []).length, 'paper')} the knowledge base already holds (`,
      (b.papers || []).map((p, i) => [i ? ', ' : '', h('a', { href: paperHref(p.key), text: paperLabel(p.key) }), ` — ${plural(p.findings || 0, 'finding')}`]),
      '), and each result was scored against those curated findings.'),
    b.reference && b.reference !== 'all'
      ? h('p', { class: 'small' }, `The reference is ${b.reference_text || 'the findings approved under the governance policy'}: `,
        (b.papers || []).map((p, i) => `${i ? '; ' : ''}${p.key} ${plural(p.findings || 0, 'finding')}${p.left_out ? ` (${p.left_out} older ones not used)` : ''}`), '. ',
        thin.length ? h('b', { text: `With so few reference findings (${thin.map((p) => p.key).join(', ')}), "known links found" is indicative at best. ` }) : null,
        'Fabricated quotes and schema issues do not depend on the reference.')
      : h('p', { class: 'caveat' }, 'A caution on the reference: this comparison was scored against every curated finding, including older ones approved before the governance policy that nobody has re-read. "Known links found" then shows agreement with an earlier model\'s reading rather than correctness. Fabricated quotes and schema issues do not depend on the reference.'),
    h('div', { class: 'table-wrap' }, table),
    h('h3', { text: 'How to read the columns' }),
    h('ul', { class: 'small' },
      h('li', {}, h('b', { text: 'Fabricated quotes. ' }), 'Every passage a model quotes is searched for in the paper\'s text. A quote that is nowhere in the paper disqualifies the model: the KB\'s promise is that every finding can be checked against its source.'),
      h('li', {}, h('b', { text: 'Schema issues. ' }), 'Drafts that break the KB\'s format (a missing field, a file that cannot be read). Each one costs a reviewer time.'),
      h('li', {}, h('b', { text: 'Known links found. ' }), 'A finding links two things, such as a region and an impairment. This is the share of the links in the curated findings that the model also drafted, whichever entry it filed them under. '),
      h('li', {}, h('b', { text: 'Precision. ' }), 'The share of the model\'s own links that the curated findings have too. The rest may be real finds or noise; a person reads them.'),
      h('li', {}, h('b', { text: 'Over-claiming. ' }), 'How much more strongly the model words its findings than the curated ones. A model that under-claims is the safer extractor.'),
      h('li', {}, h('b', { text: 'Time per paper. ' }), 'On the maintainer\'s machine. Slower is acceptable; fabricating is not.')),
    h('p', { class: 'small' }, b.rule, ' Passing makes a model eligible; adopting it is a person\'s decision, recorded with its reasons in the ',
      h('a', { href: REPO_DOCS.models, target: '_blank', rel: 'noopener', text: 'decision log' }), '.'),
    h('h3', { text: 'Model by model' }),
    h('p', { class: 'small' }, b.sourcing || 'Every model is downloaded from the Ollama library and runs offline on the maintainer\'s computer.',
      ' Open a model for its developer, licence and original weights, then its results paper by paper.'),
    ms.map(detail));
  return frag(head, intro, current ? h('section', { class: 'model-overview' },
    h('h2', { text: 'From paper to finding' }),
    h('ol', {},
      h('li', {}, h('strong', { text: 'Extract. ' }), `${current.extractors.join(' and ')} independently collect relationships and supporting passages from the main paper.`),
      h('li', {}, h('strong', { text: 'Check. ' }), 'Model checks help identify errors. A person still needs to verify the source, context and completeness.'),
      h('li', {}, h('strong', { text: 'Approve. ' }), 'Source-checked evidence is mapped into KB drafts. Approval is recorded separately, with the reviewer’s identity.')),
    h('p', { class: 'notice', text: current.review_status }),
    h('p', {}, h('a', { href: 'https://github.com/micmas/stroke-aphasia-kb/blob/main/docs/HOWTO.md', text: 'Run the workflow: commands and human review steps →' }))) : null,
    currentPanel, current
    ? h('details', {}, h('summary', { text: `Earlier drafting benchmark · ${b.date} · different method` }), previousPanel)
    : previousPanel);
}
function provenance(m) {
  // where a model comes from: model_sources.yaml (curated) + `ollama show` on the publishing machine
  const s = m.source, l = m.local;
  if (!s && !l) return h('p', { class: 'small muted', text: 'Where this model comes from has not been documented yet (model_sources.yaml).' });
  const ext = (url, text) => h('a', { href: url, target: '_blank', rel: 'noopener', text: text || url.replace(/^https?:\/\/(www\.)?/, '') });
  const item = (k, ...v) => (v.some((x) => x) ? [h('dt', { text: k }), h('dd', {}, ...v)] : null);
  const ran = l ? [l.format, l.quantization, l.parameters ? `${l.parameters} parameters` : null, l.context_length ? `context ${Number(l.context_length).toLocaleString('en')} tokens` : null].filter(Boolean).join(' · ') : '';
  return h('div', { class: 'model-source' },
    h('dl', {},
      s ? item('Developer', s.developer, s.family ? ` · ${s.family} family` : '') : null,
      s ? item('Released', s.released) : null,
      s ? item('Licence', s.licence ? (s.licence_url ? ext(s.licence_url, s.licence) : s.licence) : null) : null,
      s ? item('Architecture', s.architecture, s.context ? ` · context ${s.context}` : '') : null,
      s ? item('Training data', s.data_cutoff ? `up to ${s.data_cutoff}` : null) : null,
      s ? item('Lineage', s.lineage) : null,
      s ? item('Original weights', s.upstream ? ext(s.upstream) : null) : null,
      item('How it was obtained', h('code', { text: `ollama pull ${m.model}` }), ' from the ', s?.library ? ext(s.library, 'Ollama library') : 'Ollama library', s?.weights ? `. ${s.weights}` : '.'),
      l ? item('As run here', ran, l.digest ? [ran ? ' · ' : '', 'digest ', h('code', { text: l.digest })] : null, l.ollama_version ? ` · Ollama ${l.ollama_version}` : '') : null),
    s?.checked ? h('p', { class: 'small muted', text: `Checked on ${s.checked} against the developer's model card and the Ollama library page.` }) : null);
}

function kindBadge(kind) { return h('span', { class: 'badge badge-kind', text: ['personal_factor','predictor'].includes(kind) ? FACTORS : kind === 'region' ? ANATOMY : kind }); }

function reviewBadge(f) {
  const kind = f.review_kind || 'none';
  const who = f.reviewer ? String(f.reviewer).replace(/^(human|model|agent):/, '') : '';
  const text = kind === 'human' ? `Approved · ${who || 'named person'}`
    : kind === 'model' ? `Model-approved${who ? ` · ${who}` : ''}`
      : kind === 'legacy' ? 'Legacy approval' : 'No named reviewer';
  return h('span', { class: `badge badge-${kind}`, title: REVIEW_LABEL[kind], text });
}

function strengthBadge(s) {
  const v = s || 'not reported';
  return h('span', { class: `badge badge-strength-${v}`, text: v === 'not_assessed' ? 'evidence strength not yet assessed' : `${v} evidence` });
}

function entryLink(index, id) {
  return h('a', { href: entryHref(id), title: id, text: index.name(id) });
}

function tagClass(supports) {
  const s = String(supports || '');
  return s === 'claim' ? 'tag-claim' : s === 'statistics' ? 'tag-statistics' : s === 'sample' ? 'tag-sample' : s === 'limitation' ? 'tag-limitation' : 'tag-other';
}

function kvList(obj, { skip = [] } = {}) {
  const rows = Object.entries(obj || {}).filter(([k, v]) => !skip.includes(k) && v !== null && v !== undefined && v !== '' && !(Array.isArray(v) && !v.length));
  if (!rows.length) return null;
  return h('dl', {}, rows.map(([k, v]) => [
    h('dt', { text: k.replace(/_/g, ' ') }),
    h('dd', { text: Array.isArray(v) ? v.join('; ') : typeof v === 'object' ? JSON.stringify(v) : String(v) }),
  ]));
}

function findingCard(index, f, { route = true, open = false } = {}) {
  const paper = index.byPaper.get(f.citation) ? f.citation : null;
  const meta = [h('a', { class: 'chip', href: paperHref(f.citation), text: paperLabel(f.citation) }),
    strengthBadge(f.strength), h('span', { class: 'badge', text: f.source_status === 'approved' ? 'Approved finding' : 'Draft · awaiting review' })];
  const lic = index.kb.licences?.[f.citation];
  const pdfLink = annotatedPdfLink(index, f.citation, f.source_passages?.[0]?.page);
  const displayValue = (value, field) => {
    if ((f.flags || []).includes(`not_transcribed:${field}`)) return 'Not yet transcribed';
    return value && !['not_reported', 'not reported', 'not_transcribed'].includes(String(value)) ? value : 'Not recorded';
  };
  const sample = f.sample || {};
  const basics = kvList({
    Participants: displayValue(sample.n || f.sample_n, 'sample.n'),
    Population: displayValue(sample.population || f.population, 'sample.population'),
    Timing: displayValue(sample.time_post_onset || f.time_post_onset, 'sample.time_post_onset'),
    Outcome: index.name(f.target),
    'Measured using': f.outcome_measurement?.instruments?.map(x => x.name).join('; ') || 'Not yet verified',
    'Score / task detail': f.outcome_measurement?.metric,
    Method: f.method.join(', '),
    'Study type': displayValue(f.evidence_quality || f.design, 'design'),
  });
  const context = f.presentation;
  const interpretation = context ? h('section', { class: 'clinical-context' },
    h('h4', { text: 'Relevance to scan interpretation' }),
    h('p', { class: 'small muted', text: context.origin === 'rule_based_saved_evidence' ? 'Interpretation aid from saved extraction · not clinically reviewed' : 'Editorial interpretation · draft for review' }),
    h('p', { text: context.relevance }),
    context.feature ? h('p', {}, h('strong', { text: 'Recorded feature: ' }), context.feature) : null,
    h('p', {}, h('strong', { text: 'Applies to: ' }), context.applies_to),
    context.limits ? h('p', {}, h('strong', { text: 'Limits: ' }), context.limits) : null,
    context.review_notes?.length ? h('ul', { class: 'context-review-notes' }, context.review_notes.map(note => h('li', { text: note }))) : null) : null;

  const details = [h('h4', { text: 'Analysis context' }), kvList({ relationship: RELATIONSHIP_TEXT[f.relationship] || f.relationship, result: f.direction === 'no_effect' ? 'No association detected' : DIRECTION_LABEL[f.direction] || f.direction, method: f.method, study_design: f.design, therapy: f.therapy })];
  if (f.target_audit) details.push(h('h4', { text: 'Outcome definition audit' }), h('p', { text: f.target_audit.reason }), h('p', { class: 'small muted', text: f.outcome_measurement?.note || '' }));
  if (f.sample && Object.keys(f.sample).length) details.push(h('h4', { text: 'Sample' }), kvList(f.sample));
  else if (f.population || f.sample_n) details.push(h('h4', { text: 'Sample' }), kvList({ n: f.sample_n, population: f.population, time_post_onset: f.time_post_onset }));
  if (f.statistics && Object.keys(f.statistics).length) details.push(h('h4', { text: 'Reported statistics' }), kvList(f.statistics));
  if (f.region_definition) details.push(h('h4', { text: 'How the paper defined the region' }), kvList(f.region_definition));
  if (f.design_cautions?.length) details.push(h('h4', { text: 'Design cautions (applied by the scoring rules)' }), h('ul', {}, f.design_cautions.map((x) => h('li', { text: String(x) }))));
  if (f.author_limitations?.length) details.push(h('h4', { text: 'Author-reported limitations' }), h('ul', {}, f.author_limitations.map((x) => h('li', { text: String(x) }))));
  if (f.flags?.length) details.push(h('h4', { text: 'Extraction flags' }), h('ul', {}, f.flags.map((x) => h('li', { text: String(x) }))));
  if (f.review && Object.keys(f.review).length) details.push(h('h4', { text: 'Review record' }), kvList(f.review));
  if (f.source_passages?.length) {
    details.push(h('h4', { text: 'Source passages (verbatim, with the page they were found on)' }));
    for (const p of f.source_passages) {
      details.push(h('blockquote', {},
        h('p', { text: String(p.quote || '') }),
        h('footer', {},
          h('span', { class: tagClass(p.supports), text: p.supports ? `supports ${String(p.supports).replace(/_/g, ' ')}` : 'passage' }),
          p.page !== undefined && p.page !== null ? ` · page ${p.page}` : '', p.section ? ` · ${p.section}` : '')));
    }
  }
  if (f.notes) details.unshift(h('h4', { text: 'Measurement and interpretation qualifications' }), h('p', { class: 'finding-notes', text: f.notes }));
  if (f.confounders_controlled?.length) details.push(h('h4', { text: 'Recorded adjustment variables' }), h('p', { text: f.confounders_controlled.join('; ') }));
  if (f.imaging_details) details.push(h('h4', { text: 'Imaging details' }), kvList(f.imaging_details));
  if (f.lesion_mapping) details.push(h('h4', { text: 'Lesion mapping' }), kvList(f.lesion_mapping));
  details.push(h('h4', { text: 'Review and reuse' }), h('p', { class: 'meta' }, reviewBadge(f), lic ? licenceBadge(lic) : null, pdfLink));
  if (f.source_check) {
    const check = f.source_check;
    details.push(h('p', { class: 'small', text: check.scope || 'Model source checking does not constitute human approval.' }));
    if (check.core_review?.checks) details.push(h('details', {}, h('summary', { text: 'Independent model checks' }),
      Object.entries(check.core_review.checks).map(([name, value]) => h('section', {}, h('h5', { text: name.replace(/_/g, ' ') }), h('p', { text: `${value.answer}: ${value.reason}` })))));
    if (check.binding) details.push(h('details', {}, h('summary', { text: 'Processing provenance' }), kvList(check.binding)));
  }


  return h('article', { class: 'finding', id: `f-${esc(f.source_path || f.source_id)}-${f.id}` },
    route ? h('p', { class: 'route' }, entryLink(index, f.source_id), ' ', kindBadge(f.source_kind), ' → ', entryLink(index, f.target), ' ', kindBadge(f.target_kind)) : null,
    h('p', { class: 'claim' }, open ? String(f.claim || '').trim() : h('a', { class: 'claim-link', href: findingHref(f), text: String(f.claim || '').trim() })),
    h('p', { class: 'meta' }, meta),
    open ? h('section', { class: 'study-summary' }, h('h3', { text: 'Study at a glance' }), basics, interpretation) :
      h('details', { class: 'study-summary' }, h('summary', { text: 'Study at a glance' }), basics, interpretation,
        h('a', { class: 'evidence-link', href: findingHref(f), text: 'Read full evidence and source passages' })),
    open ? h('section', { class: 'evidence-details' }, h('h3', { text: 'Full evidence' }), details) : null,
    paper === null ? h('p', { class: 'small muted', text: 'Citation key not found in the bibliography.' }) : null);
}

function stackBar(counts) {
  const total = Object.values(counts).reduce((a, b) => a + b, 0) || 1;
  const order = ['human', 'model', 'legacy', 'none'];
  const labels = { human: 'approved by a person', model: 'model-approved (Tier A)', legacy: 'legacy approval', none: 'no reviewer' };
  return frag(
    h('div', { class: 'stack', role: 'img', 'aria-label': order.map((k) => `${labels[k]}: ${counts[k]}`).join(', ') },
      order.filter((k) => counts[k]).map((k) => h('span', { class: `sw-${k}`, style: `width:${(100 * counts[k]) / total}%`, title: `${labels[k]}: ${counts[k]}` }))),
    h('div', { class: 'stack-legend' }, order.filter((k) => counts[k]).map((k) => h('span', {}, h('i', { class: `sw-${k}` }), `${labels[k]} ${counts[k]} (${pct(counts[k], total)})`))));
}

function barList(items, { max = null, link = null } = {}) {
  const top = max === null ? items : items.slice(0, max);
  const biggest = Math.max(1, ...top.map((x) => x.n));
  return h('ul', { class: 'barlist' }, top.map((x) => h('li', {},
    link ? h('a', { href: link(x), title: x.id, text: x.label }) : h('span', { text: x.label }),
    h('span', { class: `bar${x.alt ? ' alt' : ''}`, style: `width:${Math.max(2, (100 * x.n) / biggest)}%` }),
    h('span', { class: 'n', text: String(x.n) }))));
}

// ---------------------------------------------------------------------------
// Views
// ---------------------------------------------------------------------------
function overview(index) {
  const { kb, findings, papers, entries } = index;
  const v = kb.version || {};
  const prov = provenanceCounts(findings);
  const countBy = (pred, key) => {
    const m = new Map();
    for (const f of findings) {
      if (f.source_kind === pred) m.set(f.source_id, (m.get(f.source_id) || 0) + 1);
      if (f.target_kind === pred) m.set(f.target, (m.get(f.target) || 0) + 1);
    }
    return [...m.entries()].map(([id, n]) => ({ id, n, label: index.name(id), alt: !index.hasEntry(id) })).sort((a, b) => b.n - a.n || a.label.localeCompare(b.label));
  };
  const topicList = category => barList(overviewTopics(index, category), {
    link: x => href('/topic', {category, topic:x.id}),
  });
  const atlas = atlasCoverage(index);
  const reachable = atlas.counts.mapped + atlas.counts.approximation;
  const unreachable = atlas.rows.filter(row => ['pending', 'atlas_gap'].includes(row.status));


  return h('div', { class: 'overview-page' },
    h('header', { class: 'editorial-hero' },
      h('p', { class: 'eyebrow', text: 'Stroke aphasia knowledge base' }),
      h('h1', { text: 'What can research tell us about aphasia after stroke?' }),
      h('p', { class: 'lead', text: 'Explore findings on brain injury, language, treatment and recovery. Follow each finding back to the paper, and see how it was reviewed.' }),
      h('p', { class: 'byline', text: 'A research project led by Michele Masson-Trottier, open to collaborators.' }),
      h('div', { class: 'editorial-actions' }, h('a', { class: 'editorial-button', href: '#/findings', text: 'Explore the findings' }), h('a', { href: '#/involve', text: 'Contribute to the project →' }))),
    h('p', { class: 'caveat', text: 'Research in progress. These are findings from groups of participants; they do not predict an individual person’s outcome or replace clinical assessment.' }),
    (v.statuses || []).some(s => s !== 'approved') ? h('p', { class: 'caveat drafts', text: 'This view includes unapproved drafts. Use the Status filter on the Findings page to separate them.' }) : null,
    h('div', { class: 'project-counts' },
      h('p', {}, h('strong', { text: String(papers.length) }), ' papers with findings'),
      h('p', {}, h('strong', { text: String(findings.length) }), ' findings to explore'),
      h('p', {}, h('strong', { text: pct(prov.human, findings.length) }), ' approved by a named person')),
    h('div', { class: 'editorial-columns' },
      h('section', {}, h('h2', { text: 'Read the evidence' }), h('p', { text: 'Look up a brain region, language difficulty or treatment. Read the claim, its supporting passage and the study context together.' }), h('a', { href: '#/matrix', text: 'Browse region–language links →' })),
      h('section', {}, h('h2', { text: 'Connect it to imaging' }), h('p', { text: 'CALMaR brings lesion maps, white matter disconnection estimates and literature findings into a research report.' }), h('a', { href: NOTEBOOK_PAGE, text: 'Explore the CALMaR examples →' }))),
    h('section', { class: 'review-summary' }, h('h2', { text: 'How much has been checked?' }),
      stackBar(prov),
      h('p', { text: 'Review status varies. Some findings have a named human approval; others have model approval or an older approval awaiting re-review. Read the status alongside the evidence.' }),
      h('p', {}, h('a', { href: href('/findings', { review_kind: ['human'] }), text: 'See person-approved findings' }), ' · ', h('a', { href: '#/models', text: 'How we use and test AI' }))),
    h('details', { class: 'editorial-details' }, h('summary', { text: 'Explore coverage and atlas mapping' }),
      h('p', {}, h('a', { href: '#/coverage', text: 'Search methods, screening decisions and evidence gaps →' })),
      h('div', { class: 'grid-2' },
        h('section', {}, h('h2', { text: ANATOMY }), topicList(ANATOMY)),
        h('section', {}, h('h2', { text: 'Language difficulties' }), barList(countBy('impairment'), { max: 12, link: x => entryHref(x.id) }))),
      h('p', { class: 'small muted', text: 'Bars count findings, not evidence quality. Select a topic to explore its detailed entries.' }),
      h('h2', { text: FACTORS }), topicList(FACTORS),
      h('h2', { text: 'Therapies' }), topicList('Therapies'),
      h('h2', { text: 'Atlas mapping' }), h('p', { text: `${reachable} of ${atlas.total} region entries have a curated anatomical link, including ${atlas.counts.approximation} approximations. ${atlas.counts.pending} await mapping assessment; ${atlas.counts.atlas_gap} have a documented atlas gap. Anatomical links help find relevant literature; they do not verify an exact match to the study’s imaging measure.` }),
      unreachable.length ? h('details', {}, h('summary', { text: 'Regions without a mapping' }), h('ul', {}, unreachable.map(row => h('li', {}, entryLink(index, row.entry.id), ` — ${row.reason}`)))) : null),
    h('details', { class: 'editorial-details' }, h('summary', { text: 'Data version and reuse' }),
      h('p', { class: 'small', text: `KB ${v.commit || 'uncommitted'} · ${v.date || ''} · digest ${v.contentDigest || '?'} · exported ${v.exportedOn || '?'} · statuses: ${(v.statuses || []).join(', ')}` }),
      h('p', {}, 'The code, methods and review history are available in the ', h('a', { href: 'https://github.com/micmas/stroke-aphasia-kb', text: 'project repository' }), '.')));

}

function topicOverview(index, route) {
  const category = route.params.get('category');
  const topic = overviewTopics(index, category).find(t => t.id === route.params.get('topic'));
  if (!topic) return h('p', {text:'This topic has no findings in the selected evidence version.'});
  return h('div', {},
    h('p', {}, h('a', {href:'#/',text:'← Overview'})),
    h('h1', {text:topic.label}),
    h('p', {class:'muted',text:`${category} · ${plural(topic.n, 'finding')} · ${plural(topic.entries.length, 'entry', 'entries')}`}),
    h('p', {text:'Explore the breakdown below. Entries retain their study-specific definitions and measurements; grouping them here does not combine their results.'}),
    ...topic.entries.map(e => h('section', {},
      h('h2', {}, entryLink(index,e.id)),
      h('p', {text:plural(e.n,'finding')}),
      h('a', {href:href('/findings',{key:[...e.keys]}),text:'Explore these findings →'}))));
}

function browse(index, route) {
  const filters = route.filters;
  const query = route.params.get('q') || '';
  const sort = route.params.get('sort') || 'kb';
  const counts = facetCounts(index.findings, filters, query);
  let rows = index.findings.filter((f) => matches(f, filters, query));
  const strengthRank = { strong: 0, moderate: 1, weak: 2 };
  if (sort === 'strength') rows = rows.slice().sort((a, b) => (strengthRank[a.strength] ?? 3) - (strengthRank[b.strength] ?? 3) || a.ordinal - b.ordinal);
  else if (sort === 'year') rows = rows.slice().sort((a, b) => (b.year || 0) - (a.year || 0) || a.ordinal - b.ordinal);
  else if (sort === 'paper') rows = rows.slice().sort((a, b) => String(a.citation).localeCompare(String(b.citation)) || a.page - b.page);

  const go = (next, params = {}) => { location.hash = href('/findings', { ...next, q: query, sort, ...params }); };
  const toggle = (key, value) => {
    const cur = new Set(filters[key] || []);
    if (cur.has(value)) cur.delete(value); else cur.add(value);
    go({ ...filters, [key]: [...cur] });
  };

  const facetNodes = FACETS.map((facet) => {
    const m = counts[facet.key];
    let values = [...m.keys()];
    if (facet.order) values.sort((a, b) => (facet.order.indexOf(a) === -1 ? 99 : facet.order.indexOf(a)) - (facet.order.indexOf(b) === -1 ? 99 : facet.order.indexOf(b)));
    else values.sort((a, b) => (m.get(b) - m.get(a)) || String(a).localeCompare(String(b)));
    const selected = new Set(filters[facet.key] || []);
    const many = values.length > 12;
    const shown = many ? values.filter((v, i) => i < 10 || selected.has(v)) : values;
    return h('details', { class: 'facet', open: selected.size || ['category', 'subcategory', 'relationship', 'strength', 'review_kind'].includes(facet.key) ? '' : null },
      h('summary', { text: `${facet.label}${selected.size ? ` (${selected.size})` : ''}` }),
      shown.map((v) => h('label', { class: m.get(v) ? '' : 'zero' },
        h('input', { type: 'checkbox', checked: selected.has(v) ? '' : null, onchange: () => toggle(facet.key, v) }),
        h('span', { text: facet.link ? index.name(v) : (facet.labels && facet.labels[v]) || String(v).replace(/_/g, ' '), title: String(v) }),
        h('span', { class: 'n', text: String(m.get(v) || 0) }))),
      many && shown.length < values.length ? h('p', { class: 'small muted', text: `${values.length - shown.length} more — narrow with the search box` }) : null);
  });

  const active = Object.entries(filters).filter(([k]) => k !== 'key').flatMap(([k, vs]) => vs.map((v) => h('button', { type: 'button', onclick: () => toggle(k, v), text: `${FACETS.find((f) => f.key === k)?.label || k}: ${FACETS.find((f) => f.key === k)?.link ? index.name(v) : (FACETS.find((f) => f.key === k)?.labels?.[v] || v)} ×` })));
  if (filters.key?.length) active.push(h('button', { type: 'button', onclick: () => go({ ...filters, key: [] }), text: `Selected findings: ${filters.key.length} findings ×` }));
  if (query) active.push(h('button', { type: 'button', onclick: () => go(filters, { q: '' }), text: `search: ${query} ×` }));
  if (active.length) active.push(h('button', { type: 'button', onclick: () => { location.hash = '#/findings'; }, text: 'clear all' }));

  const search = h('input', { class: 'search', type: 'search', placeholder: 'Search claims, quotes, entries, papers…', value: query, 'aria-label': 'Search findings' });
  let timer = null;
  search.addEventListener('input', () => { clearTimeout(timer); timer = setTimeout(() => go(filters, { q: search.value.trim() }), 250); });

  const shown = rows.slice(0, state.shown);
  const list = h('div', {}, shown.map((f) => findingCard(index, f)));
  const more = rows.length > shown.length ? h('button', { class: 'btn btn-primary', type: 'button', onclick: () => { state.shown += PAGE; render(); }, text: `Show ${Math.min(PAGE, rows.length - shown.length)} more of ${rows.length}` }) : null;

  return h('div', { class: 'two-col' },
    h('aside', { class: 'facets', 'aria-label': 'Filters' }, search, facetNodes),
    h('section', {},
      h('div', { class: 'results-head' }, h('h1', { text: 'Findings' }), h('span', { class: 'count', text: `${rows.length} of ${index.findings.length}` }),
        h('label', { class: 'small muted' }, 'sort ', h('select', { onchange: (e) => go(filters, { sort: e.target.value }) },
          [['kb', 'knowledge-base order'], ['strength', 'strength'], ['year', 'year, newest first'], ['paper', 'paper, then page']].map(([v, t]) => h('option', { value: v, selected: v === sort ? '' : null, text: t }))))),
      h('div', { class: 'active-filters' }, active),
      rows.length ? list : h('p', { class: 'notice', text: 'No finding matches these filters.' }),
      more));
}

function matrix(index, route) {
  const kind = route.params.get('kind') || 'region-impairment';
  const min = Number(route.params.get('min') || 1);
  const onlyEntries = route.params.get('entries') === '1';
  const find = (route.params.get('find') || '').toLowerCase();
  const level = ['broad', 'specific', 'paper'].includes(route.params.get('level')) ? route.params.get('level') : 'broad';
  const grouped = level !== 'paper';
  const m = grouped ? groupedMatrix(index, kind, level) : matrixOf(index, kind);
  const name = grouped ? m.name : index.name;
  const rowLink = r => grouped ? href('/findings', { key: [...new Set(m.cols.flatMap(c => m.cell(r, c).map(f => f.key)))] }) : entryHref(r);
  const colLink = c => grouped ? href('/findings', { key: [...new Set(m.rows.flatMap(r => m.cell(r, c).map(f => f.key)))] }) : entryHref(c);
  const keep = (id) => (grouped || !onlyEntries || index.hasEntry(id)) && (!find || name(id).toLowerCase().includes(find) || id.toLowerCase().includes(find));
  const rows = m.rows.filter((r) => keep(r) && m.rowTotals.get(r) >= min);
  const cols = m.cols.filter((c) => keep(c) && m.colTotals.get(c) >= min);
  const kinds = { 'region-impairment': ['Region', 'Impairment'], 'therapy-impairment': ['Therapy', 'Impairment'], 'predictor-outcome': [FACTORS, 'Outcome'], 'region-region': ['Region', 'Region (network / tract)'] };
  const [rowLabel, colLabel] = kinds[kind] || ['Entry', 'Target'];
  const cls = (n) => (n >= 8 ? 'c6' : n >= 5 ? 'c5' : n >= 4 ? 'c4' : n === 3 ? 'c3' : n === 2 ? 'c2' : n === 1 ? 'c1' : '');
  const go = (params) => { location.hash = href('/matrix', { kind, min, level, entries: onlyEntries ? '1' : '', find, ...params }); };

  const filtersFor = (r, c) => ({ key: m.cell(r, c).map(f => f.key) });
  const tooltip = h('div', { class: 'tooltip hidden', role: 'tooltip' });
  const showTip = (e, r, c) => {
    const cell = m.cell(r, c);
    const prov = provenanceCounts(cell);
    const rel = {}; const str = {};
    for (const f of cell) { rel[f.relationship] = (rel[f.relationship] || 0) + 1; str[f.strength] = (str[f.strength] || 0) + 1; }
    tooltip.replaceChildren(h('b', { text: `${name(r)} × ${name(c)}` }), h('br'),
      `${plural(cell.length, 'finding')} from ${plural(new Set(cell.map((f) => f.citation)).size, 'paper')}`, h('br'),
      `strength: ${Object.entries(str).map(([k, n]) => `${k === 'not_assessed' ? 'evidence strength not yet assessed' : k} ${n}`).join(', ')}`, h('br'),
      `relationship: ${Object.entries(rel).map(([k, n]) => `${k} ${n}`).join(', ')}`, h('br'),
      `approved by a person: ${prov.human}`);
    tooltip.classList.remove('hidden');
    const x = Math.min(e.clientX + 14, window.innerWidth - 330); const y = Math.min(e.clientY + 14, window.innerHeight - 120);
    tooltip.style.left = `${x}px`; tooltip.style.top = `${y}px`;
  };
  const hideTip = () => tooltip.classList.add('hidden');

  const table = h('table', { class: 'matrix' },
    h('thead', {}, h('tr', {}, h('th', { class: 'corner', scope: 'col', text: `${rowLabel} ↓ · ${colLabel} →` }),
      cols.map((c) => h('th', { scope: 'col', class: grouped || index.hasEntry(c) ? '' : 'noentry' }, h('a', { class: 'rot', href: colLink(c), title: `${name(c)} (${m.colTotals.get(c)})`, text: name(c) }))),
      h('th', { scope: 'col', class: 'total' }, h('span', { class: 'rot', text: 'total' })))),
    h('tbody', {}, rows.map((r) => h('tr', {},
      h('th', { scope: 'row', class: grouped || index.hasEntry(r) ? '' : 'noentry' }, h('a', { href: rowLink(r), title: grouped ? name(r) : index.hasEntry(r) ? r : `${r} — no entry of its own yet`, text: name(r) })),
      cols.map((c) => { const n = m.cell(r, c).length; return h('td', { class: cls(n) }, n ? h('a', { href: href('/findings', filtersFor(r, c)), 'aria-label': `${n} findings for ${name(r)} and ${name(c)}`, onmousemove: (e) => showTip(e, r, c), onmouseleave: hideTip, onfocus: (e) => showTip({ clientX: e.target.getBoundingClientRect().left, clientY: e.target.getBoundingClientRect().top }, r, c), onblur: hideTip, text: String(n) }) : ''); }),
      h('td', { class: 'total', text: String(m.rowTotals.get(r)) })))),
    h('tfoot', {}, h('tr', { class: 'total' }, h('th', { scope: 'row', text: 'total' }), cols.map((c) => h('td', { text: String(m.colTotals.get(c)) })), h('td', { text: String([...m.cells.values()].reduce((n, x) => n + x.length, 0)) }))));

  return frag(
    h('div', { class: 'page-head' }, h('h1', { text: 'Evidence matrix' }), h('span', { class: 'muted small', text: `${rows.length} ${rowLabel.toLowerCase()} rows × ${cols.length} ${colLabel.toLowerCase()} columns` })),
    h('p', { class: 'small' }, 'Start with broad anatomy and clinical domains, then refine the labels or see the original paper terms. Each finding appears in one cell; compound regions and combined outcomes stay together. Click a cell to read the original findings.'),
    h('p', { class: 'small muted', text: 'These are browsing groups, not atlas-equivalent parcels or pooled effects. Unclear anatomy stays unclassified. Harvard–Oxford correspondence needs a verified anatomical or spatial mapping; white-matter tracts keep their own names.' }),
    h('div', { class: 'matrix-controls' },
      h('label', {}, 'detail ', h('select', { 'aria-label': 'Matrix label detail', onchange: e => go({ level: e.target.value }) }, [['broad','Broad groups'],['specific','More specific labels'],['paper','Original paper terms']].map(([v,label]) => h('option', {value:v, selected:v===level?'':null, text:label})))),
      h('label', {}, 'matrix ', h('select', { onchange: (e) => go({ kind: e.target.value }) }, Object.entries(kinds).map(([v, [a, b]]) => h('option', { value: v, selected: v === kind ? '' : null, text: `${a} × ${b}` })))),
      h('label', {}, 'at least ', h('select', { onchange: (e) => go({ min: e.target.value }) }, [1, 2, 3, 5].map((v) => h('option', { value: v, selected: v === min ? '' : null, text: `${v}` }))), ' findings on the margin'),
      !grouped ? h('label', {}, h('input', { type: 'checkbox', checked: onlyEntries ? '' : null, onchange: (e) => go({ entries: e.target.checked ? '1' : '' }) }), ' only ids with an entry') : null,
      h('input', { type: 'search', placeholder: 'find a row or column…', value: find, 'aria-label': 'Filter rows and columns', onchange: (e) => go({ find: e.target.value.trim() }) }),
      h('span', { class: 'ramp' }, '1', h('i', { style: 'background:var(--seq-1)' }), h('i', { style: 'background:var(--seq-2)' }), h('i', { style: 'background:var(--seq-3)' }), h('i', { style: 'background:var(--seq-4)' }), h('i', { style: 'background:var(--seq-5)' }), h('i', { style: 'background:var(--seq-6)' }), '8+ findings')),
    rows.length && cols.length ? h('div', { class: 'matrix-wrap' }, table) : h('p', { class: 'notice', text: 'Nothing to show with these settings.' }),
    tooltip);
}

function papers(index) {
  const sortKey = { key: 'key' };
  const licences = Object.keys(index.kb.licences || {}).length ? index.kb.licences : null;
  if (licences) for (const p of index.papers) p.licence = (licences[p.key] || {}).category || 'zz';
  const table = h('table', { class: 'paper-list sortable' });
  const render = (by, dir) => {
    const rows = index.papers.slice().sort((a, b) => {
      const x = a[by]; const y = b[by];
      const r = typeof x === 'number' && typeof y === 'number' ? x - y : String(x ?? '').localeCompare(String(y ?? ''));
      return dir === 'asc' ? r : -r;
    });
    const head = (label, k, numeric = false) => h('th', { class: numeric ? 'num' : '' }, h('button', { type: 'button', 'aria-sort': by === k ? (dir === 'asc' ? 'ascending' : 'descending') : 'none', onclick: () => render(k, by === k && dir === 'desc' ? 'asc' : 'desc'), text: label }));
    table.replaceChildren(
      h('thead', {}, h('tr', {}, head('Key', 'key'), head('First author', 'author'), head('Year', 'year', true), head('Findings', 'n', true), head('Person-approved', 'human', true), h('th', { text: 'Entries' }), licences ? head('Licence', 'licence') : null, index.screening.present ? h('th', { text: 'Screening' }) : null)),
      h('tbody', {}, rows.map((p) => h('tr', {},
        h('td', {}, h('a', { class: 'chip', href: paperHref(p.key), text: paperLabel(p.key) })),
        h('td', { text: p.author }), h('td', { class: 'num', text: p.year ? String(p.year) : '—' }),
        h('td', { class: 'num', text: String(p.n) }), h('td', { class: 'num', text: String(p.human) }),
        h('td', { class: 'small' }, p.entries.slice(0, 4).map((id, i) => [i ? ', ' : '', entryLink(index, id)]), p.entries.length > 4 ? ` +${p.entries.length - 4}` : ''),
        licences ? h('td', {}, licenceBadge(licences[p.key])) : null,
        index.screening.present ? h('td', {}, (() => { const c = index.screening.byKey.get(p.key); return c ? h('a', { href: coverageHref({ q: c.id }), title: `${c.id} · ${STAGE_TEXT[c.stage] || c.stage}` }, stageBadge(c.stage)) : h('span', { class: 'muted small', text: 'not in the register' }); })()) : null))));
  };
  render('n', 'desc');
  const cited = Object.keys(index.kb.citations || {}).length;
  return frag(
    h('div', { class: 'page-head' }, h('h1', { text: 'Papers' }), h('span', { class: 'muted small', text: `${index.papers.length} papers with findings · ${cited} bibliography entries` })),
    h('p', { class: 'small' }, h('a', { href: '#/licences', text: 'Licences of these papers' }),
      licences ? ` — ${index.papers.filter((p) => licences[p.key]?.category === 'cc').length} under Creative Commons, ${index.papers.filter((p) => licences[p.key]).length} of ${index.papers.length} checked` : ' — not looked up yet'),
    h('p', { class: 'small', text: 'Source PDFs are not redistributed; the bibliography carries a DOI for every key. Open a paper to read its findings in page order and check each quote against the PDF.' }),
    index.screening.present ? h('p', { class: 'small muted' }, 'Papers that were screened but have no findings yet are listed under ', h('a', { href: '#/coverage', text: 'Coverage' }), '.') : null,
    table);
}

// Every bibliography entry with its licence (screen.py licences → screening/licences.yaml).
const LICENCE_ORDER = ['cc', 'cc_manuscript', 'free_to_read', 'rights_reserved', 'unknown', 'unchecked'];
function licencesView(index, route) {
  const lic = index.kb.licences || {};
  const keys = [...index.byPaper.keys()].filter((k) => (index.byPaper.get(k) || []).length);   // papers with findings in this export
  const rows = keys.map((key) => {
    const rec = lic[key];
    const findings = (index.byPaper.get(key) || []).length;
    return { key, rec, category: rec ? rec.category || 'unknown' : 'unchecked', year: yearOf(key, index.kb.citations?.[key]), findings,
      doi: index.papers.find((p) => p.key === key)?.doi || (index.kb.citationLinks?.[key] || '').replace(/^https?:\/\/(dx\.)?doi\.org\//, '') || null };
  });
  const counts = Object.fromEntries(LICENCE_ORDER.map((c) => [c, rows.filter((r) => r.category === c).length]));
  const pick = route.params.get('c');
  const shown = rows.filter((r) => !pick || r.category === pick)
    .sort((a, b) => LICENCE_ORDER.indexOf(a.category) - LICENCE_ORDER.indexOf(b.category) || b.findings - a.findings || a.key.localeCompare(b.key));
  const tile = (c) => h('a', { class: `tile tile-link${pick === c ? ' active' : ''}`, href: pick === c ? '#/licences' : `#/licences?c=${c}` },
    h('div', { class: 'value', text: String(counts[c]) }),
    h('div', { class: 'label' }, c === 'unchecked' ? h('span', { class: 'badge badge-licence badge-licence-unknown', text: 'not checked yet' }) : licenceBadge({ category: c })));
  return frag(
    h('div', { class: 'page-head' }, h('h1', { text: 'Licences' }),
      h('span', { class: 'muted small', text: `${keys.length} papers with findings · ${keys.filter((k) => lic[k]).length} checked` })),
    h('p', { class: 'small', text: 'What each paper may be reused under, from Crossref, Unpaywall and the PDF’s own licence statement (screen.py licences). Under a Creative Commons licence the quoted passages are reused under that licence with the citation as attribution; for every other paper they are short quotations for checking a claim. Source PDFs are not redistributed.' }),
    Object.keys(lic).length ? null : h('p', { class: 'caveat', text: 'No licence has been looked up yet: run "python scripts/screen.py licences --execute" and re-export.' }),
    h('div', { class: 'tiles' }, LICENCE_ORDER.filter((c) => counts[c]).map(tile)),
    h('table', { class: 'paper-list' },
      h('thead', {}, h('tr', {}, ['Paper', 'Year', 'Licence', 'Version', 'Source', 'Findings', 'Links'].map((t) => h('th', { class: t === 'Year' || t === 'Findings' ? 'num' : '', text: t })))),
      h('tbody', {}, shown.map((r) => h('tr', {},
        h('td', {}, h('a', { class: 'chip', href: paperHref(r.key), text: paperLabel(r.key) })),
        h('td', { class: 'num', text: r.year ? String(r.year) : '—' }),
        h('td', {}, r.rec ? licenceBadge(r.rec) : h('span', { class: 'muted small', text: 'not checked' }),
          r.rec?.label && !['cc', 'cc_manuscript'].includes(r.category) ? h('div', { class: 'small muted', text: r.rec.label }) : null),
        h('td', { class: 'small', text: r.rec?.version || '' }),
        h('td', { class: 'small muted', text: r.rec?.source || '' }),
        h('td', { class: 'num', text: String(r.findings) }),
        h('td', { class: 'small' },
          r.doi ? h('a', { href: `https://doi.org/${r.doi}`, rel: 'noopener', target: '_blank', text: 'DOI' }) : null,
          r.rec?.oa_url ? frag(r.doi ? ' · ' : '', h('a', { href: r.rec.oa_url, rel: 'noopener', target: '_blank', text: 'free copy' })) : null,
          r.rec?.url && r.rec.url !== r.rec.oa_url ? frag(' · ', h('a', { href: r.rec.url, rel: 'noopener', target: '_blank', text: /creativecommons|terms|licen|rights|pages|policies/i.test(r.rec.url) ? 'terms' : 'source' })) : null))))));
}

function paper(index, key) {
  const k = key.startsWith('@') ? key : `@${key}`;
  const rows = (index.byPaper.get(k) || []).slice().sort((a, b) => a.page - b.page || a.ordinal - b.ordinal);
  const text = index.kb.citations?.[k];
  const p = index.papers.find((x) => x.key === k);
  if (!rows.length && !text && !index.screening.byKey.has(k)) return h('p', { class: 'error', text: `No paper ${k} in this export.` });
  const prov = provenanceCounts(rows);
  return frag(
    h('div', { class: 'page-head' }, h('h1', { text: paperLabel(k) })),
    text ? h('p', { text }) : h('p', { class: 'muted', text: 'Not in the bibliography.' }),
    p?.doi ? h('p', { class: 'small' }, 'DOI ', h('a', { href: `https://doi.org/${p.doi}`, rel: 'noopener', target: '_blank', text: p.doi })) : null,
    (() => { const link = annotatedPdfLink(index, k); return link ? h('p', { class: 'paper-actions' }, link) : null; })(),
    (() => {
      const lic = index.kb.licences?.[k];
      if (!lic) return null;
      return h('p', { class: 'small' }, 'Licence ', licenceBadge(lic),
        lic.label && !['cc', 'cc_manuscript'].includes(lic.category) ? ` ${lic.label}` : '',
        lic.version ? ` · ${lic.version}` : '',
        lic.oa_url ? frag(' · ', h('a', { href: lic.oa_url, rel: 'noopener', target: '_blank', text: 'free copy' })) : '',
        lic.url && lic.url !== lic.oa_url ? frag(' · ', h('a', { href: lic.url, rel: 'noopener', target: '_blank', text: 'terms' })) : '',
        lic.source ? h('span', { class: 'muted', text: ` · from ${lic.source}${lic.checked ? `, ${lic.checked}` : ''}` }) : null);
    })(),
    h('p', { class: 'small muted', text: `${plural(rows.length, 'finding')} across ${plural(new Set(rows.map((r) => r.source_id)).size, 'entry', 'entries')} · approved by a person: ${prov.human} · model: ${prov.model} · legacy: ${prov.legacy}` }),
    screeningPanel(index, k),
    rows.length ? h('h2', { text: 'Findings, in page order' }) : h('p', { class: 'muted', text: 'No approved finding cites this paper in this export.' }),
    rows.map((f) => findingCard(index, f)));
}

function entry(index, id) {
  const e = index.entries[id];
  const inEntry = index.bySource.get(id) || [];
  const about = index.byTarget.get(id) || [];
  if (!e && !inEntry.length && !about.length) return h('p', { class: 'error', text: `No entry or target "${id}" in this export.` });
  const kind = index.kindOf(id);
  const name = index.name(id);
  const groups = (rows, by) => {
    const m = new Map();
    for (const f of rows) (m.get(f[by]) || m.set(f[by], []).get(f[by])).push(f);
    return [...m.entries()].sort((a, b) => b[1].length - a[1].length || index.name(a[0]).localeCompare(index.name(b[0])));
  };
  const mapped = index.mapping.regions[id];
  const reason = mappingStatus(index, e || {id}).reason;
  const kv = {};
  if (e) {
    kv.category = e.category || e.bucket; if(e.subcategory) kv.subcategory = e.subcategory; if (e.kind) kv['entry kind'] = e.kind; if (e.status) kv.status = e.status;
    if (e.reviewer) kv.reviewer = String(e.reviewer); if (e.review_tier) kv['review tier'] = e.review_tier;
    if (e.rtss_category) kv['RTSS category'] = e.rtss_category;
  }
  const ingredients = (e?.rtss_ingredients || []).map((i) => index.entries[i] ? h('a', { href: entryHref(i), text: index.entries[i].name }) : h('span', { text: i.replace(/_/g, ' ') }));
  const stages = index.kb.rules?.therapyEvidenceStages?.[id];
  const therapies = index.therapiesFor.get(id) || [];

  return frag(
    h('div', { class: 'entry-head' }, h('h1', { text: name }), kindBadge(kind), e ? null : h('span', { class: 'badge badge-legacy', text: 'no entry of its own — appears as a target' })),
    e?.aliases?.length ? h('p', { class: 'aliases', text: `Also: ${e.aliases.join(' · ')}` }) : null,
    e?.short_description ? h('p', { text: String(e.short_description).trim() }) : null,
    Object.keys(kv).length ? h('dl', { class: 'kv' }, Object.entries(kv).map(([k, v]) => [h('dt', { text: k }), h('dd', { text: v })])) : null,
    kind === 'region' ? h('section', { class: 'panel' }, h('h3', { text: 'Atlas mapping (how a lesion reaches this entry)' }),
      mapped ? frag(
        h('p', { class: 'small' }, 'Side: ', h('b', { text: mapped.side }), mapped.review ? h('span', { class: 'badge badge-warn', style: 'margin-left:.5rem', text: 'mapping flagged for review' }) : null),
        h('ul', {}, (mapped.units || []).map((u) => { const unit = index.mapping.units[u]; return h('li', {}, h('b', { text: unit?.name || u }), unit ? ` — ${unit.atlas}: ${(Array.isArray(unit.labels) ? unit.labels : Object.values(unit.labels || {}).flat()).join(', ')} (${unit.kind})` : ''); })),
        mapped.basis ? h('p', { class: 'small muted', text: mapped.basis }) : null)
        : h('p', { class: 'small' }, h('span', { class: 'badge badge-warn', text: 'not reachable from a lesion mask' }), ' ', reason || 'No curated atlas mapping for this entry; its findings are readable here but cannot be matched by CALMaR.')) : null,
    kind === 'therapy' ? h('section', { class: 'panel' }, h('h3', { text: 'Targets and ingredients' }),
      e?.targets_impairments?.length ? h('p', {}, 'Targets: ', e.targets_impairments.map((t, i) => [i ? ', ' : '', entryLink(index, t)])) : null,
      ingredients.length ? h('p', {}, 'RTSS ingredients: ', ingredients.map((n, i) => [i ? ', ' : '', n])) : null,
      stages?.length ? h('p', { class: 'small muted', text: `Evidence covers recovery stage(s): ${stages.join(', ')}` }) : null) : null,
    kind === 'impairment' && therapies.length ? h('section', { class: 'panel' }, h('h3', { text: 'Therapies whose entry targets this impairment' }),
      h('p', {}, therapies.map((t, i) => [i ? ', ' : '', entryLink(index, t)]))) : null,
    inEntry.length ? frag(
      h('div', { class: 'group-head' }, h('h2', { text: `Findings in this entry` }), h('span', { class: 'n', text: `${inEntry.length} · ` }), h('a', { class: 'small', href: href('/findings', { source_id: [id] }), text: 'open in the browser' })),
      groups(inEntry, 'target').map(([t, rows]) => h('section', {},
        h('div', { class: 'group-head' }, h('h3', {}, '→ ', entryLink(index, t), ' ', kindBadge(rows[0].target_kind)), h('span', { class: 'n', text: plural(rows.length, 'finding') })),
        rows.map((f) => findingCard(index, f, { route: false }))))) : null,
    about.length ? frag(
      h('div', { class: 'group-head' }, h('h2', { text: `Findings in other entries that target ${name}` }), h('span', { class: 'n', text: `${about.length} · ` }), h('a', { class: 'small', href: href('/findings', { target: [id] }), text: 'open in the browser' })),
      groups(about, 'source_id').map(([s, rows]) => h('section', {},
        h('div', { class: 'group-head' }, h('h3', {}, entryLink(index, s), ' ', kindBadge(rows[0].source_kind), ' →'), h('span', { class: 'n', text: plural(rows.length, 'finding') })),
        rows.map((f) => findingCard(index, f, { route: false }))))) : null);
}

function finding(index, source, id) {
  const f = index.byKey.get(`${source}/${id}`);
  if (!f) return h('p', { class: 'error', text: `No finding ${source}/${id} in this export.` });
  return frag(
    h('div', { class: 'page-head' }, h('h1', { text: 'Finding and evidence' }), h('span', { class: 'muted small', text: `${f.source_id} · ${f.id}` })),
    h('p', {}, h('a', { href: '#/findings', text: 'Back to findings' })),
    findingCard(index, f, { open: true }),
    h('p', { class: 'small' }, 'From the entry ', entryLink(index, f.source_id), ' · paper ', h('a', { href: paperHref(f.citation), text: paperLabel(f.citation) })));
}

// ---------------------------------------------------------------------------
// Coverage: the screening register (SCREENING.md) — PRISMA 2020 flow,
// exclusion reasons, evidence-gap coverage, searches and the candidate table.
// Counts come from the export (export_webapp.screening, computed in Python);
// the page only draws them and lets each box open the candidates behind it.
// ---------------------------------------------------------------------------
const SVG_NS = 'http://www.w3.org/2000/svg';
function s(tag, attrs = {}, ...children) {
  const el = document.createElementNS(SVG_NS, tag);
  for (const [k, v] of Object.entries(attrs)) {
    if (v === null || v === undefined || v === false) continue;
    if (k === 'text') el.textContent = v;
    else if (k === 'href') el.setAttributeNS('http://www.w3.org/1999/xlink', 'href', v), el.setAttribute('href', v);
    else el.setAttribute(k, v === true ? '' : v);
  }
  for (const c of children.flat(Infinity)) if (c !== null && c !== undefined && c !== false) el.append(c instanceof Node ? c : document.createTextNode(String(c)));
  return el;
}

const coverageHref = (params = {}) => href('/coverage', params);
const LICENCE_TEXT = { cc: 'Creative Commons', cc_manuscript: 'CC (manuscript)', free_to_read: 'free to read', rights_reserved: 'rights reserved', unknown: 'not known' };
const LICENCE_TITLE = {
  cc: 'The published version is under a Creative Commons licence',
  cc_manuscript: 'Only the accepted manuscript is under a Creative Commons licence; the published version is not',
  free_to_read: 'A free copy exists, without an open licence',
  rights_reserved: 'Publisher terms: quoted here as short attributed passages only',
  unknown: 'No licence metadata found (screen.py licences)',
};
/** Link to the annotated PDF: public for Creative-Commons papers (served by the review portal's
 *  open path), otherwise a pointer to the portal, which needs a sign-in. */
function annotatedPdfLink(index, citation, page) {
  const local = index.kb.localAnnotatedPdfs?.[citation];
  if (local?.url?.startsWith('/pdfs/')) return h('a', { class: 'btn', href: `${local.url}${page ? `#page=${page}` : ''}`, target: '_blank', rel: 'noopener', text: 'Open annotated PDF', title: `Highlights from the local draft snapshot: ${local.snapshot || ''}` });
  const portal = index.kb.portal; const lic = index.kb.licences?.[citation];
  if (!portal?.url || !lic) return null;
  const key = String(citation || '').replace(/^@/, '');
  // Served openly only when the portal's index says this paper's copy is public (publicPdfs):
  // a cc_manuscript paper is private unless its file was confirmed as the open manuscript.
  const isPublic = Array.isArray(portal.publicPdfs) ? portal.publicPdfs.includes(citation) : (portal.publicCategories || []).includes(lic.category) && lic.category === 'cc';
  if (isPublic) {
    return h('a', { class: 'small', href: `${portal.publicPdfBase}${key}_annotated.pdf${page ? `#page=${page}` : ''}`, target: '_blank', rel: 'noopener', title: `Annotated PDF (${lic.label || lic.category}) — the highlights are this entry's passages`, text: 'annotated PDF' });
  }
  const why = lic.category === 'free_to_read' ? 'free to read but not openly licensed' : lic.category === 'rights_reserved' ? 'rights reserved by the publisher'
    : lic.category === 'cc_manuscript' ? 'only the accepted manuscript is openly licensed' : lic.category === 'cc' ? 'not yet published openly' : 'licence not known';
  return h('a', { class: 'small muted', href: `${portal.url}/#/drafts`, target: '_blank', rel: 'noopener', title: `No public copy: ${why}. The annotated PDF is in the review portal, for signed-in reviewers.`, text: `annotated PDF (reviewers only: ${why})` });
}

function licenceBadge(rec) {
  if (!rec) return h('span', { class: 'muted small', text: '—' });
  const c = rec.category || 'unknown';
  const label = c === 'cc' || c === 'cc_manuscript' ? (rec.label || LICENCE_TEXT[c]) : LICENCE_TEXT[c] || c;
  return h('span', { class: `badge badge-licence badge-licence-${c}`, title: `${LICENCE_TITLE[c] || ''}${rec.label && rec.label !== label ? ` — ${rec.label}` : ''}${rec.source ? ` (from ${rec.source})` : ''}`, text: label });
}
const stageBadge = (stage) => h('span', { class: `badge badge-stage badge-stage-${stage}`, title: STAGE_TEXT[stage] || stage, text: STAGE_TEXT[stage] || String(stage || '').replace(/_/g, ' ') });
const kbBadge = (state) => h('span', { class: `badge badge-kb badge-kb-${String(state).replace(/\s+/g, '-')}`, text: KB_STATE_TEXT[state] || String(state || '').replace(/_/g, ' ') });

/** The PRISMA 2020 flow as one SVG. Every box links to the candidates it counts. */
function prismaDiagram(index, { identificationOnly = false } = {}) {
  const p = index.screening.prisma;
  if (!p) return null;
  const idn = p.identification; const db = p.screening; const ot = p.other; const inc = p.included;
  const W = 950; const colL = 48; const colR = 498; const main = 250; const side = 170; const gapX = 20; const boxH = 54; const rowGap = 34;
  const rows = [];
  let y = 24;
  const nodes = [];
  const lines = [];
  const text = (x, yy, t, cls = '') => s('text', { x, y: yy, class: `pr-text ${cls}` }, t);
  const fit = (t, w, px) => { const max = Math.max(4, Math.floor(w / px)); return String(t).length > max ? `${String(t).slice(0, max - 1)}…` : String(t); };
  const wrapLabels = (labels, w) => (labels || []).flatMap(label => {
    const max = Math.max(12, Math.floor((w - 20) / 5.5));
    const wrapped = []; let line = '';
    for (const word of String(label).split(/\s+/)) {
      if (line && `${line} ${word}`.length > max) { wrapped.push(line); line = word; }
      else line += `${line ? ' ' : ''}${word}`;
    }
    if (line) wrapped.push(line);
    return wrapped;
  });
  const contentHeight = (labels, w) => boxH + wrapLabels(labels, w).length * 16;
  const box = ({ x, y: yy, w, title, n, sub, link, cls = '', params = null, id = null, tip = null, height = boxH, breakdown = null }) => {
    // Publish initial search totals without implying downstream decisions.
    if (identificationOnly && title !== 'Records from databases' && !(id === 'removed' && Number.isFinite(idn.duplicatesRemoved))) {
      n = null; sub = null; link = null; params = null; breakdown = null;
    }
    if (identificationOnly && id === 'removed') { params = null; link = null; }
    const subLines = Array.isArray(sub) ? wrapLabels(sub, w) : [];
    height = Math.max(height, boxH + subLines.length * 16);
    if (params && id) link = coverageHref({ ...params, box: id });
    else if (link) link += `${link.includes('?') ? '&' : '?'}box=${encodeURIComponent(title)}`;
    const g = s('g', { class: `pr-box ${cls}` });
    g.append(s('rect', { x, y: yy, width: w, height, rx: 6 }));
    g.append(text(x + 10, yy + 20, fit(title, w - 16, 5.5), 'pr-title'));
    const line = text(x + 10, yy + 41, n == null ? '' : Number(n).toLocaleString(), 'pr-n');
    if (sub && !Array.isArray(sub)) line.append(s('tspan', { class: 'pr-sub', dx: 6 }, fit(sub, w - 24 - 9 * String(n).length, 5.4)));
    g.append(line);
    if (Array.isArray(sub)) subLines.forEach((label, i) => g.append(text(x + 10, yy + 60 + i * 16, label, 'pr-sub')));
    if (link) {
      const a = s('a', { href: link, class: 'pr-link' });
      if (params && cls.includes('pr-out')) {
        a.addEventListener('mouseenter', (e) => showTip(e, index, title, params, breakdown));
        a.addEventListener('mousemove', moveTip);
        a.addEventListener('mouseleave', hideTip);
        a.setAttribute('tabindex', '0');
        a.addEventListener('focus', () => { const r = a.getBoundingClientRect(); showTip({ clientX: r.left, clientY: r.bottom }, index, title, params, breakdown); });
        a.addEventListener('blur', hideTip);
      } else a.append(s('title', { text: `${title}: ${n}${sub ? ` (${sub})` : ''}${tip ? `\n${tip}` : ''}\n— click to open these candidates` }));
      a.append(g);
      return a;
    }
    return g;
  };
  const arrowV = (x, y1, y2) => lines.push(s('line', { x1: x, y1, x2: x, y2, class: 'pr-arrow', 'marker-end': 'url(#pr-head)' }));
  const arrowH = (x1, x2, yy) => lines.push(s('line', { x1, y1: yy, x2, y2: yy, class: 'pr-arrow', 'marker-end': 'url(#pr-head)' }));
  const label = (yy, t) => nodes.push(s('text', { x: 22, y: yy, class: 'pr-phase', 'text-anchor': 'middle', transform: `rotate(-90 22 ${yy})` }, t));
  const dbStages = ['awaiting_ta', 'unsure_ta', 'excluded_ta', 'awaiting_ft', 'unsure_ft', 'not_retrieved', 'excluded_ft', 'included'];
  const soughtStages = ['awaiting_ft', 'unsure_ft', 'not_retrieved', 'excluded_ft', 'included'];
  const fmtReasons = (obj) => Object.entries(obj || {}).map(([k, v]) => `${index.screening.reasonLabel(k)}: ${v.toLocaleString()}`);
  const taReasons = fmtReasons(db.excludedTitleAbstractReasons);
  const ftReasons = fmtReasons(db.excludedFullTextReasons);
  const otherReasons = fmtReasons(ot.excludedFullTextReasons);

  // Identification
  const dbSub = Object.entries(idn.databases.byDatabase || {}).map(([k, v]) => `${DATABASE_NAMES[k] || k}: ${v.toLocaleString()}`);
  const sourceLabels = { citation_chasing: 'Found in reference lists', gap_analysis: 'Suggested by gap analysis', hand_picked: 'Selected by a researcher', registered: 'Added from local PDFs', seed: 'Initial reference set' };
  const otSub = Object.entries(idn.other.byKind || {}).map(([k, v]) => `${sourceLabels[k] || index.screening.sourceKinds[k] || k}: ${v.toLocaleString()}`);
  const identificationH = Math.max(contentHeight(dbSub, main), contentHeight(otSub, main + gapX + side), boxH + 3 * 16);
  const sideX = (col) => col + main + gapX;
  // row 0
  // hover: how many records each question's searches brought in (search hits, before de-duplication)
  const byQuestion = {};
  for (const sx of index.screening.searches.values()) for (const q of sx.for || []) byQuestion[q] = (byQuestion[q] || 0) + Number(sx.hits ?? sx.retrieved ?? 0);
  const qTip = Object.keys(byQuestion).length ? 'By question (search hits, before de-duplication):\n' + Object.entries(byQuestion).sort((a, b) => b[1] - a[1]).map(([q, v]) => `  ${q.replace(/_/g, ' ')}: ${v.toLocaleString()}`).join('\n') : null;
  nodes.push(box({ x: colL, y, w: main, title: 'Records from databases', n: idn.databases.records, sub: dbSub, link: coverageHref({ arm: 'databases' }), tip: qTip, height: identificationH }));
  const preprints = idn.preprintsSuperseded || 0;
  const removedSub = identificationOnly ? ['Duplicate records'] : [`Other duplicates: ${(idn.duplicatesRemoved - preprints).toLocaleString()}`, `Preprint → published: ${preprints.toLocaleString()}`, `Grey literature: ${(idn.removedByRule || 0).toLocaleString()}`];
  nodes.push(box({ x: sideX(colL), y, w: side, title: 'Removed before screening', n: idn.duplicatesRemoved + (idn.removedByRule || 0), sub: removedSub, params: { stage: 'duplicate' }, id: 'removed', cls: 'pr-side pr-out', height: identificationH }));
  nodes.push(box({ x: colR, y, w: main + gapX + side, title: 'Records from other sources', n: idn.other.records, sub: otSub, height: identificationH, link: coverageHref({ arm: 'other' }) }));
  arrowH(colL + main, sideX(colL), y + boxH / 2);
  rows.push(y);
  y += identificationH + rowGap;
  // row 1
  nodes.push(box({ x: colL, y, w: main, title: 'Records screened (title/abstract)', n: db.screened, sub: db.awaitingTitleAbstract ? `${db.awaitingTitleAbstract} awaiting` : null, link: coverageHref({ arm: 'databases', stage: dbStages }) }));
  nodes.push(box({ x: sideX(colL), y, w: side, title: 'Excluded at title/abstract', n: db.excludedTitleAbstract, breakdown: taReasons, params: { arm: 'databases', stage: 'excluded_ta' }, id: 'excluded_ta', cls: 'pr-side pr-out' }));
  nodes.push(box({ x: colR, y, w: main, title: 'Reports sought for retrieval', n: ot.sought, link: coverageHref({ arm: 'other', stage: dbStages }) }));
  nodes.push(box({ x: sideX(colR), y, w: side, title: 'Not retrieved', n: ot.notRetrieved, params: { arm: 'other', stage: 'not_retrieved' }, id: 'other_not_retrieved', cls: 'pr-side pr-out' }));
  arrowV(colL + main / 2, rows[0] + identificationH, y); arrowV(colR + main / 2, rows[0] + identificationH, y);
  arrowH(colL + main, sideX(colL), y + boxH / 2); arrowH(colR + main, sideX(colR), y + boxH / 2);
  rows.push(y);
  y += boxH + rowGap;
  // row 2
  nodes.push(box({ x: colL, y, w: main, title: 'Reports sought for retrieval', n: db.sought, link: coverageHref({ arm: 'databases', stage: soughtStages }) }));
  nodes.push(box({ x: sideX(colL), y, w: side, title: 'Not retrieved', n: db.notRetrieved, params: { arm: 'databases', stage: 'not_retrieved' }, id: 'db_not_retrieved', cls: 'pr-side pr-out' }));
  nodes.push(box({ x: colR, y, w: main, title: 'Reports assessed for eligibility', n: ot.assessed, sub: (ot.awaitingFullText + ot.unsureFullText) ? `${ot.awaitingFullText + ot.unsureFullText} awaiting decision` : null, link: coverageHref({ arm: 'other', stage: ['excluded_ft', 'included', 'awaiting_ft', 'unsure_ft', 'awaiting_ta', 'unsure_ta', 'excluded_ta'] }) }));
  nodes.push(box({ x: sideX(colR), y, w: side, title: 'Excluded', n: ot.excludedFullText, breakdown: otherReasons, params: { arm: 'other', stage: ['excluded_ft', 'excluded_ta'] }, id: 'other_excluded', cls: 'pr-side pr-out' }));
  arrowV(colL + main / 2, rows[1] + boxH, y); arrowV(colR + main / 2, rows[1] + boxH, y);
  arrowH(colL + main, sideX(colL), y + boxH / 2); arrowH(colR + main, sideX(colR), y + boxH / 2);
  rows.push(y);
  y += boxH + rowGap;
  // row 3 (databases arm only)
  nodes.push(box({ x: colL, y, w: main, title: 'Reports assessed for eligibility', n: db.assessed, sub: (db.awaitingFullText + db.unsureFullText) ? `${db.awaitingFullText + db.unsureFullText} awaiting decision` : null, link: coverageHref({ arm: 'databases', stage: ['excluded_ft', 'included', 'awaiting_ft', 'unsure_ft'] }) }));
  nodes.push(box({ x: sideX(colL), y, w: side, title: 'Excluded at full text', n: db.excludedFullText, breakdown: ftReasons, params: { arm: 'databases', stage: 'excluded_ft' }, id: 'excluded_ft', cls: 'pr-side pr-out' }));
  arrowV(colL + main / 2, rows[2] + boxH, y);
  arrowH(colL + main, sideX(colL), y + boxH / 2);
  rows.push(y);
  y += boxH + rowGap;
  // row 4: included (merged)
  const incX = (W - main) / 2;
  nodes.push(box({ x: incX, y, w: main, title: 'Papers included', n: inc.total, sub: `${inc.approvedFindings} approved findings`, link: coverageHref({ stage: 'included' }), cls: 'pr-included' }));
  lines.push(s('path', { d: `M${colL + main / 2} ${rows[3] + boxH} V${y - 14} H${incX + main / 2} V${y}`, class: 'pr-arrow', 'marker-end': 'url(#pr-head)', fill: 'none' }));
  lines.push(s('path', { d: `M${colR + main / 2} ${rows[2] + boxH} V${y - 14} H${incX + main / 2}`, class: 'pr-arrow', fill: 'none' }));
  rows.push(y);
  y += boxH + rowGap + 12;
  // row 5: where included papers stand in the knowledge base
  const kbStates = [['no_pdf', 'No PDF yet'], ['awaiting_extraction', 'Awaiting extraction'], ['in_review', 'In review'], ['in_kb', 'In the KB'], ['rejected', 'Rejected'], ['refused', 'Refused']];
  const kbW = 136; const kbGap = 12; const kbX0 = (W - (kbStates.length * kbW + (kbStates.length - 1) * kbGap)) / 2;
  lines.push(s('line', { x1: kbX0 + kbW / 2, y1: rows[4] + boxH + 18, x2: kbX0 + (kbStates.length - 1) * (kbW + kbGap) + kbW / 2, y2: rows[4] + boxH + 18, class: 'pr-arrow pr-bus' }));
  lines.push(s('line', { x1: incX + main / 2, y1: rows[4] + boxH, x2: incX + main / 2, y2: rows[4] + boxH + 18, class: 'pr-arrow pr-bus' }));
  kbStates.forEach(([st, title], i) => {
    const x = kbX0 + i * (kbW + kbGap);
    nodes.push(box({ x, y, w: kbW, title, n: inc.kb?.[st] ?? 0, params: { stage: 'included', kb: st }, id: `kb_${st}`, cls: st === 'in_kb' ? 'pr-kb pr-included' : st === 'rejected' || st === 'refused' ? 'pr-kb pr-out' : 'pr-kb' }));
    arrowV(x + kbW / 2, rows[4] + boxH + 18, y);
  });
  y += boxH + 16;
  label(rows[0] + boxH / 2, 'Identification'); label(rows[2] + boxH / 2, 'Screening'); label(y - 16 - boxH / 2, 'Knowledge base');

  const svg = s('svg', { viewBox: `0 0 ${W} ${y}`, class: 'prisma', role: 'img', 'aria-label': 'PRISMA 2020 flow diagram of the screening register' });
  svg.append(s('defs', {}, s('marker', { id: 'pr-head', viewBox: '0 0 10 10', refX: 9, refY: 5, markerWidth: 7, markerHeight: 7, orient: 'auto-start-reverse' }, s('path', { d: 'M0 0 L10 5 L0 10 z', class: 'pr-head' }))));
  svg.append(...lines, ...nodes);
  return svg;
}

// The papers behind a PRISMA box: who (author, year), what, and why they left.
const boxFilter = (params) => Object.fromEntries(Object.entries(params).map(([k, v]) => [k, Array.isArray(v) ? v : [v]]));
const boxRows = (index, params) => index.screening.candidates.filter((c) => matches(c, boxFilter(params), ''));
function whyText(index, c) {
  const sc = index.screening;
  if (c.stage === 'duplicate') return c.duplicate?.kind === 'preprint_published' ? `Preprint superseded by published article ${c.duplicate_of}` : `Duplicate of ${c.duplicate_of || '?'}`;
  if (c.stage === 'included') return KB_STATE_TEXT[c.kb] || c.kb;
  const d = sc.lastDecision(c);
  const r = c.reason && c.reason !== 'not excluded' ? sc.reasonLabel(c.reason) : (d ? d.decision : STAGE_TEXT[c.stage] || c.stage);
  return d?.note ? `${r} — ${d.note}` : r;
}
function tipEl() {
  let t = document.getElementById('prtip');
  if (!t) { t = h('div', { id: 'prtip', class: 'prtip', role: 'tooltip' }); document.body.append(t); }
  return t;
}
function showTip(e, index, title, params, breakdown = null) {
  const sc = index.screening;
  const rows = boxRows(index, params);
  const idn = sc.prisma?.identification || {};
  const t = tipEl();
  const extra = params.stage === 'duplicate'
    ? [`${idn.duplicatesRemoved ?? 0} duplicates merged on import and after; ${idn.removedByRule || 0} grey-literature records removed by rule (${Object.entries(idn.removedByRuleTypes || {}).map(([k, v]) => `${k} ${v}`).join(', ') || 'none'}). Counted, not listed.`] : [];
  t.replaceChildren(h('b', { text: title }),
    breakdown ? h('ul', {}, breakdown.length ? breakdown.map(text => h('li', { text })) : h('li', { text: 'No exclusions' })) : rows.length ? h('ul', {}, rows.slice(0, 12).map((c) => h('li', {}, h('span', { class: 'ay', text: sc.authorYear(c) }), ' — ', h('span', { text: whyText(index, c) })))) : (extra.length ? '' : h('p', { class: 'muted', text: 'No paper listed here.' })),
    ...extra.map((x) => h('p', { class: 'small muted', text: x })),
    !breakdown && rows.length > 12 ? h('p', { class: 'small muted', text: `+${rows.length - 12} more — click for the full list` }) : rows.length ? h('p', { class: 'small muted', text: 'Click for the list with titles' }) : '');
  t.classList.add('on'); moveTip(e);
}
function moveTip(e) {
  const t = tipEl(); const pad = 14;
  const x = Math.min(e.clientX + pad, window.innerWidth - t.offsetWidth - 8);
  const y = e.clientY + pad + t.offsetHeight > window.innerHeight ? e.clientY - t.offsetHeight - pad : e.clientY + pad;
  t.style.left = `${Math.max(8, x)}px`; t.style.top = `${Math.max(8, y)}px`;
}
function hideTip() { document.getElementById('prtip')?.classList.remove('on'); }

const BOX_TITLES = { removed: 'Removed before screening', excluded_ta: 'Excluded at title/abstract', excluded_ft: 'Excluded at full text',
  other_excluded: 'Other sources: excluded', db_not_retrieved: 'Full text not retrieved', other_not_retrieved: 'Other sources: not retrieved' };
function boxPanel(index, route, rows) {
  const id = route.params.get('box') || (route.params.get('arm') === 'databases' && !route.params.has('stage') ? 'Records from databases' : route.params.get('arm') === 'other' && !route.params.has('stage') ? 'Records from other sources' : null);
  if (!id) return null;
  hideTip();
  const sc = index.screening;
  const title = BOX_TITLES[id] || (id.startsWith('kb_') ? `Included — ${KB_STATE_TEXT[id.slice(3)] || id.slice(3)}` : id);
  const idn = sc.prisma?.identification || {};
  return h('section', { id: 'boxlist', class: 'panel box-panel' },
    h('div', { class: 'results-head' }, h('h2', { text: `${title}: ${rows.length} paper${rows.length === 1 ? '' : 's'} listed` }),
      h('a', { class: 'small', href: '#/coverage', text: 'close ×' })),
    id === 'Records from databases' ? h('div', {},
      h('p', { text: `${(idn.databases?.records || 0).toLocaleString()} database records were retrieved before duplicates were removed. The table below lists the matching records available in this public export; it does not contain every search hit.` }),
      h('p', {}, h('a', { href: '#/searches', text: 'Questions, exact search terms and counts by database →' }))) : null,
    (sc.omitted.awaitingTitleAbstract || sc.omitted.removedByRule) && id !== 'removed' ? h('p', { class: 'small muted', text: 'Records still awaiting title/abstract screening and records removed by the grey-literature rule are counted in the flow but omitted from the public paper list.' }) : null,
    !rows.length ? h('p', { text: 'No matching papers are listed in this public export.' }) : null,
    id === 'removed' ? h('p', { class: 'small muted', text: `This box counts ${(idn.duplicatesRemoved || 0) - (idn.preprintsSuperseded || 0)} other duplicates, ${idn.preprintsSuperseded || 0} preprints superseded by published articles, and ${idn.removedByRule || 0} grey-literature records. Preprints are a subset of the duplicate total, not an additional subtraction. Only duplicates linked after import are listed; both versions and earlier decisions are retained in the register.` }) : null,
    rows.length ? h('table', { class: 'cand-list box-list' },
      h('thead', {}, h('tr', {}, h('th', { text: 'Paper' }), h('th', { text: 'Title' }), h('th', { text: 'Why' }), h('th', { text: 'Decided' }))),
      h('tbody', {}, rows.slice(0, 400).map((c) => { const d = c.duplicate || sc.lastDecision(c); return h('tr', {},
        h('td', {}, c.key && (index.byPaper.has(c.key) || index.kb.citations?.[c.key]) ? h('a', { href: paperHref(c.key), text: sc.authorYear(c) }) : h('b', { text: sc.authorYear(c) }), h('div', { class: 'small muted', text: c.id })),
        h('td', {}, h('span', { text: c.title || '(no title)' }), c.doi ? h('div', { class: 'small' }, h('a', { href: `https://doi.org/${c.doi}`, rel: 'noopener', target: '_blank', text: c.doi })) : null),
        h('td', { text: whyText(index, c) }),
        h('td', { class: 'small muted', text: d ? `${d.by}${d.date ? ` · ${d.date}` : ''}` : '—' })); }))) : null,
    rows.length > 400 ? h('p', { class: 'small muted', text: `First 400 of ${rows.length}; the full list is in the Candidates table below.` }) : null);
}

// Plain-English explanations of recorded strategies; the search register remains authoritative.
const SEARCH_QUESTIONS = {
  q1_lesion_impairment: ['How is brain damage related to language difficulties after stroke?',
    'Looks for aphasia, stroke and brain imaging together, to find studies linking brain regions or connections to language difficulties.'],
  q1b_language_lesion_mapping: ['Where does brain damage affect reading, writing, speaking or understanding language?',
    'Looks for specific language skills alongside stroke and lesion mapping. This helps find papers that study language difficulties without using the word “aphasia”.'],
  q1c_cognition_prosody_lesion: ['How does stroke affect thinking skills and the rhythm or tone of speech?',
    'Combines two routes: cognitive skills with lesion–symptom mapping, or prosody (the rhythm, stress and tone of speech) with brain imaging. Both routes include stroke terms.'],
  q2b_therapy_response_neural: ['How are brain structure and activity related to the response to aphasia therapy?',
    'Looks for aphasia therapy alongside imaging or lesion evidence. The aim is to understand brain features associated with treatment response.'],
  q2c_therapy_response_patient_factors: ['Which personal or clinical characteristics are linked to the response to a particular aphasia therapy?',
    'Looks for treatment response alongside patient characteristics, such as demographic, clinical, cognitive, language or genetic factors. Imaging is not required for this question.'],
  q3_predictor_outcome: ['Which brain imaging findings are associated with aphasia severity or recovery after stroke?',
    'Looks for aphasia, stroke, predictors and imaging together. Studies may also consider clinical or demographic factors alongside the imaging findings.'],
  q4_synthesis: ['What do reviews tell us about aphasia, treatment and recovery?',
    'Looks for systematic reviews, scoping reviews and meta-analyses of aphasia. The additional route for narrative reviews requires stroke and brain imaging terms.'],
  q5_recruitment_meta: ['Which brain regions support language, according to imaging meta-analyses?',
    'Looks for language tasks, imaging and meta-analysis terms. This provides synthesis evidence about language networks, including work in people without stroke; individual healthy-volunteer studies do not enter through this search.'],
};
const DATABASE_NAMES = { pubmed: 'PubMed', scopus: 'Scopus', psycinfo: 'PsycINFO', embase: 'Embase', cinahl: 'CINAHL', wos: 'Web of Science', central: 'CENTRAL', cdsr: 'Cochrane Reviews', openalex: 'OpenAlex' };
function searchQuestions(index, route) {
  const searches = [...index.screening.searches.values()];
  const groups = new Map();
  for (const run of searches) {
    const key = run.strategy || run.id;
    if (!groups.has(key)) groups.set(key, []);
    groups.get(key).push(run);
  }
  const selected = route.params.get('q');
  const questionCode = key => key.startsWith('q') ? key.split('_')[0].replace(/^q/, 'Q') : key;
  const databases = [...new Set(searches.map(run => run.database))].sort((a, b) => (['pubmed', 'scopus', 'psycinfo'].indexOf(a) - ['pubmed', 'scopus', 'psycinfo'].indexOf(b)));
  const orderedGroups = [...groups.entries()].sort(([a], [b]) => { const order = Object.keys(SEARCH_QUESTIONS); return (order.includes(a) ? order.indexOf(a) : order.length) - (order.includes(b) ? order.indexOf(b) : order.length); });
  const retrievedCount = runs => !runs.length ? '—' : runs.some(run => run.retrieved == null) ? 'Not recorded' : runs.reduce((total, run) => total + Number(run.retrieved), 0).toLocaleString();
  const countTable = h('div', { class: 'table-wrap' }, h('table', { class: 'search-counts' },
    h('caption', { text: 'Records retrieved (N), before removing duplicates within or between searches' }),
    h('thead', {}, h('tr', {}, h('th', { scope: 'col', text: 'Question' }), databases.map(db => h('th', { scope: 'col', class: 'num', text: DATABASE_NAMES[db] || db })), h('th', { scope: 'col', class: 'num', text: 'Total' }))),
    h('tbody', {}, orderedGroups.map(([key, runs]) => h('tr', {},
      h('th', { scope: 'row' }, h('a', { href: `#/searches?q=${encodeURIComponent(key)}`, text: `${questionCode(key)} · ${SEARCH_QUESTIONS[key]?.[0] || key}` })),
      databases.map(db => h('td', { class: 'num', text: retrievedCount(runs.filter(run => run.database === db)) })), h('td', { class: 'num', text: retrievedCount(runs) })))),
    h('tfoot', {}, h('tr', {}, h('th', { scope: 'row', text: 'All recorded searches' }), databases.map(db => h('td', { class: 'num', text: retrievedCount(searches.filter(run => run.database === db)) })), h('td', { class: 'num', text: retrievedCount(searches) })))));

  const filterText = run => Object.entries(run.filters || {}).map(([key, value]) => `${key}: ${value}`).join(' · ') || 'No filters recorded';
  const download = () => {
    const text = ['Stroke aphasia KB — recorded database searches',
      'Plain-English questions explain the search purpose; exact queries below are unchanged from the search register.',
      ...searches.map(run => [
        `\n${run.id} — ${DATABASE_NAMES[run.database] || run.database} — ${run.date || 'date not recorded'}`,
        `Strategy: ${run.strategy || 'not recorded'}`,
        `Question ${questionCode(run.strategy || run.id)}: ${SEARCH_QUESTIONS[run.strategy]?.[0] || 'See the recorded query'}`,
        `Filters: ${filterText(run)}`, `Hits: ${run.hits ?? 'not recorded'}; retrieved: ${run.retrieved ?? 'not recorded'}`,
        `Run by: ${run.run_by || 'not recorded'}`,
        `Protocol version: ${run.protocol?.version ?? 'not recorded'}; fingerprint: ${run.protocol?.fingerprint || 'not recorded'}; commit: ${run.protocol?.commit || 'not recorded'}`,
        run.query || 'No query recorded',
      ].join('\n'))].join('\n\n');
    const url = URL.createObjectURL(new Blob([text], { type: 'text/plain;charset=utf-8' }));
    const a = h('a', { href: url, download: 'aphasia-kb-database-searches.txt' });
    document.body.append(a); a.click(); a.remove(); setTimeout(() => URL.revokeObjectURL(url), 1000);
  };
  return h('div', { class: 'editorial-page search-guide' },
    h('p', { class: 'eyebrow', text: 'How we find the literature' }),
    h('h1', { text: 'The questions behind our searches' }),
    h('p', { class: 'lead', text: 'These questions explain what we looked for. Open a question’s search records to see the original terms, dates and filters.' }),
    h('p', {}, `${searches.length} recorded searches · ${groups.size} question areas. `,
      h('a', { href: '#/coverage', text: 'Back to the screening flow →' })),
    h('p', { class: 'small', text: 'Question labels follow the search protocol. Counts below are retrieved records before removing duplicates; the same paper can appear in several questions or databases. Screening decides which papers belong in the KB.' }),
    h('div', { class: 'editorial-actions' },
      h('button', { class: 'btn', type: 'button', onclick: download, text: 'Download all questions and exact searches' }),
      h('a', { href: 'https://github.com/micmas/stroke-aphasia-kb/blob/main/docs/SCREENING.md', text: 'Read the screening protocol' })),
    selected ? h('p', {}, h('a', { href: '#/searches', text: 'Show all search questions' })) : null,
    selected && !groups.has(selected) ? h('p', { class: 'notice', text: 'No recorded search matches this question.' }) : null,
    !selected ? h('section', { class: 'search-count-summary' }, h('h2', { text: 'Records by question and database' }), countTable) : null,
    orderedGroups.filter(([key]) => !selected || selected === key).map(([key, runs]) => {
      const [question, explanation] = SEARCH_QUESTIONS[key] || ['What does this recorded search look for?', 'This search has no plain-English summary yet. Its original query is available below.'];
      return h('section', { class: 'search-question' },
        h('p', { class: 'eyebrow', text: `Question ${questionCode(key)}` }),
        h('h2', { text: question }), h('p', { text: explanation }),
        h('p', { class: 'small muted' }, databases.filter(db => runs.some(run => run.database === db)).map(db => `${DATABASE_NAMES[db] || db}: ${retrievedCount(runs.filter(run => run.database === db))}`).join(' · '),
          ' · ', h('a', { href: `#/searches?q=${encodeURIComponent(key)}`, text: 'Link to this question' })),
        h('details', {}, h('summary', { text: `Exact search terms and records (${runs.length})` }),
          runs.map(run => h('section', { class: 'search-run' },
            h('h3', { text: `${DATABASE_NAMES[run.database] || run.database} · ${run.id} · ${run.date || 'date not recorded'}` }),
            h('p', { class: 'small', text: `${filterText(run)} · ${run.hits ?? '?'} hits · ${run.retrieved ?? '?'} retrieved · run by ${run.run_by || 'not recorded'}` }),
            h('pre', { class: 'search-query', tabindex: '0', 'aria-label': `Exact query for ${run.id}` }, h('code', { text: run.query || 'No query recorded' })),
            h('p', { class: 'small muted', text: `Strategy: ${key}. Protocol version ${run.protocol?.version ?? '?'} · fingerprint ${run.protocol?.fingerprint || '?'} · commit ${run.protocol?.commit || '?'}.` }),
            run.file ? h('p', { class: 'small muted', text: `Imported from ${run.file}` }) : null,
            h('a', { href: coverageHref({ search: run.id }), text: `See listed records from ${run.id} →` })))));
    }),
    h('details', { class: 'editorial-details' }, h('summary', { text: 'How to read the database terms' }),
      h('ul', {},
        h('li', { text: 'OR groups alternatives: any of the listed words can match.' }),
        h('li', { text: 'AND joins concepts: the record must match both groups.' }),
        h('li', { text: 'An asterisk (*) allows word endings. Quotation marks group phrases; the exact behaviour depends on the database.' }),
        h('li', { text: 'Field labels tell a database where to search. For example, PubMed [tiab] means title or abstract and [Mesh] means a subject heading. Scopus uses TITLE-ABS-KEY; PsycINFO uses labels such as TI (title), AB (abstract) and DE (subject heading).' }))),
    h('p', { class: 'small muted' }, 'This page lists searches recorded as run, with their original strings and filters. The ',
      h('a', { href: 'https://github.com/micmas/stroke-aphasia-kb/blob/main/screening/strategies.yaml', text: 'strategy file' }),
      ' also contains additional targeted searches; a planned strategy is not evidence that a search was run. ',
      h('a', { href: 'https://github.com/micmas/stroke-aphasia-kb/blob/main/screening/searches.yaml', text: 'View the full search register' }), '.'));
}

function coverage(index, route) {
  const sc = index.screening;
  if (!sc.present) {
    return frag(h('div', { class: 'page-head' }, h('h1', { text: 'Coverage' })),
      h('p', { class: 'notice', text: 'This export carries no screening register. Run `python scripts/screen.py backfill --execute` (and searches), regenerate the export, and this view shows the PRISMA flow and what each evidence gap still needs.' }));
  }
  const filters = route.filters;
  const query = route.params.get('q') || '';
  const sort = route.params.get('sort') || 'register';
  const counts = facetCounts(sc.candidates, filters, query, SCREENING_FACETS);
  let rows = sc.candidates.filter((c) => matches(c, filters, query));
  if (sort === 'year') rows = rows.slice().sort((a, b) => (b.year || 0) - (a.year || 0) || a.ordinal - b.ordinal);
  else if (sort === 'title') rows = rows.slice().sort((a, b) => String(a.title || '').localeCompare(String(b.title || '')));
  else if (sort === 'decided') rows = rows.slice().sort((a, b) => String(b.decided_on || '').localeCompare(String(a.decided_on || '')) || a.ordinal - b.ordinal);
  const go = (next, params = {}) => { location.hash = coverageHref({ ...next, q: query, sort, ...params }); };
  const toggle = (key, value) => { const cur = new Set(filters[key] || []); if (cur.has(value)) cur.delete(value); else cur.add(value); go({ ...filters, [key]: [...cur] }); };
  const valueLabel = (key, v) => (key === 'stage' ? STAGE_TEXT[v] || v : key === 'kb' ? KB_STATE_TEXT[v] || v : key === 'arm' ? ARM_TEXT[v] || v : key === 'reason' ? (v === 'not excluded' ? v : sc.reasonLabel(v)) : key === 'database' ? (DATABASE_NAMES[v] || v) : key === 'origin' ? (sc.sourceKinds[v] || String(v).replace(/_/g, ' ')) : key === 'search' ? (sc.searches.get(v) ? `${v} · ${DATABASE_NAMES[sc.searches.get(v).database] || sc.searches.get(v).database}` : v) : String(v).replace(/_/g, ' '));
  const anyFilter = Object.values(filters).some((v) => v?.length) || query;

  const facetNodes = SCREENING_FACETS.map((facet) => {
    const m = counts[facet.key];
    let values = [...m.keys()];
    if (facet.order) values.sort((a, b) => (facet.order.indexOf(a) === -1 ? 99 : facet.order.indexOf(a)) - (facet.order.indexOf(b) === -1 ? 99 : facet.order.indexOf(b)));
    else values.sort((a, b) => (m.get(b) - m.get(a)) || String(a).localeCompare(String(b)));
    const selected = new Set(filters[facet.key] || []);
    const many = values.length > 12;
    const shown = many ? values.filter((v, i) => i < 10 || selected.has(v)) : values;
    return h('details', { class: 'facet', open: selected.size || ['stage', 'kb', 'arm'].includes(facet.key) ? '' : null },
      h('summary', { text: `${facet.label}${selected.size ? ` (${selected.size})` : ''}` }),
      shown.map((v) => h('label', { class: m.get(v) ? '' : 'zero' },
        h('input', { type: 'checkbox', checked: selected.has(v) ? '' : null, onchange: () => toggle(facet.key, v) }),
        h('span', { text: valueLabel(facet.key, v), title: String(v) }),
        h('span', { class: 'n', text: String(m.get(v) || 0) }))),
      many && shown.length < values.length ? h('p', { class: 'small muted', text: `${values.length - shown.length} more — narrow with the search box` }) : null);
  });
  const active = Object.entries(filters).flatMap(([k, vs]) => vs.map((v) => h('button', { type: 'button', onclick: () => toggle(k, v), text: `${SCREENING_FACETS.find((f) => f.key === k)?.label || k}: ${valueLabel(k, v)} ×` })));
  if (query) active.push(h('button', { type: 'button', onclick: () => go(filters, { q: '' }), text: `search: ${query} ×` }));
  if (active.length) active.push(h('button', { type: 'button', onclick: () => { location.hash = '#/coverage'; }, text: 'clear all' }));
  const search = h('input', { class: 'search', type: 'search', placeholder: 'Search titles, keys, DOIs, entries…', value: query, 'aria-label': 'Search candidates' });
  let timer = null;
  search.addEventListener('input', () => { clearTimeout(timer); timer = setTimeout(() => go(filters, { q: search.value.trim() }), 250); });

  const p = sc.prisma;
  const inc = p?.included || { total: 0, kb: {}, approvedFindings: 0 };
  const decided = sc.candidates.filter((c) => !['awaiting_ta', 'awaiting_ft', 'unsure_ta', 'unsure_ft', 'duplicate'].includes(c.stage)).length;
  const awaiting = sc.candidates.filter((c) => ['awaiting_ta', 'awaiting_ft', 'unsure_ta', 'unsure_ft'].includes(c.stage)).length;
  const excludedReasons = new Map();
  for (const c of sc.candidates) if (['excluded_ta', 'excluded_ft', 'not_retrieved'].includes(c.stage)) excludedReasons.set(c.reason, (excludedReasons.get(c.reason) || 0) + 1);

  const candidateRow = (c) => {
    const paperKnown = c.key && (index.byPaper.has(c.key) || index.kb.citations?.[c.key]);
    return h('tr', {},
      h('td', {}, h('span', { class: 'chip', text: c.id })),
      h('td', {},
        paperKnown ? h('a', { href: paperHref(c.key), text: c.key }) : c.key ? h('span', { class: 'chip', text: c.key }) : null,
        h('div', { class: 'cand-title', text: c.title || '(no title)' }),
        h('div', { class: 'small muted' }, [c.first_author ? `${c.first_author}${c.year ? ` ${c.year}` : ''}` : (c.year ? String(c.year) : ''), c.journal, c.doi ? h('a', { href: `https://doi.org/${c.doi}`, rel: 'noopener', target: '_blank', text: c.doi }) : null].filter(Boolean).flatMap((x, i) => (i ? [' · ', x] : [x])))),
      h('td', { class: 'small' }, (c.sources || []).map((src, i) => [i ? h('br') : null, src.search ? h('a', { href: coverageHref({ search: src.search }), text: `${src.search}${sc.searches.get(src.search) ? ` ${DATABASE_NAMES[sc.searches.get(src.search).database] || sc.searches.get(src.search).database}` : ''}` }) : h('span', { text: sc.sourceKinds[src.kind] || src.kind })])),
      h('td', {}, stageBadge(c.stage), c.stage !== 'included' && c.reason && c.reason !== 'not excluded' ? h('div', { class: 'small muted', text: sc.reasonLabel(c.reason) }) : null,
        c.suggestion && ['awaiting_ta', 'unsure_ta'].includes(c.stage) ? h('div', { class: 'small muted', title: `${c.suggestion.model} suggested ${c.suggestion.decision}${c.suggestion.reason && c.suggestion.reason !== 'none' ? ` (${sc.reasonLabel(c.suggestion.reason)})` : ''}; a suggestion, not a decision`, text: `model suggests: ${c.suggestion.decision}` }) : null),
      h('td', {}, c.kbInfo ? frag(kbBadge(c.kb), c.kbInfo.approved_findings ? h('div', { class: 'small muted', text: `${plural(c.kbInfo.approved_findings, 'approved finding')}` }) : c.kbInfo.drafts ? h('div', { class: 'small muted', text: `${plural(c.kbInfo.drafts, 'draft')}${c.kbInfo.draft_rejected ? `, ${c.kbInfo.draft_rejected} rejected` : ''}` }) : null) : h('span', { class: 'muted', text: '—' })),
      h('td', { class: 'small muted' }, c.decided_by && c.decided_by !== 'nobody yet' ? c.decided_by : '—', c.decided_on ? h('div', { text: c.decided_on }) : null));
  };
  const shown = rows.slice(0, state.shown);
  const table = h('table', { class: 'cand-list' },
    h('thead', {}, h('tr', {}, h('th', { text: 'Id' }), h('th', { text: 'Candidate' }), h('th', { text: 'Source' }), h('th', { text: 'Screening' }), h('th', { text: 'Knowledge base' }), h('th', { text: 'Decided' }))),
    h('tbody', {}, shown.map(candidateRow)));
  const more = rows.length > shown.length ? h('button', { class: 'btn btn-primary', type: 'button', onclick: () => { state.shown += PAGE; render(); }, text: `Show ${Math.min(PAGE, rows.length - shown.length)} more of ${rows.length}` }) : null;

  const gapRows = sc.coverage.filter((g) => g.kind || g.found);
  const gapTable = gapRows.length ? h('table', { class: 'gap-list' },
    h('thead', {}, h('tr', {}, h('th', { text: 'Evidence gap' }), h('th', { text: 'Kind' }), h('th', { text: 'Areas' }), h('th', { class: 'num', text: 'Searches' }), h('th', { class: 'num', text: 'Candidates' }), h('th', { class: 'num', text: 'Screened' }), h('th', { class: 'num', text: 'Included' }), h('th', { class: 'num', text: 'In the KB' }), h('th', { class: 'num', text: 'Findings' }))),
    h('tbody', {}, gapRows.map((g) => h('tr', {},
      h('td', {}, h('a', { href: coverageHref({ gap: g.id }), text: g.id.replace(/_/g, ' ') }), g.need ? h('div', { class: 'small muted gap-need', text: g.need }) : null,
        g.suggested?.length ? h('div', { class: 'small' }, 'Suggested: ', g.suggested.map((k, i) => [i ? ', ' : '', index.kb.citations?.[k] || index.byPaper.has(k) ? h('a', { href: paperHref(k), text: paperLabel(k) }) : h('span', { class: 'chip', text: k })])) : null),
      h('td', {}, g.kind ? h('span', { class: `badge badge-gap-${g.kind}`, text: g.kind.replace(/_/g, ' ') }) : h('span', { class: 'muted', text: 'entry' })),
      h('td', { class: 'small' }, (g.areas || []).map((a, i) => [i ? ', ' : '', index.hasEntry(a) || index.byTarget.has(a) ? entryLink(index, a) : h('span', { title: a, text: index.mapping.units?.[a]?.name || a.replace(/_/g, ' ') })])),
      h('td', { class: 'num', text: String(g.searches || 0) }), h('td', { class: 'num', text: String(g.found || 0) }), h('td', { class: 'num', text: String(g.screened || 0) }),
      h('td', { class: 'num', text: String(g.included || 0) }), h('td', { class: 'num' }, h('b', { text: String(g.in_kb || 0) })), h('td', { class: 'num', text: String(g.approved_findings || 0) }))))) : h('p', { class: 'muted', text: 'No evidence gaps are declared (atlas_mapping/evidence_gaps.yaml) and no search names what it serves.' });

  const searches = [...sc.searches.values()];


  return frag(
    h('div', { class: 'page-head' }, h('h1', { text: 'Coverage' }), h('span', { class: 'muted small', text: `${sc.candidates.length} candidates · ${searches.length} searches · ${inc.total} included · ${inc.kb?.in_kb ?? 0} in the knowledge base` })),
    h('p', { class: 'lead', text: 'Follow the papers from search results to screening decisions and findings in the knowledge base.' }),
    h('div', { class: 'tiles' },
      h('div', { class: 'tile' }, h('div', { class: 'value', text: String(sc.candidates.length + (sc.omitted.awaitingTitleAbstract || 0) + (sc.omitted.removedByRule || 0)) }), h('div', { class: 'label', text: 'candidate papers' }), h('div', { class: 'detail', text: `${p?.identification.databases.records ?? 0} database records · ${p?.identification.other.records ?? 0} from other sources` })),
      h('div', { class: 'tile' }, h('div', { class: 'value', text: String(decided) }), h('div', { class: 'label', text: 'screened' }), h('div', { class: 'detail', text: `${awaiting + (sc.omitted.awaitingTitleAbstract || 0)} awaiting a decision` })),
      h('div', { class: 'tile' }, h('div', { class: 'value', text: String(inc.total) }), h('div', { class: 'label', text: 'included' }), h('div', { class: 'detail', text: `${[...excludedReasons.values()].reduce((a, b) => a + b, 0)} excluded` })),
      h('div', { class: 'tile' }, h('div', { class: 'value', text: String(inc.kb?.in_kb ?? 0) }), h('div', { class: 'label', text: 'in the knowledge base' }), h('div', { class: 'detail', text: `${inc.approvedFindings} approved findings · ${inc.kb?.in_review ?? 0} in review` }))),
    h('h2', { text: 'Flow of papers (PRISMA 2020)' }),
    h('p', { class: 'small muted', text: 'Hover over a pink box (an exit) to see its papers: author, year and why. Click any box to list its papers with titles just below the diagram. The knowledge-base row shows where included papers stand in the extraction and review pipeline.' }),
    h('p', {}, h('a', { href: '#/searches', text: 'What did we search for? Questions in plain English and exact database terms →' })),
    h('div', { class: 'prisma-wrap' }, prismaDiagram(index)),
    boxPanel(index, route, rows),
    h('div', { class: 'grid-2' },
      h('section', {}, h('h2', { text: 'Why candidates were excluded' }),
        excludedReasons.size ? barList([...excludedReasons.entries()].map(([r, n]) => ({ id: r, n, label: sc.reasonLabel(r) })).sort((a, b) => b.n - a.n), { link: (x) => coverageHref({ reason: x.id }) }) : h('p', { class: 'muted', text: 'Nothing excluded yet.' }),
        h('p', { class: 'small muted', text: 'Reasons are the controlled vocabulary of SCREENING.md §2.' })),
      h('section', {}, h('h2', { text: 'Who decided' }),
        barList([...counts.decided_by.entries()].map(([k, n]) => ({ id: k, n, label: k, alt: k === 'legacy' || k === 'nobody yet' })).sort((a, b) => b.n - a.n), { link: (x) => coverageHref({ decided_by: x.id }) }),
        h('p', { class: 'small muted', text: 'Grey: legacy stamps (papers that pre-date the register) and candidates still awaiting a decision. A model only ever suggests.' }))),
    h('h2', { text: 'Coverage of the evidence gaps' }),
    h('p', { class: 'small', text: 'For each gap declared in atlas_mapping/evidence_gaps.yaml (and each entry a search was run for): how many candidates were found, screened and included, and how many are already in the knowledge base. A gap with candidates found but none in the KB is waiting on extraction or review; a gap with none found needs a search.' }),
    gapTable,
    h('h2', { text: 'Database searches' }),
    h('p', {}, h('a', { href: '#/searches', text: 'Read the search questions and exact database terms →' })),
    h('h2', { id: 'candidates', text: 'Candidates' }),
    sc.omitted.awaitingTitleAbstract || sc.omitted.removedByRule ? h('p', { class: 'small muted', text: `Listed: every candidate someone has decided on, and everything past title/abstract. Counted in the flow above but not listed: ${sc.omitted.awaitingTitleAbstract || 0} records awaiting title/abstract screening and ${sc.omitted.removedByRule || 0} grey-literature records removed by rule.` }) : null,
    h('div', { class: 'two-col' },
      h('aside', { class: 'facets', 'aria-label': 'Filters' }, search, facetNodes),
      h('section', {},
        h('div', { class: 'results-head' }, h('span', { class: 'count', text: `${rows.length} of ${sc.candidates.length}` }),
          h('label', { class: 'small muted' }, 'sort ', h('select', { onchange: (e) => go(filters, { sort: e.target.value }) },
            [['register', 'register order'], ['year', 'year, newest first'], ['title', 'title'], ['decided', 'decided, latest first']].map(([v, t]) => h('option', { value: v, selected: v === sort ? '' : null, text: t }))))),
        h('div', { class: 'active-filters' }, active),
        rows.length ? h('div', { class: 'cand-wrap' }, table) : h('p', { class: 'notice', text: anyFilter ? 'No candidate matches these filters.' : 'The register is empty.' }),
        more)));
}

/** The screening record of one paper, for the paper page. */
function screeningPanel(index, key) {
  const c = index.screening.byKey.get(key);
  if (!c) return null;
  const sc = index.screening;
  const steps = [];
  for (const src of c.sources || []) steps.push({ when: sc.searches.get(src.search)?.date || '', what: src.search ? `identified by search ${src.search} (${DATABASE_NAMES[sc.searches.get(src.search)?.database] || sc.searches.get(src.search)?.database || '?'})` : `identified: ${sc.sourceKinds[src.kind] || src.kind}` });
  for (const d of c.history || []) steps.push({ when: d.date || '', what: `${d.stage === 'title_abstract' ? 'title/abstract' : 'full text'}: ${d.decision}${d.reason ? ` — ${sc.reasonLabel(d.reason)}` : ''} (${d.by})`, legacy: d.by === 'legacy' });
  if (c.kbInfo) steps.push({ when: '', what: KB_STATE_TEXT[c.kb] || c.kb, kb: true });
  return h('section', { class: 'panel' },
    h('h3', {}, 'Screening record ', h('a', { class: 'small', href: coverageHref({ q: c.id }), text: c.id })),
    h('p', { class: 'small' }, stageBadge(c.stage), ' ', c.kbInfo ? kbBadge(c.kb) : null),
    h('ol', { class: 'timeline' }, steps.map((x) => h('li', { class: x.legacy ? 'legacy' : x.kb ? 'kb' : '' }, x.when ? h('span', { class: 'when', text: x.when }) : null, h('span', { text: x.what })))),
    c.history?.some((d) => d.by === 'legacy') ? h('p', { class: 'small muted', text: 'Legacy: this paper entered the bibliography before the screening register existed; the decision is inferred from its status there, not from a person screening it.' }) : null);
}

// ---------------------------------------------------------------------------
// Shell
// ---------------------------------------------------------------------------
function render() {
  const main = document.getElementById('main');
  const index = state.index;
  if (!index) return;
  const route = parseRoute();
  const [head, ...rest] = route.segments;
  let view; let current = '/';
  try {
    if (!head) view = overview(index);
    else if (head === 'topic') { view = topicOverview(index, route); current = '/'; }
    else if (head === 'findings') { view = browse(index, route); current = '/findings'; }
    else if (head === 'matrix') { view = matrix(index, route); current = '/matrix'; }
    else if (head === 'papers') { view = papers(index); current = '/papers'; }
    else if (head === 'licences') { view = licencesView(index, route); current = '/papers'; }
    else if (head === 'searches') { view = searchQuestions(index, route); current = '/coverage'; }
    else if (head === 'coverage') { view = coverage(index, route); current = '/coverage'; }
    else if (head === 'involve') { view = involve(index); current = '/involve'; }
    else if (head === 'models') { view = models(index); current = null; }   // reached from the Overview, not from the menu
    else if (head === 'paper' && rest[0]) { view = paper(index, rest[0]); current = '/papers'; }
    else if (head === 'entry' && rest[0]) { view = entry(index, rest[0]); current = null; }
    else if (head === 'finding' && rest[1]) { view = finding(index, rest[0], rest[1]); current = null; }
    else view = h('p', { class: 'error', text: `Unknown page: ${route.path}` });
  } catch (err) {
    console.error(err);
    view = h('p', { class: 'error', text: `This page could not be rendered: ${err.message}` });
  }
  main.replaceChildren(view);
  for (const a of document.querySelectorAll('.nav a')) {
    if (a.getAttribute('href') === `#${current}`) a.setAttribute('aria-current', 'page'); else a.removeAttribute('aria-current');
  }
  if (head === 'finding') window.scrollTo(0, 0);
  else if (location.hash.includes('#f-')) { /* anchors scroll via :target */ }
  else if (head === 'coverage' && (route.params.has('box') || route.params.has('arm') || route.params.has('search'))) (document.getElementById('boxlist') || document.getElementById('candidates'))?.scrollIntoView({ block: 'start' });
  else window.scrollTo(0, 0);
  const titleEntry = head === 'finding' ? index.byKey.get(`${rest[0]}/${rest[1]}`)?.source_id : rest[0];
  document.title = `${head ? `${head[0].toUpperCase()}${head.slice(1)}${rest[0] ? ` · ${index.name(titleEntry || rest[0])}` : ''} · ` : ''}Stroke aphasia KB`;
}

function setSource(label, local) {
  const badge = document.getElementById('sourceBadge');
  badge.textContent = label;
  badge.classList.toggle('local', Boolean(local));
  const v = state.index?.kb?.version || {};
  document.getElementById('footerVersion').textContent = `KB ${v.commit || 'uncommitted'} · digest ${v.contentDigest || '?'} · ${v.findings ?? state.index.findings.length} findings · exported ${v.exportedOn || '?'}`;
}

async function load(url) {
  const main = document.getElementById('main');
  main.replaceChildren(h('p', { class: 'loading', text: 'Loading the knowledge base…' }));
  try {
    const kb = JSON.parse(await loadExportText(url, { cache: 'no-cache' }));
    use(kb, url.replace(/^.*\//, ''), false);
  } catch (err) {
    main.replaceChildren(h('div', { class: 'error' }, h('p', {}, h('b', { text: 'The knowledge-base export could not be loaded.' })),
      h('p', { text: `${url}: ${err.message}` }),
      h('p', { class: 'small', text: 'Run "python scripts/export_webapp.py --out export/stroke-aphasia-kb.json" in the repository, serve the repository root (npm run explorer), or open a local export with the control in the header.' })));
  }
}

/** The nav's "Review" entry: the private review portal (docs/PORTAL.md), only when the export names one. */
function portalNav(portal) {
  const nav = document.querySelector('.nav'); if (!nav) return;
  let a = nav.querySelector('a.portal');
  if (!portal?.url) { a?.remove(); return; }
  if (!a) { a = h('a', { class: 'portal', target: '_blank', rel: 'noopener', title: 'Review portal — drafts beside the annotated PDFs and the screening queue; for invited reviewers' }); nav.append(a); }
  a.setAttribute('href', portal.url); a.textContent = 'Review ↗';
}

/** The CALMaR notebook page lives on its own address and is published by the calmar repository: link to it only when it is there. */
const NOTEBOOK_PAGE = 'https://calmar.aphasia-kb.app/';
function findNotebookPage() {
  fetch(`${NOTEBOOK_PAGE}build.json`, { cache: 'no-cache' }).then((r) => (r.ok ? r.json() : null)).catch(() => null).then((info) => {
    if (!info) return;
    state.notebook = info;
    document.getElementById('notebookLink')?.removeAttribute('hidden');
    if (state.index && !parseRoute().segments[0]) render();      // the Overview lists it
  });
}

function use(kb, label, local) {
  if (kb.schemaVersion !== 1) throw new Error(`Unsupported export schema ${kb.schemaVersion}`);
  state.index = buildIndex(kb);
  portalNav(state.index.kb.portal);
  state.shown = PAGE;
  setSource(label, local);
  render();
}

function init() {
  const params = new URLSearchParams(location.search);
  document.getElementById('kbFile').addEventListener('change', async (e) => {
    const file = e.target.files?.[0];
    if (!file) return;
    try { use(JSON.parse(await file.text()), `${file.name} (local)`, true); } catch (err) { document.getElementById('main').replaceChildren(h('p', { class: 'error', text: `${file.name}: ${err.message}` })); }
  });
  window.addEventListener('hashchange', () => { state.shown = PAGE; render(); });
  const kb = params.get('kb');
  const select = document.getElementById('kbVersion');
  if (kb && !KB_VERSIONS[kb]) select.closest('label').hidden = true;   // an explicit URL: no switch
  else select.value = kb || 'drafts';
  select.addEventListener('change', () => {
    const next = new URLSearchParams(location.search);
    if (select.value === 'drafts') next.delete('kb'); else next.set('kb', select.value);
    const q = next.toString();
    location.search = q ? `?${q}` : '';   // reloads with the other export, keeps the #route
  });
  load(KB_VERSIONS[kb] || kb || DEFAULT_KB);
  findNotebookPage();
}

init();
