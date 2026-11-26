---
id: left_ba37__Hillis2007__R008
name: left BA 37 cluster
kind: review
findings:
- id: f1
  target: modality_independent_lexical_access
  target_kind: impairment
  claim: Hillis2007 reports, based on the historical clinical literature summarized in this 2007 review, that lesions in left BA 37 are associated with modality-independent lexical access disruption, and restoration of tissue function in this area is associated with recovery of this process.
  direction: likely
  relationship: synthesis
  method: narrative_review
  sample:
    n: not_reported
    population: Previously reported stroke/aphasia studies and methodological literature summarized by Hillis2007; no newly recruited cohort.
    phase: not_reported
    time_post_onset: See cited primary reports; varies across review.
  statistics:
    threshold: not_applicable_review_synthesis
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - localization of functions can only be approximate due to individual variability in cytoarchitectural boundaries and brain shape
  evidence_quality: narrative-review
  strength: weak
  notes: 'Corrected primary-study misclassification to an explicitly attributed review summary. No new independent cohort or pooled effect is asserted. Source passages preserve cited study references; human primary-source review remains pending. Source repair (unapproved): Corrected primary-study misclassification to an explicitly attributed review summary. No new independent cohort or pooled effect is asserted. Source passages preserve cited study references; human primary-source review remains pending.'
  imaging_details:
    reference_space: not_applicable
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
    - not_transcribed:sample.n
    - agent_source_repair_pending_human_review
  citation: '@Hillis2007'
  source_passages:
  - section: Original source P3-S2-C7
    page: 3
    quote: 'There is a great deal of individual

      variability in the boundaries of the cytoarchitectural

      fields identified by Brodmann, as well as in the pat-

      tern of sulci and gyri and general shape of individual

      brains.38,39 Therefore, “localization” of functions

      can only be approximate.'
    supports: limitation
  - section: Original source P9-S1-C6
    page: 9
    quote: 'For instance, lesions in left BA 37

      are associated with modality-independent lexical

      access,106,107 and restoration of tissue function in BA

      37 is associated with recovery of modality-

      '
    supports: claim
  - section: Original source P9-S2-C1
    page: 9
    quote: 'are associated with modality-independent lexical

      access,106,107 and restoration of tissue function in BA

      37 is associated with recovery of modality-

      independent lexical access.108 Diffusion tensor imag-

      ing and tractography are promising methods of

      identifying white matter tracks that connect various

      components of the neural network underlying nam-

      ing and other language tasks.53,109 To complement

      the imaging of structural connections, magnetoen-

      cephalography can reveal neural networks through

      the functional connectivity between areas revealed

      by simultaneous activation.110

      Some levels of representation computed in nam-

      ing are likely to be more distributed than others.'
    supports: claim
  - section: Original source P1-S2-C1
    page: 1
    quote: 'well articulated but meaningless.3

      Although localization of functions in the brain lost favor in the early 20th century, these

      early observations provided some of the groundwork for Norman Geschwind’s5 seminal

      writings on aphasia classification and associated sites of lesions, briefly reviewed in this

      article.'
    supports: method
  - section: Original source P1-S2-C1
    page: 1
    quote: 'well articulated but meaningless.3

      Although localization of functions in the brain lost favor in the early 20th century, these

      early observations provided some of the groundwork for Norman Geschwind’s5 seminal

      writings on aphasia classification and associated sites of lesions, briefly reviewed in this

      article.'
    supports: sample
  design: narrative-review
schema_version: '2.9'
status: draft
created_by: agent:source-repair
created_on: '2026-11-26'
relationship_review:
  paper: Hillis2007
  proposal_id: R008
  approved: false
  original_core_review: {}
  original_publication_entry: null
  original_mapping:
    decision: draft
    reason: The source explicitly associates lesions in left BA 37 with modality-independent lexical access disruption and notes that restoration of this area is associated with recovery of that function.
    bucket: regions
    entity_id: left_ba37
    name: left BA 37 cluster
    kind: network
    predictor_type: imaging_metric
    definition: Patient lesion overlap with left Brodmann area 37 (posterior middle-inferior temporal and fusiform gyri).
    assessment: []
    target: modality_independent_lexical_access
    target_kind: impairment
    claim: Lesions in left BA 37 are associated with modality-independent lexical access disruption, and restoration of tissue function in this area is associated with recovery of this process.
    direction: likely
    method: LSM
    relationship: correlational
    therapy: null
    sample_n: null
    population: patients with aphasia
    timing: not_transcribed
    qualifications: []
    limitations:
    - localization of functions can only be approximate due to individual variability in cytoarchitectural boundaries and brain shape
    optional_pending: []
    evidence_quality: cohort
    passages:
    - source_id: P9-S1-C6
      supports: claim
    - source_id: P9-S2-C1
      supports: claim
    - source_id: P3-S2-C7
      supports: limitation
  original_attempt:
    binding:
      profile: core
      version: core-source-check-v3
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      checker_model: qwen3.8:27b
      checker_digest: 47951e4a666180bc2aedfc93c169472f2de783696fe196efbf063f5730ecf163
      host: http://localhost:11434
      pdf_sha256: c801ff6927ade291fadd0f394a819dd9a4b8c2fa2a78e8076224ad6cad6c5efc
      review_sha256: 69e4e8edbc539040cac28425628c6c9491f8c958bdefccefa5dd77a6c06734f3
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
    proposal: R008
    status: failed
    reason: Claim, population and method source evidence required
    seconds_this_run: 21.793814541000756
  source_check:
    profile: agent-repair
    scope: Agent source reconstruction; original model reviews do not certify the changed record. No independent model pass or human approval.
    approved: false
    paper_complete: false
    binding:
      pdf_sha256: c801ff6927ade291fadd0f394a819dd9a4b8c2fa2a78e8076224ad6cad6c5efc
      original_mapping_sha256: 48fb20f146ac1504ab5956effc994f43735bf0028ee720ec37a981c5543d2b7f
      original_status_sha256: d3cd9abd49d3b2e2474d36aec5b0f743447caaa4111f11678f20a08c41ddf4c0
      evidence_sha256: a32ab4fef8f10e19aaf126cb20d5d3e1c57870606881add2b16e3385f1b6ad9e
    publication_correction:
      by: agent:source-repair
      date: '2026-11-26T02:05:16.806224+00:00'
      pdf_pages:
      - 1
      - 9
      note: Corrected primary-study misclassification to an explicitly attributed review summary. No new independent cohort or pooled effect is asserted. Source passages preserve cited study references; human primary-source review remains pending.
      approved: false
      audit: logs/publication/draft-repairs-2026-11-26-round2.json
    remaining:
    - Human source review and approval
    - Full paper completeness review
reviewer_marks:
- id: source-repair-round2
  status: pending
  by: agent:source-repair
  date: '2026-11-26'
  note: Corrected primary-study misclassification to an explicitly attributed review summary. No new independent cohort or pooled effect is asserted. Source passages preserve cited study references; human primary-source review remains pending.
---

# Source review required

This repaired draft remains unapproved. Original outputs and review provenance are preserved.
