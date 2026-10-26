# Aphasia knowledge base

A curated, source-traceable literature base linking stroke lesion
locations to aphasia impairments, therapy responses and recovery
predictors. CALMaR uses it to turn a lesion mask into a cited
interpretation. Entries are markdown files with YAML frontmatter,
readable by people and loaded by code.

Every finding is one claim from one paper and carries the verbatim
passages that support it, so anyone can open the paper and check.
Nothing enters the canonical folders without a second reading of that
paper — by a person, or for routine findings by an independent local
model — and a named person is accountable for all of it. That policy is
[`GOVERNANCE.md`](GOVERNANCE.md). Every model step runs on this machine
via Ollama; paper text and patient data never leave it
([`MODELS.md`](MODELS.md)).

## Where the knowledge base lives

**This repository, <https://github.com/micmas/stroke-aphasia-kb>, is the
knowledge base's only home.** It was moved here from the CALMaR
repository's `aphasia-kb/` folder in October 2026 with its full git
history; entries, scripts, governance documents and the extraction log
are edited and committed **here**, never in a copy. Two other
repositories consume it:

| Consumer | How it gets the KB |
|---|---|
| [CALMaR](https://github.com/micmas/calmar) (the Neurodesk notebook pipeline) | a git submodule at `calmar/stroke-aphasia-kb/`, pinned to one commit of this repository. The pipeline's report code imports `aphasia_kb.py`, `aphasia_rules.py` and `atlas_mapping/` from that checkout. After a KB commit is pushed, CALMaR updates its pointer (`git submodule update --remote stroke-aphasia-kb` + commit). |
| [CALMaR webapp](https://webapps.neurodesk.org/calmar/) ([neurodesk/webapps](https://github.com/neurodesk/webapps), `apps/calmar`) | a JSON export of the approved entries written by `export_webapp.py` (`apps/calmar/scripts/sync_kb.py --kb <this checkout>` runs it and records the KB commit in the webapp's manifests), plus a vendored copy of `js/kb-evidence.js`. |

Submodule checkouts are read-only by convention: if you find yourself
editing `calmar/stroke-aphasia-kb/`, commit and push from that directory
(it *is* a clone of this repository), then bump the pointer in calmar.
`EXPLORER.md` describes the export, the JavaScript port and the
GitHub Pages explorer.

**State (October 2026):** 72 entries, 262 findings, 55 papers cited. 26
entries were approved by a named person; 33 were approved before the
governance policy and are tagged `review_tier: legacy` pending
re-review. `python kb_status.py` prints the current numbers.

## Start here

| You want to… | Read / run |
|---|---|
| understand the entry format | [`schema.md`](schema.md) (v2.7), then `examples/region_ifg_opercularis_fridriksson2018.md` |
| find papers systematically and screen them | [`SCREENING.md`](SCREENING.md), then `python screen.py status` |
| take one PDF to an approved entry | [`HOWTO.md`](HOWTO.md) |
| look up any command and its options | [`COMMANDS.md`](COMMANDS.md) |
| know who may approve what | [`GOVERNANCE.md`](GOVERNANCE.md) |
| choose or benchmark a local model | [`MODELS.md`](MODELS.md) and `models.yaml` |
| see what is in the KB and what is thin | `python kb_status.py` |
| check the canonical quotes against the PDFs | `python audit_quotes.py` |
| set up the machine | `pip install -r requirements.txt`, `ollama pull gemma4:26b`, `python model_config.py` |

## How a paper becomes an entry

```
screening/ — screen.py: searches (PubMed, OpenAlex, RIS/CSV imports) → candidates → title/abstract
   │          and full-text decisions by a named person (SCREENING.md); included → citations.md
   ▼
papers/<Key>.pdf
   │  extract.py — local model reads the text layer, writes schema-bound drafts
   ▼
drafts/<bucket>/<id>__<Key>.md          + papers/<Key>_annotated.pdf (annotate_paper.py)
   │  auto_review.py — deterministic checks (reject / defer only), tier classification,
   │                   then an INDEPENDENT model re-reads the PDF and answers seven
   │                   per-finding checks; may approve Tier A only
   ▼
promote.py — a person approves Tier B (therapies, strong claims, new entries, reviews);
             stamps reviewer, tier and a per-finding review block
   ▼
regions/ impairments/ therapies/ predictors/ reviews/ ingredients/      ← what CALMaR queries
   │
extraction_log.md — append-only: EXTRACTED · REJECTED · MODEL-APPROVED · APPROVED · AUDIT
```

Minimal session, from this repository's root with the venv active:

```bash
cp ~/Downloads/1-s2.0-S00939.pdf papers/            # any name
python intake_papers.py --execute                      # rename → strip covers → OCR
python extract.py --pdf papers/Foo2024.pdf
python aphasia_kb.py --check drafts/
python auto_review.py --all --llm-review --require-pdf-match
python review_sheet.py --all --fix-pages                # open drafts/_review/*.html
python promote.py --list                               # what still needs you
python promote.py --approve drafts/<...>.md --reviewer michele
git add -A && git commit -m "Foo2024 extraction"
```

## Layout

```
stroke-aphasia-kb/
├── README.md                  # this file
├── EXPLORER.md                # the export, the JavaScript port and the GitHub Pages explorer
├── requirements.txt           # Python dependencies of the scripts below
├── schema.md                  # YAML frontmatter spec (v2.7) — the data contract
├── SCREENING.md               # protocol: how papers are found and chosen (PRISMA 2020)
├── HOWTO.md                   # procedure: one PDF → approved entry
├── GOVERNANCE.md              # policy: review tiers, model approval, audit, legacy
├── MODELS.md                  # choosing and benchmarking the local models; decision log
├── EXTRACTION_SKILL.md        # the extractor's instruction manual
├── models.yaml                # which Ollama model each role uses (extract / review / rag)
├── citations.md               # bibliography (@Key, DOI, extraction status)
├── extraction_log.md          # append-only audit log
│
│   # ---- finding papers ----
├── screen.py                  # search / import / screen / decide / register — the screening register
├── screening.py               # the register's data contract: derived stages, PRISMA counts, gap coverage
├── screening/                 # searches.yaml, candidates.yaml (tracked); abstracts and sheets (local)
│
│   # ---- building the KB ----
├── intake_papers.py           # the three steps below in one command
├── register_papers.py         # unknown PDF → citations.md entry from its DOI (Crossref)
├── match_papers.py            # rename downloaded PDFs to their citation key (DOI / title)
├── rekey_paper.py             # move drafts/log/PDF from a wrong citation key to the right one
├── verify_dois.py             # check citations.md DOIs against Crossref
├── strip_cover_pages.py       # drop JSTOR / T&F / ProQuest … cover sheets from PDFs
├── batch_ocr.py               # OCR image-only PDFs in papers/
├── extract.py                 # local model: PDF → drafts + annotated PDF
├── annotate_paper.py          # colour-highlight a PDF from a draft's source_passages
├── auto_review.py             # checks, tier classification, independent model review
├── review_sheet.py            # per-draft HTML: every quote shown on its page, graded
├── promote.py                 # the only way into the canonical folders
├── compare_extraction.py      # benchmark a model against entries you already curated
├── audit_quotes.py            # every canonical quote vs its PDF (graded)
├── quote_check.py             # the ONE quote grader the three checkers share
├── kb_status.py               # counts, review provenance, decoder reachability, papers needed
├── model_config.py            # resolves models.yaml / env vars; lists pulled models
├── ollama_client.py           # the one HTTP client to the local Ollama server
├── resource_monitor.py        # GPU/CPU watch during long runs
├── test_review_guardrails.py  # mock-Ollama tests of the review policy (no model needed)
├── neurosynth_bootstrap.py    # scaffold region drafts from Neurosynth meta-analyses
│
│   # ---- using the KB on a lesion ----
├── aphasia_kb.py              # loader + validator + query module
├── phase.py                   # recovery-phase bands (SRRR) + inference from time_post_onset
├── decode_lesion.py           # MNI mask → HarvardOxford overlap + Neurosynth terms
├── aphasia_kb_rag.py          # decode → retrieve → deterministic cited report (+ local narrative)
├── aphasia_rules.py           # stage-mismatch and reporting rules CALMaR's report applies
├── lesion_mapping.py          # v2.7 lesion-mapping design block and cohort inference
├── atlas_mapping.py  atlas_mapping/   # curated KB-region ↔ atlas-label mapping (see atlas_mapping/README.md)
│
│   # ---- what the other repositories consume ----
├── export_webapp.py           # KB → export/stroke-aphasia-kb.json (+ parity fixtures) for the webapp
├── export/                    # the JSON every JavaScript consumer reads, and kb-parity.json
├── js/                        # kb-evidence.js, the JavaScript port of the evidence logic, and its tests
├── explorer/                  # browser explorer over export/ (GitHub Pages)
├── tools/migrate-from-calmar.sh   # how the KB was moved here from calmar/aphasia-kb (historical)
│
│   # ---- canonical content (status: approved; loaded by the KB) ----
├── regions/  impairments/  therapies/  predictors/  reviews/  ingredients/
│
│   # ---- workflow material ----
├── drafts/{regions,impairments,therapies,predictors}/   # extractor writes here
├── auto_review_log/           # per-draft sidecar audit YAML
├── examples/                  # worked example (not loaded)
├── papers/                    # source + annotated PDFs — NOT tracked (copyright)
├── _compare/                  # sandbox extractions and audit CSVs — NOT tracked
└── _neurosynth_cache/         # Neurosynth v7 data — NOT tracked; regenerated
```

## Scripts

| Script | Role | Needs |
|---|---|---|
| `screen.py` | The systematic front end: record a database search (PubMed / OpenAlex live, RIS / CSV import for Scopus and the like) or backfill the bibliography; de-duplicate; let a person screen titles/abstracts and full texts in an HTML sheet, with the local model's opinion shown as a suggestion only; register included papers in `citations.md`; print the PRISMA 2020 numbers and what each evidence gap still needs. Protocol in `SCREENING.md`. | network for search/register; Ollama for `assist` |
| `intake_papers.py` | Download → extractor-ready in one command: `--from ~/Downloads` copies in PDFs that match a cited paper, then the three scripts below run in order and the papers line of `kb_status.py` is printed; `--extract` goes on to `extract.py --batch`. Every step skips what is already done, so re-running is safe. Dry run by default; `--execute` applies. | local / Ollama with `--extract` |
| `verify_dois.py` | Look every DOI in `citations.md` up at Crossref and flag title/author mismatches — run it after adding entries, since `match_papers.py` keys on those DOIs. Needs network. | network |
| `register_papers.py` | Any PDF in `papers/` with no `citations.md` entry gets one built from its DOI via Crossref, tagged `[seed]` with a dated "registered automatically" note. Needs network. The intake runs it first; `extract.py --batch` refuses a PDF that has no entry. | network |
| `match_papers.py` | Rename PDFs dropped into `papers/` under publisher names to `<Key>.pdf`, matching on the DOI in the text, the DOI in the filename or the title in the filename; `--execute` renames, nothing is overwritten. | local |
| `rekey_paper.py` | Repair after a paper was extracted under the wrong key: renames the PDF, annotated copy, drafts and sidecars, rewrites `citation:`/`id:` and the log. `--auto` finds every draft key missing from `citations.md` and matches by DOI. | local |
| `strip_cover_pages.py` | Remove leading publisher sheets (JSTOR, HighWire, Taylor & Francis, ProQuest, ResearchGate …) so page numbers and quotes refer to the article; scanned pages are never removed; originals kept in `papers/_originals/`. | local |
| `batch_ocr.py` | Detect and OCR image-only PDFs so their text layer is searchable. Run before extracting an older paper. | local |
| `extract.py` | Read a PDF's text layer and emit schema-bound drafts plus the annotated PDF. `--dry-run` previews prompt size and `num_ctx`; `--batch` does every un-extracted PDF; `--out-dir _compare/<model>` sandboxes a benchmark run. | Ollama |
| `annotate_paper.py` | Highlight each `source_passage` in the PDF, colour-coded by what it supports. The reviewer's primary tool. | local |
| `auto_review.py` | Deterministic checks (schema, every quote in the PDF, no low confidence, no contradictions) that **reject or defer, never approve**; Tier A/B classification; with `--llm-review`, an independent model re-reads the paper and may approve Tier A. | local / Ollama |
| `review_sheet.py` | One HTML page per draft for the reviewer: each finding's claim, then every quote with its grade, the page it was found on, and a crop of that page with the passage highlighted. `--fix-pages` writes the real page numbers back into the draft. Output in `drafts/_review/` (git-ignored: page images). | local |
| `promote.py` | Approve or reject as `human:<name>` or (Tier A only) `model:<tag>`; refuses a model on Tier B or reviewing its own extraction; stamps review provenance; writes the log line. | local |
| `compare_extraction.py` | Run a candidate model on a paper you already curated and grade quote fidelity, schema, coverage and calibration. The model-selection test in `MODELS.md` §3. | local |
| `audit_quotes.py` | Grade every canonical quote against its PDF: found / elided / table / anchored / near / absent / no_pdf. The legacy re-review triage. | local |
| `quote_check.py` | The shared grader behind `auto_review.py`, `compare_extraction.py` and `audit_quotes.py`, so one quote gets one grade. Module, not a CLI. | local |
| `kb_status.py` | Entries and findings per bucket, review provenance, relationship and strength counts, which KB regions the lesion decoder can reach, papers missing from `papers/` (`--papers-needed`), the screening register's PRISMA numbers and gap coverage, `--tag-legacy`. | local |
| `aphasia_kb.py` | Load, validate (`--check DIR`, `--issues`), query (`--lookup`); `KnowledgeBase(review_kinds=("human",))` restricts to person-approved findings. | local |
| `decode_lesion.py` | Atlas overlap and Neurosynth term decoding of an MNI mask. | local |
| `aphasia_kb_rag.py` | Decode → retrieve → deterministic cited report; `--llm` adds a local narrative over the same evidence; `--human-approved-only` drops model-approved and legacy findings. | local / Ollama |

Nothing here calls a cloud API. `OLLAMA_HOST` pointing off-machine is a
configuration error and the scripts warn about it.

## Papers

Source PDFs are not redistributed. `citations.md` carries the DOI for
every key; fetch papers through your own access, drop them into
`papers/` under any name and run `intake_papers.py --execute`: a
`citations.md` entry is written from the DOI if there is none, the
file is renamed to `<Key>.pdf`, publisher cover sheets are removed and
scans are OCR'd. (Or name it yourself, e.g.
`Fridriksson2018Anatomy.pdf`, and run the steps separately.) `kb_status.py --papers-needed` lists
what the canonical KB depends on and is missing. Annotated copies (`<Key>_annotated.pdf`) are generated
locally and stay local.

## What each finding captures

A finding is a structured object, not a note: the claim; its target
(impairment, therapy, predictor or region) and `relationship` (causal,
correlational, recruitment, responder, treatment_response, synthesis);
method, design and evidence class; sample; statistics; confounders
controlled and not; how the paper defined the region; the authors' own
limitations; the extractor's `strength` and `provenance.confidence`;
and the required `source_passages`, each tagged by what it supports.
From v2.5 a `review` block records who approved it, when, and at which
tier. `schema.md` has the full specification.

## How this connects to CALMaR

CALMaR consumes this repository as a git submodule (see *Where the
knowledge base lives* above), so a `git clone --recurse-submodules` of
calmar places a checkout of it at `calmar/stroke-aphasia-kb/`. The
notebooks call the KB at the clinical-interpretation stage:
`decode_lesion.py` maps the mask to atlas regions and Neurosynth terms,
`aphasia_kb_rag.py` retrieves the matching approved findings and
renders the cited report that appears per subject. The report carries a
research-only caveat that no flag removes. Only regions present in
`decode_lesion.py`'s atlas map can be reached from a mask;
`kb_status.py` lists which KB regions are currently unreachable.

## Schema history

- **v2.0** rich finding object · **v2.1** required `source_passages`,
  `imaging_details` · **v2.2** multimodal `method`, required
  `relationship` · **v2.3** `predictors/` bucket · **v2.4** `reviews/`
  bucket, `method: narrative_review` · **v2.5** review provenance
  (`review_tier`, per-finding `review` block, `human:`/`model:` reviewers)
  · **v2.6** `sample.phase` (acute … chronic; inferred for older entries,
  filterable in the RAG with `--phase`) · **v2.7** `lesion_mapping`
  design block and `sample.cohort` (inferred for older entries;
  `lesion_mapping.py`).

Changing the schema is a change to `schema.md` and `aphasia_kb.py`
together; changing who may approve what is a change to `GOVERNANCE.md`
and the scripts that enforce it together.
