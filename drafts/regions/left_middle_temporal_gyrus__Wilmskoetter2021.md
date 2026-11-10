---
schema_version: 2.8
id: left_middle_temporal_gyrus
name: Left Middle Temporal Gyrus (Ventral Stream Node)
kind: classical
status: draft
created_by: agent:ollama-extract-cli/gemma4:31b
created_on: 2026-11-10
hemisphere: left
findings:
- id: f1
  target: anomia
  target_kind: impairment
  claim: 'The response to anodal tDCS during naming treatment is moderated by the connectivity between
    the left IFG pars opercularis and the middle temporal gyrus: those with indirect connections benefit
    more from A-tDCS, while those with direct connections benefit more from sham stimulation.'
  direction: likely
  relationship: responder
  citation: '@Wilmskoetter2021'
  method: tractography
  design: longitudinal
  strength: moderate
  evidence_quality: cohort
  sample:
    n: 69
    population: chronic left-hemisphere ischemic stroke and aphasia
    time_post_onset: 6 to 202 months
    phase: chronic
    age_range: mean 59.54 (SD 10.26)
    handedness: not_reported
    language: not_reported
    cohort: NCT01927302
  statistics:
    threshold: P < .05
    effect_size: F[2, 56] = 3.45, P = .039
    p_value: '.039'
  confounders_controlled:
  - age
  - education
  - baseline WAB-AQ
  - treatment type (A-tDCS vs S-tDCS)
  confounders_not_controlled: []
  region_definition:
    kind: atlas
    atlas: JHU anatomical atlas
    description: middle temporal gyrus (MTG)
  therapy:
    id: tdcs_aphasia_treatment
    name: anodal transcranial direct current stimulation (A-tDCS) supplemented computerized language treatment
    dose: 3-week-long
  imaging_details:
    field_strength: 3T
    reference_space: MNI152
    atlases_used:
    - JHU anatomical atlas
    preprocessing_pipeline: SPM12 normalization
  author_limitations:
  - The tDCS type was not randomized according to connection type, meaning the interaction may reflect
    other group differences.
  - Indirect pathways were mapped based on structural connectomics; functional use is not confirmed.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Results, page 351
    confidence: high
    flags:
    - cohort overlaps with @Fridriksson2018JAMA (same NCT01927302 trial)
  source_passages:
  - section: Results
    page: 351
    quote: For the IFGop and MTG we revealed a significant interaction between connection type and treatment
      type on change in correct naming (F[2, 56] = 3.45 P = .039).
    supports: claim
  - section: Results
    page: 351
    quote: Participants with direct connections between the IFGop and MTG who received S-tDCS significantly
      improved... Participants with indirect connections between the IFGop and MTG who received A-tDCS
      significantly improved
    supports: claim
  - section: Discussion
    page: 352
    quote: these findings require cautious interpretation because the tDCS type was not randomized according
      to connection type.
    supports: limitation
---

Notes: This finding highlights a specific interaction between structural connectivity (direct vs indirect) and the efficacy of tDCS in treating anomia.
