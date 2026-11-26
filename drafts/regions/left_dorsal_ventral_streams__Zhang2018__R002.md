---
id: left_dorsal_ventral_streams
name: left dorsal and ventral streams cluster
kind: network
findings:
- id: f1
  target: post_stroke_aphasia
  target_kind: impairment
  claim: Compared with healthy controls, the group classified as having post-stroke aphasia showed compromised left dorsal and ventral white matter integrity on AFQ. The pattern included reduced FA and AD and increased RD, with metric effects varying by tract; it does not mean every metric changed in every tract.
  direction: likely
  relationship: correlational
  method: DTI
  sample:
    n: 22
    population: 11 analyzed patients classified as having post-stroke aphasia and 11 healthy controls; 3 recruited patients were excluded.
    phase: not_reported
    time_post_onset: MRI scans completed after 14 +/- 2 days post-stroke; language assessment performed 10 +/- 2 days after onset
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Preliminary study
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Patient diffusion tensor metrics measured by AFQ for group contrasts or TBSS for language associations, as specified in the claim. Patient-control differences must not be interpreted as correlations with aphasia severity. Additional metadata has not been transcribed; review the pending-field flags before approval. Source repair (unapproved): Repaired evidence binding and selected-analysis identity against Results pp.4–7. Restricted the denominator to analyzed participants and distinguished group contrasts from language associations.'
  imaging_details:
    reference_space: not_reported
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
  citation: '@Zhang2018'
  source_passages:
  - section: Original source P1-S2-C4
    page: 1
    quote: "Voxel-based lesion-symptom mapping found multiple linguistic \nassociations for the ventral stream, while automated fiber quantification (AFQ) showed, \nvia reduced fractional anisotropy (FA) and axial diffusivity with increased radial diffusivity \n(all corrected p < 0.05), that the integrity of both the left dorsal and ventral streams \nwas compromised."
    supports: claim
  - section: Original source P3-S3-C11
    page: 3
    quote: "Automated Fiber Quantification\nWe performed AFQ (version 1.2; Stanford University, California, \nUSA;2) to enable further quantitative analysis along the major \ntracts."
    supports: method
  - section: Original source P4-S1-C7
    page: 4
    quote: "Finally, 100 equidistant nodes were resampled along the central \nportion of the tract in each fiber group, and the mean location \nof each node in the fiber group core was calculated."
    supports: method
  - section: Original source P4-S2-C7
    page: 4
    quote: "Language function was \nassessed 10 ± 2 days after onset, and MRI scans were completed \nafter 14 ± 2 days."
    supports: sample
  - section: Original source P4-S2-C8
    page: 4
    quote: "Two patients were removed because of obvious \nhead motion, and one sample with damaged data storage was \nexcluded."
    supports: sample
  design: cross-sectional
schema_version: '2.8'
status: draft
created_by: agent:source-repair
created_on: '2026-11-26'
relationship_review:
  paper: Zhang2018
  proposal_id: R002
  approved: false
  original_core_review: {}
  original_publication_entry: null
  original_mapping:
    decision: draft
    reason: The study uses AFQ to compare diffusion metrics of the left dorsal and ventral streams between subacute aphasic patients and healthy controls, finding compromised integrity in both.
    bucket: regions
    entity_id: left_dorsal_ventral_streams
    name: left dorsal and ventral streams cluster
    kind: network
    predictor_type: imaging_metric
    definition: Patient white matter integrity measured via automated fiber quantification (AFQ) of the left dorsal and ventral streams, specifically using fractional anisotropy, axial diffusivity, and radial diffusivity.
    assessment: []
    target: post_stroke_aphasia
    target_kind: impairment
    claim: The integrity of both the left dorsal and ventral streams was compromised in subacute aphasic patients compared to healthy controls, characterized by reduced fractional anisotropy and axial diffusivity with increased radial diffusivity.
    direction: likely
    method: DTI
    relationship: correlational
    therapy: null
    sample_n: 25
    population: subacute post-stroke aphasic patients and healthy controls
    timing: MRI scans completed after 14 +/- 2 days post-stroke; language assessment performed 10 +/- 2 days after onset
    qualifications:
    - Comparison performed between 14 aphasic patients and 11 healthy controls
    - Results corrected for multiple comparisons (p < 0.05)
    limitations:
    - Preliminary study
    optional_pending: []
    evidence_quality: cohort
    passages:
    - source_id: P1-S2-C4
      supports: claim
    - source_id: P1-S2-C3
      supports: sample
    - source_id: P4-S2-C7
      supports: method
    - source_id: P3-S3-C11
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
      pdf_sha256: 1f55089b0daa53f85f07313b5f3862c188f569e267bb388418d56b3bf4748e56
      review_sha256: 905ac8d1292336fa44ac6fa433bde54c7249a3a1ffbf24814f53692ea7de7fd5
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
    proposal: R002
    status: failed
    reason: 'Zhang2018: finding[0] (id=f1): target ''post_stroke_aphasia'' is an aphasia syndrome but the claim is about a symptom; target the symptom entry (anomia, fluency, …) unless the paper classifies by syndrome'
    material_issues: []
    seconds_this_run: 89.2391282080207
  source_check:
    profile: agent-repair
    scope: Agent source reconstruction; original model reviews do not certify the changed record. No independent model pass or human approval.
    approved: false
    paper_complete: false
    binding:
      pdf_sha256: 1f55089b0daa53f85f07313b5f3862c188f569e267bb388418d56b3bf4748e56
      original_mapping_sha256: adefb2f4374a0133afec10f1c878d2df22704f6f8203916272665157cb46d385
      original_status_sha256: ea09b7a5ff57776d5024649c72f2045036927454a1a046855bb46deefecd0197
      evidence_sha256: 92d3763f80a751a9af742b6f8c638079625c24b6eeac041030cfd095d71d8913
    publication_correction:
      by: agent:source-repair
      date: '2026-11-26T02:05:16.806224+00:00'
      pdf_pages:
      - 1
      - 2
      - 3
      - 4
      - 5
      - 6
      - 7
      - 8
      - 9
      note: Repaired evidence binding and selected-analysis identity against Results pp.4–7. Restricted the denominator to analyzed participants and distinguished group contrasts from language associations.
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
  note: Repaired evidence binding and selected-analysis identity against Results pp.4–7. Restricted the denominator to analyzed participants and distinguished group contrasts from language associations.
---

# Source review required

This repaired draft remains unapproved. Original outputs and review provenance are preserved.
