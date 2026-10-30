---
schema_version: 2.8
id: left_posterior_middle_temporal_gyrus
name: "Left Posterior Middle Temporal Gyrus"
kind: classical
status: draft
created_by: "agent:ollama-extract-cli/gemma4:31b-it-q8_0"
created_on: 2026-10-30
hemisphere: left
findings:
  - id: f1
    target: syntactic_processing
    target_kind: impairment
    claim: "Damage to the left posterior middle temporal gyrus is a strong predictor of overall syntactic processing and performance on noncanonical sentences in acute aphasia."
    direction: likely
    relationship: causal
    citation: "@Kristinsson2020"
    method: RLSM
    design: cross-sectional
    strength: strong
    evidence_quality: cohort
    sample:
      n: 104
      population: "acute left-hemisphere stroke patients with aphasia"
      time_post_onset: "<20 days poststroke"
      phase: acute
      age_range: "mean 65.2 (SD 10.0) years"
      handedness: not_reported
      language: "English and Icelandic"
      cohort: not_reported
    statistics:
      threshold: "alpha level of .05"
      effect_size: "accounted for 33.7% of variance in total score; 37.1% of variance in non-CAN score"
      p_value: "<.001"
    lesion_mapping:
      analysis: region_based
      n_analysed: 104
      min_lesion_overlap: not_reported
      lesion_volume_correction: covariate
      multiple_comparisons: not_reported
    confounders_controlled:
      - "lesion volume"
    confounders_not_controlled: []
    region_definition:
      kind: atlas
      atlas: "Faria et al. (2012)"
      description: "posterior middle temporal gyrus (pMTG)"
    imaging_details:
      field_strength: "1.5T or 3T"
      preprocessing_pipeline: "SPM5 unified segmentation and normalization (Icelandic) or Clinical Toolbox/SPM12 enantiomorphic normalization (US)"
      reference_space: MNI152
      atlases_used: ["Faria et al. (2012)"]
    author_limitations:
      - "ROI-based approach compromises spatial resolution compared to voxel-based methods."
      - "Only a single measure of sentence comprehension was used."
      - "Behavioral performance was only examined in relation to structural damage, not cerebral perfusion."
    provenance:
      extracted_by: "agent"
      extracted_on: 2026-01-01
      paper_section: "Results, pages 263-264"
      confidence: high
      flags: []
    source_passages:
      - section: "Abstract"
        page: 1
        quote: "Damage to the posterior middle temporal gyrus was the strongest predictor for overall task performance and performance on noncanonical sentences."
        supports: claim
      - section: "Methods - Participants"
        page: 3
        quote: "One hundred four stroke patients with acute left-hemisphere injury participated in the study..."
        supports: sample
      - section: "Methods - Participants"
        page: 4
        quote: "In the combined sample, there were 47 female and 57 male participants with a mean age of 65.2 (SD = 10.0) years."
        supports: sample
      - section: "Methods - Neuroimaging Data"
        page: 5
        quote: "For the lesion-symptom mapping, we used a parcellated brain atlas described by Faria et al. (2012) as a framework for anatomical boundaries."
        supports: region_definition
      - section: "Methods - Data Analysis"
        page: 7
        quote: "Total lesion volume was included as a covariate in all analyses."
        supports: confounders
      - section: "Results"
        page: 8
        quote: "Damage to the pMTG alone accounted for 33.7% of the variance in performance [total score]... The pMTG alone accounted for 37.1% of variance in performance [non-CAN score]."
        supports: statistics
      - section: "Discussion"
        page: 14
        quote: "Each ROI treated as an independent variable in our models is represented by a single number (proportional damage), regardless of the size of the ROI. Consequently, spatial resolution is compromised."
        supports: limitation
---
