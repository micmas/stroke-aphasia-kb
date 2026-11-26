---
id: treatment_received__Watila2015__R018
name: treatment received
kind: review
findings:
- id: f1
  target: aphasia_recovery
  target_kind: prognosis
  claim: Watila2015 reports, based on the review discussion and its cited primary studies, that treatment type, duration, intensity and earlier initiation may influence recovery, with spontaneous recovery and conflicting or weak findings limiting conclusions
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
  - section: Original source AGENT-P4-R018
    page: 4
    quote: 'The inﬂuence of language therapy is difﬁcult to assess because

      spontaneous recovery occurs in many patients [16]; patients with

      mild aphasia are usually excluded from studies to avoid the ‘ceiling

      effect’ [68]; and those under treatment are more likely to have severe

      speech deﬁcits [9].

      There is growing evidence that treatment of aphasia may positively

      inﬂuence recovery [27,64,67,86]. Studies on repetitive transcranial mag-

      netic stimulation (rTMS) and transcranial direct current stimulation

      (tDCS) have afﬁrmed their beneﬁcial effects on post-stroke aphasia re-

      covery by inducing neuroplasticity of targeted brain areas [2,42,47,63,

      69,95]. Therapeutic techniques like melodic intonation therapy (MIT),

      constraint induced therapy (CID), action observation treatment (AOT),

      and semantic feature analysis (SFA) tend to also facilitate neuroplasticity

      [14,54,63,66,82]. Pharmacological trials of donepezil and galantamine

      have shown some beneﬁcial effects compared with placebos, as these

      drugs promote reorganisation and increase in acetylcholine concentra-

      tion [8,43]. Piracetam, dextroamphetamine, dopamine and antidepres-

      sant trials have yielded mixed results [35,65].

      Jung et al. [46] reported that a combination of speech therapy and

      tDCS had better outcome in those who commenced treatment earlier.

      A meta-analysis by Robey [84] reported that intensive therapy was

      more effective when started early. The SP-I-R-IT study [66] suggests

      better recovery for those on intensive compared to regular therapy.

      Weak evidence on the inﬂuence of treatment on aphasia recovery was

      reported in a study by David et al. [17] and a systematic review by

      Cherney et al. [12].

      In summary, the type, duration, intensity and earlier commence-

      ment of aphasia therapy may be considered a determinant factor for

      better recovery [17]. The ‘Rotterdam Aphasia Therapy Study-3’ when

      concluded may give a better insight into the role of early-intensive

      cognitive therapy compared to regular language therapy [75] [for

      summary see Table 3].'
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
  proposal_id: R018
  approved: false
  original_core_review: {}
  original_publication_entry: null
  original_mapping:
    decision: draft
    reason: The source is a narrative review that identifies 'treatment received' as one of the important factors determining post-stroke aphasia recovery.
    bucket: predictors
    entity_id: treatment_received
    name: treatment received
    kind: predictor
    predictor_type: clinical
    definition: The specific treatment received by the patient following a stroke resulting in aphasia.
    assessment: []
    target: aphasia_recovery
    target_kind: prognosis
    claim: Treatment received is one of the most important factors that determine post-stroke aphasia recovery.
    direction: likely
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
    - source_id: P1-S1-C4
      supports: claim
    - source_id: P1-S2-C13
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
    proposal: R018
    status: failed
    reason: Claim, population and method source evidence required
    seconds_this_run: 13.771595707978122
  source_check:
    profile: agent-repair
    scope: Agent source reconstruction; original model reviews do not certify the changed record. No independent model pass or human approval.
    approved: false
    paper_complete: false
    binding:
      pdf_sha256: ce9a58083bece023d95b73013b208f3f56f85f2cce3da3f00c7bbe18c1a678a2
      original_mapping_sha256: c8fd313356b32ba515ae8216c08342643a3368d8984257c0c3f2e046562aede6
      original_status_sha256: f0eb48b4f0eea0d1d534aca952ba2ce192745e6f09da936128c2c3d4e3b3d8b2
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
