---
id: permutation_thresholding__Karnath2018__R001
name: Permutation thresholding
kind: review
findings:
- id: f1
  target: familywise_error_rate
  target_kind: impairment
  claim: Karnath2018 reports, based on the cited lesion-mapping studies, that voxelwise permutation thresholding controls familywise error and is less conservative than Bonferroni correction in VLBM, according to the cited methodological work; this is an analysis-method conclusion, not a patient outcome
  direction: likely
  relationship: synthesis
  method: narrative_review
  sample:
    n: not_reported
    population: Previously reported stroke/aphasia studies and methodological literature summarized by Karnath2018; no newly recruited cohort.
    phase: not_reported
    time_post_onset: See cited primary reports; varies across review.
  statistics:
    threshold: not_applicable_review_synthesis
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - computationally slow, particularly as the number of permutations increases
  - inherently conservative
  - most useful with larger studies and studies with good statistical power
  evidence_quality: narrative-review
  strength: weak
  notes: 'Corrected primary-study misclassification to an explicitly attributed review summary. No new independent cohort or pooled effect is asserted. Source passages preserve cited study references; human primary-source review remains pending. Source repair (unapproved): Corrected primary-study misclassification to an explicitly attributed review summary. No new independent cohort or pooled effect is asserted. Source passages preserve cited study references; human primary-source review remains pending.'
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
  citation: '@Karnath2018'
  source_passages:
  - section: Original source P2-S4-C8
    page: 2
    quote: 'The primary

      weakness of permutation thresholding is that it is slow, particularly as the

      number of permutations increases.'
    supports: limitation
  - section: Original source P2-S4-C10
    page: 2
    quote: 'While voxelwise permutation thresholding does robustly control

      familywise error rate, it is inherently conservative, and therefore most

      useful with larger studies and studies with good statistical power.'
    supports: limitation
  - section: Original source P2-S4-C6
    page: 2
    quote: 'Fortunately, we can directly control for the familywise error rate using

      voxelwise permutation thresholding (Nichols and Hayasaka, 2003).'
    supports: claim
  - section: Original source P2-S4-C7
    page: 2
    quote: 'Permutation thresholding precisely controls familywise error rate, and

      (as expected) demonstrates that Bonferroni correction is overly conser-

      vative in the context of VLBM (Rorden et al., 2007).'
    supports: claim
  - section: Original source P1-S1-C5
    page: 1
    quote: 'This review il-

      lustrates how VLBM improves our knowledge of functional brain architecture, as well as how it is inherently

      limited by its mass-univariate approach.'
    supports: method
  - section: Original source P1-S1-C5
    page: 1
    quote: 'This review il-

      lustrates how VLBM improves our knowledge of functional brain architecture, as well as how it is inherently

      limited by its mass-univariate approach.'
    supports: sample
  design: narrative-review
schema_version: '2.9'
status: draft
created_by: agent:source-repair
created_on: '2026-11-26'
relationship_review:
  paper: Karnath2018
  proposal_id: R001
  approved: false
  original_core_review: {}
  original_publication_entry: null
  original_mapping:
    decision: draft
    reason: The source provides a clear comparison between two statistical thresholding methods used in voxel-based lesion-behavior mapping (VLBM), specifically stating that permutation thresholding precisely controls the familywise error rate and demonstrates that Bonferroni correction is overly conservative in this context.
    bucket: ingredients
    entity_id: permutation_thresholding
    name: Permutation thresholding
    kind: ingredient
    predictor_type: imaging_metric
    definition: A method of controlling the familywise error rate in voxel-based lesion-behavior mapping (VLBM) by using voxelwise permutation tests to determine statistical thresholds.
    assessment: []
    target: familywise_error_rate
    target_kind: impairment
    claim: Permutation thresholding precisely controls the familywise error rate and is less conservative than Bonferroni correction in the context of voxel-based lesion-behavior mapping.
    direction: likely
    method: VLSM
    relationship: correlational
    therapy: null
    sample_n: null
    population: patients with stroke
    timing: not_transcribed
    qualifications:
    - compared to Bonferroni correction
    - specifically in the context of VLBM
    limitations:
    - computationally slow, particularly as the number of permutations increases
    - inherently conservative
    - most useful with larger studies and studies with good statistical power
    optional_pending: []
    evidence_quality: narrative-review
    passages:
    - source_id: P2-S4-C6
      supports: claim
    - source_id: P2-S4-C7
      supports: claim
    - source_id: P2-S4-C8
      supports: limitation
    - source_id: P2-S4-C10
      supports: limitation
  original_attempt:
    binding:
      profile: core
      version: core-source-check-v3
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      checker_model: qwen3.8:27b
      checker_digest: 47951e4a666180bc2aedfc93c169472f2de783696fe196efbf063f5730ecf163
      host: http://localhost:11434
      pdf_sha256: dbbf5db9f646e5ed67190025aea75aff5c20f899e9304ffa7b67f2d7641a12b8
      review_sha256: 1fbc9305ad0a2f592e05e317766596032c7b6e691efb6c3ba2125c242408e7f0
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
    proposal: R001
    status: failed
    reason: Claim, population and method source evidence required
    seconds_this_run: 49.244069750013296
  source_check:
    profile: agent-repair
    scope: Agent source reconstruction; original model reviews do not certify the changed record. No independent model pass or human approval.
    approved: false
    paper_complete: false
    binding:
      pdf_sha256: dbbf5db9f646e5ed67190025aea75aff5c20f899e9304ffa7b67f2d7641a12b8
      original_mapping_sha256: 145465bd04ef42928afb1496fbb18bed47b88c660c323786f17d284652b3a2af
      original_status_sha256: 2abce25fa1ebf78645b9f5dd970e4e6e6f7924e1da1949b1911a83126d34be67
      evidence_sha256: 1fe03a7858e2c0619360925a382c4a7c8eb22dd92699fd695c60acd3a8aa9df7
    publication_correction:
      by: agent:source-repair
      date: '2026-11-26T02:05:16.806224+00:00'
      pdf_pages:
      - 1
      - 2
      note: Corrected primary-study misclassification to an explicitly attributed review summary. No new independent cohort or pooled effect is asserted. Source passages preserve cited study references; human primary-source review remains pending.
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
  note: Corrected primary-study misclassification to an explicitly attributed review summary. No new independent cohort or pooled effect is asserted. Source passages preserve cited study references; human primary-source review remains pending.
---

# Source review required

This repaired draft remains unapproved. Original outputs and review provenance are preserved.
