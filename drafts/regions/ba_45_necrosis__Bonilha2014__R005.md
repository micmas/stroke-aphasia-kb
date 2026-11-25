---
id: ba_45_necrosis
name: BA 45 necrosis cluster
kind: network
findings:
- id: f1
  target_audit:
    status: behaviour_label_present
    category: behaviour_or_language_construct
    original_target: speech_fluency
    reason: Label names a behaviour or language construct; its exact operational definition and measurement
      still need source review.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  outcome_measurement:
    status: needs_source_review
    instruments: []
    note: Outcome instrument/task is not yet verified for this finding. Do not infer it from the predictor
      or a paper-wide test list.
  target: speech_fluency
  target_kind: impairment
  claim: When used in a model combined with BA 45 disconnection, BA 45 necrosis was
    not an independent predictor of speech fluency.
  direction: no_effect
  relationship: correlational
  method: LSM
  sample:
    n: 39
    population: patients with chronic aphasia due to a left hemisphere ischemic stroke
    phase: not_reported
    time_post_onset: at least six months post-stroke
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - results are subject to the technical limitations of MRI tractography used for
    the combined model
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Percentage of necrotic damage to Brodmann area 45
    measured via T1-weighted, T2-weighted, or FLAIR MRI sequences. measured as part
    of a multiple linear regression model that included BA 45 disconnection. Additional
    metadata has not been transcribed; review the pending-field flags before approval.
    PDF image reading (P2-S2-C5, two-model agreement, human verification pending):
    Methods


    Subjects


    We studied thirty-nine individuals (mean age 62.7 ±12.8 years, 22 male, 16 female)
    who suffered a left hemisphere ischemic stroke at least six months prior to enrolling
    in this study (Table I in the Online Data Supplement) Original text-layer quotation
    is preserved below.'
  imaging_details:
    reference_space: not_reported
    atlases_used: []
  lesion_mapping: {}
  provenance:
    extracted_by: model:gemma4:31b
    extracted_on: '2026-11-20'
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
    - proposed_concept:speech_fluency
  citation: '@Bonilha2014'
  source_passages:
  - section: Original source P5-S1-C11
    page: 5
    quote: "Finally, we also observed significant relationship between \nfluency and\
      \ a model composed by BA 45 necrosis and BA 45 disconnection F=4.62, \np<0.01;\
      \ necrosis: β=2.89; p=0.13; disconnection β=7.52; p=0.025)."
    supports: claim
  - section: Original source P5-S1-C12
    page: 5
    quote: "Similarly, in this model, \nnecrosis alone was not an independent predictor\
      \ of fluency (Figure 4)."
    supports: claim
  - section: Original source P2-S2-C5
    page: 2
    quote: "Methods\nSubjects\nWe studied thirty-nine individuals (mean age 62.7 ±12.8\
      \ years, 22 male, 16 female) who \nsuffered a left hemisphere ischemic stroke\
      \ at least six months prior to enrolling in this study \n(Table I in the Online\
      \ Data Supplement)."
    supports: sample
  - section: Original source P4-S1-C7
    page: 4
    quote: "Statistical Analyses\nWe performed multiple linear regression analyses\
      \ with the performance on naming measures \ndefined as the dependent variable,\
      \ with the following independent variables: 1) percentage \nof damage to each\
      \ BA area, 2) percentage number of fibers of each BA area."
    supports: method
  - section: Original source P3-S1-C10
    page: 3
    quote: "Testing was performed by a speech pathologist and included the Western\
      \ Aphasia \nBattery16 (WAB) and the Philadelphia Naming Test17 (PNT)."
    supports: claim
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-20'
relationship_review:
  paper: Bonilha2014
  proposal_id: R005
  review_status_sha256: 79aef69c5137295615c00df451eafe7866bae6eda751eb63b2031edf5d888210
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 7d4052892e7a83bbff8a6f1682333adc8cd42c22a71092dc583c8fea43d3f125
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 7d4052892e7a83bbff8a6f1682333adc8cd42c22a71092dc583c8fea43d3f125
        A/passages.json: 014a1fc551fe09ccacd1bec7575e1d5a55de1b5b40c94ab9a25c17c1aed65b81
        A/raw.json: dab5b9db25f3b4792d5d0ea514ac6ebda8e2b5f69a1acd065b44091308bb1157
        A/source-units.json: 434de942e75cac1bfdc24ab5184102ccf8a0c02420a5fdb93d164f299faad5ed
        A/full-source-units.json: 086a3ccdc168850c3e0dccb752bfc1328767fab696eb647caab626cee2c3fa83
        A/meta.json: 7090c3b55aad2014f83a775ba509496d811967087ec545e32cde6dfbebf7d4da
        A/table-images/manifest.json: 469a4dc4888a8a8d0fda8c124c04c5e1199bd95dece15b7fbbc195b60267c11e
        A/clauses/window-03/raw.json: 30cf954a20eb21a007fd77c9dfb3f2a1fb57fbf2e7d973ab990f06a9734ac3f5
        A/clauses/window-03/prompt.txt: d511a799acf45a6f9d58c3c7302dc3850f8cae1c12f84b594adf3e2aeda51956
        A/clauses/window-03/meta.json: 66aafd0e040d2598aec5c5fc0b4f0e45b260ba7b7a9b3fbf0faaabd517b93ab9
        A/clauses/window-04/raw.json: 1dacfbb57ec412041f482c195b854ee123c7ca0e2cb889a384631b1e0332fe55
        A/clauses/window-04/prompt.txt: f8ebd5f75ac8cea2a2f60410b474ddf5ec0d80e67bc66bea5fc865b679bdd165
        A/clauses/window-04/meta.json: 8cdc2e12b01bca88af3b8f490e557f20c0bcaffc6fbeafb4cfec7cf3ada1ccec
        A/clauses/window-05/raw.json: 3a89cf0e7baae2a5acd6da60a9f5cf7cbabc5a581431d87d99763b2ce3bf4eed
        A/clauses/window-05/prompt.txt: 7e7669245c0e32111fa5367046f977f0b9bacf3e877bd0f7b8612bc4193b450a
        A/clauses/window-05/meta.json: 9a76f1f769624db0c3ace8c0b9e383aea08a5cc8f3925bafc0db7121eed86dbb
        A/clauses/window-02/raw.json: 2821e661d55eb246da4dc16e7b9f701048c9f3a8dbb53e43b0d530d2b6664f7e
        A/clauses/window-02/prompt.txt: 40e4efc8e1208399f53d1d58dd2e4860292e75b1ed07dcaedc17ae78308dc14c
        A/clauses/window-02/meta.json: cc6693ce503a4527c3ec86e0f5ae1ee130ff475a8283fbb539b282b1527c0bc0
        A/clauses/window-01/raw.json: d23750314e467d1fb5a374a045719b5e0707ddff1872d44c622532c7e15210ed
        A/clauses/window-01/prompt.txt: 8927bf5d9a2b7cbd49d6e0962421ec8fd7b24b3b13e94d042bfe3cedfa9a3f53
        A/clauses/window-01/meta.json: baf3a58caf9d070e0e6fc682d5fe7df410bcbe8460a9e6f531f7365245dab6ad
        B/passages.json: 014a1fc551fe09ccacd1bec7575e1d5a55de1b5b40c94ab9a25c17c1aed65b81
        B/raw.json: c8126a39d6a75f48b848a535d7641157d944dfb2ccddcaea72250953efbf73e0
        B/source-units.json: 434de942e75cac1bfdc24ab5184102ccf8a0c02420a5fdb93d164f299faad5ed
        B/full-source-units.json: 086a3ccdc168850c3e0dccb752bfc1328767fab696eb647caab626cee2c3fa83
        B/meta.json: 601deeb95a84f0a5d1c485d01ccec03c097cbcf90aaba986173ee2ca5b67c381
        B/table-images/manifest.json: 469a4dc4888a8a8d0fda8c124c04c5e1199bd95dece15b7fbbc195b60267c11e
        B/clauses/window-03/raw.json: 54b4a2646892e252fab3572e4b4330b098ef322ffb75d4ef9a1aab2c6373dc04
        B/clauses/window-03/prompt.txt: d511a799acf45a6f9d58c3c7302dc3850f8cae1c12f84b594adf3e2aeda51956
        B/clauses/window-03/meta.json: 06625e0bce2fc00d7c0423613c235666b44cf0246e0c4dc4d94ba9cf9f885ba2
        B/clauses/window-04/raw.json: 50cfeae658fa4d0d99c7eab6a53a18d41fa58bdb273f9d9bcacb9af30d0ef294
        B/clauses/window-04/prompt.txt: f8ebd5f75ac8cea2a2f60410b474ddf5ec0d80e67bc66bea5fc865b679bdd165
        B/clauses/window-04/meta.json: f93bdcf6fbed41bb974f74e3b6962d4507a8845d0ea8cc1e25cf675a936334e4
        B/clauses/window-05/raw.json: 1b9964e1c1895f89504349f0e422393a6d6338d0e332f8c44b834743880d4def
        B/clauses/window-05/prompt.txt: 7e7669245c0e32111fa5367046f977f0b9bacf3e877bd0f7b8612bc4193b450a
        B/clauses/window-05/meta.json: 0ca0cfca1ad6e37bf5e7ab5039d8f7b464a9afce48b1538e2a67f7bcc0296d73
        B/clauses/window-02/raw.json: 0d4621a85159266e3e99311a41c2817a2266d14f54a4098f576312029303dd4b
        B/clauses/window-02/prompt.txt: 40e4efc8e1208399f53d1d58dd2e4860292e75b1ed07dcaedc17ae78308dc14c
        B/clauses/window-02/meta.json: 7e5df46977fd9ef7530661b0732780b46833cfe146b617daa2889712ac96549c
        B/clauses/window-01/raw.json: 49c72f7bf61c30cfdbebdf70c2b7e93a177f44f2602584b6d90e646257b41f37
        B/clauses/window-01/prompt.txt: 8927bf5d9a2b7cbd49d6e0962421ec8fd7b24b3b13e94d042bfe3cedfa9a3f53
        B/clauses/window-01/meta.json: e0bb503169a37b398e90c99dea89271074121ac6f2a8180454cd8d828de1a787
      code:
        relationship_review.py: e1418d43751ffa47aebde470eca9d70747211671c954e9423a376203ee2281a0
        relationship_evidence.py: 531c8a74f366f92842f315f2722b2ba7dbdbeaf052aefa60cdf0c8365ccd6fbb
        ollama_client.py: 4f76f789470a78483698ab86b038600fc2e8c2281692a370bea05f364cee76ea
        strict_data.py: 1b2d69dbbb3b87e23d461caecf0302db7464712a2b2613624bde4a3512473d0b
      model: gemma4:26b
      model_digest: 48eb98ec778c163d87f69d735fcdd79e345063af9af4685613fd018ae5debf5e
      host: http://localhost:11434
      max_output_tokens: 20000
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 7d4052892e7a83bbff8a6f1682333adc8cd42c22a71092dc583c8fea43d3f125
      source_review: _compare/relationships-2026-11-16/review-current/Bonilha2014
      source_status_sha256: 7857c271e5f46429259a8d9c9efecb0754d003f82cde1653d8c9d74b020f8c71
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R005
    exposure:
      text: BA 45 necrosis
    outcome:
      text: speech fluency
    analysis_label: Sensitivity analysis for fluency
    relation: sensitivity
    evidence_ids:
    - P5-S1-C12
    qualifier_ids: []
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 7d4052892e7a83bbff8a6f1682333adc8cd42c22a71092dc583c8fea43d3f125
      source_review: _compare/relationships-2026-11-16/review-current/Bonilha2014
      source_status_sha256: 7857c271e5f46429259a8d9c9efecb0754d003f82cde1653d8c9d74b020f8c71
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P4-S1-C11
      - Result passage disposed without unit P4-S1-C12
      - Result passage disposed without unit P4-S1-C13
      - Result passage disposed without unit P4-S1-C14
      - Result passage disposed without unit P4-S2-C2
      - Result passage disposed without unit P4-S2-C3
      - Result passage disposed without unit P4-S2-C4
      - Result passage disposed without unit P4-S2-C6
      - Accounting without a linked unit P5-S1-C10
      - Accounting without a linked unit P5-S1-C11
      - Accounting without a linked unit P5-S1-C12
      - Result passage disposed without unit P5-S1-C3
      - Accounting without a linked unit P5-S1-C5
      - Accounting without a linked unit P5-S1-C8
      - Accounting without a linked unit P5-S1-C9
      - Unaccounted source passage P5-S1-C12
      - Unaccounted source passage P5-S1-C9
      - Unaccounted source passage P5-S1-C8
      - Unaccounted source passage P5-S1-C10
      - Unaccounted source passage P5-S1-C11
      - Unaccounted source passage P5-S1-C5
      - Result passage disposed without unit P6-S1-C4
      - Result passage disposed without unit P6-S1-C6
      - Result passage disposed without unit P6-S1-C7
      - Result passage disposed without unit P6-S2-C4
      - Result passage disposed without unit P6-S2-C6
      unattached_null_or_qualifier_ids:
      - P5-S1-C5
      - P6-S2-C4
      suppressed_nonrepresented_units: 14
      default_disposition_count_requires_completeness_check: 85
      unselected_timing_passages:
      - P2-S2-C2
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P5-S1-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P4-S1-C3
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      empty_frame_slots_require_confirmation:
      - validation
      - personal_factors
      - tested_personal_effects
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required: []
      unlinked_tables: []
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P4-S2
        - P5-S1
        - P5-S2
        - P6-S1
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 7d4052892e7a83bbff8a6f1682333adc8cd42c22a71092dc583c8fea43d3f125
      source_review: _compare/relationships-2026-11-16/review-current/Bonilha2014
      source_status_sha256: 7857c271e5f46429259a8d9c9efecb0754d003f82cde1653d8c9d74b020f8c71
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C8
      disposition: represented
      result_indexes:
      - 0
      reason: Reports the association between BA 45 damage/disconnection and naming
        performance.
    - source_id: P4-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Provides mean AQ for the group.
    - source_id: P4-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Provides mean scores for WAB subtests.
    - source_id: P4-S1-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes distribution of aphasia types.
    - source_id: P4-S1-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Provides average PNT naming performance.
    - source_id: P4-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes lesion location in the left hemisphere.
    - source_id: P4-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes variability in lesion location.
    - source_id: P4-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes maximal lesion overlap areas.
    - source_id: P4-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes relative reduction in connectivity per BA.
    - source_id: P5-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the complementary nature of connectivity damage and necrosis.
    - source_id: P5-S1-C5
      disposition: represented
      result_indexes:
      - 6
      reason: Reports null relationship between overall lesion size and language measures.
    - source_id: P5-S1-C8
      disposition: represented
      result_indexes:
      - 0
      reason: Reports the association between BA 45 damage/disconnection and naming
        performance.
    - source_id: P5-S1-C9
      disposition: represented
      result_indexes:
      - 1
      reason: Reports the association between BA 22 damage/disconnection and comprehension.
    - source_id: P5-S1-C10
      disposition: represented
      result_indexes:
      - 2
      reason: Reports that necrosis alone was not independently associated with comprehension.
    - source_id: P5-S1-C11
      disposition: represented
      result_indexes:
      - 3
      reason: Reports the association between BA 45 damage/disconnection and fluency.
    - source_id: P5-S1-C12
      disposition: represented
      result_indexes:
      - 4
      reason: Reports that necrosis alone was not an independent predictor of fluency.
    - source_id: P5-S2-C2
      disposition: repeated
      result_indexes:
      - 5
      reason: Restatement of the null association between AQ and BA models.
    - source_id: P5-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about coexistence of disconnection and necrosis.
    - source_id: P5-S2-C5
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of naming dependence on BA 45 integrity and connectivity.
    - source_id: P6-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: General observation of connectivity reduction in affected hemisphere.
    - source_id: P6-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: General observation about intact areas exhibiting reduced connectivity.
    - source_id: P6-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement that connectivity reduction cannot be inferred from
        necrosis alone.
    - source_id: P6-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes variability in connectivity preservation relative to necrosis.
    - source_id: P6-S2-C3
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of naming performance association with BA 45.
    - source_id: P6-S2-C4
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement that connectivity predicts naming when controlling for necrosis.
    - source_id: P6-S2-C6
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of preserved connectivity as an independent predictor of
        naming.
    - source_id: P7-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement on importance of subcortical lesions.
    - source_id: P7-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of functional modulation and structural connectivity.
    unresolved_coverage: []
    pending_source_ids:
    - P4-S1-C11
    - P4-S1-C12
    - P4-S1-C13
    - P4-S1-C14
    - P4-S2-C2
    - P4-S2-C3
    - P4-S2-C4
    - P4-S2-C6
    - P5-S1-C3
    - P5-S2-C2
    - P5-S2-C4
    - P5-S2-C5
    - P6-S1-C4
    - P6-S1-C5
    - P6-S1-C6
    - P6-S1-C7
    - P6-S2-C3
    - P6-S2-C4
    - P6-S2-C6
    - P7-S1-C1
    - P7-S1-C2
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review: []
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P2-S2-C5
      recruited_sample:
      - P2-S2-C5
      - P3-S1-C1
      - P3-S1-C7
      eligibility:
      - P3-S1-C2
      - P3-S1-C3
      - P3-S1-C5
      imaging_provenance:
      - P1-S1-C5
      - P3-S2-C4
      imaging_timing:
      - P2-S2-C5
      outcome_timing:
      - P3-S1-C9
      outcome_definition:
      - P3-S1-C11
      - P3-S1-C12
      - P3-S1-C13
      - P5-S1-C6
      validation: []
      analysis_restrictions:
      - P4-S1-C10
      dependent_variable_statement:
      - P4-S1-C7
      limitations:
      - P4-S1-C2
      - P6-S1-C9
      - P6-S2-C3
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P5-S1-C8
      - P5-S1-C9
      - P5-S1-C11
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P2-S2-C5
      - P2-S2-C6
      - P3-S1-C1
      - P3-S1-C2
      - P3-S1-C3
      - P3-S1-C4
      - P4-S1-C13
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P5-S1-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P4-S1-C3
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    policy: All slots and enums remain unverified. Held selections are not evidence
      of absence. Original response is preserved in frame/raw.json.
  approved: false
  source_check:
    profile: core
    scope: Independent model text review of core meaning; not human approval or complete
      PDF verification
    binding:
      profile: core
      version: core-source-check-v3
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      checker_model: qwen3.8:27b
      checker_digest: 47951e4a666180bc2aedfc93c169472f2de783696fe196efbf063f5730ecf163
      host: http://localhost:11434
      pdf_sha256: 7d4052892e7a83bbff8a6f1682333adc8cd42c22a71092dc583c8fea43d3f125
      review_sha256: 79aef69c5137295615c00df451eafe7866bae6eda751eb63b2031edf5d888210
      code_sha256: c4650d24fa3e36e6f317cb65cc7626277a28936a7cdf5d07248d4b1e5bfa09aa
      source_helpers_sha256: e0e0f295e5efa1fdb4e9e8c84ca491d062df3aefe8ca8b4d9ca85fcb6d4c9082
      converter_sha256: 048f1e35905528676837a00b1b2406b1c97cb1eb47c48d63f121a5c00cc0afeb
      table_helpers_sha256: 78e562e9725fc484d6a12279ea710856dfd1d9aa13ee178d0358e9c0acdd2c8c
      mapper_budget: 2500
      reviewer_budget: 1600
      approved: false
      visual:
        models: &id001
        - gemma4:31b
        - qwen3.8:27b
        digests: &id002
        - 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        - 47951e4a666180bc2aedfc93c169472f2de783696fe196efbf063f5730ecf163
        code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
        layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
    approved: false
    core_review:
      own_result_source_ids:
      - P5-S1-C12
      source_result: In a multiple linear regression model predicting speech fluency
        from BA 45 necrosis and BA 45 disconnection, the combined model was significant
        (F=4.62, p<0.01), but BA 45 necrosis alone was not an independent predictor
        (p=0.13), whereas BA 45 disconnection was significant (p=0.025).
      result_status: not_detected
      patient_measurement: regional_lesion_load
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis corresponds to the regression model for speech
            fluency involving BA 45 necrosis and disconnection described in P5-S1-C11
            and P5-S1-C12. The proposed core correctly identifies this specific model
            and outcome.
          source_ids:
          - P5-S1-C11
          - P5-S1-C12
        direction:
          answer: fits
          reason: The source explicitly states that 'necrosis alone was not an independent
            predictor of fluency' (P5-S1-C12) with a p-value of 0.13 (P5-S1-C11).
            The proposed core's direction of 'no_effect' accurately reflects this
            lack of independent statistical association for necrosis in the presence
            of disconnection.
          source_ids:
          - P5-S1-C11
          - P5-S1-C12
        construct:
          answer: fits
          reason: The exposure is correctly identified as BA 45 necrosis (regional
            lesion load measured via MRI), and the outcome is speech fluency (WAB
            subtest). The method is multiple linear regression. The patient measurement
            is regional_lesion_load, as the analysis uses the percentage of damage
            to BA 45, not the diffusion-derived connectivity metric itself as the
            primary exposure for this specific null finding.
          source_ids:
          - P4-S1-C7
          - P5-S1-C6
          - P5-S1-C11
        qualifications:
          answer: fits
          reason: The core correctly qualifies the null finding by stating it applies
            'When used in a model combined with BA 45 disconnection'. This is essential
            because the combined model was significant, and the null applies specifically
            to the independent contribution of necrosis in that context.
          source_ids:
          - P5-S1-C11
          - P5-S1-C12
        missing_material_caveat:
          answer: fits
          reason: The core includes the necessary qualification regarding the combined
            model. While the source mentions technical limitations of tractography
            (P6-S2-C3), these apply to the disconnection measure; the necrosis measure
            is based on standard MRI sequences. No material caveat changing the interpretation
            of the necrosis null is omitted.
          source_ids:
          - P5-S1-C12
          - P6-S2-C3
      optional_pending: []
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    normalizations: []
    analysis_identity:
      id: R005
      exposure:
        text: BA 45 necrosis
      outcome:
        text: speech fluency
      analysis_label: Sensitivity analysis for fluency
      relation: sensitivity
      evidence_ids:
      - P5-S1-C12
      qualifier_ids: []
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 7d4052892e7a83bbff8a6f1682333adc8cd42c22a71092dc583c8fea43d3f125
        source_review: _compare/relationships-2026-11-16/review-current/Bonilha2014
        source_status_sha256: 7857c271e5f46429259a8d9c9efecb0754d003f82cde1653d8c9d74b020f8c71
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P2-S2-C5:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 7d4052892e7a83bbff8a6f1682333adc8cd42c22a71092dc583c8fea43d3f125
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: cb0d2c8ae4e1991718d7c27ba5be50794493a04019aa3745cb467f98ea9af63d
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S2-C5
          page: 2
          text_layer_sha256: cb0d2c8ae4e1991718d7c27ba5be50794493a04019aa3745cb467f98ea9af63d
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "Methods\nSubjects\nWe studied thirty-nine individuals (mean\
          \ age 62.7 ±12.8 years, 22 male, 16 female) who \nsuffered a left hemisphere\
          \ ischemic stroke at least six months prior to enrolling in this study \n\
          (Table I in the Online Data Supplement)."
        anchor_text: "Methods\nSubjects\nWe studied thirty-nine individuals (mean\
          \ age 62.7 ±12.8 years, 22 male, 16 female) who \nsuffered a left hemisphere\
          \ ischemic stroke at least six months prior to enrolling in this study \n\
          (Table I in the Online Data Supplement)."
        excluded_fragments: []
        image_sha256: 965dce9ea2ccb037be609057af93a9225d616f60bc9cf58c57c4889bb88f5e39
        transcription: 'Methods


          Subjects


          We studied thirty-nine individuals (mean age 62.7 ±12.8 years, 22 male,
          16 female) who suffered a left hemisphere ischemic stroke at least six months
          prior to enrolling in this study (Table I in the Online Data Supplement)'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 5
  quote: "Finally, we also observed significant relationship between \nfluency and\
    \ a model composed by BA 45 necrosis and BA 45 disconnection F=4.62, \np<0.01;\
    \ necrosis: β=2.89; p=0.13; disconnection β=7.52; p=0.025)."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-20'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
