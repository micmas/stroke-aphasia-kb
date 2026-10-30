---
schema_version: 2.8
id: left_middle_frontal_gyrus
name: Left Middle Frontal Gyrus
kind: classical
status: draft
created_by: agent:ollama-extract-cli/gemma4:31b-it-q8_0
created_on: 2026-10-30
hemisphere: left
findings:
- id: f1
  target: fluency
  target_kind: impairment
  claim: Damage to the left middle frontal gyrus is associated with poor spontaneous speech production
    in chronic aphasia.
  direction: likely
  relationship: causal
  citation: '@MartinezMolina2022'
  method: MLPA
  design: cross-sectional
  strength: moderate
  evidence_quality: cohort
  sample:
    n: 45
    population: chronic stroke patients with aphasia
    time_post_onset: '>=6 months'
    phase: chronic
    age_range: mean 64.4 (10.2) years
    handedness: 39 right, 5 left, 1 both
    language: Finnish-speaking
  statistics:
    threshold: cluster-level FWE P < 0.05
    effect_size: not_reported
  lesion_mapping:
    analysis: multivariate
    n_analysed: 45
    min_lesion_overlap: '>= 10% of the patients'
    lesion_volume_correction: direct
    multiple_comparisons: fwe
  confounders_controlled:
  - age
  - lesion volume
  confounders_not_controlled: []
  region_definition:
    kind: data_driven_cluster
    description: Cluster identified via SVR-LSM associated with poor spontaneous speech production.
  imaging_details:
    field_strength: 3T
    acquisition:
      voxel_size_mm:
      - 1
      - 0.98
      - 0.98
      TR_ms: 1800
      TE_ms: 2.27
      sequence: T1-weighted magnetization prepared rapid gradient echo
    preprocessing_pipeline: SPM12 Unified Segmentation + cost function masking + normalization to MNI
      space
    reference_space: MNI152
    atlases_used: []
  author_limitations:
  - The extent to which this pattern of results applies to non-fluency due to aphasia and/or apraxia of
    speech (AOS) remains an open question.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Results, page 6
    confidence: high
    flags: []
  source_passages:
  - section: Results
    page: 6
    quote: Poor spontaneous speech was associated with lesions in the left inferior frontal gyrus (IFG)
      and middle frontal gyrus (MFG), superior temporal pole (TPO-STG), Rolandic operculum (ROL), inferior
      temporal gyrus and insula.
    supports: claim
  - section: Materials and methods
    page: 3
    quote: Forty-five chronic stroke patients (25 females, mean age = 64.4 + 10.2 years) were recruited...
      Inclusion criteria were time since stroke >=6 months
    supports: sample
  - section: Statistical analysis
    page: 6
    quote: Lesion-symptom relations were evaluated using the SVR-LSM... Analyses were adjusted for age
      and lesion volume using a direct total lesion volume control procedure.
    supports: method
  - section: Statistical analysis
    page: 6
    quote: In addition, a cluster size threshold [family-wise error (FWE) rate; P < 0.05] was applied
      for multiple comparisons correction.
    supports: statistics
  - section: Discussion
    page: 8
    quote: The extent to which this pattern of results applies to non-fluency due to aphasia and/or apraxia
      of speech (AOS) remains an open question.
    supports: limitation
- id: f2
  target: fluency
  target_kind: impairment
  claim: Greater grey matter volume in the left middle frontal gyrus is associated with better spontaneous
    speech production in chronic aphasia.
  direction: likely
  relationship: correlational
  citation: '@MartinezMolina2022'
  method: VBCM
  design: cross-sectional
  strength: moderate
  evidence_quality: cohort
  sample:
    n: 45
    population: chronic stroke patients with aphasia
    time_post_onset: '>=6 months'
    phase: chronic
    age_range: mean 64.4 (10.2) years
    handedness: 39 right, 5 left, 1 both
    language: Finnish-speaking
  statistics:
    threshold: FWE cluster-level correction with P < 0.05
    effect_size: T(1,41) = 5.889
  confounders_controlled:
  - age
  - total intracranial volume
  confounders_not_controlled: []
  region_definition:
    kind: data_driven_cluster
    description: Cluster identified via VBM associated with spontaneous speech production rate.
  imaging_details:
    field_strength: 3T
    preprocessing_pipeline: SPM12 Unified Segmentation + normalization to MNI space
    reference_space: MNI152
    atlases_used: []
  author_limitations:
  - The extent to which this pattern of results applies to non-fluency due to aphasia and/or apraxia of
    speech (AOS) remains an open question.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Results, page 7
    confidence: high
    flags:
    - lesion_mapping (v2.7 design) not extracted by the model — filled from statistics.threshold / confounders
      where the text says; check the Methods
  source_passages:
  - section: Results
    page: 7
    quote: Better spontaneous speech was associated with greater GMV in the left MFG.
    supports: claim
  - section: Statistical analysis
    page: 6
    quote: All VBM results were thresholded at FWE cluster-level correction with P < 0.05.
    supports: statistics
  - section: Discussion
    page: 8
    quote: The extent to which this pattern of results applies to non-fluency due to aphasia and/or apraxia
      of speech (AOS) remains an open question.
    supports: limitation
  lesion_mapping:
    analysis: univariate
    n_analysed: 45
    min_lesion_overlap: not_reported
    lesion_volume_correction: not_reported
    multiple_comparisons: cluster_fwe
---
