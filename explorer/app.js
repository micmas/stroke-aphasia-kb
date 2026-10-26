// Stroke aphasia KB explorer — views and routing.
//
// A static page: it loads export/stroke-aphasia-kb.json (or the file named by
// ?kb=<url>, or one chosen with the "Open a local export" control), indexes
// it with kb-index.js and renders one view per hash route:
//   #/                       overview
//   #/findings?facet=value   faceted finding browser (query string = filters)
//   #/matrix?kind=…          evidence matrices
//   #/papers · #/paper/<Key> bibliography and one paper's findings in page order
//   #/coverage?facet=value  the screening register: PRISMA flow, gap coverage, candidates
//   #/entry/<id>             one region / impairment / therapy / predictor
//   #/finding/<source>/<id>  one finding, permalinked
// Every string from the KB is inserted as text, never as HTML.
import {
  buildIndex, FACETS, facetCounts, matches, matrixOf, provenanceCounts,
  RELATIONSHIP_TEXT, DIRECTION_LABEL, REVIEW_LABEL,
  SCREENING_FACETS, STAGE_TEXT, KB_STATE_TEXT, ARM_TEXT,
} from './kb-index.js';

const DEFAULT_KB = '../export/stroke-aphasia-kb.json';
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
const findingHref = (f) => `#/finding/${esc(f.source_id)}/${esc(f.id)}`;

function parseRoute() {
  const raw = location.hash.replace(/^#/, '') || '/';
  const [path, qs = ''] = raw.split('?');
  const params = new URLSearchParams(qs);
  const filters = {};
  for (const [k, v] of params) { if (k === 'q' || k === 'sort' || k === 'kind' || k === 'min' || k === 'entries' || k === 'find') continue; (filters[k] ||= []).push(v); }
  return { path: decodeURI(path), params, filters, segments: path.split('/').filter(Boolean).map(decodeURIComponent) };
}

// ---------------------------------------------------------------------------
// Shared renderers
// ---------------------------------------------------------------------------
function kindBadge(kind) { return h('span', { class: 'badge badge-kind', text: kind }); }

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
  return h('span', { class: `badge badge-strength-${v}`, text: `${v} evidence` });
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
  const meta = [];
  const push = (node) => { if (meta.length) meta.push(h('span', { class: 'sep', text: '·' })); meta.push(node); };
  push(h('a', { class: 'chip', href: paperHref(f.citation), text: f.citation }));
  if (f.year) push(h('span', { text: String(f.year) }));
  push(h('span', { text: RELATIONSHIP_TEXT[f.relationship] || f.relationship || 'relationship not stated' }));
  push(h('span', { text: DIRECTION_LABEL[f.direction] || f.direction || '' }));
  push(strengthBadge(f.strength));
  push(h('span', { text: `${f.method.join(', ')}${f.design && f.design !== 'not reported' ? ` · ${f.design}` : ''}` }));
  push(h('span', { text: `stage: ${f.stage.join('/')}` }));
  if (f.evidence_quality) push(h('span', { text: f.evidence_quality }));
  push(reviewBadge(f));
  if (f.design_cautions?.length) push(h('span', { class: 'badge badge-warn', title: f.design_cautions.join('; '), text: plural(f.design_cautions.length, 'design caution') }));

  const details = [];
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
  const hasMore = details.length > 0;

  return h('article', { class: 'finding', id: `f-${f.source_id}-${f.id}` },
    route ? h('p', { class: 'route' }, entryLink(index, f.source_id), ' ', kindBadge(f.source_kind), ' → ', entryLink(index, f.target), ' ', kindBadge(f.target_kind)) : null,
    h('p', { class: 'claim', text: String(f.claim || '').trim() }),
    h('p', { class: 'meta' }, meta, h('a', { class: 'permalink', href: findingHref(f), text: `${f.id} · permalink` })),
    hasMore ? h('details', { open: open || null }, h('summary', { text: 'Study context, statistics, limitations, review and source passages' }), details) : null,
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
  const buckets = {};
  for (const e of Object.values(entries)) buckets[e.bucket] = (buckets[e.bucket] || 0) + 1;
  const prov = provenanceCounts(findings);
  const countBy = (pred, key) => {
    const m = new Map();
    for (const f of findings) {
      if (f.source_kind === pred) m.set(f.source_id, (m.get(f.source_id) || 0) + 1);
      if (f.target_kind === pred) m.set(f.target, (m.get(f.target) || 0) + 1);
    }
    return [...m.entries()].map(([id, n]) => ({ id, n, label: index.name(id), alt: !index.hasEntry(id) })).sort((a, b) => b.n - a.n || a.label.localeCompare(b.label));
  };
  const regionEntries = Object.values(entries).filter((e) => e.bucket === 'regions');
  const reachable = regionEntries.filter((e) => index.mapping.regions[e.id]).length;
  const unreachable = regionEntries.filter((e) => !index.mapping.regions[e.id]);
  const therapies = Object.values(entries).filter((e) => e.bucket === 'therapies').map((e) => ({ id: e.id, label: e.name, n: (index.bySource.get(e.id) || []).length + (index.byTarget.get(e.id) || []).length })).sort((a, b) => b.n - a.n);

  return frag(
    h('div', { class: 'page-head' }, h('h1', { text: 'Stroke aphasia knowledge base' }),
      h('span', { class: 'muted small', text: `export of KB ${v.commit || 'uncommitted'}${v.date ? ` (${v.date})` : ''} · digest ${v.contentDigest || '?'} · exported ${v.exportedOn || '?'} · statuses: ${(v.statuses || []).join(', ')}` })),
    h('p', {}, 'A curated, source-traceable literature base linking stroke lesion locations to aphasia impairments, therapy responses and recovery predictors. Every finding is one claim from one paper with the verbatim passages that support it. This page lets you read the base itself; CALMaR uses the same export to turn a lesion into a cited report.'),
    h('p', { class: 'caveat', text: 'Findings are group-level literature associations with their citations and review provenance, not clinical predictions. Research use only.' }),
    h('div', { class: 'tiles' },
      h('div', { class: 'tile' }, h('div', { class: 'value', text: String(Object.keys(entries).length) }), h('div', { class: 'label', text: 'entries' }),
        h('div', { class: 'detail', text: Object.entries(buckets).map(([b, n]) => `${n} ${b}`).join(' · ') })),
      h('div', { class: 'tile' }, h('div', { class: 'value', text: String(findings.length) }), h('div', { class: 'label', text: 'findings' }),
        h('div', { class: 'detail', text: `${findings.filter((f) => f.strength === 'strong').length} strong · ${findings.filter((f) => f.strength === 'moderate').length} moderate · ${findings.filter((f) => f.strength === 'weak').length} weak` })),
      h('div', { class: 'tile' }, h('div', { class: 'value', text: String(papers.length) }), h('div', { class: 'label', text: 'papers with findings' }),
        h('div', { class: 'detail', text: `${Object.keys(kb.citations || {}).length} entries in the bibliography` })),
      h('div', { class: 'tile' }, h('div', { class: 'value', text: pct(prov.human, findings.length) }), h('div', { class: 'label', text: 'findings approved by a named person' }),
        h('div', { class: 'detail', text: `${prov.human} of ${findings.length}` })),
      h('div', { class: 'tile' }, h('div', { class: 'value', text: `${reachable}/${regionEntries.length}` }), h('div', { class: 'label', text: 'region entries a lesion can reach' }),
        h('div', { class: 'detail', text: 'through the curated atlas mapping' })),
      index.screening.present ? h('div', { class: 'tile' }, h('div', { class: 'value', text: String(index.screening.prisma?.included?.total ?? 0) }), h('div', { class: 'label' }, h('a', { href: '#/coverage', text: 'papers included by screening' })),
        h('div', { class: 'detail', text: `of ${index.screening.candidates.length} candidates · ${index.screening.candidates.filter((c) => ['awaiting_ta', 'awaiting_ft', 'unsure_ta', 'unsure_ft'].includes(c.stage)).length} awaiting a decision` })) : null),
    h('h2', { text: 'Review provenance of findings' }),
    stackBar(prov),
    h('p', { class: 'small muted' }, 'Who may approve what is set by the governance policy. Legacy findings were approved before it and are tagged for re-review. ',
      h('a', { href: href('/findings', { review_kind: ['human'] }), text: 'Browse person-approved findings' }), ' · ',
      h('a', { href: href('/findings', { review_kind: ['legacy'] }), text: 'browse legacy findings' })),
    h('div', { class: 'grid-2' },
      h('section', {}, h('h2', { text: 'Regions by number of findings' }), barList(countBy('region'), { max: 12, link: (x) => entryHref(x.id) }),
        h('p', { class: 'small muted', text: 'Grey bars: anatomical targets named by findings that have no entry of their own yet.' })),
      h('section', {}, h('h2', { text: 'Impairments by number of findings' }), barList(countBy('impairment'), { max: 12, link: (x) => entryHref(x.id) }))),
    h('div', { class: 'grid-2' },
      h('section', {}, h('h2', { text: 'Therapies' }), barList(therapies, { link: (x) => entryHref(x.id) })),
      h('section', {}, h('h2', { text: 'Region entries a lesion cannot reach' }),
        unreachable.length ? h('ul', {}, unreachable.map((e) => h('li', {}, entryLink(index, e.id), h('span', { class: 'small muted', text: index.unmappedReason(e.id) ? ` — ${index.unmappedReason(e.id)}` : '' })))) : h('p', { class: 'muted', text: 'All region entries are reachable.' }),
        h('p', { class: 'small muted', text: 'Only regions present in the curated atlas mapping can be matched from a lesion mask; the others are still readable here.' }))),
    h('h2', { text: 'Start exploring' }),
    h('ul', {},
      h('li', {}, h('a', { href: '#/matrix', text: 'Evidence matrix' }), ' — which region–impairment links are supported, by how many findings.'),
      h('li', {}, h('a', { href: '#/findings', text: 'Findings browser' }), ' — filter by entry type, relationship, strength, method, stage, provenance or paper; full-text search of claims and quotes.'),
      h('li', {}, h('a', { href: '#/papers', text: 'Papers' }), ' — every cited paper and its findings in page order, to spot-check an extraction against the PDF.'),
      h('li', {}, h('a', { href: '#/coverage', text: 'Coverage' }), ' — how the literature was searched and screened (PRISMA flow), what each evidence gap still needs, and where every candidate paper stands.')));
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
    return h('details', { class: 'facet', open: selected.size || ['source_kind', 'relationship', 'strength', 'review_kind'].includes(facet.key) ? '' : null },
      h('summary', { text: `${facet.label}${selected.size ? ` (${selected.size})` : ''}` }),
      shown.map((v) => h('label', { class: m.get(v) ? '' : 'zero' },
        h('input', { type: 'checkbox', checked: selected.has(v) ? '' : null, onchange: () => toggle(facet.key, v) }),
        h('span', { text: facet.link ? index.name(v) : String(v).replace(/_/g, ' '), title: String(v) }),
        h('span', { class: 'n', text: String(m.get(v) || 0) }))),
      many && shown.length < values.length ? h('p', { class: 'small muted', text: `${values.length - shown.length} more — narrow with the search box` }) : null);
  });

  const active = Object.entries(filters).flatMap(([k, vs]) => vs.map((v) => h('button', { type: 'button', onclick: () => toggle(k, v), text: `${FACETS.find((f) => f.key === k)?.label || k}: ${FACETS.find((f) => f.key === k)?.link ? index.name(v) : v} ×` })));
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
  const m = matrixOf(index, kind);
  const keep = (id) => (!onlyEntries || index.hasEntry(id)) && (!find || index.name(id).toLowerCase().includes(find) || id.toLowerCase().includes(find));
  const rows = m.rows.filter((r) => keep(r) && m.rowTotals.get(r) >= min);
  const cols = m.cols.filter((c) => keep(c) && m.colTotals.get(c) >= min);
  const kinds = { 'region-impairment': ['Region', 'Impairment'], 'therapy-impairment': ['Therapy', 'Impairment'], 'predictor-outcome': ['Predictor', 'Outcome'], 'region-region': ['Region', 'Region (network / tract)'] };
  const [rowLabel, colLabel] = kinds[kind] || ['Entry', 'Target'];
  const cls = (n) => (n >= 8 ? 'c6' : n >= 5 ? 'c5' : n >= 4 ? 'c4' : n === 3 ? 'c3' : n === 2 ? 'c2' : n === 1 ? 'c1' : '');
  const go = (params) => { location.hash = href('/matrix', { kind, min, entries: onlyEntries ? '1' : '', find, ...params }); };

  const filtersFor = (r, c) => (kind === 'predictor-outcome' ? { source_id: [r], target: [c] }
    : { source_id: [r, c], target: [r, c] });
  const tooltip = h('div', { class: 'tooltip hidden', role: 'tooltip' });
  const showTip = (e, r, c) => {
    const cell = m.cell(r, c);
    const prov = provenanceCounts(cell);
    const rel = {}; const str = {};
    for (const f of cell) { rel[f.relationship] = (rel[f.relationship] || 0) + 1; str[f.strength] = (str[f.strength] || 0) + 1; }
    tooltip.replaceChildren(h('b', { text: `${index.name(r)} × ${index.name(c)}` }), h('br'),
      `${plural(cell.length, 'finding')} from ${plural(new Set(cell.map((f) => f.citation)).size, 'paper')}`, h('br'),
      `strength: ${Object.entries(str).map(([k, n]) => `${k} ${n}`).join(', ')}`, h('br'),
      `relationship: ${Object.entries(rel).map(([k, n]) => `${k} ${n}`).join(', ')}`, h('br'),
      `approved by a person: ${prov.human}`);
    tooltip.classList.remove('hidden');
    const x = Math.min(e.clientX + 14, window.innerWidth - 330); const y = Math.min(e.clientY + 14, window.innerHeight - 120);
    tooltip.style.left = `${x}px`; tooltip.style.top = `${y}px`;
  };
  const hideTip = () => tooltip.classList.add('hidden');

  const table = h('table', { class: 'matrix' },
    h('thead', {}, h('tr', {}, h('th', { class: 'corner', scope: 'col', text: `${rowLabel} ↓ · ${colLabel} →` }),
      cols.map((c) => h('th', { scope: 'col', class: index.hasEntry(c) ? '' : 'noentry' }, h('a', { class: 'rot', href: entryHref(c), title: `${index.name(c)} (${m.colTotals.get(c)})`, text: index.name(c) }))),
      h('th', { scope: 'col', class: 'total' }, h('span', { class: 'rot', text: 'total' })))),
    h('tbody', {}, rows.map((r) => h('tr', {},
      h('th', { scope: 'row', class: index.hasEntry(r) ? '' : 'noentry' }, h('a', { href: entryHref(r), title: index.hasEntry(r) ? r : `${r} — no entry of its own yet`, text: index.name(r) })),
      cols.map((c) => { const n = m.cell(r, c).length; return h('td', { class: cls(n) }, n ? h('a', { href: href('/findings', filtersFor(r, c)), 'aria-label': `${n} findings for ${index.name(r)} and ${index.name(c)}`, onmousemove: (e) => showTip(e, r, c), onmouseleave: hideTip, onfocus: (e) => showTip({ clientX: e.target.getBoundingClientRect().left, clientY: e.target.getBoundingClientRect().top }, r, c), onblur: hideTip, text: String(n) }) : ''); }),
      h('td', { class: 'total', text: String(m.rowTotals.get(r)) })))),
    h('tfoot', {}, h('tr', { class: 'total' }, h('th', { scope: 'row', text: 'total' }), cols.map((c) => h('td', { text: String(m.colTotals.get(c)) })), h('td', { text: String([...m.cells.values()].reduce((n, x) => n + x.length, 0)) }))));

  return frag(
    h('div', { class: 'page-head' }, h('h1', { text: 'Evidence matrix' }), h('span', { class: 'muted small', text: `${rows.length} ${rowLabel.toLowerCase()} rows × ${cols.length} ${colLabel.toLowerCase()} columns` })),
    h('p', { class: 'small' }, 'Each cell is the number of findings linking the row and the column, in either direction (a region entry whose finding targets an impairment, or an impairment entry whose finding targets a region). Click a cell to read them. Rows and columns are ordered by total; a row name in grey has no entry of its own yet.'),
    h('div', { class: 'matrix-controls' },
      h('label', {}, 'matrix ', h('select', { onchange: (e) => go({ kind: e.target.value }) }, Object.entries(kinds).map(([v, [a, b]]) => h('option', { value: v, selected: v === kind ? '' : null, text: `${a} × ${b}` })))),
      h('label', {}, 'at least ', h('select', { onchange: (e) => go({ min: e.target.value }) }, [1, 2, 3, 5].map((v) => h('option', { value: v, selected: v === min ? '' : null, text: `${v}` }))), ' findings on the margin'),
      h('label', {}, h('input', { type: 'checkbox', checked: onlyEntries ? '' : null, onchange: (e) => go({ entries: e.target.checked ? '1' : '' }) }), ' only ids with an entry'),
      h('input', { type: 'search', placeholder: 'find a row or column…', value: find, 'aria-label': 'Filter rows and columns', onchange: (e) => go({ find: e.target.value.trim() }) }),
      h('span', { class: 'ramp' }, '1', h('i', { style: 'background:var(--seq-1)' }), h('i', { style: 'background:var(--seq-2)' }), h('i', { style: 'background:var(--seq-3)' }), h('i', { style: 'background:var(--seq-4)' }), h('i', { style: 'background:var(--seq-5)' }), h('i', { style: 'background:var(--seq-6)' }), '8+ findings')),
    rows.length && cols.length ? h('div', { class: 'matrix-wrap' }, table) : h('p', { class: 'notice', text: 'Nothing to show with these settings.' }),
    tooltip);
}

function papers(index) {
  const sortKey = { key: 'key' };
  const table = h('table', { class: 'paper-list sortable' });
  const render = (by, dir) => {
    const rows = index.papers.slice().sort((a, b) => {
      const x = a[by]; const y = b[by];
      const r = typeof x === 'number' && typeof y === 'number' ? x - y : String(x ?? '').localeCompare(String(y ?? ''));
      return dir === 'asc' ? r : -r;
    });
    const head = (label, k, numeric = false) => h('th', { class: numeric ? 'num' : '' }, h('button', { type: 'button', 'aria-sort': by === k ? (dir === 'asc' ? 'ascending' : 'descending') : 'none', onclick: () => render(k, by === k && dir === 'desc' ? 'asc' : 'desc'), text: label }));
    table.replaceChildren(
      h('thead', {}, h('tr', {}, head('Key', 'key'), head('First author', 'author'), head('Year', 'year', true), head('Findings', 'n', true), head('Person-approved', 'human', true), h('th', { text: 'Entries' }), index.screening.present ? h('th', { text: 'Screening' }) : null)),
      h('tbody', {}, rows.map((p) => h('tr', {},
        h('td', {}, h('a', { class: 'chip', href: paperHref(p.key), text: p.key })),
        h('td', { text: p.author }), h('td', { class: 'num', text: p.year ? String(p.year) : '—' }),
        h('td', { class: 'num', text: String(p.n) }), h('td', { class: 'num', text: String(p.human) }),
        h('td', { class: 'small' }, p.entries.slice(0, 4).map((id, i) => [i ? ', ' : '', entryLink(index, id)]), p.entries.length > 4 ? ` +${p.entries.length - 4}` : ''),
        index.screening.present ? h('td', {}, (() => { const c = index.screening.byKey.get(p.key); return c ? h('a', { href: coverageHref({ q: c.id }), title: `${c.id} · ${STAGE_TEXT[c.stage] || c.stage}` }, stageBadge(c.stage)) : h('span', { class: 'muted small', text: 'not in the register' }); })()) : null))));
  };
  render('n', 'desc');
  const cited = Object.keys(index.kb.citations || {}).length;
  return frag(
    h('div', { class: 'page-head' }, h('h1', { text: 'Papers' }), h('span', { class: 'muted small', text: `${index.papers.length} papers with findings · ${cited} bibliography entries` })),
    h('p', { class: 'small', text: 'Source PDFs are not redistributed; the bibliography carries a DOI for every key. Open a paper to read its findings in page order and check each quote against the PDF.' }),
    index.screening.present ? h('p', { class: 'small muted' }, 'Papers that were screened but have no findings yet are listed under ', h('a', { href: '#/coverage', text: 'Coverage' }), '.') : null,
    table);
}

function paper(index, key) {
  const k = key.startsWith('@') ? key : `@${key}`;
  const rows = (index.byPaper.get(k) || []).slice().sort((a, b) => a.page - b.page || a.ordinal - b.ordinal);
  const text = index.kb.citations?.[k];
  const p = index.papers.find((x) => x.key === k);
  if (!rows.length && !text && !index.screening.byKey.has(k)) return h('p', { class: 'error', text: `No paper ${k} in this export.` });
  const prov = provenanceCounts(rows);
  return frag(
    h('div', { class: 'page-head' }, h('h1', { text: k })),
    text ? h('p', { text }) : h('p', { class: 'muted', text: 'Not in the bibliography.' }),
    p?.doi ? h('p', { class: 'small' }, 'DOI ', h('a', { href: `https://doi.org/${p.doi}`, rel: 'noopener', target: '_blank', text: p.doi })) : null,
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
  const reason = index.unmappedReason(id);
  const kv = {};
  if (e) {
    kv.bucket = e.bucket; if (e.kind) kv['entry kind'] = e.kind; if (e.status) kv.status = e.status;
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
    h('div', { class: 'page-head' }, h('h1', { text: 'Finding' }), h('span', { class: 'muted small', text: `${f.source_id} · ${f.id}` })),
    findingCard(index, f, { open: true }),
    h('p', { class: 'small' }, 'From the entry ', entryLink(index, f.source_id), ' · paper ', h('a', { href: paperHref(f.citation), text: f.citation })));
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
const stageBadge = (stage) => h('span', { class: `badge badge-stage badge-stage-${stage}`, title: STAGE_TEXT[stage] || stage, text: STAGE_TEXT[stage] || String(stage || '').replace(/_/g, ' ') });
const kbBadge = (state) => h('span', { class: `badge badge-kb badge-kb-${String(state).replace(/\s+/g, '-')}`, text: KB_STATE_TEXT[state] || String(state || '').replace(/_/g, ' ') });

/** The PRISMA 2020 flow as one SVG. Every box links to the candidates it counts. */
function prismaDiagram(index) {
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
  const box = ({ x, y: yy, w, title, n, sub, link, cls = '' }) => {
    const g = s('g', { class: `pr-box ${cls}` });
    g.append(s('rect', { x, y: yy, width: w, height: boxH, rx: 6 }));
    g.append(text(x + 10, yy + 20, fit(title, w - 16, 5.5), 'pr-title'));
    const line = text(x + 10, yy + 41, String(n), 'pr-n');
    if (sub) line.append(s('tspan', { class: 'pr-sub', dx: 6 }, fit(sub, w - 24 - 9 * String(n).length, 5.4)));
    g.append(line);
    if (link) {
      const a = s('a', { href: link, class: 'pr-link' });
      a.append(s('title', { text: `${title}: ${n}${sub ? ` (${sub})` : ''} — open these candidates` }));
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
  const fmtReasons = (obj) => Object.entries(obj || {}).map(([k, v]) => `${index.screening.reasonLabel(k)} ${v}`).join(', ');

  // Identification
  const dbSub = Object.entries(idn.databases.byDatabase || {}).map(([k, v]) => `${k} ${v}`).join(', ') || 'no search run yet';
  const otSub = Object.entries(idn.other.byKind || {}).map(([k, v]) => `${k.replace(/_/g, ' ')} ${v}`).join(', ');
  const sideX = (col) => col + main + gapX;
  // row 0
  nodes.push(box({ x: colL, y, w: main, title: 'Records from databases', n: idn.databases.records, sub: dbSub, link: coverageHref({ arm: 'databases' }) }));
  nodes.push(box({ x: sideX(colL), y, w: side, title: 'Duplicates merged', n: idn.duplicatesRemoved, link: coverageHref({ stage: 'duplicate' }), cls: 'pr-side' }));
  nodes.push(box({ x: colR, y, w: main + gapX + side, title: 'Records from other sources', n: idn.other.records, sub: otSub, link: coverageHref({ arm: 'other' }) }));
  arrowH(colL + main, sideX(colL), y + boxH / 2);
  rows.push(y);
  y += boxH + rowGap;
  // row 1
  nodes.push(box({ x: colL, y, w: main, title: 'Records screened (title/abstract)', n: db.screened, sub: db.awaitingTitleAbstract ? `${db.awaitingTitleAbstract} awaiting` : null, link: coverageHref({ arm: 'databases', stage: dbStages }) }));
  nodes.push(box({ x: sideX(colL), y, w: side, title: 'Excluded at title/abstract', n: db.excludedTitleAbstract, sub: db.unsureTitleAbstract ? `${db.unsureTitleAbstract} unsure` : null, link: coverageHref({ arm: 'databases', stage: 'excluded_ta' }), cls: 'pr-side pr-out' }));
  nodes.push(box({ x: colR, y, w: main, title: 'Reports sought for retrieval', n: ot.sought, link: coverageHref({ arm: 'other', stage: dbStages }) }));
  nodes.push(box({ x: sideX(colR), y, w: side, title: 'Not retrieved', n: ot.notRetrieved, link: coverageHref({ arm: 'other', stage: 'not_retrieved' }), cls: 'pr-side pr-out' }));
  arrowV(colL + main / 2, rows[0] + boxH, y); arrowV(colR + main / 2, rows[0] + boxH, y);
  arrowH(colL + main, sideX(colL), y + boxH / 2); arrowH(colR + main, sideX(colR), y + boxH / 2);
  rows.push(y);
  y += boxH + rowGap;
  // row 2
  nodes.push(box({ x: colL, y, w: main, title: 'Reports sought for retrieval', n: db.sought, link: coverageHref({ arm: 'databases', stage: soughtStages }) }));
  nodes.push(box({ x: sideX(colL), y, w: side, title: 'Not retrieved', n: db.notRetrieved, link: coverageHref({ arm: 'databases', stage: 'not_retrieved' }), cls: 'pr-side pr-out' }));
  nodes.push(box({ x: colR, y, w: main, title: 'Reports assessed for eligibility', n: ot.assessed, sub: ot.awaitingFullText ? `${ot.awaitingFullText} awaiting` : null, link: coverageHref({ arm: 'other', stage: ['excluded_ft', 'included', 'awaiting_ft', 'unsure_ft', 'awaiting_ta', 'unsure_ta', 'excluded_ta'] }) }));
  nodes.push(box({ x: sideX(colR), y, w: side, title: 'Excluded', n: ot.excludedFullText, sub: fmtReasons(ot.excludedFullTextReasons) || null, link: coverageHref({ arm: 'other', stage: ['excluded_ft', 'excluded_ta'] }), cls: 'pr-side pr-out' }));
  arrowV(colL + main / 2, rows[1] + boxH, y); arrowV(colR + main / 2, rows[1] + boxH, y);
  arrowH(colL + main, sideX(colL), y + boxH / 2); arrowH(colR + main, sideX(colR), y + boxH / 2);
  rows.push(y);
  y += boxH + rowGap;
  // row 3 (databases arm only)
  nodes.push(box({ x: colL, y, w: main, title: 'Reports assessed for eligibility', n: db.assessed, sub: db.awaitingFullText ? `${db.awaitingFullText} awaiting` : null, link: coverageHref({ arm: 'databases', stage: ['excluded_ft', 'included', 'awaiting_ft', 'unsure_ft'] }) }));
  nodes.push(box({ x: sideX(colL), y, w: side, title: 'Excluded at full text', n: db.excludedFullText, sub: fmtReasons(db.excludedFullTextReasons) || null, link: coverageHref({ arm: 'databases', stage: 'excluded_ft' }), cls: 'pr-side pr-out' }));
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
    nodes.push(box({ x, y, w: kbW, title, n: inc.kb?.[st] ?? 0, link: coverageHref({ stage: 'included', kb: st }), cls: st === 'in_kb' ? 'pr-kb pr-included' : st === 'rejected' || st === 'refused' ? 'pr-kb pr-out' : 'pr-kb' }));
    arrowV(x + kbW / 2, rows[4] + boxH + 18, y);
  });
  y += boxH + 16;
  label(rows[0] + boxH / 2, 'Identification'); label(rows[2] + boxH / 2, 'Screening'); label(y - 16 - boxH / 2, 'Knowledge base');

  const svg = s('svg', { viewBox: `0 0 ${W} ${y}`, class: 'prisma', role: 'img', 'aria-label': 'PRISMA 2020 flow diagram of the screening register' });
  svg.append(s('defs', {}, s('marker', { id: 'pr-head', viewBox: '0 0 10 10', refX: 9, refY: 5, markerWidth: 7, markerHeight: 7, orient: 'auto-start-reverse' }, s('path', { d: 'M0 0 L10 5 L0 10 z', class: 'pr-head' }))));
  svg.append(...lines, ...nodes);
  return svg;
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
  const valueLabel = (key, v) => (key === 'stage' ? STAGE_TEXT[v] || v : key === 'kb' ? KB_STATE_TEXT[v] || v : key === 'arm' ? ARM_TEXT[v] || v : key === 'reason' ? (v === 'not excluded' ? v : sc.reasonLabel(v)) : key === 'origin' ? (sc.sourceKinds[v] || String(v).replace(/_/g, ' ')) : key === 'search' ? (sc.searches.get(v) ? `${v} · ${sc.searches.get(v).database}` : v) : String(v).replace(/_/g, ' '));
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
      h('td', { class: 'small' }, (c.sources || []).map((src, i) => [i ? h('br') : null, src.search ? h('a', { href: coverageHref({ search: src.search }), text: `${src.search}${sc.searches.get(src.search) ? ` ${sc.searches.get(src.search).database}` : ''}` }) : h('span', { text: sc.sourceKinds[src.kind] || src.kind })])),
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
        g.suggested?.length ? h('div', { class: 'small' }, 'Suggested: ', g.suggested.map((k, i) => [i ? ', ' : '', index.kb.citations?.[k] || index.byPaper.has(k) ? h('a', { href: paperHref(k), text: k }) : h('span', { class: 'chip', text: k })])) : null),
      h('td', {}, g.kind ? h('span', { class: `badge badge-gap-${g.kind}`, text: g.kind.replace(/_/g, ' ') }) : h('span', { class: 'muted', text: 'entry' })),
      h('td', { class: 'small' }, (g.areas || []).map((a, i) => [i ? ', ' : '', index.hasEntry(a) || index.byTarget.has(a) ? entryLink(index, a) : h('span', { title: a, text: index.mapping.units?.[a]?.name || a.replace(/_/g, ' ') })])),
      h('td', { class: 'num', text: String(g.searches || 0) }), h('td', { class: 'num', text: String(g.found || 0) }), h('td', { class: 'num', text: String(g.screened || 0) }),
      h('td', { class: 'num', text: String(g.included || 0) }), h('td', { class: 'num' }, h('b', { text: String(g.in_kb || 0) })), h('td', { class: 'num', text: String(g.approved_findings || 0) }))))) : h('p', { class: 'muted', text: 'No evidence gaps are declared (atlas_mapping/evidence_gaps.yaml) and no search names what it serves.' });

  const searches = [...sc.searches.values()];
  const searchTable = searches.length ? h('table', { class: 'search-list' },
    h('thead', {}, h('tr', {}, h('th', { text: 'Id' }), h('th', { text: 'Database' }), h('th', { text: 'Date' }), h('th', { text: 'Query' }), h('th', { text: 'Serves' }), h('th', { class: 'num', text: 'Hits' }), h('th', { class: 'num', text: 'Retrieved' }), h('th', { text: 'Run by' }))),
    h('tbody', {}, searches.map((x) => h('tr', {},
      h('td', {}, h('a', { class: 'chip', href: coverageHref({ search: x.id }), text: x.id })), h('td', { text: x.database }), h('td', { text: x.date || '' }),
      h('td', {}, h('code', { class: 'query', text: x.query || '' }), x.filters ? h('div', { class: 'small muted', text: Object.entries(x.filters).map(([k, v]) => `${k}: ${v}`).join(' · ') }) : null, x.file ? h('div', { class: 'small muted', text: `imported from ${x.file}` }) : null),
      h('td', { class: 'small' }, (x.for || []).map((g, i) => [i ? ', ' : '', h('a', { href: coverageHref({ gap: g }), text: g.replace(/_/g, ' ') })])),
      h('td', { class: 'num', text: String(x.hits ?? '') }), h('td', { class: 'num', text: String(x.retrieved ?? '') }), h('td', { text: x.run_by || '' }))))) : h('p', { class: 'muted', text: 'No database search has been recorded yet; every candidate came from other sources. `python scripts/screen.py search` records one.' });

  return frag(
    h('div', { class: 'page-head' }, h('h1', { text: 'Coverage' }), h('span', { class: 'muted small', text: `${sc.candidates.length} candidates · ${searches.length} searches · ${inc.total} included · ${inc.kb?.in_kb ?? 0} in the knowledge base` })),
    h('p', {}, 'How the literature was searched and screened, and where every candidate paper stands: identified, screened, excluded (and why), included, extracted, approved into the knowledge base or rejected. The register is kept by ', h('code', { text: 'scripts/screen.py' }), ' under the protocol in SCREENING.md; decisions are made by a named person, and papers that entered the bibliography before the register existed are shown as "other sources" with legacy decisions.'),
    h('div', { class: 'tiles' },
      h('div', { class: 'tile' }, h('div', { class: 'value', text: String(sc.candidates.length) }), h('div', { class: 'label', text: 'candidate papers' }), h('div', { class: 'detail', text: `${p?.identification.databases.records ?? 0} database records · ${p?.identification.other.records ?? 0} from other sources` })),
      h('div', { class: 'tile' }, h('div', { class: 'value', text: String(decided) }), h('div', { class: 'label', text: 'screened' }), h('div', { class: 'detail', text: `${awaiting} awaiting a decision` })),
      h('div', { class: 'tile' }, h('div', { class: 'value', text: String(inc.total) }), h('div', { class: 'label', text: 'included' }), h('div', { class: 'detail', text: `${[...excludedReasons.values()].reduce((a, b) => a + b, 0)} excluded` })),
      h('div', { class: 'tile' }, h('div', { class: 'value', text: String(inc.kb?.in_kb ?? 0) }), h('div', { class: 'label', text: 'in the knowledge base' }), h('div', { class: 'detail', text: `${inc.approvedFindings} approved findings · ${inc.kb?.in_review ?? 0} in review` }))),
    h('h2', { text: 'Flow of papers (PRISMA 2020)' }),
    h('p', { class: 'small muted', text: 'Click a box to list the candidates it counts. Pink boxes are exits; the knowledge-base row shows where included papers stand in the extraction and review pipeline.' }),
    h('div', { class: 'prisma-wrap' }, prismaDiagram(index)),
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
    h('h2', { text: 'Searches' }),
    searchTable,
    h('h2', { id: 'candidates', text: 'Candidates' }),
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
  for (const src of c.sources || []) steps.push({ when: sc.searches.get(src.search)?.date || '', what: src.search ? `identified by search ${src.search} (${sc.searches.get(src.search)?.database || '?'})` : `identified: ${sc.sourceKinds[src.kind] || src.kind}` });
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
    else if (head === 'findings') { view = browse(index, route); current = '/findings'; }
    else if (head === 'matrix') { view = matrix(index, route); current = '/matrix'; }
    else if (head === 'papers') { view = papers(index); current = '/papers'; }
    else if (head === 'coverage') { view = coverage(index, route); current = '/coverage'; }
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
  if (head === 'finding' || location.hash.includes('#f-')) { /* permalinks scroll via :target */ }
  else window.scrollTo(0, 0);
  document.title = `${head ? `${head[0].toUpperCase()}${head.slice(1)}${rest[0] ? ` · ${index.name(rest[0])}` : ''} · ` : ''}Stroke aphasia KB`;
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
    const res = await fetch(url, { cache: 'no-cache' });
    if (!res.ok) throw new Error(`${res.status} ${res.statusText}`);
    const kb = await res.json();
    use(kb, url.replace(/^.*\//, ''), false);
  } catch (err) {
    main.replaceChildren(h('div', { class: 'error' }, h('p', {}, h('b', { text: 'The knowledge-base export could not be loaded.' })),
      h('p', { text: `${url}: ${err.message}` }),
      h('p', { class: 'small', text: 'Run "python scripts/export_webapp.py --out export/stroke-aphasia-kb.json" in the repository, serve the repository root (npm run explorer), or open a local export with the control in the header.' })));
  }
}

function use(kb, label, local) {
  if (kb.schemaVersion !== 1) throw new Error(`Unsupported export schema ${kb.schemaVersion}`);
  state.index = buildIndex(kb);
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
  load(params.get('kb') || DEFAULT_KB);
}

init();
