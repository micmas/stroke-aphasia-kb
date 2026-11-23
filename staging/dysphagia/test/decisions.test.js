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
