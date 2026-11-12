// cc/ and pdf/ serve the annotated PDFs from the bucket (PDFS binding): the file name is
// checked, a missing object is 404, no binding is 503, If-None-Match gives 304, cc/ serves only what the
// build lists as public and nothing is cached; the middleware refuses pdf/* without an Access token and lets cc/* through.
// Run: node --test portal/functions/test/
import test from 'node:test';
import assert from 'node:assert/strict';
import { onRequestGet as cc } from '../cc/[[path]].js';
import { onRequestGet as pdf } from '../pdf/[[path]].js';
import { onRequest as middleware } from '../_middleware.js';

function bucket(files) {
  return {
    async get(key, opts) {
      const f = files[key]; if (!f) return null;
      const etag = `"${key.length}"`;
      if (opts?.onlyIf?.etagDoesNotMatch === key.length.toString()) return { httpEtag: etag, size: f.length };   // R2Object without body: unchanged
      return { httpEtag: etag, size: f.length, body: f };
    },
  };
}
const files = { 'cc/Open2020_annotated.pdf': 'open', 'pdf/Closed2021_annotated.pdf': 'closed', 'cc/Revoked2019_annotated.pdf': 'still in the bucket' };
// the build's public-pdfs.json, as the ASSETS binding serves it
const assets = (list) => ({ async fetch(req) { const u = new URL(req.url); return u.pathname === '/public-pdfs.json' && list ? new Response(JSON.stringify({ files: list })) : new Response('nope', { status: 404 }); } });
const env = { PDFS: bucket(files), ASSETS: assets(['Open2020_annotated.pdf']) };
const req = (url, headers = {}) => new Request(url, { headers });

test('cc/ and pdf/ serve the object with the right headers', async () => {
  let res = await cc({ request: req('https://p.test/cc/Open2020_annotated.pdf'), env, params: { path: ['Open2020_annotated.pdf'] } });
  assert.equal(res.status, 200);
  assert.equal(res.headers.get('Content-Type'), 'application/pdf');
  assert.equal(res.headers.get('Cache-Control'), 'no-store');
  assert.equal(await res.text(), 'open');
  res = await pdf({ request: req('https://p.test/pdf/Closed2021_annotated.pdf'), env, params: { path: ['Closed2021_annotated.pdf'] } });
  assert.equal(res.status, 200);
  assert.equal(res.headers.get('Cache-Control'), 'private, no-store');
  assert.equal(await res.text(), 'closed');
});

test('missing, malformed, unchanged and unconfigured', async () => {
  assert.equal((await cc({ request: req('https://p.test/cc/Nope.pdf'), env, params: { path: ['Nope.pdf'] } })).status, 404);
  assert.equal((await cc({ request: req('https://p.test/cc/x'), env, params: { path: ['..', 'Open2020_annotated.pdf'] } })).status, 404);
  assert.equal((await pdf({ request: req('https://p.test/pdf/Open2020_annotated.pdf'), env, params: { path: ['Open2020_annotated.pdf'] } })).status, 404);  // a cc paper is not under pdf/
  const same = await cc({ request: req('https://p.test/cc/Open2020_annotated.pdf', { 'If-None-Match': '"25"' }), env, params: { path: ['Open2020_annotated.pdf'] } });
  assert.equal(same.status, 304);
  assert.equal((await cc({ request: req('https://p.test/cc/Open2020_annotated.pdf'), env: {}, params: { path: ['Open2020_annotated.pdf'] } })).status, 503);
});

test('the middleware guards pdf/* like the API and lets cc/* through', async () => {
  const next = async () => new Response('through');
  const envM = { ACCESS_TEAM_DOMAIN: 't', ACCESS_AUD: 'a' };
  const passed = await middleware({ request: req('https://p.test/cc/Open2020_annotated.pdf'), env: envM, data: {}, next });
  assert.equal(await passed.text(), 'through');
  const refused = await middleware({ request: req('https://p.test/pdf/Closed2021_annotated.pdf'), env: envM, data: {}, next });
  assert.equal(refused.status, 401);
  assert.match(await refused.text(), /not signed in/);
});

test('cc/ serves only files the build lists as public, and fails closed (REVIEW.md finding 9)', async () => {
  const get = (e, name) => cc({ request: req(`https://p.test/cc/${name}`), env: e, params: { path: [name] } });
  // in the bucket (a delete failed) but no longer listed: not served
  assert.equal((await get(env, 'Revoked2019_annotated.pdf')).status, 404);
  // no allowlist in the build, or no ASSETS binding: nothing public is served
  assert.equal((await get({ PDFS: bucket(files), ASSETS: assets(null) }, 'Open2020_annotated.pdf')).status, 404);
  assert.equal((await get({ PDFS: bucket(files) }, 'Open2020_annotated.pdf')).status, 404);
  // the private path does not depend on the list
  const priv = await pdf({ request: req('https://p.test/pdf/Closed2021_annotated.pdf'), env: { PDFS: bucket(files) }, params: { path: ['Closed2021_annotated.pdf'] } });
  assert.equal(priv.status, 200);
});
