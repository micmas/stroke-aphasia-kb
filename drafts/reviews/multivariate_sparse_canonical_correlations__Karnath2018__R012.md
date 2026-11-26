---
id: multivariate_sparse_canonical_correlations__Karnath2018__R012
name: multivariate sparse canonical correlations
kind: review
findings:
- id: f1
  target: cognitive_module_identification
  target_kind: impairment
  claim: Karnath2018 reports, based on the cited lesion-mapping studies, that lesion-behavior mapping with multivariate sparse canonical correlations performs better than mass-univariate non-parametric mapping in most, but not all, situations, demonstrating less spatial bias and a better ability to identify cognitive modules consisting of multiple brain regions.
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
  - multivariate results still suffer from a reduced but present spatial bias
  - multivariate approaches tend to be somewhat decoupled from spatial information
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
  - section: Original source P8-S1-C3
    page: 8
    quote: 'However, multivariate results were far from being perfect; they suffered

      from a reduced, but still present spatial bias.'
    supports: limitation
  - section: Original source P8-S1-C4
    page: 8
    quote: 'Beyond, multivariate approaches tend to be somewhat de-coupled

      from the spatial information.'
    supports: limitation
  - section: Original source P8-S1-C2
    page: 8
    quote: 'Pustina et al. (in press) found that

      lesion-behavior mapping with multivariate sparse canonical correlations

      indeed performs better than mass-univariate non-parametric mapping in

      most (but not all) situations, including less spatial bias and better ability

      to identify cognitive modules consisting of multiple brain regions.'
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
  proposal_id: R012
  approved: false
  original_core_review: {}
  original_publication_entry: null
  original_mapping:
    decision: draft
    reason: The source provides a specific comparison between multivariate sparse canonical correlations and mass-univariate non-parametric mapping regarding their performance in identifying cognitive modules and managing spatial bias in stroke patients.
    bucket: predictors
    entity_id: multivariate_sparse_canonical_correlations
    name: multivariate sparse canonical correlations
    kind: predictor
    predictor_type: imaging_metric
    definition: A multivariate analysis method applied to structural lesion imaging data to model behavioral variables based on multiple voxels or regions of interest.
    assessment: []
    target: cognitive_module_identification
    target_kind: impairment
    claim: Lesion-behavior mapping with multivariate sparse canonical correlations performs better than mass-univariate non-parametric mapping in most situations, demonstrating less spatial bias and a better ability to identify cognitive modules consisting of multiple brain regions.
    direction: likely
    method: MVPA
    relationship: correlational
    therapy: null
    sample_n: null
    population: patients with stroke
    timing: not_transcribed
    qualifications:
    - performance advantage observed in most but not all situations
    limitations:
    - multivariate results still suffer from a reduced but present spatial bias
    - multivariate approaches tend to be somewhat decoupled from spatial information
    optional_pending: []
    evidence_quality: cohort
    passages:
    - source_id: P8-S1-C2
      supports: claim
    - source_id: P8-S1-C3
      supports: limitation
    - source_id: P8-S1-C4
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
    proposal: R012
    status: failed
    reason: Claim, population and method source evidence required
    seconds_this_run: 46.741833166990546
  source_check:
    profile: agent-repair
    scope: Agent source reconstruction; original model reviews do not certify the changed record. No independent model pass or human approval.
    approved: false
    paper_complete: false
    binding:
      pdf_sha256: dbbf5db9f646e5ed67190025aea75aff5c20f899e9304ffa7b67f2d7641a12b8
      original_mapping_sha256: 5df8b90da8d3f53b7e274733efe7d24ac518d65fa46af3cee0350d562d219065
      original_status_sha256: b970e78d14dcf5429c873444160085859893bb0cfd9687101686f5d769111672
      evidence_sha256: 1fe03a7858e2c0619360925a382c4a7c8eb22dd92699fd695c60acd3a8aa9df7
    publication_correction:
      by: agent:source-repair
      date: '2026-11-26T02:05:16.806224+00:00'
      pdf_pages:
      - 1
      - 8
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
