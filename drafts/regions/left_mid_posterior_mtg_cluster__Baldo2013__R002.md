---
id: left_mid_posterior_mtg_cluster
name: left mid- to posterior MTG cluster
kind: network
findings:
- id: f1
  target_audit:
    status: construct_separated
    category: behaviour_or_language_construct
    original_target: bnt_naming_performance
    reason: Separated the construct from the score/task using the published claim and linked source passages.
      This is metadata correction, not scientific approval.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  outcome_measurement:
    status: identified
    instruments:
    - name: Boston Naming Test
    metric: bnt naming performance
    note: Task conditions, covariates, change metric and timing remain in the claim and source passages.
      Instrument version/subtests require final source verification.
  target: picture_naming
  target_kind: impairment
  claim: Lesions in the left mid- to posterior middle temporal gyrus (BA 21 and 37)
    and underlying white matter are associated with impaired picture naming performance
    on the BNT, a relationship that remains significant when controlling for speech
    production fluency and visual recognition deficits.
  direction: likely
  relationship: correlational
  method: VLSM
  sample:
    n: 96
    population: Native English speakers, right-handed, with a single left hemisphere
      stroke
    phase: not_reported
    time_post_onset: Chronic phase of stroke (at least 10 months post-injury)
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Lesion reconstruction methods may not register all dysfunctional tissue, especially
    in very large lesions
  - Lesion coverage did not include the entire left temporal pole, only superior portions
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Patient lesion overlap with voxels in the left mid-
    to posterior middle temporal gyrus (Brodmann areas 21 and 37) and the white matter
    immediately adjacent/medial to the MTG. Analysis controlled for speech production
    using WAB speech fluency scores; Analysis controlled for visual recognition using
    a 3-choice BNT recognition task; Analysis controlled for age and education. Additional
    metadata has not been transcribed; review the pending-field flags before approval.
    PDF image reading (P3-S1-C9, two-model agreement, human verification pending):
    Methods


    Participants


    The study sample included 96 participants (21 female) who had suffered a single
    LH stroke Original text-layer quotation is preserved below. PDF image reading
    (P3-S1-C10, two-model agreement, human verification pending): . Study criteria
    included being

    a native English speaker, right-handed, and in the chronic

    phase of stroke (at least 10 months post-injury) so that

    behaviors were stabilized Original text-layer quotation is preserved below.'
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
    - proposed_concept:bnt_naming_performance
  citation: '@Baldo2013'
  source_passages:
  - section: Original source P5-S1-C14
    page: 5
    quote: 'When we re-ran the VLSM

      analysis with overall speech ﬂuency as a covariate, the

      signiﬁcant voxels were restricted primarily to the mid- to

      posterior portion of the MTG (BA 21 and 37), again with some

      extension into the white matter just medial to the MTG (see

      '
    supports: claim
  - section: Original source P5-S2-C1
    page: 5
    quote: 'signiﬁcant voxels were restricted primarily to the mid- to

      posterior portion of the MTG (BA 21 and 37), again with some

      extension into the white matter just medial to the MTG (see

      Fig. 4).'
    supports: claim
  - section: Original source P6-S2-C1
    page: 6
    quote: 'posterior MTG and underlying white matter, suggesting that

      this region is critical for the middle stage described above,

      lexical-semantic retrieval.'
    supports: claim
  - section: Original source P3-S1-C9
    page: 3
    quote: 'Methods

      Participants

      The study sample included 96 participants (21 female) who

      had suffered a single LH stroke.'
    supports: sample
  - section: Original source P3-S1-C10
    page: 3
    quote: 'Study criteria included being

      a native English speaker, right-handed, and in the chronic

      phase of stroke (at least 10 months post-injury) so that

      behaviors were stabilized.'
    supports: sample
  - section: Original source P4-S2-C3
    page: 4
    quote: 'Lesion analysis

      To determine the anatomic correlates of picture naming on

      the BNT, we applied VLSM analyses to the lesion and behav-

      ioral data (http://neuroling.arizona.edu/resources.html; see

      Baldo et al., 2012; Bates et al., 2003).'
    supports: method
  - section: Original source P4-S1-C8
    page: 4
    quote: 'It should be noted that lesion

      reconstruction methods have limitations and that in some

      cases, there is likely lesioned/dysfunctional tissue that is not

      registered with these techniques, especially in the case of

      patients with very large lesions (Rorden and Karnath, 2004).'
    supports: limitation
  - section: Original source P7-S1-C10
    page: 7
    quote: 'It should be noted that lesion coverage in our patient

      sample did not include the entire left temporal pole but rather

      only superior portions of the left superior temporal pole,

      which may explain the discrepant ﬁndings.'
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-20'
relationship_review:
  paper: Baldo2013
  proposal_id: R002
  review_status_sha256: 6657822f97cc610a596b1702b41826fe1a100a03948f42895412d12e30e8d27a
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 76b1c80b0b15c0ab14ff9446684badad37b4d101edb13f7625b9e48dca8359b3
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 76b1c80b0b15c0ab14ff9446684badad37b4d101edb13f7625b9e48dca8359b3
        A/passages.json: 0426e01bf47bc43bcdd6fc9c489284b1a847d0d2dcc1633d778640c785cd744e
        A/raw.json: b0c8b84f4e0991aaf71b9323961c2c6abd887e5d4608c522a1b9b515df3947f6
        A/source-units.json: f992569ea3816680234e93a20620942aa3a5f6797a04c7286fef70cfe0b35dfc
        A/full-source-units.json: f992569ea3816680234e93a20620942aa3a5f6797a04c7286fef70cfe0b35dfc
        A/meta.json: 0915beec01e9cddec0000522d95ba1d7ca7068f48412e5fcea7c0f72499e286b
        A/table-images/manifest.json: cd00bd93cd913d822284e2b721e67807484782624b6615732f73924b14d1c7ab
        A/clauses/window-11/raw.json: 02ab4b7fd4eb00f1ae80e8813b75ffa416fc70c1e3a7954708a6f3e75a1c3eec
        A/clauses/window-11/prompt.txt: 6c20291a5ef826c306dbff6eff4e5d6ea67f1607bb1ad5d80c8beedae8f7a8f6
        A/clauses/window-11/meta.json: d994a5eb5f560f7a80fd1f1d42d90f71150abf00b98f9033ce28f68422f2fcbc
        A/clauses/window-10/raw.json: 59561a4e29415a4a761f734206ae1edf74898a22ba8760f9d3208d893768c975
        A/clauses/window-10/prompt.txt: 9daebd874e8cbd61bb4a42aefce4ad49aab5c3a87054401ba75781e58b5638a7
        A/clauses/window-10/meta.json: 1fa68c4789393a05c703c51ac90edebc610ee0e433117b3a23ee0a1d06ec828f
        A/clauses/window-03/raw.json: 915893b9e5fafcdd3a741dd6c31c3c8a739b1fcd9bd0e70335591c22458ae865
        A/clauses/window-03/prompt.txt: 05d741da1bcd181819083605b721101f78a4687efb402b4cae11ccdec3bfdabc
        A/clauses/window-03/meta.json: b3af7d16170461170e65c785518664355b4ff395a8b652d3345d63d32d420451
        A/clauses/window-04/raw.json: cbfeb7e388338db156c7d0ca5d3e37e926b2ba73b0e83cf20df401962a6cb470
        A/clauses/window-04/prompt.txt: 3b6dc95cd149909d5e5fe84c7f5d4958b3da4676d3a545ea8b8e8abe34c518de
        A/clauses/window-04/meta.json: 9936114eede8de2f62a6d8799d472ea6d6d70372a6d1770e5e293b74b1163a24
        A/clauses/window-05/raw.json: f8fe28d042fb1b858e3e9a6cbf9265a91c79a95ccc73ba455e2e5ac2653cad62
        A/clauses/window-05/prompt.txt: a8a4ca967fedc5ce422ad6f795aac0d24dfbad8dee18ec03b702bdf980b0cbf8
        A/clauses/window-05/meta.json: 9af67115e0b87a57c8b4fce4fae03c1b98eff66b2013fd8ede3d033446307c7d
        A/clauses/window-02/raw.json: d1c8be6f5d4405278a20e04e46d23eb7c8fe5c51a90c0e88154f3017fa283f47
        A/clauses/window-02/prompt.txt: 37d61589c8fdeb24c134fe2caf2c6970b6a0d34df9cb1bdd0dc7958b310f1253
        A/clauses/window-02/meta.json: dad9360a1d339bc9c5224b6007b8127dd3218ee2446e082f9cfd2911a6055747
        A/clauses/window-12/raw.json: 5d404ee9e911ff962e431ab2487b3ac327a145d1a45b093915abda0ac8919916
        A/clauses/window-12/prompt.txt: 6f4c8abfa8ea6eaaa62e27528d6cb59a5e4288d0518cb4c05c5ccf9008b56641
        A/clauses/window-12/meta.json: 505e9350b59f7e5507e63b23a08591edaa77a13ffd38b9b0d3fbd8c8b9d49eb0
        A/clauses/window-13/raw.json: 9b081808bb0c79155c98cad99774888b8e1fc586751fc1d91582c5919f16fa15
        A/clauses/window-13/prompt.txt: fe5c85209860d83ee3e6b8a33586184c2651e4ea10ef1f02f6a6cadf2d8075d9
        A/clauses/window-13/meta.json: cb65f48da5839c838893c9ac150372dd515483996209a8effa621bd52ef04566
        A/clauses/window-09/raw.json: 1a0fcabe7d173806e497e342745339716e785e3f21abe0e87da7b003065602cb
        A/clauses/window-09/prompt.txt: 6da46fe89fc9a25e0f55198ebcc6184102d8285fbe79ceeb899ddd5403354768
        A/clauses/window-09/meta.json: 1632d2f33d32f87e4c2e509a0ec881957766fb185e3ba0d1589217cd2b19897a
        A/clauses/window-07/raw.json: ea78315f6128827f0e9a72d94c727dffb7731ff27b3a4e932579e828e19be1d2
        A/clauses/window-07/prompt.txt: 50c4a59dd395a185baa576f111ed5fe9ec83575cfedbfba9ab7affd429d5887c
        A/clauses/window-07/meta.json: 2f9c2d3d63b713a34a1abbf7dccd002b1cfada65a0b7f235c48011cbbe82fd0b
        A/clauses/window-01/raw.json: 023fbcb59f206f3dfa70168602727c6b30a6fb5c7a9640c51a1e52362e775950
        A/clauses/window-01/prompt.txt: a7d81139cf25e909f829d0d24744f0339240c96e3117ab61856542b1bd44c597
        A/clauses/window-01/meta.json: 276bfb8616cb573236d35ad0cd95a8bc66b284f26311b1f11ac10c36226f705d
        A/clauses/window-06/raw.json: 7d166513758c04c3bc9027547c9ef15659994f2b18e7ef6b5a2b83a9dc37ae85
        A/clauses/window-06/prompt.txt: d584c642d0becb3e21ad618de2202d37718e0414608265fa45e7a77159da1f2e
        A/clauses/window-06/meta.json: 2ed6dbb4aedb2855324c9925bda94816bb9c95eed5dce0ffd1ef9c0748f2782e
        A/clauses/window-08/raw.json: 11f0c82303693416cc215e50fe6c063ccfde326e99a700cad2858e02d15f40d4
        A/clauses/window-08/prompt.txt: f19f44a6f24be145fb5e5420c433a60d0f864cab2516f9fa7f68dee55b383af1
        A/clauses/window-08/meta.json: c721189ea13aa90fd2db061a5f78ef821e576032d99898ce525ae7da37d0a5f9
        B/passages.json: 0426e01bf47bc43bcdd6fc9c489284b1a847d0d2dcc1633d778640c785cd744e
        B/raw.json: dedd9de5415f6c55e86f0f605ba4bef1696a298b057bf24ec4486bb6bd52e381
        B/source-units.json: f992569ea3816680234e93a20620942aa3a5f6797a04c7286fef70cfe0b35dfc
        B/full-source-units.json: f992569ea3816680234e93a20620942aa3a5f6797a04c7286fef70cfe0b35dfc
        B/meta.json: cd8ab36da6f1238cec0bb4a2f40923c53fa34a013011be9f314b0b219bf80fd4
        B/table-images/manifest.json: cd00bd93cd913d822284e2b721e67807484782624b6615732f73924b14d1c7ab
        B/clauses/window-11/raw.json: d816f6988d2ab427f1bac3e070ee485a6fad6f2ec7e43dce17fad14ffdc2b4c6
        B/clauses/window-11/prompt.txt: 6c20291a5ef826c306dbff6eff4e5d6ea67f1607bb1ad5d80c8beedae8f7a8f6
        B/clauses/window-11/meta.json: 762406c21f0a1030f1a906f94f8835ccbe17b85e1cba9b45cd09edd5a0a2c933
        B/clauses/window-10/raw.json: d5dd516774e936d33877c41bb3561a82b127db89ce2a2dd4f885c73588c6e552
        B/clauses/window-10/prompt.txt: 9daebd874e8cbd61bb4a42aefce4ad49aab5c3a87054401ba75781e58b5638a7
        B/clauses/window-10/meta.json: 6095793192d5cde7fff4c8273fefddebab30d57c258b93767ac9c51c3152c6d0
        B/clauses/window-03/raw.json: ed5407a65faa3dce4752913a7c27fbc7257eb0ce7d157ad17ef96bca504faa99
        B/clauses/window-03/prompt.txt: 05d741da1bcd181819083605b721101f78a4687efb402b4cae11ccdec3bfdabc
        B/clauses/window-03/meta.json: 219a2e45f686c85f6aab038b6aedf37594559d9a43e8669e779367ff1612f7f1
        B/clauses/window-04/raw.json: 99a10f647526be445ed2d2fba8a932681daa6b63b4bb902e813967c71d6980c1
        B/clauses/window-04/prompt.txt: 3b6dc95cd149909d5e5fe84c7f5d4958b3da4676d3a545ea8b8e8abe34c518de
        B/clauses/window-04/meta.json: f9a7ef0efed8efe42bf1db05418be7a09e74b5a10b3a7391740fa0a38b2637f6
        B/clauses/window-05/raw.json: 5b108ed09dc0f76ff5f81936ce1c570236bd6b1e37a5abad2f04d0e5ee3ce887
        B/clauses/window-05/prompt.txt: a8a4ca967fedc5ce422ad6f795aac0d24dfbad8dee18ec03b702bdf980b0cbf8
        B/clauses/window-05/meta.json: f2df3f5962c7ac0c1d31ef461441b452aa49f93a888c2ed4eda64124a343bcaf
        B/clauses/window-02/raw.json: 0224b6402a210cbb44530d24e5bcb516e594e542be309b9fcf6c08550f7fd71c
        B/clauses/window-02/prompt.txt: 37d61589c8fdeb24c134fe2caf2c6970b6a0d34df9cb1bdd0dc7958b310f1253
        B/clauses/window-02/meta.json: 0611f528720b5ccc5be89df3482e3cb1c316c984711881cf9a7186c7d5f7c4b6
        B/clauses/window-12/raw.json: 2fb6b0614ab9d4aab48a27e23dc90307efa6e9aaed716843ad0a02fb8cbdf59b
        B/clauses/window-12/prompt.txt: 6f4c8abfa8ea6eaaa62e27528d6cb59a5e4288d0518cb4c05c5ccf9008b56641
        B/clauses/window-12/meta.json: 80b17471ff9591551b62be5361f77ffc85ab45fa3acd9f8d3242245e0ddc74f9
        B/clauses/window-13/raw.json: 84fd293438a614ca0c830ac218fbd185ddd55f3fc92910122159882732887be7
        B/clauses/window-13/prompt.txt: fe5c85209860d83ee3e6b8a33586184c2651e4ea10ef1f02f6a6cadf2d8075d9
        B/clauses/window-13/meta.json: 1820d194f5c893c749cf835ac99b0e355a9c856c53e546e1a9cdaa4138139983
        B/clauses/window-09/raw.json: 6fba54bec7c39113e296eb3f7409dcba7497d151cbd59778b8dbb79b1f6f4106
        B/clauses/window-09/prompt.txt: 6da46fe89fc9a25e0f55198ebcc6184102d8285fbe79ceeb899ddd5403354768
        B/clauses/window-09/meta.json: b7810401d97969acb06d0434f89e7107c4e95b0a1a58937d56b67b9cba68efbb
        B/clauses/window-07/raw.json: 9b0aa5fce8b3f067c538c03fc103e92b29ed7dc0d7df7ffda6ff0ddc4fadbf8f
        B/clauses/window-07/prompt.txt: 50c4a59dd395a185baa576f111ed5fe9ec83575cfedbfba9ab7affd429d5887c
        B/clauses/window-07/meta.json: c3638cc7cb89e43ef1b6febba7f3944b97b81ef85637d2ecf3e1c19cda233505
        B/clauses/window-01/raw.json: 0df8ef81e1d848eb760ada47e35b7b45adf28d034985b0fed88487b375b80097
        B/clauses/window-01/prompt.txt: a7d81139cf25e909f829d0d24744f0339240c96e3117ab61856542b1bd44c597
        B/clauses/window-01/meta.json: a72babd1a3a0ced4164af8dcd63663cf762cf2f64a237552f2976749c9c58892
        B/clauses/window-06/raw.json: e9a2ef3dd7e9e4974f8ba8a5ff0452eb974c1137252f8f905a12cd2763f75d26
        B/clauses/window-06/prompt.txt: d584c642d0becb3e21ad618de2202d37718e0414608265fa45e7a77159da1f2e
        B/clauses/window-06/meta.json: 9b02e923564fc4e5b0ba446b23887b33d6f3f4a6e8ed65d198cee9255a702542
        B/clauses/window-08/raw.json: 71fac7758ea13dc4790ab4a299559a1744eceb368ab8e1afc4cc05f2585641fb
        B/clauses/window-08/prompt.txt: f19f44a6f24be145fb5e5420c433a60d0f864cab2516f9fa7f68dee55b383af1
        B/clauses/window-08/meta.json: 75d79de23d6b99224532e9f714a957141cdf198bd8085b17e9eee212d27351c1
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
      pdf_sha256: 76b1c80b0b15c0ab14ff9446684badad37b4d101edb13f7625b9e48dca8359b3
      source_review: _compare/relationships-2026-11-16/review-current/Baldo2013
      source_status_sha256: 32d2198af0a3114dd0bd5d2b1f79ef30be70603f13569c4cd91e53f62d02c5ce
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R002
    exposure:
      text: lesions in left mid- to posterior MTG (BA 21 and 37) and underlying white
        matter
    outcome:
      text: naming performance on the BNT
    analysis_label: VLSM of naming performance controlling for speech production
    relation: sensitivity
    evidence_ids:
    - P5-S1-C14
    - P5-S2-C10
    - P6-S2-C1
    qualifier_ids:
    - P5-S1-C12
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 76b1c80b0b15c0ab14ff9446684badad37b4d101edb13f7625b9e48dca8359b3
      source_review: _compare/relationships-2026-11-16/review-current/Baldo2013
      source_status_sha256: 32d2198af0a3114dd0bd5d2b1f79ef30be70603f13569c4cd91e53f62d02c5ce
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P1-S1-C10
      - Accounting without a linked unit P1-S1-C9
      - Accounting without a linked unit P2-S1-C10
      - Unaccounted source passage P2-S1-C10
      - Unaccounted source passage P1-S1-C9
      - Result passage disposed without unit P3-S2-C10
      - Result passage disposed without unit P4-S1-C11
      - Result passage disposed without unit P4-S1-C12
      - Result passage disposed without unit P4-S1-C15
      - Result passage disposed without unit P4-S2-C2
      - Result passage disposed without unit P5-S1-C1
      - Accounting without a linked unit P5-S1-C3
      - Accounting without a linked unit P5-S1-C4
      - Accounting without a linked unit P5-S1-C5
      - Accounting without a linked unit P5-S1-C6
      - Accounting without a linked unit P5-S1-C7
      - Accounting without a linked unit P5-S1-C8
      - Accounting without a linked unit P5-S1-C9
      - Unaccounted source passage P5-S1-C7
      - Unaccounted source passage P5-S1-C6
      - Unaccounted source passage P5-S1-C8
      - Unaccounted source passage P5-S1-C9
      - Unaccounted source passage P5-S1-C3
      - Unaccounted source passage P5-S1-C4
      - Unaccounted source passage P5-S1-C5
      - Result passage disposed without unit P5-S1-C10
      - Result passage disposed without unit P5-S2-C10
      - Accounting without a linked unit P7-S1-C9
      - Accounting without a linked unit P7-S2-C3
      - Accounting without a linked unit P7-S3-C5
      - Accounting without a linked unit P7-S3-C9
      - Unaccounted source passage P7-S3-C5
      - Unaccounted source passage P7-S2-C3
      - Unaccounted source passage P7-S1-C9
      - Unaccounted source passage P7-S3-C9
      unattached_null_or_qualifier_ids:
      - P1-S1-C10
      suppressed_nonrepresented_units: 6
      default_disposition_count_requires_completeness_check: 170
      unselected_timing_passages:
      - P3-S1-C10
      - P3-S1-C12
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P5-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: adjustment_roles
        source_ids:
        - P3-S1-C5
        - P3-S1-C6
        - P4-S3-C1
        - P4-S3-C2
        - P4-S3-C3
        - P4-S3-C4
        - P4-S3-C6
        - P4-S3-C7
        - P5-S1-C11
        - P5-S1-C12
        - P5-S1-C13
        - P5-S2-C4
        - P5-S2-C6
        - P6-S1-C5
        - P6-S1-C7
        - P6-S1-C8
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - personal_factors
      - tested_personal_effects
      - adjustment_roles
      - explicitly_not_adjusted
      unclassified_extraction_ids:
      - P4-S2-C15
      - P5-S3-C1
      table_review_required: []
      unlinked_tables: []
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P4-S1
        - P4-S2
        - P4-S3
        - P5-S1
        - P5-S2
        - P6-S2
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 76b1c80b0b15c0ab14ff9446684badad37b4d101edb13f7625b9e48dca8359b3
      source_review: _compare/relationships-2026-11-16/review-current/Baldo2013
      source_status_sha256: 32d2198af0a3114dd0bd5d2b1f79ef30be70603f13569c4cd91e53f62d02c5ce
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C9
      disposition: represented
      result_indexes:
      - 0
      reason: States association between BNT performance and LH network including
        MTG, STG, white matter, and inferior parietal cortex.
    - source_id: P1-S1-C10
      disposition: represented
      result_indexes:
      - 2
      reason: Describes the result of adding covariates (visual recognition and motor
        speech) to the analysis.
    - source_id: P3-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports mean WAB score for the sample.
    - source_id: P3-S3-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the subjective nature of providing semantic cues during BNT
        administration.
    - source_id: P4-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes lesion coverage of the middle cerebral artery.
    - source_id: P4-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports average lesion volume.
    - source_id: P4-S1-C15
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes statistical power in the left peri-Sylvian region.
    - source_id: P4-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes statistical power in the left peri-Sylvian region.
    - source_id: P5-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: References Table 1 for behavioral performance.
    - source_id: P5-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports average spontaneous naming score.
    - source_id: P5-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports average naming score with semantic cues.
    - source_id: P5-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports average naming score with phonemic cues.
    - source_id: P5-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports average recognition task score.
    - source_id: P5-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Introduces the VLSM analysis of spontaneous naming.
    - source_id: P5-S1-C7
      disposition: represented
      result_indexes:
      - 0
      reason: Identifies significant foci in MTG, STG, and white matter for spontaneous
        naming.
    - source_id: P5-S1-C8
      disposition: represented
      result_indexes:
      - 0
      reason: Specifies maximum t-value and location in white matter medial to MTG.
    - source_id: P5-S1-C9
      disposition: represented
      result_indexes:
      - 0
      reason: Specifies extension of significant voxels to temporal pole and inferior
        parietal cortex.
    - source_id: P5-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports the minimum cut-off t-value for the analysis.
    - source_id: P5-S1-C14
      disposition: represented
      result_indexes:
      - 1
      reason: Reports significant voxels restricted to mid-posterior MTG and white
        matter when controlling for fluency.
    - source_id: P5-S2-C1
      disposition: represented
      result_indexes:
      - 1
      reason: Reports significant voxels restricted to mid-posterior MTG and white
        matter when controlling for fluency.
    - source_id: P5-S2-C2
      disposition: represented
      result_indexes:
      - 1
      reason: Specifies maximum t-value and location for the fluency-controlled analysis.
    - source_id: P5-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports minimum t-value cut-off for the fluency-controlled analysis.
    - source_id: P5-S2-C6
      disposition: represented
      result_indexes:
      - 2
      reason: States significant regions were almost identical when adding recognition
        task as a covariate.
    - source_id: P5-S2-C7
      disposition: represented
      result_indexes:
      - 2
      reason: Specifies regions as predominantly left mid-posterior MTG and adjacent
        white matter.
    - source_id: P5-S2-C8
      disposition: represented
      result_indexes:
      - 2
      reason: Specifies t-values and location for the dual-covariate analysis.
    - source_id: P5-S2-C9
      disposition: represented
      result_indexes:
      - 0
      reason: Restates association between spontaneous naming and LH temporal/parietal
        network.
    - source_id: P5-S2-C10
      disposition: represented
      result_indexes:
      - 2
      reason: Restates that significant regions were confined to mid-posterior MTG
        and white matter after covariation.
    - source_id: P6-S1-C9
      disposition: represented
      result_indexes:
      - 2
      reason: Restates that left mid-posterior MTG and white matter remained significant
        after covariates.
    - source_id: P7-S1-C9
      disposition: represented
      result_indexes:
      - 0
      reason: Restates BNT dependence on LH MTG, STG, white matter, and inferior parietal
        cortex.
    - source_id: P7-S2-C3
      disposition: represented
      result_indexes:
      - 3
      reason: Reports that no significant voxels emerged for semantic errors using
        strict correction.
    - source_id: P7-S3-C5
      disposition: represented
      result_indexes:
      - 0
      reason: Notes extension of significant voxels into white matter medial to left
        MTG.
    - source_id: P7-S3-C9
      disposition: represented
      result_indexes:
      - 0
      reason: Restates BNT dependence on LH MTG, STG, white matter, and inferior parietal
        cortex.
    - source_id: P7-S4-C2
      disposition: represented
      result_indexes:
      - 2
      reason: Restates that performance was most critically dependent on mid-posterior
        left MTG and white matter after factoring out speech and perception.
    unresolved_coverage: []
    pending_source_ids:
    - P1-S1-C10
    - P3-S2-C10
    - P3-S3-C1
    - P4-S1-C11
    - P4-S1-C12
    - P4-S1-C15
    - P4-S2-C2
    - P5-S1-C1
    - P5-S1-C2
    - P5-S1-C3
    - P5-S1-C4
    - P5-S1-C5
    - P5-S1-C6
    - P5-S1-C8
    - P5-S1-C10
    - P5-S2-C1
    - P5-S2-C2
    - P5-S2-C3
    - P5-S2-C8
    - P7-S1-C9
    - P7-S3-C5
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
      - P3-S1-C9
      recruited_sample:
      - P3-S1-C9
      eligibility:
      - P3-S1-C10
      - P3-S1-C11
      - P3-S1-C13
      imaging_provenance:
      - P3-S3-C9
      - P3-S3-C10
      - P3-S3-C11
      - P3-S3-C12
      - P4-S1-C1
      - P4-S1-C2
      - P4-S1-C3
      - P4-S3-C1
      imaging_timing:
      - P3-S3-C8
      outcome_timing:
      - P3-S3-C8
      outcome_definition:
      - P3-S2-C12
      - P5-S1-C2
      - P5-S1-C3
      - P5-S1-C4
      - P5-S1-C5
      validation:
      - P4-S2-C7
      analysis_restrictions:
      - P4-S2-C6
      - P4-S2-C13
      dependent_variable_statement:
      - P3-S2-C12
      - P4-S2-C5
      limitations:
      - P4-S1-C8
      - P7-S1-C10
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles: []
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P3-S1-C12
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P5-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: adjustment_roles
      source_ids:
      - P3-S1-C5
      - P3-S1-C6
      - P4-S3-C1
      - P4-S3-C2
      - P4-S3-C3
      - P4-S3-C4
      - P4-S3-C6
      - P4-S3-C7
      - P5-S1-C11
      - P5-S1-C12
      - P5-S1-C13
      - P5-S2-C4
      - P5-S2-C6
      - P6-S1-C5
      - P6-S1-C7
      - P6-S1-C8
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
      pdf_sha256: 76b1c80b0b15c0ab14ff9446684badad37b4d101edb13f7625b9e48dca8359b3
      review_sha256: 6657822f97cc610a596b1702b41826fe1a100a03948f42895412d12e30e8d27a
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
      - P5-S1-C14
      - P5-S2-C10
      - P6-S2-C1
      source_result: VLSM analysis of BNT naming performance controlling for speech
        fluency and visual recognition identified significant voxels primarily in
        the left mid- to posterior MTG (BA 21 and 37) and underlying white matter.
        This association remained significant after adjusting for speech production
        and visual recognition deficits, isolating the region's role in lexical-semantic
        retrieval.
      result_status: detected
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis corresponds to the VLSM of BNT naming performance
            with covariates for speech fluency and visual recognition, as described
            in P5-S1-C14, P5-S2-C10, and P6-S2-C1. The draft correctly identifies
            this specific model.
          source_ids:
          - P5-S1-C14
          - P5-S2-C10
          - P6-S2-C1
        direction:
          answer: fits
          reason: The source indicates that lesions in these regions are associated
            with naming deficits (impaired performance). The draft correctly states
            the association with impaired picture naming performance.
          source_ids:
          - P5-S1-C14
          - P5-S2-C10
          - P6-S2-C1
        construct:
          answer: fits
          reason: The exposure is correctly identified as lesions in the left mid-
            to posterior MTG and underlying white matter. The outcome is BNT naming
            performance. The method is VLSM. The patient measurement is template lesion
            overlap (voxel-based), not patient diffusion or functional imaging.
          source_ids:
          - P5-S1-C14
          - P5-S2-C10
          - P6-S2-C1
          - P4-S2-C3
        qualifications:
          answer: fits
          reason: 'The draft includes the necessary qualifications: controlling for
            speech production (WAB fluency) and visual recognition (3-choice task).
            It also notes the population (LH stroke, chronic phase) and limitations
            (lesion reconstruction, temporal pole coverage).'
          source_ids:
          - P5-S1-C12
          - P5-S2-C4
          - P3-S1-C9
          - P3-S1-C10
          - P4-S1-C8
          - P7-S1-C10
        missing_material_caveat:
          answer: fits
          reason: No material caveats are missing. The draft correctly reflects the
            robustness of the finding after covariate adjustment and includes relevant
            limitations regarding lesion reconstruction and coverage.
          source_ids:
          - P5-S1-C14
          - P5-S2-C10
          - P6-S2-C1
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
      id: R002
      exposure:
        text: lesions in left mid- to posterior MTG (BA 21 and 37) and underlying
          white matter
      outcome:
        text: naming performance on the BNT
      analysis_label: VLSM of naming performance controlling for speech production
      relation: sensitivity
      evidence_ids:
      - P5-S1-C14
      - P5-S2-C10
      - P6-S2-C1
      qualifier_ids:
      - P5-S1-C12
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 76b1c80b0b15c0ab14ff9446684badad37b4d101edb13f7625b9e48dca8359b3
        source_review: _compare/relationships-2026-11-16/review-current/Baldo2013
        source_status_sha256: 32d2198af0a3114dd0bd5d2b1f79ef30be70603f13569c4cd91e53f62d02c5ce
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P3-S1-C9:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 76b1c80b0b15c0ab14ff9446684badad37b4d101edb13f7625b9e48dca8359b3
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 59d8bb982aee64dc4d91198b42850b8d19eaf4a6518eb0bc3ad64b5e3857d1d5
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S1-C9
          page: 3
          text_layer_sha256: 59d8bb982aee64dc4d91198b42850b8d19eaf4a6518eb0bc3ad64b5e3857d1d5
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Methods

          Participants

          The study sample included 96 participants (21 female) who

          had suffered a single LH stroke.'
        anchor_text: 'Methods

          Participants

          The study sample included 96 participants (21 female) who

          had suffered a single LH stroke.'
        excluded_fragments: []
        image_sha256: c0054813f3a99984786e31a46d70dba0410ff0b8ec83bc3dc148ae4be92bed21
        transcription: 'Methods


          Participants


          The study sample included 96 participants (21 female) who had suffered a
          single LH stroke'
      P3-S1-C10:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 76b1c80b0b15c0ab14ff9446684badad37b4d101edb13f7625b9e48dca8359b3
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 8548eaf05dbe1d00d3b287e141003576ec95398e4278d8427f5b7c1eb9c9b1e7
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S1-C10
          page: 3
          text_layer_sha256: 8548eaf05dbe1d00d3b287e141003576ec95398e4278d8427f5b7c1eb9c9b1e7
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Study criteria included being

          a native English speaker, right-handed, and in the chronic

          phase of stroke (at least 10 months post-injury) so that

          behaviors were stabilized.'
        anchor_text: 'Study criteria included being

          a native English speaker, right-handed, and in the chronic

          phase of stroke (at least 10 months post-injury) so that

          behaviors were stabilized.'
        excluded_fragments: []
        image_sha256: b4c38883b59b7507278839830544c2a27bed5164579741f6988fd5770f8dc4ba
        transcription: '. Study criteria included being

          a native English speaker, right-handed, and in the chronic

          phase of stroke (at least 10 months post-injury) so that

          behaviors were stabilized'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 5
  quote: 'When we re-ran the VLSM

    analysis with overall speech ﬂuency as a covariate, the

    signiﬁcant voxels were restricted primarily to the mid- to

    posterior portion of the MTG (BA 21 and 37), again with some

    extension into the white matter just medial to the MTG (see

    '
  status: pending
  by: agent:relationship-converter
  date: '2026-11-20'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
