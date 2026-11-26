// Queue selection is a convenience for reviewers, never an approval decision.
export function selectDrafts(drafts, { query = '', filter = 'all', page = 0, pageSize = 25, paper = '', citations = {} } = {}) {
  const q = query.trim().toLowerCase();
  const matches = drafts.filter(d => {
    if (paper && d.citation !== paper) return false;
    if (filter === 'target' && !d.findings.some(f => f.target_audit?.status === 'needs_source_review')) return false;
    if (filter === 'measurement' && !d.findings.some(f => f.outcome_measurement?.status !== 'identified')) return false;
    if (filter === 'high' && !d.findings.some(f => f.confidence === 'high')) return false;
    if (!q) return true;
    const text = [d.citation, citations[d.citation], d.entry, ...d.findings.flatMap(f => [f.target, f.claim, ...(f.outcome_measurement?.instruments || []).map(x => x.name)])].join(' ').replace(/_/g, ' ').toLowerCase();
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

/** Exact draft/version receipts, never truncated filenames or approval status. */
export function reviewProgress(draft, binding, receipts = []) {
  const ids = new Set(draft.findings.map(f => f.id));
  const decided = new Set(); const by = new Set();
  if (!binding?.digest) return { complete: false, decided: 0, total: ids.size, by: [] };
  const rows = [...receipts.filter(r => r.id === draft.path && r.draft_digest === binding.digest),
    ...(binding.reviews || []).filter(r => !r.stale && r.reviewed_digest === binding.digest).map(r => ({ per_finding: r.findings, by: r.by }))];
  for (const r of rows) {
    let useful = false;
    for (const f of r.per_finding || []) if (ids.has(f.id) && ['agree', 'disagree', 'unsure'].includes(f.verdict)) { decided.add(f.id); useful = true; }
    if (useful) by.add(r.by || r.reviewer_name || r.reviewer || 'a reviewer');
  }
  return { complete: ids.size > 0 && decided.size === ids.size, decided: decided.size, total: ids.size, by: [...by] };
}

export function pendingFirst(drafts, complete) {
  return [...drafts.filter(d => !complete(d)), ...drafts.filter(complete)];
}

export function nextPaperDraft(drafts, current, complete) {
  const paper = drafts.filter(d => d.citation === current.citation);
  const at = paper.findIndex(d => d.path === current.path);
  return [...paper.slice(at + 1), ...paper.slice(0, Math.max(0, at))].find(d => d.path !== current.path && !complete(d)) || null;
}
