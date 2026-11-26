import test from 'node:test';
import assert from 'node:assert/strict';
import worker from './worker.js';
import {DatabaseSync} from 'node:sqlite';
import {readFileSync} from 'node:fs';
import {excluded} from '../../portal/lib/open-access.js';
test('unconfigured sign-in cannot expose assets or records',async()=>{
 for(const path of ['/','/records.json','/api/decisions']){
 const res=await worker.fetch(new Request('https://review.dysphagia-kb.app'+path),{});assert.equal(res.status,503);
 }
});

test('scheduled reconciliation resumes audit events and honours a later correction',async()=>{
 const db=new DatabaseSync(':memory:');db.exec(readFileSync(new URL('../../staging/dysphagia/schema.sql',import.meta.url),'utf8'));
 const files=new Map(),id='DYS-0123456789abcdef',reviewer='test@example.org';
 const bucket={async put(k,v){files.set(k,v);return{};},async delete(k){files.delete(k);},async get(k){const v=files.get(k);return v===undefined?null:{httpEtag:'"test"',text:async()=>v,json:async()=>JSON.parse(v)};},async list({prefix}){return{objects:[...files.keys()].filter(k=>k.startsWith(prefix)).map(key=>({key}))};}};
 const env={PRIVATE:bucket,SCREENING:{prepare(sql){return{bind(...values){return{async all(){return{results:db.prepare(sql).all(...values)};}};}};}}};
 function event(n,decision){
  const date=`2026-11-26T${String(n).padStart(2,'0')}:00:00Z`,value={id,stage:'title_abstract',decision,date};
  db.prepare('INSERT OR REPLACE INTO screening_decisions VALUES (?,?,?)').run(reviewer,id,JSON.stringify(value));
  db.prepare('INSERT INTO decision_events VALUES (?,?,?,?,?)').run('event-'+n,reviewer,date,n,JSON.stringify([value]));
 }
 event(1,'include');event(2,'exclude');files.set(`open-access/pdf/${id}.pdf`,'PDF');
 await worker.scheduled({},env);
 assert.equal(await excluded(bucket,id),true);assert.equal(files.has(`open-access/pdf/${id}.pdf`),false);
 assert.equal(JSON.parse(files.get('open-access/decision-cursor.json')).event,2);
 event(3,'include');await worker.scheduled({},env);
 assert.equal(await excluded(bucket,id),false);assert.ok(files.has(`open-access/retry/${id}.json`));
 files.delete(`open-access/retry/${id}.json`);await worker.scheduled({},env);
 assert.equal(files.has(`open-access/retry/${id}.json`),false);assert.ok(files.has('open-access/decisions-ready.json'));
 db.close();
});
test('missing identity cannot reach private R2 or assets',async()=>{
 for(const path of ['/','/records-000.json','/api/decisions']){
 const res=await worker.fetch(new Request('https://review.dysphagia-kb.app'+path),{ACCESS_AUD:'dedicated-audience'});assert.equal(res.status,401);
 }
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
 const env={ACCESS_AUD:'dysphagia',ACCESS_TEAM_DOMAIN:'test-team',PRIVATE:{async get(key){reads.push(key);return {body:'private screening bundle'};}}};
 const request=async(aud)=>new Request('https://review.dysphagia-kb.app/records-000.json',{headers:{'Cf-Access-Jwt-Assertion':await token(aud)}});
 assert.equal((await worker.fetch(await request('aphasia'),env)).status,401);
 assert.deepEqual(reads,[]);
 const res=await worker.fetch(await request('dysphagia'),env);
 assert.equal(res.status,200);
 assert.equal(await res.text(),'private screening bundle');
 assert.equal(res.headers.get('Cache-Control'),'no-store');
 assert.deepEqual(reads,['screening/records-000.json']);
});
