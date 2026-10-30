---
schema_version: 2.8
id: left_superior_temporal_gyrus
name: Left Superior Temporal Gyrus (Dorsal Stream Node)
kind: classical
status: draft
created_by: agent:ollama-extract-cli/gemma4:31b-it-q8_0
created_on: 2026-10-30
hemisphere: left
findings:
- id: f1
  target: anomia
  target_kind: impairment
  claim: Damage to the left superior temporal gyrus and sulcus is uniquely associated with paraphasias
    (selection errors) in naturalistic language production.
  direction: likely
  relationship: causal
  citation: '@Casilio2025'
  method: VLSM
  design: cross-sectional
  strength: strong
  evidence_quality: cohort
  sample:
    n: 118
    population: acute post-stroke aphasia
    time_post_onset: 1-5 days post-onset
    phase: acute
    age_range: 18-90 years
    handedness: 105 right; 11 left; 2 ambidextrous
    language: English
  statistics:
    threshold: corrected P < 0.05
    effect_size: maximum t = 4.93
    p_value: < 0.001
  lesion_mapping:
    analysis: univariate
    n_analysed: 118
    min_lesion_overlap: '>= 6 patients'
    lesion_volume_correction: covariate
    multiple_comparisons: permutation_fwe
  confounders_controlled:
  - total lesion extent
  confounders_not_controlled: []
  region_definition:
    kind: data_driven_cluster
    description: Permutation-corrected cluster peaking in left supramarginal gyrus, encompassing left
      middle and posterior superior temporal gyrus and sulcus.
  imaging_details:
    reference_space: MNI152
    atlases_used:
    - AAL
    preprocessing_pipeline: Unified Segmentation + enantiomorphic normalization + 8mm Gaussian smoothing
  author_limitations:
  - Sample skewed towards participants with less severe impairments due to the requirement of a scorable
    naturalistic language sample.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Results - Paraphasia
    confidence: high
    flags: []
  source_passages:
  - section: Results - Paraphasia
    page: 8
    quote: For the voxel-wise analysis, one large and significant cluster emerged (volume = 51.30 cm3;
      maximum t = 4.93; corrected P < 0.001), spanning almost the entirety of posterior temporoparietal
      cortex... the cluster encompassed nearly all the left middle and posterior superior temporal gyrus
      and sulcus
    supports: claim
  - section: Materials and methods - Participants
    page: 2
    quote: The present study included 118 participants with aphasia who were evaluated in the acute post-stroke
      period (1-5 days post-onset)
    supports: sample
  - section: Statistical analysis - Dimension-voxel-wise associations
    page: 7
    quote: Total lesion extent was included as a controlling covariate. Statistical significance of a
      voxel's effect on a dimension score was determined using a one-tailed... t-test of P < 0.01... only
      clusters with sizes falling within the extreme 5% of the permuted null distribution's right tail
      were considered significant (i.e. corrected P < 0.05).
    supports: method
  - section: Limitations
    page: 16
    quote: individuals with unscorable naturalistic language samples were excluded... consequently means
      that our sample was skewed towards participants with less severe speech-language impairments
    supports: limitation
---
