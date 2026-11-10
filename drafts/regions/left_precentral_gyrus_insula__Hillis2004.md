---
schema_version: 2.8
id: left_precentral_gyrus_insula
name: Left precentral gyrus of the insula
kind: classical
status: draft
created_by: agent:ollama-extract-cli/gemma4:31b
created_on: 2026-11-10
hemisphere: left
findings:
- id: f1
  target: apraxia_of_speech
  target_kind: impairment
  claim: There is no significant association between acute apraxia of speech and dysfunction (infarct
    or hypoperfusion) of the left anterior insula or the superior tip of the left precentral gyrus of
    the insula.
  direction: no_effect
  relationship: causal
  citation: '@Hillis2004'
  method:
  - DWI
  - PWI
  design: cross-sectional
  strength: moderate
  evidence_quality: cohort
  sample:
    n: 80
    population: adults with first ever, non-lacunar, ischaemic stroke affecting the left MCA territory
    time_post_onset: within 24 h of onset of stroke
    phase: hyperacute
    age_range: not_reported
    handedness: all right-handed
    language: English
  statistics:
    threshold: chi-square
    effect_size: chi2(1) = 0.13
    p_value: NS
  lesion_mapping:
    analysis: univariate
    n_analysed: 80
    min_lesion_overlap: not_reported
    lesion_volume_correction: none
    multiple_comparisons: not_reported
  confounders_controlled: []
  confounders_not_controlled:
  - lesion volume
  region_definition:
    kind: manual_ROI
    description: superior tip of the left precentral gyrus of the insula
  imaging_details:
    field_strength: 1.5 Tesla
    reference_space: not_reported
    atlases_used: []
    modalities:
    - modality: DWI
      sequence: multislice, isotropic, single shot EPI
      voxel_size_mm: not_reported
      TR_ms: 10000
      TE_ms: 120
    - modality: PWI
      sequence: single shot gradient echo EPI
      TR_ms: 2000
      TE_ms: 60
  author_limitations:
  - The results indicate that the observed relationship [in chronic studies] may not be causative (i.e.
    may instead reflect the vulnerability of the insula to ischaemia in large MCA strokes).
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Results, page 1481
    confidence: high
    flags: []
  source_passages:
  - section: Results
    page: 1481
    quote: Analysis of the entire region of dysfunctional brain tissue (abnormalities on DWI and/or PWI)
      also showed no association between apraxia of speech and dysfunction (hypoperfusion and/or infarct)
      of the left insula [c2(1) = 2.5; NS], anterior insula [c2(1) = 2.8; NS] or superior tip of the precentral
      gyrus of the insula [c2(1) = 0.13; NS; Table 2].
    supports: claim
  - section: Methods - Subjects
    page: 2
    quote: Subjects were adults with first ever, non-lacunar, ischaemic stroke affecting the left MCA
      territory as determined by MRI.
    supports: sample
  - section: Methods - Imaging
    page: 3
    quote: MRI scans included DWI and fluid attenuated inversion recovery (FLAIR) to identify the extent
      of damaged or severely ischaemic tissue, and PWI to identify areas of delayed arrival and clearance
      of a bolus of contrast... Scans were done on a GE Signa 1.5 Tesla
    supports: method
  - section: Results
    page: 1481
    quote: Analysis of the entire region of dysfunctional brain tissue (abnormalities on DWI and/or PWI)
      also showed no association between apraxia of speech and dysfunction... superior tip of the precentral
      gyrus of the insula [c2(1) = 0.13; NS; Table 2].
    supports: statistics
  - section: Discussion
    page: 1483
    quote: Our results indicate that the observed relationship may not be causative (i.e. may instead
      reflect the vulnerability of the insula to ischaemia in large MCA strokes).
    supports: limitation
---
