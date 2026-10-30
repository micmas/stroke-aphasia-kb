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
  target: syntactic_processing
  target_kind: impairment
  claim: Damage to the left anterior and posterior superior temporal gyri is associated with deficits
    in both sentence production and comprehension.
  direction: likely
  relationship: causal
  citation: '@Lukic2021'
  method: VLSM
  design: cross-sectional
  strength: strong
  evidence_quality: cohort
  sample:
    n: 76
    population: chronic stroke-induced aphasia
    time_post_onset: 8 to 209 months (M = 58.53 months; SD = 50.28)
    phase: chronic
    age_range: mean 58.6 years (SD = 11.99, range = 22-81 years)
    handedness: 64 right-handed, 10 left-handed, 2 ambidextrous
    language: not_reported
  statistics:
    threshold: p < .001 with cluster size and permutation-based correction
    effect_size: not_reported
  lesion_mapping:
    analysis: univariate
    n_analysed: 76
    min_lesion_overlap: '>= 6 participants (at least 10%)'
    lesion_volume_correction: covariate
    multiple_comparisons: permutation_fwe
  confounders_controlled:
  - age
  - months post onset
  - education
  - sex
  - handedness
  - total lesion volume
  - verb production/comprehension
  confounders_not_controlled: []
  region_definition:
    kind: atlas
    atlas: Harvard-Oxford Atlas
    description: Anterior and posterior superior temporal gyri (aSTG, pSTG)
  imaging_details:
    field_strength: 3T
    preprocessing_pipeline: NUNDA anatomical preprocessing pipeline; enantiomorphic registration to VBM-DARTEL
      template
    reference_space: MNI152
    atlases_used:
    - Harvard-Oxford Atlas
  author_limitations:
  - Limited statistical power in frontal regions after verb processing deficits were partialed out.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Results, page 4
    confidence: high
    flags: []
  source_passages:
  - section: Abstract
    page: 1
    quote: Results revealed shared regions across domains in the anterior and posterior superior temporal
      gyri (aSTG, pSTG), and the temporal pole (adjusted for verb production/comprehension).
    supports: claim
  - section: Materials and methods
    page: 3
    quote: Participants included 76 individuals (50 males) with stroke-induced aphasia... Months post-stroke
      ranged from 8 to 209 months ( M = 58.53 months; SD = 50.28).
    supports: sample
  - section: MRI preprocessing and analyses
    page: 3
    quote: A VLSM ( Bates et al., 2003 ; Ivanova et al., 2020 ) approach was used to analyze the relationship
      between lesions in the left hemisphere and language performance...
    supports: method
  - section: MRI preprocessing and analyses
    page: 4
    quote: Significant results were derived from voxel-wise t -tests using a threshold of p < .001 with
      cluster size and permutation-based correction for multiple comparisons.
    supports: statistics
  - section: Discussion
    page: 8
    quote: As noted above, our participants' lesion overlay map yielded limited statistical power in frontal
      regions (specifically after taking into account verb deficits).
    supports: limitation
- id: f2
  target: syntactic_processing
  target_kind: impairment
  claim: Damage to the left posterior superior temporal gyrus is specifically associated with the processing
    of syntactically complex, noncanonical sentences across both production and comprehension domains.
  direction: likely
  relationship: causal
  citation: '@Lukic2021'
  method: VLSM
  design: cross-sectional
  strength: strong
  evidence_quality: cohort
  sample:
    n: 76
    population: chronic stroke-induced aphasia
    time_post_onset: 8 to 209 months
    phase: chronic
    age_range: mean 58.6 years
    handedness: mixed
    language: not_reported
  statistics:
    threshold: p < .001 with cluster size and permutation-based correction
    effect_size: not_reported
  lesion_mapping:
    analysis: univariate
    n_analysed: 76
    min_lesion_overlap: '>= 6 participants'
    lesion_volume_correction: covariate
    multiple_comparisons: permutation_fwe
  confounders_controlled:
  - age
  - months post onset
  - education
  - sex
  - handedness
  - total lesion volume
  - canonical sentence performance
  confounders_not_controlled: []
  region_definition:
    kind: atlas
    atlas: Harvard-Oxford Atlas
    description: Posterior superior temporal gyrus (pSTG)
  imaging_details:
    field_strength: 3T
    preprocessing_pipeline: NUNDA anatomical preprocessing pipeline
    reference_space: MNI152
    atlases_used:
    - Harvard-Oxford Atlas
  author_limitations:
  - Limited statistical power in frontal regions after verb processing deficits were partialed out.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Results, page 4
    confidence: high
    flags: []
  source_passages:
  - section: Abstract
    page: 1
    quote: Processing of syntactically complex, noncanonical (adjusted for canonical), sentences was associated
      with damage to the pSTG across domains...
    supports: claim
  - section: MRI preprocessing and analyses
    page: 4
    quote: Lastly, VLSM analyses on syntactically complex sentences for both production and comprehension
      (adjusted for performance on canonical sentences) were performed.
    supports: method
  - section: Discussion
    page: 8
    quote: The finding that damage to the pSTG is associated with processing of noncanonical sentences
      is in line with previous neuroimaging and lesion-symptom mapping studies...
    supports: claim
---
