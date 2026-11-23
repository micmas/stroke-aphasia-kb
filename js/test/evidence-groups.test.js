import test from 'node:test';
import assert from 'node:assert/strict';
import {anatomicalGroup, clinicalGroup, groupedMatrix} from '../../explorer/evidence-groups.js';
test('specific clinical measures share broad domains without merging composites',()=>{
 assert.equal(clinicalGroup('naming_accuracy')[0],clinicalGroup('bnt_performance')[0]);
 assert.equal(clinicalGroup('sentence_comprehension')[0],clinicalGroup('auditory_comprehension')[0]);
 assert.notEqual(clinicalGroup('sentence_comprehension')[1],clinicalGroup('auditory_comprehension')[1]);
 assert.equal(clinicalGroup('naming_and_comprehension_accuracy')[0],'Combined domains / composite outcomes');
 assert.equal(clinicalGroup('unrecognised_new_measure')[0],'Clinical domain awaiting classification');
});
test('paper clusters stay compound and unknown anatomy is not guessed',()=>{
 assert.equal(anatomicalGroup({citation:'@Basilakos2015'},'aphasia_aos_production_cluster')[0],'Multi-region anatomy');
 assert.equal(anatomicalGroup({citation:'@Casilio2025'},'aprocsa_dimension_overlap')[0],'Cross-region map comparisons');
 assert.equal(anatomicalGroup({},'left_ifg_triangular_part')[1],anatomicalGroup({},'left_ifg_pars_triangularis')[1]);
 assert.equal(anatomicalGroup({},'cluster_1')[0],'Anatomy awaiting classification');
});
test('one finding per cell and identical cell membership at both levels',()=>{
 const findings=['naming_accuracy','bnt_performance','sentence_comprehension'].map((col,i)=>({key:`f${i}`,pair:{kind:'region-impairment',row:'left_ifg_pars_triangularis',col}}));
 const index={findings,name:x=>x};
 for(const level of ['broad','specific']) {
  const m=groupedMatrix(index,'region-impairment',level);
  assert.equal(m.total,3);assert.equal([...m.cells.values()].flat().length,3);
  assert.deepEqual(new Set([...m.cells.values()].flat().map(f=>f.key)),new Set(['f0','f1','f2']));
 }
});
