---
id: handedness__Watila2015__R014
name: Handedness
kind: review
findings:
- id: f1
  target: aphasia_recovery
  target_kind: prognosis
  claim: Watila2015 reports, based on the review discussion and its cited primary studies, that reviewed studies did not demonstrate an influence of handedness on aphasia recovery
  direction: no_effect
  relationship: synthesis
  method: narrative_review
  sample:
    n: not_reported
    population: 'Studies of post-stroke populations summarized by Watila2015; secondary evidence, not a newly recruited cohort. Attribution: the review discussion and its cited primary studies'
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
  notes: 'Reconstructed as a secondary review summary attributed to the review discussion and its cited primary studies. This is not a new patient cohort or independent replication. Primary-study verification and human approval remain pending. Checked the full source PDF beyond the truncated original evidence index. Source repair (unapproved): Reconstructed as a secondary review summary attributed to the review discussion and its cited primary studies. This is not a new patient cohort or independent replication. Primary-study verification and human approval remain pending. Checked the full source PDF beyond the truncated original evidence index.'
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
  citation: '@Watila2015'
  source_passages:
  - section: Original source AGENT-P4-R014
    page: 4
    quote: 'Studies have not shown any inﬂuence between handedness and

      aphasia recovery despite the potential greater neural capacity for recov-

      ery in left-handers and the ambidextrous, since they are more likely to

      have language representation in both hemispheres and a higher likeli-

      hood for right hemisphere dominance [25,77,79].'
    supports: claim
  - section: Original source P1-S1-C3
    page: 1
    quote: 'Method: Papers were identiﬁed through PubMed and MEDLINE search, with keywords such as: ‘stroke’, ‘aphasia’,

      ‘post-stroke aphasia’, ‘factors that predict aphasia recovery’, ‘aphasia outcomes’ and ‘aphasia prognosis’.'
    supports: method
  - section: Original source P1-S1-C3
    page: 1
    quote: 'Method: Papers were identiﬁed through PubMed and MEDLINE search, with keywords such as: ‘stroke’, ‘aphasia’,

      ‘post-stroke aphasia’, ‘factors that predict aphasia recovery’, ‘aphasia outcomes’ and ‘aphasia prognosis’.'
    supports: sample
  design: narrative-review
schema_version: '2.9'
status: draft
created_by: agent:source-repair
created_on: '2026-11-26'
relationship_review:
  paper: Watila2015
  proposal_id: R014
  approved: false
  original_core_review: {}
  original_publication_entry: null
  original_mapping:
    decision: draft
    reason: The source is a narrative review that explicitly states handedness has not been found to be a robust predictor of post-stroke aphasia recovery.
    bucket: predictors
    entity_id: handedness
    name: Handedness
    kind: predictor
    predictor_type: demographic
    definition: Patient handedness as an anagraphic factor.
    assessment: []
    target: aphasia_recovery
    target_kind: prognosis
    claim: Handedness has not been found to be a robust predictor of post-stroke aphasia recovery.
    direction: no_effect
    method: narrative_review
    relationship: synthesis
    therapy: null
    sample_n: null
    population: stroke patients with aphasia
    timing: post-stroke
    qualifications: []
    limitations: []
    optional_pending: []
    evidence_quality: narrative-review
    passages:
    - source_id: P1-S1-C5
      supports: claim
    - source_id: P1-S2-C9
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
      pdf_sha256: ce9a58083bece023d95b73013b208f3f56f85f2cce3da3f00c7bbe18c1a678a2
      review_sha256: 8c720747e71514e16a1bb1844e5c4895976d95710dc687e7d68986c4d4327569
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
    proposal: R014
    status: failed
    reason: Claim, population and method source evidence required
    seconds_this_run: 12.83859791699797
  source_check:
    profile: agent-repair
    scope: Agent source reconstruction; original model reviews do not certify the changed record. No independent model pass or human approval.
    approved: false
    paper_complete: false
    binding:
      pdf_sha256: ce9a58083bece023d95b73013b208f3f56f85f2cce3da3f00c7bbe18c1a678a2
      original_mapping_sha256: cc44847fcd75c0669fb8a938b6eb1832e02d8901ada821ced1dccfcaa2e9879d
      original_status_sha256: 70427f675c22b8ccc85823feb6759ae55649a7c6efd410cb09dc02b45c454085
      evidence_sha256: bda694bdef276118893bc0f58663d74b0e48dbd57f9507fdfd49a08c1e336ad7
    publication_correction:
      by: agent:source-repair
      date: '2026-11-26T02:05:16.806224+00:00'
      pdf_pages:
      - 1
      - 4
      note: Reconstructed as a secondary review summary attributed to the review discussion and its cited primary studies. This is not a new patient cohort or independent replication. Primary-study verification and human approval remain pending. Checked the full source PDF beyond the truncated original evidence index.
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
  note: Reconstructed as a secondary review summary attributed to the review discussion and its cited primary studies. This is not a new patient cohort or independent replication. Primary-study verification and human approval remain pending. Checked the full source PDF beyond the truncated original evidence index.
---

# Source review required

This repaired draft remains unapproved. Original outputs and review provenance are preserved.
