# Local extraction accuracy experiment — 11 November 2026

Status: all nine local runs completed (three baseline, three revised, three verification). Claude completed blind reviews of all three papers and subsequently reviewed the verification outputs; Codex reviewed all three papers and all verification outputs.

The first-pass intervention improves several evidence quotations and claim qualifications, but does not make these drafts ready for approval. It changes instructions, supplied target definitions and validation; it does not fine-tune or replace the local model.

## Reproducible comparison

Baseline code: `13f15f5`. First-pass intervention: `d7de780`. Model: `gemma4:31b`, temperature 0, thinking off, 16,000 maximum output tokens, auto-sized context. Historical reviewed drafts used a different model variant, `gemma4:31b-it-q8_0`, and are not the experimental baseline. Each arm runs once per paper, serially. Prompt hashes, raw outputs, frozen rubrics and PDF hashes are retained in the local experiment directory.

OsaGarcia2020 and Fritsch2022 are calibration papers. Thye2018 is held out for the first-pass prompt changes. Claude scored randomly labelled raw outputs against frozen source-based rubrics without inspecting the arm mapping. Codex reviewed the same sources and code with knowledge of the intervention. The model self-check is not independent review.

## Calibration observations

| Paper | Baseline exact quotations on stated page | Revised first pass | Main result |
|---|---:|---:|---|
| OsaGarcia2020 | 2/8 | 4/8 | Adjusted null moved into main claim, but statistical model still incorrectly labelled univariate. |
| Fritsch2022 | 2/7 | 9/11 | Better quotation fidelity, cautious strength and contrary evidence; word-generation finding still missing and secondary references incorrectly listed as primary. |
| Thye2018 | 2/2 after parsing; 7/8 in raw text | 6/7 (includes claims) | Direct claim evidence added; still only two findings and most required adjusted outcome comparisons omitted. |

Osa required-unit coverage improved from 1/2 to 2/2; the restricted-model unit still requires revision. Fritsch required-unit coverage remains 2/3, with problematic additional findings. Coverage is not correctness. Neither output is ready for approval. Claude found no fabricated quotations in either arm: failed matches were altered or mislocated real text.

The Osa revised predictor draft has two missing-metadata validation errors in the isolated output sandbox. Canonical entry autofill was unavailable to both arms because drafts were saved outside the canonical KB. The Fritsch revised output originally passed schema validation; Claude identified a narrative-review finding labelled causal. A subsequent validator fix now catches that existing documented constraint. This is improved detection, not improved raw-model accuracy.

The third-paper first-pass comparison also fails to establish a coverage gain. Both outputs focus on combined WAB/naming lesion-size results and a Heschl’s-gyrus association, omitting the systematic five-outcome adjusted template-load comparison. Codex reviewed this against the source. Claude subsequently completed the third-paper blind scoring: both arms covered only 2/5 required units. It also discovered duplicate `source_passages` YAML keys in the baseline: only two of eight raw passages survive permissive parsing. The 2/2 table value is a parsed-output diagnostic, not raw-output completeness or improved quotation accuracy. Raw baseline quotes were 7/8 exact; candidate quotes were 6/7 exact. The new strict parser rejects this silent data-loss defect.

## Deterministic protections and optional verification

Saved drafts record the actual extraction model and date. Quotes that fail an exact single-page match receive review flags and confidence is capped at medium unless already low. The checker never silently changes claims, effects or quote pages. A successful match establishes neither scientific support nor correct target mapping.

The optional verifier rereads the paper and draft and writes a separate, unapproved output. It preserves raw responses, reports failures and changes in findings, rejects citation drift, and refuses to overwrite an existing run. It is applied only to candidate outputs, so comparisons with the candidate measure an additional inference pass on top of the revised prompt. They do not isolate a prompt effect or establish independent verification.

The verifier was designed after calibration results and after the Thye source/rubric were known, although before Thye outputs were inspected. All verifier results are exploratory. No new held-out validation claim is made for it.

## Second-pass results and decision

| Paper | Extra pass time | Exact quotations on stated page | Result |
|---|---:|---:|---|
| OsaGarcia2020 | 124 seconds model call | 4/8, unchanged | Retains wrong model label; adds a wrong target and stronger evidence rating; two metadata errors remain. |
| Fritsch2022 | 127 seconds model call | 11/12 | Fixes synthesis relationship and one quote; introduces syndrome/impairment target errors, retains secondary references and missing finding. |
| Thye2018 | 110 seconds model call | 6/7, unchanged | Fixes causal labels; coverage, page error and template mismatch remain. |

The optional verifier is **not recommended for automatic replacement**. Its own correction notes sometimes assert changes it did not make. No findings were dropped by count (2→2, 5→5, 2→2), but unchanged count does not guarantee unchanged meaning. The raw files and deterministic before/after inventories expose those regressions. Two passes completed with structurally valid drafts; Osa completed inference but exited unsuccessfully with two schema errors. None is scientifically approved.

Retain the first-pass evidence/context improvements and deterministic review checks on the branch, while keeping human source review. Before enabling any self-check by default, evaluate a different verification approach on a larger, newly held-out set with adjudicated claims and coverage. This experiment does not justify a model-weight change or a general accuracy percentage.

## Artifacts

The local artifact directory is `/Users/uqmmasso/GITHUB/_coordination/extraction-accuracy-2026-11-11`. It contains `experiment-plan.md`, frozen prompt hashes, original raw outputs, per-run evidence reports, `codex-candidate-notes.md`, Claude's blind scores and code reviews, and before/after verification inventories. The sealed source PDFs and initial paper reviews are in the sibling `paper-reviews-2026-11-11` directory. These paths are local and are not published.

## Limits

One run per arm on a small selected sample cannot establish general extraction accuracy. Quotation matching, schema validity, semantic correctness and coverage are reported separately. Processing times are affected by prompt-prefix caching and resource conditions, so they are not stable speed comparisons. Original drafts, canonical findings and published outputs remain unchanged. No extraction has been approved.

Implementation verification at the original experiment: 133 tests passed, with five pre-existing PyMuPDF/SWIG deprecation warnings.

The subsequent independent-model experiment is documented in [DUAL_EXTRACTION_RESULTS_2026-11-11.md](DUAL_EXTRACTION_RESULTS_2026-11-11.md). It reuses known papers and makes no new held-out claim.
