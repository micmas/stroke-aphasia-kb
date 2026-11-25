---
id: ci_aphasia_therapy
name: Constraint-Induced (CI) Aphasia Therapy
kind: therapy
findings:
- id: f1
  target_audit:
    status: behaviour_label_present
    category: behaviour_or_language_construct
    original_target: everyday_communication_amount
    reason: Label names a behaviour or language construct; its exact operational definition and measurement
      still need source review.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  outcome_measurement:
    status: needs_source_review
    instruments: []
    note: Outcome instrument/task is not yet verified for this finding. Do not infer it from the predictor
      or a paper-wide test list.
  target: everyday_communication_amount
  target_kind: prognosis
  claim: Patients receiving CI aphasia therapy reported a significant increase in
    the amount of communication in everyday life, whereas those receiving conventional
    aphasia therapy did not show improvement in this measure.
  direction: likely
  relationship: treatment_response
  method: clinical_RCT
  sample:
    n: 17
    population: Monolingual native German speakers with chronic aphasia following
      a single ischemic stroke affecting the left middle cerebral artery territory.
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
  - Single study with a small sample size
  - Unable to determine which specific feature of the CI approach (e.g., massed practice
    vs. constraints) contributed most to the success
  evidence_quality: RCT
  strength: weak
  notes: 'Exposure measurement: Intensive practice of speech acts over a short period
    (3 hours per weekday for 2 weeks) using therapeutic language games that constrain
    non-verbal communication and force the use of difficult verbal utterances through
    shaping and reinforcement. The CI group received 3 hours of therapy per weekday
    over 2 weeks; The conventional therapy group received the same total amount of
    treatment hours but spread over 4 weeks. Additional metadata has not been transcribed;
    review the pending-field flags before approval. PDF image reading (P2-S1-C5, two-model
    agreement, human verification pending): In the present study, subjects with chronic
    aphasia con-

    sequent to stroke who previously had participated in extensive

    conventional speech therapy and had reached an apparent

    maximum in recovery of language function received CI

    aphasia therapy for 3 hours each weekday over a 2-week

    period Original text-layer quotation is preserved below. PDF image reading (P2-S1-C7,
    two-model agreement, human verification pending): Subjects and Methods

    A total of 17 patients suffering from aphasia were treated Original text-layer
    quotation is preserved below.'
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
    - proposed_concept:everyday_communication_amount
  therapy:
    id: ci_aphasia_therapy
    name: Constraint-Induced Aphasia Therapy
  citation: '@Pulvermuller2001'
  source_passages:
  - section: Original source P4-S1-C8
    page: 4
    quote: 'Consistent with this result, the CAL revealed that the CI

      therapy patients’ performance in everyday life situations also

      improved.'
    supports: claim
  - section: Original source P4-S1-C9
    page: 4
    quote: 'These patients reported a significant increase of 30%

      in the amount of communication in everyday life after treatment

      (F[1,7]525.0, P,0.001; average, 30.1 versus 39.2 points).'
    supports: claim
  - section: Original source P4-S1-C10
    page: 4
    quote: 'Control patients who participated in conventional aphasia ther-

      apy did not show an improvement in this measure (F,1).'
    supports: claim
  - section: Original source P2-S1-C5
    page: 2
    quote: 'In the present study, subjects with chronic aphasia conse-

      quent to stroke who previously had participated in extensive

      conventional speech therapy and had reached an apparent

      maximum in recovery of language function received CI

      aphasia therapy for 3 hours each weekday over a 2-week

      period.'
    supports: method
  - section: Original source P2-S1-C7
    page: 2
    quote: 'Subjects and Methods

      A total of 17 patients suffering from aphasia were treated.'
    supports: sample
  - section: Original source P2-S1-C8
    page: 2
    quote: 'Patients

      presented with language impairment due to a single stroke affecting

      the territory of the left middle cerebral artery.'
    supports: sample
  - section: Original source P3-S2-C8
    page: 3
    quote: 'In

      addition, a questionnaire, the Communicative Activity Log (CAL),

      was developed to ascertain patient use of verbal language in

      everyday life (see Appendix).'
    supports: method
  - section: Original source P4-S2-C4
    page: 4
    quote: 'That significant language

      improvements were obtained over such a short period of time

      in patients with chronic aphasia (average, 8.3 years after

      onset) is noteworthy.'
    supports: sample
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-25'
relationship_review:
  paper: Pulvermuller2001
  proposal_id: R007
  review_status_sha256: c9e77892865911bd5f87e0922c97382448aeff098669dfff7e724996d896b151
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 57cb79977ebd854e7ff73befdaf436deea54bd2bb862229464b0aa9c0a41b375
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 57cb79977ebd854e7ff73befdaf436deea54bd2bb862229464b0aa9c0a41b375
        A/passages.json: b7906ce8db6773835b9d31e44d8b94aa54f0f729a712e26844d79083a21f77d9
        A/raw.json: a8d065ef0fb64462f47075e6e03a1fd77cf59460c46e6b461547b33971efd832
        A/source-units.json: 5a92dcc12680db4022c9291f6708cff408a0b2d1d67fed8ac1678eb8f3b9b661
        A/full-source-units.json: 4eb4aa734b22f711e1be4cee4b9e977da16f7a93c00e12e2203ab8e54d2420ce
        A/meta.json: 2b1cd397d545068a463a27d0a307b8f023c4453dba997f55e550685628f0806a
        A/table-images/manifest.json: dd2657b12c64a3d80cb9dcc7015f194679bfffb4a3eb35ebaf7a0710dc972c37
        A/clauses/window-03/raw.json: a35592f9f7ce93948afcbf9edf21c73630605458674010ac0ebb5d5377d6d66d
        A/clauses/window-03/prompt.txt: 8795c7e7b6c8bf5bd5442fecae4b7bd14d2bb65ac242e7f07634c6c03a6c354d
        A/clauses/window-03/meta.json: bb2e56a3929cd0af857ab0ba6f81151871503791ee516f9198e0f85e481721bf
        A/clauses/window-04/raw.json: d5adb0bf69096dff98167eb03f3f188be3d7270aff95b1a367688188a8322964
        A/clauses/window-04/prompt.txt: 8b21f72347e516d53d5b42671c7d765e62d81da84407e34296aeb6e5aa564ad6
        A/clauses/window-04/meta.json: 3f355d1865fbbdac620d4c04c4fb21a3bfc0ee3c6e7f2e7cfb4aeaa6ff330cd5
        A/clauses/window-05/raw.json: 134b380723cc8ee0e3df32fd7a53059f2c5268f0dc67fbec508ffa8fb2bc6b77
        A/clauses/window-05/prompt.txt: 0bae46ebf715f497b9c262ee750cf198809082e6f3cb17ce62db7b1a0d1d5641
        A/clauses/window-05/meta.json: d2a4771f8f03a50963a54d2dd29c5f2b2817bc1c48f019621c7a686f9c544664
        A/clauses/window-02/raw.json: a469bb5ddd1d74644d91941f386a2f118cdeaeccee7ad4b2ac7f8300c5a720a9
        A/clauses/window-02/prompt.txt: 4d3ef27ee93fc27d4c792be1fcb8f4d871fb5766509b9f92cf5286daeef5e14f
        A/clauses/window-02/meta.json: 375353bb7878bbea57725d6226127978315a5523c42c0ee8e52decc262f64ee1
        A/clauses/window-01/raw.json: 174dc08d8ff0a083726f478c752432b77eb2e94597c83060596b526f2c0b1520
        A/clauses/window-01/prompt.txt: 8d4fbef8630f47ac3be8a87a5d1da86d88dea3439253f0f76e0cb1871af3cc71
        A/clauses/window-01/meta.json: 9c6cf95ff27d89c01c60f36e8e5f5981d6d241621933054469e118008786e543
        A/clauses/window-06/raw.json: 33677d9d84f1afac5e9f5288c154a2f4d8f28fed040048ca8f46dcd364a46755
        A/clauses/window-06/prompt.txt: 00dfa17b0c9091458c24d8a2a8a28f69fe7a6f9507fc9d5a48c89cb7d889bf6f
        A/clauses/window-06/meta.json: 087cdb33eebd52b8f5bba9cfe472d75c0f9b096ae666b4fffa138e66cd72066d
        B/passages.json: b7906ce8db6773835b9d31e44d8b94aa54f0f729a712e26844d79083a21f77d9
        B/raw.json: 5423d07ddbc5b63c339d273aac3c8a124bab0edbadcfa124f203c80c71bcae44
        B/source-units.json: 5a92dcc12680db4022c9291f6708cff408a0b2d1d67fed8ac1678eb8f3b9b661
        B/full-source-units.json: 4eb4aa734b22f711e1be4cee4b9e977da16f7a93c00e12e2203ab8e54d2420ce
        B/meta.json: 1161ca6d8e2efa107adbaf1a8242294bc96bae7b0ce982437c0b7161c1ae6f48
        B/table-images/manifest.json: dd2657b12c64a3d80cb9dcc7015f194679bfffb4a3eb35ebaf7a0710dc972c37
        B/clauses/window-03/raw.json: b12bf951031725621aa43d5de300d8e65512a1be6f038204697e3a76e220d8d3
        B/clauses/window-03/prompt.txt: 8795c7e7b6c8bf5bd5442fecae4b7bd14d2bb65ac242e7f07634c6c03a6c354d
        B/clauses/window-03/meta.json: 046f00f5edac27add19970d4edf01311b96af586ccba45f5a812bb21f0e21524
        B/clauses/window-04/raw.json: b9a7514a81bea10a86ef116896fc168275cc12c6a61ee335005971b8a0dab53a
        B/clauses/window-04/prompt.txt: 8b21f72347e516d53d5b42671c7d765e62d81da84407e34296aeb6e5aa564ad6
        B/clauses/window-04/meta.json: 2973c91d9eeff11ea33daf73b6bbcaa09a33ee6231ad806cb9ebc4ba29d562fb
        B/clauses/window-05/raw.json: 07258fd84be2b2c64928a500664f3cb914d1eed6a95ee0d416bfdf2765cc2d12
        B/clauses/window-05/prompt.txt: 0bae46ebf715f497b9c262ee750cf198809082e6f3cb17ce62db7b1a0d1d5641
        B/clauses/window-05/meta.json: fe04f577df94672a812523203b03a348aa857b4135bcec5b76eaaee2d0a8c6b0
        B/clauses/window-02/raw.json: 5f32916825681dbaa427863fe54993bd29c98e9c293b8fd5b4444330822a5f18
        B/clauses/window-02/prompt.txt: 4d3ef27ee93fc27d4c792be1fcb8f4d871fb5766509b9f92cf5286daeef5e14f
        B/clauses/window-02/meta.json: 7b725443a18dcc5afb81b477a6b31d151ad04be70f01139ccbd82b858fadbc13
        B/clauses/window-01/raw.json: 10185b3b821c4f13f216df09f326f84a443d28c830312a13c058520a08e76d78
        B/clauses/window-01/prompt.txt: 8d4fbef8630f47ac3be8a87a5d1da86d88dea3439253f0f76e0cb1871af3cc71
        B/clauses/window-01/meta.json: 85acffa8a85297fc2b4413e64e4983f3b17889a0f2409f617979040165f6ae7e
        B/clauses/window-06/raw.json: 6b9e595d7044fc2fff80df050f8d9b3c69ce8b44c36f1c728867a74a8d613f02
        B/clauses/window-06/prompt.txt: 00dfa17b0c9091458c24d8a2a8a28f69fe7a6f9507fc9d5a48c89cb7d889bf6f
        B/clauses/window-06/meta.json: 861840b4d1cf3cf14a1ee5a607f7a54e8bf2944a58b7010ac95a744e6d7aa23e
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
      pdf_sha256: 57cb79977ebd854e7ff73befdaf436deea54bd2bb862229464b0aa9c0a41b375
      source_review: _compare/relationships-2026-11-16/review-current/Pulvermuller2001
      source_status_sha256: 0efed064dbf176b5a05ffaba2d857437e9b069330b5f4e67076a7f691ee1454f
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R007
    exposure:
      text: CI aphasia therapy
    outcome:
      text: amount of communication in everyday life (CAL)
    analysis_label: Everyday communication amount (Self-rating)
    relation: treatment_effect
    evidence_ids:
    - P4-S1-C8
    - P4-S1-C9
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
      pdf_sha256: 57cb79977ebd854e7ff73befdaf436deea54bd2bb862229464b0aa9c0a41b375
      source_review: _compare/relationships-2026-11-16/review-current/Pulvermuller2001
      source_status_sha256: 0efed064dbf176b5a05ffaba2d857437e9b069330b5f4e67076a7f691ee1454f
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Accounting without a linked unit P1-S1-C1
      - Accounting without a linked unit P1-S1-C5
      - Accounting without a linked unit P1-S1-C7
      - Accounting without a linked unit P1-S2-C1
      - Accounting without a linked unit P1-S2-C3
      - Accounting without a linked unit P1-S2-C4
      - Accounting without a linked unit P1-S2-C5
      - Unaccounted source passage P1-S1-C1
      - Unaccounted source passage P1-S2-C5
      - Unaccounted source passage P1-S2-C4
      - Unaccounted source passage P1-S2-C3
      - Unaccounted source passage P1-S1-C7
      - Unaccounted source passage P1-S1-C5
      - Unaccounted source passage P1-S2-C1
      - Result passage disposed without unit P2-S3-C14
      - Result passage disposed without unit P2-S3-C4
      - Result passage disposed without unit P2-S3-C7
      - Result passage disposed without unit P2-S3-C8
      - Result passage disposed without unit P2-S4-C2
      - Result passage disposed without unit P2-S4-C3
      - Result passage disposed without unit P3-S2-C15
      - Accounting without a linked unit P4-S1-C2
      - Accounting without a linked unit P4-S1-C3
      - Accounting without a linked unit P4-S1-C4
      - Accounting without a linked unit P4-S1-C5
      - Accounting without a linked unit P4-S1-C7
      - Accounting without a linked unit P4-S1-C8
      - Accounting without a linked unit P4-S1-C9
      - Unaccounted source passage P4-S1-C3
      - Unaccounted source passage P4-S1-C9
      - Unaccounted source passage P4-S1-C5
      - Unaccounted source passage P4-S1-C4
      - Unaccounted source passage P4-S1-C8
      - Unaccounted source passage P4-S1-C7
      - Unaccounted source passage P4-S1-C2
      - Accounting without a linked unit P4-S1-C11
      - Accounting without a linked unit P4-S1-C12
      - Accounting without a linked unit P4-S1-C13
      - Accounting without a linked unit P4-S1-C14
      - Accounting without a linked unit P4-S2-C3
      - Accounting without a linked unit P4-S2-C8
      - Unaccounted source passage P4-S1-C13
      - Unaccounted source passage P4-S1-C11
      - Unaccounted source passage P4-S2-C8
      - Unaccounted source passage P4-S1-C14
      - Unaccounted source passage P4-S1-C12
      - Unaccounted source passage P4-S2-C3
      - Accounting without a linked unit P4-S2-C10
      - Accounting without a linked unit P4-S2-C11
      - Accounting without a linked unit P4-S3-C10
      - Accounting without a linked unit P4-S3-C2
      - Unaccounted source passage P4-S2-C10
      - Unaccounted source passage P4-S2-C11
      - Unaccounted source passage P4-S3-C2
      - Unaccounted source passage P4-S3-C10
      - Accounting without a linked unit P5-S3-C7
      - Unaccounted source passage P5-S3-C7
      unattached_null_or_qualifier_ids:
      - P2-S3-C4
      - P2-S3-C14
      - P3-S2-C15
      - P4-S1-C2
      - P4-S1-C3
      - P4-S1-C5
      - P4-S1-C14
      - P4-S2-C11
      suppressed_nonrepresented_units: 2
      default_disposition_count_requires_completeness_check: 132
      unselected_timing_passages:
      - P1-S1-C1
      - P1-S1-C3
      - P2-S1-C5
      - P2-S1-C6
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P4-S1-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S1-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S1-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S1-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S1-C12
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S3-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      empty_frame_slots_require_confirmation:
      - imaging_provenance
      - imaging_timing
      - validation
      - analysis_restrictions
      - personal_factors
      - tested_personal_effects
      - adjustment_roles
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required: []
      unlinked_tables: []
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units: []
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 57cb79977ebd854e7ff73befdaf436deea54bd2bb862229464b0aa9c0a41b375
      source_review: _compare/relationships-2026-11-16/review-current/Pulvermuller2001
      source_status_sha256: 0efed064dbf176b5a05ffaba2d857437e9b069330b5f4e67076a7f691ee1454f
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C4
      disposition: repeated
      result_indexes:
      - 0
      - 1
      - 6
      - 7
      reason: Abstract restatement of results
    - source_id: P1-S1-C5
      disposition: repeated
      result_indexes:
      - 3
      - 4
      - 8
      reason: Abstract restatement of control group results
    - source_id: P2-S3-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes baseline demographic differences between groups
    - source_id: P2-S3-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes baseline aphasia severity
    - source_id: P2-S3-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes baseline aphasia syndromes
    - source_id: P2-S3-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes total therapy hours administered
    - source_id: P2-S4-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes total amount of therapy
    - source_id: P2-S4-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes therapy frequency and hours per day
    - source_id: P3-S2-C15
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of overall score interaction
    - source_id: P4-S1-C1
      disposition: represented
      result_indexes:
      - 0
      reason: Establishes significant interaction of group and time for overall scores
    - source_id: P4-S1-C2
      disposition: represented
      result_indexes:
      - 0
      reason: Establishes substantial improvement for CI group vs no significant improvement
        for conventional group
    - source_id: P4-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Refers to a figure showing interaction and means
    - source_id: P4-S1-C4
      disposition: represented
      result_indexes:
      - 1
      - 2
      reason: Specifies improvements in Token, naming, and comprehension tests, and
        lack thereof in repetition test
    - source_id: P4-S1-C5
      disposition: represented
      result_indexes:
      - 3
      reason: Specifies conventional therapy group improved on only one test
    - source_id: P4-S1-C7
      disposition: represented
      result_indexes:
      - 4
      - 5
      reason: Provides cumulative change percentages for both groups
    - source_id: P4-S1-C8
      disposition: represented
      result_indexes:
      - 6
      reason: Links CAL results to CI therapy improvement
    - source_id: P4-S1-C9
      disposition: represented
      result_indexes:
      - 6
      reason: Provides quantitative increase in amount of communication for CI group
    - source_id: P4-S1-C10
      disposition: represented
      result_indexes:
      - 7
      reason: States no improvement in amount of communication for control group
    - source_id: P4-S1-C11
      disposition: represented
      result_indexes:
      - 8
      reason: Confirms CI group improvement via blinded clinicians' ratings
    - source_id: P4-S1-C12
      disposition: represented
      result_indexes:
      - 8
      reason: Provides quantitative improvement from blinded clinicians' ratings
    - source_id: P4-S1-C13
      disposition: represented
      result_indexes:
      - 8
      reason: States increase occurred for each subject in clinicians' ratings
    - source_id: P4-S1-C14
      disposition: repeated
      result_indexes:
      - 0
      - 1
      - 6
      - 8
      reason: Summary statement of 6 of 8 measures showing improvement
    - source_id: P4-S2-C3
      disposition: repeated
      result_indexes:
      - 0
      - 6
      reason: Discussion restatement of substantial improvement
    - source_id: P4-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison of therapy hours to prior studies
    - source_id: P4-S2-C8
      disposition: repeated
      result_indexes:
      - 3
      reason: Discussion restatement of naming test improvement in control group
    - source_id: P4-S2-C9
      disposition: repeated
      result_indexes:
      - 0
      - 3
      reason: Discussion restatement of global improvements in CI vs conventional
    - source_id: P4-S2-C10
      disposition: repeated
      result_indexes:
      - 0
      - 1
      - 6
      - 8
      reason: Discussion restatement of 6 of 8 measures
    - source_id: P4-S2-C11
      disposition: repeated
      result_indexes:
      - 6
      - 7
      reason: Discussion restatement of everyday communication results
    - source_id: P4-S3-C2
      disposition: repeated
      result_indexes:
      - 7
      reason: Discussion restatement of lack of transfer in conventional group
    - source_id: P4-S3-C10
      disposition: represented
      result_indexes:
      - 0
      reason: Establishes significant improvement in overall language profile for
        CI group vs control
    - source_id: P5-S3-C7
      disposition: repeated
      result_indexes:
      - 0
      - 6
      reason: Conclusion restatement of efficiency and better outcome of CI therapy
    unresolved_coverage: []
    pending_source_ids:
    - P1-S1-C4
    - P1-S1-C5
    - P2-S3-C4
    - P2-S3-C7
    - P2-S3-C8
    - P2-S3-C14
    - P2-S4-C2
    - P2-S4-C3
    - P3-S2-C15
    - P4-S1-C3
    - P4-S1-C14
    - P4-S2-C3
    - P4-S2-C7
    - P4-S2-C8
    - P4-S2-C9
    - P4-S2-C10
    - P4-S2-C11
    - P4-S3-C2
    - P5-S3-C7
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
      - P2-S2-C10
      recruited_sample:
      - P2-S1-C7
      eligibility:
      - P2-S2-C3
      - P2-S2-C4
      - P2-S2-C6
      - P2-S2-C7
      imaging_provenance: []
      imaging_timing: []
      outcome_timing:
      - P3-S1-C8
      outcome_definition:
      - P3-S1-C9
      - P3-S2-C8
      - P3-S2-C9
      validation: []
      analysis_restrictions: []
      dependent_variable_statement:
      - P3-S2-C11
      - P3-S2-C13
      - P3-S2-C14
      limitations:
      - P4-S3-C7
      - P4-S3-C8
      - P5-S2-C10
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles: []
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P2-S3-C3
      - P2-S3-C4
      - P2-S3-C7
      - P2-S3-C8
      - P3-S3-C1
    outcome_type: both_reported
    imaging_vs_outcome: not_stated
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P4-S1-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S1-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S1-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S1-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S1-C12
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S3-C10
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
      pdf_sha256: 57cb79977ebd854e7ff73befdaf436deea54bd2bb862229464b0aa9c0a41b375
      review_sha256: c9e77892865911bd5f87e0922c97382448aeff098669dfff7e724996d896b151
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
      - P4-S1-C8
      - P4-S1-C9
      source_result: The CI aphasia therapy group reported a significant increase
        in the amount of communication in everyday life (CAL) after treatment (F[1,7]=25.0,
        P<0.001; average 30.1 vs 39.2 points), whereas the control group receiving
        conventional therapy did not show improvement in this measure.
      result_status: detected
      patient_measurement: non_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis corresponds to the CAL self-rating results
            for the CI group versus the control group, as described in P4-S1-C8 and
            P4-S1-C9. The proposed core correctly identifies this specific outcome
            and comparison.
          source_ids:
          - P4-S1-C8
          - P4-S1-C9
          - P4-S1-C10
        direction:
          answer: fits
          reason: The source explicitly states a significant increase for the CI group
            and no improvement for the control group. The proposed claim preserves
            this direction (improvement in CI, no improvement in control).
          source_ids:
          - P4-S1-C8
          - P4-S1-C9
          - P4-S1-C10
        construct:
          answer: fits
          reason: The exposure is CI aphasia therapy, the outcome is amount of communication
            in everyday life, and the measurement is the Communicative Activity Log
            (CAL). The source confirms the CAL was used to ascertain patient use of
            verbal language in everyday life (P3-S2-C8, P3-S2-C9). The patient measurement
            is non-imaging (questionnaire), not diffusion or lesion overlap.
          source_ids:
          - P3-S2-C8
          - P3-S2-C9
          - P4-S1-C8
          - P4-S1-C9
        qualifications:
          answer: fits
          reason: The proposed core includes qualifications regarding the therapy
            duration and intensity (3 hours/weekday for 2 weeks vs conventional spread
            over 4 weeks), which aligns with the source descriptions of the treatment
            protocols (P1-S1-C3, P2-S1-C5, P2-S1-C6).
          source_ids:
          - P1-S1-C3
          - P2-S1-C5
          - P2-S1-C6
        missing_material_caveat:
          answer: fits
          reason: The proposed core includes limitations regarding the single study
            nature and inability to isolate specific CI features, which are supported
            by P4-S3-C7, P4-S3-C8, and P5-S2-C10. No material caveats changing the
            interpretation of the CAL result are omitted.
          source_ids:
          - P4-S3-C7
          - P4-S3-C8
          - P5-S2-C10
      optional_pending:
      - sample.time_post_onset
      - statistics.CI_group_F_value
      - statistics.CI_group_P_value
      - statistics.CI_group_mean_change
      - statistics.control_group_result
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
    - sample.time_post_onset
    - statistics.CI_group_F_value
    - statistics.CI_group_P_value
    - statistics.CI_group_mean_change
    - statistics.control_group_result
    normalizations:
    - field: sample.time_post_onset
      original: Measured immediately before and 1 day after a 10-day treatment interval;
        patients had an average of 8.3 years since stroke onset.
      action: not_transcribed
      reason: 'Numbers not grounded in usable selected source readings: 1E+1'
    analysis_identity:
      id: R007
      exposure:
        text: CI aphasia therapy
      outcome:
        text: amount of communication in everyday life (CAL)
      analysis_label: Everyday communication amount (Self-rating)
      relation: treatment_effect
      evidence_ids:
      - P4-S1-C8
      - P4-S1-C9
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
        pdf_sha256: 57cb79977ebd854e7ff73befdaf436deea54bd2bb862229464b0aa9c0a41b375
        source_review: _compare/relationships-2026-11-16/review-current/Pulvermuller2001
        source_status_sha256: 0efed064dbf176b5a05ffaba2d857437e9b069330b5f4e67076a7f691ee1454f
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P2-S1-C5:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 57cb79977ebd854e7ff73befdaf436deea54bd2bb862229464b0aa9c0a41b375
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 14c833fc75b11d7f9ad9c07223af47528d961752d47bbb3c67ff93baf4983f33
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S1-C5
          page: 2
          text_layer_sha256: 14c833fc75b11d7f9ad9c07223af47528d961752d47bbb3c67ff93baf4983f33
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'In the present study, subjects with chronic aphasia conse-

          quent to stroke who previously had participated in extensive

          conventional speech therapy and had reached an apparent

          maximum in recovery of language function received CI

          aphasia therapy for 3 hours each weekday over a 2-week

          period.'
        anchor_text: 'In the present study, subjects with chronic aphasia conse-

          quent to stroke who previously had participated in extensive

          conventional speech therapy and had reached an apparent

          maximum in recovery of language function received CI

          aphasia therapy for 3 hours each weekday over a 2-week

          period.'
        excluded_fragments: []
        image_sha256: f6e0ffec75c3f4f179e7d7490e880614f53e3957a2c9192f889a59301c2e5bef
        transcription: 'In the present study, subjects with chronic aphasia con-

          sequent to stroke who previously had participated in extensive

          conventional speech therapy and had reached an apparent

          maximum in recovery of language function received CI

          aphasia therapy for 3 hours each weekday over a 2-week

          period'
      P2-S1-C7:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 57cb79977ebd854e7ff73befdaf436deea54bd2bb862229464b0aa9c0a41b375
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 0a28c30f5dad82e2dbd29263801a31128925ed7d1e0fda61b9fe845d49bafa42
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S1-C7
          page: 2
          text_layer_sha256: 0a28c30f5dad82e2dbd29263801a31128925ed7d1e0fda61b9fe845d49bafa42
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Subjects and Methods

          A total of 17 patients suffering from aphasia were treated.'
        anchor_text: 'Subjects and Methods

          A total of 17 patients suffering from aphasia were treated.'
        excluded_fragments: []
        image_sha256: a5eefb31f81633479abc931c3f2af7760d87209ba97a7185fb3e2e80e3c7c3f1
        transcription: 'Subjects and Methods

          A total of 17 patients suffering from aphasia were treated'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 4
  quote: 'Consistent with this result, the CAL revealed that the CI

    therapy patients’ performance in everyday life situations also

    improved.'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-25'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
