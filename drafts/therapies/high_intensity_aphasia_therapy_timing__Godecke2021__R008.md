---
id: high_intensity_aphasia_therapy_timing
name: high intensity aphasia therapy timing
kind: therapy
findings:
- id: f1
  target: time_to_first_therapy
  target_kind: impairment
  claim: Participants in the high intensity therapy groups received treatment two
    days earlier than those receiving usual care.
  direction: likely
  relationship: treatment_response
  method: clinical_RCT
  sample:
    n: not_reported
    population: Not transcribed; confirm from the original PDF population and timing
      passages.
    phase: not_reported
    time_post_onset: Concurrent with the intervention period in the acute post-stroke
      phase
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - The finding describes a difference in delivery timing rather than a clinical outcome
  evidence_quality: RCT
  strength: weak
  notes: 'Exposure measurement: A high-intensity therapy regimen (UC-Plus or VERSE)
    consisting of approximately 5 hours of direct aphasia therapy per week, compared
    to usual care (UC). High intensity groups included both UC-Plus and VERSE arms;
    Usual care was not controlled for amount, frequency, or type. Additional metadata
    has not been transcribed; review the pending-field flags before approval.'
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
    - not_transcribed:sample.population
    - proposed_concept:time_to_first_therapy
  therapy:
    id: high_intensity_aphasia_therapy
    name: high intensity aphasia therapy
  citation: '@Godecke2021'
  source_passages:
  - section: Original source P5-S1-C14
    page: 5
    quote: 'As intended, the

      high intensity groups received treatment two days ear-

      lier than those receiving UC (p ¼ 0.008).'
    supports: claim
  - section: Original source P3-S2-C2
    page: 3
    quote: 'Eligibility criteria

      Participants were aged over 18 years and admitted to

      hospital with an acute stroke, resultant acute aphasia of

      any type, within 14 days of stroke onset.'
    supports: sample
  - section: Original source P5-S1-C9
    page: 5
    quote: 'One

      randomized participant withdrew consent; their data

      were withdrawn from analysis (N ¼ 245).'
    supports: sample
  - section: Original source P3-S1-C7
    page: 3
    quote: 'Methods

      Study design

      A phase three, multicenter, randomized controlled trial,

      with allocation 1:2 (UC: UC-Plus and VERSE) and

      blinded outcomes assessed at 12 (primary outcome)

      and 26 weeks post stroke.'
    supports: method
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-24'
relationship_review:
  paper: Godecke2021
  proposal_id: R008
  review_status_sha256: 8bb819a9db33b698a7927d185024bd7f9ce3b010e9bdb39ff8eab174004b925b
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: fde5e768424dda3995a78864524c91a56e61002acc1f3fd76f7f9447c757774c
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: fde5e768424dda3995a78864524c91a56e61002acc1f3fd76f7f9447c757774c
        A/passages.json: 73d59662839b66d47eb56216b43a5b5484907947a17df0be691592c99a0b4fab
        A/raw.json: 1439e5158778c8d0c667b0121463b431e27c86259a12d66b86841a80f8d67648
        A/source-units.json: 0f3d0d726338d115ab449a2ad725e2ad7b2fdf30b114c0af1eaab7a1599c50a5
        A/full-source-units.json: c077bb5e22bd052941423403d5219ec4ca673194a0868f4b00f56ce61a09c20f
        A/meta.json: 35b3effe17f81468019e16ac9d01fa2068a64dfbcc12f990c714fbbb70ba942f
        A/table-images/TABLE-S3-page-4-1.png: 824798cd0fd6c33ab956ec30c420b2a62e54e61c327135f3e41678968fc4bd5a
        A/table-images/TABLE-1-page-5-1.png: f2e600803516048e0d0fc803810bcffa25f87677310d3dab7aafd0ad763123aa
        A/table-images/TABLE-4-page-10-1.png: 20aab0973394225f3182a873f39499af81bc5fb3071754f5360c93d9d9c07cde
        A/table-images/page-12.png: 2386d74cda135fc04a6f2bac3b7b90e301a2aa262206803940cc6588d9a19769
        A/table-images/page-10.png: a419f28bc95155bac6cf2cd4d064aadbd99ea373048faade0fc22e8251d8b7fb
        A/table-images/TABLE-3-page-9-1.png: 9272807506b747f2445afb329ec3d4a805ce6ad68d2e24d10811e2baf600bcd5
        A/table-images/page-11.png: f5f375f747594aef43bab866ac4af3d1c682414e84ecd6b5a980672322326442
        A/table-images/TABLE-2-page-8-1.png: e003b7fd4d6d9074538a7e8222846a3682eea989d36d6a31fa37ad1e3d56fdb1
        A/table-images/page-7.png: 29bc5b0f7d331644de39b54edb1db0dd2f9258a60fa879128e2c62f504b7aa36
        A/table-images/page-5.png: 8b092fbe2991b6f82c844c5c6338b7e85dede4cb053782ceaa49ddee79a8ddd2
        A/table-images/page-4.png: 333fd59efc48b4a7e10c0d5eac43a05ea3a9198baf91cf0e7a9050d5945f1123
        A/table-images/page-9.png: bab7ef998a950467b39dd4fb2eb3f28e11cd70d7860b8a3e23efea18e8fc3fef
        A/table-images/page-8.png: df603d323f238251d1317fbf286b586f2fa89db63afe432061bc97f206e62282
        A/table-images/TABLE-5-page-11-1.png: e0f6d2d15ee97f0de8bc22f80dd5258caeb65785eb133bf29a5f380ae8035d85
        A/table-images/manifest.json: 0601265c13f674676591b420fba4e1e53f51a43f6a96f8984d065e304f56542f
        A/table-images/TABLE-5-page-12-1.png: fa49a521d3538a441bd6102191745ed6b7801e5631812f939ddf07116fc0b95f
        A/table-images/TABLE-2-page-7-1.png: 47c894f976d2286b78a1ea1d527e434caa5977fa49567808ea4715ec983e4ff2
        A/clauses/window-03/raw.json: 1bd4970498616dab83ab98473a5512295030c0f30bd95822499a6e886ef54697
        A/clauses/window-03/prompt.txt: acb6878b13e56c15a7e5641a26d3defba22c8a285f2378f15868423b76a673a1
        A/clauses/window-03/meta.json: 5b6885ab429c33043d47e7c14a74656d13786bb4e276eec2563e42f67975626b
        A/clauses/window-04/raw.json: 2aefd06a33401030660d5856ec158d36daef03339cf2278627788a3985f34292
        A/clauses/window-04/prompt.txt: da0d8d6457fa1fbce13adcba737759938df8818321c4193db66c5f9b91fb91c8
        A/clauses/window-04/meta.json: 8fb01952bd783a869cc4a6db040c3880941c59dccc7796f9402f356506e6eb3f
        A/clauses/window-05/raw.json: 217e8286a65e0a5f476cc0f69aeec9129b65c8699f06a0fa1c3e1d74240a5cda
        A/clauses/window-05/prompt.txt: ea3fd9d7f7fb20d8dd631e3c5bcb2a4fdd787be601855a1b95abf93bd3697af8
        A/clauses/window-05/meta.json: ac7903cba5f3da801601396ab29e11f75623524a6f4b00c1178b2f960a1be053
        A/clauses/window-02/raw.json: d33eb4999d8093bcdab8e9711506da9f5b522a554c4f7a06375c9b067df6279e
        A/clauses/window-02/prompt.txt: 7693d7946f43c8e1ac90a7e027ce09f94a4b15f695b0c02d985405f8dcc17d48
        A/clauses/window-02/meta.json: eaf9312660e61260f2894d07930ba86a9754fa1374a3949b667eb45df38bfb7a
        A/clauses/window-07/raw.json: c4c315f52d33ff636163630be0ec0e0baad94ca86e5800c93384a2988d1f84b5
        A/clauses/window-07/prompt.txt: 7b93ca81a9cb3a108129e780f485e3431cbcc79112a152707b1cdc4e9c00e0b5
        A/clauses/window-07/meta.json: ebd8beea64f73f3aeaa50b7a2a5543e42683ec4bf8ea7aea506e096fc7fd2e32
        A/clauses/window-01/raw.json: de26ea37b711eb15595837a63fbed09ff5867966df9ddd55935924f249bb7064
        A/clauses/window-01/prompt.txt: 4352fec59d1a47132404cb20c66c6be11666d6a1386af8bd6946cf575ae0b965
        A/clauses/window-01/meta.json: 487f33eb78f02a5ad222553d04b984dea23c61fb3fa9fcb54a3f9e6c6bdbf68b
        A/clauses/window-06/raw.json: e2dbf921ddee412674cb556f95ae5750e1a593ef55b568c474e227a569702bc3
        A/clauses/window-06/prompt.txt: 3978980ad5a21e711aa9c00e7717ee048f492a9ec8c31a37aa5f241333234466
        A/clauses/window-06/meta.json: 2ecc75b4eba060537c712ca19d30b45b1b41b970974716ddc0773d13980be247
        A/tables/TABLE-4-page-10-6/raw.json: 27326785d9e5e5c254806a70332368cb572f0f4f195b0e05cf22b8637611b44d
        A/tables/TABLE-4-page-10-6/prompt.txt: 0091caa6694e0bd20c564c65a1ae916557eab464a6785426613c0895e9e03c1b
        A/tables/TABLE-4-page-10-6/meta.json: b4a55982267632bca6527f6f6eace2ad004ff40bf7dcb2a190821c9957679057
        A/tables/TABLE-2-page-8-4/raw.json: 1106b485c798370b4539a5a5c4cdbe79b4761ddf696dcef40f0d81542199f74e
        A/tables/TABLE-2-page-8-4/prompt.txt: 6977dfcd25fc37825b258df831a235d5cd53f1c4457d474fa7b73fdedb77812a
        A/tables/TABLE-2-page-8-4/meta.json: 38dd0e064315b76c17b4567a96d28ee819830fca45cf387572ae615ac87686cd
        A/tables/TABLE-1-page-5-2/raw.json: 494aea7d4dfce8c408d64247156b8c82afb19638f636646ba117b9385e51240a
        A/tables/TABLE-1-page-5-2/prompt.txt: 51318dbc1b7b87ece95f08173e8f428067d62d1d4410584837b48338a82ca239
        A/tables/TABLE-1-page-5-2/meta.json: 8fc2f7c347df1e46423df9b95ed88b07fd0414f59d08356c5c63dfa5414646b7
        A/tables/TABLE-S3-page-4-1/raw.json: 1c9b4cea569fe000a10b7435a52ffadc0349ef9b4f8fab95ed123f65b88c5a1f
        A/tables/TABLE-S3-page-4-1/prompt.txt: 5d86ac289f610f72c2f4db306e9d39ed82fdc46bd1bfaf7d6f2bab516f56013e
        A/tables/TABLE-S3-page-4-1/meta.json: dc3437f4d64a0e976a12f174638cb93aa51ae9053a3ad64811dec0255ea121a7
        A/tables/TABLE-3-page-9-5/raw.json: ec976c2164f32b65de64f244ce6880a112900886a3e806e6ce0ddcbaf93799d0
        A/tables/TABLE-3-page-9-5/prompt.txt: 396be003ba82595252a76819918679bd180a4b1236388cf7609d07b686bc4941
        A/tables/TABLE-3-page-9-5/meta.json: 0c426020e89e099f99353a7157207acee329976aeb74b1e728284205a3eae7d8
        A/tables/TABLE-2-page-7-3/raw.json: e0b568fd5729a852c3098ceec2827dcdf904330542e7a409315f7712d354d72d
        A/tables/TABLE-2-page-7-3/prompt.txt: a04b1ce380aa38ffca19efdcbd01814c2db2247c182f62e59f2f93d022ab36d2
        A/tables/TABLE-2-page-7-3/meta.json: 101befef1593ab56a76e05af52cbbcfc08752f2957fbe96fb1c1650988d3d187
        A/tables/TABLE-5-page-12-8/raw.json: 80847e595d01a74b76617750d68660c1f499c0b1cd5251cf1134e05bd37282ac
        A/tables/TABLE-5-page-12-8/prompt.txt: 2c41eb07df15503c63753c930bc626805f2bcbd400b321117811a5d093e9a5a5
        A/tables/TABLE-5-page-12-8/meta.json: 236370534be54e814b2059d0faec3c0e0c56790157a545c65fb89e06d236b613
        A/tables/TABLE-5-page-11-7/raw.json: ff2b901506716d3551de6429548df7b05d48f4ef44022a86645927ab103f5fcd
        A/tables/TABLE-5-page-11-7/prompt.txt: fa6c25c5fd410a260289bec65cb4466fb6465994d41b98d7862191b53a204466
        A/tables/TABLE-5-page-11-7/meta.json: b4d335ae55c5e54c35c3b41f0941fac2c8ae053baab5f9447323f06bc2d17673
        B/passages.json: 73d59662839b66d47eb56216b43a5b5484907947a17df0be691592c99a0b4fab
        B/raw.json: bc1d0299c1dedf717c8c5e403db48282cc27df14d199c2f3864f97566eaff365
        B/source-units.json: 0f3d0d726338d115ab449a2ad725e2ad7b2fdf30b114c0af1eaab7a1599c50a5
        B/full-source-units.json: c077bb5e22bd052941423403d5219ec4ca673194a0868f4b00f56ce61a09c20f
        B/meta.json: ad5d2d87b69e3f945fcd8500fcbdfd44c9a0f3c898c21a759ae61f2414be39cf
        B/table-images/TABLE-S3-page-4-1.png: 824798cd0fd6c33ab956ec30c420b2a62e54e61c327135f3e41678968fc4bd5a
        B/table-images/TABLE-1-page-5-1.png: f2e600803516048e0d0fc803810bcffa25f87677310d3dab7aafd0ad763123aa
        B/table-images/TABLE-4-page-10-1.png: 20aab0973394225f3182a873f39499af81bc5fb3071754f5360c93d9d9c07cde
        B/table-images/page-12.png: 2386d74cda135fc04a6f2bac3b7b90e301a2aa262206803940cc6588d9a19769
        B/table-images/page-10.png: a419f28bc95155bac6cf2cd4d064aadbd99ea373048faade0fc22e8251d8b7fb
        B/table-images/TABLE-3-page-9-1.png: 9272807506b747f2445afb329ec3d4a805ce6ad68d2e24d10811e2baf600bcd5
        B/table-images/page-11.png: f5f375f747594aef43bab866ac4af3d1c682414e84ecd6b5a980672322326442
        B/table-images/TABLE-2-page-8-1.png: e003b7fd4d6d9074538a7e8222846a3682eea989d36d6a31fa37ad1e3d56fdb1
        B/table-images/page-7.png: 29bc5b0f7d331644de39b54edb1db0dd2f9258a60fa879128e2c62f504b7aa36
        B/table-images/page-5.png: 8b092fbe2991b6f82c844c5c6338b7e85dede4cb053782ceaa49ddee79a8ddd2
        B/table-images/page-4.png: 333fd59efc48b4a7e10c0d5eac43a05ea3a9198baf91cf0e7a9050d5945f1123
        B/table-images/page-9.png: bab7ef998a950467b39dd4fb2eb3f28e11cd70d7860b8a3e23efea18e8fc3fef
        B/table-images/page-8.png: df603d323f238251d1317fbf286b586f2fa89db63afe432061bc97f206e62282
        B/table-images/TABLE-5-page-11-1.png: e0f6d2d15ee97f0de8bc22f80dd5258caeb65785eb133bf29a5f380ae8035d85
        B/table-images/manifest.json: e050a8993e032a7004d33e48254f60ddd5011e81cffbbc039f1c93acf30dd116
        B/table-images/TABLE-5-page-12-1.png: fa49a521d3538a441bd6102191745ed6b7801e5631812f939ddf07116fc0b95f
        B/table-images/TABLE-2-page-7-1.png: 47c894f976d2286b78a1ea1d527e434caa5977fa49567808ea4715ec983e4ff2
        B/clauses/window-03/raw.json: 360994410aa56f88ec999dbf52f2dd593491fdd8254261a7cb5f284fef09def0
        B/clauses/window-03/prompt.txt: acb6878b13e56c15a7e5641a26d3defba22c8a285f2378f15868423b76a673a1
        B/clauses/window-03/meta.json: 92ef17d095cb41fab1f90a1390783be1e46b83e77b607c0306db7daa5fe9aba2
        B/clauses/window-04/raw.json: 7955ae0827064a0ca2331f61d9fc79ba13804f14e1bf84b7327adec44c1b918e
        B/clauses/window-04/prompt.txt: da0d8d6457fa1fbce13adcba737759938df8818321c4193db66c5f9b91fb91c8
        B/clauses/window-04/meta.json: 990e9b7ed2d39b9f8727d083f8e89163e5737521789bebc2ad5b9a83f0ebbc0d
        B/clauses/window-05/raw.json: 193c62cefc39f9091bcdaf068d748b648262d129b3afd3e81f239704ae4b9586
        B/clauses/window-05/prompt.txt: ea3fd9d7f7fb20d8dd631e3c5bcb2a4fdd787be601855a1b95abf93bd3697af8
        B/clauses/window-05/meta.json: bcc2bdabc8156c9a99552e703999aeb8383414c150738856ab9a451a70bd5632
        B/clauses/window-02/raw.json: bee721e224b7fe35b889478108c58b75ad36e042551dd39928948e74dc0b2ea9
        B/clauses/window-02/prompt.txt: 7693d7946f43c8e1ac90a7e027ce09f94a4b15f695b0c02d985405f8dcc17d48
        B/clauses/window-02/meta.json: 9388f50fba25c10548e529760913a6d27962a28e7ffd1effd29f7cda5a6c51ed
        B/clauses/window-07/raw.json: 1555ea411ac68ebd59f6dc8720e1964243ef372d0ae03ff172688b86b21a8e5d
        B/clauses/window-07/prompt.txt: 7b93ca81a9cb3a108129e780f485e3431cbcc79112a152707b1cdc4e9c00e0b5
        B/clauses/window-07/meta.json: c04e3de5359ce149865e545e5df15a36f8549ab801044491fb95b1ad30d0a278
        B/clauses/window-01/raw.json: 8cadeea0208b72d4067344da8662e0dd9e20b2bb6dab09de4f5b8e47d16acc0e
        B/clauses/window-01/prompt.txt: 4352fec59d1a47132404cb20c66c6be11666d6a1386af8bd6946cf575ae0b965
        B/clauses/window-01/meta.json: 1c26ff212d6411393023072a3c78147429c4f31882752dd112ff79a7112b5b95
        B/clauses/window-06/raw.json: 7ca75aa3e4c9140102259a02a483d19409e3e248a830b013c47a1b21c5214449
        B/clauses/window-06/prompt.txt: 3978980ad5a21e711aa9c00e7717ee048f492a9ec8c31a37aa5f241333234466
        B/clauses/window-06/meta.json: 8beb872cbe34bcd638bd11cb387a36dcb0f2eafdb67711d21da9e82803abedae
        B/tables/TABLE-4-page-10-6/raw.json: f1ffc31cf3e952c7c873ed8a5e9786835f7397dcd9f769a557bfc21ae52dde91
        B/tables/TABLE-4-page-10-6/prompt.txt: 0091caa6694e0bd20c564c65a1ae916557eab464a6785426613c0895e9e03c1b
        B/tables/TABLE-4-page-10-6/meta.json: 175ebf12c2695a20d5439305f3ff58c3376c35d18e1187cee0561522c2decb92
        B/tables/TABLE-2-page-8-4/raw.json: ed55ac2027c535b0bc9244b19abd78a1890106d97378340ae498eab3456f0353
        B/tables/TABLE-2-page-8-4/prompt.txt: 6977dfcd25fc37825b258df831a235d5cd53f1c4457d474fa7b73fdedb77812a
        B/tables/TABLE-2-page-8-4/meta.json: 28a4a7411d27756e166048d83859eb5e1f0fb51b6f4d10f99e3da537eb8615a7
        B/tables/TABLE-1-page-5-2/raw.json: a12b59832575c1d33ec82cf776e7d4e0e53c23f42b9ef503a08fac2a32c3501e
        B/tables/TABLE-1-page-5-2/prompt.txt: 51318dbc1b7b87ece95f08173e8f428067d62d1d4410584837b48338a82ca239
        B/tables/TABLE-1-page-5-2/meta.json: 3c66a897c09409405afc0189597cc43fd5d17937fb41a4b611119232091a2364
        B/tables/TABLE-S3-page-4-1/raw.json: 496e5602a80e2c2c2d34560a733e7a8964901a36e1ce5342edbc9f1a18822e7c
        B/tables/TABLE-S3-page-4-1/prompt.txt: 5d86ac289f610f72c2f4db306e9d39ed82fdc46bd1bfaf7d6f2bab516f56013e
        B/tables/TABLE-S3-page-4-1/meta.json: 004e19ccf447e5d3dc2f7530779af17f393760ed8c4c83fce0a4ba38ee9359c7
        B/tables/TABLE-3-page-9-5/raw.json: 9426a4848bf63582e472628fa75dbbeaba0a6236e8c9587ab0f04062083a7d08
        B/tables/TABLE-3-page-9-5/prompt.txt: 396be003ba82595252a76819918679bd180a4b1236388cf7609d07b686bc4941
        B/tables/TABLE-3-page-9-5/meta.json: 0711453c2991cf052efb2182119ad4d3b6ebd1f7f45d2bc70d2c1392e45eb6ce
        B/tables/TABLE-2-page-7-3/raw.json: cbb4b494c8dbcb165b731173663b6190bec056583d8f27a95e3bb450a08e8611
        B/tables/TABLE-2-page-7-3/prompt.txt: a04b1ce380aa38ffca19efdcbd01814c2db2247c182f62e59f2f93d022ab36d2
        B/tables/TABLE-2-page-7-3/meta.json: 47673c0467bfda0c72b0f03d4e68e8e71113767d3a0f355fbd2b272f3ac7d232
        B/tables/TABLE-5-page-12-8/raw.json: 32852e4bf13935fce7d7b7a6d1c470a63fc0961dc770673fad7763769e03dca8
        B/tables/TABLE-5-page-12-8/prompt.txt: 2c41eb07df15503c63753c930bc626805f2bcbd400b321117811a5d093e9a5a5
        B/tables/TABLE-5-page-12-8/meta.json: 7696fe0420565b6e884d61f003cd8b5887faea91fd41873454d11be1d1ecd5ef
        B/tables/TABLE-5-page-11-7/raw.json: bd4faad6ade219e5883b726ee11be6bb5eedc30954028a5f91f2bd481e61dc24
        B/tables/TABLE-5-page-11-7/prompt.txt: fa6c25c5fd410a260289bec65cb4466fb6465994d41b98d7862191b53a204466
        B/tables/TABLE-5-page-11-7/meta.json: 2171209056766b56ea02f1c3b42acc55187b73c2c07446d0b2d31b5a4c89b869
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
      pdf_sha256: fde5e768424dda3995a78864524c91a56e61002acc1f3fd76f7f9447c757774c
      source_review: _compare/relationships-2026-11-16/review-current/Godecke2021
      source_status_sha256: 2979899496e62f415db24a54bd923b051234705c109f812248b91bb6c55a8385
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R008
    exposure:
      text: high intensity therapy regimen
    outcome:
      text: time to first therapy
    analysis_label: Treatment Timing Analysis
    relation: association
    evidence_ids:
    - P5-S1-C14
    - P9-S2-C1
    qualifier_ids:
    - P5-S1-C14
    - P9-S2-C1
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: fde5e768424dda3995a78864524c91a56e61002acc1f3fd76f7f9447c757774c
      source_review: _compare/relationships-2026-11-16/review-current/Godecke2021
      source_status_sha256: 2979899496e62f415db24a54bd923b051234705c109f812248b91bb6c55a8385
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Accounting without a linked unit P5-S1-C14
      - Accounting without a linked unit P5-S2-C2
      - Accounting without a linked unit P5-S2-C3
      - Accounting without a linked unit P5-S2-C4
      - Accounting without a linked unit P5-S2-C5
      - Accounting without a linked unit P5-S2-C6
      - Accounting without a linked unit P6-S1-C1
      - Unaccounted source passage P5-S2-C6
      - Unaccounted source passage P5-S2-C2
      - Unaccounted source passage P5-S2-C3
      - Unaccounted source passage P6-S1-C1
      - Unaccounted source passage P5-S1-C14
      - Unaccounted source passage P5-S2-C4
      - Unaccounted source passage P5-S2-C5
      - Result passage disposed without unit P6-S1-C2
      - Accounting without a linked unit P6-S1-C3
      - Accounting without a linked unit P6-S1-C4
      - Accounting without a linked unit P8-S1-C1
      - Accounting without a linked unit P8-S1-C2
      - Accounting without a linked unit P8-S1-C3
      - Unaccounted source passage P8-S1-C2
      - Unaccounted source passage P8-S1-C3
      - Unaccounted source passage P6-S1-C3
      - Unaccounted source passage P6-S1-C4
      - Unaccounted source passage P8-S1-C1
      - Result passage disposed without unit P10-S1-C1
      - Result passage disposed without unit P10-S1-C10
      - Result passage disposed without unit P10-S1-C11
      - Result passage disposed without unit P10-S1-C12
      - Result passage disposed without unit P10-S1-C8
      - Accounting without a linked unit P10-S1-C9
      - Accounting without a linked unit P10-S2-C2
      - Unaccounted source passage P10-S1-C9
      - Unaccounted source passage P10-S2-C2
      - Result passage disposed without unit P12-S1-C11
      - Result passage disposed without unit P12-S2-C4
      - Result passage disposed without unit P13-S1-C4
      - Result passage disposed without unit P13-S1-C12
      - Result passage disposed without unit P13-S2-C1
      unattached_null_or_qualifier_ids:
      - P6-S1-C4
      - P8-S1-C2
      - P8-S1-C3
      - P10-S2-C2
      suppressed_nonrepresented_units: 4
      default_disposition_count_requires_completeness_check: 146
      unselected_timing_passages:
      - P2-S1-C4
      - P2-S1-C5
      - P3-S1-C9
      - P3-S2-C2
      - P5-S1-C7
      - P5-S1-C10
      - P5-S1-C12
      - P5-S1-C13
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P8-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      empty_frame_slots_require_confirmation:
      - imaging_provenance
      - imaging_timing
      - validation
      - analysis_restrictions
      - personal_factors
      - tested_personal_effects
      unclassified_extraction_ids:
      - P9-S1-C10
      table_review_required:
      - TABLE-1-page-5-2
      - TABLE-2-page-7-3
      - TABLE-2-page-8-4
      - TABLE-3-page-9-5
      - TABLE-4-page-10-6
      - TABLE-5-page-11-7
      - TABLE-5-page-12-8
      - TABLE-S3-page-4-1
      unlinked_tables:
      - TABLE-1-page-5-2
      - TABLE-4-page-10-6
      - TABLE-5-page-11-7
      - TABLE-5-page-12-8
      - TABLE-S3-page-4-1
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P5-S1
        - P6-S1
        - P8-S1
        - P13-S2
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: fde5e768424dda3995a78864524c91a56e61002acc1f3fd76f7f9447c757774c
      source_review: _compare/relationships-2026-11-16/review-current/Godecke2021
      source_status_sha256: 2979899496e62f415db24a54bd923b051234705c109f812248b91bb6c55a8385
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C4
      disposition: represented
      result_indexes:
      - 0
      - 5
      reason: Reports primary outcome result and safety result.
    - source_id: P2-S1-C7
      disposition: repeated
      result_indexes:
      - 0
      - 2
      reason: Restatement of findings for language impairment, QoL, and depression.
    - source_id: P2-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes therapy amount increase compared to pilot study.
    - source_id: P2-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Compares findings to AVERT trial.
    - source_id: P2-S3-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports results from a previous Phase I pilot study.
    - source_id: P2-S3-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports results from previous pilot and RATS-3 trial.
    - source_id: P3-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports results from a previous Phase II pilot trial.
    - source_id: P5-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes baseline characteristics balance.
    - source_id: P5-S1-C14
      disposition: represented
      result_indexes:
      - 7
      reason: Reports difference in treatment start date.
    - source_id: P5-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes therapy sessions completed.
    - source_id: P5-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes therapy hours in UC group.
    - source_id: P5-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports number of UC participants receiving no therapy.
    - source_id: P5-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports video recording rates for UC.
    - source_id: P6-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes additional therapy hours received after week 12.
    - source_id: P6-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes limited additional therapy after week 12.
    - source_id: P6-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports protocol compliance rate.
    - source_id: P6-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes reasons for non-completion of intervention.
    - source_id: P8-S1-C1
      disposition: represented
      result_indexes:
      - 1
      reason: Reports unadjusted mean %MPR at 12 weeks.
    - source_id: P8-S1-C2
      disposition: represented
      result_indexes:
      - 0
      reason: Reports adjusted primary outcome results.
    - source_id: P8-S1-C3
      disposition: represented
      result_indexes:
      - 2
      - 3
      - 5
      - 6
      reason: Reports secondary outcomes, safety, and subgroup %MPR.
    - source_id: P9-S1-C3
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of primary outcome result.
    - source_id: P9-S1-C4
      disposition: repeated
      result_indexes:
      - 0
      - 2
      reason: Restatement of lack of benefit for language, QoL, and depression.
    - source_id: P9-S1-C5
      disposition: repeated
      result_indexes:
      - 5
      reason: Restatement of safety result.
    - source_id: P9-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about clinically meaningful gains.
    - source_id: P9-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes increase in UC therapy amount compared to pilot.
    - source_id: P9-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes UC service delivery characteristics.
    - source_id: P10-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Restatement of UC service delivery.
    - source_id: P10-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports video recording rates for UC.
    - source_id: P10-S1-C8
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of diminishing returns from additional therapy.
    - source_id: P10-S1-C9
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of small difference in %MPR.
    - source_id: P10-S1-C10
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of small difference in %MPR.
    - source_id: P10-S1-C11
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of lack of clinical relevance.
    - source_id: P10-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes within-group differences.
    - source_id: P10-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement on clinical progress of participants.
    - source_id: P10-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Compares findings to prior research on predicted recovery.
    - source_id: P10-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Compares findings to chronic aphasia interventions.
    - source_id: P12-S1-C9
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement that UC may be sufficient.
    - source_id: P12-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Speculates on efficacy of much higher doses.
    - source_id: P12-S2-C1
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of lack of significant benefit.
    - source_id: P12-S2-C4
      disposition: repeated
      result_indexes:
      - 0
      - 3
      reason: Restatement of no benefit at 12 and 26 weeks.
    - source_id: P13-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement on clinically meaningful change in UC.
    - source_id: P13-S1-C12
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement that results do not support increasing intensity.
    - source_id: P13-S2-C1
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement that results do not support increasing intensity.
    - source_id: P11-S1-C2
      disposition: represented
      result_indexes:
      - 0
      - 1
      - 2
      - 3
      reason: Table 5 contains primary and secondary outcomes for 12 and 26 weeks.
    - source_id: P12-S2-C6
      disposition: represented
      result_indexes:
      - 3
      reason: Table 5 continued contains 26-week secondary outcomes.
    - source_id: P9-S2-C1
      disposition: represented
      result_indexes:
      - 7
      reason: Table 3 reports time to first therapy difference.
    unresolved_coverage:
    - source_id: P11-S1-C2
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P12-S2-C6
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P9-S2-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    pending_source_ids:
    - P2-S1-C7
    - P2-S1-C8
    - P2-S1-C9
    - P2-S3-C3
    - P2-S3-C5
    - P3-S1-C2
    - P5-S1-C11
    - P5-S2-C2
    - P5-S2-C3
    - P5-S2-C4
    - P5-S2-C5
    - P6-S1-C1
    - P6-S1-C2
    - P6-S1-C3
    - P6-S1-C4
    - P9-S1-C3
    - P9-S1-C4
    - P9-S1-C5
    - P9-S1-C6
    - P9-S1-C8
    - P9-S1-C9
    - P10-S1-C1
    - P10-S1-C5
    - P10-S1-C8
    - P10-S1-C9
    - P10-S1-C10
    - P10-S1-C11
    - P10-S1-C12
    - P10-S2-C2
    - P10-S2-C3
    - P10-S2-C4
    - P12-S1-C9
    - P12-S1-C11
    - P12-S2-C1
    - P12-S2-C4
    - P13-S1-C4
    - P13-S1-C12
    - P13-S2-C1
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-5-2
    - TABLE-2-page-7-3
    - TABLE-2-page-8-4
    - TABLE-3-page-9-5
    - TABLE-4-page-10-6
    - TABLE-5-page-11-7
    - TABLE-5-page-12-8
    - TABLE-S3-page-4-1
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P5-S1-C10
      recruited_sample:
      - P1-S1-C4
      - P5-S1-C7
      eligibility:
      - P3-S2-C2
      - P3-S2-C3
      - P3-S2-C4
      - P3-S2-C5
      imaging_provenance: []
      imaging_timing: []
      outcome_timing:
      - P1-S1-C4
      - P3-S1-C7
      - P4-S2-C7
      - P8-S1-C1
      - P8-S1-C2
      - P8-S1-C3
      - P11-S1-C1
      - P11-S1-C2
      outcome_definition:
      - P1-S1-C4
      - P3-S1-C3
      - P4-S2-C4
      - P4-S2-C7
      validation: []
      analysis_restrictions: []
      dependent_variable_statement:
      - P4-S3-C2
      limitations:
      - P10-S1-C3
      - P10-S1-C4
      - P13-S1-C9
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P4-S3-C2
      - P8-S1-C2
      - P12-S2-C8
      explicitly_not_adjusted:
      - P5-S1-C3
      descriptive_personal_factors:
      - P7-S1-C2
      - P8-S2-C1
    outcome_type: both_reported
    imaging_vs_outcome: not_stated
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P8-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S1-C2
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
      pdf_sha256: fde5e768424dda3995a78864524c91a56e61002acc1f3fd76f7f9447c757774c
      review_sha256: 8bb819a9db33b698a7927d185024bd7f9ce3b010e9bdb39ff8eab174004b925b
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
      source_result: The high intensity therapy groups (UC-Plus and VERSE combined)
        received treatment two days earlier than the usual care group (p = 0.008).
      result_status: detected
      patient_measurement: non_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The source P5-S1-C14 explicitly reports the comparison of therapy
            commencement timing between high intensity and usual care groups, matching
            the proposed analysis label and exposure/outcome structure.
          source_ids:
          - P5-S1-C14
        direction:
          answer: fits
          reason: The source states high intensity groups received treatment 'two
            days earlier' than UC, which aligns with the proposed claim of earlier
            timing. The direction is consistent.
          source_ids:
          - P5-S1-C14
        construct:
          answer: fits
          reason: The exposure is correctly identified as the high intensity regimen
            (UC-Plus/VERSE) and the outcome as time to first therapy. The measurement
            is a clinical timing metric (days), not an imaging or functional outcome
            measure.
          source_ids:
          - P5-S1-C14
          - P4-S1-C4
        qualifications:
          answer: fits
          reason: The proposed qualifications correctly note that the high intensity
            group is a combination of UC-Plus and VERSE, and that usual care was uncontrolled,
            which are accurate reflections of the trial design described in the source.
          source_ids:
          - P5-S1-C14
          - P4-S1-C2
        missing_material_caveat:
          answer: fits
          reason: The draft correctly identifies that this is a difference in delivery
            timing rather than a clinical outcome. No material caveats regarding the
            statistical significance or the nature of the comparison are omitted.
          source_ids:
          - P5-S1-C14
      optional_pending:
      - Sample size requires source confirmation; it has not been transcribed.
      - 'sample.population: source confirmation required; original proposed wording
        remains in the audit.'
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Sample size requires source confirmation; it has not been transcribed.
    - 'sample.population: source confirmation required; original proposed wording
      remains in the audit.'
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Sample size requires source confirmation; it has not been transcribed.
    - 'sample.population: source confirmation required; original proposed wording
      remains in the audit.'
    normalizations:
    - field: sample.n
      original: 245
      action: not_transcribed
      reason: Not supported by selected quotations
    - field: sample.population
      original: Adults with acute stroke and resultant acute aphasia (mild to severe)
        recruited within 14 days of stroke onset
      action: not_transcribed
      reason: 'Numbers not grounded in usable selected source readings: 14'
    analysis_identity:
      id: R008
      exposure:
        text: high intensity therapy regimen
      outcome:
        text: time to first therapy
      analysis_label: Treatment Timing Analysis
      relation: association
      evidence_ids:
      - P5-S1-C14
      - P9-S2-C1
      qualifier_ids:
      - P5-S1-C14
      - P9-S2-C1
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: fde5e768424dda3995a78864524c91a56e61002acc1f3fd76f7f9447c757774c
        source_review: _compare/relationships-2026-11-16/review-current/Godecke2021
        source_status_sha256: 2979899496e62f415db24a54bd923b051234705c109f812248b91bb6c55a8385
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P5-S1-C14:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: fde5e768424dda3995a78864524c91a56e61002acc1f3fd76f7f9447c757774c
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: f22946556b5c8f6c8033071ed326624e89c8b2810eb7872c0927bcf2655ad01b
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P5-S1-C14
          page: 5
          text_layer_sha256: f22946556b5c8f6c8033071ed326624e89c8b2810eb7872c0927bcf2655ad01b
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: 'As intended, the

          high intensity groups received treatment two days ear-

          lier than those receiving UC (p ¼ 0.008).'
        anchor_text: 'As intended, the

          high intensity groups received treatment two days ear-

          lier than those receiving UC (p ¼ 0.008).'
        excluded_fragments: []
        image_sha256: c627a94cbd1b6e4ec3df0439b1e0c635c4545c2efd583b348da5a7b77e1ce29d
      P3-S2-C2:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: fde5e768424dda3995a78864524c91a56e61002acc1f3fd76f7f9447c757774c
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: dceeeba6b8265d4e158f2444236484cf27058f0afbabc4eae7c9702bbf79aed0
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S2-C2
          page: 3
          text_layer_sha256: dceeeba6b8265d4e158f2444236484cf27058f0afbabc4eae7c9702bbf79aed0
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: 'Eligibility criteria

          Participants were aged over 18 years and admitted to

          hospital with an acute stroke, resultant acute aphasia of

          any type, within 14 days of stroke onset.'
        anchor_text: 'Eligibility criteria

          Participants were aged over 18 years and admitted to

          hospital with an acute stroke, resultant acute aphasia of

          any type, within 14 days of stroke onset.'
        excluded_fragments: []
      P5-S1-C9:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: fde5e768424dda3995a78864524c91a56e61002acc1f3fd76f7f9447c757774c
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: b9e58dd87f5b48c2f1309124ea788b8045ebf1fe8c40391d15e4769353fef9e2
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P5-S1-C9
          page: 5
          text_layer_sha256: b9e58dd87f5b48c2f1309124ea788b8045ebf1fe8c40391d15e4769353fef9e2
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: 'One

          randomized participant withdrew consent; their data

          were withdrawn from analysis (N ¼ 245).'
        anchor_text: 'One

          randomized participant withdrew consent; their data

          were withdrawn from analysis (N ¼ 245).'
        excluded_fragments: []
        image_sha256: 35a10b05710c876f98992d59b4bcf9a733e9b9c7b00fcbf873162c3848fcc85e
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 5
  quote: 'As intended, the

    high intensity groups received treatment two days ear-

    lier than those receiving UC (p ¼ 0.008).'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-24'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
