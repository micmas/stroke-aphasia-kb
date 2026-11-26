---
id: tuf_wh_movement
name: TUF treatment of wh-movement structures
kind: therapy
findings:
- id: f1
  target: sentence_comprehension
  target_kind: impairment
  claim: 'Post-treatment Northwestern Sentence Comprehension Test results showed gains for specific sentence types: actives in participant 2, passives in participants 2, 3 and 4, and subject relatives in participants 2 and 4. The Discussion broadly describes improvement across sentence types for most participants.'
  direction: likely
  relationship: treatment_response
  method: behavioral_only
  sample:
    n: 4
    population: Four participants with Broca’s aphasia and agrammatism in a single-subject experimental design.
    phase: not_reported
    time_post_onset: 1–11 years post-stroke.
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - small sample size (N=4)
  evidence_quality: case-study
  strength: weak
  notes: 'Reconstructed the saved mapping after an incomplete checker response, using the original article passages. This is an agent source check, not a completed model review or human approval. Corrected the design to the reported single-subject experiment; no randomized trial. Training-order contrasts involve two participants each. Source repair (unapproved): Reconstructed the saved mapping after an incomplete checker response, using the original article passages. This is an agent source check, not a completed model review or human approval. Corrected the design to the reported single-subject experiment; no randomized trial. Training-order contrasts involve two participants each.'
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
  therapy:
    id: tuf
    name: TUF
  citation: '@Thompson2003'
  source_passages:
  - section: Original source P10-S1-C6
    page: 10
    quote: "In addition, improvement was noted on post- \ntreatment administration of the Northwestern Sentence \nComprehension Test for some sentence types."
    supports: claim
  - section: Original source P10-S1-C7
    page: 10
    quote: "All showed \nincreases in percent correct production of object rela- \ntives; Participant 2 showed gains in comprehension of \nactives; Participants 2, 3, and 4 evinced increases in com- \nprehension of passives; Participants 2 and 4 improved \ntheir comprehension of subject relatives. \n"
    supports: claim
  - section: Original source P12-S2-C10
    page: 12
    quote: "In addition, posttreatment administration of the North- \nwestern Sentence Comprehension Test showed improved \ncomprehension of all sentence types for most partici- \npants."
    supports: claim
  - section: Original source P4-S2-C11
    page: 4
    quote: "Method \nParticipants \nFour individuals with Broca’s aphasia with agram- \nmatism participated in the study."
    supports: sample
  - section: Original source P7-S1-C5
    page: 7
    quote: "Treatment \nParticipants were trained to comprehend and pro- \nduce each sentence type using TUF."
    supports: method
  - section: Original source P7-S1-C6
    page: 7
    quote: "This linguistic-spe- \ncific treatment uses the active form of target sentences \nto train participants to (a) comprehend and produce the \nverbs and the NPs representing the arguments of the \nverb in each sentence, (b) move the proper sentence con- \nstituents to form target sentence structures, (c) produce \nthe surface form of the target sentence, and (d) compre- \nhend and produce the verbs and verb arguments in their \nnoncanonical position."
    supports: method
  design: case-series
schema_version: '2.8'
status: draft
created_by: agent:source-repair
created_on: '2026-11-26'
relationship_review:
  paper: Thompson2003
  proposal_id: R007
  approved: false
  original_core_review: {}
  original_publication_entry: null
  original_mapping:
    decision: draft
    reason: The study evaluates the effect of a specific linguistic treatment (TUF) on sentence comprehension and production in patients with agrammatic Broca's aphasia, specifically focusing on wh-movement structures. The finding regarding the Northwestern Sentence Comprehension Test is explicitly stated as a posttreatment improvement.
    bucket: therapies
    entity_id: tuf_wh_movement
    name: TUF treatment of wh-movement structures
    kind: therapy
    predictor_type: clinical
    definition: Linguistic-specific treatment using the active form of target sentences to train participants to comprehend and produce verbs and NPs, move sentence constituents to form target structures, and produce/comprehend verbs and arguments in noncanonical positions.
    assessment:
    - Northwestern Sentence Comprehension Test
    target: sentence_comprehension
    target_kind: impairment
    claim: Posttreatment administration of the Northwestern Sentence Comprehension Test showed improved comprehension of all sentence types for most participants, including increases in comprehension of actives, passives, and subject relatives for specific participants.
    direction: likely
    method: clinical_RCT
    relationship: treatment_response
    therapy:
      id: tuf
      name: TUF
    sample_n: 4
    population: individuals with Broca's aphasia with agrammatism
    timing: posttreatment
    qualifications:
    - improvement in comprehension of actives was noted for Participant 2
    - improvement in comprehension of passives was noted for Participants 2, 3, and 4
    - improvement in comprehension of subject relatives was noted for Participants 2 and 4
    limitations:
    - small sample size (N=4)
    optional_pending: []
    evidence_quality: cohort
    passages:
    - source_id: P10-S1-C6
      supports: claim
    - source_id: P10-S1-C7
      supports: claim
    - source_id: P12-S2-C10
      supports: claim
    - source_id: P4-S2-C11
      supports: sample
    - source_id: P7-S1-C5
      supports: method
    - source_id: P7-S1-C6
      supports: method
  original_attempt:
    binding:
      profile: core
      version: core-source-check-v3
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      checker_model: qwen3.8:27b
      checker_digest: 47951e4a666180bc2aedfc93c169472f2de783696fe196efbf063f5730ecf163
      host: http://localhost:11434
      pdf_sha256: 2a2d9be43ae21651d18035a60374c8dc5e7fb10a9d2ab5ca8b4cf27c2dd2fe3a
      review_sha256: 43bbc24fec5b8c696fe292b23c4e17c81df386e1770eb369fd15244130cd1826
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
    proposal: R007
    status: failed
    reason: Truncated output held
    seconds_this_run: 155.19017325001187
  source_check:
    profile: agent-repair
    scope: Agent source reconstruction; original model reviews do not certify the changed record. No independent model pass or human approval.
    approved: false
    paper_complete: false
    binding:
      pdf_sha256: 2a2d9be43ae21651d18035a60374c8dc5e7fb10a9d2ab5ca8b4cf27c2dd2fe3a
      original_mapping_sha256: 432694c045a0540ae4fed22a5a7d820545b7c4e467df25d8fcac34911ede31b6
      original_status_sha256: f832a0e0851097922f3b1daf7eb0fe74a96dfdfe3552d36bb43ffedb409e3037
      evidence_sha256: 2cda6bf1fcbe26d5c2a4baf7c7e50da2bac4728b3bea8c3e880f9edca9622f97
    publication_correction:
      by: agent:source-repair
      date: '2026-11-26T02:05:16.806224+00:00'
      pdf_pages:
      - 4
      - 7
      - 10
      - 12
      note: Reconstructed the saved mapping after an incomplete checker response, using the original article passages. This is an agent source check, not a completed model review or human approval. Corrected the design to the reported single-subject experiment; no randomized trial. Training-order contrasts involve two participants each.
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
  note: Reconstructed the saved mapping after an incomplete checker response, using the original article passages. This is an agent source check, not a completed model review or human approval. Corrected the design to the reported single-subject experiment; no randomized trial. Training-order contrasts involve two participants each.
---

# Source review required

This repaired draft remains unapproved. Original outputs and review provenance are preserved.
