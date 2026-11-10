---
schema_version: 2.8
id: left_arcuate_fasciculus
name: Left arcuate fasciculus
kind: tract
status: draft
created_by: agent:ollama-extract-cli/gemma4:31b
created_on: 2026-11-10
hemisphere: left
findings:
- id: f1
  target: semantics
  target_kind: impairment
  claim: Integrity of the left arcuate fasciculus is associated with lexical-semantic performance in the
    late chronic phase of recovery.
  direction: likely
  relationship: correlational
  citation: '@Keser2020'
  method: DTI
  design: longitudinal
  strength: moderate
  evidence_quality: cohort
  sample:
    n: 28
    population: patients with mild to severe language impairments after left hemispheric lobar and/or
      subcortical ischemic stroke
    time_post_onset: late chronic (11-13 months after stroke)
    phase: chronic
    language: native English-speaking
  statistics:
    threshold: FDR correction
    effect_size: r = -0.71
    p_value: '0.00065'
  confounders_controlled:
  - age
  - education
  - lesion load
  confounders_not_controlled: []
  region_definition:
    kind: atlas
    atlas: Human Connectome Project white matter atlas
    description: Atlas-based segmentation of the left AF warped into individual subject space with an
      FA threshold of 0.15.
  imaging_details:
    field_strength: 3T
    modalities:
    - modality: DTI
      sequence: DWI
      voxel_size_mm:
      - 0.82
      - 0.82
      - 2.2
      TR_ms: 7013
      TE_ms: 71
      n_directions: 32
      b_values:
      - 0
      - 700
    preprocessing_pipeline: dcm2nii/MRIconvert, DSIstudio eddy motion correction, resampled at 1mm isotropic
    reference_space: native
    atlases_used:
    - Human Connectome Project white matter atlas
  author_limitations:
  - Study is limited by a small sample size and missing time points.
  - Only one experienced rater of the imaging data was used.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Results, page 5
    confidence: high
    flags: []
  source_passages:
  - section: Results
    page: 5
    quote: at one year post-stroke, the strongest correlations were found between lexical-semantic performance
      and left AF radial diffusivity (r = -0.71, p = 0.00065).
    supports: claim
  - section: Methods
    page: 2
    quote: Twenty-eight native English-speaking patients... with clinically diagnosed mild to severe aphasia
      after left hemispheric lobar and subcortical ischemic stroke were enrolled in the study.
    supports: sample
  - section: Methods
    page: 4
    quote: The atlas-based segmentation function in DSI studio was then conducted to obtain atlas-based
      segmentation of the right and left AF... by warping Human Connectome Project white matter atlas...
      into individual subject space.
    supports: region_definition
  - section: Methods
    page: 4
    quote: Multivariable regression models and partial correlation analyses adjusted for age, education,
      and lesion load were conducted...
    supports: confounders
  - section: Discussion
    page: 8
    quote: our study is also limited by a small sample size, missing time points... and only one experienced
      rater of the imaging data.
    supports: limitation
---
