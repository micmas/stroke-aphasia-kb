# The explorer, the export and the JavaScript port

The explorer is the public face of the knowledge base: a website,
rebuilt on every push, where anyone can browse the findings and follow
each one back to its paper and page. It has no server; it is a page that
reads a JSON export of the KB in the browser. The same export feeds the
CALMaR webapp, through a small JavaScript library that re-implements the
evidence logic. This page covers those three pieces.

**Live site:** https://micmas.github.io/stroke-aphasia-kb/explorer/

## What the explorer shows

**Overview**: counts, who reviewed what, regions and impairments by
number of findings (grey bars for regions findings point to that have
no entry yet), region entries a lesion cannot reach, and where to go
next.

**Findings**: every finding with its claim, passages, review record and
links. Filters for entry type, relationship, strength, status, review
provenance, recovery stage, method, design, evidence class, paper
licence, direction, entry, target, paper and therapy, plus full-text
search over claims and quotes. Every filter state is a URL you can send
to someone. The **Findings** switch in the header shows the approved KB
or the approved KB plus the drafts still under review.

**Matrix**: region × impairment (also therapy × impairment, predictor ×
outcome, region × region), each cell the number of findings linking the
two, clicking through to them.

**Papers**: the bibliography, with a page per paper listing its findings
in page order, its licence, and a link to the annotated PDF (public for
Creative-Commons papers, in the review portal for the rest). A
**Licences** page lists every paper by licence category.

**Entry pages**: one per region, impairment, therapy, predictor or
review article, with the atlas mapping that lets a lesion reach a region
and the findings that target the entry from elsewhere. **Finding
permalinks** (`#/finding/<entry>/<finding>`) are what the CALMaR report
links to.

**Coverage**: the screening register as a PRISMA flow whose boxes open
the candidates they count (hover the database box for the records per
question), the exclusion reasons, how far each evidence gap has got, the
searches that were run, and a table of every candidate paper.

**Models**: which local model drafts the findings, which one checks them,
and the latest comparison behind that choice: fabricated quotes, schema
issues, how many of the known links each model found, over-claiming and
speed, model by model and paper by paper. Each model's block also says
where it comes from: developer, release, licence, architecture, the
original weights and the Ollama tag it was pulled as (`model_sources.yaml`,
curated), and what was installed on the publishing machine. The page reads
`export/model-benchmark.json`, which `benchmark_models.py --publish`
writes (numbers and ids only, no paper text); `--refresh-sources`
updates only the provenance.

**Get involved**: the five levels at which a person can take part, from
reading to building, with what each needs. **Review ↗** opens the
private review portal ([PORTAL.md](PORTAL.md)).

## Running it locally

```bash
npm run explorer
```

then http://localhost:8765/explorer/ — the page reads
`export/stroke-aphasia-kb.json` from the repository. To look at an
export that is not published, use **Open a local export** in the header
or pass `?kb=<url>`; nothing is uploaded.

## The export

```bash
python3 scripts/export_webapp.py --out export/stroke-aphasia-kb.json --fixtures export --indent 1
python3 scripts/export_webapp.py --include approved,in_review,draft --out export/stroke-aphasia-kb-drafts.json
npm test
```

The first line writes the approved KB plus the parity fixtures
(`export/kb-parity.json`, what the Python answers for a few synthetic
lesions); the second writes the approved + drafts export the explorer's
switch and the portal use; `npm test` replays the fixtures through the
JavaScript port. `snapshot.py` does all of this and commits.

Commit `export/` together with the entries it was built from: the webapp
pins this repository at a commit and reads the export at that commit,
and `version.commit` / `version.contentDigest` inside the JSON are what
the report's provenance line shows. The Pages workflow re-runs the export
on every push to `main`, so the live explorer never lags the entries.

The export also carries the screening register (computed in Python by
`export_webapp.screening`), the licences, and the portal's address, so
the explorer can link public PDFs and the Get-involved page can point at
the portal.

## The JavaScript port

`js/kb-evidence.js` re-implements, without dependencies, the Python that
turns measured damage into cited findings (`aphasia_kb.location_findings`
/ `interpret_damage` / `interpret_therapies`, `atlas_mapping.unit_damage`
/ `region_damage`, the display rules in `aphasia_rules`). `npm test`
replays `export/kb-parity.json` through it and fails on any divergence,
so the Python stays the reference. The CALMaR webapp vendors this file
rather than keeping a copy of its own.

## Files

```
scripts/export_webapp.py          KB → export/*.json (+ parity fixtures)
export/stroke-aphasia-kb.json     the approved KB, read by every JavaScript consumer
export/stroke-aphasia-kb-drafts.json   approved + drafts (explorer switch, review portal)
export/kb-parity.json             the Python's answers for synthetic lesions
export/model-benchmark.json       the latest model comparison (benchmark_models.py --publish), for the Models page
js/kb-evidence.js, js/test/       the port and its parity test
explorer/                         index.html, app.js, kb-index.js, styles.css
.github/workflows/pages.yml       publishes explorer/ + export/ + js/ to GitHub Pages
```

The CALMaR notebook has a page of its own at https://calmar.aphasia-kb.app
(`scripts/build_notebook_page.py`, `explorer/notebook.css`; published by the
`calmar` repository whenever a notebook is pushed there — see
[COMMANDS.md](COMMANDS.md)). The explorer links to it from the Overview and
the footer once the page exists.

Colours follow the CALMaR palette: grape for headings and the person,
blue for data and the model, cyan for approved, pink for attention.
