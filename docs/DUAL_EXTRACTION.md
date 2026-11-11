# Main-paper extraction with independent reconciliation

Status: experimental workflow, developed on OsaGarcia2020 and Thye2018. It produces a source-based research extraction, not an approved knowledge-base entry or a validated method of interpreting an individual scan. No model weights have been changed. The default KB extractor is unchanged by this optional workflow.

## Source scope and completeness

Use the main paper's full text, tables, captions and figures. Supplementary files are excluded by user choice. Mark details available only through an excluded supplement as outside scope. Do not retrieve them to fill gaps, infer missing values, or claim that main-paper extraction represents every analysis the authors conducted.

Before extracting, record the citation, DOI, licence, PDF checksum, page count and source version. Check whether text extraction lost pages, symbols, table columns or image-only content. Inspect relevant tables and figures visually. A text-only local model does not see image content: preserve that limitation and assign it to the separate source review. Empty text is a failure, not an empty findings set.

Completeness means coverage of every substantive main-paper outcome and analysis, including null results, adjustments, model comparisons, limitations and source inconsistencies. A large record count or agreement between models is not evidence of completeness.

## Run two independent extractions

```sh
python scripts/dual_extract.py \
  --pdf /path/to/Paper.pdf --citation @Paper2020 \
  --models gemma4:31b qwen3.8:27b \
  --output-dir /path/to/new-run
```

The command runs the models serially to avoid competing for local memory, but they are independent: each receives the same original source and prompt, never the other's answer. Same-model repeats can be requested, but at temperature zero they may add little diversity. Different models also share errors; neither setup supplies an independent ground truth.

Each run retains its prompt, page-labelled source units, raw response, checksums, settings and errors. The output directory must be new. The review packet requires identical citation, PDF, prompt and source-unit hashes. The local client requires loopback processing. Quote mismatches remain visible for review. Duplicate JSON fields are rejected; the canonical extraction/KB parsers also reject duplicate YAML fields so evidence cannot silently disappear.

The inventory stage does not map findings into existing KB entities. This avoids losing results simply because they have no obvious existing target. It records outcomes, timing, separate models, candidate/retained predictors, covariates, estimates, evidence and uncertainties. A significant coefficient is not the same thing as a variable retained in a model. Cross-sectional score prediction is not recovery prediction.

The current runner records and fails truncated input/output without silently retrying with instructions to omit detail. Repetition failures retain partial responses. An explicit rerun should use a new directory after fixing the source or budget. The four development runs used the earlier transport wrapper; none retried or truncated, and their saved prompts remain the experimental record.

## Third-model review and source adjudication

The command prepares `review/packet.json` and `review/review-instructions.txt`; it does **not** call an external reviewer or automatically merge answers. In this development exercise, Claude reviewed both independent local inventories and Codex checked the reconciled files against the sources.

Review the union of both inventories, then reread the source for omissions shared by both. Do not take a majority vote. For every substantive record:

1. Confirm outcome definition, units, direction and assessment time; distinguish current level, future level and measured change.
2. Identify the exact statistical model, candidate and retained terms, covariates, selection procedure, comparison and validation design. Keep restricted and fully adjusted findings separate.
3. Verify each numerical estimate, sign, denominator and uncertainty against its sentence or table row/column. Preserve printed disagreements rather than choosing or repairing a value silently. Label any reviewer arithmetic as derived.
4. Check supporting quotations against their declared source units and PDF pages. Exact matching is necessary provenance evidence, not proof that the quotation supports the interpretation.
5. Inspect population, stroke type/phase, laterality, modality, acquisition and processing, lesion/tract definition, atlas/reference space, spatial resolution and relevant thresholds. Record unreported details explicitly. Never substitute MNI152 for Colin27 or infer an atlas from familiar anatomy.
6. Distinguish regional template coverage from effect size, participant lesion probability and diagnostic thresholds. Check whether the study actually supplies a patient-level prediction equation, calibration and external validation.
7. Preserve null/contrary evidence, limitations, overlap with previous cohorts and the distinction between the authors' conclusion and results.

Review outputs:

- `inventory.json`: reconciled source-first records, with original source IDs.
- `decisions.md`: what was retained, corrected, rejected, split or added by the reviewer, with locators and origin in each run.
- `final-extraction.md`: readable findings and imaging/population context.
- `coverage.json`: every substantive main-paper outcome/model/table/figure mapped to records or a prose section, with explicit partial coverage and unresolved reasons. Supplements are excluded, not counted as model failures.

Run the same quotation/structure audit over the final inventory. A failed check requires correction or an explicit unresolved disposition; it must not be converted into approval. Record source-review changes separately from raw-model performance.

## Knowledge-base mapping and use for neuroimaging

Only after source reconciliation should a separate mapping stage consider canonical brain regions, tracts, assessments and impairments. Compare their definitions, not just labels. Preserve study-specific factors when equivalence is unproven, retain unmatched findings for review, and never force a mapping to improve apparent coverage. Schema validation and the existing human approval rules still apply.

A scan-facing interpretation should retain the population, phase, imaging method, anatomical definition, outcome and adjustment context alongside a finding. Group-level lesion associations do not establish that an individual patient has a deficit or will recover. Lack of significance is not proof of no association. This workflow supplies traceable research evidence; it has not established individual clinical utility.

## Evaluation before broader adoption

Freeze prompts and sources before each comparison. Build an independently adjudicated reference set on new papers, spanning methods, scan modalities and stroke phases. Evaluate claim precision and recall separately; also report numerical fidelity, model/adjustment fidelity, outcome/timing fidelity, quote/page accuracy, anatomical mapping and unresolved cases. Count omitted nulls and shared omissions, not just model disagreements.

Compare one pass, same-model second pass, different-model independent extraction, and independent extraction plus source review. Repeat runs, retain failures and measure reviewer effort. Predeclare acceptance criteria and critical errors. The two development papers cannot establish a general accuracy percentage or an optimal model combination. Do not use reviewer-corrected finals as evidence that the unreviewed local outputs were correct.

## Full-corpus rollout (source-inventory-v2)

Use the same method for every registered paper, including previously extracted or
approved papers and the five development/pilot papers. Do not create a permanent
"legacy" method tier. Track progress separately: source preparation required,
extraction failed, awaiting source review, reconciled, and mapped/approved.
Until replacement findings pass source review and the existing approval boundary,
retain the current KB; an extraction run alone is not a completed migration.

The unified prompt distinguishes original empirical analyses, pooled review
analyses, narrative synthesis, opinion and hypotheses. Review claims must retain
secondary attribution; the extractor must not invent new samples or statistics.
Image-only content still requires visual source review. Long papers may exceed
model context/output limits; preserve these failures for source preparation or
an explicitly planned segmented extraction, rather than silently dropping pages.

Create a frozen inventory from a checkout holding the PDFs:

```sh
python scripts/prepare_dual_batch.py --repo /path/to/stroke-aphasia-kb \
  --output /path/to/full-corpus.json
python scripts/batch_dual_extract.py --manifest /path/to/full-corpus.json \
  --output-dir /path/to/full-corpus-run
```

The second command is a preview. Add `--run --continue-on-error` to execute.
Both models run serially, with a 20,000-token output budget per model. Every
registered bibliography paper is included regardless of its earlier extraction
status. Missing/not-extractable sources remain pending. Uploaded filenames can
be resolved through an exact screening-record/bibliography DOI match. Annotated
copies and supplementary files are not input sources. Unregistered PDFs are
listed separately for identification rather than guessed into the cohort.

Licence metadata is retained, including explicit unknown status. This local
processing inventory does not authorize external sharing or publication; source
review and sharing must respect the particular file's permissions. PDF contents,
raw outputs and local absolute-path manifests should stay out of GitHub.

Repeat the identical run command to reuse completed paper pairs. Incomplete or
failed papers are preserved and skipped with `--continue-on-error`. After
inspecting failures, add `--retry-failed` to archive each failed paper attempt and
rerun its pair; completed papers remain reused. Ctrl-C leaves the interrupted
paper for that explicit retry. Concurrent execution of the same output directory
is blocked. Changed source checksums, model settings or extraction code require
a new batch directory. The final batch status lists failed and missing sources;
no successful output is automatically approved or written into KB drafts.

This command prepares independent review packets; it does **not** automatically
run Claude or another third reviewer. Review every successful paper against its
main PDF, including tables/figures and shared omissions, before mapping findings.

## Recovery of failed or newly available papers

Use a **new manifest and output directory**, keeping the original batch immutable.
The existing preparation command accepts `--papers Key1 Key2 ...` to select a
recovery cohort. `--segment-chars 50000` requests bounded source segments through
the same dual-extraction batch command; it is not a separate user-facing runner.

In segmented mode each model independently receives every original source-text
unit as a core unit exactly once. Original front matter and adjacent units supply
limited supporting context. Page/source IDs are preserved. No summary substitutes
for omitted source pages, and no supplementary files are loaded. Main-PDF
appendices remain part of the PDF. Each segment saves its actual prompt, original
units, response, settings and audit. An empty segment must give an explicit reason
for reviewer verification; an entirely empty paper is a failure.

A complete arm concatenates its segment inventories with unique prefixed record
IDs. It deliberately preserves possible overlap duplicates. **This is not a
cross-segment synthesis**: references to methods, model definitions, samples or
results elsewhere in the document may still be unresolved. Those dependencies,
duplicates and exclusions require source review. A failed/truncated/malformed
segment prevents the paper arm from being marked complete. Partial segments stay
on disk, but are not currently reused automatically by a paper-level retry.

The November 12 recovery cohort uses 32,000 output tokens per call rather than
20,000. Raising output budget alone cannot fix an oversized input; segmentation
is what addresses the 315-page Brady2016 input failure. It also limits how many
analyses the model must emit at once in the formerly truncated papers. These are
explicit recovery settings, not a guarantee of accuracy or successful generation.

The text reviewer currently submits a whole-paper reconciliation prompt. It may
still exceed context limits for very long segmented papers. Do not claim those
papers are fully reviewed merely because their segmented extraction completes;
segmented reconciliation and visual review remain separate work.

Registered-source corrections: Walker2011 is DOI 10.1016/j.bandl.2010.09.008
(PMID 20961612). Brady2022RELEASE now explicitly identifies the existing NIHR
monograph, DOI 10.3310/RTLH7522 (PMID 36223438); the related journal subgroup
analysis remains @Brady2022. Preserve cohort overlap rather than counting these
RELEASE reports as independent datasets. The uploaded Walker and Hillis PDFs stay
local; their availability does not imply an open redistribution licence.
