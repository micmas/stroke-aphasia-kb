---
id: subcallosal_periventricular_cluster__Plowman2012__R016
name: subcallosal and periventricular white matter cluster
kind: review
findings:
- id: f1
  target: spontaneous_speech_fluency
  target_kind: impairment
  claim: Plowman2012 reports, based on Naeser et al., reference 48, that spontaneous speech fluency was significantly influenced by lesion size in two subcortical white matter areas when combined
  direction: likely
  relationship: synthesis
  method: narrative_review
  sample:
    n: not_reported
    population: 'Studies of post-stroke populations summarized by Plowman2012; secondary evidence, not a newly recruited cohort. Attribution: Naeser et al., reference 48'
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
  - finding is reported via a narrative review of a prior study
  evidence_quality: narrative-review
  strength: weak
  notes: 'Reconstructed as a secondary review summary attributed to Naeser et al., reference 48. This is not a new patient cohort or independent replication. Primary-study verification and human approval remain pending. Source repair (unapproved): Reconstructed as a secondary review summary attributed to Naeser et al., reference 48. This is not a new patient cohort or independent replication. Primary-study verification and human approval remain pending.'
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
  - section: Original source P4-S1-C8
    page: 4
    quote: 'A later study by this group did not iden-

      tify a single neuroanatomical area where extent of lesion could

      discriminate outcomes for spontaneous speech ﬂuency; however,

      Naeser et al. concluded that spontaneous speech ﬂuency was sig-

      niﬁcantly inﬂuenced by lesion size in two subcortical white matter

      areas when combined [48].'
    supports: confounders
  - section: Original source P4-S1-C8
    page: 4
    quote: 'A later study by this group did not iden-

      tify a single neuroanatomical area where extent of lesion could

      discriminate outcomes for spontaneous speech ﬂuency; however,

      Naeser et al. concluded that spontaneous speech ﬂuency was sig-

      niﬁcantly inﬂuenced by lesion size in two subcortical white matter

      areas when combined [48].'
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
  proposal_id: R016
  approved: false
  original_core_review: {}
  original_publication_entry: null
  original_mapping:
    decision: draft
    reason: The source describes a specific finding from Naeser et al. regarding the combined effect of lesion size in two subcortical white matter areas on spontaneous speech fluency.
    bucket: regions
    entity_id: subcallosal_periventricular_cluster
    name: subcallosal and periventricular white matter cluster
    kind: network
    predictor_type: imaging_metric
    definition: combined lesion size in the most medial and rostral portion of the subcallosal fasciculus and the periventricular white matter area near the body of the lateral ventricle and deep to the lower motor/sensory cortex area of the mouth
    assessment: []
    target: spontaneous_speech_fluency
    target_kind: impairment
    claim: spontaneous speech fluency was significantly influenced by lesion size in two subcortical white matter areas when combined
    direction: likely
    method: LSM
    relationship: correlational
    therapy: null
    sample_n: null
    population: patients with aphasia
    timing: not_transcribed
    qualifications:
    - the effect was found when the two areas were combined
    - a single neuroanatomical area was not found to discriminate outcomes for spontaneous speech fluency
    limitations:
    - finding is reported via a narrative review of a prior study
    optional_pending: []
    evidence_quality: cohort
    passages:
    - source_id: P4-S1-C8
      supports: claim
    - source_id: P4-S1-C9
      supports: method
    - source_id: P4-S1-C8
      supports: confounders
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
    proposal: R016
    status: failed
    reason: Claim, population and method source evidence required
    seconds_this_run: 21.44656808298896
  source_check:
    profile: agent-repair
    scope: Agent source reconstruction; original model reviews do not certify the changed record. No independent model pass or human approval.
    approved: false
    paper_complete: false
    binding:
      pdf_sha256: ef0aaf55a3919bf3928bc764f9271e407b8176b38f51ed6574cbb892431360d2
      original_mapping_sha256: 4c34c3b01f3186f73751706cff2fc3998a454a0a180e760f8ce9396bb06e3907
      original_status_sha256: 6ec485fa6b97c364607d8a273204318c262230d976efe923eebc64c75b398e98
      evidence_sha256: 57d9ad6e551715316e46a646fde9c49e245751b03f1a7b407778a308d8cafc6a
    publication_correction:
      by: agent:source-repair
      date: '2026-11-26T02:05:16.806224+00:00'
      pdf_pages:
      - 1
      - 4
      note: Reconstructed as a secondary review summary attributed to Naeser et al., reference 48. This is not a new patient cohort or independent replication. Primary-study verification and human approval remain pending.
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
  note: Reconstructed as a secondary review summary attributed to Naeser et al., reference 48. This is not a new patient cohort or independent replication. Primary-study verification and human approval remain pending.
---

# Source review required

This repaired draft remains unapproved. Original outputs and review provenance are preserved.
