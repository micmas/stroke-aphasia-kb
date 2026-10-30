---
schema_version: 2.8
id: right_ifg_pars_opercularis
name: "Right Inferior Frontal Gyrus Pars Opercularis"
kind: classical
status: draft
created_by: "agent:ollama-extract-cli/gemma4:31b-it-q8_0"
created_on: 2026-10-30
hemisphere: right
findings:
  - id: f1
    target: severity_metric
    target_kind: predictor
    claim: "Lower fractional anisotropy in the right pars opercularis is associated with severe aphasia in chronic stroke patients."
    direction: likely
    relationship: correlational
    citation: "@Lee2018"
    method: DTI
    design: cross-sectional
    strength: moderate
    evidence_quality: cohort
    sample:
      n: 23
      population: "chronic left hemisphere stroke with aphasia"
      time_post_onset: "more than 6 months since onset of stroke"
      phase: chronic
      age_range: "mean 69.3-69.8 years"
      handedness: "right handedness before the stroke"
      language: "native Korean speaker"
    statistics:
      threshold: "Bonferroni-corrected P < 0.05"
      effect_size: "0.20 +/- 0.01 (severe group) vs 0.26 +/- 0.02 (control)"
    confounders_controlled: ["
      age"
    ]
    confounders_not_controlled: ["
      lesion volume"
    ]
    region_definition:
      kind: atlas
      atlas: "Harvard-Oxford Cortical and Subcortical Atlas"
      description: "pars opercularis identified via Harvard-Oxford atlas inbuilt in FSL 5.0.10"
    imaging_details:
      field_strength: "3T"
      modalities:
        - modality: DTI
          voxel_size_mm: [2, 2, 2]
          TR_ms: 9700
          TE_ms: 92.0
          n_directions: 30
          b_values: [1000]
          slice_thickness_mm: 2
      preprocessing_pipeline: "FSL 5.0.10 eddy current correction + SPM12 nonlinear transformation to MNI space + 4mm Gaussian smoothing"
      reference_space: MNI152
      atlases_used: ["Harvard-Oxford Cortical and Subcortical Atlas"]
    author_limitations:
      - "Small sample size, making it impossible to compare mild and moderate groups."
      - "Potential bias from cognitive defects affecting language skills."
      - "High average patient age and long duration after stroke may reflect brain degeneration."
    provenance:
      extracted_by: "agent"
      extracted_on: 2026-01-01
      paper_section: "Results, page 3"
      confidence: high
      flags: []
    source_passages:
      - section: "Results"
        page: 3
        quote: "Relative to the control group, group 2 exhibited significantly lower FA in the bilateral pars opercularis... (corrected P < 0.05)."
        supports: claim
      - section: "Patients and methods"
        page: 2
        quote: "Twenty-three patients with left hemisphere stroke with aphasia were recruited... (f) more than 6 months since onset of stroke"
        supports: sample
      - section: "MRI preprocessing"
        page: 2
        quote: "Specific areas of the brain were identified in accordance with the Harvard-Oxford Cortical and Subcortical Atlas inbuilt in FSL 5.0.10."
        supports: region_definition
      - section: "Statistical analysis"
        page: 2
        quote: "Significance was set at Bonferroni-corrected P value of less than 0.05."
        supports: statistics
      - section: "Discussion"
        page: 5
        quote: "Our study has several limitations, with the first one being its small sample size."
        supports: limitation
---
