---
id: education_ses__Plowman2012__R007
name: educational achievement and socio-economic status
kind: review
findings:
- id: f1
  target: aphasia_recovery_rate
  target_kind: prognosis
  claim: Plowman2012 reports, based on the literature review synthesis, that data to date suggest no consistent relationship between education level and aphasia recovery rate.
  direction: no_effect
  relationship: synthesis
  method: narrative_review
  sample:
    n: not_reported
    population: 'Studies of post-stroke populations summarized by Plowman2012; secondary evidence, not a newly recruited cohort. Attribution: the literature review synthesis'
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
  - The existence of confounds such as literacy levels, general intelligence, learning disabilities, and cultural influences makes this area challenging to study
  evidence_quality: narrative-review
  strength: weak
  notes: 'Reconstructed as a secondary review summary attributed to the literature review synthesis. This is not a new patient cohort or independent replication. Primary-study verification and human approval remain pending. Source repair (unapproved): Reconstructed as a secondary review summary attributed to the literature review synthesis. This is not a new patient cohort or independent replication. Primary-study verification and human approval remain pending.'
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
  citation: '@Plowman2012'
  source_passages:
  - section: Original source P3-S1-C6
    page: 3
    quote: 'This is likely due to the existence of a

      plethora of confounds, such as literacy levels, general intelligence,

      existence of learning disabilities, socio-economic status (SES) and

      cultural inﬂuences, that make this area particularly challenging to

      study.'
    supports: limitation
  - section: Original source P3-S2-C5
    page: 3
    quote: 'While data regarding the inﬂuence of educational

      levels on aphasia outcomes remain limited, data to date suggest

      no consistent relationship between education level and aphasia

      severity or recovery.'
    supports: claim
  - section: Original source P3-S2-C3
    page: 3
    quote: 'These authors noted that

      both educational achievement and SES did not impact aphasia

      recovery rate; however, initial aphasia severity was worse in those

      with less education then in those with a higher level of education.'
    supports: claim
  - section: Original source P1-S1-C5
    page: 1
    quote: 'Methods We completed a literature review to assess and identify evidence-based patient

      and stroke-related variables shown to be inﬂuential in aphasia recovery.'
    supports: method
  - section: Original source P1-S1-C4
    page: 1
    quote: 'Therefore, the objective of this review was to assess the inﬂuence

      of patient-related and stroke-related factors on language recovery in individuals with

      post-stroke aphasia.'
    supports: sample
  design: narrative-review
schema_version: '2.9'
status: draft
created_by: agent:source-repair
created_on: '2026-11-26'
relationship_review:
  paper: Plowman2012
  proposal_id: R007
  approved: false
  original_core_review: {}
  original_publication_entry: null
  original_mapping:
    decision: draft
    reason: The review synthesizes findings from multiple studies (e.g., Connor et al., Lazar et al.) regarding the impact of education and SES on aphasia recovery, concluding there is no consistent relationship.
    bucket: predictors
    entity_id: education_ses
    name: educational achievement and socio-economic status
    kind: predictor
    predictor_type: demographic
    definition: Patient educational achievement and socio-economic status (SES), where SES is described as a complex interaction of income, insurance status, access to health care, and health-related beliefs.
    assessment: []
    target: aphasia_recovery_rate
    target_kind: prognosis
    claim: Data to date suggest no consistent relationship between education level and aphasia recovery rate.
    direction: no_effect
    method: narrative_review
    relationship: synthesis
    therapy: null
    sample_n: null
    population: individuals with post-stroke aphasia
    timing: post-stroke
    qualifications:
    - One cited study of 39 individuals found that while education and SES did not impact recovery rate, initial aphasia severity was worse in those with less education
    - Another cited study reported no relationship between education level, initial aphasia severity, or recovery
    limitations:
    - The existence of confounds such as literacy levels, general intelligence, learning disabilities, and cultural influences makes this area challenging to study
    optional_pending: []
    evidence_quality: narrative-review
    passages:
    - source_id: P3-S2-C5
      supports: claim
    - source_id: P3-S2-C3
      supports: claim
    - source_id: P3-S1-C6
      supports: limitation
    - source_id: P1-S1-C5
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
      pdf_sha256: ef0aaf55a3919bf3928bc764f9271e407b8176b38f51ed6574cbb892431360d2
      review_sha256: c89504ffcf33add92b2797f423ef92b6b5661c51290ed24470391997daef7a1d
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
    reason: Claim, population and method source evidence required
    seconds_this_run: 21.811864916002378
  source_check:
    profile: agent-repair
    scope: Agent source reconstruction; original model reviews do not certify the changed record. No independent model pass or human approval.
    approved: false
    paper_complete: false
    binding:
      pdf_sha256: ef0aaf55a3919bf3928bc764f9271e407b8176b38f51ed6574cbb892431360d2
      original_mapping_sha256: c7d28e020f4595e92a69a39abfd1ae9201f106dcea285be1c3814db5ded6fc4f
      original_status_sha256: 876610e9ae99404411cb2bfa00431513573c594078b762a5d44d600c612c7079
      evidence_sha256: 57d9ad6e551715316e46a646fde9c49e245751b03f1a7b407778a308d8cafc6a
    publication_correction:
      by: agent:source-repair
      date: '2026-11-26T02:05:16.806224+00:00'
      pdf_pages:
      - 1
      - 3
      note: Reconstructed as a secondary review summary attributed to the literature review synthesis. This is not a new patient cohort or independent replication. Primary-study verification and human approval remain pending.
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
  note: Reconstructed as a secondary review summary attributed to the literature review synthesis. This is not a new patient cohort or independent replication. Primary-study verification and human approval remain pending.
---

# Source review required

This repaired draft remains unapproved. Original outputs and review provenance are preserved.
