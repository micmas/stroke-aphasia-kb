# Prepare, extract and review papers

Run commands from the repository root using `.venv/bin/python kb.py`.
Install the environment using the [README](../README.md), and install the local
models you intend to use in Ollama. See [Models](MODELS.md).

Extraction inventories, reconciled text and approved KB findings are different
outputs. The pipeline below preserves that distinction.

The previous draft queue was retired at the clean baseline. Before mapping a
replacement paper, check `logs/baseline/2026-11-12.json` and any preserved reviewer
material for unresolved source questions. An archived approval or model verdict
does not automatically approve a newly extracted finding.

## Download portal uploads without starting models

Run `.venv/bin/python kb.py sync` to download uploaded PDFs and publish their
completion receipts. This does not start extraction or review, approve findings,
or run intake/OCR. To download and prepare in one action, use
`.venv/bin/python kb.py sync --intake` once processing is idle, or add `--wait`.
For files already downloaded, use `kb.py intake --execute`. Intake can rename,
strip cover pages and OCR sources, so it will not run during extraction or review.
It never starts model extraction. Create fresh manifests after changing PDFs.

Use `.venv/bin/python kb.py status --jobs` to see active KB model jobs. Start
extraction or review only when you choose. Their `--run` commands refuse to
compete with a detected job; add `--wait` to wait in your open terminal.
See [Commands](COMMANDS.md) for sync prerequisites and recovery.

## 1. Prepare verified sources

Select papers under the [screening protocol](SCREENING.md), register their
citation keys and DOIs in `citations.md`, and place each main PDF in
`papers/<Key>.pdf`. Check that title, authors, DOI and version match. A file being
available locally does not establish permission to redistribute it.

Create a new run manifest for your selected keys:

```bash
.venv/bin/python kb.py prepare \
  --papers Paper2024 Another2025 \
  --output _compare/my-batch/manifest.json
```

Replace the example keys with registered paper keys. Preparation writes the
manifest but does not call a model. It records source hashes and licence metadata,
resolves known filename aliases by DOI, and lists missing sources separately.
Without `--papers`, preparation selects the entire registered bibliography; use
that for a deliberate full-corpus run, not as a substitute for screening new papers.

Use `--segment-chars 50000` when preparing a batch that needs bounded source
sections. Every original text unit remains covered; no summaries replace omitted
pages. Main-PDF appendices remain included, while separate supplementary files do
not enter the workflow. Image-only content still needs visual checking.

## 2. Extract independently

Preview first:

```bash
.venv/bin/python kb.py extract \
  --manifest _compare/my-batch/manifest.json \
  --output-dir _compare/my-batch/extraction
```

Add `--run --continue-on-error` to start. By default the models are `gemma4:31b`
and `qwen3.8:27b`, each with a 20,000-token output allowance. Override explicitly
with `--models MODEL_A MODEL_B` and `--max-output-tokens 32000` when needed.
The models run serially, each receiving source text without the other's answer.

The output retains both raw inventories, prompts, source IDs, hashes, settings,
audit warnings and errors. Each completed pair retains the files needed for independent review. No KB draft
is created or approved at this stage.

Segmented extraction saves every section separately, then concatenates each
model's records with unique IDs. It does not resolve cross-section dependencies
or deduplicate overlapping findings. A failed section prevents that model's
whole-paper output from being marked complete.

## 3. Reconcile with a separate local model

Finish or stop extraction with Ctrl-C before using the same local resources for
review. Choose an installed reviewer distinct from both extraction models.

```bash
.venv/bin/python kb.py review \
  --run-dir _compare/my-batch/extraction \
  --output-dir _compare/my-batch/review \
  --model YOUR_REVIEW_MODEL --limit 3
```

This previews completed paper pairs only. Add `--run` to execute. Inspect the
first three reviews before removing `--limit 3`. The script checks the extraction
batch lock and refuses to run while that batch is active.

The reviewer first inventories the source without seeing either extraction. It
then reconciles both outputs against the original text, records a decision for
each original analysis, and accounts for every source-text unit. Both calls use
a 20,000-token output allowance unless overridden. Model digest, prompts, settings,
source hashes and raw responses are retained. Agreement is not evidence of truth.

Review outputs include `inventory.json`, `decisions.json`, `coverage.json`,
`audit.json`, `provisional-extraction.txt`, `visual-review-required.json` and
`status.json`. All have provisional meaning and `approved: false`; no status means approved.

| Status | Meaning |
|---|---|
| `failed` | Input integrity, parsing, transport or generation failed. |
| `requires_revision` | The reconciliation failed evidence, schema, coverage or decision checks. |
| `requires_visual_review` | Deterministic checks passed; semantic accuracy and completeness are not certified. |

The reviewer is text-only. Figures, table geometry, image-only values and OCR
fidelity still need checking against the PDF. The current reviewer also submits a
whole-paper prompt: very long segmented papers may require a separate segmented
reconciliation process, which is not yet implemented. Oversized inputs fail rather than being silently
truncated; these papers remain extracted but not reconciled.

## 4. Verify, map and approve

Read the main PDF, checking important tables and figures visually. Confirm sample
sizes, model definitions, adjustment variables, timing, uncertainty, anatomical
meaning, null results and source inconsistencies. Resolve evidence warnings and
check for omissions shared by every model.

Map reconciled findings into the [KB schema](schema.md), retaining unmatched
findings rather than forcing an incorrect anatomical or outcome label. This
mapping stage is currently a separate task; there is no automatic conversion from
`inventory.json` to approvable KB drafts.

Record the visual check in a separate `human-check.md` beside the paper's review
outputs, with reviewer, date, source PDF hash, checked pages, unresolved issues and
links to the resulting drafts. This is a manual audit record, not an automatically
enforced approval stamp. Check:

- Exact supporting quote and page for each claim and value.
- Rendered tables and figures, including signs, coordinates and footnotes.
- Sample size and denominator for each analysis.
- Threshold, correction, covariates and model belonging to that analysis.
- Direction, timing and the distinction between selection and significance.
- Null results, qualifying findings and unmapped results retained explicitly.

For existing KB drafts:

```bash
.venv/bin/python kb.py drafts
.venv/bin/python kb.py inspect --draft drafts/<collection>/<file>.md
.venv/bin/python kb.py validate --check drafts/
```

Use the [approval policy](GOVERNANCE.md) and [portal](PORTAL.md) for approval and
publication. Model reconciliation is not the delegated KB approval procedure.
Nothing is promoted simply because a local review returned valid JSON. After
source verification and mapping, an authorized human approver uses:

```bash
.venv/bin/python scripts/promote.py --approve drafts/<collection>/<file>.md --reviewer human:<name>
```

`kb.py status` reports the existing KB, not per-paper migration progress. Its
historical missing-stamp hint is a compatibility diagnostic; the product wrapper
intentionally refuses `--tag-legacy`. Do not stamp unchanged findings merely to
clear that hint.

## Stop, resume and recover

- Ctrl-C preserves completed papers and partial outputs. Repeat the identical
  extraction command to reuse completed pairs. Incomplete/failed papers remain
  skipped with `--continue-on-error` until explicitly retried.
- After examining failures, `--retry-failed` archives and reruns failed paper pairs.
  It does not reuse completed sections inside a failed segmented paper.
- Changed source files, code or settings require a new manifest/output directory.
  Never edit a completed run to make it appear to have used the new settings.
- Output truncation may need a larger output budget or smaller source sections.
  An oversized input needs segmentation; a larger output budget cannot fix it.
- Review resumes only when saved inputs, code, settings and output hashes match.
  Failed or interrupted reviews require a new output directory for retry.

A full-corpus migration is complete only when replacements have passed the same
review and approval requirements. Track pending work by processing stage; do not
create a permanent lower-quality category or relabel old findings as newly reviewed.
