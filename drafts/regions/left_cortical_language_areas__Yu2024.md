---
schema_version: 2.8
id: left_cortical_language_areas
name: "Left Cortical Language Areas"
kind: network
status: draft
created_by: "agent:ollama-extract-cli/gemma4:31b"
created_on: 2026-11-10
hemisphere: left
members: ["left_ifg_pars_opercularis", "left_ifg_pars_triangularis", "left_angular_gyrus", "left_supramarginal_gyrus", "left_superior_temporal_gyrus", "left_middle_temporal_gyrus"]
findings:
  - id: f1
    target: severity_metric
    target_kind: predictor
    claim: "Lesion load of left cortical language areas is significantly associated with increased aphasia severity in subacute stroke."
    direction: likely
    relationship: causal
    citation: "@Yu2024"
    method: RLSM
    design: cross-sectional
    strength: moderate
    evidence_quality: cohort
    sample:
      n: 46
      population: "right-handed patients with post-stroke aphasia"
      time_post_onset: "median 23.50 (41) days, range, 5-89 days"
      phase: early_subacute
      age_range: "mean 56.09 (12.46) years, range, 25-78 years"
      handedness: "all right-handed"
      language: "Chinese speakers"
    statistics:
      threshold: "p < 0.05"
      effect_size: "R2 = 0.594 (in Model III)"
    lesion_mapping:
      analysis: region_based
      n_analysed: 46
      min_lesion_overlap: not_reported
      lesion_volume_correction: not_reported
      multiple_comparisons: not_reported
    confounders_controlled: ["SLF-LL", "IFOF-LL"]
    confounders_not_controlled: ["lesion volume"]
    region_definition:
      kind: atlas
      atlas: "HarvardOxford-sub-maxprob-thr25-2mm"
      description: "Frontal regions (pars opercularis, pars triangularis), parietal regions (angular gyrus, supramarginal gyrus), and temporal regions (pSTG, pMTG)."
    imaging_details:
      field_strength: "3.0 Tesla"
      reference_space: "MNI152"
      atlases_used: ["HarvardOxford-sub-maxprob-thr25-2mm"]
      preprocessing_pipeline: "FSL 5.0.9, FLIRT registration to MNI152"
    author_limitations:
      - "The sample was relatively small, which limits the generalizability of the results."
      - "Conclusions based solely on lesion load might be misleading compared to tract disconnection."
    provenance:
      extracted_by: "agent"
      extracted_on: 2026-01-01
      paper_section: "Results, page 4"
      confidence: high
      flags: []
    source_passages:
      - section: "Results"
        page: 4
        quote: "The variables including Areas-LL, the SLF-LL, and the IFOF-LL were significantly negatively associated with aphasia severity (p < 0.05)."
        supports: claim
      - section: "Materials and methods"
        page: 2
        quote: "Data on forty-six right-handed patients [31 cases of ischemic stroke and 15 cases of hemorrhagic stroke... median (IQR) time post-stroke (TPO), 23.50 (41) days, range, 5-89 days] with PSA... were analyzed."
        supports: sample
      - section: "Materials and methods"
        page: 3
        quote: "The critical cortical language-related areas were extracted from the Harvard-Oxford Cortical Structural Atlas (HarvardOxford-sub-maxprob-thr25-2 mm) within the FSL software package"
        supports: region_definition
      - section: "Discussion"
        page: 9
        quote: "First, the sample was relatively small, which limits the generalizability of the results."
        supports: limitation
---
