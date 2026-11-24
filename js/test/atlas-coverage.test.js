import test from 'node:test';
import assert from 'node:assert/strict';
import {atlasCoverage, mappingStatus} from '../../explorer/atlas-coverage.js';

test('coverage distinguishes anatomical links, approximations, known gaps and unassessed entries', () => {
  const entries = Object.fromEntries(['named', 'approx', 'gap', 'new_cluster'].map(id => [id, {id, bucket:'regions', kind:'network'}]));
  entries.age = {id:'age', bucket:'personal_factors'};
  const index = {entries, mapping:{regions:{named:{}, approx:{review:true}}}, unmappedReason:id => id === 'gap' ? 'No corresponding atlas label.' : null};
  const audit = atlasCoverage(index);
  assert.equal(audit.total,4);
  assert.deepEqual(audit.counts,{mapped:1,approximation:1,atlas_gap:1,pending:1});
  assert.match(mappingStatus(index,entries.new_cluster).reason,/not yet assessed/);
  assert.equal(mappingStatus(index,entries.gap).reason,'No corresponding atlas label.');
  assert.equal(index.mapping.regions.new_cluster,undefined);
});
