---
id: left_ilf
name: left ILF cluster
kind: network
findings:
- id: f1
  target: post_stroke_aphasia
  target_kind: impairment
  claim: Compared with healthy controls, patients classified as having post-stroke aphasia had altered mean FA and RD of the left ILF, without significant AD or MD differences.
  direction: likely
  relationship: correlational
  method: DTI
  sample:
    n: 22
    population: 11 analyzed patients classified as having post-stroke aphasia and 11 healthy controls; 3 recruited patients were excluded.
    phase: not_reported
    time_post_onset: Language function assessed 10 ± 2 days after onset; MRI scans completed after 14 ± 2 days
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
  - section: Original source P6-S1-C5
    page: 6
    quote: "All the correlations were controlled by additional covariates including \nage, sex, and lesion size."
    supports: confounders
  - section: Original source P5-S2-C11
    page: 5
    quote: "For the left ILF, FA, and RD \nchanged significantly with no obvious alterations in AD or MD; \nin the left AF and UF, only reductions in FA were recorded among \nthe four diffusion metrics (all corrected p < 0.05)."
    supports: claim
  - section: Original source P7-S1-C2
    page: 7
    quote: 'Tracts

      FA, mean (SD)

      AD, mean (SD)

      RD, mean (SD)

      Patient

      Control

      Patient

      Control

      Patient

      Control

      SLF

      0.29 (0.05)a

      0.37 (0.04)

      1.05 (0.15)

      1.09 (0.08)

      0.68 (0.11)

      0.60 (0.04)

      AF

      0.33 (0.06)a

      0.47 (0.03)

      1.08 (0.16)

      1.21 (0.05)

      0.64 (0.10)

      0.56 (0.04)

      IFOF

      0.32 (0.07)a

      0.48 (0.03)

      1.19 (0.13)a

      1.35 (0.04)

      0.72 (0.08)a

      0.60 (0.05)

      UF

      0.34 (0.07)a

      0.43 (0.03)

      1.16 (0.13)

      1.27 (0.06)

      0.67 (0.03)

      0.62 (0.04)

      ILF

      0.36 (0.03)a

      0.42 (0.02)

      1.27 (0.07)

      1.29 (0.05)

      0.71 (0.05)a

      0.65 (0.03)

      Values are expressed as mean (SD); AD and RD are measured in square millimeter per second × 10−3.

      aSignificantly impaired relative to healthy controls at P < 0.05 after Bonferroni correction.'
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
  proposal_id: R011
  approved: false
  original_core_review: {}
  original_publication_entry: null
  original_mapping:
    decision: draft
    reason: The study provides a clear association between the microstructural integrity of the left inferior longitudinal fasciculus (ILF) and specific language impairments (comprehension and repetition) in subacute stroke patients, measured via AFQ point-wise correlations.
    bucket: regions
    entity_id: left_ilf
    name: left ILF cluster
    kind: network
    predictor_type: imaging_metric
    definition: mean diffusion metrics (FA, RD) of the left inferior longitudinal fasciculus extracted via automated fiber quantification (AFQ) by resampling 100 equidistant nodes along the tract
    assessment:
    - Aphasia Battery of Chinese
    target: post_stroke_aphasia
    target_kind: impairment
    claim: The temporal segment of the left ILF showed significant positive correlations with comprehension and repetition scores.
    direction: likely
    method: DTI
    relationship: correlational
    therapy: null
    sample_n: 14
    population: right-handed native Chinese-speaking subacute post-stroke patients with left hemisphere infarction and aphasia
    timing: Language function assessed 10 ± 2 days after onset; MRI scans completed after 14 ± 2 days
    qualifications:
    - correlations were controlled for age, sex, and lesion size
    - significant correlations were specifically located in the temporal segment of the tract
    limitations:
    - small sample size
    optional_pending: []
    evidence_quality: cohort
    passages:
    - source_id: P7-S1-C4
      supports: claim
    - source_id: P2-S3-C12
      supports: sample
    - source_id: P4-S2-C7
      supports: sample
    - source_id: P6-S1-C5
      supports: confounders
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
    proposal: R011
    status: failed
    reason: No primary evidence for the selected analysis
    seconds_this_run: 46.97053654096089
  source_check:
    profile: agent-repair
    scope: Agent source reconstruction; original model reviews do not certify the changed record. No independent model pass or human approval.
    approved: false
    paper_complete: false
    binding:
      pdf_sha256: 1f55089b0daa53f85f07313b5f3862c188f569e267bb388418d56b3bf4748e56
      original_mapping_sha256: 7472dc3d352ce98f5273bff59471b96487e963010b3e7e519f56bd72eea55d98
      original_status_sha256: c2fc3408d2e5998a859881b61c8b4599225d0d84c16cc2d8b3b270b86b8bbd60
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
