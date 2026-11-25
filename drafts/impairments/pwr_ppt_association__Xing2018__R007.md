---
id: pwr_ppt_association
name: PWR and PPT association
kind: impairment
findings:
- id: f1
  target: ppt_scores
  target_kind: impairment
  claim: There was no significant relationship between PWR and PPT scores when controlling
    for age, gender, education level, handedness, time from stroke, and total lesion
    size.
  direction: no_effect
  relationship: correlational
  method: behavioral_only
  sample:
    n: 45
    population: chronic left hemisphere stroke survivors with history of aphasia
    phase: not_reported
    time_post_onset: at least 6 months poststroke
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations: []
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Concurrent measurement of phonological processing
    (via a 30-item in-house pseudoword repetition task) and nonverbal semantic processing
    (via the Pyramids and Palm Trees Test). controlled for age, gender, education
    level, handedness, time from stroke, and total lesion size. Additional metadata
    has not been transcribed; review the pending-field flags before approval. PDF
    image reading (P2-S2-C2, two-model agreement, human verification pending): Methods


    Participants


    A total of 45 chronic left hemisphere stroke survivors with history of aphasia
    were recruited in the study, with inclusion criteria as follows: native English
    speaker, at least 6 months poststroke, able to follow testing instructions, and
    no history of other significant neurological illnesses Original text-layer quotation
    is preserved below.'
  imaging_details:
    reference_space: not_reported
    atlases_used: []
  lesion_mapping: {}
  provenance:
    extracted_by: model:gemma4:31b
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
    - not_transcribed:author_limitations
    - proposed_concept:ppt_scores
  citation: '@Xing2018'
  source_passages:
  - section: Original source P6-S2-C10
    page: 6
    quote: "There was no \nsignificant relationship between PWR and PPT scores con-\n\
      trolling for the above variables (partial r = 0.01; P > .05), \n"
    supports: claim
  - section: Original source P6-S3-C2
    page: 6
    quote: "There was no \nsignificant relationship between PWR and PPT scores con-\n\
      trolling for the above variables (partial r = 0.01; P > .05), \nindicating the\
      \ independence of these 2 measures."
    supports: claim
  - section: Original source P2-S2-C2
    page: 2
    quote: "Methods\nParticipants\nA total of 45 chronic left hemisphere stroke survivors\
      \ with \nhistory of aphasia were recruited in the study, with inclu-\nsion criteria\
      \ as follows: native English speaker, at least 6 \nmonths poststroke, able to\
      \ follow testing instructions, and \nno history of other significant neurological\
      \ illnesses."
    supports: sample
  - section: Original source P2-S2-C9
    page: 2
    quote: 'Phonological processing was assessed with a 30-item in-

      house pseudoword repetition (PWR) task.'
    supports: method
  - section: Original source P2-S2-C10
    page: 2
    quote: "The Pyramids \nand Palm Trees Test (PPT)24 was administered to assess\
      \ \nnonverbal semantic processing."
    supports: method
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-26'
relationship_review:
  paper: Xing2018
  proposal_id: R007
  review_status_sha256: ea95ecb3de034313d4762941fde2402326e2ae6f6e7e41756cb7f4a3f875f2c6
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: f25fce04666dc022f51c9d2164d19b05e16f5fe93880a5764a534461a0d7fea4
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: f25fce04666dc022f51c9d2164d19b05e16f5fe93880a5764a534461a0d7fea4
        A/passages.json: 16f4f9e33548dd1eba22840120ce7b0824083c72e8612ca136f4c69938861d46
        A/raw.json: 0ad82939d83da0024dd6660ce9fa116f2d002fbcad4ee30c579427101c79896c
        A/source-units.json: bacfea3ebb1b8de4d1e9d39ffcff1e564da9bcd72180d672db1d91e31ecf264b
        A/full-source-units.json: 4db06df8a4c0884a8647e8d6f2ddfb2bf0703f0bca1fa229623e796459baa624
        A/meta.json: 729d32b946bfc3adca9c4940e4a66c0c60caa55ec4a723a2702ff308303f589d
        A/table-images/TABLE-1-page-2-1.png: 82b4445597c0865fb2c8dc777549c689d5b6a61d3f05669573c5e550beab2735
        A/table-images/page-2.png: fb19de444fab6f172a0bcd57f73d0093690abd682c76bcb00b99100a67515e72
        A/table-images/page-6.png: 7a3b4f884fecf3a4061f3c22a05663165aadfacbe86c4731660bd01177bb41da
        A/table-images/page-5.png: 8ff1ccff35e63e75b49286ff301c802c0064a452d2fd8fb2e95c2167109c9e4e
        A/table-images/page-4.png: f72c2b944634a2de1264a5c147fc62b2d81ddb8df901d00e3205694c2673e655
        A/table-images/TABLE-3-page-6-1.png: c79bf5b9912b8767984286a16ab172bccaf765db4029829b07c28d719d5c0c4e
        A/table-images/manifest.json: dc21376173dc6d004586009bbebd7a4e191b580f56007c1cdc031830ee3f8a4a
        A/table-images/TABLE-2-page-4-1.png: d57abd91e706b7c3874817ace9f2483611bce7dd494272f75413f369b6d1fc85
        A/table-images/TABLE-3-page-5-1.png: 55d663a7ce2fde452606e3726f04e72e9cebd3700c74a165a7ea3dc31b41b3ab
        A/clauses/window-03/raw.json: b1764e7a118a80eecdc2fed577e5e028240a1906155c29ce442aa11ca9994e76
        A/clauses/window-03/prompt.txt: 46021408f81bd1207c00d5c3350e66a660859107757462b2c2e2b1f2bd8d5e5d
        A/clauses/window-03/meta.json: d1383f94c3e0a6ffe373369c0cd3d56dc1a9e2534a828f468afee773b7b65e3f
        A/clauses/window-04/raw.json: 53ee65346b6a1e179261c3b5f930380534340fce1f9c25e0653407b51ffddbbc
        A/clauses/window-04/prompt.txt: a0e0f0874c5cad2c0ee09506e3713f44a1524421f47ce8b68ea81cb00105fe94
        A/clauses/window-04/meta.json: 762d57e082e706e02e6f9d6f505417afb1afa678e5b34004dd4e90639172e454
        A/clauses/window-05/raw.json: 9e8e0f58d3476aac5f588516464d4223e045101f92ad0ded6d3a9084c3bc3885
        A/clauses/window-05/prompt.txt: c929a5da1f2cde5643baa49f861c62a32062b809e133fdc3cff407a63dfeb20f
        A/clauses/window-05/meta.json: e8d0bd34ea6b32de3509c830b4a7cab2f3e5f8b8f95c25c5fb560fa6eeb37cff
        A/clauses/window-02/raw.json: 8f1608b9d4bc665dff63f7d53f5d52d87704ac3f36e3e26bff01d70d48cb0bbd
        A/clauses/window-02/prompt.txt: c33ed6a0f1326777a4037970071dc874bc9f290dcef8e9b4ba267756ee7b0d7b
        A/clauses/window-02/meta.json: 1f5a34c7012c3bb16a09ae79294c7e2cc6bd9cb6ab89c5f95738c13d5eba1f57
        A/clauses/window-01/raw.json: a74a48a0113b5ee45783c474b6986e16bdfd4b7fafb26100e30f799734f56b66
        A/clauses/window-01/prompt.txt: a52b5fbd5ae1ef0dd862d843220979e070158bbf6cba26a85dba940801c4a7f1
        A/clauses/window-01/meta.json: 6662fb5c96437cc091b2a022e1d1929123dac623aebe5e4b6510f0cf8e635e0f
        A/clauses/window-06/raw.json: 971f8e1b7a3d9db191190b4f6629f8582166f822122d0adfe742d3fdda4bf9c8
        A/clauses/window-06/prompt.txt: 0ffaf5f2f5ef6787b6b716a1c18ac5436e3c3e6c1486a3795cc6839d8e884931
        A/clauses/window-06/meta.json: 2ed5b88563fe6d417e8a488700e0bcaabd1ceda99a15eb1d611f519d8b182260
        A/tables/TABLE-3-page-5-3/raw.json: 996b714d860d02db610af393a7ac1d467ccd96c1ad83f505490b370dbca254eb
        A/tables/TABLE-3-page-5-3/prompt.txt: d336ceb841ece8ba389fe8df7af9500a936bb5887d477f709613eda261545e99
        A/tables/TABLE-3-page-5-3/meta.json: ae2adf8c99e3844212a8c39fa4d632dfcc1f1709d4592cf40b8650449a1ab529
        A/tables/TABLE-1-page-2-1/raw.json: 335a14f903d5b84f5b0dd8e7dda5a20c4bff12bccb7903e1c15f8a8493eae679
        A/tables/TABLE-1-page-2-1/prompt.txt: f8f26ae1cc39116504ec2b42e7604e980d67d97d6b23c48cadc0557a7f58f9fc
        A/tables/TABLE-1-page-2-1/meta.json: 506164358442ecdcf35fe3da2fbcf5476e3f6b0321b152611fc291f76e995d37
        A/tables/TABLE-3-page-6-4/raw.json: 652c10a0733de89164ba269e604ca497d0dad32c17cfdb56d7756b7b8d6b2370
        A/tables/TABLE-3-page-6-4/prompt.txt: 49f91b318a0a907de97427a91bbe7f1d9b198c36b138e5cdd8f04714e21b1c40
        A/tables/TABLE-3-page-6-4/meta.json: 6f8fbb01b2f2ad0dcd9024f5f894abd8c0b2f8c1a2f9ce69f05dbf846e72b2f9
        A/tables/TABLE-2-page-4-2/raw.json: 44fd2333ac3c29066b8b854803d7fcabc01c16b4a6d9058f97b3f1204ef8017a
        A/tables/TABLE-2-page-4-2/prompt.txt: 2dbc4c1fe53bb99c650f3088a05ed0fca58b2388ccb284c6cf3408b80c8beddf
        A/tables/TABLE-2-page-4-2/meta.json: cb3525b4d17b35fe060a9566aed46a7f68f6399b1dc6bb476811a083cca61f9b
        B/passages.json: 16f4f9e33548dd1eba22840120ce7b0824083c72e8612ca136f4c69938861d46
        B/raw.json: 9aeee213115ba67e9f8d30b0476bd17f2d196fe728d1f2cc852f393bc5fe5bf7
        B/source-units.json: bacfea3ebb1b8de4d1e9d39ffcff1e564da9bcd72180d672db1d91e31ecf264b
        B/full-source-units.json: 4db06df8a4c0884a8647e8d6f2ddfb2bf0703f0bca1fa229623e796459baa624
        B/meta.json: f99f31b729d2524a4a6bae9636a73d954209c336154ed75aa2c087eaa155b323
        B/table-images/TABLE-1-page-2-1.png: 82b4445597c0865fb2c8dc777549c689d5b6a61d3f05669573c5e550beab2735
        B/table-images/page-2.png: fb19de444fab6f172a0bcd57f73d0093690abd682c76bcb00b99100a67515e72
        B/table-images/page-6.png: 7a3b4f884fecf3a4061f3c22a05663165aadfacbe86c4731660bd01177bb41da
        B/table-images/page-5.png: 8ff1ccff35e63e75b49286ff301c802c0064a452d2fd8fb2e95c2167109c9e4e
        B/table-images/page-4.png: f72c2b944634a2de1264a5c147fc62b2d81ddb8df901d00e3205694c2673e655
        B/table-images/TABLE-3-page-6-1.png: c79bf5b9912b8767984286a16ab172bccaf765db4029829b07c28d719d5c0c4e
        B/table-images/manifest.json: 212d980c9ca6e66c5db5f88ee817999547f0e28e866689db3d6df196dcedb75b
        B/table-images/TABLE-2-page-4-1.png: d57abd91e706b7c3874817ace9f2483611bce7dd494272f75413f369b6d1fc85
        B/table-images/TABLE-3-page-5-1.png: 55d663a7ce2fde452606e3726f04e72e9cebd3700c74a165a7ea3dc31b41b3ab
        B/clauses/window-03/raw.json: 8d1c24c47d944f7b107630d4ddf275011ac5faa6fbfe3dd46f7ce67b8203f54c
        B/clauses/window-03/prompt.txt: 46021408f81bd1207c00d5c3350e66a660859107757462b2c2e2b1f2bd8d5e5d
        B/clauses/window-03/meta.json: d1e73852adca96da3ed9a73f9aa9c299379caf62147cf819a06a76061fab8c31
        B/clauses/window-04/raw.json: b146e20ed96dc83dd8a2d1e06a48e0bb4561f7a8c200629b44586975d2dda823
        B/clauses/window-04/prompt.txt: a0e0f0874c5cad2c0ee09506e3713f44a1524421f47ce8b68ea81cb00105fe94
        B/clauses/window-04/meta.json: 9c2f84cfdbb591dfebebab34f450caab00cc118a1af0a153053236b1ba4f112a
        B/clauses/window-05/raw.json: f421a04b5205d776820b84035aeb6a9b6103b3e91968de8b19f4db5739c03013
        B/clauses/window-05/prompt.txt: c929a5da1f2cde5643baa49f861c62a32062b809e133fdc3cff407a63dfeb20f
        B/clauses/window-05/meta.json: e2daed60e231237bb5d8a39ad7044555e86b28764aa7d1843740376738781a4e
        B/clauses/window-02/raw.json: ae55a7307f112e8ec2b01274042473f784f846e1d0072c29d82b9318abb97d27
        B/clauses/window-02/prompt.txt: c33ed6a0f1326777a4037970071dc874bc9f290dcef8e9b4ba267756ee7b0d7b
        B/clauses/window-02/meta.json: 0d5b55137007d4caf5e52d714f08f19351a56be2d0de773b4efd2906536118a8
        B/clauses/window-01/raw.json: 6992b065eac2b1f0d1333c20b7db09761965f6f4e9588f197f6c191afcde3c69
        B/clauses/window-01/prompt.txt: a52b5fbd5ae1ef0dd862d843220979e070158bbf6cba26a85dba940801c4a7f1
        B/clauses/window-01/meta.json: d0089e4478836e162c3788e2eee69ff897b4161f2ab75ef1360b06320fdb0883
        B/clauses/window-06/raw.json: 827ae204d765b49b5a38aea51161f51816b919a14c559139734a2f21b863e431
        B/clauses/window-06/prompt.txt: 0ffaf5f2f5ef6787b6b716a1c18ac5436e3c3e6c1486a3795cc6839d8e884931
        B/clauses/window-06/meta.json: a8dde91b62061d95b41de1dd06b1f614afb27fabf768907e9d8c0d87d95a9fb8
        B/tables/TABLE-3-page-5-3/raw.json: 54d5ff20c89a91c80b00de70e764e31029f278fe30c1a15d3511dfab6a56ce15
        B/tables/TABLE-3-page-5-3/prompt.txt: d336ceb841ece8ba389fe8df7af9500a936bb5887d477f709613eda261545e99
        B/tables/TABLE-3-page-5-3/meta.json: 02a82ca8b54d7d23f45cdb69002c853652d06eb3581da007de272fe53234a064
        B/tables/TABLE-1-page-2-1/raw.json: 32eb1f30acb9cde828573a92d04faf713015814ce98b63959fbd950e2620e7d7
        B/tables/TABLE-1-page-2-1/prompt.txt: f8f26ae1cc39116504ec2b42e7604e980d67d97d6b23c48cadc0557a7f58f9fc
        B/tables/TABLE-1-page-2-1/meta.json: 20adc97abacb8931ec4a25f934cf331a2339fe758d24029c6dbc1769d9d91c6b
        B/tables/TABLE-3-page-6-4/raw.json: 817708b742db74ff7ac6b7118d96e315e43db0b85f652cb19efd77c2540b5909
        B/tables/TABLE-3-page-6-4/prompt.txt: 49f91b318a0a907de97427a91bbe7f1d9b198c36b138e5cdd8f04714e21b1c40
        B/tables/TABLE-3-page-6-4/meta.json: 1a75d4d7011a9e7a76035cf65b77bc94f6c99bb8755a530c5a85b28b61e4828f
        B/tables/TABLE-2-page-4-2/raw.json: 46819bea58194e1aa9e1db4c9a01b11d0421b9ffd4a64c99e46945035a68f0bf
        B/tables/TABLE-2-page-4-2/prompt.txt: 2dbc4c1fe53bb99c650f3088a05ed0fca58b2388ccb284c6cf3408b80c8beddf
        B/tables/TABLE-2-page-4-2/meta.json: eba1242087633342896eec190c672395d445682a127eaf82e25b5116371dba0b
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
      pdf_sha256: f25fce04666dc022f51c9d2164d19b05e16f5fe93880a5764a534461a0d7fea4
      source_review: _compare/relationships-2026-11-16/review-current/Xing2018
      source_status_sha256: d156f0d819db0d1942fe2272400317be39efa8a6fa176024507589569c98872e
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R007
    exposure:
      text: PWR scores
    outcome:
      text: PPT scores
    analysis_label: Partial correlation of phonology and semantics measures
    relation: association
    evidence_ids:
    - P6-S2-C10
    - P6-S3-C2
    qualifier_ids:
    - P6-S2-C10
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: f25fce04666dc022f51c9d2164d19b05e16f5fe93880a5764a534461a0d7fea4
      source_review: _compare/relationships-2026-11-16/review-current/Xing2018
      source_status_sha256: d156f0d819db0d1942fe2272400317be39efa8a6fa176024507589569c98872e
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Accounting without a linked unit P1-S2-C14
      - Accounting without a linked unit P1-S2-C15
      - Accounting without a linked unit P1-S2-C16
      - Unaccounted source passage P1-S2-C16
      - Unaccounted source passage P1-S2-C14
      - Unaccounted source passage P1-S2-C15
      - Result passage disposed without unit P4-S1-C3
      - Result passage disposed without unit P5-S1-C10
      - Result passage disposed without unit P5-S1-C12
      - Result passage disposed without unit P5-S1-C8
      - Result passage disposed without unit P5-S1-C9
      - Result passage disposed without unit P5-S2-C2
      - Accounting without a linked unit P5-S2-C3
      - Accounting without a linked unit P6-S1-C3
      - Accounting without a linked unit P6-S1-C4
      - Unaccounted source passage P6-S1-C3
      - Unaccounted source passage P5-S2-C3
      - Unaccounted source passage P6-S1-C4
      - Unresolved source passage P6-S1-C7
      - Result passage disposed without unit P7-S1-C3
      - Result passage disposed without unit P7-S1-C4
      - Accounting without a linked unit P8-S1-C1
      - Accounting without a linked unit P8-S1-C2
      - Result passage disposed without unit P8-S1-C4
      - Accounting without a linked unit P8-S1-C5
      - Result passage disposed without unit P8-S1-C6
      - Unaccounted source passage P8-S1-C5
      - Unaccounted source passage P8-S1-C2
      - Unaccounted source passage P8-S1-C1
      - Result passage disposed without unit P9-S1-C10
      - Result passage disposed without unit P9-S1-C3
      - Accounting without a linked unit P9-S2-C10
      - Result passage disposed without unit P9-S2-C3
      - Result passage disposed without unit P9-S2-C7
      - Unaccounted source passage P9-S2-C10
      - Result passage disposed without unit P9-S3-C8
      unattached_null_or_qualifier_ids:
      - P1-S2-C14
      - P1-S2-C15
      - P5-S2-C3
      - P8-S1-C1
      - P8-S1-C2
      - P8-S1-C5
      - P9-S1-C3
      - P9-S2-C6
      suppressed_nonrepresented_units: 5
      default_disposition_count_requires_completeness_check: 136
      unselected_timing_passages:
      - P2-S2-C4
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P6-S2-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S2-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S2-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P9-S3-C5
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: analysis_restrictions
        source_ids:
        - P5-S1-C4
        - P5-S1-C5
        - P5-S1-C6
        - P6-S1-C4
        - P6-S2-C2
        - P6-S2-C6
        - P6-S2-C7
        - P6-S2-C8
        - P6-S3-C3
        - P7-S1-C11
        - P8-S1-C2
        - P8-S2-C6
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: adjustment_roles
        source_ids:
        - P5-S1-C4
        - P5-S1-C5
        - P5-S1-C6
        - P6-S1-C4
        - P6-S2-C2
        - P6-S2-C6
        - P6-S2-C7
        - P6-S2-C8
        - P6-S3-C3
        - P7-S1-C11
        - P8-S1-C2
        - P8-S2-C6
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - validation
      - analysis_restrictions
      - personal_factors
      - tested_personal_effects
      - adjustment_roles
      - explicitly_not_adjusted
      unclassified_extraction_ids:
      - P9-S2-C11
      table_review_required:
      - TABLE-1-page-2-1
      - TABLE-2-page-4-2
      - TABLE-3-page-5-3
      - TABLE-3-page-6-4
      unlinked_tables:
      - TABLE-1-page-2-1
      - TABLE-2-page-4-2
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P3-S1
        - P3-S2
        - P3-S3
        - P5-S1
        - P6-S2
        - P7-S1
        - P8-S2
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: f25fce04666dc022f51c9d2164d19b05e16f5fe93880a5764a534461a0d7fea4
      source_review: _compare/relationships-2026-11-16/review-current/Xing2018
      source_status_sha256: d156f0d819db0d1942fe2272400317be39efa8a6fa176024507589569c98872e
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S2-C14
      disposition: represented
      result_indexes:
      - 0
      reason: Abstract statement of FA values in 13 LH tracts and 1 interhemispheric
        tract relating to naming.
    - source_id: P1-S2-C15
      disposition: represented
      result_indexes:
      - 1
      reason: Abstract statement that cortical node lesion loads were not related
        to naming after control.
    - source_id: P1-S2-C16
      disposition: represented
      result_indexes:
      - 2
      - 3
      reason: Abstract statement of 4 ventral tracts relating to semantics and 1 dorsal
        tract relating to phonology.
    - source_id: P3-S2-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes fMRI analysis methodology for identifying naming activity.
    - source_id: P4-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the identification of 12 bilateral homologous regions.
    - source_id: P4-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes thresholding of group-wise connection maps.
    - source_id: P5-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the consistency of connections in healthy participants.
    - source_id: P5-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Restates the number of cortical seeds identified.
    - source_id: P5-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the total number of reconstructed connections.
    - source_id: P5-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Provides average size of tracts.
    - source_id: P5-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Provides average lesion load of LH seeds.
    - source_id: P5-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Provides percentage of patients with lesions in LH seeds.
    - source_id: P5-S2-C3
      disposition: unresolved
      result_indexes: []
      reason: Table 3 contains specific FA correlations for 48 tracts; requires transcription
        of flattened cells.
    - source_id: P6-S1-C3
      disposition: represented
      result_indexes:
      - 1
      reason: Reports significant negative relation between PNT and 7 LH seeds before
        adding total lesion volume.
    - source_id: P6-S1-C4
      disposition: represented
      result_indexes:
      - 1
      reason: Reports null result for LH seeds when adding total lesion volume as
        covariate.
    - source_id: P6-S1-C5
      disposition: represented
      result_indexes:
      - 1
      reason: Conclusion that no specific LH cortical ROIs affected naming above total
        lesion size.
    - source_id: P6-S1-C7
      disposition: represented
      result_indexes:
      - 0
      reason: Reports 14 tracts significantly correlated with PNT scores.
    - source_id: P6-S2-C2
      disposition: represented
      result_indexes:
      - 0
      reason: Details the 14 tracts' correlation with PNT scores and the covariates
        used.
    - source_id: P6-S2-C3
      disposition: represented
      result_indexes:
      - 0
      reason: Specifies the distribution of the 14 tracts (13 LH, 1 interhemispheric).
    - source_id: P6-S2-C4
      disposition: represented
      result_indexes:
      - 4
      reason: Reports no significant relationships between PNT and FA of right hemisphere
        tracts.
    - source_id: P6-S2-C7
      disposition: represented
      result_indexes:
      - 2
      reason: Reports lpSTG-lOperIFG tract integrity relating to PWR performance.
    - source_id: P6-S2-C8
      disposition: represented
      result_indexes:
      - 3
      reason: Reports 5 LH tracts correlating with PPT scores.
    - source_id: P6-S3-C2
      disposition: represented
      result_indexes:
      - 6
      reason: Reports no significant relationship between PWR and PPT scores.
    - source_id: P6-S3-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Introduces the sensitivity analysis adding PPT as a covariate.
    - source_id: P7-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the number of reconstructed tracts in healthy participants.
    - source_id: P7-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes dorsal and ventral connections between specific seed pairs.
    - source_id: P8-S1-C1
      disposition: represented
      result_indexes:
      - 2
      reason: 'Sensitivity result: lpSTG-lOperIFG relationship to PWR remains significant
        when controlling for PPT.'
    - source_id: P8-S1-C2
      disposition: represented
      result_indexes:
      - 3
      reason: 'Sensitivity result: 5 semantic tracts remain significant when controlling
        for PWR.'
    - source_id: P8-S1-C5
      disposition: repeated
      result_indexes:
      - 1
      reason: Discussion restatement of the null result for gray matter nodes.
    - source_id: P9-S1-C10
      disposition: repeated
      result_indexes:
      - 0
      reason: Discussion restatement that naming depends on tracts in both streams.
    - source_id: P9-S2-C10
      disposition: represented
      result_indexes:
      - 4
      reason: Reports no significant relationships between right hemisphere white
        matter and naming.
    - source_id: P9-S3-C1
      disposition: repeated
      result_indexes:
      - 4
      reason: Restatement of the null result for right hemisphere white matter.
    - source_id: P9-S3-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discusses the specificity of connections compared to prior studies.
    - source_id: P9-S3-C3
      disposition: represented
      result_indexes:
      - 5
      reason: Identifies the left aSTG–right aSTG connection as associated with naming.
    - source_id: P10-S1-C1
      disposition: repeated
      result_indexes:
      - 0
      - 1
      reason: Conclusion restating the importance of white matter over gray matter
        for naming.
    unresolved_coverage:
    - source_id: P9-S3-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P9-S3-C2
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P8-S1-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S1-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S2-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S1-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S2-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S2-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S2-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S3-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S3-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P3-S2-C13
    - P4-S1-C3
    - P4-S2-C4
    - P5-S1-C1
    - P5-S1-C8
    - P5-S1-C9
    - P5-S1-C10
    - P5-S1-C12
    - P5-S2-C2
    - P5-S2-C3
    - P6-S1-C3
    - P6-S2-C3
    - P6-S3-C4
    - P7-S1-C3
    - P7-S1-C4
    - P8-S1-C4
    - P8-S1-C5
    - P8-S1-C6
    - P8-S2-C2
    - P9-S1-C3
    - P9-S1-C10
    - P9-S2-C3
    - P9-S2-C6
    - P9-S2-C7
    - P9-S3-C8
    - P9-S3-C9
    - P10-S1-C1
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-2-1
    - TABLE-2-page-4-2
    - TABLE-3-page-5-3
    - TABLE-3-page-6-4
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P2-S2-C6
      - P2-S2-C2
      recruited_sample:
      - P2-S2-C2
      - P2-S2-C6
      eligibility:
      - P2-S2-C2
      imaging_provenance:
      - P4-S1-C8
      - P4-S1-C12
      - P5-S1-C3
      imaging_timing:
      - P2-S2-C2
      outcome_timing:
      - P2-S2-C1
      outcome_definition:
      - P2-S2-C8
      - P2-S2-C9
      - P2-S2-C10
      - P5-S1-C5
      - P5-S1-C6
      validation: []
      analysis_restrictions: []
      dependent_variable_statement:
      - P5-S1-C4
      - P5-S1-C5
      - P5-S1-C6
      - P6-S2-C6
      limitations:
      - P9-S3-C4
      - P9-S3-C5
      - P9-S3-C6
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles: []
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P2-S3-C4
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P6-S2-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S2-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S2-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P9-S3-C5
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: analysis_restrictions
      source_ids:
      - P5-S1-C4
      - P5-S1-C5
      - P5-S1-C6
      - P6-S1-C4
      - P6-S2-C2
      - P6-S2-C6
      - P6-S2-C7
      - P6-S2-C8
      - P6-S3-C3
      - P7-S1-C11
      - P8-S1-C2
      - P8-S2-C6
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: adjustment_roles
      source_ids:
      - P5-S1-C4
      - P5-S1-C5
      - P5-S1-C6
      - P6-S1-C4
      - P6-S2-C2
      - P6-S2-C6
      - P6-S2-C7
      - P6-S2-C8
      - P6-S3-C3
      - P7-S1-C11
      - P8-S1-C2
      - P8-S2-C6
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
      pdf_sha256: f25fce04666dc022f51c9d2164d19b05e16f5fe93880a5764a534461a0d7fea4
      review_sha256: ea95ecb3de034313d4762941fde2402326e2ae6f6e7e41756cb7f4a3f875f2c6
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
      - P6-S2-C10
      - P6-S3-C2
      source_result: The source reports that there was no significant relationship
        between PWR (phonology) and PPT (semantics) scores in patients when controlling
        for age, gender, education, handedness, time from stroke, and total lesion
        volume (partial r = 0.01, P > .05). This null result is used to establish
        the independence of the two measures, allowing subsequent analyses to add
        one as a covariate to the other without concern for collinearity.
      result_status: not_detected
      patient_measurement: non_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis is the partial correlation between PWR and
            PPT scores. The source explicitly states this was done to check for independence
            (P6-S2-C10, P6-S3-C2). The proposed core correctly identifies this as
            the analysis being reviewed.
          source_ids:
          - P6-S2-C10
          - P6-S3-C2
        direction:
          answer: fits
          reason: The source reports a non-significant correlation (partial r = 0.01,
            P > .05). The proposed core claims 'no significant relationship' and sets
            direction to 'no_effect'. This accurately reflects the null finding in
            the source.
          source_ids:
          - P6-S2-C10
          - P6-S3-C2
        construct:
          answer: fits
          reason: The exposure is PWR scores and the outcome is PPT scores. The source
            confirms PWR is a pseudoword repetition task (P2-S2-C9) and PPT is the
            Pyramids and Palm Trees Test (P2-S2-C10). The method is behavioral correlation,
            not imaging-based. The patient measurement is non_imaging (behavioral
            scores), which is correct as the analysis correlates two behavioral tests,
            not imaging data directly (though the imaging data was used in other analyses,
            this specific check is on the PWR-PPT relationship).
          source_ids:
          - P2-S2-C9
          - P2-S2-C10
          - P6-S2-C10
        qualifications:
          answer: fits
          reason: The source specifies that the null result was obtained 'controlling
            for the above variables' (P6-S2-C10), which refers to age, gender, education,
            handedness, time from stroke, and total lesion volume (listed in P6-S2-C2
            and P5-S1-C4). The proposed core includes these exact covariates in the
            qualifications.
          source_ids:
          - P6-S2-C10
          - P6-S3-C2
          - P5-S1-C4
        missing_material_caveat:
          answer: fits
          reason: The core captures the null finding and the covariates. There are
            no omitted material caveats that change the interpretation of this specific
            null result. The fact that this null result supports the independence
            of measures for subsequent analyses is a methodological justification,
            not a caveat that alters the finding itself.
          source_ids:
          - P6-S2-C10
          - P6-S3-C2
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
      id: R007
      exposure:
        text: PWR scores
      outcome:
        text: PPT scores
      analysis_label: Partial correlation of phonology and semantics measures
      relation: association
      evidence_ids:
      - P6-S2-C10
      - P6-S3-C2
      qualifier_ids:
      - P6-S2-C10
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: f25fce04666dc022f51c9d2164d19b05e16f5fe93880a5764a534461a0d7fea4
        source_review: _compare/relationships-2026-11-16/review-current/Xing2018
        source_status_sha256: d156f0d819db0d1942fe2272400317be39efa8a6fa176024507589569c98872e
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P2-S2-C2:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: f25fce04666dc022f51c9d2164d19b05e16f5fe93880a5764a534461a0d7fea4
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 46fa73a59a66e668e2d9df023172311037c13fa37ee68cc5d16d3271d89fdd62
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S2-C2
          page: 2
          text_layer_sha256: 46fa73a59a66e668e2d9df023172311037c13fa37ee68cc5d16d3271d89fdd62
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "Methods\nParticipants\nA total of 45 chronic left hemisphere\
          \ stroke survivors with \nhistory of aphasia were recruited in the study,\
          \ with inclu-\nsion criteria as follows: native English speaker, at least\
          \ 6 \nmonths poststroke, able to follow testing instructions, and \nno history\
          \ of other significant neurological illnesses."
        anchor_text: "Methods\nParticipants\nA total of 45 chronic left hemisphere\
          \ stroke survivors with \nhistory of aphasia were recruited in the study,\
          \ with inclu-\nsion criteria as follows: native English speaker, at least\
          \ 6 \nmonths poststroke, able to follow testing instructions, and \nno history\
          \ of other significant neurological illnesses."
        excluded_fragments: []
        image_sha256: 738fda89eccd7fa421821f75c36e3b3327c6152e3b8f0a7795ad4e63b68476c8
        transcription: 'Methods


          Participants


          A total of 45 chronic left hemisphere stroke survivors with history of aphasia
          were recruited in the study, with inclusion criteria as follows: native
          English speaker, at least 6 months poststroke, able to follow testing instructions,
          and no history of other significant neurological illnesses'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 6
  quote: "There was no \nsignificant relationship between PWR and PPT scores con-\n\
    trolling for the above variables (partial r = 0.01; P > .05), \n"
  status: pending
  by: agent:relationship-converter
  date: '2026-11-26'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
