# Three-paper retrospective pilot — 11 November 2026

Gemma 4 (31B) and Qwen 3.8 (27B) independently extracted Yu2023,
Zevgolatakou2022 and Hope2017 from their main PDFs. Claude reconciled the outputs;
Codex cross-checked the reconciliations against independent source reviews.
Supplements were excluded. Reconciled inventories contain 23, 21 and 16 analysis
records respectively. All 60 pass the exact-source quotation/structure audit;
that audit is not a semantic accuracy or completeness score.

The interrupted Zevgolatakou Qwen arm was rerun with a 20,000-token output
budget, and both Hope arms used that budget. All three recovery calls finished
normally. The earlier completed runs were reused; failed outputs were retained.

Key corrections:

- Yu2023: recovered 12 figure-printed partial-correlation values and additional
  analyses/nulls. Preserved inconsistencies in printed t/P pairs rather than
  asserting that all six regressions establish significance.
- Zevgolatakou2022: restored an entire graph-analysis family omitted by Gemma.
  Both models incorrectly called the language-network semantics lesion-volume
  term significant. Its table confidence interval crosses zero; the source's
  conflicting prose remains an explicit discrepancy.
- Hope2017: corrected the peak negative-cluster statistic misidentified by both
  models. Added omitted information and distinguished change associations
  requiring two scans from baseline-only prediction.

These observations motivate prompt refinements for variable selection,
confidence-interval signs, distinct analysis families and image-only evidence.
They do not establish an accuracy percentage or the best model pairing. This was
a risk-selected sample, and the updated prompt still needs wider evaluation.

No pilot extraction was automatically promoted, approved or published. Raw paper
text and local review packets remain local. See DUAL_EXTRACTION.md for the
full-corpus command and the required separate source-review stage.
