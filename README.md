# Stroke aphasia knowledge base

What does the research literature say about a person's aphasia, given
where their stroke is? This knowledge base collects the answers, one
claim at a time, with the exact passage of the paper each claim comes
from. Anyone can open the paper and check.

It feeds [CALMaR](https://github.com/micmas/calmar), which turns a
lesion mask into a cited interpretation, and the
[CALMaR webapp](https://webapps.neurodesk.org/calmar/). You can browse it
yourself in the [explorer](https://micmas.github.io/stroke-aphasia-kb/explorer/).

**Where we are (November 2026):** 73 entries, 269 findings, 60 papers.
The [explorer's Overview](https://micmas.github.io/stroke-aphasia-kb/explorer/)
shows today's numbers.

## Where to go

| You want to… | Go to |
|---|---|
| read the evidence | the [explorer](https://micmas.github.io/stroke-aphasia-kb/explorer/): findings, evidence matrix, papers, coverage |
| help, without installing anything | the explorer's **Get involved** page, then the review portal ([docs/PORTAL.md](docs/PORTAL.md)) |
| contribute from a checkout: review drafts, add papers | [CONTRIBUTING.md](CONTRIBUTING.md), then [docs/HOWTO.md](docs/HOWTO.md) |
| look up a command | [docs/COMMANDS.md](docs/COMMANDS.md) |
| understand how entries are written | [docs/schema.md](docs/schema.md), with a [worked example](docs/examples/region_ifg_opercularis_fridriksson2018.md) |
| know who decides what goes in | [docs/GOVERNANCE.md](docs/GOVERNANCE.md) |
| see how papers are found and chosen | [docs/SCREENING.md](docs/SCREENING.md) |
| choose a local model | [docs/MODELS.md](docs/MODELS.md) |
| build on the export or the JavaScript port | [docs/EXPLORER.md](docs/EXPLORER.md) |

## How it works, in short

An **entry** is one brain region, impairment, therapy, recovery
predictor or review article. It holds **findings**: each one a single
claim from a single paper, with the paper's own words to back it, the
method and sample, and how sure the extractor was.

A language model running on the maintainer's own computer reads each
PDF and writes draft findings: currently Gemma 4 31B (`gemma4:31b-it-q8_0`)
through Ollama. A person, or for routine findings a second, independent
local model, currently Gemma 4 26B (`gemma4:26b`), then re-reads the
paper and agrees or not. The choice of models and the tests behind it
are in [docs/MODELS.md](docs/MODELS.md). Only after that does a finding become part of the
knowledge base, and a named person is accountable for it. That is the
whole idea; the rules are in [docs/GOVERNANCE.md](docs/GOVERNANCE.md).

Each finding records which model wrote it. Most of the entries approved
before October 2026 were drafted by Claude models over an API, a route
the project no longer uses; they are marked as pre-policy and are being
re-reviewed against the papers.

Papers never leave the machine they are read on. The repository holds
findings, quotations and DOIs; never the PDFs.

## Quick start

```bash
git clone https://github.com/micmas/stroke-aphasia-kb.git
cd stroke-aphasia-kb
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

python scripts/kb_status.py                     # what is in the KB
python scripts/promote.py --list                # drafts waiting for a reviewer
python scripts/review_app.py                    # review a draft beside its paper
```

Extracting new papers needs the local models: `ollama serve`, then
`ollama pull gemma4:31b-it-q8_0` (the extractor; needs about 48 GB of
RAM, otherwise `gemma4:26b`) and `ollama pull gemma4:26b` (the
reviewer). `python scripts/model_config.py` confirms both resolve.
[docs/HOWTO.md](docs/HOWTO.md) walks from a PDF to an approved entry.

## What is where

```
regions/ impairments/ therapies/ predictors/ reviews/ ingredients/
                      the approved entries (what CALMaR reads)
drafts/               entries waiting for review
citations.md          one block per paper: key, DOI, status
screening/            the systematic-search register
atlas_mapping/        atlas labels → KB regions

scripts/              the tooling (docs/COMMANDS.md)
tests/                its tests
docs/                 guides, policy, schema, figures
logs/                 the audit trail: what was extracted, reviewed, applied

export/               JSON exports for the webapp and the explorer
js/                   the JavaScript port of the evidence logic
explorer/             the public site (GitHub Pages)
portal/               the private review portal (Cloudflare Pages)

models.yaml           which local model does which job
papers/               the PDFs — on your machine only, never committed
```

## The other repositories

[CALMaR](https://github.com/micmas/calmar) includes this repository as
a git submodule pinned to one commit. After a change lands on `main`,
bump the pointer there:

```bash
git submodule update --remote stroke-aphasia-kb
git add stroke-aphasia-kb && git commit -m "KB: bump"
```

The [webapp](https://github.com/neurodesk/webapps) (`apps/calmar`)
takes a JSON export: `apps/calmar/scripts/sync_kb.py --kb <this checkout>`.

Edit entries, scripts and policy here, not in a copy. If you find
yourself inside `calmar/stroke-aphasia-kb/`, commit and push from there
(it is a clone of this repository), then bump the pointer.

## Licence

MIT ([LICENSE](LICENSE)). PDFs are not redistributed; `citations.md`
has the DOI of every paper so you can fetch it through your own access.
