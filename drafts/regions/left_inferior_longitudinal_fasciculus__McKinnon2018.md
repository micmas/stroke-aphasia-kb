---
schema_version: 2.8
id: left_inferior_longitudinal_fasciculus
name: "Left Inferior Longitudinal Fasciculus"
kind: tract
status: draft
created_by: "agent:ollama-extract-cli/gemma4:31b"
created_on: 2026-11-10
hemisphere: left
members: []
networks: []
tracts_adjacent: []

findings:
  - id: f1
    target: anomia
    target_kind: impairment
    claim: "Reduced axonal density (AWF) in the posterior segment of the left inferior longitudinal fasciculus is associated with an increased frequency of semantic paraphasias during naming."
    direction: likely
    relationship: correlational
    citation: "@McKinnon2018"
    method: tractography
    design: cross-sectional
    strength: moderate
    evidence_quality: cohort
    sample:
      n: 29
      population: "chronic post-stroke aphasia"
      time_post_onset: "35 \u00b1 30 mos"
      phase: chronic
      age_range: "57 \u00b1 11 y"
      handedness: "right-handed"
      language: "native English"
    statistics:
      threshold: "p < 0.05 corrected"
      effect_size: "r = -0.67 (segment 1), r = -0.63 (segment 2)"
    confounders_controlled: ["white matter lesion overlap"]
    confounders_not_controlled: []
    region_definition:
      kind: tract
      description: "Deterministic kurtosis-based tractography seeded from JHU atlas ILF mask (thresholded at 25%)"
    imaging_details:
      field_strength: "3T"
      modalities:
        - modality: DWI
          sequence: multi-shell DKI
          voxel_size_mm: [2.7, 2.7, 2.7]
          TR_ms: 6100
          TE_ms: 101
          b_values: [0, 1000, 2000]
        - modality: T1
          sequence: MPRAGE
          voxel_size_mm: [1, 1, 1]
      preprocessing_pipeline: "DKE denoising, Gibbs ringing removal, FSL linear coregistration, enantiomorphic unified segmentation-normalization (Clinical Toolbox, SPM12)"
      reference_space: MNI152
      atlases_used: ["JHU atlas"]
    author_limitations:
      - "Small sample size and limited number of tracts studied."
      - "Tract nomenclature inconsistency (ILF may overlap with IFOF)."
      - "AWF model assumes axons are coplanar, which may be inaccurate in complex crossing areas."
    provenance:
      extracted_by: "agent"
      extracted_on: 2026-01-01
      paper_section: "Results, page 6"
      confidence: high
      flags: []
    source_passages:
      - section: "Results"
        page: 6
        quote: "semantic paraphasias had the highest relationship with the average AWF within the posterior portion of the ILF (segment 1: r = -0.67 and segment 2: r = -0.63, p < 0.05 corrected)."
        supports: claim
      - section: "Materials and Methods"
        page: 2
        quote: "We studied 32 participants with chronic post-stroke aphasia (age: 57 \u00b1 11 y, time post-stroke: 35 \u00b1 30 mos, gender: 8 women)."
        supports: sample
      - section: "Materials and Methods"
        page: 3
        quote: "All participants were scanned on a Siemens 3 T TIM Trio MRI scanner... using 30 diffusion-encoding directions acquired twice for each b = 1000 and b = 2000, as well as eleven additional images without diffusion weighting (b = 0), for a total of 131 volumes."
        supports: imaging_details
      - section: "Materials and Methods"
        page: 4
        quote: "Enantiomorphic unified segmentation-normalization was employed to calculate the spatial transformation between MNI and native T1-space (Clinical Toolbox, SPM12) taking into account lesions."
        supports: imaging_details
      - section: "Discussion"
        page: 9
        quote: "It is a limitation of this study that only the ILF and the SLF were studied in a small number of cases without the assessment of other tracts..."
        supports: limitation
---
