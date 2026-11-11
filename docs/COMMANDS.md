# Commands

Run from the repository root with `.venv/bin/python kb.py COMMAND`.
For setup and the complete procedure, follow [HOWTO](HOWTO.md).

| Command | Purpose | Writes or runs models? |
|---|---|---|
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
