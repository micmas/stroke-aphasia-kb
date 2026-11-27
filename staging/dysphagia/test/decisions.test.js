import test from 'node:test';
import assert from 'node:assert/strict';
import {validate,onRequest,BRANCH} from '../functions/api/decisions.js';
const d={id:'DYS-0123456789abcdef',decision:'include',reason:'',notes:''};
test('rejects Aphasia IDs and requires exclusion reasons',()=>{
 assert.equal(validate({decisions:[d]}),null);
 assert.ok(validate({decisions:[{...d,id:'C123'}]}));
 assert.ok(validate({decisions:[{...d,decision:'exclude'}]}));
});
test('refuses production branch before any network request',async()=>{
 const response=await onRequest({env:{GITHUB_BRANCH:'main'}});
 assert.equal(response.status,503);
});
import {DatabaseSync} from 'node:sqlite';
import {readFileSync} from 'node:fs';
function database(){
 const db=new DatabaseSync(':memory:');db.exec(readFileSync(new URL('../schema.sql',import.meta.url),'utf8'));
 return {db,prepare(sql){return {bind(...values){return {sql,values,async first(){return db.prepare(sql).get(...values)||null;},async all(){return {results:db.prepare(sql).all(...values)};}};}};},async batch(statements){db.exec('BEGIN');try{const result=statements.map(s=>({meta:{changes:Number(db.prepare(s.sql).run(...s.values).changes)}}));db.exec('COMMIT');return result;}catch(e){db.exec('ROLLBACK');throw e;}}};
}
test('transaction saves attributed decisions and audit, then rejects stale revision',async()=>{
 const storage=database(),env={GITHUB_BRANCH:BRANCH,SCREENING:storage},data={reviewer:{email:'test@example.org'}};
 const submit=async(body)=>onRequest({request:new Request('https://staging/api/decisions',{method:'POST',body:JSON.stringify(body)}),env,data});
 const first=await submit({sha:0,decisions:[d]});assert.equal(first.status,200);
 assert.equal((await first.json()).decisions[d.id].reviewer,'test@example.org');
 const stale=await submit({sha:0,decisions:[{...d,decision:'unsure'}]});assert.equal(stale.status,409);
 const read=await onRequest({request:new Request('https://staging/api/decisions'),env,data});assert.equal((await read.json()).decisions[d.id].decision,'include');
 assert.equal(storage.db.prepare('SELECT COUNT(*) n FROM decision_events').get().n,1);
 const other=await onRequest({request:new Request('https://staging/api/decisions'),env,data:{reviewer:{email:'other@example.org'}}});assert.deepEqual((await other.json()).decisions,{});
 storage.db.close();
});
test('concurrent saves yield one winner and one audit event',async()=>{
 const storage=database(),env={GITHUB_BRANCH:BRANCH,SCREENING:storage},data={reviewer:{email:'test@example.org'}};
 const results=await Promise.all(['include','unsure'].map(decision=>onRequest({request:new Request('https://staging/api/decisions',{method:'POST',body:JSON.stringify({sha:0,decisions:[{...d,decision}]})}),env,data})));
 assert.deepEqual(results.map(r=>r.status).sort(),[200,409]);
 assert.equal(storage.db.prepare('SELECT COUNT(*) n FROM decision_events').get().n,1);storage.db.close();
});
test('production explicitly opts into the same durable Dysphagia decisions',async()=>{
 const storage=database(),data={reviewer:{email:'test@example.org'}};
 const response=await onRequest({request:new Request('https://preview/api/decisions',{method:'POST',body:JSON.stringify({sha:0,decisions:[d]})}),env:{GITHUB_BRANCH:BRANCH,SCREENING:storage},data});
 assert.equal(response.status,200);
 const production=await onRequest({request:new Request('https://review.aphasia-kb.app/api/dysphagia-decisions'),env:{GITHUB_BRANCH:'main',SCREENING_CHAPTER:'dysphagia',SCREENING:storage},data});
 assert.equal(production.status,200);assert.equal((await production.json()).decisions[d.id].decision,'include');storage.db.close();
});
test('full-text decisions require TA inclusion and a PDF, preserve TA and use separate revisions',async()=>{
 const storage=database(),files=new Map();
 const bucket={async head(k){return files.has(k)?{key:k}:null;},async get(k){return null;},async put(){return{};},async delete(){},async list(){return{objects:[]};}};
 const env={GITHUB_BRANCH:BRANCH,SCREENING:storage,PRIVATE:bucket},data={reviewer:{email:'test@example.org'}};
 const submit=async(stage,decision='include',sha=0)=>onRequest({request:new Request('https://preview/api/decisions',{method:'POST',body:JSON.stringify({sha,decisions:[{...d,decision,reason:decision==='exclude'?'wrong_question':''}]})}),env,data},stage);
 assert.equal((await submit('full_text')).status,400);
 assert.equal((await submit('title_abstract')).status,200);
 assert.equal((await submit('full_text')).status,400);
 files.set(`uploads/${d.id}.pdf`,true);
 assert.equal((await submit('full_text')).status,200);
 assert.equal(JSON.parse(storage.db.prepare('SELECT value FROM screening_decisions').get().value).stage,'title_abstract');
 assert.equal(JSON.parse(storage.db.prepare('SELECT value FROM fulltext_decisions').get().value).stage,'full_text');
 assert.equal((await submit('full_text','exclude',0)).status,409);
 assert.equal((await submit('full_text','exclude',1)).status,200);
 assert.equal(storage.db.prepare('SELECT COUNT(*) n FROM fulltext_events').get().n,2);
 storage.db.close();
});
