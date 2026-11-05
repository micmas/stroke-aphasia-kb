// Stroke aphasia KB — review portal (portal/web, published by scripts/publish_portal.py).
//
// A private site behind Cloudflare Access. It reads the KB exports and the
// screening queue it was built with, renders annotated PDFs (pdf.js) and sends
// every decision as a record to /api/reviews, which writes it into the
// repository (logs/portal/inbox/) for scripts/portal_import.py to apply.
//   #/                 home: queues and who you are
//   #/drafts           drafts awaiting review, grouped by paper
//   #/draft/<path>     one draft beside its annotated PDF: verdicts, edits, marks, comments
//   #/screen/ta        title/abstract screening queue
//   #/screen/ft        full-text screening queue (with the PDF when the portal holds it)
//   #/mine             the records you have sent
// Every string from the KB is inserted as text, never as HTML.

const PDFJS = './vendor/pdf.min.mjs';            // vendored by scripts/publish_portal.py from pdfjs-dist
const PDFJS_WORKER = './vendor/pdf.worker.min.mjs';
const EDITABLE = ['claim', 'direction', 'relationship', 'strength', 'target', 'target_kind'];
const VOCAB = {
  direction: ['likely', 'unlikely', 'no_effect', 'mixed', 'likely_responder', 'unlikely_responder'],
  relationship: ['causal', 'correlational', 'recruitment', 'responder', 'treatment_response', 'synthesis'],
  strength: ['strong', 'moderate', 'weak'],
  target_kind: ['impairment', 'therapy', 'region', 'prognosis', 'predictor'],
  supports: ['claim', 'method', 'sample', 'statistics', 'confounders', 'region_definition', 'limitation', 'imaging_details'],
};
const state = { me: null, manifest: null, kb: null, screening: null, mine: { inbox: [], applied: [] }, pdfjs: null, zoom: 1, sel: null, docs: new Map() };

// ---------------------------------------------------------------- helpers
function h(tag, attrs = {}, ...kids) {
  const el = document.createElement(tag);
  for (const [k, v] of Object.entries(attrs)) {
    if (v === null || v === undefined || v === false) continue;
    if (k === 'class') el.className = v; else if (k === 'text') el.textContent = v;
    else if (k.startsWith('on') && typeof v === 'function') el.addEventListener(k.slice(2), v);
    else if (k === 'style') el.style.cssText = v; else el.setAttribute(k, v === true ? '' : v);
  }
  for (const c of kids.flat(Infinity)) if (c !== null && c !== undefined && c !== false) el.append(c instanceof Node ? c : document.createTextNode(String(c)));
  return el;
}
const frag = (...kids) => { const f = document.createDocumentFragment(); for (const c of kids.flat(Infinity)) if (c !== null && c !== undefined && c !== false) f.append(c instanceof Node ? c : document.createTextNode(String(c))); return f; };
const esc = (s) => String(s ?? '');
const plural = (n, w, ws = `${w}s`) => `${n} ${n === 1 ? w : ws}`;
const draftHref = (p) => `#/draft/${encodeURIComponent(p)}`;
const store = { get: (k, d) => { try { const v = localStorage.getItem(k); return v === null ? d : JSON.parse(v); } catch { return d; } }, set: (k, v) => { try { localStorage.setItem(k, JSON.stringify(v)); } catch { /* private window */ } }, del: (k) => { try { localStorage.removeItem(k); } catch { /* ignore */ } } };
function toast(msg, err = false) { const t = h('div', { class: `toast${err ? ' err' : ''}`, text: msg }); document.body.append(t); setTimeout(() => t.remove(), err ? 6000 : 2500); }

async function api(path, init) {
  const res = await fetch(`/api/${path}`, { headers: { 'Content-Type': 'application/json' }, ...init });
  const data = await res.json().catch(() => ({ error: `${res.status}` }));
  if (!res.ok || data.error) throw new Error(data.error || `${res.status}`);
  return data;
}
async function send(record) {
  const out = await api('reviews', { method: 'POST', body: JSON.stringify(record) });
  state.mine.inbox.push(out.file.split('/').pop());
  return out;
}

// ---------------------------------------------------------------- data
function draftsIndex(kb) {
  // drafts = findings whose source_status is draft/in_review, grouped by source_path
  const by = new Map();
  for (const f of kb.findings || []) {
    if (!['draft', 'in_review'].includes(f.source_status)) continue;
    const p = f.source_path;
    (by.get(p) || by.set(p, { path: p, entry: f.source_id, kind: f.source_kind, citation: f.citation, findings: [] }).get(p)).findings.push(f);
  }
  return [...by.values()].sort((a, b) => String(a.citation).localeCompare(String(b.citation)) || a.path.localeCompare(b.path));
}
const entryName = (id) => state.kb?.entries?.[id]?.name || String(id || '').replace(/_/g, ' ');
const paperPdf = (citation) => state.manifest?.papers?.[citation] || null;
const myRecords = () => [...state.mine.inbox, ...state.mine.applied].filter((n) => n.includes(`_${slug(state.me?.email?.split('@')[0])}_`));
const slug = (s) => String(s || '').toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '').slice(0, 40);
const reviewedBy = (id) => { const s = slug(id.replace(/^drafts\//, '').replace(/\.md$/, '')); return [...state.mine.inbox, ...state.mine.applied].filter((n) => n.endsWith(`_${s}.json`)).map((n) => n.split('_')[2]); };

// ---------------------------------------------------------------- views
function home() {
  const drafts = draftsIndex(state.kb);
  const sc = state.screening?.candidates || [];
  const ta = sc.filter((c) => ['awaiting_ta', 'unsure_ta'].includes(c.stage));
  const ft = sc.filter((c) => ['awaiting_ft', 'unsure_ft'].includes(c.stage));
  const m = state.manifest || {};
  return frag(
    h('div', { class: 'page-head' }, h('h1', { text: 'Review portal' }), h('span', { class: 'muted small', text: `KB ${m.kbCommit || '?'} (${m.kbDate || '?'}) · built ${m.built || '?'}` })),
    h('p', {}, `You are signed in as ${state.me.email}. Everything you decide here is sent to the knowledge base's repository under that name and applied by the maintainer; the governance policy still decides who may approve what.`),
    h('div', { class: 'tiles' },
      h('a', { class: 'tile tile-link', href: '#/drafts' }, h('div', { class: 'value', text: String(drafts.length) }), h('div', { class: 'label', text: 'drafts to review' }), h('div', { class: 'detail', text: `${drafts.reduce((n, d) => n + d.findings.length, 0)} findings` })),
      h('a', { class: 'tile tile-link', href: '#/screen/ta' }, h('div', { class: 'value', text: String(ta.length) }), h('div', { class: 'label', text: 'titles/abstracts to screen' })),
      h('a', { class: 'tile tile-link', href: '#/screen/ft' }, h('div', { class: 'value', text: String(ft.length) }), h('div', { class: 'label', text: 'full texts to assess' })),
      h('div', { class: 'tile' }, h('div', { class: 'value', text: String(m.counts?.private ?? 0) }), h('div', { class: 'label', text: 'annotated PDFs here (private)' }), h('div', { class: 'detail', text: `${m.counts?.public ?? 0} more are public (Creative Commons)` })),
      h('a', { class: 'tile tile-link', href: '#/mine' }, h('div', { class: 'value', text: String(myRecords().length) }), h('div', { class: 'label', text: 'reviews you have sent' }))),
    h('h2', { text: 'How to review' }),
    h('p', { class: 'small' }, 'A draft is what the local model extracted from one paper: findings, each with the verbatim passages that support it. Open it beside the annotated PDF (the highlights are the passages, in the colour of what they support) and say, finding by finding, whether the claim is what the paper shows. Fix a field when the paper says otherwise, select words in the PDF to add a passage or to mark something the extractor missed, then send the review. For screening, read the title and abstract (or the full text) against the eligibility criteria in SCREENING.md and include or exclude with a reason.'),
    h('p', { class: 'small muted', text: 'Keys in the screening queues: i include · e exclude (then a reason) · u unsure · click a card first.' }));
}

function draftsList() {
  const drafts = draftsIndex(state.kb);
  const byPaper = new Map();
  for (const d of drafts) (byPaper.get(d.citation) || byPaper.set(d.citation, []).get(d.citation)).push(d);
  const rows = [];
  for (const [cit, ds] of [...byPaper.entries()].sort((a, b) => String(a[0]).localeCompare(String(b[0])))) {
    const pdf = paperPdf(cit);
    rows.push(h('tr', { class: 'paper-row' }, h('th', { colspan: 5 }, h('span', { class: 'chip', text: cit }), ' ', h('span', { class: 'small muted', text: (state.kb.citations?.[cit] || '').slice(0, 140) }), ' ',
      pdf ? h('span', { class: `badge ${pdf.public ? 'badge-human' : 'badge-kind'}`, text: pdf.public ? 'annotated PDF, public' : 'annotated PDF, here' }) : h('span', { class: 'badge badge-warn', text: 'no annotated PDF in the portal' }))));
    for (const d of ds) {
      const who = reviewedBy(d.path);
      rows.push(h('tr', {}, h('td', {}, h('a', { href: draftHref(d.path), text: d.path.replace(/^drafts\//, '') })), h('td', { text: entryName(d.entry) }), h('td', { text: d.kind }),
        h('td', { class: 'num', text: String(d.findings.length) }), h('td', { class: 'small muted', text: who.length ? `reviewed by ${[...new Set(who)].join(', ')}` : '' })));
    }
  }
  return frag(h('div', { class: 'page-head' }, h('h1', { text: 'Drafts awaiting review' }), h('span', { class: 'muted small', text: `${drafts.length} drafts · ${byPaper.size} papers` })),
    h('p', { class: 'small', text: 'One draft is one entry (a region, impairment, therapy or predictor) as read from one paper. Open it to review each finding against the paper.' }),
    h('table', { class: 'queue' }, h('thead', {}, h('tr', {}, h('th', { text: 'Draft' }), h('th', { text: 'Entry' }), h('th', { text: 'Kind' }), h('th', { class: 'num', text: 'Findings' }), h('th', { text: '' }))), h('tbody', {}, rows)));
}

// ---- one draft beside its PDF ----
function draftView(path) {
  const d = draftsIndex(state.kb).find((x) => x.path === path);
  if (!d) return h('p', { class: 'error', text: `No draft ${path} in this export (it may have been promoted or rejected since the portal was built).` });
  const key = `review:${path}`;
  const r = store.get(key, { verdict: '', rationale: '', findings: {}, marks: [], comments: {} });
  const save = () => store.set(key, r);
  const pdf = paperPdf(d.citation);
  state.draft = { path, d, r, save, pdf };
  const left = draftLeft(d, r, save, pdf, path);
  const right = h('div', { class: 'right' });
  const layout = h('div', { class: 'review-layout', 'data-path': path }, left, right);
  if (pdf) mountPdf(right, pdf.annotated, d, r, save);
  else right.append(h('div', { class: 'pdf-missing' }, h('h3', { text: 'No annotated PDF here' }), h('p', { text: 'The portal holds annotated PDFs that the maintainer has published: Creative-Commons papers publicly and the others for signed-in reviewers. This paper is not among them yet.' }), state.kb.citationLinks?.[d.citation] ? h('p', {}, h('a', { href: state.kb.citationLinks[d.citation], target: '_blank', rel: 'noopener', text: 'Open the paper at the publisher' })) : null));
  return layout;
}

function draftLeft(d, r, save, pdf, path) {
  const left = h('div', { class: 'left' });
  left.append(h('div', { class: 'page-head' }, h('h1', { text: entryName(d.entry) }), h('span', { class: 'chip', text: d.citation })),
    h('p', { class: 'small muted' }, `${path} · ${plural(d.findings.length, 'finding')} · `, h('a', { href: '#/drafts', text: 'all drafts' }), pdf ? '' : ' · no annotated PDF in the portal for this paper: review from the quotes, or ask the maintainer to add it'),
    h('p', { class: 'small' }, 'For each finding: does the paper show this? ', h('b', { text: 'agree' }), ' when the claim, direction and strength are what the passages say; ', h('b', { text: 'disagree' }), ' with a concern when not; ', h('b', { text: 'unsure' }), ' when you cannot tell. Fix a field in place when the paper says otherwise (it is sent as an edit). Select words in the PDF to add a passage to a finding, or to mark something no finding covers.'));
  for (const f of d.findings) left.append(findingCard(d, f, r, save, pdf));
  left.append(marksPanel(r, save));
  left.append(verdictPanel(d, r, save));
  return left;
}

function findingCard(d, f, r, save, pdf) {
  const fr = (r.findings[f.id] = r.findings[f.id] || { verdict: '', concern: '', edits: {}, passages: {}, added: [] });
  const field = (k, label) => {
    const cur = fr.edits[k] !== undefined ? fr.edits[k] : f[k];
    const changed = fr.edits[k] !== undefined && fr.edits[k] !== f[k];
    const onchange = (v) => { if (v === String(f[k] ?? '')) delete fr.edits[k]; else fr.edits[k] = v; save(); render(); };
    const ctrl = VOCAB[k] ? h('select', { class: changed ? 'changed' : '', onchange: (e) => onchange(e.target.value) }, VOCAB[k].map((o) => h('option', { value: o, selected: cur === o ? '' : null, text: o })), VOCAB[k].includes(cur) ? null : h('option', { value: cur ?? '', selected: '', text: `${cur ?? '(unset)'}` }))
      : h('input', { type: 'text', class: changed ? 'changed' : '', value: esc(cur), style: 'flex:1;min-width:12em', onchange: (e) => onchange(e.target.value.trim()) });
    return h('div', { class: 'field' }, h('label', { text: label }), ctrl, changed ? h('span', { class: 'small muted', text: `was: ${esc(f[k])}` }) : null);
  };
  const claimCur = fr.edits.claim !== undefined ? fr.edits.claim : f.claim;
  const card = h('article', { class: 'finding', id: `f-${f.id}` },
    h('p', { class: 'route' }, h('span', { class: 'badge badge-kind', text: f.id }), ' ', entryName(f.source_id), ' → ', h('b', { text: entryName(fr.edits.target ?? f.target) }), ` (${fr.edits.target_kind ?? f.target_kind}) · ${Array.isArray(f.method) ? f.method.join(', ') : esc(f.method)}${f.therapy?.name ? ` · therapy: ${f.therapy.name}` : ''}`),
    h('textarea', { rows: 3, class: fr.edits.claim !== undefined ? 'changed' : '', onchange: (e) => { const v = e.target.value.trim(); if (v === String(f.claim || '').trim()) delete fr.edits.claim; else fr.edits.claim = v; save(); } }, esc(claimCur)),
    h('div', { class: 'field' }, field('direction', 'direction'), field('relationship', 'relationship'), field('strength', 'strength')),
    h('div', { class: 'field' }, field('target', 'target'), field('target_kind', 'target kind')),
    f.sample ? h('p', { class: 'small muted', text: `sample: ${Object.entries(f.sample).filter(([, v]) => v).map(([k, v]) => `${k} ${v}`).join(' · ')}` }) : null,
    f.statistics && Object.keys(f.statistics).length ? h('p', { class: 'small muted', text: `statistics: ${Object.entries(f.statistics).filter(([, v]) => v).map(([k, v]) => `${k} ${v}`).join(' · ')}` }) : null,
    f.author_limitations?.length ? h('p', { class: 'small muted', text: `authors' limitations: ${f.author_limitations.join('; ')}` }) : null,
    f.flags?.length ? h('p', { class: 'small muted', text: `extractor flags: ${f.flags.join('; ')}` }) : null,
    h('h4', { text: 'Source passages' }),
    (f.source_passages || []).map((p, i) => passageCard(f, p, i, fr, save, pdf)),
    fr.added.map((p, i) => h('div', { class: 'passage', style: 'border-left-color:var(--grape)' }, h('div', { class: 'meta' }, h('span', { class: 'badge badge-kind', text: 'added by you' }), ` page ${p.page} · supports ${p.supports}`, h('button', { class: 'btn', onclick: () => { fr.added.splice(i, 1); save(); render(); }, text: 'remove' })), h('div', { text: `“${p.quote}”` }))),
    h('div', { class: 'fverdict' }, h('span', { class: 'muted', text: 'Your verdict:' }),
      ['agree', 'disagree', 'unsure'].map((v) => h('label', {}, h('input', { type: 'radio', name: `v-${f.id}`, value: v, checked: fr.verdict === v ? '' : null, onchange: () => { fr.verdict = v; save(); } }), ` ${v}`))),
    h('textarea', { rows: 2, placeholder: 'concern or comment (required for disagree): what the paper says instead, which passage is wrong …', onchange: (e) => { fr.concern = e.target.value.trim(); save(); } }, esc(fr.concern)));
  return card;
}

function passageCard(f, p, i, fr, save, pdf) {
  const pk = String(i);
  const flag = fr.passages[pk] || '';
  const colours = state.kb.rules?.supportsColors || { claim: '#a8c8ff', sample: '#a8e6a3', statistics: '#ffcc99', method: '#fff4a3', region_definition: '#d9b3e6', imaging_details: '#d9b3e6', limitation: '#ffb3b3', confounders: '#cccccc' };
  return h('div', { class: `passage${flag ? ' flagged' : ''}`, style: `border-left-color:${colours[p.supports] || '#ccc'}` },
    h('div', { class: 'meta' }, h('span', { text: `supports ${esc(p.supports)}` }), p.page ? h('span', { text: `page ${p.page}` }) : null, p.section ? h('span', { text: esc(p.section) }) : null,
      pdf && p.page ? h('button', { class: 'btn', onclick: () => goToPage(Number(p.page), p.quote), text: 'show in paper' }) : null,
      h('select', { onchange: (e) => { if (e.target.value) fr.passages[pk] = e.target.value; else delete fr.passages[pk]; save(); render(); } },
        [['', 'passage is fine'], ['not_in_paper', 'not in the paper'], ['wrong_page', 'wrong page'], ['does_not_support', 'does not support the claim'], ['truncated', 'truncated / altered']].map(([v, t]) => h('option', { value: v, selected: flag === v ? '' : null, text: t })))),
    h('div', { text: `“${esc(p.quote)}”` }));
}

function marksPanel(r, save) {
  return h('div', { class: 'marks' }, h('h4', { text: `Passages no finding covers (${r.marks.length})` }),
    h('p', { class: 'small muted', text: 'Select words in the paper and choose "Mark for re-extraction": the maintainer runs the extractor on exactly these passages.' }),
    r.marks.map((m, i) => h('div', { class: 'mark' }, h('div', {}, h('div', { class: 'quote', text: `“${m.quote}”` }), h('div', { class: 'small muted', text: `page ${m.page}` }), h('input', { type: 'text', value: m.note || '', placeholder: 'what this passage shows (for the extractor)', style: 'width:100%;margin-top:.2rem', onchange: (e) => { m.note = e.target.value; save(); } })),
      h('button', { class: 'btn', onclick: () => { r.marks.splice(i, 1); save(); render(); }, text: 'remove' }))));
}

function verdictPanel(d, r, save) {
  const pending = Object.values(r.findings).filter((x) => x.verdict).length;
  const total = d.findings.length;
  const edits = Object.entries(r.findings).filter(([, x]) => Object.keys(x.edits).length || x.added.length || Object.keys(x.passages).length).length;
  const bar = h('div', { class: 'submitbar' });
  const btn = h('button', { class: 'btn btn-primary', disabled: pending === 0 && edits === 0 && r.marks.length === 0 ? '' : null, text: 'Send this review', onclick: async () => {
    const missing = d.findings.filter((f) => r.findings[f.id]?.verdict === 'disagree' && !r.findings[f.id]?.concern);
    if (missing.length) { toast(`Say why you disagree on ${missing.map((f) => f.id).join(', ')}`, true); return; }
    if (!r.verdict && pending === total) { toast('Give an overall verdict for the draft', true); return; }
    btn.disabled = true; btn.textContent = 'Sending…';
    try {
      const sent = [];
      const perFinding = d.findings.filter((f) => r.findings[f.id]?.verdict).map((f) => ({ id: f.id, verdict: r.findings[f.id].verdict, concern: r.findings[f.id].concern || '', supports_approval: r.findings[f.id].verdict === 'agree', passages: r.findings[f.id].passages }));
      if (perFinding.length || r.verdict) sent.push(await send({ kind: 'verdict', id: d.path, citation: d.citation, verdict: r.verdict || null, rationale: r.rationale || '', per_finding: perFinding }));
      for (const f of d.findings) {
        const x = r.findings[f.id]; if (!x) continue;
        if (Object.keys(x.edits).length || x.added.length) sent.push(await send({ kind: 'edit', id: d.path, citation: d.citation, finding: f.id, fields: Object.fromEntries(Object.entries(x.edits).map(([k, v]) => [k, { old: f[k], new: v }])), passages_added: x.added }));
      }
      for (const m of r.marks) sent.push(await send({ kind: 'mark', id: d.path, citation: d.citation, page: m.page, quote: m.quote, note: m.note || '' }));
      store.del(`review:${d.path}`);
      toast(`Sent ${plural(sent.length, 'record')} — thank you`);
      location.hash = '#/drafts';
    } catch (e) { toast(`Not sent: ${e.message}`, true); btn.disabled = false; btn.textContent = 'Send this review'; }
  } });
  bar.append(btn, h('span', { class: 'pending', text: `${pending} of ${total} findings decided${edits ? ` · ${edits} edited` : ''}${r.marks.length ? ` · ${r.marks.length} marks` : ''}` }), h('span', { class: 'small muted', text: 'Saved in this browser until you send.' }));
  return frag(h('div', { class: 'verdict' }, h('h4', { text: 'Overall' }),
    h('div', { class: 'row' }, h('span', { class: 'muted', text: 'This draft should be' }), ['approve', 'agree_defer', 'reject'].map((v) => h('label', {}, h('input', { type: 'radio', name: 'overall', value: v, checked: r.verdict === v ? '' : null, onchange: () => { r.verdict = v; save(); } }), ` ${v === 'agree_defer' ? 'kept for more review' : v === 'approve' ? 'approved' : 'rejected'}`))),
    h('textarea', { rows: 2, placeholder: 'rationale, 1–3 sentences', onchange: (e) => { r.rationale = e.target.value.trim(); save(); } }, esc(r.rationale)),
    h('p', { class: 'small muted', text: 'Only a person named in the governance policy approves; if that is not you, your verdict is recorded as an opinion the maintainer reads before promoting.' })), bar);
}

// ---- screening ----
function screenView(stage) {
  const sc = state.screening;
  if (!sc) return h('p', { class: 'notice', text: 'No screening queue in this build of the portal.' });
  const stages = stage === 'ta' ? ['awaiting_ta', 'unsure_ta'] : ['awaiting_ft', 'unsure_ft'];
  const key = `screen:${stage}`;
  const decided = store.get(key, {});
  const cands = sc.candidates.filter((c) => stages.includes(c.stage));
  const reasons = Object.entries(sc.reasons || {}).filter(([, v]) => stage === 'ft' || !v.fullTextOnly);
  const head = h('div', { class: 'page-head' }, h('h1', { text: stage === 'ta' ? 'Title/abstract screening' : 'Full-text screening' }), h('span', { class: 'muted small', text: `${cands.length} awaiting · ${Object.keys(decided).length} decided here, not yet sent` }),
    h('button', { class: 'btn btn-primary', style: 'margin-left:auto', onclick: () => sendScreen(stage, decided, cands), text: 'Send decisions' }));
  const list = h('div', {});
  for (const c of cands) {
    const dec = decided[c.id] || {};
    const pdf = c.key ? paperPdf(c.key) : null;
    const card = h('article', { class: `screen${dec.decision ? ' done' : ''}`, tabindex: '-1', 'data-id': c.id },
      h('p', { class: 't' }, h('span', { class: 'chip', text: c.id }), ' ', esc(c.title)),
      h('p', { class: 'small muted' }, [c.year, c.journal, (c.authors || '').slice(0, 120)].filter(Boolean).join(' · '), c.doi ? [' · ', h('a', { href: `https://doi.org/${c.doi}`, target: '_blank', rel: 'noopener', text: c.doi })] : null, c.pmid ? [' · PMID ', h('a', { href: `https://pubmed.ncbi.nlm.nih.gov/${c.pmid}`, target: '_blank', rel: 'noopener', text: String(c.pmid) })] : null,
        c.for?.length ? ` · for ${c.for.join(', ')}` : '', c.history?.length ? ` · ${c.history.map((x) => `${x.stage === 'title_abstract' ? 'T/A' : 'FT'}: ${x.decision} (${x.by})`).join('; ')}` : '',
        pdf ? [' · ', h('a', { href: pdf.annotated, target: '_blank', rel: 'noopener', text: 'annotated PDF' })] : (stage === 'ft' ? ' · no PDF in the portal' : '')),
      h('p', { class: 'ab', text: c.abstract || '(no abstract available)' }),
      c.suggestion?.decision ? h('p', { class: 'sug', text: `Model suggests ${c.suggestion.decision}${c.suggestion.reason && c.suggestion.reason !== 'none' ? ` (${c.suggestion.reason})` : ''} — a suggestion, not a decision.` }) : null,
      h('div', { class: 'dec' }, ['include', 'exclude', 'unsure'].map((v) => h('label', {}, h('input', { type: 'radio', name: `s-${c.id}`, value: v, checked: dec.decision === v ? '' : null, onchange: () => { decided[c.id] = { ...dec, decision: v }; store.set(key, decided); card.classList.add('done'); } }), ` ${v}`)),
        h('select', { onchange: (e) => { decided[c.id] = { ...(decided[c.id] || {}), reason: e.target.value }; store.set(key, decided); } }, h('option', { value: '', text: 'reason…' }), reasons.map(([k, v]) => h('option', { value: k, selected: dec.reason === k ? '' : null, text: v.label }))),
        h('input', { type: 'text', value: dec.note || '', placeholder: 'note', style: 'min-width:220px', onchange: (e) => { decided[c.id] = { ...(decided[c.id] || {}), note: e.target.value }; store.set(key, decided); } })));
    list.append(card);
  }
  if (!cands.length) list.append(h('p', { class: 'notice', text: 'Nothing awaiting a decision at this stage.' }));
  const onkey = (e) => {
    if (e.target.tagName === 'INPUT' && e.target.type === 'text') return;
    const card = document.activeElement?.closest?.('.screen'); if (!card) return;
    const map = { i: 'include', e: 'exclude', u: 'unsure' }; const v = map[e.key]; if (!v) return;
    const radio = card.querySelector(`input[type=radio][value="${v}"]`); if (radio) { radio.checked = true; radio.dispatchEvent(new Event('change')); }
    if (v === 'exclude') card.querySelector('select').focus(); else { const next = card.nextElementSibling; if (next) { next.focus(); next.scrollIntoView({ block: 'center' }); } }
    e.preventDefault();
  };
  document.addEventListener('keydown', onkey, { once: false });
  state.keyHandler = onkey;
  return frag(head, h('p', { class: 'small', text: `Criteria: docs/SCREENING.md §2. ${stage === 'ta' ? 'Include whatever might answer one of the KB questions; exclude only for a listed reason.' : 'Read the paper; include when it answers a question in §1 and no exclusion reason applies.'} Decisions are kept in this browser until you send them.` }), list);
}

async function sendScreen(stage, decided, cands) {
  const st = stage === 'ta' ? 'title_abstract' : 'full_text';
  const items = Object.entries(decided).filter(([, d]) => d.decision);
  if (!items.length) { toast('Nothing decided yet', true); return; }
  const bad = items.filter(([, d]) => d.decision === 'exclude' && !d.reason);
  if (bad.length) { toast(`An exclusion needs a reason: ${bad.map(([id]) => id).join(', ')}`, true); return; }
  let n = 0;
  try {
    for (const [id, d] of items) {
      await send({ kind: 'screen', id, stage: st, decision: d.decision, reason: d.decision === 'exclude' ? d.reason : null, note: d.note || '' });
      delete decided[id]; store.set(`screen:${stage}`, decided); n += 1;
    }
    toast(`Sent ${plural(n, 'decision')} — thank you`);
    render();
  } catch (e) { toast(`Sent ${n}; then: ${e.message}`, true); }
}

function mine() {
  const names = myRecords().sort().reverse();
  const row = (n, applied) => { const [stamp, kind, , ...rest] = n.replace(/\.json$/, '').split('_'); return h('tr', {}, h('td', { text: `${stamp.slice(0, 4)}-${stamp.slice(4, 6)}-${stamp.slice(6, 8)} ${stamp.slice(9, 11)}:${stamp.slice(11, 13)}` }), h('td', { text: kind }), h('td', { text: rest.join('_') }), h('td', {}, h('span', { class: `badge ${applied ? 'badge-human' : 'badge-legacy'}`, text: applied ? 'applied' : 'waiting for the maintainer' }))); };
  return frag(h('div', { class: 'page-head' }, h('h1', { text: 'Reviews you have sent' }), h('span', { class: 'muted small', text: `${names.length} records` })),
    h('p', { class: 'small', text: 'Each record is a file in the repository (logs/portal/). "Applied" means the maintainer has run it into the register or the draft; the explorer shows the result after the next export.' }),
    names.length ? h('table', {}, h('thead', {}, h('tr', {}, h('th', { text: 'Sent' }), h('th', { text: 'Kind' }), h('th', { text: 'About' }), h('th', { text: 'State' }))), h('tbody', {}, names.map((n) => row(n, state.mine.applied.includes(n))))) : h('p', { class: 'notice', text: 'Nothing sent yet.' }));
}

// ---------------------------------------------------------------- PDF pane (pdf.js)
async function pdfjs() {
  if (state.pdfjs) return state.pdfjs;
  const lib = await import(PDFJS);
  lib.GlobalWorkerOptions.workerSrc = PDFJS_WORKER;
  state.pdfjs = lib;
  return lib;
}
async function mountPdf(right, url, d, r, save) {
  const bar = h('div', { class: 'pdfbar' }, h('span', { class: 'muted', text: url.split('/').pop() }),
    h('span', { class: 'zoom' }, h('button', { class: 'btn', onclick: () => setZoom(right, -0.15), text: '−' }), h('span', { id: 'zoomLabel', class: 'muted', text: `${Math.round(state.zoom * 100)}%` }), h('button', { class: 'btn', onclick: () => setZoom(right, 0.15), text: '+' })),
    h('a', { href: url, target: '_blank', rel: 'noopener', class: 'small', text: 'open the PDF itself' }),
    h('span', { class: 'small muted', text: 'Highlights are the draft’s passages. Drag across words to quote them.' }));
  const pages = h('div', { id: 'pdfpages' });
  right.append(bar, pages);
  try {
    const lib = await pdfjs();
    const doc = await lib.getDocument({ url }).promise;
    state.docs.set(url, doc);
    right.dataset.url = url;
    layoutPages(right, doc, d, r, save);
  } catch (e) {
    pages.append(h('div', { class: 'pdf-missing' }, h('h3', { text: 'The PDF could not be loaded' }), h('p', { text: e.message })));
  }
}
function setZoom(right, dz) { state.zoom = Math.max(0.5, Math.min(2.5, state.zoom + dz)); const doc = state.docs.get(right.dataset.url); if (doc) layoutPages(right, doc, null, null, null, true); document.getElementById('zoomLabel').textContent = `${Math.round(state.zoom * 100)}%`; }
async function layoutPages(right, doc, d, r, save, keepScroll = false) {
  const wrap = document.getElementById('pdfpages'); const frac = keepScroll ? right.scrollTop / Math.max(1, wrap.scrollHeight) : 0;
  wrap.replaceChildren();
  const width = Math.min(900, right.clientWidth - 40) * state.zoom;
  const first = await doc.getPage(1); const vp0 = first.getViewport({ scale: 1 });
  const scale = width / vp0.width;
  for (let n = 1; n <= doc.numPages; n += 1) {
    wrap.append(h('div', { class: 'pdfpage', id: `page-${n}`, 'data-n': n, style: `width:${width}px;height:${vp0.height * scale}px` }, h('span', { class: 'pno', text: `p. ${n}` })));
  }
  const io = new IntersectionObserver((entries) => { for (const e of entries) if (e.isIntersecting) renderPage(doc, e.target, scale); }, { root: right, rootMargin: '800px 0px' });
  wrap.querySelectorAll('.pdfpage').forEach((el) => io.observe(el));
  if (!right.dataset.wired) { right.dataset.wired = '1'; right.addEventListener('mousedown', selStart); right.addEventListener('mousemove', selMove); document.addEventListener('mouseup', selEnd); }
  state.reviewCtx = { d, r, save };
  if (keepScroll) right.scrollTop = frac * wrap.scrollHeight;
}
async function renderPage(doc, el, scale) {
  if (el.dataset.loaded) return; el.dataset.loaded = '1';
  const n = Number(el.dataset.n);
  const page = await doc.getPage(n);
  const vp = page.getViewport({ scale });
  const canvas = h('canvas', { width: Math.floor(vp.width * devicePixelRatio), height: Math.floor(vp.height * devicePixelRatio) });
  el.style.height = `${vp.height}px`;
  const ctx = canvas.getContext('2d'); ctx.scale(devicePixelRatio, devicePixelRatio);
  const lib = state.pdfjs;
  await page.render({ canvasContext: ctx, viewport: vp, annotationMode: lib.AnnotationMode.ENABLE }).promise;
  el.prepend(canvas);
  // Word layer for selection: pdf.js text items are runs (often whole lines), so each run is
  // split into words placed by measured widths, scaled so the words fill the run's width.
  const text = await page.getTextContent();
  const layer = h('div', { class: 'textlayer' });
  const measure = document.createElement('canvas').getContext('2d');
  let wi = 0;
  for (const it of text.items) {
    if (!it.str || !it.str.trim()) continue;
    const tx = lib.Util.transform(vp.transform, it.transform);
    const fontH = Math.hypot(tx[2], tx[3]);
    const x0 = tx[4]; const y = tx[5] - fontH;
    const runW = it.width * scale;
    const family = text.styles?.[it.fontName]?.fontFamily || 'sans-serif';
    measure.font = `${fontH}px ${family}`;
    const total = Math.max(1, measure.measureText(it.str).width);
    const k = runW / total;
    const re = /\S+/g; let m;
    while ((m = re.exec(it.str))) {
      const before = measure.measureText(it.str.slice(0, m.index)).width * k;
      const w = Math.max(2, measure.measureText(m[0]).width * k);
      layer.append(h('span', { class: 't', 'data-i': wi, 'data-t': m[0], 'data-p': n, style: `left:${x0 + before}px;top:${y}px;font-size:${fontH}px;width:${w}px;height:${fontH * 1.1}px`, text: m[0] }));
      wi += 1;
    }
  }
  el.append(layer);
}
function goToPage(n, quote) {
  const el = document.getElementById(`page-${n}`); const right = el?.closest('.right'); if (!el || !right) return;
  right.scrollTo({ top: el.offsetTop - 60, behavior: 'smooth' });
  const tryMark = () => {
    const spans = [...el.querySelectorAll('.t')]; if (!spans.length) { setTimeout(tryMark, 300); return; }
    const norm = (s) => s.toLowerCase().replace(/[^a-z0-9]+/g, ' ').trim();
    const head = norm(String(quote || '')).split(' ').slice(0, 6).join(' ');
    if (!head) return;
    let acc = ''; const idx = [];
    for (const s of spans) { acc += ` ${norm(s.dataset.t)}`; idx.push(acc.length); }
    const at = acc.indexOf(head);
    if (at < 0) return;
    const i = idx.findIndex((end) => end > at); const s = spans[Math.max(0, i)];
    if (s) { const m = h('div', { class: 'target', style: `left:${s.offsetLeft - 4}px;top:${s.offsetTop - 4}px;width:${s.offsetWidth + 8}px;height:${s.offsetHeight + 8}px` }); el.append(m); right.scrollTo({ top: el.offsetTop + s.offsetTop - 160, behavior: 'smooth' }); setTimeout(() => m.remove(), 3000); }
  };
  tryMark();
}
// ---- word selection → quote ----
const wordAt = (e) => (e.target?.classList?.contains('t') ? e.target : null);
function selStart(e) { const w = wordAt(e); clearSel(); if (!w || e.button !== 0) return; state.sel = { a: Number(w.dataset.i), b: Number(w.dataset.i), layer: w.parentElement, page: Number(w.dataset.p) }; paintSel(); e.preventDefault(); }
function selMove(e) { if (!state.sel) return; const w = wordAt(e); if (!w || w.parentElement !== state.sel.layer) return; state.sel.b = Number(w.dataset.i); paintSel(); }
function paintSel() { const { a, b, layer } = state.sel; const lo = Math.min(a, b); const hi = Math.max(a, b); layer.querySelectorAll('.t').forEach((x) => { const i = Number(x.dataset.i); x.classList.toggle('sel', i >= lo && i <= hi); }); }
function selEnd(e) {
  if (!state.sel) return; const { a, b, layer, page } = state.sel; state.sel = null;
  const lo = Math.min(a, b); const hi = Math.max(a, b);
  const quote = [...layer.querySelectorAll('.t')].filter((x) => { const i = Number(x.dataset.i); return i >= lo && i <= hi; }).map((x) => x.dataset.t).join(' ').replace(/\s+/g, ' ').replace(/-\s+(?=[a-z])/g, '').trim();
  if (!quote) { clearSel(); return; }
  showSelTool(e.clientX, e.clientY, quote, page);
}
function clearSel() { document.querySelectorAll('.t.sel').forEach((x) => x.classList.remove('sel')); document.getElementById('seltool')?.remove(); }
function showSelTool(x, y, quote, page) {
  document.getElementById('seltool')?.remove();
  const ctx = state.reviewCtx; if (!ctx?.d) return;
  const fsel = h('select', {}, ctx.d.findings.map((f) => h('option', { value: f.id, text: `${f.id} · ${String(f.claim || '').slice(0, 50)}` })));
  const ssel = h('select', {}, VOCAB.supports.map((o) => h('option', { value: o, text: o })));
  const note = h('input', { type: 'text', placeholder: 'note for the extractor (optional)', style: 'width:100%;margin-top:.3rem' });
  const tool = h('div', { id: 'seltool', style: `left:${Math.min(x, window.innerWidth - 460)}px;top:${Math.min(y + 12, window.innerHeight - 180)}px` },
    h('div', { class: 'small muted', text: `page ${page} · ${quote.split(' ').length} words` }), h('div', { class: 'q', text: quote }),
    h('div', { class: 'actions' }, 'attach to ', fsel, ' as ', ssel, h('button', { class: 'btn btn-primary', onclick: () => { const fr = ctx.r.findings[fsel.value] = ctx.r.findings[fsel.value] || { verdict: '', concern: '', edits: {}, passages: {}, added: [] }; fr.added.push({ page, quote, supports: ssel.value }); ctx.save(); clearSel(); render(); }, text: 'Attach' })),
    note,
    h('div', { class: 'actions' }, h('button', { class: 'btn', onclick: () => { ctx.r.marks.push({ page, quote, note: note.value }); ctx.save(); clearSel(); render(); }, text: 'Mark for re-extraction' }), h('button', { class: 'btn', onclick: () => navigator.clipboard?.writeText(quote), text: 'Copy' }), h('button', { class: 'btn', onclick: clearSel, text: 'Cancel' })));
  document.body.append(tool);
}

// ---------------------------------------------------------------- shell
function parseRoute() { const raw = location.hash.replace(/^#/, '') || '/'; return raw.split('/').filter(Boolean).map(decodeURIComponent); }
function render() {
  const main = document.getElementById('main');
  if (state.keyHandler) { document.removeEventListener('keydown', state.keyHandler); state.keyHandler = null; }
  const [head, ...rest] = parseRoute();
  // An edit inside a draft re-renders only the left pane: the PDF pane keeps its pages and scroll.
  const existing = main.querySelector('.review-layout');
  if (head === 'draft' && existing && existing.dataset.path === rest.join('/') && state.draft) {
    const leftEl = existing.querySelector('.left'); const top = leftEl.scrollTop;
    const { d, r, save, pdf, path } = state.draft;
    leftEl.replaceWith(draftLeft(d, r, save, pdf, path));
    existing.querySelector('.left').scrollTop = top;
    return;
  }
  let view; let current = '/';
  try {
    if (!head) view = home();
    else if (head === 'drafts') { view = draftsList(); current = '/drafts'; }
    else if (head === 'draft') { view = draftView(rest.join('/')); current = '/drafts'; }
    else if (head === 'screen') { view = screenView(rest[0] === 'ft' ? 'ft' : 'ta'); current = `/screen/${rest[0] === 'ft' ? 'ft' : 'ta'}`; }
    else if (head === 'mine') { view = mine(); current = '/mine'; }
    else view = h('p', { class: 'error', text: `Unknown page: ${head}` });
  } catch (err) { console.error(err); view = h('p', { class: 'error', text: `This page could not be rendered: ${err.message}` }); }
  main.replaceChildren(view);
  for (const a of document.querySelectorAll('.nav a')) { if (a.getAttribute('href') === `#${current}`) a.setAttribute('aria-current', 'page'); else a.removeAttribute('aria-current'); }
  if (head !== 'draft') window.scrollTo(0, 0);
}

async function init() {
  const main = document.getElementById('main');
  try {
    const [me, manifest, kb] = await Promise.all([api('me'), fetch('manifest.json').then((r) => r.json()), fetch('export/stroke-aphasia-kb-drafts.json').then((r) => r.json())]);
    state.me = me; state.manifest = manifest; state.kb = kb;
    state.screening = await fetch('screening.json').then((r) => (r.ok ? r.json() : null)).catch(() => null);
    state.mine = await api('reviews').catch(() => ({ inbox: [], applied: [] }));
    document.getElementById('who').textContent = me.email;
    document.getElementById('footerVersion').textContent = `KB ${manifest.kbCommit || '?'} · ${kb.findings?.length ?? 0} findings in the drafts export · portal built ${manifest.built || '?'}`;
    if (manifest.config?.explorerUrl) document.getElementById('explorerLink').href = manifest.config.explorerUrl;
    window.addEventListener('hashchange', render);
    render();
  } catch (e) {
    main.replaceChildren(h('div', { class: 'error' }, h('p', {}, h('b', { text: 'The portal could not start.' })), h('p', { text: e.message }), h('p', { class: 'small', text: 'If you reached this page without the Cloudflare Access sign-in, open the portal address again and sign in with the email the maintainer allow-listed.' })));
  }
}
init();
