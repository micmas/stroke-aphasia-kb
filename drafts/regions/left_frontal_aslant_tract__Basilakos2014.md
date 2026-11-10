---
schema_version: 2.8
id: left_frontal_aslant_tract
name: Left Frontal Aslant Tract
kind: tract
status: draft
created_by: agent:ollama-extract-cli/gemma4:31b
created_on: 2026-11-10
hemisphere: left
findings:
- id: f1
  target: fluency
  target_kind: impairment
  claim: Damage to the frontal aslant tract is associated with reduced speech fluency in chronic post-stroke
    aphasia.
  direction: likely
  relationship: causal
  citation: '@Basilakos2014'
  method: VBCM
  design: cross-sectional
  strength: strong
  evidence_quality: cohort
  sample:
    n: 76
    population: chronic left-hemisphere ischemic stroke aphasia
    time_post_onset: mean 35.57 months (SD = 47.56, range = 6-276)
    phase: chronic
    age_range: mean 61.35 years (SD = 12.67, range = 36-83)
    handedness: 73 right-handed
    language: not_reported
  statistics:
    threshold: Bonferroni corrected p = 0.008
    effect_size: r = 0.634
    p_value: < 0.001
  confounders_controlled:
  - lesion size
  confounders_not_controlled: []
  region_definition:
    kind: atlas
    atlas: Catani et al. (2012)
    description: white matter corresponding to the aslant tract
  imaging_details:
    field_strength: 3T
    reference_space: MNI152
    atlases_used:
    - ' '
    preprocessing_pipeline: SPM8 cost-function approach normalization to 1 mm isotropic ICBM standard
      brain template
    modalities:
    - modality: T1
      sequence: MP-RAGE (TFE)
      voxel_size_mm: not_reported
      TR_ms: 2250
      TE_ms: 4.2
    - modality: T2
      sequence: 3D SPACE
      TR_ms: 3200
      TE_ms: 352
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Results, page 3
    confidence: high
    flags:
    - lesion_mapping (v2.7 design) not extracted by the model — filled from statistics.threshold / confounders
      where the text says; check the Methods
  source_passages:
  - section: Results
    page: 3
    quote: aslant (r = 0.634, p < 0.001)... were correlated with speech fluency scores
    supports: claim
  - section: Materials and Methods - Participants
    page: 2
    quote: This study included 76 patients (32 female, 73 right-handed) with chronic aphasia... history
      of one single, left-hemisphere ischemic stroke
    supports: sample
  - section: Materials and Methods - Preprocessing of structural images
    page: 2
    quote: T1-signal intensity in white matter regions was used to relate cortical damage... to behavior
      (Tyler et al., 2005).
    supports: method
  - section: Materials and Methods - Region of interest analyses
    page: 3
    quote: To control for multiple comparisons in the correlation analyses, the alpha-level was Bonferroni
      corrected... threshold for significance was set to p = 0.008.
    supports: statistics
  - section: Materials and Methods - Region of interest analyses
    page: 3
    quote: A white matter atlas constructed by Catani et al. (2012) was consulted to define... the white
      matter corresponding to the aslant tract.
    supports: region_definition
  - section: Discussion
    page: 5
    quote: We observed that the integrity of the overlap between two previously reported white matter
      regions [aslant tract (Catani et al., 2013) and ASAF (Fridriksson et al., 2013)] was a significant
      predictor of fluency in post-stroke aphasia.
    supports: limitation
  author_limitations:
  - T1-signal intensity is an indirect measure of tissue integrity.
  - Use of WAB-R fluency scale is not a perfect measure of speech fluency as it is a forced-choice assignment.
  lesion_mapping:
    analysis: univariate
    n_analysed: 76
    min_lesion_overlap: not_reported
    lesion_volume_correction: covariate
    multiple_comparisons: bonferroni
---
