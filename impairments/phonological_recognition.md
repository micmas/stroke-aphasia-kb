---
schema_version: 2.7
id: phonological_recognition
name: Phonological recognition
kind: impairment
status: approved
review_tier: legacy
created_by: agent:claude-opus-4-7
created_on: 2026-05-01
short_definition: Underlying language component capturing phonemic discrimination
  — distinguishing word and non-word minimal pairs (PALPA 1 and PALPA 2). Distinct
  from phonological production (Factor 1, repetition + naming). One of five orthogonal
  factors recovered by PCA over the standard chronic-aphasia neuropsychological battery
  (Butler et al. 2014; Halai et al. 2017; Alyahya et al. 2018).
assessment:
- Non-word minimal pairs (PALPA 1)
- Word minimal pairs (PALPA 2)
findings: []
source: agent_draft
last_reviewed: '2026-05-06'
notes: 'First-extraction draft from Alyahya et al. 2018 (NounVerb). The

  phonological recognition PCA factor (Factor 4: 6.27% variance) is

  associated with a 4088-voxel cluster in superior temporal cortex

  including Heschl''s gyrus, planum temporale, and posterior STG. Three

  peak findings recorded.


  Loadings (Table 4) used to interpret this factor as "phonological

  recognition": non-word minimal pairs (.893), word minimal pairs

  (.816). Both are PALPA phoneme-discrimination tasks. Note that the

  factor loads minimally on production-side measures, justifying its

  separation from Factor 1.


  This factor has the lowest correlation with lesion volume (r=0.18,

  p=0.21), so the cluster is highly robust to lesion-volume control.

  The findings here are among the most lesion-volume-robust in the

  whole paper.'
reviewer: auto-reviewer
reviewed_on: '2026-05-05'
---
# Phonological recognition

## Component definition

Phonological recognition is the underlying language component
capturing phonemic discrimination — the ability to tell minimal pairs
of words and non-words apart (PALPA 1 and PALPA 2). It is conceptually
distinct from phonological production (Factor 1, which captures
repetition and naming) and from semantics. The factor accounts for
6.27% of the variance in the rotated PCA solution.

## Lesion correlates (per Alyahya 2018 NounVerb)

PCA-VBCM identifies a 4088-voxel cluster centered on the auditory
cortex region:

  - Planum temporale (Z=4.42)
  - Middle temporal gyrus (Z=4.31)
  - Heschl's gyrus (Z=3.96)
  - Angular gyrus (Z=3.40, cross-loaded with Factors 1 and 2)
  - Posterior supramarginal gyrus (Z=3.36, cross-loaded with Factor 1)
  - Posterior superior temporal gyrus (Z=3.32)

The Discussion (page 227) singles out Heschl's gyrus and planum
temporale as the headline regions, citing DeWitt & Rauschecker (2012)
and Mirman et al. (2015).

## Notes for next extraction round

  - Add left_heschls_gyrus, left_planum_temporale, left_posterior_superior_temporal_gyrus
    as region entries before re-extracting on the region side.
