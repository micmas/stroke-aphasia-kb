# Commands

Run from the repository root with `.venv/bin/python kb.py COMMAND`.
For setup and the complete procedure, follow [HOWTO](HOWTO.md).

| Command | Purpose | Writes or runs models? |
|---|---|---|
| `sync` | Download portal PDFs and publish completion receipts | Downloads and Git sync; no models or PDF intake |
| `status --jobs` | Show active KB model processes | Read-only |
| `prepare` | Select registered papers and freeze their source manifest | Writes manifest; no inference |
| `extract` | Two independent local extractions | Preview by default; `--run` starts inference |
| `review` | Independent source reading and reconciliation | Preview by default; `--run` starts inference |
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

Sync fetches and fast-forwards main, downloads uploaded PDFs, then commits and
pushes only import records and their register links. It never runs extraction,
review, intake/OCR, or approval. Other local edits are not committed. Staged edits
or unpublished import records must be resolved first. A changed existing PDF is
preserved for manual review. Failed downloads stay pending. If a push fails,
the local commit remains: resolve the Git error and rerun sync.

Sync can run alongside model processing. If incoming code changes would affect
an active job, it stops before updating the checkout; retry after the job finishes.
New downloads still need source verification/preparation before extraction.

`extract --run` and `review --run` refuse to start while another detected KB model
job is active. Add `--wait` to wait in the terminal and start when idle; keep that
terminal open. Ctrl-C cancels a waiting command. This is not a persistent scheduler.
The shared lock protects commands started through `kb.py`; older direct script
jobs are detected, but external model apps and later direct script launches are
not controlled. Use `kb.py` for new processing jobs.

## Typical batch

```bash
.venv/bin/python kb.py prepare --papers Paper2024 Another2025 --output _compare/my-batch/manifest.json
.venv/bin/python kb.py extract --manifest _compare/my-batch/manifest.json --output-dir _compare/my-batch/extraction
.venv/bin/python kb.py review --run-dir _compare/my-batch/extraction --output-dir _compare/my-batch/review --model YOUR_REVIEW_MODEL --limit 3
```

Replace paper keys and reviewer model with your selections. Add `--run` to
extraction or review only after checking the preview. Finish or stop extraction
before starting local review. See [HOWTO](HOWTO.md) for source preparation,
segmentation, recovery, visual checks and approval.

## Maintainer operations

Screening, intake, approval, export, portal administration and migration are
specialist operations documented in the [developer guide](development/README.md),
[screening guide](SCREENING.md), [portal guide](PORTAL.md) and
[governance policy](GOVERNANCE.md). The modules under `scripts/` remain available
for those operations and existing integrations; they are not alternative
recommended extraction workflows.
