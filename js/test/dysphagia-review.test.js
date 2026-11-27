import test from 'node:test';
import assert from 'node:assert/strict';
import {instrumentalLabels,prioritiseInstrumentalStudies} from '../../portal/web/dysphagia-priority.js';
import {candidate,createDysphagiaReview} from '../../portal/web/dysphagia-review.js';
test('FEES/VFSS title and abstract matches move first without changing or dropping records',()=>{
 const rows=[{id:'a',title:'Consultation fees'},{id:'b',title:'Stroke',abstract:'Evaluated with FEES.'},{id:'c',title:'Video-fluoroscopic swallowing assessment'},{id:'d',title:'Ordinary study'},{id:'e',abstract:'Flexible endoscopic evaluation of swallowing'}];
 assert.deepEqual(prioritiseInstrumentalStudies(rows).map(r=>r.id),['b','c','e','a','d']);
 assert.deepEqual(rows.map(r=>r.id),['a','b','c','d','e']);
 assert.deepEqual(instrumentalLabels({title:'VFSS and FEES'}),['FEES','VFSS']);
 assert.deepEqual(instrumentalLabels({title:'Modified barium swallow'}),['VFSS']);
});
test('stage transitions retain separate decisions and never turn TA inclusion into final inclusion',()=>{
 const row={id:'a',authors:['Smith','Jones']},ta={stage:'title_abstract',decision:'include'},ft={stage:'full_text',decision:'include'};
 assert.equal(candidate(row).stage,'awaiting_ta');assert.equal(candidate(row,ta).stage,'awaiting_ft');
 assert.equal(candidate(row,ta,ft).stage,'included');
 assert.equal(candidate(row,{...ta,decision:'exclude'},ft).stage,'excluded');
 assert.equal(candidate(row,ta,{...ft,decision:'unsure'}).stage,'unsure_ft');
 assert.equal(candidate(row,ta,ft).history.length,2);assert.equal(candidate(row).authors,'Smith; Jones');
});
test('legacy browser choices migrate once, preserving new edits and notes',async t=>{
 const mem=new Map([['dysphagia-production:me@example.org:2026-11-23',JSON.stringify({one:{decision:'include',notes:'retain',reason:''}})]]);
 t.mock.method(globalThis,'fetch',async path=>Response.json(path==='records.json'?{chunks:['records-000.json'],summary:{search_date:'2026-11-23'}}:[{id:'one',title:'FEES',authors:[]} ]));
 const storage={getItem:k=>mem.get(k)||null,setItem:(k,v)=>mem.set(k,v)};
 const adapter=createDysphagiaReview(async()=>({reviewer:'me@example.org',decisions:{},sha:0}),storage);
 await adapter.load();const key='dysphagia:me@example.org:screen:ta';assert.equal(JSON.parse(mem.get(key)).one.note,'retain');
 mem.set(key,'{}');await adapter.load();assert.deepEqual(JSON.parse(mem.get(key)),{});
 assert.ok(mem.has('dysphagia-production:me@example.org:2026-11-23'));
});
