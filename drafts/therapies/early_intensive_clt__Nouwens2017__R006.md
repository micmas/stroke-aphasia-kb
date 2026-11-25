---
id: early_intensive_clt
name: Early intensive cognitive-linguistic treatment
kind: therapy
findings:
- id: f1
  target_audit:
    status: construct_separated
    category: behaviour_or_language_construct
    original_target: cat_word_comprehension
    reason: Separated the construct from the score/task using the published claim and linked source passages.
      This is metadata correction, not scientific approval.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  outcome_measurement:
    status: identified
    instruments:
    - name: Comprehensive Aphasia Test
    metric: Word comprehension subtest; modality requires verification
    note: Task conditions, covariates, change metric and timing remain in the claim and source passages.
      Instrument version/subtests require final source verification.
  target: word_comprehension
  target_kind: impairment
  claim: In an on-treatment analysis, patients who received at least the specified
    intensity of 28 h of treatment in 4 weeks reached significantly higher scores
    on CAT word comprehension than those in the control group who received no treatment
    during the first 4 weeks.
  direction: likely
  relationship: treatment_response
  method: clinical_RCT
  sample:
    n: not_reported
    population: Stroke patients with first-ever aphasia
    phase: not_reported
    time_post_onset: 4 weeks after randomisation
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - On-treatment analysis results should be interpreted with caution as they only
    include patients who could tolerate the intensive regime
  evidence_quality: RCT
  strength: weak
  notes: 'Exposure measurement: 4 weeks of early intensive cognitive-linguistic treatment
    (at least 1 h/day) initiated within 2 weeks of stroke onset. Finding is based
    on on-treatment analysis (intervention group: n=23 who achieved >=28h intensity;
    control group: n=62 who received no treatment); Adjusted for age, sex, education,
    baseline aphasia severity, stroke type, stroke location, and baseline Barthel
    Index. Additional metadata has not been transcribed; review the pending-field
    flags before approval. PDF image reading (P1-S1-C5, two-model agreement, human
    verification pending): Methods and patients: Stroke patients with first-ever aphasia
    were randomised within 2 weeks of onset to either 4 weeks of early intensive cognitive-linguistic
    treatment (1 h/day) or no language treatment Original text-layer quotation is
    preserved below.'
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
    - not_transcribed:sample.n
    - proposed_concept:cat_word_comprehension
  therapy:
    id: early_intensive_clt
    name: Early intensive cognitive-linguistic treatment
  citation: '@Nouwens2017'
  source_passages:
  - section: Original source P4-S3-C1
    page: 4
    quote: 'come ANELT-A (adjusted diﬀerence ¼ 5.41, 95% CI:

      [1.52 to 9.31], p ¼ 0.007); SAT verbal (adjusted diﬀer-

      ence ¼ 3.57, 95% CI: [0.36 to 6.78], p ¼ 0.030) and CAT

      word comprehension (adjusted diﬀerence ¼ 3.64, 95%

      CI: [0.58 to 6.69], p ¼ 0.020) (Figure 3, online Table

      6).'
    supports: claim
  - section: Original source P4-S2-C13
    page: 4
    quote: 'On-treatment analysis

      In the on-treatment analysis, we included all patients of

      the intervention-group who received at least the prespe-

      ciﬁed intensity of 28 h in 4 weeks (n ¼ 23, 29%) and all

      subjects in the control-group who did not receive any

      treatment (n ¼ 62, 86%).'
    supports: sample
  - section: Original source P4-S1-C2
    page: 4
    quote: 'We used

      linear regression to analyse the treatment eﬀect as a

      mean diﬀerence in ANELT-A scores between the inter-

      vention and control-group 4 weeks after randomisa-

      tion, adjusted for age (years), sex, education (high or

      low), baseline aphasia severity (ASRS-score), type of

      stroke (ischaemic or haemorrhagic), location of stroke

      (right or left hemisphere) and baseline Barthel Index

      score.'
    supports: method
  - section: Original source P9-S1-C4
    page: 9
    quote: 'However, this ﬁnding should be inter-

      preted with great caution, as on-treatment analyses

      could only be performed in patients in the interven-

      tion-group who could tolerate intensive treatment,

      whereas the control-group comprised both patients

      who may and may not tolerate this intensive regime.'
    supports: limitation
  - section: Original source P1-S1-C5
    page: 1
    quote: 'Methods and patients: Stroke patients with first-ever aphasia were randomised
      within 2 weeks of onset to either 4

      weeks of early intensive cognitive-linguistic treatment (1 h/day) or no language
      treatment.'
    supports: method
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-25'
relationship_review:
  paper: Nouwens2017
  proposal_id: R006
  review_status_sha256: a0bb61823b0a5abd0449870c3ab2658b45196addadd7f466c4100725258225fb
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: a5d4e2d6027e4815bcfa24420c514aff33ab702ce1cb431a7b4519cf2f1f7dd9
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: a5d4e2d6027e4815bcfa24420c514aff33ab702ce1cb431a7b4519cf2f1f7dd9
        A/passages.json: c51c1d42b62e25a03cbd784dec10a43f9bf9f0328fc966b6c549348b4731446c
        A/raw.json: f55db65ecf3c1cd5600c8f81805e484e8cfa42a524cd677516b79a62368bbf42
        A/source-units.json: 9fcc3c26a29de15f040ce058c92875502968f48a5c57ae4044aabbb1f8cbcb7e
        A/full-source-units.json: 92c31da89ed525ac038cf7c42a8d54875ed725324b5120a8ac554dab0a60d530
        A/meta.json: 467542d56c88645835d3272cd2bb4e9612551ae79cfd3adf30434e22e58ec574
        A/table-images/TABLE-1-page-2-1.png: cb8ba742c58d8c96f0e0bd5bb68337f3cc45eb3fd2efde163878c3085cc3bf72
        A/table-images/page-2.png: 2785ab906559512efaf020d616215a587f8c2be3d230849e089571674a11871f
        A/table-images/page-5.png: 4b087dad1a68ecc99a35aaa440510dfb36826aeb79e2dc1c8afd99758624959a
        A/table-images/manifest.json: 9aedc6e1b8e076d87aa217fea9a115a51c4fd8727c44f006fd893d5d5082a29f
        A/table-images/TABLE-2-page-5-1.png: 4b0a1d0102ba4b8f3b515a3adc6bf424c44b24a16c5d851121105fb8127520f7
        A/clauses/window-03/raw.json: 74b9f582bf737b6d1a876f93a9b6c6c84f33226ba43b7baeed92fbc1ff491194
        A/clauses/window-03/prompt.txt: ac93c30787a7196b96b7fe8a6ef36c67f4bab56bd317a7042e70eb52bcdd8d1d
        A/clauses/window-03/meta.json: 26fd7cf108daa170fa790792a0c638f906d2111a5f67fd23ed1a3e1af547068a
        A/clauses/window-04/raw.json: eecdcae6a7bb6e27f7f8192df6e0c82cea01b6d224abe5446b32c9f1260ff1f0
        A/clauses/window-04/prompt.txt: bf40400d1688b937e60d414d77e50706242fec389a89e31723e22d891a4f666c
        A/clauses/window-04/meta.json: dbe8023a6642c3eefd1dcebed38a1b3e82197ae72e721c7bb7489f6bbd59e538
        A/clauses/window-05/raw.json: a7379072df386b5cfd5b725c738deae3ddea53a614001da38a3e4235e306a7a3
        A/clauses/window-05/prompt.txt: c178c8b3f27c885fa4f8fd453f3c3702b3f9eed569d5355fe84cf87b403c0322
        A/clauses/window-05/meta.json: 72f92aa0f5c263849be1c5a9a0a8b3c4e0c1e3a9ab3f16519616ed19ad6d101a
        A/clauses/window-02/raw.json: caf1550d93c4e57ba75def6ea8216c1ec873e8bc21f8f95c9e28bbbb5029ff4d
        A/clauses/window-02/prompt.txt: 20fbac5c05fa1406a3df6f6b96011d5432dc248b80350aa65e2803ebb2451576
        A/clauses/window-02/meta.json: 1e1542dc165f659af27fb1ba50439042630ef268af5ed17338071c15b18dd2d4
        A/clauses/window-01/raw.json: b0e87d97c5de0f46f10ddd7539e9f2f9827231492261a9036d16d57c74fe7de1
        A/clauses/window-01/prompt.txt: e8fcd05a31fb8d252bd64cadefdca44177d61cedfba42710bedd46c5ab5b66f3
        A/clauses/window-01/meta.json: d381ddaaaaa1a42e61e6c0063c8166bbda74fe0e84e01b6e6678eec46e430dcd
        A/clauses/window-06/raw.json: 33cad73a88548c66f18f0a2e83d7bc214caa1344ce9cc066504458e7c3c083ea
        A/clauses/window-06/prompt.txt: 52ceac908967363900483616b8a7924fd7cca6ab22b08414a1d29d565cf5743b
        A/clauses/window-06/meta.json: e6c7de35993604506fe557c306dfbaab03f796643d1d1c23d5cd2b47b403ab48
        A/tables/TABLE-2-page-5-2/raw.json: c9d8aae166c5605619fe0bb76c72738710841f35601c0d3187840666f5f9a4d4
        A/tables/TABLE-2-page-5-2/prompt.txt: f2add63c4c7a3604888a5b91f346ac31d6a3b6cd3b3e262a944954e7dcdfc4a3
        A/tables/TABLE-2-page-5-2/meta.json: e98e243e49abb27378b7d8699319495f1bbb28c9e86af321dda080235ca2a6f7
        A/tables/TABLE-1-page-2-1/raw.json: 53156bd438ac1edd5bf0c119b594909f37e01153ab3b327c82a26c204fe304c9
        A/tables/TABLE-1-page-2-1/prompt.txt: 60f1ceac234b57f26dce93d686e05c41512a809019019d9b967661d0f977d245
        A/tables/TABLE-1-page-2-1/meta.json: ec2394c45647472a407aa34d38f72e103d0eca1c3604e1279bfd88231924ea14
        B/passages.json: c51c1d42b62e25a03cbd784dec10a43f9bf9f0328fc966b6c549348b4731446c
        B/raw.json: 8c0eb2f0b140d73629dd813f682b8e4a7bd9b9aa71023c7420118f0f6f4a56bd
        B/source-units.json: 9fcc3c26a29de15f040ce058c92875502968f48a5c57ae4044aabbb1f8cbcb7e
        B/full-source-units.json: 92c31da89ed525ac038cf7c42a8d54875ed725324b5120a8ac554dab0a60d530
        B/meta.json: 7db30fa7289d226ce4f5e6a718261ea696d4401e70bb28cc3a8323770891be1f
        B/table-images/TABLE-1-page-2-1.png: cb8ba742c58d8c96f0e0bd5bb68337f3cc45eb3fd2efde163878c3085cc3bf72
        B/table-images/page-2.png: 2785ab906559512efaf020d616215a587f8c2be3d230849e089571674a11871f
        B/table-images/page-5.png: 4b087dad1a68ecc99a35aaa440510dfb36826aeb79e2dc1c8afd99758624959a
        B/table-images/manifest.json: a2d01849e6b2e60dbefeeabcc854496bf770c0d6776e67427681c077fa3d9dbf
        B/table-images/TABLE-2-page-5-1.png: 4b0a1d0102ba4b8f3b515a3adc6bf424c44b24a16c5d851121105fb8127520f7
        B/clauses/window-03/raw.json: c62ec2d7257e3503dfba0788e3be6b7d076fda9f02148a68d120b500869b5e36
        B/clauses/window-03/prompt.txt: ac93c30787a7196b96b7fe8a6ef36c67f4bab56bd317a7042e70eb52bcdd8d1d
        B/clauses/window-03/meta.json: 6341b9dfca8a49c723a39e2c7b1c5617a98f69772cb42a097007d4c8a03ba059
        B/clauses/window-04/raw.json: 30dea15524b93a6581c5450e10f9e5869f0153e05ce0fccae0d6df6e2196cb8f
        B/clauses/window-04/prompt.txt: bf40400d1688b937e60d414d77e50706242fec389a89e31723e22d891a4f666c
        B/clauses/window-04/meta.json: baa0f4915214e14fa8c4426e8768c7d25e4654c271a4d26226d27f077717b591
        B/clauses/window-05/raw.json: 5c80961e54f2e0889906483ae90676bdf7418ef875fc7b0997cf9c004f213f73
        B/clauses/window-05/prompt.txt: c178c8b3f27c885fa4f8fd453f3c3702b3f9eed569d5355fe84cf87b403c0322
        B/clauses/window-05/meta.json: 5569828cb48dc0055f2e3666833b76bb9a9348884da9aff9daf2599b3bf9181c
        B/clauses/window-02/raw.json: cfe6ee2ca58e37dae248bcbc7e1dd8467067b63dde4de5dd5e167a4e84a9f36e
        B/clauses/window-02/prompt.txt: 20fbac5c05fa1406a3df6f6b96011d5432dc248b80350aa65e2803ebb2451576
        B/clauses/window-02/meta.json: b5c4e9719145727e3776d6679f5ace3d71e4848dbb7885e6df1d4989ff6ac5b0
        B/clauses/window-01/raw.json: 386d964f160cb4331c53176e8152858ddabb3817a2817e771f97e502de725329
        B/clauses/window-01/prompt.txt: e8fcd05a31fb8d252bd64cadefdca44177d61cedfba42710bedd46c5ab5b66f3
        B/clauses/window-01/meta.json: cc6ad5d932b69fc9eac08fe64bb37371e1ac084b32cefe8ae2043c8a61631d6e
        B/clauses/window-06/raw.json: 76c963ce7890bf4753cd11240129e754db1e2b5ee138889b051ab4d5ec040ab8
        B/clauses/window-06/prompt.txt: 52ceac908967363900483616b8a7924fd7cca6ab22b08414a1d29d565cf5743b
        B/clauses/window-06/meta.json: 4c11365db402c4fe1d661f759eb2c609e66ecc8772b1b6ea942c428557cc4f6e
        B/tables/TABLE-2-page-5-2/raw.json: c9d8aae166c5605619fe0bb76c72738710841f35601c0d3187840666f5f9a4d4
        B/tables/TABLE-2-page-5-2/prompt.txt: f2add63c4c7a3604888a5b91f346ac31d6a3b6cd3b3e262a944954e7dcdfc4a3
        B/tables/TABLE-2-page-5-2/meta.json: aa06530911d086c16c97d7da01935e25ec63c23508864e1bcb23e7267bba3ba0
        B/tables/TABLE-1-page-2-1/raw.json: 402378ba2249704432a9db84b2f3af85acc68800c5933da7be04cbbe9fd33cf9
        B/tables/TABLE-1-page-2-1/prompt.txt: 60f1ceac234b57f26dce93d686e05c41512a809019019d9b967661d0f977d245
        B/tables/TABLE-1-page-2-1/meta.json: 3fec454cd37e20b76ec2cfcb0b4e809a9dbe03417072ca1a0dab88309466b631
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
      pdf_sha256: a5d4e2d6027e4815bcfa24420c514aff33ab702ce1cb431a7b4519cf2f1f7dd9
      source_review: _compare/relationships-2026-11-16/review-current/Nouwens2017
      source_status_sha256: f380a9c981612399f69598b33d551abc9344d7c68962ca698292e3958be59676
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R006
    exposure:
      text: 4 weeks of early intensive cognitive-linguistic treatment (CLT)
    outcome:
      text: CAT word comprehension score at 4 weeks
    analysis_label: On-treatment analysis
    relation: treatment_effect
    evidence_ids:
    - P4-S3-C1
    qualifier_ids:
    - P4-S2-C13
    - P4-S2-C15
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: a5d4e2d6027e4815bcfa24420c514aff33ab702ce1cb431a7b4519cf2f1f7dd9
      source_review: _compare/relationships-2026-11-16/review-current/Nouwens2017
      source_status_sha256: f380a9c981612399f69598b33d551abc9344d7c68962ca698292e3958be59676
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P1-S1-C11
      - 'window 1: invalid/duplicate disposition P1-S1-C5'
      - Result passage disposed without unit P4-S1-C10
      - Result passage disposed without unit P4-S1-C11
      - Result passage disposed without unit P4-S1-C12
      - Result passage disposed without unit P4-S1-C13
      - Result passage disposed without unit P4-S1-C9
      - Result passage disposed without unit P4-S2-C4
      - Result passage disposed without unit P4-S2-C5
      - Result passage disposed without unit P4-S2-C12
      - Result passage disposed without unit P4-S2-C14
      - Result passage disposed without unit P7-S1-C1
      - Result passage disposed without unit P8-S1-C2
      - Result passage disposed without unit P8-S1-C3
      - Result passage disposed without unit P8-S1-C4
      - Result passage disposed without unit P8-S1-C5
      - Result passage disposed without unit P9-S1-C1
      - Result passage disposed without unit P9-S2-C5
      - Result passage disposed without unit P9-S2-C7
      unattached_null_or_qualifier_ids:
      - P4-S1-C12
      suppressed_nonrepresented_units: 20
      default_disposition_count_requires_completeness_check: 122
      unselected_timing_passages:
      - P1-S1-C5
      - P2-S2-C5
      - P2-S2-C14
      - P4-S2-C13
      - P9-S1-C5
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P4-S2-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S2-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S2-C15
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      empty_frame_slots_require_confirmation:
      - imaging_provenance
      - imaging_timing
      - validation
      - analysis_restrictions
      - personal_factors
      - tested_personal_effects
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-2-1
      - TABLE-2-page-5-2
      unlinked_tables:
      - TABLE-1-page-2-1
      - TABLE-2-page-5-2
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P4-S1
        - P4-S2
        - P4-S3
        - P6-S1
        - P7-S1
        - P8-S1
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: a5d4e2d6027e4815bcfa24420c514aff33ab702ce1cb431a7b4519cf2f1f7dd9
      source_review: _compare/relationships-2026-11-16/review-current/Nouwens2017
      source_status_sha256: f380a9c981612399f69598b33d551abc9344d7c68962ca698292e3958be59676
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes patient allocation counts.
    - source_id: P1-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes median treatment intensity.
    - source_id: P1-S1-C12
      disposition: repeated
      result_indexes:
      - 0
      reason: Abstract restatement of primary adjusted difference.
    - source_id: P1-S1-C13
      disposition: repeated
      result_indexes:
      - 1
      reason: Abstract restatement of secondary outcomes.
    - source_id: P4-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes baseline clinical characteristics similarity.
    - source_id: P4-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports mortality during intervention period.
    - source_id: P4-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports mortality during follow-up.
    - source_id: P4-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes treatment non-compliance.
    - source_id: P4-S1-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes control group treatment refusal.
    - source_id: P4-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports compliance percentage.
    - source_id: P4-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports median treatment intensity.
    - source_id: P4-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports unadjusted mean scores.
    - source_id: P4-S2-C7
      disposition: represented
      result_indexes:
      - 7
      reason: Identifies prognostic factors in the regression model.
    - source_id: P4-S2-C8
      disposition: represented
      result_indexes:
      - 0
      reason: Reports adjusted mean difference for primary outcome.
    - source_id: P4-S2-C9
      disposition: represented
      result_indexes:
      - 1
      reason: Reports adjusted differences for secondary outcomes at 3 and 6 months.
    - source_id: P4-S2-C10
      disposition: represented
      result_indexes:
      - 2
      reason: Reports lack of significant effects on linguistic and functional outcomes.
    - source_id: P4-S2-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Refers to meta-analysis results in online appendix.
    - source_id: P4-S2-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes baseline characteristics of on-treatment cohort.
    - source_id: P4-S2-C15
      disposition: repeated
      result_indexes:
      - 3
      - 4
      - 5
      reason: Restatement of on-treatment results.
    - source_id: P4-S3-C1
      disposition: represented
      result_indexes:
      - 3
      - 4
      - 5
      reason: Reports significant on-treatment effects for ANELT-A, SAT, and CAT.
    - source_id: P4-S3-C2
      disposition: represented
      result_indexes:
      - 6
      reason: Reports on-treatment results for other measures/time-points.
    - source_id: P4-S3-C3
      disposition: repeated
      result_indexes:
      - 0
      reason: Discussion restatement of primary finding.
    - source_id: P6-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison to other studies.
    - source_id: P7-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Summary of meta-analysis evidence.
    - source_id: P8-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of treatment intensity challenges.
    - source_id: P8-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of compliance rates.
    - source_id: P8-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of patient-related issues.
    - source_id: P8-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of organizational problems.
    - source_id: P9-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of follow-up completeness.
    - source_id: P9-S1-C3
      disposition: repeated
      result_indexes:
      - 3
      - 4
      - 5
      reason: Discussion restatement of on-treatment effects.
    - source_id: P9-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports follow-up percentages.
    - source_id: P9-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of follow-up validity.
    - source_id: P9-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Clinical implication regarding delay of treatment.
    - source_id: P9-S2-C5
      disposition: repeated
      result_indexes:
      - 3
      - 4
      - 5
      reason: Discussion restatement of on-treatment results.
    - source_id: P9-S2-C7
      disposition: repeated
      result_indexes:
      - 0
      reason: Conclusion restatement of primary finding.
    unresolved_coverage: []
    pending_source_ids:
    - P1-S1-C10
    - P1-S1-C11
    - P1-S1-C12
    - P1-S1-C13
    - P4-S1-C9
    - P4-S1-C10
    - P4-S1-C11
    - P4-S1-C12
    - P4-S1-C13
    - P4-S2-C4
    - P4-S2-C5
    - P4-S2-C6
    - P4-S2-C12
    - P4-S2-C14
    - P4-S2-C15
    - P4-S3-C3
    - P6-S1-C3
    - P7-S1-C1
    - P8-S1-C2
    - P8-S1-C3
    - P8-S1-C4
    - P8-S1-C5
    - P9-S1-C1
    - P9-S1-C3
    - P9-S1-C5
    - P9-S1-C6
    - P9-S1-C8
    - P9-S2-C5
    - P9-S2-C7
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-2-1
    - TABLE-2-page-5-2
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P4-S1-C7
      - P4-S2-C13
      recruited_sample:
      - P1-S1-C10
      - P4-S1-C7
      eligibility:
      - P2-S2-C14
      imaging_provenance: []
      imaging_timing: []
      outcome_timing:
      - P1-S1-C7
      - P1-S1-C8
      - P3-S2-C5
      - P3-S2-C11
      - P4-S1-C3
      - P4-S2-C9
      - P4-S2-C15
      outcome_definition:
      - P3-S2-C8
      - P3-S2-C11
      validation: []
      analysis_restrictions: []
      dependent_variable_statement:
      - P4-S1-C2
      - P4-S1-C3
      limitations:
      - P8-S1-C2
      - P8-S1-C3
      - P8-S1-C4
      - P8-S1-C5
      - P9-S1-C4
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P4-S1-C2
      - P4-S1-C3
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P5-S1-C5
    outcome_type: status_at_assessment
    imaging_vs_outcome: not_stated
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P4-S2-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S2-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S2-C15
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
      pdf_sha256: a5d4e2d6027e4815bcfa24420c514aff33ab702ce1cb431a7b4519cf2f1f7dd9
      review_sha256: a0bb61823b0a5abd0449870c3ab2658b45196addadd7f466c4100725258225fb
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
      - P4-S3-C1
      source_result: 'In the on-treatment analysis, the intervention group (n=23,
        achieving >=28h intensity) reached significantly higher scores on CAT word
        comprehension than the control group (n=62, no treatment) at 4 weeks (adjusted
        difference = 3.64, 95% CI: [0.58 to 6.69], p = 0.020).'
      result_status: detected
      patient_measurement: non_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The draft correctly identifies the specific analysis as the 'on-treatment'
            analysis, distinct from the intention-to-treat analysis. It correctly
            specifies the outcome as CAT word comprehension at 4 weeks, matching the
            source P4-S3-C1.
          source_ids:
          - P4-S3-C1
          - P4-S2-C13
        direction:
          answer: fits
          reason: The draft states that the intervention group reached 'significantly
            higher scores', which aligns with the source reporting a positive adjusted
            difference (3.64) and p-value (0.020) indicating a significant benefit
            for the treatment group.
          source_ids:
          - P4-S3-C1
        construct:
          answer: fits
          reason: The exposure (4 weeks early intensive CLT) and outcome (CAT word
            comprehension) are correctly identified. The patient measurement is a
            linguistic test score (non-imaging), not a diffusion or lesion overlap
            metric. The draft correctly distinguishes this from the primary outcome
            (ANELT-A).
          source_ids:
          - P4-S3-C1
          - P3-S2-C6
        qualifications:
          answer: fits
          reason: The draft includes the critical qualification that this is an on-treatment
            analysis with specific sample sizes (n=23 vs n=62) and lists the adjustment
            covariates. It also includes the limitation regarding the interpretation
            of on-treatment analyses (selection bias/tolerance), which is present
            in P9-S1-C4.
          source_ids:
          - P4-S2-C13
          - P4-S1-C2
          - P9-S1-C4
        missing_material_caveat:
          answer: fits
          reason: The draft includes the necessary caveats about the on-treatment
            nature of the analysis and the specific sample composition. No material
            caveats regarding the specific CAT result are omitted.
          source_ids:
          - P9-S1-C4
          - P4-S2-C13
      optional_pending:
      - Exact sample sizes for the on-treatment analysis are transcribed in the draft
        (n=23, n=62) based on P4-S2-C13, but the main sample_n field is null as per
        the qualitative draft instruction not to require optional numbers unless central
        to the core relationship definition.
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Sample size requires source confirmation; it has not been transcribed.
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Exact sample sizes for the on-treatment analysis are transcribed in the draft
      (n=23, n=62) based on P4-S2-C13, but the main sample_n field is null as per
      the qualitative draft instruction not to require optional numbers unless central
      to the core relationship definition.
    normalizations:
    - field: sample.n
      original: 152
      action: not_transcribed
      reason: Not supported by selected quotations
    analysis_identity:
      id: R006
      exposure:
        text: 4 weeks of early intensive cognitive-linguistic treatment (CLT)
      outcome:
        text: CAT word comprehension score at 4 weeks
      analysis_label: On-treatment analysis
      relation: treatment_effect
      evidence_ids:
      - P4-S3-C1
      qualifier_ids:
      - P4-S2-C13
      - P4-S2-C15
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: a5d4e2d6027e4815bcfa24420c514aff33ab702ce1cb431a7b4519cf2f1f7dd9
        source_review: _compare/relationships-2026-11-16/review-current/Nouwens2017
        source_status_sha256: f380a9c981612399f69598b33d551abc9344d7c68962ca698292e3958be59676
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P4-S3-C1:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: a5d4e2d6027e4815bcfa24420c514aff33ab702ce1cb431a7b4519cf2f1f7dd9
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 65c077c82b2d4b6519f452b5777351edb1b08d0be608e1be81bda48f2264d509
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P4-S3-C1
          page: 4
          text_layer_sha256: 65c077c82b2d4b6519f452b5777351edb1b08d0be608e1be81bda48f2264d509
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: 'come ANELT-A (adjusted diﬀerence ¼ 5.41, 95% CI:

          [1.52 to 9.31], p ¼ 0.007); SAT verbal (adjusted diﬀer-

          ence ¼ 3.57, 95% CI: [0.36 to 6.78], p ¼ 0.030) and CAT

          word comprehension (adjusted diﬀerence ¼ 3.64, 95%

          CI: [0.58 to 6.69], p ¼ 0.020) (Figure 3, online Table

          6).'
        anchor_text: 'come ANELT-A (adjusted diﬀerence ¼ 5.41, 95% CI:

          [1.52 to 9.31], p ¼ 0.007); SAT verbal (adjusted diﬀer-

          ence ¼ 3.57, 95% CI: [0.36 to 6.78], p ¼ 0.030) and CAT

          word comprehension (adjusted diﬀerence ¼ 3.64, 95%

          CI: [0.58 to 6.69], p ¼ 0.020) (Figure 3, online Table

          6).'
        excluded_fragments: []
        image_sha256: 0ba29592ae66bed2e1f2c133be2876618cbc4d229cd48fd305b245a438216ae1
      P4-S2-C13:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: a5d4e2d6027e4815bcfa24420c514aff33ab702ce1cb431a7b4519cf2f1f7dd9
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 25254ab1135b12f8bf2dab26ea1c3890698adeca3eba8fa6cb8d833f681744a9
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P4-S2-C13
          page: 4
          text_layer_sha256: 25254ab1135b12f8bf2dab26ea1c3890698adeca3eba8fa6cb8d833f681744a9
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: 'On-treatment analysis

          In the on-treatment analysis, we included all patients of

          the intervention-group who received at least the prespe-

          ciﬁed intensity of 28 h in 4 weeks (n ¼ 23, 29%) and all

          subjects in the control-group who did not receive any

          treatment (n ¼ 62, 86%).'
        anchor_text: 'On-treatment analysis

          In the on-treatment analysis, we included all patients of

          the intervention-group who received at least the prespe-

          ciﬁed intensity of 28 h in 4 weeks (n ¼ 23, 29%) and all

          subjects in the control-group who did not receive any

          treatment (n ¼ 62, 86%).'
        excluded_fragments: []
        image_sha256: 6a894a1088d07a8bd04dcf2240fe3ff5130c00f9e9b9ed2ade259d277441ebd1
      P1-S1-C5:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: a5d4e2d6027e4815bcfa24420c514aff33ab702ce1cb431a7b4519cf2f1f7dd9
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 716ef30c3d96f23504ea1c0729a3c78cacac98fc4a399c3b45d0543800447cb0
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P1-S1-C5
          page: 1
          text_layer_sha256: 716ef30c3d96f23504ea1c0729a3c78cacac98fc4a399c3b45d0543800447cb0
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Methods and patients: Stroke patients with first-ever aphasia
          were randomised within 2 weeks of onset to either 4

          weeks of early intensive cognitive-linguistic treatment (1 h/day) or no
          language treatment.'
        anchor_text: 'Methods and patients: Stroke patients with first-ever aphasia
          were randomised within 2 weeks of onset to either 4

          weeks of early intensive cognitive-linguistic treatment (1 h/day) or no
          language treatment.'
        excluded_fragments: []
        image_sha256: 76c9505410b460b0388c67f0497b237cd99603a7ca579d2084d36dafe9a2ea61
        transcription: 'Methods and patients: Stroke patients with first-ever aphasia
          were randomised within 2 weeks of onset to either 4 weeks of early intensive
          cognitive-linguistic treatment (1 h/day) or no language treatment'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 4
  quote: 'come ANELT-A (adjusted diﬀerence ¼ 5.41, 95% CI:

    [1.52 to 9.31], p ¼ 0.007); SAT verbal (adjusted diﬀer-

    ence ¼ 3.57, 95% CI: [0.36 to 6.78], p ¼ 0.030) and CAT

    word comprehension (adjusted diﬀerence ¼ 3.64, 95%

    CI: [0.58 to 6.69], p ¼ 0.020) (Figure 3, online Table

    6).'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-25'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
