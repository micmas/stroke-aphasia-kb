---
schema_version: 2.8
id: left_uncinate_fasciculus
name: "Left Uncinate Fasciculus"
kind: tract
status: draft
created_by: "agent:ollama-extract-cli/gemma4:31b"
created_on: 2026-11-10
hemisphere: left
findings:
  - id: f1
    target: severity_metric
    target_kind: predictor
    claim: "Integrity of the left uncinate fasciculus (UF) is not significantly associated with overall aphasia severity in acute and subacute stroke."
    direction: no_effect
    relationship: correlational
    citation: "@Yu2023"
    method: DTI
    design: cross-sectional
    strength: moderate
    evidence_quality: cohort
    sample:
      n: 36
      population: "acute/subacute post-stroke aphasia"
      time_post_onset: "mean 36.56 ± 28.25 days"
      phase: early_subacute
      age_range: "25–78 years"
      handedness: "right-handed"
      language: "native Chinese"
    statistics:
      threshold: "p > 0.05"
      effect_size: "not_reported"
    confounders_controlled: []
    confounders_not_controlled: []
    region_definition:
      kind: tract
      description: "Uncinate fasciculus (UF) reconstructed using ROIs on the temporal stem and anterior white matter of the temporal lobe."
    imaging_details:
      field_strength: "3.0 Tesla"
      reference_space: "MNI152"
      atlases_used: ["MNI152 atlas"]
      preprocessing_pipeline: "FSL"
      modalities:
        - modality: T1
          sequence: MPRAGE
          voxel_size_mm: [1.1, 1.1, 1.1]
          TR_ms: 2300
          TE_ms: 2.98
        - modality: DTI
          sequence: EPI
          voxel_size_mm: [2.5, 2.5, 2.5]
          TR_ms: 7200
          TE_ms: 104
          n_directions: 64
          b_values: [0, 1000]
    provenance:
      extracted_by: "agent"
      extracted_on: 2026-01-01
      paper_section: "Results, page 7"
      confidence: high
      flags: []
    source_passages:
      - section: "Results"
        page: 7
        quote: "no significant correlation was found between diffusion indices of the left UF and language measures"
        supports: claim
      - section: "Materials and Methods"
        page: 4
        quote: "Thirty-six participants... with acute/subacute PSA were recruited"
        supports: sample
      - section: "Materials and Methods"
        page: 5
        quote: "To reconstruct the UF, the first ROI was placed on the temporal stem and anterior floor of the external/extrema capsules, and the second ROI was located in the anterior white matter of the temporal lobe"
        supports: region_definition
      - section: "Discussion"
        page: 13
        quote: "First, the sample of each group subject was relatively small, which limits the generalizability of the results."
        supports: limitation
    author_limitations:
      - "Small sample size limits generalizability."
      - "Difficulty in measuring the UF due to susceptibility artifacts around the sinuses."
---
