# Stroke aphasia knowledge base

A curated literature base linking stroke lesion locations to aphasia
impairments, therapy responses and recovery predictors. Every finding is
one claim from one paper, with the verbatim passages that support it, so
anyone can open the paper and check. Entries are markdown files with
YAML frontmatter: readable by people, loaded by code.

[CALMaR](https://github.com/micmas/calmar) uses it to turn a lesion mask
into a cited clinical interpretation, and the
[CALMaR webapp](https://webapps.neurodesk.org/calmar/) ships an export of
it. The `explorer/` folder is a static site for browsing the findings,
published with GitHub Pages on every push to `main`
([`docs/EXPLORER.md`](docs/EXPLORER.md)).

**Status (October 2026):** 72 entries, 262 findings, 55 papers cited.
`python scripts/kb_status.py` prints the current numbers.

## What is in an entry

Each entry describes one region, impairment, therapy, predictor or
review article, and holds a list of findings. A finding records the
claim, its direction and relationship (causal, correlational, treatment
response, …), the method, sample and statistics, the confounders the
authors did and did not control, how the paper defined the region, the
extractor's confidence, and the source passages that back it. Who
approved it, when, and at which review tier is recorded with it. The
full field list is [`docs/schema.md`](docs/schema.md) and a worked
example is
[`docs/examples/`](docs/examples/region_ifg_opercularis_fridriksson2018.md).

Nothing enters the approved folders without a second reading of the
paper, by a person or (for routine findings) by an independent local
model, and a named person is accountable for all of it. That policy is
[`docs/GOVERNANCE.md`](docs/GOVERNANCE.md). Every model step runs on
your own machine through Ollama; paper text never leaves it.

## Repository layout

```
regions/ impairments/ therapies/ predictors/ reviews/ ingredients/
                      approved entries — what CALMaR and the webapp read
drafts/               entries waiting for review
citations.md          bibliography: one block per paper (@Key, DOI, status)
screening/            the systematic-search register (what was searched and decided)
atlas_mapping/        how atlas labels map onto KB regions (data + its README)

scripts/              all the Python tooling (see docs/COMMANDS.md)
tests/                tests for the tooling
docs/                 how-tos, policy, schema and the model guide (index below)
logs/                 append-only audit trail: extraction_log.md, auto_review/

export/               JSON export of the approved entries, for the webapp and explorer
js/                   kb-evidence.js, the JavaScript port of the evidence logic
explorer/             the static explorer site (published by GitHub Pages)

models.yaml           which local Ollama model each role uses
requirements.txt      Python dependencies of scripts/
papers/               source PDFs — local only, never committed (copyright)
```

## Documentation

| If you want to… | Read |
|---|---|
| add a paper and get it to an approved entry | [`CONTRIBUTING.md`](CONTRIBUTING.md), then [`docs/HOWTO.md`](docs/HOWTO.md) |
| look up a command and its options | [`docs/COMMANDS.md`](docs/COMMANDS.md) |
| understand the entry format | [`docs/schema.md`](docs/schema.md) |
| know who may approve what | [`docs/GOVERNANCE.md`](docs/GOVERNANCE.md) |
| find papers systematically (PRISMA) | [`docs/SCREENING.md`](docs/SCREENING.md) |
| choose or benchmark a local model | [`docs/MODELS.md`](docs/MODELS.md) and `models.yaml` |
| understand the export, the JS port and the explorer | [`docs/EXPLORER.md`](docs/EXPLORER.md) |
| see the instructions the extractor model is given | [`docs/EXTRACTION_SKILL.md`](docs/EXTRACTION_SKILL.md) |

## Quick start

```bash
git clone https://github.com/micmas/stroke-aphasia-kb.git
cd stroke-aphasia-kb
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

python scripts/kb_status.py                 # what is in the KB
python scripts/aphasia_kb.py --check drafts/   # validate entries
python scripts/promote.py --list            # what needs a reviewer
```

Extracting and reviewing papers needs a local model:
`ollama serve && ollama pull gemma4:26b`, then `python scripts/model_config.py`
to confirm the roles in `models.yaml` resolve. The whole route from a
PDF to an approved entry is in [`docs/HOWTO.md`](docs/HOWTO.md).

## How the other repositories use it

| Consumer | How |
|---|---|
| [CALMaR](https://github.com/micmas/calmar) | git submodule `stroke-aphasia-kb/`, pinned to one commit. Its report code imports `scripts/aphasia_kb.py`, `scripts/aphasia_rules.py` and `scripts/atlas_mapping.py`. After a KB push, CALMaR bumps the pointer: `git submodule update --remote stroke-aphasia-kb && git add stroke-aphasia-kb && git commit`. |
| [CALMaR webapp](https://github.com/neurodesk/webapps) (`apps/calmar`) | a JSON export written by `scripts/export_webapp.py`; `apps/calmar/scripts/sync_kb.py --kb <this checkout>` runs it and records the KB commit. Also vendors `js/kb-evidence.js`. |

This repository is the knowledge base's only home: entries, scripts and
policy are edited and committed here, never in a copy. If you find
yourself editing `calmar/stroke-aphasia-kb/`, commit and push from
there (it is a clone of this repository), then bump the pointer in
calmar.

## Licence

MIT, see [`LICENSE`](LICENSE). Source PDFs are not redistributed;
`citations.md` carries the DOI of every paper so you can fetch it
through your own access.
