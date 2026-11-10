---
schema_version: 2.8
id: left_angular_gyrus
name: "Left Angular Gyrus"
kind: classical
status: draft
created_by: "agent:ollama-extract-cli/gemma4:31b"
created_on: 2026-11-10
hemisphere: left
findings:
  - id: f1
    target: fluency
    target_kind: impairment
    claim: "Baseline microstructural integrity of the left angular gyrus predicts short-term recovery of discourse efficiency in subacute aphasia."
    direction: likely
    relationship: responder
    citation: "@Stockbridge2024"
    method: DTI
    design: longitudinal
    strength: moderate
    evidence_quality: cohort
    sample:
      n: 22
      population: "subacute post-stroke aphasia"
      time_post_onset: "within three months"
      phase: early_subacute
      age_range: "mean 69 (SD 13)"
      handedness: "right-handed"
      language: "English"
    statistics:
      threshold: "p < 0.05"
      effect_size: not_reported
    confounders_controlled: ["age", "days post onset"]
    confounders_not_controlled: []
    region_definition:
      kind: atlas
      atlas: "Brainnectome"
      description: "Left angular gyrus (AG) defined via Brainnectome map (IPL 6_5)."
    imaging_details:
      field_strength: "3T"
      reference_space: "MNI152"
      atlases_used: ["Brainnectome"]
      preprocessing_pipeline: "DSI studio with FSL eddy tool for motion/eddy current correction; resampled to 1mm isotropic"
      modalities:
        - modality: DTI
          sequence: "32 direction DWI"
          voxel_size_mm: [0.82, 0.82, 2.2]
          TR_ms: 7013
          TE_ms: 71
          b_values: [700]
    author_limitations:
      - "Small sample size with heterogeneous aphasia subtypes."
      - "Atlas-based segmentation performed in native diffusion space rather than coregistering with T1w or T2w maps."
    provenance:
      extracted_by: "agent"
      extracted_on: 2026-01-01
      paper_section: "Discussion, page 6"
      confidence: high
      flags: []
    source_passages:
      - section: "Discussion"
        page: 6
        quote: "In addition to age, lower diffusivity in the pITG, AG, AF, and SLF also significantly predicted better recovery of efficiency."
        supports: claim
      - section: "Statistical analyses"
        page: 4
        quote: "a series of regressions were calculated controlling for age and the number of days between stroke and the start of the study (days post onset)."
        supports: confounders
      - section: "Methods"
        page: 3
        quote: "we used embedded maps... AG (IPL 6_5; Brainnectome map)"
        supports: region_definition
      - section: "Limitations"
        page: 9
        quote: "One of the main limitations is small sample size with heterogeneous aphasia subtypes."
        supports: limitation
---
