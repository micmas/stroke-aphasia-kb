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
