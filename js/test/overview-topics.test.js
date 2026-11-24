import test from 'node:test';
import assert from 'node:assert/strict';
import {overviewTopics} from '../../explorer/overview-topics.js';
import {FACTORS} from '../../explorer/topic-categories.js';
test('age variants share one topic with an exact breakdown and no double-counting',()=>{
 const entries=Object.fromEntries(['age','age_under_55','age_and_education','age_of_acquisition'].map(id=>[id,{category:FACTORS,subcategory:'Personal characteristics',name:id==='age_of_acquisition'?'Imageability and age-of-acquisition prediction model':id}]));
 const index={entries,name:id=>id,findings:[{key:'a',source_id:'age',target:'age_under_55'},{key:'b',source_id:'age_and_education'},{key:'c',source_id:'age_of_acquisition'}]};
 const age=overviewTopics(index,FACTORS).find(t=>t.label==='Age');
 assert.equal(age.n,2);assert.equal(age.entries.length,3);assert.deepEqual([...age.keys],['a','b']);
 assert.ok(!age.entries.some(e=>e.id==='age_of_acquisition'));
});

test('therapy variants share topics while retaining safety and dose entries',()=>{
 const ids=['semantic_feature_analysis','sfa_treatment','sfa_treatment_discourse_efficiency','a_tdcs_safety','adjunctive_a_tdcs_speech_therapy','high_intensity_aphasia_therapy','low_intensity_slt_followup','control_treatment_aphasia','thrombolysis'];
 const index={entries:Object.fromEntries(ids.map(id=>[id,{category:'Therapies',name:id}])),name:id=>id,
 findings:ids.map((id,i)=>({key:String(i),source_id:id,target:i===0?'sfa_treatment':'naming'}))};
 const topics=overviewTopics(index,'Therapies');
 const sfa=topics.find(t=>t.label==='Semantic Feature Analysis');assert.equal(sfa.n,3);assert.equal(sfa.entries.length,3);
 const stimulation=topics.find(t=>t.label==='Brain stimulation (tDCS)');assert.equal(stimulation.entries.length,2);assert.ok(stimulation.entries.some(e=>e.id==='a_tdcs_safety'));
 assert.equal(topics.find(t=>t.label==='Speech and language therapy intensity').n,2);
 assert.equal(topics.find(t=>t.label==='Treatment comparisons and control conditions').n,1);
 assert.equal(topics.find(t=>t.label==='Acute stroke treatment').n,1);
 assert.equal(topics.reduce((n,t)=>n+t.n,0),ids.length);
});
