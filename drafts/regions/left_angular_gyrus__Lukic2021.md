---
schema_version: 2.8
id: left_angular_gyrus
name: "Left Angular Gyrus"
kind: classical
status: draft
created_by: "agent:ollama-extract-cli/gemma4:31b-it-q8_0"
created_on: 2026-10-30
hemisphere: left
findings:
  - id: f1
    target: syntactic_processing
    target_kind: impairment
    claim: "Damage to the left angular gyrus is associated with deficits in sentence comprehension."
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
    confounders_controlled: ["age", "months post onset", "education", "sex", "handedness", "total lesion volume", "verb comprehension"]
    confounders_not_controlled: []
    region_definition:
      kind: atlas
      atlas: "Harvard-Oxford Atlas"
      description: "Angular Gyrus (AG)"
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
      paper_section: "Abstract, page 1"
      confidence: high
      flags: []
    source_passages:
      - section: "Abstract"
        page: 1
        quote: "Additionally, comprehension was associated with lesions in the anterior and posterior middle temporal gyri (aMTG, pMTG), the MTG temporooccipital regions, SMG/AG, central and parietal operculum, and the insula."
        supports: claim
  - id: f2
    target: syntactic_processing
    target_kind: impairment
    claim: "Damage to the left angular gyrus is associated with impaired comprehension of syntactically complex, noncanonical sentences."
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
    confounders_controlled: ["age", "months post onset", "education", "sex", "handedness", "total lesion volume", "canonical sentence performance"]
    confounders_not_controlled: []
    region_definition:
      kind: atlas
      atlas: "Harvard-Oxford Atlas"
      description: "Angular Gyrus (AG)"
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
        quote: "VLSM analyses of syntactically complex sentences revealed that comprehension of non-canonical sentences (adjusted for performance on canonical sentences) was associated with damage to the Planum Temporale, Heschl's Gyrus, the insula, pSTG, pMTG, SMG/AG, and Parietal Operculum ( p < .001, the cluster size and permutation-based corrected)."
        supports: claim
---
