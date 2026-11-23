---
schema_version: 2.7
id: executive_functions
name: Executive functions
kind: impairment
status: approved
created_by: agent:claude-opus-4-7
created_on: 2026-05-01
short_definition: Underlying cognitive component capturing non-linguistic executive
  control — rule anticipation and visuospatial reasoning. Loads heavily on the Brixton
  Spatial Anticipation Test and Raven's Coloured Progressive Matrices. One of five
  orthogonal factors recovered by PCA over the standard chronic-aphasia neuropsychological
  battery (Butler et al. 2014; Halai et al. 2017; Alyahya et al. 2018). Conceptually
  closer to a fluid-intelligence / cognitive-control construct than to language per
  se.
assessment:
- Brixton Spatial Anticipation Test (Burgess and Shallice 1997)
- Raven's Coloured Progressive Matrices (Raven 1962)
- Type-token ratio (negatively loaded fluency measure)
findings: []
source: agent_draft
last_reviewed: null
notes: 'First-extraction draft from Alyahya et al. 2018 (NounVerb). The

  executive function PCA factor (Factor 5: 4.6% variance — the smallest

  factor) did NOT yield significant clusters at the standard

  p<0.001 voxel threshold. Authors relaxed the threshold to p<0.005

  voxel-level, FWE p<0.05 cluster-level, recovering a 1085-voxel

  cluster in left superior frontal cortex. Three peak findings

  recorded with strength flagged as ''weak''.


  Loadings (Table 4) used to interpret this factor as "executive

  functions": Raven''s Coloured Progressive Matrices (.549), Brixton

  spatial anticipation test (.526), type-token ratio (-.591;

  negatively loaded). Visuospatial reasoning + verbal-diversity

  measures.


  Factor 5 has the lowest correlation with lesion volume (r=0.14,

  p=0.33), so the cluster IS robust to lesion-volume covariate at the

  relaxed threshold. The interpretation in the paper aligns this with

  generic prefrontal cognitive control (Duncan and Owen 2000), not a

  language-specific finding.'
reviewer: michele
reviewed_on: '2026-05-06'
---
# Executive functions

## Component definition

Executive functions in this paper means the non-linguistic cognitive
control component recovered by PCA — primarily fluid-reasoning and
rule-anticipation tasks (Raven's, Brixton). It is the smallest of the
five factors (4.6% of variance) and the only one that did not yield
significant lesion correlates at the standard threshold.

## Lesion correlates (per Alyahya 2018 NounVerb)

At a relaxed threshold (p<0.005 voxel-level, FWE-cluster p<0.05) a
1085-voxel left frontal cluster emerges:

  - Superior frontal gyrus (Z=3.65)
  - Paracingulate gyrus (Z=3.36)
  - Supplementary motor area (Z=3.27)
  - Pre-central gyrus (Z=2.96, also loaded on Factor 3)

The Discussion (page 228) interprets this as consistent with
prefrontal cognitive-control regions (Duncan & Owen 2000).

## Notes for next extraction round

  - Findings here have `strength: weak` because they required a
    relaxed threshold. Reviewers should consider whether Factor 5 is
    even worth promoting given it captures only 4.6% of variance and
    primarily indexes non-language cognition.
  - Add left_superior_frontal_gyrus, left_paracingulate_gyrus,
    left_supplementary_motor_area as region entries before re-extracting.
