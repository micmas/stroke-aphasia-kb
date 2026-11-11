# Independent review: stroke-aphasia-kb

Fix status and validation are recorded separately in [REVIEW_FIXES.md](REVIEW_FIXES.md). The findings below describe the original revision.

Reviewed 11 November 2026 (Australia/Brisbane), revision `d19028241b65902892542f0a690030b5c30e4c91`.

**The main risk is that approval is a convention shared by several scripts, rather than an enforced boundary.** The default loader can export an approved-labelled draft; the extractor can write outside drafts; the same extraction model can satisfy the independence check; direct promotion trusts a caller-supplied tier. Fixing only the portal would leave these other routes open.

## Scope and evidence

Read README, GOVERNANCE, schema, MODELS and PORTAL first, then traced ingestion/extraction, deterministic and model review, promotion, portal upload/record/import, publication and exports. Findings below refer to the starting revision, not concurrent edits. A separate `recheck_drafts.py --papers Stockbridge2024 Yu2023 --execute --retry` process began changing the working checkout during review. I left it alone and continued against a `git archive` snapshot in `/tmp/stroke-kb-review-snapshot`.

No source PDFs, benchmark sandboxes, real Ollama calls, Cloudflare, R2 or GitHub services were used. Dependency installation was the only intentional external access. Tests use temporary fixtures/fake services. Runtime Access policies, deployed routes, token permissions, branch rules and actual paper versions remain unverified. “Verified” means reproduced locally or traced through the checked-in code, not that exploitation or a bad scientific conclusion has occurred in production.

Validation:

- `npm test`: **12 passed**.
- `node --test portal/functions/test/*.test.mjs`: **21 passed**.
- Requested `python -m pytest tests -q`: **collection aborts**, `SystemExit: 0` at `tests/test_review_guardrails.py:257`. The default system Python also lacks pytest; installed requirements plus pytest into a temporary Python 3.12 environment.
- Running all **12 existing Python test files individually**, as `.github/workflows/test.yml` does: **all exited 0**.
- `python scripts/export_webapp.py --out /tmp/kb-review.json --fixtures /tmp --indent 1`: completed, **219 findings, 59 entries, 212 citations**. The reported KB commit `540cd86` is the last commit affecting export inputs, not an accidental use of the sibling CALMaR copy (`export_webapp.py:259–270`).
- Added `tests/review_reproductions.py`: **19 passed** against the archived revision. These deliberately assert the observed defective behavior; they are evidence, **not desired-behavior regression tests**. Convert/invert them when fixing. They are explicitly invoked and do not match CI's `test_*.py` glob:

  ```sh
  python -m pytest tests/review_reproductions.py -q
  # 19 passed
  ```

No production fixes, commits, pushes, history rewrites or edits to scientific findings were made by this review. Optional fix work is deferred: the approval and publication changes need coherent enforcement and compatibility tests, rather than piecemeal policy changes.

## Findings — high severity

### 1. An approved-labelled draft enters the default approved export

**High · Exports and explorer · verified (reproduced).**

**References:** `scripts/aphasia_kb.py:697–740`; `scripts/extract.py:676–760`, `966–985`; `scripts/export_webapp.py:534`.

The loader reads `drafts/`, then admits entries using only `entry.get("status") in self.include`. Its comment says the caller must also have requested drafts, but that condition is absent. Extraction forces `created_by` and `created_on`, not `status`, reviewer fields or per-finding approval metadata.

**Evidence:** `test_approved_status_in_draft_enters_default_loader` writes a valid fixture only under `drafts/regions/`, with `status: approved` and an invented reviewer. `KnowledgeBase(tmp_path)` returns its finding without any canonical entry or promotion. Default export consumes that loader.

**Scenario:** a model emits an approved example it saw in context, or a local edit leaves an approval stamp in a draft. The next public export includes it without `promote.py` ever running.

**Fix:** enforce origin as well as status in the loader; ordinary approved loads must exclude every draft-origin file. At the extraction boundary, set status to draft and remove approval metadata supplied by the model. Test this through the actual export, including a mixed canonical/draft entry ID.

### 2. Model-supplied filenames can overwrite canonical entries or arbitrary local files

**High · security · verified (reproduced).**

**References:** `scripts/extract.py:966–989`; `scripts/refocus.py:195–200`.

`out = kb_root / "drafts" / bucket / fname` uses the model's filename without validating a basename or checking containment. `write_text()` overwrites an existing destination. Validating the bucket does not constrain `fname`; absolute names also discard preceding path components.

**Evidence:** `test_model_filename_escapes_drafts_and_overwrites` supplies `../../regions/example.md` and overwrites a temporary canonical file. The write happens before validation. The new-file branch of refocus has the same untrusted-name construction.

**Scenario:** malformed model output or instructions embedded in a paper produce a traversal filename. The extractor can modify canonical content, scripts or configuration with the maintainer's filesystem privileges. This also defeats the sandbox guarantee.

**Fix:** derive filenames from validated entry ID and citation key; reject absolute paths, separators and traversal; resolve and assert destination containment; never overwrite canonical content from extraction. Validate all outputs before any write.

### 3. Normal extraction provenance defeats model independence

**High · Checks and review · verified (reproduced).**

**References:** `scripts/extract.py:1150–1152`; `scripts/refocus.py:165`; `scripts/auto_review.py:679–693`, `812–817`; `scripts/promote.py:106–137`.

The extractor records `agent:ollama-extract-cli/<tag>`. Both independence implementations remove only `agent:` or `model:`. They compare `ollama-extract-cli/gemma4:31b` to `gemma4:31b`, and conclude they differ. Refocus has the analogous `ollama-refocus-cli/` prefix.

**Evidence:** `test_same_extractor_is_considered_independent` gets `True` from `reviewer_is_independent("agent:ollama-extract-cli/gemma4:31b", "gemma4:31b")`; promotion validation returns no problems too.

**Scenario:** setting review to the extraction tag, or choosing `--model` for a single review, silently permits self-review of otherwise Tier A material. The existing test uses `agent:gemma4:31b`, so misses the production format.

**Fix:** share one provenance parser for current and historical formats; fail closed on unrecognised formats; compare actual tags and inspect finding-level extraction provenance when a draft mixes extract/refocus runs. Do not let `--extractor` override known contradictory provenance.

### 4. Direct promotion treats “Tier A” as an unchecked assertion

**High · Checks and review · verified (reproduced and traced).**

**References:** `scripts/promote.py:117–138`, `205–290`; `scripts/auto_review.py:1203–1278`.

`validate_review_args` requires the string `A` for model review, but does not classify the draft, read a PDF, or require a successful independent review record. `cmd_approve` runs schema validation, not quote validation. A human can also directly promote a schema-valid fabricated quote. `--extractor` takes precedence over recorded `created_by`. Empty names such as `human:` pass normalisation.

**Evidence:** `test_supplied_tier_allows_new_therapy_without_pdf` creates a new therapy entry with no PDF and promotes it as `model:other --tier A`. This also demonstrates that an empty findings list validates. New therapies are unconditionally Tier B in policy. Separately, `test_manual_require_pdf_match_is_ignored` returns `auto_approve` even with `require_pdf_match=True` and no PDF: that argument is unused by `apply_manual_verdict`.

**Scenario:** a maintainer follows the documented direct model command, a wrapper supplies the wrong tier, or a worksheet runs on a machine without papers and expects `--require-pdf-match` to protect it. Approval appears legitimate although the required checks did not run.

**Fix:** centralise approval in one service that recomputes tier, verifies current content and review evidence, enforces quote policy, validates nonempty human identity, and cannot be bypassed by caller metadata. Portal humans may read the hosted PDF while Actions lacks local PDFs; support that explicitly with a content/PDF-bound attestation rather than silently ignoring the match option.

### 5. The quote matcher can certify fabricated text as found

**High · Checks and review · verified (reproduced).**

**References:** `scripts/quote_check.py:116–147`; `scripts/annotate_paper.py:116–144`.

Elision matching drops all fragments shorter than 20 characters, then checks whether the remaining fragments occur anywhere, without order or locality. Numeric hyphens are also removed by `\w`-based normalisation. `anchored` requires only the first 60 characters to match, irrespective of the rest.

**Evidence:** the reproductions show:

- `real sentence [...] cured everyone [...] another real sentence` → **elided** although “cured everyone” is fabricated;
- reversing the two real sentences → **elided**;
- quote `There were 12 participants.` against paper `There were 1–2 participants.` → **exact**.

**Scenario:** altered sample sizes or inserted short conclusions satisfy FOUND; an invented long suffix after a real opening is labelled “anchored”, avoiding the benchmark's absent disqualification. A second reader may catch this, but the deterministic integrity claim is false.

**Fix:** preserve numeric signs/ranges; require every nonempty elision fragment to match, in order within a justified window; downgrade unsupported fragments to unverified. Treat an anchor as a search hint, not evidence that the entire quote is real. Add negatives for negation, numbers and fabricated suffixes. Existing ligature expansion and line-break joining handle some typography; two-column reading order still needs representative PDF fixtures, unavailable here.

### 6. Up to 20% absent quotes do not fail manual approval checks

**High · Checks and review · verified (reproduced).**

**References:** `scripts/auto_review.py:145`, `340–404`, `1240–1253`.

The PDF check computes `(total - len(misses)) / total >= 0.80`. It is not an all-pass check. Missing citations are skipped, so a partial set of available papers can also produce a passing check.

**Evidence:** `test_one_absent_of_five_passes` returns `passed=True` with detail `absent 1`. Manual approval only hard-rejects when this boolean is false. The normal model classifier additionally checks the matched fraction and therefore blocks this particular 4/5 case; that does not protect manual or direct promotion.

**Scenario:** a reviewer approves a five-passage draft containing one fabricated quote. The purported non-overridable absent-quote check does not reject it.

**Fix:** any absent quote must fail. Track missing/unreadable papers explicitly and require a defined human-attestation path where local verification cannot run. Keep near/elided/table distinctions separate from hard failure counts.

### 7. Portal upload IDs escape the papers directory on import

**High · security · verified (reproduced destination, write path traced).**

**References:** `portal/functions/api/upload.js:53–60`, `83–86`; `scripts/portal_import.py:263–284`, `301–319`.

The upload endpoint accepts any nonempty ID. Slugging protects the R2 object name, but the original ID is retained in the record. Import accepts any ID beginning with `@` and constructs `PAPERS / (id_without_at + ".pdf")` without citation validation or containment.

**Evidence:** `test_pdf_upload_destination_escapes_papers` resolves `@../outside` to a file beside `papers/`. `apply_pdf` subsequently moves verified PDF bytes to that destination. `@/absolute/path` also produces an absolute destination.

**Scenario:** an Access-admitted uploader creates a PDF outside the intended directory when the maintainer fetches uploads. Existing destinations are not overwritten, and arbitrary Python execution is **not** established by this PDF-only primitive. With the real symlink, traversal is relative to the resolved OneDrive location, not necessarily the repository.

**Fix:** allow only known candidate IDs or registered citation keys; validate on both server and importer; resolve against the configured papers root and assert containment. Treat all inbox records as untrusted even if the endpoint already validates them.

### 8. A manuscript-only licence publishes whichever PDF happens to be present

**High · Review portal · verified (reproduced); actual wrong-version exposure unconfirmed.**

**References:** `scripts/licences.py:18–20`, `142–148`; `scripts/publish_portal.py:62`, `86–98`; `portal/papers.json`.

`cc_manuscript` explicitly means the accepted manuscript is reusable, not the publisher version. `PUBLIC_CATEGORIES` includes it, and `scan_pdfs` assigns any matching annotated PDF to `cc/` without verifying which version its bytes represent. The committed index contains **8** `cc_manuscript` papers.

**Evidence:** `test_manuscript_metadata_publishes_any_annotated_version` returns `public=True` based only on that category.

**Scenario:** the maintainer obtained the publisher PDF through institutional access, but metadata found a CC accepted manuscript elsewhere. The institutional copy is published openly.

**Fix:** record redistribution permission against the specific file hash and version; default manuscript-only metadata to private until the supplied copy is confirmed. Review the eight indexed objects on the maintainer's machine. This is a technical mismatch between recorded version and published file, not a legal conclusion about individual papers.

### 9. Failed public-PDF removal is forgotten permanently

**High · Review portal · verified (reproduced).**

**References:** `scripts/publish_portal.py:170–193`, `219–228`; `portal/lib/pdfs.js:12–20`.

`do_delete()` only prints failure. The sync still saves the new private location or removes the index entry, losing the old public object name. The serving function reads `cc/<name>` directly from R2; it does not consult the index.

**Evidence:** `test_failed_public_deletion_forgotten` simulates a failed deletion during CC → private migration. A second sync never retries the deletion: the fake delete receives exactly one call while the new index says private.

**Scenario:** a transient R2 failure during licence correction leaves a rights-reserved file publicly retrievable indefinitely, even after later successful syncs. Public cache headers also permit a day's cached availability after an otherwise successful change.

**Fix:** persist pending deletions and retry; count deletion failures in result/exit status; reconcile actual bucket inventory or enforce an authoritative public allowlist at serving time. Define cache invalidation for revoked public objects.

### 10. Portal approval is not tied to the draft that was reviewed

**High · Review portal · verified (reproduced and traced).**

**References:** `portal/functions/api/reviews.js:18–25`; `scripts/portal_import.py:191–224`; `scripts/auto_review.py:1235–1278`.

A verdict identifies only a path. There is no reviewed-content digest or revision check. `per_finding` may be empty or stale; the human approval path does not validate completeness, agreement or finding identity as the model path does. Edits have a field-level old-value check, but approvals do not.

**Evidence:** `test_stale_portal_verdict_has_no_content_binding` changes a draft and shows that a verdict with no per-finding answers is handed to promotion for the changed content.

**Scenario:** reviewer A opens the snapshot, reviewer B edits it or a re-extraction replaces it, and A's approval later applies to the new findings. Earlier records in one apply batch can cause the same race.

**Fix:** include a hash of the reviewed draft and PDF plus stable finding identities; compare at apply time; keep stale decisions as opinions requiring reconfirmation. Validate per-finding coverage and agreement. Do not use a filename as the identity of reviewed content.

### 11. Human work is not protected across all rewrite paths

**High · Extraction · verified (reproduced and traced).**

**References:** `scripts/extract.py:966–989`, `1282–1330`; `scripts/reextract.py:119–145`; `scripts/normalize_drafts.py:54–65`; `scripts/recheck_drafts.py:90–109`.

Direct `extract.py --pdf` unconditionally overwrites same-named drafts; only `--batch` skips already-extracted keys. `reextract.py` moves drafts and review sidecars away without checking human work. `normalize_drafts.py` rewrites reviewed drafts without an edit stamp or approval invalidation. Recheck's protection applies only in recheck, and parse failures return “not touched”.

**Evidence:** `test_save_overwrites_person_review_and_keeps_invalid_yaml` replaces a draft carrying `portal_reviews` and removes that review. Reextract's loop moves every matching draft and sidecar before calling the extractor; model failure does not restore them.

**Scenario:** rerunning one paper after a portal review discards current review context; a failed re-extraction leaves reviewed drafts absent from the portal. Backups/git may permit recovery, but work is no longer part of the active review and uncommitted work need not be in git.

**Fix:** one shared protection/precondition check for all writers; work in an isolated per-paper directory; diff and validate before replacement; preserve reviewer metadata and stable identities deliberately, or require a new review. Treat unparsable existing human documents as protected until inspected.

## Findings — medium severity

### 12. The main loader validates v2.4–v2.8 as v1

**Medium · Checks and review · verified (reproduced).**

**References:** `scripts/aphasia_kb.py:710–720`; `tests/test_schema_v28.py:39–44`.

The dispatch recognises only versions 2–2.3 for `_validate_v2_entry`; later versions fall into `_validate_v1_entry`. Unit tests call the newer validator directly and miss this wiring error.

**Evidence:** `test_loader_sends_v28_to_v1_validator` spies on both validators and observes only `v1` for a v2.8 fixture. Thus loader issue reports do not apply the advertised therapy and lesion-mapping requirements. Promotion calls the v2 validator directly, so this is not a claim that its version dispatch is broken too.

**Scenario:** a hand-edited or old canonical v2.8 entry violates the new contract but loader/export diagnostics do not report the right errors.

**Fix:** centralise version dispatch, test through `KnowledgeBase`, and distinguish validation diagnostics from enforcement. Also add explicit structural checks: empty findings currently pass; required `design` is only checked if truthy (`aphasia_kb.py:413`); malformed finding shapes can raise instead of returning validation issues.

### 13. Benchmark eligibility can reward empty output and omits two buckets

**Medium · Model benchmark · verified (reproduced and traced).**

**References:** `scripts/compare_extraction.py:55`, `62–91`, `145–191`; `scripts/benchmark_models.py:472–540`; `scripts/aphasia_kb.py:392`.

A candidate file with no findings is not `failed`; no passages means `ungraded=False`; zero quotes and zero issues can be eligible. Comparison discovery only visits regions, impairments, therapies and predictors, excluding reviews and ingredients. That also affects recheck, which reuses comparison helpers. Calibration uses mean strength only, although the metrics table also names confidence. Aggregate means can cancel a severe overclaim on one paper against underclaiming on another.

**Evidence:** `test_empty_extraction_can_be_eligible` returns eligible for zero findings/quotes. A fully valid empty entry satisfies the validator (finding 4). Four Hazelton impairment drafts have `findings: []` at lines 14 or 16. Schema failures in ignored review drafts cannot affect the benchmark score.

**Scenario:** an extractor emits nothing useful, or puts bad material into `reviews/`, and looks cleaner than a model that attempted the findings. “Eligible” overstates what was evaluated.

**Fix:** require nonempty graded findings for every requested paper, complete evaluation of all supported buckets, a usable paired incumbent baseline and explicit unknown states. Define calibration at paper level, including what confidence is meant to contribute. Make the benchmark configuration/ref hashes part of the result.

### 14. Publishing a subset replaces the full benchmark

**Medium · Model benchmark · verified (reproduced).**

**References:** `scripts/benchmark_models.py:680–712`, `907–908`.

`publish` builds only from the supplied rows/papers and unconditionally calls `path.write_text(...)`; it does not read the existing summary or check a required reference set.

**Evidence:** `test_publish_replaces_previous_papers` seeds an Old-paper summary, publishes New, and reads only New back.

**Scenario:** a one-paper rerun silently deletes all other published results and changes model-level eligibility to reflect the subset.

**Fix:** preferably refuse incomplete publication against an explicit versioned benchmark manifest. Alternatively merge by model × paper only when reference hash, prompt/schema/scorer version, model digest and configuration match, then recompute summaries. Blind merging mixes incomparable runs. Use atomic replacement.

### 15. Backup drafts are reviewed as active drafts and share sidecars

**Medium · Checks and review · verified (reproduced).**

**References:** `scripts/auto_review.py:998–1001`, `1451–1483`.

`DRAFTS_DIR.rglob("*.md")` includes `_backup`. Reports use only `draft_path.stem`, so a backup and live draft share the same sidecar.

**Evidence:** `test_backup_is_selected` returns a `_backup/stamp/regions/x.md` file under `--all`. Its report path is the same as a live `x.md`.

**Scenario:** stale YAML causes noisy failures and inflates counts; more seriously, a backup run overwrites `latest_verdict` for the current draft and influences deferred/provisional selection.

**Fix:** enumerate the six supported active bucket directories, reject backup paths even when explicitly selected for approval, and make report identity include draft identity/content revision.

### 16. Recheck's rollback does not cover ordinary exceptions

**Medium · Extraction · verified (code trace).**

**References:** `scripts/recheck_drafts.py:178–219`.

After backup and deletion, the `try` catches only `KeyboardInterrupt`. The new audit is outside that protected block. An `OSError`, subprocess launch error or malformed replacement that crashes audit escapes without restoring old drafts. The backup exists, but automatic recovery does not occur.

**Evidence:** the sole exception handler at line 201 is `except KeyboardInterrupt: restore(); raise`; `new = audit(...)` is at line 211, outside it.

**Scenario:** disk/model-output failure midway through a night run leaves the active queue partially empty or replaced, contrary to the stop-and-resume assurance.

**Fix:** stage outputs without deleting active drafts, validate first, then atomically switch; on all unsuccessful paths restore/retain the old set. Keep an explicit operation journal so a killed process can recover on the next run.

### 17. Invalid YAML and missing file defaults are saved as completed extraction

**Medium · Extraction · verified (reproduced).**

**References:** `scripts/extract.py:838–846`, `983–985`, `1000–1018`, `1149–1164`.

The normaliser returns unparseable content unchanged. Save happens before validation. Validation issues are printed but extraction continues, including a successful sandbox result. Required status is never filled by the normaliser.

**Evidence:** the save reproduction preserves `atlases_used: [""MNI152 atlas"]`; `test_normalizer_does_not_fill_status` leaves status absent. Current manual repairs do not fix the writer.

**Scenario:** a batch marks a paper processed, but some drafts cannot be loaded or reviewed. A bad replacement may destroy a valid prior draft before the error is reported.

**Fix:** parse and validate all outputs in staging; deterministically set file-level metadata known to the pipeline; quarantine malformed output with an explicit failed result. Preserve the raw response for diagnosis, without admitting it to active drafts. Do not attempt unconstrained “repairs” that change scientific text.

### 18. Reviewer mark IDs collide across drafts of the same paper

**Medium · Checks and review · verified (code trace).**

**References:** `scripts/portal_import.py:165–169`; `scripts/refocus.py:156–164`, `179–191`, `209–220`; `scripts/promote.py:221–231`.

Marks are numbered locally within each draft (`m1`, `m2`). Refocus gathers multiple drafts but keys its `produced` map only by that local ID, then marks every same-ID mark done if any finding answered it. Unresolved marks also cease to block promotion because the gate tests only `status == "pending"`.

**Evidence:** `refs = produced.get(str(m.get("id")))` has no draft component. Promotion's pending filter does not include unresolved marks.

**Scenario:** two region drafts each have m1; answering one marks both completed. Or the model returns no finding, sets unresolved, and promotion no longer requires a person's resolution.

**Fix:** globally unique mark IDs or `(draft identity, mark ID)` keys throughout prompts/results; validate returned mappings. Unresolved marks must remain a review obligation until a person explicitly resolves or dismisses them.

### 19. Extraction commits include unrelated edits under broad directory paths

**Medium · Extraction · verified (code trace).**

**References:** `scripts/extract_ready.py:43`, `214–219`; `.github/workflows/portal-apply.yml:87–101`.

The local command commits all changes under `drafts`, `logs`, `screening`, `citations.md` and `portal/papers.json`, not just files it wrote. Using `git commit -- <paths>` does correctly avoid unrelated staged files *outside* those paths, but includes pre-existing work *inside* them. The apply workflow stages everything with `git add -A`, then rebases/pushes with a bypass token before test results can gate publication.

**Evidence:** `COMMIT_PATHS = ["drafts", "logs", "citations.md", "screening", "portal/papers.json"]`; no clean-state or before/after ownership check.

**Scenario:** a maintainer has unfinished human draft edits or protocol changes; running extraction publishes them along with the generated drafts. CI's clean checkout reduces this specific local risk, but its direct push still bypasses review and checks.

**Fix:** use a clean isolated worktree or fail on pre-existing changes in managed paths; track exact generated changes. For apply, create a bot branch/PR and require checks before merge. Keep maintainer bypass only for deliberate emergency use, not the normal scheduler. Actual repository rule/token settings were not queried.

### 20. Apply and promotion are not transactional or reliably replayable

**Medium · Checks and review · verified (code trace).**

**References:** `scripts/promote.py:271–306`; `scripts/portal_import.py:145–153`, `175–188`, `339–399`.

Promotion writes the canonical file, then deletes the draft, then appends the audit log. Import modifies drafts record-by-record but moves applied records only at the end. No operation ID is stored with passage additions/comments or canonical merges.

**Evidence:** a crash after `_write(canonical, ...)` but before `draft.unlink()` leaves both; retry appends the same findings under fresh f-IDs. A crash after `apply_comment` but before inbox archival replays the comment. `apply_verdict` catches promotion errors and returns a normal summary string; `run` treats anything not starting `skip`/`error` as applied, so a failed promotion can be archived as successful application.

**Scenario:** laptop interruption duplicates evidence or loses the audit link; a transient promotion problem disappears from the actionable inbox.

**Fix:** durable operation IDs and idempotency checks; atomic file replacement plus a recoverable multi-file journal; structured per-record outcomes that distinguish opinion recorded, promotion blocked and fully applied. Archive only the intended completed operation.

### 21. Repetition-loop recovery crashes with an undefined name

**Medium · Extraction · verified (reproduced).**

**References:** `scripts/ollama_client.py:283–290`; `scripts/extract.py:592–606`.

The exception message interpolates `LOOP_BLOCK`, which is never defined. Python raises `NameError` before constructing `RepetitionLoop`, bypassing the retry and partial-response preservation logic.

**Evidence:** `test_loop_detection_raises_name_error` feeds a fake repeated stream and gets `NameError: name 'LOOP_BLOCK' is not defined`.

**Scenario:** the exact repetitive-output failure the retry was meant to handle terminates that extraction attempt without its intended diagnostic artifact.

**Fix:** remove the nonexistent value or have the detector return the measured period; test the streaming client through the extractor's retry path. Separately, the advertised timeout is a socket-operation timeout, not a wall-clock deadline: continuously arriving output can exceed it. Add an overall deadline if “seconds per paper” is intended literally. HTTP 500 handling does raise `OllamaError`; there is no automatic 500 retry, and extraction catches it per paper.

## Findings — low severity

### 22. The requested pytest entry point cannot run the full suite

**Low · tests · verified (reproduced).**

**References:** `tests/test_review_guardrails.py:54–56`, `257`; `requirements-ci.txt:1–5`; `.github/workflows/test.yml:59–68`.

The guardrail module starts a server and runs checks at import time, then calls `sys.exit`, aborting pytest collection. Requirements do not include pytest. CI instead runs each script individually and passed locally, so this is a testing-interface defect, not proof that existing CI is red.

**Evidence:** requested command ends with `INTERNALERROR ... SystemExit: 0`. Tests do not exercise the real extraction provenance format, default loader admission, deletion failure, stale review or path traversal cases above.

**Scenario:** a contributor's standard test run never executes the rest of the suite.

**Fix:** move script-only execution under `if __name__ == "__main__"` or convert it to test functions/fixtures; document one supported suite entry point and include its dependency. Add the demonstrated negative cases as desired-behavior regression tests.

### 23. Logs leak machine paths and record ambiguous local times

**Low · repo hygiene · verified (tracked content and code).**

**References:** `scripts/auto_review.py:345`, `1020`; `logs/auto_review/stroke_severity__Pedersen2004.yaml:4`, `21`, `40`.

The checked-in log contains `/Users/uqmmasso/.../papers` and timestamps such as `2026-05-06T16:45:27` without timezone. New sidecar timestamps still use naive `datetime.now()`; check details interpolate absolute directories.

**Scenario:** runs on UTC and Brisbane machines appear out of order; logs disclose workstation layout and are less portable.

**Fix:** timezone-aware UTC timestamps, repo-relative logical paths and a separate local diagnostic path if needed. Do not invent offsets for historical ambiguous timestamps; annotate provenance/uncertainty when migrating them.

### 24. A redundant 15 MB source snapshot is tracked

**Low · repo hygiene · verified (tracked archive inspection).**

**References:** root `_sync_snapshot.tgz` (binary, no line number); `scripts/snapshot.py`.

`git ls-files _sync_snapshot.tgz` returns the archive; size is **15,190,444 bytes**. Its member list includes source, canonical entries and drafts, duplicating old versions inside an opaque artifact. This inspection did not extract its papers or evaluate quotation rights.

**Scenario:** deletion or correction of a draft in the normal tree leaves its older text available in the archive; every clone pays for the blob and ordinary diffs cannot review its contents.

**Fix:** remove it from the current tree, ignore future sync artifacts, use explicit local transfer/release storage. Do **not** routinely rewrite history for size alone. Only consider a coordinated history cleanup if the maintainer establishes actual sensitive content requiring removal; that would require a separate decision. No history changes made here.

## Requested questions and known-issue disposition

### Governance and preservation

The normal automatic path does classify Tier A, checks full-paper availability for its second reading, requires unanimous valid model votes and keeps Tier B approvals deferred. `--allow-local-override` is deprecated and ignored (`auto_review.py:792–806`, `1703–1705`); it is not the bypass. Provisional verdicts do not themselves promote. Those guardrails do not repair findings 1–6.

Recheck preserves *parseable* drafts with named reviewers, edits, portal reviews, comments, marks, non-draft status and `rereview_of`. It does not protect these through every other script. Rereview preserves existing replacement drafts, but **drops all legacy findings for that paper merely because the destination exists**, without checking that it is complete or even parseable (`rereview.py:124–128`, `158–162`). This is documented in its own header, so not a newly discovered covert overwrite; it is a risky replacement policy. Prefer retaining the old evidence as a comparison artifact until a person reconciles it. Governance §5's simpler preservation description does not explain this loss.

Keeping a rewrite with absent quotes (known issue 10) is **confirmed**: `better()` compares `(absent, schema_issues)` lexicographically (`recheck_drafts.py:174–175`), so 3 → 1 is kept even if schema problems increase. Keeping an explicitly failing *draft* is not itself approval and is defensible as repair progress. Calling it ready would not be; quote failures must remain visibly blocked, and finding 6 currently weakens that block.

### Benchmark interpretation and privacy

The checked-in summary uses **Alyahya2018NounVerb and Yourganov2015Predicting**, not Bonilha2014. It excludes 16 and 30 legacy findings respectively and uses 17 and 10 current findings. Offline inspection found 14 reference links for Alyahya. Link matching already uses canonical IDs/aliases, legacy symptom mappings, undirected endpoint pairs and self-link exclusion (`benchmark_models.py:383–443`). It does **not** merely compare draft filename stems against canonical filenames; that suspected old bug is not present in this revision.

The 0–10% numbers cannot be independently recomputed without candidate sandboxes. Current output counts are only 0–11 findings per model/paper, so low measured coverage is plausible. The metric is still exact endpoint recovery after limited normalisation, not semantic recall of all claims: alternative anatomical granularity or a concept without an alias can look like a miss. Review missed/shared links against claims before interpreting the ranking. Do not claim the low recall is conclusively real or conclusively a matcher bug from this checkout alone.

Summing nonnegative absent counts does implement zero absent on each **evaluated** paper. Empty/ignored outputs and incomplete publication defeat the completeness assumption (findings 13–14). Schema totals and mean strength comparisons are aggregate, with the documented +0.2 tolerance, not a robust per-paper non-inferiority test. The two selected papers have the same main reference bucket (`impairments`); they provide a narrow paired pilot, not general validation of extraction across therapies/reviews or validation of model review. The reference paper set, reference content hash, scorer/prompt/schema revision and per-run model digest/settings should be frozen for reproducibility; publishing current `ollama show` facts does not establish which bytes produced an old sandbox.

The public JSON uses an explicit row allowlist (`benchmark_models.py:594–599`, `700`) and excludes `absent_examples`, `schema_examples` and full claims/passages. I found no source-passage payload in the checked-in summary. “Only numbers and ids” is literally inaccurate: it includes reasons, reference descriptions, model notes and source URLs, but those are not paper text. This review makes no blanket copyright determination.

Known issue 11: poor **extraction** schema performance by 26b does not prove poor **review** performance under a constrained response schema. The defect is claiming review needs only short context while the reviewer actually receives the whole paper (`auto_review.py:967–968`). A separate held-out review benchmark with fabricated quotes, false numbers, reversed direction and omitted qualifiers is needed before assigning approval authority. Repeated votes from one model are not independent validation of its accuracy.

### Portal security boundary

Traced upload → private R2 object → signed-email GitHub record → importer destination/checksum → intake → extraction → review → promotion. Also traced review POST → batched GitHub record → scheduled apply → `apply_manual_verdict` → `promote.py` → bypass-token push. The dangerous breaks are detailed above.

The checked-in middleware cryptographically verifies the JWT signature and audience; identity fields from request JSON are overwritten by signed identity in `portal/lib/github.js:36–40`. The maintainer-only Apply/requests endpoints enforce the environment allowlist. PDF serving validates a single basename and keeps a fixed `cc` or `pdf` prefix, so I did not find a route-name traversal from public cc to private pdf. Upload checks actual byte length and `%PDF-` magic rather than trusting Content-Type; it buffers the entire body before the actual-length limit and does not validate full PDF structure.

An email accepted by Access but **absent from `portal/reviewers.yaml` can still read private PDFs, fetch uploads and submit edits/screening records**: middleware does not consult that file; importer `who()` assigns unknown emails a human name with no approval right (`portal_import.py:74–81`). That is documented importer behavior. It conflicts with any operational expectation that the YAML file is the read/write allowlist. With the suggested broad `@uq.edu.au` Access rule, it is especially material. Choose an explicit access model and test it; do not assume removing YAML membership revokes portal access.

Static screening bundles containing abstracts pass through the middleware unchanged (`_middleware.js:62–65`; `publish_portal.py:253–287`). Their privacy depends entirely on externally configured Access coverage, including preview domains. **Suspected deployment risk only:** uncovered hostnames or a broad bypass could expose them; no deployed configuration was inspected. JWT validation also does not require expiry or check issuer/nbf; key/audience verification prevents a simple client-forged identity, so no unauthenticated bypass is claimed on that basis.

Token scope is described as repository-scoped Contents write + Actions write and held as a Pages secret; the code only sends it to GitHub via the server-side helper. Actual scope/storage could not be verified offline. It is not directory-scoped: compromise of the function/token can write more than inbox records. `portal-apply.yml:93` directly interpolates `requested_by` into shell text; pass it through an environment variable instead. Workflow dispatch already requires privileged access, so this review does not label it an unauthenticated RCE.

### All eleven supplied suspicions

| # | Disposition |
|---|---|
| 1 | Confirmed: subset publication replaces full JSON; finding 14. |
| 2 | Confirmed: backups included and sidecars collide; finding 15. |
| 3 | Confirmed: invalid YAML saved; finding 17. |
| 4 | Confirmed writer defect: missing status not defaulted; finding 17. The cited manual repair does not repair normalisation. |
| 5 | The schema and extraction guidance are clear: responder means a therapy moderator (`docs/schema.md:226–233`; `docs/EXTRACTION_SKILL.md:190–194`, `376`). This is a model classification error, not an instruction to call natural recovery responder. Add explicit spontaneous-recovery counterexamples and a semantic review check. The actual Stockbridge interpretation remains unverified without its paper. |
| 6 | Confirmed: absolute paths and naive timestamps; finding 23. |
| 7 | Confirmed: many import-time `ROOT / "papers"` constants/defaults, e.g. `auto_review.py:135`, `322`; `portal_import.py:63`; `recheck_drafts.py:57`, `113`. Some CLIs have overrides, but no shared configuration. Introduce one late-bound path resolver and test a relocated papers directory. |
| 8 | Confirmed: four empty Hazelton impairment drafts plus a nonempty review draft. Empty topic placeholders should not count as extracted/reviewable findings. Whether to exclude the paper needs the screening protocol, abstract/full text and intended scope; its title alone is insufficient. |
| 9 | Confirmed tracked 15 MB archive; finding 24. No history rewrite recommended by default. |
| 10 | Confirmed improving-but-still-failing drafts retained; not itself an approval, discussed above. |
| 11 | Extraction results do not validate/refute reviewer quality; the short-context and same-model advice is inconsistent with the current review path/policy. |

### Consolidation and test priorities

Consolidate the **approval gate, model-provenance parser, active-draft enumeration, safe path resolver, validation dispatch and transactional frontmatter writer** first. These duplications already cause observable inconsistent behavior. Then unify paper lookup/configuration and the six-bucket catalogue (comparison has four; extraction/normalisation five; other tools six). `ollama_client.py` already provides useful shared transport; repair and test it before creating another wrapper.

Do not declare scripts dead from names alone. `reextract.py`, `normalize_drafts.py` and `rereview.py` are documented alternate workflows with different preservation semantics; deprecating or routing them through one implementation would pay off, but deleting them without mapping callers is not justified by this review.

The highest-value missing tests are complete ingestion-to-export boundary tests, production-format self-review, stale portal review, hostile filenames/IDs, all-or-nothing rewrite failure, idempotent replay and public-object revocation failure. Browser/Python parity can prove that both sides agree while both consume improperly admitted evidence; add admission expectations, not only parity fixtures.

## What I would change first

1. Close every approval/export bypass together: draft-origin exclusion, safe model output paths, real tag comparison and one validated promotion gate.
2. Make absent quotes unconditionally blocking; repair numeric/elision matching with adversarial negatives before relying on new benchmark conclusions.
3. Audit public manuscript-only objects and fix deletion retry/serving authorisation so a licence correction actually revokes exposure.
4. Bind portal decisions to reviewed content and make rewrites/import/promotion recoverable and idempotent; protect human work across all entry points.
5. Freeze a complete benchmark manifest and enforce paired nonempty evaluations before publication; add the demonstrated failures to the regular suite.

## Documentation contradicting code

- **GOVERNANCE §1–3** requires checked quotes, a second reader, actual Tier A and a different tag. Findings 1–6 show enforcement failures; `--tier A` is not evidence that these happened.
- **GOVERNANCE §3** says reviewer output reports per-field `agree | disagree | cannot_verify`, reasons and passage page. `auto_review.py:599–621` uses per-finding booleans for the six checks, one finding verdict and no located-page field. It also does not include schema text in `_build_llm_prompt`, despite the policy saying the reviewer gets it.
- **GOVERNANCE §4** says rejection moves a canonical entry back to drafts. `promote.py:310–330` merely marks the supplied file rejected in place; it does not move it.
- **GOVERNANCE §5** describes moving the old evidence to rereview drafts with previous approval preserved. `rereview.py:124–128` instead drops it whenever a replacement path already exists.
- **MODELS.md:28, 248–251** describes short-context review, recommends reusing the extract model, and describes the old `--allow-local-override` guardrail. Current review appends the entire paper, requires a different tag in policy, and ignores that flag.
- **MODELS.md:98, 266** still calls 26b the default while its introduction and `models.yaml` select 31b for extraction. The public results now use Yourganov rather than the Bonilha example used in some commands; commands should be clearly labelled examples versus the versioned benchmark set.
- **MODELS §3** promises meaningful every-paper eligibility. Empty/unexamined output and subset publication violate that implication (findings 13–14). `compare_extraction.py:367–400` also tolerates some absent quotes relative to the curated baseline, unlike the document's zero-absent decision rule.
- **schema.md:7, 90, 419** simultaneously says current 2.4, “Must be 2”, and current 2.7, while line 83 requires 2.8. The loader dispatch itself validates 2.8 through the v1 branch.
- **schema.md:507–512** says promotion creates stubs for unresolved target IDs. `promote.py:253–290` only writes/merges the draft's own entry; there is no target-stub creation pass.
- **README.md:52, 95** says papers never leave the machine. `publish_portal.py` publishes annotated copies and private source copies for screening. GOVERNANCE has the more accurate exceptions.
- **PORTAL.md:83–84** says source PDFs are never published. `publish_portal.py:194–211` uploads source full texts to private `pdf/<cid>_fulltext.pdf`; private publication should be stated explicitly.
- **PORTAL routine** says extraction commits only what it wrote; `extract_ready.py:43,214–219` commits broad paths including pre-existing changes. PDF sync also describes deletion as completed even when its deletion call failed.
- **promote.py:14** promises atomic approval; canonical write, draft removal and audit append are separate operations.
- **extract.py:757** calls the rebuilt frontmatter always parseable; repair preserves syntax failures and save accepts them.
- **Local-only transport descriptions** are guarantees the code does not enforce: extraction merely warns and continues for a remote host (`extract.py:1342–1347`), review records a warning (`auto_review.py:809–810`), and `ollama_client.is_local` uses substring matching (`106–111`). A URL such as `https://localhost.example.invalid` is classified local. Reject remote hosts/cloud tags for restricted paper work rather than relying on a warning, or narrow the documented guarantee.
