---
id: intensive_anomia_therapy__Shekari2022__R007
name: intensive anomia therapy
kind: review
findings:
- id: f1
  target: bilateral_brain_recruitment
  target_kind: impairment
  claim: Shekari2022 reports, summarizing Menke et al. (2009), Marcotte et al. (2012) and van Hees et al. (2014), that Intensive anomia therapy was associated with the recruitment of both hemisphere areas in patients with moderate-to-severe naming impairments.
  direction: likely
  relationship: synthesis
  method: narrative_review
  sample:
    n: not_reported
    population: Reviewed chronic post-stroke aphasia studies; secondary report of Menke et al. (2009), Marcotte et al. (2012) and van Hees et al. (2014). No new patient cohort.
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
  - narrative synthesis of heterogeneous studies
  - limited number of studies and experimental quality
  - lack of reported random sampling, blindness, or treatment fidelity in reviewed studies
  evidence_quality: narrative-review
  strength: weak
  notes: 'Reconstructed as a secondary review report, explicitly attributed to Menke et al. (2009), Marcotte et al. (2012) and van Hees et al. (2014). Not a new independent patient cohort; human source review remains pending. Source repair (unapproved): Reconstructed as a secondary review report, explicitly attributed to Menke et al. (2009), Marcotte et al. (2012) and van Hees et al. (2014). Not a new independent patient cohort; human source review remains pending.'
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
    id: intensive_anomia_therapy
    name: intensive anomia therapy
  citation: '@Shekari2022'
  source_passages:
  - section: Original source P15-S3-C8
    page: 15
    quote: 'This is a significant limita-

      tion, and future research must focus on it because meta-

      analyses could integrate variable results from the small-data

      studies, which are still very frequent in this field of research.'
    supports: limitation
  - section: Original source P9-S1-C3
    page: 9
    quote: 'In Menke et al’s study (2009), intensive treatment of

      anomia therapy was associated with the significant improve-

      ment in the treated and moderate improvement of the

      untreated items.'
    supports: claim
  - section: Original source P9-S1-C4
    page: 9
    quote: 'In this study, naming improvement was

      related to the recruitment of both hemisphere areas.'
    supports: claim
  - section: Original source P9-S1-C6
    page: 9
    quote: 'Such effects were

      reported with changes limited to several language-related

      areas in milder aphasia patients (van Hees et al., 2014) and

      the recruitment of bilateral brain areas in patients with

      moderate-to-severe word-finding difficulties (Marcotte et al.,

      2012; Menke et al., 2009).'
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
  proposal_id: R007
  approved: false
  original_core_review: {}
  original_publication_entry: null
  original_mapping:
    decision: draft
    reason: The review synthesizes findings on the relationship between anomia therapy intensity and brain recruitment, specifically citing a study (Menke et al., 2009) where intensive treatment was associated with bilateral brain recruitment in patients with moderate-to-severe naming impairments.
    bucket: therapies
    entity_id: intensive_anomia_therapy
    name: intensive anomia therapy
    kind: therapy
    predictor_type: clinical
    definition: Anomia therapy delivered with a higher number of sessions and hours in shorter periods (defined as extensity of therapy).
    assessment:
    - task-based fMRI
    target: bilateral_brain_recruitment
    target_kind: impairment
    claim: Intensive anomia therapy was associated with the recruitment of both hemisphere areas in patients with moderate-to-severe naming impairments.
    direction: likely
    method: fMRI_activation
    relationship: treatment_response
    therapy:
      id: intensive_anomia_therapy
      name: intensive anomia therapy
    sample_n: 146
    population: individuals with acquired aphasia caused by CVA in the chronic phase
    timing: post-treatment
    qualifications:
    - finding specifically noted for patients with moderate-to-severe word-finding difficulties
    - contrasted with milder aphasia patients where changes were limited to several language-related areas
    limitations:
    - narrative synthesis of heterogeneous studies
    - limited number of studies and experimental quality
    - lack of reported random sampling, blindness, or treatment fidelity in reviewed studies
    optional_pending: []
    evidence_quality: narrative-review
    passages:
    - source_id: P9-S1-C3
      supports: claim
    - source_id: P9-S1-C4
      supports: claim
    - source_id: P9-S1-C5
      supports: sample
    - source_id: P9-S1-C6
      supports: claim
    - source_id: P8-S2-C7
      supports: method
    - source_id: P3-S1-C14
      supports: sample
    - source_id: P3-S1-C11
      supports: sample
    - source_id: P15-S3-C8
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
    proposal: R007
    status: failed
    reason: No primary evidence for the selected analysis
    seconds_this_run: 37.495681499975035
  source_check:
    profile: agent-repair
    scope: Agent source reconstruction; original model reviews do not certify the changed record. No independent model pass or human approval.
    approved: false
    paper_complete: false
    binding:
      pdf_sha256: 070c1deead0f311773ac0324e4b3ca57dcd9dd5c348f9de6ef0cfdda433ae20a
      original_mapping_sha256: dc2a669b820ed4dc734033ff24fbfbe792e7eed8e0eb86ff259edd0465d6284d
      original_status_sha256: 1221e25bbe522f4da5167f2ac3dadb6ffcc701343d7c2dc06b9241160d58d176
      evidence_sha256: 100c19bb8503a67799d79af5cc983e1c13496a9aae4d7dcfca4a75bdd03c7a43
    publication_correction:
      by: agent:source-repair
      date: '2026-11-26T02:05:16.806224+00:00'
      pdf_pages:
      - 1
      - 3
      - 8
      - 9
      note: Reconstructed as a secondary review report, explicitly attributed to Menke et al. (2009), Marcotte et al. (2012) and van Hees et al. (2014). Not a new independent patient cohort; human source review remains pending.
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
  note: Reconstructed as a secondary review report, explicitly attributed to Menke et al. (2009), Marcotte et al. (2012) and van Hees et al. (2014). Not a new independent patient cohort; human source review remains pending.
---

# Source review required

This repaired draft remains unapproved. Original outputs and review provenance are preserved.
