# Practice and lived experience: Aphasia meaningful outcomes

This is a shared Stroke KB evidence section, not a third clinical condition.
The initial collection concerns adults with post-stroke aphasia. Future condition
collections need their own searches and eligibility records.

## Questions and eligibility

Q1 examines experiences, priorities, participation and living well. Q2 examines
personally meaningful outcomes and interpretation of change, including mixed-methods,
consensus, co-design and anchor-based studies. No imaging requirement applies.
Include patient perspectives and separately identifiable family/clinician perspectives
about post-stroke aphasia. Mixed populations require separable relevant findings.
At title/abstract screening, include means retain for full text. Missing abstracts
are not an exclusion reason. Exclude other aetiologies, unrelated questions and
reports without eligible findings. Pure efficacy, diagnostic accuracy or reliability
alone are outside these questions. Reviews support citation chasing; do not double
count their primary studies as independent participants. Record overlapping cohorts.

## Search and import

The 26 November 2026 exports use two searches per database across PubMed, MEDLINE
(EBSCO), Embase.com, CINAHL, PsycINFO, Scopus and Web of Science. The original
Manning 2019 strategy (10.1371/journal.pone.0214200.s007) is the methodological
foundation, not an exact reproduction. Q2 and relevant tool/intervention studies
expand its scope. No date/language filter was proposed. Query execution settings
still require checking against saved histories. MEDLINE was translated from Ovid
to EBSCO after the researcher identified the actual interface.

Run `python scripts/build_practice.py --exports <original export directory>`.
Source files remain unchanged outside Git. The tracked manifest contains only
search provenance and aggregate counts. Private records and abstracts are ignored.
All occurrence provenance is retained when deduplicating; conflicts stay separate.

## Screening, extraction and review

The private workspace uses separate title/abstract, full-text and evidence-review
stages. Records reach full text after that reviewer's title/abstract inclusion;
evidence review requires that reviewer's full-text inclusion. Each stage has
independent decisions and append-only audit events. Revising an upstream decision
hides later-stage work but preserves its audit record. Counts are per reviewer,
not adjudicated final systematic-review totals. Independent reviewers must reconcile
disagreements before reporting final included-study counts.

At evidence review record the claim, supporting source passage, source locator,
whose perspective is represented, context/limitations and an appraisal note.
For numeric meaningful-change findings also record measure, anchor, time after
stroke and estimation context; statistical detectable change is not MIC.
The workspace supports a paper-level evidence note, not automated extraction or
claim-level publication. Reviewed notes remain private until a human-authorised
publication workflow maps and checks individual findings. Public evidence sections
must show empty states until approved findings are published; they never load
Aphasia's lesion-based evidence as practice findings.

Qualitative thematic synthesis and numeric change estimates remain distinguishable.
Use design-appropriate appraisal and assess confidence in synthesis findings.
Report PRISMA 2020, PRISMA-S and ENTREQ with explicit review responsibilities.
