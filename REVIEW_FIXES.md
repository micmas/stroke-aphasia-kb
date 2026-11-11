# Review fixes — 11 November 2026

Work is isolated on `codex/review-fixes`, based on d190282. Codex handled the extraction, review, benchmark and loader changes; Claude, in the existing desktop chat, implemented the portal changes in a separate clone. Claude's commits are reviewed and integrated here. No draft or canonical finding content, governance rules, deployed services or model choices have been changed. The original checkout and its running extraction were left alone.

## Changes by finding

| Review finding | Change |
|---|---|
| 1 | Default loader excludes approved-labelled entries that are still in drafts. |
| 2 | Model output filenames are restricted to safe Markdown basenames and active buckets; canonical paths are contained too. |
| 3 | Independence compares real extraction/refocus provenance tags; missing or unknown identity fails closed. |
| 4 | Promotion recomputes tier, rejects absent quotes and unresolved marks, and requires a current content-bound independent model report for model approval. Empty entries cannot be promoted. |
| 5–6 | Numeric separators survive normalization; every elision fragment must appear in order; anchored matching considers the whole quote; any absent quote blocks approval. Missing PDFs defer when required. |
| 7 | Upload identifiers and destination filenames are checked against the register and contained in papers/. |
| 8 | Manuscript-only permissions default to private; public copies require a human confirmation bound to both source and annotated PDF hashes. Explorer links follow the public manifest. |
| 9–10 | Failed PDF deletions remain queued; public serving checks an allowlist and uses no-store. Portal verdicts bind to reviewed content, finding IDs and open marks; stale decisions remain opinions. Saved browser decisions reset on a version change, retaining old notes; mixed or stale export/build assets cannot authorize a verdict. |
| 11 | Extraction refuses existing files, normalisation and rewrite paths protect human work, refocus creates drafts without inherited approval stamps. Rereview now blocks on collisions instead of dropping old findings. |
| 12 | All v2 versions reach the v2 validator; malformed entry containers fail clearly. |
| 13–14 | All six buckets are scored; empty, ungraded and incomplete paired evaluations are ineligible. Publication requires the versioned paper manifest and all previously published papers. |
| 15 | Review selection uses only active buckets; new reports are scoped by bucket. Old flat sidecars remain historical and cannot authorize new model approvals. |
| 16 | Recheck restores originals after extraction or audit exceptions, including interruption. |
| 17 | Extraction validates all output YAML before writing, supplies draft status, rejects empty output and strips approval metadata. |
| 18 | Duplicate local mark IDs receive stable paper-wide identities during refocus; unresolved marks block promotion. |
| 19 | Automatic extraction commits refuse pre-existing edits in managed paths. Portal Python and Node checks run before push; requested_by is passed as data rather than interpolated shell code. |
| 20 | Approval writes use a serialized, recoverable journal, with idempotent audit and duplicate-promotion protection. Portal record IDs, explicit outcomes and a ledger protect retries; promotion journals identify completed approvals after a crash. |
| 21 | Repetition detection raises the intended recoverable exception. Continuous streams observe an elapsed-time deadline. Paper prompts require loopback transport and reject cloud tags. |
| 22 | Pytest collects and runs the suite; CI uses it, including the new regression tests. |
| 23 | New review reports use timezone-aware UTC and logical source-directory descriptions. Historical timestamps and logs were not rewritten. |
| 24 | The redundant tracked snapshot is removed from this branch and future snapshots ignored. History is unchanged. |

## Measured effects on unchanged data

- Approved findings: **219 → 210**, and exported entries **59 → 56**. Excluded draft-only findings: Robson2014 (4), Leff2009 (4), Goldenberg1994 (1). They remain in their original files for proper review/promotion.
- Loader issues: **26 → 53**, because v2.8 now receives its intended checks and approved-in-drafts is reported. The complete list is in [review-validation-issues.txt](docs/review-validation-issues.txt). Existing ingredient approval metadata is missing; draft issues include methods outside the vocabulary, missing lesion mapping, responder claims without a therapy, and missing assessment fields. No scientific corrections were guessed.
- Public PDF links: **70 → 62** before any explicit copy confirmation. Eight manuscript-only papers become private on the next sync. Nothing has been deployed or removed from remote storage during this work.

## Verification

Final combined validation:

- `python -m pytest tests -q`: **116 passed** (five dependency deprecation warnings).
- `node --test portal/functions/test/*.test.mjs`: **28 passed**.
- `npm test`: **12 passed**, both against checked-in fixtures and freshly regenerated exports.
- Offline portal assembly from an isolated archive with regenerated approved and draft exports: **371 bound drafts**, **62 allowed public PDF filenames**. Export hashes and review-binding hashes agree. The clean archive lacks installed pdf.js assets; its build reports that dependency, so this is an assembly/binding check rather than a live PDF-pane test.
- `git diff --check`: clean. No changes under draft/canonical buckets, citations, screening data, model configuration or GOVERNANCE.

Tests use synthetic PDFs, temporary files and fake services. Export comparison uses unchanged d190282 data; no source paper was downloaded, no real model was called, and no production service was modified.

## Remaining checks and decisions

- Re-grade actual paper PDFs before deployment to measure stricter matching on columns, OCR, tables and ligatures. Synthetic adversarial tests cannot establish real-corpus false-positive/negative rates. The existing benchmark must be rerun before making new model recommendations.
- Have a person resolve the surfaced scientific/schema issues. Correcting Stockbridge's relationship, expanding vocabulary, changing screening eligibility or establishing reviewer-model performance needs source-based review, not automatic rewriting.
- Existing inbox verdicts without a content fingerprint become stale opinions and must be sent again after review. Saved browser reviews also restart when their content version is unknown or changed. Stale/blocked outcomes are currently visible in import output and audit records, not as a dedicated portal notification.
- Confirm the actual files for manuscript-only public copies. Run PDF sync and regenerate exports before building/deploying the portal; existing deployed copies do not change merely because this branch exists.
- Keep absent-quote overrides disabled under current governance. Adding an exception requires a policy decision; none is introduced here.
- Portal applies retain the current direct-push workflow with checks before push. Moving normal applies to protected pull requests, reviewing live Access/token/branch settings and deciding who may write records remain maintainer decisions. They cannot be verified offline.
- Recovery journals address interrupted promotion. Recheck backups restore ordinary exceptions; a hard process kill still requires inspecting backups. Other writers must not modify the same draft concurrently. The extraction command's clean-state guard does not identify edits made by another process after it starts.
- Historical naive timestamps remain ambiguous unless their source timezone is independently known. No offset was invented. The removed archive remains in Git history.
- Governance's richer per-field review-response contract still exceeds the present boolean-check response format; changing that format and evaluating the reviewer is a separate substantive change. The papers-directory configuration remains distributed. Neither was silently presented as fixed.

## Using the branch

Review the commit series and this report before merging. Install `requirements-ci.txt`, then run `python -m pytest tests -q`, `npm test`, and `node --test portal/functions/test/*.test.mjs`. `tests/review_reproductions.py` preserves historical defective behavior at d190282 and is deliberately outside normal test discovery; it is not the regression suite.

New review sidecars live in `logs/auto_review/<bucket>/<stem>.yaml`. A draft changed since review needs a fresh model review. Retrying an interrupted approval recovers pending journals in `logs/promotion_transactions/`; unexpected draft/canonical changes stop recovery for manual reconciliation rather than overwriting them. Completed journal metadata remains as audit evidence.
