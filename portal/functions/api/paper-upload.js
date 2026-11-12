// Upload any paper: match the full deployed register plus pending submissions,
// atomically record candidate registration/priority and PDF intake in GitHub.
import { putRecords } from '../../lib/github.js';
import { MAX_BYTES, objectKey, onRequestGet as listUploads } from './upload.js';
import { normalizeDoi, normalizeTitle, matchPapers } from '../../web/paper-intake.js';

export async function onRequestPost({ request, env, data }) {
  if (!env.UPLOADS || !env.ASSETS) return Response.json({ error: 'Paper intake is not configured.' }, { status: 503 });
  if (Number(request.headers.get('Content-Length') || 0) > MAX_BYTES + 10000) return Response.json({ error: 'PDF limit: 60 MB.' }, { status: 413 });
  let form;
  try { form = await request.formData(); } catch { return Response.json({ error: 'Choose a PDF and enter its title.' }, { status: 400 }); }
  const file = form.get('pdf');
  const title = String(form.get('title') || '').trim();
  const doi = normalizeDoi(form.get('doi'));
  if (title.length < 8 || title.length > 500 || (doi && !/^10\.\d{4,9}\/\S{1,180}$/.test(doi))) return Response.json({ error: 'Enter the paper title (8–500 characters) and a valid DOI, or leave DOI blank.' }, { status: 400 });
  if (!file || typeof file.arrayBuffer !== 'function' || file.size < 1024 || file.size > MAX_BYTES) return Response.json({ error: 'Choose a PDF between 1 KB and 60 MB.' }, { status: 400 });
  const buf = await file.arrayBuffer();
  if (!new TextDecoder().decode(new Uint8Array(buf, 0, 5)).startsWith('%PDF-')) return Response.json({ error: 'This file is not a PDF.' }, { status: 400 });
  let register, uploads;
  try {
    const res = await env.ASSETS.fetch(new Request(new URL('/screening-index.json', request.url)));
    if (!res.ok) throw new Error('missing index');
    register = (await res.json()).candidates;
    if (!Array.isArray(register)) throw new Error('invalid index');
    uploads = (await (await listUploads({ env })).json()).uploads;
  } catch { return Response.json({ error: 'Cannot check the screening register. Please try again later.' }, { status: 503 }); }
  const pending = uploads.filter((u) => u.candidate && !register.some((c) => c.id === u.id || (c.upload_ids || []).includes(u.id))).map((u) => u.candidate);
  const matches = matchPapers({ title, doi }, [...register, ...pending]);
  const chosen = String(form.get('candidate') || '');
  if (matches.length > 1 && !matches.some((c) => c.id === chosen)) return Response.json({ error: 'Several records match. Choose the paper you are uploading.', matches }, { status: 409 });
  const match = matches.find((c) => c.id === chosen) || matches[0];
  // Same title with a conflicting DOI requires correction, not a silent duplicate.
  if (!match && doi && [...register, ...pending].some((c) => normalizeTitle(c.title) === normalizeTitle(title))) return Response.json({ error: 'This title is already registered with another DOI. Check the DOI or ask the maintainer to resolve the record.' }, { status: 409 });
  const hash = async (bytes) => [...new Uint8Array(await crypto.subtle.digest('SHA-256', bytes))].map((b) => b.toString(16).padStart(2, '0')).join('');
  const id = match?.id || `U${(await hash(new TextEncoder().encode(doi || normalizeTitle(title)))).slice(0, 32)}`;
  const key = objectKey(id), sha256 = await hash(buf), uploaded = new Date().toISOString();
  if (await env.UPLOADS.head(key)) return Response.json({ error: 'A PDF for this paper is already waiting in the portal. Open it from the screening queue.', id }, { status: 409 });
  const candidate = match || { id, title, doi: doi || null, stage: 'awaiting_ta', sources: [{ kind: 'hand_picked', note: 'Reviewer PDF upload (other source)' }] };
  const name = String(file.name || 'paper.pdf').replace(/[^\w.() -]+/g, '_').slice(0, 120);
  // Metadata stays small; no abstract or PDF text is sent to GitHub.
  const summary = Object.fromEntries(['id', 'key', 'title', 'doi', 'stage'].filter((k) => candidate[k]).map((k) => [k, candidate[k]]));
  summary.title = String(summary.title || '').slice(0, 200);
  const stored = await env.UPLOADS.put(key, buf, { onlyIf: new Headers({ 'If-None-Match': '*' }), httpMetadata: { contentType: 'application/pdf' }, customMetadata: { id, name, by: data.reviewer.email, sha256, uploaded, candidate: JSON.stringify(summary) } });
  if (!stored) return Response.json({ error: 'Another reviewer just uploaded this paper. Reload to see their PDF.' }, { status: 409 });
  try {
    const result = await putRecords(env, data.reviewer, [
      { kind: 'paper', id, body: { title: candidate.title, doi: candidate.doi || null, new_candidate: !match, uploaded } },
      { kind: 'pdf', id, body: { name, bytes: buf.byteLength, sha256, bucket: env.UPLOADS_BUCKET || '', object: key } },
    ]);
    return Response.json({ ok: true, ...result, matched: Boolean(match), candidate, upload: { id, name, bytes: buf.byteLength, uploaded, by: data.reviewer.email, object: key, candidate: summary } });
  } catch (e) {
    await env.UPLOADS.delete(key).catch(() => {});
    return Response.json({ error: `Could not save the screening record: ${e.message}` }, { status: 502 });
  }
}
