---
schema_version: 2.8
id: left_arcuate_fasciculus
name: Left arcuate fasciculus
kind: tract
status: draft
created_by: agent:ollama-extract-cli/gemma4:31b
created_on: 2026-11-10
hemisphere: left
findings:
- id: f1
  target: severity_metric
  target_kind: predictor
  claim: Disconnection of the left arcuate fasciculus is associated with higher initial aphasia severity.
  direction: likely
  relationship: causal
  citation: '@Haldin2026'
  method: disconnectome
  design: cross-sectional
  strength: moderate
  evidence_quality: cohort
  sample:
    n: 70
    population: post-stroke aphasia
    time_post_onset: within 2 months post-stroke
    phase: early_subacute
    age_range: median 64.11 years
    handedness: 94.44 % right-handed
    language: French
  statistics:
    threshold: p < 0.005, 5,000 permutations
    effect_size: z-values ranging from 0 to -3.5
  confounders_controlled:
  - lesion volume
  confounders_not_controlled: []
  region_definition:
    kind: tract
    atlas: HCP1065
    description: Left Arcuate Fasciculus
  lesion_mapping:
    analysis: multivariate
    n_analysed: 70
    min_lesion_overlap: '>= 10 % of the participants'
    lesion_volume_correction: covariate
    multiple_comparisons: permutation_fwe
  imaging_details:
    field_strength: 1.5T
    reference_space: MNI152
    atlases_used:
    - HCP1065
    coordinates_reported:
    - region: Left Arcuate Fasciculus
      mni:
      - -38.9
      - -37.0
      - 25.6
  author_limitations:
  - The sample size for investigating the damaged brain structures associated with aphasia outcome or
    naming was relatively small.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Results, page 5
    confidence: high
    flags: []
  source_passages:
  - section: Results
    page: 5
    quote: Regarding the initial severity of aphasia, we found three significant clusters... The largest
      cluster (1,644 voxels) included voxels in the left AF (641 voxels) and the CC bilaterally (1,282
      voxels).
    supports: claim
  - section: Materials and methods
    page: 4
    quote: For each patient, a probability map of the WM tract's disconnection was generated using the
      Disconnectome map tool within the BCB Toolkit software
    supports: method
  - section: Materials and methods
    page: 4
    quote: regression of lesion volume out of both the ASRS score at FA and the lesion maps
    supports: confounders
  - section: Discussion
    page: 8
    quote: First, the sample size for investigating the damaged brain structures associated with aphasia
      outcome or naming was relatively small.
    supports: limitation
---
