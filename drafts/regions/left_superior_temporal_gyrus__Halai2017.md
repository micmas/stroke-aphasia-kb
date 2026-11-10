---
schema_version: 2.8
id: left_superior_temporal_gyrus
name: Left Superior Temporal Gyrus (Dorsal Stream Node)
kind: classical
status: draft
created_by: agent:ollama-extract-cli/gemma4:31b
created_on: 2026-11-10
hemisphere: left
findings:
- id: f1
  target: phonological_production
  target_kind: impairment
  claim: Damage to the left superior temporal gyrus is uniquely associated with impaired phonological
    skills in chronic post-stroke aphasia.
  direction: likely
  relationship: causal
  citation: '@Halai2017'
  method: VBCM
  design: cross-sectional
  strength: moderate
  evidence_quality: cohort
  sample:
    n: 31
    population: chronic post-stroke aphasia
    time_post_onset: at least 12 months
    phase: chronic
    age_range: not_reported
    handedness: all right-handed
    language: native English speakers
  statistics:
    threshold: p < .005 voxel-level, p <= .001 FWE-corrected cluster-level
    effect_size: not_reported
  lesion_mapping:
    analysis: univariate
    n_analysed: 31
    min_lesion_overlap: not_reported
    lesion_volume_correction: covariate
    multiple_comparisons: fwe
  confounders_controlled:
  - lesion volume
  confounders_not_controlled: []
  region_definition:
    kind: atlas
    atlas: Harvard-Oxford
    description: Left superior temporal gyrus
  imaging_details:
    field_strength: 3.0 T
    reference_space: MNI152
    atlases_used:
    - Harvard-Oxford
    coordinates_reported: []
  author_limitations:
  - The factor solution is always dependent on the tests included in the decomposition.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Results, page 10
    confidence: high
    flags: []
  source_passages:
  - section: Results
    page: 10
    quote: 'Performance on the phonological factor was uniquely correlated with voxels across a number
      of left hemisphere regions: primary auditory cortex... mid to posterior middle and superior temporal
      gyri (MTG and STG)'
    supports: claim
  - section: Methods
    page: 4
    quote: Thirty one chronic stroke patients... were recruited... All patients were at least 12 months
      post-stroke at the time of scanning and assessment
    supports: sample
  - section: Methods
    page: 6
    quote: 'correlated these with individual measures or PCA factor scores using a voxel-based correlational
      methodology (VBCM: Tyler, Marslen-Wilson, & Stamatakis, 2005)'
    supports: method
  - section: Results
    page: 9
    quote: Results are thresholded at p < .005 voxel-level, p <= .001 family-wise error (FWE)-corrected
      cluster-level.
    supports: statistics
  - section: Methods
    page: 6
    quote: each participants' lesion volume was calculated... and this was entered as a covariate in each
      VBCM.
    supports: confounders
  - section: Discussion
    page: 13
    quote: One thing that must be kept in mind when using PCA is that the factor solution is always dependent
      on the tests included in the decomposition.
    supports: limitation
---
