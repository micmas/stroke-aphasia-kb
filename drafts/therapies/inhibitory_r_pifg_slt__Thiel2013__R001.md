---
id: inhibitory_r_pifg_slt
name: inhibitory 1 Hz rTMS over right pIFG combined with SLT
kind: therapy
findings:
- id: f1
  target: global_aat_score_change
  target_kind: prognosis
  claim: Aphasia recovery, measured as absolute change in global Aachen Aphasia Test
    (AAT) score, was significantly higher in the rTMS group compared to the sham group.
  direction: likely
  relationship: treatment_response
  method: clinical_RCT
  sample:
    n: 24
    population: Right-handed patients with first ischemic infarct within the left
      middle cerebral artery territory and subacute poststroke aphasia.
    phase: not_reported
    time_post_onset: Not transcribed; confirm from the original PDF population and
      timing passages.
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Small sample size (proof-of-principle study)
  - Underpowered to detect interactions between treatment and specific aphasia types,
    infarct size, or infarct location
  evidence_quality: RCT
  strength: weak
  notes: 'Exposure measurement: A 10-day protocol consisting of 20-minute inhibitory
    1 Hz rTMS over the triangular part of the right posterior inferior frontal gyrus
    (at 90% of individual resting motor threshold), followed immediately by 45 minutes
    of deficit-specific speech and language therapy (SLT). The strongest increase
    was observed in the naming subtest; A trend toward higher average change was observed
    in comprehension, writing, and token test. Additional metadata has not been transcribed;
    review the pending-field flags before approval. PDF image reading (P2-S1-C2, two-model
    agreement, human verification pending): Methods


    A total of 30 patients with first ischemic infarct within the left middle cerebral
    artery territory were recruited at the rehabilitation hospital RehaNova in Cologne,
    Germany Original text-layer quotation is preserved below. PDF image reading (P2-S1-C8,
    two-model agreement, human verification pending): . From the total of 30 patients,
    15 were

    consented and randomized to the sham group and 15 to the treat-

    ment group Original text-layer quotation is preserved below. PDF image reading
    (P2-S1-C10, two-model agreement, human verification pending): . Of these, 4 were
    randomized to

    the sham group and 2 to the TMS group, thus yielding a total of 24

    patients with 11 subjects assigned to the sham and 13 to the TMS

    group (Table 1) Original text-layer quotation is preserved below.'
  imaging_details:
    reference_space: not_reported
    atlases_used: []
  lesion_mapping: {}
  provenance:
    extracted_by: model:gemma4:31b
    extracted_on: '2026-11-25'
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
    - not_transcribed:sample.time_post_onset
    - proposed_concept:global_aat_score_change
  therapy:
    id: inhibitory_r_pifg_slt
    name: inhibitory 1 Hz rTMS over right pIFG combined with SLT
  citation: '@Thiel2013'
  source_passages:
  - section: Original source P1-S2-C2
    page: 1
    quote: "Methods—Twenty-four patients with subacute poststroke aphasia were randomized\
      \ to a 10-day protocol of 20-minute \ninhibitory 1 Hz rTMS over the right triangular\
      \ part of the posterior inferior frontal gyrus or sham stimulation, followed\
      \ \nby 45 minutes of speech and language therapy."
    supports: method
  - section: Original source P2-S1-C2
    page: 2
    quote: 'Methods

      A total of 30 patients with first ischemic infarct within the left mid-

      dle cerebral artery territory were recruited at the rehabilitation hos-

      pital RehaNova in Cologne, Germany.'
    supports: sample
  - section: Original source P2-S1-C8
    page: 2
    quote: "From the total of 30 patients, 15 were \nconsented and randomized to the\
      \ sham group and 15 to the treat-\nment group."
    supports: sample
  - section: Original source P2-S1-C10
    page: 2
    quote: "Of these, 4 were randomized to \nthe sham group and 2 to the TMS group,\
      \ thus yielding a total of 24 \npatients with 11 subjects assigned to the sham\
      \ and 13 to the TMS \ngroup (Table 1)."
    supports: sample
  - section: Original source P2-S2-C8
    page: 2
    quote: "After randomization, patients either received 20 minutes of inhibi-\n\
      tory 1 Hz rTMS with an intensity of 90% of the daily-defined indi-\nvidual resting\
      \ motor threshold over the triangular part of the right \nposterior inferior\
      \ frontal gyrus (treatment group)14 or over the midline \nat the vertex (sham\
      \ group) using a Magstim Rapid2 stimulator with a \ndouble 70-mm coil."
    supports: method
  - section: Original source P2-S2-C11
    page: 2
    quote: "Patients in both groups received 45 minutes of deficit-specific \naphasia\
      \ therapy focused on the individual linguistic symptoms by a \nblinded certified\
      \ therapist."
    supports: method
  - section: Original source P2-S4-C5
    page: 2
    quote: "Average treatment onset time was 5.4 weeks (TMS group) and \n7.2 weeks\
      \ (sham group), with 50% of subjects in each group \nstarting between 24 and\
      \ 59 days (interquartile range)."
    supports: sample
  - section: Original source P2-S4-C12
    page: 2
    quote: "Aphasia recovery measured as absolute change in global \nAAT score was\
      \ significantly higher in the TMS group (mean \n23.6±SD 12.15) than in the sham\
      \ group (mean 7.55±SD \n11.00; P=0.003; Figure 1A; Table 2)."
    supports: claim
  - section: Original source P4-S1-C7
    page: 4
    quote: "Our study, based on these pathophysiological consider-\nations, demonstrated\
      \ a highly significant treatment effect: \nthe intervention group experienced\
      \ a significantly larger \nimprovement in the global AAT score than the sham\
      \ group \n(Figure 1A)."
    supports: claim
  - section: Original source P5-S1-C6
    page: 5
    quote: "A formal statistical analysis did not indicate an \ninfluence of aphasia\
      \ type on recovery; however, the study was \nunderpowered to detect a specific\
      \ aphasia type and treatment \ninteraction, so larger studies are needed to\
      \ specifically address \nthis question."
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-25'
relationship_review:
  paper: Thiel2013
  proposal_id: R001
  review_status_sha256: 16aac3c96ae6a99eb04a4ea9182254b76978089a831fdcdca8c51986e7029257
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: d2b19385a834c6473946693ead6093e429d1854bc63e127583eda76f4625d4e5
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: d2b19385a834c6473946693ead6093e429d1854bc63e127583eda76f4625d4e5
        A/passages.json: 28a907ecf72dde130eb329c8bfa9159e2bcdb27d0c2a70d74259ac99c034d09e
        A/raw.json: 976a423763c2a29c65bf468abdad55a2e2ecfda3914ea074f3d989b32703b043
        A/source-units.json: ce9a7166866dfca9f00079eab79d9b3aaa33127f10cc24de373a0162487cc14a
        A/full-source-units.json: 77d053ba463bffe170ff35b14f9141c1cbe82f584e64abf0add7d8597b5b1ad9
        A/meta.json: 55905141824505aa43c2ec7e2e0e4e09e5ef11463e71665893231338e5553292
        A/table-images/page-5.png: e4ec4fcc846e51e654052cc80c8b062e65adb34e1842c66dc5cd738bb75a94f2
        A/table-images/manifest.json: 2985b5033f0d2231af7ffb92ace7ceba20033400a70bc37b660fa5bf2f41ef4c
        A/table-images/TABLE-2-page-5-1.png: 505c9e3b7fded78d3bdcb73d0d0151f149b6e420a6ea7ceb59b19e804e5a27c9
        A/clauses/window-03/raw.json: 16f6f032768208ad1bf6ba853a7894b18ea4c829693a281b01545578ee2bb687
        A/clauses/window-03/prompt.txt: 9835f0e48afbb934dd1882d904d423822a66bca376e4bf642e28fa015ccf478a
        A/clauses/window-03/meta.json: cf6b87a7716bf0de47ed2b3ed9ab59c4285b832ef5027c2ec7f1f4d8d6ca3d6f
        A/clauses/window-04/raw.json: 94f6e930cfe249ae88bad5979246b4a7c768e22c36cff1719e92311f286a2530
        A/clauses/window-04/prompt.txt: 26ac5fa734b7dfe45d3b9a3e226832df8f912c63e618be1ec9e1d448f5a3ab33
        A/clauses/window-04/meta.json: ba28f5c319982d9f7b2f6958d7e11ef58170035ba1db0367c7e8818f9cd3efd8
        A/clauses/window-02/raw.json: 84eb3357e3e9a1c294d718e7eea0869eac7d1514774b5447e06310c4988de5c4
        A/clauses/window-02/prompt.txt: 36e490c9bf955d8ff7d28445b1366037171ec5ee82db4785fb6381b978fbd0c6
        A/clauses/window-02/meta.json: 5de661a27c7cc074467c9cced619a3be755f86367202f3de5dde92ca8cddafdc
        A/clauses/window-01/raw.json: 2bda8aa440c6401266dea0c8e7e58c37e1907dd6986b4bb7cefc3cebbba4d95d
        A/clauses/window-01/prompt.txt: fdc10ee6f6ed95172df1975f1e9d75eaa120e60ea065f5bab3562cd57968b97b
        A/clauses/window-01/meta.json: 268a3c5d543c05c241e1fc170a8d7b5ca47328ffb64aff254436df3047a339c1
        A/tables/TABLE-2-page-5-1/raw.json: 8dbb010214f9fe5ec30768080e929d617ab999179f147f91120405598f924645
        A/tables/TABLE-2-page-5-1/prompt.txt: fde0eb0205dcab69c0308163e6dd25d6509e8d242d2ec55a7f0da348d46f9e9c
        A/tables/TABLE-2-page-5-1/meta.json: a4fe120a8d9d6057a9092f2eb4295e38db9715d560bab23f294c3224e29e6462
        B/passages.json: 28a907ecf72dde130eb329c8bfa9159e2bcdb27d0c2a70d74259ac99c034d09e
        B/raw.json: bb6d4560ed9de607ff6c4f93de4c966385de725af4cb110b3e0e2da4eb4ac1c7
        B/source-units.json: ce9a7166866dfca9f00079eab79d9b3aaa33127f10cc24de373a0162487cc14a
        B/full-source-units.json: 77d053ba463bffe170ff35b14f9141c1cbe82f584e64abf0add7d8597b5b1ad9
        B/meta.json: d6ab9c8e64f0fab7b29b830a4c97d2d500fe9153f1eb520357de4fa032578d53
        B/table-images/page-5.png: e4ec4fcc846e51e654052cc80c8b062e65adb34e1842c66dc5cd738bb75a94f2
        B/table-images/manifest.json: c420f00364f013636e3b36d0b70f2e043ab4167db4c55b9d00ec6c8f99c41310
        B/table-images/TABLE-2-page-5-1.png: 505c9e3b7fded78d3bdcb73d0d0151f149b6e420a6ea7ceb59b19e804e5a27c9
        B/clauses/window-03/raw.json: bae1de072b8329327449babd9e73d71376ddde979badd692d450cb6b8366442c
        B/clauses/window-03/prompt.txt: 9835f0e48afbb934dd1882d904d423822a66bca376e4bf642e28fa015ccf478a
        B/clauses/window-03/meta.json: e7e800bbc06cfa7b2cb6c8f5a38c4f8a309e0ff0d8be4443301266c46c60b86b
        B/clauses/window-04/raw.json: 1aab3edce0165c9066e2d437f722415d56a1086bd543b111e1bf16e4ef8418b5
        B/clauses/window-04/prompt.txt: 26ac5fa734b7dfe45d3b9a3e226832df8f912c63e618be1ec9e1d448f5a3ab33
        B/clauses/window-04/meta.json: 59a3cbb0f8cfee8ed96458b9e0a4fc7623f2e7f5e11ae55b299f4abc35d192ad
        B/clauses/window-02/raw.json: 8425cd66727c63c61c4f63b0b1ef20452918795005240f33c005843d1335bf4b
        B/clauses/window-02/prompt.txt: 36e490c9bf955d8ff7d28445b1366037171ec5ee82db4785fb6381b978fbd0c6
        B/clauses/window-02/meta.json: c83e69c784e416bf974faf4d2057d6674cb64016a75ae261da5465498637cd82
        B/clauses/window-01/raw.json: ffa3442be98217167b9d27ab0662040f7dc4e03d57657196479bf558aab231e5
        B/clauses/window-01/prompt.txt: fdc10ee6f6ed95172df1975f1e9d75eaa120e60ea065f5bab3562cd57968b97b
        B/clauses/window-01/meta.json: c77e7a55e86ec3d121eabe0d0ab4c6f8f5fbe6fd0339bca1a33692cff0abf430
        B/tables/TABLE-2-page-5-1/raw.json: 64042160a8e9d4e40add765bea4822087d7c66bbd822c918c96f011f52d05173
        B/tables/TABLE-2-page-5-1/prompt.txt: fde0eb0205dcab69c0308163e6dd25d6509e8d242d2ec55a7f0da348d46f9e9c
        B/tables/TABLE-2-page-5-1/meta.json: 6ab92da6ddad9801bf34c6549fca8cefd0bbf47b77082024a97fc0a71a2e7eb6
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
      pdf_sha256: d2b19385a834c6473946693ead6093e429d1854bc63e127583eda76f4625d4e5
      source_review: _compare/relationships-2026-11-16/review-current/Thiel2013
      source_status_sha256: 9b9b094cc2d11de3e48fc2d282e6fe7a7e094b816512578659b591d43ac0b9bb
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R001
    exposure:
      text: inhibitory 1 Hz rTMS over the right posterior inferior frontal gyrus combined
        with speech and language therapy
    outcome:
      text: global Aachen Aphasia Test (AAT) score change
    analysis_label: Primary clinical outcome analysis
    relation: treatment_effect
    evidence_ids:
    - P1-S2-C5
    - P2-S4-C12
    - P4-S1-C7
    - P4-S2-C4
    - P5-S2-C5
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
      pdf_sha256: d2b19385a834c6473946693ead6093e429d1854bc63e127583eda76f4625d4e5
      source_review: _compare/relationships-2026-11-16/review-current/Thiel2013
      source_status_sha256: 9b9b094cc2d11de3e48fc2d282e6fe7a7e094b816512578659b591d43ac0b9bb
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P2-S3-C8
      - Result passage disposed without unit P2-S4-C10
      - Result passage disposed without unit P2-S4-C11
      - Result passage disposed without unit P2-S4-C6
      - Result passage disposed without unit P2-S4-C7
      - Result passage disposed without unit P2-S4-C8
      - Result passage disposed without unit P2-S4-C9
      - Result passage disposed without unit P4-S2-C3
      - Unresolved source passage P4-S2-C3
      - Result passage disposed without unit P5-S1-C1
      - Result passage disposed without unit P5-S1-C8
      - Result passage disposed without unit P6-S1-C1
      unattached_null_or_qualifier_ids:
      - P2-S4-C8
      - P5-S1-C1
      suppressed_nonrepresented_units: 4
      default_disposition_count_requires_completeness_check: 69
      unselected_timing_passages:
      - P2-S4-C5
      - P6-S1-C5
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P1-S2-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P1-S2-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P3-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P3-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S2-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      empty_frame_slots_require_confirmation:
      - validation
      - analysis_restrictions
      - personal_factors
      - tested_personal_effects
      - adjustment_roles
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-2-page-5-1
      unlinked_tables: []
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P2-S3
        - P2-S4
        - P3-S1
        - P4-S1
        - P4-S2
        - P5-S1
        - P5-S2
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: d2b19385a834c6473946693ead6093e429d1854bc63e127583eda76f4625d4e5
      source_review: _compare/relationships-2026-11-16/review-current/Thiel2013
      source_status_sha256: 9b9b094cc2d11de3e48fc2d282e6fe7a7e094b816512578659b591d43ac0b9bb
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S2-C5
      disposition: represented
      result_indexes:
      - 0
      reason: Reports significant higher global AAT score change in rTMS group.
    - source_id: P1-S2-C6
      disposition: represented
      result_indexes:
      - 1
      reason: Reports subtest naming and trends for others.
    - source_id: P1-S2-C7
      disposition: represented
      result_indexes:
      - 2
      reason: Reports proportional increase in left hemisphere voxels (AVI) for rTMS
        group.
    - source_id: P1-S2-C8
      disposition: represented
      result_indexes:
      - 3
      reason: Reports linear relationship between AVI change and global AAT change.
    - source_id: P1-S2-C9
      disposition: repeated
      result_indexes:
      - 0
      - 2
      reason: Conclusion restating primary clinical and imaging results.
    - source_id: P2-S3-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes normality and independence tests.
    - source_id: P2-S4-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes distribution of aphasia types.
    - source_id: P2-S4-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes lack of between-group difference in baseline variables.
    - source_id: P2-S4-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes ceiling effects.
    - source_id: P2-S4-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports absence of serious adverse events.
    - source_id: P2-S4-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports absence of reported side effects.
    - source_id: P2-S4-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports no decline in language function in TMS group.
    - source_id: P2-S4-C12
      disposition: represented
      result_indexes:
      - 0
      reason: Reports significant higher global AAT change in TMS group.
    - source_id: P2-S4-C13
      disposition: represented
      result_indexes:
      - 1
      reason: Reports overall treatment effect in subtest analysis.
    - source_id: P2-S4-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports no significant interaction between treatment and subtest.
    - source_id: P2-S4-C15
      disposition: represented
      result_indexes:
      - 1
      reason: Reports higher mean increase in all subtests for TMS group.
    - source_id: P2-S4-C16
      disposition: represented
      result_indexes:
      - 1
      reason: Reports highest increase for naming and trends for others.
    - source_id: P3-S1-C1
      disposition: represented
      result_indexes:
      - 1
      reason: Reports naming significance and trends for comprehension, writing, token
        test.
    - source_id: P3-S1-C2
      disposition: represented
      result_indexes:
      - 4
      reason: Reports no differential treatment effect for different aphasia types.
    - source_id: P3-S1-C3
      disposition: represented
      result_indexes:
      - 2
      reason: Reports significantly larger AVI changes in treatment group.
    - source_id: P3-S1-C6
      disposition: represented
      result_indexes:
      - 3
      reason: Reports linear correlation between AVI change and global AAT change.
    - source_id: P3-S1-C9
      disposition: repeated
      result_indexes:
      - 0
      - 2
      reason: Discussion restatement of clinical and imaging results.
    - source_id: P4-S1-C7
      disposition: repeated
      result_indexes:
      - 0
      reason: Discussion restatement of global AAT improvement.
    - source_id: P4-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Restates lack of interaction between treatment and subtest.
    - source_id: P4-S1-C9
      disposition: repeated
      result_indexes:
      - 1
      reason: Restates strongest increase in naming.
    - source_id: P4-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to Figure 1.
    - source_id: P4-S2-C4
      disposition: repeated
      result_indexes:
      - 0
      reason: Figure 1A caption restating global AAT result.
    - source_id: P4-S2-C5
      disposition: repeated
      result_indexes:
      - 1
      reason: Figure 1B caption restating subtest results.
    - source_id: P4-S2-C6
      disposition: represented
      result_indexes:
      - 1
      reason: Reports no effect on word repetition.
    - source_id: P4-S2-C10
      disposition: repeated
      result_indexes:
      - 2
      reason: Figure 2A caption restating AVI change result.
    - source_id: P4-S2-C11
      disposition: repeated
      result_indexes:
      - 3
      reason: Figure 2B caption restating AVI/AAT correlation.
    - source_id: P5-S1-C1
      disposition: repeated
      result_indexes:
      - 1
      reason: Discussion restatement of subtest trends.
    - source_id: P5-S1-C6
      disposition: represented
      result_indexes:
      - 4
      reason: Reports no influence of aphasia type on recovery.
    - source_id: P5-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discusses limitations regarding infarct size/location.
    - source_id: P5-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes baseline matching of infarct size.
    - source_id: P5-S2-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes baseline AV maps comparison.
    - source_id: P5-S2-C2
      disposition: repeated
      result_indexes:
      - 2
      reason: Discussion restatement of network shift to left hemisphere.
    - source_id: P5-S2-C4
      disposition: repeated
      result_indexes:
      - 3
      reason: Discussion restatement of AVI explaining variability.
    - source_id: P5-S2-C5
      disposition: represented
      result_indexes:
      - 0
      - 1
      - 2
      - 3
      - 4
      reason: Table 2 provides statistical values for global AAT, subtests, AVI, and
        aphasia type analysis.
    - source_id: P6-S1-C1
      disposition: repeated
      result_indexes:
      - 3
      reason: Restates AVI explains ~25% of variability.
    - source_id: P6-S1-C8
      disposition: repeated
      result_indexes:
      - 2
      reason: Restates positive average AVI posttreatment in rTMS group.
    - source_id: P6-S1-C9
      disposition: repeated
      result_indexes:
      - 0
      - 2
      reason: Conclusion restating clinical and imaging results.
    unresolved_coverage:
    - source_id: P4-S2-C4
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P4-S2-C5
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P4-S2-C6
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P5-S2-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P5-S2-C5
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    pending_source_ids:
    - P1-S2-C9
    - P2-S3-C8
    - P2-S4-C6
    - P2-S4-C7
    - P2-S4-C8
    - P2-S4-C9
    - P2-S4-C10
    - P2-S4-C11
    - P2-S4-C14
    - P3-S1-C9
    - P4-S1-C8
    - P4-S1-C9
    - P4-S2-C3
    - P5-S1-C1
    - P5-S1-C7
    - P5-S1-C8
    - P6-S1-C8
    - P6-S1-C9
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-2-page-5-1
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P2-S1-C10
      recruited_sample:
      - P2-S1-C2
      eligibility:
      - P2-S1-C4
      - P2-S1-C5
      imaging_provenance:
      - P2-S2-C2
      - P2-S3-C5
      imaging_timing:
      - P2-S2-C2
      outcome_timing:
      - P2-S3-C3
      outcome_definition:
      - P2-S3-C3
      - P2-S3-C4
      validation: []
      analysis_restrictions: []
      dependent_variable_statement:
      - P2-S3-C3
      - P2-S3-C4
      - P2-S3-C9
      - P2-S3-C10
      limitations:
      - P5-S1-C6
      - P5-S1-C7
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles: []
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P2-S1-C4
      - P2-S4-C3
      - P3-S2-C5
    outcome_type: both_reported
    imaging_vs_outcome: mixed
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P1-S2-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P1-S2-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P3-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P3-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S2-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
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
      pdf_sha256: d2b19385a834c6473946693ead6093e429d1854bc63e127583eda76f4625d4e5
      review_sha256: 16aac3c96ae6a99eb04a4ea9182254b76978089a831fdcdca8c51986e7029257
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
      - P1-S2-C5
      - P2-S4-C12
      - P4-S1-C7
      source_result: The primary outcome, global Aachen Aphasia Test (AAT) score change,
        was significantly higher in the rTMS group compared to the sham group (P=0.003).
        This indicates a detected treatment effect of inhibitory 1 Hz rTMS over the
        right posterior inferior frontal gyrus combined with speech and language therapy
        on aphasia recovery in subacute stroke patients.
      result_status: detected
      patient_measurement: non_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: 'The selected analysis corresponds to the primary clinical outcome
            analysis described in the source: a comparison of global AAT score change
            between the rTMS and sham groups using a t-test for independent samples.
            The source explicitly identifies this as the primary outcome measure.'
          source_ids:
          - P1-S2-C5
          - P2-S3-C3
          - P2-S3-C9
          - P2-S4-C12
        direction:
          answer: fits
          reason: The source states that the global AAT score change was 'significantly
            higher' in the rTMS group. The proposed core claim states that recovery
            was 'significantly higher' in the rTMS group. The direction of the effect
            (improvement/favorable outcome) is preserved.
          source_ids:
          - P1-S2-C5
          - P2-S4-C12
          - P4-S1-C7
        construct:
          answer: fits
          reason: The exposure is correctly identified as inhibitory 1 Hz rTMS over
            the right posterior inferior frontal gyrus combined with SLT. The outcome
            is correctly identified as global AAT score change. The patient measurement
            is non-imaging (clinical test), distinct from the imaging measures (PET/AVI)
            also reported in the paper. The population (subacute ischemic stroke,
            left MCA territory) and timing (subacute) are consistent with the source.
          source_ids:
          - P1-S2-C2
          - P2-S1-C2
          - P2-S2-C8
          - P2-S3-C3
        qualifications:
          answer: fits
          reason: The proposed core includes qualifications regarding subtest performance
            (naming strongest, trends in others) and limitations (small sample, underpowered
            for interactions). These are supported by the source text (P2-S4-C16,
            P3-S1-C1, P5-S1-C6). The core does not incorrectly claim these are the
            primary findings but lists them as qualifications/limitations.
          source_ids:
          - P2-S4-C16
          - P3-S1-C1
          - P5-S1-C6
        missing_material_caveat:
          answer: fits
          reason: The core captures the main result and key limitations. The 'proof-of-principle'
            nature and small sample size are noted. The lack of a significant interaction
            between treatment and subtest is noted. No material caveat that changes
            the interpretation of the primary result (that rTMS+SLT improved global
            AAT scores more than sham+SLT) is omitted.
          source_ids:
          - P1-S2-C9
          - P5-S1-C6
          - P6-S1-C10
      optional_pending:
      - 'sample.time_post_onset: Source P2-S4-C5 has an unresolved image-reading disagreement
        regarding the exact average treatment onset time (5.4 vs 7.2 weeks or other
        values). The core marks this as not transcribed, which is appropriate given
        the conflict.'
      - 'detailed_statistics: Specific mean/SD values and P-values are not transcribed
        in the core, which is acceptable for a qualitative draft.'
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - 'sample.time_post_onset: source confirmation required; original proposed wording
      remains in the audit.'
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - 'sample.time_post_onset: Source P2-S4-C5 has an unresolved image-reading disagreement
      regarding the exact average treatment onset time (5.4 vs 7.2 weeks or other
      values). The core marks this as not transcribed, which is appropriate given
      the conflict.'
    - 'detailed_statistics: Specific mean/SD values and P-values are not transcribed
      in the core, which is acceptable for a qualitative draft.'
    normalizations:
    - field: sample.time_post_onset
      original: Treatment onset average was 5.4 weeks (TMS group) and 7.2 weeks (sham
        group) post-stroke; assessment was post-treatment.
      action: not_transcribed
      reason: 'Numbers not grounded in usable selected source readings: 5.4, 7.2'
    analysis_identity:
      id: R001
      exposure:
        text: inhibitory 1 Hz rTMS over the right posterior inferior frontal gyrus
          combined with speech and language therapy
      outcome:
        text: global Aachen Aphasia Test (AAT) score change
      analysis_label: Primary clinical outcome analysis
      relation: treatment_effect
      evidence_ids:
      - P1-S2-C5
      - P2-S4-C12
      - P4-S1-C7
      - P4-S2-C4
      - P5-S2-C5
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
        pdf_sha256: d2b19385a834c6473946693ead6093e429d1854bc63e127583eda76f4625d4e5
        source_review: _compare/relationships-2026-11-16/review-current/Thiel2013
        source_status_sha256: 9b9b094cc2d11de3e48fc2d282e6fe7a7e094b816512578659b591d43ac0b9bb
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P2-S1-C2:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: d2b19385a834c6473946693ead6093e429d1854bc63e127583eda76f4625d4e5
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 14e655d884c4daa33a3350ba4e809f4d3219b7289030ab3d73f89734a9bdc62c
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S1-C2
          page: 2
          text_layer_sha256: 14e655d884c4daa33a3350ba4e809f4d3219b7289030ab3d73f89734a9bdc62c
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Methods

          A total of 30 patients with first ischemic infarct within the left mid-

          dle cerebral artery territory were recruited at the rehabilitation hos-

          pital RehaNova in Cologne, Germany.'
        anchor_text: 'Methods

          A total of 30 patients with first ischemic infarct within the left mid-

          dle cerebral artery territory were recruited at the rehabilitation hos-

          pital RehaNova in Cologne, Germany.'
        excluded_fragments: []
        image_sha256: 7c7d1510c57aa643cb4de116535cc13266772911003797411a6bccd32cb67171
        transcription: 'Methods


          A total of 30 patients with first ischemic infarct within the left middle
          cerebral artery territory were recruited at the rehabilitation hospital
          RehaNova in Cologne, Germany'
      P2-S1-C8:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: d2b19385a834c6473946693ead6093e429d1854bc63e127583eda76f4625d4e5
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 063952eaa9f8f976a50d3ed41f399dbcf45307f7f450572ab3136f71f11995a9
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S1-C8
          page: 2
          text_layer_sha256: 063952eaa9f8f976a50d3ed41f399dbcf45307f7f450572ab3136f71f11995a9
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "From the total of 30 patients, 15 were \nconsented and randomized\
          \ to the sham group and 15 to the treat-\nment group."
        anchor_text: "From the total of 30 patients, 15 were \nconsented and randomized\
          \ to the sham group and 15 to the treat-\nment group."
        excluded_fragments: []
        image_sha256: b0c30bd7eb3d5b724bc0fbaf2b028dc1347d53629973047e146128d7e9b0841f
        transcription: '. From the total of 30 patients, 15 were

          consented and randomized to the sham group and 15 to the treat-

          ment group'
      P2-S1-C10:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: d2b19385a834c6473946693ead6093e429d1854bc63e127583eda76f4625d4e5
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 70f091d954bc5bdbf28384fadb2738e0db02a54e8797138af776a0eefa35d01a
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S1-C10
          page: 2
          text_layer_sha256: 70f091d954bc5bdbf28384fadb2738e0db02a54e8797138af776a0eefa35d01a
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "Of these, 4 were randomized to \nthe sham group and 2 to the\
          \ TMS group, thus yielding a total of 24 \npatients with 11 subjects assigned\
          \ to the sham and 13 to the TMS \ngroup (Table 1)."
        anchor_text: "Of these, 4 were randomized to \nthe sham group and 2 to the\
          \ TMS group, thus yielding a total of 24 \npatients with 11 subjects assigned\
          \ to the sham and 13 to the TMS \ngroup (Table 1)."
        excluded_fragments: []
        image_sha256: 605fce0ea9b217e9aa20d7c831797962ceb68f41810670efdd21e129b54b1cc9
        transcription: '. Of these, 4 were randomized to

          the sham group and 2 to the TMS group, thus yielding a total of 24

          patients with 11 subjects assigned to the sham and 13 to the TMS

          group (Table 1)'
      P2-S4-C5:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: d2b19385a834c6473946693ead6093e429d1854bc63e127583eda76f4625d4e5
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 76e3accfa06392874a87a01a927aba574e653c928016674df82b7488aeb76a3b
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S4-C5
          page: 2
          text_layer_sha256: 76e3accfa06392874a87a01a927aba574e653c928016674df82b7488aeb76a3b
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: "Average treatment onset time was 5.4 weeks (TMS group) and\
          \ \n7.2 weeks (sham group), with 50% of subjects in each group \nstarting\
          \ between 24 and 59 days (interquartile range)."
        anchor_text: "Average treatment onset time was 5.4 weeks (TMS group) and \n\
          7.2 weeks (sham group), with 50% of subjects in each group \nstarting between\
          \ 24 and 59 days (interquartile range)."
        excluded_fragments: []
        image_sha256: ccbb04242d6c34d1fe925c8e32b8b692e35544a9ca1b06e05cf324364a40e481
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 1
  quote: "Methods—Twenty-four patients with subacute poststroke aphasia were randomized\
    \ to a 10-day protocol of 20-minute \ninhibitory 1 Hz rTMS over the right triangular\
    \ part of the posterior inferior frontal gyrus or sham stimulation, followed \n\
    by 45 minutes of speech and language therapy."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-25'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
