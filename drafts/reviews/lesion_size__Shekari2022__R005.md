---
id: lesion_size__Shekari2022__R005
name: lesion size
kind: review
findings:
- id: f1
  target: naming_improvement
  target_kind: prognosis
  claim: Shekari2022 reports, summarizing Vitali et al. (2007) and Fridriksson et al. (2007), that larger lesion size was associated with slight naming improvement
  direction: likely
  relationship: synthesis
  method: narrative_review
  sample:
    n: not_reported
    population: Reviewed chronic post-stroke aphasia studies; secondary report of Vitali et al. (2007) and Fridriksson et al. (2007). No new patient cohort.
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
  - limited number of extracted studies
  - variable experimental quality of included studies
  - lack of reported random sampling, blindness, or treatment fidelity in reviewed studies
  evidence_quality: narrative-review
  strength: weak
  notes: 'Reconstructed as a secondary review report, explicitly attributed to Vitali et al. (2007) and Fridriksson et al. (2007). Not a new independent patient cohort; human source review remains pending. Source repair (unapproved): Reconstructed as a secondary review report, explicitly attributed to Vitali et al. (2007) and Fridriksson et al. (2007). Not a new independent patient cohort; human source review remains pending.'
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
  therapy:
    id: anomia_therapy
    name: anomia therapy
  citation: '@Shekari2022'
  source_passages:
  - section: Original source P8-S1-C4
    page: 8
    quote: 'Although one cannot interpret the results with

      certainty due to the extracted studies’ limited number and

      experimental quality, this review revealed that both semantic

      and phonological treatments improved naming.'
    supports: limitation
  - section: Original source P3-S1-C16
    page: 3
    quote: 'However, the reviewed studies did not report ran-

      dom sampling, blindness, or treatment fidelity.'
    supports: limitation
  - section: Original source P8-S2-C3
    page: 8
    quote: 'On the other hand,

      larger lesion size was associated with slight naming improve-

      ment.'
    supports: claim
  - section: Original source P3-S1-C2
    page: 3
    quote: 'Data were

      synthesized using a narrative method and meta-analysis was

      not conducted due to the heterogeneity of the studies

      (Table 1).'
    supports: method
  - section: Original source P3-S1-C11
    page: 3
    quote: 'Results

      Included studies

      A total of 14 studies were included (Figure 1). 146 aphasia

      participants (63 females) participated in these studies. 11

      studies had reported detailed data about the age of partici-

      pants

      that

      ranged

      from

      21

      to

      81 years

      (Mean

      ¼

      56.04 ± 11.91).'
    supports: sample
  design: systematic-review
schema_version: '2.9'
status: draft
created_by: agent:source-repair
created_on: '2026-11-26'
relationship_review:
  paper: Shekari2022
  proposal_id: R005
  approved: false
  original_core_review: {}
  original_publication_entry: null
  original_mapping:
    decision: draft
    reason: The source is a narrative review that synthesizes findings from 14 studies. It explicitly reports an association between larger lesion size and slight naming improvement following anomia therapy, contrasting this with the more significant improvements seen with smaller lesion sizes.
    bucket: predictors
    entity_id: lesion_size
    name: lesion size
    kind: classical
    predictor_type: imaging_metric
    definition: lesion size as reported in the reviewed studies
    assessment: []
    target: naming_improvement
    target_kind: prognosis
    claim: larger lesion size was associated with slight naming improvement
    direction: likely
    method: meta-analysis
    relationship: synthesis
    therapy:
      id: anomia_therapy
      name: anomia therapy
    sample_n: 146
    population: individuals with acquired aphasia caused by CVA in the chronic phase of stroke
    timing: chronic phase of stroke
    qualifications:
    - finding is part of a synthesis of 14 studies
    - contrasted with smaller lesion size which was associated with more significant improvements
    limitations:
    - limited number of extracted studies
    - variable experimental quality of included studies
    - lack of reported random sampling, blindness, or treatment fidelity in reviewed studies
    optional_pending: []
    evidence_quality: narrative-review
    passages:
    - source_id: P8-S2-C3
      supports: claim
    - source_id: P3-S1-C11
      supports: sample
    - source_id: P3-S1-C14
      supports: sample
    - source_id: P2-S3-C7
      supports: sample
    - source_id: P3-S1-C2
      supports: method
    - source_id: P8-S1-C4
      supports: limitation
    - source_id: P3-S1-C16
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
      pdf_sha256: 070c1deead0f311773ac0324e4b3ca57dcd9dd5c348f9de6ef0cfdda433ae20a
      review_sha256: ddcc5025518180128fcc9f580a9d484df35db26e268192e69650a6c10abf9ef3
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
    proposal: R005
    status: failed
    reason: No primary evidence for the selected analysis
    seconds_this_run: 37.28691837500082
  source_check:
    profile: agent-repair
    scope: Agent source reconstruction; original model reviews do not certify the changed record. No independent model pass or human approval.
    approved: false
    paper_complete: false
    binding:
      pdf_sha256: 070c1deead0f311773ac0324e4b3ca57dcd9dd5c348f9de6ef0cfdda433ae20a
      original_mapping_sha256: bf25ffa3234557362db13b37479c4a44171379d2a0a108e92d2fbb8eb8cce9da
      original_status_sha256: 7af1dbaaedef006736953a0abe9aacd9c0ccb91b21b4869e460e11ad398b462b
      evidence_sha256: 100c19bb8503a67799d79af5cc983e1c13496a9aae4d7dcfca4a75bdd03c7a43
    publication_correction:
      by: agent:source-repair
      date: '2026-11-26T02:05:16.806224+00:00'
      pdf_pages:
      - 1
      - 3
      - 8
      - 9
      note: Reconstructed as a secondary review report, explicitly attributed to Vitali et al. (2007) and Fridriksson et al. (2007). Not a new independent patient cohort; human source review remains pending.
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
  note: Reconstructed as a secondary review report, explicitly attributed to Vitali et al. (2007) and Fridriksson et al. (2007). Not a new independent patient cohort; human source review remains pending.
---

# Source review required

This repaired draft remains unapproved. Original outputs and review provenance are preserved.
