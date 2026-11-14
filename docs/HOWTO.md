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

No hidden retries are performed. Failed/interrupted attempts stay preserved;
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
mapping stage is currently a separate task; there is no automatic conversion from
`proposals.json` to approvable KB drafts.

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
