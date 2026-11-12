import test from 'node:test';
import assert from 'node:assert/strict';
import { runProgress } from '../api/apply.js';
import { applyState } from '../../web/apply-state.js';

const run = {id:123, head_sha:'a'.repeat(40), run_attempt:2, status:'in_progress'};
test('only matching workflow attempt supplies the record counter', async () => {
  globalThis.fetch = async url => url.includes('check-runs')
    ? Response.json({check_runs:[{external_id:'portal-apply:123:1',output:{summary:JSON.stringify({version:1,total:99,current:99,processed:99})}},
      {external_id:'portal-apply:123:2',output:{summary:JSON.stringify({version:1,total:9,current:2,processed:1,phase:'applying'})}}]})
    : Response.json({jobs:[{steps:[{name:'Apply the inbox',status:'in_progress'}]}]});
  const progress = await runProgress({GITHUB_REPO:'o/r'},run);
  assert.equal(progress.progress.current,2);
  assert.equal(applyState({...run,...progress}).label,'Applying 2 of 9');
  assert.equal(applyState({...run,...progress,phase:'checking'}).label,'Checking changes…');
});
test('publication waits for both sites at the exact pushed commit', async () => {
  const sha='b'.repeat(40);
  globalThis.fetch = async url => {
    if (url.includes('check-runs')) return Response.json({check_runs:[{external_id:'portal-apply:123:2',output:{summary:JSON.stringify({version:1,total:9,current:9,processed:9,phase:'published',published_sha:sha})}}]});
    assert.ok(url.includes(`head_sha=${sha}`));
    return Response.json({workflow_runs:[{path:'.github/workflows/portal.yml',status:'in_progress'},
      {path:'.github/workflows/pages.yml',status:'completed',conclusion:'success'}]});
  };
  const completed={...run,status:'completed',conclusion:'success'};
  const result=await runProgress({GITHUB_REPO:'o/r'},completed);
  assert.equal(applyState({...completed,...result}).label,'Rebuilding sites…');
  assert.equal(applyState({...completed,...result}).poll,true);
  assert.equal(applyState({...completed,publication:{status:'success'}}).poll,false);
  assert.match(applyState({...completed,publication:{status:'success'}}).next,/Refresh/);
  assert.match(applyState({...completed,publication:{status:'failure'}}).next,/failed/);
});
test('missing telemetry and workflow failures never invent counts or success', async () => {
  globalThis.fetch=async()=>new Response('',{status:403});
  const result=await runProgress({GITHUB_REPO:'o/r'},run);
  assert.equal(result.progress,null);
  assert.equal(applyState({...run,...result}).label,'Preparing to apply…');
  assert.match(applyState({status:'completed',conclusion:'failure'}).next,/Do not assume/);
});
