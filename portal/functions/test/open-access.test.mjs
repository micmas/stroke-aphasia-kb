import test from 'node:test';
import assert from 'node:assert/strict';
import {syncOaDecisions,serveOpenAccess,pdfKey,excluded} from '../../lib/open-access.js';
function bucket(){
 const files=new Map();return{files,
 async put(k,v){files.set(k,v);return{};},async delete(k){files.delete(k);},async head(k){return files.has(k)?{}:null;},
 async get(k){const v=files.get(k);return v===undefined?null:{body:v,size:v.length,httpEtag:'"test"',text:async()=>v,json:async()=>JSON.parse(v)};},
 async list({prefix,limit=1000}){return{objects:[...files.keys()].filter(k=>k.startsWith(prefix)).slice(0,limit).map(key=>({key}))};}};
}
const d=(decision,date='2026-11-26T00:00:00Z')=>({id:'C1234',stage:'title_abstract',decision,date});
test('exclusion deletes only collected bytes, retains provenance, and refuses downloads',async()=>{
 const b=bucket();await b.put(pdfKey('C1234'),'PDF');await b.put('pdf/C1234_source.pdf','working');
 await b.put('open-access/status/C1234.json',JSON.stringify({status:'available',source:{sha256:'audit'}}));
 await syncOaDecisions(b,'reviewer@example.org',[d('exclude')]);
 assert.equal(await b.head(pdfKey('C1234')),null);assert.ok(await b.head('pdf/C1234_source.pdf'));
 assert.equal((await (await serveOpenAccess(new Request('https://review/api/open-access?id=C1234'),b)).json()).status,'excluded');
 assert.equal((await serveOpenAccess(new Request('https://review/api/open-access?id=C1234&file=1'),b)).status,404);
 assert.equal((await b.get('open-access/status/C1234.json')).json instanceof Function,true);
});
test('including queues retrieval once; stale reconciliation and another reviewer cannot undo exclusion',async()=>{
 const b=bucket();await syncOaDecisions(b,'a',[d('exclude','2026-11-26T02:00:00Z')]);
 await syncOaDecisions(b,'a',[d('include','2026-11-26T01:00:00Z')]);assert.ok(await excluded(b,'C1234'));
 await syncOaDecisions(b,'b',[d('include','2026-11-26T03:00:00Z')]);assert.ok(await excluded(b,'C1234'));
 await syncOaDecisions(b,'a',[d('include','2026-11-26T03:00:00Z')]);assert.equal(await excluded(b,'C1234'),false);
 await b.delete('open-access/retry/C1234.json');
 await syncOaDecisions(b,'a',[d('include','2026-11-26T03:00:00Z')]);assert.equal(await b.head('open-access/retry/C1234.json'),null);
});
test('invalid ids and check opinions cannot delete files; tombstone persists if deletion fails',async()=>{
 const b=bucket();await syncOaDecisions(b,'a',[{...d('exclude'),role:'check'},{...d('exclude'),id:'../pdf/source'}]);assert.equal(b.files.size,0);
 b.delete=async()=>{throw new Error('storage outage');};
 await assert.rejects(syncOaDecisions(b,'a',[d('exclude')]));assert.ok(await excluded(b,'C1234'));
 assert.equal((await serveOpenAccess(new Request('https://review/api/open-access?id=..%2Fsource&file=1'),b)).status,400);
});
test('decision metadata avoids per-reviewer reads for large screening batches',async()=>{
 const b=bucket();b.list=async()=>({objects:[{key:'first',customMetadata:{decision:'include'}},{key:'second',customMetadata:{decision:'exclude'}}]});
 b.get=async()=>{assert.fail('R2 metadata should avoid another subrequest');};
 assert.equal(await excluded(b,'C1234'),true);
});
test('conditional-write conflict rereads the newer decision instead of undoing it',async()=>{
 const b=bucket();const put=b.put;
 let conflict=true;
 b.put=async(k,v,options)=>{
  if(conflict&&options?.onlyIf){conflict=false;await put(k,JSON.stringify(d('exclude','2026-11-26T05:00:00Z')));return null;}
  return put(k,v,options);
 };
 await syncOaDecisions(b,'a',[d('include','2026-11-26T04:00:00Z')]);
 assert.equal(await excluded(b,'C1234'),true);
 assert.equal(await b.head('open-access/retry/C1234.json'),null);
});
test('available index reconciles excluded and missing copies before full-text screening',async()=>{
 const b=bucket();await b.put('open-access/index.json',JSON.stringify({C1234:{status:'available'},C1235:{status:'available'},C1236:{status:'available'}}));
 await b.put(pdfKey('C1234'),'PDF');await b.put(pdfKey('C1235'),'PDF');
 await syncOaDecisions(b,'a',[d('exclude')]);
 const response=await serveOpenAccess(new Request('https://review/api/open-access?available=1'),b);
 assert.deepEqual(Object.keys((await response.json()).papers),['C1235']);
});
