# The explorer, the export and the JavaScript port

A curated, source-traceable literature base linking stroke lesion
locations to aphasia impairments, therapy responses and recovery
predictors. Every finding is one claim from one paper and carries the
verbatim passages that support it, so anyone can open the paper and
check. Entries are markdown files with YAML frontmatter, readable by
people and loaded by code.

This repository is the KB's home. It is consumed by three things:

| Consumer | How |
|---|---|
| [CALMaR](https://github.com/micmas/calmar) notebook pipeline | git submodule at `stroke-aphasia-kb/`; imports `aphasia_kb.py`, `aphasia_rules.py`, `atlas_mapping` |
| [CALMaR webapp](https://webapps.neurodesk.org/calmar/) (neurodesk/webapps) | vendors `js/kb-evidence.js` and `export/stroke-aphasia-kb.json` at a pinned commit |
| The explorer (this repo, GitHub Pages) | `explorer/` reads `export/stroke-aphasia-kb.json` in the browser |

The move from `calmar/aphasia-kb` happened in October 2026 (history
preserved; `tools/migrate-from-calmar.sh` is how). This repository is
now the only place the KB is edited; calmar pins it as a submodule and
the webapp ships an export of it. See `README.md`, *Where the knowledge
base lives*.

## Layout

```
stroke-aphasia-kb/
├── scripts/export_webapp.py               KB → export/stroke-aphasia-kb.json (+ parity fixtures)
├── export/
│   ├── stroke-aphasia-kb.json             the one JSON every JavaScript consumer reads
│   └── kb-parity.json                     what the Python answers for synthetic lesions
├── js/
│   ├── kb-evidence.js                     JavaScript port of the evidence logic (no dependencies)
│   └── test/kb-evidence.test.js           the port against export/kb-parity.json
├── explorer/                              static site: browse findings, evidence matrix, papers, entries
└── .github/workflows/pages.yml            publishes explorer/ + export/ + js/ to GitHub Pages
```

The entries, the bibliography and the Python tooling that produce the
export are described in the repository [`README.md`](../README.md).

## The explorer

A static page with no backend: it loads the export and renders

- an **overview** — counts, review provenance, regions and impairments by
  number of findings, region entries a lesion cannot reach;
- a **findings browser** — facets for entry type, relationship, strength,
  review provenance, recovery stage, method, design, evidence class,
  direction, entry, target and paper, plus full-text search over claims
  and quotes; every filter state is a URL;
- an **evidence matrix** — region × impairment (also therapy ×
  impairment, predictor × outcome, region × region), cells coloured by
  number of findings, click-through to the findings;
- **papers** — the bibliography with one page per paper listing its
  findings in page order, to spot-check an extraction against the PDF;
- **entry pages** — one per region, impairment, therapy or predictor,
  including the atlas mapping that lets a lesion reach a region and the
  findings that target the entry from elsewhere;
- **finding permalinks** — `#/finding/<entry id>/<finding id>`, which the
  CALMaR report can link to;
- **coverage** — the screening register (`SCREENING.md`): a PRISMA 2020
  flow diagram whose every box opens the candidates it counts, the
  exclusion reasons, how far each evidence gap has been searched,
  screened, included and extracted, the searches that were run, and a
  faceted table of every candidate paper (stage, reason, source, search,
  gap, decider); the Papers page shows each paper's screening stage and
  the paper page its screening record. The counts come from the export
  (`export_webapp.screening`, computed in Python).

Run it locally from the repository root (the page fetches
`../export/stroke-aphasia-kb.json`):

```bash
npm run explorer          # python3 -m http.server 8765
open http://localhost:8765/explorer/
```

To look at an export that is not published — for example one that
includes drafts — use **Open a local export** in the page header, or pass
`?kb=<url>`. Nothing is uploaded; the file is read in the browser.

Colours follow the CALMaR palette (`calmar/docs/CALMAR_PALETTE.md`): grape
for headings and the person, blue for data and the model, cyan (fill only,
always labelled) for approved/canonical, pink for attention, platinum for
surfaces.

## Regenerating the export

```bash
python3 scripts/export_webapp.py --out export/stroke-aphasia-kb.json --fixtures export --indent 1
python3 scripts/export_webapp.py --include approved,in_review,draft --out export/stroke-aphasia-kb-drafts.json
npm test                  # the JavaScript port against the fresh fixtures
# or all copies at once (explorer, webapp, notebook): python3 scripts/snapshot.py --no-commit

The explorer's **Findings** switch (`?kb=drafts`) shows the second export:
approved findings plus unreviewed drafts, with a warning on the overview
and a *Status* facet to separate them.
```

Commit `export/` with the entries it was built from: the webapp pins this
repository at a commit and reads the export at that commit, and
`version.commit` / `version.contentDigest` inside the JSON are what the
report's provenance line shows. The Pages workflow re-runs the export on
every push to `main` so the explorer never lags the entries.

## The JavaScript port

`js/kb-evidence.js` re-implements, without dependencies, the parts of the
Python that turn measured damage into cited findings
(`aphasia_kb.location_findings` / `interpret_damage` /
`interpret_therapies`, `atlas_mapping.unit_damage` / `region_damage`,
the display rules of `aphasia_rules`). `npm test` replays
`export/kb-parity.json` through it and fails on any divergence, so the
Python stays the reference and the port stays honest. The CALMaR webapp
vendors this file; it does not keep a copy of its own.

## Licence

MIT (see `LICENSE`). Source PDFs are never redistributed; `citations.md`
carries a DOI for every key.
