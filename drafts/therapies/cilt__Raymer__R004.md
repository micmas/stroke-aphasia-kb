---
id: cilt
name: Constraint-induced language therapy
kind: therapy
findings:
- id: f1
  target: generalized_language_effects
  target_kind: impairment
  claim: Generalized effects of constraint-induced language therapy for standardized
    language measures were limited in two meta-analyses.
  direction: unlikely
  relationship: treatment_response
  method: meta-analysis
  sample:
    n: not_reported
    population: individuals with stroke-induced aphasia
    phase: not_reported
    time_post_onset: poststroke
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - The synthesis included systematic reviews that were each lacking two or more critical
    domains of the AMSTAR 2 quality appraisal
  evidence_quality: narrative-review
  strength: weak
  notes: 'Exposure measurement: Aphasia treatment incorporating forced verbal use
    and high-intensity training (up to 3 hours per day over 2 to 3 weeks) to facilitate
    language recovery. Finding based on a synthesis of six systematic reviews, specifically
    two meta-analyses. Additional metadata has not been transcribed; review the pending-field
    flags before approval.'
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
    - proposed_concept:generalized_language_effects
  therapy:
    id: cilt
    name: Constraint-induced language therapy
  citation: '@Raymer'
  source_passages:
  - section: Original source P1-S1-C14
    page: 1
    quote: 'Generalized CILT effects for standardized

      language measures were limited in two other MAs.'
    supports: claim
  - section: Original source P1-S2-C6
    page: 1
    quote: 'Constraint-induced language therapy (CILT) is an

      aphasia treatment approach that incorporates use-dependent

      principles to facilitate language recovery in individuals with

      aphasia following left hemisphere stroke (Pulvermüller et al.,

      2001).'
    supports: sample
  - section: Original source P1-S2-C10
    page: 1
    quote: 'Patients with aphasia partici-

      pate in as many as 3 hr per day of treatment delivered over a

      2- to 3-week period.'
    supports: method
  - section: Original source P1-S1-C10
    page: 1
    quote: 'Although

      the six SRs generally were conducted with satisfactory rigor, each was lacking

      two or more critical domains.'
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-25'
relationship_review:
  paper: Raymer
  proposal_id: R004
  review_status_sha256: 208e58450578e1e01e3e485633efe261728e0eb6fa1eb494708b6fb7f9173ea1
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 33521110ebe2c8dcb01c2dbbfe5d81e8687899afe9b62c31ed91166320cd31b2
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 33521110ebe2c8dcb01c2dbbfe5d81e8687899afe9b62c31ed91166320cd31b2
        A/passages.json: 689fd7157569f68eb45c9f81a0027af0c0d0d43dd7bf37d685f8ae3b00a8ffdb
        A/raw.json: 4b293fe40e1860401b1fa05afad53c24e867751c4ca8377c61c14c12aafdec34
        A/source-units.json: 1abe2ef669f0df2be0f35bd00cad43113b9d581dc783b28389f3dce8ecac07d0
        A/full-source-units.json: 6f05421aeeb100409c7304fea6bc1d916c536a16efb7aeda11cd2c2e38b1d3e5
        A/meta.json: c3034339b18a51da83df36dd65e00ca89f332de6fa0e9b58b9d8cde170e4534f
        A/table-images/TABLE-1-page-3-1.png: 3214fa8740d31c679f31570b4ef78ccff12a8484e5ab14c9cc50cb406168d080
        A/table-images/page-3.png: 1a286e345c6c5de0c095d75672c9c967a19dd00a29be8293a0b5954bcffd80f1
        A/table-images/page-6.png: 2405398c651e4c6750df132f221f62dd0ee09cf6298953ecb88f4bd0da216813
        A/table-images/page-5.png: f47ca70229f30aa8198030ebc111c2a372646a414f67762801986367ccd30358
        A/table-images/page-4.png: 88179e4936574bcdf8420d768b33a2e8c3652db84c4f805db77e79a14babebb2
        A/table-images/TABLE-3-page-6-1.png: beeb343531e826d361222205355a3ea2992bcb82eaea4d172534f26de05e8a7f
        A/table-images/TABLE-3-page-4-1.png: 24b25a43bfcd501e0fc3a12978a7b230a0b77addcc060e1967dbee85d94d0431
        A/table-images/manifest.json: d258e1b7cb873007e19fd311bda4f4aa973a96a7d1ac33d8d835cecb7f19773a
        A/table-images/TABLE-2-page-5-1.png: bf4d552af2e0882a2e00a6ba78948bf37b66e6bdb6f4cc449f0702465f5e1edc
        A/clauses/window-03/raw.json: a7a9b96984d19923c7275a9ca49f54ed0607171671f37b8186d7c32dfbf0ecd9
        A/clauses/window-03/prompt.txt: d05056f1a89c582bffc7e2c0904a18cf46e58af3b9dc4d03d7378ed99ee73055
        A/clauses/window-03/meta.json: b75cf9490483e4ca44dce61690297b1a559a9c40774f2c672dfeed462670aba7
        A/clauses/window-04/raw.json: be1a41e04c590d35f7543e342338deecaea74e1b9b8066045d5f94c77b8dece3
        A/clauses/window-04/prompt.txt: c420b47140d22b8ed48e56dc10571338833f36593a01b8a8631b76cadb67d963
        A/clauses/window-04/meta.json: b4ad11ce8ba46fa29e99e670dc8f2dae9c101c310f6defa8ac9a0fb89d9ea5b3
        A/clauses/window-05/raw.json: 1e84ce055c73449930fd374d632f56f90946fa343aae46c8befd13108fd7d570
        A/clauses/window-05/prompt.txt: 0836f6b520a89f74b7caf36d580f48c4c3fb4a7dd99fe8af99364762abd4480d
        A/clauses/window-05/meta.json: 34d681203e42634ec9c54f06f4db7913b0e638003f6773a7292689d46f983eec
        A/clauses/window-02/raw.json: 2b012915bb087cb7fb7097442c65ee22473af60188304fdd86e8d0937d07fb00
        A/clauses/window-02/prompt.txt: 7438424c0a99082a4f39d32648e2d0045def8c6895608167d127a2cc6d2ab81c
        A/clauses/window-02/meta.json: c9d10c560cd9710f73cb5eabdc99bcd8269763e18878e99ba850766419c4edef
        A/clauses/window-07/raw.json: 2a1a63b51204598bdb78a5bb1913ad3b6990a31cd5778013dd7c54dde92cd6e9
        A/clauses/window-07/prompt.txt: e1f01f68ab3577a102f558334c115ca8328124e0ecd2f2c2bc0004a875d31149
        A/clauses/window-07/meta.json: 55624713f570a9f01788058f4c4a9d36ea4725419917ebd5edda39930ca3d88c
        A/clauses/window-01/raw.json: 8a6bf0e6999a06bbe21ecb7c3f3f51d64d2dede96249a90438ec82bd99f59c91
        A/clauses/window-01/prompt.txt: 2642cf5e7111a398485fe94a3317742574605961ee7bf10a606c48a594bef565
        A/clauses/window-01/meta.json: 10cfd7b2e0bb0fa246ab3c4e40a1ff45fa5ace50b95a45c8bf1945e0bdef2243
        A/clauses/window-06/raw.json: baa7bc55159664ba26428725f9646e7d5cf9b7b0bf1a8183c183ef69858eb67e
        A/clauses/window-06/prompt.txt: 278e5cad7b389e821bbe6558ceff8060f667ef05515aaa885899a8faab0753a3
        A/clauses/window-06/meta.json: 7077b14b09738cdfe60de08f2bfbbc7c1f906907aa1449fdf384d4ed49f1d748
        A/tables/TABLE-2-page-5-3/raw.json: 789e10b7265c87ceac8785ad31e37439b43d0c1890802ce3144188753f2b2b8e
        A/tables/TABLE-2-page-5-3/prompt.txt: 66910199cf32a47354ad4f0b0885491ee572a8cda3b0e895f0a116d28e0ad8a8
        A/tables/TABLE-2-page-5-3/meta.json: 39ddb7c60819874436e0bd0247b4d7753cc2b7334be6785bd85c46cfda74fd29
        A/tables/TABLE-3-page-6-4/raw.json: 80723b0050c88336b96afed54c5bb7c5123ff82c65ba077f771781ea30f1a43f
        A/tables/TABLE-3-page-6-4/prompt.txt: 9998f8af7fe458e190bd84e8e4322495407c1296371a84cb2d9b52bf1fcba377
        A/tables/TABLE-3-page-6-4/meta.json: f6c20df743a279201ff9137e798088debd6540953f02c73d6c93d10da260d29c
        A/tables/TABLE-1-page-3-1/raw.json: 553b097a75028aca8e07bf14bf855d4de8e7874ea65401b19b19138b52c75ad4
        A/tables/TABLE-1-page-3-1/prompt.txt: c7462a47058aa689f54f27a900cdb37ed24e1489616fa2168aed234a71d76331
        A/tables/TABLE-1-page-3-1/meta.json: e35d2f5b0740a64be895b4b597bd0e3966ee53d0889459a03eba88ee3bb2afd2
        A/tables/TABLE-3-page-4-2/raw.json: 72f113091e0a5e6ada53f9630e73232a32d8e7643308732f92970b6175b99eba
        A/tables/TABLE-3-page-4-2/prompt.txt: c1ebe816f4675640dadac379ed61f0ee739ab5a6bdad4822885e88933f007ef6
        A/tables/TABLE-3-page-4-2/meta.json: 9d68762f5ea9880d0b7c064fe7f6000c4ccabb43c5ec5174f82972b5b05998bb
        B/passages.json: 689fd7157569f68eb45c9f81a0027af0c0d0d43dd7bf37d685f8ae3b00a8ffdb
        B/raw.json: 6a7df41ef0939ff22a7a8a37e565f7de760b7993e4e510a2dbb6aa8b977d7ed3
        B/source-units.json: 1abe2ef669f0df2be0f35bd00cad43113b9d581dc783b28389f3dce8ecac07d0
        B/full-source-units.json: 6f05421aeeb100409c7304fea6bc1d916c536a16efb7aeda11cd2c2e38b1d3e5
        B/meta.json: 52d2500686da4ca5d802a6d21a1025e8a49346b15a3de60f1b1dd4848c59c312
        B/table-images/TABLE-1-page-3-1.png: 3214fa8740d31c679f31570b4ef78ccff12a8484e5ab14c9cc50cb406168d080
        B/table-images/page-3.png: 1a286e345c6c5de0c095d75672c9c967a19dd00a29be8293a0b5954bcffd80f1
        B/table-images/page-6.png: 2405398c651e4c6750df132f221f62dd0ee09cf6298953ecb88f4bd0da216813
        B/table-images/page-5.png: f47ca70229f30aa8198030ebc111c2a372646a414f67762801986367ccd30358
        B/table-images/page-4.png: 88179e4936574bcdf8420d768b33a2e8c3652db84c4f805db77e79a14babebb2
        B/table-images/TABLE-3-page-6-1.png: beeb343531e826d361222205355a3ea2992bcb82eaea4d172534f26de05e8a7f
        B/table-images/TABLE-3-page-4-1.png: 24b25a43bfcd501e0fc3a12978a7b230a0b77addcc060e1967dbee85d94d0431
        B/table-images/manifest.json: c5c3543f7589b7a3c7a3a0e8a7e87ff9523032c5b51c11e263d4480f0af2a879
        B/table-images/TABLE-2-page-5-1.png: bf4d552af2e0882a2e00a6ba78948bf37b66e6bdb6f4cc449f0702465f5e1edc
        B/clauses/window-03/raw.json: 7ffd8f7c3d0fba18eb216dcd6dab53806baa26333c9fe2a9db02e6ff011527c5
        B/clauses/window-03/prompt.txt: d05056f1a89c582bffc7e2c0904a18cf46e58af3b9dc4d03d7378ed99ee73055
        B/clauses/window-03/meta.json: 0d22557f3f363fd45cedcad8a32348b34ada95ca00f655ab0ae1a7241332fc13
        B/clauses/window-04/raw.json: 4ce8dd87d5663a2be3ae2d95c576a6604f106e8db6d2c99bfba03f3e1db4cd5f
        B/clauses/window-04/prompt.txt: c420b47140d22b8ed48e56dc10571338833f36593a01b8a8631b76cadb67d963
        B/clauses/window-04/meta.json: 0c75928c160e70505641017c6359da68f8017d0f7dd15f39b62db33d5cccdb5d
        B/clauses/window-05/raw.json: 6ae4ed7445e9f7ee5b7a6d2ed0a541cdb460123dcd2a2529fb2f88f7c29b839c
        B/clauses/window-05/prompt.txt: 0836f6b520a89f74b7caf36d580f48c4c3fb4a7dd99fe8af99364762abd4480d
        B/clauses/window-05/meta.json: 6558172ac4c6613473ee91e84e8cbbbfcd5cac5d91665006cb44af4aeecdc928
        B/clauses/window-02/raw.json: 5b03b4af76fe520ec08e3ea4757754fea35a5ea91340a31284aba148a4fdc349
        B/clauses/window-02/prompt.txt: 7438424c0a99082a4f39d32648e2d0045def8c6895608167d127a2cc6d2ab81c
        B/clauses/window-02/meta.json: bf20c42c89806f66ae7dd2a0553730bddde4565f7932952ace3893c0a0f0a7b8
        B/clauses/window-07/raw.json: 593f7c26ad7a1df680b074a90cc64b3f8a9219080404fe04a1992c49ead43c5f
        B/clauses/window-07/prompt.txt: e1f01f68ab3577a102f558334c115ca8328124e0ecd2f2c2bc0004a875d31149
        B/clauses/window-07/meta.json: 581faa2d43b620c027673e040f4a7f92155f87254f31d069c840b315c3b406e9
        B/clauses/window-01/raw.json: baf87158c925a240c427f18a40c4ef5823d413eccb2465d165ea41b8db4c83a8
        B/clauses/window-01/prompt.txt: 2642cf5e7111a398485fe94a3317742574605961ee7bf10a606c48a594bef565
        B/clauses/window-01/meta.json: b6528c6e694633d5372c2e9769ee697e019a66f495efe6495108ec8fb03df673
        B/clauses/window-06/raw.json: f8ca74e509bae9b2e2ffb2a08067b1d8befa771266aac3d879e2fc6cd7a9e5c2
        B/clauses/window-06/prompt.txt: 278e5cad7b389e821bbe6558ceff8060f667ef05515aaa885899a8faab0753a3
        B/clauses/window-06/meta.json: 2b4913022346723a72df5098914711fcf6a1c2c381b59e4d5fbf960ca0c917d5
        B/tables/TABLE-2-page-5-3/raw.json: 2e19f6ab950f48da1764f3a73dbcce2c8f39ba5d4fce370970bc0f9b4192891c
        B/tables/TABLE-2-page-5-3/prompt.txt: 66910199cf32a47354ad4f0b0885491ee572a8cda3b0e895f0a116d28e0ad8a8
        B/tables/TABLE-2-page-5-3/meta.json: c9f9b972d4fff253f9e9442bf9e28470d0b0ce5aaba39c65d28694f3af84ab1c
        B/tables/TABLE-3-page-6-4/raw.json: 044c32cea9972b2f51af59e1356369d26df6253e4c94709b63cec53fa4d3f7a2
        B/tables/TABLE-3-page-6-4/prompt.txt: 9998f8af7fe458e190bd84e8e4322495407c1296371a84cb2d9b52bf1fcba377
        B/tables/TABLE-3-page-6-4/meta.json: 6a50b22fd1bcba6ffef82dca18928b3266f1503e81370766a444a64311c9cd2a
        B/tables/TABLE-1-page-3-1/raw.json: a541bfe7d8075e139bd619ba763dd2fce23d5965be3ba529bed4f1da7dcff4e6
        B/tables/TABLE-1-page-3-1/prompt.txt: c7462a47058aa689f54f27a900cdb37ed24e1489616fa2168aed234a71d76331
        B/tables/TABLE-1-page-3-1/meta.json: f02209ae47f5ed6b3ff0ddbab21e874c5b220abce0a2ecef0bd9f63f418a97b1
        B/tables/TABLE-3-page-4-2/raw.json: d0318857126dfd21670f6a4310d7df9f2c5d054739f0f83432980b8e40c5a100
        B/tables/TABLE-3-page-4-2/prompt.txt: c1ebe816f4675640dadac379ed61f0ee739ab5a6bdad4822885e88933f007ef6
        B/tables/TABLE-3-page-4-2/meta.json: e8ac4c36d7a0c6b930425e8547d8661bd5dd7fe5d6fab363bd890a0725c6a36a
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
      pdf_sha256: 33521110ebe2c8dcb01c2dbbfe5d81e8687899afe9b62c31ed91166320cd31b2
      source_review: _compare/relationships-2026-11-16/review-current/Raymer
      source_status_sha256: 0c6fa6a490f6659d2263f007d86d80cd9f7bee5df0eddc9247b95e5025bbb93a
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R004
    exposure:
      text: Constraint-induced language therapy (CILT)
    outcome:
      text: generalized language effects
    analysis_label: MA (standardized language measures)
    relation: association
    evidence_ids:
    - P1-S1-C14
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
      pdf_sha256: 33521110ebe2c8dcb01c2dbbfe5d81e8687899afe9b62c31ed91166320cd31b2
      source_review: _compare/relationships-2026-11-16/review-current/Raymer
      source_status_sha256: 0c6fa6a490f6659d2263f007d86d80cd9f7bee5df0eddc9247b95e5025bbb93a
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P1-S1-C7
      - Result passage disposed without unit P1-S1-C9
      - Result passage disposed without unit P2-S3-C4
      - Result passage disposed without unit P3-S1-C8
      - Result passage disposed without unit P3-S1-C9
      - Result passage disposed without unit P3-S1-C10
      - Result passage disposed without unit P3-S1-C11
      - Result passage disposed without unit P3-S1-C12
      - Result passage disposed without unit P3-S1-C13
      - Result passage disposed without unit P3-S1-C14
      - Result passage disposed without unit P3-S1-C15
      - Result passage disposed without unit P3-S1-C16
      - Result passage disposed without unit P3-S2-C1
      - Result passage disposed without unit P3-S2-C2
      - Result passage disposed without unit P3-S2-C3
      - Result passage disposed without unit P3-S2-C4
      - Result passage disposed without unit P3-S2-C5
      - Result passage disposed without unit P4-S1-C1
      - Result passage disposed without unit P4-S1-C10
      - Result passage disposed without unit P4-S1-C11
      - Result passage disposed without unit P4-S1-C12
      - Result passage disposed without unit P4-S1-C13
      - Result passage disposed without unit P4-S1-C9
      - Result passage disposed without unit P4-S1-C14
      - Result passage disposed without unit P4-S2-C3
      - Result passage disposed without unit P4-S2-C4
      - Result passage disposed without unit P4-S2-C5
      - Accounting without a linked unit P4-S2-C6
      - Accounting without a linked unit P4-S2-C7
      - Accounting without a linked unit P4-S2-C8
      - Result passage disposed without unit P4-S2-C9
      - Unaccounted source passage P4-S2-C7
      - Unaccounted source passage P4-S2-C8
      - Unaccounted source passage P4-S2-C6
      - Result passage disposed without unit P7-S1-C1
      - Result passage disposed without unit P7-S1-C2
      - Result passage disposed without unit P7-S1-C3
      - Result passage disposed without unit P7-S1-C6
      - Result passage disposed without unit P7-S1-C14
      - Result passage disposed without unit P7-S2-C11
      - Result passage disposed without unit P7-S2-C2
      - Result passage disposed without unit P7-S3-C2
      - Result passage disposed without unit P7-S3-C4
      - Result passage disposed without unit P7-S3-C5
      - Result passage disposed without unit P7-S3-C6
      - Result passage disposed without unit P7-S3-C7
      - Result passage disposed without unit P7-S3-C8
      - Result passage disposed without unit P8-S1-C13
      - Result passage disposed without unit P8-S2-C4
      - Result passage disposed without unit P8-S2-C8
      - Result passage disposed without unit P9-S1-C1
      unattached_null_or_qualifier_ids:
      - P3-S1-C15
      - P3-S2-C4
      - P3-S2-C5
      - P4-S1-C1
      - P4-S1-C9
      - P4-S2-C7
      - P7-S3-C7
      - P8-S2-C8
      suppressed_nonrepresented_units: 32
      default_disposition_count_requires_completeness_check: 118
      unselected_timing_passages: []
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P4-S2-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S2-C12
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S3-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      empty_frame_slots_require_confirmation:
      - imaging_provenance
      - imaging_timing
      - outcome_timing
      - validation
      - analysis_restrictions
      - personal_factors
      - tested_personal_effects
      - adjustment_roles
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-3-1
      - TABLE-2-page-5-3
      - TABLE-3-page-4-2
      - TABLE-3-page-6-4
      unlinked_tables:
      - TABLE-1-page-3-1
      - TABLE-2-page-5-3
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
      pdf_sha256: 33521110ebe2c8dcb01c2dbbfe5d81e8687899afe9b62c31ed91166320cd31b2
      source_review: _compare/relationships-2026-11-16/review-current/Raymer
      source_status_sha256: 0c6fa6a490f6659d2263f007d86d80cd9f7bee5df0eddc9247b95e5025bbb93a
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the number and type of SRs identified.
    - source_id: P1-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the application of the AMSTAR 2 tool.
    - source_id: P1-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the quality of the SRs.
    - source_id: P1-S1-C11
      disposition: represented
      result_indexes:
      - 0
      reason: Reports positive effects of CILT in descriptive summaries.
    - source_id: P1-S1-C12
      disposition: represented
      result_indexes:
      - 1
      reason: Reports that MA effects often did not surpass comparison treatments.
    - source_id: P1-S1-C13
      disposition: represented
      result_indexes:
      - 2
      reason: Reports positive MA findings for trained naming items.
    - source_id: P1-S1-C14
      disposition: represented
      result_indexes:
      - 3
      reason: Reports limited generalized CILT effects in MAs.
    - source_id: P1-S1-C15
      disposition: repeated
      result_indexes:
      - 4
      reason: Restatement of CILT leading to improvements.
    - source_id: P1-S2-C3
      disposition: represented
      result_indexes:
      - 4
      reason: Conclusion that CILT led to improvements.
    - source_id: P2-S3-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the identification of SR papers.
    - source_id: P3-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports inter-rater reliability for AMSTAR 2.
    - source_id: P3-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the range of AMSTAR 2 scores.
    - source_id: P3-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes funding/conflict of interest reporting.
    - source_id: P3-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes PICO format implementation.
    - source_id: P3-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes detail of included studies.
    - source_id: P3-S1-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes risk of bias assessment.
    - source_id: P3-S1-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes duplicate selection and extraction.
    - source_id: P3-S1-C15
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes summary of evidence relative to quality.
    - source_id: P3-S1-C16
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes statistical combination and risk of bias reporting.
    - source_id: P3-S2-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes MA statistical findings.
    - source_id: P3-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes lacking appraisal items.
    - source_id: P3-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes missing critical domains.
    - source_id: P3-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes lacking items regarding study design and funding.
    - source_id: P3-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes specific SR quality (Balardin & Miotto).
    - source_id: P3-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes other SRs' AMSTAR 2 performance.
    - source_id: P4-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes SR quality.
    - source_id: P4-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes specific SR quality (Cherney 2008).
    - source_id: P4-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes specific SR quality (Cherney 2010, Zhang 2017).
    - source_id: P4-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes specific SR quality (Pierce 2019).
    - source_id: P4-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes specific SR quality (Wang 2020).
    - source_id: P4-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes overall AMSTAR 2 confidence scale.
    - source_id: P4-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes number of studies in SRs.
    - source_id: P4-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes total participants in SRs.
    - source_id: P4-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes aphasia recovery phase.
    - source_id: P4-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes aphasia type and severity.
    - source_id: P4-S1-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes variation in comparison treatments.
    - source_id: P4-S1-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes types of comparison treatments.
    - source_id: P4-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about positive findings in original studies.
    - source_id: P4-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about varied MA findings.
    - source_id: P4-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes use of aphasia test batteries.
    - source_id: P4-S2-C6
      disposition: represented
      result_indexes:
      - 6
      reason: Reports positive results for aphasia batteries in descriptive SR.
    - source_id: P4-S2-C7
      disposition: represented
      result_indexes:
      - 7
      reason: Reports limited advantages for aphasia batteries in MAs.
    - source_id: P4-S2-C8
      disposition: represented
      result_indexes:
      - 8
      reason: Reports specific AAT and WAB results in quantitative synthesis.
    - source_id: P4-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes naming measures used.
    - source_id: P4-S2-C10
      disposition: represented
      result_indexes:
      - 9
      reason: Reports naming improvements in descriptive SR.
    - source_id: P4-S2-C11
      disposition: represented
      result_indexes:
      - 10
      reason: Reports positive MA effects for trained naming stimuli.
    - source_id: P4-S2-C12
      disposition: represented
      result_indexes:
      - 11
      reason: Reports non-significant generalized naming improvements in MAs.
    - source_id: P4-S2-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about patterns in other measures.
    - source_id: P4-S2-C14
      disposition: represented
      result_indexes:
      - 13
      reason: Reports positive effects for comprehension, repetition, and speech in
        descriptive SR.
    - source_id: P4-S3-C2
      disposition: represented
      result_indexes:
      - 14
      reason: Reports no significant MA effects for comprehension, repetition, and
        speech.
    - source_id: P4-S3-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about maintenance of effects.
    - source_id: P4-S3-C4
      disposition: represented
      result_indexes:
      - 15
      reason: Reports lasting effects beyond 1 month.
    - source_id: P4-S3-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes reporting of activity/participation measures.
    - source_id: P4-S3-C6
      disposition: represented
      result_indexes:
      - 16
      reason: Reports discourse outcomes favoring CILT or showing no advantage.
    - source_id: P4-S3-C7
      disposition: represented
      result_indexes:
      - 17
      reason: Reports communication log results favoring CILT.
    - source_id: P4-S3-C8
      disposition: represented
      result_indexes:
      - 18
      reason: Reports communication rating scale results favoring CILT.
    - source_id: P4-S3-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: States metrics were not amenable to quantitative synthesis.
    - source_id: P7-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes number of SRs identified.
    - source_id: P7-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes number of original studies.
    - source_id: P7-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes number of RCTs.
    - source_id: P7-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about varied answers to effectiveness.
    - source_id: P7-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about optimistic conclusions when all designs are
        included.
    - source_id: P7-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about limited positive outcomes in RCT-only MAs.
    - source_id: P7-S1-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: States variety of measures precluded quantitative analysis.
    - source_id: P7-S2-C2
      disposition: repeated
      result_indexes:
      - 17
      reason: Restatement of positive outcomes for communication logs.
    - source_id: P7-S2-C8
      disposition: represented
      result_indexes:
      - 19
      reason: Reports CILT effects are often no different than multimodality treatments
        at comparable intensity.
    - source_id: P7-S2-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about methodological quality of SRs.
    - source_id: P7-S3-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: States all six SRs lacked critical domains.
    - source_id: P7-S3-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes lack of established protocols.
    - source_id: P7-S3-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes lack of search details.
    - source_id: P7-S3-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes varied subsets of studies across reviews.
    - source_id: P7-S3-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes lack of excluded studies lists.
    - source_id: P7-S3-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes lack of publication bias consideration.
    - source_id: P8-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes reliability of AMSTAR 2 ratings.
    - source_id: P8-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes lack of critical domains in SRs.
    - source_id: P8-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: General summary statement of CILT effectiveness.
    - source_id: P8-S3-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes Intensive Comprehensive Aphasia Programs (ICAPs).
    unresolved_coverage:
    - source_id: P4-S3-C6
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P4-S3-C7
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P4-S3-C8
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P7-S1-C11
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P7-S2-C8
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P8-S3-C2
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P8-S1-C13
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S2-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S2-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S3-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S3-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S3-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S1-C1
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C7
    - P1-S1-C9
    - P1-S1-C10
    - P1-S1-C15
    - P2-S3-C4
    - P3-S1-C8
    - P3-S1-C9
    - P3-S1-C10
    - P3-S1-C11
    - P3-S1-C12
    - P3-S1-C13
    - P3-S1-C14
    - P3-S1-C15
    - P3-S1-C16
    - P3-S2-C1
    - P3-S2-C2
    - P3-S2-C3
    - P3-S2-C4
    - P3-S2-C5
    - P3-S2-C6
    - P4-S1-C1
    - P4-S1-C2
    - P4-S1-C3
    - P4-S1-C4
    - P4-S1-C5
    - P4-S1-C6
    - P4-S1-C9
    - P4-S1-C10
    - P4-S1-C11
    - P4-S1-C12
    - P4-S1-C13
    - P4-S1-C14
    - P4-S2-C3
    - P4-S2-C4
    - P4-S2-C5
    - P4-S2-C9
    - P4-S2-C13
    - P4-S3-C3
    - P4-S3-C5
    - P4-S3-C9
    - P7-S1-C1
    - P7-S1-C2
    - P7-S1-C3
    - P7-S1-C6
    - P7-S1-C9
    - P7-S1-C14
    - P7-S2-C2
    - P7-S2-C11
    - P7-S3-C2
    - P7-S3-C4
    - P7-S3-C5
    - P7-S3-C6
    - P7-S3-C7
    - P7-S3-C8
    - P8-S1-C8
    - P8-S1-C13
    - P8-S2-C4
    - P8-S2-C6
    - P8-S2-C7
    - P8-S2-C8
    - P8-S3-C5
    - P8-S3-C6
    - P8-S3-C7
    - P9-S1-C1
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-3-1
    - TABLE-2-page-5-3
    - TABLE-3-page-4-2
    - TABLE-3-page-6-4
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P2-S3-C4
      recruited_sample:
      - P2-S3-C2
      eligibility:
      - P2-S3-C3
      - P4-S1-C11
      - P4-S1-C12
      imaging_provenance: []
      imaging_timing: []
      outcome_timing: []
      outcome_definition:
      - P2-S2-C12
      - P4-S1-C15
      - P4-S2-C5
      - P4-S2-C9
      - P4-S3-C5
      - P6-S1-C2
      validation: []
      analysis_restrictions: []
      dependent_variable_statement:
      - P2-S2-C12
      limitations:
      - P7-S3-C4
      - P7-S3-C5
      - P7-S3-C8
      - P8-S1-C4
      - P8-S1-C5
      - P8-S1-C6
      - P8-S1-C7
      - P8-S1-C9
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles: []
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P4-S1-C10
      - P4-S1-C11
      - P4-S1-C12
      - P5-S1-C3
    outcome_type: change_from_baseline
    imaging_vs_outcome: not_stated
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P4-S2-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S2-C12
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S3-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C8
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
      pdf_sha256: 33521110ebe2c8dcb01c2dbbfe5d81e8687899afe9b62c31ed91166320cd31b2
      review_sha256: 208e58450578e1e01e3e485633efe261728e0eb6fa1eb494708b6fb7f9173ea1
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
    approved: false
    core_review:
      own_result_source_ids:
      - P1-S1-C14
      source_result: The source states that 'Generalized CILT effects for standardized
        language measures were limited in two other MAs.' This indicates that in two
        of the three meta-analyses examined, the effects of CILT on generalized standardized
        language measures were not robust or were small/limited, contrasting with
        the positive findings in the third MA (which focused on trained items).
      result_status: not_detected
      patient_measurement: non_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis R004 correctly identifies the source as P1-S1-C14,
            which discusses the findings of two specific meta-analyses regarding generalized
            language measures. The draft correctly identifies this as a synthesis
            of MAs.
          source_ids:
          - P1-S1-C14
          - P1-S1-C12
          - P1-S1-C13
        direction:
          answer: fits
          reason: The source states effects were 'limited'. The draft uses the direction
            'unlikely' and the claim 'effects... were limited'. This accurately reflects
            the lack of strong positive association (or limited effect size) found
            in those specific MAs, without falsely claiming a null effect of zero
            or a negative effect.
          source_ids:
          - P1-S1-C14
        construct:
          answer: fits
          reason: The exposure is CILT, the outcome is generalized language effects
            measured by standardized language measures. The patient measurement is
            non_imaging (standardized language tests), which is correct as this is
            a clinical/behavioral outcome, not an imaging metric. The draft correctly
            identifies the population as stroke-induced aphasia.
          source_ids:
          - P1-S1-C14
          - P1-S1-C3
          - P1-S2-C6
        qualifications:
          answer: fits
          reason: The draft includes the qualification that the finding is based on
            a synthesis of six SRs, specifically two MAs. It also includes the limitation
            that the SRs lacked critical domains. These are material qualifiers present
            in the source (P1-S1-C10, P1-S1-C14).
          source_ids:
          - P1-S1-C14
          - P1-S1-C10
          - P1-S1-C7
        missing_material_caveat:
          answer: fits
          reason: The draft captures the key caveat that the effects were limited
            in 'two other MAs', implying a contrast with the third MA which showed
            positive effects for trained items (P1-S1-C13). It also notes the quality
            limitations of the underlying SRs. No material caveat is omitted that
            would change the interpretation of the 'limited' finding.
          source_ids:
          - P1-S1-C13
          - P1-S1-C14
          - P1-S1-C10
      optional_pending:
      - Specific effect sizes or confidence intervals from the two MAs are not transcribed.
      - Details of the specific standardized language measures used in the two MAs
        are not transcribed.
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Specific effect sizes or confidence intervals from the two MAs are not transcribed.
    - Details of the specific standardized language measures used in the two MAs are
      not transcribed.
    normalizations: []
    analysis_identity:
      id: R004
      exposure:
        text: Constraint-induced language therapy (CILT)
      outcome:
        text: generalized language effects
      analysis_label: MA (standardized language measures)
      relation: association
      evidence_ids:
      - P1-S1-C14
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
        pdf_sha256: 33521110ebe2c8dcb01c2dbbfe5d81e8687899afe9b62c31ed91166320cd31b2
        source_review: _compare/relationships-2026-11-16/review-current/Raymer
        source_status_sha256: 0c6fa6a490f6659d2263f007d86d80cd9f7bee5df0eddc9247b95e5025bbb93a
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings: {}
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 1
  quote: 'Generalized CILT effects for standardized

    language measures were limited in two other MAs.'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-25'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
