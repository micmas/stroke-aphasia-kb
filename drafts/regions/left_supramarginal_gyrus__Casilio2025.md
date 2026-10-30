---
schema_version: 2.8
id: left_supramarginal_gyrus
name: "Left Supramarginal Gyrus"
kind: classical
status: draft
created_by: "agent:ollama-extract-cli/gemma4:31b-it-q8_0"
created_on: 2026-10-30
hemisphere: left
findings:
  - id: f1
    target: anomia
    target_kind: impairment
    claim: "Damage to the left supramarginal gyrus is uniquely associated with logopenia (paucity of words) in naturalistic language production."
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
      effect_size: "maximum t = 3.56"
      p_value: "0.014"
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
      description: "Permutation-corrected cluster encompassing most of the left inferior parietal lobe, including supramarginal and angular gyri."
    imaging_details:
      reference_space: MNI152
      atlases_used: ["AAL"]
      preprocessing_pipeline: "Unified Segmentation + enantiomorphic normalization + 8mm Gaussian smoothing"
    author_limitations:
      - "Sample skewed towards participants with less severe impairments due to the requirement of a scorable naturalistic language sample."
    provenance:
      extracted_by: "agent"
      extracted_on: 2026-01-01
      paper_section: "Results - Logopenia"
      confidence: high
      flags: []
    source_passages:
      - section: "Results - Logopenia"
        page: 8
        quote: "For the voxel-wise analysis, one significant cluster emerged (volume = 22.05 cm3; maximum t = 3.56; corrected P = 0.014), encompassing most of the left inferior parietal lobe, including supramarginal and angular gyri"
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
