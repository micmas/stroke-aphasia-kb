# Stroke aphasia knowledge base

Traceable research findings about language, recovery and intervention after
stroke. Each finding connects a claim to its source paper, study context and
supporting evidence.

[Browse the evidence](https://aphasia-kb.app/) ·
[Contribute](CONTRIBUTING.md) · [Run locally](docs/HOWTO.md)

The knowledge base supplies evidence to [CALMaR](https://github.com/micmas/calmar).
It supports research interpretation; group-level associations do not establish
an individual patient's deficit, prognosis or treatment response.

## Use the knowledge base

The public explorer provides findings, source references and coverage information.
You do not need to install models to read the evidence. Contributors can screen
papers and review existing findings through the
[review portal](https://review.aphasia-kb.app/).

For a local checkout:

```bash
git clone https://github.com/micmas/stroke-aphasia-kb.git
cd stroke-aphasia-kb
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python kb.py --help
```

Use **`kb.py`** for routine preparation, extraction, review and inspection. The
[workflow guide](docs/HOWTO.md) explains the steps; the
[command reference](docs/COMMANDS.md) lists the supported entry points.

## From paper to finding

1. Select and register the paper, then verify its main PDF.
2. Extract independently with two local models, preserving source evidence and
   both original outputs. Long papers can be processed in bounded source sections.
3. Reconcile against the source with a separate local reviewer, recording
   corrections, omissions and unresolved issues.
4. Verify tables and figures, resolve source questions, and map findings to KB
   entries before applying the approval rules.

Dual extraction has shown complementary coverage in source audits, but a measured
accuracy advantage has not been established; both models can share errors.

**Current implementation:** extraction and local text reconciliation are
available. Visual verification and mapping of reconciled inventories to KB drafts
are separate review tasks, not an automated end-to-end process. Successful model
calls do not approve findings. Existing published findings retain their recorded
provenance until reviewed replacements are ready.

Only the main PDF is supplied to extraction; supplementary files are excluded.
Original outputs and failed attempts are preserved. Models run locally through
Ollama. PDFs stay out of Git and may be shared through the project-controlled
portal only under its access and licence rules.

## Documentation

| Need | Reference |
|---|---|
| Prepare, extract and review papers | [Workflow](docs/HOWTO.md) |
| Find a command | [Commands](docs/COMMANDS.md) |
| Configure local models | [Models](docs/MODELS.md) |
| Understand approval and accountability | [Governance](docs/GOVERNANCE.md) |
| Understand entry fields and evidence | [Schema](docs/schema.md) |
| Select papers or use the review portal | [Screening](docs/SCREENING.md) · [Portal](docs/PORTAL.md) |
| Integrate the export or maintain the code | [Developer guide](docs/development/README.md) |

## Repository layout

- `regions/`, `impairments/`, `predictors/`, `reviews/`, `ingredients/` and other
  entry collections hold knowledge-base data; `drafts/` holds pending KB findings.
- `citations.md`, `screening/` and `atlas_mapping/` hold source and mapping records.
- `papers/` holds local PDFs; `_compare/` holds local extraction and review runs.
  Neither is committed.
- `kb.py` is the user command. `scripts/` contains its implementation and
  maintainer tools; `tests/` checks their behavior.
- `explorer/`, `portal/`, `export/` and `js/` support browsing, collaboration and
  integration. `logs/` preserves the audit trail.

Code is [MIT licensed](LICENSE). Source papers retain their own licences.
