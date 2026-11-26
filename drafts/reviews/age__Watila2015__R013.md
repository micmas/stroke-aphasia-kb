---
id: age__Watila2015__R013
name: age
kind: review
findings:
- id: f1
  target: aphasia_recovery
  target_kind: prognosis
  claim: Watila2015 reports, based on the review discussion and its cited primary studies, that the influence of age on aphasia recovery remains unclear despite a tendency for poorer recovery in older patients
  direction: mixed
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
  - section: Original source AGENT-P3-R013
    page: 3
    quote: 'Generally patients with aphasia are more likely to be older and re-

      port a higher prevalence of ﬂuent aphasia [24,77,78]; while De Renzi

      et al. [21] reported Broca''s aphasia to be commoner in younger patients.

      Kang et al. [48] found no difference between age and aphasia type or

      severity.

      A study by Pickersgill & Lincoln [79] found that younger patients

      with aphasia improved better than older patients. Lendrem & Lincoln

      [61] found an inﬂuence of younger age on recovery in those treated

      for aphasia. Laska et al. [56] reported that older age is a negative predic-

      tor for improvement. The studies by Kertesz & Mccabe [51] and Peder-

      sen et al. [77] reported a non-signiﬁcant age difference. Other studies

      found no inﬂuence of age on aphasia recovery [41,44,58,61,78,92]. The

      inﬂuence of age on aphasia recovery still remains unclear, with a

      tendency for older patients to have a poorer recovery.'
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
  proposal_id: R013
  approved: false
  original_core_review: {}
  original_publication_entry: null
  original_mapping:
    decision: draft
    reason: The source is a narrative review that explicitly states age is not a robust predictor of post-stroke aphasia recovery.
    bucket: predictors
    entity_id: age
    name: age
    kind: predictor
    predictor_type: demographic
    definition: Patient age at the time of stroke
    assessment: []
    target: aphasia_recovery
    target_kind: prognosis
    claim: Age has not been found to be a robust predictor of post-stroke aphasia recovery.
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
    - source_id: P1-S2-C8
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
    proposal: R013
    status: failed
    reason: Claim, population and method source evidence required
    seconds_this_run: 11.904430958995363
  source_check:
    profile: agent-repair
    scope: Agent source reconstruction; original model reviews do not certify the changed record. No independent model pass or human approval.
    approved: false
    paper_complete: false
    binding:
      pdf_sha256: ce9a58083bece023d95b73013b208f3f56f85f2cce3da3f00c7bbe18c1a678a2
      original_mapping_sha256: f7bc8b1696f81fcd640eadd1a02dd81672df3329082adfd664b943f95b671fdd
      original_status_sha256: e132593a90ef3b5b0617859005ec2a5d21fb5a4d0b719c9d9856198ecdf2800f
      evidence_sha256: bda694bdef276118893bc0f58663d74b0e48dbd57f9507fdfd49a08c1e336ad7
    publication_correction:
      by: agent:source-repair
      date: '2026-11-26T02:05:16.806224+00:00'
      pdf_pages:
      - 1
      - 3
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
