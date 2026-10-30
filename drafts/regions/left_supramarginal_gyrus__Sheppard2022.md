---
schema_version: 2.8
id: left_supramarginal_gyrus
name: Left Supramarginal Gyrus
kind: classical
status: draft
created_by: agent:ollama-extract-cli/gemma4:31b-it-q8_0
created_on: 2026-10-30
hemisphere: left
findings:
- id: f1
  target: syntactic_processing
  target_kind: impairment
  claim: Damage to the left supramarginal gyrus is associated with impaired canonical and noncanonical
    sentence comprehension in the acute stage of stroke recovery.
  direction: likely
  relationship: causal
  citation: '@Sheppard2022'
  method: MLPA
  design: longitudinal
  evidence_quality: cohort
  strength: moderate
  sample:
    n: 15
    population: left hemisphere stroke
    time_post_onset: average of 2.5 days (SD = 1.8) post-stroke onset at the acute time point
    phase: acute
    age_range: mean 56.0 (SD = 15.9) years
    handedness: 12 right-handed, 3 left-handed
    language: native speakers of English
  statistics:
    threshold: p <= 0.05
    effect_size: not_reported
  lesion_mapping:
    analysis: multivariate
    n_analysed: 15
    min_lesion_overlap: '>= 3 participants'
    lesion_volume_correction: covariate
    multiple_comparisons: not_reported
  confounders_controlled:
  - age
  - overall lesion volume
  - word-level comprehension deficits
  - time since stroke onset
  confounders_not_controlled: []
  region_definition:
    kind: atlas
    atlas: Johns Hopkins University (JHU) atlas
    description: Supramarginal gyrus parcel from JHU atlas
  author_limitations:
  - relatively small sample size
  - did not test patients at a subacute stage of recovery
  - do not have information about the speech language therapy some patients may have received
  - did not assess hypoperfusion
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Results, page 7
    confidence: high
    flags:
    - imaging_details.reference_space not extracted by the model — set to not_reported; verify against
      the paper
  source_passages:
  - section: Results
    page: 7
    quote: At the acute time point, more time since stroke onset, more severe word-level comprehension
      deficits and greater percent damage to SMG were implicated in impaired canonical sentence comprehension.
    supports: claim
  - section: Methods
    page: 3
    quote: Fifteen patients (6 women, 9 men) at Johns Hopkins Hospital with ischemic left hemisphere stroke
      were enrolled in this study
    supports: sample
  - section: Methods
    page: 5
    quote: Least Absolute Shrinkage and Selection Operator (LASSO) regression (Tibshirani, 1996) was used
      to evaluate whether damage to specific ROIs were related to sentence comprehension
    supports: method
  - section: Results
    page: 7
    quote: Note * denotes significance at p <= 0.05.
    supports: statistics
  - section: Methods
    page: 5
    quote: Predictors included age, overall lesion volume, number of unrelated errors on the SOAP out
      of the 40 total sentences (to control for word-level comprehension deficits), time since stroke
      onset, and percent damage to seven ROIs
    supports: confounders
  - section: Methods
    page: 3
    quote: Proportion of infarcted tissue was calculated for each participant in every anatomical parcel
      of the Johns Hopkins University (JHU) atlas
    supports: region_definition
  - section: Discussion
    page: 9
    quote: First, we have a relatively small sample size.
    supports: limitation
  imaging_details:
    reference_space: not_reported
    atlases_used: []
---
