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
//   #/pdfs             the included papers whose PDF nobody has yet, every annotated PDF the portal holds, and the uploads waiting for the maintainer
//   #/mine             the records you have sent
// A paper the portal lacks can be uploaded (any candidate; required before a full-text
// decision): the file goes to a private bucket via /api/upload and a `pdf` record tells the
// maintainer to pull it into papers/ (their OneDrive folder).
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
const state = { me: null, manifest: null, kb: null, screening: null, mine: { inbox: [], applied: [] }, uploads: [], uploadsOk: false, pdfjs: null, zoom: 1, sel: null, docs: new Map() };
const MAX_UPLOAD = 60 * 1024 * 1024;

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
/** Send records to the repository in one request = one commit, however many there are. */
async function sendAll(records) {
  if (!records.length) return { files: [] };
  const out = await api('reviews', { method: 'POST', body: JSON.stringify({ records }) });
  for (const f of out.files || [out.file]) state.mine.inbox.push(f.split('/').pop());
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
/** The maintainer has the paper's source PDF (annotated or not). */
const paperSource = (citation) => Boolean(citation && (paperPdf(citation) || (state.manifest?.sources?.keys || []).includes(citation)));
/** A candidate's PDF is with the maintainer: named after its key, or linked through `pdf_file`. */
const candidateHasPdf = (c) => Boolean(c.pdf_file) || paperSource(c.key);
/** An upload waiting in the bucket for this candidate id or citation key, if any. */
const uploadFor = (...ids) => state.uploads.find((u) => ids.filter(Boolean).some((id) => u.id === id || u.id === String(id).replace(/^@/, '') || `@${u.id}` === id)) || null;

/** The upload control: a file picker and a button; on success the upload joins state.uploads and the page re-renders. */
function uploadControl(id, citation, { required = false, label = null } = {}) {
  if (!state.uploadsOk) return h('span', { class: 'small muted', text: required ? 'Uploads are not enabled on this portal: ask the maintainer for the PDF.' : '' });
  const input = h('input', { type: 'file', accept: 'application/pdf,.pdf', 'aria-label': `PDF for ${id}` });
  let busy = false;
  const upload = async (file) => {
    if (busy) return;
    if (!file) { toast('Choose the PDF file first', true); return; }
    if (file.type !== 'application/pdf' && !/\.pdf$/i.test(file.name || '')) { toast(`${file.name || 'That file'} is not a PDF`, true); return; }
    if (file.size > MAX_UPLOAD) { toast(`That file is ${Math.round(file.size / 1048576)} MB; the limit is ${MAX_UPLOAD / 1048576} MB`, true); return; }
    busy = true; btn.disabled = true; btn.textContent = `Uploading ${Math.round(file.size / 1024)} KB…`;
    try {
      const q = new URLSearchParams({ id, name: file.name, citation: citation || '' });
      const res = await fetch(`/api/upload?${q}`, { method: 'POST', headers: { 'Content-Type': 'application/pdf' }, body: file });
      const data = await res.json().catch(() => ({ error: `${res.status}` }));
      if (!res.ok || data.error) throw new Error(data.error || `${res.status}`);
      state.uploads.push({ object: data.object, id, name: file.name, bytes: file.size, by: state.me.email, uploaded: new Date().toISOString() });
      if (data.file) state.mine.inbox.push(data.file.split('/').pop());
      toast(`PDF uploaded for ${id} — the maintainer will add it to the papers folder`);
      render();
    } catch (e) { toast(`Not uploaded: ${e.message}`, true); busy = false; btn.disabled = false; btn.textContent = label || 'Upload the PDF'; }
  };
  const btn = h('button', { class: `btn${required ? ' btn-primary' : ''}`, text: label || 'Upload the PDF', onclick: () => upload(input.files?.[0]) });
  const el = h('span', { class: 'upload' }, input, btn, h('span', { class: 'small muted', text: 'Choose a PDF or drop one here; up to 60 MB. It goes to the maintainer, never to the public site.' }));
  el.uploadFile = upload;                 // so a larger area (a table row, a screening card) can be the drop target too
  dropZone(el, upload);
  return el;
}

/** Make `zone` accept a dropped file: highlighted while a file is dragged over it, `onFile(file)` on drop. */
function dropZone(zone, onFile) {
  if (!onFile) return zone;
  let depth = 0;                          // dragenter/leave fire for every child; count them
  const hasFiles = (e) => [...(e.dataTransfer?.types || [])].includes('Files');
  zone.addEventListener('dragenter', (e) => { if (!hasFiles(e)) return; e.preventDefault(); depth += 1; zone.classList.add('dropping'); });
  zone.addEventListener('dragover', (e) => { if (!hasFiles(e)) return; e.preventDefault(); e.stopPropagation(); e.dataTransfer.dropEffect = 'copy'; });
  zone.addEventListener('dragleave', () => { depth = Math.max(0, depth - 1); if (!depth) zone.classList.remove('dropping'); });
  zone.addEventListener('drop', (e) => {
    if (!hasFiles(e)) return;
    e.preventDefault(); e.stopPropagation(); depth = 0; zone.classList.remove('dropping');
    const files = [...(e.dataTransfer.files || [])];
    if (files.length > 1) toast('One PDF per paper: taking the first file', true);
    onFile(files[0]);
  });
  return zone;
}
// A file dropped beside a drop zone must not make the browser open it and leave the page (unsent decisions live here).
window.addEventListener('dragover', (e) => { if ([...(e.dataTransfer?.types || [])].includes('Files')) { e.preventDefault(); e.dataTransfer.dropEffect = 'none'; } });
window.addEventListener('drop', (e) => { if ([...(e.dataTransfer?.types || [])].includes('Files')) e.preventDefault(); });
/** "PDF uploaded by … on …, waiting for the maintainer" */
const uploadedNote = (u) => h('span', { class: 'badge badge-warn', title: u.name, text: `PDF uploaded${u.by === state.me?.email ? ' by you' : u.by ? ` by ${u.by}` : ''}${u.uploaded ? ` on ${String(u.uploaded).slice(0, 10)}` : ''}, with the maintainer` });
const myRecords = () => [...state.mine.inbox, ...state.mine.applied].filter((n) => n.includes(`_${slug(state.me?.email?.split('@')[0])}_`));
/** Screening decisions sent from this browser and not yet applied (the candidate is still in its old stage): [{id, stage, decision}]. */
function pendingSent() {
  const sent = store.get('screen:sent', {});
  const cands = state.screening?.candidates || [];
  return Object.entries(sent).filter(([, v]) => v && typeof v === 'object').map(([id, v]) => ({ id, ...v })).filter((x) => cands.some((c) => c.id === x.id));
}
/** Candidates included at title/abstract (awaiting the full text) whose paper the maintainer does not have. */
const missingPdfs = () => (state.screening?.candidates || []).filter((c) => ['awaiting_ft', 'unsure_ft'].includes(c.stage) && !candidateHasPdf(c));
const slug = (s) => String(s || '').toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '').slice(0, 40);
const reviewedBy = (id) => { const s = slug(id.replace(/^drafts\//, '').replace(/\.md$/, '')); return [...state.mine.inbox, ...state.mine.applied].filter((n) => n.endsWith(`_${s}.json`)).map((n) => n.split('_')[2]); };

// ---------------------------------------------------------------- views
function home() {
  const drafts = draftsIndex(state.kb);
  const sc = state.screening?.candidates || [];
  const ta = sc.filter((c) => ['awaiting_ta', 'unsure_ta'].includes(c.stage));
  const ft = sc.filter((c) => ['awaiting_ft', 'unsure_ft'].includes(c.stage));
  const m = state.manifest || {};
  const missing = missingPdfs();
  const pendingTa = pendingSent().filter((x) => x.stage === 'ta' && x.decision === 'include').length;
  return frag(
    h('div', { class: 'page-head' }, h('h1', { text: 'Review portal' }), h('span', { class: 'muted small', text: `KB ${m.kbCommit || '?'} (${m.kbDate || '?'}) · built ${m.built || '?'}` })),
    h('p', {}, `You are signed in as ${state.me.email}. Everything you decide here is sent to the knowledge base's repository under that name and applied by the maintainer; the governance policy still decides who may approve what.`),
    h('p', { class: 'small muted', text: 'This portal is a snapshot of the knowledge base, rebuilt after what reviewers sent has been applied. Your decisions reach the repository the moment you send them; the queues here (and a paper moving from title/abstract to full text) change at the next build, a few minutes after the maintainer applies the inbox, which also happens on its own every six hours.' }),
    (m.maintainers || []).includes(String(state.me.email || '').toLowerCase()) ? applyPanel() : null,
    h('div', { class: 'tiles' },
      h('a', { class: 'tile tile-link', href: '#/drafts' }, h('div', { class: 'value', text: String(drafts.length) }), h('div', { class: 'label', text: 'drafts to review' }), h('div', { class: 'detail', text: `${drafts.reduce((n, d) => n + d.findings.length, 0)} findings` })),
      h('a', { class: 'tile tile-link', href: '#/screen/ta' }, h('div', { class: 'value', text: String(ta.length) }), h('div', { class: 'label', text: 'titles/abstracts to screen' })),
      h('a', { class: 'tile tile-link', href: '#/screen/ft' }, h('div', { class: 'value', text: String(ft.length) }), h('div', { class: 'label', text: 'full texts to assess' }), h('div', { class: 'detail', text: [missing.length ? `${missing.length} without a PDF yet` : '', pendingTa ? `${pendingTa} included by you at T/A, waiting to be applied` : ''].filter(Boolean).join(' · ') })),
      h('a', { class: 'tile tile-link', href: '#/pdfs' }, h('div', { class: 'value', text: String(m.counts?.private ?? 0) }), h('div', { class: 'label', text: 'annotated PDFs here (private)' }), h('div', { class: 'detail', text: `${m.counts?.public ?? 0} more are public (Creative Commons)${missing.length ? ` · ${missing.length} still needed` : ''}${state.uploads.length ? ` · ${plural(state.uploads.length, 'upload')} waiting` : ''}` })),
      h('a', { class: 'tile tile-link', href: '#/mine' }, h('div', { class: 'value', text: String(myRecords().length) }), h('div', { class: 'label', text: 'reviews you have sent' }))),
    h('h2', { text: 'How to review' }),
    h('p', { class: 'small' }, 'A draft is what the local model extracted from one paper: findings, each with the verbatim passages that support it. Open it beside the annotated PDF (the highlights are the passages, in the colour of what they support) and say, finding by finding, whether the claim is what the paper shows. Fix a field when the paper says otherwise, select words in the PDF to add a passage or to mark something the extractor missed, then send the review. For screening, read the title and abstract (or the full text) against the eligibility criteria in SCREENING.md and include or exclude with a reason.'),
    h('p', { class: 'small muted', text: 'Keys in the screening queues: i include · e exclude (then a reason) · u unsure · click a card first.' }));
}

/** The maintainer's panel: what waits in the inbox, the last apply run, and the button that starts one. */
function applyPanel() {
  const box = h('div', { class: 'applybox' });
  const status = h('span', { class: 'small muted', text: 'checking the inbox…' });
  const btn = h('button', { class: 'btn btn-primary', disabled: '', text: 'Apply now' });
  const runLine = h('div', { class: 'small muted' });
  const when = (iso) => (iso ? new Date(iso).toLocaleString(undefined, { dateStyle: 'medium', timeStyle: 'short' }) : '?');
  const describe = (r) => {
    if (!r) return 'No apply run yet.';
    const link = h('a', { href: r.url, target: '_blank', rel: 'noopener', text: 'open the run' });
    if (r.status !== 'completed') return frag(`An apply is ${r.status.replace('_', ' ')} (started ${when(r.started)}) — the explorer and this portal rebuild when it finishes. `, link);
    return frag(`Last apply ${r.conclusion === 'success' ? 'succeeded' : `ended: ${r.conclusion}`} at ${when(r.updated)} (${r.event === 'schedule' ? 'scheduled' : r.event === 'workflow_dispatch' ? 'by hand' : r.event}). `, link);
  };
  let timer = null;
  const refresh = async () => {
    try {
      const a = await api('apply');
      const running = a.run && a.run.status !== 'completed';
      status.textContent = a.inbox ? `${plural(a.inbox, 'record')} waiting in the inbox` : 'The inbox is empty';
      runLine.replaceChildren(describe(a.run));
      btn.disabled = !a.inbox || running || a.local;
      btn.textContent = running ? 'Applying…' : a.inbox ? `Apply ${plural(a.inbox, 'record')} now` : 'Apply now';
      btn.classList.toggle('working', Boolean(running));
      if (running && document.body.contains(box)) timer = setTimeout(refresh, 20000);
      else if (a.local) status.textContent += ' — local stand-in: run portal_import.py in a terminal';
    } catch (e) { status.textContent = `Could not read the inbox: ${e.message}`; }
  };
  btn.onclick = async () => {
    btn.disabled = true; btn.classList.add('working'); btn.textContent = 'Starting…';
    try {
      const out = await api('apply', { method: 'POST', body: '{}' });
      toast(out.alreadyRunning ? 'An apply is already running' : 'Apply started: the records are applied and both sites rebuild in a few minutes');
      setTimeout(refresh, 4000);
    } catch (e) { toast(`Not started: ${e.message}`, true); btn.disabled = false; btn.classList.remove('working'); btn.textContent = 'Apply now'; }
  };
  box.append(h('div', { class: 'row' }, h('strong', { text: 'Maintainer' }), status, btn), runLine,
    h('div', { class: 'small muted', text: 'Apply runs portal_import.py in GitHub Actions: screening decisions into the register, verdicts, edits, marks and comments into the drafts, promote.py for approvers; then the explorer and this portal rebuild. Uploaded PDFs stay for you to pull on your machine (portal_import.py --kind pdf), and marks still need refocus.py there.' }));
  refresh();
  return box;
}

function draftsList() {
  const drafts = draftsIndex(state.kb);
  const byPaper = new Map();
  for (const d of drafts) (byPaper.get(d.citation) || byPaper.set(d.citation, []).get(d.citation)).push(d);
  const rows = [];
  for (const [cit, ds] of [...byPaper.entries()].sort((a, b) => String(a[0]).localeCompare(String(b[0])))) {
    const pdf = paperPdf(cit);
    rows.push(h('tr', { class: 'paper-row' }, h('th', { colspan: 5 }, h('span', { class: 'chip', text: cit }), ' ', h('span', { class: 'small muted', text: (state.kb.citations?.[cit] || '').slice(0, 140) }), ' ',
      pdf ? h('a', { class: `badge ${pdf.public ? 'badge-human' : 'badge-kind'}`, href: pdf.annotated, target: '_blank', rel: 'noopener', title: 'Open the annotated PDF in a new tab (the highlights are the drafts’ passages)', text: pdf.public ? 'annotated PDF ↗ (public)' : 'annotated PDF ↗ (reviewers)' })
        : paperSource(cit) ? h('span', { class: 'badge badge-warn', title: 'The maintainer has the paper; the annotated copy is not in this build yet', text: 'PDF with the maintainer, not annotated yet' })
          : h('span', { class: 'badge badge-warn', title: 'Nobody has this paper yet — open a draft to upload it', text: 'no PDF anywhere yet' }))));
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
  else {
    const up = uploadFor(d.citation);
    right.append(h('div', { class: 'pdf-missing' }, h('h3', { text: 'No annotated PDF here' }),
      paperSource(d.citation) ? h('p', { text: 'The maintainer has this paper; its annotated copy has not been published to the portal yet. Review from the quotes, or come back after the next build.' })
        : up ? h('p', {}, uploadedNote(up), ' The maintainer will add it to the papers folder and annotate it; until then, review from the quotes.')
          : frag(h('p', { text: 'The maintainer does not have this paper at all. If you do, upload it here: it goes into the papers folder, gets annotated, and appears beside the draft at the next build.' }), uploadControl(d.citation, d.citation)),
      state.kb.citationLinks?.[d.citation] ? h('p', {}, h('a', { href: state.kb.citationLinks[d.citation], target: '_blank', rel: 'noopener', text: 'Open the paper at the publisher' })) : null));
  }
  return layout;
}

function draftLeft(d, r, save, pdf, path) {
  const left = h('div', { class: 'left' });
  left.append(h('div', { class: 'page-head' }, h('h1', { text: entryName(d.entry) }), h('span', { class: 'chip', text: d.citation })),
    h('p', { class: 'small muted' }, `${path} · ${plural(d.findings.length, 'finding')} · `, h('a', { href: '#/drafts', text: 'all drafts' }), pdf ? '' : ' · no annotated PDF in the portal for this paper: review from the quotes, or ask the maintainer to add it'),
    h('p', { class: 'small' }, 'For each finding: does the paper show this? ', h('b', { text: 'agree' }), ' when the claim, direction and strength are what the passages say; ', h('b', { text: 'disagree' }), ' with a concern when not; ', h('b', { text: 'unsure' }), ' when you cannot tell. For each passage, say whether you checked it in the paper; what you leave as "not checked" stays open for another reviewer. Fix a field in place when the paper says otherwise (it is sent as an edit). Select words in the PDF to add a passage to a finding, or to mark something no finding covers.'));
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
  const problem = flag && !['fine', 'unsure'].includes(flag);
  return h('div', { class: `passage${problem ? ' flagged' : ''}${flag === 'fine' ? ' ok' : ''}${flag === 'unsure' ? ' unsure' : ''}`, style: `border-left-color:${colours[p.supports] || '#ccc'}` },
    h('div', { class: 'meta' }, h('span', { text: `supports ${esc(p.supports)}` }), p.page ? h('span', { text: `page ${p.page}` }) : null, p.section ? h('span', { text: esc(p.section) }) : null,
      pdf && p.page ? h('button', { class: 'btn', onclick: () => goToPage(Number(p.page), p.quote), text: 'show in paper' }) : null,
      h('select', { class: flag ? (flag === 'fine' ? 'checked-ok' : flag === 'unsure' ? 'checked-unsure' : 'checked-flag') : 'unchecked', title: 'Leave "not checked" if you did not look at this passage: it stays open for another reviewer', onchange: (e) => { if (e.target.value) fr.passages[pk] = e.target.value; else delete fr.passages[pk]; save(); render(); } },
        [['', 'not checked'], ['fine', 'checked — it is in the paper and supports the field'], ['unsure', 'not sure — someone else should look'], ['not_in_paper', 'not in the paper'], ['wrong_page', 'wrong page'], ['does_not_support', 'does not support the claim'], ['truncated', 'truncated / altered']].map(([v, t]) => h('option', { value: v, selected: flag === v ? '' : null, text: t })))),
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
  const edits = Object.entries(r.findings).filter(([, x]) => Object.keys(x.edits).length || x.added.length || Object.keys(x.passages).some((k) => !['fine', 'unsure'].includes(x.passages[k]))).length;
  const nPassages = d.findings.reduce((n, f) => n + (f.source_passages || []).length, 0);
  const checked = Object.values(r.findings).reduce((n, x) => n + Object.keys(x.passages).length, 0);
  const bar = h('div', { class: 'submitbar' });
  const btn = h('button', { class: 'btn btn-primary', disabled: pending === 0 && edits === 0 && checked === 0 && r.marks.length === 0 ? '' : null, text: 'Send this review', onclick: async () => {
    const missing = d.findings.filter((f) => r.findings[f.id]?.verdict === 'disagree' && !r.findings[f.id]?.concern);
    if (missing.length) { toast(`Say why you disagree on ${missing.map((f) => f.id).join(', ')}`, true); return; }
    if (!r.verdict && pending === total) { toast('Give an overall verdict for the draft', true); return; }
    btn.disabled = true; btn.classList.add('working'); btn.textContent = 'Sending…';
    try {
      const records = [];
      const perFinding = d.findings.filter((f) => r.findings[f.id]?.verdict).map((f) => ({ id: f.id, verdict: r.findings[f.id].verdict, concern: r.findings[f.id].concern || '', supports_approval: r.findings[f.id].verdict === 'agree', passages: r.findings[f.id].passages }));
      if (perFinding.length || r.verdict) records.push({ kind: 'verdict', id: d.path, citation: d.citation, verdict: r.verdict || null, rationale: r.rationale || '', per_finding: perFinding });
      for (const f of d.findings) {
        const x = r.findings[f.id]; if (!x) continue;
        if (Object.keys(x.edits).length || x.added.length) records.push({ kind: 'edit', id: d.path, citation: d.citation, finding: f.id, fields: Object.fromEntries(Object.entries(x.edits).map(([k, v]) => [k, { old: f[k], new: v }])), passages_added: x.added });
      }
      for (const m of r.marks) records.push({ kind: 'mark', id: d.path, citation: d.citation, page: m.page, quote: m.quote, note: m.note || '' });
      btn.textContent = `Sending ${plural(records.length, 'record')} in one commit…`;
      await sendAll(records);
      store.del(`review:${d.path}`);
      toast(`Sent ${plural(records.length, 'record')} — thank you`);
      location.hash = '#/drafts';
    } catch (e) { toast(`Not sent: ${e.message}`, true); btn.disabled = false; btn.classList.remove('working'); btn.textContent = 'Send this review'; }
  } });
  bar.append(btn, h('span', { class: 'pending', text: `${pending} of ${total} findings decided · ${checked} of ${nPassages} passages checked${edits ? ` · ${edits} edited` : ''}${r.marks.length ? ` · ${r.marks.length} marks` : ''}` }), h('span', { class: 'small muted', text: 'Saved in this browser until you send.' }));
  return frag(h('div', { class: 'verdict' }, h('h4', { text: 'Overall' }),
    h('div', { class: 'row' }, h('span', { class: 'muted', text: 'This draft should be' }), ['approve', 'agree_defer', 'reject'].map((v) => h('label', {}, h('input', { type: 'radio', name: 'overall', value: v, checked: r.verdict === v ? '' : null, onchange: () => { r.verdict = v; save(); } }), ` ${v === 'agree_defer' ? 'kept for more review' : v === 'approve' ? 'approved' : 'rejected'}`))),
    h('textarea', { rows: 2, placeholder: 'rationale, 1–3 sentences', onchange: (e) => { r.rationale = e.target.value.trim(); save(); } }, esc(r.rationale)),
    h('p', { class: 'small muted', text: 'Only someone marked approver in the Reviewer team (portal/reviewers.yaml) approves; if that is not you, your verdict is recorded as an opinion the maintainer reads before promoting.' })), bar);
}

// ---- screening ----
function screenView(stage) {
  const sc = state.screening;
  if (!sc) return h('p', { class: 'notice', text: 'No screening queue in this build of the portal.' });
  const stages = stage === 'ta' ? ['awaiting_ta', 'unsure_ta'] : ['awaiting_ft', 'unsure_ft'];
  const key = `screen:${stage}`;
  const decided = store.get(key, {});
  // Records already sent (from this browser, or listed by the repository under your name)
  // leave the queue until the maintainer applies them and rebuilds the portal.
  const sentLocal = store.get('screen:sent', {});
  const mineSlug = slug(state.me?.email?.split('@')[0]);
  const sentIds = new Set(Object.keys(sentLocal));
  for (const n of [...state.mine.inbox, ...state.mine.applied]) { const m = n.match(new RegExp(`_screen_${mineSlug}_([a-z0-9-]+)\\.json$`)); if (m) sentIds.add(m[1]); }
  const all = sc.candidates.filter((c) => stages.includes(c.stage));
  const cands = all.filter((c) => !sentIds.has(slug(c.id)) && !sentIds.has(c.id));
  const hidden = all.length - cands.length;
  const reasons = Object.entries(sc.reasons || {}).filter(([, v]) => stage === 'ft' || !v.fullTextOnly);
  const nDecided = Object.values(decided).filter((d) => d.decision).length;
  const statusText = (k) => `${cands.length} awaiting · ${k} decided here, not yet sent${hidden ? ` · ${hidden} sent by you, waiting for the maintainer` : ''}`;
  const status = h('span', { class: 'muted small', text: statusText(nDecided) });
  const sendBtn = h('button', { class: 'btn btn-primary', style: 'margin-left:auto', disabled: nDecided ? null : '', text: nDecided ? `Send ${plural(nDecided, 'decision')}` : 'Send decisions', onclick: () => sendScreen(stage, decided, cands, sendBtn, status) });
  const head = h('div', { class: 'page-head sticky-head' }, h('h1', { text: stage === 'ta' ? 'Title/abstract screening' : 'Full-text screening' }), status, sendBtn);
  const list = h('div', {});
  for (const c of cands) {
    const dec = decided[c.id] || {};
    const pdf = c.key ? paperPdf(c.key) : null;
    const have = candidateHasPdf(c);
    const up = have ? null : uploadFor(c.id, c.key);
    const gated = stage === 'ft' && !have && !up;        // a full-text decision needs the paper
    const pdfLine = pdf ? h('span', {}, h('a', { href: pdf.annotated, target: '_blank', rel: 'noopener', text: 'annotated PDF' }))
      : have ? h('span', { class: 'small muted', text: 'PDF with the maintainer (not annotated yet)' })
        : up ? uploadedNote(up)
          : h('span', { class: 'pdfask' }, h('span', { class: `small ${stage === 'ft' ? '' : 'muted'}`, text: stage === 'ft' ? 'No PDF of this paper anywhere yet — upload it to assess the full text: ' : 'No PDF yet; if you have it: ' }), uploadControl(c.id, c.key, { required: stage === 'ft' }));
    const card = h('article', { class: `screen${dec.decision ? ' done' : ''}${gated ? ' gated' : ''}`, tabindex: '-1', 'data-id': c.id },
      h('p', { class: 't' }, h('span', { class: 'chip', text: c.id }), ' ', esc(c.title)),
      h('p', { class: 'small muted' }, [c.year, c.journal, (c.authors || '').slice(0, 120)].filter(Boolean).join(' · '), c.doi ? [' · ', h('a', { href: `https://doi.org/${c.doi}`, target: '_blank', rel: 'noopener', text: c.doi })] : null, c.pmid ? [' · PMID ', h('a', { href: `https://pubmed.ncbi.nlm.nih.gov/${c.pmid}`, target: '_blank', rel: 'noopener', text: String(c.pmid) })] : null,
        c.for?.length ? ` · for ${c.for.join(', ')}` : '', c.history?.length ? ` · ${c.history.map((x) => `${x.stage === 'title_abstract' ? 'T/A' : 'FT'}: ${x.decision} (${x.by})`).join('; ')}` : ''),
      h('p', { class: 'small pdfline' }, pdfLine),
      h('p', { class: 'ab', text: c.abstract || '(no abstract available)' }),
      c.suggestion?.decision ? h('p', { class: 'sug', text: `Model suggests ${c.suggestion.decision}${c.suggestion.reason && c.suggestion.reason !== 'none' ? ` (${c.suggestion.reason})` : ''} — a suggestion, not a decision.` }) : null,
      h('div', { class: 'dec' }, ['include', 'exclude', 'unsure'].map((v) => h('label', { title: gated ? 'Upload the PDF first' : null }, h('input', { type: 'radio', name: `s-${c.id}`, value: v, disabled: gated ? '' : null, checked: dec.decision === v ? '' : null, onchange: () => { decided[c.id] = { ...dec, decision: v }; store.set(key, decided); card.classList.add('done'); const k = Object.values(decided).filter((x) => x.decision).length; status.textContent = statusText(k); sendBtn.disabled = k ? false : true; sendBtn.textContent = k ? `Send ${plural(k, 'decision')}` : 'Send decisions'; } }), ` ${v}`)),
        h('select', { onchange: (e) => { decided[c.id] = { ...(decided[c.id] || {}), reason: e.target.value }; store.set(key, decided); } }, h('option', { value: '', text: 'reason…' }), reasons.map(([k, v]) => h('option', { value: k, selected: dec.reason === k ? '' : null, text: v.label }))),
        h('input', { type: 'text', value: dec.note || '', placeholder: 'note', style: 'min-width:220px', onchange: (e) => { decided[c.id] = { ...(decided[c.id] || {}), note: e.target.value }; store.set(key, decided); } })));
    const ctl = card.querySelector('.upload');
    if (ctl?.uploadFile) dropZone(card, ctl.uploadFile);       // drop the paper's PDF anywhere on its card
    list.append(card);
  }
  if (!cands.length) list.append(h('p', { class: 'notice', text: 'Nothing awaiting a decision at this stage.' }));
  const onkey = (e) => {
    if (e.target.tagName === 'INPUT' && e.target.type === 'text') return;
    const card = document.activeElement?.closest?.('.screen'); if (!card) return;
    const map = { i: 'include', e: 'exclude', u: 'unsure' }; const v = map[e.key]; if (!v) return;
    if (card.classList.contains('gated')) { toast('Upload the paper’s PDF before deciding on its full text', true); e.preventDefault(); return; }
    const radio = card.querySelector(`input[type=radio][value="${v}"]`); if (radio) { radio.checked = true; radio.dispatchEvent(new Event('change')); }
    if (v === 'exclude') card.querySelector('select').focus(); else { const next = card.nextElementSibling; if (next) { next.focus(); next.scrollIntoView({ block: 'center' }); } }
    e.preventDefault();
  };
  document.addEventListener('keydown', onkey, { once: false });
  state.keyHandler = onkey;
  return frag(head, h('p', { class: 'small', text: `Criteria: docs/SCREENING.md §2. ${stage === 'ta' ? 'Include whatever might answer one of the KB questions; exclude only for a listed reason.' : 'Read the paper; include when it answers a question in §1 and no exclusion reason applies.'} Decisions are kept in this browser until you send them.` }), list);
}

async function sendScreen(stage, decided, cands, btn = null, status = null) {
  const st = stage === 'ta' ? 'title_abstract' : 'full_text';
  const items = Object.entries(decided).filter(([, d]) => d.decision);
  if (!items.length) { toast('Nothing decided yet', true); return; }
  const label = btn ? btn.textContent : '';
  const working = () => { if (btn) { btn.disabled = true; btn.classList.add('working'); btn.textContent = `Sending ${plural(items.length, 'decision')}…`; } if (status) status.textContent = 'writing them to the repository as one commit; a few seconds'; };
  const done = () => { if (btn) { btn.disabled = false; btn.classList.remove('working'); btn.textContent = label; } };
  const bad = items.filter(([, d]) => d.decision === 'exclude' && !d.reason);
  if (bad.length) { toast(`An exclusion needs a reason: ${bad.map(([id]) => id).join(', ')}`, true); return; }
  if (stage === 'ft') {
    const noPdf = items.filter(([id]) => { const c = cands.find((x) => x.id === id); return c && !candidateHasPdf(c) && !uploadFor(c.id, c.key); }).map(([id]) => id);
    if (noPdf.length) { toast(`A full-text decision needs the paper's PDF first: ${noPdf.join(', ')}`, true); return; }
  }
  working();
  try {
    await sendAll(items.map(([id, d]) => ({ kind: 'screen', id, stage: st, decision: d.decision, reason: d.decision === 'exclude' ? d.reason : null, note: d.note || '' })));
    const sentLocal = store.get('screen:sent', {});
    const at = new Date().toISOString();
    for (const [id, d] of items) { delete decided[id]; sentLocal[id] = { at, stage, decision: d.decision }; }
    store.set(`screen:${stage}`, decided); store.set('screen:sent', sentLocal);
    toast(`Sent ${plural(items.length, 'decision')} — thank you. They leave the queue until the maintainer applies them${stage === 'ta' ? '; included papers then move to the Full text queue at the next build' : ''}.`);
    render();
    window.scrollTo(0, 0);
    document.querySelector('.screen')?.focus();
  } catch (e) { done(); toast(`Not sent: ${e.message}`, true); }
}

// ---- the PDFs the portal holds ----
function pdfsView() {
  const m = state.manifest || {};
  const papers = Object.entries(m.papers || {}).sort((a, b) => a[0].localeCompare(b[0]));
  const drafts = draftsIndex(state.kb);
  const draftsBy = new Map();
  for (const d of drafts) (draftsBy.get(d.citation) || draftsBy.set(d.citation, []).get(d.citation)).push(d);
  const approvedBy = new Map();
  for (const f of state.kb.findings || []) if (f.source_status === 'approved') approvedBy.set(f.citation, (approvedBy.get(f.citation) || 0) + 1);
  const filter = h('input', { type: 'search', placeholder: 'filter by key or title…', 'aria-label': 'Filter PDFs', style: 'min-width:260px', oninput: (e) => { const q = e.target.value.trim().toLowerCase(); for (const tr of table.querySelectorAll('tbody tr')) tr.hidden = Boolean(q) && !tr.dataset.q.includes(q); } });
  const row = ([cit, p]) => {
    const ds = draftsBy.get(cit) || [];
    return h('tr', { 'data-q': `${cit} ${state.kb.citations?.[cit] || ''}`.toLowerCase() },
      h('td', {}, h('a', { href: p.annotated, target: '_blank', rel: 'noopener', text: cit.replace(/^@/, '') })),
      h('td', { class: 'small', text: (state.kb.citations?.[cit] || '').slice(0, 160) }),
      h('td', {}, h('span', { class: `badge ${p.public ? 'badge-human' : 'badge-kind'}`, title: p.label || p.category, text: p.public ? 'public (CC)' : 'private' })),
      h('td', { class: 'num', text: String(approvedBy.get(cit) || 0) }),
      h('td', {}, ds.length ? ds.map((d, i) => [i ? ', ' : '', h('a', { href: draftHref(d.path), text: entryName(d.entry) })]) : h('span', { class: 'muted small', text: '—' })),
      h('td', { class: 'small muted', text: `${Math.round((p.bytes || 0) / 1024)} KB` }));
  };
  const table = h('table', { class: 'queue' }, h('thead', {}, h('tr', {}, h('th', { text: 'Paper' }), h('th', { text: 'Citation' }), h('th', { text: 'Access' }), h('th', { class: 'num', text: 'Approved findings' }), h('th', { text: 'Drafts to review' }), h('th', { text: 'Size' }))), h('tbody', {}, papers.map(row)));
  const ups = [...state.uploads].sort((a, b) => String(b.uploaded).localeCompare(String(a.uploaded)));
  // Papers included at title/abstract whose PDF nobody has yet: the list to work from when looking for full texts.
  const missing = missingPdfs().sort((a, b) => (Number(b.year) || 0) - (Number(a.year) || 0) || String(a.id).localeCompare(String(b.id)));
  const missingRow = (c) => {
    const up = uploadFor(c.id, c.key);
    const ctl = up ? null : uploadControl(c.id, c.key, { label: 'Upload' });
    return dropZone(h('tr', { class: up ? 'has-upload' : 'droppable' },
      h('td', {}, h('span', { class: 'chip', text: c.id }), c.key ? h('div', { class: 'small muted', text: c.key }) : null),
      h('td', { class: 'small' }, h('div', { text: c.title || '' }), h('div', { class: 'muted', text: [c.year, c.journal, (c.authors || '').slice(0, 80)].filter(Boolean).join(' · ') })),
      h('td', { class: 'small' }, c.doi ? h('a', { href: `https://doi.org/${c.doi}`, target: '_blank', rel: 'noopener', text: 'doi' }) : null, c.doi && c.pmid ? ' · ' : '', c.pmid ? h('a', { href: `https://pubmed.ncbi.nlm.nih.gov/${c.pmid}`, target: '_blank', rel: 'noopener', text: 'PubMed' }) : null, !c.doi && !c.pmid ? h('span', { class: 'muted', text: '—' }) : null),
      h('td', { class: 'small' }, c.history?.length ? c.history.map((x) => `${x.stage === 'title_abstract' ? 'T/A' : 'FT'}: ${x.decision}${x.by ? ` (${x.by})` : ''}`).join('; ') : h('span', { class: 'muted', text: c.stage === 'unsure_ft' ? 'unsure at full text' : 'included at T/A' })),
      h('td', {}, up ? uploadedNote(up) : ctl)), ctl?.uploadFile);
  };
  const missingTable = h('table', { class: 'queue missing' }, h('thead', {}, h('tr', {}, h('th', { text: 'Candidate' }), h('th', { text: 'Paper' }), h('th', { text: 'Find it' }), h('th', { text: 'Screening' }), h('th', { text: 'PDF' }))), h('tbody', {}, missing.map(missingRow)));
  const nUp = missing.filter((c) => uploadFor(c.id, c.key)).length;
  return frag(h('div', { class: 'page-head' }, h('h1', { text: 'PDFs' }), h('span', { class: 'muted small', text: `${m.counts?.private ?? 0} private · ${m.counts?.public ?? 0} public · ${m.counts?.sources ?? 0} more source PDFs with the maintainer, not annotated yet · ${missing.length} included papers without a PDF` })),
    h('h2', { id: 'missing', text: `Papers we still need (${missing.length})` }),
    h('p', { class: 'small', text: `Included at title/abstract, waiting for a full-text decision, and nobody has the PDF yet${nUp ? ` (${nUp} uploaded, with the maintainer)` : ''}. If you can get one — through your library, the authors, or a repository copy — drag the PDF onto the paper's row (or choose the file and press Upload); it goes to the maintainer's papers folder, never to the public site. The full-text decision for a paper can only be made once its PDF exists.` }),
    missing.length ? missingTable : h('p', { class: 'notice', text: 'Every paper awaiting a full-text decision has its PDF.' }),
    h('h2', { text: `Annotated PDFs (${papers.length})` }),
    h('p', { class: 'small', text: 'Every paper whose annotated PDF this build of the portal holds. The highlights in each PDF are the passages the KB cites from it, coloured by what they support. Public copies are papers under a Creative Commons licence; the private ones are for signed-in reviewers only and must not be passed on.' }),
    h('div', { class: 'matrix-controls' }, filter),
    papers.length ? table : h('p', { class: 'notice', text: 'No annotated PDFs in this build.' }),
    h('h2', { text: `Uploads waiting for the maintainer (${ups.length})` }),
    state.uploadsOk ? (ups.length ? h('table', { class: 'queue' }, h('thead', {}, h('tr', {}, h('th', { text: 'For' }), h('th', { text: 'File' }), h('th', { text: 'By' }), h('th', { text: 'When' }), h('th', { text: 'Size' }))), h('tbody', {}, ups.map((u) => h('tr', {}, h('td', { text: u.id }), h('td', { class: 'small', text: u.name }), h('td', { class: 'small', text: u.by }), h('td', { class: 'small', text: String(u.uploaded || '').slice(0, 16).replace('T', ' ') }), h('td', { class: 'small muted', text: `${Math.round((u.bytes || 0) / 1024)} KB` })))))
      : h('p', { class: 'small muted', text: 'None. A paper the portal lacks can be uploaded from its screening card or its draft; it goes to the maintainer, who adds it to the papers folder.' }))
      : h('p', { class: 'small muted', text: 'Uploads are not enabled on this portal.' }));
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
    else if (head === 'pdfs') { view = pdfsView(); current = '/pdfs'; }
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
    try { const sent = store.get('screen:sent', {}); const built = manifest.built || ''; for (const [id, when] of Object.entries(sent)) if (built && String(when?.at || when) < built) delete sent[id]; store.set('screen:sent', sent); } catch { /* ignore */ }
    state.screening = await fetch('screening.json').then((r) => (r.ok ? r.json() : null)).catch(() => null);
    state.mine = await api('reviews').catch(() => ({ inbox: [], applied: [] }));
    try { const u = await api('upload'); state.uploads = u.uploads || []; state.uploadsOk = true; } catch { state.uploads = []; state.uploadsOk = false; }
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
