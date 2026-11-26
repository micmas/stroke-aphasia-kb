---
id: right_hemisphere_naming_cluster
name: right hemisphere naming cluster
kind: network
findings:
- id: f1
  target: cortical_thickness
  target_kind: impairment
  claim: No significant relationships were found between cortical thickness in the right hemisphere cluster for naming/word finding and lesion size or the interhemispheric tracts connecting to lesions.
  direction: no_effect
  relationship: correlational
  method: DTI
  sample:
    n: 32
    population: patients with chronic left subcortical stroke and aphasia
    phase: not_reported
    time_post_onset: over 6 months after stroke
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Cross-sectional investigation
  - DTI findings should be interpreted with caution
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Patient fractional anisotropy of reconstructed interhemispheric fibers connecting the lesion and right naming-related cortical cluster, and lesion volume. Analysis controlled for demographic variables. Additional metadata has not been transcribed; review the pending-field flags before approval. Source repair (unapproved): The exposure is patient FA in reconstructed interhemispheric connections plus lesion volume, not normative template lesion overlap. Selected result is a null correlation with right-hemisphere cortical thickness. Correct method and retain both P>.20 tests.'
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
  citation: '@Tang2022'
  source_passages:
  - section: Original source P7-S1-C7
    page: 7
    quote: 'No signiﬁcant relationships were found between cortical

      thickness in the right hemisphere cluster for naming/word

      ﬁnding and lesion size or the interhemispheric tracts connecting

      to lesions (both p > 0.20).'
    supports: claim
  - section: Original source P7-S1-C4
    page: 7
    quote: 'The demographic variables,

      lesion size and FA values of connecting tracts were added to the

      models as independent factors.'
    supports: method
  - section: Original source P2-S2-C11
    page: 2
    quote: 'Materials and methods

      Participants

      Thirty-two patients with chronic left subcortical stroke

      (ischemic or hemorrhagic) and history of aphasia were recruited

      with the following inclusion criteria: (i) Native Chinese speakers;

      (ii) over 6 months after stroke; (iii) unilateral subcortical

      lesion; (iv) ability to perform tests; and (v) absence of prior

      diagnosis of neurological disease.'
    supports: sample
  - section: Original source P10-S2-C2
    page: 10
    quote: 'First,

      this is a cross-sectional investigation that might preclude

      the empirical evidence of remote cortical atrophy mediated

      by neurodegeneration of the connecting ﬁber tracts.'
    supports: limitation
  - section: Original source P10-S2-C4
    page: 10
    quote: 'Secondly, the DTI ﬁndings should be

      interpreted with caution.'
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:source-repair
created_on: '2026-11-26'
relationship_review:
  paper: Tang2022
  proposal_id: R012
  approved: false
  original_core_review: {}
  original_publication_entry: null
  original_mapping:
    decision: draft
    reason: 'The study explicitly tested the relationship between cortical thickness in a right hemisphere cluster (related to naming/word finding) and two exposures: lesion size and the integrity of interhemispheric tracts connecting the lesion to that cluster. It reported a null finding for both.'
    bucket: regions
    entity_id: right_hemisphere_naming_cluster
    name: right hemisphere naming cluster
    kind: network
    predictor_type: imaging_metric
    definition: Patient lesion overlap with a population/reference tract template for interhemispheric tracts connecting to the right hemisphere cluster for naming/word finding, and measured lesion size.
    assessment:
    - FreeSurfer
    - DTI
    target: cortical_thickness
    target_kind: impairment
    claim: No significant relationships were found between cortical thickness in the right hemisphere cluster for naming/word finding and lesion size or the interhemispheric tracts connecting to lesions.
    direction: no_effect
    method: LSM
    relationship: correlational
    therapy: null
    sample_n: 32
    population: patients with chronic left subcortical stroke and aphasia
    timing: over 6 months after stroke
    qualifications:
    - Analysis controlled for demographic variables
    limitations:
    - Cross-sectional investigation
    - DTI findings should be interpreted with caution
    optional_pending: []
    evidence_quality: cohort
    passages:
    - source_id: P7-S1-C7
      supports: claim
    - source_id: P7-S1-C4
      supports: method
    - source_id: P2-S2-C11
      supports: sample
    - source_id: P10-S2-C2
      supports: limitation
    - source_id: P10-S2-C4
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
      pdf_sha256: 570fbc62b7fa0a1625963c4cd4bc8916ca2db0115cd1aae08677e2b0e5facb7b
      review_sha256: 31adbe281ea00eb7ba313dc37b9789f34a6b2f52ed43da11ad670c7faba52750
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
    status: hold
    reason: 'construct: The draft''s ''definition'' field incorrectly describes the exposure as ''Patient lesion overlap with a population/reference tract template''. The source (P4-S1-C3, P4-S1-C9, P7-S1-C5) indicates that the exposure is the Fractional Anisotropy (FA) of reconstructed fiber tracts connecting the lesion to the cortical ROI, not a template overlap metric. Additionally, the ''method'' field lists ''LSM'' (Lesion-Symptom Mapping), but this specific null result comes from the subsequent regression/correlation analysis of tract integrity, not the initial SVR-LSM step which identified the clusters.'
    material_issues:
    - issue: 'construct: The draft''s ''definition'' field incorrectly describes the exposure as ''Patient lesion overlap with a population/reference tract template''. The source (P4-S1-C3, P4-S1-C9, P7-S1-C5) indicates that the exposure is the Fractional Anisotropy (FA) of reconstructed fiber tracts connecting the lesion to the cortical ROI, not a template overlap metric. Additionally, the ''method'' field lists ''LSM'' (Lesion-Symptom Mapping), but this specific null result comes from the subsequent regression/correlation analysis of tract integrity, not the initial SVR-LSM step which identified the clusters.'
      source_ids:
      - P4-S1-C3
      - P4-S1-C9
      - P7-S1-C5
      - P3-S1-C7
    seconds_this_run: 80.51996050000889
  source_check:
    profile: agent-repair
    scope: Agent source reconstruction; original model reviews do not certify the changed record. No independent model pass or human approval.
    approved: false
    paper_complete: false
    binding:
      pdf_sha256: 570fbc62b7fa0a1625963c4cd4bc8916ca2db0115cd1aae08677e2b0e5facb7b
      original_mapping_sha256: e2e7455dcb9b1f4e4f87a4de0287c7e1b778179e9118ccaa274f1b2ea576ea33
      original_status_sha256: 01a5c83f90936303b8473054bc82092738aada742d95a0d4e4b208391a90864b
      evidence_sha256: 5cb0d53826e6994543e881497cc8f6c9b8d54198b90f7bddefb41e14edee776e
    publication_correction:
      by: agent:source-repair
      date: '2026-11-26T03:33:02.412795+00:00'
      pdf_pages:
      - 2
      - 4
      - 7
      - 10
      note: The exposure is patient FA in reconstructed interhemispheric connections plus lesion volume, not normative template lesion overlap. Selected result is a null correlation with right-hemisphere cortical thickness. Correct method and retain both P>.20 tests.
      approved: false
      audit: logs/publication/draft-repairs-2026-11-26-round3.json
    remaining:
    - Human source review and approval
    - Full paper completeness review
reviewer_marks:
- id: source-repair-round3
  status: pending
  by: agent:source-repair
  date: '2026-11-26'
  note: The exposure is patient FA in reconstructed interhemispheric connections plus lesion volume, not normative template lesion overlap. Selected result is a null correlation with right-hemisphere cortical thickness. Correct method and retain both P>.20 tests.
---

# Source review required

This repaired draft remains unapproved. Original outputs and review provenance are preserved.
