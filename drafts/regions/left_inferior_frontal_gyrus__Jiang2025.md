---
schema_version: 2.8
id: left_inferior_frontal_gyrus
name: Left Inferior Frontal Gyrus
kind: classical
status: draft
created_by: agent:ollama-extract-cli/gemma4:31b-it-q8_0
created_on: 2026-10-30
hemisphere: left
findings:
- id: f1
  target: form_to_meaning
  target_kind: impairment
  claim: In the subacute phase, both frontal and temporo-parietal stroke patients show facilitatory effective
    connectivity from the left posterior temporal lobe to the left IFG during sentence comprehension.
  direction: likely
  relationship: correlational
  citation: '@Jiang2025'
  method: fMRI_activation
  design: longitudinal
  strength: moderate
  evidence_quality: cohort
  sample:
    n: 34
    population: patients with left-hemispheric frontal or temporo-parietal stroke
    time_post_onset: 1-2 weeks
    phase: mixed
    language: German
  statistics:
    threshold: posterior probability > 95%
    effect_size: 'frontal: 0.334; temporo-parietal: 0.354'
  confounders_controlled: []
  confounders_not_controlled:
  - ' lesion heterogeneity'
  region_definition:
    kind: peak_coord_sphere
    mni_peak:
    - -39
    - 29
    - -13
    radius_mm: 20
    description: Sphere around mean group coordinate for auditory speech processing contrast.
  imaging_details:
    field_strength: 3T
    preprocessing_pipeline: SPM12 (slice-timing correction, spatial realignment, coregistration, normalization,
      resampling and smoothing)
    reference_space: MNI152
    atlases_used: []
    task:
      name: Auditory sentence comprehension
      description: Participants listened to short German sentences and temporally reversed versions.
      contrasts:
      - auditory speech > reversed speech
      baseline: reversed speech
  author_limitations:
  - Small sample size (n=17 per group).
  - Findings may not generalize to speech production.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Results, page 5
    confidence: high
    flags:
    - ' cohort overlaps with @Stockert2022 (same participants)'
  source_passages:
  - section: Results
    page: 5
    quote: In the subacute phase (Fig. 2C), we observed speech processing-induced facilitation of connectivity
      from lPTL to lIFG (0.334).
    supports: claim
  - section: Results
    page: 5
    quote: In the subacute phase (Fig. 2F), comparable to patients with frontal lesions, we found auditory
      speech processing-induced facilitation from lPTL to lIFG (0.354).
    supports: claim
  - section: Materials and methods
    page: 3
    quote: Two groups of patients with either frontal (n = 17...) or temporo-parietal (n = 17...)
    supports: sample
  - section: Statistical analysis
    page: 5
    quote: Significant patterns of effective connectivity... were obtained by thresholding the Bayesian
      Model Average to exclusively retain parameters with a posterior probability larger than 95%
    supports: statistics
  - section: Materials and methods
    page: 3
    quote: The final set of ROIs representing the LN were in the pars orbitalis in the left IFG [IFGorb,
      Montreal Neurological Institute (MNI) coordinates x = −39, y = 29, z = −13]
    supports: region_definition
  - section: Limitations
    page: 11
    quote: there were ultimately only 17 patients in each group.
    supports: limitation
  - section: Limitations
    page: 11
    quote: our findings may not generalize to speech production.
    supports: limitation
---
