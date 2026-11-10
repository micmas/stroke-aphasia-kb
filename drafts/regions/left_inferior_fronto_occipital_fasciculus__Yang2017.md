---
schema_version: 2.8
id: left_inferior_fronto_occipital_fasciculus
name: "Left Inferior Fronto-Occipital Fasciculus"
kind: tract
status: draft
created_by: "agent:ollama-extract-cli/gemma4:31b"
created_on: 2026-11-11
hemisphere: left
findings:
  - id: f1
    target: severity_metric
    target_kind: predictor
    claim: "Reduced white matter integrity of the left inferior fronto-occipital fasciculus is positively correlated with aphasia severity (WAB-AQ) in acute stroke."
    direction: likely
    relationship: correlational
    citation: "@Yang2017"
    method: DTI
    design: cross-sectional
    strength: moderate
    evidence_quality: cohort
    sample:
      n: 18
      population: "acute aphasia after stroke"
      time_post_onset: "average of 9.7 ± 5.3 days"
      phase: acute
      age_range: "53.67 ± 13.66 years"
      handedness: "all right-handed"
      language: "Chinese native speaker"
    statistics:
      threshold: "P < 0.05 (false discovery rate [FDR]-corrected)"
      effect_size: "R = 0.5754"
      p_value: "0.0125"
    confounders_controlled: []
    confounders_not_controlled: ["lesion volume"]
    region_definition:
      kind: atlas
      atlas: "JHU DTI-based white-matter atlases"
      description: "Left inferior fronto-occipital fasciculus (IFOF)"
    imaging_details:
      field_strength: "3.0T"
      acquisition:
        voxel_size_mm: [1, 1, 1]
        TR_ms: 8500
        TE_ms: 93
        sequence: "DTI"
      preprocessing_pipeline: "FSL v5.0, TBSS, non-linear alignment to FMRIB58 FA template"
      reference_space: MNI152
      atlases_used: ["JHU DTI-based white-matter atlases"]
    author_limitations:
      - "The sample size was relatively small for studies involving abnormal WM integrity in aphasia."
    provenance:
      extracted_by: "agent"
      extracted_on: 2026-01-01
      paper_section: "Results, page 4"
      confidence: high
      flags: []
    source_passages:
      - section: "Results"
        page: 4
        quote: "the left IFOF were positively correlated with the AQ (R = 0.5754, P = 0.0125)"
        supports: claim
      - section: "Materials and Methods"
        page: 2
        quote: "Eighteen aphasia patients (all right-handed, six females; age, 53.67 ± 13.66 years) were recruited"
        supports: sample
      - section: "Materials and Methods"
        page: 3
        quote: "underwent MRI for an average of 9.7 ± 5.3 days after stroke"
        supports: sample
      - section: "Statistical Analysis"
        page: 4
        quote: "A threshold of P < 0.05 (false discovery rate [FDR]-corrected) was used to indicate statistical significance."
        supports: statistics
      - section: "Discussion"
        page: 6
        quote: "First, the sample size was relatively small for studies involving abnormal WM integrity in aphasia."
        supports: limitation
---
