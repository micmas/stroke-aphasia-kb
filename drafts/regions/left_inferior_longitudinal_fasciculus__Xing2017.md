---
schema_version: 2.8
id: left_inferior_longitudinal_fasciculus
name: "Left Inferior Longitudinal Fasciculus"
kind: tract
status: draft
created_by: "agent:ollama-extract-cli/gemma4:31b-it-q8_0"
created_on: 2026-10-30
hemisphere: left
findings:
  - id: f1
    target: syntactic_processing
    target_kind: impairment
    claim: "Reduced white matter integrity in the left inferior longitudinal fasciculus is associated with auditory sentence-level comprehension deficits in chronic post-stroke aphasia."
    direction: likely
    relationship: correlational
    citation: "@Xing2017"
    method: DTI
    design: cross-sectional
    strength: moderate
    evidence_quality: cohort
    sample:
      n: 40
      population: "chronic left hemisphere stroke survivors"
      time_post_onset: "at least 6 months post-stroke"
      phase: chronic
      age_range: "59.6 +/- 10.1 years"
      handedness: "33/6/1 (R/L/ambidextrous)"
      language: "native English speaker"
    statistics:
      threshold: "P < (0.05/4) = 0.0125 (Bonferroni correction)"
      effect_size: "RFA = 0.382, RMD = -0.461, RAD = -0.457, RRD = -0.453"
      p_value: "0.02"
    confounders_controlled:
      - "age"
      - "total lesion volume"
      - "lesion load on the tract"
    confounders_not_controlled: []
    region_definition:
      kind: tract
      description: "Reconstructed using probabilistic tractography in healthy older participants."
    imaging_details:
      field_strength: "3.0-T"
      modalities:
        - modality: T1
          sequence: "high-resolution T1-weighted"
          voxel_size_mm: [1, 1, 1]
          TR_ms: 1900
          TE_ms: 2.56
        - modality: DTI
          sequence: "single-shot echo-planar imaging"
          voxel_size_mm: [2.5, 2.5, 2.5]
          TR_ms: 7500
          TE_ms: 87
          n_directions: 60
          b_values: [0, 300, 1100]
      preprocessing_pipeline: "FSL diffusion toolbox + FNIRT non-linear registration to MNI template"
      reference_space: MNI152
      atlases_used: []
    author_limitations:
      - "Lack of objective measures of individual tracts in patients due to varied lesions; used group-based probability maps."
      - "Did not determine involvement of left hemisphere cortical areas."
    provenance:
      extracted_by: "agent"
      extracted_on: 2026-01-01
      paper_section: "Results, page 4"
      confidence: high
      flags: []
    source_passages:
      - section: "Abstract"
        page: 1
        quote: "Posterior temporal white matter integrity loss and involvement of the inferior longitudinal fasciculus related to sentence-level comprehension deficits"
        supports: claim
      - section: "Materials and Methods - Participants"
        page: 2
        quote: "Forty (14 females) chronic left hemisphere stroke survivors were recruited... native English speaker; at least 6 months post-stroke"
        supports: sample
      - section: "Materials and Methods - Image Acquisition"
        page: 3
        quote: "Subjects were scanned on a 3.0-T Siemens Trio scanner... high-resolution T1-weighted images... Diffusion data were acquired using a single-shot echo-planar imaging sequence"
        supports: imaging_details
      - section: "Statistical Analysis"
        page: 4
        quote: "we considered tracts that showed significant correlations with behavior for the each DTI index at a threshold of P < (0.05/4) = 0.0125 (Bonferroni correction)."
        supports: statistics
      - section: "Results"
        page: 4
        quote: "DTI metrics in the left ILF significantly related to the SLC scores, with significant correlations with MD, AD, RD, and a marginal correlation with FA (corrected P < 0.05)"
        supports: statistics
      - section: "Discussion"
        page: 8
        quote: "First, lack of objective measures of the individual tracts in patients is a main caveat of this study."
        supports: limitation
---
