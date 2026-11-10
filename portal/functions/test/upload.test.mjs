// /api/upload against a fake bucket and a fake GitHub: a PDF is stored with the reviewer's
// name and a `pdf` record is written; a non-PDF, an oversized body, a missing id, a second
// reviewer's duplicate and a missing bucket are refused. Run: node --test portal/functions/test/
import test from 'node:test';
import assert from 'node:assert/strict';
import { onRequestPost, onRequestGet, objectKey, MAX_BYTES } from '../api/upload.js';

function bucket() {
  const store = new Map();
  return {
    store,
    async head(k) { return store.get(k) || null; },
    async put(k, buf, opts) { store.set(k, { key: k, size: buf.byteLength, customMetadata: opts.customMetadata, uploaded: new Date() }); },
    async delete(k) { store.delete(k); },
    async list() { return { objects: [...store.values()], truncated: false }; },
  };
}
const commits = [];
globalThis.fetch = async (url, init) => {
  commits.push({ url, body: JSON.parse(init.body) });
  return { ok: true, status: 201, json: async () => ({ commit: { sha: 'abc1234def' } }), text: async () => '' };
};
const pdf = (n = 4096) => { const b = Buffer.alloc(n, 0x20); b.write('%PDF-1.4\n'); return b; };
const env = (b) => ({ UPLOADS: b, UPLOADS_BUCKET: 'test-bucket', GITHUB_REPO: 'o/r', GITHUB_TOKEN: 't', GITHUB_BRANCH: 'main' });
const data = { reviewer: { email: 'alex@example.org', name: 'alex' } };
const post = (b, q, body, d = data) => onRequestPost({ request: new Request(`https://p.test/api/upload?${q}`, { method: 'POST', body, headers: { 'Content-Length': String(body.length) } }), env: env(b), data: d });

test('a PDF is stored under the id and recorded for the maintainer', async () => {
  const b = bucket();
  const res = await post(b, 'id=C0123&name=smith 2020.pdf&citation=@Smith2020', pdf());
  const out = await res.json();
  assert.equal(res.status, 200);
  assert.equal(out.object, objectKey('C0123'));
  const obj = b.store.get('uploads/c0123.pdf');
  assert.equal(obj.customMetadata.by, 'alex@example.org');
  assert.equal(obj.customMetadata.name, 'smith 2020.pdf');
  assert.match(obj.customMetadata.sha256, /^[0-9a-f]{64}$/);
  const rec = commits.at(-1).body;
  assert.match(commits.at(-1).url, /logs\/portal\/inbox\/\d{8}T\d{6}Z_pdf_alex_c0123\.json$/);
  const record = JSON.parse(Buffer.from(rec.content, 'base64').toString('utf8'));
  assert.equal(record.kind, 'pdf'); assert.equal(record.id, 'C0123'); assert.equal(record.citation, '@Smith2020');
  assert.equal(record.bucket, 'test-bucket'); assert.equal(record.object, 'uploads/c0123.pdf'); assert.equal(record.bytes, 4096);
  const list = await (await onRequestGet({ env: env(b) })).json();
  assert.deepEqual(list.uploads.map((u) => [u.id, u.by, u.name]), [['C0123', 'alex@example.org', 'smith 2020.pdf']]);
});

test('refusals: not a PDF, too large, no id, someone else already uploaded, no bucket', async () => {
  const b = bucket();
  assert.equal((await post(b, 'id=C1', Buffer.alloc(4096, 0x41))).status, 400);
  assert.equal((await post(b, 'id=C1', Buffer.alloc(100))).status, 400);
  assert.equal((await post(b, 'name=x.pdf', pdf())).status, 400);
  const big = new Request('https://p.test/api/upload?id=C1', { method: 'POST', body: pdf(), headers: { 'Content-Length': String(MAX_BYTES + 1) } });
  assert.equal((await onRequestPost({ request: big, env: env(b), data })).status, 413);
  assert.equal((await post(b, 'id=C2', pdf())).status, 200);
  const other = { reviewer: { email: 'sam@example.org', name: 'sam' } };
  assert.equal((await post(b, 'id=C2', pdf(), other)).status, 409);
  assert.equal((await post(b, 'id=C2', pdf())).status, 200);           // the same reviewer may replace it
  assert.equal((await onRequestPost({ request: new Request('https://p.test/api/upload?id=C3', { method: 'POST', body: pdf() }), env: { GITHUB_REPO: 'o/r' }, data })).status, 503);
  assert.equal((await onRequestGet({ env: { } })).status, 503);
});

test('a failed GitHub write removes the stored file again', async () => {
  const b = bucket();
  const saved = globalThis.fetch;
  globalThis.fetch = async () => ({ ok: false, status: 401, text: async () => 'Bad credentials' });
  const res = await post(b, 'id=C9', pdf());
  globalThis.fetch = saved;
  assert.equal(res.status, 502);
  assert.equal(b.store.size, 0);
});

test('an upload can be read back for the full-text screen; an unknown one is 404', async () => {
  const bytes = pdf(2048);
  const b = { async get(k) { return k === 'uploads/c0456.pdf' ? { body: bytes, size: bytes.length } : null; } };
  const ok = await onRequestGet({ request: new Request('https://p.test/api/upload?file=C0456'), env: { UPLOADS: b } });
  assert.equal(ok.status, 200);
  assert.equal(ok.headers.get('Content-Type'), 'application/pdf');
  assert.equal(ok.headers.get('Cache-Control'), 'private, no-store');
  assert.equal(Buffer.from(await ok.arrayBuffer()).subarray(0, 5).toString(), '%PDF-');
  assert.equal((await onRequestGet({ request: new Request('https://p.test/api/upload?file=C9999'), env: { UPLOADS: b } })).status, 404);
});
