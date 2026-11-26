---
id: semantic_feature_analysis__Efstratiadou2018__R004
name: semantic feature analysis
kind: review
findings:
- id: f1
  target: generalization_to_untrained_items
  target_kind: prognosis
  claim: Efstratiadou2018 reports from its analysis of published cases that semantic feature analysis (SFA) has a small effect on generalization to untrained items, with positive generalization outcomes evident for 40% of participants.
  direction: likely
  relationship: synthesis
  method: narrative_review
  sample:
    n: not_reported
    population: 21 published single-case/case-series studies, 55 persons with aphasia, including stroke and traumatic brain injury; not a stroke-only new cohort.
    phase: not_reported
    time_post_onset: posttherapy gains assessed immediately after treatment ended
  statistics:
    threshold: See source passages for the review’s case-level statistical analysis; not a new cohort.
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - High heterogeneity across participants in age and time post onset
  - Lack of standardized dosage and treatment duration across included studies
  - Variability in treatment protocols (e.g., modifications to feature categories or eliciting fewer features)
  - Based on single case and case series studies
  evidence_quality: narrative-review
  strength: weak
  notes: 'Reconstructed the saved mapping after an incomplete checker response, using the original article passages. This is an agent source check, not a completed model review or human approval. Preserved the review-level result without treating the reported cases as a newly recruited cohort or inferring missing comparison denominators. Source repair (unapproved): Reconstructed the saved mapping after an incomplete checker response, using the original article passages. This is an agent source check, not a completed model review or human approval. Preserved the review-level result without treating the reported cases as a newly recruited cohort or inferring missing comparison denominators.'
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
  therapy:
    id: semantic_feature_analysis
    name: semantic feature analysis
  citation: '@Efstratiadou2018'
  source_passages:
  - section: Original source P15-S1-C13
    page: 15
    quote: 'Synthesizing the find-

      ings of 21 single case and case series studies suggests that

      SFA is effective in improving treated items and has a small

      effect on generalization to untrained items.'
    supports: claim
  - section: Original source P14-S1-C15
    page: 14
    quote: 'Positive generalization outcomes were evident

      for 40% of participants.'
    supports: claim
  - section: Original source P10-S2-C4
    page: 10
    quote: 'Generalization effects ranged

      from negligible (e.g., Rider et al., 2008) to strong (Boyle,

      2004).'
    supports: claim
  - section: Original source P10-S2-C10
    page: 10
    quote: 'In terms of generalization to untreated

      items, it was mostly the individuals with Broca’s aphasia

      that showed positive gains (57.14%).'
    supports: claim
  - section: Original source P15-S1-C2
    page: 15
    quote: 'Therefore, another limiting factor is the lack

      of a standardized dosage and treatment duration across

      studies.'
    supports: limitation
  - section: Original source P14-S3-C12
    page: 14
    quote: 'Many studies changed the tra-

      ditional SFA protocol in various ways, such as modifica-

      tions to the semantic feature categories (Mehta & Isaki,

      2016; Wambaugh & Ferguson, 2007; Wambaugh et al.,

      2014), eliciting fewer features (Hashimoto & Frome, 2011;

      Mehta & Isaki, 2016), writing the features in addition

      to or instead of saying them (Hashimoto & Frome, 2011),

      following different treatment stages (L. A. Davis & Stanton,

      2005), and adding new factors, such as independent home-

      work (Falconer & Antonucci, 2012).'
    supports: limitation
  - section: Original source P4-S3-C6
    page: 4
    quote: 'All studies were single case

      studies (N = 21).'
    supports: limitation
  - section: Original source P15-S1-C13
    page: 15
    quote: 'Synthesizing the find-

      ings of 21 single case and case series studies suggests that

      SFA is effective in improving treated items and has a small

      effect on generalization to untrained items.'
    supports: method
  - section: Original source P1-S1-C6
    page: 1
    quote: 'Results: Twenty-one studies were reviewed reporting

      on 55 persons with aphasia.'
    supports: sample
  - section: Original source P10-S1-C12
    page: 10
    quote: 'Apha-

      sia was due to a stroke in 51 individuals and to traumatic

      brain injury in four individuals (neuropathology for three

      individuals was not reported).'
    supports: sample
  design: systematic-review
schema_version: '2.9'
status: draft
created_by: agent:source-repair
created_on: '2026-11-26'
relationship_review:
  paper: Efstratiadou2018
  proposal_id: R004
  approved: false
  original_core_review: {}
  original_publication_entry: null
  original_mapping:
    decision: draft
    reason: The systematic review synthesizes results from 21 single-case studies to evaluate the efficacy of SFA, specifically reporting on the rate of generalization to untrained items across the total participant pool.
    bucket: therapies
    entity_id: semantic_feature_analysis
    name: semantic feature analysis
    kind: therapy
    predictor_type: clinical
    definition: A treatment protocol where individuals with word retrieval difficulties are shown a picture to name and encouraged to generate semantic features (e.g., group, action, use, location, properties, associations) by completing a feature analysis chart, with clinician cueing that is gradually faded.
    assessment: []
    target: generalization_to_untrained_items
    target_kind: prognosis
    claim: Semantic feature analysis (SFA) has a small effect on generalization to untrained items, with positive generalization outcomes evident for 40% of participants.
    direction: likely
    method: meta-analysis
    relationship: treatment_response
    therapy:
      id: semantic_feature_analysis
      name: semantic feature analysis
    sample_n: 55
    population: persons with aphasia (including fluent and nonfluent types, with a majority having mild to moderate severity)
    timing: posttherapy gains assessed immediately after treatment ended
    qualifications:
    - Generalization effects ranged from negligible to strong across studies
    - Positive gains in generalization were most frequent in individuals with Broca's aphasia (57.14%)
    limitations:
    - High heterogeneity across participants in age and time post onset
    - Lack of standardized dosage and treatment duration across included studies
    - Variability in treatment protocols (e.g., modifications to feature categories or eliciting fewer features)
    - Based on single case and case series studies
    optional_pending: []
    evidence_quality: meta-analysis
    passages:
    - source_id: P15-S1-C13
      supports: claim
    - source_id: P14-S1-C15
      supports: claim
    - source_id: P10-S2-C4
      supports: claim
    - source_id: P10-S2-C10
      supports: claim
    - source_id: P6-S3-C4
      supports: sample
    - source_id: P12-S1-C3
      supports: method
    - source_id: P15-S1-C2
      supports: limitation
    - source_id: P14-S3-C12
      supports: limitation
    - source_id: P4-S3-C6
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
      pdf_sha256: c8562d7b60d51b5ec07c8d06adda9523b0af176ca21610d4d53af3f26f94ec8a
      review_sha256: 71453e86d91903d06b2957c7e7f267f13b820fc57127950d0f32df0aeb2c5e77
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
    proposal: R004
    status: failed
    reason: Truncated output held
    seconds_this_run: 135.32209704100387
  source_check:
    profile: agent-repair
    scope: Agent source reconstruction; original model reviews do not certify the changed record. No independent model pass or human approval.
    approved: false
    paper_complete: false
    binding:
      pdf_sha256: c8562d7b60d51b5ec07c8d06adda9523b0af176ca21610d4d53af3f26f94ec8a
      original_mapping_sha256: dd9e636fce724eee17e9dcc2d5ce9a92df5c52eef053413281aaa57cab35a10d
      original_status_sha256: 99fb2b381f414d768e8dcc8fd6cf85fd74cf60e148c30e7f89dd8557e70b3199
      evidence_sha256: 7972900ed5b1ab60c1ebf0dd108c0f774915f0668bec045c7679f8e5c5043fcc
    publication_correction:
      by: agent:source-repair
      date: '2026-11-26T02:05:16.806224+00:00'
      pdf_pages:
      - 6
      - 10
      - 12
      - 14
      - 15
      note: Reconstructed the saved mapping after an incomplete checker response, using the original article passages. This is an agent source check, not a completed model review or human approval. Preserved the review-level result without treating the reported cases as a newly recruited cohort or inferring missing comparison denominators.
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
  note: Reconstructed the saved mapping after an incomplete checker response, using the original article passages. This is an agent source check, not a completed model review or human approval. Preserved the review-level result without treating the reported cases as a newly recruited cohort or inferring missing comparison denominators.
---

# Source review required

This repaired draft remains unapproved. Original outputs and review provenance are preserved.
