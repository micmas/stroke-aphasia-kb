// /api/apply: a maintainer (MAINTAINERS) starts the apply workflow through the GitHub API, a
// reviewer is refused, a run already going is reported instead of started twice, GET reports
// the latest run and the inbox size. Run: node --test portal/functions/test/
import test from 'node:test';
import assert from 'node:assert/strict';
import { onRequestGet, onRequestPost, WORKFLOW } from '../api/apply.js';

const calls = [];
let runs = [];
globalThis.fetch = async (url, init = {}) => {
  calls.push({ url, method: init.method || 'GET', body: init.body ? JSON.parse(init.body) : null });
  const json = (status, payload) => ({ ok: status < 300, status, json: async () => payload, text: async () => JSON.stringify(payload) });
  if (url.includes(`/actions/workflows/${WORKFLOW}/runs`)) return json(200, { workflow_runs: runs });
  if (url.includes(`/actions/workflows/${WORKFLOW}/dispatches`)) return { ok: true, status: 204, text: async () => '' };
  if (url.includes('/contents/logs/portal/inbox')) return json(200, [{ type: 'file', name: 'a_screen_x_c1.json' }, { type: 'file', name: 'b_screen_x_c2.json' }]);
  if (url.includes('/contents/logs/portal/applied')) return json(404, {});
  return json(404, {});
};
const env = { GITHUB_REPO: 'o/r', GITHUB_TOKEN: 't', GITHUB_BRANCH: 'main', MAINTAINERS: 'Maint@Example.org, other@example.org' };
const as = (email) => ({ reviewer: { email, name: 'x' } });

test('GET reports the inbox and the latest run, and who may apply', async () => {
  runs = [{ status: 'completed', conclusion: 'success', created_at: '2026-11-09T10:00:00Z', updated_at: '2026-11-09T10:03:00Z', html_url: 'https://github.com/o/r/actions/runs/1', event: 'workflow_dispatch' }];
  const out = await (await onRequestGet({ env, data: as('maint@example.org') })).json();
  assert.equal(out.inbox, 2); assert.equal(out.maintainer, true); assert.equal(out.run.conclusion, 'success'); assert.equal(out.run.url, 'https://github.com/o/r/actions/runs/1');
  const other = await (await onRequestGet({ env, data: as('sam@example.org') })).json();
  assert.equal(other.maintainer, false);
});

test('POST starts the workflow for a maintainer only, once', async () => {
  calls.length = 0; runs = [];
  const res = await onRequestPost({ env, data: as('maint@example.org') });
  assert.equal(res.status, 200);
  const dispatch = calls.find((c) => c.url.includes('/dispatches'));
  assert.equal(dispatch.method, 'POST'); assert.equal(dispatch.body.ref, 'main'); assert.equal(dispatch.body.inputs.requested_by, 'maint@example.org');
  calls.length = 0;
  assert.equal((await onRequestPost({ env, data: as('sam@example.org') })).status, 403);
  assert.equal(calls.length, 0);
  runs = [{ status: 'in_progress', conclusion: null, created_at: '2026-11-09T10:00:00Z', html_url: 'u' }];
  const again = await (await onRequestPost({ env, data: as('maint@example.org') })).json();
  assert.equal(again.alreadyRunning, true);
  assert.equal(calls.filter((c) => c.url.includes('/dispatches')).length, 0);
});

test('four PDFs and two orphan edits are not six actionable records', async () => {
  const saved = globalThis.fetch;
  const names = ['1_pdf_x_c1.json','2_pdf_x_c2.json','3_pdf_x_c3.json','4_pdf_x_c4.json','5_edit_x_one.json','6_edit_x_two.json'];
  let dispatched = false;
  globalThis.fetch = async (url) => {
    if (url.includes('/dispatches')) { dispatched = true; return new Response(null, {status:204}); }
    if (url.includes('/runs?')) return Response.json({workflow_runs:[]});
    if (url.includes('/contents/logs/portal/applied')) return new Response('',{status:404});
    if (url.includes('/contents/drafts/')) return new Response('',{status:404});
    if (url.includes('/inbox/') && url.includes('_edit_')) return Response.json({content:Buffer.from(JSON.stringify({id:'drafts/regions/already_approved.md'})).toString('base64')});
    if (url.includes('/contents/logs/portal/inbox')) return Response.json(names.map(name=>({type:'file',name})));
    throw new Error(`Unexpected request ${url}`);
  };
  try {
    const out = await (await onRequestGet({env,data:as('maint@example.org')})).json();
    assert.equal(out.inbox,6); assert.equal(out.ready,0); assert.equal(out.pdf,4); assert.equal(out.attention.length,2);
    const post = await (await onRequestPost({env,data:as('maint@example.org')})).json();
    assert.equal(post.nothingToApply,true); assert.equal(dispatched,false);
  } finally { globalThis.fetch=saved; }
});
