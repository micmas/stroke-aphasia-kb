// Queue selection is a convenience for reviewers, never an approval decision.
export function selectDrafts(drafts, { query = '', filter = 'all', page = 0, pageSize = 25 } = {}) {
  const q = query.trim().toLowerCase();
  const matches = drafts.filter(d => {
    if (filter === 'target' && !d.findings.some(f => f.target_audit?.status === 'needs_source_review')) return false;
    if (filter === 'measurement' && !d.findings.some(f => f.outcome_measurement?.status !== 'identified')) return false;
    if (filter === 'high' && !d.findings.some(f => f.confidence === 'high')) return false;
    if (!q) return true;
    const text = [d.citation, d.entry, ...d.findings.flatMap(f => [f.target, f.claim, ...(f.outcome_measurement?.instruments || []).map(x => x.name)])].join(' ').replace(/_/g, ' ').toLowerCase();
    return q.split(/\s+/).every(word => text.includes(word));
  });
  const pages = Math.max(1, Math.ceil(matches.length / pageSize));
  const current = Math.min(Math.max(0, page), pages - 1);
  return { items: matches.slice(current * pageSize, (current + 1) * pageSize), total: matches.length, pages, page: current };
}

export function measurementLabel(f) {
  const m = f.outcome_measurement;
  const names = (m?.instruments || []).map(x => [x.name, x.subtest].filter(Boolean).join(' — '));
  return names.length ? names.join('; ') : 'Not yet verified — check the paper';
}
