import test from 'node:test';
import assert from 'node:assert/strict';
import { clinicalContext } from '../../explorer/clinical-context.js';
import { buildIndex } from '../../explorer/kb-index.js';
const base = {source_id:'feature',id:'f1',source_path:'drafts/a.md',source_kind:'region',method:'LSM',direction:'likely',flags:['core_profile_machine_prepared','not_transcribed:region_definition'],claim:'An association.',notes:'Exposure measurement: lesion load in a study-defined region. Additional metadata has not been transcribed;',source_check:{analysis_identity:{exposure:{text:'lesion load'},outcome:{text:'naming'}}}};
test('region matching is conditional, preserves original evidence, and flags missing metadata',()=>{
 const original=structuredClone(base); const c=clinicalContext(base);
 assert.equal(c.match_status,'requires_feature_verification');assert.match(c.applies_to,/another atlas/);assert.match(c.review_notes.join(' '),/exact scan-feature match has not been verified/);assert.deepEqual(base,original);
});
test('non-imaging age cannot become an anatomical match because of a bad entry kind',()=>{
 const c=clinicalContext({...base,method:'meta-analysis',source_check:{analysis_identity:{exposure:{text:'age <55 years'},outcome:{text:'naming recovery'}}}});
 assert.equal(c.match_status,'no_direct_imaging_match');assert.equal(c.review_notes.length,0);assert.match(c.relevance,/do not by themselves establish effects of treatment timing/);
});
test('nulls are not individual reassurance or proof of equivalence',()=>{
 const c=clinicalContext({...base,direction:'no_effect'});assert.match(c.relevance,/rather than reassurance/);assert.match(c.limits,/not proof of equivalence/);
});
test('template overlap is not patient diffusion, and graph metrics are not tract overlap',()=>{
 assert.equal(clinicalContext({...base,notes:'Exposure measurement: lesion overlap with a reference tract template.'}).category,'Lesion overlap with a reference network');
 assert.equal(clinicalContext({...base,notes:'Exposure measurement: global efficiency from a structural connectome.',method:'tractography'}).category,'Network graph measure');
});
test('task materials remain non-anatomical and PCA constructs keep limits',()=>{
 const c=clinicalContext({...base,method:'behavioral_only',claim:'PCA results.',source_check:{analysis_identity:{exposure:{text:'word imageability'},outcome:{text:'naming'}}}});
 assert.equal(c.category,'Assessment or task factor');assert.match(c.limits,/not automatically interchangeable/);
});
test('unrelated old findings receive no automatic interpretation',()=>assert.equal(clinicalContext({...base,flags:[]}),null));
test('different source files with the same entity/finding IDs retain separate permalinks',()=>{
 const i=buildIndex({findings:[base,{...base,source_path:'drafts/b.md',claim:'Another result'}]});
 assert.equal(i.byKey.get('drafts/a.md/f1').claim,'An association.');assert.equal(i.byKey.get('drafts/b.md/f1').claim,'Another result');assert.equal(i.byKey.has('feature/f1'),false);
});

test('a graph covariate does not turn a lesion-volume result into a network finding',()=>{
 const c=clinicalContext({...base,source_check:{analysis_identity:{exposure:{text:'overall lesion volume'},outcome:{text:'Token Test'}}},notes:'Exposure measurement: Total lesion volume. Regression also included graph theory metrics.'});
 assert.equal(c.category,'Lesion volume');
});

test('personal factors have their own display category without changing the source record',()=>{
 const f={...base,method:'meta-analysis',source_check:{analysis_identity:{exposure:{text:'age <55 years'},outcome:{text:'naming recovery'}}}};
 const kb={entries:{feature:{id:'feature',name:'Age',bucket:'regions'}},findings:[f]};
 const i=buildIndex(kb);assert.equal(i.findings[0].source_kind,'personal_factor');assert.equal(i.kindOf('feature'),'personal_factor');assert.equal(i.findings[0].pair.kind,'predictor-outcome');assert.equal(kb.entries.feature.bucket,'regions');assert.equal(kb.findings[0].source_kind,'region');
 assert.ok(!i.findings[0].presentation.limits.includes('A study finding is not'));
});
