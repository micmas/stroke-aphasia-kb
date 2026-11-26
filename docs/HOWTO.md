# Prepare, extract and review papers

Run commands from the repository root using `.venv/bin/python kb.py`.
Install the environment using the [README](../README.md), and install the local
models you intend to use in Ollama. See [Models](MODELS.md).

Literal source evidence, provisional review proposals and approved KB findings are different
outputs. The pipeline below preserves that distinction.

The previous draft queue was retired at the clean baseline. Before mapping a
replacement paper, check `logs/baseline/2026-11-12.json` and any preserved reviewer
material for unresolved source questions. An archived approval or model verdict
does not automatically approve a newly extracted finding.

## Collect open-access copies and sync kept papers

Use `./collect-pdfs.command` for all three collections, then
`./sync-pdfs.command` to download only saved, kept papers into
`papers/_incoming/open-access/{aphasia,dysphagia,practice}/`. These commands do not
format PDFs or run extraction. See [PDF collection and local sync](OPEN_ACCESS.md)
for the complete terminal workflow and filename/source metadata rules.

## Download portal uploads without starting models

Run `.venv/bin/python kb.py sync` to download uploaded PDFs and publish their
completion receipts. This does not start extraction or review, approve findings,
or run intake/OCR. To download and prepare in one action, use
`.venv/bin/python kb.py sync --intake` once processing is idle, or add `--wait`.
Sync verifies uploaded bytes against both the working PDF and same-record files in
`_originals`. An already received original is acknowledged even if intake changed
the working copy. A genuinely different replacement remains pending for review;
other uploads continue, and the working PDF is not overwritten.

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
`papers/CXXXX_<Key>.pdf`, where `CXXXX` is its screening record ID (the numeric
part can have more than four digits). Annotated copies retain the same prefix.
The portal mirrors annotated PDFs and private source PDFs awaiting screening or
annotation; it does not publish `_originals` or excluded duplicates.
Citation keys remain unchanged: for example, `C0046_Hillis2007.pdf` is still
`@Hillis2007`. Check that title, authors, DOI and version match. A file being
available locally does not establish permission to redistribute it.

Keep `papers/_originals/`: those files preserve downloaded versions before OCR or
cover-page removal. `_set_aside` is storage, not a screening decision; register
those papers and screen them before extraction. New portal uploads receive a
provisional upload identity until Apply assigns their permanent screening ID.

Renaming alone does not require re-extraction. The tools resolve older citation
filenames and still verify the frozen PDF checksum. Local `.filename-aliases.json`
retains exceptional download-name mappings. Do not edit old run manifests; prepare
a new manifest/output directory for a new extraction with updated code.

Automatic extraction is limited to **50 PDF pages**. Longer sources remain in the
manifest's pending list as `source_selection_required`; they are not excluded from
the screening register. Select a shorter publication under its own citation key,
or use `kb.py prepare --allow-long-papers` for a deliberate complete-source run.
That override is recorded in the frozen manifest. No pages are silently omitted.
The execution step also checks the limit, including for older manifests.

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
Unregistered PDFs already excluded by the screening register are listed separately
as `screened_out_unregistered_pdfs`; they do not need identification again. Their
files and screening history are preserved. An unresolved or newly included PDF
without a bibliography entry still needs registration before extraction.

For the relationship workflow below, omit `--segment-chars`: it creates small
passage and table tasks internally. Main-PDF appendices remain included; separate
supplementary files do not enter the workflow. Image-only content needs visual
checking.

## 2. Extract original evidence independently

The relationship workflow preserves source evidence and provides an incomplete review aid; it does not automate source verification. Use a fresh output
folder and a manifest without `segment_chars`. The models are
`gemma4:31b` and `qwen3.8:27b`; neither sees the other's answers.

```bash
.venv/bin/python kb.py extract \
  --profile relationships \
  --manifest _compare/my-batch/manifest.json \
  --output-dir _compare/my-batch/extraction
```

`--profile relationships` explicitly selects the current method; it is also the
default. See [Extraction options](COMMANDS.md#extraction-options) for every option
in this command and the progress counter.

This previews the batch. Add `--run --continue-on-error` only when you choose to
start local processing. Override the pair explicitly with `--models MODEL_A MODEL_B`
when testing a different configuration. Changing a model, prompt or code requires
a new run directory; do not edit files used by an active run.

Both models classify small windows of original passages and transcribe individual
main-paper table images. Code copies the original text with page numbers and
source offsets; models do not rewrite its quotations. Main-PDF appendices stay
in scope. Separate supplementary files are excluded. The 50-page limit applies.

Each completed pair saves `review/packet.json`, including original evidence,
both classifications, table transcriptions, disagreements and source warnings.
All passages remain available, including unclassified passages, nulls and
limitations. Nearby-passage links and search tags help locate timing, personal
factors and model roles; they are not verified analysis scope or clinical effects.

Matching table values do not certify header interpretation or visual completeness.
Unresolved tables remain held. Figures, damaged symbols and source contradictions
need visual source review. Actual model identities, prompts, settings, hashes,
raw answers, timings and failures are preserved. No KB drafts are created here.

## 3. Review the saved evidence with a separate local model

Finish or stop extraction with Ctrl-C before using the same local resources for
review. Choose an installed reviewer whose recorded weights differ from both
extractors. See [Models](MODELS.md) for measured candidates and current limitations.

```bash
.venv/bin/python kb.py review \
  --run-dir _compare/my-batch/extraction \
  --output-dir _compare/my-batch/review \
  --model YOUR_REVIEW_MODEL --limit 1
```

This previews completed pairs. Add `--run` to execute. Review reads the saved
extractions and verifies their source hashes; it does not re-extract the paper.
Inspect the pilot against the PDF before removing the limit. Different model
weights do not guarantee independent errors.

The reviewer selects a provisional study frame, then proposes relationships from
small groups of likely results, disagreements and flagged passages. Context is
kept separate from target evidence. Other passages retain visible dispositions
based on the two extractors' classifications, not independent verification.
They remain part of the human completeness check.

Each proposed relationship retains original evidence IDs, exact labels, outcome
type, model-versus-individual-effect category, qualifiers and unresolved checks.
The software checks source links and passage accounting. It flags context-derived
outcomes, unsupported model increments and author interpretations. It never
repairs source contradictions or releases held table values automatically.
A valid source label can still name the wrong outcome; passing checks is not
proof of semantic correctness.

Open the paper's `review.html` beside its original main PDF. Supporting files are:

| File | What to inspect |
|---|---|
| `study-frame.json` | Population, imaging, timing, personal-factor roles and applicability; all selections remain unverified |
| `proposals.json` | Proposed relationships, dispositions and suppressed contradictory proposals |
| `audit.json` | Missing relationships, nulls, unselected timing passages, role checks and visual-review requirements |
| `evidence.json` / `worklist.json` | Complete source evidence and which passages received model review |
| `status.json` and call folders | Exact source/code/model binding, prompts, schemas, raw responses and timings |

| Status | Meaning |
|---|---|
| `running` / `interrupted` | Processing / stopped; no completed review |
| `failed` | Input integrity, transport, parsing or generation failed |
| `requires_revision` | The saved review has unresolved coverage or evidence checks |
| `requires_source_review` | Structural processing finished; independent source verification is still required |

All outputs are unapproved. Empty frame slots mean **not located**, not confirmed
absent. The proposal list is incomplete. Check every proposed relationship, then
check completeness against the original Results and dispositions; inspect all
main-paper tables and figures visually. The HTML is a read-only review sheet,
not a portal approval form. Mapping into KB drafts is still a separate task.

Review v6 processes the study frame in bounded source windows and keeps all
selected IDs when merging them. Conflicting window summaries remain mixed or
uncertain. Relationship windows contain at most four target passages. Each model
call may make one logged retry using plain JSON, a different seed and a larger
output allowance; the same schema validation applies to both attempts. Raw
responses, settings and errors remain in `attempt-1/` and `attempt-2/`.

If a response copies a non-printing PDF character into a JSON string, v6 records
an encoding-only correction in `encoding-repaired.json`. The decoded text is
unchanged and `raw.json` preserves the model response. Duplicate fields, unknown
source IDs, incomplete responses and schema errors still fail validation. This
does not interpret damaged PDF glyphs or replace a visual source check.

Recover selected failures without rerunning completed papers:

```bash
.venv/bin/python kb.py review --run-dir _compare/my-batch/extraction \
  --output-dir _compare/my-batch/review-recovery \
  --model YOUR_REVIEW_MODEL --papers Paper2021 Other2023 --run
```

Failed/interrupted attempts stay preserved;
use a new review directory after changing the configuration or retrying an
incomplete attempt. Completed outputs can be reused only if their inputs, code,
settings and output hashes still match.

## 4. Verify, map and approve

Read the main PDF, checking important tables and figures visually. Confirm sample
sizes, model definitions, adjustment variables, timing, uncertainty, anatomical
meaning, null results and source inconsistencies. Resolve evidence warnings and
check for omissions shared by every model.

Map source-verified findings into the [KB schema](schema.md), retaining unmatched
findings rather than forcing an incorrect anatomical or outcome label. This
mapping is explicit: the converter does not infer an atlas parcel or treat model
labels as verified findings. Choose the bulk model-assisted route below or prepare
an explicit mapping after an agent/person source check.

`kb.py source-check --profile core` prepares short, source-linked drafts. Gemma
writes one finding; Qwen independently checks its analysis, direction, clinical
and imaging meaning, qualifications and missing caveats. There is no automatic
rewrite cycle. Unclear findings stay held while supported findings can move on.
Population and timing numbers are read from PDF crops once per paper by two
local models. The original text and both readings remain in the audit. This is
model assistance for a human reviewer, not approval or a completeness certificate.
Test a few papers before a full batch.

```bash
.venv/bin/python kb.py source-check --profile core \
  --run-dir _compare/my-batch/extraction \
  --review-dir _compare/my-batch/review \
  --output-dir _compare/my-batch/core-drafts \
  --model gemma4:31b --checker-model qwen3.8:27b \
  --limit 3
```

This previews the papers. Add `--run --convert` to run the local models and write
unapproved drafts. Remove `--limit 3` for the full manifest. Use `--papers KEY1
KEY2` to select papers, or `--proposals R001 R004` for a focused test. Progress
shows both the paper and finding counts. Existing drafts and source-review
decisions are preserved. A separate `--repo PATH` keeps pilot drafts outside
the live queue.

A core draft keeps the exposure, measured outcome, population, timing, useful
null findings and qualifications needed to interpret the result. For example,
a relaxed threshold, a selected patient population or internal-only validation
must remain explicit. Detailed statistics, coordinates, atlas fields and
structured covariate lists can remain **not transcribed**. That means pending
work, not that the paper did not report them. Each omitted field is flagged.

Before approving, the person reviewing must:

- Check the claim and quotations against the main PDF, including relevant tables
  and figures. Model text checking does not establish visual accuracy.
- Confirm the population, timing, clinical outcome and imaging measurement;
  template overlap must not be presented as patient tractography.
- Resolve the pending metadata needed for the intended use and check whether
  important findings are missing from the paper's draft set.

When rebuilding a corpus, add `--repo _compare/my-batch/new-drafts` to keep the
new draft batch separate from the current review queue. The generated Markdown
files are under that folder’s `drafts/`. They are not online until deliberately
transferred and published. Papers with earlier drafts or source-review records
are flagged for reconciliation; new candidate IDs do not inherit earlier
decisions. Corrected PDF image readings appear in the draft notes beside the
unchanged source-text quotations.

Every paper saves `status.json`, a conversion `mapping.json`, and each finding's
prompts, responses and five review answers. `batch-status.json` reports drafts,
holds, failures and preserved earlier work. The source PDF, code and model
identities are recorded. Neither JSON validation nor two-model agreement proves
scientific accuracy.

Repeat the identical command to resume completed checks. Changed source, code,
models or settings require a new output directory. Incomplete or invalid saved
model responses are preserved for inspection; they are not silently overwritten.
Papers over 50 pages or the input limit require manual source selection.
`--refresh-candidates` rebuilds the analysis inventory from the main paper while
preserving the previous review packet. It adds processing time and still does
not certify completeness. The core profile includes independent readings of numeric population/timing
passages and flagged PDF text by default. Disputed numbers become explicitly
pending rather than being copied as facts; a dispute about the core finding
still holds the finding. All drafts require human PDF review.

The older detailed checker remains available as `--profile full` for existing
runs. Its repair, consolidation and alternative context options are separate
from the core workflow. Do not mix settings or relabel old checks as core checks.

You can release supported drafts in small batches: the entire corpus does not
need to finish first. Check each completed paper's mapping and remaining issues,
then rerun its same source-check command with `--convert` to create drafts from
saved checks. Commit and push the new draft files to make them available in the
review portal and the explorer's drafts view. Refresh the annotated PDF when
new evidence passages have been added. A person's review and approval are still
required before these become approved KB findings. Existing approved content is
not replaced by this process. An excluded *candidate* is recorded in the local
report; it does not change the paper's screening decision.

The explicit mapping workflow remains available for agent/person source checks:

```bash
.venv/bin/python kb.py convert --review-dir _compare/my-batch/review \
  --mapping _compare/my-batch/mapping.json
```

This takes a snapshot of completed proposals, skipping unfinished papers. It can
run while other papers are being reviewed and does not start a model. Use a new
mapping filename to collect later results; existing mapping files are preserved.

For each proposal being retained, fill `bucket` (for example, `regions` or
`predictors`) and `entry`, a schema 2.8 entry containing exactly one mapped
finding. Leave `entry: null` for unresolved proposals. This is a maintainer-facing
JSON mapping step, not yet a point-and-click mapping interface. Use the original
PDF and `review.html` to establish the claim, target, method, sample, timing and
limitations; schema validity alone cannot establish scientific accuracy.

Preview the completed mappings, then create held drafts:

```bash
.venv/bin/python kb.py convert --mapping _compare/my-batch/mapping.json
.venv/bin/python kb.py convert --mapping _compare/my-batch/mapping.json --execute
```

The converter validates every selected entry before writing. It copies the
proposal's original source quotations and pages, attaches its full audit and
study frame, strips approval stamps, and adds a pending source-check mark.
Changed review files and conflicting existing drafts stop conversion. Unmapped
proposals remain in the mapping file; conversion does not declare a paper complete.
The command neither publishes drafts nor replaces existing KB findings.

Source mapping can add `additional_evidence` entries with an existing `source_id`
and schema `supports` category. For a table omitted from the passage inventory,
`pdf_evidence` supplies page, section, quote and supports alongside `source_pdf`:
conversion checks the reviewed PDF hash and exact page text. This text check does
not replace inspecting the table layout. Record agent source checks separately
from human approvals in `logs/source-review/`; a checked subset must not be called
a complete paper review. Use `draft_suffix` to distinguish different outcomes
mapped from the same proposal to the same entry.

New drafts can then enter the normal portal publication workflow described in
[PORTAL.md](PORTAL.md). Resolve the source-check mark only after the checks below;
automatic re-extraction is not a substitute for that check. Approval and canonical
publication remain separate steps. Existing approved findings must be reconciled
against the new source-verified findings, not blindly appended as duplicates.

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

For imaging and clinical reports, also check the relationship's intended use:

- Is the feature a patient's lesion, tract measure or disconnectome, or a
  normative atlas/tract used to interpret it? Preserve the atlas, space and method.
- Does the outcome describe status at an assessment, observed change, treatment
  response or model performance? Preserve the timing of both imaging and outcome.
- Is a personal factor a tested association, a model input, an adjustment variable,
  an eligibility condition or merely a sample characteristic? Roles can differ
  between analyses in the same paper.
- Does an apparent association remain after the relevant adjustment? Keep nulls,
  conditional effects, population restrictions and unresolved source conflicts
  attached. Feature importance is not an individual lesion effect.

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


## Compatibility with older runs

The `analyses` extraction profile and its inventory reconciliation remain
available to inspect and recover existing runs. `kb.py review` detects the saved
profile; older reviews can report `requires_visual_review`. These outputs are
also unapproved. Do not mix profiles within a run or relabel earlier outputs as
having passed the relationship workflow. New runs default to `relationships`; the explicit option above records the choice
clearly. To resume an older analysis-profile batch, explicitly use `--profile analyses`.

## Clinical interpretation in the explorer

New core drafts receive a presentation-only interpretation aid from their saved
exposure, outcome, method, qualifications and source references. It explains the
role of the result, the kind of scan feature or patient/task information it could
relate to, and limits on its use. It makes no new model call and does not change
source findings, approval, evidence scores or the extraction run.

These are rule-based, unreviewed reading aids, not new findings or patient-specific
clinical recommendations. They distinguish lesion location, tissue measures,
reference-template overlap, patient diffusion, network graph measures, functional
imaging, complete prediction models and non-imaging factors. Missing atlas/metric
information stays unresolved; a similar anatomical label is not an established
cross-atlas match. Personal factors (age, sex and post-stroke timing) have their own explorer
category. Other non-imaging factors are presented without anatomical meaning.
These display categories preserve the original extraction metadata; they do not
change an active run or create an atlas mapping.

The explorer applies this layer when it loads new drafts. A local preview remains
a fixed snapshot until refreshed; re-extraction is not required. Full source
qualifications and review records remain on the finding page. Human review of the
interpretation and its measurement compatibility is required before clinical use.


## Reviewing the current draft release

The explorer opens the current findings, including unapproved drafts. The
approved-only export remains separate for software that requires approved
evidence; it may be empty while the replacement findings await approval.
The previous findings and their review history are preserved in the GitHub tag
[archive/pre-core-drafts-2026-11-20](https://github.com/micmas/stroke-aphasia-kb/tree/archive/pre-core-drafts-2026-11-20).

Use the review portal's Drafts page to check sources and submit decisions.
Each decision is bound to the displayed draft version. Publishing another
snapshot does not overwrite edits, restore rejected drafts, or repeat promoted
findings. Held and failed candidates are not published.

During an active local run, publish from a separate checkout. Copy only completed
drafts with scripts/snapshot_checked_drafts.py --run-dir <source-check-output>
--source-repo <conversion-output> --destination <publishing-checkout>, then
regenerate the exports, check them and commit. The publication manifest records
the source hashes; changed versions are reported for reconciliation rather than
silently replacing a reviewed draft. This step does not start models.
