---
schema_version: 2.8
id: left_caudate
name: "Left Caudate"
kind: classical
status: draft
created_by: "agent:ollama-extract-cli/gemma4:31b"
created_on: 2026-11-10
hemisphere: left
findings:
  - id: f1
    target: executive_functions
    target_kind: impairment
    claim: "Damage to the left caudate is associated with more severe executive dysfunction initially."
    direction: likely
    relationship: causal
    citation: "@Haldin2026"
    method: MLPA
    design: cross-sectional
    strength: moderate
    evidence_quality: cohort
    sample:
      n: 70
      population: "post-stroke aphasia"
      time_post_onset: "within 2 months post-stroke"
      phase: early_subacute
      age_range: "median 64.11 years"
      handedness: "94.44 % right-handed"
      language: "French"
    statistics:
      threshold: "p < 0.005, 5,000 permutations"
      effect_size: "z-values between 0 and -3.3"
    confounders_controlled: ["lesion volume", "age", "stroke subtype"]
    confounders_not_controlled: []
    region_definition:
      kind: atlas
      atlas: "AAL"
      description: "Left Caudate"
    lesion_mapping:
      analysis: multivariate
      n_analysed: 70
      min_lesion_overlap: ">= 10 % of the participants"
      lesion_volume_correction: covariate
      multiple_comparisons: permutation_fwe
    imaging_details:
      field_strength: "1.5T"
      reference_space: "MNI152"
      atlases_used: ["AAL"]
      coordinates_reported: [{region: "Left Caudate", mni: [-19.0, 25.7, 16.0]}]
    author_limitations:
      - "EF was assessed using an ad-hoc executive score that combines several executive skills."
    provenance:
      extracted_by: "agent"
      extracted_on: 2026-01-01
      paper_section: "Results, page 5"
      confidence: high
      flags: []
    source_passages:
      - section: "Results"
        page: 5
        quote: "Additionally, we identified two clusters... associated with greater EF deficits... The largest cluster (155 voxels) involved voxels in the left caudate (29 voxels)."
        supports: claim
      - section: "Materials and methods"
        page: 4
        quote: "regression of age and stroke subtype out of the EF score, and regression of lesion volume out of the lesion maps"
        supports: confounders
      - section: "Discussion"
        page: 8
        quote: "Second, EF was assessed using an ad-hoc executive score that combines several executive skills."
        supports: limitation
---
