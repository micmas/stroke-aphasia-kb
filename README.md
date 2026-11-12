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

Start with `kb.py` and this README. The remaining folders serve four purposes:

| Purpose | Folders |
|---|---|
| Evidence and sources | `regions/`, `impairments/`, `predictors/`, `reviews/`, `ingredients/`, `atlas_mapping/`, `screening/` |
| Processing and quality checks | `scripts/`, `tests/`, `drafts/` |
| Websites and integration | `explorer/`, `portal/`, `js/`, `export/` |
| Documentation and accountability | `docs/`, `logs/` |

`citations.md` is the bibliography. `papers/` contains local PDFs and `_compare/`
contains local model runs; neither belongs in Git. Generated diagnostics and
retired work belong outside the checkout, not alongside product files.

### Clean baseline

The previous draft queue was retired on 12 November 2026. `drafts/` starts empty;
new drafts must come from source-reviewed extractions through the documented
workflow. Previously approved KB entries retain their original evidence and
approval provenance; the repository reset does not certify them as newly
extracted or newly verified. They remain subject to source-reviewed replacement.

The complete pre-reset history and retired drafts were backed up before replacing
Git history. `logs/baseline/2026-11-12.json` records the retired files and hashes;
reviewer material is retained under `logs/baseline/reviewer-material/` for the
replacement review. This is an audit archive, not another draft queue. Source,
screening, approval and correction records remain part of the product.

Code is [MIT licensed](LICENSE). Source papers retain their own licences.
