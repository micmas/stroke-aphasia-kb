---
id: mood_priming_paragraph__Durfee2021__R036
name: congruent mood-priming paragraph
kind: review
findings:
- id: f1
  target: emotional_prosody_recognition
  target_kind: impairment
  claim: Durfee2021 reports, based on Tompkins and Flowers (1987), that adults with RH stroke improved in emotional prosody recognition following a congruent mood-priming paragraph similarly to adults with LH stroke and adults without brain damage
  direction: likely
  relationship: synthesis
  method: narrative_review
  sample:
    n: not_reported
    population: 'Studies of post-stroke populations summarized by Durfee2021; secondary evidence, not a newly recruited cohort. Attribution: Tompkins and Flowers (1987)'
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
  notes: 'Reconstructed as a secondary review summary attributed to Tompkins and Flowers (1987). This is not a new patient cohort or independent replication. Primary-study verification and human approval remain pending. Source repair (unapproved): Reconstructed as a secondary review summary attributed to Tompkins and Flowers (1987). This is not a new patient cohort or independent replication. Primary-study verification and human approval remain pending.'
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
    id: mood_priming
    name: mood-priming
  citation: '@Durfee2021'
  source_passages:
  - section: Original source P10-S4-C12
    page: 10
    quote: "Tompkins and \nFlowers (1987) found that adults with RH stroke improved in emotional \nprosody recognition following a congruent mood-priming paragraph \nsimilarly to adults with LH stroke and adults without brain damage."
    supports: claim
  - section: Original source P1-S1-C7
    page: 1
    quote: "The current systematic review aimed to evaluate the evidence on \naffective prosody localization in the RH."
    supports: method
  - section: Original source P1-S1-C9
    page: 1
    quote: "Eleven articles met inclusion criteria, passed quality reviews, and were analyzed for affective \nprosody localization."
    supports: sample
  design: systematic-review
schema_version: '2.9'
status: draft
created_by: agent:source-repair
created_on: '2026-11-26'
relationship_review:
  paper: Durfee2021
  proposal_id: R036
  approved: false
  original_core_review: {}
  original_publication_entry: null
  original_mapping:
    decision: draft
    reason: The source provides a specific finding from Tompkins and Flowers (1987) regarding the effect of mood-priming on emotional prosody recognition in patients with RH stroke.
    bucket: therapies
    entity_id: mood_priming_paragraph
    name: congruent mood-priming paragraph
    kind: therapy
    predictor_type: clinical
    definition: exposure to a congruent mood-priming paragraph prior to assessment
    assessment:
    - emotional prosody recognition
    target: emotional_prosody_recognition
    target_kind: impairment
    claim: adults with RH stroke improved in emotional prosody recognition following a congruent mood-priming paragraph similarly to adults with LH stroke and adults without brain damage
    direction: likely
    method: behavioral_only
    relationship: treatment_response
    therapy:
      id: mood_priming
      name: mood-priming
    sample_n: null
    population: adults with RH stroke
    timing: not_transcribed
    qualifications:
    - improvement was similar to that observed in adults with LH stroke and adults without brain damage
    limitations: []
    optional_pending: []
    evidence_quality: cohort
    passages:
    - source_id: P10-S4-C12
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
      pdf_sha256: ccd84f115f464675d9dc92bc5df1deabc67b02a9eb42f72849745a981dc374d8
      review_sha256: 3c3e749bbeb85252e97e4dec8e8dbb5075c4d0e2ddb45ff086cbc832ee2697ee
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
    proposal: R036
    status: failed
    reason: Claim, population and method source evidence required
    seconds_this_run: 38.28942520900455
  source_check:
    profile: agent-repair
    scope: Agent source reconstruction; original model reviews do not certify the changed record. No independent model pass or human approval.
    approved: false
    paper_complete: false
    binding:
      pdf_sha256: ccd84f115f464675d9dc92bc5df1deabc67b02a9eb42f72849745a981dc374d8
      original_mapping_sha256: 991fbd967b2d280397a7eb8cf9d137eb6625b74b1b033b7de01c65e67671fe85
      original_status_sha256: 9730abbd445aa88801d4ae7d479a8b2b4dac3b5300c4e0bc8456a7ef12cdc314
      evidence_sha256: 1a2ffa6ce12653b1a48461fd815432d7cacdf039f7d80229543a34243f44b298
    publication_correction:
      by: agent:source-repair
      date: '2026-11-26T02:05:16.806224+00:00'
      pdf_pages:
      - 1
      - 10
      note: Reconstructed as a secondary review summary attributed to Tompkins and Flowers (1987). This is not a new patient cohort or independent replication. Primary-study verification and human approval remain pending.
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
  note: Reconstructed as a secondary review summary attributed to Tompkins and Flowers (1987). This is not a new patient cohort or independent replication. Primary-study verification and human approval remain pending.
---

# Source review required

This repaired draft remains unapproved. Original outputs and review provenance are preserved.
