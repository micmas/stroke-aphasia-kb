# Aphasia KB — command reference

Every command, **in the order the work flows**: from the protocol and the
searches, through screening, to extracted findings reviewed into the
knowledge base. Each section starts with the commands as you run them,
then lists every option. Run from the **repository root** with the venv
active (`source .venv/bin/activate`). The method is in
[`SCREENING.md`](SCREENING.md) (finding and choosing papers),
[`HOWTO.md`](HOWTO.md) (extracting and reviewing) and
[`GOVERNANCE.md`](GOVERNANCE.md) (who may decide and approve what).

**Dry run is the default.** Every command that writes only prints what it
would do until you add `--execute`. The exceptions act when run:
`screen_app.py` and `screen.py decide` (each decision is the act),
`extract.py`, `promote.py` and `auto_review.py` (each has its own preview
flag, listed below).

---

## The flow at a glance

| Step | What happens | Command | Section |
|---|---|---|---|
| 1 | Protocol: strategies written and locked *(once; again on each amendment)* | `screen.py strategies` · lock · `screen.py rebaseline` | [0.1](#01-protocol) |
| 2 | Identification: run and import the searches, remove duplicates and grey literature *(once; again when a search is re-run)* | `screen.py search` · `import-all` · `dedupe` · `grey` · `recall` | [0.2](#02-identification) |
| 3 | Title/abstract screening, prioritised, until the stopping rule is met | `screen_app.py --by <you>` · `screen.py progress` · `stop` | [0.3](#03-titleabstract-screening) |
| 4 | Second screener on a 20 % blind sample; agreement | `screen_app.py --check` · `screen.py agreement` | [0.4](#04-second-screener) |
| 5 | Full-text assessment (PDF beside the record); pillar papers by citation chasing | `screen.py fulltext` · `screen_app.py --stage ft` · `screen.py chase` | [0.5](#05-full-text-assessment) |
| 6 | Hand-over: citation entry and PDF for each paper included at full text | `screen.py register` · PDFs into `papers/` · `intake_papers.py --execute --no-register` | [0.6](#06-hand-over-to-the-knowledge-base) · [1](#1-getting-papers-in) |
| 7 | Extraction, one paper at a time | `extract.py --pdf papers/<Key>.pdf` | [2](#2-extracting) |
| 8 | Review: checks, the workbench, focused re-extraction, approval | `auto_review.py` · `review_app.py` · `refocus.py` · `promote.py` | [3](#3-reviewing) |
| 9 | Report and sync | `screen.py status` · `kb_status.py` · git | [4](#4-checking-the-kb) · [8](#8-git-and-the-papers-folder) |

A paper reaches extraction only after it was included at full text
(`screen.py fulltext` lists what each paper needs next). Do not use
`intake_papers.py --extract` or `extract.py --batch` any more: they
extract every PDF that has no findings, screened or not.

### A screening session

```bash
git pull
python scripts/screen_app.py --by michele                 # title/abstract   (--stage ft for full text)
python scripts/screen.py progress                         # the stopping rule
git add screening logs && git commit -m "Screening session" && git push
```

### From an included paper to reviewed findings

```bash
python scripts/screen.py fulltext                         # what each included paper needs next
python scripts/screen.py register --execute               # citation entries and keys
python scripts/intake_papers.py --execute --no-register       # PDFs saved into papers/ (OneDrive calmar-papers) → <Key>.pdf, cleaned, OCR'd
python scripts/extract.py --pdf papers/<Key>.pdf          # one paper (20–30 min)
python scripts/auto_review.py --draft drafts/<bucket>/<file>.md --llm-review   # optional checks and tier
python scripts/review_app.py --citation <Key>             # findings beside the highlighted paper
python scripts/refocus.py --citation <Key> --execute      # findings for passages you marked
python scripts/promote.py --approve drafts/<bucket>/<file>.md --reviewer michele
git add -A && git commit -m "…" && git pull --rebase --autostash && git push
```

### The same, for every included paper at once

```bash
python scripts/screen.py register --execute                    # every included paper without a key
python scripts/screen.py fulltext                              # ends with "Papers without a PDF": key + DOI link for each
# download each into papers/ = ~/Library/CloudStorage/OneDrive-TheUniversityofQueensland/Documents/calmar-papers (any file name)
python scripts/screen.py pdfs --execute                        # links each saved PDF to its record by DOI (or title); the app shows it
python scripts/screen.py register --execute                    # on inclusion: citation entry + key, and the linked PDF renamed <Key>.pdf
python scripts/intake_papers.py --execute --no-register        # strips cover pages, OCRs scans (and renames any PDF of a cited paper)
python scripts/screen.py extract                               # dry run: the queue (included, PDF, no findings)
python scripts/screen.py extract --execute                     # extract them one after another (≈ 25 min each; --limit N)
python scripts/screen.py extract --backfill --execute          # bring included papers' findings up to the current schema (missing fields only)
python scripts/screen.py extract --reextract-below 2.7 --execute  # re-extract included papers whose findings are still old drafts (≈ 25 min each)
python scripts/auto_review.py --all --llm-review               # checks, tiers and model opinion on every pending draft
python scripts/review_app.py                                   # index of every draft; review paper by paper, mark passages
python scripts/refocus.py --all --execute                      # findings for every paper with pending marks
python scripts/promote.py --list                               # what is left for you
for f in drafts/*/*__<Key>.md; do python scripts/promote.py --approve "$f" --reviewer michele; done   # a paper you reviewed
git add -A && git commit -m "…" && git pull --rebase --autostash && git push
```

Approval stays a person's act per paper: approve the drafts of a paper
once you have reviewed it (`--reject … --reason` for the ones you do not
accept). `auto_review.py --all --llm-review` may itself promote Tier A
drafts a model approved unanimously; add `--no-model-approve` to keep
every approval yours.

---

## 0. Finding and screening papers — the screening register

The systematic front end (protocol: [`SCREENING.md`](SCREENING.md)).
`screen.py` and `screen_app.py` record every search, every candidate and
every decision in `screening/`, and hand papers included at full text to
`citations.md`. Neither touches `drafts/` or the canonical folders. The
stage of a candidate is derived, never typed (SCREENING.md §5).

### 0.1 Protocol

```bash
python scripts/screen.py strategies                              # strategies, version, years, fingerprint, LOCKED?
python scripts/screen.py strategies --show q1_lesion_impairment --db scopus   # the exact string for a database
python scripts/screen.py strategies --show all_questions --db psycinfo        # every question strategy in one string
# lock: set `status: locked` in screening/strategies.yaml, commit and push both protocol files
python scripts/screen.py rebaseline --execute                    # once, at the restart
```

An amendment is a change to `screening/strategies.yaml` or `SCREENING.md`
after locking: bump `version`, add an entry under `amendments` (what, why,
when), commit — the lock holds again once both files are committed.

### 0.2 Identification

```bash
# PubMed (live; dry run first: hits and how many benchmark papers they retrieve)
python scripts/screen.py search --strategy q1_lesion_impairment --db pubmed --by michele
python scripts/screen.py search --strategy q1_lesion_impairment --db pubmed --by michele --execute
# Scopus / PsycINFO: paste the string in the database, export RIS (Abstract + PubMed ID), name it <db>_<strategy>[_<count>].ris
python scripts/screen.py import-all --db scopus --files '~/Downloads/scopus_*.ris' --by michele --execute
python scripts/screen.py import --strategy q4_synthesis --db scopus --file ~/Downloads/scopus_q4.ris --hits 3503 --by michele --execute
python scripts/screen.py withdraw S010 --why "export held one page only" --by michele --execute   # take a bad import back
# after the last import
python scripts/screen.py dedupe --by michele --execute           # second duplicate pass
python scripts/screen.py grey --from ~/Downloads --by michele --execute   # theses, books, conference records out by rule
python scripts/screen.py recall                                  # coverage of the benchmark papers
python scripts/screen.py status                                  # PRISMA identification numbers
```

OpenAlex (not searched since amendment v3) needs a free API key:
`export OPENALEX_API_KEY=<key>` in `~/.zshrc`, never in the repository.
Ad-hoc searches (`search --query …`, `import --query …`) are recorded and
reported but are not part of the protocol.

### 0.3 Title/abstract screening

```bash
python scripts/screen_app.py --by michele                        # opens http://127.0.0.1:8767/ — ranked, saves as you go
python scripts/screen.py progress                                # the three stopping checks
python scripts/screen.py stop --by michele --execute             # once the rule is met: the rest recorded as not screened
```

`screen_app.py` keys: `i` include · `u` unsure · `1`–`9` exclude with that
reason (1 not stroke · 2 no language/cognitive outcome · 3 no imaging ·
4 narrative review · 5 design · 6 not a full report · 7 thesis/book/conference ·
8 duplicate · 9 therapy study without patient-characteristic analysis; "before 2000" and the
rest are buttons) · `0` Other (write the note first) · `n` note ·
`z` undo · `a` accept the suggestion shown. Decisions are journalled at once
(`screening/_sheet/app_journal.jsonl`) and the register is saved a few
seconds later and on Ctrl-C; the queue is re-ranked every `--rerank`
decisions. Offline. Close it before running other commands that write the
register (`decide`, `import`, `dedupe`, `grey`, `chase`).

Optional: `python scripts/screen.py assist` asks the local model for a
suggestion on each title/abstract (shown in the app, never a decision).
Without the app: `screen.py sheet --ranked --batch 200`, then
`screen.py decide --csv <downloaded file> --by michele`, and repeat.

### 0.4 Second screener

```bash
python scripts/screen_app.py --by alex --check --sample 0.2 --seed 1        # blind: no prior decision, no suggestion
python scripts/screen_app.py --by alex --check --stage ft --sample 0.2 --seed 1
python scripts/screen.py agreement                               # Cohen's kappa per stage, per second screener, disagreements
```

Disagreements are settled by discussion and the agreed decision recorded
in the app as a normal decision (it becomes the decision of record). Report
the seed.

### 0.5 Full-text assessment

```bash
python scripts/screen.py fulltext                                # paper by paper: what to assess, and each included paper's next step
python scripts/screen_app.py --by michele --stage ft             # the record on the left, its PDF from papers/ on the right
python scripts/screen.py chase --doi 10.1038/nn1050 --cited-by C0123 \
    --why "VLSM method behind the regions/ lesion maps" --by michele --execute   # a pillar paper no search returned
python scripts/screen.py decide --id C1031 --stage ft --decision exclude --reason duplicate_report \
    --note "preprint of C0018" --by michele                      # one decision by hand
```

In the app, full text adds `p` (hide/show the PDF; click the left side
after scrolling the PDF to use the keys again). Papers kept at
title/abstract come first, then the other-methods arm (legacy papers no
search returned: exclude with their reason, or chase them as pillars once
a paper citing them is included).

### 0.6 Hand-over to the knowledge base

```bash
python scripts/screen.py register --execute                      # included papers without a key → citations.md entry + key (Crossref)
python scripts/intake_papers.py --execute --no-register         # PDFs saved into papers/ → <Key>.pdf (section 1)
python scripts/screen.py fulltext                                # what is left: PDF, extract (commands listed), review
```

### `screen_app.py` — options

| Option | Meaning |
|---|---|
| `--by NAME` | The person screening (required; not `model`, `legacy`, `agent`). |
| `--stage ta\|ft` | Title/abstract (default, ranked) or full text (split view with the PDF). |
| `--check` | Second screener: a blind random sample of records that already have a decision of record. |
| `--sample F` | With `--check`: a fraction (0.2) or a number (50). |
| `--seed N` | With `--check`: random seed (default 1; report it). |
| `--rerank N` | Re-rank the title/abstract queue after N decisions (default 50). |
| `--port N` | Default 8767 (the review workbench uses 8766). |
| `--no-browser` | Do not open the browser. |

### `screen.py` — every subcommand, in the order of the flow

| Subcommand | What it does | Options |
|---|---|---|
| `strategies` | Lists the strategies in `screening/strategies.yaml`, the protocol version, publication years and fingerprint, whether it is locked (status `locked` and both protocol files committed), and which strategies have been run where. | `--show ID --db pubmed\|openalex\|scopus` `-v` |
| `rebaseline` | Moves every `by: legacy` decision into the candidate's `legacy` record and marks legacy includes `benchmark: true`, so each paper is screened afresh under the protocol. Nothing is deleted. Idempotent. | `--date` `--execute` |
| `search` | Live PubMed (E-utilities) or OpenAlex query; hits become candidates, de-duplicated by DOI / PMID / title+year; the search is one record in `screening/searches.yaml`. With `--strategy` the query, years and `--for` come from the protocol, the run records the strategy and protocol fingerprint, nothing is capped, an incomplete retrieval is refused, and `--execute` is refused until the protocol is locked. Every run (dry or not) reports how many benchmark papers it retrieved. PubMed queries over 10,000 hits are split by publication year. Network. | `--strategy` or `--query` · `--db pubmed\|openalex` `--years 2000-2026` `--for gap,entry` `--by` `--max` `--oa-field` `--notes` `--allow-unlocked` `--execute` |
| `import` | The same from a RIS or CSV export (Scopus, Embase, PsycINFO, Web of Science); with `--strategy` the recorded query is the protocol's string for that database, otherwise give the query and date so the record is complete. | `--file` `--db` `--strategy` or `--query` · `--date` `--years` `--for` `--by` `--execute` |
| `import-all` | Imports every export matching a wildcard, one search record per strategy. Names carry the strategy and, optionally, the count the database showed: `scopus_q1_lesion_impairment.ris` or `scopus_q1_lesion_impairment_5312.ris`; a split export adds `-a`, `-b`. A count not in the name is asked for (or given with `--counts`). | `--db` `--files '~/Downloads/scopus_*.ris'` `--counts id=n,…` `--by` `--date` `--execute` |
| `--strategy all_questions` | One search per database that ORs every question strategy (q1–q5): one export instead of seven (`strategies --show all_questions --db psycinfo`; file `psycinfo_all_questions.ris`). Counts in overall and per-database recall, not per strategy. | with `search`, `import`, `import-all`, `strategies --show` |
| `withdraw` | Takes back a recorded search (an incomplete export, a wrong file): the record moves to `withdrawn` in `searches.yaml` with the reason, candidates that came only from it leave the register, the id is never reused. Logs `SEARCH-WITHDRAWN`. | `<id>` `--why` `--by` `--execute` |
| `dedupe` | Second de-duplication pass after all imports: same title, years ±1, no conflicting PMID/DOI → `duplicate_of` (record with identifiers kept, sources merged). Logs `DEDUPED`. | `--by` `--execute` |
| `grey` | Grey literature by rule (protocol v4): theses, books/chapters, conference records → excluded before screening with the evidence (`rule: …`); preprints kept. `--from ~/Downloads` re-reads the Scopus/PsycINFO exports for each record's own type. | `--from` `--types` `--show` `--by` `--execute` |
| `recall` | Relative recall: benchmark papers found by any database search, per strategy (against the benchmark papers in its KB folders) and per database, and the list no search found. | `--json` |
| `status` | The protocol version and lock, the PRISMA numbers (both arms), recall against the benchmark, kappa if double-screened, where included papers stand in the KB, and found / included / in-KB per evidence gap. | `--json` |
| `assist` | The local model (role `screen`, else `review`, in `models.yaml`) reads title + abstract against SCREENING.md §2 and writes `suggestion`. Ollama. | `--model` `--ids` `--max` `--redo` |
| `sheet` | One HTML card per candidate awaiting the pass, with the suggestion, keyboard shortcuts and a CSV download. Written to `screening/_sheet/` (git-ignored). Title/abstract cards are blind: no citation key, no hand-picked or legacy provenance. `--check` writes a blind random sample of already-decided candidates for a second screener (no prior decision, no suggestion). | `--stage title_abstract\|full_text` `--for gap` `--ids` `--out` · `--check --sample 0.2 --seed 1` |
| `sheet --ranked` | Title/abstract sheet ordered by the prioritisation model (SCREENING.md §4.1), the top `--batch` records (default 200); prints the stopping-rule status. Keys `1`–`9` exclude with that reason and move on. | `--ranked` `--batch 200` |
| `decide` | Records decisions from the sheet's CSV or one by hand; an exclusion needs a reason, `other` and `duplicate_report` need a note, `--by` must be a person. Appends `SCREENED` to the log. Acts at once. `--role check` records a second screener's decision for the agreement statistic (never the decision of record; must be a different person). | `--csv` or `--id --stage --decision --reason --note` · `--by` `--date` `--role check` |
| `progress` | Prioritised screening against the stopping rule: share screened, last run of exclusions, validation papers screened. | `--json` |
| `stop` | Once the stopping rule is met, records every database record still awaiting title/abstract as not screened (`not_screened_stopping_rule`). Logs `SCREEN-STOPPED`. | `--by` `--date` `--execute` |
| `agreement` | Cohen's kappa between decisions of record and check decisions per stage (unsure counts as include at title/abstract), the 2×2 table and each disagreement. | `--stage ta\|ft` |
| `pdfs` | Links PDFs saved in `papers/` under any name to their screening records — the paper's own DOI on its first pages (the first that matches a record), else the file name against the titles awaiting full text — and sets `pdf_file`. The full-text app then shows them; `register` renames each to `<Key>.pdf` when its paper is included. Lists PDFs that match no record (not returned by the searches, or a second copy). Download PDFs before the full-text decision if you like. | `--execute` |
| `fulltext` | Ends with **Papers without a PDF**: every paper still needing one, with its key and `https://doi.org/…` link, and any PDF already sitting in `papers/` under another name that carries its DOI. The full-text stage, paper by paper: what is waiting for assessment (already extracted before the protocol, or not), and for papers included at full text the next step — register, fetch the PDF, extract (with the commands), review — or "in the KB". Also lists papers excluded at full text that still have findings. | — |
| `chase` | Enters a pillar paper by citation chasing (before 2000, primary healthy-volunteer study, no abstract …): `--cited-by` must name papers included under the protocol and `--why` says what the KB needs it for. Existing candidate → source added; else Crossref record from the DOI (or `--title --year`). Goes to full text, other-methods arm. Logs `CHASED`. | `--doi` or `--title --year` · `--cited-by` `--why` `--by` `--date` `--execute` |
| `extract` | The screening-aware batch: extracts every paper included at full text that has its PDF and no findings yet, one `extract.py` run after another (a failure is reported, the next one runs). Dry run lists the queue. | `--limit N` `--model` `--num-ctx` `--max-tokens` `--timeout` `--lean` `--execute` |
| `register` | Included candidates without a key: Crossref record from the DOI → `citations.md` block (house format, `[seed]`, note says which candidate) and `key:` set; existing DOIs are linked instead. Network. | `--execute` |
| `list` | Candidates with id, derived stage, KB state, key and title. | `--stage` |
| `fetch-abstracts` | Fills `screening/abstracts.jsonl` from PubMed (by PMID) then OpenAlex (by DOI). Network. | `--max` |
| `backfill` | Every `citations.md` key not in the register becomes an *other-source* candidate; extracted keys are stamped included `by: legacy`, `[refused]` excluded, seeds left awaiting assessment. Idempotent. | `--date` `--execute` |

## 1. Getting papers in

For papers included at full text (step 6 of the flow): `screen.py register`
gives each one its citation entry; download the PDFs straight into `papers/`
(the OneDrive `calmar-papers` folder) under any name, then
`intake_papers.py --execute --no-register` renames each to `<Key>.pdf` by its
DOI, strips cover pages and OCRs scans. `screen.py fulltext` ends with every
paper still lacking a PDF, with its DOI link. Use `--no-register` with
screened work: without it, a PDF that matches no citation gets a new
`citations.md` entry of its own, bypassing screening. (`--from DIR` still
pulls matching PDFs out of another folder, e.g. `~/Downloads`.)

### `intake_papers.py` — everything between the download and the extractor

Runs, in order: register → rename → strip cover sheets → OCR → status →
(optionally) extract. Each step skips what is already done, so
re-running is safe and resumes an interrupted batch.

| Option | Meaning |
|---|---|
| *(none)* | Dry run of every step. |
| `--execute` | Apply all steps. |
| `--allow-probable` | Also rename files matched only by author + year + title (PDFs that print no DOI, e.g. Lancet, Neurology). The dry run shows which. |
| `--extract` | Afterwards run `extract.py --batch` on every paper with no findings yet. With `--execute` it extracts; without, it lists the queue. **Not for screened work:** it does not check full-text inclusion — extract included papers one by one (section 2). |
| `--from DIR` | First copy PDFs out of `DIR` (e.g. `~/Downloads`) whose DOI matches a cited paper that has no PDF yet. Nothing is moved; other files are ignored. |
| `--no-register` | Skip step 1: do not create `citations.md` entries for unknown PDFs. |
| `--no-ocr` | Skip the OCR step. |
| `--papers-dir DIR` | Use another papers folder (default `papers`). |

The steps also run on their own:

### `register_papers.py` — give every PDF a citation entry

Looks up each unknown PDF's DOI at Crossref and appends a `[seed]`
block to `citations.md` under "Registered automatically", with a dated
note. Needs network. A PDF with no DOI is listed for a hand-written
block.

| Option | Meaning |
|---|---|
| `--execute` | Append the entries. |
| `--papers-dir DIR`, `--citations FILE` | Other locations. |

### `match_papers.py` — rename downloads to `<Key>.pdf`

Matches on the DOI in the text, the DOI in the filename, or the title
in the filename; author + year + title as a last resort ("probable").
Never overwrites.

| Option | Meaning |
|---|---|
| `--execute` | Rename. |
| `--allow-probable` | With `--execute`, also rename the author/year/title matches. |
| `--papers-dir DIR`, `--citations FILE` | Other locations. |

### `strip_cover_pages.py` — drop publisher cover sheets

JSTOR, HighWire/AJNR, Taylor & Francis, ProQuest, ResearchGate,
Elsevier/Springer author copies, ClinicalKey. Scanned pages and running
footers are never treated as covers. Originals go to `papers/_originals/`.

| Option | Meaning |
|---|---|
| `FILE …` | Only these PDFs (default: all of `papers/`). |
| `--execute` | Strip. |
| `--pages N` | With named files: drop exactly N leading pages, no detection. |
| `--papers-dir DIR` | Other folder. |

### `batch_ocr.py` — make scans searchable

Needs `brew install ocrmypdf`. Detects image-only PDFs, including scans
with a stamped text line; retries with forced OCR if the first pass
leaves the text thin. Originals go to `papers/_originals/`.

| Option | Meaning |
|---|---|
| `--execute` | Run OCR (default is a dry run). |
| `--threshold N` | Characters in the first 3 pages below which a PDF counts as image-only (default 200). |
| `--limit N` | Stop after N files (testing). |
| `--papers-dir DIR` | Other folder. |

### `verify_dois.py` — check `citations.md` against Crossref

Flags entries whose DOI resolves to a different title or first author.
Run after writing citation blocks by hand. Needs network; read-only.

| Option | Meaning |
|---|---|
| `--status TAG` | Only entries with this tag (`seed`, `cited`, …). |
| `--key @Key` | Only this entry (repeatable). |
| `--citations FILE` | Check another file in the same format. |

---

## 2. Extracting

Step 7 of the flow: one paper at a time, for papers included at full text
(`screen.py fulltext` prints the command for each one that has its PDF and
no findings yet).

```bash
python scripts/extract.py --pdf papers/<Key>.pdf --dry-run    # the prompt only
python scripts/extract.py --pdf papers/<Key>.pdf              # 20–30 min; drafts in drafts/<bucket>/
```

### `extract.py` — the local model reads a paper and writes drafts

Writes `drafts/<bucket>/<id>__<Key>.md`, the annotated PDF and an
EXTRACTED line in `logs/extraction_log.md`. Streams the response (progress
every 2 minutes), cuts repetition loops early and retries once, and
retries once with a larger budget if a genuine output overflows.

| Option | Meaning |
|---|---|
| `--pdf FILE …` | Extract these PDFs (one or more). Works even if the paper already has findings. |
| `--batch` | Every PDF in `papers/` with no findings yet. Skips `[refused]` papers, PDFs over 60 pages, and PDFs with no `citations.md` entry. **Does not check full-text inclusion** — not for screened work. |
| `--citation @Key` | Force the key (single `--pdf` only; normally inferred from the filename). |
| `--out-dir DIR` | Sandbox: write drafts under `DIR/drafts/`, no annotated PDF, no log line. For benchmarks and second opinions. |
| `--dry-run` | Build the prompt, don't call the model; saves it to `_extraction_dry_run.txt`. |
| `--model TAG` | Ollama model for this run (default from `models.yaml`). |
| `--pick-model` | Choose interactively from the pulled models. |
| `--max-tokens N` | Output budget (default from `models.yaml`, 16000). |
| `--num-ctx N` | Context window (default: sized from the prompt). |
| `--lean` | Leave `citations.md` out of the prompt (smaller, faster; the model then can't see what is already cited). |
| `--timeout S` | Give up on one paper after S seconds (default 3600). |
| `--no-monitor` | No GPU/CPU monitor line. |
| `--ollama-host URL` | Another Ollama server (default `http://localhost:11434`; a non-local host is warned about). |

### `backfill.py` — bring older findings up to schema v2.8

Asks the extraction model, once per paper, only for the fields a finding
is missing (`lesion_mapping`, `sample.phase`, `sample.cohort`,
`author_limitations`, and from v2.8 `therapy`: the `{id, name}` of the
intervention behind every `treatment_response` / `responder` finding,
quoted from the sentence that names it). Claims, quotes and reviews are untouched. A value
is written only if its quote is found in the PDF (or it is
`not_reported`); the quote is added to the finding's `source_passages`
and the finding gets `filled: {by, date, tool, fields}`. Approved entries
are written too; the report labels these values "filled in by a model".
A file moves to `schema_version: 2.8` once all its findings are complete.

| Option | Meaning |
|---|---|
| (none) | Dry run: papers and their missing fields. |
| `--execute` | Ask the model and write the verified values. |
| `--citation @Key` | Only these papers (repeatable). |
| `--fields a,b` | Subset of `lesion_mapping,phase,cohort,author_limitations,therapy`. |
| `--drafts-only` | Leave approved entries alone. |
| `--limit N` | Stop after N papers. |
| `--from-response FILE` | Apply a saved response (`_last_backfill_response_<Key>.txt`) for one `--citation`. |
| `--reapply` | No model: apply every saved response again to the fields still missing. |
| `--retry` | Ask again for fields already answered without a verifiable quote (`filled.unresolved`). |

### `retarget_symptoms.py` — symptom, not syndrome (schema v2.8)

```bash
python scripts/retarget_symptoms.py              # dry run: RETARGET / KEEP / REVIEW lists
python scripts/retarget_symptoms.py --execute    # drafts and canonical entries
python scripts/retarget_symptoms.py --execute --drafts-only
```

Moves findings whose target is an aphasia syndrome but whose claim is a
symptom onto the symptom entry: `naming`, `confrontation_naming` and
`anomic_aphasia`-with-a-naming-claim → `anomia`. A syndrome target whose
claim speaks of the classified type is kept and listed for a person to
confirm; other `*_aphasia` targets with symptom claims are listed for
the workbench. The old target is kept in `provenance.flags`, an `edits`
record is added, and one `RETARGETED` line per file goes to the log.
Re-run `export_webapp.py` after.

### `reextract.py` — extract chosen papers again, on purpose

Old drafts and sidecars move to `_compare/superseded/<date>/` (nothing
deleted); a paper that already has approved findings goes to the
sandbox `_compare/rerun/` instead, so nothing approved is duplicated.

| Option | Meaning |
|---|---|
| `KEY …` | Citation keys, with or without `@`. |
| `--preset placeholder` | The five therapy papers whose May findings quote "clinical knowledge". |
| `--preset selective-retry` | The fifteen papers cut to 8 findings by the 20–21 Oct overflow retry. |
| `--into-drafts` | Write fresh drafts even when approved findings exist (to replace, not compare). |
| `--execute` | Move the old drafts and extract. |
| `--papers-dir DIR` | Other folder. |

### `compare_extraction.py` — compare a sandbox extraction with the KB

Quote fidelity, schema, coverage and calibration of a sandbox run
against the curated entries for the same paper. The model-selection
test in `MODELS.md` §3, and the way to merge a `reextract.py` sandbox run.

| Option | Meaning |
|---|---|
| `--citation @Key` | The paper (required). |
| `--candidate-dir DIR` | Where the sandbox run wrote (required). |
| `--show-claims` | Print every claim from both sides. Recommended. |
| `--reference-root DIR`, `--papers-dir DIR` | Other locations. |

### `annotate_paper.py` — highlight a draft's quotes in its PDF

`extract.py` runs this itself; use it to redo one by hand.

| Option | Meaning |
|---|---|
| `--draft FILE …` | Drafts whose passages to highlight (required). |
| `--pdf FILE` | The paper (required). |
| `--out FILE` | Output path (default `<pdf>_annotated.pdf`). |
| `--no-legend` | No colour-legend page. |
| `--fail-on-missing` | Exit non-zero if a quote can't be placed. |
| `--no-rename` | Don't rename the source PDF to `<Key>.pdf` first. |

---

## 3. Reviewing

Step 8 of the flow, per paper: optional automatic checks
(`auto_review.py`), then the workbench (`review_app.py`) to correct
findings against the highlighted paper and mark passages the extraction
missed, `refocus.py` for those marks, and `promote.py` to approve or
reject each draft. `normalize_drafts.py` and `review_sheet.py` are the
older, batch-oriented tools.

```bash
python scripts/auto_review.py --draft drafts/<bucket>/<file>.md --llm-review   # checks, tier, model opinion
python scripts/review_app.py --citation <Key>                                 # http://127.0.0.1:8766/
python scripts/refocus.py --citation <Key> --execute                          # after marking passages
python scripts/promote.py --list
python scripts/promote.py --approve drafts/<bucket>/<file>.md --reviewer michele
python scripts/promote.py --reject  drafts/<bucket>/<file>.md --reviewer michele --reason "..."
```

### `normalize_drafts.py` — apply the save-time repairs to existing drafts

Missing `author_limitations` → `[]` + flag; missing `sample.phase` →
inferred; `region_definition` without `kind` → `not_reported`; imaging
finding without `reference_space` → `not_reported` + flag; predictor
fields copied from the canonical entry. Never touches canonical folders.

| Option | Meaning |
|---|---|
| `--execute` | Rewrite the drafts. |
| `--draft FILE` | Only this draft (repeatable). |

### `auto_review.py` — checks, tier, independent model review

Deterministic checks (schema, every quote in the PDF, confidence,
contradictions) can only reject or defer. With `--llm-review` the
review model re-reads the paper; it may approve **Tier A only** and
never its own extraction. Verdicts: `auto_approve` (promoted),
`checks_passed` (Tier B, yours), `defer_to_human`, `auto_reject`
(blocked until fixed; the draft stays where it is). Each draft gets a
sidecar in `logs/auto_review/`.

| Option | Meaning |
|---|---|
| `--all` | Every pending draft. |
| `--draft FILE` | One draft. |
| `--deferred` | Only drafts whose last verdict was `defer_to_human`. |
| `--pending-pdf` | Only drafts provisionally approved on a machine without the PDF. |
| `--llm-review` | Use the local review model (`models.yaml` → `review`). Without it, deterministic checks only. |
| `--require-pdf-match` | Refuse approval when the PDF is unavailable. Use always. |
| `--provisional-without-pdf` | Without the PDF, mark would-be approvals provisional instead (for a laptop without papers). |
| `--votes N` | Model reviews per draft; approval needs all N to agree (default 3). |
| `--no-model-approve` | Record the model's verdicts but promote nothing (calibrating a new reviewer). |
| `--no-promote` | Compute and log verdicts, don't promote. |
| `--dry-run` | Compute verdicts; no promotion, no logs. |
| `--emit-worksheet FILE` | Write the selected drafts and their problems to a YAML worksheet for batch human review. |
| `--apply-verdicts FILE` | Apply a filled-in worksheet; needs `--reviewer human:<name>`. |
| `--reviewer human:<name>` | Who filled in the worksheet. |
| `--model TAG`, `--ollama-host URL`, `--papers-dir DIR` | Overrides. |

### `review_sheet.py` — one HTML page per draft, every quote on its page

Output in `drafts/_review/` (git-ignored: contains page images). Shows
each finding's claim, phase and time post-onset, and each quote with
its grade, the page it was found on, and a highlighted crop.

| Option | Meaning |
|---|---|
| `--all` | Every draft. |
| `--draft FILE` | One draft (repeatable). |
| `--fix-pages` | Write the page each quote was actually found on into the draft. |
| `--fill-phase` | Write the inferred `sample.phase` into drafts that lack it. |
| `--out-dir DIR`, `--papers-dir DIR` | Other locations. |

### `review_app.py` — the review workbench: draft and paper side by side

```bash
python scripts/review_app.py                                            # index of every draft, pick one
python scripts/review_app.py --draft drafts/regions/<entry>__<Key>.md   # open one
python scripts/review_app.py --citation <Key>                           # the paper's first draft (index lists the rest)
```

A local page (127.0.0.1 only, no dependency beyond PyMuPDF): each
finding's claim, direction, relationship, strength, confidence, flags
and author limitations on the left, editable, with every source passage
graded (`quote_check.py`), located on its page and colour-coded; on the
right the whole paper, every page, with the passages highlighted as in
the annotated PDF. Drag across words to quote the PDF's own text layer,
then attach the quote to a finding (choosing `supports`) or **mark it
for re-extraction** with a note. Save validates against `schema.md`
(an edit may not add a validation issue; existing ones are listed),
keeps the previous version in `drafts/_backup/` (git-ignored), stamps
`edits: [{by, date, fields}]` on each changed finding, appends
`REVIEW-EDITED` to the log and regenerates `papers/<Key>_annotated.pdf`.
Only drafts are editable.

| Option | Meaning |
|---|---|
| `--draft FILE` | Open this draft. |
| `--citation KEY` | Open the first draft citing the paper. |
| `--port N` | Default 8766. |
| `--no-open` | Do not open the browser. |

### `refocus.py` — findings for the passages a reviewer marked

```bash
python scripts/refocus.py drafts/regions/<entry>__<Key>.md             # dry run: the marks, prompt size
python scripts/refocus.py drafts/regions/<entry>__<Key>.md --execute   # call the model, merge
python scripts/refocus.py --citation <Key> --execute                   # every draft of the paper with pending marks
python scripts/refocus.py --all --execute                              # every paper with pending marks, one model call each
```

Takes the pending `reviewer_marks` of a draft, gives the local model
(role `extract`) the paper, the findings already drafted from it and the
marks, and asks for findings whose passages include each marked quote.
Returned findings are appended to the existing draft of their entry
(next free id) or saved as new drafts, flagged `refocus: m<n>`; each
mark becomes `status: done` with the finding ids it produced, or
`unresolved` with the model's reason. Then the annotated PDF is
regenerated and `REFOCUSED` logged. The new findings are drafts: review
them in the workbench, promote as usual. `promote.py` refuses a draft
that still has a pending mark.

| Option | Meaning |
|---|---|
| `--citation KEY` | All drafts of the paper. |
| `--all` | Every paper with a pending mark, one model call per paper. |
| `--model TAG` | Override `models.yaml` role `extract`. |
| `--timeout S` | Model call timeout (default 3600). |
| `--execute` | Call the model (default: dry run, prompt written to `_refocus_dry_run.txt`). |

### `promote.py` — the only way into the canonical KB

| Option | Meaning |
|---|---|
| `--list` | Pending drafts — your review queue. |
| `--show FILE` | Print one draft. |
| `--diff FILE` | Diff a draft against the canonical entry it would merge into. |
| `--approve FILE` | Approve: merge into the canonical entry, stamp the review block, log APPROVED. |
| `--reject FILE` | Mark `status: rejected` in place, log REJECTED. |
| `--reviewer human:<name>` | Required for approve/reject. `model:<tag>` only for Tier A and only if it didn't extract the draft. |
| `--reason "..."` | Why rejected (goes to the log). |
| `--tier A\|B` | Tier from `auto_review.py`; required (as A) for a model reviewer. |
| `--extractor agent:<tag>` | Who extracted the draft (default: its `created_by`). |

Approval is refused while the draft has a pending reviewer mark
(`review_app.py`); resolved marks are dropped from the canonical copy,
per-finding `edits` records are kept.

---

## 4. Checking the KB

Step 9 of the flow. For the screening side: `screen.py status` (PRISMA
numbers, recall, kappa), `screen.py recall`, `screen.py progress` and
`screen.py fulltext` (section 0).

### `kb_status.py` — counts and gaps

Ends with the screening register's PRISMA numbers and the coverage of
each evidence gap (`screen.py status` has the full breakdown).

Entries and findings per bucket, review provenance (person / model /
legacy), findings by recovery phase, relationship and strength, which
regions the lesion decoder can reach, papers cited vs present.

| Option | Meaning |
|---|---|
| *(none)* | The summary. |
| `--papers-needed` | Cited papers with no PDF, with DOIs. |
| `--tag-legacy` | Tag pre-policy entries `review_tier: legacy` (with `--dry-run` to list only). |
| `--json` | Machine-readable output. |

### `audit_quotes.py` — every canonical quote against its PDF

Grades: found · elided · table (verified) · anchored · near (check by
eye) · absent (re-review first) · no_pdf. The legacy re-review triage
and the 20 % audit in GOVERNANCE.md.

| Option | Meaning |
|---|---|
| `--bucket NAME` | Only this bucket (repeatable). |
| `--show-absent` | List every absent quote. |
| `--csv FILE` | One row per passage. |
| `--fail-on-missing` | Exit 1 if any quote is absent (for CI). |
| `--root DIR`, `--papers-dir DIR` | Other locations. |

### `aphasia_kb.py` — loader and validator

| Option | Meaning |
|---|---|
| `--check DIR` | Validate the entries in DIR (`drafts/`, `regions`, …). |
| `--issues` | Print every validation issue in the KB. |
| `--drafts` | List pending drafts. |
| `--lookup NAME` | Find a region by id, name or alias. |
| `--include STATUS …` | Statuses to load (default: everything). |
| `--root DIR` | Other KB folder. |

### `atlas_mapping.py` — atlas labels → KB regions

| Option | Meaning |
|---|---|
| `--write-table` | Regenerate `atlas_mapping/MAPPING.md` and `EVIDENCE_GAPS.md`. |
| `--coverage` | How many location findings the mapping can reach. |

### Tests

```
python tests/test_review_guardrails.py      # the review policy, against a mock Ollama
python tests/test_screening.py              # the screening register: parsers, de-duplication, stages, PRISMA counts, strategies, rebaseline, recall, kappa
python tests/test_review_app.py             # the review workbench and refocus merge, against a generated PDF (needs PyMuPDF)
python tests/test_schema_v28.py             # v2.8: therapy block, symptom vs syndrome, retargeting, therapy backfill checks
python -m pytest tests/test_kb_atlas_mapping.py  # the atlas mapping
```

---

## 5. Repairs

### `rekey_paper.py` — move a paper from a wrong key to the right one

Renames the PDF, annotated PDF, drafts and sidecars; rewrites `id:` and
`citation:`; fixes the log and adds a REKEYED line. Drafts only.

| Option | Meaning |
|---|---|
| `--auto` | Every draft key missing from `citations.md`, matched by the PDF's DOI. |
| `--from @Old --to @New` | One paper explicitly (the new key must exist in `citations.md`). |
| `--execute` | Apply. |

---

## 6. Using the KB on a lesion

### `aphasia_kb_rag.py` — decode a mask, retrieve evidence, write the report

| Option | Meaning |
|---|---|
| `LESION` | Binary lesion mask in MNI space (`.nii.gz`). |
| `--human-approved-only` | Use only findings a person approved (the notebook default). |
| `--phase PHASE …` | Only findings from these recovery phases, e.g. `--phase chronic mixed longitudinal` for a chronic patient. |
| `--llm` | Add a narrative written by the local model over the same evidence. |
| `--min-overlap-pct X` | Ignore atlas regions the lesion covers less than X % of (default 1). |
| `--min-term-r R` | Ignore Neurosynth terms below correlation R (default 0). |
| `-o FILE` | Write the report markdown here. |
| `--model TAG`, `--ollama-host URL`, `--kb-root DIR` | Overrides. |

### `decode_lesion.py` — atlas overlap and Neurosynth terms only

| Option | Meaning |
|---|---|
| `LESION` | The mask. |
| `--terms T …` | Neurosynth terms to decode (default list in the script). |
| `--cache DIR` | Neurosynth cache (default `_neurosynth_cache/`). |

---

## 7. Models

```
python scripts/model_config.py      # which model each role uses, and what is pulled
ollama ps                              # what is loaded, and whether it is 100 % on the GPU
```

Roles live in `models.yaml` (`extract`, `review`, `rag`). One-off
overrides without editing it:

```
APHASIA_EXTRACT_MODEL=qwen3.8:27b python scripts/extract.py --pdf …
APHASIA_REVIEW_MODEL=… python scripts/auto_review.py …
APHASIA_RAG_MODEL=…     python scripts/aphasia_kb_rag.py …
```

Benchmark a candidate before adopting it (`MODELS.md` §3):

```
python scripts/extract.py --pdf papers/Alyahya2018NounVerb.pdf --model <tag> --out-dir _compare/<tag>
python scripts/compare_extraction.py --citation @Alyahya2018NounVerb --candidate-dir _compare/<tag> --show-claims
```

---

## 8. Git and the papers folder

```
git pull --rebase --autostash          # before starting work
git add -A                     # papers/, _compare/, drafts/_review/ are ignored
git commit -m "..."
git push
git status --short                     # should list nothing after the push
ls -la papers               # should end in "-> …/OneDrive…/calmar-papers"
```

`papers` is a link to `calmar-papers` in OneDrive on every
computer (set "Always Keep on This Device" on that folder). To set it
up on a new clone, from the repository root:

```
rm -rf papers
ln -s "$HOME/Library/CloudStorage/OneDrive-TheUniversityofQueensland/Documents/calmar-papers" papers
```

Extract on one computer only; two computers annotating the same paper
at once make OneDrive write conflict copies.
