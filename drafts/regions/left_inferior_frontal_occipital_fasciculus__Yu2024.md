---
schema_version: 2.8
id: left_inferior_frontal_occipital_fasciculus
name: "Left Inferior Frontal Occipital Fasciculus"
kind: tract
status: draft
created_by: "agent:ollama-extract-cli/gemma4:31b"
created_on: 2026-11-10
hemisphere: left
findings:
  - id: f1
    target: severity_metric
    target_kind: predictor
    claim: "Lesion load of the left IFOF is an independent predictor of aphasia severity in subacute stroke."
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
      threshold: "p = 0.013"
      effect_size: "Beta = -0.266 (Model III)"
    lesion_mapping:
      analysis: region_based
      n_analysed: 46
      min_lesion_overlap: not_reported
      lesion_volume_correction: not_reported
      multiple_comparisons: not_reported
    confounders_controlled: ["SLF-LL", "Areas-LL"]
    confounders_not_controlled: ["lesion volume"]
    region_definition:
      kind: atlas
      atlas: "JHU-ICBM-tracts-prob-thr25-2mm"
      description: "Left IFOF extracted from JHU White Matter Tractography Atlas."
    imaging_details:
      field_strength: "3.0 Tesla"
      reference_space: "MNI152"
      atlases_used: ["JHU-ICBM-tracts-prob-thr25-2mm"]
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
        quote: "Then, in Model III, the IFOF-LL was added as an independent variable while controlling for the SLF-LL and the Areas-LL, all these three variables explained 59.4 % of the variation in aphasia severity (F = 22.919, p < 0.001, R2 = 0.594)."
        supports: claim
      - section: "Materials and methods"
        page: 3
        quote: "Several critical sub-cortical language-related neural tracts were extracted from the Johns Hopkins University (JHU) White Matter Tractography Atlas (JHU-ICBM-tracts-prob-thr25-2 mm)"
        supports: region_definition
      - section: "Discussion"
        page: 9
        quote: "First, the sample was relatively small, which limits the generalizability of the results."
        supports: limitation
---
