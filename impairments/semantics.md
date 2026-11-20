---
schema_version: 2.7
id: semantics
name: Semantics (semantic processing)
kind: impairment
status: approved
created_by: agent:claude-opus-4-7
created_on: 2026-05-01
short_definition: Underlying language component capturing semantic processing — comprehension
  and meaning-based judgments across receptive and expressive tasks (synonym judgments,
  picture-to-word matching, Camel & Cactus). One of five orthogonal factors recovered
  by PCA over the standard chronic-aphasia neuropsychological battery (Butler et al.
  2014; Halai et al. 2017; Alyahya et al. 2018).
assessment:
- Camel and Cactus Test — pictures (Cambridge Semantic Battery)
- 96-trial Synonym Judgment Test (Jefferies et al. 2009)
- Verb Synonym Judgment Test
- Spoken word-to-picture matching (Cambridge Semantic Battery)
- Written word-to-picture matching
- Spoken Sentence Comprehension (CAT)
- Picture-to-word matching (noun and verb)
findings: []
source: agent_draft
last_reviewed: null
notes: 'First-extraction draft from Alyahya et al. 2018 (NounVerb). The

  semantic PCA factor (Factor 2: 11.5% variance) is associated with the

  largest cluster in the entire analysis (8326 voxels) spanning

  occipito-temporal cortex, anterior temporal lobe (including the

  temporal pole), the inferior longitudinal fasciculus, and precuneus.

  Five strongest peaks recorded as separate findings.


  Loadings (Table 4) used to interpret this factor as "semantics":

  Camel and Cactus pictures (.873), verb picture-to-word matching

  (.829), noun picture-to-word matching (.816), verb synonym judgment

  (.799), 96-synonym judgment (.798), written word-to-picture matching

  (.778), spoken word-to-picture matching (.756), spoken sentence

  comprehension (.613), Raven''s Coloured Progressive Matrices (.563),

  noun naming OANB (.617).


  Important caveat: the semantic factor showed mild correlation with

  lesion volume (r=0.37, p=0.01); when lesion volume was partialled

  out, the cluster shrank and was limited to occipital sub-regions

  (superior + inferior lateral occipital cortex, precuneus, occipital

  fusiform). Temporal-lobe peaks (temporal pole, anterior MTG) did NOT

  survive that covariate. Reviewers should weigh this when promoting

  individual findings.'
reviewer: michele
reviewed_on: '2026-05-06'
---
# Semantics (semantic processing)

## How to read this entry

First-extraction draft from Alyahya et al. 2018 (NounVerb). Defines
"semantics" as a draft impairment-like component ID and lists the
brain regions whose tissue concentration uniquely covaries with the
semantic PCA factor (Factor 2).

## Component definition

Semantics is the underlying language component capturing semantic
processing across both receptive (synonym judgments, picture-to-word
matching) and expressive (naming) tasks. In Alyahya et al. it accounts
for 11.5% of variance and is conceptually distinct from phonological
production (Factor 1), fluency (Factor 3), phonological recognition
(Factor 4), and executive function (Factor 5). Factor loadings concentrate
on Camel & Cactus, synonym judgments (verbal and verb-specific), and
picture-to-word matching tasks.

## Lesion correlates (per Alyahya 2018 NounVerb)

PCA-VBCM identifies an 8326-voxel cluster — the largest in the analysis —
with peaks in:

  - Superior lateral occipital cortex (Z=5.53)
  - Precuneus cortex (Z=5.01)
  - Inferior longitudinal fasciculus (Z=4.67)
  - Anterior temporal fusiform cortex (Z=4.67)
  - Anterior inferior temporal gyrus (Z=4.28)
  - Posterior inferior temporal gyrus (Z=4.12)
  - Posterior middle temporal gyrus (Z=4.04)
  - Anterior middle temporal gyrus (Z=3.90)
  - Temporal pole (Z=3.78)

When lesion volume is partialled out, the cluster shrinks substantially
and survives only in the left superior and inferior lateral occipital
cortex, precuneus, and occipital fusiform gyrus. Temporal-lobe peaks
do not survive that covariate.

## Notes for next extraction round

  - Add left_anterior_middle_temporal_gyrus, left_temporal_pole,
    left_superior_lateral_occipital_cortex, left_inferior_longitudinal_fasciculus,
    left_precuneus as region entries before re-extracting on the region
    side.
  - When promoting these findings, prioritise occipital peaks
    (left_superior_lateral_occipital_cortex, left_precuneus) since they are the
    only ones that survive lesion-volume control.
