// POST /api/upload?id=<candidate id or citation key>&name=<file name>[&citation=<key>]   body: the PDF bytes
//      — store a paper's PDF a reviewer has (and the portal lacks) in the private R2 bucket,
//        then write a `pdf` record into logs/portal/inbox/ so scripts/portal_import.py pulls
//        the file into papers/ (the maintainer's OneDrive folder) and deletes it here.
// GET  /api/upload — the uploads waiting in the bucket (id, name, who, when), so the portal
//        can say "PDF uploaded, with the maintainer" and let the full-text decision through.
//
// The bucket is bound as UPLOADS in portal/wrangler.toml ([[r2_buckets]]); without the
// binding the route answers 503 and the portal hides the control. Nothing here is public:
// the middleware has already verified the Access token (data.reviewer).
import { putRecord, slug } from '../../lib/github.js';

export const MAX_BYTES = 60 * 1024 * 1024;   // Pages Functions accept 100 MB bodies on the free plan
const PREFIX = 'uploads/';

export const objectKey = (id) => `${PREFIX}${slug(id)}.pdf`;

function describe(obj) {
  const m = obj.customMetadata || {};
  return { object: obj.key, id: m.id || obj.key.slice(PREFIX.length, -4), name: m.name || '', bytes: obj.size, by: m.by || '', uploaded: m.uploaded || (obj.uploaded ? new Date(obj.uploaded).toISOString() : ''), sha256: m.sha256 || '' };
}

export async function onRequestGet({ env }) {
  if (!env.UPLOADS) return Response.json({ error: 'uploads are not set up on this portal (no R2 bucket bound)', uploads: [] }, { status: 503 });
  const out = [];
  let cursor;
  do {
    const page = await env.UPLOADS.list({ prefix: PREFIX, cursor, include: ['customMetadata'] });
    for (const obj of page.objects || []) out.push(describe(obj));
    cursor = page.truncated ? page.cursor : undefined;
  } while (cursor);
  return Response.json({ uploads: out });
}

export async function onRequestPost({ request, env, data }) {
  if (!env.UPLOADS) return Response.json({ error: 'uploads are not set up on this portal (no R2 bucket bound)' }, { status: 503 });
  const url = new URL(request.url);
  const id = String(url.searchParams.get('id') || '').trim();
  const name = String(url.searchParams.get('name') || '').trim().replace(/[^\w.() -]+/g, '_').slice(0, 120) || 'paper.pdf';
  const citation = String(url.searchParams.get('citation') || '').trim();
  if (!id) return Response.json({ error: 'id is required (the candidate id, or the citation key)' }, { status: 400 });
  const declared = Number(request.headers.get('Content-Length') || 0);
  if (declared > MAX_BYTES) return Response.json({ error: `file too large (${Math.round(declared / 1048576)} MB; the limit is ${MAX_BYTES / 1048576} MB)` }, { status: 413 });
  const buf = await request.arrayBuffer();
  if (buf.byteLength > MAX_BYTES) return Response.json({ error: `file too large (the limit is ${MAX_BYTES / 1048576} MB)` }, { status: 413 });
  if (buf.byteLength < 1024) return Response.json({ error: 'that is not a PDF (too small)' }, { status: 400 });
  const head = new TextDecoder('latin1').decode(new Uint8Array(buf, 0, 8));
  if (!head.startsWith('%PDF-')) return Response.json({ error: 'that is not a PDF (no %PDF header)' }, { status: 400 });
  const key = objectKey(id);
  const existing = await env.UPLOADS.head(key);
  if (existing && (existing.customMetadata?.by || '') !== data.reviewer.email) {
    return Response.json({ error: `a PDF for ${id} was already uploaded by ${existing.customMetadata?.by || 'someone'} and is waiting for the maintainer` }, { status: 409 });
  }
  const digest = await crypto.subtle.digest('SHA-256', buf);
  const sha256 = [...new Uint8Array(digest)].map((b) => b.toString(16).padStart(2, '0')).join('');
  const uploaded = new Date().toISOString();
  await env.UPLOADS.put(key, buf, { httpMetadata: { contentType: 'application/pdf' }, customMetadata: { id, name, by: data.reviewer.email, sha256, uploaded } });
  try {
    const { file, commit } = await putRecord(env, data.reviewer, 'pdf', id, { citation: citation || null, name, bytes: buf.byteLength, sha256, bucket: env.UPLOADS_BUCKET || '', object: key, replaced: Boolean(existing) });
    return Response.json({ ok: true, file, commit, object: key, bytes: buf.byteLength });
  } catch (e) {
    await env.UPLOADS.delete(key).catch(() => {});
    return Response.json({ error: `stored, then could not record it: ${e.message}` }, { status: e.status || 502 });
  }
}
