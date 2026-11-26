---
id: fornix_infarct__Biesbroek2017__R006
name: fornix cluster
kind: review
findings:
- id: f1
  target: acute_memory_loss
  target_kind: impairment
  claim: Biesbroek2017 reports, based on the case and lesion studies cited in the linked passages, that a single case study reported acute memory loss in a patient with a small infarct in the corpus callosum with involvement of the fornix.
  direction: likely
  relationship: synthesis
  method: narrative_review
  sample:
    n: not_reported
    population: Previously reported stroke/aphasia studies and methodological literature summarized by Biesbroek2017; no newly recruited cohort.
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
  - single case study
  - prone to publication bias
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
    - agent_source_repair_pending_human_review
  citation: '@Biesbroek2017'
  source_passages:
  - section: Original source P3-S2-C12
    page: 3
    quote: 'First, single case studies and small case series cannot

      prove that infarcts at strategic locations always result in cognitive impairment and are prone to publication bias.'
    supports: limitation
  - section: Original source P3-S2-C2
    page: 3
    quote: 'The fornix

      A single case study reported acute memory loss in a patient with a small infarct in the corpus callosum with involve-

      ment of the fornix [21].'
    supports: claim
  - section: Original source P1-S1-C6
    page: 1
    quote: 'This narrative review addresses the role of anatomical lesion location in the im-

      pact of SVD on cognition, integrating findings from early autopsy studies with emerging

      findings from recent studies with advanced image analysis techniques.'
    supports: method
  - section: Original source P1-S1-C6
    page: 1
    quote: 'This narrative review addresses the role of anatomical lesion location in the im-

      pact of SVD on cognition, integrating findings from early autopsy studies with emerging

      findings from recent studies with advanced image analysis techniques.'
    supports: sample
  design: narrative-review
schema_version: '2.9'
status: draft
created_by: agent:source-repair
created_on: '2026-11-26'
relationship_review:
  paper: Biesbroek2017
  proposal_id: R006
  approved: false
  original_core_review: {}
  original_publication_entry: null
  original_mapping:
    decision: draft
    reason: The source describes a specific case study where a small infarct in the corpus callosum involving the fornix was associated with acute memory loss.
    bucket: regions
    entity_id: fornix_infarct
    name: fornix cluster
    kind: network
    predictor_type: imaging_metric
    definition: presence of a small infarct in the corpus callosum with involvement of the fornix
    assessment: []
    target: acute_memory_loss
    target_kind: impairment
    claim: A single case study reported acute memory loss in a patient with a small infarct in the corpus callosum with involvement of the fornix.
    direction: likely
    method: behavioral_only
    relationship: correlational
    therapy: null
    sample_n: 1
    population: patient with a small infarct in the corpus callosum
    timing: acute
    qualifications: []
    limitations:
    - single case study
    - prone to publication bias
    optional_pending: []
    evidence_quality: case-study
    passages:
    - source_id: P3-S2-C2
      supports: claim
    - source_id: P3-S2-C12
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
      pdf_sha256: 3ea3ce26a31cec57a11d684730925dbff173d0b8a14a5666a8a89e0b8bc35f30
      review_sha256: 911e35bf4806eea150d96d358eb72d4544f378a25f66178a000e02e581e2aaad
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
    proposal: R006
    status: failed
    reason: Claim, population and method source evidence required
    seconds_this_run: 0.003656875000160653
  source_check:
    profile: agent-repair
    scope: Agent source reconstruction; original model reviews do not certify the changed record. No independent model pass or human approval.
    approved: false
    paper_complete: false
    binding:
      pdf_sha256: 3ea3ce26a31cec57a11d684730925dbff173d0b8a14a5666a8a89e0b8bc35f30
      original_mapping_sha256: 7c2bcb5d2aab4386e3676fde653203d0118b9c2f22c85a299431fef42e35203c
      original_status_sha256: 47bca6a22e7112831fb4ece295f9f7dd45544af01460366ebebeb10dd8de213b
      evidence_sha256: eea6ec506fc94fa20c4923e666e9fe0f84383e09140b41753024728b469e6a3f
    publication_correction:
      by: agent:source-repair
      date: '2026-11-26T02:05:16.806224+00:00'
      pdf_pages:
      - 1
      - 3
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
