---
schema_version: 2.8
id: left_ifg_pars_opercularis
name: Left IFG Pars Opercularis (Broca's area, dorsal stream hub)
kind: classical
status: draft
created_by: agent:ollama-extract-cli/gemma4:31b
created_on: 2026-11-10
hemisphere: left
findings:
- id: f1
  target: severity_metric
  target_kind: predictor
  claim: Damage to the left inferior frontal gyrus pars opercularis is associated with poor aphasia outcome
    at discharge in the late subacute phase.
  direction: likely
  relationship: causal
  citation: '@Haldin2026'
  method: MLPA
  design: cross-sectional
  strength: moderate
  evidence_quality: cohort
  sample:
    n: 54
    population: post-stroke aphasia
    time_post_onset: within 6 months post-stroke
    phase: late_subacute
    age_range: median 64.11 years
    handedness: 94.44 % right-handed
    language: French
  statistics:
    threshold: p < 0.005, 5,000 permutations
    effect_size: z-values ranging from 0 to -2.9
  confounders_controlled:
  - lesion volume
  - ASRS score at FA
  confounders_not_controlled: []
  region_definition:
    kind: atlas
    atlas: AAL
    description: Left Inferior Frontal Gyrus, pars opercularis
  lesion_mapping:
    analysis: multivariate
    n_analysed: 54
    min_lesion_overlap: '>= 10 % of the participants'
    lesion_volume_correction: covariate
    multiple_comparisons: permutation_fwe
  imaging_details:
    field_strength: 1.5T
    reference_space: MNI152
    atlases_used:
    - AAL
    coordinates_reported:
    - region: Left Inferior Frontal Gyrus, pars opercularis
      mni:
      - -30.0
      - -0.1
      - 29.3
  author_limitations:
  - The sample size for investigating the damaged brain structures associated with aphasia outcome...
    was relatively small.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Results, page 5
    confidence: high
    flags: []
  source_passages:
  - section: Results
    page: 5
    quote: Regarding aphasia outcome at discharge, one small cluster (61 voxels) survived voxel-wise thresholding...
      This cluster involved voxels in the left IFG pars opercularis (IFG-op, 32 voxels).
    supports: claim
  - section: Materials and methods
    page: 3
    quote: 'The inclusion criteria were: age above 18 years, a left-hemispheric stroke confirmed by MRI,
      a diagnosis of aphasia confirmed by speech and language assessment, and a speech and language assessment
      performed at FA within 60 days post-stroke.'
    supports: sample
  - section: Materials and methods
    page: 4
    quote: we used a multivariate method based on a machine learning regression algorithm (i.e., support-vector
      regression) to investigate brain-behavior relationships.
    supports: method
  - section: Materials and methods
    page: 4
    quote: The resulting SVR-beta values were thresholded voxel-wise at p < 0.005 and corrected for cluster
      size at p < 0.05, both based on 5,000 permutations.
    supports: statistics
  - section: Materials and methods
    page: 4
    quote: regression of the ASRS score at FA out of aphasia severity at discharge, and regression of
      lesion volume out of the lesion maps.
    supports: confounders
  - section: Discussion
    page: 8
    quote: First, the sample size for investigating the damaged brain structures associated with aphasia
      outcome or naming was relatively small.
    supports: limitation
---
