import test from 'node:test';
import assert from 'node:assert/strict';
import {DatabaseSync} from 'node:sqlite';
import {readFileSync} from 'node:fs';
import worker,{decisions,validate,reconcileOpenAccess} from './worker.js';
const id='PLE-0123456789abcdef';
const choice=(stage='title_abstract',patch={})=>({id,stage,decision:'include',notes:'',reason:'',...patch});
function bucket(){
 const files=new Map([['screening/record-ids.json',JSON.stringify([id])]]);
 return {files,async get(key){const v=files.get(key);return v===undefined?null:{body:v,size:v.length,httpEtag:'"test"',text:async()=>v,json:async()=>JSON.parse(v)};},
 async put(key,value){files.set(key,value);return{};},async delete(key){files.delete(key);},async head(key){return files.has(key)?{}:null;},
 async list({prefix}){return {objects:[...files.keys()].filter(key=>key.startsWith(prefix)).map(key=>({key}))};}};
}
function fixture(){
 const db=new DatabaseSync(':memory:');db.exec(readFileSync(new URL('./schema.sql',import.meta.url),'utf8'));
 const prepare=sql=>({bind(...values){return {async first(){return db.prepare(sql).get(...values);},async all(){return {results:db.prepare(sql).all(...values)};},async run(){return {meta:{changes:Number(db.prepare(sql).run(...values).changes)}};}};}});
 return {db,env:{PRIVATE:bucket(),SCREENING:{prepare,async batch(items){db.exec('BEGIN');try{const result=[];for(const item of items)result.push(await item.run());db.exec('COMMIT');return result;}catch(e){db.exec('ROLLBACK');throw e;}}}}};
}
const req=body=>new Request('https://review.test/api/decisions',body?{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)}:{});
test('unconfigured and unauthenticated requests cannot expose private assets',async()=>{
 for(const path of ['/','/records.json','/records-000.json','/api/decisions']){
  assert.equal((await worker.fetch(new Request('https://review.test'+path),{})).status,503);
  assert.equal((await worker.fetch(new Request('https://review.test'+path),{ACCESS_AUD:'practice'})).status,401);
 }
});
test('stage gates, unknown records and incomplete evidence are rejected',()=>{
 const ids=new Set([id]);
 assert.match(validate({decisions:[choice('full_text')]},ids,{}),/preceding/);
 assert.match(validate({decisions:[choice('title_abstract',{id:'DYS-0123456789abcdef'})]},ids,{}),/Unknown/);
 assert.match(validate({decisions:[choice('title_abstract',{decision:'exclude'})]},ids,{}),/reason/);
 const saved={['title_abstract:'+id]:choice(),['full_text:'+id]:choice('full_text')};
 assert.match(validate({decisions:[choice('evidence_review')]},ids,saved),/source passage/);
 assert.match(validate({decisions:[choice('full_text',{evidence:{source_url:'javascript:alert(1)'}})]},ids,saved),/HTTP/);
});
test('durable stage decisions, isolated reviewers, stale saves and append-only history',async()=>{
 const {db,env}=fixture();
 try{
  let response=await decisions(req({sha:0,decisions:[choice()]}),env,'a@example.test');assert.equal(response.status,200);
  assert.equal((await response.json()).sha,1);
  assert.equal((await decisions(req({sha:0,decisions:[choice()]}),env,'a@example.test')).status,409);
  assert.deepEqual((await (await decisions(req(),env,'b@example.test')).json()).decisions,{});
  assert.equal((await decisions(req({sha:1,decisions:[choice('full_text')]}),env,'a@example.test')).status,200);
  const evidence=Object.fromEntries(['claim','passage','locator','perspective','limitations','appraisal'].map(k=>[k,'Source-checked '+k]));
  response=await decisions(req({sha:2,decisions:[choice('evidence_review',{evidence})]}),env,'a@example.test');assert.equal(response.status,200);
  const saved=(await response.json()).decisions['evidence_review:'+id];assert.equal(saved.reviewer,'a@example.test');assert.equal(saved.clinical_domain,'aphasia');
  assert.equal(db.prepare('SELECT COUNT(*) AS n FROM decision_events').get().n,3);
 }finally{db.close();}
});

test('only the dedicated signed identity can fetch records from its private bucket', async (t) => {
 const keys = await crypto.subtle.generateKey({name:'RSASSA-PKCS1-v1_5',modulusLength:2048,publicExponent:new Uint8Array([1,0,1]),hash:'SHA-256'},true,['sign','verify']);
 const jwk = await crypto.subtle.exportKey('jwk',keys.publicKey);
 jwk.kid='review-test';
 t.mock.method(globalThis,'fetch',async()=>Response.json({keys:[jwk]}));
 async function token(aud) {
  const h=Buffer.from(JSON.stringify({alg:'RS256',kid:jwk.kid})).toString('base64url');
  const p=Buffer.from(JSON.stringify({aud,email:'reviewer@example.test',exp:Math.floor(Date.now()/1000)+60})).toString('base64url');
  const signature=await crypto.subtle.sign('RSASSA-PKCS1-v1_5',keys.privateKey,new TextEncoder().encode(`${h}.${p}`));
  return `${h}.${p}.${Buffer.from(signature).toString('base64url')}`;
 }
 const reads=[];
 const env={ACCESS_AUD:'practice',ACCESS_TEAM_DOMAIN:'test-team',PRIVATE:{async get(key){reads.push(key);return {body:'private screening bundle'};}}};
 const request=async(aud)=>new Request('https://review.stroke-kb.app/records-000.json',{headers:{'Cf-Access-Jwt-Assertion':await token(aud)}});
 assert.equal((await worker.fetch(await request('aphasia'),env)).status,401);
 assert.deepEqual(reads,[]);
 const res=await worker.fetch(await request('practice'),env);
 assert.equal(res.status,200);
 assert.equal(await res.text(),'private screening bundle');
 assert.equal(res.headers.get('Cache-Control'),'no-store');
 assert.deepEqual(reads,['screening/records-000.json']);
});

test('saved screening exclusions remove only this collection copy; note rejection keeps PDFs',async()=>{
 const {db,env}=fixture(),other=bucket(),pdf='open-access/pdf/'+id+'.pdf';
 try{
  await env.PRIVATE.put(pdf,'PDF');await other.put(pdf,'same paper in another collection');
  const save=async(sha,d)=>{const res=await decisions(req({sha,decisions:[d]}),env,'a@example.test');assert.equal(res.status,200);return res.json();};
  await save(0,choice());await save(1,choice('full_text'));
  await save(2,choice('evidence_review',{decision:'exclude',reason:'unsupported note'}));
  assert.ok(await env.PRIVATE.head(pdf));
  await save(3,choice('full_text',{decision:'exclude',reason:'wrong population'}));
  assert.equal(await env.PRIVATE.head(pdf),null);assert.ok(await other.head(pdf));
  const history=db.prepare('SELECT COUNT(*) AS n FROM decision_events').get();assert.equal(history.n,4);
  await save(4,choice('full_text'));
  assert.ok(await env.PRIVATE.head('open-access/retry/'+id+'.json'));
 }finally{db.close();}
});
test('reconciliation repairs interrupted PDF removal using current stage values and preserves saved decisions',async()=>{
 const {db,env}=fixture(),pdf='open-access/pdf/'+id+'.pdf',original=env.PRIVATE.put;
 try{
  await env.PRIVATE.put(pdf,'PDF');
  env.PRIVATE.put=async()=>{throw Error('temporary storage outage');};
  const res=await decisions(req({sha:0,decisions:[choice('title_abstract',{decision:'exclude',reason:'wrong population'})]}),env,'a@example.test');
  assert.equal(res.status,200);assert.match((await res.json()).oaWarning,/saved/);
  env.PRIVATE.put=original;await reconcileOpenAccess(env);
  assert.equal(await env.PRIVATE.head(pdf),null);
  assert.ok(await env.PRIVATE.head('open-access/decisions-ready.json'));
  assert.equal((await (await env.PRIVATE.get('open-access/decision-cursor.json')).json()).event,1);
  await decisions(req({sha:1,decisions:[choice()]}),env,'a@example.test');
  await reconcileOpenAccess(env);
  assert.equal((await (await env.PRIVATE.get('open-access/decision-cursor.json')).json()).event,2);
 }finally{db.close();}
});
