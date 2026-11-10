---
schema_version: 2.8
id: left_arcuate_fasciculus_slf
name: Left Arcuate Fasciculus and Superior Longitudinal Fascicle (Dorsal Language Pathway)
kind: tract
status: draft
created_by: agent:ollama-extract-cli/gemma4:31b
created_on: 2026-11-10
hemisphere: left
findings:
- id: f1
  target: severity_metric
  target_kind: predictor
  claim: Lesion load of the left SLF is a significant independent predictor of aphasia severity in subacute
    stroke.
  direction: likely
  relationship: causal
  citation: '@Yu2024'
  method: RLSM
  design: cross-sectional
  strength: moderate
  evidence_quality: cohort
  sample:
    n: 46
    population: right-handed patients with post-stroke aphasia
    time_post_onset: median 23.50 (41) days, range, 5-89 days
    phase: early_subacute
    age_range: mean 56.09 (12.46) years, range, 25-78 years
    handedness: all right-handed
    language: Chinese speakers
  statistics:
    threshold: p < 0.001
    effect_size: R2 = 0.413 (Model I)
  lesion_mapping:
    analysis: region_based
    n_analysed: 46
    min_lesion_overlap: not_reported
    lesion_volume_correction: not_reported
    multiple_comparisons: not_reported
  confounders_controlled:
  - Areas-LL
  - IFOF-LL
  confounders_not_controlled:
  - lesion volume
  region_definition:
    kind: atlas
    atlas: JHU-ICBM-tracts-prob-thr25-2mm
    description: Left SLF extracted from JHU White Matter Tractography Atlas.
  imaging_details:
    field_strength: 3.0 Tesla
    reference_space: MNI152
    atlases_used:
    - JHU-ICBM-tracts-prob-thr25-2mm
    preprocessing_pipeline: FSL 5.0.9, FLIRT registration to MNI152
  author_limitations:
  - The sample was relatively small, which limits the generalizability of the results.
  - Conclusions based solely on lesion load might be misleading compared to tract disconnection.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Results, page 4
    confidence: high
    flags: []
  source_passages:
  - section: Results
    page: 4
    quote: The result of Model I showed that 41.3 % of the variation in aphasia severity can be explained
      by the SLF-LL (F = 32.620, p < 0.001, R2 = 0.413).
    supports: claim
  - section: Materials and methods
    page: 3
    quote: Several critical sub-cortical language-related neural tracts were extracted from the Johns
      Hopkins University (JHU) White Matter Tractography Atlas (JHU-ICBM-tracts-prob-thr25-2 mm)
    supports: region_definition
  - section: Discussion
    page: 9
    quote: First, the sample was relatively small, which limits the generalizability of the results.
    supports: limitation
---
