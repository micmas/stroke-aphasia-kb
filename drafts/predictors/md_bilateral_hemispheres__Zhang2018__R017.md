---
id: md_bilateral_hemispheres
name: mean diffusivity (both hemispheres)
kind: predictor
findings:
- id: f1
  target: post_stroke_aphasia
  target_kind: impairment
  claim: In the comparison of participants classified as having post-stroke aphasia with healthy controls, mean diffusivity did not differ significantly in either hemisphere (all corrected p>.05). The authors used this observation in discussing possible edema; it does not prove that edema was absent.
  direction: no_effect
  relationship: correlational
  method: DTI
  sample:
    n: 22
    population: 11 analyzed patients classified as having post-stroke aphasia and 11 healthy controls; 3 recruited patients were excluded.
    phase: not_reported
    time_post_onset: MRI scans completed after 14 ± 2 days post-stroke
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - small sample size
  evidence_quality: cohort
  strength: weak
  notes: 'Corrected the sample from recruited to analysed participants (11 patients and 11 controls). Preserved the between-group MD null result without claiming that it excludes edema. Unapproved. Source repair (unapproved): Corrected the sample from recruited to analysed participants (11 patients and 11 controls). Preserved the between-group MD null result without claiming that it excludes edema. Unapproved.'
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
  - section: Original source P5-S3-C6
    page: 5
    quote: "The brain edema was not influential \nin the subacute post-stroke group since MD did not change \nsignificantly in both hemispheres (all corrected p > 0.05)."
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
predictor_type: imaging_metric
short_definition: Patient diffusion tensor metrics measured by AFQ for group contrasts or TBSS for language associations, as specified in the claim.
assessment:
- Automated Fiber Quantification (AFQ)
schema_version: '2.8'
status: draft
created_by: agent:source-repair
created_on: '2026-11-26'
relationship_review:
  paper: Zhang2018
  proposal_id: R017
  approved: false
  original_core_review: {}
  original_publication_entry: null
  original_mapping:
    decision: draft
    reason: The study tested the association between mean diffusivity (MD) and post-stroke aphasia using AFQ point-wise comparisons and found no significant difference between patients and controls, which the authors interpret as an absence of influential brain edema in the subacute group.
    bucket: predictors
    entity_id: md_bilateral_hemispheres
    name: mean diffusivity (both hemispheres)
    kind: predictor
    predictor_type: imaging_metric
    definition: mean diffusivity (MD) measured via automated fiber quantification (AFQ) resampled at 100 equidistant nodes along bilateral major fascicles
    assessment:
    - Automated Fiber Quantification (AFQ)
    target: post_stroke_aphasia
    target_kind: impairment
    claim: mean diffusivity (MD) did not change significantly in both hemispheres between aphasic patients and healthy controls
    direction: no_effect
    method: DTI
    relationship: correlational
    therapy: null
    sample_n: 25
    population: subacute post-stroke patients with language dysfunction and matched healthy controls
    timing: MRI scans completed after 14 ± 2 days post-stroke
    qualifications:
    - comparison between aphasic patients and healthy controls
    limitations:
    - small sample size
    optional_pending: []
    evidence_quality: cohort
    passages:
    - source_id: P5-S3-C6
      supports: claim
    - source_id: P2-S3-C7
      supports: method
    - source_id: P1-S2-C3
      supports: sample
    - source_id: P4-S2-C7
      supports: sample
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
    proposal: R017
    status: failed
    reason: 'Zhang2018: finding[0] (id=f1): target ''post_stroke_aphasia'' is an aphasia syndrome but the claim is about a symptom; target the symptom entry (anomia, fluency, …) unless the paper classifies by syndrome'
    material_issues: []
    seconds_this_run: 87.49838137498591
  source_check:
    profile: agent-repair
    scope: Agent source reconstruction; original model reviews do not certify the changed record. No independent model pass or human approval.
    approved: false
    paper_complete: false
    binding:
      pdf_sha256: 1f55089b0daa53f85f07313b5f3862c188f569e267bb388418d56b3bf4748e56
      original_mapping_sha256: ec5fa48f61f2f60426ee477db6385618ab2de515cf29e563e55e36ec72c8df5c
      original_status_sha256: cbae091b416e7c233eb50e4cff06518a53827439f929d938808a218c8614f816
      evidence_sha256: 92d3763f80a751a9af742b6f8c638079625c24b6eeac041030cfd095d71d8913
    publication_correction:
      by: agent:source-repair
      date: '2026-11-26T02:05:16.806224+00:00'
      pdf_pages:
      - 2
      - 3
      - 5
      note: Corrected the sample from recruited to analysed participants (11 patients and 11 controls). Preserved the between-group MD null result without claiming that it excludes edema. Unapproved.
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
  note: Corrected the sample from recruited to analysed participants (11 patients and 11 controls). Preserved the between-group MD null result without claiming that it excludes edema. Unapproved.
---

# Source review required

This repaired draft remains unapproved. Original outputs and review provenance are preserved.
