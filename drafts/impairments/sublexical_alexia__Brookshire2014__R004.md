---
id: sublexical_alexia
name: sublexical alexia
kind: impairment
findings:
- id: f1
  target: alexia_subtype
  target_kind: impairment
  claim: In a convenience sample of persons with aphasia and coexisting alexia, the
    impairment was predominantly sublexical in nature, with 97% of the alexia group
    demonstrating superior lexical reading relative to sublexical reading.
  direction: likely
  relationship: correlational
  method: behavioral_only
  sample:
    n: 67
    population: persons with chronic aphasia and coexisting alexia (defined as reading
      scores >2 SD below normal controls) following left hemisphere stroke
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
  - Retrospective convenience sample
  - Lack of access to actual verbal responses precluded detailed error analysis
  - Potential impact of cooccurring motor speech impairments (apraxia of speech or
    dysarthria) on oral reading performance
  - Assessment limited to single-word oral reading, not text comprehension
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Reading impairment characterized by a nonword/irregular
    word reading ratio at or below the normal control group mean ratio, and/or performance
    at or below chance level for sublexical reading (pseudohomophones and nonwords).
    Lexical alexia was identified in only 2.99% of the sample; Sublexical nature was
    evidenced by 98.5% of the alexia group performing at or below chance level for
    sublexical reading. Additional metadata has not been transcribed; review the pending-field
    flags before approval.'
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
    - not_transcribed:sample.time_post_onset
    - proposed_concept:alexia_subtype
  citation: '@Brookshire2014'
  source_passages:
  - section: Original source P9-S1-C7
    page: 9
    quote: 'Moreover, alexia in this sample of PWA

      appears sublexical in nature, as demonstrated by 66 of the 67 (98.5%) PWA and

      coexisting alexia being at or below chance level performance for sublexical
      reading

      (see Figure 3).'
    supports: claim
  - section: Original source P13-S1-C2
    page: 13
    quote: 'Only 2 of 67 (2.99%) PWA and

      alexia were classified as having a lexical/surface alexia (defined by a ratio
      of non-

      word/irregular word reading greater than the mean ratio for the NC), suggesting
      that

      most of the PWA and alexia in this study present with a sublexical alexia.'
    supports: claim
  - section: Original source P3-S2-C7
    page: 3
    quote: 'The inclusion criteria for PWA were history of left hemisphere stroke
      at least 6

      months prior to enrolment and a diagnosis of aphasia confirmed by a licenced

      speech–language pathologist based on an aphasia quotient (AQ) of less than 93.8/

      1466

      BROOKSHIRE ET AL.


      '
    supports: sample
  - section: Original source P8-S1-C1
    page: 8
    quote: '

      Frequency of alexia

      To determine the frequency of alexia in our convenience sample of 99 PWA, we

      operationally defined alexia by a score of >2 SD below the mean reading score
      of

      the NC group (M = 44.97; SD = 4.15).'
    supports: method
  - section: Original source P14-S2-C3
    page: 14
    quote: 'We employed a retrospective analysis of a convenience sample of indivi-

      duals with chronic aphasia that may not have been fully representative of the

      population with stroke-associated aphasia at large, despite our inclusion of
      indivi-

      duals with a range of aphasia types and severity, and despite the fact that
      type of

      aphasia and alexia was not a criterion for inclusion.'
    supports: limitation
  - section: Original source P15-S1-C5
    page: 15
    quote: 'Regarding the stimuli employed, this study is limited by the fact that
      only oral

      reading abilities for single words were assessed, and this work does not speak
      to text

      comprehension abilities in PWA and alexia.'
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-20'
relationship_review:
  paper: Brookshire2014
  proposal_id: R004
  review_status_sha256: 9340369bc4d7ac385f5f75d75f67a1cd31fb29d07181ec46cc8e5d721ccb5bb4
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 43f66b041547a2af306e30ecedce5d9e2ce8f83bc3860d233d5409a8d457be2d
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 43f66b041547a2af306e30ecedce5d9e2ce8f83bc3860d233d5409a8d457be2d
        A/passages.json: da9bb28ba01b8374de82d9643d1a6f064909d2e3129924cf031d030ce0c37d10
        A/raw.json: b417645495397dce298056f27abc8e6aa5012b0a2a287312d8bf711fbfbda01a
        A/source-units.json: b93b77de66a43e886c7e041713f1675d12d3e30761ef85a04e2f3f9c7a8633a2
        A/full-source-units.json: ae9b033538d6a0e5e089aee2973e07b80bf0a42c49a4c46c4ac66fa58da0c7b4
        A/meta.json: 645f831be238ee6232a7880aa36022303328a00ef3a84e5218888883b918dfe1
        A/table-images/TABLE-1-page-5-2.png: 1543489f36c99b50c1d11365f5ebfbf0977e3a496eb70a38cd3d46eb3290f357
        A/table-images/page-11.png: e2c683987e385bd1a2aafe7e7efaaec7f2d9637905e8a672cc67c752aa94bdc2
        A/table-images/page-7.png: 28059085cec6fa763a17c0430ce2398d94074d403de9178686a0f6291f1c7aed
        A/table-images/page-5.png: 3032814b0e744089a5a36a85ded4806066ff34ab6fde51a37563213c863e171e
        A/table-images/TABLE-4-page-11-1.png: f4ef6fa4c58d43dd9e36ffc9b1b2234f10c1584d317f48bcc735805480a4d1be
        A/table-images/manifest.json: 9440c8a23f4dc0b734eb1372006e4353d3095c39ad18937facbb40eb3a2cf894
        A/table-images/TABLE-3-page-7-1.png: 9f7f6ca3ecf6111596208850b6ba993fe6862497e9fa6a08df85639689303264
        A/table-images/TABLE-2-page-5-1.png: 1543489f36c99b50c1d11365f5ebfbf0977e3a496eb70a38cd3d46eb3290f357
        A/clauses/window-03/raw.json: 3af02fa17d35b384721f29a8ded5ffb78eb251aeb702b28a96629b62b29b1c01
        A/clauses/window-03/prompt.txt: 14d613ad37a764e011f7f3fac028272446b9801cefecbb8ddb8979463bd60687
        A/clauses/window-03/meta.json: 8bb8b754b3c9bbf55877ed28a0ce1cb082eb2d2fb4aeaf51be9068359b994bd0
        A/clauses/window-04/raw.json: c6b3ae3a5c3cdeaa84448ebf6e668847628ccdd9ce42bcaf7371cffe9b29e08d
        A/clauses/window-04/prompt.txt: 2af7731b3b75a29a167ca79f82cb2ebfe2b9dfeda1204080a594e071cacadf22
        A/clauses/window-04/meta.json: f18eb8b294f90e3ece81f1fcee379025d1d087e857f0e0b98a313e5d6e78f60d
        A/clauses/window-05/raw.json: f52f83d7a6569f085b6ee1f80fcf6d905beb0b3d5a36a8370178ba49a8d34af8
        A/clauses/window-05/prompt.txt: eb41b25397c34b58fef0171bad74da858fe3551eeb161f32d90656ff6418be93
        A/clauses/window-05/meta.json: 0fb11d8c0434e23f1598a3a51ecfbc3b1240b09ac54614c5e3727b0249265357
        A/clauses/window-02/raw.json: 8a92c7a0e8bbb0b9ce33a313c09fef292ccbe0d9786644e3332d1cbfb800723d
        A/clauses/window-02/prompt.txt: 82c8c294500544837abe08fa826ca2014ab54d251a1779a9f9cbfe8502e16980
        A/clauses/window-02/meta.json: 60139673fed44b837563c0917ea3bae87ac1fa9b5dcef1ad0d404de234ad7c8e
        A/clauses/window-07/raw.json: 670684e94d9553996cc67668cfc7dbd5b07d8f258060d53bf0196919d0fb3b3b
        A/clauses/window-07/prompt.txt: 879dcddbd26fe9f6237a599cf840bb49a383a7d1193e536c93ca27542f407fdd
        A/clauses/window-07/meta.json: 6aa7d4a24915267f3018e30ff16dde686f557fbb82c62e9d77364d34bb4786b8
        A/clauses/window-01/raw.json: 444f44ca57b8e245d168725145ab130db54c67038ca8e94e47001c7584eec8ba
        A/clauses/window-01/prompt.txt: e95d5d42321302239d666cbdbb967cd80676f4566c1dc9a5fe8f69c1ad9f0cb9
        A/clauses/window-01/meta.json: e71903b7a7ff307f5e7d54b797747732d897c540f4b55047022e0dbf8913f2ed
        A/clauses/window-06/raw.json: beb95c83b8bebcd3712f2a0dc5d532d437c95cb68fda28dd0cfbcde11c1e4655
        A/clauses/window-06/prompt.txt: 0930cf8b93d38eb340e53bcd29cac40d66a6ce061af75e79b4e7cfa685a0af07
        A/clauses/window-06/meta.json: ab830ee6a833d7ace59037cf9332d749c3c9a07debbfbf2cc9a1ce07b7fdd4d5
        A/clauses/window-08/raw.json: 42a077324f6b58abf30bad6f153666b770750481a9fe9d97ac48e58aed4e13ba
        A/clauses/window-08/prompt.txt: 3699d4a1407d795952fd244285efaa282edc1b886ac25cc3b4ce02c2a9989aff
        A/clauses/window-08/meta.json: acc440eb4eae7ea353c6bbc17b71dc7d979935f28a4933d6cc10afc43cb86ac6
        A/tables/TABLE-4-page-11-4/raw.json: 8981883176d809455a977889e1b8fc2f67200c9f1023da40061eaec555f24c21
        A/tables/TABLE-4-page-11-4/prompt.txt: 84a70cea82eb1c660c035a5f8e0fbdf640be598356a43706c66145ecb9500dc8
        A/tables/TABLE-4-page-11-4/meta.json: b3fd86df6bc064cc2057966b4b0cd53be47e9a78b421701cb107f7cce321c5a3
        A/tables/TABLE-1-page-5-2/raw.json: 8e78d780e4d6fe97a8af15cac224b7d087e9724751fd069442aeeeaff6c41115
        A/tables/TABLE-1-page-5-2/prompt.txt: 04c8f224911c5950790095af7aa1edf2369b3daf1faf2dfb10066d09ca5b38d7
        A/tables/TABLE-1-page-5-2/meta.json: 584adbfe9883e7c529aaa51d9bd20e3916750df21522873e24243dd745ca61a6
        A/tables/TABLE-3-page-7-3/raw.json: f4116eaa0042e6e3dd19b70d19c92529348ee2067c6855e8a1bcf36b62842444
        A/tables/TABLE-3-page-7-3/prompt.txt: 4699f5271a034556e9507365fc21ccc4047dd8f70e1c6b2e55567854417e81df
        A/tables/TABLE-3-page-7-3/meta.json: 1e95f03fbf1e9945026622e323561be82e9d12d84ebe3e7dfa7987686fd1ae2a
        A/tables/TABLE-2-page-5-1/raw.json: b2bba4c98454d772bcca6ae1727d956323691d5922befc2692ec6cb90f309045
        A/tables/TABLE-2-page-5-1/prompt.txt: 83e84f3f64a746b6286755d57dbe188eb0090bf8354611aad77ec12058b81cc1
        A/tables/TABLE-2-page-5-1/meta.json: ba06184fc7c3484aca83a8f567978d43d67bc5f6ea49fd67977e824110106cc1
        B/passages.json: da9bb28ba01b8374de82d9643d1a6f064909d2e3129924cf031d030ce0c37d10
        B/raw.json: da29d029984f1c95873d13c47c1fb839f6304bdadcc16415a0423157a59cfdcb
        B/source-units.json: b93b77de66a43e886c7e041713f1675d12d3e30761ef85a04e2f3f9c7a8633a2
        B/full-source-units.json: ae9b033538d6a0e5e089aee2973e07b80bf0a42c49a4c46c4ac66fa58da0c7b4
        B/meta.json: 9be0f78733947fd606a4e1356cb4fcf55106ee4957f8d489ba3afc40bc57daf9
        B/table-images/TABLE-1-page-5-2.png: 1543489f36c99b50c1d11365f5ebfbf0977e3a496eb70a38cd3d46eb3290f357
        B/table-images/page-11.png: e2c683987e385bd1a2aafe7e7efaaec7f2d9637905e8a672cc67c752aa94bdc2
        B/table-images/page-7.png: 28059085cec6fa763a17c0430ce2398d94074d403de9178686a0f6291f1c7aed
        B/table-images/page-5.png: 3032814b0e744089a5a36a85ded4806066ff34ab6fde51a37563213c863e171e
        B/table-images/TABLE-4-page-11-1.png: f4ef6fa4c58d43dd9e36ffc9b1b2234f10c1584d317f48bcc735805480a4d1be
        B/table-images/manifest.json: e196bf5075fa62a58f76e443f10c3d6ab1a8f35ec5bb3b2c268dbc92ff3eea1f
        B/table-images/TABLE-3-page-7-1.png: 9f7f6ca3ecf6111596208850b6ba993fe6862497e9fa6a08df85639689303264
        B/table-images/TABLE-2-page-5-1.png: 1543489f36c99b50c1d11365f5ebfbf0977e3a496eb70a38cd3d46eb3290f357
        B/clauses/window-03/raw.json: d95b1e1445989744d50f6cc71becdd03872d2b9b961da3939697f7a99dd481c6
        B/clauses/window-03/prompt.txt: 14d613ad37a764e011f7f3fac028272446b9801cefecbb8ddb8979463bd60687
        B/clauses/window-03/meta.json: a66ba370c5e1080d28ab5b8470021a8ea36611ff03dd00a90c70260dd8d12079
        B/clauses/window-04/raw.json: e3e20a5e1d89e7ba1f2864e97f202a3d72330a45001b75930c67c2ef4ec624f7
        B/clauses/window-04/prompt.txt: 2af7731b3b75a29a167ca79f82cb2ebfe2b9dfeda1204080a594e071cacadf22
        B/clauses/window-04/meta.json: 7b286e199fca15fddc65770a06d109993f3a13197cecd4948ca3c3a8627f58f5
        B/clauses/window-05/raw.json: 358057dad03b6cc70139f85b60fa31720192e46a65a635ee35ab66380e29a4e8
        B/clauses/window-05/prompt.txt: eb41b25397c34b58fef0171bad74da858fe3551eeb161f32d90656ff6418be93
        B/clauses/window-05/meta.json: 19f8b03d2bd81b056611e65d1d3f01d77c1e00bfbe95984c62bc64765f10dec5
        B/clauses/window-02/raw.json: 93138566fe8023c3db4fb3ef721d2fde797b12f55fbf713e452b837fca2ded40
        B/clauses/window-02/prompt.txt: 82c8c294500544837abe08fa826ca2014ab54d251a1779a9f9cbfe8502e16980
        B/clauses/window-02/meta.json: f952cc4e1224226b21b1ee084311c538926ec6d1badca8de0214be9e8dca8843
        B/clauses/window-07/raw.json: dbc55733eaf930f2ce6cbf0c87150e83c0fbd5680a3c99b32581310f51f82670
        B/clauses/window-07/prompt.txt: 879dcddbd26fe9f6237a599cf840bb49a383a7d1193e536c93ca27542f407fdd
        B/clauses/window-07/meta.json: 2ae526607f5bd47ca7f352c6c225b2a611fd687ab66ef6470b9f6a1b3f7c4108
        B/clauses/window-01/raw.json: fd448e6c73073732407bb7647dfc079841d06775202a41b1fe3e5d13b4f7bc61
        B/clauses/window-01/prompt.txt: e95d5d42321302239d666cbdbb967cd80676f4566c1dc9a5fe8f69c1ad9f0cb9
        B/clauses/window-01/meta.json: f4326e9aff0d76dc1c9d796c314147c8871fa42af5b7cef03a7fb90e555e264a
        B/clauses/window-06/raw.json: e695bee853b519de1a63310bcbe05ccd09b104fff4b1aa311067119c5a0cbf78
        B/clauses/window-06/prompt.txt: 0930cf8b93d38eb340e53bcd29cac40d66a6ce061af75e79b4e7cfa685a0af07
        B/clauses/window-06/meta.json: 390d0f00e0e0a8893a4b6e67cfe5676d5a0714bd674fe60d5100d001eda096c6
        B/clauses/window-08/raw.json: 673c0e4ebf8e1831cb3f806a42247e2707c48285a006827dbf6ac4cb3d1e99f7
        B/clauses/window-08/prompt.txt: 3699d4a1407d795952fd244285efaa282edc1b886ac25cc3b4ce02c2a9989aff
        B/clauses/window-08/meta.json: 64b33ff040a0d2b989892a04d09a6328e43bef5af1b73db8dc8f2c10523b3204
        B/tables/TABLE-4-page-11-4/raw.json: 8981883176d809455a977889e1b8fc2f67200c9f1023da40061eaec555f24c21
        B/tables/TABLE-4-page-11-4/prompt.txt: 84a70cea82eb1c660c035a5f8e0fbdf640be598356a43706c66145ecb9500dc8
        B/tables/TABLE-4-page-11-4/meta.json: 40a2d60f13a7323c3aa524e493daaddb88a263cb770a721727c63c902ab3ec2a
        B/tables/TABLE-1-page-5-2/raw.json: 8b72b7eab4349521e288cf801162997c0dbf9191a488ae38d9981882a071bdb7
        B/tables/TABLE-1-page-5-2/prompt.txt: 04c8f224911c5950790095af7aa1edf2369b3daf1faf2dfb10066d09ca5b38d7
        B/tables/TABLE-1-page-5-2/meta.json: 9e1a89cf6183ccdd0d172b9ab75777daf1acaa7fc7f5ddd167778f2bd1cf698e
        B/tables/TABLE-3-page-7-3/raw.json: f4116eaa0042e6e3dd19b70d19c92529348ee2067c6855e8a1bcf36b62842444
        B/tables/TABLE-3-page-7-3/prompt.txt: 4699f5271a034556e9507365fc21ccc4047dd8f70e1c6b2e55567854417e81df
        B/tables/TABLE-3-page-7-3/meta.json: 9274b3c26b949bd04661676bfd7e546f73e3f6ec7f2b2a36190a5700658a92eb
        B/tables/TABLE-2-page-5-1/raw.json: 6885f40ec51964afe5ec8ae2719130c4011bab6693ac1d34bb7e45493766bd43
        B/tables/TABLE-2-page-5-1/prompt.txt: 83e84f3f64a746b6286755d57dbe188eb0090bf8354611aad77ec12058b81cc1
        B/tables/TABLE-2-page-5-1/meta.json: 743da86be12d8a26b607de3079974627f5fd3a00247b1e419d7342b66abcc6b4
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
      pdf_sha256: 43f66b041547a2af306e30ecedce5d9e2ce8f83bc3860d233d5409a8d457be2d
      source_review: _compare/relationships-2026-11-16/review-current/Brookshire2014
      source_status_sha256: e973d8754151f110c667c3e1f16212a3fd4e99de493cdde7745813532025ef44
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R004
    exposure:
      text: alexia (PWA)
    outcome:
      text: alexia subtype (lexical/surface vs sublexical)
    analysis_label: Alexia subtype classification
    relation: association
    evidence_ids:
    - P9-S1-C4
    - P9-S1-C7
    - P13-S1-C2
    qualifier_ids:
    - P9-S1-C3
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 43f66b041547a2af306e30ecedce5d9e2ce8f83bc3860d233d5409a8d457be2d
      source_review: _compare/relationships-2026-11-16/review-current/Brookshire2014
      source_status_sha256: e973d8754151f110c667c3e1f16212a3fd4e99de493cdde7745813532025ef44
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P1-S1-C10
      - Result passage disposed without unit P1-S1-C11
      - Result passage disposed without unit P1-S1-C12
      - Accounting without a linked unit P1-S1-C13
      - Unaccounted source passage P1-S1-C13
      - Result passage disposed without unit P4-S1-C4
      - Accounting without a linked unit P4-S2-C8
      - Accounting without a linked unit P6-S1-C2
      - Accounting without a linked unit P6-S1-C3
      - Unaccounted source passage P4-S2-C8
      - Unaccounted source passage P6-S1-C3
      - Unaccounted source passage P6-S1-C2
      - Result passage disposed without unit P6-S1-C7
      - Result passage disposed without unit P7-S1-C5
      - Result passage disposed without unit P7-S1-C12
      - Result passage disposed without unit P7-S1-C13
      - Result passage disposed without unit P9-S2-C3
      - Result passage disposed without unit P11-S1-C1
      - Accounting without a linked unit P11-S1-C6
      - Accounting without a linked unit P11-S1-C7
      - Accounting without a linked unit P11-S1-C8
      - Accounting without a linked unit P11-S1-C9
      - Result passage disposed without unit P12-S1-C2
      - Result passage disposed without unit P12-S1-C4
      - Unaccounted source passage P11-S1-C8
      - Unaccounted source passage P11-S1-C7
      - Unaccounted source passage P11-S1-C6
      - Unaccounted source passage P11-S1-C9
      - Result passage disposed without unit P12-S1-C5
      - Accounting without a linked unit P12-S1-C6
      - Result passage disposed without unit P12-S2-C7
      - Result passage disposed without unit P13-S1-C1
      - Result passage disposed without unit P13-S1-C2
      - Accounting without a linked unit P13-S2-C3
      - Accounting without a linked unit P13-S2-C4
      - Unaccounted source passage P12-S1-C6
      - Unaccounted source passage P13-S2-C3
      - Unaccounted source passage P13-S2-C4
      - Result passage disposed without unit P15-S1-C10
      - Result passage disposed without unit P15-S1-C11
      - Result passage disposed without unit P15-S1-C12
      unattached_null_or_qualifier_ids:
      - P6-S1-C3
      - P9-S1-C10
      - P13-S1-C2
      - P13-S2-C3
      - P13-S2-C4
      suppressed_nonrepresented_units: 23
      default_disposition_count_requires_completeness_check: 155
      unselected_timing_passages:
      - P3-S2-C7
      - P7-S1-C10
      - P14-S2-C3
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P1-S1-C13
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P1-S1-C14
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S1-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S1-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S2-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S2-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S2-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: analysed_sample
        source_ids:
        - P1-S1-C9
        - P1-S1-C10
        - P3-S2-C2
        - P3-S2-C6
        - P4-S1-C7
        - P8-S1-C5
        - P8-S1-C6
        - P9-S1-C9
        - P9-S1-C10
        - P11-S1-C3
        - P11-S2-C2
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: limitations
        source_ids:
        - P14-S2-C2
        - P14-S2-C3
        - P14-S2-C4
        - P14-S2-C5
        - P14-S2-C6
        - P14-S2-C7
        - P15-S1-C5
        - P15-S1-C6
        - P15-S1-C7
        - P15-S1-C9
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - analysed_sample
      - imaging_provenance
      - imaging_timing
      - validation
      - dependent_variable_statement
      - limitations
      - personal_factors
      - adjustment_roles
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-5-2
      - TABLE-2-page-5-1
      - TABLE-3-page-7-3
      - TABLE-4-page-11-4
      unlinked_tables:
      - TABLE-1-page-5-2
      - TABLE-2-page-5-1
      - TABLE-3-page-7-3
      - TABLE-4-page-11-4
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P8-S1
        - P8-S2
        - P9-S1
        - P9-S2
        - P10-S1
        - P12-S1
        - P13-S1
        - P13-S2
        - P15-S1
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 43f66b041547a2af306e30ecedce5d9e2ce8f83bc3860d233d5409a8d457be2d
      source_review: _compare/relationships-2026-11-16/review-current/Brookshire2014
      source_status_sha256: e973d8754151f110c667c3e1f16212a3fd4e99de493cdde7745813532025ef44
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C10
      disposition: represented
      result_indexes:
      - 0
      reason: Reports 68% alexia frequency.
    - source_id: P1-S1-C11
      disposition: represented
      result_indexes:
      - 1
      - 2
      reason: Reports PWA performed worse than NC and worse on sublexical than lexical
        stimuli.
    - source_id: P1-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the range of aphasia types/severities in the group.
    - source_id: P1-S1-C13
      disposition: repeated
      result_indexes:
      - 6
      - 7
      - 8
      reason: Restatement of aphasia severity as a predictor.
    - source_id: P1-S1-C14
      disposition: represented
      result_indexes:
      - 9
      reason: Reports education was not a significant predictor.
    - source_id: P4-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes control group performance.
    - source_id: P4-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes stimuli frequency comparisons.
    - source_id: P6-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes nonword biphone probabilities.
    - source_id: P6-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes word length comparisons.
    - source_id: P6-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes word length t-test results.
    - source_id: P6-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes pseudohomophone length differences.
    - source_id: P6-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes pseudohomophone length t-tests.
    - source_id: P6-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes part of speech of stimuli.
    - source_id: P7-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Compares UF and UW participants.
    - source_id: P7-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports rater reliability.
    - source_id: P7-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes group similarities in age, education, handedness.
    - source_id: P7-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports mean WAB-AQ and BNT scores.
    - source_id: P7-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports average months poststroke.
    - source_id: P7-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Lists aphasia type counts.
    - source_id: P7-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes PWA reading score range.
    - source_id: P7-S1-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes NC reading score range.
    - source_id: P8-S1-C5
      disposition: represented
      result_indexes:
      - 0
      reason: Reports 67.78% of PWA met alexia criteria.
    - source_id: P8-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports average accuracy percentages.
    - source_id: P8-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports ANOVA main effects and interaction.
    - source_id: P8-S1-C11
      disposition: represented
      result_indexes:
      - 1
      reason: Reports PWA read all word types significantly worse than NC.
    - source_id: P9-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes reading patterns across word types.
    - source_id: P9-S1-C2
      disposition: represented
      result_indexes:
      - 2
      reason: Reports lexical reading significantly higher than sublexical reading
        for PWA.
    - source_id: P9-S1-C4
      disposition: represented
      result_indexes:
      - 3
      reason: Reports 2.99% of PWA had lexical alexia.
    - source_id: P9-S1-C5
      disposition: repeated
      result_indexes:
      - 3
      reason: Provides specific ratios for the 2.99%.
    - source_id: P9-S1-C6
      disposition: repeated
      result_indexes:
      - 3
      reason: Reports the remaining PWA demonstrated superior lexical reading.
    - source_id: P9-S1-C7
      disposition: represented
      result_indexes:
      - 3
      reason: Reports 98.5% of PWA at or below chance for sublexical reading.
    - source_id: P9-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Lists aphasia type counts for alexia group.
    - source_id: P9-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Lists PWA who did not meet alexia criteria.
    - source_id: P10-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes Figure 3 (real vs nonword reading).
    - source_id: P11-S1-C1
      disposition: represented
      result_indexes:
      - 4
      reason: Reports variability in lexical vs sublexical reading across aphasia
        types.
    - source_id: P11-S1-C6
      disposition: represented
      result_indexes:
      - 8
      reason: Reports R2 and p-values for the three regression models.
    - source_id: P11-S1-C7
      disposition: represented
      result_indexes:
      - 6
      - 7
      - 8
      reason: Reports WAB-AQ had a unique positive effect on all reading types.
    - source_id: P11-S1-C8
      disposition: represented
      result_indexes:
      - 6
      - 7
      - 8
      reason: Provides specific predicted increases based on WAB-AQ.
    - source_id: P11-S1-C9
      disposition: represented
      result_indexes:
      - 9
      reason: Reports education was not uniquely predictive.
    - source_id: P11-S2-C2
      disposition: represented
      result_indexes:
      - 6
      - 7
      - 8
      - 9
      reason: Table 4 provides coefficients and p-values for WAB-AQ and Education.
    - source_id: P12-S1-C2
      disposition: represented
      result_indexes:
      - 0
      reason: Restates 68% alexia frequency.
    - source_id: P12-S1-C5
      disposition: repeated
      result_indexes:
      - 4
      reason: Restates variability in lexical vs sublexical reading across aphasia
        types.
    - source_id: P13-S1-C1
      disposition: represented
      result_indexes:
      - 1
      - 2
      reason: Restates PWA read worse than NC and superior lexical vs sublexical.
    - source_id: P13-S1-C2
      disposition: repeated
      result_indexes:
      - 3
      reason: Restates 2.99% lexical alexia.
    - source_id: P13-S2-C3
      disposition: represented
      result_indexes:
      - 8
      reason: Restates variance explained by models.
    - source_id: P13-S2-C4
      disposition: repeated
      result_indexes:
      - 6
      - 7
      - 8
      reason: Restates aphasia severity as the only unique predictor.
    - source_id: P13-S2-C9
      disposition: represented
      result_indexes:
      - 4
      reason: Links aphasia types (WAB-AQ scores) to reading accuracy.
    - source_id: P14-S1-C1
      disposition: represented
      result_indexes:
      - 9
      reason: Reports only a trend relationship for education.
    - source_id: P15-S2-C2
      disposition: represented
      result_indexes:
      - 2
      reason: Restates more severe impairment of sublexical reading.
    unresolved_coverage:
    - source_id: P11-S2-C2
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P9-S2-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S1-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S1-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S2-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S2-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S2-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S2-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P14-S1-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P15-S1-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P15-S1-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P15-S1-C12
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C12
    - P1-S1-C13
    - P4-S1-C4
    - P4-S2-C8
    - P6-S1-C2
    - P6-S1-C3
    - P6-S1-C4
    - P6-S1-C5
    - P6-S1-C6
    - P6-S1-C7
    - P7-S1-C2
    - P7-S1-C5
    - P7-S1-C7
    - P7-S1-C9
    - P7-S1-C10
    - P7-S1-C11
    - P7-S1-C12
    - P7-S1-C13
    - P8-S1-C8
    - P8-S1-C10
    - P9-S1-C1
    - P9-S1-C5
    - P9-S1-C6
    - P9-S1-C9
    - P9-S1-C10
    - P9-S2-C3
    - P10-S1-C3
    - P12-S1-C4
    - P12-S1-C6
    - P12-S2-C7
    - P13-S2-C4
    - P13-S2-C5
    - P13-S2-C6
    - P13-S2-C8
    - P14-S1-C11
    - P15-S1-C10
    - P15-S1-C11
    - P15-S1-C12
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-5-2
    - TABLE-2-page-5-1
    - TABLE-3-page-7-3
    - TABLE-4-page-11-4
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample: []
      recruited_sample:
      - P3-S2-C2
      - P3-S2-C4
      - P3-S2-C6
      eligibility:
      - P3-S2-C7
      - P4-S1-C1
      - P4-S1-C2
      - P4-S1-C5
      - P4-S1-C6
      imaging_provenance: []
      imaging_timing: []
      outcome_timing:
      - P1-S1-C9
      - P3-S2-C3
      - P14-S2-C2
      outcome_definition:
      - P1-S1-C10
      - P8-S1-C1
      - P8-S1-C2
      - P11-S1-C3
      - P12-S1-C2
      validation: []
      analysis_restrictions:
      - P14-S2-C2
      - P14-S2-C3
      - P14-S2-C4
      - P14-S2-C5
      - P15-S1-C1
      - P15-S1-C2
      - P15-S1-C3
      dependent_variable_statement: []
      limitations: []
      personal_factors: []
      tested_personal_effects:
      - P1-S1-C13
      - P1-S1-C14
      - P11-S1-C7
      - P11-S1-C8
      - P11-S1-C9
      - P13-S2-C4
      - P13-S2-C5
      adjustment_roles: []
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P7-S1-C7
      - P7-S1-C14
      - P7-S2-C1
    outcome_type: status_at_assessment
    imaging_vs_outcome: not_stated
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P1-S1-C13
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P1-S1-C14
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S1-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S1-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S2-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S2-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S2-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: analysed_sample
      source_ids:
      - P1-S1-C9
      - P1-S1-C10
      - P3-S2-C2
      - P3-S2-C6
      - P4-S1-C7
      - P8-S1-C5
      - P8-S1-C6
      - P9-S1-C9
      - P9-S1-C10
      - P11-S1-C3
      - P11-S2-C2
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: limitations
      source_ids:
      - P14-S2-C2
      - P14-S2-C3
      - P14-S2-C4
      - P14-S2-C5
      - P14-S2-C6
      - P14-S2-C7
      - P15-S1-C5
      - P15-S1-C6
      - P15-S1-C7
      - P15-S1-C9
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
      pdf_sha256: 43f66b041547a2af306e30ecedce5d9e2ce8f83bc3860d233d5409a8d457be2d
      review_sha256: 9340369bc4d7ac385f5f75d75f67a1cd31fb29d07181ec46cc8e5d721ccb5bb4
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
      - P9-S1-C4
      - P9-S1-C7
      - P13-S1-C2
      source_result: In a convenience sample of 67 persons with aphasia and coexisting
        alexia, the alexia was predominantly sublexical in nature. This was determined
        by a nonword/irregular word reading ratio, where 65 of 67 (97%) had a ratio
        below the normal control mean, indicating superior lexical reading. Additionally,
        66 of 67 (98.5%) performed at or below chance level for sublexical reading
        (pseudohomophones and nonwords). Only 2 individuals (2.99%) were classified
        as having lexical/surface alexia.
      result_status: detected
      patient_measurement: non_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis is the classification of alexia subtype (lexical
            vs sublexical) in PWA. The source explicitly describes this classification
            using the nonword/irregular word ratio and chance-level performance on
            sublexical items. The proposed core correctly identifies this as the analysis.
          source_ids:
          - P9-S1-C3
          - P9-S1-C4
          - P13-S1-C2
        direction:
          answer: fits
          reason: 'The source states that the majority of PWA with alexia demonstrated
            superior lexical reading relative to sublexical reading (P9-S1-C2, P13-S1-C2).
            The proposed core claims the impairment was ''predominantly sublexical
            in nature'' and that 97% demonstrated superior lexical reading. This preserves
            the direction of the finding: the deficit is in the sublexical route,
            while the lexical route is relatively preserved.'
          source_ids:
          - P9-S1-C2
          - P9-S1-C7
          - P13-S1-C2
        construct:
          answer: fits
          reason: The exposure is alexia (PWA), and the outcome is the subtype (sublexical
            vs lexical). The measurement is behavioral (oral reading of specific word
            types), not imaging. The proposed core correctly identifies the population
            as PWA with alexia and the measurement as behavioral (SAPA).
          source_ids:
          - P1-S1-C9
          - P8-S1-C1
          - P9-S1-C3
        qualifications:
          answer: fits
          reason: 'The proposed core includes the key qualifications: the small percentage
            of lexical alexia (2.99%) and the high percentage of sublexical performance
            (98.5% at/below chance). It also lists relevant limitations such as the
            retrospective design and lack of verbal response data, which are material
            to the interpretation of the subtype classification.'
          source_ids:
          - P9-S1-C4
          - P9-S1-C7
          - P13-S1-C3
          - P14-S2-C3
        missing_material_caveat:
          answer: fits
          reason: The core includes the critical caveat that the distinction between
            subtypes is tentative due to variable NC performance and lack of access
            to verbal responses (P13-S1-C3). It also includes the limitation regarding
            motor speech impairments (P14-S2-C4) and the single-word nature of the
            assessment (P15-S1-C5). No material caveats that change the interpretation
            of the sublexical finding are omitted.
          source_ids:
          - P13-S1-C3
          - P14-S2-C4
          - P15-S1-C5
      optional_pending:
      - sample.time_post_onset
      - statistics.ratio_values
      - statistics.chance_level_definition
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
    - statistics.ratio_values
    - statistics.chance_level_definition
    normalizations:
    - field: sample.time_post_onset
      original: at least 6 months post-stroke
      action: not_transcribed
      reason: 'Numbers not grounded in usable selected source readings: 6'
    analysis_identity:
      id: R004
      exposure:
        text: alexia (PWA)
      outcome:
        text: alexia subtype (lexical/surface vs sublexical)
      analysis_label: Alexia subtype classification
      relation: association
      evidence_ids:
      - P9-S1-C4
      - P9-S1-C7
      - P13-S1-C2
      qualifier_ids:
      - P9-S1-C3
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 43f66b041547a2af306e30ecedce5d9e2ce8f83bc3860d233d5409a8d457be2d
        source_review: _compare/relationships-2026-11-16/review-current/Brookshire2014
        source_status_sha256: e973d8754151f110c667c3e1f16212a3fd4e99de493cdde7745813532025ef44
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P3-S2-C7:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 43f66b041547a2af306e30ecedce5d9e2ce8f83bc3860d233d5409a8d457be2d
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 714a5d080aa1ef2cd918ba26e948c1fa586c2ab9989fde60e1d9d1fe98b7fdda
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S2-C7
          page: 3
          text_layer_sha256: 30b865c89c02ad92c41e6d701706c9c1f568412689b996a8acf5f6da8b7769a9
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: 'The inclusion criteria for PWA were history of left hemisphere
          stroke at least 6

          months prior to enrolment and a diagnosis of aphasia confirmed by a licenced

          speech–language pathologist based on an aphasia quotient (AQ) of less than
          93.8/

          1466

          BROOKSHIRE ET AL.


          '
        anchor_text: 'The inclusion criteria for PWA were history of left hemisphere
          stroke at least 6

          months prior to enrolment and a diagnosis of aphasia confirmed by a licenced

          speech–language pathologist based on an aphasia quotient (AQ) of less than
          93.8/

          1466

          BROOKSHIRE ET AL.'
        excluded_fragments: []
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 9
  quote: 'Moreover, alexia in this sample of PWA

    appears sublexical in nature, as demonstrated by 66 of the 67 (98.5%) PWA and

    coexisting alexia being at or below chance level performance for sublexical reading

    (see Figure 3).'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-20'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
