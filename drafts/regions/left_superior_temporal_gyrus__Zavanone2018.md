---
schema_version: 2.8
id: left_superior_temporal_gyrus
name: Left Superior Temporal Gyrus (Dorsal Stream Node)
kind: classical
status: draft
created_by: agent:ollama-extract-cli/gemma4:31b
created_on: 2026-11-10
hemisphere: left
findings:
- id: f1
  target: severity_metric
  target_kind: predictor
  claim: Damage to the left superior temporal gyrus and temporo-parietal junction is associated with greater
    aphasia severity at 3 and 6 months post-stroke.
  direction: likely
  relationship: causal
  citation: '@Zavanone2018'
  method: VLSM
  design: cross-sectional
  strength: moderate
  evidence_quality: cohort
  sample:
    n: 19
    population: acute left middle cerebral territory stroke
    time_post_onset: 24 h (MRI), 3-6 months (outcome)
    phase: chronic
    age_range: 18-85 years
    handedness: right-handed
    language: French native
  statistics:
    threshold: height threshold of 0.001, cluster-level FWE p < 0.05
    effect_size: not_reported
  lesion_mapping:
    analysis: univariate
    n_analysed: 19
    min_lesion_overlap: not_reported
    lesion_volume_correction: not_reported
    multiple_comparisons: fwe
  confounders_controlled:
  - age
  confounders_not_controlled: []
  region_definition:
    kind: data_driven_cluster
    description: single cluster, mainly at the level of the left superior temporal gyrus (STG) and reached
      the left temporo-parietal junction
  imaging_details:
    field_strength: 3T
    acquisition:
      voxel_size_mm:
      - 5
      - 5
      - 5
      sequence: spin-echo multi-slice single-shot echo planar imaging
    preprocessing_pipeline: normalized to MNI space using EPI template in SPM8, smoothed by 6mm Gaussian
      filter
    reference_space: MNI152
    atlases_used: []
    coordinates_reported:
    - region: Posterior division of medium temporal gyrus
      mni:
      - -56
      - -32
      - -8
    - region: Posterior division of superior temporal gyrus
      mni:
      - -52
      - -14
      - -10
    - region: Posterior division of superior temporal gyrus
      mni:
      - -64
      - -14
      - 0
  author_limitations:
  - The number of subjects was relatively small, limiting the generalizability of the results.
  - Voxel-based analysis on clinical routine ADC maps is more suitable to detect differences in white
    matter areas than cortical areas.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Results, page 4
    confidence: high
    flags: []
  source_passages:
  - section: Results
    page: 4
    quote: The regions associated with greater aphasia severity evaluated with the ART at three months
      were also located in a single cluster, mainly at the level of the left superior temporal gyrus (STG)
      and reached the left temporo-parietal junction
    supports: claim
  - section: Materials and methods
    page: 2
    quote: Nineteen patients were finally included in the study
    supports: sample
  - section: Materials and methods
    page: 3
    quote: The analysis was conducted using a height threshold of 0.001 and was corrected at the cluster
      level by a family-wise-error threshold at p < 0.05 for multiple comparisons
    supports: statistics
  - section: Discussion
    page: 6
    quote: First, the number of subjects was relatively small, limiting the generalizability of the results.
    supports: limitation
---
