---
schema_version: 2.8
id: left_middle_temporal_gyrus
name: Left Middle Temporal Gyrus (Ventral Stream Node)
kind: classical
status: draft
created_by: agent:ollama-extract-cli/gemma4:31b-it-q8_0
created_on: 2026-10-30
hemisphere: left
findings:
- id: f1
  target: semantics
  target_kind: impairment
  claim: Damage to the left middle temporal gyrus is associated with semantic deficits in chronic aphasia.
  direction: likely
  relationship: causal
  citation: '@Akkad2023'
  method: VBCM
  design: cross-sectional
  strength: moderate
  evidence_quality: cohort
  sample:
    n: 36
    population: adults with long-term speech production deficits caused by post-stroke aphasia
    time_post_onset: at least 12 months post-stroke
    phase: chronic
    language: English speakers
  statistics:
    threshold: p <= 0.001 voxel-level and p < 0.05 FWE corrected at cluster-level
    effect_size: Z = 4.14
  lesion_mapping:
    analysis: univariate
    n_analysed: 36
    min_lesion_overlap: not_reported
    lesion_volume_correction: covariate
    multiple_comparisons: fwe
  confounders_controlled:
  - lesion volume
  - age
  - time post-stroke
  confounders_not_controlled: []
  region_definition:
    kind: atlas
    atlas: Harvard-Oxford
    description: Left Middle Temporal Gyrus
  imaging_details:
    field_strength: 3T
    preprocessing_pipeline: SPM12 unified segmentation-normalisation procedure optimised for focal lesioned
      brains
    reference_space: MNI152
    atlases_used:
    - Harvard-Oxford
    coordinates_reported:
    - region: Left Middle Temporal Gyrus
      mni:
      - -62
      - -14
      - -12
  author_limitations:
  - Findings are limited by a small sample size and should be interpreted with caution.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Results, page 5; Table 3
    confidence: high
    flags: []
  source_passages:
  - section: Results
    page: 5
    quote: Performance on the semantic factor was uniquely related to two clusters in the left hemisphere
      with peak voxels in the superior/ middle temporal pole and superior/middle temporal gyrus.
    supports: claim
  - section: Materials and methods
    page: 2
    quote: Thirty-six English speakers with chronic aphasia following a single left-hemisphere stroke
      participated in the study
    supports: sample
  - section: Materials and methods
    page: 4
    quote: correlated these with PCA factor scores using a voxel-based correlational methodology (VBCM)
      (Tyler et al., 2005)
    supports: method
  - section: Results
    page: 5
    quote: Results are thresholded at p <= 0.001 voxel-level and p < 0.05 FWE corrected at cluster-level.
    supports: statistics
  - section: Conclusions
    page: 7
    quote: It is important to note that our findings are limited by a small sample size and should be
      interpreted with caution.
    supports: limitation
---
