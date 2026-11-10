---
schema_version: 2.8
id: right_ifg
name: "Right Inferior Frontal Gyrus"
kind: classical
status: draft
created_by: "agent:ollama-extract-cli/gemma4:31b"
created_on: 2026-11-10
hemisphere: right
findings:
  - id: f1
    target: severity_metric
    target_kind: predictor
    claim: "An increase of activation in the right inferior frontal gyrus during the subacute phase is strongly correlated with improvement in overall language function."
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
      time_post_onset: "mean: 12.1 dps (subacute phase)"
      phase: late_subacute
      age_range: "16-68 years, mean (SD): 51.9 (14.2)"
      handedness: "12 right-handed, 1 left-handed, 1 converted left-handed"
      language: "German"
    statistics:
      threshold: "P < 0.001 uncorrected"
      effect_size: "r = 0.88"
    confounders_controlled: []
    confounders_not_controlled: ["
      practice effects"
    ]
    region_definition:
      kind: peak_coord_sphere
      mni_peak: [54, 30, 21]
      description: "Right IFG pars triangularis peak voxel"
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
      paper_section: "Results, page 8"
      confidence: high
      flags: []
    source_passages:
      - section: "Results"
        page: 8
        quote: "Only the correlation of early relative improvement of language function (LRSEx2/Ex1) and increase of language activation (Ex2 > Ex1) was significant. This correlation revealed strong activation in the SMA (r = 0.92, P < 0.001) and right IFG including right insular cortex (r = 0.88, P < 0.001; Fig. 4B)."
        supports: claim
      - section: "Methods"
        page: 2
        quote: "14 patients with aphasia due to an infarction of the left middle cerebral artery territory"
        supports: sample
      - section: "Methods"
        page: 3
        quote: "fMRI was performed on a 3T Siemens TRIO system... repetition time (TR) = 1.83 s, echo time (TE) = 25 ms"
        supports: imaging_details
      - section: "Discussion"
        page: 12
        quote: "the results are limited to somewhat less severely impaired patients who were clearly aphasic at the first exam but were able to understand the task."
        supports: limitation
---
