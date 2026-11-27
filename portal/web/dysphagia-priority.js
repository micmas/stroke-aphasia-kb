// Ordering only: a method mention is not an eligibility decision.
export function instrumentalLabels(record) {
  const text = `${record.title || ''}\n${record.abstract || ''}`.normalize('NFKC');
  const labels = [];
  // Keep FEES case-sensitive: ordinary service/consultation fees are not the test.
  if (/\bFEES(?:ST)?\b/.test(text) || /\b(?:fibre?optic|fiberoptic|flexible)?\s*endoscopic\s+(?:evaluation|assessment)\s+of\s+swallowing\b/i.test(text)) labels.push('FEES');
  if (/\bVFSS\b|\bvideo[\s-]*fluoro\w*|\bmodified\s+barium\s+swallow\b/i.test(text)) labels.push('VFSS');
  return labels;
}

export function prioritiseInstrumentalStudies(records) {
  const priority = [], other = [];
  for (const record of records) (instrumentalLabels(record).length ? priority : other).push(record);
  return [...priority, ...other];
}
