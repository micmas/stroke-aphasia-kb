---
schema_version: 2.8
id: right_arcuate_fasciculus
name: "Right Arcuate Fasciculus"
kind: tract
status: draft
created_by: "agent:ollama-extract-cli/gemma4:31b-it-q8_0"
created_on: 2026-10-30
hemisphere: right
findings:
  - id: f1
    target: severity_metric
    target_kind: predictor
    claim: "Fractional anisotropy (FA) of the right arcuate fasciculus is a significant predictor of early subacute aphasia outcomes."
    direction: likely
    relationship: correlational
    citation: "@OsaGarcia2020"
    method: tractography
    design: longitudinal
    strength: weak
    evidence_quality: cohort
    sample:
      n: 20
      population: "individuals with post-stroke aphasia"
      time_post_onset: "<72 h (initial) and 10-14 days (follow-up)"
      phase: longitudinal
      age_range: "mean 71.6 (SD 12.45)"
      handedness: "all right-handed"
      language: "French or English"
    statistics:
      threshold: "P < 0.05"
      effect_size: "beta = 0.590"
      p_value: "0.023"
    confounders_controlled: []
    confounders_not_controlled: ["lesion volume", "age"]
    region_definition:
      kind: tract
      description: "Long segment of the right arcuate fasciculus"
    imaging_details:
      field_strength: "3T"
      modalities:
        - modality: T1
          sequence: MP-RAGE
          voxel_size_mm: [1, 1, 1]
          TR_ms: 2200
          TE_ms: 2.96
        - modality: DTI
          voxel_size_mm: [2, 2, 2]
          n_directions: 64
          b_values: [1000]
      preprocessing_pipeline: "Clusterize for lesion demarcation, FreeSurfer for ROI extraction, MRtrix3 for tensors/fiber orientation"
      reference_space: not_reported
      atlases_used: []
    author_limitations:
      - "Small sample size."
      - "The involvement of the right AF is much less significant when introduced into a multivariate model."
    provenance:
      extracted_by: "agent"
      extracted_on: 2026-01-01
      paper_section: "Results, page 5"
      confidence: high
      flags: ["reference_space not explicitly stated, likely MNI but not reported"]
    source_passages:
      - section: "Results"
        page: 5
        quote: "Among the diffusion measures, only FA from right AF was found to be a significant predictor of early subacute aphasia outcome."
        supports: claim
      - section: "Results"
        page: 5
        quote: "From these two variables, only rFA had a significant beta coefficient (beta = 0.590, P = 0.023)."
        supports: statistics
      - section: "Materials and Methods"
        page: 3
        quote: "The MRI protocol was acquired using a Skyra 3T MRI scanner... One high resolution 3D T1-weighted scan was acquired using a Magnetization Prepared Rapid Gradient Echo (MP-RAGE) sequence... A diffusion weighted imaging (DWI) series... (64 images with non-collinear diffusion gradients at b = 1,000 s/mm2)"
        supports: imaging_details
      - section: "Discussion"
        page: 6
        quote: "However, its involvement, as measured using FA, is much less significant when introduced into a multivariate model."
        supports: limitation
---
