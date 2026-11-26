---
id: right_smg_slf_damage
name: right supramarginal gyrus and SLF damage
kind: network
findings:
- id: f1
  target: covf0
  target_kind: impairment
  claim: Durfee2021 reports, based on Patel et al. (2018), that percent damage to the right supramarginal gyrus and SLF were independent predictors of the coefficient of variation in fundamental frequency (CoVF0).
  direction: likely
  relationship: synthesis
  method: narrative_review
  sample:
    n: not_reported
    population: 'Participants in the studies summarized by Durfee2021; this record is a secondary review report, not a newly recruited cohort. Primary source: Patel et al. (2018).'
    phase: not_reported
    time_post_onset: Varies across reviewed studies; see cited primary study and source passages.
  statistics:
    threshold: not_applicable_review_synthesis
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - finding is part of a systematic review of 11 articles
  evidence_quality: narrative-review
  strength: weak
  notes: 'Reclassified as a secondary review report, explicitly attributing the result to Patel et al. (2018). This is not a new primary sample or independent replication; quantitative estimates and study-level attribution require human verification against the primary publication. Source repair (unapproved): Reclassified as a secondary review report, explicitly attributing the result to Patel et al. (2018). This is not a new primary sample or independent replication; quantitative estimates and study-level attribution require human verification against the primary publication.'
  imaging_details:
    reference_space: not_applicable
    atlases_used: []
  lesion_mapping: {}
  provenance:
    extracted_by: agent:source-repair
    extracted_on: '2026-11-23'
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
    - proposed_concept:covf0
    - agent_source_repair_pending_human_review
  citation: '@Durfee2021'
  source_passages:
  - section: Original source P8-S1-C2
    page: 8
    quote: "Independent predictors of CoVF0 included age \nand percent damage to right supramarginal gyrus and SLF."
    supports: claim
  - section: Original source P4-S2-C5
    page: 4
    quote: "Time post-stroke and brain imaging considerations \nResults are divided into studies of patients with acute stroke (<1 \nweek) versus those with subacute (1 week–3 months) or chronic (>3 \nmonths) because different approaches to brain imaging and mapping are \nneeded depending on the time post-onset at which patients are studied."
    supports: sample
  - section: Original source P4-S2-C7
    page: 4
    quote: "Acute lesion-deficit association studies use either follow-up head \ncomputed tomography (CT) or diffusion-weighted imaging (DWI; \nrevealing the infarct within minutes of onset) with or without perfusion- \nweighted imaging (PWI; revealing hypoperfused, dysfunctional tissue \nsurrounding the infarct)."
    supports: method
  design: systematic-review
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-23'
relationship_review:
  paper: Durfee2021
  proposal_id: R015
  approved: false
  original_core_review:
    paper: Durfee2021
    proposal_id: R015
    review_status_sha256: 3c3e749bbeb85252e97e4dec8e8dbb5075c4d0e2ddb45ff086cbc832ee2697ee
    review_binding:
      version: candidate-inventory-v1
      input_hashes:
        pdf: ccd84f115f464675d9dc92bc5df1deabc67b02a9eb42f72849745a981dc374d8
      original_review_binding:
        version: relationship-review-v4
        input_hashes:
          pdf: ccd84f115f464675d9dc92bc5df1deabc67b02a9eb42f72849745a981dc374d8
          A/passages.json: 9940d5cdf1b01ec683c0cc01265a41a196bd09af1ae5492eb65075cdddf7a34e
          A/raw.json: 1da4f1ca288ba7288e76b418189710efb50191ad1bb69b72212d109a6a9ba45b
          A/source-units.json: 6368a5d4fe40ace5037d754cfd4f455ffda3cab1111c5f7d3bfc30dae13dd5bf
          A/full-source-units.json: 4b35e89efe1e861bb33369cd36aba3074af33699bd0ded2728a90993d5c1d8a1
          A/meta.json: 71a47fc491423b49aa2c36e68d4a48e10cdcbd0e0e5ea343290c8207c5cb907b
          A/table-images/page-11.png: b77d1ccb0718256caa489f4956bcbb3b23fdb2d8bbeb10a59aa550650208d04f
          A/table-images/TABLE-5-page-8-1.png: ac6c4c63816de9780c9c961a1489dd4393ed7ec02a788e377c3f27751c86b881
          A/table-images/page-6.png: 3d534538a361d492318181ae3cfc24a1d971c97cd5a8d94df9a89bb385ee41e0
          A/table-images/page-7.png: e7c643e9a648be4d90f9f2ebea0f4aba54974b621dc415d5ba48123b2de9ae8b
          A/table-images/page-5.png: 88b5365c9a983b3474247a5035e35d7a0f7c00a753d2ab0f2ab29a6adc4709d2
          A/table-images/page-4.png: 40a0d144166d26aeba70303eedcc23a9f7d702185221aab632ca4a64170bffa9
          A/table-images/TABLE-1-page-4-1.png: 155ef3a5432cbeff517d5df085e73230cb6bee1fd573f8849813270c2acaf58f
          A/table-images/TABLE-4-page-6-1.png: b6ed4a220def952a83a8452f7523885d959bb2d7abe8b30247d27a37e4edf123
          A/table-images/page-8.png: 92530218370780a2ec0ba616287f24a720302fbb0c51e72ec52def044b0ee0bb
          A/table-images/TABLE-6-page-11-1.png: 61de752fe80af2e298e86f2d03285bb4ccdeaecdbe37aaec0da6fa7d92a7461f
          A/table-images/TABLE-2-page-4-2.png: e785915270f8d16b1b07dfdad681f6b89836429dc238d0cf35755c0b233871f1
          A/table-images/manifest.json: 2282b3d7df7aaae6d286f080161519d5c6e315dca67c6581aa571168de252e9c
          A/table-images/TABLE-6-page-11-2.png: 2ab3cd9eb8c46ee4854f5b77d1cd5e3b702effaa398136f944fa75fecffe5aa3
          A/table-images/TABLE-3-page-5-1.png: 0ce70e7875b1dbfe64e1f1f2fdffc04232db59119cf000b69bee06431d275c11
          A/table-images/TABLE-5-page-7-1.png: 6bee08da6c58d5591a46fce1952cba96ca584cc62cf9c09859f7257384fb1ad7
          A/clauses/window-11/raw.json: d207e08b679ecb8944273048640f452555dc529810edc82d96a04fea37755092
          A/clauses/window-11/prompt.txt: 8e499193a44781032843e1617f80878f4262fca7bdd14906bca22dd3047f0863
          A/clauses/window-11/meta.json: c2d588a4c92972af3575b3925d3b6e02334f199efb69d93415e7ab66e4b9be63
          A/clauses/window-10/raw.json: c2ce714b32355c0bb3cfdcc7e5c9688a1cd1081fd92cf8215a3297e9aeef16ad
          A/clauses/window-10/prompt.txt: 0e0b288d869131c3d64b6e09301f193a05e8c2cbd4d650d4fae2c5294975d034
          A/clauses/window-10/meta.json: 4131d46e96048491648263fd482db19b386c1d9921a0001f1a0c45a52ccff7f8
          A/clauses/window-03/raw.json: d3395a8f28b16b23a280df0cb86731d2a447adb26a56c6b392e592063c777a1c
          A/clauses/window-03/prompt.txt: 0afe2a35b6fa3545fc338d65d91b63e16c67f63a96acdcf8264fb1e4c2cface7
          A/clauses/window-03/meta.json: a5e1ec6cbf27fe69578f80a1351646f07478acb1575a72bf11e4eea2230d7759
          A/clauses/window-04/raw.json: 608530d70b45925642f06b59b10142634935a36d6425a6c59c89945c5f6a0282
          A/clauses/window-04/prompt.txt: e3894beb1dd39d87550ed62292f079a4deef9cbda463176897bce2b0aed70fd2
          A/clauses/window-04/meta.json: 5418fa330f12bf4683fdf55d42731e91ca69d1160faff7596c994ce2654add28
          A/clauses/window-05/raw.json: 8fc728e3712f7b0dd9424f75f1a8a4489b82a493927eb19e405f42c6e1ef5410
          A/clauses/window-05/prompt.txt: 9d42250cd8bd5e4e3bd3c16a6766461c3d45aa9cebe9faedbfc8f4211b00b604
          A/clauses/window-05/meta.json: 8f1a269836be5d730ffd0530fcca0a2fc1e1ded9ad207f722205e792ebeb29d4
          A/clauses/window-02/raw.json: 1d34bb9ad619f0087b8d980c3511c6dc81bd74808b580b6801d932f5f877cff8
          A/clauses/window-02/prompt.txt: 44e2e215d40fe86f74395a9c0e732f9031955040e83f1298830a89949609207d
          A/clauses/window-02/meta.json: c33dc41c3d84a8fac39d9a41177c7a785237c5696d1de3e1d5538e2daef40596
          A/clauses/window-12/raw.json: 882da49aca5959baa9bf73ccb64e31bcc15786db8c7886ecd23145a509b50f8e
          A/clauses/window-12/prompt.txt: 59304e2db4ebff2421d5bbec13233209ad4c2f00ae21c02863f505d7189a9e14
          A/clauses/window-12/meta.json: 4f17b25da9d8536ef2cc39be34ca80de06f3884096e83309ab3a1f26e1a8ed71
          A/clauses/window-09/raw.json: eb7b5df01ead7f6808c31b2c6be86af12182401366e26dcc23321e7caf346f4b
          A/clauses/window-09/prompt.txt: 1005da75d8394954fd60bf002e5bebfa63f98b3e453c7cfc2f902e50ff8a698d
          A/clauses/window-09/meta.json: 8378417bf603b06f1ea931d2d8b5feb2853b3eb2e35a7ff1c83a1e168e7933bb
          A/clauses/window-07/raw.json: cc73beeadc8d7cce39801b88d36314c693ae8b48c2002547c0f567c963a85d1b
          A/clauses/window-07/prompt.txt: 49134434f878a1013fc09269768c615200c29eb3a6037159441877ec42449394
          A/clauses/window-07/meta.json: 1c2ae55da975b253427468f1f9f036ac62230b1295c392adc148855233fce4e4
          A/clauses/window-01/raw.json: a08e1173d89929e6aeb74a080741a3a65a71665bc904797261a8d443727c5795
          A/clauses/window-01/prompt.txt: efd7329fb8dfd2d24b4ef906188f9d85221525b59bbc490b369197c007ca81e9
          A/clauses/window-01/meta.json: 33f83c44fcdeac820e8c1bc29d443f82222370d16413483fdae65da44f79f93b
          A/clauses/window-06/raw.json: aae81b5136ead07d41a726dca63198b1e17d334c2a33b0fa862f509e756e96a3
          A/clauses/window-06/prompt.txt: d716dcb0ac39b255238db75160af8dfbb954f169e3b8d4db1d32ca3f8150c78f
          A/clauses/window-06/meta.json: 8317d89042fe14c2d735f7e55f44f89a042319e781e0f6f6487154dcd724aa7b
          A/clauses/window-08/raw.json: dbfe9dc303458bfb18ee01ada58952e896b5c006ea9c2b6d0a47b43c808e057f
          A/clauses/window-08/prompt.txt: 3d2ee0f34140f2737ede91bd3ea748f065ebf8a09f2bd1926af03acdc6013d40
          A/clauses/window-08/meta.json: 256efa8c397465c544e9bf4744bce482bc4c21306caa3cca8964e38a17d44fec
          A/tables/TABLE-4-page-6-4/raw.json: c7119b44d61121965f0764ee146117e5156139ffc64166c6f06979de85188568
          A/tables/TABLE-4-page-6-4/prompt.txt: 257b25324e41a8dce84bc1e7514933367d098f36c4f5aae446180727096aa490
          A/tables/TABLE-4-page-6-4/meta.json: e785dae97371842f8f9390f939524012a3cd415f679b6c921fa35343ea360adf
          A/tables/TABLE-3-page-5-3/raw.json: d7c8a7277d4eb099afa999bd9cc1f4aa88e1a580433fb6272487c1a5aae88cbd
          A/tables/TABLE-3-page-5-3/prompt.txt: 51e8ff831667e9b99dd0e7d3b546f6b4c618187c3ce0be32f9f007bdeba8c5e5
          A/tables/TABLE-3-page-5-3/meta.json: 843778231a2476c9e0519b2c2a39a0f4dfba00be58885a445ebb2bdcbe428ec8
          A/tables/TABLE-6-page-11-8/raw.json: 519c8108f829be68590cd2273bebff757a5b1bac35336147e6516cd850143446
          A/tables/TABLE-6-page-11-8/prompt.txt: 46e31bcd871935e1c91bbf8b6d8253ca5f8478a2e0123a964bd976de7094b5d9
          A/tables/TABLE-6-page-11-8/meta.json: c5e0981e795c223d0b38126a82f85f39184c91886d0526db3efa1274b604f4a1
          A/tables/TABLE-6-page-11-7/raw.json: 5423f4a64647b0897ec4b839eab6767fcc1f2680e4d167ec4ccd657d656d0a92
          A/tables/TABLE-6-page-11-7/prompt.txt: b12906cd7835b45e8502b8f6f94d9df8e909e0901c36978ae3722a85aca6c50f
          A/tables/TABLE-6-page-11-7/meta.json: ab28ffc5ea49d0101b6eaad3d5917924efcb6814ef32d511f08f5d611207f793
          A/tables/TABLE-5-page-8-6/raw.json: b9bb31c781d35ebf35ff49be09a7874073636db72bc6fa066b76e37664fe5f01
          A/tables/TABLE-5-page-8-6/prompt.txt: 79683064f99b6c1b8a6d229f945ac23a0b2bae6c2ecaf5b0c3d4438b2a84d946
          A/tables/TABLE-5-page-8-6/meta.json: 9c401e562462a1638616479bea4be0cd93e978186cfdf9bb0602bee4883105ad
          A/tables/TABLE-1-page-4-1/raw.json: 871725b345fdc526d5cab8ddc511b943efd40803c951d261c40ffb63d4258072
          A/tables/TABLE-1-page-4-1/prompt.txt: ac7936ebb3deacf60fed55bdfd28b4fe69bb13cf11de5afcd8ba08ac43b73b9d
          A/tables/TABLE-1-page-4-1/meta.json: 6f9f78b3191164c36dc7c07971249aea776b3d7a165ff268d767c91755ac4712
          A/tables/TABLE-5-page-7-5/raw.json: 4a40adb15409f6393c79c6ad525ad1c2a7f0a669675d98066e31954d7e066035
          A/tables/TABLE-5-page-7-5/prompt.txt: 364563fb118a545dfbf2a526ab6eecb0924e42e513541279ccaae9e4228159e2
          A/tables/TABLE-5-page-7-5/meta.json: 9c815000a778bb4a4b313f4942425f43ed2d8892415cf1c994b145252ba75d85
          A/tables/TABLE-2-page-4-2/raw.json: f3a127297ee15846b718e5dba3de7b180bfeec0ea8f113d760e631e677b917c6
          A/tables/TABLE-2-page-4-2/prompt.txt: ab9282e57a288b60895ce547e088b832c3a2a917be04e3eb80eb290f6b91abf6
          A/tables/TABLE-2-page-4-2/meta.json: a1929a3982d53d5737207478483aad6bc3631de9f77dd8ef8706e7fe4fa56a67
          B/passages.json: 9940d5cdf1b01ec683c0cc01265a41a196bd09af1ae5492eb65075cdddf7a34e
          B/raw.json: 10bd35cccf75e442f72761af929550af7a29b9a8d175ec5d309942825e8fbf02
          B/source-units.json: 6368a5d4fe40ace5037d754cfd4f455ffda3cab1111c5f7d3bfc30dae13dd5bf
          B/full-source-units.json: 4b35e89efe1e861bb33369cd36aba3074af33699bd0ded2728a90993d5c1d8a1
          B/meta.json: 364d53699a1161c323f7d7dcdafca5c49fbdf3ee073f0b5ffd8ce0c02f3479f8
          B/table-images/page-11.png: b77d1ccb0718256caa489f4956bcbb3b23fdb2d8bbeb10a59aa550650208d04f
          B/table-images/TABLE-5-page-8-1.png: ac6c4c63816de9780c9c961a1489dd4393ed7ec02a788e377c3f27751c86b881
          B/table-images/page-6.png: 3d534538a361d492318181ae3cfc24a1d971c97cd5a8d94df9a89bb385ee41e0
          B/table-images/page-7.png: e7c643e9a648be4d90f9f2ebea0f4aba54974b621dc415d5ba48123b2de9ae8b
          B/table-images/page-5.png: 88b5365c9a983b3474247a5035e35d7a0f7c00a753d2ab0f2ab29a6adc4709d2
          B/table-images/page-4.png: 40a0d144166d26aeba70303eedcc23a9f7d702185221aab632ca4a64170bffa9
          B/table-images/TABLE-1-page-4-1.png: 155ef3a5432cbeff517d5df085e73230cb6bee1fd573f8849813270c2acaf58f
          B/table-images/TABLE-4-page-6-1.png: b6ed4a220def952a83a8452f7523885d959bb2d7abe8b30247d27a37e4edf123
          B/table-images/page-8.png: 92530218370780a2ec0ba616287f24a720302fbb0c51e72ec52def044b0ee0bb
          B/table-images/TABLE-6-page-11-1.png: 61de752fe80af2e298e86f2d03285bb4ccdeaecdbe37aaec0da6fa7d92a7461f
          B/table-images/TABLE-2-page-4-2.png: e785915270f8d16b1b07dfdad681f6b89836429dc238d0cf35755c0b233871f1
          B/table-images/manifest.json: fc7f7911335d23fd667572a4e1466989e3e49a2579c727a25b1089481efddbab
          B/table-images/TABLE-6-page-11-2.png: 2ab3cd9eb8c46ee4854f5b77d1cd5e3b702effaa398136f944fa75fecffe5aa3
          B/table-images/TABLE-3-page-5-1.png: 0ce70e7875b1dbfe64e1f1f2fdffc04232db59119cf000b69bee06431d275c11
          B/table-images/TABLE-5-page-7-1.png: 6bee08da6c58d5591a46fce1952cba96ca584cc62cf9c09859f7257384fb1ad7
          B/clauses/window-11/raw.json: a082ee8380eff54e1169e3dd025aaf499a3446bfc3394f82f1d6325759677ae9
          B/clauses/window-11/prompt.txt: 8e499193a44781032843e1617f80878f4262fca7bdd14906bca22dd3047f0863
          B/clauses/window-11/meta.json: d91571bb76b84a8aa35ef133afc4ca29ef6a14929ea53e7724f99012d883d1f8
          B/clauses/window-10/raw.json: 69e27ba49770e579688f133b0b49189690627fc53e6fa5aa6819af101f61f504
          B/clauses/window-10/prompt.txt: 0e0b288d869131c3d64b6e09301f193a05e8c2cbd4d650d4fae2c5294975d034
          B/clauses/window-10/meta.json: 0b3d6dbc0891237ca685f6e55716651cc04c211f69909055d76754ca8715e38a
          B/clauses/window-03/raw.json: 025e6cf60f13ed1398e585d7626e7f25429184b6d3c34b84c5fb97ce75cb0ae4
          B/clauses/window-03/prompt.txt: 0afe2a35b6fa3545fc338d65d91b63e16c67f63a96acdcf8264fb1e4c2cface7
          B/clauses/window-03/meta.json: cdcdccbc17671f507220c3f9a6612251bc137bf22f94d9970a5751d160d67080
          B/clauses/window-04/raw.json: a261c44c6fbac09d29876bd7c72d519138e86785029d8866b23c63865c86c93c
          B/clauses/window-04/prompt.txt: e3894beb1dd39d87550ed62292f079a4deef9cbda463176897bce2b0aed70fd2
          B/clauses/window-04/meta.json: 625b94a078a88802c60750311d350c0b83ab5a784b621049a8557ea6f1352c9b
          B/clauses/window-05/raw.json: df4181b7c203d660387bb2b4ab5e74246204ebdb8806bbc3779e5effb59776bd
          B/clauses/window-05/prompt.txt: 9d42250cd8bd5e4e3bd3c16a6766461c3d45aa9cebe9faedbfc8f4211b00b604
          B/clauses/window-05/meta.json: de8cbd5beac9af9ce45424ae41eb945286d10f73376dc606011af84afa1ea782
          B/clauses/window-02/raw.json: 721d847ff1e70c8359195bce1b2b9c195ac676b34f8cbb2bbe1f971e64832958
          B/clauses/window-02/prompt.txt: 44e2e215d40fe86f74395a9c0e732f9031955040e83f1298830a89949609207d
          B/clauses/window-02/meta.json: 79e11c504ecc572b8efedf111c9ef93cf18ee6f5dadd34d44bf395050a435017
          B/clauses/window-12/raw.json: eed250e048e13e65f8d524fa6b4803275970119b03eb134bd91a626581ad3ba1
          B/clauses/window-12/prompt.txt: 59304e2db4ebff2421d5bbec13233209ad4c2f00ae21c02863f505d7189a9e14
          B/clauses/window-12/meta.json: 665f0a853a326947fd73ab4e1c3aeb8f3f6ed35df888c74cbf8abd475ff1b281
          B/clauses/window-09/raw.json: 911ba497160df3de628583cfc915f553631d2db9b0f5568723f1df5f643f8f60
          B/clauses/window-09/prompt.txt: 1005da75d8394954fd60bf002e5bebfa63f98b3e453c7cfc2f902e50ff8a698d
          B/clauses/window-09/meta.json: 72716cc83756caf225adfa21b37977e3f3f5dfa2bc6c5264aa273b39d4fdaeff
          B/clauses/window-07/raw.json: 58df4da7fec737b12e80d2266198913558155b62c3be8a5dab18112dc5c2eab1
          B/clauses/window-07/prompt.txt: 49134434f878a1013fc09269768c615200c29eb3a6037159441877ec42449394
          B/clauses/window-07/meta.json: 23bc48e7b525afb0326520268dd4a0e4c8d9381a5ceda40016cb8fe11a570640
          B/clauses/window-01/raw.json: e350d88569dc5cd09575444c722fb506a60083ad5b300556bf939ca4892fe72a
          B/clauses/window-01/prompt.txt: efd7329fb8dfd2d24b4ef906188f9d85221525b59bbc490b369197c007ca81e9
          B/clauses/window-01/meta.json: fbcc58e12442501b21e7fc72c7175af72fda7d4fe1ba5adc4fd9e5e97cec92d4
          B/clauses/window-06/raw.json: 00323113876c10d4d550a94b11f563cdb61c165aed985173686517eda61fb984
          B/clauses/window-06/prompt.txt: d716dcb0ac39b255238db75160af8dfbb954f169e3b8d4db1d32ca3f8150c78f
          B/clauses/window-06/meta.json: 055ae02db4a4856e7a9ba5ac317a837a1d5c12874cbf1070e9b954d11cbb6462
          B/clauses/window-08/raw.json: fe5ff08992ef9b574f6f67610a22a1704434c816aeacbc38e0b499d301080010
          B/clauses/window-08/prompt.txt: 3d2ee0f34140f2737ede91bd3ea748f065ebf8a09f2bd1926af03acdc6013d40
          B/clauses/window-08/meta.json: 411808dbf5cd583c4db8fdc4df2e5d70d58d1a5840ab1aa69b8669532c0bb69e
          B/tables/TABLE-4-page-6-4/raw.json: 6a77564f47c790d420a48a9f884ba08922323d06244a48e990736cc9046f9caf
          B/tables/TABLE-4-page-6-4/prompt.txt: 257b25324e41a8dce84bc1e7514933367d098f36c4f5aae446180727096aa490
          B/tables/TABLE-4-page-6-4/meta.json: 0bfb7675b8b4cc7d79b0b59b2b4d604502cf9b37e571bb4ed350b29102e6f5e6
          B/tables/TABLE-3-page-5-3/raw.json: 3107c8bded705d3ca755daa1562ef668eec5280cd4f72553a046907104243efa
          B/tables/TABLE-3-page-5-3/prompt.txt: 51e8ff831667e9b99dd0e7d3b546f6b4c618187c3ce0be32f9f007bdeba8c5e5
          B/tables/TABLE-3-page-5-3/meta.json: cebf48bd51df275590a4441ff889b4ba8ba3b77de19cddb83e38a99f09e51d14
          B/tables/TABLE-6-page-11-8/raw.json: ad5dc5a51755b828fe979214e80babca0e106b1be9d290e07de56ffff98679af
          B/tables/TABLE-6-page-11-8/prompt.txt: 46e31bcd871935e1c91bbf8b6d8253ca5f8478a2e0123a964bd976de7094b5d9
          B/tables/TABLE-6-page-11-8/meta.json: e79f226af50a57202562b7cc2674ac1cf9a6dbfb02cd3d36855a39f40ca8fa08
          B/tables/TABLE-6-page-11-7/raw.json: 7c40215cb1f8c41e9393b8f2fb9137d90475c8b1e827193f2ef1d184c1b86c22
          B/tables/TABLE-6-page-11-7/prompt.txt: b12906cd7835b45e8502b8f6f94d9df8e909e0901c36978ae3722a85aca6c50f
          B/tables/TABLE-6-page-11-7/meta.json: a9840e85dc2c4481fe4ba9fd150a5bb719b13fbf12f64ff969d9ed59c9a99182
          B/tables/TABLE-5-page-8-6/raw.json: 088c364582929440df875c52b36aa300721901c2b3c382d4c2f69f23817da38e
          B/tables/TABLE-5-page-8-6/prompt.txt: 79683064f99b6c1b8a6d229f945ac23a0b2bae6c2ecaf5b0c3d4438b2a84d946
          B/tables/TABLE-5-page-8-6/meta.json: 552361af1b3fb77299ae8d82356a1ac6cc3b87487de559400258eaedd019391c
          B/tables/TABLE-1-page-4-1/raw.json: 9ae3517024478797d52552e1ea71919db757a8ddc9df450cf9fdecbc13e29e81
          B/tables/TABLE-1-page-4-1/prompt.txt: ac7936ebb3deacf60fed55bdfd28b4fe69bb13cf11de5afcd8ba08ac43b73b9d
          B/tables/TABLE-1-page-4-1/meta.json: 5acd643ccadf97935006a72d12dd5fe43c2d195f6dff986fba56a277580a67d9
          B/tables/TABLE-5-page-7-5/raw.json: ddc1f6b6828988d8b8f3e414c7d2f03d463534bcdc9f37ef1dc25a40ccdff813
          B/tables/TABLE-5-page-7-5/prompt.txt: 364563fb118a545dfbf2a526ab6eecb0924e42e513541279ccaae9e4228159e2
          B/tables/TABLE-5-page-7-5/meta.json: 7eb427ec8ea0b9940c6e1f07fb633986bb7679cd9d09f1f98b0632c537baedfb
          B/tables/TABLE-2-page-4-2/raw.json: b1fc74f95c4897f8aea2df7fb017ead34dd49e9b429f8ca833c694293d8c335d
          B/tables/TABLE-2-page-4-2/prompt.txt: ab9282e57a288b60895ce547e088b832c3a2a917be04e3eb80eb290f6b91abf6
          B/tables/TABLE-2-page-4-2/meta.json: f8657bdf5b944a0953e88fa793e4331c9307fe2f9ec9086e2a70f1237b1b1af9
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
        pdf_sha256: ccd84f115f464675d9dc92bc5df1deabc67b02a9eb42f72849745a981dc374d8
        source_review: _compare/relationships-2026-11-16/review-current/Durfee2021
        source_status_sha256: 3f761cdd0e697255bda542b600e23688e5810cf3517c0e413f6ea2cb3dcfa017
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
      packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
    proposal:
      id: R015
      exposure:
        text: right supramarginal gyrus and SLF damage
      outcome:
        text: coefficient of variation in fundamental frequency (CoVF0)
      analysis_label: Acute lesion analysis (Patel et al., 2018)
      relation: association
      evidence_ids:
      - P8-S1-C2
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
        pdf_sha256: ccd84f115f464675d9dc92bc5df1deabc67b02a9eb42f72849745a981dc374d8
        source_review: _compare/relationships-2026-11-16/review-current/Durfee2021
        source_status_sha256: 3f761cdd0e697255bda542b600e23688e5810cf3517c0e413f6ea2cb3dcfa017
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    audit:
      original_audit:
        coverage_issues:
        - Result passage disposed without unit P1-S1-C10
        - Result passage disposed without unit P1-S1-C11
        - Result passage disposed without unit P4-S1-C10
        - Result passage disposed without unit P4-S1-C11
        - Result passage disposed without unit P4-S1-C12
        - Result passage disposed without unit P4-S1-C13
        - Result passage disposed without unit P4-S1-C14
        - Result passage disposed without unit P4-S1-C15
        - Result passage disposed without unit P4-S2-C2
        - Result passage disposed without unit P4-S2-C3
        - Result passage disposed without unit P4-S2-C4
        - Accounting without a linked unit P8-S1-C4
        - Unaccounted source passage P8-S1-C4
        - Accounting without a linked unit P9-S1-C1
        - Accounting without a linked unit P9-S1-C2
        - Accounting without a linked unit P9-S1-C3
        - Accounting without a linked unit P9-S1-C4
        - Unaccounted source passage P9-S1-C2
        - Unaccounted source passage P9-S1-C4
        - Unaccounted source passage P9-S1-C3
        - Unaccounted source passage P9-S1-C1
        - Result passage disposed without unit P9-S1-C10
        - Result passage disposed without unit P9-S1-C9
        - Result passage disposed without unit P9-S2-C2
        - Result passage disposed without unit P9-S2-C8
        - Result passage disposed without unit P9-S3-C4
        - Result passage disposed without unit P9-S4-C4
        - Result passage disposed without unit P9-S4-C5
        - Result passage disposed without unit P9-S4-C6
        - Result passage disposed without unit P9-S4-C9
        - Result passage disposed without unit P10-S1-C5
        - Result passage disposed without unit P9-S4-C11
        - Result passage disposed without unit P9-S4-C12
        - Result passage disposed without unit P11-S2-C2
        - Result passage disposed without unit P11-S2-C3
        - Result passage disposed without unit P12-S1-C3
        unattached_null_or_qualifier_ids:
        - P4-S1-C11
        - P4-S1-C12
        - P4-S1-C14
        - P4-S2-C4
        - P6-S2-C10
        - P9-S3-C5
        - P9-S4-C12
        - P10-S3-C11
        - P11-S2-C2
        - P11-S2-C7
        suppressed_nonrepresented_units: 11
        default_disposition_count_requires_completeness_check: 251
        unselected_timing_passages:
        - P2-S3-C9
        personal_effect_slots_without_result_classification: []
        held_frame_selections:
        - slot: dependent_variable_statement
          source_id: P6-S2-C10
          reason: Requires a Methods outcome definition; model selection retained for inspection only
        - slot: dependent_variable_statement
          source_id: P6-S2-C11
          reason: Requires a Methods outcome definition; model selection retained for inspection only
        - slot: dependent_variable_statement
          source_id: P6-S2-C12
          reason: Requires a Methods outcome definition; model selection retained for inspection only
        - slot: dependent_variable_statement
          source_id: P6-S2-C13
          reason: Requires a Methods outcome definition; model selection retained for inspection only
        - slot: dependent_variable_statement
          source_id: P8-S1-C2
          reason: Requires a Methods outcome definition; model selection retained for inspection only
        - slot: dependent_variable_statement
          source_id: P8-S1-C3
          reason: Requires a Methods outcome definition; model selection retained for inspection only
        - slot: dependent_variable_statement
          source_id: P8-S3-C4
          reason: Requires a Methods outcome definition; model selection retained for inspection only
        - slot: dependent_variable_statement
          source_id: P8-S3-C5
          reason: Requires a Methods outcome definition; model selection retained for inspection only
        - slot: dependent_variable_statement
          source_id: P9-S4-C6
          reason: Requires a Methods outcome definition; model selection retained for inspection only
        - slot: eligibility
          source_ids:
          - P2-S3-C9
          - P2-S3-C10
          - P4-S1-C13
          - P4-S1-C14
          - P4-S1-C15
          - P4-S1-C16
          - P4-S3-C5
          - P4-S3-C6
          - P4-S3-C7
          - P4-S3-C8
          - P5-S1-C8
          reason: Runaway selection (>8 passages); entire slot requires source review
        - slot: outcome_definition
          source_ids:
          - P5-S1-C9
          - P5-S1-C10
          - P5-S2-C3
          - P5-S2-C6
          - P5-S2-C7
          - P5-S2-C9
          - P5-S2-C10
          - P5-S2-C12
          - P5-S2-C13
          - P5-S2-C14
          - P5-S3-C3
          - P5-S3-C4
          - P6-S1-C3
          - P6-S1-C4
          - P6-S1-C5
          - P6-S1-C6
          - P6-S1-C7
          - P6-S1-C8
          - P6-S1-C9
          - P6-S1-C10
          - P6-S1-C11
          - P6-S2-C10
          - P6-S2-C11
          - P6-S2-C12
          - P6-S2-C13
          - P7-S1-C2
          - P7-S2-C1
          - P8-S1-C8
          - P8-S1-C9
          - P8-S1-C10
          - P8-S1-C11
          - P8-S1-C12
          - P8-S1-C13
          - P8-S2-C5
          - P8-S2-C6
          - P8-S2-C7
          - P8-S2-C8
          - P8-S2-C9
          - P8-S2-C10
          - P8-S2-C11
          - P8-S2-C12
          - P8-S2-C13
          - P8-S3-C3
          - P8-S3-C4
          - P8-S3-C5
          - P8-S3-C6
          - P8-S3-C7
          - P8-S3-C8
          - P8-S3-C9
          - P8-S3-C10
          - P9-S1-C8
          - P9-S1-C9
          - P9-S1-C10
          - P9-S2-C2
          - P9-S2-C3
          - P9-S2-C4
          - P9-S2-C5
          - P9-S2-C6
          - P9-S2-C7
          - P9-S2-C8
          - P9-S2-C9
          - P9-S3-C2
          - P9-S3-C3
          - P9-S3-C4
          - P9-S3-C5
          - P9-S3-C6
          - P9-S3-C7
          - P9-S3-C8
          - P9-S3-C9
          - P9-S3-C10
          - P9-S3-C11
          - P9-S3-C12
          - P9-S4-C4
          - P9-S4-C5
          - P9-S4-C6
          - P9-S4-C7
          - P9-S4-C8
          - P9-S4-C9
          - P9-S4-C10
          - P9-S4-C11
          reason: Runaway selection (>8 passages); entire slot requires source review
        - slot: limitations
          source_ids:
          - P10-S3-C3
          - P10-S3-C4
          - P10-S3-C5
          - P10-S3-C6
          - P10-S3-C7
          - P10-S3-C8
          - P10-S3-C9
          - P10-S3-C10
          - P10-S3-C11
          - P10-S4-C2
          - P10-S4-C3
          - P10-S4-C4
          - P10-S4-C5
          - P10-S4-C6
          - P10-S4-C7
          - P10-S4-C8
          - P10-S4-C9
          - P10-S4-C10
          - P10-S4-C11
          - P10-S4-C12
          - P11-S1-C1
          - P11-S1-C2
          - P11-S1-C4
          - P11-S1-C5
          - P11-S1-C6
          - P11-S1-C7
          - P11-S1-C8
          - P11-S1-C9
          - P11-S1-C10
          - P11-S1-C11
          - P12-S1-C3
          reason: Runaway selection (>8 passages); entire slot requires source review
        empty_frame_slots_require_confirmation:
        - eligibility
        - outcome_definition
        - limitations
        - personal_factors
        - tested_personal_effects
        - explicitly_not_adjusted
        unclassified_extraction_ids: []
        table_review_required:
        - TABLE-1-page-4-1
        - TABLE-2-page-4-2
        - TABLE-3-page-5-3
        - TABLE-4-page-6-4
        - TABLE-5-page-7-5
        - TABLE-5-page-8-6
        - TABLE-6-page-11-7
        - TABLE-6-page-11-8
        unlinked_tables:
        - TABLE-1-page-4-1
        - TABLE-2-page-4-2
        - TABLE-3-page-5-3
        - TABLE-4-page-6-4
        - TABLE-5-page-7-5
        - TABLE-5-page-8-6
        - TABLE-6-page-11-7
        - TABLE-6-page-11-8
        source_anomalies: []
        visual_review_required:
          scope: All main-paper figures and table crops
          note: Automatic crops and matching transcriptions do not certify visual completeness. Figures are not automatically interpreted.
          caption_candidate_units:
          - P2-S3
          - P2-S4
          - P3-S1
        approval: Not performed. Structural checks and model selections do not establish semantic correctness.
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: ccd84f115f464675d9dc92bc5df1deabc67b02a9eb42f72849745a981dc374d8
        source_review: _compare/relationships-2026-11-16/review-current/Durfee2021
        source_status_sha256: 3f761cdd0e697255bda542b600e23688e5810cf3517c0e413f6ea2cb3dcfa017
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
      coverage:
      - source_id: P1-S1-C10
        disposition: background_or_descriptive
        result_indexes: []
        reason: Describes general profile characteristics of lesions across timeframes without a specific relationship.
      - source_id: P1-S1-C11
        disposition: represented
        result_indexes:
        - 0
        - 1
        reason: Establishes the relationship between RH dorsal/ventral regions and production/comprehension impairments.
      - source_id: P4-S1-C10
        disposition: background_or_descriptive
        result_indexes: []
        reason: Reports total number of articles yielded by search.
      - source_id: P4-S1-C11
        disposition: background_or_descriptive
        result_indexes: []
        reason: Reports number of articles after duplicate removal.
      - source_id: P4-S1-C12
        disposition: background_or_descriptive
        result_indexes: []
        reason: Reports number of articles removed for lack of prosody or RH damage.
      - source_id: P4-S1-C13
        disposition: background_or_descriptive
        result_indexes: []
        reason: Reports number of articles excluded due to poor methodological strength.
      - source_id: P4-S1-C14
        disposition: background_or_descriptive
        result_indexes: []
        reason: Reports number of articles excluded due to inability to determine localization.
      - source_id: P4-S1-C15
        disposition: background_or_descriptive
        result_indexes: []
        reason: Reports number of articles removed for inadequate imaging or control information.
      - source_id: P4-S2-C2
        disposition: background_or_descriptive
        result_indexes: []
        reason: Reports inter-rater reliability of quality ratings.
      - source_id: P4-S2-C3
        disposition: background_or_descriptive
        result_indexes: []
        reason: Reports inter-rater reliability of quality ratings.
      - source_id: P4-S2-C4
        disposition: background_or_descriptive
        result_indexes: []
        reason: Reports inter-rater reliability of quality ratings.
      - source_id: P6-S2-C4
        disposition: represented
        result_indexes:
        - 13
        reason: Reports large effect sizes for RH vs LH lesions on recognition tasks.
      - source_id: P6-S2-C5
        disposition: represented
        result_indexes:
        - 14
        reason: Reports trivial effect sizes for specific lesion regions vs others.
      - source_id: P6-S2-C10
        disposition: background_or_descriptive
        result_indexes: []
        reason: States the number of studies associating acute stroke with production impairment.
      - source_id: P8-S4-C10
        disposition: background_or_descriptive
        result_indexes: []
        reason: Explains the calculation method for odds ratios.
      - source_id: P8-S5-C2
        disposition: background_or_descriptive
        result_indexes: []
        reason: Explains the calculation method for odds ratios.
      - source_id: P9-S1-C1
        disposition: represented
        result_indexes:
        - 27
        reason: Reports higher likelihood of expressive aprosodia for frontal lobe, insula, and white matter pathways.
      - source_id: P9-S1-C2
        disposition: repeated
        result_indexes:
        - 27
        reason: Restates the association of white matter pathways with expressive aprosodia.
      - source_id: P9-S1-C3
        disposition: represented
        result_indexes:
        - 28
        reason: Reports higher likelihood of receptive aprosodia for temporal/occipital lobes and subcortical nuclei.
      - source_id: P9-S1-C4
        disposition: represented
        result_indexes:
        - 29
        reason: Reports similar ratios of receptive vs expressive aprosodia for parietal damage.
      - source_id: P9-S1-C9
        disposition: repeated
        result_indexes:
        - 27
        reason: Restates that frontal regions are more consistently observed with expressive over receptive aprosodia.
      - source_id: P9-S1-C10
        disposition: repeated
        result_indexes:
        - 28
        reason: Restates that receptive aprosodia is more often associated with posterior damage.
      - source_id: P9-S2-C2
        disposition: repeated
        result_indexes:
        - 28
        reason: Restates the association of receptive aprosodia with posterior damage.
      - source_id: P9-S2-C8
        disposition: repeated
        result_indexes:
        - 27
        reason: Restates that frontal RH regions were more often associated with expressive aprosodia.
      - source_id: P9-S3-C4
        disposition: repeated
        result_indexes:
        - 27
        reason: Restates that white matter pathways were more likely associated with expressive over receptive aprosodia.
      - source_id: P9-S3-C5
        disposition: background_or_descriptive
        result_indexes: []
        reason: Cites specific study (Patel et al., 2018) regarding white matter pathways.
      - source_id: P9-S4-C4
        disposition: repeated
        result_indexes:
        - 29
        reason: Restates that neither aprosodia type occurred more frequently for parietal lobe.
      - source_id: P9-S4-C5
        disposition: repeated
        result_indexes:
        - 29
        reason: Provides the specific article counts for parietal damage.
      - source_id: P9-S4-C6
        disposition: background_or_descriptive
        result_indexes: []
        reason: Discusses the role of the supramarginal gyrus as an integrative region.
      - source_id: P9-S4-C9
        disposition: repeated
        result_indexes:
        - 28
        reason: Restates that temporal regions were associated with receptive over expressive aprosodia.
      - source_id: P9-S4-C10
        disposition: background_or_descriptive
        result_indexes: []
        reason: Discusses the role of the posterior superior temporal gyrus.
      - source_id: P9-S4-C11
        disposition: background_or_descriptive
        result_indexes: []
        reason: Compares frequency of basal ganglia involvement to other nuclei.
      - source_id: P9-S5-C1
        disposition: background_or_descriptive
        result_indexes: []
        reason: Continuation of sentence regarding basal ganglia.
      - source_id: P9-S5-C3
        disposition: background_or_descriptive
        result_indexes: []
        reason: Posits the role of basal ganglia in both expression and recognition.
      - source_id: P10-S1-C5
        disposition: background_or_descriptive
        result_indexes: []
        reason: States that limited data does not support a review of specific cognitive processes at this time.
      - source_id: P10-S1-C6
        disposition: background_or_descriptive
        result_indexes: []
        reason: Introduces the topic of longitudinal stroke recovery.
      - source_id: P10-S3-C11
        disposition: background_or_descriptive
        result_indexes: []
        reason: Discusses the number of articles reporting perfusion information.
      - source_id: P11-S2-C2
        disposition: background_or_descriptive
        result_indexes: []
        reason: Reports the proportion of articles reporting concomitant motor/cognitive deficits.
      - source_id: P11-S2-C3
        disposition: background_or_descriptive
        result_indexes: []
        reason: Describes the variation in reported post-stroke communication abilities.
      - source_id: P11-S2-C7
        disposition: background_or_descriptive
        result_indexes: []
        reason: Describes co-occurrence of receptive affective aprosodia with other deficits.
      - source_id: P12-S1-C1
        disposition: background_or_descriptive
        result_indexes: []
        reason: Continuation of sentence regarding co-occurrence of deficits.
      - source_id: P12-S1-C3
        disposition: repeated
        result_indexes:
        - 0
        - 1
        reason: Conclusion restating the essential roles of frontal, temporal, and parietal regions.
      unresolved_coverage:
      - source_id: P9-S5-C1
        disposition: unresolved
        reason: Coverage source was not requested or was repeated; not accepted as coverage
      - source_id: P9-S5-C3
        disposition: unresolved
        reason: Coverage source was not requested or was repeated; not accepted as coverage
      - source_id: P9-S4-C12
        disposition: unresolved
        reason: Discovery omitted this passage
      pending_source_ids:
      - P1-S1-C10
      - P4-S1-C10
      - P4-S1-C11
      - P4-S1-C12
      - P4-S1-C13
      - P4-S1-C14
      - P4-S1-C15
      - P4-S2-C2
      - P4-S2-C3
      - P4-S2-C4
      - P6-S2-C10
      - P8-S4-C10
      - P8-S5-C2
      - P9-S1-C2
      - P9-S1-C9
      - P9-S1-C10
      - P9-S2-C2
      - P9-S2-C8
      - P9-S3-C4
      - P9-S3-C5
      - P9-S4-C4
      - P9-S4-C5
      - P9-S4-C6
      - P9-S4-C9
      - P9-S4-C10
      - P9-S4-C11
      - P9-S4-C12
      - P10-S1-C5
      - P10-S1-C6
      - P10-S3-C11
      - P11-S2-C2
      - P11-S2-C3
      - P11-S2-C7
      - P12-S1-C1
      - P12-S1-C3
      pending_policy: Every result passage without direct candidate evidence remains pending, including model-labelled background and restatements; those labels never certify completeness.
      tables_requiring_review:
      - TABLE-1-page-4-1
      - TABLE-2-page-4-2
      - TABLE-3-page-5-3
      - TABLE-4-page-6-4
      - TABLE-5-page-7-5
      - TABLE-5-page-8-6
      - TABLE-6-page-11-7
      - TABLE-6-page-11-8
      paper_complete: false
      approved: false
      policy: New candidates require independent source checks; coverage dispositions are model suggestions. No original outputs changed.
    study_frame:
      slots:
        analysed_sample:
        - P1-S1-C9
        recruited_sample:
        - P1-S1-C8
        eligibility: []
        imaging_provenance:
        - P4-S2-C7
        - P4-S2-C9
        - P4-S2-C11
        - P5-S1-C4
        - P10-S3-C6
        - P10-S3-C7
        - P10-S3-C9
        - P10-S3-C11
        imaging_timing:
        - P4-S2-C5
        - P4-S2-C7
        - P4-S2-C11
        - P5-S1-C4
        - P10-S1-C7
        - P10-S1-C10
        - P10-S3-C7
        - P10-S3-C9
        outcome_timing:
        - P4-S2-C5
        - P4-S2-C10
        - P5-S1-C6
        - P10-S1-C7
        - P10-S1-C10
        - P10-S1-C11
        - P10-S1-C12
        outcome_definition: []
        validation:
        - P9-S1-C5
        analysis_restrictions:
        - P4-S2-C6
        - P4-S2-C10
        - P4-S3-C4
        - P5-S1-C8
        - P8-S4-C7
        - P10-S3-C3
        dependent_variable_statement:
        - P5-S2-C7
        - P5-S2-C8
        - P6-S2-C6
        - P6-S2-C7
        limitations: []
        personal_factors: []
        tested_personal_effects: []
        adjustment_roles:
        - P5-S2-C7
        - P6-S3-C2
        - P8-S1-C2
        - P8-S1-C3
        - P8-S3-C4
        - P9-S4-C6
        explicitly_not_adjusted: []
        descriptive_personal_factors:
        - P2-S4-C10
        - P5-S3-C5
        - P11-S2-C2
      outcome_type: both_reported
      imaging_vs_outcome: mixed
      validation_type: none_described
      held_selections:
      - slot: dependent_variable_statement
        source_id: P6-S2-C10
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: dependent_variable_statement
        source_id: P6-S2-C11
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: dependent_variable_statement
        source_id: P6-S2-C12
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: dependent_variable_statement
        source_id: P6-S2-C13
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C3
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: dependent_variable_statement
        source_id: P8-S3-C4
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: dependent_variable_statement
        source_id: P8-S3-C5
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: dependent_variable_statement
        source_id: P9-S4-C6
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: eligibility
        source_ids:
        - P2-S3-C9
        - P2-S3-C10
        - P4-S1-C13
        - P4-S1-C14
        - P4-S1-C15
        - P4-S1-C16
        - P4-S3-C5
        - P4-S3-C6
        - P4-S3-C7
        - P4-S3-C8
        - P5-S1-C8
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: outcome_definition
        source_ids:
        - P5-S1-C9
        - P5-S1-C10
        - P5-S2-C3
        - P5-S2-C6
        - P5-S2-C7
        - P5-S2-C9
        - P5-S2-C10
        - P5-S2-C12
        - P5-S2-C13
        - P5-S2-C14
        - P5-S3-C3
        - P5-S3-C4
        - P6-S1-C3
        - P6-S1-C4
        - P6-S1-C5
        - P6-S1-C6
        - P6-S1-C7
        - P6-S1-C8
        - P6-S1-C9
        - P6-S1-C10
        - P6-S1-C11
        - P6-S2-C10
        - P6-S2-C11
        - P6-S2-C12
        - P6-S2-C13
        - P7-S1-C2
        - P7-S2-C1
        - P8-S1-C8
        - P8-S1-C9
        - P8-S1-C10
        - P8-S1-C11
        - P8-S1-C12
        - P8-S1-C13
        - P8-S2-C5
        - P8-S2-C6
        - P8-S2-C7
        - P8-S2-C8
        - P8-S2-C9
        - P8-S2-C10
        - P8-S2-C11
        - P8-S2-C12
        - P8-S2-C13
        - P8-S3-C3
        - P8-S3-C4
        - P8-S3-C5
        - P8-S3-C6
        - P8-S3-C7
        - P8-S3-C8
        - P8-S3-C9
        - P8-S3-C10
        - P9-S1-C8
        - P9-S1-C9
        - P9-S1-C10
        - P9-S2-C2
        - P9-S2-C3
        - P9-S2-C4
        - P9-S2-C5
        - P9-S2-C6
        - P9-S2-C7
        - P9-S2-C8
        - P9-S2-C9
        - P9-S3-C2
        - P9-S3-C3
        - P9-S3-C4
        - P9-S3-C5
        - P9-S3-C6
        - P9-S3-C7
        - P9-S3-C8
        - P9-S3-C9
        - P9-S3-C10
        - P9-S3-C11
        - P9-S3-C12
        - P9-S4-C4
        - P9-S4-C5
        - P9-S4-C6
        - P9-S4-C7
        - P9-S4-C8
        - P9-S4-C9
        - P9-S4-C10
        - P9-S4-C11
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: limitations
        source_ids:
        - P10-S3-C3
        - P10-S3-C4
        - P10-S3-C5
        - P10-S3-C6
        - P10-S3-C7
        - P10-S3-C8
        - P10-S3-C9
        - P10-S3-C10
        - P10-S3-C11
        - P10-S4-C2
        - P10-S4-C3
        - P10-S4-C4
        - P10-S4-C5
        - P10-S4-C6
        - P10-S4-C7
        - P10-S4-C8
        - P10-S4-C9
        - P10-S4-C10
        - P10-S4-C11
        - P10-S4-C12
        - P11-S1-C1
        - P11-S1-C2
        - P11-S1-C4
        - P11-S1-C5
        - P11-S1-C6
        - P11-S1-C7
        - P11-S1-C8
        - P11-S1-C9
        - P11-S1-C10
        - P11-S1-C11
        - P12-S1-C3
        reason: Runaway selection (>8 passages); entire slot requires source review
      policy: All slots and enums remain unverified. Held selections are not evidence of absence. Original response is preserved in frame/raw.json.
    approved: false
    source_check:
      profile: core
      scope: Independent model text review of core meaning; not human approval or complete PDF verification
      binding:
        profile: core
        version: core-source-check-v3
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        checker_model: qwen3.8:27b
        checker_digest: 47951e4a666180bc2aedfc93c169472f2de783696fe196efbf063f5730ecf163
        host: http://localhost:11434
        pdf_sha256: ccd84f115f464675d9dc92bc5df1deabc67b02a9eb42f72849745a981dc374d8
        review_sha256: 3c3e749bbeb85252e97e4dec8e8dbb5075c4d0e2ddb45ff086cbc832ee2697ee
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
        - P8-S1-C2
        source_result: In a study of acute stroke patients (Patel et al., 2018), percent damage to the right supramarginal gyrus and superior longitudinal fasciculus (SLF) were identified as independent predictors of the coefficient of variation in fundamental frequency (CoVF0).
        result_status: detected
        patient_measurement: template_lesion_overlap
        checks:
          analysis_identity:
            answer: fits
            reason: The source P8-S1-C2 explicitly identifies 'percent damage to right supramarginal gyrus and SLF' as 'independent predictors of CoVF0'. The proposed core correctly identifies this specific analysis and its outcome.
            source_ids:
            - P8-S1-C2
          direction:
            answer: fits
            reason: The source states these factors are 'independent predictors', implying a statistically detected association. The proposed core uses 'likely' direction, which is a reasonable qualitative representation of a predictive relationship without specifying the sign (positive/negative) which is not explicitly detailed in the snippet, but the existence of the association is preserved.
            source_ids:
            - P8-S1-C2
          construct:
            answer: fits
            reason: The exposure is correctly identified as damage to the right supramarginal gyrus and SLF. The outcome is CoVF0. The method is described as 'LSM' (Lesion-Symptom Mapping) in the core, which aligns with the source's context of acute lesion-deficit associations (P4-S2-C8) and the use of 'percent damage' (a metric derived from overlaying lesions on anatomical maps). The patient measurement is template_lesion_overlap because 'percent damage' to specific named structures (SMG, SLF) implies overlaying patient lesions onto reference tract/region maps, rather than patient-specific diffusion tractography or voxel-wise tissue analysis.
            source_ids:
            - P8-S1-C2
            - P4-S2-C8
          qualifications:
            answer: fits
            reason: The core includes the qualification 'measured as independent predictors', which accurately reflects the source text 'Independent predictors of CoVF0 included...'. It also notes the context of a systematic review. No material qualifiers are lost.
            source_ids:
            - P8-S1-C2
          missing_material_caveat:
            answer: fits
            reason: The source P8-S1-C2 is a concise statement of a finding. While P8-S1-C4 mentions that ventral stream regions were *not* associated, this is a separate finding. The core focuses on the positive finding for SMG/SLF. No material caveat regarding the specific SMG/SLF finding is omitted from the source snippet provided.
            source_ids:
            - P8-S1-C2
        optional_pending:
        - Specific statistical values (p-values, beta coefficients) for the SMG/SLF prediction of CoVF0 are not transcribed in the source snippet.
        - The specific direction of the effect (whether damage increases or decreases CoVF0) is not explicitly stated in P8-S1-C2, only that it is a predictor.
        verdict: draft
        reason: All five core checks fit the source.
        material_issues: []
      pending_details:
      - Detailed statistics, atlas/reference-space and structured confounder metadata not transcribed.
      - Recovery phase is not classified; use the reported timing words.
      - Evidence-strength rating is a conservative draft placeholder pending human review.
      - Specific statistical values (p-values, beta coefficients) for the SMG/SLF prediction of CoVF0 are not transcribed in the source snippet.
      - The specific direction of the effect (whether damage increases or decreases CoVF0) is not explicitly stated in P8-S1-C2, only that it is a predictor.
      normalizations:
      - field: bucket
        original: predictors
        action: route_from_kind
        value: regions
      analysis_identity:
        id: R015
        exposure:
          text: right supramarginal gyrus and SLF damage
        outcome:
          text: coefficient of variation in fundamental frequency (CoVF0)
        analysis_label: Acute lesion analysis (Patel et al., 2018)
        relation: association
        evidence_ids:
        - P8-S1-C2
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
          pdf_sha256: ccd84f115f464675d9dc92bc5df1deabc67b02a9eb42f72849745a981dc374d8
          source_review: _compare/relationships-2026-11-16/review-current/Durfee2021
          source_status_sha256: 3f761cdd0e697255bda542b600e23688e5810cf3517c0e413f6ea2cb3dcfa017
          code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
          version: candidate-inventory-v1
      paper_complete: false
      visual_prose_readings:
        P4-S2-C5:
          binding:
            version: prose-images-v14
            code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
            pdf_sha256: ccd84f115f464675d9dc92bc5df1deabc67b02a9eb42f72849745a981dc374d8
            layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
            anchor_sha256: 0eaaa395a575d721b38ebceae3c90d8cc50833e5dd2cc0c636c505472f0424f0
            exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
            source_id: P4-S2-C5
            page: 4
            text_layer_sha256: 0eaaa395a575d721b38ebceae3c90d8cc50833e5dd2cc0c636c505472f0424f0
            models: *id001
            model_digests: *id002
            host: http://localhost:11434
          status: agreed_model_transcription
          original_text: "Time post-stroke and brain imaging considerations \nResults are divided into studies of patients with acute stroke (<1 \nweek) versus those with subacute (1 week–3 months) or chronic (>3 \nmonths) because different approaches to brain imaging and mapping are \nneeded depending on the time post-onset at which patients are studied."
          anchor_text: "Time post-stroke and brain imaging considerations \nResults are divided into studies of patients with acute stroke (<1 \nweek) versus those with subacute (1 week–3 months) or chronic (>3 \nmonths) because different approaches to brain imaging and mapping are \nneeded depending on the time post-onset at which patients are studied."
          excluded_fragments: []
          image_sha256: abd40fe946cae34243f54279746bc0909447564f2403d813139a54a3ff85e3b7
          transcription: 'Time post-stroke and brain imaging considerations


            Results are divided into studies of patients with acute stroke (<1 week) versus those with subacute (1 week–3 months) or chronic (>3 months) because different approaches to brain imaging and mapping are needed depending on the time post-onset at which patients are studied'
      remaining:
      - Human PDF review and approval
      - Pending metadata enrichment
      - Main Results, figures and tables completeness check
  original_publication_entry:
    id: right_smg_slf_damage
    name: right supramarginal gyrus and SLF damage
    kind: network
    findings:
    - id: f1
      target: covf0
      target_kind: impairment
      claim: percent damage to the right supramarginal gyrus and SLF were independent predictors of the coefficient of variation in fundamental frequency (CoVF0).
      direction: likely
      relationship: correlational
      method: LSM
      sample:
        n: not_reported
        population: patients with acute stroke
        phase: not_reported
        time_post_onset: acute (<1 week post-stroke)
      statistics:
        threshold: not_transcribed
      confounders_controlled: []
      confounders_not_controlled: []
      region_definition:
        kind: not_reported
        description: Not transcribed; see source passages and claim.
      author_limitations:
      - finding is part of a systematic review of 11 articles
      evidence_quality: cohort
      strength: weak
      notes: 'Exposure measurement: percent damage to the right supramarginal gyrus and superior longitudinal fasciculus (SLF). measured as independent predictors. Additional metadata has not been transcribed; review the pending-field flags before approval. PDF image reading (P4-S2-C5, two-model agreement, human verification pending): Time post-stroke and brain imaging considerations


        Results are divided into studies of patients with acute stroke (<1 week) versus those with subacute (1 week–3 months) or chronic (>3 months) because different approaches to brain imaging and mapping are needed depending on the time post-onset at which patients are studied Original text-layer quotation is preserved below.'
      imaging_details:
        reference_space: not_reported
        atlases_used: []
      lesion_mapping: {}
      provenance:
        extracted_by: model:gemma4:31b
        extracted_on: '2026-11-23'
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
        - proposed_concept:covf0
      citation: '@Durfee2021'
      source_passages:
      - section: Original source P8-S1-C2
        page: 8
        quote: "Independent predictors of CoVF0 included age \nand percent damage to right supramarginal gyrus and SLF."
        supports: claim
      - section: Original source P4-S2-C5
        page: 4
        quote: "Time post-stroke and brain imaging considerations \nResults are divided into studies of patients with acute stroke (<1 \nweek) versus those with subacute (1 week–3 months) or chronic (>3 \nmonths) because different approaches to brain imaging and mapping are \nneeded depending on the time post-onset at which patients are studied."
        supports: sample
      - section: Original source P4-S2-C7
        page: 4
        quote: "Acute lesion-deficit association studies use either follow-up head \ncomputed tomography (CT) or diffusion-weighted imaging (DWI; \nrevealing the infarct within minutes of onset) with or without perfusion- \nweighted imaging (PWI; revealing hypoperfused, dysfunctional tissue \nsurrounding the infarct)."
        supports: method
    schema_version: '2.8'
    status: draft
    created_by: agent:relationship-converter
    created_on: '2026-11-23'
    relationship_review:
      paper: Durfee2021
      proposal_id: R015
      review_status_sha256: 3c3e749bbeb85252e97e4dec8e8dbb5075c4d0e2ddb45ff086cbc832ee2697ee
      review_binding:
        version: candidate-inventory-v1
        input_hashes:
          pdf: ccd84f115f464675d9dc92bc5df1deabc67b02a9eb42f72849745a981dc374d8
        original_review_binding:
          version: relationship-review-v4
          input_hashes:
            pdf: ccd84f115f464675d9dc92bc5df1deabc67b02a9eb42f72849745a981dc374d8
            A/passages.json: 9940d5cdf1b01ec683c0cc01265a41a196bd09af1ae5492eb65075cdddf7a34e
            A/raw.json: 1da4f1ca288ba7288e76b418189710efb50191ad1bb69b72212d109a6a9ba45b
            A/source-units.json: 6368a5d4fe40ace5037d754cfd4f455ffda3cab1111c5f7d3bfc30dae13dd5bf
            A/full-source-units.json: 4b35e89efe1e861bb33369cd36aba3074af33699bd0ded2728a90993d5c1d8a1
            A/meta.json: 71a47fc491423b49aa2c36e68d4a48e10cdcbd0e0e5ea343290c8207c5cb907b
            A/table-images/page-11.png: b77d1ccb0718256caa489f4956bcbb3b23fdb2d8bbeb10a59aa550650208d04f
            A/table-images/TABLE-5-page-8-1.png: ac6c4c63816de9780c9c961a1489dd4393ed7ec02a788e377c3f27751c86b881
            A/table-images/page-6.png: 3d534538a361d492318181ae3cfc24a1d971c97cd5a8d94df9a89bb385ee41e0
            A/table-images/page-7.png: e7c643e9a648be4d90f9f2ebea0f4aba54974b621dc415d5ba48123b2de9ae8b
            A/table-images/page-5.png: 88b5365c9a983b3474247a5035e35d7a0f7c00a753d2ab0f2ab29a6adc4709d2
            A/table-images/page-4.png: 40a0d144166d26aeba70303eedcc23a9f7d702185221aab632ca4a64170bffa9
            A/table-images/TABLE-1-page-4-1.png: 155ef3a5432cbeff517d5df085e73230cb6bee1fd573f8849813270c2acaf58f
            A/table-images/TABLE-4-page-6-1.png: b6ed4a220def952a83a8452f7523885d959bb2d7abe8b30247d27a37e4edf123
            A/table-images/page-8.png: 92530218370780a2ec0ba616287f24a720302fbb0c51e72ec52def044b0ee0bb
            A/table-images/TABLE-6-page-11-1.png: 61de752fe80af2e298e86f2d03285bb4ccdeaecdbe37aaec0da6fa7d92a7461f
            A/table-images/TABLE-2-page-4-2.png: e785915270f8d16b1b07dfdad681f6b89836429dc238d0cf35755c0b233871f1
            A/table-images/manifest.json: 2282b3d7df7aaae6d286f080161519d5c6e315dca67c6581aa571168de252e9c
            A/table-images/TABLE-6-page-11-2.png: 2ab3cd9eb8c46ee4854f5b77d1cd5e3b702effaa398136f944fa75fecffe5aa3
            A/table-images/TABLE-3-page-5-1.png: 0ce70e7875b1dbfe64e1f1f2fdffc04232db59119cf000b69bee06431d275c11
            A/table-images/TABLE-5-page-7-1.png: 6bee08da6c58d5591a46fce1952cba96ca584cc62cf9c09859f7257384fb1ad7
            A/clauses/window-11/raw.json: d207e08b679ecb8944273048640f452555dc529810edc82d96a04fea37755092
            A/clauses/window-11/prompt.txt: 8e499193a44781032843e1617f80878f4262fca7bdd14906bca22dd3047f0863
            A/clauses/window-11/meta.json: c2d588a4c92972af3575b3925d3b6e02334f199efb69d93415e7ab66e4b9be63
            A/clauses/window-10/raw.json: c2ce714b32355c0bb3cfdcc7e5c9688a1cd1081fd92cf8215a3297e9aeef16ad
            A/clauses/window-10/prompt.txt: 0e0b288d869131c3d64b6e09301f193a05e8c2cbd4d650d4fae2c5294975d034
            A/clauses/window-10/meta.json: 4131d46e96048491648263fd482db19b386c1d9921a0001f1a0c45a52ccff7f8
            A/clauses/window-03/raw.json: d3395a8f28b16b23a280df0cb86731d2a447adb26a56c6b392e592063c777a1c
            A/clauses/window-03/prompt.txt: 0afe2a35b6fa3545fc338d65d91b63e16c67f63a96acdcf8264fb1e4c2cface7
            A/clauses/window-03/meta.json: a5e1ec6cbf27fe69578f80a1351646f07478acb1575a72bf11e4eea2230d7759
            A/clauses/window-04/raw.json: 608530d70b45925642f06b59b10142634935a36d6425a6c59c89945c5f6a0282
            A/clauses/window-04/prompt.txt: e3894beb1dd39d87550ed62292f079a4deef9cbda463176897bce2b0aed70fd2
            A/clauses/window-04/meta.json: 5418fa330f12bf4683fdf55d42731e91ca69d1160faff7596c994ce2654add28
            A/clauses/window-05/raw.json: 8fc728e3712f7b0dd9424f75f1a8a4489b82a493927eb19e405f42c6e1ef5410
            A/clauses/window-05/prompt.txt: 9d42250cd8bd5e4e3bd3c16a6766461c3d45aa9cebe9faedbfc8f4211b00b604
            A/clauses/window-05/meta.json: 8f1a269836be5d730ffd0530fcca0a2fc1e1ded9ad207f722205e792ebeb29d4
            A/clauses/window-02/raw.json: 1d34bb9ad619f0087b8d980c3511c6dc81bd74808b580b6801d932f5f877cff8
            A/clauses/window-02/prompt.txt: 44e2e215d40fe86f74395a9c0e732f9031955040e83f1298830a89949609207d
            A/clauses/window-02/meta.json: c33dc41c3d84a8fac39d9a41177c7a785237c5696d1de3e1d5538e2daef40596
            A/clauses/window-12/raw.json: 882da49aca5959baa9bf73ccb64e31bcc15786db8c7886ecd23145a509b50f8e
            A/clauses/window-12/prompt.txt: 59304e2db4ebff2421d5bbec13233209ad4c2f00ae21c02863f505d7189a9e14
            A/clauses/window-12/meta.json: 4f17b25da9d8536ef2cc39be34ca80de06f3884096e83309ab3a1f26e1a8ed71
            A/clauses/window-09/raw.json: eb7b5df01ead7f6808c31b2c6be86af12182401366e26dcc23321e7caf346f4b
            A/clauses/window-09/prompt.txt: 1005da75d8394954fd60bf002e5bebfa63f98b3e453c7cfc2f902e50ff8a698d
            A/clauses/window-09/meta.json: 8378417bf603b06f1ea931d2d8b5feb2853b3eb2e35a7ff1c83a1e168e7933bb
            A/clauses/window-07/raw.json: cc73beeadc8d7cce39801b88d36314c693ae8b48c2002547c0f567c963a85d1b
            A/clauses/window-07/prompt.txt: 49134434f878a1013fc09269768c615200c29eb3a6037159441877ec42449394
            A/clauses/window-07/meta.json: 1c2ae55da975b253427468f1f9f036ac62230b1295c392adc148855233fce4e4
            A/clauses/window-01/raw.json: a08e1173d89929e6aeb74a080741a3a65a71665bc904797261a8d443727c5795
            A/clauses/window-01/prompt.txt: efd7329fb8dfd2d24b4ef906188f9d85221525b59bbc490b369197c007ca81e9
            A/clauses/window-01/meta.json: 33f83c44fcdeac820e8c1bc29d443f82222370d16413483fdae65da44f79f93b
            A/clauses/window-06/raw.json: aae81b5136ead07d41a726dca63198b1e17d334c2a33b0fa862f509e756e96a3
            A/clauses/window-06/prompt.txt: d716dcb0ac39b255238db75160af8dfbb954f169e3b8d4db1d32ca3f8150c78f
            A/clauses/window-06/meta.json: 8317d89042fe14c2d735f7e55f44f89a042319e781e0f6f6487154dcd724aa7b
            A/clauses/window-08/raw.json: dbfe9dc303458bfb18ee01ada58952e896b5c006ea9c2b6d0a47b43c808e057f
            A/clauses/window-08/prompt.txt: 3d2ee0f34140f2737ede91bd3ea748f065ebf8a09f2bd1926af03acdc6013d40
            A/clauses/window-08/meta.json: 256efa8c397465c544e9bf4744bce482bc4c21306caa3cca8964e38a17d44fec
            A/tables/TABLE-4-page-6-4/raw.json: c7119b44d61121965f0764ee146117e5156139ffc64166c6f06979de85188568
            A/tables/TABLE-4-page-6-4/prompt.txt: 257b25324e41a8dce84bc1e7514933367d098f36c4f5aae446180727096aa490
            A/tables/TABLE-4-page-6-4/meta.json: e785dae97371842f8f9390f939524012a3cd415f679b6c921fa35343ea360adf
            A/tables/TABLE-3-page-5-3/raw.json: d7c8a7277d4eb099afa999bd9cc1f4aa88e1a580433fb6272487c1a5aae88cbd
            A/tables/TABLE-3-page-5-3/prompt.txt: 51e8ff831667e9b99dd0e7d3b546f6b4c618187c3ce0be32f9f007bdeba8c5e5
            A/tables/TABLE-3-page-5-3/meta.json: 843778231a2476c9e0519b2c2a39a0f4dfba00be58885a445ebb2bdcbe428ec8
            A/tables/TABLE-6-page-11-8/raw.json: 519c8108f829be68590cd2273bebff757a5b1bac35336147e6516cd850143446
            A/tables/TABLE-6-page-11-8/prompt.txt: 46e31bcd871935e1c91bbf8b6d8253ca5f8478a2e0123a964bd976de7094b5d9
            A/tables/TABLE-6-page-11-8/meta.json: c5e0981e795c223d0b38126a82f85f39184c91886d0526db3efa1274b604f4a1
            A/tables/TABLE-6-page-11-7/raw.json: 5423f4a64647b0897ec4b839eab6767fcc1f2680e4d167ec4ccd657d656d0a92
            A/tables/TABLE-6-page-11-7/prompt.txt: b12906cd7835b45e8502b8f6f94d9df8e909e0901c36978ae3722a85aca6c50f
            A/tables/TABLE-6-page-11-7/meta.json: ab28ffc5ea49d0101b6eaad3d5917924efcb6814ef32d511f08f5d611207f793
            A/tables/TABLE-5-page-8-6/raw.json: b9bb31c781d35ebf35ff49be09a7874073636db72bc6fa066b76e37664fe5f01
            A/tables/TABLE-5-page-8-6/prompt.txt: 79683064f99b6c1b8a6d229f945ac23a0b2bae6c2ecaf5b0c3d4438b2a84d946
            A/tables/TABLE-5-page-8-6/meta.json: 9c401e562462a1638616479bea4be0cd93e978186cfdf9bb0602bee4883105ad
            A/tables/TABLE-1-page-4-1/raw.json: 871725b345fdc526d5cab8ddc511b943efd40803c951d261c40ffb63d4258072
            A/tables/TABLE-1-page-4-1/prompt.txt: ac7936ebb3deacf60fed55bdfd28b4fe69bb13cf11de5afcd8ba08ac43b73b9d
            A/tables/TABLE-1-page-4-1/meta.json: 6f9f78b3191164c36dc7c07971249aea776b3d7a165ff268d767c91755ac4712
            A/tables/TABLE-5-page-7-5/raw.json: 4a40adb15409f6393c79c6ad525ad1c2a7f0a669675d98066e31954d7e066035
            A/tables/TABLE-5-page-7-5/prompt.txt: 364563fb118a545dfbf2a526ab6eecb0924e42e513541279ccaae9e4228159e2
            A/tables/TABLE-5-page-7-5/meta.json: 9c815000a778bb4a4b313f4942425f43ed2d8892415cf1c994b145252ba75d85
            A/tables/TABLE-2-page-4-2/raw.json: f3a127297ee15846b718e5dba3de7b180bfeec0ea8f113d760e631e677b917c6
            A/tables/TABLE-2-page-4-2/prompt.txt: ab9282e57a288b60895ce547e088b832c3a2a917be04e3eb80eb290f6b91abf6
            A/tables/TABLE-2-page-4-2/meta.json: a1929a3982d53d5737207478483aad6bc3631de9f77dd8ef8706e7fe4fa56a67
            B/passages.json: 9940d5cdf1b01ec683c0cc01265a41a196bd09af1ae5492eb65075cdddf7a34e
            B/raw.json: 10bd35cccf75e442f72761af929550af7a29b9a8d175ec5d309942825e8fbf02
            B/source-units.json: 6368a5d4fe40ace5037d754cfd4f455ffda3cab1111c5f7d3bfc30dae13dd5bf
            B/full-source-units.json: 4b35e89efe1e861bb33369cd36aba3074af33699bd0ded2728a90993d5c1d8a1
            B/meta.json: 364d53699a1161c323f7d7dcdafca5c49fbdf3ee073f0b5ffd8ce0c02f3479f8
            B/table-images/page-11.png: b77d1ccb0718256caa489f4956bcbb3b23fdb2d8bbeb10a59aa550650208d04f
            B/table-images/TABLE-5-page-8-1.png: ac6c4c63816de9780c9c961a1489dd4393ed7ec02a788e377c3f27751c86b881
            B/table-images/page-6.png: 3d534538a361d492318181ae3cfc24a1d971c97cd5a8d94df9a89bb385ee41e0
            B/table-images/page-7.png: e7c643e9a648be4d90f9f2ebea0f4aba54974b621dc415d5ba48123b2de9ae8b
            B/table-images/page-5.png: 88b5365c9a983b3474247a5035e35d7a0f7c00a753d2ab0f2ab29a6adc4709d2
            B/table-images/page-4.png: 40a0d144166d26aeba70303eedcc23a9f7d702185221aab632ca4a64170bffa9
            B/table-images/TABLE-1-page-4-1.png: 155ef3a5432cbeff517d5df085e73230cb6bee1fd573f8849813270c2acaf58f
            B/table-images/TABLE-4-page-6-1.png: b6ed4a220def952a83a8452f7523885d959bb2d7abe8b30247d27a37e4edf123
            B/table-images/page-8.png: 92530218370780a2ec0ba616287f24a720302fbb0c51e72ec52def044b0ee0bb
            B/table-images/TABLE-6-page-11-1.png: 61de752fe80af2e298e86f2d03285bb4ccdeaecdbe37aaec0da6fa7d92a7461f
            B/table-images/TABLE-2-page-4-2.png: e785915270f8d16b1b07dfdad681f6b89836429dc238d0cf35755c0b233871f1
            B/table-images/manifest.json: fc7f7911335d23fd667572a4e1466989e3e49a2579c727a25b1089481efddbab
            B/table-images/TABLE-6-page-11-2.png: 2ab3cd9eb8c46ee4854f5b77d1cd5e3b702effaa398136f944fa75fecffe5aa3
            B/table-images/TABLE-3-page-5-1.png: 0ce70e7875b1dbfe64e1f1f2fdffc04232db59119cf000b69bee06431d275c11
            B/table-images/TABLE-5-page-7-1.png: 6bee08da6c58d5591a46fce1952cba96ca584cc62cf9c09859f7257384fb1ad7
            B/clauses/window-11/raw.json: a082ee8380eff54e1169e3dd025aaf499a3446bfc3394f82f1d6325759677ae9
            B/clauses/window-11/prompt.txt: 8e499193a44781032843e1617f80878f4262fca7bdd14906bca22dd3047f0863
            B/clauses/window-11/meta.json: d91571bb76b84a8aa35ef133afc4ca29ef6a14929ea53e7724f99012d883d1f8
            B/clauses/window-10/raw.json: 69e27ba49770e579688f133b0b49189690627fc53e6fa5aa6819af101f61f504
            B/clauses/window-10/prompt.txt: 0e0b288d869131c3d64b6e09301f193a05e8c2cbd4d650d4fae2c5294975d034
            B/clauses/window-10/meta.json: 0b3d6dbc0891237ca685f6e55716651cc04c211f69909055d76754ca8715e38a
            B/clauses/window-03/raw.json: 025e6cf60f13ed1398e585d7626e7f25429184b6d3c34b84c5fb97ce75cb0ae4
            B/clauses/window-03/prompt.txt: 0afe2a35b6fa3545fc338d65d91b63e16c67f63a96acdcf8264fb1e4c2cface7
            B/clauses/window-03/meta.json: cdcdccbc17671f507220c3f9a6612251bc137bf22f94d9970a5751d160d67080
            B/clauses/window-04/raw.json: a261c44c6fbac09d29876bd7c72d519138e86785029d8866b23c63865c86c93c
            B/clauses/window-04/prompt.txt: e3894beb1dd39d87550ed62292f079a4deef9cbda463176897bce2b0aed70fd2
            B/clauses/window-04/meta.json: 625b94a078a88802c60750311d350c0b83ab5a784b621049a8557ea6f1352c9b
            B/clauses/window-05/raw.json: df4181b7c203d660387bb2b4ab5e74246204ebdb8806bbc3779e5effb59776bd
            B/clauses/window-05/prompt.txt: 9d42250cd8bd5e4e3bd3c16a6766461c3d45aa9cebe9faedbfc8f4211b00b604
            B/clauses/window-05/meta.json: de8cbd5beac9af9ce45424ae41eb945286d10f73376dc606011af84afa1ea782
            B/clauses/window-02/raw.json: 721d847ff1e70c8359195bce1b2b9c195ac676b34f8cbb2bbe1f971e64832958
            B/clauses/window-02/prompt.txt: 44e2e215d40fe86f74395a9c0e732f9031955040e83f1298830a89949609207d
            B/clauses/window-02/meta.json: 79e11c504ecc572b8efedf111c9ef93cf18ee6f5dadd34d44bf395050a435017
            B/clauses/window-12/raw.json: eed250e048e13e65f8d524fa6b4803275970119b03eb134bd91a626581ad3ba1
            B/clauses/window-12/prompt.txt: 59304e2db4ebff2421d5bbec13233209ad4c2f00ae21c02863f505d7189a9e14
            B/clauses/window-12/meta.json: 665f0a853a326947fd73ab4e1c3aeb8f3f6ed35df888c74cbf8abd475ff1b281
            B/clauses/window-09/raw.json: 911ba497160df3de628583cfc915f553631d2db9b0f5568723f1df5f643f8f60
            B/clauses/window-09/prompt.txt: 1005da75d8394954fd60bf002e5bebfa63f98b3e453c7cfc2f902e50ff8a698d
            B/clauses/window-09/meta.json: 72716cc83756caf225adfa21b37977e3f3f5dfa2bc6c5264aa273b39d4fdaeff
            B/clauses/window-07/raw.json: 58df4da7fec737b12e80d2266198913558155b62c3be8a5dab18112dc5c2eab1
            B/clauses/window-07/prompt.txt: 49134434f878a1013fc09269768c615200c29eb3a6037159441877ec42449394
            B/clauses/window-07/meta.json: 23bc48e7b525afb0326520268dd4a0e4c8d9381a5ceda40016cb8fe11a570640
            B/clauses/window-01/raw.json: e350d88569dc5cd09575444c722fb506a60083ad5b300556bf939ca4892fe72a
            B/clauses/window-01/prompt.txt: efd7329fb8dfd2d24b4ef906188f9d85221525b59bbc490b369197c007ca81e9
            B/clauses/window-01/meta.json: fbcc58e12442501b21e7fc72c7175af72fda7d4fe1ba5adc4fd9e5e97cec92d4
            B/clauses/window-06/raw.json: 00323113876c10d4d550a94b11f563cdb61c165aed985173686517eda61fb984
            B/clauses/window-06/prompt.txt: d716dcb0ac39b255238db75160af8dfbb954f169e3b8d4db1d32ca3f8150c78f
            B/clauses/window-06/meta.json: 055ae02db4a4856e7a9ba5ac317a837a1d5c12874cbf1070e9b954d11cbb6462
            B/clauses/window-08/raw.json: fe5ff08992ef9b574f6f67610a22a1704434c816aeacbc38e0b499d301080010
            B/clauses/window-08/prompt.txt: 3d2ee0f34140f2737ede91bd3ea748f065ebf8a09f2bd1926af03acdc6013d40
            B/clauses/window-08/meta.json: 411808dbf5cd583c4db8fdc4df2e5d70d58d1a5840ab1aa69b8669532c0bb69e
            B/tables/TABLE-4-page-6-4/raw.json: 6a77564f47c790d420a48a9f884ba08922323d06244a48e990736cc9046f9caf
            B/tables/TABLE-4-page-6-4/prompt.txt: 257b25324e41a8dce84bc1e7514933367d098f36c4f5aae446180727096aa490
            B/tables/TABLE-4-page-6-4/meta.json: 0bfb7675b8b4cc7d79b0b59b2b4d604502cf9b37e571bb4ed350b29102e6f5e6
            B/tables/TABLE-3-page-5-3/raw.json: 3107c8bded705d3ca755daa1562ef668eec5280cd4f72553a046907104243efa
            B/tables/TABLE-3-page-5-3/prompt.txt: 51e8ff831667e9b99dd0e7d3b546f6b4c618187c3ce0be32f9f007bdeba8c5e5
            B/tables/TABLE-3-page-5-3/meta.json: cebf48bd51df275590a4441ff889b4ba8ba3b77de19cddb83e38a99f09e51d14
            B/tables/TABLE-6-page-11-8/raw.json: ad5dc5a51755b828fe979214e80babca0e106b1be9d290e07de56ffff98679af
            B/tables/TABLE-6-page-11-8/prompt.txt: 46e31bcd871935e1c91bbf8b6d8253ca5f8478a2e0123a964bd976de7094b5d9
            B/tables/TABLE-6-page-11-8/meta.json: e79f226af50a57202562b7cc2674ac1cf9a6dbfb02cd3d36855a39f40ca8fa08
            B/tables/TABLE-6-page-11-7/raw.json: 7c40215cb1f8c41e9393b8f2fb9137d90475c8b1e827193f2ef1d184c1b86c22
            B/tables/TABLE-6-page-11-7/prompt.txt: b12906cd7835b45e8502b8f6f94d9df8e909e0901c36978ae3722a85aca6c50f
            B/tables/TABLE-6-page-11-7/meta.json: a9840e85dc2c4481fe4ba9fd150a5bb719b13fbf12f64ff969d9ed59c9a99182
            B/tables/TABLE-5-page-8-6/raw.json: 088c364582929440df875c52b36aa300721901c2b3c382d4c2f69f23817da38e
            B/tables/TABLE-5-page-8-6/prompt.txt: 79683064f99b6c1b8a6d229f945ac23a0b2bae6c2ecaf5b0c3d4438b2a84d946
            B/tables/TABLE-5-page-8-6/meta.json: 552361af1b3fb77299ae8d82356a1ac6cc3b87487de559400258eaedd019391c
            B/tables/TABLE-1-page-4-1/raw.json: 9ae3517024478797d52552e1ea71919db757a8ddc9df450cf9fdecbc13e29e81
            B/tables/TABLE-1-page-4-1/prompt.txt: ac7936ebb3deacf60fed55bdfd28b4fe69bb13cf11de5afcd8ba08ac43b73b9d
            B/tables/TABLE-1-page-4-1/meta.json: 5acd643ccadf97935006a72d12dd5fe43c2d195f6dff986fba56a277580a67d9
            B/tables/TABLE-5-page-7-5/raw.json: ddc1f6b6828988d8b8f3e414c7d2f03d463534bcdc9f37ef1dc25a40ccdff813
            B/tables/TABLE-5-page-7-5/prompt.txt: 364563fb118a545dfbf2a526ab6eecb0924e42e513541279ccaae9e4228159e2
            B/tables/TABLE-5-page-7-5/meta.json: 7eb427ec8ea0b9940c6e1f07fb633986bb7679cd9d09f1f98b0632c537baedfb
            B/tables/TABLE-2-page-4-2/raw.json: b1fc74f95c4897f8aea2df7fb017ead34dd49e9b429f8ca833c694293d8c335d
            B/tables/TABLE-2-page-4-2/prompt.txt: ab9282e57a288b60895ce547e088b832c3a2a917be04e3eb80eb290f6b91abf6
            B/tables/TABLE-2-page-4-2/meta.json: f8657bdf5b944a0953e88fa793e4331c9307fe2f9ec9086e2a70f1237b1b1af9
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
          pdf_sha256: ccd84f115f464675d9dc92bc5df1deabc67b02a9eb42f72849745a981dc374d8
          source_review: _compare/relationships-2026-11-16/review-current/Durfee2021
          source_status_sha256: 3f761cdd0e697255bda542b600e23688e5810cf3517c0e413f6ea2cb3dcfa017
          code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
          version: candidate-inventory-v1
        packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      proposal:
        id: R015
        exposure:
          text: right supramarginal gyrus and SLF damage
        outcome:
          text: coefficient of variation in fundamental frequency (CoVF0)
        analysis_label: Acute lesion analysis (Patel et al., 2018)
        relation: association
        evidence_ids:
        - P8-S1-C2
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
          pdf_sha256: ccd84f115f464675d9dc92bc5df1deabc67b02a9eb42f72849745a981dc374d8
          source_review: _compare/relationships-2026-11-16/review-current/Durfee2021
          source_status_sha256: 3f761cdd0e697255bda542b600e23688e5810cf3517c0e413f6ea2cb3dcfa017
          code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
          version: candidate-inventory-v1
      audit:
        original_audit:
          coverage_issues:
          - Result passage disposed without unit P1-S1-C10
          - Result passage disposed without unit P1-S1-C11
          - Result passage disposed without unit P4-S1-C10
          - Result passage disposed without unit P4-S1-C11
          - Result passage disposed without unit P4-S1-C12
          - Result passage disposed without unit P4-S1-C13
          - Result passage disposed without unit P4-S1-C14
          - Result passage disposed without unit P4-S1-C15
          - Result passage disposed without unit P4-S2-C2
          - Result passage disposed without unit P4-S2-C3
          - Result passage disposed without unit P4-S2-C4
          - Accounting without a linked unit P8-S1-C4
          - Unaccounted source passage P8-S1-C4
          - Accounting without a linked unit P9-S1-C1
          - Accounting without a linked unit P9-S1-C2
          - Accounting without a linked unit P9-S1-C3
          - Accounting without a linked unit P9-S1-C4
          - Unaccounted source passage P9-S1-C2
          - Unaccounted source passage P9-S1-C4
          - Unaccounted source passage P9-S1-C3
          - Unaccounted source passage P9-S1-C1
          - Result passage disposed without unit P9-S1-C10
          - Result passage disposed without unit P9-S1-C9
          - Result passage disposed without unit P9-S2-C2
          - Result passage disposed without unit P9-S2-C8
          - Result passage disposed without unit P9-S3-C4
          - Result passage disposed without unit P9-S4-C4
          - Result passage disposed without unit P9-S4-C5
          - Result passage disposed without unit P9-S4-C6
          - Result passage disposed without unit P9-S4-C9
          - Result passage disposed without unit P10-S1-C5
          - Result passage disposed without unit P9-S4-C11
          - Result passage disposed without unit P9-S4-C12
          - Result passage disposed without unit P11-S2-C2
          - Result passage disposed without unit P11-S2-C3
          - Result passage disposed without unit P12-S1-C3
          unattached_null_or_qualifier_ids:
          - P4-S1-C11
          - P4-S1-C12
          - P4-S1-C14
          - P4-S2-C4
          - P6-S2-C10
          - P9-S3-C5
          - P9-S4-C12
          - P10-S3-C11
          - P11-S2-C2
          - P11-S2-C7
          suppressed_nonrepresented_units: 11
          default_disposition_count_requires_completeness_check: 251
          unselected_timing_passages:
          - P2-S3-C9
          personal_effect_slots_without_result_classification: []
          held_frame_selections:
          - slot: dependent_variable_statement
            source_id: P6-S2-C10
            reason: Requires a Methods outcome definition; model selection retained for inspection only
          - slot: dependent_variable_statement
            source_id: P6-S2-C11
            reason: Requires a Methods outcome definition; model selection retained for inspection only
          - slot: dependent_variable_statement
            source_id: P6-S2-C12
            reason: Requires a Methods outcome definition; model selection retained for inspection only
          - slot: dependent_variable_statement
            source_id: P6-S2-C13
            reason: Requires a Methods outcome definition; model selection retained for inspection only
          - slot: dependent_variable_statement
            source_id: P8-S1-C2
            reason: Requires a Methods outcome definition; model selection retained for inspection only
          - slot: dependent_variable_statement
            source_id: P8-S1-C3
            reason: Requires a Methods outcome definition; model selection retained for inspection only
          - slot: dependent_variable_statement
            source_id: P8-S3-C4
            reason: Requires a Methods outcome definition; model selection retained for inspection only
          - slot: dependent_variable_statement
            source_id: P8-S3-C5
            reason: Requires a Methods outcome definition; model selection retained for inspection only
          - slot: dependent_variable_statement
            source_id: P9-S4-C6
            reason: Requires a Methods outcome definition; model selection retained for inspection only
          - slot: eligibility
            source_ids:
            - P2-S3-C9
            - P2-S3-C10
            - P4-S1-C13
            - P4-S1-C14
            - P4-S1-C15
            - P4-S1-C16
            - P4-S3-C5
            - P4-S3-C6
            - P4-S3-C7
            - P4-S3-C8
            - P5-S1-C8
            reason: Runaway selection (>8 passages); entire slot requires source review
          - slot: outcome_definition
            source_ids:
            - P5-S1-C9
            - P5-S1-C10
            - P5-S2-C3
            - P5-S2-C6
            - P5-S2-C7
            - P5-S2-C9
            - P5-S2-C10
            - P5-S2-C12
            - P5-S2-C13
            - P5-S2-C14
            - P5-S3-C3
            - P5-S3-C4
            - P6-S1-C3
            - P6-S1-C4
            - P6-S1-C5
            - P6-S1-C6
            - P6-S1-C7
            - P6-S1-C8
            - P6-S1-C9
            - P6-S1-C10
            - P6-S1-C11
            - P6-S2-C10
            - P6-S2-C11
            - P6-S2-C12
            - P6-S2-C13
            - P7-S1-C2
            - P7-S2-C1
            - P8-S1-C8
            - P8-S1-C9
            - P8-S1-C10
            - P8-S1-C11
            - P8-S1-C12
            - P8-S1-C13
            - P8-S2-C5
            - P8-S2-C6
            - P8-S2-C7
            - P8-S2-C8
            - P8-S2-C9
            - P8-S2-C10
            - P8-S2-C11
            - P8-S2-C12
            - P8-S2-C13
            - P8-S3-C3
            - P8-S3-C4
            - P8-S3-C5
            - P8-S3-C6
            - P8-S3-C7
            - P8-S3-C8
            - P8-S3-C9
            - P8-S3-C10
            - P9-S1-C8
            - P9-S1-C9
            - P9-S1-C10
            - P9-S2-C2
            - P9-S2-C3
            - P9-S2-C4
            - P9-S2-C5
            - P9-S2-C6
            - P9-S2-C7
            - P9-S2-C8
            - P9-S2-C9
            - P9-S3-C2
            - P9-S3-C3
            - P9-S3-C4
            - P9-S3-C5
            - P9-S3-C6
            - P9-S3-C7
            - P9-S3-C8
            - P9-S3-C9
            - P9-S3-C10
            - P9-S3-C11
            - P9-S3-C12
            - P9-S4-C4
            - P9-S4-C5
            - P9-S4-C6
            - P9-S4-C7
            - P9-S4-C8
            - P9-S4-C9
            - P9-S4-C10
            - P9-S4-C11
            reason: Runaway selection (>8 passages); entire slot requires source review
          - slot: limitations
            source_ids:
            - P10-S3-C3
            - P10-S3-C4
            - P10-S3-C5
            - P10-S3-C6
            - P10-S3-C7
            - P10-S3-C8
            - P10-S3-C9
            - P10-S3-C10
            - P10-S3-C11
            - P10-S4-C2
            - P10-S4-C3
            - P10-S4-C4
            - P10-S4-C5
            - P10-S4-C6
            - P10-S4-C7
            - P10-S4-C8
            - P10-S4-C9
            - P10-S4-C10
            - P10-S4-C11
            - P10-S4-C12
            - P11-S1-C1
            - P11-S1-C2
            - P11-S1-C4
            - P11-S1-C5
            - P11-S1-C6
            - P11-S1-C7
            - P11-S1-C8
            - P11-S1-C9
            - P11-S1-C10
            - P11-S1-C11
            - P12-S1-C3
            reason: Runaway selection (>8 passages); entire slot requires source review
          empty_frame_slots_require_confirmation:
          - eligibility
          - outcome_definition
          - limitations
          - personal_factors
          - tested_personal_effects
          - explicitly_not_adjusted
          unclassified_extraction_ids: []
          table_review_required:
          - TABLE-1-page-4-1
          - TABLE-2-page-4-2
          - TABLE-3-page-5-3
          - TABLE-4-page-6-4
          - TABLE-5-page-7-5
          - TABLE-5-page-8-6
          - TABLE-6-page-11-7
          - TABLE-6-page-11-8
          unlinked_tables:
          - TABLE-1-page-4-1
          - TABLE-2-page-4-2
          - TABLE-3-page-5-3
          - TABLE-4-page-6-4
          - TABLE-5-page-7-5
          - TABLE-5-page-8-6
          - TABLE-6-page-11-7
          - TABLE-6-page-11-8
          source_anomalies: []
          visual_review_required:
            scope: All main-paper figures and table crops
            note: Automatic crops and matching transcriptions do not certify visual completeness. Figures are not automatically interpreted.
            caption_candidate_units:
            - P2-S3
            - P2-S4
            - P3-S1
          approval: Not performed. Structural checks and model selections do not establish semantic correctness.
        candidate_discovery:
          model: gemma4:31b
          model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
          pdf_sha256: ccd84f115f464675d9dc92bc5df1deabc67b02a9eb42f72849745a981dc374d8
          source_review: _compare/relationships-2026-11-16/review-current/Durfee2021
          source_status_sha256: 3f761cdd0e697255bda542b600e23688e5810cf3517c0e413f6ea2cb3dcfa017
          code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
          version: candidate-inventory-v1
        coverage:
        - source_id: P1-S1-C10
          disposition: background_or_descriptive
          result_indexes: []
          reason: Describes general profile characteristics of lesions across timeframes without a specific relationship.
        - source_id: P1-S1-C11
          disposition: represented
          result_indexes:
          - 0
          - 1
          reason: Establishes the relationship between RH dorsal/ventral regions and production/comprehension impairments.
        - source_id: P4-S1-C10
          disposition: background_or_descriptive
          result_indexes: []
          reason: Reports total number of articles yielded by search.
        - source_id: P4-S1-C11
          disposition: background_or_descriptive
          result_indexes: []
          reason: Reports number of articles after duplicate removal.
        - source_id: P4-S1-C12
          disposition: background_or_descriptive
          result_indexes: []
          reason: Reports number of articles removed for lack of prosody or RH damage.
        - source_id: P4-S1-C13
          disposition: background_or_descriptive
          result_indexes: []
          reason: Reports number of articles excluded due to poor methodological strength.
        - source_id: P4-S1-C14
          disposition: background_or_descriptive
          result_indexes: []
          reason: Reports number of articles excluded due to inability to determine localization.
        - source_id: P4-S1-C15
          disposition: background_or_descriptive
          result_indexes: []
          reason: Reports number of articles removed for inadequate imaging or control information.
        - source_id: P4-S2-C2
          disposition: background_or_descriptive
          result_indexes: []
          reason: Reports inter-rater reliability of quality ratings.
        - source_id: P4-S2-C3
          disposition: background_or_descriptive
          result_indexes: []
          reason: Reports inter-rater reliability of quality ratings.
        - source_id: P4-S2-C4
          disposition: background_or_descriptive
          result_indexes: []
          reason: Reports inter-rater reliability of quality ratings.
        - source_id: P6-S2-C4
          disposition: represented
          result_indexes:
          - 13
          reason: Reports large effect sizes for RH vs LH lesions on recognition tasks.
        - source_id: P6-S2-C5
          disposition: represented
          result_indexes:
          - 14
          reason: Reports trivial effect sizes for specific lesion regions vs others.
        - source_id: P6-S2-C10
          disposition: background_or_descriptive
          result_indexes: []
          reason: States the number of studies associating acute stroke with production impairment.
        - source_id: P8-S4-C10
          disposition: background_or_descriptive
          result_indexes: []
          reason: Explains the calculation method for odds ratios.
        - source_id: P8-S5-C2
          disposition: background_or_descriptive
          result_indexes: []
          reason: Explains the calculation method for odds ratios.
        - source_id: P9-S1-C1
          disposition: represented
          result_indexes:
          - 27
          reason: Reports higher likelihood of expressive aprosodia for frontal lobe, insula, and white matter pathways.
        - source_id: P9-S1-C2
          disposition: repeated
          result_indexes:
          - 27
          reason: Restates the association of white matter pathways with expressive aprosodia.
        - source_id: P9-S1-C3
          disposition: represented
          result_indexes:
          - 28
          reason: Reports higher likelihood of receptive aprosodia for temporal/occipital lobes and subcortical nuclei.
        - source_id: P9-S1-C4
          disposition: represented
          result_indexes:
          - 29
          reason: Reports similar ratios of receptive vs expressive aprosodia for parietal damage.
        - source_id: P9-S1-C9
          disposition: repeated
          result_indexes:
          - 27
          reason: Restates that frontal regions are more consistently observed with expressive over receptive aprosodia.
        - source_id: P9-S1-C10
          disposition: repeated
          result_indexes:
          - 28
          reason: Restates that receptive aprosodia is more often associated with posterior damage.
        - source_id: P9-S2-C2
          disposition: repeated
          result_indexes:
          - 28
          reason: Restates the association of receptive aprosodia with posterior damage.
        - source_id: P9-S2-C8
          disposition: repeated
          result_indexes:
          - 27
          reason: Restates that frontal RH regions were more often associated with expressive aprosodia.
        - source_id: P9-S3-C4
          disposition: repeated
          result_indexes:
          - 27
          reason: Restates that white matter pathways were more likely associated with expressive over receptive aprosodia.
        - source_id: P9-S3-C5
          disposition: background_or_descriptive
          result_indexes: []
          reason: Cites specific study (Patel et al., 2018) regarding white matter pathways.
        - source_id: P9-S4-C4
          disposition: repeated
          result_indexes:
          - 29
          reason: Restates that neither aprosodia type occurred more frequently for parietal lobe.
        - source_id: P9-S4-C5
          disposition: repeated
          result_indexes:
          - 29
          reason: Provides the specific article counts for parietal damage.
        - source_id: P9-S4-C6
          disposition: background_or_descriptive
          result_indexes: []
          reason: Discusses the role of the supramarginal gyrus as an integrative region.
        - source_id: P9-S4-C9
          disposition: repeated
          result_indexes:
          - 28
          reason: Restates that temporal regions were associated with receptive over expressive aprosodia.
        - source_id: P9-S4-C10
          disposition: background_or_descriptive
          result_indexes: []
          reason: Discusses the role of the posterior superior temporal gyrus.
        - source_id: P9-S4-C11
          disposition: background_or_descriptive
          result_indexes: []
          reason: Compares frequency of basal ganglia involvement to other nuclei.
        - source_id: P9-S5-C1
          disposition: background_or_descriptive
          result_indexes: []
          reason: Continuation of sentence regarding basal ganglia.
        - source_id: P9-S5-C3
          disposition: background_or_descriptive
          result_indexes: []
          reason: Posits the role of basal ganglia in both expression and recognition.
        - source_id: P10-S1-C5
          disposition: background_or_descriptive
          result_indexes: []
          reason: States that limited data does not support a review of specific cognitive processes at this time.
        - source_id: P10-S1-C6
          disposition: background_or_descriptive
          result_indexes: []
          reason: Introduces the topic of longitudinal stroke recovery.
        - source_id: P10-S3-C11
          disposition: background_or_descriptive
          result_indexes: []
          reason: Discusses the number of articles reporting perfusion information.
        - source_id: P11-S2-C2
          disposition: background_or_descriptive
          result_indexes: []
          reason: Reports the proportion of articles reporting concomitant motor/cognitive deficits.
        - source_id: P11-S2-C3
          disposition: background_or_descriptive
          result_indexes: []
          reason: Describes the variation in reported post-stroke communication abilities.
        - source_id: P11-S2-C7
          disposition: background_or_descriptive
          result_indexes: []
          reason: Describes co-occurrence of receptive affective aprosodia with other deficits.
        - source_id: P12-S1-C1
          disposition: background_or_descriptive
          result_indexes: []
          reason: Continuation of sentence regarding co-occurrence of deficits.
        - source_id: P12-S1-C3
          disposition: repeated
          result_indexes:
          - 0
          - 1
          reason: Conclusion restating the essential roles of frontal, temporal, and parietal regions.
        unresolved_coverage:
        - source_id: P9-S5-C1
          disposition: unresolved
          reason: Coverage source was not requested or was repeated; not accepted as coverage
        - source_id: P9-S5-C3
          disposition: unresolved
          reason: Coverage source was not requested or was repeated; not accepted as coverage
        - source_id: P9-S4-C12
          disposition: unresolved
          reason: Discovery omitted this passage
        pending_source_ids:
        - P1-S1-C10
        - P4-S1-C10
        - P4-S1-C11
        - P4-S1-C12
        - P4-S1-C13
        - P4-S1-C14
        - P4-S1-C15
        - P4-S2-C2
        - P4-S2-C3
        - P4-S2-C4
        - P6-S2-C10
        - P8-S4-C10
        - P8-S5-C2
        - P9-S1-C2
        - P9-S1-C9
        - P9-S1-C10
        - P9-S2-C2
        - P9-S2-C8
        - P9-S3-C4
        - P9-S3-C5
        - P9-S4-C4
        - P9-S4-C5
        - P9-S4-C6
        - P9-S4-C9
        - P9-S4-C10
        - P9-S4-C11
        - P9-S4-C12
        - P10-S1-C5
        - P10-S1-C6
        - P10-S3-C11
        - P11-S2-C2
        - P11-S2-C3
        - P11-S2-C7
        - P12-S1-C1
        - P12-S1-C3
        pending_policy: Every result passage without direct candidate evidence remains pending, including model-labelled background and restatements; those labels never certify completeness.
        tables_requiring_review:
        - TABLE-1-page-4-1
        - TABLE-2-page-4-2
        - TABLE-3-page-5-3
        - TABLE-4-page-6-4
        - TABLE-5-page-7-5
        - TABLE-5-page-8-6
        - TABLE-6-page-11-7
        - TABLE-6-page-11-8
        paper_complete: false
        approved: false
        policy: New candidates require independent source checks; coverage dispositions are model suggestions. No original outputs changed.
      study_frame:
        slots:
          analysed_sample:
          - P1-S1-C9
          recruited_sample:
          - P1-S1-C8
          eligibility: []
          imaging_provenance:
          - P4-S2-C7
          - P4-S2-C9
          - P4-S2-C11
          - P5-S1-C4
          - P10-S3-C6
          - P10-S3-C7
          - P10-S3-C9
          - P10-S3-C11
          imaging_timing:
          - P4-S2-C5
          - P4-S2-C7
          - P4-S2-C11
          - P5-S1-C4
          - P10-S1-C7
          - P10-S1-C10
          - P10-S3-C7
          - P10-S3-C9
          outcome_timing:
          - P4-S2-C5
          - P4-S2-C10
          - P5-S1-C6
          - P10-S1-C7
          - P10-S1-C10
          - P10-S1-C11
          - P10-S1-C12
          outcome_definition: []
          validation:
          - P9-S1-C5
          analysis_restrictions:
          - P4-S2-C6
          - P4-S2-C10
          - P4-S3-C4
          - P5-S1-C8
          - P8-S4-C7
          - P10-S3-C3
          dependent_variable_statement:
          - P5-S2-C7
          - P5-S2-C8
          - P6-S2-C6
          - P6-S2-C7
          limitations: []
          personal_factors: []
          tested_personal_effects: []
          adjustment_roles:
          - P5-S2-C7
          - P6-S3-C2
          - P8-S1-C2
          - P8-S1-C3
          - P8-S3-C4
          - P9-S4-C6
          explicitly_not_adjusted: []
          descriptive_personal_factors:
          - P2-S4-C10
          - P5-S3-C5
          - P11-S2-C2
        outcome_type: both_reported
        imaging_vs_outcome: mixed
        validation_type: none_described
        held_selections:
        - slot: dependent_variable_statement
          source_id: P6-S2-C10
          reason: Requires a Methods outcome definition; model selection retained for inspection only
        - slot: dependent_variable_statement
          source_id: P6-S2-C11
          reason: Requires a Methods outcome definition; model selection retained for inspection only
        - slot: dependent_variable_statement
          source_id: P6-S2-C12
          reason: Requires a Methods outcome definition; model selection retained for inspection only
        - slot: dependent_variable_statement
          source_id: P6-S2-C13
          reason: Requires a Methods outcome definition; model selection retained for inspection only
        - slot: dependent_variable_statement
          source_id: P8-S1-C2
          reason: Requires a Methods outcome definition; model selection retained for inspection only
        - slot: dependent_variable_statement
          source_id: P8-S1-C3
          reason: Requires a Methods outcome definition; model selection retained for inspection only
        - slot: dependent_variable_statement
          source_id: P8-S3-C4
          reason: Requires a Methods outcome definition; model selection retained for inspection only
        - slot: dependent_variable_statement
          source_id: P8-S3-C5
          reason: Requires a Methods outcome definition; model selection retained for inspection only
        - slot: dependent_variable_statement
          source_id: P9-S4-C6
          reason: Requires a Methods outcome definition; model selection retained for inspection only
        - slot: eligibility
          source_ids:
          - P2-S3-C9
          - P2-S3-C10
          - P4-S1-C13
          - P4-S1-C14
          - P4-S1-C15
          - P4-S1-C16
          - P4-S3-C5
          - P4-S3-C6
          - P4-S3-C7
          - P4-S3-C8
          - P5-S1-C8
          reason: Runaway selection (>8 passages); entire slot requires source review
        - slot: outcome_definition
          source_ids:
          - P5-S1-C9
          - P5-S1-C10
          - P5-S2-C3
          - P5-S2-C6
          - P5-S2-C7
          - P5-S2-C9
          - P5-S2-C10
          - P5-S2-C12
          - P5-S2-C13
          - P5-S2-C14
          - P5-S3-C3
          - P5-S3-C4
          - P6-S1-C3
          - P6-S1-C4
          - P6-S1-C5
          - P6-S1-C6
          - P6-S1-C7
          - P6-S1-C8
          - P6-S1-C9
          - P6-S1-C10
          - P6-S1-C11
          - P6-S2-C10
          - P6-S2-C11
          - P6-S2-C12
          - P6-S2-C13
          - P7-S1-C2
          - P7-S2-C1
          - P8-S1-C8
          - P8-S1-C9
          - P8-S1-C10
          - P8-S1-C11
          - P8-S1-C12
          - P8-S1-C13
          - P8-S2-C5
          - P8-S2-C6
          - P8-S2-C7
          - P8-S2-C8
          - P8-S2-C9
          - P8-S2-C10
          - P8-S2-C11
          - P8-S2-C12
          - P8-S2-C13
          - P8-S3-C3
          - P8-S3-C4
          - P8-S3-C5
          - P8-S3-C6
          - P8-S3-C7
          - P8-S3-C8
          - P8-S3-C9
          - P8-S3-C10
          - P9-S1-C8
          - P9-S1-C9
          - P9-S1-C10
          - P9-S2-C2
          - P9-S2-C3
          - P9-S2-C4
          - P9-S2-C5
          - P9-S2-C6
          - P9-S2-C7
          - P9-S2-C8
          - P9-S2-C9
          - P9-S3-C2
          - P9-S3-C3
          - P9-S3-C4
          - P9-S3-C5
          - P9-S3-C6
          - P9-S3-C7
          - P9-S3-C8
          - P9-S3-C9
          - P9-S3-C10
          - P9-S3-C11
          - P9-S3-C12
          - P9-S4-C4
          - P9-S4-C5
          - P9-S4-C6
          - P9-S4-C7
          - P9-S4-C8
          - P9-S4-C9
          - P9-S4-C10
          - P9-S4-C11
          reason: Runaway selection (>8 passages); entire slot requires source review
        - slot: limitations
          source_ids:
          - P10-S3-C3
          - P10-S3-C4
          - P10-S3-C5
          - P10-S3-C6
          - P10-S3-C7
          - P10-S3-C8
          - P10-S3-C9
          - P10-S3-C10
          - P10-S3-C11
          - P10-S4-C2
          - P10-S4-C3
          - P10-S4-C4
          - P10-S4-C5
          - P10-S4-C6
          - P10-S4-C7
          - P10-S4-C8
          - P10-S4-C9
          - P10-S4-C10
          - P10-S4-C11
          - P10-S4-C12
          - P11-S1-C1
          - P11-S1-C2
          - P11-S1-C4
          - P11-S1-C5
          - P11-S1-C6
          - P11-S1-C7
          - P11-S1-C8
          - P11-S1-C9
          - P11-S1-C10
          - P11-S1-C11
          - P12-S1-C3
          reason: Runaway selection (>8 passages); entire slot requires source review
        policy: All slots and enums remain unverified. Held selections are not evidence of absence. Original response is preserved in frame/raw.json.
      approved: false
      source_check:
        profile: core
        scope: Independent model text review of core meaning; not human approval or complete PDF verification
        binding:
          profile: core
          version: core-source-check-v3
          model: gemma4:31b
          model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
          checker_model: qwen3.8:27b
          checker_digest: 47951e4a666180bc2aedfc93c169472f2de783696fe196efbf063f5730ecf163
          host: http://localhost:11434
          pdf_sha256: ccd84f115f464675d9dc92bc5df1deabc67b02a9eb42f72849745a981dc374d8
          review_sha256: 3c3e749bbeb85252e97e4dec8e8dbb5075c4d0e2ddb45ff086cbc832ee2697ee
          code_sha256: c4650d24fa3e36e6f317cb65cc7626277a28936a7cdf5d07248d4b1e5bfa09aa
          source_helpers_sha256: e0e0f295e5efa1fdb4e9e8c84ca491d062df3aefe8ca8b4d9ca85fcb6d4c9082
          converter_sha256: 048f1e35905528676837a00b1b2406b1c97cb1eb47c48d63f121a5c00cc0afeb
          table_helpers_sha256: 78e562e9725fc484d6a12279ea710856dfd1d9aa13ee178d0358e9c0acdd2c8c
          mapper_budget: 2500
          reviewer_budget: 1600
          approved: false
          visual:
            models: &id003
            - gemma4:31b
            - qwen3.8:27b
            digests: &id004
            - 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
            - 47951e4a666180bc2aedfc93c169472f2de783696fe196efbf063f5730ecf163
            code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
            layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
        approved: false
        core_review:
          own_result_source_ids:
          - P8-S1-C2
          source_result: In a study of acute stroke patients (Patel et al., 2018), percent damage to the right supramarginal gyrus and superior longitudinal fasciculus (SLF) were identified as independent predictors of the coefficient of variation in fundamental frequency (CoVF0).
          result_status: detected
          patient_measurement: template_lesion_overlap
          checks:
            analysis_identity:
              answer: fits
              reason: The source P8-S1-C2 explicitly identifies 'percent damage to right supramarginal gyrus and SLF' as 'independent predictors of CoVF0'. The proposed core correctly identifies this specific analysis and its outcome.
              source_ids:
              - P8-S1-C2
            direction:
              answer: fits
              reason: The source states these factors are 'independent predictors', implying a statistically detected association. The proposed core uses 'likely' direction, which is a reasonable qualitative representation of a predictive relationship without specifying the sign (positive/negative) which is not explicitly detailed in the snippet, but the existence of the association is preserved.
              source_ids:
              - P8-S1-C2
            construct:
              answer: fits
              reason: The exposure is correctly identified as damage to the right supramarginal gyrus and SLF. The outcome is CoVF0. The method is described as 'LSM' (Lesion-Symptom Mapping) in the core, which aligns with the source's context of acute lesion-deficit associations (P4-S2-C8) and the use of 'percent damage' (a metric derived from overlaying lesions on anatomical maps). The patient measurement is template_lesion_overlap because 'percent damage' to specific named structures (SMG, SLF) implies overlaying patient lesions onto reference tract/region maps, rather than patient-specific diffusion tractography or voxel-wise tissue analysis.
              source_ids:
              - P8-S1-C2
              - P4-S2-C8
            qualifications:
              answer: fits
              reason: The core includes the qualification 'measured as independent predictors', which accurately reflects the source text 'Independent predictors of CoVF0 included...'. It also notes the context of a systematic review. No material qualifiers are lost.
              source_ids:
              - P8-S1-C2
            missing_material_caveat:
              answer: fits
              reason: The source P8-S1-C2 is a concise statement of a finding. While P8-S1-C4 mentions that ventral stream regions were *not* associated, this is a separate finding. The core focuses on the positive finding for SMG/SLF. No material caveat regarding the specific SMG/SLF finding is omitted from the source snippet provided.
              source_ids:
              - P8-S1-C2
          optional_pending:
          - Specific statistical values (p-values, beta coefficients) for the SMG/SLF prediction of CoVF0 are not transcribed in the source snippet.
          - The specific direction of the effect (whether damage increases or decreases CoVF0) is not explicitly stated in P8-S1-C2, only that it is a predictor.
          verdict: draft
          reason: All five core checks fit the source.
          material_issues: []
        pending_details:
        - Detailed statistics, atlas/reference-space and structured confounder metadata not transcribed.
        - Recovery phase is not classified; use the reported timing words.
        - Evidence-strength rating is a conservative draft placeholder pending human review.
        - Specific statistical values (p-values, beta coefficients) for the SMG/SLF prediction of CoVF0 are not transcribed in the source snippet.
        - The specific direction of the effect (whether damage increases or decreases CoVF0) is not explicitly stated in P8-S1-C2, only that it is a predictor.
        normalizations:
        - field: bucket
          original: predictors
          action: route_from_kind
          value: regions
        analysis_identity:
          id: R015
          exposure:
            text: right supramarginal gyrus and SLF damage
          outcome:
            text: coefficient of variation in fundamental frequency (CoVF0)
          analysis_label: Acute lesion analysis (Patel et al., 2018)
          relation: association
          evidence_ids:
          - P8-S1-C2
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
            pdf_sha256: ccd84f115f464675d9dc92bc5df1deabc67b02a9eb42f72849745a981dc374d8
            source_review: _compare/relationships-2026-11-16/review-current/Durfee2021
            source_status_sha256: 3f761cdd0e697255bda542b600e23688e5810cf3517c0e413f6ea2cb3dcfa017
            code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
            version: candidate-inventory-v1
        paper_complete: false
        visual_prose_readings:
          P4-S2-C5:
            binding:
              version: prose-images-v14
              code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
              pdf_sha256: ccd84f115f464675d9dc92bc5df1deabc67b02a9eb42f72849745a981dc374d8
              layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
              anchor_sha256: 0eaaa395a575d721b38ebceae3c90d8cc50833e5dd2cc0c636c505472f0424f0
              exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
              source_id: P4-S2-C5
              page: 4
              text_layer_sha256: 0eaaa395a575d721b38ebceae3c90d8cc50833e5dd2cc0c636c505472f0424f0
              models: *id003
              model_digests: *id004
              host: http://localhost:11434
            status: agreed_model_transcription
            original_text: "Time post-stroke and brain imaging considerations \nResults are divided into studies of patients with acute stroke (<1 \nweek) versus those with subacute (1 week–3 months) or chronic (>3 \nmonths) because different approaches to brain imaging and mapping are \nneeded depending on the time post-onset at which patients are studied."
            anchor_text: "Time post-stroke and brain imaging considerations \nResults are divided into studies of patients with acute stroke (<1 \nweek) versus those with subacute (1 week–3 months) or chronic (>3 \nmonths) because different approaches to brain imaging and mapping are \nneeded depending on the time post-onset at which patients are studied."
            excluded_fragments: []
            image_sha256: abd40fe946cae34243f54279746bc0909447564f2403d813139a54a3ff85e3b7
            transcription: 'Time post-stroke and brain imaging considerations


              Results are divided into studies of patients with acute stroke (<1 week) versus those with subacute (1 week–3 months) or chronic (>3 months) because different approaches to brain imaging and mapping are needed depending on the time post-onset at which patients are studied'
        remaining:
        - Human PDF review and approval
        - Pending metadata enrichment
        - Main Results, figures and tables completeness check
    reviewer_marks:
    - id: relationship-source-check
      page: 8
      quote: "Independent predictors of CoVF0 included age \nand percent damage to right supramarginal gyrus and SLF."
      status: pending
      by: agent:relationship-converter
      date: '2026-11-23'
      note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor roles, all qualifiers, source audit issues and main-PDF tables/figures; check missing results. This model proposal is not verified.'
  original_mapping:
    decision: draft
    reason: The source describes a specific finding from a study of acute stroke patients where percent damage to the right supramarginal gyrus and SLF were independent predictors of CoVF0 (a measure of expressive prosody).
    bucket: predictors
    entity_id: right_smg_slf_damage
    name: right supramarginal gyrus and SLF damage
    kind: network
    predictor_type: imaging_metric
    definition: percent damage to the right supramarginal gyrus and superior longitudinal fasciculus (SLF)
    assessment:
    - coefficient of variation in fundamental frequency (CoVF0)
    target: covf0
    target_kind: impairment
    claim: percent damage to the right supramarginal gyrus and SLF were independent predictors of the coefficient of variation in fundamental frequency (CoVF0).
    direction: likely
    method: LSM
    relationship: correlational
    therapy: null
    sample_n: null
    population: patients with acute stroke
    timing: acute (<1 week post-stroke)
    qualifications:
    - measured as independent predictors
    limitations:
    - finding is part of a systematic review of 11 articles
    optional_pending: []
    evidence_quality: cohort
    passages:
    - source_id: P8-S1-C2
      supports: claim
    - source_id: P4-S2-C5
      supports: sample
    - source_id: P4-S2-C7
      supports: method
  original_attempt:
    binding:
      profile: core
      version: core-source-check-v3
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      checker_model: qwen3.8:27b
      checker_digest: 47951e4a666180bc2aedfc93c169472f2de783696fe196efbf063f5730ecf163
      host: http://localhost:11434
      pdf_sha256: ccd84f115f464675d9dc92bc5df1deabc67b02a9eb42f72849745a981dc374d8
      review_sha256: 3c3e749bbeb85252e97e4dec8e8dbb5075c4d0e2ddb45ff086cbc832ee2697ee
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
    proposal: R015
    status: draft
    reason: All five core checks fit the source.
    material_issues: []
    path: drafts/regions/right_smg_slf_damage__Durfee2021__R015.md
    seconds_this_run: 81.01624691599864
  source_check:
    profile: agent-repair
    scope: Agent source reconstruction; original model reviews do not certify the changed record. No independent model pass or human approval.
    approved: false
    paper_complete: false
    binding:
      pdf_sha256: ccd84f115f464675d9dc92bc5df1deabc67b02a9eb42f72849745a981dc374d8
      original_mapping_sha256: 773fe90903961e0cdbb2e0c53cb21d7741142d0ba29cd099bdb696524a1b2452
      original_status_sha256: e817e181ff85a2137e8915fd9bf4d14eb5504973cff5dbb456a81e8e886bd5ad
      evidence_sha256: 1a2ffa6ce12653b1a48461fd815432d7cacdf039f7d80229543a34243f44b298
    publication_correction:
      by: agent:source-repair
      date: '2026-11-26T02:05:16.806224+00:00'
      pdf_pages:
      - 1
      - 2
      - 5
      - 6
      - 7
      - 8
      - 9
      - 10
      note: Reclassified as a secondary review report, explicitly attributing the result to Patel et al. (2018). This is not a new primary sample or independent replication; quantitative estimates and study-level attribution require human verification against the primary publication.
      approved: false
      audit: logs/publication/draft-repairs-2026-11-26-round2.json
    remaining:
    - Human source review and approval
    - Full paper completeness review
reviewer_marks:
- id: relationship-source-check
  page: 8
  quote: "Independent predictors of CoVF0 included age \nand percent damage to right supramarginal gyrus and SLF."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-23'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor roles, all qualifiers, source audit issues and main-PDF tables/figures; check missing results. This model proposal is not verified.'
- id: source-repair-round2
  status: pending
  by: agent:source-repair
  date: '2026-11-26'
  note: Reclassified as a secondary review report, explicitly attributing the result to Patel et al. (2018). This is not a new primary sample or independent replication; quantitative estimates and study-level attribution require human verification against the primary publication.
---

# Source review required

This repaired draft remains unapproved. Original outputs and review provenance are preserved.
