# Screening protocol: how papers are found and chosen

The knowledge base holds findings extracted from papers; this document
says how papers get to the extractor in the first place. Until October
2026 they were picked by hand. From here on, identification and
screening follow the protocol below, every step is recorded in the
screening register (`screening/`, kept by `screen.py`), and the
explorer's **Coverage** view draws the result as a PRISMA 2020 flow
diagram with every box clickable. The aim is coverage you can audit:
anyone can see which searches were run, what they returned, what was
excluded and why, and what each evidence gap still needs.

**The October 2026 restart.** The bibliography built during
development (`citations.md` up to 2026-10) was chosen by hand. It is not
the KB's justification any more: the protocol's searches are run from
scratch, every candidate — legacy papers included — is screened against
§2, and the legacy set is used to measure the searches (§3.3), not to
decide anything. A legacy paper keeps its findings while it is re-screened;
it stays in the KB only if it passes.

The register sits upstream of everything in `HOWTO.md`. Nothing here
writes to `drafts/` or the canonical folders; an included paper is
handed to `intake_papers.py` exactly as a hand-picked one was.

## 1. Questions the knowledge base answers

A paper is relevant when it reports, for people with aphasia after
stroke, at least one of:

- **lesion → impairment**: an association between damage to a brain
  region, tract or network and a language or communication outcome —
  motor speech (dysarthria, apraxia of speech) and prosody included — or
  a domain-general cognitive outcome after stroke
  (executive function, working memory, cognitive control) (regions/,
  impairments/);
- **therapy → response**: the neural correlates or imaging/lesion
  predictors of response to a named therapy or ingredient (therapies/,
  ingredients/);
- **predictor → outcome**: a lesion or imaging predictor of aphasia
  severity or recovery, alone or with demographic, clinical or genetic
  predictors (predictors/);
- **synthesis**: a systematic review, scoping review or meta-analysis of
  any of the above; a narrative review only when it covers neuroimaging
  or lesion evidence in stroke (reviews/, since schema v2.4).

Healthy-volunteer imaging that maps a language function to anatomy is
in scope as *recruitment* evidence (see `schema.md`, relationship
`recruitment`) through **meta-analyses and systematic reviews only**
(coordinate-based: ALE, MKDA, SDM); it must still concern a function the
KB tracks. A primary healthy-volunteer study enters only as a pillar
paper by citation chasing (§3.4).

**Imaging-anchored scope (protocol v2).** The knowledge base serves
CALMaR, which interprets an individual's lesion, so a *primary* study is
in scope only when it relates brain imaging or lesion data to an
outcome. Evidence without imaging — the efficacy of a therapy,
clinical and demographic predictors such as age, initial severity or
time post onset — enters **only through systematic reviews and
meta-analyses** (synthesis). A primary study without imaging is
excluded with `no_imaging_primary`.

**Publication years: 2000 onward** (`years` in
`screening/strategies.yaml`). Earlier papers enter only as pillar papers
by citation chasing.

## 2. Eligibility criteria

Screening is done in two passes — title/abstract, then full text — and
a candidate is excluded for exactly one reason from this list. The ids
are what `screen.py decide --reason` accepts and what the explorer
reports; change this list and `screening.REASONS` together.

| id | Exclude when… | Applies at |
|---|---|---|
| `not_stroke` | the population is not (post-)stroke: tumour, TBI, primary progressive aphasia, dementia, developmental; or healthy-only with no language-mapping question | both passes |
| `not_aphasia` | no aphasia, language, communication (motor speech — dysarthria, apraxia of speech — and prosody included) or domain-general cognitive outcome is reported (e.g. motor recovery only, spatial neglect only) | both passes |
| `no_imaging_primary` | a primary study with no brain imaging or lesion data related to the outcome (e.g. a therapy trial, a clinical prognostic cohort); its evidence enters through syntheses (§1) | both passes |
| `narrative_review_out_of_scope` | a narrative (non-systematic) review that does not cover neuroimaging or lesion evidence in stroke | both passes |
| `out_of_date_range` | published before 2000 (the protocol's `years`) and not entered as a pillar paper by citation chasing | both passes |
| `design_out_of_scope` | nothing the schema can hold: no lesion–behaviour, therapy-response, predictor or network evidence (pure psycholinguistic modelling, instrument validation without brain or outcome data, qualitative studies of lived experience) | both passes |
| `not_full_report` | editorial, letter, commentary, conference abstract, protocol, erratum, thesis | both passes |
| `insufficient_sample` | fewer than **5** participants for a lesion-mapping or therapy claim; single cases are kept only when they are the classic source for a region entry (note it) | both passes |
| `language` | not available in a language the screener reads | both passes |
| `duplicate_report` | a secondary publication of a cohort already included — note which; the primary report is the one extracted | both passes |
| `not_retrieved` | the full text could not be obtained through the screener's access (counts as "reports not retrieved" in PRISMA, not as an exclusion for cause) | full text |
| `not_extractable` | read in full, but the findings cannot be written into the schema with verbatim support (e.g. results only in figures, pooled across aetiologies with no stroke breakdown) — note why | full text |
| `other` | anything else — the note is required | both passes |

A candidate that is *not* excluded at title/abstract is included to
full text. At full text it is included when it answers at least one
question in §1 and none of the reasons above applies. When the
screener cannot decide, `unsure` keeps it visible without inventing a
decision; it returns in the next sheet.

Reviews and meta-analyses are eligible (they become `reviews/` entries)
— the 2026-05 rule refusing them is obsolete (`citations.md`, "Refused
papers").

## 3. Identification

### 3.1 Pre-specified strategies

The searches are written before they are run, in
`screening/strategies.yaml`: one strategy per question family of §1
(`q1_lesion_impairment`, `q1b_language_lesion_mapping`,
`q1c_cognition_prosody_lesion`, `q2b_therapy_response_neural`,
`q3_predictor_outcome`, `q4_synthesis`, `q5_recruitment_meta`; protocol
v2 removed `q2a_therapy_efficacy` and requires imaging in q2b and q3)
and one per evidence gap (`gap_…`). Each is a
combination of shared concept blocks (aphasia, stroke, imaging, therapy,
trial design, response, predictor, synthesis), written once per database
— PubMed (MeSH + title/abstract, truncation), OpenAlex (boolean
title + abstract filter, no wildcards) and Scopus (`TITLE-ABS-KEY`).
`screen.py strategies --show <id> --db <db>` prints the expanded string.

Databases: **PubMed**, **Scopus** and **PsycINFO** for every question
strategy (much of the aphasia literature, e.g. *Aphasiology*, is not in
MEDLINE). **OpenAlex** is not searched (amendment v3: PsycINFO, the third
database, added no benchmark paper beyond PubMed and Scopus; v2 had made
OpenAlex a conditional supplement). The gap strategies, when run, use
PubMed. Scopus and PsycINFO are run
in their own interface through UQ Library access with the string from
`screen.py strategies --show <id> --db scopus|psycinfo` (PsycINFO is
APA PsycInfo on EBSCOhost: TI/AB fields, `DE` subject headings, `ZC`
methodology; the subject headings are checked against the APA
Thesaurus before locking) and imported with `screen.py import
--strategy <id>`. Publication
years 2000 to the date of the search: from 2000, clinical MRI with
diffusion and perfusion imaging was routine, voxel-wise lesion–symptom
mapping (2003) and tractography followed, and lesion localisation
became comparable to what the KB maps onto atlases; for therapy and
prognosis, 2000 also marks contemporary stroke care (stroke units,
thrombolysis). PubMed and OpenAlex runs apply the window as a filter;
the Scopus string carries it (`PUBYEAR > 1999`). No language filter in
the search (language is a screening reason).

### 3.2 Locking and amendments

The protocol is this file plus `screening/strategies.yaml`. Its
fingerprint (sha256 of both) is stamped on every strategy run with the
strategy id, the protocol version and the commit. Before the first
protocol search: confirm the scope choices noted in `strategies.yaml`,
set `status: locked`, commit both files (and, optionally, register the
protocol on OSF with that commit). `screen.py search --strategy …
--execute` refuses to run while the status is draft or either file has
uncommitted changes; `--allow-unlocked` is for pilot runs and records
them as such.

A change after locking is an **amendment**: bump `version`, add an
entry under `amendments` (date, what, why — e.g. "q1: added *aphemia*;
benchmark paper C0045 was missed"), commit, and re-run the strategies
it affects. The register de-duplicates, so a re-run adds only what is
new; both runs stay in `searches.yaml`.

### 3.3 The benchmark and the recall check

`screen.py rebaseline --execute` (once, at the restart) moves every
legacy decision out of the screening history into the candidate's
`legacy` record and marks the 151 legacy includes `benchmark: true`.
They are papers already judged relevant and read in full, so they
measure the searches: **relative recall** is the share of benchmark
papers a strategy's runs retrieve, counted against the benchmark papers
whose findings sit in the KB folders the strategy serves (`buckets`).
Every `search`, dry run or not, prints this number and the papers it
missed; `screen.py recall` gives it per strategy, per database and
overall.

Before the title/abstract pass starts, each question strategy is run in
all its databases and every benchmark paper no search found is
classified: **out of scope** under §2 (excluded at full text with that
reason — it then leaves the recall denominator), a **search gap** (amend
the strategy and re-run), or a **pillar** the searches cannot reach
(citation chasing, §3.4). Benchmark papers published before 2000 are
reported separately and are not counted.
The target is ≥ 90 % relative recall per question strategy on in-scope
benchmark papers; the figure reached and the classification of the
misses are reported with the PRISMA diagram.

### 3.4 Citation chasing for pillar papers

Some papers the field rests on cannot come from the searches: published
before 2000 (Geschwind 1965, Dronkers 1996, Pedersen 1995), primary
healthy-volunteer studies (Saur 2008), records without an abstract
(Bates 2003), or reviews and studies whose records lack the search
terms. Such a paper enters as a **pillar** when an included paper cites
it as the source of a claim the KB records and the KB needs it for that
claim:

    python scripts/screen.py chase --doi <doi> --cited-by <included candidate ids> \
        --why "<the entry or claim that needs it>" --by <you> --execute

The citing papers must already be included under the protocol (a
person's full-text include), and the reason is required. The candidate
is marked `pillar: true` with a `citation_chasing` source (cited by,
why, who, when) and goes to full-text assessment in the
other-methods arm, where §2 applies except the publication years and the
healthy-volunteer rule. PRISMA reports these as identified by citation
searching.

### 3.5 Recording

Each search is one record in
`screening/searches.yaml` with the database, the verbatim query, the
filters, the date, who ran it, the number of hits and — the part that
makes coverage measurable — `for`: the evidence gaps
(`atlas_mapping/evidence_gaps.yaml`) or KB entries the search serves.
`screen.py search` runs PubMed (E-utilities) and OpenAlex live and
records all of that; Scopus, Embase, PsycINFO and Web of Science are
run in their own interface through UQ Library access and brought in
with `screen.py import --file export.ris` (RIS or CSV), with the query
and date given on the command line so the record is complete.

Searches are built per question family and per gap, not as one giant string:
a search for the thalamus / basal-ganglia gap is written and recorded
on its own, so the Coverage view can say how many candidates that gap
has had, screened, included and extracted. Re-run searches get a new
record (new date); the register de-duplicates.

**Other sources.** Benchmark papers that no protocol search
retrieves, hand-picked papers, papers found by citation chasing
from an extracted paper, papers suggested by the gap analysis, and
PDFs dropped into `papers/` and registered from their DOI all enter the
register through `screen.py backfill` (for what is already in
`citations.md`) or as candidates with `sources: [{kind: …}]`. PRISMA
2020 reports these as *identified via other methods*: they skip the
title/abstract pass and go straight to full-text assessment.

**De-duplication** happens in two passes. (1) On import, by DOI, then
PMID, then normalised title + year (never merging two records whose PMIDs
or DOIs differ): a record that matches an existing candidate adds its
search to that candidate's `sources` instead of creating a new one.
(2) After the last import and before screening, `screen.py dedupe` finds
what the first pass could not — the same title with publication years one
apart (epub vs print) and no conflicting identifiers — and marks each with
`duplicate_of` (the record with identifiers is kept; sources move to it).
Duplicates noticed during screening are merged the same way. PRISMA
"duplicates removed" is the database records retrieved minus the unique
candidates they became.

## 4. Screening

1. `python scripts/screen.py assist` — optional. The local model reads each
   unscreened title and abstract against §2 and writes a
   *suggestion* (decision, reason, one-line rationale) under the
   candidate's `suggestion` key. It is shown in the sheet and never
   becomes a decision, consistent with `GOVERNANCE.md`: a model may
   point, a person decides.
2. `python scripts/screen.py sheet` writes `screening/_sheet/title_abstract.html`
   (git-ignored): one card per candidate with title, abstract, links
   and the model's suggestion if any; keys `i` / `e` / `u`; an
   exclusion needs a reason. The sheet keeps your work in the browser
   and exports a CSV of decisions.
3. `python scripts/screen.py decide --csv decisions.csv --by <name>` records
   them, stamped with the person and the date, and appends a
   `SCREENED` line to `logs/extraction_log.md`. One decision can be
   recorded by hand with `--id/--stage/--decision/--reason`.
4. `python scripts/screen.py sheet --stage full_text` and the same `decide` for
   the full-text pass. `not_retrieved` is the reason for a full text
   that could not be obtained.
5. `python scripts/screen.py register --execute` writes a `citations.md` block
   for every included candidate that has none (Crossref, from the
   DOI) and sets its `key`. From here the paper is a normal citation:
   fetch the PDF into `papers/`, `intake_papers.py --execute`,
   `extract.py`, review, `promote.py` (`HOWTO.md`).

### 4.1 Prioritised title/abstract screening and the stopping rule

The title/abstract pass is prioritised (active learning, as in ASReview):
`python scripts/screen.py sheet --ranked --batch 200` writes the 200
records the model rates most likely relevant; after `decide`, the next
sheet is ranked again with those decisions included. The model
(`scripts/prioritise.py`) is TF-IDF features with multinomial Naive
Bayes, trained on the records a person has included (positives) and
excluded (negatives); until there are 50 exclusions, a seeded random
sample of unscreened records stands in for the negatives.

**Prior knowledge and validation.** The in-window benchmark papers are
split by a seeded hash (`prioritised_screening` in
`screening/strategies.yaml`): half are prior knowledge (positives from the
start), half are a **validation set** the model never sees as positive.
How early validation papers surface shows how well the ordering works.
In a cold-start test on the v1 PubMed pilot (titles only, no screening
decisions), 38 of 52 validation papers ranked in the top 30 % and 47 in
the top 50 %; abstracts and the screener's decisions improve this.

**Stopping rule** (all three must hold; `screen.py progress` shows them):

1. at least **15 %** of the database-arm records have been screened
   (30 % until amendment v3);
2. the last **200** decisions, in the order they were made, were all
   exclusions;
3. at least **95 %** of the validation papers the searches retrieved have
   been screened.

Then `screen.py stop --by <you> --execute` records every record still
awaiting the pass as not screened (reason `not_screened_stopping_rule`).
PRISMA reports them separately, with the three figures above. The
model only orders the sheet; every decision is a person's.

**Blind screening.** Title/abstract cards show the record as the
search returned it: no citation key, no "hand-picked" or legacy
provenance, so a legacy paper is judged like any other. At full text
the key is shown (the PDF is needed anyway).

**Dual screening on a sample.** One named screener makes the decision
of record for every candidate. A second person independently screens a
random 20 % of the title/abstract decisions and of the full-text
decisions (`screen.py sheet --check --sample 0.2 --seed <n>`, blind to
the first decision and to the model; the seed is reported), recorded
with `decide --role check`. `screen.py agreement` gives Cohen's kappa
per stage and lists the disagreements. Disagreements are resolved by
discussion and the agreed decision is recorded as a new decision of
record (it supersedes; all are kept). Kappa ≥ 0.6 is accepted; below
that, the ambiguous criterion in §2 is clarified (an amendment) and a
fresh sample is double-screened. The second screener may change over the
review; every check decision names its person, and `agreement` reports
kappa overall and for each second screener.

## 5. What is derived, not recorded

A candidate's record stops at inclusion. Everything after that is read
from where it already lives, so there is one source of truth per fact:

| State | Read from |
|---|---|
| registered (`key`) | `citations.md` has the `@Key` |
| PDF present | `papers/<Key>.pdf` |
| extracted / in review | `drafts/*/…__<Key>.md` with `status: draft` |
| rejected | every draft of the key has `status: rejected` |
| in the knowledge base | a canonical entry (`status: approved`) has a finding with `citation: @Key` |
| refused | `[refused]` tag in `citations.md` |

`screen.py status`, `kb_status.py` and the export compute these on the
fly (`screening.kb_facts`).

## 6. Reporting

`python scripts/screen.py status` prints the PRISMA 2020 numbers for both
identification arms and the coverage of each evidence gap;
`export_webapp.py` writes the same into the export's `screening` block,
and the explorer's **Coverage** view draws the flow diagram, the
exclusion reasons, the coverage table, the searches and a filterable
candidate table. For a manuscript, the diagram's numbers are the
export's — cite the KB commit shown in the explorer footer.

Papers that entered the bibliography before this protocol carry their
old decisions under `legacy` after the re-baseline (§3.3); they count
in PRISMA only through their new, protocol decisions — in the
databases arm when a search found them, otherwise as identified via
other methods. The report also gives: the protocol version and
fingerprint, the date and verbatim string of every search with its
hit count (PRISMA-S), relative recall per question strategy with the
classification of missed benchmark papers, and kappa per stage.

## 7. Files

```
SCREENING.md                  this protocol
screen.py                     strategies · rebaseline · search · import · recall · backfill · assist · sheet · decide · agreement · register · status · list
screening.py                  the register's data contract and derivations (used by export_webapp.py, kb_status.py)
screening/strategies.yaml     the pre-specified search strategies (protocol) (tracked)
screening/searches.yaml       one record per search run / import            (tracked)
screening/candidates.yaml     one record per candidate, with decisions       (tracked)
screening/abstracts.jsonl     abstract cache for the sheet and the model     (git-ignored; `screen.py fetch-abstracts` refills it)
screening/_sheet/*.html       the screening sheets                            (git-ignored)
```

Changing the eligibility criteria is a change to §2 of this file and
`screening.REASONS` together, and after locking it is an amendment
(§3.2); changing who may decide is a change to
`GOVERNANCE.md` and `screen.py decide` together.
