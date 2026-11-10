---
schema_version: 2.8
id: left_ifg
name: "Left Inferior Frontal Gyrus"
kind: classical
status: draft
created_by: "agent:ollama-extract-cli/gemma4:31b"
created_on: 2026-11-10
hemisphere: left
findings:
  - id: f1
    target: severity_metric
    target_kind: predictor
    claim: "In the acute phase, better initial language performance is linked to higher activation in the left inferior frontal gyrus."
    direction: likely
    relationship: correlational
    citation: "@Saur2006"
    method: fMRI_activation
    design: longitudinal
    strength: moderate
    evidence_quality: cohort
    sample:
      n: 14
      population: "aphasia due to an infarction of the left middle cerebral artery territory"
      time_post_onset: "mean: 1.8 dps (acute phase)"
      phase: acute
      age_range: "16-68 years, mean (SD): 51.9 (14.2)"
      handedness: "12 right-handed, 1 left-handed, 1 converted left-handed"
      language: "German"
    statistics:
      threshold: "P < 0.001 uncorrected"
      effect_size: "r = 0.93"
    confounders_controlled: []
    confounders_not_controlled: []
    region_definition:
      kind: peak_coord_sphere
      mni_peak: [-57, 15, -9]
      description: "Left IFG peak voxel"
    imaging_details:
      field_strength: "3T"
      modalities:
        - modality: fMRI
          sequence: "gradient echo echoplanar imaging (EPI) T2*-sensitive"
          voxel_size_mm: [3, 3, 3]
          TR_ms: 1830
          TE_ms: 25
      preprocessing_pipeline: "SPM2; slice timing, realignment, lesion-masked normalization to MNI, 9mm Gaussian smoothing"
      reference_space: MNI152
      atlases_used: []
    author_limitations:
      - "Results are limited to somewhat less severely impaired patients who were able to understand the task and sustain an fMRI session in the first days after stroke."
    provenance:
      extracted_by: "agent"
      extracted_on: 2026-01-01
      paper_section: "Results, page 7"
      confidence: high
      flags: []
    source_passages:
      - section: "Results"
        page: 7
        quote: "In the acute phase, there was a strong positive linear correlation of LRSEx1 with language activation with two large clusters in the left IFG (r = 0.93, P < 0.001)"
        supports: claim
      - section: "Methods"
        page: 2
        quote: "14 patients with aphasia due to an infarction of the left middle cerebral artery territory"
        supports: sample
      - section: "Discussion"
        page: 12
        quote: "the results are limited to somewhat less severely impaired patients who were clearly aphasic at the first exam but were able to understand the task."
        supports: limitation
---
