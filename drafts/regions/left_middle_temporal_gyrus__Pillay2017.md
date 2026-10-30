---
schema_version: 2.8
id: left_middle_temporal_gyrus
name: Left Middle Temporal Gyrus (Ventral Stream Node)
kind: classical
status: draft
created_by: agent:ollama-extract-cli/gemma4:31b-it-q8_0
created_on: 2026-10-30
hemisphere: left
findings:
- id: f1
  target: form_to_meaning
  target_kind: impairment
  claim: Damage to the mid-to-posterior left middle temporal gyrus is specifically associated with impairments
    in integrating multiword utterances during spoken language comprehension.
  direction: likely
  relationship: causal
  citation: '@Pillay2017'
  method: VLSM
  design: cross-sectional
  strength: strong
  evidence_quality: cohort
  sample:
    n: 51
    population: right-handed patients with chronic left hemisphere stroke
    time_post_onset: at least 180 days poststroke
    phase: chronic
    age_range: mean 59.2 (SD 12.6)
    handedness: all right-handed
    language: native English speakers
  statistics:
    threshold: voxel-wise p < 0.005 and cluster-corrected at a family-wise alpha of p < 0.05
    cluster_extent: 5500
  lesion_mapping:
    analysis: univariate
    n_analysed: 51
    min_lesion_overlap: '>= 3 patients'
    lesion_volume_correction: covariate
    multiple_comparisons: fwe
  confounders_controlled:
  - picture naming accuracy
  - lesion volume
  confounders_not_controlled: []
  region_definition:
    kind: data_driven_cluster
    description: mid-to-posterior portion of the middle temporal gyrus (MTG), extending into the superior
      temporal sulcus
  imaging_details:
    field_strength: 3T
    reference_space: MNI152
    atlases_used: []
    preprocessing_pipeline: nonlinear image registration
  author_limitations:
  - The methods used in the present study do not allow conclusions to be drawn concerning regions outside
    the left middle cerebral artery territory.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Results, page 972
    confidence: high
    flags: []
  source_passages:
  - section: Abstract
    page: 1
    quote: When PN impairment was included as a covariate, both ADN and ASC deficits were specifically
      correlated with damage localized to the mid-to-posterior portion of the middle temporal gyrus (MTG).
    supports: claim
  - section: Methods - Participants
    page: 2
    quote: Participants were 51 patients (25 women) with focal encephalomalacia from chronic left hemisphere
      stroke... All participants were at least 180 days poststroke, native English speakers, and premorbidly
      right-handed
    supports: sample
  - section: Methods - Voxel-based lesion-symptom mapping
    page: 2
    quote: Voxel-based lesion-symptom mapping (VLSM) uses lesion status at each voxel as a grouping variable...
      VLSM was implemented as an analysis of covariance
    supports: method
  - section: Methods - Voxel-based lesion-symptom mapping
    page: 3
    quote: All t statistic maps were thresholded at voxel-wise p < 0.005 and cluster-corrected at a family-wise
      alpha of p < 0.05 using a minimum cluster size criterion of 5,500 mL
    supports: statistics
  - section: Methods - Voxel-based lesion-symptom mapping
    page: 3
    quote: Lesion volume was included as an additional covariate in this analysis to more specifically
      isolate the regions critical for ADN
    supports: confounders
  - section: Results - VLSM results
    page: 3
    quote: As shown in figure 1B, ADN impairment was correlated with damage primarily in the middle and
      posterior MTG, extending into the superior temporal sulcus.
    supports: region_definition
  - section: Discussion
    page: 5
    quote: The methods used in the present study do not allow conclusions to be drawn concerning regions
      outside the left middle cerebral artery territory that are not well-represented in this patient
      sample.
    supports: limitation
  - section: Methods - MRI
    page: 2
    quote: MRI was performed at 3T in 48 patients and 1.5T in 3 patients. Details regarding lesion tracing
      and nonlinear image registration methods are described elsewhere.
    supports: imaging_details
---
