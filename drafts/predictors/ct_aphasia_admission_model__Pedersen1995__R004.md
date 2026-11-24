---
id: ct_aphasia_admission_model
name: CT-based aphasia admission predictor
kind: predictor
findings:
- id: f1
  target: aphasia_score_admission
  target_kind: impairment
  claim: Side of stroke lesion, size of lesion, and cortical involvement had a significant
    independent influence on the aphasia score on admission, explaining 35% of the
    total variance.
  direction: likely
  relationship: correlational
  method: behavioral_only
  sample:
    n: not_reported
    population: unselected community-based sample of patients with acute stroke
    phase: not_reported
    time_post_onset: on admission
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - CT scans were evaluated by visual inspection
  - Aphasia assessment rates spoken language but does not assess auditory impressive
    function
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: A multiple linear regression model using visual inspection
    of CT scans to determine the side of the stroke lesion, the largest diameter of
    the lesion (size), and whether the lesion involved the cortex. Analysis was restricted
    to patients with visible focal lesions on CT scan. Additional metadata has not
    been transcribed; review the pending-field flags before approval.'
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
    - proposed_concept:aphasia_score_admission
  citation: '@Pedersen1995'
  source_passages:
  - section: Original source P3-S1-C7
    page: 3
    quote: "In a multiple \nlinear regression analysis, three of these variables had\
      \ a \nsignificant independent influence on the aphasia score."
    supports: claim
  - section: Original source P3-S1-C8
    page: 3
    quote: "Side of stroke lesion, size of lesion, and cortical \ninvolvement explained\
      \ 35% of the total variance."
    supports: claim
  - section: Original source P2-S1-C16
    page: 2
    quote: "Type, size, and localization of the stroke lesion were deter- \nmined\
      \ by visual inspection of the computed tomography \n(CT) scan."
    supports: method
  - section: Original source P2-S1-C17
    page: 2
    quote: Lesion size was measured as the largest diameter.
    supports: method
  - section: Original source P3-S1-C5
    page: 3
    quote: "The patients in whom the CT scan was without visi- \nble lesions were\
      \ excluded from the analyses substitut- \ning neurological severity with CT\
      \ variables."
    supports: confounders
  - section: Original source P1-S1-C2
    page: 1
    quote: "We studied prospectively and consecutively an unselected and \ncommunity-based\
      \ sample of 881 patients with acute stroke."
    supports: sample
  - section: Original source P6-S1-C6
    page: 6
    quote: "The aphasia assessment employed in this study \nrates spoken language,\
      \ but does not assess auditory \nimpressive function."
    supports: limitation
predictor_type: imaging_metric
short_definition: A multiple linear regression model using visual inspection of CT
  scans to determine the side of the stroke lesion, the largest diameter of the lesion
  (size), and whether the lesion involved the cortex.
assessment:
- Scandinavian Stroke Scale aphasia score
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-25'
relationship_review:
  paper: Pedersen1995
  proposal_id: R004
  review_status_sha256: 44bc705116eb4e26624b4c08ba0954bb5026b0e17b0699a306fa8898da9352c5
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 3c1103578c6cd352094b85581bc71ba0deb8faba7430f641ed0cef58397ee493
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 3c1103578c6cd352094b85581bc71ba0deb8faba7430f641ed0cef58397ee493
        A/passages.json: 29bc6689e2be49995f48b73d104793045704f05b10270bbfd268705d3c06149c
        A/raw.json: 37f0d999740364171d1c1d188e98ea079bdf10eee6b6df722e93aad0833affef
        A/source-units.json: 98b216e4b5a0d2186c9d7ebf4441278436aeb77b12715ab0e0ed32fe878d8236
        A/full-source-units.json: 6884153269268c704fbd984a6c7c320bd4e155d1a1d26bcb28b187d7249bc046
        A/meta.json: ae8f656f7140595d1829d146e3a48005d13c5da29fd1650e16ca3b895b8038fc
        A/table-images/page-3.png: 5441159e186c0f81e07cb54800b76e015da50f5ac0a24097de0cd0d4bb5de6ac
        A/table-images/manifest.json: 2e425fc0e806b3b75fef5c0824ec7bfcfb735f3fe0f80868c66ead90095f3b56
        A/table-images/TABLE-2-page-3-2.png: add3f37262a84500a84d12d744ab6c4a33344e31d607d849c7ffa33aff4324b7
        A/table-images/TABLE-I-page-3-1.png: add3f37262a84500a84d12d744ab6c4a33344e31d607d849c7ffa33aff4324b7
        A/clauses/window-03/raw.json: c3061ff4abb26b62e6a9654b98eba6d73d8097eaca0f16d48c31910a58809265
        A/clauses/window-03/prompt.txt: a7a8dfda9ac46ccbcb3cc89ac8dd4988f430423ab74869fee88d7ae7c14f91a6
        A/clauses/window-03/meta.json: eee5439efbeef1a0825519eddd69566dd1b2e6f2c180cd89b4ba47d5d71a268e
        A/clauses/window-04/raw.json: 10fae6376a9b93dd91b9982fdef5253e181cb4513a42a3ad7551a06bc3f2c8b2
        A/clauses/window-04/prompt.txt: a77511d5be0e08b799719fc0d91227f07363b349e34fbf69bc43474e874b3598
        A/clauses/window-04/meta.json: c852eb17778990fe5ad5025e3e8eaac238bc7a6d8d924a3e3cdb2719cd58dd13
        A/clauses/window-05/raw.json: 8818bf944ef7e24a96fb582cb76f939d29d530686f0239750fcfd4e3fe1340d7
        A/clauses/window-05/prompt.txt: 84f681130db48aefaea488642146ea4e51fdd43fb2d91e37737374f8ed35a104
        A/clauses/window-05/meta.json: be452891eef958c2919720a23a5e83d3b38adfd70e8dd04b197069e3045bce45
        A/clauses/window-02/raw.json: 76dc4b68943cac954a2bcde921f390127dc7d9d747a7744d4ea087496d230ea6
        A/clauses/window-02/prompt.txt: c6a0ac31e40525bc4cb092a4dc19f36d198b8cd105628ddfd68c943e6d30e86e
        A/clauses/window-02/meta.json: 30ad370c1883f20b503dbc6001cc43a380c23a3343c5d1f2929a40fdb60e395e
        A/clauses/window-07/raw.json: 8411c2734ebb5afaa4d8ce00de6b0f2ed0208e84a86747fe7ebbd34b47b56401
        A/clauses/window-07/prompt.txt: f00c377bee27cd89e4a33ed4f0847296e734ee22a13d914717c512ed5beed9f8
        A/clauses/window-07/meta.json: ddeed49640b65c6004ddf32f43ebff6065ce9edf782665c05aefa98a7cb5aae4
        A/clauses/window-01/raw.json: b63128c679965781f89e5f27c160c7ea1164a1e80556d543fb8227ed043a23ff
        A/clauses/window-01/prompt.txt: ed75b2f9809d231ec500cd3eb9c0e861562cb4d2d8ba32ca88ab8cd0c6b90160
        A/clauses/window-01/meta.json: d1d32cee9116f7df6b5c65ba891a49a420181d588a55a647b88a4be58dbfda3f
        A/clauses/window-06/raw.json: 53a2e5294d5c2ca741c47638508d694a119fe78ee0e27f7e22a3c3efc820581a
        A/clauses/window-06/prompt.txt: f8d5b451a0fa5843fd9386c6209f5aba9e4964f0a6853e0c2021d6582df76041
        A/clauses/window-06/meta.json: fbd2c82f80053696c22111823bb57880ee1487c94ad311d4773c2472521c2cc2
        A/tables/TABLE-2-page-3-2/raw.json: 59f26ed4ebd9c913f92f38565b10a193037a4cc4c461987815c7f100341f98b5
        A/tables/TABLE-2-page-3-2/prompt.txt: 139803975a5f013640bcd84cfd7bb3338ea34cb19497a5a9b66ebbed63940e36
        A/tables/TABLE-2-page-3-2/meta.json: f730f4609fb7ed0096fbeae34add0b92e0c561e99cf68cbf986c4ec4590ee3fa
        A/tables/TABLE-I-page-3-1/raw.json: f82aae784bc1eafd109fd7a886171efc52742d1714717b033a816698f0ec6358
        A/tables/TABLE-I-page-3-1/prompt.txt: d125618e848f00156ed646a4a94b680333ac5b34f15d14c40c2cc0b22c850a2e
        A/tables/TABLE-I-page-3-1/meta.json: 169fa1a650c2a857f3afc835b22dd393be631e79411fb129b2fd382210f4439b
        B/passages.json: 29bc6689e2be49995f48b73d104793045704f05b10270bbfd268705d3c06149c
        B/raw.json: aac58373a489856b7ff39545571a9be2b403982e656b9f04debca288bf4a930d
        B/source-units.json: 98b216e4b5a0d2186c9d7ebf4441278436aeb77b12715ab0e0ed32fe878d8236
        B/full-source-units.json: 6884153269268c704fbd984a6c7c320bd4e155d1a1d26bcb28b187d7249bc046
        B/meta.json: 0a9d6bee7e491254dfd47af6176216107956ca3eaa96646304198ca490074c6f
        B/table-images/page-3.png: 5441159e186c0f81e07cb54800b76e015da50f5ac0a24097de0cd0d4bb5de6ac
        B/table-images/manifest.json: 06058a59c440d3f3e9952eb92ccb01a07cc0970c035c376ce6dd6cd84801322c
        B/table-images/TABLE-2-page-3-2.png: add3f37262a84500a84d12d744ab6c4a33344e31d607d849c7ffa33aff4324b7
        B/table-images/TABLE-I-page-3-1.png: add3f37262a84500a84d12d744ab6c4a33344e31d607d849c7ffa33aff4324b7
        B/clauses/window-03/raw.json: 5e96729fe25ce39209d66bb5ff69b97978bdc539f3378259d642725a773a2bcb
        B/clauses/window-03/prompt.txt: a7a8dfda9ac46ccbcb3cc89ac8dd4988f430423ab74869fee88d7ae7c14f91a6
        B/clauses/window-03/meta.json: d7717f488fa3c84d293f5eadf0d5722f9b9802a7bfdbd6458dc52b5e4aa344ee
        B/clauses/window-04/raw.json: 289b29fcab35d69fd54b05b338b64a8bd26a8a098f8d55cd11ff8340c3960e01
        B/clauses/window-04/prompt.txt: a77511d5be0e08b799719fc0d91227f07363b349e34fbf69bc43474e874b3598
        B/clauses/window-04/meta.json: 28217640a9ad4448b458368393f2492b983733e0e5989974676cc39579d782a6
        B/clauses/window-05/raw.json: 39d7baa7472bfd5fa2969bd7736b76891a096f863eeae6eed7cd89fd31891749
        B/clauses/window-05/prompt.txt: 84f681130db48aefaea488642146ea4e51fdd43fb2d91e37737374f8ed35a104
        B/clauses/window-05/meta.json: 9f6492c1a8e16998545d5f797dd568fc4259824c48673a75d01bcbee2b905606
        B/clauses/window-02/raw.json: c5e0fb9764c46c1f0b6c7ef8f5f44de608608ed0f9baee9fc541c091323acd7d
        B/clauses/window-02/prompt.txt: c6a0ac31e40525bc4cb092a4dc19f36d198b8cd105628ddfd68c943e6d30e86e
        B/clauses/window-02/meta.json: 4c37e805f65c5a78d9527b723422bd9d1e6ab7e2cebc0d051e798350393f54e4
        B/clauses/window-07/raw.json: 13293feee4ae6f66f7e9cfa4c39e99c42a75df6d83abdad903f47c42eb1f418d
        B/clauses/window-07/prompt.txt: f00c377bee27cd89e4a33ed4f0847296e734ee22a13d914717c512ed5beed9f8
        B/clauses/window-07/meta.json: 894057407cb1ebc63ee050ed2c11c93c3c698c1422cd71b277744cb4bb271e3f
        B/clauses/window-01/raw.json: 107f94a324784376ef4a9a758f33135c4397299d40e79117aa6ca1db47007f62
        B/clauses/window-01/prompt.txt: ed75b2f9809d231ec500cd3eb9c0e861562cb4d2d8ba32ca88ab8cd0c6b90160
        B/clauses/window-01/meta.json: 1e3acaaaea713851d962dbe3e98adec80ac446a9779517fd0494e23e68c24d55
        B/clauses/window-06/raw.json: 47f28d94e09cdb5590fec7fa901ace86c8e6b3e88180c88f779cb157d00eaf9e
        B/clauses/window-06/prompt.txt: f8d5b451a0fa5843fd9386c6209f5aba9e4964f0a6853e0c2021d6582df76041
        B/clauses/window-06/meta.json: b8772780be4c23fd3c03d9f03b22bf7641ddea92b1655d773c8257ae49ea71b1
        B/tables/TABLE-2-page-3-2/raw.json: e7d0f7da19bfb765269d52c9e6ca3b009723034e8fe6ab3ce3e17703bd2d81d9
        B/tables/TABLE-2-page-3-2/prompt.txt: 139803975a5f013640bcd84cfd7bb3338ea34cb19497a5a9b66ebbed63940e36
        B/tables/TABLE-2-page-3-2/meta.json: e98f98ce0edaf68c962d23006f727b9a9a9f7e70bed41df892aba091314f0078
        B/tables/TABLE-I-page-3-1/raw.json: f82aae784bc1eafd109fd7a886171efc52742d1714717b033a816698f0ec6358
        B/tables/TABLE-I-page-3-1/prompt.txt: d125618e848f00156ed646a4a94b680333ac5b34f15d14c40c2cc0b22c850a2e
        B/tables/TABLE-I-page-3-1/meta.json: 5c498ee5ef535d0aa9385b55a1999d0a5a328990f7d00dc84ab1ce051fa5936a
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
      pdf_sha256: 3c1103578c6cd352094b85581bc71ba0deb8faba7430f641ed0cef58397ee493
      source_review: _compare/relationships-2026-11-16/review-current/Pedersen1995
      source_status_sha256: e2c5094ea532ee40d6695881b4aaab716986bed379d2c590b56e53c41f85843a
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R004
    exposure:
      text: side of stroke lesion, size of lesion, cortical involvement
    outcome:
      text: aphasia score on admission
    analysis_label: Multiple linear regression of aphasia determinants (visible lesions
      only)
    relation: association
    evidence_ids:
    - P3-S1-C7
    - P3-S1-C8
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
      pdf_sha256: 3c1103578c6cd352094b85581bc71ba0deb8faba7430f641ed0cef58397ee493
      source_review: _compare/relationships-2026-11-16/review-current/Pedersen1995
      source_status_sha256: e2c5094ea532ee40d6695881b4aaab716986bed379d2c590b56e53c41f85843a
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Accounting without a linked unit P1-S1-C5
      - Accounting without a linked unit P1-S1-C6
      - Accounting without a linked unit P1-S1-C7
      - Accounting without a linked unit P1-S1-C8
      - Accounting without a linked unit P1-S1-C9
      - Unaccounted source passage P1-S1-C6
      - Unaccounted source passage P1-S1-C8
      - Unaccounted source passage P1-S1-C7
      - Unaccounted source passage P1-S1-C9
      - Unaccounted source passage P1-S1-C5
      - Accounting without a linked unit P1-S2-C11
      - Accounting without a linked unit P1-S2-C12
      - Unaccounted source passage P1-S2-C11
      - Unaccounted source passage P1-S2-C12
      - Result passage disposed without unit P2-S2-C6
      - Result passage disposed without unit P2-S2-C7
      - Result passage disposed without unit P2-S3-C5
      - Result passage disposed without unit P2-S3-C6
      - Result passage disposed without unit P2-S3-C7
      - Result passage disposed without unit P2-S3-C9
      - Result passage disposed without unit P2-S3-C10
      - Result passage disposed without unit P2-S3-C11
      - Result passage disposed without unit P2-S3-C12
      - Result passage disposed without unit P2-S3-C13
      - Result passage disposed without unit P2-S3-C14
      - 'window 4: invalid/duplicate disposition P3-S1-C3'
      - Result passage disposed without unit P3-S1-C3
      - Result passage disposed without unit P3-S2-C11
      - Result passage disposed without unit P3-S2-C12
      - Result passage disposed without unit P3-S2-C13
      - Result passage disposed without unit P3-S2-C14
      - Result passage disposed without unit P3-S2-C15
      - Unresolved source passage P3-S2-C16
      - Result passage disposed without unit P3-S3-C3
      - Result passage disposed without unit P4-S1-C2
      - Accounting without a linked unit P4-S1-C10
      - Accounting without a linked unit P4-S1-C11
      - Accounting without a linked unit P4-S1-C4
      - Accounting without a linked unit P4-S1-C5
      - Accounting without a linked unit P4-S1-C6
      - Accounting without a linked unit P4-S1-C8
      - Accounting without a linked unit P4-S1-C9
      - Unaccounted source passage P4-S1-C10
      - Unaccounted source passage P4-S1-C9
      - Unaccounted source passage P4-S1-C6
      - Unaccounted source passage P4-S1-C5
      - Unaccounted source passage P4-S1-C4
      - Unaccounted source passage P4-S1-C8
      - Unaccounted source passage P4-S1-C11
      - Accounting without a linked unit P6-S1-C10
      - Accounting without a linked unit P6-S1-C11
      - Accounting without a linked unit P6-S1-C12
      - Accounting without a linked unit P6-S1-C7
      - Unaccounted source passage P6-S1-C11
      - Unaccounted source passage P6-S1-C12
      - Unaccounted source passage P6-S1-C10
      - Unaccounted source passage P6-S1-C7
      - Unresolved source passage P7-S2-C1
      - Result passage disposed without unit P7-S2-C10
      - Accounting without a linked unit P7-S2-C11
      - Accounting without a linked unit P7-S2-C12
      - Accounting without a linked unit P7-S2-C13
      - Accounting without a linked unit P7-S2-C15
      - Accounting without a linked unit P7-S3-C3
      - Unaccounted source passage P7-S2-C12
      - Unaccounted source passage P7-S2-C15
      - Unaccounted source passage P7-S3-C3
      - Unaccounted source passage P7-S2-C11
      - Unaccounted source passage P7-S2-C13
      - Result passage disposed without unit P7-S3-C5
      unattached_null_or_qualifier_ids:
      - P1-S1-C8
      - P2-S3-C9
      - P3-S2-C11
      - P3-S2-C15
      - P4-S1-C6
      - P7-S2-C15
      - P7-S3-C3
      suppressed_nonrepresented_units: 18
      default_disposition_count_requires_completeness_check: 104
      unselected_timing_passages:
      - P1-S1-C2
      - P1-S2-C9
      - P1-S2-C14
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P3-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P3-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P3-S1-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S1-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S1-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C12
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P2-S2-C12
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: tested_personal_effects
        source_id: P3-S1-C2
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P4-S1-C7
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P5-S1-C11
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P7-S1-C1
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: personal_factors
        source_ids:
        - P1-S1-C5
        - P1-S1-C9
        - P2-S1-C3
        - P2-S1-C5
        - P3-S1-C2
        - P3-S1-C6
        - P4-S1-C5
        - P4-S1-C7
        - P4-S1-C10
        - P5-S1-C9
        - P5-S1-C11
        - P5-S2-C3
        - P6-S1-C10
        - P6-S1-C11
        - P6-S1-C12
        - P6-S1-C13
        - P6-S2-C9
        - P7-S1-C1
        - P7-S1-C2
        - P7-S1-C3
        - P7-S1-C8
        - P7-S1-C9
        - P7-S2-C13
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: tested_personal_effects
        source_ids:
        - P1-S1-C5
        - P1-S1-C9
        - P2-S3-C8
        - P3-S1-C6
        - P4-S1-C5
        - P4-S1-C8
        - P4-S1-C10
        - P5-S1-C9
        - P5-S2-C3
        - P6-S1-C10
        - P6-S1-C11
        - P6-S1-C12
        - P6-S1-C13
        - P6-S2-C9
        - P7-S1-C2
        - P7-S1-C3
        - P7-S1-C8
        - P7-S1-C9
        - P7-S2-C13
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - validation
      - personal_factors
      - tested_personal_effects
      unclassified_extraction_ids:
      - P2-S1-C21
      table_review_required:
      - TABLE-2-page-3-2
      - TABLE-I-page-3-1
      unlinked_tables:
      - TABLE-2-page-3-2
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P4-S1
        - P4-S2
        - P5-S1
        - P6-S1
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 3c1103578c6cd352094b85581bc71ba0deb8faba7430f641ed0cef58397ee493
      source_review: _compare/relationships-2026-11-16/review-current/Pedersen1995
      source_status_sha256: e2c5094ea532ee40d6695881b4aaab716986bed379d2c590b56e53c41f85843a
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive incidence of aphasia at admission and discharge.
    - source_id: P1-S1-C5
      disposition: represented
      result_indexes:
      - 5
      reason: States sex was not a determinant of aphasia and no sex difference in
        lesion distribution.
    - source_id: P1-S1-C6
      disposition: represented
      result_indexes:
      - 10
      reason: Describes remission time based on initial severity.
    - source_id: P1-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about prognosis timing.
    - source_id: P1-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: General summary of predictor.
    - source_id: P1-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: General summary of non-predictors.
    - source_id: P1-S2-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Demographic comparison of included vs excluded patients.
    - source_id: P1-S2-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Demographic comparison of included vs excluded patients.
    - source_id: P2-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive mortality and early recovery rates.
    - source_id: P2-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive referral rate to therapy.
    - source_id: P2-S3-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to Table 1.
    - source_id: P2-S3-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive incidence of aphasia.
    - source_id: P2-S3-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive incidence of dysarthria.
    - source_id: P2-S3-C8
      disposition: represented
      result_indexes:
      - 0
      reason: States correlations of aphasia to lesion side, severity, handedness,
        and comorbidity.
    - source_id: P2-S3-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive incidence in hemisphere lesion patients.
    - source_id: P2-S3-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive CT performance rate.
    - source_id: P2-S3-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive timing of CT.
    - source_id: P2-S3-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive timing of CT.
    - source_id: P2-S3-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive CT findings by aphasia severity.
    - source_id: P2-S3-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive CT hemorrhage findings.
    - source_id: P2-S3-C15
      disposition: represented
      result_indexes:
      - 0
      reason: Provides univariate correlations for aphasia score.
    - source_id: P3-S1-C3
      disposition: represented
      result_indexes:
      - 1
      reason: Confirms univariate relations in multiple linear regression.
    - source_id: P3-S1-C4
      disposition: represented
      result_indexes:
      - 1
      reason: Specifies variance explained by predictors in multiple regression.
    - source_id: P3-S1-C6
      disposition: represented
      result_indexes:
      - 2
      reason: Univariate correlations for patients with visible lesions.
    - source_id: P3-S1-C7
      disposition: represented
      result_indexes:
      - 3
      reason: Identifies significant independent influence in multiple regression.
    - source_id: P3-S1-C8
      disposition: represented
      result_indexes:
      - 3
      reason: Specifies variance explained by predictors in multiple regression.
    - source_id: P3-S1-C9
      disposition: represented
      result_indexes:
      - 4
      reason: No difference in aphasia score between frontal and posterior lesions.
    - source_id: P3-S2-C2
      disposition: represented
      result_indexes:
      - 4
      reason: No difference in aphasia score between frontal and posterior lesions
        at discharge.
    - source_id: P3-S2-C4
      disposition: represented
      result_indexes:
      - 5
      reason: No significant difference between men and women in aphasia/lesion distribution.
    - source_id: P3-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive mean scores for men.
    - source_id: P3-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive mean scores for women.
    - source_id: P3-S2-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statistical test of mean scores.
    - source_id: P3-S2-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive incidence of aphasia in right-hemisphere lesions.
    - source_id: P3-S2-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive history of prior strokes.
    - source_id: P3-S2-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive severity distribution in right-hemisphere lesions.
    - source_id: P3-S2-C15
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison of severity distribution between left and right lesions.
    - source_id: P3-S3-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive handedness in right-hemisphere aphasia.
    - source_id: P4-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive handedness in left-hemisphere aphasia.
    - source_id: P4-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive incidence of crossed aphasia on admission.
    - source_id: P4-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive incidence of crossed aphasia at discharge.
    - source_id: P4-S1-C5
      disposition: represented
      result_indexes:
      - 6
      reason: Incidence of aphasia in right-hemisphere lesions by sex.
    - source_id: P4-S1-C6
      disposition: represented
      result_indexes:
      - 6
      reason: Incidence of right-hemisphere lesions in aphasic patients by sex.
    - source_id: P4-S1-C7
      disposition: represented
      result_indexes:
      - 6
      reason: Multiple linear regression for right-hemisphere lesions.
    - source_id: P4-S1-C8
      disposition: represented
      result_indexes:
      - 6
      reason: Significance of sex in right-hemisphere regression.
    - source_id: P4-S1-C9
      disposition: represented
      result_indexes:
      - 6
      reason: Variance explained in right-hemisphere regression.
    - source_id: P4-S1-C10
      disposition: represented
      result_indexes:
      - 7
      reason: Analysis of aphasia in left-sided lesions by sex.
    - source_id: P4-S1-C11
      disposition: represented
      result_indexes:
      - 8
      reason: Comparison of aphasia severity in women by lesion side.
    - source_id: P4-S2-C1
      disposition: represented
      result_indexes:
      - 8
      reason: Comparison of aphasia gain in women by lesion side.
    - source_id: P4-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive mortality rate.
    - source_id: P4-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive full recovery rate.
    - source_id: P4-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive recovery rate among survivors.
    - source_id: P4-S2-C5
      disposition: represented
      result_indexes:
      - 9
      reason: Reference to Figure 1 (outcome by initial severity).
    - source_id: P4-S2-C6
      disposition: represented
      result_indexes:
      - 9
      reason: Recovery rates at discharge by initial severity.
    - source_id: P4-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive aphasia rate at discharge.
    - source_id: P4-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive mortality and noncompliance at 6 months.
    - source_id: P4-S2-C9
      disposition: represented
      result_indexes:
      - 9
      reason: Reference to Figure 2 (outcome at 6 months).
    - source_id: P4-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive aphasia rate at 6 months.
    - source_id: P4-S2-C11
      disposition: represented
      result_indexes:
      - 9
      reason: Recovery rates at 6 months by initial severity.
    - source_id: P5-S1-C2
      disposition: represented
      result_indexes:
      - 9
      reason: Recovery rates at 6 months by initial severity.
    - source_id: P5-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive change in score from discharge to follow-up.
    - source_id: P5-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive mean score change.
    - source_id: P5-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive general time to stationary function.
    - source_id: P5-S1-C6
      disposition: represented
      result_indexes:
      - 10
      reason: Reference to Figure 3 (time course by severity).
    - source_id: P5-S1-C7
      disposition: represented
      result_indexes:
      - 10
      reason: Specific time to reach best level by initial severity.
    - source_id: P5-S1-C8
      disposition: represented
      result_indexes:
      - 11
      reason: Univariate correlations for aphasia score at discharge.
    - source_id: P5-S1-C9
      disposition: represented
      result_indexes:
      - 11
      reason: Non-correlations for aphasia score at discharge.
    - source_id: P5-S1-C10
      disposition: represented
      result_indexes:
      - 14
      reason: Comparison of gain by lesion side.
    - source_id: P5-S1-C11
      disposition: represented
      result_indexes:
      - 12
      reason: Multiple linear regression for aphasia recovery.
    - source_id: P5-S1-C12
      disposition: represented
      result_indexes:
      - 12
      reason: Variance explained in recovery regression.
    - source_id: P5-S1-C13
      disposition: represented
      result_indexes:
      - 12
      reason: Non-related factors in recovery regression.
    - source_id: P5-S2-C3
      disposition: represented
      result_indexes:
      - 12
      reason: Non-related factors in recovery regression.
    - source_id: P5-S2-C4
      disposition: represented
      result_indexes:
      - 13
      reason: Comparison of admission scores by therapy receipt.
    - source_id: P5-S2-C5
      disposition: represented
      result_indexes:
      - 13
      reason: Comparison of discharge scores and gain by therapy receipt.
    - source_id: P5-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison with previous studies.
    - source_id: P5-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement on early assessment.
    - source_id: P5-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive aphasia rate at discharge.
    - source_id: P5-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement on assessment comprehensiveness.
    - source_id: P5-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement on assessment sensitivity.
    - source_id: P6-S1-C7
      disposition: represented
      result_indexes:
      - 4
      reason: No difference in aphasia score between anterior and posterior lesions.
    - source_id: P6-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: General summary of aphasia relations.
    - source_id: P6-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: General summary of age influence.
    - source_id: P6-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: General summary of prior stroke influence.
    - source_id: P6-S1-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: General summary of handedness influence.
    - source_id: P6-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison of crossed aphasia with previous studies.
    - source_id: P6-S2-C9
      disposition: represented
      result_indexes:
      - 0
      reason: Sex difference in aphasia score disappeared in multiple regression.
    - source_id: P7-S1-C2
      disposition: represented
      result_indexes:
      - 5
      reason: No influence of sex on aphasia outcome.
    - source_id: P7-S1-C3
      disposition: represented
      result_indexes:
      - 5
      reason: No evidence of different hemispheric localization between sexes.
    - source_id: P7-S1-C8
      disposition: represented
      result_indexes:
      - 6
      reason: Right-sided aphasia more common in women.
    - source_id: P7-S1-C9
      disposition: represented
      result_indexes:
      - 8
      reason: No difference in severity or gain between women with left vs right lesions.
    - source_id: P7-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive general time to stationary function.
    - source_id: P7-S2-C5
      disposition: represented
      result_indexes:
      - 9
      reason: Recovery rates for severe and moderate aphasia.
    - source_id: P7-S2-C6
      disposition: represented
      result_indexes:
      - 9
      reason: Recovery rate for mild aphasia.
    - source_id: P7-S2-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: General summary of initial severity as a predictor.
    - source_id: P7-S2-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: General summary of age influence on outcome.
    - source_id: P7-S2-C15
      disposition: represented
      result_indexes:
      - 14
      reason: Right-sided lesion aphasia did not have a more favorable prognosis than
        left-sided.
    - source_id: P7-S3-C1
      disposition: represented
      result_indexes:
      - 14
      reason: Right-sided lesion aphasia did not have a more favorable prognosis than
        left-sided.
    - source_id: P7-S3-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison with other studies.
    - source_id: P7-S3-C3
      disposition: represented
      result_indexes:
      - 13
      reason: No difference in recovery between those who did and did not receive
        therapy.
    - source_id: P7-S3-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of study design limitations regarding therapy.
    - source_id: P7-S3-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement on unexplained variance in regression.
    unresolved_coverage:
    - source_id: P3-S1-C9
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P4-S1-C7
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P5-S1-C6
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P5-S1-C11
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P5-S1-C13
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P5-S2-C7
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P5-S2-C9
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P5-S2-C10
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P7-S3-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P7-S1-C13
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P7-S2-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P7-S2-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C4
    - P1-S1-C7
    - P1-S1-C8
    - P1-S1-C9
    - P1-S2-C11
    - P1-S2-C12
    - P2-S2-C6
    - P2-S2-C7
    - P2-S3-C5
    - P2-S3-C6
    - P2-S3-C7
    - P2-S3-C8
    - P2-S3-C9
    - P2-S3-C10
    - P2-S3-C11
    - P2-S3-C12
    - P2-S3-C13
    - P2-S3-C14
    - P3-S2-C5
    - P3-S2-C10
    - P3-S2-C11
    - P3-S2-C12
    - P3-S2-C13
    - P3-S2-C14
    - P3-S2-C15
    - P3-S3-C3
    - P4-S1-C2
    - P4-S1-C3
    - P4-S1-C4
    - P4-S1-C5
    - P4-S1-C6
    - P4-S2-C2
    - P4-S2-C3
    - P4-S2-C4
    - P4-S2-C5
    - P4-S2-C7
    - P4-S2-C8
    - P4-S2-C9
    - P4-S2-C10
    - P4-S2-C11
    - P5-S1-C3
    - P5-S1-C4
    - P5-S1-C5
    - P5-S2-C6
    - P5-S2-C8
    - P6-S1-C7
    - P6-S1-C10
    - P6-S1-C11
    - P6-S1-C12
    - P6-S1-C13
    - P6-S2-C3
    - P6-S2-C9
    - P7-S1-C2
    - P7-S1-C3
    - P7-S1-C8
    - P7-S1-C9
    - P7-S1-C13
    - P7-S2-C3
    - P7-S2-C10
    - P7-S2-C11
    - P7-S2-C12
    - P7-S2-C13
    - P7-S3-C2
    - P7-S3-C4
    - P7-S3-C5
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-2-page-3-2
    - TABLE-I-page-3-1
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P1-S1-C2
      - P1-S2-C9
      - P1-S2-C13
      recruited_sample:
      - P1-S2-C9
      eligibility:
      - P1-S2-C10
      - P1-S2-C11
      imaging_provenance:
      - P2-S1-C16
      - P2-S1-C19
      imaging_timing:
      - P2-S3-C11
      outcome_timing:
      - P1-S1-C3
      - P2-S1-C7
      - P4-S2-C9
      - P5-S1-C2
      - P7-S2-C2
      outcome_definition:
      - P1-S1-C3
      - P2-S1-C12
      - P2-S1-C14
      - P4-S2-C5
      - P5-S1-C2
      validation: []
      analysis_restrictions:
      - P2-S1-C10
      - P3-S1-C5
      dependent_variable_statement:
      - P2-S2-C12
      - P4-S1-C7
      - P5-S1-C11
      limitations:
      - P6-S1-C6
      - P6-S1-C7
      - P7-S3-C4
      - P7-S3-C5
      - P7-S3-C6
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P3-S1-C4
      - P3-S1-C7
      - P3-S1-C8
      - P4-S1-C7
      - P4-S1-C9
      - P4-S1-C10
      - P5-S1-C11
      - P5-S1-C12
      explicitly_not_adjusted:
      - P6-S2-C9
      descriptive_personal_factors:
      - P1-S2-C9
      - P3-S1-C2
    outcome_type: both_reported
    imaging_vs_outcome: precedes_outcome
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P3-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P3-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P3-S1-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S1-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S1-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C12
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P2-S2-C12
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: tested_personal_effects
      source_id: P3-S1-C2
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P4-S1-C7
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P5-S1-C11
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P7-S1-C1
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: personal_factors
      source_ids:
      - P1-S1-C5
      - P1-S1-C9
      - P2-S1-C3
      - P2-S1-C5
      - P3-S1-C2
      - P3-S1-C6
      - P4-S1-C5
      - P4-S1-C7
      - P4-S1-C10
      - P5-S1-C9
      - P5-S1-C11
      - P5-S2-C3
      - P6-S1-C10
      - P6-S1-C11
      - P6-S1-C12
      - P6-S1-C13
      - P6-S2-C9
      - P7-S1-C1
      - P7-S1-C2
      - P7-S1-C3
      - P7-S1-C8
      - P7-S1-C9
      - P7-S2-C13
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: tested_personal_effects
      source_ids:
      - P1-S1-C5
      - P1-S1-C9
      - P2-S3-C8
      - P3-S1-C6
      - P4-S1-C5
      - P4-S1-C8
      - P4-S1-C10
      - P5-S1-C9
      - P5-S2-C3
      - P6-S1-C10
      - P6-S1-C11
      - P6-S1-C12
      - P6-S1-C13
      - P6-S2-C9
      - P7-S1-C2
      - P7-S1-C3
      - P7-S1-C8
      - P7-S1-C9
      - P7-S2-C13
      reason: Runaway selection (>8 passages); entire slot requires source review
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
      pdf_sha256: 3c1103578c6cd352094b85581bc71ba0deb8faba7430f641ed0cef58397ee493
      review_sha256: 44bc705116eb4e26624b4c08ba0954bb5026b0e17b0699a306fa8898da9352c5
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
      - P3-S1-C7
      - P3-S1-C8
      source_result: In a multiple linear regression analysis restricted to patients
        with visible focal lesions on CT, side of stroke lesion, size of lesion, and
        cortical involvement had a significant independent influence on the aphasia
        score on admission, explaining 35% of the total variance.
      result_status: detected
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The source explicitly describes a multiple linear regression analysis
            where aphasia score on admission is the dependent variable and side, size,
            and cortical involvement are the independent variables, restricted to
            patients with visible lesions. This matches the selected analysis.
          source_ids:
          - P3-S1-C7
          - P3-S1-C8
          - P3-S1-C5
        direction:
          answer: fits
          reason: The source states these variables had a 'significant independent
            influence' and explained 35% of variance, indicating a detected association.
            The draft's claim of significant independent influence is faithful to
            the source's direction of finding an effect.
          source_ids:
          - P3-S1-C7
          - P3-S1-C8
        construct:
          answer: fits
          reason: 'The exposure (CT-based lesion characteristics: side, size, cortical
            involvement) and outcome (aphasia score on admission) are correctly identified.
            The patient measurement is template_lesion_overlap because the lesions
            were determined by visual inspection of CT scans (P2-S1-C16), which involves
            overlaying patient lesion data onto anatomical reference structures (cortex,
            hemispheres) rather than patient-specific diffusion tractography.'
          source_ids:
          - P2-S1-C16
          - P2-S1-C17
          - P3-S1-C6
          - P3-S1-C8
        qualifications:
          answer: fits
          reason: The draft correctly includes the qualification that the analysis
            was restricted to patients with visible focal lesions on CT scan, which
            is a material constraint stated in P3-S1-C5. It also correctly notes the
            limitation regarding the aphasia assessment (spoken language only) from
            P6-S1-C6.
          source_ids:
          - P3-S1-C5
          - P6-S1-C6
        missing_material_caveat:
          answer: fits
          reason: No material caveats are missing. The restriction to visible lesions
            is included. The limitation of the aphasia scale is included. The method
            of visual inspection is noted. The source does not indicate other material
            caveats that would change the interpretation of this specific regression
            result.
          source_ids:
          - P3-S1-C5
          - P6-S1-C6
          - P2-S1-C18
      optional_pending:
      - Sample size for the visible lesion subgroup is not transcribed in the provided
        source window.
      - Specific regression coefficients or p-values for the individual variables
        are not transcribed.
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Sample size requires source confirmation; it has not been transcribed.
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Sample size for the visible lesion subgroup is not transcribed in the provided
      source window.
    - Specific regression coefficients or p-values for the individual variables are
      not transcribed.
    normalizations:
    - field: sample.n
      original: 881
      action: not_transcribed
      reason: Not supported by selected quotations
    analysis_identity:
      id: R004
      exposure:
        text: side of stroke lesion, size of lesion, cortical involvement
      outcome:
        text: aphasia score on admission
      analysis_label: Multiple linear regression of aphasia determinants (visible
        lesions only)
      relation: association
      evidence_ids:
      - P3-S1-C7
      - P3-S1-C8
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
        pdf_sha256: 3c1103578c6cd352094b85581bc71ba0deb8faba7430f641ed0cef58397ee493
        source_review: _compare/relationships-2026-11-16/review-current/Pedersen1995
        source_status_sha256: e2c5094ea532ee40d6695881b4aaab716986bed379d2c590b56e53c41f85843a
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P1-S1-C2:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 3c1103578c6cd352094b85581bc71ba0deb8faba7430f641ed0cef58397ee493
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: a6db809f1b798eb7b973610bd94ef04ff233bb6a0f48c22acfda883e8d33b059
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P1-S1-C2
          page: 1
          text_layer_sha256: a6db809f1b798eb7b973610bd94ef04ff233bb6a0f48c22acfda883e8d33b059
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: "We studied prospectively and consecutively an unselected and\
          \ \ncommunity-based sample of 881 patients with acute stroke."
        anchor_text: "We studied prospectively and consecutively an unselected and\
          \ \ncommunity-based sample of 881 patients with acute stroke."
        excluded_fragments: []
        image_sha256: 5b2dd1f61492c9351a78e5859f3ac1a92d5ba13dfb911e635c20f696893a69be
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 3
  quote: "In a multiple \nlinear regression analysis, three of these variables had\
    \ a \nsignificant independent influence on the aphasia score."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-25'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
