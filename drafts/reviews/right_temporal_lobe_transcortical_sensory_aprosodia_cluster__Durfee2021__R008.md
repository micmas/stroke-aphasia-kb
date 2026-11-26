---
id: right_temporal_lobe_transcortical_sensory_aprosodia_cluster__Durfee2021__R008
name: right temporal lobe cluster (transcortical sensory aprosodia)
kind: review
findings:
- id: f1
  target: transcortical_sensory_aprosodia
  target_kind: impairment
  claim: Durfee2021 reports, based on Ross (1981), that damage to the right middle and inferior temporal regions anteriorly and the middle temporal lobe posteriorly was associated with transcortical sensory aprosodia (impaired affective prosody recognition but spared repetition and spontaneous production).
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
  - The systematic review notes that fewer than half of the included studies employed MRI to evaluate lesion loci
  - The review lacked access to raw lesion data for some articles, preventing formal lesion-symptom mapping
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
    - not_transcribed:sample.n
    - agent_source_repair_pending_human_review
  citation: '@Durfee2021'
  source_passages:
  - section: Original source P8-S4-C6
    page: 8
    quote: "Fewer \nthan half of the studies employed MRI to evaluate lesion loci, making \nformal analyses of lesion-symptom mapping unrealistic with this data­\nset."
    supports: limitation
  - section: Original source P8-S4-C7
    page: 8
    quote: "Additionally, we did not have access to the raw (lesion) data in all \nthe articles, and without access to this lesion data specifically, recreation \nof lesion overlay or subtraction maps to compare cross-study lesion- \nsymptom correlates of affective aprosodia was not feasible."
    supports: limitation
  - section: Original source P5-S2-C12
    page: 5
    quote: "Subacute and chronic lesions \nRoss (1981) observed that patients with sensory aprosodia (impaired \naffective prosody recognition and imitation but spared production in \nspontaneous speech) or transcortical sensory aprosodia (impaired af­\nfective prosody recognition but spared repetition and spontaneous \nproduction) had temporal and/or parietal lesions."
    supports: claim
  - section: Original source P5-S2-C14
    page: 5
    quote: "Temporal damage associated with transcortical \nsensory aprosodia included middle and inferior regions anteriorly and \nnarrowing to the middle temporal lobe posteriorly."
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
  proposal_id: R008
  approved: false
  original_core_review: {}
  original_publication_entry: null
  original_mapping:
    decision: draft
    reason: The source provides a specific anatomical association between right temporal lobe lesions and transcortical sensory aprosodia based on the work of Ross (1981), as synthesized in this systematic review.
    bucket: regions
    entity_id: right_temporal_lobe_transcortical_sensory_aprosodia_cluster
    name: right temporal lobe cluster (transcortical sensory aprosodia)
    kind: network
    predictor_type: imaging_metric
    definition: Patient lesion overlap with middle and inferior temporal regions anteriorly and the middle temporal lobe posteriorly.
    assessment: []
    target: transcortical_sensory_aprosodia
    target_kind: impairment
    claim: Damage to the right middle and inferior temporal regions anteriorly and the middle temporal lobe posteriorly was associated with transcortical sensory aprosodia (impaired affective prosody recognition but spared repetition and spontaneous production).
    direction: likely
    method: VLSM
    relationship: correlational
    therapy: null
    sample_n: null
    population: patients with right hemisphere stroke
    timing: subacute or chronic
    qualifications:
    - Finding is based on a synthesis of a study by Ross (1981)
    limitations:
    - The systematic review notes that fewer than half of the included studies employed MRI to evaluate lesion loci
    - The review lacked access to raw lesion data for some articles, preventing formal lesion-symptom mapping
    optional_pending: []
    evidence_quality: narrative-review
    passages:
    - source_id: P5-S2-C12
      supports: claim
    - source_id: P5-S2-C14
      supports: claim
    - source_id: P4-S2-C5
      supports: method
    - source_id: P8-S4-C6
      supports: limitation
    - source_id: P8-S4-C7
      supports: limitation
    - source_id: P1-S1-C7
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
    proposal: R008
    status: failed
    reason: Claim, population and method source evidence required
    seconds_this_run: 31.709131041003275
  source_check:
    profile: agent-repair
    scope: Agent source reconstruction; original model reviews do not certify the changed record. No independent model pass or human approval.
    approved: false
    paper_complete: false
    binding:
      pdf_sha256: ccd84f115f464675d9dc92bc5df1deabc67b02a9eb42f72849745a981dc374d8
      original_mapping_sha256: 0d859b7340719dceefa7a96b383d46a86adbfb1fdec398171f9968af2cec6667
      original_status_sha256: bac2c4d34b81791a33e10d1f29aad95993e2f26939ecd2ad04a02dde175b6456
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
