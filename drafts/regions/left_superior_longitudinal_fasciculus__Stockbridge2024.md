---
schema_version: 2.8
id: left_superior_longitudinal_fasciculus
name: "Left Superior Longitudinal Fasciculus"
kind: tract
status: draft
created_by: "agent:ollama-extract-cli/gemma4:31b"
created_on: 2026-11-10
hemisphere: left
findings:
  - id: f1
    target: anomia
    target_kind: impairment
    claim: "Baseline microstructural integrity of the left superior longitudinal fasciculus predicts short-term and long-term recovery of picture naming performance in subacute aphasia."
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
      atlas: "HCP842"
      description: "Left superior longitudinal fasciculus (SLF) defined via HCP842 map in DSI studio."
    imaging_details:
      field_strength: "3T"
      reference_space: "MNI152"
      atlases_used: ["HCP842"]
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
        quote: "Recovery following language treatment was significantly predicted by days since stroke and microstructural integrity of the pMTG, AF, and SLF... PNT improvement was significantly predicted by lower diffusivity in the pMTG and SLF and higher diffusivity in the pITG and AF."
        supports: claim
      - section: "Statistical analyses"
        page: 4
        quote: "a series of regressions were calculated controlling for age and the number of days between stroke and the start of the study (days post onset)."
        supports: confounders
      - section: "Methods"
        page: 3
        quote: "we used embedded maps... SLF (HCP842 map)"
        supports: region_definition
      - section: "Limitations"
        page: 9
        quote: "One of the main limitations is small sample size with heterogeneous aphasia subtypes."
        supports: limitation
---
