---
schema_version: 2.8
id: brocas_aphasia
name: Broca's aphasia
kind: impairment
status: approved
review_tier: legacy
created_by: agent:claude-opus-4-7
created_on: 2026-05-01
short_definition: Non-fluent aphasia syndrome with effortful, halting speech, agrammatism,
  relatively preserved auditory comprehension, and impaired repetition. Classically
  associated with damage to left posterior inferior frontal cortex.
assessment:
- Western Aphasia Battery (WAB / WAB-R)
- Boston Diagnostic Aphasia Examination (BDAE)
findings: []
source: agent_draft
last_reviewed: '2026-05-06'
notes: 'Re-extraction draft from Yourganov 2015 (predictive relevance > 1

  thresholds in Table 3). Seven findings recorded, covering all eight

  regions in Table 3''s Broca''s column except the "arcuate (combined)"

  entry (Z = 1.91) — that entry is a redundant aggregation of the

  anterior + long + posterior segments which are recorded as

  individual findings (f1 anterior, f2 long; the posterior segment

  appears in conduction_aphasia rather than Broca''s).


  Per the multi-paper consolidation rule (schema.md), the canonical

  `ho-cort_44.md` already carries a Fridriksson 2018 finding (`f1`).

  When promote.py runs, this draft''s f3 (the Yourganov IFG-pars-

  opercularis finding) gets appended to that file as `f2` (or whatever

  the next available id is). The cohort-overlap flag on f3 makes the

  shared-cohort relationship explicit so interpret_overlap() doesn''t

  double-count.


  Anchored on impairment because the paper is a multi-class syndrome-

  classification study; per-region claims are most naturally

  organized by syndrome label.'
reviewer: auto-reviewer
reviewed_on: '2026-05-05'
---
# Broca's aphasia

## Clinical definition

Broca's aphasia is a non-fluent aphasia syndrome characterized by
effortful, halting speech production, agrammatism, relatively
preserved single-word auditory comprehension, and impaired
repetition. Classically associated with damage to left posterior
inferior frontal cortex (Broca's area, BA 44/45) and the underlying
white matter, though modern lesion-symptom evidence shows damage
typically extends well beyond classical Broca's area.

## Lesion correlates (per Yourganov 2015)

Multivariate SVM classification of 98 chronic stroke patients across
five aphasia types identifies the following regions as most
predictive of Broca's aphasia, ranked by predictive relevance
(weighted Z-score across pairwise classifications):

  - Anterior segment of arcuate fasciculus (Z = 3.2) — f1
  - Long segment of arcuate fasciculus (Z = 2.85) — f2
  - IFG pars opercularis / `ho-cort_44` (Z = 2.45) — f3
  - Rolandic operculum (Z = 2.2) — f4
  - Superior temporal gyrus (Z = 1.99) — f5
  - Arcuate fasciculus (combined; Z = 1.91) — covered by f1 + f2
  - Supramarginal gyrus (Z = 1.66) — f6
  - Heschl's gyrus (Z = 1.35) — f7

The Discussion (page 12) notes that damage limited to Broca's area
alone does NOT produce Broca's aphasia (Damasio 1992; Alexander 1987;
Mohr 1978; Fridriksson 2014); the syndrome requires a multivariate
signature of damage spanning the IFG, adjacent motor cortex, the
arcuate fasciculus, and (often) extending to STG / SMG / Heschl's.

## Important caveat: Broca's vs global at chance

Broca's vs global aphasia could not be classified above chance with
any atlas (Table 1). The Discussion attributes this to lesion-pattern
similarity between the two non-fluent syndromes and notes that global
aphasia often resolves to Broca's during recovery (Pedersen 2003).
