---
schema_version: 2.7
id: form_to_meaning
name: Form-to-meaning processing (ventral stream)
aliases:
- ventral stream (speech processing)
- lexical-semantic processing
- meaning-to-form processing
kind: impairment
status: approved
review_tier: legacy
created_by: agent:claude-opus-4-7
created_on: 2026-05-01
short_definition: 'Underlying processing component for the lexical-semantic aspects
  of speech: comprehension of single words and sentences, and lexical-semantic access
  for production. Operationally defined as the positive loadings of Principal Component
  2 in Fridriksson et al. 2018, indexed by sentence-comprehension impairment, auditory-comprehension
  impairment, semantic and phonological errors during naming, and sentence repetition.'
assessment:
- Western Aphasia Battery (WAB) — auditory verbal comprehension subtests
- Northwestern Assessment of Verbs and Sentences (NAVS) — Sentence Comprehension Test
- Philadelphia Naming Test (PNT) — semantic and phonological error scoring
- Sentence repetition tasks
findings: []
source: agent_draft
last_reviewed: '2026-05-06'
notes: 'First-extraction draft from Fridriksson et al. 2018 (PNAS). The

  paper''s primary finding is a data-driven empirical localization of

  the VENTRAL stream of speech processing — the positive loadings of

  Principal Component 2 from a VLSM-then-PCA pipeline on 71

  behavioural subscores in n=138 chronic LH stroke. The ventral

  stream is characterized as supporting "form-to-meaning"

  (lexical-semantic) processing.


  Seven findings extracted: posterior MTG and posterior STG (the two

  "anchoring" regions per the Discussion), uncinate fasciculus

  (>85% voxel coverage), posterior SMG, angular gyrus, pars

  orbitalis (anterior frontal endpoint), and anterior MTG.


  Together with the form_to_articulation draft (which captures the

  dorsal stream from the same Component 2 negative loadings), this

  pair of drafts represents the primary contribution of Fridriksson

  et al. 2018: a data-driven empirical localization of the

  ventral/dorsal dual streams of speech processing.


  Cohort: USC Aphasia Lab archival database, n=138 chronic LH

  stroke, ≥6 months post-stroke. Substantially overlaps with

  @Yourganov2015Predicting (same lab, n=98). Cohort-overlap flag is

  on every finding.'
reviewer: auto-reviewer
reviewed_on: '2026-05-05'
---
# Form-to-meaning processing (ventral stream)

## Component definition

Form-to-meaning processing is the data-driven ventral-stream
component recovered by Fridriksson et al. 2018. It is operationalized
as the positive loadings of Principal Component 2 (which together
with negative loadings explains 27% of variance after Component 1
captures lesion volume).

The component loads heavily on:
  - Sentence-comprehension impairment (NAVS Sentence Comprehension Test)
  - Auditory-comprehension impairment (yes/no questions)
  - Semantic and phonological errors during naming (PNT)
  - Sentence repetition

## Lesion correlates (per Fridriksson 2018)

The ventral stream is anchored on (Discussion page 4: "the areas
showing the greatest expression of Component 2"):

  - Posterior middle temporal gyrus — f1
  - Posterior superior temporal gyrus — f2

And extends via:
  - Uncinate fasciculus (>85% voxel coverage) — f3
  - Posterior supramarginal gyrus — f4
  - Angular gyrus — f5
  - Pars orbitalis (anterior frontal endpoint) — f6
  - Anterior middle temporal gyrus — f7

## Relationship to the dorsal stream (form-to-articulation)

The same Component 2's negative loadings identify the DORSAL
stream (form-to-articulation processing), captured in
`drafts/impairments/form_to_articulation__Fridriksson2018.md`. The
two streams are anatomically distinct but functionally interactive
— area Spt (Hickok & Poeppel 2007) sits at the boundary, and the
SMG splits into anterior (dorsal) vs posterior (ventral) sub-regions
right at this notch.

## Notes for next extraction round

  - Tables S3 and S4 (paper supplement) carry the full voxelwise
    loadings per region. A more exhaustive extraction could add
    findings for any S3/S4 region with strong Component 2 positive
    loadings.
  - The relationship between this ventral stream and Alyahya 2018's
    semantics PCA factor (also extracted in the KB) is theoretically
    similar but operationally distinct: Fridriksson runs VLSM-then-PCA;
    Alyahya runs PCA-then-VBCM. The two should converge but don't
    necessarily — comparing the canonical region entries when both
    sets of findings are promoted will be informative.
