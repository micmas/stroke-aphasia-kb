---
schema_version: 2.8
id: left_anterior_temporal_lobe
name: "Left Anterior Temporal Lobe"
kind: classical
status: draft
created_by: "agent:ollama-extract-cli/gemma4:31b-it-q8_0"
created_on: 2026-10-30
hemisphere: left
findings:
  - id: f1
    target: syntactic_processing
    target_kind: impairment
    claim: "Damage to the left temporal pole is associated with deficits in both sentence production and comprehension."
    direction: likely
    relationship: causal
    citation: "@Lukic2021"
    method: VLSM
    design: cross-sectional
    strength: strong
    evidence_quality: cohort
    sample:
      n: 76
      population: "chronic stroke-induced aphasia"
      time_post_onset: "8 to 209 months"
      phase: chronic
      age_range: "mean 58.6 years"
      handedness: "mixed"
      language: not_reported
    statistics:
      threshold: "p < .001 with cluster size and permutation-based correction"
      effect_size: not_reported
    lesion_mapping:
      analysis: univariate
      n_analysed: 76
      min_lesion_overlap: ">= 6 participants"
      lesion_volume_correction: covariate
      multiple_comparisons: permutation_fwe
    confounders_controlled: ["age", "months post onset", "education", "sex", "handedness", "total lesion volume", "verb production/comprehension"]
    confounders_not_controlled: []
    region_definition:
      kind: atlas
      atlas: "Harvard-Oxford Atlas"
      description: "Temporal Pole"
    imaging_details:
      field_strength: "3T"
      preprocessing_pipeline: "NUNDA anatomical preprocessing pipeline"
      reference_space: MNI152
      atlases_used: ["Harvard-Oxford Atlas"]
    author_limitations:
      - "Limited statistical power in frontal regions after verb processing deficits were partialed out."
    provenance:
      extracted_by: "agent"
      extracted_on: 2026-01-01
      paper_section: "Results, page 4"
      confidence: high
      flags: []
    source_passages:
      - section: "Abstract"
        page: 1
        quote: "Results revealed shared regions across domains in the anterior and posterior superior temporal gyri (aSTG, pSTG), and the temporal pole (adjusted for verb production/comprehension)."
        supports: claim
  - id: f2
    target: syntactic_processing
    target_kind: impairment
    claim: "The left temporal pole is a critical region specifically for sentence production over sentence comprehension."
    direction: likely
    relationship: causal
    citation: "@Lukic2021"
    method: VLSM
    design: cross-sectional
    strength: strong
    evidence_quality: cohort
    sample:
      n: 76
      population: "chronic stroke-induced aphasia"
      time_post_onset: "8 to 209 months"
      phase: chronic
      age_range: "mean 58.6 years"
      handedness: "mixed"
      language: not_reported
    statistics:
      threshold: "p < .001, the cluster size and permutation-based corrected"
      effect_size: not_reported
    lesion_mapping:
      analysis: univariate
      n_analysed: 76
      min_lesion_overlap: ">= 6 participants"
      lesion_volume_correction: covariate
      multiple_comparisons: permutation_fwe
    confounders_controlled: ["age", "months post onset", "education", "sex", "handedness", "total lesion volume", "sentence comprehension"]
    confounders_not_controlled: []
    region_definition:
      kind: atlas
      atlas: "Harvard-Oxford Atlas"
      description: "Temporal Pole"
    imaging_details:
      field_strength: "3T"
      preprocessing_pipeline: "NUNDA anatomical preprocessing pipeline"
      reference_space: MNI152
      atlases_used: ["Harvard-Oxford Atlas"]
    author_limitations:
      - "Limited statistical power in frontal regions after verb processing deficits were partialed out."
    provenance:
      extracted_by: "agent"
      extracted_on: 2026-01-01
      paper_section: "Results, page 4"
      confidence: high
      flags: []
    source_passages:
      - section: "Results"
        page: 4
        quote: "For sentence production (over sentence comprehension), a negative relationship was observed in the Planum Polare and Temporal Pole ( p < .001, the cluster size and permutation-based corrected)"
        supports: claim
---
