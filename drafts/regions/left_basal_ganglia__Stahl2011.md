---
schema_version: 2.8
id: left_basal_ganglia
name: "Left Basal Ganglia"
kind: classical
status: draft
created_by: "agent:ollama-extract-cli/gemma4:31b-it-q8_0"
created_on: 2026-10-30
hemisphere: left
findings:
  - id: f1
    target: fluency
    target_kind: impairment
    claim: "Damage to the left basal ganglia is associated with a reduced ability to benefit from rhythmic cues for speech production in non-fluent aphasia."
    direction: likely
    relationship: causal
    citation: "@Stahl2011"
    method: LSM
    design: cross-sectional
    strength: moderate
    evidence_quality: cohort
    sample:
      n: 17
      population: "non-fluent aphasics"
      time_post_onset: "at least 3 months post-infarction"
      phase: chronic
      age_range: "27-80 years [mean (standard deviation) age 56 (14) years]"
      handedness: "right-handed"
      language: "German native-speakers"
    statistics:
      threshold: "P = 0.001"
      effect_size: "partial eta squared = 0.55"
    lesion_mapping:
      analysis: univariate
      n_analysed: 17
      min_lesion_overlap: not_reported
      lesion_volume_correction: not_reported
      multiple_comparisons: bonferroni
    confounders_controlled:
      - "patients' age"
    confounders_not_controlled: []
    region_definition:
      kind: manual_ROI
      description: "Left basal ganglia including the caudate nucleus, the putamen and the pallidum."
    imaging_details:
      reference_space: not_reported
      atlases_used: []
    author_limitations:
      - "The study was limited to a small sample of 17 patients."
      - "The arrhythmic control is not completely devoid of rhythm but rather provides a gradual decrease in perceived rhythmicity."
    provenance:
      extracted_by: "agent"
      extracted_on: 2026-01-01
      paper_section: "Results, Part 2: Rhythmic speech"
      confidence: high
      flags: []
    source_passages:
      - section: "Results"
        page: 8
        quote: "A contrast analysis indicated an interaction of basal ganglia lesions with rhythmic speech and the arrhythmic control [F(1) = 16.90, P = 0.001, partial eta squared = 0.55]."
        supports: statistics
      - section: "Results"
        page: 8
        quote: "patients with larger basal ganglia lesions tended to perform worse in the arrhythmic control compared with rhythmic speech."
        supports: claim
      - section: "Materials and methods"
        page: 4
        quote: "All CT or MRI scans were thoroughly analysed for lesions within the left basal ganglia, including the caudate nucleus, the putamen and the pallidum."
        supports: region_definition
      - section: "Materials and methods"
        page: 3
        quote: "Seventeen stroke patients were included in the study."
        supports: sample
      - section: "Materials and methods"
        page: 3
        quote: "At the time of testing, all patients were at least 3 months post-infarction, except in one case (Patient HS)."
        supports: sample
      - section: "Results"
        page: 7
        quote: "An alpha level of 0.05 and the Bonferroni correction for multiple comparisons were applied."
        supports: method
      - section: "Discussion"
        page: 9
        quote: "it should be considered that arrhythmic control is not completely devoid of rhythm but rather provides a gradual decrease in perceived rhythmicity."
        supports: limitation
---
