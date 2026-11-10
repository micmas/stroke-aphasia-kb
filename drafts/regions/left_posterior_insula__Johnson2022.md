---
schema_version: 2.8
id: left_posterior_insula
name: "Left Posterior Insula"
kind: classical
status: draft
created_by: "agent:ollama-extract-cli/gemma4:31b"
created_on: 2026-11-10
hemisphere: left
findings:
  - id: f1
    target: severity_metric
    target_kind: predictor
    claim: "Damage to the left posterior insula is associated with more severe aphasia (lower WAB-AQ scores) in chronic stroke."
    direction: likely
    relationship: causal
    citation: "@Johnson2022"
    method: LSM
    design: cross-sectional
    strength: moderate
    evidence_quality: cohort
    sample:
      n: 224
      population: "chronic left-hemisphere stroke"
      time_post_onset: ">= 6 months"
      phase: chronic
      age_range: "21-85 years"
      handedness: "pre-morbidly right-handed"
      language: not_reported
    statistics:
      threshold: "P < .05, corrected for multiple comparisons using permutation thresholding (5000 permutations)"
      effect_size: "z = 3.15"
    confounders_controlled: ["total lesion volume"]
    confounders_not_controlled: []
    region_definition:
      kind: atlas
      atlas: "JHU neuroanatomical atlas"
      description: "posterior insula"
    lesion_mapping:
      analysis: univariate
      n_analysed: 224
      min_lesion_overlap: ">= 10% (N = 22)"
      lesion_volume_correction: covariate
      multiple_comparisons: permutation_fwe
    imaging_details:
      field_strength: not_reported
      reference_space: MNI152
      atlases_used: ["JHU"]
      preprocessing_pipeline: "T2 aligned to T1; enantiomorphic normalization to MNI space"
    author_limitations:
      - "Retrospective nature of the study may lead to unrepresentative samples."
      - "Use of residual values for non-lesion predictors may compromise ease of interpretability."
    provenance:
      extracted_by: "agent"
      extracted_on: 2026-01-01
      paper_section: "Results, page 381"
      confidence: high
      flags: []
    source_passages:
      - section: "Results"
        page: 381
        quote: "The LSM analysis to predict WAB-AQ revealed one white matter tract and one cortical region, which, when damaged, were associated with more severe aphasia: the superior longitudinal fasciculus (SLF; z = 3.64) and posterior insula (z = 3.15; Fig. 2B and C)."
        supports: claim
      - section: "Materials and methods"
        page: 385
        quote: "P-values < .05, corrected for multiple comparisons using permutation thresholding (5000 permutations), while also controlling for total lesion volume as a nuisance regressor"
        supports: statistics
      - section: "Materials and methods"
        page: 385
        quote: "Areas that were damaged in at least 10% (N = 22) of participants were included in analysis."
        supports: method
      - section: "Discussion"
        page: 386
        quote: "Due to the retrospective nature of the present study, there are several limitations that should be considered when interpreting the results."
        supports: limitation
---
