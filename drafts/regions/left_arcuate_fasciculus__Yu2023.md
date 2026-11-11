---
schema_version: 2.8
id: left_arcuate_fasciculus
name: "Left Arcuate Fasciculus"
kind: tract
status: draft
created_by: "agent:ollama-extract-cli/gemma4:31b"
created_on: 2026-11-10
hemisphere: left
findings:
  - id: f1
    target: severity_metric
    target_kind: predictor
    claim: "Integrity of the left long segment of the arcuate fasciculus (LSAF) is positively associated with overall aphasia severity in acute and subacute stroke."
    direction: likely
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
      threshold: "p < 0.05"
      effect_size: "ρ = 0.761"
    confounders_controlled: ["lesion volume"]
    confounders_not_controlled: []
    region_definition:
      kind: tract
      description: "Long segment of the arcuate fasciculus (LSAF) defined as streamlines going through frontal and parietal ROIs but not the temporal ROI."
    imaging_details:
      field_strength: "3.0 Tesla"
      reference_space: "MNI152"
      atlases_used: ["MNI152 atlas"]
      preprocessing_pipeline: "FSL (dcm2niigui, eddy_correct, BET v2.1, DTIFIT, FLIRT)"
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
        quote: "the mean FA values and fiber number of the left LSAF rather than the left UF was significantly positively associated with language domain scores (p < 0.05)."
        supports: claim
      - section: "Materials and Methods"
        page: 4
        quote: "Thirty-six participants... with acute/subacute PSA were recruited... time post-stroke less than 90 days"
        supports: sample
      - section: "Materials and Methods"
        page: 5
        quote: "The streamlines going through both ROI 1 and ROI 3 but not ROI 2 were defined as the LSAF"
        supports: region_definition
      - section: "Materials and Methods"
        page: 5
        quote: "All original T1-weighted and diffusion image data were pre-processed with the FM-RIB Software Library (FSL version 5.0.9 software package)"
        supports: imaging_details
      - section: "Results"
        page: 7
        quote: "When lesion volume was set as a controlled variable, partial correlation analyses revealed that the diffusion indices of the left LSAF still had moderately to strongly positive correlations with all language domain scores (p < 0.05)"
        supports: statistics
      - section: "Discussion"
        page: 13
        quote: "First, the sample of each group subject was relatively small, which limits the generalizability of the results."
        supports: limitation
    author_limitations:
      - "Small sample size limits generalizability."
      - "Deterministic fiber-tracking algorithm has disadvantages regarding crossed fiber tracking."
      - "Difficulty in measuring the UF due to susceptibility artifacts around the sinuses."
  - id: f2
    target: anomia
    target_kind: impairment
    claim: "Integrity of the left long segment of the arcuate fasciculus (LSAF) is positively associated with naming performance in acute and subacute stroke."
    direction: likely
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
      threshold: "p < 0.05"
      effect_size: "ρ = 0.639"
    confounders_controlled: ["lesion volume"]
    confounders_not_controlled: []
    region_definition:
      kind: tract
      description: "Long segment of the arcuate fasciculus (LSAF)."
    imaging_details:
      field_strength: "3.0 Tesla"
      reference_space: "MNI152"
      atlases_used: ["MNI152 atlas"]
      preprocessing_pipeline: "FSL"
    provenance:
      extracted_by: "agent"
      extracted_on: 2026-01-01
      paper_section: "Results, page 7"
      confidence: high
      flags: []
    source_passages:
      - section: "Results"
        page: 7
        quote: "the mean FA values and fiber number of the left LSAF rather than the left UF was significantly positively associated with language domain scores (p < 0.05)."
        supports: claim
      - section: "Results"
        page: 7
        quote: "the mean FA values and fiber number of the left LSAF had moderately to strongly positive correlations with scores of any language subsets"
        supports: statistics
    author_limitations:
      - "Small sample size limits generalizability."
  - id: f3
    target: fluency
    target_kind: impairment
    claim: "Integrity of the left long segment of the arcuate fasciculus (LSAF) is positively associated with speech fluency in acute and subacute stroke."
    direction: likely
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
      threshold: "p < 0.05"
      effect_size: "ρ = 0.459"
    confounders_controlled: ["lesion volume"]
    confounders_not_controlled: []
    region_definition:
      kind: tract
      description: "Long segment of the arcuate fasciculus (LSAF)."
    imaging_details:
      field_strength: "3.0 Tesla"
      reference_space: "MNI152"
      atlases_used: ["MNI152 atlas"]
      preprocessing_pipeline: "FSL"
    provenance:
      extracted_by: "agent"
      extracted_on: 2026-01-01
      paper_section: "Results, page 7"
      confidence: high
      flags: []
    source_passages:
      - section: "Results"
        page: 7
        quote: "the mean FA values and fiber number of the left LSAF rather than the left UF was significantly positively associated with language domain scores (p < 0.05)."
        supports: claim
    author_limitations:
      - "Small sample size limits generalizability."
  - id: f4
    target: form_to_meaning
    target_kind: impairment
    claim: "Integrity of the left long segment of the arcuate fasciculus (LSAF) is positively associated with auditory comprehension in acute and subacute stroke."
    direction: likely
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
      threshold: "p < 0.05"
      effect_size: "ρ = 0.637"
    confounders_controlled: ["lesion volume"]
    confounders_not_controlled: []
    region_definition:
      kind: tract
      description: "Long segment of the arcuate fasciculus (LSAF)."
    imaging_details:
      field_strength: "3.0 Tesla"
      reference_space: "MNI152"
      atlases_used: ["MNI152 atlas"]
      preprocessing_pipeline: "FSL"
    provenance:
      extracted_by: "agent"
      extracted_on: 2026-01-01
      paper_section: "Results, page 7"
      confidence: high
      flags: []
    source_passages:
      - section: "Results"
        page: 7
        quote: "the mean FA values and fiber number of the left LSAF rather than the left UF was significantly positively associated with language domain scores (p < 0.05)."
        supports: claim
    author_limitations:
      - "Small sample size limits generalizability."
  - id: f5
    target: phonological_production
    target_kind: impairment
    claim: "Integrity of the left long segment of the arcuate fasciculus (LSAF) is positively associated with speech repetition in acute and subacute stroke."
    direction: likely
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
      threshold: "p < 0.05"
      effect_size: "ρ = 0.768"
    confounders_controlled: ["lesion volume"]
    confounders_not_controlled: []
    region_definition:
      kind: tract
      description: "Long segment of the arcuate fasciculus (LSAF)."
    imaging_details:
      field_strength: "3.0 Tesla"
      reference_space: "MNI152"
      atlases_used: ["MNI152 atlas"]
      preprocessing_pipeline: "FSL"
    provenance:
      extracted_by: "agent"
      extracted_on: 2026-01-01
      paper_section: "Results, page 7"
      confidence: high
      flags: []
    source_passages:
      - section: "Results"
        page: 7
        quote: "the mean FA values and fiber number of the left LSAF rather than the left UF was significantly positively associated with language domain scores (p < 0.05)."
        supports: claim
    author_limitations:
      - "Small sample size limits generalizability."
---
