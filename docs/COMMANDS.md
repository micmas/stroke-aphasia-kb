# Commands

Run from the repository root with `.venv/bin/python kb.py COMMAND`.
For setup and the complete procedure, follow [HOWTO](HOWTO.md).

| Command | Purpose | Writes or runs models? |
|---|---|---|
| `sync` | Download portal PDFs and publish completion receipts | Downloads and Git sync; no models or PDF intake |
| `intake` | Prepare PDFs already downloaded | Preview by default; `--execute` renames, checks, OCRs and syncs PDFs; no models |
| `sync --intake` | Download, prepare PDFs and publish metadata together | Writes source files and metadata; no models |
| `status --jobs` | Show active KB model processes | Read-only |
| `prepare` | Select registered papers and freeze their source manifest; hold PDFs over 50 pages | Writes manifest; no inference |
| `extract` | Two independent local extractions | Preview by default; `--run` starts inference |
| `review` | Generate an incomplete source-review aid; human verification required | Preview by default; `--run` starts inference |
| `source-check` | Check and recover reviewed candidates against the main PDF | Preview by default; `--run` starts mapper and checker; `--convert` writes held drafts |
| `convert` | Convert explicit source-checked mappings | Preview by default; `--execute` writes held drafts; no models |
| `status` | Inspect KB content and provenance | Read-only |
| `drafts` | List existing KB drafts | Read-only |
| `inspect --draft PATH` | Open a KB draft beside its source | Interactive review workbench; edits are logged |
| `validate --check PATH` | Validate KB entries or drafts | Checks files |

Use `COMMAND --help` for its full options. `validate` also exposes the KB query
options described by its help. Run outputs are separate from `drafts/`: neither
extraction nor reconciliation approves or publishes findings.

## Portal downloads and busy models

```bash
.venv/bin/python kb.py sync
.venv/bin/python kb.py status --jobs
```

To include source preparation in the same action, when the current processing job
has finished:

```bash
.venv/bin/python kb.py sync --intake
```

Add `--wait` to wait in the terminal for the current KB processing job. Intake can
change PDF bytes and filenames, so it uses the same guard as extraction/review.
Prepare a fresh extraction manifest after intake. The combined command publishes
both download receipts and intake metadata. If preparation or portal sync fails,
local changes remain for inspection; it does not commit or push a partial result.
For PDFs already downloaded, `kb.py intake` previews and `kb.py intake --execute`
applies preparation (with the existing intake options). Standalone intake leaves
its metadata changes for you to commit; use the combined command for one-step
publication. Neither command permits the old `--extract` shortcut.

Plain sync fetches and fast-forwards main, downloads uploaded PDFs, then commits and
pushes only import records and their register links. It never runs extraction,
review, intake/OCR, or approval. Other local edits are not committed. Staged edits
or unpublished import records must be resolved first. A changed existing PDF is
preserved for manual review. Failed downloads stay pending. If a push fails,
the local commit remains: resolve the Git error and rerun sync.

Sync can run alongside model processing. If incoming code changes would affect
an active job, it stops before updating the checkout; retry after the job finishes.
New downloads still need source verification/preparation before extraction.

`extract --run`, `review --run` and `source-check --run` refuse to start while another detected KB model
job is active. Add `--wait` to wait in the terminal and start when idle; keep that
terminal open. Ctrl-C cancels a waiting command. This is not a persistent scheduler.
The shared lock protects commands started through `kb.py`; older direct script
jobs are detected, but external model apps and later direct script launches are
not controlled. Use `kb.py` for new processing jobs.

## Typical batch

```bash
.venv/bin/python kb.py prepare --papers Paper2024 Another2025 --output _compare/my-batch/manifest.json
.venv/bin/python kb.py extract --profile relationships --manifest _compare/my-batch/manifest.json --output-dir _compare/my-batch/extraction
.venv/bin/python kb.py review --run-dir _compare/my-batch/extraction --output-dir _compare/my-batch/review --model YOUR_REVIEW_MODEL --limit 3
```

This is the current relationship source-evidence workflow. Replace paper keys
and reviewer model with your selections. Add `--run` to
extraction or review only after checking the preview. Finish or stop extraction
before starting local review. See [HOWTO](HOWTO.md) for source preparation,
segmentation, recovery, visual checks and approval.

## Extraction options

`--profile relationships` selects the current source-evidence method: two local
models independently classify original passages and transcribe main-paper tables.
It preserves evidence for imaging–outcome relationships, personal factors and
clinical context. It does not automatically create or approve KB findings.
This is already the default; writing it explicitly makes the method clear.
`--profile analyses` is retained for compatibility with older runs, not as the
recommended choice for a new corpus extraction.

| Option | What it does |
|---|---|
| `--manifest PATH` | Reads the frozen paper list, PDF checksums and source metadata created by `kb.py prepare`. |
| `--output-dir PATH` | Saves this batch's evidence, model responses and progress. Use a fresh folder for a changed method or configuration. |
| `--profile relationships` | Selects the current source-evidence extraction method (the default). |
| `--run` | Starts local model calls. Without it, only previews the list. |
| `--continue-on-error` | Preserves a failed paper's output and continues with the next paper. It does not fix or approve failures. |
| `--models MODEL_A MODEL_B` | Overrides the default pair: `gemma4:31b` and `qwen3.8:27b`. |
| `--retry-failed` | Archives and retries incomplete or failed paper attempts after inspection; completed pairs are reused. |
| `--wait` | Waits in this terminal for another detected KB model job to finish. |
| `--max-output-tokens N` | Advanced output allowance. The relationship method also applies smaller per-task caps; this is not a paper-length or input-context limit. |

The terminal shows `[X/N] Extract PaperKey`, or `Reuse`, `Skip` or `Failed`.
`X/N` is the paper's position in the full manifest, not the number of successful
extractions or the percentage of processing time elapsed. Repeat the identical
command to resume; with `--continue-on-error`, incomplete attempts remain skipped
until explicitly retried. Do not change model code or prompts during a run.

## Maintainer operations

Screening, intake, approval, export, portal administration and migration are
specialist operations documented in the [developer guide](development/README.md),
[screening guide](SCREENING.md), [portal guide](PORTAL.md) and
[governance policy](GOVERNANCE.md). The modules under `scripts/` remain available
for those operations and existing integrations; they are not alternative
recommended extraction workflows.


## Recover interpretations and prepare drafts

```bash
.venv/bin/python kb.py source-check \
  --run-dir _compare/my-batch/extraction \
  --review-dir _compare/my-batch/review \
  --output-dir _compare/my-batch/source-check \
  --model gemma4:31b --checker-model qwen3.8:27b \
  --limit 3
```

Add `--run` to process the previewed papers. Add `--convert` to create held drafts
for supported findings. Omit `--limit` to cover the complete frozen manifest.
Use `--papers KEY1 KEY2` for selected papers. Existing drafts are preserved.
Use `--recover-from OLD_SOURCE_CHECK_DIR` with a new output folder to reuse saved
mapper responses for fresh checking, rather than repeating their generation.
PDF, review and mapper identity must match. The same command resumes from matching saved checks; changed model, source or
code requires a new output directory. Ctrl-C preserves completed work.

The mapper can recover incorrect interpretations, including useful null results.
A separate model checks the mapping without the mapper's self-ratings. Unresolved
interpretations and invalid mappings remain held. Outputs include attempts,
checker decisions, `mapping.json`, per-paper `status.json` and `batch-status.json`.
Checking candidate findings is not a paper-completeness assessment.

New drafts become visible online when committed and pushed; source checking alone
does not publish them. They remain unapproved until the person reviewing resolves
the source-check mark and applies the approval rules. You can release completed
papers incrementally rather than waiting for the whole corpus.
