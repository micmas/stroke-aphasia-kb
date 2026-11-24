// Coverage describes curated anatomical links, not verified scan-feature equivalence.
export function mappingStatus(index, entry) {
  const mapping = index.mapping.regions[entry.id];
  if (mapping) return {
    status: mapping.review ? 'approximation' : 'mapped',
    reason: mapping.basis || 'Curated anatomical mapping.',
  };
  const knownGap = index.unmappedReason(entry.id);
  if (knownGap) return {status: 'atlas_gap', reason: knownGap};
  return {status: 'pending', reason: entry.kind === 'network'
    ? 'Mapping not yet assessed: verify the study-defined cluster or network, its extent and hemisphere before choosing an atlas region.'
    : 'Mapping not yet assessed: verify the anatomical definition, hemisphere and source atlas. A similar name alone is insufficient.'};
}

export function atlasCoverage(index) {
  const rows = Object.values(index.entries).filter(e => e.bucket === 'regions')
    .map(entry => ({entry, ...mappingStatus(index, entry)}));
  const counts = {mapped: 0, approximation: 0, atlas_gap: 0, pending: 0};
  for (const row of rows) counts[row.status]++;
  return {rows, counts, total: rows.length};
}
