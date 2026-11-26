---
id: semantic_processing_component
name: semantic processing component
kind: predictor
findings:
- id: f1
  target: lesion_volume
  target_kind: predictor
  claim: Among seven PCA components, only semantic processing correlated with lesion volume (r=-0.54, P<.001) in 46 people with chronic post-stroke aphasia.
  direction: likely
  relationship: correlational
  method: structural_MRI
  sample:
    n: 46
    population: patients with chronic post-stroke aphasia following a single left haemorrhagic or ischaemic stroke
    phase: not_reported
    time_post_onset: chronic stage (4-12 months post-stroke)
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - VBCM uses signal intensity per voxel as a continuous value rather than binary lesion status
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: A data-driven component extracted via principal component analysis (PCA) of a neuropsychological battery, specifically loading with comprehension tests probing semantic knowledge (e.g., picture-to-word matching and synonym judgement tests). Semantic processing was the only component correlated with lesion volume; r=-0.54, P<.001. Additional metadata has not been transcribed; review the pending-field flags before approval. Source repair (unapproved): Verified source r=-0.54 and P<.001. Lesion volume is an imaging predictor concept rather than an impairment. This is the reported component-volume correlation, distinct from voxel-wise mapping.'
  imaging_details:
    reference_space: not_reported
    atlases_used: []
  lesion_mapping: {}
  provenance:
    extracted_by: agent:source-repair
    extracted_on: '2026-11-26'
    paper_section: Main paper; qualitative core draft
    confidence: low
    flags:
    - core_profile_machine_prepared
    - human_approval_pending
    - core_text_check_only
    - paper_completeness_pending
    - pdf_visual_review_pending
    - not_transcribed:statistics
    - not_transcribed:confounders_controlled
    - not_transcribed:confounders_not_controlled
    - not_transcribed:region_definition
    - not_transcribed:imaging_details.reference_space
    - not_transcribed:imaging_details.atlases_used
    - not_transcribed:lesion_mapping
    - not_transcribed:sample.phase
    - not_transcribed:strength
    - agent_source_repair_pending_human_review
  citation: '@Alyahya2020'
  source_passages:
  - section: Original source P8-S3-C3
    page: 8
    quote: 'None of the seven fundamental components correlate with

      lesion volume except for the semantic processing component

      (r = –0.54, P 5 0.001).'
    supports: claim
  - section: Original source P3-S1-C8
    page: 3
    quote: 'Materials and methods

      Participants

      Forty-six patients who had developed aphasia following a single

      left haemorrhagic or ischaemic stroke were tested in the chronic

      stage (412 months post-stroke).'
    supports: sample
  - section: Original source P4-S2-C3
    page: 4
    quote: 'Analysis of neuroimaging data

      The unified PCA model was mapped onto brain lesions using a

      voxel-based correlational methodology (VBCM) (Tyler et al.,

      2005).'
    supports: method
  - section: Original source P8-S1-C4
    page: 8
    quote: 'The third component (19.12% variance

      explained) loaded with comprehension tests that probe se-

      mantic knowledge (e.g. picture-to-word matching and syno-

      nym

      judgement

      tests)

      and

      thus

      this

      component

      was

      interpreted as ‘semantic processing’.'
    supports: claim
predictor_type: imaging_metric
short_definition: A data-driven component extracted via principal component analysis (PCA) of a neuropsychological battery, specifically loading with comprehension tests probing semantic knowledge (e.g., picture-to-word matching and synonym judgement tests).
assessment:
- picture-to-word matching
- synonym judgement tests
schema_version: '2.8'
status: draft
created_by: agent:source-repair
created_on: '2026-11-26'
relationship_review:
  paper: Alyahya2020
  proposal_id: R024
  approved: false
  original_core_review: {}
  original_publication_entry: null
  original_mapping:
    decision: draft
    reason: The study used PCA to identify a 'semantic processing' component and then tested its correlation with lesion volume using VBCM. A significant correlation was found for this specific component, while other components showed no effect.
    bucket: predictors
    entity_id: semantic_processing_component
    name: semantic processing component
    kind: predictor
    predictor_type: imaging_metric
    definition: A data-driven component extracted via principal component analysis (PCA) of a neuropsychological battery, specifically loading with comprehension tests probing semantic knowledge (e.g., picture-to-word matching and synonym judgement tests).
    assessment:
    - picture-to-word matching
    - synonym judgement tests
    target: lesion_volume
    target_kind: impairment
    claim: The semantic processing component was the only one of seven fundamental components that correlated with lesion volume.
    direction: likely
    method: VBCM
    relationship: correlational
    therapy: null
    sample_n: 46
    population: patients with chronic post-stroke aphasia following a single left haemorrhagic or ischaemic stroke
    timing: chronic stage (4-12 months post-stroke)
    qualifications:
    - The correlation was found in an analysis without lesion volume as a covariate
    limitations:
    - VBCM uses signal intensity per voxel as a continuous value rather than binary lesion status
    optional_pending: []
    evidence_quality: cohort
    passages:
    - source_id: P8-S3-C3
      supports: claim
    - source_id: P3-S1-C8
      supports: sample
    - source_id: P4-S2-C3
      supports: method
    - source_id: P8-S1-C4
      supports: claim
  original_attempt:
    binding:
      profile: core
      version: core-source-check-v3
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      checker_model: qwen3.8:27b
      checker_digest: 47951e4a666180bc2aedfc93c169472f2de783696fe196efbf063f5730ecf163
      host: http://localhost:11434
      pdf_sha256: 7c7fe679ca9614ffbed99fcf352167912a75739289a9dcd5406488095ae29b29
      review_sha256: 2568f8e8fd3fcb3e46c5c0ec673c4dd1ad443886b7107e9ca56082c087a0b526
      code_sha256: c4650d24fa3e36e6f317cb65cc7626277a28936a7cdf5d07248d4b1e5bfa09aa
      source_helpers_sha256: e0e0f295e5efa1fdb4e9e8c84ca491d062df3aefe8ca8b4d9ca85fcb6d4c9082
      converter_sha256: 048f1e35905528676837a00b1b2406b1c97cb1eb47c48d63f121a5c00cc0afeb
      table_helpers_sha256: 78e562e9725fc484d6a12279ea710856dfd1d9aa13ee178d0358e9c0acdd2c8c
      mapper_budget: 2500
      reviewer_budget: 1600
      approved: false
      visual:
        models:
        - gemma4:31b
        - qwen3.8:27b
        digests:
        - 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        - 47951e4a666180bc2aedfc93c169472f2de783696fe196efbf063f5730ecf163
        code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
        layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
    proposal: R024
    status: failed
    reason: Target kind conflicts with existing KB concept
    material_issues: []
    seconds_this_run: 0.0628948749981646
  source_check:
    profile: agent-repair
    scope: Agent source reconstruction; original model reviews do not certify the changed record. No independent model pass or human approval.
    approved: false
    paper_complete: false
    binding:
      pdf_sha256: 7c7fe679ca9614ffbed99fcf352167912a75739289a9dcd5406488095ae29b29
      original_mapping_sha256: 641be73128e8795465042935102213fd96f8d07f0b17ecbc64e585745ccd1456
      original_status_sha256: 3ee9584ec4502a7ef533fed4e2bf498617df530249b8c43bd7f0272a2828dfea
      evidence_sha256: a2f912878162dac82e68d84efa653429115f42ccf7cfac587314b44b12a04c64
    publication_correction:
      by: agent:source-repair
      date: '2026-11-26T03:33:02.412795+00:00'
      pdf_pages:
      - 3
      - 4
      - 8
      note: Verified source r=-0.54 and P<.001. Lesion volume is an imaging predictor concept rather than an impairment. This is the reported component-volume correlation, distinct from voxel-wise mapping.
      approved: false
      audit: logs/publication/draft-repairs-2026-11-26-round3.json
    remaining:
    - Human source review and approval
    - Full paper completeness review
reviewer_marks:
- id: source-repair-round3
  status: pending
  by: agent:source-repair
  date: '2026-11-26'
  note: Verified source r=-0.54 and P<.001. Lesion volume is an imaging predictor concept rather than an impairment. This is the reported component-volume correlation, distinct from voxel-wise mapping.
---

# Source review required

This repaired draft remains unapproved. Original outputs and review provenance are preserved.
