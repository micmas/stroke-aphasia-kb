// Indexes the exported knowledge base (export_webapp.py → stroke-aphasia-kb.json)
// for exploration: lookups by entry, by paper, by (region, impairment) pair, and
// faceted filtering of findings. Pure functions over the JSON; no DOM.
//
// Naming and display rules come from js/kb-evidence.js so the explorer shows a
// finding exactly as the participant report and the webapp do.
import { displayName, labelFor, fullMapping, findingStages } from '../js/kb-evidence.js';

export const RELATIONSHIP_TEXT = {
  causal: 'causal (lesion → impairment)',
  correlational: 'correlational',
  recruitment: 'recruitment (region engaged for the function)',
  responder: 'responder characteristic',
  treatment_response: 'treatment response',
  synthesis: 'synthesis (review)',
};

export const DIRECTION_LABEL = {
  likely: 'association reported',
  unlikely: 'association not supported',
  no_effect: 'no effect reported',
  mixed: 'mixed / unclear',
  likely_responder: 'likely responder',
  unlikely_responder: 'unlikely responder',
};

export const REVIEW_LABEL = {
  human: 'approved by a named person',
  model: 'approved by an independent local model (Tier A)',
  legacy: 'approved before the governance policy (legacy)',
  none: 'no named reviewer',
};

export const FACETS = [
  { key: 'source_kind', label: 'Entry type', order: ['region', 'impairment', 'therapy', 'predictor'] },
  { key: 'target_kind', label: 'Target type', order: ['impairment', 'region', 'therapy', 'predictor', 'prognosis'] },
  { key: 'relationship', label: 'Relationship', order: ['causal', 'correlational', 'recruitment', 'responder', 'treatment_response', 'synthesis'] },
  { key: 'strength', label: 'Strength', order: ['strong', 'moderate', 'weak'] },
  { key: 'review_kind', label: 'Review provenance', order: ['human', 'model', 'legacy', 'none'] },
  { key: 'stage', label: 'Recovery stage', order: ['acute', 'subacute', 'chronic', 'not stated'] },
  { key: 'method', label: 'Method', order: null },
  { key: 'design', label: 'Design', order: null },
  { key: 'evidence_quality', label: 'Evidence class', order: ['RCT', 'cohort', 'case-study'] },
  { key: 'direction', label: 'Direction', order: ['likely', 'mixed', 'no_effect', 'unlikely', 'likely_responder', 'unlikely_responder'] },
  { key: 'source_id', label: 'Entry', order: null, link: 'entry' },
  { key: 'target', label: 'Target', order: null, link: 'entry' },
  { key: 'citation', label: 'Paper', order: null, link: 'paper' },
];

const BUCKET_KIND = { regions: 'region', impairments: 'impairment', therapies: 'therapy', predictors: 'predictor', reviews: 'review', ingredients: 'ingredient' };

const asList = (v) => (v === null || v === undefined ? [] : Array.isArray(v) ? v.map(String) : [String(v)]);

export function yearOf(citationKey, text) {
  const fromKey = String(citationKey || '').match(/(19|20)\d{2}/);
  if (fromKey) return Number(fromKey[0]);
  const fromText = String(text || '').match(/\.\s*((?:19|20)\d{2})\b/);
  return fromText ? Number(fromText[1]) : null;
}

export function firstAuthorOf(citationKey, text) {
  const m = String(text || '').match(/^([^,.]+?)(?:\s+[A-Z]{1,3})?[,.]/);
  if (m) return m[1].trim();
  const k = String(citationKey || '').replace(/^@/, '').match(/^[A-Za-z]+/);
  return k ? k[0] : String(citationKey || '');
}

export function doiOf(text) {
  const m = String(text || '').match(/10\.\d{4,9}\/[^\s"<>]+/);
  return m ? m[0].replace(/[.,;)]+$/, '') : null;
}

export function pagesOf(finding) {
  const pages = (finding.source_passages || []).map((p) => Number(p.page)).filter((n) => Number.isFinite(n));
  return pages.length ? Math.min(...pages) : Infinity;
}

/** The (region, impairment)-style pair a finding expresses, whichever side is the entry. */
export function pairOf(f) {
  const s = f.source_kind; const t = f.target_kind;
  if (s === 'region' && t === 'impairment') return { kind: 'region-impairment', row: f.source_id, col: f.target };
  if (s === 'impairment' && t === 'region') return { kind: 'region-impairment', row: f.target, col: f.source_id };
  if (s === 'therapy' && t === 'impairment') return { kind: 'therapy-impairment', row: f.source_id, col: f.target };
  if (s === 'impairment' && t === 'therapy') return { kind: 'therapy-impairment', row: f.target, col: f.source_id };
  if (s === 'predictor') return { kind: 'predictor-outcome', row: f.source_id, col: f.target };
  if (s === 'region' && t === 'region') return { kind: 'region-region', row: f.source_id, col: f.target };
  return null;
}

export function buildIndex(kb) {
  const entries = kb.entries || {};
  const findings = (kb.findings || []).map((f, i) => {
    const stages = findingStages(f);
    return {
      ...f,
      key: `${f.source_id}/${f.id}`,
      ordinal: i,
      stage: stages.length ? stages : ['not stated'],
      method: asList(f.method).length ? asList(f.method) : ['not reported'],
      design: f.design ? String(f.design) : 'not reported',
      review_kind: f.review_kind || 'none',
      year: yearOf(f.citation, kb.citations?.[f.citation]),
      page: pagesOf(f),
      pair: pairOf(f),
      text: [f.claim, f.population, f.time_post_onset, ...(f.source_passages || []).map((p) => p.quote), f.source_id, f.target, f.citation,
        labelFor(kb, f.source_id), labelFor(kb, f.target), ...(f.flags || []), ...(f.author_limitations || [])]
        .filter(Boolean).join(' \n ').toLowerCase(),
    };
  });

  const bySource = new Map(); const byTarget = new Map(); const byPaper = new Map(); const byKey = new Map();
  for (const f of findings) {
    byKey.set(f.key, f);
    (bySource.get(f.source_id) || bySource.set(f.source_id, []).get(f.source_id)).push(f);
    (byTarget.get(f.target) || byTarget.set(f.target, []).get(f.target)).push(f);
    (byPaper.get(f.citation) || byPaper.set(f.citation, []).get(f.citation)).push(f);
  }

  const papers = [...byPaper.entries()].map(([key, rows]) => {
    const text = kb.citations?.[key] || '';
    return {
      key, text, findings: rows, n: rows.length,
      year: yearOf(key, text), author: firstAuthorOf(key, text), doi: doiOf(text),
      entries: [...new Set(rows.map((r) => r.source_id))],
      human: rows.filter((r) => r.review_kind === 'human').length,
    };
  }).sort((a, b) => (b.n - a.n) || String(a.key).localeCompare(b.key));

  // Entities that appear only as targets still deserve a page.
  const ids = new Set(Object.keys(entries));
  for (const f of findings) { ids.add(f.source_id); ids.add(f.target); }

  const mapping = fullMapping(kb.mapping || {});
  const unmapped = kb.mapping?.unmapped || {};
  const unmappedReason = (id) => (Array.isArray(unmapped) ? (unmapped.includes(id) ? 'not mapped' : null) : (unmapped[id] ?? null));

  // Therapies that list an impairment among their targets.
  const therapiesFor = new Map();
  for (const e of Object.values(entries)) {
    for (const t of e.targets_impairments || []) (therapiesFor.get(t) || therapiesFor.set(t, []).get(t)).push(e.id);
  }

  return {
    kb, entries, findings, byKey, bySource, byTarget, byPaper, papers, ids, mapping, unmappedReason, therapiesFor,
    name: (id) => displayName(kb, id),
    hasEntry: (id) => Boolean(entries[id]),
    kindOf(id) {
      const e = entries[id];
      if (e) return BUCKET_KIND[e.bucket] || e.bucket;
      const f = byTarget.get(id)?.[0];
      return f ? f.target_kind : 'unknown';
    },
  };
}

/** Facet values of one finding (multi-valued facets return several). */
export function facetValues(f, key) {
  const v = f[key];
  return Array.isArray(v) ? v : [v === null || v === undefined || v === '' ? 'not reported' : String(v)];
}

export function matches(f, filters, query) {
  for (const [key, wanted] of Object.entries(filters)) {
    if (!wanted?.length) continue;
    const values = facetValues(f, key);
    if (!wanted.some((w) => values.includes(w))) return false;
  }
  if (query) {
    const terms = query.toLowerCase().split(/\s+/).filter(Boolean);
    if (!terms.every((t) => f.text.includes(t))) return false;
  }
  return true;
}

/** Counts per facet value, each facet computed with every *other* filter applied. */
export function facetCounts(findings, filters, query) {
  const out = {};
  for (const facet of FACETS) {
    const others = { ...filters, [facet.key]: [] };
    const counts = new Map();
    for (const f of findings) {
      if (!matches(f, others, query)) continue;
      for (const v of facetValues(f, facet.key)) counts.set(v, (counts.get(v) || 0) + 1);
    }
    out[facet.key] = counts;
  }
  return out;
}

export function matrixOf(index, kind) {
  const rows = new Map(); const cols = new Map(); const cells = new Map();
  for (const f of index.findings) {
    if (!f.pair || f.pair.kind !== kind) continue;
    const { row, col } = f.pair;
    rows.set(row, (rows.get(row) || 0) + 1);
    cols.set(col, (cols.get(col) || 0) + 1);
    const k = `${row}\u0000${col}`;
    (cells.get(k) || cells.set(k, []).get(k)).push(f);
  }
  const sortDesc = (m) => [...m.entries()].sort((a, b) => (b[1] - a[1]) || index.name(a[0]).localeCompare(index.name(b[0]))).map(([id]) => id);
  return { rows: sortDesc(rows), cols: sortDesc(cols), rowTotals: rows, colTotals: cols, cells, cell: (r, c) => cells.get(`${r}\u0000${c}`) || [] };
}

export function provenanceCounts(findings) {
  const c = { human: 0, model: 0, legacy: 0, none: 0 };
  for (const f of findings) c[f.review_kind in c ? f.review_kind : 'none'] += 1;
  return c;
}
