---
schema_version: 2.8
id: left_middle_temporal_gyrus
name: Left Middle Temporal Gyrus (Ventral Stream Node)
kind: classical
status: draft
created_by: agent:ollama-extract-cli/gemma4:31b-it-q8_0
created_on: 2026-10-30
hemisphere: left
findings:
- id: f1
  target: anomia
  target_kind: impairment
  claim: Fewer propagation steps along indirect white matter connections between the left angular gyrus
    and the middle temporal gyrus significantly predict greater naming improvement after treatment in
    chronic aphasia.
  direction: likely
  relationship: responder
  citation: '@Wilmskoetter2021'
  method: tractography
  design: cross-sectional
  strength: moderate
  evidence_quality: cohort
  therapy:
    id: computerized_lexical_semantic_treatment
    name: 3-week-long computerized language treatment focusing on lexical-semantic processing
  sample:
    n: 69
    population: chronic left-hemisphere ischemic stroke and aphasia
    time_post_onset: mean 41.15 months (SD 40.00)
    phase: chronic
    age_range: mean 59.54 (SD 10.26)
    handedness: not_reported
    language: not_reported
    cohort: NCT03416738
  statistics:
    threshold: P = .012
    effect_size: standardized beta = -0.517
  confounders_controlled:
  - age
  - years of formal education
  - baseline WAB-AQ
  - treatment type
  confounders_not_controlled: []
  region_definition:
    kind: atlas
    atlas: JHU anatomical atlas
    description: Middle temporal gyrus (MTG)
  imaging_details:
    field_strength: 3T
    modalities:
    - modality: T1
      sequence: not_reported
    - modality: T2
      sequence: not_reported
    - modality: DTI
      sequence: not_reported
    preprocessing_pipeline: SPM12 normalization into standard space
    reference_space: MNI152
    atlases_used:
    - JHU anatomical atlas
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Results, page 350
    confidence: high
    flags:
    - cohort overlaps with @Fridriksson2018JAMA (same phase 2 RCT)
  source_passages:
  - section: Results
    page: 350
    quote: fewer steps along the indirect connection between the AG and MTG significantly predicted an
      increase in correct naming responses after treatment (standardized beta = -0.517, P = .012).
    supports: claim
  - section: Participants
    page: 348
    quote: We included 69 of 74 participants from the clinical trial... individuals with chronic left-hemisphere
      ischemic stroke and aphasia
    supports: sample
  - section: Limitations
    page: 353
    quote: We mapped indirect connections based on structural connectomics; thus, we cannot claim that
      these indirect pathways are indeed functionally used.
    supports: limitation
  author_limitations:
  - Structural connectomics does not guarantee functional use of the identified indirect pathways.
---
