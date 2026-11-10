---
schema_version: 2.8
id: left_middle_longitudinal_fasciculus
name: "Left Middle Longitudinal Fasciculus"
kind: tract
status: draft
created_by: "agent:ollama-extract-cli/gemma4:31b"
created_on: 2026-11-10
hemisphere: left
findings:
  - id: f1
    target: anomia
    target_kind: impairment
    claim: "Disconnection of the left middle longitudinal fasciculus is associated with reduced naming abilities initially."
    direction: likely
    relationship: causal
    citation: "@Haldin2026"
    method: disconnectome
    design: cross-sectional
    strength: moderate
    evidence_quality: cohort
    sample:
      n: 61
      population: "post-stroke aphasia"
      time_post_onset: "within 2 months post-stroke"
      phase: early_subacute
      age_range: "median 64.11 years"
      handedness: "94.44 % right-handed"
      language: "French"
    statistics:
      threshold: "p < 0.005, 5,000 permutations"
      effect_size: "z-values ranging from 0 to -3.4"
    confounders_controlled: ["lesion volume", "age"]
    confounders_not_controlled: []
    region_definition:
      kind: tract
      atlas: "HCP1065"
      description: "Left Middle Longitudinal Fasciculus"
    lesion_mapping:
      analysis: multivariate
      n_analysed: 61
      min_lesion_overlap: ">= 10 % of the participants"
      lesion_volume_correction: covariate
      multiple_comparisons: permutation_fwe
    imaging_details:
      field_strength: "1.5T"
      reference_space: "MNI152"
      atlases_used: ["HCP1065"]
      coordinates_reported: [{region: "Left Middle Longitudinal Fasciculus", mni: [-35.9, -30.4, 4.9]}]
    author_limitations:
      - "The sample size for investigating the damaged brain structures associated with aphasia outcome or naming was relatively small."
    provenance:
      extracted_by: "agent"
      extracted_on: 2026-01-01
      paper_section: "Results, page 5"
      confidence: high
      flags: []
    source_passages:
      - section: "Results"
        page: 5
        quote: "We identified four clusters... associated with reduced naming abilities... The largest cluster (389 voxels) included voxels in the CC bilaterally (222 voxels) and the left middle longitudinal fasciculus (MdLF, 179 voxels)."
        supports: claim
      - section: "Materials and methods"
        page: 4
        quote: "regression of lesion volume out of both the naming score and the lesion maps, and regression of age out of the naming score"
        supports: confounders
      - section: "Discussion"
        page: 8
        quote: "First, the sample size for investigating the damaged brain structures associated with aphasia outcome or naming was relatively small."
        supports: limitation
---
