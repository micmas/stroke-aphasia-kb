---
schema_version: 2.8
id: left_ifg_pars_opercularis
name: Left IFG Pars Opercularis (Broca's area, dorsal stream hub)
kind: classical
status: draft
created_by: agent:ollama-extract-cli/gemma4:31b-it-q8_0
created_on: 2026-10-30
hemisphere: left
findings:
- id: f1
  target: syntactic_processing
  target_kind: impairment
  claim: Damage to Broca's area (including pars opercularis) is associated with impaired noncanonical
    sentence comprehension and asyntactic comprehension patterns in the chronic stage of stroke recovery.
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
    time_post_onset: average of 21.4 months (SD = 22.3) post-stroke onset at the chronic time point
    phase: chronic
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
    description: Broca's area (IFGtri + IFGop) parcel from JHU atlas
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
    quote: The model of noncanonical sentence comprehension at the chronic time point contained proportion
      of damage to Broca's area and pSTG; proportion of damage to pSTG was the only significant independent
      predictor.
    supports: claim
  - section: Results
    page: 7
    quote: Broca's area was implicated in more severe deficits at the chronic time point along with more
      time since stroke onset and greater word-level comprehension deficits. Damage to Broca's area was
      the only significant independent predictor in the model of chronic asyntactic comprehension.
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
