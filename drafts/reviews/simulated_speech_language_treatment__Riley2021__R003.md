---
id: simulated_speech_language_treatment__Riley2021__R003
name: simulated speech and language treatment session
kind: review
findings:
- id: f1
  target: feelings_of_fatigue
  target_kind: impairment
  claim: Riley2021 reports, based on Riley, Owora, McCleary and Anderson (2019), that participants with aphasia experienced a significant increase in feelings of fatigue after completing a 72-minute simulated speech and language treatment session, although the reported amount of fatigue did not significantly differ from age-matched control participants
  direction: likely
  relationship: synthesis
  method: narrative_review
  sample:
    n: not_reported
    population: 'Studies of post-stroke populations summarized by Riley2021; secondary evidence, not a newly recruited cohort. Attribution: Riley, Owora, McCleary and Anderson (2019)'
    phase: not_reported
    time_post_onset: Varies across reviewed studies; see cited primary report.
  statistics:
    threshold: not_applicable_review_synthesis
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations: []
  evidence_quality: narrative-review
  strength: weak
  notes: 'Reconstructed as a secondary review summary attributed to Riley, Owora, McCleary and Anderson (2019). This is not a new patient cohort or independent replication. Primary-study verification and human approval remain pending. Source repair (unapproved): Reconstructed as a secondary review summary attributed to Riley, Owora, McCleary and Anderson (2019). This is not a new patient cohort or independent replication. Primary-study verification and human approval remain pending.'
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
    - not_transcribed:author_limitations
    - agent_source_repair_pending_human_review
  therapy:
    id: simulated_speech_language_treatment
    name: simulated speech and language treatment session
  citation: '@Riley2021'
  source_passages:
  - section: Original source P8-S1-C5
    page: 8
    quote: "Results of this study showed that participants with aphasia experienced a significant increase in \nfeelings of fatigue after completing a 72-minute simulated speech and language treatment session, but that the reported amount of \nfatigue did not significantly differ from age-matched control participants (Riley, Owora, McCleary, & Anderson, 2019). \n3.3."
    supports: claim
  - section: Original source P1-S1-C8
    page: 1
    quote: "Methods:  A systematic scoping review was conducted to identify studies measuring post-stroke \nfatigue."
    supports: method
  - section: Original source P7-S1-C8
    page: 7
    quote: "From this process, another 241 articles were excluded, leaving 161 articles that were included in our final \nanalysis (see Fig. 1)."
    supports: sample
  design: systematic-review
schema_version: '2.9'
status: draft
created_by: agent:source-repair
created_on: '2026-11-26'
relationship_review:
  paper: Riley2021
  proposal_id: R003
  approved: false
  original_core_review: {}
  original_publication_entry: null
  original_mapping:
    decision: draft
    reason: The source describes a specific study (Riley et al., 2019) within the scoping review that tested the effect of a simulated treatment session on fatigue in participants with aphasia.
    bucket: therapies
    entity_id: simulated_speech_language_treatment
    name: simulated speech and language treatment session
    kind: therapy
    predictor_type: clinical
    definition: completion of a 72-minute simulated speech and language treatment session
    assessment: []
    target: feelings_of_fatigue
    target_kind: impairment
    claim: participants with aphasia experienced a significant increase in feelings of fatigue after completing a 72-minute simulated speech and language treatment session, although the reported amount of fatigue did not significantly differ from age-matched control participants
    direction: likely
    method: behavioral_only
    relationship: treatment_response
    therapy:
      id: simulated_speech_language_treatment
      name: simulated speech and language treatment session
    sample_n: null
    population: participants with aphasia and age-matched control participants
    timing: post-treatment
    qualifications:
    - reported amount of fatigue did not significantly differ from age-matched control participants
    limitations: []
    optional_pending:
    - sample_n
    evidence_quality: cohort
    passages:
    - source_id: P8-S1-C5
      supports: claim
    - source_id: P8-S1-C4
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
      pdf_sha256: c692b1c38bf63a3cd745f21f7a29fb3c962cfbd79ced781ca245540010642491
      review_sha256: b6915557c03aaaa7c62433c45c72c8d407da475efc7bcc9e455f294dea6c7e94
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
    proposal: R003
    status: failed
    reason: Claim, population and method source evidence required
    seconds_this_run: 31.448170499992557
  source_check:
    profile: agent-repair
    scope: Agent source reconstruction; original model reviews do not certify the changed record. No independent model pass or human approval.
    approved: false
    paper_complete: false
    binding:
      pdf_sha256: c692b1c38bf63a3cd745f21f7a29fb3c962cfbd79ced781ca245540010642491
      original_mapping_sha256: 7e042900ed6674a6e6715512db354bb0f0cf1bb66e25dfb5ed1574d9eaf3e15f
      original_status_sha256: 6a51e705c5f709912b9932c95f95183c51d23a9e6c5f94499224265b87ad3a5f
      evidence_sha256: ddfbd7e05d83116652fedd512c73f34b0aa2a412390656c2cb684b9a3390c885
    publication_correction:
      by: agent:source-repair
      date: '2026-11-26T02:05:16.806224+00:00'
      pdf_pages:
      - 1
      - 7
      - 8
      note: Reconstructed as a secondary review summary attributed to Riley, Owora, McCleary and Anderson (2019). This is not a new patient cohort or independent replication. Primary-study verification and human approval remain pending.
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
  note: Reconstructed as a secondary review summary attributed to Riley, Owora, McCleary and Anderson (2019). This is not a new patient cohort or independent replication. Primary-study verification and human approval remain pending.
---

# Source review required

This repaired draft remains unapproved. Original outputs and review provenance are preserved.
