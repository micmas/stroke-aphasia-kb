import test from 'node:test';
import assert from 'node:assert/strict';
import {coveragePage, summaryTiles} from '../../explorer/chapter-presentation.js';
class Node {
  constructor(tag){this.tag=tag;this.children=[];this.attrs={};this.textContent='';}
  setAttribute(k,v){this.attrs[k]=v;}
  append(...nodes){this.children.push(...nodes);}
}
function dom(t){const original=globalThis.document;globalThis.document={createElement:tag=>new Node(tag),createDocumentFragment:()=>new Node('fragment')};t.after(()=>{if(original===undefined)delete globalThis.document;else globalThis.document=original;});}
const all=n=>[n,...(n.children||[]).filter(x=>typeof x==='object').flatMap(all)];
test('all coverage sections follow the Aphasia order and preserve interactive chapter content',t=>{
 dom(t);const candidates=new Node('form'),panel=new Node('details');candidates.onchange=()=>42;
 const page=coveragePage({meta:'Test collection',tiles:[],diagram:new Node('svg'),afterDiagram:panel,candidates:[candidates]});
 assert.deepEqual(all(page).filter(n=>['h1','h2'].includes(n.tag)).map(n=>n.textContent),[
 'Coverage','Flow of papers (PRISMA 2020)','Why candidates were excluded','Who decided','Coverage of the evidence gaps','Database searches','Candidates']);
 assert.ok(all(page).includes(candidates));assert.ok(all(page).includes(panel));assert.equal(candidates.onchange(),42);
 assert.equal(all(page).filter(n=>n.attrs?.id==='database-searches').length,1);
});
test('unreported counts stay blank while a known zero remains zero',t=>{
 dom(t);const tiles=summaryTiles([{value:null,label:'screened'},{value:0,label:'included'}]);
 assert.deepEqual(all(tiles).filter(n=>n.attrs?.class==='value').map(n=>n.textContent),['\u00a0','0']);
});
