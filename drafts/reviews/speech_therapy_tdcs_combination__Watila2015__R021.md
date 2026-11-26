---
id: speech_therapy_tdcs_combination__Watila2015__R021
name: combination of speech therapy and tDCS
kind: review
findings:
- id: f1
  target: aphasia_recovery
  target_kind: prognosis
  claim: Watila2015 reports, based on the review discussion and its cited primary studies, that jung et al. [46] reported better outcomes with combined speech therapy and tDCS among those starting treatment earlier
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
  therapy:
    id: speech_therapy_tdcs_combination
    name: combination of speech therapy and tDCS
  citation: '@Watila2015'
  source_passages:
  - section: Original source AGENT-P4-R021
    page: 4
    quote: 'Jung et al. [46] reported that a combination of speech therapy and

      tDCS had better outcome in those who commenced treatment earlier.'
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
  proposal_id: R021
  approved: false
  original_core_review: {}
  original_publication_entry: null
  original_mapping:
    decision: hold
    reason: The selected analysis (R021) claims a relationship between 'combination of speech therapy and tDCS' and 'outcome', but the provided source text only contains the table of contents and abstract of a narrative review. The specific finding regarding tDCS and speech therapy is not present in the provided source window; only the general heading 'Treatment related factors' (P1-S2-C13) is visible. The core claim and its direction are unresolved.
    bucket: therapies
    entity_id: speech_therapy_tdcs_combination
    name: combination of speech therapy and tDCS
    kind: therapy
    predictor_type: clinical
    definition: combination of speech therapy and tDCS
    assessment: []
    target: aphasia_recovery
    target_kind: prognosis
    claim: unresolved
    direction: mixed
    method: narrative_review
    relationship: synthesis
    therapy:
      id: speech_therapy_tdcs_combination
      name: combination of speech therapy and tDCS
    sample_n: null
    population: stroke patients with aphasia
    timing: unresolved
    qualifications: []
    limitations: []
    optional_pending: []
    evidence_quality: narrative-review
    passages:
    - source_id: P1-S2-C13
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
    proposal: R021
    status: hold
    reason: The selected analysis (R021) claims a relationship between 'combination of speech therapy and tDCS' and 'outcome', but the provided source text only contains the table of contents and abstract of a narrative review. The specific finding regarding tDCS and speech therapy is not present in the provided source window; only the general heading 'Treatment related factors' (P1-S2-C13) is visible. The core claim and its direction are unresolved.
    seconds_this_run: 15.578473458008375
  source_check:
    profile: agent-repair
    scope: Agent source reconstruction; original model reviews do not certify the changed record. No independent model pass or human approval.
    approved: false
    paper_complete: false
    binding:
      pdf_sha256: ce9a58083bece023d95b73013b208f3f56f85f2cce3da3f00c7bbe18c1a678a2
      original_mapping_sha256: 6a90cf6dc5768d6d997b1ede0e90b241e203b0dc7bbe822997668c9943ae9ddb
      original_status_sha256: b66b4c1d40ff8bdb641b0dc5d1e5ab3f0e14a3e5720c29ec5028575259f084f9
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
