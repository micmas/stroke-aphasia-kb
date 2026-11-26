---
id: time_post_stroke_prosody_recovery__Durfee2021__R033
name: time post-stroke (acute vs 6 months)
kind: review
findings:
- id: f1
  target: impaired_prosody
  target_kind: impairment
  claim: Durfee2021 reports, based on Sheppard et al. (2020), that 40% of patients with impaired prosody acutely were no longer impaired chronically.
  direction: likely
  relationship: synthesis
  method: narrative_review
  sample:
    n: not_reported
    population: 'Studies of post-stroke populations summarized by Durfee2021; secondary evidence, not a newly recruited cohort. Attribution: Sheppard et al. (2020)'
    phase: not_reported
    time_post_onset: Varies across reviewed studies; see cited primary report.
  statistics:
    threshold: not_applicable_review_synthesis
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - lesions did not change between assessments
  evidence_quality: narrative-review
  strength: weak
  notes: 'Reconstructed as a secondary review summary attributed to Sheppard et al. (2020). This is not a new patient cohort or independent replication. Primary-study verification and human approval remain pending. Source repair (unapproved): Reconstructed as a secondary review summary attributed to Sheppard et al. (2020). This is not a new patient cohort or independent replication. Primary-study verification and human approval remain pending.'
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
  citation: '@Durfee2021'
  source_passages:
  - section: Original source P10-S1-C12
    page: 10
    quote: "As their \nlesions did not change, lesion-deficit correlations would be different at \nthe acute versus chronic stage in these participants. \n4.4."
    supports: limitation
  - section: Original source P10-S1-C11
    page: 10
    quote: "They found that 40% of patients with \nimpaired prosody acutely were no longer impaired chronically."
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
  proposal_id: R033
  approved: false
  original_core_review: {}
  original_publication_entry: null
  original_mapping:
    decision: draft
    reason: The source provides a specific longitudinal finding from Sheppard et al. (2020) regarding the recovery of prosody impairment from acute to chronic stages.
    bucket: predictors
    entity_id: time_post_stroke_prosody_recovery
    name: time post-stroke (acute vs 6 months)
    kind: predictor
    predictor_type: demographic
    definition: Comparison of prosody impairment status between an acute assessment (within 5 days of stroke) and a chronic follow-up assessment (at least 6 months post-stroke).
    assessment: []
    target: impaired_prosody
    target_kind: impairment
    claim: 40% of patients with impaired prosody acutely were no longer impaired chronically.
    direction: likely
    method: behavioral_only
    relationship: correlational
    therapy: null
    sample_n: null
    population: patients with stroke
    timing: acute (within 5 days) and chronic (at least 6 months post-stroke)
    qualifications:
    - finding reported for a subset of patients who underwent follow-up testing
    limitations:
    - lesions did not change between assessments
    optional_pending: []
    evidence_quality: cohort
    passages:
    - source_id: P10-S1-C10
      supports: method
    - source_id: P10-S1-C11
      supports: claim
    - source_id: P10-S1-C12
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
    proposal: R033
    status: failed
    reason: Claim, population and method source evidence required
    seconds_this_run: 36.058916791997035
  source_check:
    profile: agent-repair
    scope: Agent source reconstruction; original model reviews do not certify the changed record. No independent model pass or human approval.
    approved: false
    paper_complete: false
    binding:
      pdf_sha256: ccd84f115f464675d9dc92bc5df1deabc67b02a9eb42f72849745a981dc374d8
      original_mapping_sha256: ea135dc614dccd898ce1ebfd0d27e232fd5041b096416477e38afbd565d9ea3d
      original_status_sha256: a9609d337f355b8ccaf654df5f04137fe39c27a3ec12181e31416713dc2bbc71
      evidence_sha256: 1a2ffa6ce12653b1a48461fd815432d7cacdf039f7d80229543a34243f44b298
    publication_correction:
      by: agent:source-repair
      date: '2026-11-26T02:05:16.806224+00:00'
      pdf_pages:
      - 1
      - 10
      note: Reconstructed as a secondary review summary attributed to Sheppard et al. (2020). This is not a new patient cohort or independent replication. Primary-study verification and human approval remain pending.
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
  note: Reconstructed as a secondary review summary attributed to Sheppard et al. (2020). This is not a new patient cohort or independent replication. Primary-study verification and human approval remain pending.
---

# Source review required

This repaired draft remains unapproved. Original outputs and review provenance are preserved.
