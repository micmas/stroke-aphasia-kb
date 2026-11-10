---
schema_version: 2.8
id: inhibitory_rtms_right_ifg
name: Inhibitory rTMS to right posterior inferior frontal gyrus
kind: therapy
status: draft
created_by: agent:ollama-extract-cli/gemma4:31b
created_on: 2026-11-10
targets_impairments:
- anomia
- form_to_meaning
- fluency
dosage: 10 days of 20-minute sessions followed by 45 minutes of SLT
findings:
- id: f1
  target: severity_metric
  target_kind: predictor
  claim: Inhibitory 1 Hz rTMS over the right posterior inferior frontal gyrus, combined with speech and
    language therapy, significantly improves global aphasia recovery in subacute stroke.
  direction: likely
  relationship: responder
  citation: '@Thiel2013'
  method: clinical_RCT
  design: RCT
  strength: moderate
  evidence_quality: RCT
  sample:
    n: 24
    population: subacute poststroke aphasia
    time_post_onset: average treatment onset time was 5.4 weeks (TMS group) and 7.2 weeks (sham group)
    phase: early_subacute
    age_range: not_reported
    handedness: all right handed
    language: German
  statistics:
    threshold: P=0.003
    effect_size: mean 23.6±SD 12.15 (TMS) vs 7.55±SD 11.00 (sham)
  confounders_controlled:
  - initial test performance
  confounders_not_controlled:
  - infarct size
  - infarct location
  author_limitations:
  - The study was underpowered to detect a specific aphasia type and treatment interaction.
  - The same limitation holds for possible differential effects of infarct size and location.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Results, page 2241
    confidence: high
    flags: []
  therapy:
    id: inhibitory_rtms_right_ifg
    name: inhibitory 1 Hz rTMS over the right triangular part of the posterior inferior frontal gyrus
    dose: 10-day protocol of 20-minute sessions followed by 45 minutes of SLT
  source_passages:
  - section: Results
    page: 2241
    quote: Aphasia recovery measured as absolute change in global AAT score was significantly higher in
      the TMS group (mean 23.6±SD 12.15) than in the sham group (mean 7.55±SD 11.00; P=0.003; Figure 1A;
      Table 2).
    supports: claim
  - section: Methods
    page: 2241
    quote: Twenty-four patients with subacute poststroke aphasia were randomized to a 10-day protocol
      of 20-minute inhibitory 1 Hz rTMS over the right triangular part of the posterior inferior frontal
      gyrus or sham stimulation, followed by 45 minutes of speech and language therapy.
    supports: method
  - section: Methods
    page: 2241
    quote: All patients were right handed, with German as the first language.
    supports: sample
  - section: Discussion
    page: 2244
    quote: however, the study was underpowered to detect a specific aphasia type and treatment interaction,
      so larger studies are needed to specifically address this question.
    supports: limitation
  region_definition:
    kind: not_reported
- id: f2
  target: anomia
  target_kind: impairment
  claim: Inhibitory rTMS to the right posterior inferior frontal gyrus combined with SLT most strongly
    improves naming performance.
  direction: likely
  relationship: responder
  citation: '@Thiel2013'
  method: clinical_RCT
  design: RCT
  strength: moderate
  evidence_quality: RCT
  sample:
    n: 24
    population: subacute poststroke aphasia
    time_post_onset: average treatment onset time was 5.4 weeks (TMS group) and 7.2 weeks (sham group)
    phase: early_subacute
    age_range: not_reported
    handedness: all right handed
    language: German
  statistics:
    threshold: P=0.002
    effect_size: not_reported
  confounders_controlled:
  - initial test performance
  confounders_not_controlled:
  - infarct size
  - infarct location
  author_limitations:
  - The study was underpowered to detect a specific aphasia type and treatment interaction.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Results, page 2241
    confidence: high
    flags: []
  therapy:
    id: inhibitory_rtms_right_ifg
    name: inhibitory 1 Hz rTMS over the right triangular part of the posterior inferior frontal gyrus
    dose: 10-day protocol of 20-minute sessions followed by 45 minutes of SLT
  source_passages:
  - section: Results
    page: 2241
    quote: The mean increase in subtest scores was higher for the TMS group in all subtests. It was highest
      for subtest naming (P=0.002)
    supports: claim
  - section: Discussion
    page: 2243
    quote: Consistent with previous studies, the strongest increase was observed on naming performance.
    supports: claim
  region_definition:
    kind: not_reported
- id: f3
  target: right_posterior_inferior_frontal_gyrus
  target_kind: region
  claim: Inhibitory rTMS to the right posterior inferior frontal gyrus favors the recruitment of left-hemispheric
    language networks during recovery.
  direction: likely
  relationship: treatment_response
  citation: '@Thiel2013'
  method:
  - fMRI_activation
  - clinical_RCT
  design: RCT
  strength: moderate
  evidence_quality: RCT
  sample:
    n: 24
    population: subacute poststroke aphasia
    time_post_onset: average treatment onset time was 5.4 weeks (TMS group) and 7.2 weeks (sham group)
    phase: early_subacute
    age_range: not_reported
    handedness: all right handed
    language: German
  statistics:
    threshold: P=0.002
    effect_size: TMS 40.9±29.91 vs sham -9.8±39.71 (AVI change)
  confounders_controlled:
  - initial test performance
  confounders_not_controlled:
  - infarct size
  - infarct location
  author_limitations:
  - The study was underpowered to detect a specific aphasia type and treatment interaction.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Results, page 2242
    confidence: high
    flags: []
  therapy:
    id: inhibitory_rtms_right_ifg
    name: inhibitory 1 Hz rTMS over the right triangular part of the posterior inferior frontal gyrus
    dose: 10-day protocol of 20-minute sessions followed by 45 minutes of SLT
  region_definition:
    kind: manual_ROI
    description: triangular part of the right posterior inferior frontal gyrus
  imaging_details:
    reference_space: MNI152
    atlases_used: []
    preprocessing_pipeline: spatially normalized to MNI space using SPM8
    modalities:
    - modality: PET
      sequence: O-15-water positron emission tomography
      voxel_size_mm:
      - 2.2
      - 2.2
      - 3.125
    task:
      name: verb generation
      description: patients were instructed to generate out loud 1 semantically matching verb to each
        noun
      contrasts:
      - activation > baseline
      baseline: eyes closed and no auditory input
  source_passages:
  - section: Results
    page: 2242
    quote: Changes in AVI were significantly larger in the treatment group (TMS 40.9±29.91) compared with
      the sham group (sham -9.8±39.71), indicating a shift toward the left hemisphere in the TMS and a
      consolidation of the right-hemispheric network in the sham group (P=0.002; Figure 2A; Table 2).
    supports: claim
  - section: Methods
    page: 2241
    quote: 8 consecutive measurements of relative cerebral blood flow with O-15-water (370 MBq per injection)
      were performed on a CTI/Siemens ECAT EXACT HR scanner in 3-dimensional (3D) mode.
    supports: imaging_details
  - section: Methods
    page: 2241
    quote: The 8 PET images of each patient were spatially normalized to MNI space using SPM8 (Wellcome
      Trust Center for Neuroimaging).
    supports: imaging_details
---
