---
schema_version: 2.8
id: left_posterior_stg
name: "Left Posterior Superior Temporal Gyrus"
kind: classical
status: draft
created_by: "agent:ollama-extract-cli/gemma4:31b-it-q8_0"
created_on: 2026-10-30
hemisphere: left
findings:
  - id: f1
    target: syntactic_processing
    target_kind: impairment
    claim: "Damage to the left posterior superior temporal gyrus is the strongest predictor of noncanonical sentence comprehension when performance on canonical sentences is controlled for."
    direction: likely
    relationship: causal
    citation: "@Kristinsson2020"
    method: RLSM
    design: cross-sectional
    strength: strong
    evidence_quality: cohort
    sample:
      n: 104
      population: "acute left-hemisphere stroke patients with aphasia"
      time_post_onset: "<20 days poststroke"
      phase: acute
      age_range: "mean 65.2 (SD 10.0) years"
      handedness: not_reported
      language: "English and Icelandic"
      cohort: not_reported
    statistics:
      threshold: "alpha level of .05"
      effect_size: "accounted for 19.2% of the variance in non-CAN residual scores"
      p_value: "<.001"
    lesion_mapping:
      analysis: region_based
      n_analysed: 104
      min_lesion_overlap: not_reported
      lesion_volume_correction: covariate
      multiple_comparisons: not_reported
    confounders_controlled:
      - "lesion volume"
      - "performance on canonical sentences"
    confounders_not_controlled: []
    region_definition:
      kind: atlas
      atlas: "Faria et al. (2012)"
      description: "posterior superior temporal gyrus (pSTG)"
    imaging_details:
      field_strength: "1.5T or 3T"
      preprocessing_pipeline: "SPM5 unified segmentation and normalization (Icelandic) or Clinical Toolbox/SPM12 enantiomorphic normalization (US)"
      reference_space: MNI152
      atlases_used: ["Faria et al. (2012)"]
    author_limitations:
      - "ROI-based approach compromises spatial resolution compared to voxel-based methods."
      - "Only a single measure of sentence comprehension was used."
      - "Behavioral performance was only examined in relation to structural damage, not cerebral perfusion."
    provenance:
      extracted_by: "agent"
      extracted_on: 2026-01-01
      paper_section: "Results, page 8-9"
      confidence: high
      flags: []
    source_passages:
      - section: "Abstract"
        page: 1
        quote: "damage to the posterior superior temporal gyrus predicted non-canonical scores when performance on canonical sentences was included as a cofactor."
        supports: claim
      - section: "Results"
        page: 9
        quote: "When variance accounted for by performance on CAN sentence structures was regressed out, the model predictive of non-CAN residual score included pSTG, IFGop, SMG, and IFGtri... The pSTG accounted for 19.2% of the variance."
        supports: statistics
      - section: "Discussion"
        page: 14
        quote: "Each ROI treated as an independent variable in our models is represented by a single number (proportional damage), regardless of the size of the ROI. Consequently, spatial resolution is compromised."
        supports: limitation
---
