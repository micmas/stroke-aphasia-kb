---
schema_version: 2.7
id: form_to_articulation
name: Form-to-articulation processing (dorsal stream)
aliases:
- dorsal stream (speech processing)
- phonological-motor processing
- motor-phonological speech processing
kind: impairment
status: approved
review_tier: legacy
created_by: agent:claude-opus-4-7
created_on: 2026-05-01
short_definition: 'Underlying processing component for the motor-phonological aspects
  of speech: articulation, phonological encoding for production, and motor planning.
  Operationally defined as the negative loadings of Principal Component 2 in Fridriksson
  et al. 2018, indexed by apraxia-of-speech severity, articulation errors during picture
  naming, total verbal output in connected speech, and spoken phonological errors.'
assessment:
- Apraxia Battery for Adults, second edition (ABA-2)
- Apraxia of Speech Rating Scale (ASRS)
- Philadelphia Naming Test (PNT) — articulation/phonological error scoring
- Connected speech analysis — total verbal output (Grandfather Passage, picture description)
findings: []
source: agent_draft
last_reviewed: '2026-05-06'
notes: 'First-extraction draft from Fridriksson et al. 2018 (PNAS). The

  paper''s primary finding is a data-driven empirical localization of

  the DORSAL stream of speech processing — the negative loadings of

  Principal Component 2 from a VLSM-then-PCA pipeline on 71

  behavioural subscores in n=138 chronic LH stroke. The dorsal

  stream is characterized as supporting "form-to-articulation"

  processing.


  Five findings extracted: pars opercularis (ho-cort_44 — legacy id

  retained), lateral premotor cortex, middle frontal gyrus (the

  three "highest expression" regions per the Discussion), anterior

  supramarginal gyrus (the inferior-parietal endpoint of the dorsal

  stream), and precentral gyrus.


  Component 1 of the same PCA was essentially the lesion-volume

  spatial pattern (47% variance, r=-0.78 with cohort lesion-overlap

  map) — that''s a strong replication of "lesion volume → severity"

  but not a region-specific finding, so it is captured in the

  file-level notes here rather than as a separate finding.


  Cohort: USC Aphasia Lab archival database, n=138 chronic LH

  stroke, ≥6 months post-stroke. Substantially overlaps with

  @Yourganov2015Predicting (same lab, n=98, same enrolment window

  2007–2014). The flag for cross-paper cohort overlap is on every

  finding here.


  Important note for promote.py: the canonical `regions/ho-cort_44.md`

  already cites @Fridriksson2018 in its `f1` finding but with

  `[PLACEHOLDER]` source passages. When promoting f1 of THIS draft,

  the placeholders in the canonical entry should be replaced with the

  real source_passages from this draft (or this draft''s f1 should

  append as a new finding `f2` and the placeholder `f1` should be

  flagged for deletion or completion).'
reviewer: auto-reviewer
reviewed_on: '2026-05-05'
---
# Form-to-articulation processing (dorsal stream)

## Component definition

Form-to-articulation processing is the data-driven dorsal-stream
component recovered by Fridriksson et al. 2018 from a VLSM-then-PCA
analysis on n=138 chronic LH stroke patients. It is operationalized
as the negative loadings of Principal Component 2 (which together
with positive loadings explains 27% of variance after Component 1
captures lesion volume).

The component loads heavily on:
  - Apraxia-of-speech severity (ABA-2; Apraxia of Speech Rating Scale)
  - Articulation errors during picture naming (PNT)
  - Total verbal output in connected speech (Cookie theft, Grandfather Passage)
  - Spoken phonological errors

## Lesion correlates (per Fridriksson 2018)

The dorsal stream is anchored on (Discussion page 4 highlights the
top three):

  - IFG pars opercularis (the canonical Broca's area, `ho-cort_44`) — f1
  - Lateral premotor cortex — f2
  - Middle frontal gyrus — f3

Plus extending to:
  - Anterior supramarginal gyrus (inferior parietal endpoint) — f4
  - Precentral gyrus (primary motor cortex) — f5

Adjacent white-matter tracts also load on the dorsal stream but are
not extracted here as separate findings (the paper does not name
specific tracts in its main text — see Tables S3/S4 for the full
voxelwise list).

## Relationship to the ventral stream (form-to-meaning)

The same Component 2's positive loadings identify the VENTRAL
stream (form-to-meaning processing), captured in
`drafts/impairments/form_to_meaning__Fridriksson2018.md`. The two
streams are anatomically distinct but functionally interactive — the
paper notes that conduction aphasia (impaired interaction between
the streams at area Spt) and Wernicke's aphasia (ventral damage with
secondary production effects) both illustrate the cross-stream
interaction.

## Notes for next extraction round

  - The canonical `regions/ho-cort_44.md` has placeholder source
    passages for its existing Fridriksson 2018 finding. promote.py
    should replace the placeholders with the real passages from this
    draft.
  - Tables S3 and S4 (paper supplement) contain the full voxelwise
    loadings per region. A future, more thorough extraction could
    add additional findings for any S3/S4 region with a strong
    Component 2 negative loading.
