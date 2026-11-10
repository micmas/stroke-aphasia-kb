---
schema_version: 2.8
id: left_middle_temporal_gyrus
name: Left Middle Temporal Gyrus (Ventral Stream Node)
kind: classical
status: draft
created_by: agent:ollama-extract-cli/gemma4:31b
created_on: 2026-11-10
hemisphere: left
findings:
- id: f1
  target: syntactic_processing
  target_kind: impairment
  claim: Damage to the left middle temporal gyrus is associated with deficits in general sentence comprehension.
  direction: likely
  relationship: causal
  citation: '@Biondo2024'
  method: VLSM
  design: cross-sectional
  strength: strong
  evidence_quality: cohort
  sample:
    n: 131
    population: left hemisphere stroke survivors
    time_post_onset: at least 6 months
    phase: chronic
    age_range: 31-86 years
    handedness: all right handed
    language: native-like proficiency in English
  statistics:
    threshold: continuous permutation-based family-wise error rate (FWER) correction... final threshold
      set at P = 0.05
    effect_size: not_reported
  lesion_mapping:
    analysis: univariate
    n_analysed: 131
    min_lesion_overlap: '>= 5 participants'
    lesion_volume_correction: covariate
    multiple_comparisons: permutation_fwe
  confounders_controlled:
  - age
  - years of education
  - months post-stroke
  - lesion size
  confounders_not_controlled: []
  region_definition:
    kind: data_driven_cluster
    description: significant cluster identified by univariate LSM for general sentence-level comprehension
  imaging_details:
    reference_space: MNI152
    atlases_used:
    - Brainnetome Atlas
    preprocessing_pipeline: SPM2/SPM8 cost function masking normalization to MNI
  author_limitations:
  - The current study utilized the CYCLE-R, which... has a small number of test stimuli per subtest and
    a non-exhaustive set of sentence types.
  - other variables are not controlled (e.g. sentence length), thus limiting the ability of creating controlled
    minimal pairs.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Results, page 8
    confidence: high
    flags: []
  source_passages:
  - section: Results
    page: 8
    quote: The results of the univariate LSM analysis assessing crucial neural underpinnings for general
      sentence-level comprehension identified portions of the left mid-posterior temporal lobe and left
      inferior parietal lobe, namely the mid-posterior STS and STG, the MTG...
    supports: claim
  - section: Materials and methods
    page: 5
    quote: Participants included 131 individuals... who sustained a single left hemisphere stroke at least
      6 months before being tested and scanned.
    supports: sample
  - section: Statistical analysis
    page: 7
    quote: In order to account for false positive results due to the large number of voxels being sampled,
      permutation testing was applied... with a final threshold set at P = 0.05.
    supports: statistics
  - section: Statistical analysis
    page: 7
    quote: 'In all LSM analyses, we included the following demographic variables as covariates: age, years
      of education, months post-stroke and lesion size.'
    supports: confounders
  - section: Limitations and future directions
    page: 13
    quote: The current study utilized the CYCLE-R, which was developed to test comprehension on a wide
      range of syntactic structures but has a small number of test stimuli per subtest and a non-exhaustive
      set of sentence types.
    supports: limitation
---
