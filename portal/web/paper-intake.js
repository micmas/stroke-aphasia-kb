// Shared, deterministic identity matching. Never merge conflicting DOIs by title.
export const normalizeDoi = (s) => String(s || '').trim().toLowerCase().replace(/^https?:\/\/(?:dx\.)?doi\.org\//, '').replace(/^doi:\s*/, '').replace(/[.,;]+$/, '');
export const normalizeTitle = (s) => String(s || '').normalize('NFKC').toLowerCase().replace(/[^\p{L}\p{N}]+/gu, ' ').trim();
export function matchPapers(paper, candidates) {
  const doi = normalizeDoi(paper.doi), title = normalizeTitle(paper.title);
  const eligible = candidates.filter((c) => !c.duplicate_of);
  const exact = doi ? eligible.filter((c) => normalizeDoi(c.doi) === doi) : [];
  if (exact.length) return exact;
  return title ? eligible.filter((c) => normalizeTitle(c.title) === title && !(doi && c.doi && normalizeDoi(c.doi) !== doi)) : [];
}
export function prioritizePapers(candidates, uploads) {
  const stamp = (c) => uploads.filter((u) => [c.id, c.key, ...(c.upload_ids || [])].filter(Boolean).map(String).some((id) => id.replace(/^@/, '') === String(u.id).replace(/^@/, ''))).reduce((s, u) => String(u.uploaded || '') > s ? String(u.uploaded) : s, String(c.pdf_uploaded_at || ''));
  return [...candidates].sort((a, b) => stamp(b).localeCompare(stamp(a)));
}
// Uploads must not move the title/abstract card a reviewer is working through.
export function orderScreeningPapers(candidates, uploads, stage) {
  return stage === 'ta' ? [...candidates] : prioritizePapers(candidates, uploads);
}
// A deployment date is not evidence that a submitted decision was applied.
export function pendingScreenReceipts(sent, register) {
  return Object.fromEntries(Object.entries(sent).filter(([id, receipt]) => {
    const candidate = register.find((c) => c.id === id || (c.upload_ids || []).includes(id));
    if (!candidate) return true;
    if (receipt?.record) return !(candidate.history || []).some((h) => h.record === receipt.record);
    // Older receipts have no record ID: only a confirmed stage transition can retire them.
    return !receipt?.stage || ['awaiting_' + receipt.stage, 'unsure_' + receipt.stage].includes(candidate.stage);
  }));
}
export function mergePendingPapers(candidates, uploads, register = candidates) {
  const out = [...candidates];
  for (const u of uploads) {
    if (!u.candidate) continue;
    const found = out.find((c) => c.id === u.id || (c.upload_ids || []).includes(u.id));
    const current = register.find((c) => c.id === u.id || (c.upload_ids || []).includes(u.id));
    const pending = current || u.candidate;
    if (!found && ['awaiting_ta', 'unsure_ta', 'awaiting_ft', 'unsure_ft'].includes(pending.stage)) out.push(pending);
  }
  return out;
}
