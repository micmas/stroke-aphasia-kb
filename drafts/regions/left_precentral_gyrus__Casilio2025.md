---
schema_version: 2.8
id: left_precentral_gyrus
name: "Left Precentral Gyrus"
kind: classical
status: draft
created_by: "agent:ollama-extract-cli/gemma4:31b-it-q8_0"
created_on: 2026-10-30
hemisphere: left
findings:
  - id: f1
    target: syntactic_processing
    target_kind: impairment
    claim: "Damage to the left precentral gyrus is associated with agrammatism (grammatical omissions) in naturalistic language production."
    direction: likely
    relationship: causal
    citation: "@Casilio2025"
    method: VLSM
    design: cross-sectional
    strength: strong
    evidence_quality: cohort
    sample:
      n: 118
      population: "acute post-stroke aphasia"
      time_post_onset: "1-5 days post-onset"
      phase: acute
      age_range: "18-90 years"
      handedness: "105 right; 11 left; 2 ambidextrous"
      language: "English"
    statistics:
      threshold: "corrected P < 0.05"
      effect_size: "maximum t = 4.92"
      p_value: "0.005"
    lesion_mapping:
      analysis: univariate
      n_analysed: 118
      min_lesion_overlap: ">= 6 patients"
      lesion_volume_correction: covariate
      multiple_comparisons: permutation_fwe
    confounders_controlled:
      - "total lesion extent"
    confounders_not_controlled: []
    region_definition:
      kind: data_driven_cluster
      description: "Permutation-corrected cluster involving the majority of the left precentral gyrus."
    imaging_details:
      reference_space: MNI152
      atlases_used: ["AAL"]
      preprocessing_pipeline: "Unified Segmentation + enantiomorphic normalization + 8mm Gaussian smoothing"
    author_limitations:
      - "Sample skewed towards participants with less severe impairments due to the requirement of a scorable naturalistic language sample."
    provenance:
      extracted_by: "agent"
      extracted_on: 2026-01-01
      paper_section: "Results - Agrammatism"
      confidence: high
      flags: []
    source_passages:
      - section: "Results - Agrammatism"
        page: 10
        quote: "For the voxel-wise analysis, one significant cluster emerged (volume = 30.15 cm3; maximum t = 4.92; corrected P = 0.005, involving the majority of the left precentral gyrus"
        supports: claim
      - section: "Materials and methods - Participants"
        page: 2
        quote: "The present study included 118 participants with aphasia who were evaluated in the acute post-stroke period (1-5 days post-onset)"
        supports: sample
      - section: "Statistical analysis - Dimension-voxel-wise associations"
        page: 7
        quote: "Total lesion extent was included as a controlling covariate... only clusters with sizes falling within the extreme 5% of the permuted null distribution's right tail were considered significant (i.e. corrected P < 0.05)."
        supports: method
      - section: "Limitations"
        page: 16
        quote: "individuals with unscorable naturalistic language samples were excluded... consequently means that our sample was skewed towards participants with less severe speech-language impairments"
        supports: limitation
---
