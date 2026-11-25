---
id: early_language_and_age_predictor
name: Early language performance and age predictor
kind: predictor
findings:
- id: f1
  target_audit:
    status: behaviour_label_present
    category: behaviour_or_language_construct
    original_target: language_recovery
    reason: Label names a behaviour or language construct; its exact operational definition and measurement
      still need source review.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  outcome_measurement:
    status: needs_source_review
    instruments: []
    note: Outcome instrument/task is not yet verified for this finding. Do not infer it from the predictor
      or a paper-wide test list.
  target: language_recovery
  target_kind: prognosis
  claim: Early language performance and age were the only overall significant predictors
    of language recovery over time.
  direction: likely
  relationship: correlational
  method: behavioral_only
  sample:
    n: not_reported
    population: patients with a left hemisphere stroke
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
  author_limitations: []
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: A multiple regression model using early language performance
    (measured by in-scanner language measure) and age as independent variables. language
    recovery was defined as improvement in scores between Time 1 and Time 2. Additional
    metadata has not been transcribed; review the pending-field flags before approval.'
  imaging_details:
    reference_space: not_reported
    atlases_used: []
  lesion_mapping: {}
  provenance:
    extracted_by: model:gemma4:31b
    extracted_on: '2026-11-24'
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
    - not_transcribed:author_limitations
    - not_transcribed:sample.time_post_onset
    - proposed_concept:language_recovery
  citation: '@Geranmayeh2017'
  source_passages:
  - section: Original source P7-S1-C2
    page: 7
    quote: "Again, only early\nlanguage performance (beta = \x040.813, P = 0.002)\
      \ and age\n(beta = \x040.306, P = 0.047) were the overall signiﬁcant pre-\n\
      dictors of language recovery over time."
    supports: claim
  - section: Original source P2-S3-C10
    page: 2
    quote: "Twenty-seven participants were scanned at two time points;\nﬁrst in the\
      \ early phase after the stroke [15 \x02 7.6 days,\nmean \x02 standard deviation\
      \ (SD)] and again at \x034 months\n(108 \x02 26\ndays)\nafter\nan\naverage\n\
      interscan\ninterval\nof\n93 \x02 26 days."
    supports: sample
  - section: Original source P3-S2-C6
    page: 3
    quote: "The language\noutcome was deﬁned as the raw score at \x034 months post-\n\
      ictus, and the language recovery was deﬁned as improvement\nin the scores over\
      \ time (Time 2 \x04 Time 1)."
    supports: method
  - section: Original source P2-S3-C2
    page: 2
    quote: "Speciﬁcally, a cohort of patients undertook event-\nrelated functional\
      \ MRI tasks ﬁrst at \x032 weeks (early scan)\nand then at \x034 months (late\
      \ scan) after a left hemisphere\nstroke."
    supports: sample
predictor_type: clinical
short_definition: A multiple regression model using early language performance (measured
  by in-scanner language measure) and age as independent variables.
assessment:
- in-scanner language measure
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-24'
relationship_review:
  paper: Geranmayeh2017
  proposal_id: R019
  review_status_sha256: f4976444b35a74aa6c6d4d0ddf7cc67bca1cac6d6c9f092a92319f8ff2432088
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 157e72766fb6e1e9ce6d22f96620848cc228a1c001212df9dabb7dc69edbb607
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 157e72766fb6e1e9ce6d22f96620848cc228a1c001212df9dabb7dc69edbb607
        A/passages.json: faf20e230bb970a3cc3675324218b3edc0481e6185f271cdbcabe55dc2c93ff6
        A/raw.json: 648bcd7b2e68205939d9282c8d8e7fc2e019df7b4d624ed73b8e27703342c51b
        A/source-units.json: fbba6188dba777357b6c143d7eeb1b19497ccec13f5d3eea2b44275f7fafa0b9
        A/full-source-units.json: 43c9f53b055c6b0089926af08242c85fba333bce8f9ad36beae71e6eb878eca5
        A/meta.json: df76cc66be34ec705faae9bcea07473373cb43b6961d86cf30a9eb183a65c1ab
        A/table-images/TABLE-1-page-3-1.png: 063979c3046f2ca854684e38e6b3576089ed8ca5a73e005c6af5ddae6c76b3ae
        A/table-images/page-3.png: a78ac652f5bee557e6088d2ce625fc5cdbc7dc9c9686642dad75eab9c2df214e
        A/table-images/TABLE-1-page-6-1.png: 2ce90ca6bfea6128d36349c02f7081b87ee2cef23147a5318a2a046530100777
        A/table-images/page-6.png: 1cc38659dbe0a0d5c41fcf98f32c6891ef3c8930cc4b88ec9bc534c327cfc0c6
        A/table-images/TABLE-3-page-8-1.png: 551352a785e3c52e555fe75d6888989af9e1e6d95fd3086b862ee66fae1e278a
        A/table-images/page-4.png: 8554f7c9cd23cb2f41d6927d605ad5439db0b0a98db8667f4948134d6fd2eb65
        A/table-images/TABLE-1-page-4-1.png: 593f3135eeb825c1904081993e806525aa8218b9180cfb0d35c01e8bdc6817fd
        A/table-images/page-8.png: cf3146a912a40c5ee6fa93601cc83ae2ca0c0639796b46ce7d1d03596089b4f2
        A/table-images/manifest.json: 4663dfaf88aaf7bc933fd4168a1aac745c82e3ba9469d9662a848d124cb6af51
        A/table-images/TABLE-2-page-6-2.png: 849d378740288c1211d73952eb196385b45b36face071b870ca674c070ad75d6
        A/clauses/window-03/raw.json: 8aedd3b031c2cb68306b5011dbd0269cb7463dcae7e5ef1c15647647ce091d8b
        A/clauses/window-03/prompt.txt: 0a1149a8545b71bb0b64afe13c180da3ecf5aab6409e908219e245aa6c286cbc
        A/clauses/window-03/meta.json: 56572471533cce34b5b57fc33afef6bb2925341b11729d787f324912e15cf6db
        A/clauses/window-04/raw.json: b4ef8f543577d8dee06a23658764a7ee6d2d836e417b216441600a49055d93f8
        A/clauses/window-04/prompt.txt: d6a6682764cefa9ff6b2beb42cc842fbe15ff998d138f4f783fd72014e7e2ca2
        A/clauses/window-04/meta.json: 1461aa23a3d7d24a6974cf21cac7044043c1f18f374dfa95ced1bf5812c8ef24
        A/clauses/window-05/raw.json: 925839a44ca448043b62d1d2ae73ae318898b4478e1c81befe12de8d26403ea3
        A/clauses/window-05/prompt.txt: e67fbaad829bf59c42bba3124134c20e4e38463bff059cb481456aa7042a8c5c
        A/clauses/window-05/meta.json: 9d7818d0642fd35ad3aed431632acf8c79625cbea3d792c9772d4e145281c171
        A/clauses/window-02/raw.json: ccd41edacc0520041662067345f82be4ac74400dad5e9aa78c82b0e7d4a5ef54
        A/clauses/window-02/prompt.txt: fb0c245d4477d2c1e5f8940221ff322618571fcb779fdf876e84926f344f8195
        A/clauses/window-02/meta.json: f2138adfaecc893d1d6c75468b6f058f6545a3f37fb9b04bff937051e2ece817
        A/clauses/window-07/raw.json: 455d73b5583c425b79859f66a26b75b941d5f7d6453d6a4e36d36e294ce1937a
        A/clauses/window-07/prompt.txt: 6621a88dd33c51f737f3b14941eb367231e6c4e2c050785ba03603724fba1456
        A/clauses/window-07/meta.json: 0b3a05d6638dd37f20b4d1c9a7cc9f747a23efd3e70bb6e6675406720dde3743
        A/clauses/window-01/raw.json: 72239fe03bfe8d0cdbe22912f7f89e6334cf21b8a1b20e142da9f8c5435d0f82
        A/clauses/window-01/prompt.txt: 024012c9fe8c5a365a723ba1e92a7485894e8bcf96c3fb24a339b250ce8d6f6a
        A/clauses/window-01/meta.json: 58ffb210f906bcd947585f6418d9327e7c968b0d599ec338f77f7397d655983a
        A/clauses/window-06/raw.json: 9192e0b9068b272ca6d10445cdc4550ed171748e41e2c08f74aa0870d772df98
        A/clauses/window-06/prompt.txt: 64141fb86c9f41014f7ac12b1d2357acc39ccb5802f7209dcf586412db22bf1e
        A/clauses/window-06/meta.json: 43b54dbbd6b4ab1bf227fbda31507303d6bb08f1e6829ee99fc50be5598e8692
        A/clauses/window-08/raw.json: bfd8b455b6ab8d6264cde9636446fadb7a951dbc8998bd9d50509444ac822950
        A/clauses/window-08/prompt.txt: 085d2167a8e335dc2cfe6bd02da056d211104f10e40c68b1f1b810cf1a175c4a
        A/clauses/window-08/meta.json: a0436bd205e0022bc53d3a7e75e8a1ff7687713c6c2eda0fd794fce7187c9b11
        A/tables/TABLE-1-page-4-2/raw.json: 6c98d7da7005b39d0e03b8b7c129453de01364d643c79cc77c9385f48b483ded
        A/tables/TABLE-1-page-4-2/prompt.txt: a84498229a5e906ebe7fadb811edac4d4bbf5d9228ccf0fce0860afd8ce35fe7
        A/tables/TABLE-1-page-4-2/meta.json: a6ce73d004173e67b57723fa87d2888a7cf4a21dc042111f0ae8e06534bcd905
        A/tables/TABLE-3-page-8-5/raw.json: 0610aa777a061ffde92baf6db3c8365adc1d5c9bc86f3041354297422337db2e
        A/tables/TABLE-3-page-8-5/prompt.txt: e20cb2f2a321269ad947ab7faeef6f0f9d5544145329ece47fec63ed2148e826
        A/tables/TABLE-3-page-8-5/meta.json: 89293fabef775b1782a1e201b017b2d18aee0c2a929d5fc20229e3835687884a
        A/tables/TABLE-2-page-6-4/raw.json: ea213352d5dfcfdb923441c4649712d766c16563913ea763e709a2fc1fc89c1e
        A/tables/TABLE-2-page-6-4/prompt.txt: 0f56892efab7aa4cc628ea16a47a4ef145474768050516ad2f92fbeb3ff12651
        A/tables/TABLE-2-page-6-4/meta.json: 880f8863291b6ce5de98003554abc206b3abd2bb9f31fcdbb8f4a12a0fa095a4
        A/tables/TABLE-1-page-3-1/raw.json: a66ef5478fa3faaff6670b846a0f5d057bd53caa7759947b30c314343822e5bf
        A/tables/TABLE-1-page-3-1/prompt.txt: ae73619b5e3b64551da1830a4e5726c7be957f12bfb4d48ffb7fb190819146f8
        A/tables/TABLE-1-page-3-1/meta.json: c90c107fe4729bbcb08a73531d6400a97188927e0b3828c867168671a5c24084
        A/tables/TABLE-1-page-6-3/raw.json: bb30c07953fa78701a9be1d0572c6da22a16a685e5a384e499490dab491f2bfa
        A/tables/TABLE-1-page-6-3/prompt.txt: f0217ae81f6a2b020d30e446580eb3ebb783c7a8b4a761cf0f2f1528bdedecfb
        A/tables/TABLE-1-page-6-3/meta.json: 64d912f79ab43bff26db5404dddbf1acd0e09ab90a6719fe797fa84f98076312
        B/passages.json: faf20e230bb970a3cc3675324218b3edc0481e6185f271cdbcabe55dc2c93ff6
        B/raw.json: 146b56abd5b7131598579c65f88fab15190de99b96de838239da22d0f31741f7
        B/source-units.json: fbba6188dba777357b6c143d7eeb1b19497ccec13f5d3eea2b44275f7fafa0b9
        B/full-source-units.json: 43c9f53b055c6b0089926af08242c85fba333bce8f9ad36beae71e6eb878eca5
        B/meta.json: e5cebb0c262b6a859b2a3911eef485c7be03fc7c8344f6d0d1f12c6dbda830d0
        B/table-images/TABLE-1-page-3-1.png: 063979c3046f2ca854684e38e6b3576089ed8ca5a73e005c6af5ddae6c76b3ae
        B/table-images/page-3.png: a78ac652f5bee557e6088d2ce625fc5cdbc7dc9c9686642dad75eab9c2df214e
        B/table-images/TABLE-1-page-6-1.png: 2ce90ca6bfea6128d36349c02f7081b87ee2cef23147a5318a2a046530100777
        B/table-images/page-6.png: 1cc38659dbe0a0d5c41fcf98f32c6891ef3c8930cc4b88ec9bc534c327cfc0c6
        B/table-images/TABLE-3-page-8-1.png: 551352a785e3c52e555fe75d6888989af9e1e6d95fd3086b862ee66fae1e278a
        B/table-images/page-4.png: 8554f7c9cd23cb2f41d6927d605ad5439db0b0a98db8667f4948134d6fd2eb65
        B/table-images/TABLE-1-page-4-1.png: 593f3135eeb825c1904081993e806525aa8218b9180cfb0d35c01e8bdc6817fd
        B/table-images/page-8.png: cf3146a912a40c5ee6fa93601cc83ae2ca0c0639796b46ce7d1d03596089b4f2
        B/table-images/manifest.json: 83cac85a9cfc19a51f64b5556267a1cf7d454fb316bea02359c222436d424834
        B/table-images/TABLE-2-page-6-2.png: 849d378740288c1211d73952eb196385b45b36face071b870ca674c070ad75d6
        B/clauses/window-03/raw.json: eb7b060b65a8152e1364d0d37dcb60787d9bde1eb46adc23a700c6fb031472f8
        B/clauses/window-03/prompt.txt: 0a1149a8545b71bb0b64afe13c180da3ecf5aab6409e908219e245aa6c286cbc
        B/clauses/window-03/meta.json: f4e6cdd6dd451697273cb2cf92ade62f683766f3900aa58d8d382f775a90dad7
        B/clauses/window-04/raw.json: 2bc45909a5ad36da7b0d1859bb153bd9575fc50ff76f908a9834adeee68fa39d
        B/clauses/window-04/prompt.txt: d6a6682764cefa9ff6b2beb42cc842fbe15ff998d138f4f783fd72014e7e2ca2
        B/clauses/window-04/meta.json: 212fc66ca654d223883a9c2467181dd617070a6667d4f017386869e25163ea93
        B/clauses/window-05/raw.json: 9dede81d5eeb45f27613759f0d5787a178ded1e0213e6de5a47e660a351c6ae2
        B/clauses/window-05/prompt.txt: e67fbaad829bf59c42bba3124134c20e4e38463bff059cb481456aa7042a8c5c
        B/clauses/window-05/meta.json: d1ecf12cfd0e43c8bad2f8560b81de1e3dff6a3c426a5102221eb1392068253c
        B/clauses/window-02/raw.json: 4587d83d9557f3760bcfe21bdddafa5ac4e603a62f1b8ef9a19969a01002657a
        B/clauses/window-02/prompt.txt: fb0c245d4477d2c1e5f8940221ff322618571fcb779fdf876e84926f344f8195
        B/clauses/window-02/meta.json: 2ea4db44c5002bf8a7092abc44bf5ad980a81b8b371ba41e26c27f0ce59f1729
        B/clauses/window-07/raw.json: 4945da4b2e3695970da4318bed584a86d4c16f273461d48f96cf04fe33762227
        B/clauses/window-07/prompt.txt: 6621a88dd33c51f737f3b14941eb367231e6c4e2c050785ba03603724fba1456
        B/clauses/window-07/meta.json: fa6d693df3ab90294cc7e344ef511fe4c1fadd5d37b87bec42629d08afd3a5e7
        B/clauses/window-01/raw.json: 2ea64bd58dbb0962995d25ec3c318986717e252e9fa72e2aa74e38a4d52f16f6
        B/clauses/window-01/prompt.txt: 024012c9fe8c5a365a723ba1e92a7485894e8bcf96c3fb24a339b250ce8d6f6a
        B/clauses/window-01/meta.json: 410b13ad6bb385ca36bafe454f50217794ef90eca8aaca5b06159b65a4ffc8d6
        B/clauses/window-06/raw.json: 71271362c2c7164476deef2b4c1e0ae01c67f47868e8b6d692a015928b91472e
        B/clauses/window-06/prompt.txt: 64141fb86c9f41014f7ac12b1d2357acc39ccb5802f7209dcf586412db22bf1e
        B/clauses/window-06/meta.json: 1a627b819a11fa219e98af3a741459ffadfda4ed480615524c6aff99ee19c661
        B/clauses/window-08/raw.json: b1f0ac2770685191454865b6a3553f5846c596c89c0069fec03eb3c267a3302b
        B/clauses/window-08/prompt.txt: 085d2167a8e335dc2cfe6bd02da056d211104f10e40c68b1f1b810cf1a175c4a
        B/clauses/window-08/meta.json: a4956b4166ce3020f1e7ebb6cf292e6ed42e30e3053d9a1472d342e04f152ac6
        B/tables/TABLE-1-page-4-2/raw.json: 0da2c842cb639d511abf34e1a5d0559ebcbfcaab69addf2d5f47c5678029b458
        B/tables/TABLE-1-page-4-2/prompt.txt: a84498229a5e906ebe7fadb811edac4d4bbf5d9228ccf0fce0860afd8ce35fe7
        B/tables/TABLE-1-page-4-2/meta.json: 1f66110879bed6a5781fd873e130dda6045953127923e88e82b16d3fbff44793
        B/tables/TABLE-3-page-8-5/raw.json: c72136c2b3b5ea6c55292e3b5804cca482dbabb4fc4ba234f97fc3ccf0dad0ac
        B/tables/TABLE-3-page-8-5/prompt.txt: e20cb2f2a321269ad947ab7faeef6f0f9d5544145329ece47fec63ed2148e826
        B/tables/TABLE-3-page-8-5/meta.json: 97210f2c3a34175c12e315ff9caf470959ba8fa654c27ac243df2c7c94e9635a
        B/tables/TABLE-2-page-6-4/raw.json: e3fe26bef268af0fa3d31c60a6b0d694772dc2de9621c26c4aa62d3d237e7df1
        B/tables/TABLE-2-page-6-4/prompt.txt: 0f56892efab7aa4cc628ea16a47a4ef145474768050516ad2f92fbeb3ff12651
        B/tables/TABLE-2-page-6-4/meta.json: 2bffdd12a1b6cf8cd40bcac10d894c5624e2d4315c8b94d3930c76c51e6bc7bd
        B/tables/TABLE-1-page-3-1/raw.json: eed3d45ca4a65b0946cc2972d484e29bd6d2e32cd04570ce626b4b91a2977bc4
        B/tables/TABLE-1-page-3-1/prompt.txt: ae73619b5e3b64551da1830a4e5726c7be957f12bfb4d48ffb7fb190819146f8
        B/tables/TABLE-1-page-3-1/meta.json: b29f92be80515c6ca0834a7798d7f7318cf1eb0c5319419897e252315661f6e8
        B/tables/TABLE-1-page-6-3/raw.json: 4982fbca84bb90e90a3cf23cc702371f84bed798ce123951eaf37205e9b08b4a
        B/tables/TABLE-1-page-6-3/prompt.txt: f0217ae81f6a2b020d30e446580eb3ebb783c7a8b4a761cf0f2f1528bdedecfb
        B/tables/TABLE-1-page-6-3/meta.json: 8017f67cbbb6cf89c827b110bf51a2fd64c94183bedb0e86a685993fb434762c
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
      pdf_sha256: 157e72766fb6e1e9ce6d22f96620848cc228a1c001212df9dabb7dc69edbb607
      source_review: _compare/relationships-2026-11-16/review-current/Geranmayeh2017
      source_status_sha256: 7bb2270392d2acd7803f06c77f84a40c4e6b7cca17c0277bcd29a884db1efd04
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R019
    exposure:
      text: early language performance and age
    outcome:
      text: language recovery over time
    analysis_label: Multiple regression (Recovery)
    relation: association
    evidence_ids:
    - P7-S1-C2
    qualifier_ids:
    - P7-S1-C1
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 157e72766fb6e1e9ce6d22f96620848cc228a1c001212df9dabb7dc69edbb607
      source_review: _compare/relationships-2026-11-16/review-current/Geranmayeh2017
      source_status_sha256: 7bb2270392d2acd7803f06c77f84a40c4e6b7cca17c0277bcd29a884db1efd04
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P1-S1-C10
      - Accounting without a linked unit P1-S1-C12
      - Accounting without a linked unit P1-S2-C3
      - Accounting without a linked unit P1-S2-C4
      - Unaccounted source passage P1-S2-C4
      - Unaccounted source passage P1-S2-C3
      - Unaccounted source passage P1-S1-C12
      - Result passage disposed without unit P3-S2-C5
      - Accounting without a linked unit P3-S3-C5
      - Unresolved source passage P4-S1-C21
      - Unaccounted source passage P3-S3-C5
      - Result passage disposed without unit P5-S2-C5
      - Accounting without a linked unit P6-S1-C8
      - Accounting without a linked unit P6-S1-C9
      - Unaccounted source passage P6-S1-C9
      - Unaccounted source passage P6-S1-C8
      - Result passage disposed without unit P6-S1-C11
      - Accounting without a linked unit P6-S1-C13
      - Accounting without a linked unit P6-S2-C2
      - Accounting without a linked unit P6-S2-C3
      - Accounting without a linked unit P6-S2-C4
      - Accounting without a linked unit P6-S2-C5
      - Unaccounted source passage P6-S2-C5
      - Unaccounted source passage P6-S2-C2
      - Unaccounted source passage P6-S2-C3
      - Unaccounted source passage P6-S2-C4
      - Unaccounted source passage P6-S1-C13
      - Result passage disposed without unit P6-S2-C6
      - Result passage disposed without unit P7-S1-C11
      - Result passage disposed without unit P7-S2-C11
      - Accounting without a linked unit P7-S2-C16
      - Accounting without a linked unit P7-S2-C17
      - Accounting without a linked unit P7-S3-C1
      - Accounting without a linked unit P7-S3-C2
      - Accounting without a linked unit P7-S3-C4
      - Accounting without a linked unit P7-S3-C5
      - Unaccounted source passage P7-S3-C1
      - Unaccounted source passage P7-S3-C2
      - Unaccounted source passage P7-S2-C16
      - Unaccounted source passage P7-S3-C5
      - Unaccounted source passage P7-S2-C17
      - Unaccounted source passage P7-S3-C4
      - Result passage disposed without unit P8-S1-C4
      - Accounting without a linked unit P8-S1-C6
      - Accounting without a linked unit P8-S2-C5
      - Result passage disposed without unit P9-S2-C2
      - Result passage disposed without unit P9-S2-C4
      - Unaccounted source passage P8-S1-C6
      - Unaccounted source passage P8-S2-C5
      - Result passage disposed without unit P10-S1-C2
      - Result passage disposed without unit P10-S1-C11
      unattached_null_or_qualifier_ids:
      - P6-S1-C11
      - P6-S2-C6
      - P7-S2-C16
      - P7-S3-C2
      - P9-S2-C2
      suppressed_nonrepresented_units: 9
      default_disposition_count_requires_completeness_check: 179
      unselected_timing_passages:
      - P1-S1-C6
      - P2-S3-C2
      - P2-S3-C11
      - P3-S1-C5
      - P3-S3-C4
      - P9-S2-C7
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P1-S2-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S2-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S2-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S2-C17
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S2-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P2-S3-C5
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P4-S2-C7
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P5-S2-C10
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P7-S3-C3
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: tested_personal_effects
        source_id: P7-S2-C10
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P8-S2-C1
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P9-S2-C5
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: outcome_timing
        source_ids:
        - P3-S2-C6
        - P6-S2-C5
        - P6-S2-C7
        - P7-S1-C11
        - P7-S2-C17
        - P8-S1-C4
        - P8-S1-C6
        - P8-S2-C1
        - P10-S1-C4
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: personal_factors
        source_ids:
        - P6-S2-C4
        - P6-S2-C6
        - P7-S1-C11
        - P7-S2-C10
        - P7-S2-C16
        - P8-S1-C4
        - P8-S1-C6
        - P8-S2-C1
        - P9-S2-C4
        - P9-S2-C5
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: adjustment_roles
        source_ids:
        - P1-S2-C3
        - P6-S2-C5
        - P6-S2-C7
        - P7-S2-C9
        - P7-S2-C10
        - P7-S2-C14
        - P7-S2-C16
        - P8-S1-C5
        - P8-S1-C6
        - P8-S2-C1
        - P9-S2-C4
        - P9-S2-C5
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - outcome_timing
      - validation
      - personal_factors
      - adjustment_roles
      - explicitly_not_adjusted
      unclassified_extraction_ids:
      - P4-S1-C21
      - P6-S3-C1
      table_review_required:
      - TABLE-1-page-3-1
      - TABLE-1-page-4-2
      - TABLE-1-page-6-3
      - TABLE-2-page-6-4
      - TABLE-3-page-8-5
      unlinked_tables:
      - TABLE-1-page-3-1
      - TABLE-1-page-4-2
      - TABLE-1-page-6-3
      - TABLE-2-page-6-4
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P2-S2
        - P3-S1
        - P3-S2
        - P4-S2
        - P5-S1
        - P5-S2
        - P6-S2
        - P7-S1
        - P7-S3
        - P8-S2
        - P9-S2
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 157e72766fb6e1e9ce6d22f96620848cc228a1c001212df9dabb7dc69edbb607
      source_review: _compare/relationships-2026-11-16/review-current/Geranmayeh2017
      source_status_sha256: 7bb2270392d2acd7803f06c77f84a40c4e6b7cca17c0277bcd29a884db1efd04
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C10
      disposition: represented
      result_indexes: []
      reason: Descriptive of task-evoked activity, not a relationship with clinical
        outcome.
    - source_id: P1-S1-C11
      disposition: represented
      result_indexes:
      - 0
      - 1
      reason: Establishes positive correlation between preSMA/dACC activity and recovery.
    - source_id: P1-S1-C12
      disposition: represented
      result_indexes:
      - 0
      - 1
      reason: Provides specific correlation values for early and late phases.
    - source_id: P1-S2-C3
      disposition: represented
      result_indexes:
      - 8
      reason: Identifies preSMA/dACC as a predictor of language outcome at 4 months.
    - source_id: P1-S2-C4
      disposition: represented
      result_indexes:
      - 7
      reason: Confirms relationship via voxel-wise correlation analysis.
    - source_id: P2-S3-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports average lesion volume (demographic/descriptive).
    - source_id: P3-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports average lesion volume (demographic/descriptive).
    - source_id: P3-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes PCA result to justify choice of language measure.
    - source_id: P3-S3-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports correlation of lesion volumes across sessions.
    - source_id: P4-S1-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Example of patient response.
    - source_id: P5-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes volume excluded from analysis.
    - source_id: P5-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Lists numbered regions in Figure 3.
    - source_id: P5-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports thalamic activation (descriptive).
    - source_id: P6-S1-C8
      disposition: represented
      result_indexes: []
      reason: Reports reduced performance in patients vs controls (cross-sectional
        baseline).
    - source_id: P6-S1-C9
      disposition: represented
      result_indexes: []
      reason: Reports reduced performance in patients vs controls (cross-sectional
        baseline).
    - source_id: P6-S1-C10
      disposition: represented
      result_indexes: []
      reason: Reports significant effect of session (general recovery).
    - source_id: P6-S1-C11
      disposition: represented
      result_indexes: []
      reason: Reports improvement across assessments.
    - source_id: P6-S1-C13
      disposition: represented
      result_indexes:
      - 8
      - 9
      - 10
      reason: Correlates early cognitive score, language measure, and decision accuracy
        with 4-month performance.
    - source_id: P6-S2-C2
      disposition: represented
      result_indexes:
      - 11
      reason: Correlates early reaction time with 4-month outcome.
    - source_id: P6-S2-C3
      disposition: represented
      result_indexes:
      - 12
      - 13
      - 14
      reason: Correlates lesion volume and network damage with 4-month outcome.
    - source_id: P6-S2-C4
      disposition: represented
      result_indexes:
      - 15
      - 16
      - 17
      reason: Correlates education, age, and therapy with 4-month outcome.
    - source_id: P6-S2-C5
      disposition: represented
      result_indexes:
      - 18
      reason: Provides variance explained by the outcome regression model.
    - source_id: P6-S2-C6
      disposition: represented
      result_indexes:
      - 18
      reason: Identifies significant predictors (language measure, age) for outcome.
    - source_id: P7-S1-C1
      disposition: represented
      result_indexes:
      - 19
      reason: Provides variance explained by the recovery regression model.
    - source_id: P7-S1-C2
      disposition: represented
      result_indexes:
      - 19
      reason: Identifies significant predictors (language performance, age) for recovery.
    - source_id: P7-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes anatomical extent of the cluster.
    - source_id: P7-S2-C4
      disposition: represented
      result_indexes: []
      reason: Reports null effect of session and session*recovery interaction.
    - source_id: P7-S2-C5
      disposition: represented
      result_indexes:
      - 20
      reason: Reports significant main effect of recovery on preSMA/dACC activity.
    - source_id: P7-S2-C11
      disposition: represented
      result_indexes:
      - 2
      - 3
      - 4
      reason: States all three GLM models were significant.
    - source_id: P7-S2-C12
      disposition: represented
      result_indexes:
      - 2
      reason: Identifies preSMA/dACC activity as a significant predictor of recovery.
    - source_id: P7-S2-C13
      disposition: represented
      result_indexes:
      - 2
      reason: Provides effect size for preSMA/dACC activity in Model 1.
    - source_id: P7-S2-C14
      disposition: represented
      result_indexes:
      - 3
      reason: Confirms significance of preSMA/dACC activity after adding lesion volume.
    - source_id: P7-S2-C15
      disposition: represented
      result_indexes:
      - 3
      reason: Reports lesion volume as non-significant in Model 2.
    - source_id: P7-S2-C16
      disposition: represented
      result_indexes:
      - 4
      reason: Confirms significance of preSMA/dACC activity after adding age and early
        language score.
    - source_id: P7-S2-C17
      disposition: represented
      result_indexes:
      - 8
      reason: Extends GLM results to language outcome at 4 months.
    - source_id: P7-S3-C1
      disposition: represented
      result_indexes:
      - 0
      - 1
      reason: Reports positive correlations for early and late scans.
    - source_id: P7-S3-C4
      disposition: represented
      result_indexes:
      - 7
      reason: Identifies the cluster encompassing dACC, preSMA, and SMA.
    - source_id: P7-S3-C5
      disposition: represented
      result_indexes:
      - 7
      reason: Reports peak voxel significance for the whole-brain correlation.
    - source_id: P8-S1-C2
      disposition: repeated
      result_indexes:
      - 0
      - 1
      - 2
      - 4
      reason: Restatement of preSMA/dACC activity correlating with recovery.
    - source_id: P8-S2-C1
      disposition: repeated
      result_indexes:
      - 2
      - 3
      - 4
      - 8
      reason: Restatement of GLM results from Table 3.
    - source_id: P9-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison with healthy controls from previous study.
    - source_id: P9-S2-C4
      disposition: repeated
      result_indexes:
      - 2
      - 3
      - 4
      reason: Restatement of predictive value of activity, initial severity, and age.
    - source_id: P9-S2-C9
      disposition: represented
      result_indexes:
      - 7
      reason: Describes the cluster of activity correlating with recovery.
    - source_id: P9-S2-C10
      disposition: represented
      result_indexes:
      - 7
      reason: Identifies other regions (pre/post-central gyri, temporal gyrus) correlating
        with recovery.
    - source_id: P9-S2-C11
      disposition: represented
      result_indexes:
      - 7
      reason: Reports peak voxel significance for whole-brain correlation.
    - source_id: P10-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports on vascular reactivity (methodological control).
    - source_id: P10-S1-C4
      disposition: repeated
      result_indexes:
      - 0
      - 1
      reason: Restatement of predictive value of absolute activation at each time
        point.
    - source_id: P10-S1-C6
      disposition: represented
      result_indexes: []
      reason: Reports null relationship between recovery and other cingular-opercular
        network regions.
    - source_id: P10-S1-C11
      disposition: represented
      result_indexes:
      - 3
      reason: States preSMA/dACC effect is not simply related to overall lesion volume.
    - source_id: P10-S2-C1
      disposition: repeated
      result_indexes:
      - 3
      reason: Restatement of the non-simple relationship with lesion volume.
    - source_id: P10-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of network activity during difficult tasks.
    unresolved_coverage:
    - source_id: P1-S1-C10
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P6-S1-C8
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P6-S1-C9
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P6-S1-C10
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P6-S1-C11
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P7-S2-C4
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P8-S2-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P10-S1-C6
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P10-S2-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P10-S2-C2
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P7-S1-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P7-S1-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P7-S1-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P7-S1-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P7-S3-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S1-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S1-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S2-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S2-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C10
    - P1-S1-C11
    - P2-S3-C14
    - P3-S1-C1
    - P3-S2-C5
    - P3-S3-C5
    - P4-S1-C13
    - P5-S1-C9
    - P5-S2-C4
    - P5-S2-C5
    - P6-S1-C8
    - P6-S1-C9
    - P6-S1-C10
    - P6-S1-C11
    - P6-S2-C5
    - P7-S1-C1
    - P7-S1-C4
    - P7-S1-C5
    - P7-S1-C6
    - P7-S1-C11
    - P7-S2-C4
    - P7-S2-C11
    - P7-S2-C15
    - P7-S3-C2
    - P8-S1-C2
    - P8-S1-C4
    - P8-S1-C6
    - P8-S2-C5
    - P9-S2-C2
    - P9-S2-C4
    - P9-S2-C9
    - P9-S2-C10
    - P9-S2-C11
    - P10-S1-C2
    - P10-S1-C4
    - P10-S1-C6
    - P10-S1-C11
    - P10-S2-C7
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-3-1
    - TABLE-1-page-4-2
    - TABLE-1-page-6-3
    - TABLE-2-page-6-4
    - TABLE-3-page-8-5
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P2-S3-C10
      - P3-S1-C5
      recruited_sample:
      - P2-S3-C8
      - P2-S3-C10
      - P3-S1-C5
      eligibility:
      - P2-S3-C8
      - P2-S3-C9
      imaging_provenance:
      - P4-S2-C7
      - P5-S2-C10
      imaging_timing:
      - P2-S3-C10
      - P4-S1-C4
      outcome_timing: []
      outcome_definition:
      - P3-S2-C6
      validation: []
      analysis_restrictions:
      - P5-S1-C8
      - P5-S1-C9
      - P5-S1-C10
      - P7-S1-C6
      dependent_variable_statement:
      - P7-S2-C6
      limitations:
      - P10-S1-C7
      - P10-S1-C9
      personal_factors: []
      tested_personal_effects:
      - P6-S2-C4
      - P6-S2-C6
      - P7-S2-C16
      - P8-S1-C4
      - P8-S1-C6
      - P9-S2-C4
      adjustment_roles: []
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P2-S3-C11
      - P3-S1-C5
      - P6-S2-C4
    outcome_type: both_reported
    imaging_vs_outcome: mixed
    validation_type: internal_cross_validation
    held_selections:
    - slot: dependent_variable_statement
      source_id: P1-S2-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S2-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S2-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S2-C17
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S2-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P2-S3-C5
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P4-S2-C7
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P5-S2-C10
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P7-S3-C3
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: tested_personal_effects
      source_id: P7-S2-C10
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P8-S2-C1
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P9-S2-C5
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: outcome_timing
      source_ids:
      - P3-S2-C6
      - P6-S2-C5
      - P6-S2-C7
      - P7-S1-C11
      - P7-S2-C17
      - P8-S1-C4
      - P8-S1-C6
      - P8-S2-C1
      - P10-S1-C4
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: personal_factors
      source_ids:
      - P6-S2-C4
      - P6-S2-C6
      - P7-S1-C11
      - P7-S2-C10
      - P7-S2-C16
      - P8-S1-C4
      - P8-S1-C6
      - P8-S2-C1
      - P9-S2-C4
      - P9-S2-C5
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: adjustment_roles
      source_ids:
      - P1-S2-C3
      - P6-S2-C5
      - P6-S2-C7
      - P7-S2-C9
      - P7-S2-C10
      - P7-S2-C14
      - P7-S2-C16
      - P8-S1-C5
      - P8-S1-C6
      - P8-S2-C1
      - P9-S2-C4
      - P9-S2-C5
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
      pdf_sha256: 157e72766fb6e1e9ce6d22f96620848cc228a1c001212df9dabb7dc69edbb607
      review_sha256: f4976444b35a74aa6c6d4d0ddf7cc67bca1cac6d6c9f092a92319f8ff2432088
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
      - P7-S1-C2
      source_result: In a multiple regression model predicting language recovery (defined
        as improvement in scores between Time 1 and Time 2), early language performance
        and age were the only overall significant predictors. The model accounted
        for 63% of the variance in language recovery.
      result_status: detected
      patient_measurement: non_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The source P7-S1-C2 explicitly describes a multiple regression model
            where 'early language performance' and 'age' are the significant predictors
            of 'language recovery over time'. This matches the selected analysis label
            and evidence ID.
          source_ids:
          - P7-S1-C2
          - P7-S1-C1
        direction:
          answer: fits
          reason: The source states these were the 'overall significant predictors'.
            The proposed claim 'Early language performance and age were the only overall
            significant predictors' accurately reflects the detection of association.
            The direction of the coefficients (positive for early language, negative
            for age) is not explicitly detailed in the proposed claim text, but the
            claim of 'significant predictors' is directionally faithful to the source's
            assertion of significance.
          source_ids:
          - P7-S1-C2
        construct:
          answer: fits
          reason: The exposure (early language performance, age) and outcome (language
            recovery) are correctly identified. The measurement is non-imaging (behavioral
            language scores), which is correct for this specific regression analysis,
            distinct from the fMRI analyses in the paper.
          source_ids:
          - P7-S1-C2
          - P3-S2-C6
        qualifications:
          answer: fits
          reason: The qualification that language recovery was defined as improvement
            in scores between Time 1 and Time 2 is present in the proposed draft and
            supported by P3-S2-C6. The draft correctly identifies this as a behavioral
            analysis.
          source_ids:
          - P3-S2-C6
          - P7-S1-C2
        missing_material_caveat:
          answer: fits
          reason: No material caveats are missing. The draft correctly notes the definition
            of recovery. The sample size and timing are marked as pending, which is
            appropriate given the OCR warnings and the qualitative nature of the draft.
          source_ids:
          - P7-S1-C2
      optional_pending:
      - Sample size requires source confirmation; it has not been transcribed.
      - 'sample.time_post_onset: source confirmation required; original proposed wording
        remains in the audit.'
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Sample size requires source confirmation; it has not been transcribed.
    - 'sample.time_post_onset: source confirmation required; original proposed wording
      remains in the audit.'
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Sample size requires source confirmation; it has not been transcribed.
    - 'sample.time_post_onset: source confirmation required; original proposed wording
      remains in the audit.'
    normalizations:
    - field: sample.n
      original: 27
      action: not_transcribed
      reason: Not supported by selected quotations
    - field: sample.time_post_onset
      original: early phase (approximately 2 weeks) to approximately 4 months after
        stroke
      action: not_transcribed
      reason: 'Numbers not grounded in usable selected source readings: 2, 4'
    analysis_identity:
      id: R019
      exposure:
        text: early language performance and age
      outcome:
        text: language recovery over time
      analysis_label: Multiple regression (Recovery)
      relation: association
      evidence_ids:
      - P7-S1-C2
      qualifier_ids:
      - P7-S1-C1
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 157e72766fb6e1e9ce6d22f96620848cc228a1c001212df9dabb7dc69edbb607
        source_review: _compare/relationships-2026-11-16/review-current/Geranmayeh2017
        source_status_sha256: 7bb2270392d2acd7803f06c77f84a40c4e6b7cca17c0277bcd29a884db1efd04
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P7-S1-C2:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 157e72766fb6e1e9ce6d22f96620848cc228a1c001212df9dabb7dc69edbb607
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: cc128aa4a2671a0398ffc34db925542937b845b5a5518249e84fc9e00f73bbe9
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P7-S1-C2
          page: 7
          text_layer_sha256: cc128aa4a2671a0398ffc34db925542937b845b5a5518249e84fc9e00f73bbe9
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: "Again, only early\nlanguage performance (beta = \x040.813,\
          \ P = 0.002) and age\n(beta = \x040.306, P = 0.047) were the overall signiﬁcant\
          \ pre-\ndictors of language recovery over time."
        anchor_text: "Again, only early\nlanguage performance (beta = \x040.813, P\
          \ = 0.002) and age\n(beta = \x040.306, P = 0.047) were the overall signiﬁcant\
          \ pre-\ndictors of language recovery over time."
        excluded_fragments: []
      P2-S3-C10:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 157e72766fb6e1e9ce6d22f96620848cc228a1c001212df9dabb7dc69edbb607
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 8e220354ccfbbb733d201766275f58b7d9b99a2f0523492503d088b179202895
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S3-C10
          page: 2
          text_layer_sha256: 8e220354ccfbbb733d201766275f58b7d9b99a2f0523492503d088b179202895
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: "Twenty-seven participants were scanned at two time points;\n\
          ﬁrst in the early phase after the stroke [15 \x02 7.6 days,\nmean \x02 standard\
          \ deviation (SD)] and again at \x034 months\n(108 \x02 26\ndays)\nafter\n\
          an\naverage\ninterscan\ninterval\nof\n93 \x02 26 days."
        anchor_text: "Twenty-seven participants were scanned at two time points;\n\
          ﬁrst in the early phase after the stroke [15 \x02 7.6 days,\nmean \x02 standard\
          \ deviation (SD)] and again at \x034 months\n(108 \x02 26\ndays)\nafter\n\
          an\naverage\ninterscan\ninterval\nof\n93 \x02 26 days."
        excluded_fragments: []
      P3-S2-C6:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 157e72766fb6e1e9ce6d22f96620848cc228a1c001212df9dabb7dc69edbb607
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 9e0c0f32504b846fca0d91ab39d5af6c0c106efa020766f25f11d46d4fdc2c8b
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S2-C6
          page: 3
          text_layer_sha256: 9e0c0f32504b846fca0d91ab39d5af6c0c106efa020766f25f11d46d4fdc2c8b
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: "The language\noutcome was deﬁned as the raw score at \x03\
          4 months post-\nictus, and the language recovery was deﬁned as improvement\n\
          in the scores over time (Time 2 \x04 Time 1)."
        anchor_text: "The language\noutcome was deﬁned as the raw score at \x034 months\
          \ post-\nictus, and the language recovery was deﬁned as improvement\nin\
          \ the scores over time (Time 2 \x04 Time 1)."
        excluded_fragments: []
      P2-S3-C2:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 157e72766fb6e1e9ce6d22f96620848cc228a1c001212df9dabb7dc69edbb607
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 5707f08c4f9d974db06c2eada2610aafa52f2fd22f053c61ce4509a5c41158d2
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S3-C2
          page: 2
          text_layer_sha256: 5707f08c4f9d974db06c2eada2610aafa52f2fd22f053c61ce4509a5c41158d2
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: "Speciﬁcally, a cohort of patients undertook event-\nrelated\
          \ functional MRI tasks ﬁrst at \x032 weeks (early scan)\nand then at \x03\
          4 months (late scan) after a left hemisphere\nstroke."
        anchor_text: "Speciﬁcally, a cohort of patients undertook event-\nrelated\
          \ functional MRI tasks ﬁrst at \x032 weeks (early scan)\nand then at \x03\
          4 months (late scan) after a left hemisphere\nstroke."
        excluded_fragments: []
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 7
  quote: "Again, only early\nlanguage performance (beta = \x040.813, P = 0.002) and\
    \ age\n(beta = \x040.306, P = 0.047) were the overall signiﬁcant pre-\ndictors\
    \ of language recovery over time."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-24'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
