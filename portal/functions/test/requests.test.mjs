// "I'd like to become a reviewer": the public form endpoint (/welcome/request) and the
// maintainer's list (/api/requests), against a fake bucket, a fake GitHub and a fake mail
// Worker. A request is checked, kept privately once per email, and announced by email when
// a mail Worker is bound, otherwise through the GitHub workflow (never more than once per
// ten minutes, and with nothing personal). Only maintainers read or remove requests.
// Run: node --test portal/functions/test/
import test from 'node:test';
import assert from 'node:assert/strict';
import { onRequestPost, onRequest } from '../welcome/request.js';
import { onRequestGet, onRequestDelete } from '../api/requests.js';
import { onRequestGet as signin } from '../api/signin.js';
import { MAX_WAITING, WORKFLOW, keyFor, notify, validate } from '../../lib/requests.js';

function bucket() {
  const store = new Map();
  return {
    store,
    async head(k) { return store.get(k) || null; },
    async get(k) { const o = store.get(k); return o ? { json: async () => JSON.parse(o.body) } : null; },
    async put(k, body, opts = {}) { store.set(k, { key: k, body: String(body), customMetadata: opts.customMetadata || {} }); },
    async delete(k) { store.delete(k); },
    async list({ prefix = '' } = {}) { return { objects: [...store.values()].filter((o) => o.key.startsWith(prefix)), truncated: false }; },
  };
}
const calls = [];
let dispatchStatus = 204;
globalThis.fetch = async (url, init = {}) => {
  calls.push({ url: String(url), method: init.method || 'GET', body: init.body ? JSON.parse(init.body) : null });
  return { ok: dispatchStatus < 300, status: dispatchStatus, json: async () => ({}), text: async () => '' };
};
const env = (b, extra = {}) => ({ UPLOADS: b, GITHUB_REPO: 'o/r', GITHUB_TOKEN: 't', GITHUB_BRANCH: 'main', MAINTAINERS: 'maint@example.org', ...extra });
const ask = (e, body, type = 'application/json') => onRequestPost({ request: new Request('https://review.test/welcome/request', { method: 'POST', headers: { 'Content-Type': type }, body: typeof body === 'string' ? body : JSON.stringify(body) }), env: e });
const zoe = { name: '  Zoé   Tremblay ', email: 'Zoe@Example.org', affiliation: 'UdeM', note: 'Speech-language pathologist.\nTen years with aphasia.' };
const as = (email) => ({ reviewer: { email, name: 'x' } });

test('a request is checked, kept privately and announced through GitHub with nothing personal', async () => {
  calls.length = 0;
  const b = bucket();
  const res = await ask(env(b), zoe);
  assert.equal(res.status, 200); assert.deepEqual(await res.json(), { ok: true });
  const kept = JSON.parse(b.store.get(await keyFor('zoe@example.org')).body);
  assert.equal(kept.name, 'Zoé Tremblay'); assert.equal(kept.email, 'zoe@example.org'); assert.match(kept.requested, /^\d{4}-\d\d-\d\dT/);
  assert.equal(kept.note, 'Speech-language pathologist.\nTen years with aphasia.');
  const dispatch = calls.filter((c) => c.url.includes(`/actions/workflows/${WORKFLOW}/dispatches`));
  assert.equal(dispatch.length, 1); assert.deepEqual(dispatch[0].body, { ref: 'main' });                 // no name, no email
  assert.ok(!JSON.stringify(calls).toLowerCase().includes('zoe'));
});

test('the same email again replaces the request and does not notify twice; a new person within ten minutes is stored quietly', async () => {
  calls.length = 0;
  const b = bucket();
  await ask(env(b), zoe);
  await ask(env(b), { ...zoe, note: 'Updated note' });
  assert.equal([...b.store.keys()].filter((k) => k.endsWith('.json')).length, 1);
  assert.equal(JSON.parse(b.store.get(await keyFor('zoe@example.org')).body).note, 'Updated note');
  await ask(env(b), { name: 'Sam', email: 'sam@example.org' });
  assert.equal([...b.store.keys()].filter((k) => k.endsWith('.json')).length, 2);
  assert.equal(calls.filter((c) => c.url.includes('/dispatches')).length, 1);
});

test('what is refused: bad input, other content types, oversized bodies, a full list; a filled trap field is ignored', async () => {
  const b = bucket();
  assert.equal((await ask(env(b), { name: '', email: 'a@b.org' })).status, 400);
  assert.equal((await ask(env(b), { name: 'A', email: 'not an email' })).status, 400);
  assert.equal((await ask(env(b), { name: 'A', email: 'a@b.org, c@d.org' })).status, 400);                 // one address, not a list
  assert.equal((await ask(env(b), 'name=A', 'application/x-www-form-urlencoded')).status, 415);
  assert.equal((await ask(env(b), { name: 'A', email: 'a@b.org', note: 'x'.repeat(9000) })).status, 413);
  assert.equal((await ask(env(b), '{not json')).status, 400);
  assert.equal((await ask(env({ ...b, UPLOADS: undefined }, { UPLOADS: undefined }), zoe)).status, 503);
  assert.equal((await onRequest()).status, 405);
  const trap = await ask(env(b), { ...zoe, website: 'https://spam.example' });
  assert.equal(trap.status, 200); assert.equal(b.store.size, 0);                                            // looks accepted, nothing kept
  assert.equal(validate({ name: 'A\u0000B', email: 'A@B.org', note: 'x'.repeat(5000) }).request.note.length, 1500);
  for (let i = 0; i < MAX_WAITING; i += 1) await b.put(`requests/${String(i).padStart(24, '0')}.json`, '{}');
  assert.equal((await ask(env(b), zoe)).status, 429);
});

test('with a mail Worker bound the maintainers get the request by email, and GitHub is the fallback', async () => {
  calls.length = 0;
  const b = bucket();
  const mails = [];
  const MAILER = { fetch: async (url, init) => { mails.push(JSON.parse(init.body)); return new Response('{"ok":true}'); } };
  await ask(env(b, { MAILER }), zoe);
  assert.equal(mails.length, 1); assert.deepEqual(mails[0].to, ['maint@example.org']);
  assert.equal(mails[0].request.email, 'zoe@example.org'); assert.equal(mails[0].portalUrl, 'https://review.test');
  assert.equal(calls.filter((c) => c.url.includes('/dispatches')).length, 0);
  const broken = { fetch: async () => new Response('no', { status: 502 }) };
  assert.deepEqual(await notify(env(bucket(), { MAILER: broken }), { name: 'A', email: 'a@b.org' }, 'https://review.test'), { by: 'github' });
  dispatchStatus = 403;
  assert.equal((await notify(env(bucket()), { name: 'A', email: 'a@b.org' }, 'u')).by, 'none');           // never throws
  const stillStored = await ask(env(bucket()), zoe);
  assert.equal(stillStored.status, 200);                                                                   // a failed notification is not the person's problem
  dispatchStatus = 204;
});

test('only a maintainer reads and removes requests', async () => {
  const b = bucket();
  await ask(env(b), zoe); await ask(env(b), { name: 'Sam', email: 'sam@example.org' });
  assert.equal((await onRequestGet({ env: env(b), data: as('sam@example.org') })).status, 403);
  const out = await (await onRequestGet({ env: env(b), data: as('Maint@Example.org') })).json();
  assert.deepEqual(out.requests.map((r) => r.email).sort(), ['sam@example.org', 'zoe@example.org']);
  assert.match(out.requests[0].id, /^[0-9a-f]{24}$/);
  const del = (id, who) => onRequestDelete({ request: new Request(`https://review.test/api/requests?id=${id}`, { method: 'DELETE' }), env: env(b), data: as(who) });
  assert.equal((await del(out.requests[0].id, 'sam@example.org')).status, 403);
  assert.equal((await del('../uploads/x', 'maint@example.org')).status, 404);                              // an id is 24 hex digits, nothing else
  assert.equal((await del(out.requests[0].id, 'maint@example.org')).status, 200);
  assert.equal((await (await onRequestGet({ env: env(b), data: as('maint@example.org') })).json()).requests.length, 1);
});

test('the sign-in link sends a signed-in reviewer on to the portal', async () => {
  const res = signin({ request: new Request('https://review.test/api/signin') });
  assert.equal(res.status, 302); assert.equal(res.headers.get('Location'), 'https://review.test/');
});
