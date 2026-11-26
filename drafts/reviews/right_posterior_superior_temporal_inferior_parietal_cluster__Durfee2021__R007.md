---
id: right_posterior_superior_temporal_inferior_parietal_cluster__Durfee2021__R007
name: posterior superior temporal and inferior parietal lobe cluster
kind: review
findings:
- id: f1
  target: sensory_aprosodia
  target_kind: impairment
  claim: Durfee2021 reports, based on Ross (1981), that sensory aprosodia was observed in a patient with posterior superior temporal and inferior parietal lobe infarction, encompassing the right homologue of Wernicke’s area.
  direction: likely
  relationship: synthesis
  method: narrative_review
  sample:
    n: not_reported
    population: 'Studies of post-stroke populations summarized by Durfee2021; secondary evidence, not a newly recruited cohort. Attribution: Ross (1981)'
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
  - finding based on a single patient case observation
  evidence_quality: narrative-review
  strength: weak
  notes: 'Reconstructed as a secondary review summary attributed to Ross (1981). This is not a new patient cohort or independent replication. Primary-study verification and human approval remain pending. Source repair (unapproved): Reconstructed as a secondary review summary attributed to Ross (1981). This is not a new patient cohort or independent replication. Primary-study verification and human approval remain pending.'
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
    - agent_source_repair_pending_human_review
  citation: '@Durfee2021'
  source_passages:
  - section: Original source P5-S2-C13
    page: 5
    quote: "Specifically, sensory \naprosodia was observed in a patient with posterior superior temporal \nand inferior parietal lobe infarction, encompassing the right homologue \nof Wernicke’s area."
    supports: claim
  - section: Original source P5-S2-C12
    page: 5
    quote: "Subacute and chronic lesions \nRoss (1981) observed that patients with sensory aprosodia (impaired \naffective prosody recognition and imitation but spared production in \nspontaneous speech) or transcortical sensory aprosodia (impaired af­\nfective prosody recognition but spared repetition and spontaneous \nproduction) had temporal and/or parietal lesions."
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
  proposal_id: R007
  approved: false
  original_core_review: {}
  original_publication_entry: null
  original_mapping:
    decision: draft
    reason: The source describes a specific case observation from Ross (1981) where a patient with a defined infarct location (posterior superior temporal and inferior parietal lobe) exhibited sensory aprosodia.
    bucket: regions
    entity_id: right_posterior_superior_temporal_inferior_parietal_cluster
    name: posterior superior temporal and inferior parietal lobe cluster
    kind: network
    predictor_type: imaging_metric
    definition: Patient lesion overlap with the posterior superior temporal and inferior parietal lobe, encompassing the right homologue of Wernicke’s area.
    assessment: []
    target: sensory_aprosodia
    target_kind: impairment
    claim: Sensory aprosodia was observed in a patient with posterior superior temporal and inferior parietal lobe infarction, encompassing the right homologue of Wernicke’s area.
    direction: likely
    method: VLSM
    relationship: correlational
    therapy: null
    sample_n: 1
    population: patients with RH stroke
    timing: subacute or chronic
    qualifications:
    - sensory aprosodia is defined as impaired affective prosody recognition and imitation but spared production in spontaneous speech
    limitations:
    - finding based on a single patient case observation
    optional_pending: []
    evidence_quality: case-study
    passages:
    - source_id: P5-S2-C13
      supports: claim
    - source_id: P5-S2-C12
      supports: claim
    - source_id: P4-S2-C5
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
    proposal: R007
    status: failed
    reason: Claim, population and method source evidence required
    seconds_this_run: 28.447498583002016
  source_check:
    profile: agent-repair
    scope: Agent source reconstruction; original model reviews do not certify the changed record. No independent model pass or human approval.
    approved: false
    paper_complete: false
    binding:
      pdf_sha256: ccd84f115f464675d9dc92bc5df1deabc67b02a9eb42f72849745a981dc374d8
      original_mapping_sha256: 1f9398b6779ce00a3363f35b8136561c922fdd1ab3bc6c96520afa9475415236
      original_status_sha256: f17f0c33540fa0cd655bdc785c77b3e0ae18aa292d330a541e3d4c9dc6afab03
      evidence_sha256: 1a2ffa6ce12653b1a48461fd815432d7cacdf039f7d80229543a34243f44b298
    publication_correction:
      by: agent:source-repair
      date: '2026-11-26T02:05:16.806224+00:00'
      pdf_pages:
      - 1
      - 5
      note: Reconstructed as a secondary review summary attributed to Ross (1981). This is not a new patient cohort or independent replication. Primary-study verification and human approval remain pending.
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
  note: Reconstructed as a secondary review summary attributed to Ross (1981). This is not a new patient cohort or independent replication. Primary-study verification and human approval remain pending.
---

# Source review required

This repaired draft remains unapproved. Original outputs and review provenance are preserved.
