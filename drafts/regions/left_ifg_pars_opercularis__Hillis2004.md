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
  target: apraxia_of_speech
  target_kind: impairment
  claim: Dysfunction (infarct or hypoperfusion) of the left posterior inferior frontal gyrus (Broca's
    area) is strongly associated with acute apraxia of speech.
  direction: likely
  relationship: causal
  citation: '@Hillis2004'
  method:
  - DWI
  - PWI
  design: cross-sectional
  strength: strong
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
    effect_size: chi2(1) = 46.4
    p_value: P < 0.00001
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
    description: left posterior inferior frontal gyrus (Broca's area)
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
  - Broca's area is unlikely to be the only area essential for orchestrating speech production, as some
    patients had apraxia of speech without Broca's area dysfunction.
  - Individual variability in brain shape or structure-function relationships may lead to missing abnormalities
    in Broca's area.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Results, page 1481
    confidence: high
    flags: []
  source_passages:
  - section: Results
    page: 1481
    quote: Instead, the presence of apraxia of speech was associated with hypoperfusion and/or infarct
      of Broca's area [c2(1) = 46.4; P < 0.00001; Table 3], but not with other regions evaluated.
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
    quote: the presence of apraxia of speech was associated with hypoperfusion and/or infarct of Broca's
      area [c2(1) = 46.4; P < 0.00001; Table 3]
    supports: statistics
  - section: Discussion
    page: 1483
    quote: Broca's area is unlikely to be the only area essential for orchestrating speech production,
      since five patients had apraxia of speech with no evidence of functional inactivation of Broca's
      area on MRI.
    supports: limitation
---
