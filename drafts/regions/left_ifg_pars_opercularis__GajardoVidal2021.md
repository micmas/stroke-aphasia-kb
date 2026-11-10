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
  target: fluency
  target_kind: impairment
  claim: Damage to the left IFG pars opercularis (BA44) does not uniquely contribute to long-term speech
    production impairments when damage to the anterior arcuate fasciculus is controlled for.
  direction: no_effect
  relationship: causal
  citation: '@GajardoVidal2021'
  method: RLSM
  design: cross-sectional
  strength: strong
  evidence_quality: cohort
  sample:
    n: 134
    population: left-hemisphere stroke patients
    time_post_onset: at least 3 months post-stroke
    phase: chronic
    age_range: 31-87 years (mean 60)
    handedness: right handed pre-morbidly
    language: native speaker of English
    cohort: PLORAS
  statistics:
    threshold: P = 0.567
    effect_size: Beta = 0.102
  lesion_mapping:
    analysis: multivariate
    n_analysed: 134
    min_lesion_overlap: not_reported
    lesion_volume_correction: covariate
    multiple_comparisons: uncorrected
  confounders_controlled:
  - total lesion volume
  - months post-stroke
  - age at stroke
  - CAT semantic memory scores
  - lesion load in aAF
  confounders_not_controlled: []
  region_definition:
    kind: atlas
    atlas: Brainnetome
    description: BA44 (pars opercularis)
  author_limitations:
  - The use of atlas-based lesion load may lead to false negatives if only specific subparts of a region
    are critical.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Results, page 824
    confidence: high
    flags:
    - ' cohort overlaps with @Saur2008, @White2024 (PLORAS database)'
  source_passages:
  - section: Results
    page: 824
    quote: When the effect of damage to regions neighbouring Broca's area was taken into account (i.e.
      Model 2 in Table 3), lesion load in BA44 no longer explained speech production scores (P = 0.567).
    supports: claim
  - section: Materials and methods
    page: 3
    quote: 'The six grey matter regions were derived from the Brainnetome atlas... These were: BA44, BA45...'
    supports: region_definition
  - section: Results
    page: 824
    quote: Across all eight anatomical predictors included in Model 2, only lesion load in aAF reached
      statistical significance (P = 0.008).
    supports: statistics
  imaging_details:
    reference_space: MNI152
    atlases_used:
    - Brainnetome
    - Natbrainlab
    preprocessing_pipeline: automated procedures reported in Seghier et al. (2008)
    field_strength: mixed (1.5T and 3T)
---
