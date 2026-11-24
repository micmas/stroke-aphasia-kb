import test from 'node:test';
import assert from 'node:assert/strict';
import {buildIndex, matches} from '../../explorer/kb-index.js';
import {topicCategory, ANATOMY, FACTORS} from '../../explorer/topic-categories.js';
test('injury measures leave anatomical matrices without altering saved evidence or IDs',()=>{
 const kb={entries:{lesion_size:{id:'lesion_size',bucket:'regions',kind:'classical'}},findings:[{id:'f1',source_id:'lesion_size',source_kind:'region',target:'naming',target_kind:'impairment',citation:'@Example2020'}]};
 const original=structuredClone(kb); const i=buildIndex(kb), f=i.findings[0];
 assert.equal(f.category,FACTORS);assert.equal(f.subcategory,'Lesion and imaging measures');assert.equal(f.pair.kind,'predictor-outcome');assert.equal(i.kindOf('lesion_size'),'predictor');assert.equal(f.recorded_source_kind,'region');assert.deepEqual(kb,original);
 assert.equal(matches(f,{category:[FACTORS]}),true);
});
test('age, initial severity and volume share a parent with distinct subcategories',()=>{
 assert.equal(topicCategory('age',{},'predictor').subcategory,'Personal characteristics');
 assert.equal(topicCategory('initial_severity',{},'region').subcategory,'Clinical characteristics');
 assert.equal(topicCategory('total_lesion_volume',{},'region').subcategory,'Lesion and imaging measures');
});
test('bottlenecks stay shared white-matter concepts and uncertain clusters are not guessed',()=>{
 assert.deepEqual(topicCategory('posterior_bottleneck_cluster',{},'region'),{category:ANATOMY,subcategory:'White-matter regions and pathways'});
 assert.equal(topicCategory('brocas_area',{},'region').subcategory,'Grey-matter regions');
 assert.equal(topicCategory('frontoparietal_roi',{},'region').subcategory,'Mixed or distributed regions');
 assert.equal(topicCategory('unknown_cluster',{},'region').subcategory,'Anatomical definition to check');
});
