---
id: wernickes_aphasia
name: Wernicke's aphasia
kind: impairment
findings:
- id: f1
  target: sentence_comprehension
  target_kind: impairment
  claim: Patients with Wernicke's aphasia performed worst on all subtests of the CYCLE-R
    and differed from each of the non-aphasic groups on all subtests.
  direction: unlikely
  relationship: correlational
  method: behavioral_only
  sample:
    n: 64
    population: Chronic left hemisphere stroke patients
    phase: not_reported
    time_post_onset: Chronic phase (mean 4.8 years post onset)
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Comparison is based on average percent scores for each aphasia type
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Chronic aphasia classification determined by the Western
    Aphasia Battery (WAB). Highest scores for this group were seen on the Possession
    subtest. Additional metadata has not been transcribed; review the pending-field
    flags before approval. PDF image reading (P5-S1-C3, two-model agreement, human
    verification pending): LH patients ranged in age from 31 to 80 years (mean 61.5),
    in time post onset from the stroke from 1 to 20.5 years (mean 4.8), and in education
    from 5 to 20 years (mean 14.3) Original text-layer quotation is preserved below.
    PDF image reading (P4-S2-C6, two-model agreement, human verification pending):
    Participants


    Sixty-four left hemisphere-injured (LH) chronic stroke patients, eight right hemisphere-injured
    (RH) chronic stroke patients, and 15 neurologically normal older controls participated
    in the study Original text-layer quotation is preserved below.'
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
    - proposed_concept:sentence_comprehension
  citation: '@Dronkers2004'
  source_passages:
  - section: Original source P12-S1-C8
    page: 12
    quote: 'Patients with Wernicke’s aphasia

      performed worst on all subtests, with their highest scores seen on the Possession
      subtest.'
    supports: claim
  - section: Original source P12-S1-C12
    page: 12
    quote: 'Patients with Wernicke’s

      aphasia differed from each of the non-aphasic groups plotted in Fig. 1 on all
      subtests.'
    supports: claim
  - section: Original source P5-S1-C10
    page: 5
    quote: 'All patients were assessed with the Western Aphasia Battery (WAB; Kertesz,
      1982) to

      determine their chronic aphasia classiﬁcation.'
    supports: method
  - section: Original source P5-S1-C3
    page: 5
    quote: 'LH patients ranged in age from 31 to 80 years (mean 61.5), in time post
      onset from the

      stroke from 1 to 20.5 years (mean 4.8), and in education from 5 to 20 years
      (mean 14.3).'
    supports: sample
  - section: Original source P4-S2-C6
    page: 4
    quote: 'Participants

      Sixty-four left hemisphere-injured (LH) chronic stroke patients, eight right
      hemi-

      sphere-injured (RH) chronic stroke patients, and 15 neurologically normal older
      controls

      participated in the study.'
    supports: sample
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-23'
relationship_review:
  paper: Dronkers2004
  proposal_id: R023
  review_status_sha256: 00c94fd463b4d9ce603080b76b83135e97e55107028edcee9312b46d7dcfd8cf
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 98dc43d10fb41da63e9a1017bd5ea1a046b22a793633e774c539f6e2d4b2a4bc
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 98dc43d10fb41da63e9a1017bd5ea1a046b22a793633e774c539f6e2d4b2a4bc
        A/passages.json: a377360ada7954bda2919c89f3484d31c97025df8d2ac06bbf5199f11378b76b
        A/raw.json: a3b7e3ca4bb6e32962b2564d6d105a46a7d3780ce9af8e8554f2e80d16682840
        A/source-units.json: 1bd8c991e3d8cc2e1a9a75ec2b2a558d719cf2a9ee4815c1d50f668d7ac06732
        A/full-source-units.json: 9923e498444d96013d6ad7ed15a6fd623d3241c493e6572e701d5346159c26b0
        A/meta.json: 75e525f9bd0938bbd03fb58b42fa76648c5ee4f22a5f16824368c39e13d1b7ad
        A/table-images/page-16.png: 6932c396e53fa8eae086b3a6ba69c9766fdd1e25ffead0b6bb3c48f4673a8293
        A/table-images/TABLE-2-page-9-1.png: 7d1850d4b2e4cbbdd6512af94d9ae1d1ed2160ac2ecfac60d713e56c109baf7f
        A/table-images/TABLE-4-page-16-2.png: 01c6bdf2fd454716826792332a967671bb389d5da0cabfe88b9fd390a2fc340c
        A/table-images/TABLE-3-page-16-1.png: abdd425d54aad81e3d994ad8bc15b2f3326f0f1d218ca31a5162df0b7c1901e7
        A/table-images/TABLE-1-page-6-1.png: 97514560bbebd967d299ccdca179943d1e097e41f8eb7512cdfea5134d4f103b
        A/table-images/page-6.png: a0dd68c8d0a07a3b860b1dfcf66f01d8b22254a33d78f7712975801f5388cbba
        A/table-images/TABLE-1-page-8-1.png: 92ce1c18a177c49ec8da32fc07ad55eb8e55944f44e93dd7b0240f49526705ca
        A/table-images/page-9.png: 3c2ddf87ce75403658051d0f124917658d2a9997d9f7e8efaf4adad3dac8e237
        A/table-images/page-8.png: 06688e2fb17a00b29450ed9f5012acb5aa3a8ce82a743c63bd70c5c2949ef017
        A/table-images/manifest.json: 03886085b5cc0cb2236ffb4e6924bb10293385794117b207d2314b8711b89516
        A/clauses/window-11/raw.json: 439880a8392a67ff55f0bcbfa66131777840b9e0d5d48de25462294680744930
        A/clauses/window-11/prompt.txt: f0563f49eaf2c446345bc6e05ca1757a8a0bbb9edf23c0bf8eefd295c75e1a24
        A/clauses/window-11/meta.json: 12ad04fcfe53304916b9605e2fe9fcbd6b8bb595c9512c55c90352af430ff764
        A/clauses/window-10/raw.json: b8c9ca44b2e0a55437e1d2bebf13274b97e18c09779fc1c7f61dfac3d89a0c3e
        A/clauses/window-10/prompt.txt: 7d6648cd797c163d79b4f34bbaa0b0a4c420ae84d4918923dbc190327322098c
        A/clauses/window-10/meta.json: f98c05b20b34cc929023b1af4fd0c052c3ffd067d43f1a727a7f15b13dcc1114
        A/clauses/window-03/raw.json: f659a4203e8bf370bde543c0ca99b29c8f9b20189821b5f6596dc137998a1ad9
        A/clauses/window-03/prompt.txt: 6cd701372d4db0132f50268c5f7ee73432cda79c54984bcbe56b715ce18f5b65
        A/clauses/window-03/meta.json: ccedecc3797535806b50e2a5f15c833ed14ad75970047a291f08b2d73c82f836
        A/clauses/window-04/raw.json: 64279db6ada1f2cad683c7a8f306d793aff0ee2681131ad3064991ed54571030
        A/clauses/window-04/prompt.txt: 7e7e91f3914aae3a08227288ea34f50d97a120f9b2622c8f90529ff1b13421db
        A/clauses/window-04/meta.json: 3582b05fcd28cfb8267ef5f412b0bbd907da8e4c118d43d53c74f4bd7ce3edce
        A/clauses/window-05/raw.json: ccd1f7873f52d14fe0b59d395f8805f13254fcfcf00c5f0b2cf9799d83614acf
        A/clauses/window-05/prompt.txt: 04f8db7e91c40b2581fbe6ae51dcc17152e4fdaf2aff32b537b27c266f7a8e65
        A/clauses/window-05/meta.json: 3bf57fcfc3b12df7d4bc67c88a30cd4dba932cf38fea5395b5fa3a1b02b52789
        A/clauses/window-02/raw.json: ea9fe646bfcc96ca23ba23b9eb7d1673c7ad830656fb06b44b05ee020b19b285
        A/clauses/window-02/prompt.txt: 7b06900c8789c785de090bd71db2380b823a4c6cda9d9af5d8fe96e0bfef51dd
        A/clauses/window-02/meta.json: d7d68d3f634a9ee192ff8ebcc556dd20c36ad8a304c2bb67499377d6a5b5de3c
        A/clauses/window-15/raw.json: 07db754f60c46fb4c2984e2f37b931cd6e64e8fc8946c2035536083c399785a4
        A/clauses/window-15/prompt.txt: 4d0a1f116e0badd4950aff52a89d6562e3fa384995a1df19ab5f5598b69ddbc4
        A/clauses/window-15/meta.json: dae1fc0fbe06bb7ad5fbfa34311275946ea96e57f74a967ff11553accc749663
        A/clauses/window-12/raw.json: 2846001e2c234c7019406f1fc2a324e6af11072ffbeee3114461b39d44593bcf
        A/clauses/window-12/prompt.txt: ed465cf6099c0fac079305797439e8fb52214b22cf6745eb9d50330ab8feeda5
        A/clauses/window-12/meta.json: 906130ebd6a29d33f3253bc7e5bb49b4cbdfcd8bf4a831021c53a3abdac0b5f7
        A/clauses/window-13/raw.json: 8c8bfb3739c3e709167bdf16f0b8b9fb383fe783a5d7d233746af0e230e23046
        A/clauses/window-13/prompt.txt: d8659928b61ad17feff5dcd763e63f434d358dab8c15e0673d695fada80f140b
        A/clauses/window-13/meta.json: 15cc67765d8037b3ce591e8881c068dd84a340da0ffa53eaa0c2efc774049eef
        A/clauses/window-14/raw.json: cefda20252de23f3e7c13466c3dbf61aa9cf44bae6fa236e78e5351eb2c40fc8
        A/clauses/window-14/prompt.txt: 7f12f40710c94e78ab5be6397952f48a85db1757d1c22c8b78cfe4a58ef45472
        A/clauses/window-14/meta.json: 74f5ead2b497e3540e3e5376372cfd0cb56a92e49785b34b22181217ba06fa9d
        A/clauses/window-09/raw.json: d4391021427c4c03924147bdbce1e0f972ce232fbdef8cfbf66f39d128a610dd
        A/clauses/window-09/prompt.txt: 86e51d841ede02bb429e988761883f3f00dd9cff2767f98161a1e985b3c9139a
        A/clauses/window-09/meta.json: e2ce88b3614a13dd7e4b6ccce298aebfcbd67920b3d884bb9c4b944503136abe
        A/clauses/window-07/raw.json: fe958f44e4cbcf34d92e6cab4005a17f73a47dc19377f9dd0bb5e778da7db10e
        A/clauses/window-07/prompt.txt: bb9c276c92d80939baf5582eaa139b1a21d423c0c5de63a3a1d97c7502124fea
        A/clauses/window-07/meta.json: 55ca111c146f90e8234be10b8d253885b365087cf3b9077c140638ffb384edc7
        A/clauses/window-01/raw.json: 4e9c11ad80c132e5d4aac8340f93424f06d080a05aa416d3cae51491b9c11c59
        A/clauses/window-01/prompt.txt: 4731c1595f63cf7cc159ca6af8673a5b537c9b2f20ab5999451a2f2cea386371
        A/clauses/window-01/meta.json: fb48cec448777f193f828daa20c48c042a28ddd5da4f8196a42410cabfcb918b
        A/clauses/window-06/raw.json: 6be3b7d31fc55e6cb80a7e65c18fe87762161d85a02c11104d1832d1d0a3cef3
        A/clauses/window-06/prompt.txt: 691f16c8215ca6da53c2f30ea144de029529e9814e7d83a19d5a9e02e63ee35b
        A/clauses/window-06/meta.json: e05b5716f965d82e16e362b6c7eeecf8c858566644eb75a5f2942819f54d70d3
        A/clauses/window-08/raw.json: 794e07d02d6ee7e9826ec49eaefd3b2e062da6e882f56fb40c6e07cb964a4320
        A/clauses/window-08/prompt.txt: 8caae0eca774b2eb9b3226f609b8f3c20f03691e93c8dd58b0cf42f8b4ecd64e
        A/clauses/window-08/meta.json: 0ba4bdf5eacebf4287b65440b1b1e8307b96246af48e279e6f6620eb2f74c590
        A/tables/TABLE-3-page-16-4/raw.json: 5ebd79d58b425b786faefc0d4e0da1bc45d65af4865f4c028077d4e5bd3f2dd8
        A/tables/TABLE-3-page-16-4/prompt.txt: 691c7b8f88d4983b467074608713a5c5bde89659355f263c19a5c0640e3def1a
        A/tables/TABLE-3-page-16-4/meta.json: 72e293f928b8967457b5fa4debfb1880e28a5f02b67f13afe45e332286e881b4
        A/tables/TABLE-1-page-6-1/raw.json: 6f67ac57f90995b9dc9fd74709232f5d2cabc725050b57369c2d678128e036b0
        A/tables/TABLE-1-page-6-1/prompt.txt: 8dd6cae3edd3081382f78a60913bdc459d0a68b5fea4ffe2844c2372c3e3a43d
        A/tables/TABLE-1-page-6-1/meta.json: 74a3b722becdd16d77ba1a40aefd22cde6ce65ba65588606a395ee10c2c7b275
        A/tables/TABLE-4-page-16-5/raw.json: bcbb4d69a678c1fa7d1d6470a1b2f88f8234ef75fa14e3a16e387ddb1be806a1
        A/tables/TABLE-4-page-16-5/prompt.txt: 36c9b0986b8e31d26719a7b8e2b0d366fb41bdce845109dac851ecfc339d89c8
        A/tables/TABLE-4-page-16-5/meta.json: ce98fc24ec66dbf96ba343234f3082559d2e510340b14b2ecfa38d07ed5ae7cc
        A/tables/TABLE-2-page-9-3/raw.json: 71c0846f469882e7851c5463b0376136a6684e41e946e50c8d110e9571b840a6
        A/tables/TABLE-2-page-9-3/prompt.txt: aad73022c531bc2f80c1f58f34273cf0704ec1394911970314793a0b998a4b80
        A/tables/TABLE-2-page-9-3/meta.json: 70d38b7f37c6781b4ec8c5b648cd816f89794acb18cccde8d1cc202a596302b2
        A/tables/TABLE-1-page-8-2/raw.json: 1ece589c67b2d1ab90f596c2bfc21327d435159cfabd0c6e32b5999ed448661b
        A/tables/TABLE-1-page-8-2/prompt.txt: ef9e50d45ef71180ffd4e758931a38c46edd898bf8f052d02951cdc882fbf5a4
        A/tables/TABLE-1-page-8-2/meta.json: 483a9d001fb07810939920cc420bb36db3fe5f56682c51cce93174ee51675056
        B/passages.json: a377360ada7954bda2919c89f3484d31c97025df8d2ac06bbf5199f11378b76b
        B/raw.json: 909c086e667ee5e085cbccd9a821589ff5331c3faa9339d605f513a404b3cf8f
        B/source-units.json: 1bd8c991e3d8cc2e1a9a75ec2b2a558d719cf2a9ee4815c1d50f668d7ac06732
        B/full-source-units.json: 9923e498444d96013d6ad7ed15a6fd623d3241c493e6572e701d5346159c26b0
        B/meta.json: a37031941ffccbb12fe5a4b7141414dcf8ce33323000595a0b03321b5be0fa70
        B/table-images/page-16.png: 6932c396e53fa8eae086b3a6ba69c9766fdd1e25ffead0b6bb3c48f4673a8293
        B/table-images/TABLE-2-page-9-1.png: 7d1850d4b2e4cbbdd6512af94d9ae1d1ed2160ac2ecfac60d713e56c109baf7f
        B/table-images/TABLE-4-page-16-2.png: 01c6bdf2fd454716826792332a967671bb389d5da0cabfe88b9fd390a2fc340c
        B/table-images/TABLE-3-page-16-1.png: abdd425d54aad81e3d994ad8bc15b2f3326f0f1d218ca31a5162df0b7c1901e7
        B/table-images/TABLE-1-page-6-1.png: 97514560bbebd967d299ccdca179943d1e097e41f8eb7512cdfea5134d4f103b
        B/table-images/page-6.png: a0dd68c8d0a07a3b860b1dfcf66f01d8b22254a33d78f7712975801f5388cbba
        B/table-images/TABLE-1-page-8-1.png: 92ce1c18a177c49ec8da32fc07ad55eb8e55944f44e93dd7b0240f49526705ca
        B/table-images/page-9.png: 3c2ddf87ce75403658051d0f124917658d2a9997d9f7e8efaf4adad3dac8e237
        B/table-images/page-8.png: 06688e2fb17a00b29450ed9f5012acb5aa3a8ce82a743c63bd70c5c2949ef017
        B/table-images/manifest.json: 6d822f3bcea057e78389bce48b8a9802602671dd8ce92c24775d42b06547996f
        B/clauses/window-11/raw.json: 39daca769f61f635b584e95f19e4ded17cc77665690bfa6a67dc33c1047340b5
        B/clauses/window-11/prompt.txt: f0563f49eaf2c446345bc6e05ca1757a8a0bbb9edf23c0bf8eefd295c75e1a24
        B/clauses/window-11/meta.json: a3db8ca66709be252cbea5ded3e11a6aee6adf3854039ce145dcb4ec9cea8352
        B/clauses/window-10/raw.json: ec1dfd43a8bff9602f5ab8dd98420ab1f49bca030a71e39aa523818fce28e9e9
        B/clauses/window-10/prompt.txt: 7d6648cd797c163d79b4f34bbaa0b0a4c420ae84d4918923dbc190327322098c
        B/clauses/window-10/meta.json: eb90dc72545c9afb204c86ff854c0a78c99ec3ed353373f257630ca7fcce0170
        B/clauses/window-03/raw.json: 4c2c371243ac248e7ff5a031a1aa2f617e9a878c1ee1ee7ff7a4f406db40759d
        B/clauses/window-03/prompt.txt: 6cd701372d4db0132f50268c5f7ee73432cda79c54984bcbe56b715ce18f5b65
        B/clauses/window-03/meta.json: 27f78863dcf2db773cf8cdc4900a787e7664bebeed3a4ba33d51d74ed0c233ae
        B/clauses/window-04/raw.json: deae0ebb45bbf8a09d00f0506efa3a9956b2c11a25a1b96b773a77461d559332
        B/clauses/window-04/prompt.txt: 7e7e91f3914aae3a08227288ea34f50d97a120f9b2622c8f90529ff1b13421db
        B/clauses/window-04/meta.json: 33e99b7dbf79163f19c1d346b448e76a374dfecdb18794e1c68ec46d2e8059b1
        B/clauses/window-05/raw.json: bdd3a5a85f54c0ed626b4e72f96f6a71bfa81c05a1ffd36ad99e12a1691834a4
        B/clauses/window-05/prompt.txt: 04f8db7e91c40b2581fbe6ae51dcc17152e4fdaf2aff32b537b27c266f7a8e65
        B/clauses/window-05/meta.json: 8831112cca8ca6cfb82c25dbd97db63c7dad1f00ebbbc225f9379ed62db2de94
        B/clauses/window-02/raw.json: dc76d8ff64ba684d2b46679575bf0b5f610a7473e3a09a776cd4d5c4da74bff6
        B/clauses/window-02/prompt.txt: 7b06900c8789c785de090bd71db2380b823a4c6cda9d9af5d8fe96e0bfef51dd
        B/clauses/window-02/meta.json: e09daea81ca1a4c1ff9a05fad6b2cee9c345e8a097b063395115434e31b668a5
        B/clauses/window-15/raw.json: 0220fe8e139dc295da439fb2436d7afe3ce90c98da341ca72ea687e8f7553802
        B/clauses/window-15/prompt.txt: 4d0a1f116e0badd4950aff52a89d6562e3fa384995a1df19ab5f5598b69ddbc4
        B/clauses/window-15/meta.json: f3e51571ceaddfe30445ba050d03df69fa018f76dc4d84f88f6dd3a4dac68e06
        B/clauses/window-12/raw.json: 3da29580d187464c5ad734cfe32add9d13136564169b0be9b3b07d55d138c888
        B/clauses/window-12/prompt.txt: ed465cf6099c0fac079305797439e8fb52214b22cf6745eb9d50330ab8feeda5
        B/clauses/window-12/meta.json: 7b72b7339f4d09a341a6f661a2054d0a0fedf81b71193d90732b091de55f44d4
        B/clauses/window-13/raw.json: 2f6ffcbd8b16019a46139d29f78d11b3d481068142a683e900cfae70c20d600b
        B/clauses/window-13/prompt.txt: d8659928b61ad17feff5dcd763e63f434d358dab8c15e0673d695fada80f140b
        B/clauses/window-13/meta.json: 2730e304433803aacc3ae4ff38fabf765d39968ef059aba0f93651561d27833d
        B/clauses/window-14/raw.json: cf143f62d35943ee8696e8f05192e21ef4372629fb67893ca45fe92f5dcbf9e2
        B/clauses/window-14/prompt.txt: 7f12f40710c94e78ab5be6397952f48a85db1757d1c22c8b78cfe4a58ef45472
        B/clauses/window-14/meta.json: 44e20aeba787a6fe9ca5bb24724158d15eda0aac5485e1948782198b65b4f975
        B/clauses/window-09/raw.json: 90fbfebbfad1d885911ef2185228d523e2e95ec9d13605bfcd3fedf811994dfb
        B/clauses/window-09/prompt.txt: 86e51d841ede02bb429e988761883f3f00dd9cff2767f98161a1e985b3c9139a
        B/clauses/window-09/meta.json: 4cfc4cce8ca8e84fcd423df62df0e7b09ab5ea7e643ba2dccd78a2c252caab96
        B/clauses/window-07/raw.json: 30cf47cf9d1b9fb28338adb82c78f9a10007dac6add8e451fe7504178b1993ac
        B/clauses/window-07/prompt.txt: bb9c276c92d80939baf5582eaa139b1a21d423c0c5de63a3a1d97c7502124fea
        B/clauses/window-07/meta.json: f10700197ae0fa5a9a009c8b4b18344b222b2ca047d4f9702bb1a90532455986
        B/clauses/window-01/raw.json: e77a2308e1826fac5c9d0dbca84dbcc413feadedc997641601799b56f3650c66
        B/clauses/window-01/prompt.txt: 4731c1595f63cf7cc159ca6af8673a5b537c9b2f20ab5999451a2f2cea386371
        B/clauses/window-01/meta.json: 3b6dc1a1257d5e01754ceb064a48b221e0522722dccc50b50f6c481255510122
        B/clauses/window-06/raw.json: affe172cadb0ea11901215d7e29b26dc53e0117d148ebc5329ac6acb304c2a5e
        B/clauses/window-06/prompt.txt: 691f16c8215ca6da53c2f30ea144de029529e9814e7d83a19d5a9e02e63ee35b
        B/clauses/window-06/meta.json: 1515b94d73239a5d1390f627b35d5746bba2b68a0ee0e3680006216994ce4c8f
        B/clauses/window-08/raw.json: d8831974fb2214a92128de29a9d4dea934394dcef14b068c2b07d6631ea5ab9f
        B/clauses/window-08/prompt.txt: 8caae0eca774b2eb9b3226f609b8f3c20f03691e93c8dd58b0cf42f8b4ecd64e
        B/clauses/window-08/meta.json: 1354487a23079ef5f4ddfa96b8e65613c280ac07e30baec0df1efd8b113f4d98
        B/tables/TABLE-3-page-16-4/raw.json: 571e35d8c70deef82b864f8d938b47a20f83a83dd8fb717f7bcd47ad667fa906
        B/tables/TABLE-3-page-16-4/prompt.txt: 691c7b8f88d4983b467074608713a5c5bde89659355f263c19a5c0640e3def1a
        B/tables/TABLE-3-page-16-4/meta.json: b1dea7fb6c925c861977fab9962d50d820d6d48d9ad6e19c767891fa99675454
        B/tables/TABLE-1-page-6-1/raw.json: b8ab0dc76a483d8933499fecc614ed9cd88f5bebd0787d27efa2ca557678f1df
        B/tables/TABLE-1-page-6-1/prompt.txt: 8dd6cae3edd3081382f78a60913bdc459d0a68b5fea4ffe2844c2372c3e3a43d
        B/tables/TABLE-1-page-6-1/meta.json: 8daf1cbcdd236666e7159bab53d63a1d9719ddbdce3931e5c2df1054801ddef8
        B/tables/TABLE-4-page-16-5/raw.json: bcbb4d69a678c1fa7d1d6470a1b2f88f8234ef75fa14e3a16e387ddb1be806a1
        B/tables/TABLE-4-page-16-5/prompt.txt: 36c9b0986b8e31d26719a7b8e2b0d366fb41bdce845109dac851ecfc339d89c8
        B/tables/TABLE-4-page-16-5/meta.json: 0df24fd7a06268b015bd2fb26127c8fb5597da8ca11dc7f76ecc7c7ce36f561b
        B/tables/TABLE-2-page-9-3/raw.json: 58bd19d6f64a0f9b4daac5d13286b79510633c7518058eccbae73eed9b010b75
        B/tables/TABLE-2-page-9-3/prompt.txt: aad73022c531bc2f80c1f58f34273cf0704ec1394911970314793a0b998a4b80
        B/tables/TABLE-2-page-9-3/meta.json: 750352d2a8adc8f5881b02f2ccae2bacc1ca77788da0d8691191d87f18705ae0
        B/tables/TABLE-1-page-8-2/raw.json: c7899db9aacb91d1ca36f9f69a699cffbe2ff0db0e98029dc801ee431cadb11f
        B/tables/TABLE-1-page-8-2/prompt.txt: ef9e50d45ef71180ffd4e758931a38c46edd898bf8f052d02951cdc882fbf5a4
        B/tables/TABLE-1-page-8-2/meta.json: 8058ffcbee33e91e9f3fcefb357671ea763377cdd4ba30f75f7d9192dba8ecd1
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
      pdf_sha256: 98dc43d10fb41da63e9a1017bd5ea1a046b22a793633e774c539f6e2d4b2a4bc
      source_review: _compare/relationships-2026-11-16/review-current/Dronkers2004
      source_status_sha256: bcd43ef94b87ec31e7817c03ae0166da6f5ad547f642a7266ab9190a9d26faa3
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R023
    exposure:
      text: Wernicke’s aphasia vs non-aphasic groups
    outcome:
      text: all subtests
    analysis_label: Comparison of aphasia types
    relation: association
    evidence_ids:
    - P12-S1-C12
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
      pdf_sha256: 98dc43d10fb41da63e9a1017bd5ea1a046b22a793633e774c539f6e2d4b2a4bc
      source_review: _compare/relationships-2026-11-16/review-current/Dronkers2004
      source_status_sha256: bcd43ef94b87ec31e7817c03ae0166da6f5ad547f642a7266ab9190a9d26faa3
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P5-S1-C11
      - Result passage disposed without unit P5-S1-C12
      - Result passage disposed without unit P5-S1-C13
      - Result passage disposed without unit P5-S1-C14
      - Result passage disposed without unit P5-S1-C15
      - Result passage disposed without unit P5-S1-C8
      - Result passage disposed without unit P5-S1-C16
      - Result passage disposed without unit P10-S1-C14
      - Result passage disposed without unit P10-S1-C15
      - Result passage disposed without unit P10-S2-C1
      - Accounting without a linked unit P10-S2-C2
      - Accounting without a linked unit P10-S2-C3
      - Result passage disposed without unit P12-S1-C1
      - Accounting without a linked unit P12-S1-C2
      - Unaccounted source passage P12-S1-C2
      - Unaccounted source passage P10-S2-C3
      - Unaccounted source passage P10-S2-C2
      - Result passage disposed without unit P12-S1-C10
      - Accounting without a linked unit P12-S1-C12
      - Accounting without a linked unit P12-S1-C6
      - Result passage disposed without unit P12-S1-C7
      - Accounting without a linked unit P12-S1-C8
      - Accounting without a linked unit P12-S1-C9
      - Unaccounted source passage P12-S1-C12
      - Unaccounted source passage P12-S1-C9
      - Unaccounted source passage P12-S1-C6
      - Unaccounted source passage P12-S1-C8
      - Result passage disposed without unit P14-S1-C4
      - Result passage disposed without unit P17-S1-C4
      - Result passage disposed without unit P17-S1-C5
      - Result passage disposed without unit P17-S1-C6
      - Result passage disposed without unit P17-S1-C7
      - Result passage disposed without unit P17-S1-C8
      - Result passage disposed without unit P17-S1-C10
      - Accounting without a linked unit P17-S1-C12
      - Accounting without a linked unit P17-S1-C16
      - Accounting without a linked unit P17-S1-C19
      - Accounting without a linked unit P17-S2-C3
      - Accounting without a linked unit P17-S2-C6
      - Accounting without a linked unit P17-S2-C7
      - Unaccounted source passage P17-S1-C19
      - Unaccounted source passage P17-S1-C12
      - Unaccounted source passage P17-S2-C3
      - Unaccounted source passage P17-S1-C16
      - Unaccounted source passage P17-S2-C6
      - Unaccounted source passage P17-S2-C7
      - Result passage disposed without unit P18-S1-C14
      - Result passage disposed without unit P18-S2-C2
      - Result passage disposed without unit P18-S2-C3
      - Result passage disposed without unit P18-S2-C5
      - Result passage disposed without unit P18-S2-C6
      - Result passage disposed without unit P18-S2-C7
      - Result passage disposed without unit P20-S1-C3
      - Result passage disposed without unit P20-S1-C10
      - Result passage disposed without unit P20-S1-C9
      - Result passage disposed without unit P20-S2-C3
      - Accounting without a linked unit P20-S2-C6
      - Result passage disposed without unit P20-S2-C7
      - Accounting without a linked unit P20-S2-C9
      - Accounting without a linked unit P21-S1-C2
      - Result passage disposed without unit P21-S1-C9
      - Unaccounted source passage P21-S1-C2
      - Unaccounted source passage P20-S2-C9
      - Unaccounted source passage P20-S2-C6
      - Result passage disposed without unit P21-S2-C12
      - Result passage disposed without unit P22-S1-C1
      - Accounting without a linked unit P22-S2-C10
      - Accounting without a linked unit P22-S2-C9
      - Unaccounted source passage P22-S2-C9
      - Unaccounted source passage P22-S2-C10
      - Result passage disposed without unit P23-S1-C12
      - Result passage disposed without unit P23-S1-C7
      - Result passage disposed without unit P24-S1-C9
      - Result passage disposed without unit P25-S1-C10
      - Result passage disposed without unit P25-S1-C11
      - Result passage disposed without unit P25-S1-C12
      - Result passage disposed without unit P25-S1-C7
      - Result passage disposed without unit P25-S1-C8
      - Result passage disposed without unit P25-S1-C9
      - Result passage disposed without unit P25-S2-C9
      - Result passage disposed without unit P27-S2-C2
      - Result passage disposed without unit P28-S1-C5
      - Result passage disposed without unit P28-S1-C6
      - Result passage disposed without unit P28-S1-C8
      unattached_null_or_qualifier_ids:
      - P5-S1-C8
      - P5-S1-C12
      - P5-S1-C15
      - P10-S1-C15
      - P10-S2-C3
      - P10-S2-C4
      - P12-S1-C2
      - P12-S1-C9
      - P12-S1-C10
      - P17-S1-C10
      - P17-S2-C6
      - P18-S1-C14
      - P18-S2-C3
      - P18-S2-C5
      - P21-S1-C2
      - P25-S1-C11
      suppressed_nonrepresented_units: 32
      default_disposition_count_requires_completeness_check: 310
      unselected_timing_passages:
      - P1-S1-C9
      - P3-S1-C4
      - P4-S2-C6
      - P5-S1-C3
      - P5-S1-C5
      - P5-S1-C7
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P18-S1-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P3-S2-C11
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P14-S1-C4
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P14-S1-C5
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P17-S1-C2
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: analysed_sample
        source_ids:
        - P1-S1-C9
        - P1-S1-C10
        - P4-S2-C6
        - P5-S1-C3
        - P5-S1-C5
        - P5-S1-C7
        - P10-S1-C13
        - P12-S2-C5
        - P14-S1-C1
        - P15-S1-C6
        - P18-S1-C1
        - P20-S1-C2
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - analysed_sample
      - validation
      - tested_personal_effects
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-6-1
      - TABLE-1-page-8-2
      - TABLE-2-page-9-3
      - TABLE-3-page-16-4
      - TABLE-4-page-16-5
      unlinked_tables:
      - TABLE-1-page-6-1
      - TABLE-1-page-8-2
      - TABLE-2-page-9-3
      - TABLE-3-page-16-4
      - TABLE-4-page-16-5
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P10-S1
        - P10-S2
        - P11-S1
        - P12-S1
        - P13-S1
        - P14-S1
        - P15-S1
        - P18-S1
        - P19-S1
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 98dc43d10fb41da63e9a1017bd5ea1a046b22a793633e774c539f6e2d4b2a4bc
      source_review: _compare/relationships-2026-11-16/review-current/Dronkers2004
      source_status_sha256: bcd43ef94b87ec31e7817c03ae0166da6f5ad547f642a7266ab9190a9d26faa3
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C14
      disposition: represented
      result_indexes:
      - 0
      reason: Introduces the five brain regions affecting CYCLE-R performance.
    - source_id: P1-S2-C1
      disposition: represented
      result_indexes:
      - 0
      reason: Lists the five brain regions affecting CYCLE-R performance.
    - source_id: P1-S2-C2
      disposition: represented
      result_indexes:
      - 1
      reason: States Broca's and Wernicke's areas did not significantly alter comprehension.
    - source_id: P2-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Abstract/discussion speculation on word vs sentence level.
    - source_id: P3-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to prior findings from 1994/1996.
    - source_id: P3-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to prior findings from 1994/1996.
    - source_id: P5-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Demographic comparison of age and education.
    - source_id: P5-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient classification counts.
    - source_id: P5-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Clinical observation of word-finding difficulty.
    - source_id: P5-S1-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Aphasia classification counts.
    - source_id: P5-S1-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: WAB AQ score ranges.
    - source_id: P5-S1-C15
      disposition: background_or_descriptive
      result_indexes: []
      reason: RH patient aphasia status.
    - source_id: P5-S1-C16
      disposition: background_or_descriptive
      result_indexes: []
      reason: RH patient WAB AQ scores.
    - source_id: P10-S1-C14
      disposition: represented
      result_indexes:
      - 20
      reason: Comparison of aphasic vs non-aphasic performance.
    - source_id: P10-S1-C15
      disposition: background_or_descriptive
      result_indexes: []
      reason: Explanation of control group subtest administration.
    - source_id: P10-S2-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of aphasic group performance trend.
    - source_id: P10-S2-C2
      disposition: represented
      result_indexes:
      - 20
      reason: Statistical significance of aphasic vs non-aphasic performance.
    - source_id: P10-S2-C3
      disposition: represented
      result_indexes:
      - 21
      reason: Non-aphasic groups did not differ from each other.
    - source_id: P10-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Case detail for patient BRJ.
    - source_id: P12-S1-C1
      disposition: repeated
      result_indexes:
      - 20
      reason: Restatement of aphasic group difficulty.
    - source_id: P12-S1-C2
      disposition: represented
      result_indexes:
      - 21
      reason: Confirms brain injury alone (WNL/RH) did not affect performance.
    - source_id: P12-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of Anomic aphasia performance.
    - source_id: P12-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of Conduction/Broca aphasia performance.
    - source_id: P12-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation of performance range.
    - source_id: P12-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of Wernicke's aphasia performance.
    - source_id: P12-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of Global aphasia performance.
    - source_id: P12-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of unclassifiable patients.
    - source_id: P12-S1-C12
      disposition: represented
      result_indexes:
      - 22
      reason: Wernicke's aphasia differed from non-aphasic groups on all subtests.
    - source_id: P12-S1-C13
      disposition: represented
      result_indexes:
      - 23
      reason: Broca's aphasia performance differences by subtest.
    - source_id: P12-S1-C14
      disposition: represented
      result_indexes:
      - 24
      reason: Conduction aphasia performance differences by subtest.
    - source_id: P12-S2-C3
      disposition: represented
      result_indexes:
      - 25
      reason: Anomic aphasia performance differences by subtest.
    - source_id: P12-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of VLSM methodology.
    - source_id: P12-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of VLSM methodology.
    - source_id: P12-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of VLSM methodology.
    - source_id: P14-S1-C4
      disposition: represented
      result_indexes:
      - 0
      reason: Defines statistical significance threshold (t > 4.7).
    - source_id: P14-S1-C5
      disposition: represented
      result_indexes:
      - 0
      reason: Identifies five distinct regions affecting performance.
    - source_id: P14-S1-C6
      disposition: represented
      result_indexes:
      - 0
      reason: Lists the five regions.
    - source_id: P15-S1-C1
      disposition: represented
      result_indexes:
      - 0
      reason: Lists the five regions.
    - source_id: P15-S1-C2
      disposition: represented
      result_indexes:
      - 1
      reason: States Broca's and Wernicke's areas did not contribute.
    - source_id: P17-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to Table 4.
    - source_id: P17-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about five regions.
    - source_id: P17-S1-C6
      disposition: represented
      result_indexes:
      - 2
      reason: MTG importance for Possession and Simple Declaratives.
    - source_id: P17-S1-C7
      disposition: represented
      result_indexes:
      - 2
      reason: MTG lesions correlate with worse performance on these subtests.
    - source_id: P17-S1-C8
      disposition: represented
      result_indexes:
      - 2
      reason: MTG lesions correlate with worse performance on Active Voice, Double
        Embedding, Agentless Passive.
    - source_id: P17-S1-C9
      disposition: represented
      result_indexes:
      - 2
      reason: MTG not uniquely important for subsequent subtests.
    - source_id: P17-S1-C10
      disposition: represented
      result_indexes:
      - 2
      reason: MTG not uniquely important for subsequent subtests.
    - source_id: P17-S1-C12
      disposition: represented
      result_indexes:
      - 3
      reason: Anterior BA22 significance for specific subtests.
    - source_id: P17-S1-C16
      disposition: represented
      result_indexes:
      - 4
      reason: STS/BA39 significance for specific subtests.
    - source_id: P17-S1-C19
      disposition: represented
      result_indexes:
      - 5
      reason: BA46 significance for specific subtests.
    - source_id: P17-S2-C3
      disposition: represented
      result_indexes:
      - 6
      reason: BA47 significance for specific subtests.
    - source_id: P17-S2-C6
      disposition: represented
      result_indexes:
      - 7
      reason: Broca's area not important for any subtest.
    - source_id: P17-S2-C7
      disposition: represented
      result_indexes:
      - 8
      reason: Wernicke's area not significant.
    - source_id: P17-S2-C8
      disposition: represented
      result_indexes:
      - 9
      reason: White matter region significance for Double Embedding and Agentless
        Passive.
    - source_id: P17-S2-C10
      disposition: represented
      result_indexes:
      - 10
      reason: Postcentral gyrus significance for Agentless Passive.
    - source_id: P18-S1-C1
      disposition: represented
      result_indexes:
      - 10
      reason: Postcentral gyrus not found in overall analysis.
    - source_id: P18-S1-C11
      disposition: represented
      result_indexes:
      - 11
      reason: 'MTG lesions: well on Possession, poorly on others.'
    - source_id: P18-S1-C12
      disposition: represented
      result_indexes:
      - 12
      reason: 'Other four regions: passing on Possession/Simple Declaratives, failed
        complex.'
    - source_id: P18-S2-C1
      disposition: represented
      result_indexes:
      - 13
      reason: Sparing all VLSM areas barely affected performance.
    - source_id: P18-S2-C3
      disposition: represented
      result_indexes:
      - 14
      reason: 'Any VLSM lesion vs sparing all: differed on all except Possession.'
    - source_id: P18-S2-C5
      disposition: represented
      result_indexes:
      - 15
      reason: Only MTG group differed from spared group on Possession.
    - source_id: P20-S1-C3
      disposition: represented
      result_indexes:
      - 16
      reason: 'MTG lesions vs non-MTG: worse on Single Word Comprehension.'
    - source_id: P20-S1-C4
      disposition: represented
      result_indexes:
      - 17
      reason: 'MTG lesions vs non-MTG: worse on Sequential Commands and Yes/No questions.'
    - source_id: P20-S1-C7
      disposition: represented
      result_indexes:
      - 18
      reason: 'MTG lesions vs non-MTG: worse on WAB Naming.'
    - source_id: P20-S1-C8
      disposition: represented
      result_indexes:
      - 19
      reason: 'MTG lesions vs non-MTG: worse on BNT.'
    unresolved_coverage:
    - source_id: P12-S2-C6
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P12-S2-C7
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P12-S2-C8
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P18-S2-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P17-S1-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P18-S1-C14
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P18-S2-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P18-S2-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P18-S2-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P20-S1-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P20-S1-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P20-S1-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P20-S2-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P20-S2-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P20-S2-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P20-S2-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P20-S2-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P20-S2-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P21-S1-C1
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P21-S1-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P21-S1-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P21-S1-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P21-S1-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P21-S1-C12
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P21-S2-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P21-S2-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P21-S2-C12
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P22-S1-C1
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P22-S2-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P22-S2-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P22-S2-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P23-S1-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P23-S1-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P23-S1-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P23-S1-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P23-S1-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P23-S1-C12
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P24-S1-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P24-S1-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P24-S1-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P24-S1-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P25-S1-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P25-S1-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P25-S1-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P25-S1-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P25-S1-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P25-S1-C12
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P25-S2-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P26-S1-C1
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P26-S1-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P27-S1-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P27-S2-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P27-S2-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P28-S1-C1
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P28-S1-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P28-S1-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P28-S1-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P28-S1-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C14
    - P2-S1-C1
    - P3-S1-C9
    - P3-S2-C2
    - P5-S1-C8
    - P5-S1-C11
    - P5-S1-C12
    - P5-S1-C13
    - P5-S1-C14
    - P5-S1-C15
    - P5-S1-C16
    - P10-S1-C14
    - P10-S1-C15
    - P10-S2-C1
    - P10-S2-C4
    - P12-S1-C1
    - P12-S1-C5
    - P12-S1-C6
    - P12-S1-C7
    - P12-S1-C8
    - P12-S1-C9
    - P12-S1-C10
    - P14-S1-C4
    - P17-S1-C3
    - P17-S1-C4
    - P17-S1-C5
    - P17-S1-C9
    - P17-S1-C10
    - P18-S1-C1
    - P18-S1-C14
    - P18-S2-C2
    - P18-S2-C6
    - P18-S2-C7
    - P20-S1-C5
    - P20-S1-C9
    - P20-S1-C10
    - P20-S2-C3
    - P20-S2-C4
    - P20-S2-C5
    - P20-S2-C6
    - P20-S2-C7
    - P20-S2-C9
    - P21-S1-C1
    - P21-S1-C2
    - P21-S1-C9
    - P21-S1-C10
    - P21-S1-C11
    - P21-S1-C12
    - P21-S2-C10
    - P21-S2-C11
    - P21-S2-C12
    - P22-S1-C1
    - P22-S2-C8
    - P22-S2-C9
    - P22-S2-C10
    - P23-S1-C2
    - P23-S1-C3
    - P23-S1-C7
    - P23-S1-C10
    - P23-S1-C11
    - P23-S1-C12
    - P24-S1-C4
    - P24-S1-C5
    - P24-S1-C6
    - P24-S1-C9
    - P25-S1-C7
    - P25-S1-C8
    - P25-S1-C9
    - P25-S1-C10
    - P25-S1-C11
    - P25-S1-C12
    - P25-S2-C9
    - P26-S1-C1
    - P26-S1-C4
    - P27-S1-C7
    - P27-S2-C2
    - P27-S2-C3
    - P28-S1-C1
    - P28-S1-C5
    - P28-S1-C6
    - P28-S1-C7
    - P28-S1-C8
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-6-1
    - TABLE-1-page-8-2
    - TABLE-2-page-9-3
    - TABLE-3-page-16-4
    - TABLE-4-page-16-5
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample: []
      recruited_sample:
      - P1-S1-C9
      - P1-S1-C10
      - P4-S2-C6
      - P5-S1-C3
      - P5-S1-C5
      - P5-S1-C7
      eligibility:
      - P2-S1-C11
      - P4-S2-C7
      - P4-S2-C8
      - P5-S1-C2
      imaging_provenance:
      - P1-S1-C12
      - P9-S1-C7
      - P9-S1-C9
      imaging_timing:
      - P9-S1-C7
      - P9-S1-C8
      outcome_timing:
      - P10-S1-C7
      - P14-S1-C1
      - P15-S1-C6
      - P17-S1-C7
      - P17-S1-C16
      - P17-S1-C19
      - P18-S1-C1
      - P20-S1-C2
      outcome_definition:
      - P1-S1-C9
      - P5-S2-C3
      - P10-S1-C7
      - P14-S1-C1
      - P15-S1-C6
      - P18-S1-C1
      - P20-S1-C2
      validation: []
      analysis_restrictions:
      - P10-S1-C6
      - P14-S1-C2
      - P14-S1-C4
      - P14-S1-C5
      - P17-S1-C1
      dependent_variable_statement:
      - P10-S1-C7
      - P14-S1-C1
      - P15-S1-C6
      - P20-S1-C2
      limitations:
      - P21-S2-C2
      - P21-S2-C3
      - P21-S2-C4
      - P21-S2-C6
      personal_factors:
      - P5-S1-C3
      - P5-S1-C5
      - P5-S1-C7
      - P5-S1-C8
      tested_personal_effects: []
      adjustment_roles:
      - P14-S1-C4
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P5-S1-C3
      - P5-S1-C4
      - P5-S1-C5
      - P5-S1-C6
      - P5-S1-C7
      - P5-S1-C8
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: internal_cross_validation
    held_selections:
    - slot: dependent_variable_statement
      source_id: P18-S1-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P3-S2-C11
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P14-S1-C4
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P14-S1-C5
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P17-S1-C2
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: analysed_sample
      source_ids:
      - P1-S1-C9
      - P1-S1-C10
      - P4-S2-C6
      - P5-S1-C3
      - P5-S1-C5
      - P5-S1-C7
      - P10-S1-C13
      - P12-S2-C5
      - P14-S1-C1
      - P15-S1-C6
      - P18-S1-C1
      - P20-S1-C2
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
      pdf_sha256: 98dc43d10fb41da63e9a1017bd5ea1a046b22a793633e774c539f6e2d4b2a4bc
      review_sha256: 00c94fd463b4d9ce603080b76b83135e97e55107028edcee9312b46d7dcfd8cf
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
      - P12-S1-C12
      source_result: Patients with Wernicke's aphasia differed from each of the non-aphasic
        groups on all 11 CYCLE-R subtests, performing worst among the aphasic types.
      result_status: detected
      patient_measurement: non_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis (R023) and source P12-S1-C12 both refer to
            the comparison of Wernicke's aphasia patients against non-aphasic groups
            across all CYCLE-R subtests. This is a distinct behavioral group comparison,
            separate from the VLSM lesion-symptom mapping analysis.
          source_ids:
          - P12-S1-C12
          - P12-S1-C3
        direction:
          answer: fits
          reason: The source explicitly states that Wernicke's patients 'differed
            from each of the non-aphasic groups... on all subtests' and 'performed
            worst'. The proposed claim accurately reflects this detected association/impairment.
          source_ids:
          - P12-S1-C8
          - P12-S1-C12
        construct:
          answer: fits
          reason: The exposure is Wernicke's aphasia (clinical classification via
            WAB, P5-S1-C10) and the outcome is performance on CYCLE-R subtests (behavioral,
            P5-S1-C18). The patient measurement is behavioral (non_imaging), not the
            lesion overlap used in the VLSM analysis.
          source_ids:
          - P5-S1-C10
          - P5-S1-C18
          - P12-S1-C4
        qualifications:
          answer: fits
          reason: The proposed draft includes the qualification that the highest scores
            for this group were on the Possession subtest, which is supported by P12-S1-C8.
            The comparison is correctly identified as being against non-aphasic groups.
          source_ids:
          - P12-S1-C8
          - P12-S1-C12
        missing_material_caveat:
          answer: fits
          reason: The draft correctly identifies the analysis as a comparison of average
            percent scores (P12-S1-C4) and does not conflate it with the VLSM lesion
            analysis. No material caveats regarding the specific group comparison
            are omitted.
          source_ids:
          - P12-S1-C4
          - P12-S1-C12
      optional_pending:
      - Specific P-values or confidence intervals for the Wernicke's vs non-aphasic
        comparisons are not transcribed in the provided source window, though the
        text confirms significance.
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Specific P-values or confidence intervals for the Wernicke's vs non-aphasic
      comparisons are not transcribed in the provided source window, though the text
      confirms significance.
    normalizations: []
    analysis_identity:
      id: R023
      exposure:
        text: Wernicke’s aphasia vs non-aphasic groups
      outcome:
        text: all subtests
      analysis_label: Comparison of aphasia types
      relation: association
      evidence_ids:
      - P12-S1-C12
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
        pdf_sha256: 98dc43d10fb41da63e9a1017bd5ea1a046b22a793633e774c539f6e2d4b2a4bc
        source_review: _compare/relationships-2026-11-16/review-current/Dronkers2004
        source_status_sha256: bcd43ef94b87ec31e7817c03ae0166da6f5ad547f642a7266ab9190a9d26faa3
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P5-S1-C3:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 98dc43d10fb41da63e9a1017bd5ea1a046b22a793633e774c539f6e2d4b2a4bc
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 041fc2e61e9bafd0b80acd6effdf6a1ffbed87d4b1017b1591ecbd8dcb6989e0
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P5-S1-C3
          page: 5
          text_layer_sha256: 041fc2e61e9bafd0b80acd6effdf6a1ffbed87d4b1017b1591ecbd8dcb6989e0
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'LH patients ranged in age from 31 to 80 years (mean 61.5),
          in time post onset from the

          stroke from 1 to 20.5 years (mean 4.8), and in education from 5 to 20 years
          (mean 14.3).'
        anchor_text: 'LH patients ranged in age from 31 to 80 years (mean 61.5), in
          time post onset from the

          stroke from 1 to 20.5 years (mean 4.8), and in education from 5 to 20 years
          (mean 14.3).'
        excluded_fragments: []
        image_sha256: 8b92ea6ec1c6a6950d085b520a2314041e5610e8705220947120b60164e3ce5b
        transcription: LH patients ranged in age from 31 to 80 years (mean 61.5),
          in time post onset from the stroke from 1 to 20.5 years (mean 4.8), and
          in education from 5 to 20 years (mean 14.3)
      P4-S2-C6:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 98dc43d10fb41da63e9a1017bd5ea1a046b22a793633e774c539f6e2d4b2a4bc
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 4222dbe3de3aa8d5e559a4d6b85c5a367f7fac43d339a1c8500458239ba68ced
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P4-S2-C6
          page: 4
          text_layer_sha256: 4222dbe3de3aa8d5e559a4d6b85c5a367f7fac43d339a1c8500458239ba68ced
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Participants

          Sixty-four left hemisphere-injured (LH) chronic stroke patients, eight right
          hemi-

          sphere-injured (RH) chronic stroke patients, and 15 neurologically normal
          older controls

          participated in the study.'
        anchor_text: 'Participants

          Sixty-four left hemisphere-injured (LH) chronic stroke patients, eight right
          hemi-

          sphere-injured (RH) chronic stroke patients, and 15 neurologically normal
          older controls

          participated in the study.'
        excluded_fragments: []
        image_sha256: 1f240293194a24512845f499a9252f3160aee808b3ef9ac8d5e62e32dcf1943e
        transcription: 'Participants


          Sixty-four left hemisphere-injured (LH) chronic stroke patients, eight right
          hemisphere-injured (RH) chronic stroke patients, and 15 neurologically normal
          older controls participated in the study'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 12
  quote: 'Patients with Wernicke’s aphasia

    performed worst on all subtests, with their highest scores seen on the Possession
    subtest.'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-23'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
