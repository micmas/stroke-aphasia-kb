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

The register sits upstream of everything in `HOWTO.md`. Nothing here
writes to `drafts/` or the canonical folders; an included paper is
handed to `intake_papers.py` exactly as a hand-picked one was.

## 1. Questions the knowledge base answers

A paper is relevant when it reports, for people with aphasia after
stroke, at least one of:

- **lesion → impairment**: an association between damage to a brain
  region, tract or network and a language or communication outcome
  (regions/, impairments/);
- **therapy → response**: the effect of a named therapy or ingredient
  on a language outcome, or who responds (therapies/, ingredients/);
- **predictor → outcome**: a demographic, clinical, lesion or genetic
  predictor of aphasia severity or recovery (predictors/);
- **synthesis**: a review or meta-analysis of any of the above
  (reviews/, since schema v2.4).

Healthy-volunteer imaging that maps a language function to anatomy is
in scope as *recruitment* evidence (see `schema.md`, relationship
`recruitment`); it must still concern a function the KB tracks.

## 2. Eligibility criteria

Screening is done in two passes — title/abstract, then full text — and
a candidate is excluded for exactly one reason from this list. The ids
are what `screen.py decide --reason` accepts and what the explorer
reports; change this list and `screening.REASONS` together.

| id | Exclude when… | Applies at |
|---|---|---|
| `not_stroke` | the population is not (post-)stroke: tumour, TBI, primary progressive aphasia, dementia, developmental; or healthy-only with no language-mapping question | both passes |
| `not_aphasia` | no aphasia, language or communication outcome is reported (e.g. motor recovery only, neglect only) | both passes |
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

**Database searches.** Each search is one record in
`screening/searches.yaml` with the database, the verbatim query, the
filters, the date, who ran it, the number of hits and — the part that
makes coverage measurable — `for`: the evidence gaps
(`atlas_mapping/evidence_gaps.yaml`) or KB entries the search serves.
`screen.py search` runs PubMed (E-utilities) and OpenAlex live and
records all of that; Scopus, Embase, PsycINFO and Web of Science are
run in their own interface through UQ Library access and brought in
with `screen.py import --file export.ris` (RIS or CSV), with the query
and date given on the command line so the record is complete.

Searches are built per gap or per entry, not as one giant string:
a search for the thalamus / basal-ganglia gap is written and recorded
on its own, so the Coverage view can say how many candidates that gap
has had, screened, included and extracted. Re-run searches get a new
record (new date); the register de-duplicates.

**Other sources.** Hand-picked papers, papers found by citation chasing
from an extracted paper, papers suggested by the gap analysis, and
PDFs dropped into `papers/` and registered from their DOI all enter the
register through `screen.py backfill` (for what is already in
`citations.md`) or as candidates with `sources: [{kind: …}]`. PRISMA
2020 reports these as *identified via other methods*: they skip the
title/abstract pass and go straight to full-text assessment.

**De-duplication** is by DOI, then PMID, then normalised title + year.
A record that matches an existing candidate adds its search to that
candidate's `sources` instead of creating a new one; `duplicate_of` on
a candidate marks a merge done by hand.

## 4. Screening

1. `python screen.py assist` — optional. The local model reads each
   unscreened title and abstract against §2 and writes a
   *suggestion* (decision, reason, one-line rationale) under the
   candidate's `suggestion` key. It is shown in the sheet and never
   becomes a decision, consistent with `GOVERNANCE.md`: a model may
   point, a person decides.
2. `python screen.py sheet` writes `screening/_sheet/title_abstract.html`
   (git-ignored): one card per candidate with title, abstract, links
   and the model's suggestion if any; keys `i` / `e` / `u`; an
   exclusion needs a reason. The sheet keeps your work in the browser
   and exports a CSV of decisions.
3. `python screen.py decide --csv decisions.csv --by <name>` records
   them, stamped with the person and the date, and appends a
   `SCREENED` line to `extraction_log.md`. One decision can be
   recorded by hand with `--id/--stage/--decision/--reason`.
4. `python screen.py sheet --stage full_text` and the same `decide` for
   the full-text pass. `not_retrieved` is the reason for a full text
   that could not be obtained.
5. `python screen.py register --execute` writes a `citations.md` block
   for every included candidate that has none (Crossref, from the
   DOI) and sets its `key`. From here the paper is a normal citation:
   fetch the PDF into `papers/`, `intake_papers.py --execute`,
   `extract.py`, review, `promote.py` (`HOWTO.md`).

One named screener decides each candidate (single screening with an
audit trail). The register supports more than one decision per stage —
a later decision by another person supersedes, and both are kept — so
dual screening can be adopted later without changing the format.

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

`python screen.py status` prints the PRISMA 2020 numbers for both
identification arms and the coverage of each evidence gap;
`export_webapp.py` writes the same into the export's `screening` block,
and the explorer's **Coverage** view draws the flow diagram, the
exclusion reasons, the coverage table, the searches and a filterable
candidate table. For a manuscript, the diagram's numbers are the
export's — cite the KB commit shown in the explorer footer.

Papers that entered the bibliography before this protocol (the 2026-10
backfill) carry decisions stamped `by: legacy` and are reported as
identified via other methods; the register does not claim a person
screened them. Re-screening them against §2 is a one-off task that the
full-text sheet supports (`screen.py sheet --stage full_text --ids …`).

## 7. Files

```
SCREENING.md                  this protocol
screen.py                     search · import · backfill · assist · sheet · decide · register · status · list
screening.py                  the register's data contract and derivations (used by export_webapp.py, kb_status.py)
screening/searches.yaml       one record per search run / import            (tracked)
screening/candidates.yaml     one record per candidate, with decisions       (tracked)
screening/abstracts.jsonl     abstract cache for the sheet and the model     (git-ignored; `screen.py fetch-abstracts` refills it)
screening/_sheet/*.html       the screening sheets                            (git-ignored)
```

Changing the eligibility criteria is a change to §2 of this file and
`screening.REASONS` together; changing who may decide is a change to
`GOVERNANCE.md` and `screen.py decide` together.
