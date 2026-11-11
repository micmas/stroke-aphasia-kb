// What a review in progress (kept in this browser) and the files this page loaded are bound to.
// Pure functions, so they can be tested without a browser (portal/functions/test/review-state.test.mjs).

/** An empty review of the draft version `digest`. */
export const freshReview = (digest) => ({ verdict: '', rationale: '', findings: {}, marks: [], comments: {}, digest: digest || null });

const touched = (x) => Boolean(x && (x.verdict || x.rationale || Object.keys(x.findings || {}).length || (x.marks || []).length));

/**
 * The saved review state for a draft whose current version is `digest`. Decisions belong to the
 * version they were made on: if the draft changed since (or the state predates the binding and
 * holds decisions), they are not carried over. The earlier state is kept as `previous`, for
 * reference only, and the review starts afresh. Returns {review, setAside}.
 */
export function carryOver(saved, digest, now = new Date()) {
  if (!digest) return { review: saved || freshReview(null), setAside: false };   // not reviewable: nothing is sent anyway
  if (!saved) return { review: freshReview(digest), setAside: false };
  if (saved.digest === digest) return { review: saved, setAside: false };
  if (!touched(saved)) return { review: { ...saved, digest }, setAside: false };
  const { previous: _older, ...earlier } = saved;
  return { review: { ...freshReview(digest), previous: { ...earlier, digest: saved.digest || null, set_aside: now.toISOString() } }, setAside: true };
}

/**
 * The manifest, the drafts export and drafts.json come from one build, and the export on screen is
 * the very file the bindings were computed for (same build id, same content digest, same bytes).
 * Anything else, and verdicts are not sent.
 */
export function sameBuild(manifest, bindings, kb, kbSha256) {
  return Boolean(manifest && bindings && kb && kbSha256
    && manifest.buildId && bindings.buildId === manifest.buildId
    && bindings.exportDigest && bindings.exportDigest === kb.version?.contentDigest && manifest.exportDigest === bindings.exportDigest
    && bindings.exportSha256 && bindings.exportSha256 === kbSha256 && manifest.exportSha256 === kbSha256);
}
