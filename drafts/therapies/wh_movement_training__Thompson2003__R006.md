---
id: wh_movement_training
name: wh-movement structure training
kind: therapy
findings:
- id: f1
  target: verb_naming_and_sentence_production
  target_kind: impairment
  claim: All participants showed improved verb naming and sentence production, reflecting improved production of verbs and verb argument structure, following treatment of wh-movement structures.
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
    id: wh_movement_training
    name: wh-movement structure training
  citation: '@Thompson2003'
  source_passages:
  - section: Original source P10-S1-C5
    page: 10
    quote: "All participants showed im- \nproved verb naming and sentence production, reflect- \ning improved production of verbs and verb argument \nstructure."
    supports: claim
  - section: Original source P12-S2-C9
    page: 12
    quote: "Participants also \nshowed improvements on other posttreatment language \nmeasures (i.e., all showed improved verb naming and \nsentence production on the Verb Production Battery)."
    supports: claim
  - section: Original source P4-S2-C11
    page: 4
    quote: "Method \nParticipants \nFour individuals with Broca’s aphasia with agram- \nmatism participated in the study."
    supports: sample
  - section: Original source P7-S1-C5
    page: 7
    quote: "Treatment \nParticipants were trained to comprehend and pro- \nduce each sentence type using TUF."
    supports: method
  - section: Original source P5-S1-C5
    page: 5
    quote: "Verb production was tested extensively using a bat- \ntery of tests developed to examine naming and compre- \nhension of verbs by argument structure type as well as \nproduction of verbs and their arguments in sentences \n(The Northwestern Verb Production Battery; Thomp- \nson, unpublished)."
    supports: method
  design: case-series
schema_version: '2.8'
status: draft
created_by: agent:source-repair
created_on: '2026-11-26'
relationship_review:
  paper: Thompson2003
  proposal_id: R006
  approved: false
  original_core_review: {}
  original_publication_entry: null
  original_mapping:
    decision: draft
    reason: The study reports a treatment effect of wh-movement structure training on general language measures (verb naming and sentence production) in patients with Broca's aphasia.
    bucket: therapies
    entity_id: wh_movement_training
    name: wh-movement structure training
    kind: therapy
    predictor_type: clinical
    definition: Training to comprehend and produce sentences involving wh-movement (object-extracted who-questions, object clefts, and object-relative clauses) using a linguistic-specific treatment (TUF) involving active form training, constituent card manipulation, and production priming.
    assessment:
    - Northwestern Verb Production Battery
    target: verb_naming_and_sentence_production
    target_kind: impairment
    claim: All participants showed improved verb naming and sentence production, reflecting improved production of verbs and verb argument structure, following treatment of wh-movement structures.
    direction: likely
    method: behavioral_only
    relationship: treatment_response
    therapy:
      id: wh_movement_training
      name: wh-movement structure training
    sample_n: 4
    population: individuals with Broca's aphasia with agrammatism
    timing: posttreatment
    qualifications:
    - improvement was noted regardless of whether participants received treatment on complex versus simple sentence types
    limitations:
    - small sample size (N=4)
    optional_pending: []
    evidence_quality: cohort
    passages:
    - source_id: P10-S1-C5
      supports: claim
    - source_id: P12-S2-C9
      supports: claim
    - source_id: P4-S2-C11
      supports: sample
    - source_id: P7-S1-C5
      supports: method
    - source_id: P5-S1-C5
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
    proposal: R006
    status: failed
    reason: Truncated output held
    seconds_this_run: 149.15332579199458
  source_check:
    profile: agent-repair
    scope: Agent source reconstruction; original model reviews do not certify the changed record. No independent model pass or human approval.
    approved: false
    paper_complete: false
    binding:
      pdf_sha256: 2a2d9be43ae21651d18035a60374c8dc5e7fb10a9d2ab5ca8b4cf27c2dd2fe3a
      original_mapping_sha256: ddf3b033f5d02cf9b072371e11541314bd6ad1c80214328e28a212ab9aa70d34
      original_status_sha256: 559c99d5567c0dd53cb0b11c8ee5d906813fe530489b7d25b8ef89d1cefb4c88
      evidence_sha256: 2cda6bf1fcbe26d5c2a4baf7c7e50da2bac4728b3bea8c3e880f9edca9622f97
    publication_correction:
      by: agent:source-repair
      date: '2026-11-26T02:05:16.806224+00:00'
      pdf_pages:
      - 4
      - 5
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
