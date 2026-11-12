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
//   #/screen/ft[/<id>] full-text screening: one paper at a time beside its PDF (include needs the PDF; upload or skip)
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
import { orderScreeningPapers, mergePendingPapers, pendingScreenReceipts } from './paper-intake.js';
import { applyState } from './apply-state.js';
import { carryOver, sameBuild } from './review-state.js';

const state = { me: null, manifest: null, kb: null, bindings: {}, bindingProblem: '', screening: null, screeningIndex: [], mine: { inbox: [], applied: [] }, uploads: [], uploadsOk: false, pdfjs: null, zoom: 1, sel: null, docs: new Map() };
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

/** SHA-256 of the exact bytes fetched (the drafts export on screen must be the one the bindings were made for). */
async function sha256Hex(text) {
  const buf = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(text));
  return [...new Uint8Array(buf)].map((b) => b.toString(16).padStart(2, '0')).join('');
}

async function api(path, init) {
  const res = await fetch(`/api/${path}`, { cache: 'no-store', headers: { 'Content-Type': 'application/json' }, ...init });
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
const candidateHasPdf = (c) => Boolean(c.pdf_file || state.manifest?.fulltext?.[c.id]?.object || state.screeningIndex.find((r) => r.id === c.id)?.pdf_file) || paperSource(c.key);
/** An upload waiting in the bucket for this candidate id or citation key, if any. */
const uploadFor = (...ids) => {
  const aliases = (state.screening?.candidates || []).filter((c) => ids.includes(c.id)).flatMap((c) => c.upload_ids || []);
  return state.uploads.find((u) => [...ids, ...aliases].filter(Boolean).some((id) => u.id === id || u.id === String(id).replace(/^@/, '') || `@${u.id}` === id)) || null;
};

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
      render({ preserveScroll: location.hash === '#/screen/ta' });
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
  return Object.entries(sent).filter(([, v]) => v && typeof v === 'object').map(([id, v]) => ({ id, ...v })).filter((x) => cands.some((c) => c.id === x.id && (!x.stage || c.stage.endsWith(`_${x.stage}`))));
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
    (m.maintainers || []).includes(String(state.me.email || '').toLowerCase()) ? frag(applyPanel(), requestsPanel()) : null,
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
  const waitingLine = h('div', { class: 'small' });
  const nextLine = h('div', { class: 'small' });
  const when = (iso) => (iso ? new Date(iso).toLocaleString(undefined, { dateStyle: 'medium', timeStyle: 'short' }) : '?');
  const describe = (r) => {
    if (!r) return 'No apply run yet.';
    const link = h('a', { href: r.url, target: '_blank', rel: 'noopener', text: 'open the run' });
    if (r.status !== 'completed') return frag(`An apply is ${r.status.replace('_', ' ')} (started ${when(r.started)}) — the explorer and this portal rebuild when it finishes. `, link);
    return frag(`Last apply ${r.conclusion === 'success' ? 'succeeded' : `ended: ${r.conclusion}`} at ${when(r.updated)} (${r.event === 'schedule' ? 'scheduled' : r.event === 'workflow_dispatch' ? 'by hand' : r.event}). `, link);
  };
  let timer = null;
  let waitingSince = 0;
  const refresh = async () => {
    clearTimeout(timer);
    try {
      const a = await api('apply');
      let view = applyState(a.run);
      if (waitingSince && (!a.run || Date.parse(a.run.started) < waitingSince - 5000)) {
        view = { label: 'Waiting to start…', busy: true, poll: true, next: 'GitHub is starting the apply workflow.' };
      } else waitingSince = 0;
      const running = view.busy;
      const ready = a.ready ?? a.inbox;
      status.textContent = ready ? `${plural(ready, 'record')} ready to apply` : 'No records ready to apply';
      waitingLine.replaceChildren(...[
        a.pdf ? h('p', { text: `${plural(a.pdf, 'uploaded PDF')} waiting for local download. Apply does not download PDFs. On your computer run: .venv/bin/python kb.py sync` }) : null,
        a.attention?.length ? h('details', {}, h('summary', { text: `${plural(a.attention.length, 'record')} need maintainer attention` }), a.attention.map((x) => h('p', { text: `${x.draft || x.file}: ${x.reason}` }))) : null].filter(Boolean));
      runLine.replaceChildren(describe(a.run));
      nextLine.textContent = view.next;
      if (view.label) status.textContent = `${view.label} · ${status.textContent}`;
      btn.disabled = !ready || running || a.local;
      btn.textContent = running ? view.label : ready ? `Apply ${plural(ready, 'record')} now` : 'Nothing to apply';
      btn.classList.toggle('working', Boolean(running));
      if (view.poll && document.body.contains(box)) timer = setTimeout(refresh, 3000);
      else if (a.local) status.textContent += ' — local stand-in: run portal_import.py in a terminal';
    } catch (e) { status.textContent = `Could not read the inbox: ${e.message}`; }
  };
  btn.onclick = async () => {
    btn.disabled = true; btn.classList.add('working'); btn.textContent = 'Starting…';
    try {
      const out = await api('apply', { method: 'POST', body: '{}' });
      if (!out.nothingToApply && !out.alreadyRunning) waitingSince = Date.parse(out.started) || Date.now();
      toast(out.nothingToApply ? 'No records are ready to apply; check the items awaiting local download or attention.' : out.alreadyRunning ? 'An apply is already running' : 'Apply started: the records are applied and both sites rebuild in a few minutes');
      setTimeout(refresh, 4000);
    } catch (e) { toast(`Not started: ${e.message}`, true); btn.disabled = false; btn.classList.remove('working'); btn.textContent = 'Apply now'; }
  };
  box.append(h('div', { class: 'row' }, h('strong', { text: 'Maintainer' }), status, btn), runLine, nextLine, waitingLine,
    h('div', { class: 'small muted', text: 'Apply saves screening and review decisions, checks the changes, and rebuilds both sites. Uploaded PDFs are separate: use kb.py sync, or kb.py sync --intake --wait to download and prepare them. Model extraction and source review start only when you choose.' }));
  refresh();
  return box;
}

/** The maintainer's list of people who asked, on the welcome page, to become reviewers. */
function requestsPanel() {
  const box = h('div', { class: 'applybox requests' });
  const head = h('span', { class: 'small muted', text: 'checking for reviewer requests…' });
  const list = h('div', { class: 'request-list' });
  const when = (iso) => (iso ? new Date(iso).toLocaleDateString(undefined, { dateStyle: 'medium' }) : '');
  // The welcome a new reviewer gets: shown beside each request to copy, and behind "Write to them".
  const WELCOME_SUBJECT = 'You can now review for the stroke aphasia knowledge base';
  const welcomeText = (r) => `Hello ${r.name},\n\n`
    + 'Thank you for offering to review for the stroke aphasia knowledge base. You have been added as a reviewer.\n\n'
    + 'To start:\n'
    + `1. Open ${location.origin}/ and choose "I'm already an approved reviewer".\n`
    + `2. Type this email address (${r.email}) and press "Send login code".\n`
    + '3. Enter the code that arrives by email. The sign-in then lasts a week.\n\n'
    + 'You do not need to create an account or a password. The sign-in page is run by Cloudflare Access, but no Cloudflare account is needed; if the code does not arrive, look in your junk folder.\n\n'
    + 'The Home page of the portal explains how to review: screening titles and abstracts takes about ten minutes for twenty papers, and checking a draft against its paper about half an hour. Everything you decide is recorded under your name, and nothing enters the knowledge base without a named person.\n\n'
    + 'I am glad to answer any question.\n\nBest wishes,\n' + (state.manifest?.config?.maintainer || '') + '\n';
  const welcome = (r) => `mailto:${encodeURIComponent(r.email)}?subject=${encodeURIComponent(WELCOME_SUBJECT)}&body=${encodeURIComponent(welcomeText(r))}`;
  // the page where an email is added: the edit page of the Access policy the portal uses (portal.config.json)
  const policyUrl = state.manifest?.config?.accessPolicyUrl || '';
  const row = (r) => {
    const copy = h('button', { class: 'btn', type: 'button', text: 'Copy email', onclick: async () => { try { await navigator.clipboard.writeText(r.email); toast('Email copied'); } catch { toast(r.email); } } });
    const remove = h('button', { class: 'btn', type: 'button', text: 'Remove from list', title: 'Once the person has been added (or declined). Removing does not write to them.', onclick: async () => {
      remove.disabled = true;
      try { await api(`requests?id=${encodeURIComponent(r.id)}`, { method: 'DELETE' }); toast('Removed'); refresh(); } catch (e) { toast(`Not removed: ${e.message}`, true); remove.disabled = false; }
    } });
    return h('div', { class: 'request' },
      h('div', {}, h('strong', { text: r.name }), ' · ', h('span', { text: r.email }), r.affiliation ? frag(' · ', h('span', { class: 'muted', text: r.affiliation })) : null, h('span', { class: 'small muted', text: ` · asked ${when(r.requested)}` })),
      r.note ? h('div', { class: 'small request-note', text: r.note }) : null,
      h('div', { class: 'row' }, copy, h('a', { class: 'btn', href: policyUrl || 'https://one.dash.cloudflare.com/', target: '_blank', rel: 'noopener', text: 'Add in Cloudflare ↗',
        title: policyUrl ? 'Copies the email and opens the Reviewers policy in Cloudflare: paste it into the Emails box, then Save' : 'Zero Trust → Access controls → Policies → Reviewers: add the email',
        onclick: () => { navigator.clipboard?.writeText(r.email).then(() => toast('Email copied: paste it into the Emails box in Cloudflare, then Save'), () => {}); } }),
        h('a', { class: 'btn', href: welcome(r), text: 'Write to them', title: 'Opens the welcome email below in your mail program, addressed to them' }), remove),
      h('details', { class: 'request-mail' }, h('summary', { text: 'Welcome email to send them' }),
        h('div', { class: 'small muted', text: `To: ${r.email} · Subject: ${WELCOME_SUBJECT}` }),
        h('pre', { class: 'request-mail-text', text: welcomeText(r) }),
        h('div', { class: 'row' },
          h('button', { class: 'btn', type: 'button', text: 'Copy the text', onclick: async () => { try { await navigator.clipboard.writeText(welcomeText(r)); toast('Welcome email copied'); } catch { toast('Select the text and copy it', true); } } }),
          h('button', { class: 'btn', type: 'button', text: 'Copy the subject', onclick: async () => { try { await navigator.clipboard.writeText(WELCOME_SUBJECT); toast('Subject copied'); } catch { toast(WELCOME_SUBJECT); } } }))));
  };
  const refresh = async () => {
    try {
      const out = await api('requests');
      const n = (out.requests || []).length;
      head.textContent = n ? `${plural(n, 'person', 'people')} asked to become a reviewer` : 'No reviewer requests waiting';
      list.replaceChildren(...(out.requests || []).map(row));
      steps.hidden = !n;
    } catch (e) { head.textContent = `Reviewer requests could not be read: ${e.message}`; }
  };
  const steps = h('div', { class: 'small muted', hidden: '', text: 'To accept someone: "Add in Cloudflare" copies their email and opens the Reviewers policy; paste it into the Emails box and save (now they can sign in). Add them to portal/reviewers.yaml (so their reviews carry their name), send them the welcome email ("Write to them", or copy it from "Welcome email to send them"), then remove the request here.' });
  box.append(h('div', { class: 'row' }, h('strong', { text: 'Reviewer requests' }), head), list, steps);
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
  const bound = state.bindings?.[path];
  // Decisions saved in this browser belong to the version of the draft they were made on: a
  // changed draft starts afresh, the earlier state kept as `previous` for reference (review-state.js).
  const { review: r, setAside } = carryOver(store.get(key, null), bound?.digest);
  const save = () => store.set(key, r);
  if (setAside) save();
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
  if (r.previous) {
    const p = r.previous;
    const agreed = Object.entries(p.findings || {}).filter(([, x]) => x.verdict).map(([id, x]) => `${id} ${x.verdict}`).join(', ');
    left.append(h('div', { class: 'notice' }, h('b', { text: 'This draft changed since you started reviewing it in this browser. ' }),
      'Your earlier decisions were not carried over: review the current version. For reference, you had: ',
      `${p.verdict ? `overall ${p.verdict}` : 'no overall verdict'}${agreed ? `; ${agreed}` : ''}${p.rationale ? `; note: “${p.rationale}”` : ''}. `,
      h('button', { class: 'btn', text: 'Dismiss', onclick: () => { delete r.previous; save(); render(); } })));
  }
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
    const bound = state.bindings?.[d.path];
    if (bound && r.digest && r.digest !== bound.digest) { toast('This draft changed while you were reviewing it: reload the page and review the current version', true); return; }
    if ((r.verdict || pending) && !bound) { toast(state.bindingProblem || 'This draft is not in the portal build any more (or the build is older than this page): reload, then review the current version', true); return; }
    if (r.verdict === 'approve') {
      const notAgreed = d.findings.filter((f) => r.findings[f.id]?.verdict !== 'agree').map((f) => f.id);
      if (notAgreed.length) { toast(`To approve, agree with every finding (${notAgreed.join(', ')} not agreed), or choose "kept for more review"`, true); return; }
      if (bound?.obligations?.length) { toast(`This draft has reviewer marks still open (${bound.obligations.join(', ')}): it cannot be approved until they are resolved`, true); return; }
    }
    btn.disabled = true; btn.classList.add('working'); btn.textContent = 'Sending…';
    try {
      const records = [];
      const perFinding = d.findings.filter((f) => r.findings[f.id]?.verdict).map((f) => ({ id: f.id, verdict: r.findings[f.id].verdict, concern: r.findings[f.id].concern || '', supports_approval: r.findings[f.id].verdict === 'agree', passages: r.findings[f.id].passages }));
      for (const f of d.findings) {
        const x = r.findings[f.id]; if (!x) continue;
        if (Object.keys(x.edits).length || x.added.length) records.push({ kind: 'edit', id: d.path, citation: d.citation, finding: f.id, fields: Object.fromEntries(Object.entries(x.edits).map(([k, v]) => [k, { old: f[k], new: v }])), passages_added: x.added });
      }
      for (const m of r.marks) records.push({ kind: 'mark', id: d.path, citation: d.citation, page: m.page, quote: m.quote, note: m.note || '' });
      // the verdict last: it is about the draft with this send's own edits and marks in it, and it
      // names the version reviewed (the import treats a verdict on a since-changed draft as an opinion)
      if (perFinding.length || r.verdict) records.push({ kind: 'verdict', id: d.path, citation: d.citation, verdict: r.verdict || null, rationale: r.rationale || '', per_finding: perFinding, draft_digest: bound.digest, finding_ids: bound.findings });
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
/** The records awaiting a decision at `stage` (ta | ft), less those you already sent at that stage. */
function screenQueue(stage) {
  const sc = state.screening;
  const stages = stage === 'ta' ? ['awaiting_ta', 'unsure_ta'] : ['awaiting_ft', 'unsure_ft'];
  // Records you already decided at THIS stage leave the queue until the decision is applied
  // and the portal rebuilt. A decision at the other stage never hides a record: a paper you
  // included at title/abstract must show up here for its full-text assessment.
  //   - this browser: decisions sent at this stage (older entries carry no stage: kept);
  //   - the inbox (not applied yet): the build still shows the record at the stage the
  //     decision was made at, so it is this stage's decision;
  //   - applied: already part of this build, unless it was applied after the build.
  const sentLocal = store.get('screen:sent', {});
  const mineSlug = slug(state.me?.email?.split('@')[0]);
  const builtAt = Date.parse(sc.built || '') || 0;
  const stampAt = (n) => { const t = n.match(/^(\d{4})(\d\d)(\d\d)T(\d\d)(\d\d)(\d\d)Z/); return t ? Date.UTC(+t[1], +t[2] - 1, +t[3], +t[4], +t[5], +t[6]) : Infinity; };
  const sentIds = new Set(Object.entries(sentLocal).filter(([, v]) => !v?.stage || v.stage === stage).map(([id]) => id));
  const screenId = (n) => n.match(new RegExp(`_screen_${mineSlug}_([a-z0-9-]+)\\.json$`))?.[1];
  for (const n of state.mine.inbox) { const id = screenId(n); if (id) sentIds.add(id); }
  for (const n of state.mine.applied) { const id = screenId(n); if (id && stampAt(n) > builtAt) sentIds.add(id); }
  const all = sc.candidates.filter((c) => stages.includes(c.stage));
  const cands = orderScreeningPapers(all.filter((c) => !sentIds.has(slug(c.id)) && !sentIds.has(c.id)), state.uploads, stage);
  return { cands, hidden: all.length - cands.length };
}

function screenView(stage) {
  const sc = state.screening;
  if (!sc) return h('p', { class: 'notice', text: 'No screening queue in this build of the portal.' });
  const key = `screen:${stage}`;
  const decided = store.get(key, {});
  const { cands, hidden } = screenQueue(stage);
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
    const sourcePdf = state.manifest?.fulltext?.[c.id];
    const have = candidateHasPdf(c);
    const up = have ? null : uploadFor(c.id, c.key);
    const gated = stage === 'ft' && !have && !up;        // a full-text decision needs the paper
    const pdfLine = pdf ? h('span', {}, h('a', { href: pdf.annotated, target: '_blank', rel: 'noopener', text: 'annotated PDF' }))
      : sourcePdf?.object ? h('a', { href: sourcePdf.object, target: '_blank', rel: 'noopener', text: 'Open PDF' })
      : have ? h('span', { class: 'small muted', text: 'PDF with the maintainer (not annotated yet)' })
        : up ? uploadedNote(up)
          : !state.uploadsOk ? h('span', { class: 'notice', text: 'Upload status could not be checked. Reload before uploading this paper again.' })
          : h('span', { class: 'pdfask' }, h('span', { class: `small ${stage === 'ft' ? '' : 'muted'}`, text: stage === 'ft' ? 'No PDF of this paper anywhere yet — upload it to assess the full text: ' : 'No PDF yet; if you have it: ' }), uploadControl(c.id, c.key, { required: stage === 'ft' }));
    const card = h('article', { class: `screen${dec.decision ? ' done' : ''}${gated ? ' gated' : ''}`, tabindex: '-1', 'data-id': c.id },
      h('p', { class: 't' }, h('span', { class: 'chip', text: c.id }), ' ', esc(c.title)),
      h('p', { class: 'small muted' }, [c.year, c.journal, (c.authors || '').slice(0, 120)].filter(Boolean).join(' · '), c.doi ? [' · ', h('a', { href: `https://doi.org/${c.doi}`, target: '_blank', rel: 'noopener', text: c.doi })] : null, c.pmid ? [' · PMID ', h('a', { href: `https://pubmed.ncbi.nlm.nih.gov/${c.pmid}`, target: '_blank', rel: 'noopener', text: String(c.pmid) })] : null,
        c.for?.length ? ` · for ${c.for.join(', ')}` : '', c.history?.length ? ` · ${c.history.map((x) => `${x.stage === 'title_abstract' ? 'T/A' : 'FT'}: ${x.decision} (${x.by})`).join('; ')}` : ''),
      h('p', { class: 'small pdfline' }, pdfLine, up ? [' · ', h('a', { href: `api/upload?file=${encodeURIComponent(up.id)}`, target: '_blank', rel: 'noopener', text: 'Open uploaded PDF' })] : null),
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

// ---- full-text screening: one paper at a time, beside its PDF ----
// The decision needs the paper: "include" stays disabled until the portal can show the PDF
// (an annotated copy, the maintainer's full text synced for screening, or an upload). A paper
// without one can be uploaded (drop it on the PDF side) or skipped for now: skipped papers go
// to the end of the queue and stay there until they are decided.
const FT_SKIP = 'screen:ft:skipped';
/** The PDF the portal can show for a full-text candidate: {url, label} or null. */
function ftPdf(c) {
  const ann = c.key ? paperPdf(c.key) : null;
  if (ann) return { url: ann.annotated, label: 'annotated PDF' };
  const ft = state.manifest?.fulltext?.[c.id];
  if (ft?.object) return { url: ft.object, label: 'full text' };
  const up = uploadFor(c.id, c.key);
  if (up) return { url: `api/upload?file=${encodeURIComponent(up.id)}`, label: 'uploaded PDF', upload: up };
  return null;
}
/** The queue in the order shown (skipped papers last) and the paper on screen. */
function ftQueue(wanted) {
  const { cands, hidden } = screenQueue('ft');
  const skipped = new Set(store.get(FT_SKIP, []));
  const decided = store.get('screen:ft', {});
  const order = [...cands.filter((c) => !skipped.has(c.id)), ...cands.filter((c) => skipped.has(c.id))];
  const current = order.find((c) => c.id === wanted) || order.find((c) => !decided[c.id]?.decision && !skipped.has(c.id)) || order.find((c) => !decided[c.id]?.decision) || order[0] || null;
  return { order, current, skipped, decided, hidden };
}
const ftGo = (c) => { if (c) location.hash = `#/screen/ft/${encodeURIComponent(c.id)}`; };
function ftView(wanted) {
  const sc = state.screening;
  if (!sc) return h('p', { class: 'notice', text: 'No screening queue in this build of the portal.' });
  const q = ftQueue(wanted);
  if (!q.current) {
    return frag(h('div', { class: 'page-head' }, h('h1', { text: 'Full-text screening' })),
      h('p', { class: 'notice', text: q.hidden ? `Nothing left to assess here: ${plural(q.hidden, 'decision')} you sent wait for the maintainer to apply them.` : 'Nothing awaiting a full-text decision.' }));
  }
  const c = q.current;
  const pdf = ftPdf(c);
  const right = h('div', { class: 'right' });
  const layout = h('div', { class: 'review-layout ft', 'data-id': c.id, 'data-pdf': pdf?.url || '' }, ftLeft(q, c, pdf), right);
  if (pdf) mountPdf(right, pdf.url, null, null, null);
  else right.append(ftNoPdf(c, q));
  state.keyHandler = ftKeys;
  document.addEventListener('keydown', ftKeys);
  return layout;
}
function ftNoPdf(c, q) {
  const has = candidateHasPdf(c);
  const ctl = uploadControl(c.id, c.key, { required: true });
  const box = h('div', { class: 'pdf-missing ft-missing' },
    h('h3', { text: has ? 'The maintainer has this PDF, but it is not in the portal yet' : 'No PDF of this paper yet' }),
    h('p', { text: has ? 'It reaches the portal with the maintainer’s next sync. If you have a copy, upload it to assess the paper now.' : 'A full-text decision needs the paper. If you have it, upload it (or drop the file anywhere on this side); otherwise skip it for now.' }),
    ctl,
    h('p', { class: 'small' }, c.doi ? h('a', { href: `https://doi.org/${c.doi}`, target: '_blank', rel: 'noopener', text: 'Find it at the publisher (DOI)' }) : null, c.doi && c.pmid ? ' · ' : '', c.pmid ? h('a', { href: `https://pubmed.ncbi.nlm.nih.gov/${c.pmid}`, target: '_blank', rel: 'noopener', text: 'PubMed' }) : null),
    h('p', {}, h('button', { class: 'btn', onclick: () => ftSkip(c, q), text: 'Skip it for now (s)' })));
  dropZone(box, ctl.uploadFile);
  return box;
}
function ftSkip(c, q) {
  const skipped = new Set(store.get(FT_SKIP, [])); skipped.add(c.id); store.set(FT_SKIP, [...skipped]);
  const i = q.order.findIndex((x) => x.id === c.id);
  const next = q.order.slice(i + 1).find((x) => !q.decided[x.id]?.decision && !skipped.has(x.id)) || q.order.find((x) => !q.decided[x.id]?.decision && !skipped.has(x.id) && x.id !== c.id);
  toast(next ? `${c.id} skipped: it waits at the end of the queue` : `${c.id} skipped`);
  if (next) ftGo(next); else render();
}
function ftLeft(q, c, pdf) {
  const { order, decided, skipped } = q;
  const i = order.findIndex((x) => x.id === c.id);
  const dec = decided[c.id] || {};
  const nDecided = Object.entries(decided).filter(([id, d]) => d.decision && order.some((x) => x.id === id)).length;
  const save = (patch) => {
    decided[c.id] = { ...(decided[c.id] || {}), ...patch }; store.set('screen:ft', decided);
    if (patch.decision) { const s = new Set(store.get(FT_SKIP, [])); if (s.delete(c.id)) store.set(FT_SKIP, [...s]); }
    render();
  };
  const reasons = Object.entries(state.screening.reasons || {});
  const sendBtn = h('button', { class: 'btn btn-primary', disabled: nDecided ? null : '', text: nDecided ? `Send ${plural(nDecided, 'decision')}` : 'Send decisions' });
  const status = h('span', { class: 'muted small', text: `${i + 1} of ${order.length} · ${nDecided} decided, not sent${skipped.size ? ` · ${skipped.size} skipped` : ''}${q.hidden ? ` · ${q.hidden} sent, waiting for the maintainer` : ''}` });
  sendBtn.onclick = () => sendScreen('ft', Object.fromEntries(Object.entries(decided).filter(([id]) => order.some((x) => x.id === id))), order, sendBtn, status);
  const nav = h('div', { class: 'ft-nav' },
    h('button', { class: 'btn', disabled: i > 0 ? null : '', onclick: () => ftGo(order[i - 1]), text: '← Previous' }),
    h('button', { class: 'btn', onclick: () => ftSkip(c, q), text: 'Skip for now' }),
    h('button', { class: `btn${dec.decision ? ' btn-primary' : ''}`, disabled: i < order.length - 1 ? null : '', onclick: () => ftGo(order[i + 1]), text: 'Next →' }));
  const radio = (v) => {
    const blocked = v === 'include' && !pdf;
    return h('label', { class: blocked ? 'blocked' : null, title: blocked ? 'Include needs the PDF: upload it first' : null },
      h('input', { type: 'radio', name: `ft-${c.id}`, value: v, disabled: blocked ? '' : null, checked: dec.decision === v ? '' : null, onchange: () => save({ decision: v }) }), ` ${v}`);
  };
  const reasonSel = h('select', { 'aria-label': 'Exclusion reason', onchange: (e) => save({ reason: e.target.value }) }, h('option', { value: '', text: 'reason…' }), reasons.map(([k, v]) => h('option', { value: k, selected: dec.reason === k ? '' : null, text: v.label })));
  const card = h('article', { class: 'screen ft-card' },
    h('p', { class: 't' }, h('span', { class: 'chip', text: c.id }), ' ', esc(c.title)),
    h('p', { class: 'small muted' }, [c.year, c.journal, (c.authors || '').slice(0, 160)].filter(Boolean).join(' · '),
      c.doi ? [' · ', h('a', { href: `https://doi.org/${c.doi}`, target: '_blank', rel: 'noopener', text: c.doi })] : null,
      c.pmid ? [' · PMID ', h('a', { href: `https://pubmed.ncbi.nlm.nih.gov/${c.pmid}`, target: '_blank', rel: 'noopener', text: String(c.pmid) })] : null,
      c.for?.length ? ` · for ${c.for.join(', ')}` : '',
      c.history?.length ? ` · ${c.history.map((x) => `${x.stage === 'title_abstract' ? 'T/A' : 'FT'}: ${x.decision} (${x.by})`).join('; ')}` : ''),
    h('p', { class: 'small pdfline' }, pdf ? (pdf.upload ? uploadedNote(pdf.upload) : h('span', { class: 'badge badge-human', text: `PDF: ${pdf.label}` })) : h('span', { class: 'badge badge-warn', text: 'No PDF yet — upload it on the right, or skip' })),
    c.suggestion?.decision ? h('p', { class: 'sug', text: `Model suggests ${c.suggestion.decision}${c.suggestion.reason && c.suggestion.reason !== 'none' ? ` (${c.suggestion.reason})` : ''} — a suggestion, not a decision.` }) : null,
    h('div', { class: 'dec' }, ['include', 'exclude', 'unsure'].map(radio), reasonSel),
    h('input', { type: 'text', class: 'ft-note', value: dec.note || '', placeholder: 'note (optional)', onchange: (e) => save({ note: e.target.value }) }),
    dec.decision === 'exclude' && !dec.reason ? h('p', { class: 'small err-text', text: 'An exclusion needs a reason.' }) : null,
    h('details', { class: 'ft-abstract', open: pdf ? null : '' }, h('summary', { text: 'Abstract' }), h('p', { class: 'ab', text: c.abstract || '(no abstract available)' })));
  const list = h('ol', { class: 'ft-list' }, order.map((x, n) => {
    const d = decided[x.id]?.decision; const p = Boolean(ftPdf(x));
    return h('li', { class: `${x.id === c.id ? 'current' : ''}${d ? ' done' : ''}` },
      h('a', { href: `#/screen/ft/${encodeURIComponent(x.id)}` }, h('span', { class: 'chip', text: x.id }), ' ', String(x.title || '').slice(0, 90)),
      h('span', { class: 'small muted', text: ` ${[d || (skipped.has(x.id) ? 'skipped' : ''), p ? '' : 'no PDF'].filter(Boolean).join(' · ')}` }));
  }));
  return h('div', { class: 'left' },
    h('div', { class: 'page-head sticky-head' }, h('h1', { text: 'Full-text screening' }), status, h('span', { style: 'margin-left:auto' }, sendBtn)),
    nav, card,
    h('p', { class: 'small muted', text: 'Criteria: docs/SCREENING.md §2 — include when the paper answers a question in §1 and no exclusion reason applies. Keys: i include · e exclude · u unsure · s skip · ← → previous/next. Decisions stay in this browser until you send them.' }),
    h('h3', { text: 'The queue' }), list);
}
function ftKeys(e) {
  if (['INPUT', 'SELECT', 'TEXTAREA'].includes(e.target.tagName) && e.target.type !== 'radio') return;
  if (e.metaKey || e.ctrlKey || e.altKey) return;
  const [, , id] = parseRoute();
  const q = ftQueue(id); const c = q.current; if (!c) return;
  const i = q.order.findIndex((x) => x.id === c.id);
  const pick = (v) => { const r = document.querySelector(`.ft-card input[type=radio][value="${v}"]`); if (!r || r.disabled) { toast('Include needs the PDF: upload it first, or skip the paper', true); return; } r.checked = true; r.dispatchEvent(new Event('change')); };
  const k = e.key;
  if (k === 'i') pick('include');
  else if (k === 'u') pick('unsure');
  else if (k === 'e') { pick('exclude'); setTimeout(() => document.querySelector('.ft-card select')?.focus(), 0); }
  else if (k === 's') ftSkip(c, q);
  else if (k === 'ArrowRight' || k === 'n') ftGo(q.order[i + 1]);
  else if (k === 'ArrowLeft' || k === 'p') ftGo(q.order[i - 1]);
  else return;
  e.preventDefault();
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
    const noPdf = items.filter(([id, d]) => { const c = cands.find((x) => x.id === id); return d.decision === 'include' && c && !ftPdf(c); }).map(([id]) => id);
    if (noPdf.length) { toast(`Including a paper needs its PDF first: ${noPdf.join(', ')}`, true); return; }
  }
  working();
  try {
    const receipt = await sendAll(items.map(([id, d]) => ({ kind: 'screen', id, stage: st, decision: d.decision, reason: d.decision === 'exclude' ? d.reason : null, note: d.note || '' })));
    const sentLocal = store.get('screen:sent', {});
    const at = new Date().toISOString();
    for (const [i, [id, d]] of items.entries()) { delete decided[id]; sentLocal[id] = { at, stage, decision: d.decision, record: receipt.files?.[i]?.split('/').pop() }; }
    store.set(`screen:${stage}`, decided); store.set('screen:sent', sentLocal);
    toast(`Sent ${plural(items.length, 'decision')} — thank you. They leave the queue until the maintainer applies them${stage === 'ta' ? '; included papers then move to the Full text queue at the next build' : ''}.`);
    render();
    window.scrollTo(0, 0);
    document.querySelector('.screen')?.focus();
  } catch (e) { done(); toast(`Not sent: ${e.message}`, true); }
}

// ---- the PDFs the portal holds ----
function anyPaperUpload() {
  if (!state.uploadsOk) return null;
  let selected = null, busy = false, generation = 0;
  const title = h('input', { type: 'text', maxlength: 500, placeholder: 'Paper title', 'aria-label': 'Paper title', style: 'width:100%' });
  const doi = h('input', { type: 'text', placeholder: 'DOI (optional)', 'aria-label': 'DOI', style: 'width:100%' });
  const message = h('p', { class: 'small', role: 'status', text: 'Choose a PDF. Check its title and DOI before uploading; these identify the paper in the full register.' });
  const choices = h('select', { 'aria-label': 'Matching screening record', hidden: true });
  const choose = async (file) => {
    if (busy || !file) return;
    if (file.size > MAX_UPLOAD) { toast('The PDF limit is 60 MB.', true); return; }
    selected = file; const version = ++generation;
    title.value = ''; doi.value = ''; choices.hidden = true; choices.replaceChildren();
    message.textContent = `Selected ${file.name}. Reading its metadata locally…`;
    button.disabled = true;
    let doc;
    try {
      const lib = await pdfjs(); doc = await lib.getDocument({ data: new Uint8Array(await file.arrayBuffer()) }).promise;
      const meta = await doc.getMetadata();
      const page = await doc.getPage(1); const text = (await page.getTextContent()).items.map((x) => x.str || '').join(' ');
      if (version !== generation) return;
      title.value = String(meta.info?.Title || '').slice(0, 500);
      doi.value = (text.match(/10\.\d{4,9}\/[^\s<>]+/i)?.[0] || '').replace(/[.,;]+$/, '');
      message.textContent = 'Check the paper title and DOI below. PDF metadata can be incomplete or incorrect.';
    } catch { if (version === generation) message.textContent = 'Enter the paper title and DOI below; they could not be read reliably from this PDF.'; }
    finally { if (doc) await doc.destroy(); if (version === generation) button.disabled = false; }
  };
  const picker = h('input', { type: 'file', accept: '.pdf,application/pdf', 'aria-label': 'Upload any paper PDF', onchange: (e) => choose(e.target.files?.[0]) });
  const button = h('button', { class: 'btn btn-primary', text: 'Upload and check register', onclick: async () => {
    if (busy || !selected) { if (!selected) toast('Choose a PDF first.', true); return; }
    if (title.value.trim().length < 8) { toast('Enter the full paper title.', true); return; }
    busy = true; button.disabled = true; picker.disabled = true;
    try {
      const form = new FormData(); form.append('pdf', selected); form.append('title', title.value.trim()); form.append('doi', doi.value.trim());
      if (choices.value) form.append('candidate', choices.value);
      const response = await fetch('/api/paper-upload', { method: 'POST', body: form });
      const result = await response.json();
      if (!response.ok) {
        if (result.matches) { choices.replaceChildren(...result.matches.map((c) => h('option', { value: c.id, text: `${c.id}: ${c.title}` }))); choices.hidden = false; }
        throw new Error(result.error || `Upload failed (${response.status})`);
      }
      state.uploads.push(result.upload);
      if (state.screening) state.screening.candidates = mergePendingPapers(state.screening.candidates, state.uploads, state.screeningIndex);
      toast(result.matched ? 'PDF linked. Title/abstract screening stays in its current order.' : 'Paper added from another source, with its PDF, at the end of title/abstract screening.');
      for (const file of result.files || []) state.mine.inbox.push(file.split('/').pop());
      render();
    } catch (e) { message.textContent = e.message; toast(e.message, true); }
    finally { busy = false; button.disabled = false; picker.disabled = false; }
  } });
  return dropZone(h('section', { class: 'notice' }, h('h2', { text: 'Upload any paper' }),
    h('p', { text: 'Drop a PDF here or choose a file. We check the full screening register first. Matching papers get their PDF without moving the title/abstract queue; new papers are appended as records from other sources. Existing screening decisions are preserved.' }),
    picker, message, h('label', {}, 'Paper title', title), h('label', {}, 'DOI (optional)', doi), choices, button), choose);
}

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
    anyPaperUpload(),
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
    h('span', { class: 'small muted', text: d ? 'Highlights are the draft’s passages. Drag across words to quote them.' : 'The paper, for the full-text decision.' }));
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
function render({ preserveScroll = false } = {}) {
  // Capture at refresh time: reviewers may keep scrolling while a PDF uploads.
  const scroll = preserveScroll ? { left: window.scrollX, top: window.scrollY, behavior: 'instant' } : null;
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
  // Full-text screening: a decision re-renders only the left pane while the same paper and PDF stay on screen.
  const ftLayout = main.querySelector('.review-layout.ft');
  if (head === 'screen' && rest[0] === 'ft' && ftLayout && state.screening) {
    const q = ftQueue(rest[1]); const pdf = q.current ? ftPdf(q.current) : null;
    if (q.current && ftLayout.dataset.id === q.current.id && ftLayout.dataset.pdf === (pdf?.url || '')) {
      const leftEl = ftLayout.querySelector('.left'); const top = leftEl.scrollTop;
      leftEl.replaceWith(ftLeft(q, q.current, pdf));
      ftLayout.querySelector('.left').scrollTop = top;
      state.keyHandler = ftKeys; document.addEventListener('keydown', ftKeys);
      return;
    }
  }
  let view; let current = '/';
  try {
    if (!head) view = home();
    else if (head === 'drafts') { view = draftsList(); current = '/drafts'; }
    else if (head === 'draft') { view = draftView(rest.join('/')); current = '/drafts'; }
    else if (head === 'screen' && rest[0] === 'ft') { view = ftView(rest[1]); current = '/screen/ft'; }
    else if (head === 'screen') { view = screenView('ta'); current = '/screen/ta'; }
    else if (head === 'pdfs') { view = pdfsView(); current = '/pdfs'; }
    else if (head === 'mine') { view = mine(); current = '/mine'; }
    else view = h('p', { class: 'error', text: `Unknown page: ${head}` });
  } catch (err) { console.error(err); view = h('p', { class: 'error', text: `This page could not be rendered: ${err.message}` }); }
  main.replaceChildren(view);
  for (const a of document.querySelectorAll('.nav a')) { if (a.getAttribute('href') === `#${current}`) a.setAttribute('aria-current', 'page'); else a.removeAttribute('aria-current'); }
  if (scroll) window.scrollTo(scroll);
  else if (head !== 'draft') window.scrollTo(0, 0);
}

async function init() {
  const main = document.getElementById('main');
  try {
    const fresh = { cache: 'no-store' };
    const [me, manifest, kbText, bindings] = await Promise.all([api('me'), fetch('manifest.json', fresh).then((r) => r.json()),
      fetch('export/stroke-aphasia-kb-drafts.json', fresh).then((r) => r.text()),
      fetch('drafts.json', fresh).then((r) => (r.ok ? r.json() : null)).catch(() => null)]);
    const kb = JSON.parse(kbText);
    const kbSha = await sha256Hex(kbText).catch(() => '');
    state.me = me; state.manifest = manifest; state.kb = kb;
    // What each draft was when this page was built: a verdict is sent with it (review binding).
    // The three files must come from the same build, and the export must be the one the bindings
    // were computed against; anything mixed (a cached copy, a half-finished deploy) and no verdict
    // can be sent: fail closed, ask for a reload.
    const consistent = sameBuild(manifest, bindings, kb, kbSha);
    state.bindings = consistent ? (bindings.drafts || {}) : {};
    state.bindingProblem = consistent ? '' : 'The portal files loaded are not all from the same build: reload the page before sending a draft review.';
    state.screening = await fetch('screening.json', fresh).then((r) => (r.ok ? r.json() : null)).catch(() => null);
    state.screeningIndex = await fetch('screening-index.json', fresh).then((r) => r.ok ? r.json() : null).then((x) => x?.candidates || []).catch(() => []);
    store.set('screen:sent', pendingScreenReceipts(store.get('screen:sent', {}), state.screeningIndex));
    state.mine = await api('reviews').catch(() => ({ inbox: [], applied: [] }));
    try { const u = await api('upload'); state.uploads = u.uploads || []; state.uploadsOk = true; if (state.screening) state.screening.candidates = mergePendingPapers(state.screening.candidates, state.uploads, state.screeningIndex); } catch { state.uploads = []; state.uploadsOk = false; }
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
