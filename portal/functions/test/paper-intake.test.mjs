import test from 'node:test';
import assert from 'node:assert/strict';
import { matchPapers, prioritizePapers, orderScreeningPapers, mergePendingPapers } from '../../web/paper-intake.js';
import { onRequestPost } from '../api/paper-upload.js';

test('DOI canonicalization, title fallback and conflicting DOI protection', () => {
  const cs = [{ id: 'C1', title: 'Language after stroke!', doi: '10.1234/test' }, { id: 'C2', title: 'Another paper' }];
  assert.equal(matchPapers({doi:'https://doi.org/10.1234/TEST'}, cs)[0].id, 'C1');
  assert.equal(matchPapers({title:'LANGUAGE after stroke'}, cs)[0].id, 'C1');
  assert.deepEqual(matchPapers({title:'Language after stroke',doi:'10.1234/else'}, cs), []);
  assert.deepEqual(matchPapers({title:'Language after stroke'}, [{...cs[0], duplicate_of:'C2'}]), []);
});
test('pending records appear immediately, aliases do not duplicate, upload priority survives import', () => {
  const cs = [{id:'C1'}, {id:'C2',pdf_uploaded_at:'2026-11-12'}];
  const ups = [{id:'U123',uploaded:'2026-11-13',candidate:{id:'U123',stage:'awaiting_ta'}}];
  assert.equal(prioritizePapers(mergePendingPapers(cs,ups),ups)[0].id,'U123');
  assert.equal(prioritizePapers(cs,[])[0].id,'C2');
  assert.equal(mergePendingPapers([{id:'C9',upload_ids:['U123']}],ups).length,1);
});
function context(candidates=[],fail=false) {
  const store=new Map(); const commits=[];
  const env={GITHUB_REPO:'o/r',GITHUB_TOKEN:'test',UPLOADS_BUCKET:'uploads',ASSETS:{fetch:async()=>Response.json({candidates})},UPLOADS:{
    list:async()=>({objects:[...store.values()],truncated:false}),head:async k=>store.get(k),delete:async k=>store.delete(k),
    put:async(k,b,opts)=>{const o={key:k,size:b.byteLength,customMetadata:opts.customMetadata};store.set(k,o);return o;}
  }};
  globalThis.fetch=async(url,init)=>{
    if(fail)return new Response('failed',{status:502});
    if(url.includes('/git/ref/heads/'))return Response.json({object:{sha:'head'}});
    if(url.includes('/git/trees')){commits.push(JSON.parse(init.body));return Response.json({sha:'tree'});}
    return Response.json({sha:'commit'});
  };
  const send=async(title,doi='')=>{
    const form=new FormData();form.set('title',title);form.set('doi',doi);form.set('pdf',new Blob(['%PDF-1.4\n'+' '.repeat(2048)],{type:'application/pdf'}),'paper.pdf');
    return onRequestPost({request:new Request('https://p.test/api/paper-upload',{method:'POST',body:form}),env,data:{reviewer:{email:'test@example.org',name:'Tester'}}});
  };
  return {send,store,commits,env};
}
test('existing full-register paper matched without changing its screening stage', async()=>{
 const c=context([{id:'C900',title:'An existing paper',doi:'10.1234/a',stage:'excluded_ta'}]);
 const res=await c.send('An existing paper','10.1234/a');const out=await res.json();
 assert.equal(res.status,200);assert.equal(out.candidate.id,'C900');assert.equal(out.candidate.stage,'excluded_ta');assert.equal(out.matched,true);
 const records=c.commits[0].tree.map(x=>JSON.parse(x.content));assert.deepEqual(records.map(r=>r.kind),['paper','pdf']);assert.equal(records[0].new_candidate,false);
 assert.equal((await c.send('An existing paper','10.1234/a')).status,409);
});
test('unmatched PDF creates stable other-source identity; failed commit rolls back upload',async()=>{
 const c=context();const res=await c.send('A previously unknown paper');const out=await res.json();assert.equal(res.status,200);
 assert.match(out.candidate.id,/^U[0-9a-f]{32}$/);assert.equal(out.candidate.stage,'awaiting_ta');assert.equal(out.matched,false);
 const failed=context([],true);assert.equal((await failed.send('A previously unknown paper')).status,502);assert.equal(failed.store.size,0);
});
test('ambiguous matches and missing full index fail without storing a PDF',async()=>{
 const c=context([{id:'C1',title:'A duplicated title'},{id:'C2',title:'A duplicated title'}]);assert.equal((await c.send('A duplicated title')).status,409);assert.equal(c.store.size,0);
 c.env.ASSETS.fetch=async()=>new Response('',{status:404});assert.equal((await c.send('An unknown title')).status,503);
});
test('conditional storage refuses concurrent upload without a GitHub record',async()=>{
 const c=context();c.env.UPLOADS.put=async()=>null;
 assert.equal((await c.send('A simultaneous paper')).status,409);assert.equal(c.commits.length,0);
});
test('applied exclusions do not reappear through stale upload metadata',()=>{
 const ups=[{id:'Uold',candidate:{id:'Uold',stage:'awaiting_ta'}}];
 assert.deepEqual(mergePendingPapers([],ups,[{id:'Uold',stage:'excluded_ta'}]),[]);
 assert.deepEqual(mergePendingPapers([],ups,[{id:'C1',upload_ids:['Uold'],stage:'included'}]),[]);
});


test('PDF uploads keep title/abstract order and append new papers', () => {
  const original = [{id:'C1'}, {id:'C2',pdf_uploaded_at:'2026-11-12'}];
  const uploads = [{id:'C2',uploaded:'2026-11-13'},
    {id:'U1',uploaded:'2026-11-14',candidate:{id:'U1',stage:'awaiting_ta'}}];
  const combined = mergePendingPapers(original, uploads);
  assert.deepEqual(orderScreeningPapers(combined, uploads, 'ta').map(c=>c.id), ['C1','C2','U1']);
  assert.deepEqual(orderScreeningPapers(combined, [], 'ta').map(c=>c.id), ['C1','C2','U1']);
  assert.deepEqual(original.map(c=>c.id), ['C1','C2']);
  assert.equal(orderScreeningPapers(original, uploads, 'ft')[0].id, 'C2');
});

test('screen receipts survive rebuilds until the exact decision is in the register', async () => {
 const { pendingScreenReceipts } = await import('../../web/paper-intake.js');
 const sent = {C1:{at:'2026-11-12T01:00:00Z',stage:'ta',decision:'unsure',record:'new.json'}};
 assert.deepEqual(pendingScreenReceipts(sent,[{id:'C1',stage:'awaiting_ta',history:[]}]),sent);
 assert.deepEqual(pendingScreenReceipts(sent,[{id:'C1',stage:'unsure_ta',history:[{record:'old.json'}]}]),sent);
 assert.deepEqual(pendingScreenReceipts(sent,[{id:'C1',stage:'unsure_ta',history:[{record:'new.json'}]}]),{});
 assert.deepEqual(pendingScreenReceipts(sent,[]),sent);
 const old={C1:{stage:'ta',decision:'include'}};
 assert.deepEqual(pendingScreenReceipts(old,[{id:'C1',stage:'awaiting_ta'}]),old);
 assert.deepEqual(pendingScreenReceipts(old,[{id:'C1',stage:'awaiting_ft'}]),{});
});
