---
schema_version: 2.8
id: left_anterior_arcuate_fasciculus
name: Left anterior arcuate fasciculus
kind: tract
status: draft
created_by: agent:ollama-extract-cli/gemma4:31b
created_on: 2026-11-10
hemisphere: left
findings:
- id: f1
  target: fluency
  target_kind: impairment
  claim: Damage to the anterior segment of the left arcuate fasciculus is a primary predictor of long-term
    speech production impairments in chronic stroke.
  direction: likely
  relationship: causal
  citation: '@GajardoVidal2021'
  method: RLSM
  design: cross-sectional
  strength: strong
  evidence_quality: cohort
  sample:
    n: 134
    population: left-hemisphere stroke patients
    time_post_onset: at least 3 months post-stroke
    phase: chronic
    age_range: 31-87 years (mean 60)
    handedness: right handed pre-morbidly
    language: native speaker of English
    cohort: PLORAS
  statistics:
    threshold: P = 0.008
    effect_size: Beta = -0.330
  lesion_mapping:
    analysis: multivariate
    n_analysed: 134
    min_lesion_overlap: not_reported
    lesion_volume_correction: covariate
    multiple_comparisons: uncorrected
  confounders_controlled:
  - total lesion volume
  - months post-stroke
  - age at stroke
  - CAT semantic memory scores
  confounders_not_controlled: []
  region_definition:
    kind: atlas
    atlas: Natbrainlab
    description: Anterior segment of the arcuate fasciculus (aAF)
  author_limitations:
  - The use of atlas-based lesion load may lead to false negatives if only specific subparts of a region
    are critical.
  - White matter lesions likely damage multiple crossing fibres, making it difficult to isolate the effect
    of a single tract.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Results, page 824
    confidence: high
    flags:
    - ' cohort overlaps with @Saur2008, @White2024 (PLORAS database)'
  source_passages:
  - section: Results
    page: 824
    quote: Across all eight anatomical predictors included in Model 2, only lesion load in aAF reached
      statistical significance (P = 0.008).
    supports: statistics
  - section: Results
    page: 824
    quote: long-term speech production impairments (lasting beyond 3 months post-stroke) were solely predicted
      by the degree of damage to white matter, directly above the insula, in the vicinity of the anterior
      part of the arcuate fasciculus
    supports: claim
  - section: Materials and methods
    page: 4
    quote: Two (of three) white matter tracts were derived from the Natbrainlab atlas... These were the
      anterior segment of the arcuate fasciculus...
    supports: region_definition
  - section: Materials and methods
    page: 7
    quote: 'we factored out variance that was unrelated to lesion site by including the following regressors
      of no interest: (i) total lesion volume; (ii) months post-stroke; (iii) age at stroke; and (iv)
      scores from the CAT semantic memory task'
    supports: confounders
  - section: Limitations and future directions
    page: 12
    quote: Estimating the effect of damage only in terms of lesion load in atlas-based regions of interest
      may therefore lead to false negative results.
    supports: limitation
  imaging_details:
    reference_space: MNI152
    atlases_used:
    - Natbrainlab
    - Brainnetome
    preprocessing_pipeline: automated procedures reported in Seghier et al. (2008)
    field_strength: mixed (1.5T and 3T)
---
