# Contributing

You can help by finding errors, screening papers, checking source evidence or
maintaining the code.

## Review evidence without installing anything

Browse the [explorer](https://aphasia-kb.app/) and report a problem with its entry
ID, finding ID and source page. Explain the incorrect claim, missing qualification
or omitted result. The [review portal](https://review.aphasia-kb.app/) lets registered
reviewers screen papers, review existing drafts and supply missing PDFs. See the
[portal guide](docs/PORTAL.md) for access. Review opinions and approval permissions
are separate; the [governance policy](docs/GOVERNANCE.md) defines who may approve.

## Work locally

Install using the [README](README.md), then follow the single
[paper-to-finding workflow](docs/HOWTO.md). Routine commands start with
`.venv/bin/python kb.py`; the [command reference](docs/COMMANDS.md) explains them.

New papers must be screened, registered and matched to the correct main PDF.
Two independent local extractions and a separate source review produce provisional
inventories. Visual verification and mapping into KB drafts remain separate tasks.
Do not treat a successful model run as an approved finding. Supplementary files
are outside the extraction scope.

For existing drafts:

```bash
.venv/bin/python kb.py drafts
.venv/bin/python kb.py inspect --draft drafts/<collection>/<file>.md
.venv/bin/python kb.py validate --check drafts/
```

Keep original outputs and true provenance. Do not relabel older findings as having
passed the new method, or overwrite them merely because a new extraction exists.
The intended endpoint is one consistently reviewed corpus, with pending migration
tracked by processing stage.

## Maintain the project

Use the [developer guide](docs/development/README.md) for implementation,
validation and publication. PDFs stay outside Git. Approved entries change through
the approval tooling under the governance policy. Schema or approval changes must
update both the documentation and the code that enforces them.
