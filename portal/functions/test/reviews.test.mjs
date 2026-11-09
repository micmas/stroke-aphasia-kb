// /api/reviews against a fake GitHub: one record is one contents-API commit; several records
// sent together are one git-data commit holding one file per record (so a "Send" of many
// screening decisions is one push); malformed records are refused before anything is written;
// a branch that moved under us is retried on its new head. Run: node --test portal/functions/test/
import test from 'node:test';
import assert from 'node:assert/strict';
import { onRequestPost } from '../api/reviews.js';

const calls = [];
let headSha = 'aaaa111';
let moveFailuresLeft = 0;
globalThis.fetch = async (url, init = {}) => {
  const body = init.body ? JSON.parse(init.body) : null;
  calls.push({ url, method: init.method || 'GET', body });
  const json = (status, payload) => ({ ok: status < 300, status, json: async () => payload, text: async () => JSON.stringify(payload) });
  if (url.endsWith('/git/ref/heads/main')) return json(200, { object: { sha: headSha } });
  if (url.endsWith('/git/trees')) return json(201, { sha: 'tree0001' });
  if (url.endsWith('/git/commits')) return json(201, { sha: 'c0ffee1234567' });
  if (url.endsWith('/git/refs/heads/main')) {
    if (moveFailuresLeft > 0) { moveFailuresLeft -= 1; headSha = 'bbbb222'; return json(422, { message: 'Update is not a fast forward' }); }
    return json(200, { object: { sha: 'c0ffee1234567' } });
  }
  if (url.includes('/contents/')) return json(201, { commit: { sha: 'abc1234def' } });
  return json(404, {});
};
const env = { GITHUB_REPO: 'o/r', GITHUB_TOKEN: 't', GITHUB_BRANCH: 'main' };
const data = { reviewer: { email: 'alex@example.org', name: 'alex' } };
const post = (body) => onRequestPost({ request: new Request('https://p.test/api/reviews', { method: 'POST', body: JSON.stringify(body) }), env, data });
const screen = (id, decision) => ({ kind: 'screen', id, stage: 'title_abstract', decision, reason: null, note: '' });

test('one record is one contents-API commit', async () => {
  calls.length = 0;
  const res = await post(screen('C0001', 'include'));
  const out = await res.json();
  assert.equal(res.status, 200);
  assert.equal(calls.length, 1);
  assert.match(calls[0].url, /contents\/logs\/portal\/inbox\/\d{8}T\d{6}Z_screen_alex_c0001\.json$/);
  assert.equal(out.files.length, 1); assert.equal(out.file, out.files[0]); assert.equal(out.commit, 'abc1234');
});

test('several records are one commit with one file each', async () => {
  calls.length = 0;
  const res = await post({ records: [screen('C0001', 'include'), screen('C0002', 'exclude'), { kind: 'comment', id: 'drafts/therapies/x__Y2020.md', text: 'hi' }] });
  const out = await res.json();
  assert.equal(res.status, 200);
  assert.deepEqual(calls.map((c) => c.method + ' ' + c.url.split('/repos/o/r/')[1]), ['GET git/ref/heads/main', 'POST git/trees', 'POST git/commits', 'PATCH git/refs/heads/main']);
  const tree = calls[1].body;
  assert.equal(tree.base_tree, headSha);
  assert.equal(tree.tree.length, 3);
  assert.match(tree.tree[0].path, /^logs\/portal\/inbox\/\d{8}T\d{6}Z-01_screen_alex_c0001\.json$/);
  assert.match(tree.tree[2].path, /^logs\/portal\/inbox\/\d{8}T\d{6}Z-03_comment_alex_therapies-x-y2020\.json$/);
  const rec = JSON.parse(tree.tree[1].content);
  assert.equal(rec.kind, 'screen'); assert.equal(rec.decision, 'exclude'); assert.equal(rec.reviewer, 'alex@example.org'); assert.equal(rec.portal, 1);
  assert.equal(calls[2].body.parents[0], headSha);
  assert.match(calls[2].body.message, /^Portal: 3 screen, comment records by alex@example.org$/);
  assert.equal(calls[3].body.force, false);
  assert.equal(out.files.length, 3); assert.equal(out.commit, 'c0ffee1');
});

test('a branch that moved is retried on its new head; bad records are refused before any write', async () => {
  calls.length = 0; headSha = 'aaaa111'; moveFailuresLeft = 1;
  const res = await post({ records: [screen('C1', 'include'), screen('C2', 'include')] });
  assert.equal(res.status, 200);
  const refReads = calls.filter((c) => c.url.endsWith('/git/ref/heads/main'));
  assert.equal(refReads.length, 2);
  assert.equal(calls.filter((c) => c.url.endsWith('/git/trees'))[1].body.base_tree, 'bbbb222');
  calls.length = 0;
  assert.equal((await post({ records: [screen('C1', 'include'), { kind: 'bogus', id: 'x' }] })).status, 400);
  assert.equal((await post({ records: [{ kind: 'screen' }] })).status, 400);
  assert.equal((await post({ records: [] })).status, 400);
  assert.equal(calls.length, 0);
});
