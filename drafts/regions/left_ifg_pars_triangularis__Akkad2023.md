---
schema_version: 2.8
id: left_ifg_pars_triangularis
name: Left IFG Pars Triangularis (BA 45)
kind: classical
status: draft
created_by: agent:ollama-extract-cli/gemma4:31b-it-q8_0
created_on: 2026-10-30
hemisphere: left
findings:
- id: f1
  target: executive_functions
  target_kind: impairment
  claim: Damage to the left inferior frontal gyrus pars triangularis is associated with non-linguistic
    executive dysfunction in patients with chronic aphasia.
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
    effect_size: Z = 3.93
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
    description: Left Inferior Frontal Gyrus (Pars Triangularis)
  imaging_details:
    field_strength: 3T
    preprocessing_pipeline: SPM12 unified segmentation-normalisation procedure optimised for focal lesioned
      brains
    reference_space: MNI152
    atlases_used:
    - Harvard-Oxford
    coordinates_reported:
    - region: Left Inferior Frontal Gyrus (Pars Triangularis)
      mni:
      - -44
      - 36
      - 2
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
    quote: Performance on the executive functions factor was uniquely related to a cluster of voxels in
      the left frontal lobe, with peak voxels in the left dorsolateral prefrontal cortex and the left
      inferior frontal gyrus (LIFG, pars orbitalis and pars triangularis).
    supports: claim
  - section: Materials and methods
    page: 2
    quote: Thirty-six English speakers with chronic aphasia following a single left-hemisphere stroke
      participated in the study
    supports: sample
  - section: Materials and methods
    page: 2
    quote: All were at least 12 months post-stroke
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
  - section: Materials and methods
    page: 5
    quote: each participants' lesion volume was calculated [...] and this was entered as a covariate in
      the VBCM.
    supports: method
  - section: Conclusions
    page: 7
    quote: It is important to note that our findings are limited by a small sample size and should be
      interpreted with caution.
    supports: limitation
---
