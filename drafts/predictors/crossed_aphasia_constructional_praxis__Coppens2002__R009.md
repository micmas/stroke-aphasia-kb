---
id: crossed_aphasia_constructional_praxis
name: crossed aphasia constructional praxis
kind: predictor
findings:
- id: f1
  target_audit:
    status: needs_source_review
    category: non_behaviour_or_methodological
    original_target: language_lateralization
    reason: This endpoint is not a behaviour. Review its scope and target kind; do not relabel it as a behavioural
      deficit.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  outcome_measurement:
    status: needs_source_review
    instruments: []
    note: Outcome instrument/task is not yet verified for this finding. Do not infer it from the predictor
      or a paper-wide test list.
  target: language_lateralization
  target_kind: impairment
  claim: Constructional praxis lateralizes with language skills in patients with crossed
    aphasia, as evidenced by a higher frequency of left-hemisphere type constructional
    apraxia features compared to right-hemisphere type features.
  direction: likely
  relationship: correlational
  method: meta-analysis
  sample:
    n: not_reported
    population: right-handed patients with crossed aphasia (right hemisphere cerebrovascular
      accident and acquired language impairment)
    phase: not_reported
    time_post_onset: diagnosis preferentially used in the subacute period (3 weeks
      to 2 months postonset)
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Nonstandardized character of published case descriptions
  - Variability in the definition of constructional apraxia across reports
  - Potential for right-hemisphere type constructional apraxia to overshadow left-hemisphere
    type characteristics in patients with severe visuoperceptual impairment
  evidence_quality: meta-analysis
  strength: weak
  notes: 'Exposure measurement: Presence of constructional apraxia in patients with
    crossed aphasia, categorized by the presence of left-hemisphere features (loss
    of 3D perspective, distorted angles) or right-hemisphere features (exploded shapes,
    loss of component relationships), measured via drawing of a cube or similar 3D-to-2D
    renditions. Among 55 cases of reported constructional apraxia, 22 showed left-hemisphere
    features, 9 showed right-hemisphere features, 2 showed both, and 22 were undetermined.
    Additional metadata has not been transcribed; review the pending-field flags before
    approval. PDF image reading (P5-S2-C3, two-model agreement, human verification
    pending): . Whenever

    possible, the diagnosis in the subacute period was used (i.e., 3 weeks to 2 months

    postonset) Original text-layer quotation is preserved below.'
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
    - proposed_concept:language_lateralization
  citation: '@Coppens2002'
  source_passages:
  - section: Original source P26-S1-C7
    page: 26
    quote: 'Among the 55 cases (57.9% of patients assessed) of reported constructional
      apraxia,

      22 patients performed similarly to typical left-hemisphere stroke patients,
      9 patients

      similarly to a typical right-hemisphere lesion, 2 patients showed both left-
      and right-

      hemisphere features, and the type of constructional apraxia could not be determined

      in the remaining 22 patients.'
    supports: claim
  - section: Original source P26-S1-C8
    page: 26
    quote: 'These ﬁgures suggest that constructional praxis later-

      alizes with language skills.'
    supports: claim
  - section: Original source P26-S1-C3
    page: 26
    quote: 'Left-hemisphere stroke patients lose the three dimensional perspective,
      distort an-

      gles, whereas right-hemisphere stroke patients tend to add shapes, lose relationships

      between the diﬀerent component of the picture, which leads to an ‘‘exploded’’
      ren-

      dition of the cube (Brookshire, 1997; Kaplan, Gallagher, & Glosser, 1998; Tomp-

      kins, 1995).'
    supports: method
  - section: Original source P25-S1-C6
    page: 25
    quote: 'In the present review, constructional apraxia was diagnosed

      based on the drawing of a cube, or similar renditions of three dimensional material
      in

      two dimensions.'
    supports: method
  - section: Original source P4-S1-C10
    page: 4
    quote: 'The inclusion criteria included (a) a clear right

      hemisphere cerebrovascular accident, (b) a strongly right-handed patient, (c)
      a di-

      agnosis of acquired language impairment, and (d) the absence of previous brain

      damage, such as trauma or epilepsy.'
    supports: sample
  - section: Original source P5-S2-C3
    page: 5
    quote: 'Whenever

      possible, the diagnosis in the subacute period was used (i.e., 3 weeks to 2
      months

      postonset).'
    supports: sample
  - section: Original source P29-S1-C11
    page: 29
    quote: 'The limitations of this review are inherent to the nonstandardized character
      of

      published CA case descriptions.'
    supports: limitation
  - section: Original source P26-S1-C9
    page: 26
    quote: 'It is also to be anticipated that the more severe the vi-

      suoperceptual impairment in a given CA subject, the more likely the right-

      hemisphere type constructional apraxia will overshadow the left-hemisphere type

      characteristics.'
    supports: limitation
predictor_type: clinical
short_definition: Presence of constructional apraxia in patients with crossed aphasia,
  categorized by the presence of left-hemisphere features (loss of 3D perspective,
  distorted angles) or right-hemisphere features (exploded shapes, loss of component
  relationships), measured via drawing of a cube or similar 3D-to-2D renditions.
assessment:
- drawing of a cube
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-23'
relationship_review:
  paper: Coppens2002
  proposal_id: R009
  review_status_sha256: 3d3639b15bf67edde5fd481a6aacd66b70c50bd9fcec6baabfc53381f1004181
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 1e0ddf98a41068c3306d0356e708c9e06e6a8e29aee9ba8f28cca59497060866
    original_review_binding:
      version: relationship-review-v6
      input_hashes:
        pdf: 1e0ddf98a41068c3306d0356e708c9e06e6a8e29aee9ba8f28cca59497060866
        A/passages.json: 09d2c994d55b81ca69667dcee73c60d70bc3470531b43b241e87a3cbdc01073a
        A/raw.json: a206db8b2a0cb9ee2d59c20f0e3cf210511b6fcef419b66b5b77b45dec83e1ee
        A/source-units.json: 40272cd921b00057348700d814c810ab12aef6b2c4aae5ca185c06edd7ceb4c0
        A/full-source-units.json: cd7e3689948e965071d4031a4a978472d9e04be90e4cd1675519ed3eefef4442
        A/meta.json: d9b7c3cf86f086a002ce723619ce4cee0d4b30e57a6263bda42814a2652307b6
        A/table-images/page-14.png: 12d5c7ea4c61e5451e2d91f6646df017a0212f1e019d1aebf999e4a11cebb99d
        A/table-images/TABLE-6-page-23-1.png: a3ad243faad6c08dc8caa72263a899c6e92547b7d413218307b075c7416fe0ec
        A/table-images/page-12.png: 8a02e0a1087a5cb08b5919a92d33be9af96411e1221037dfdb3b039d7cbc1224
        A/table-images/page-10.png: 67cbe27343fa46cbca638e3f8779f3741cf8796ae2d6e3747cd88b8cdc91a0ac
        A/table-images/TABLE-6-page-25-1.png: a6c3dfa440cc69b5269b0e39685eb12169541f54b4647fef0c282d37bd81a7db
        A/table-images/TABLE-2-page-18-1.png: cb656cd8647867d8096bb909e3875a28434c7880796741287d8dd2e727d97e24
        A/table-images/TABLE-5-page-19-2.png: 717534c22eacb1bb8b83e6bcd25940780ffcee0107cecd6552b81d11bd73203a
        A/table-images/TABLE-6-page-22-1.png: e580e50ae4f9a12e5e17da9af4ae1d450ce11a1e2e618c947978d6d0a1e5f663
        A/table-images/TABLE-6-page-24-1.png: 5a1bbe2ef18c3c944f739df1aceada392690e230be0eacd2a200a7c3818a6a30
        A/table-images/TABLE-1-page-6-1.png: 137fb7681d0632c4e5193d490658de60bad2657291093ab926c494fbf41b578b
        A/table-images/page-6.png: 89057005b2331a1e5ad74ab38bc7ebf40a4f98400a1d1aec8689939d7ab11eea
        A/table-images/TABLE-1-page-8-1.png: b06d2493c0dd7cc485edf4cc1cc0e10456864b378593b092369606254387b285
        A/table-images/page-8.png: 4c568faa175ebfb13a23c7325991a19e298cfdca03bc6f51a4dd8df7af4001dc
        A/table-images/TABLE-7-page-26-1.png: f1757634ab2590963cc36e4e876d3b3258c0b848e11c3421c4d87184b64a4d29
        A/table-images/manifest.json: 032e426b35fadada5d6d5e759ce80090dd3da6b997612af6a32fa4471d959e7a
        A/table-images/TABLE-4-page-19-1.png: 2d9df642b3eea9c7c1adf85826deac2500259d47d5453615c29cdc21d018d8c9
        A/table-images/TABLE-3-page-18-2.png: cb656cd8647867d8096bb909e3875a28434c7880796741287d8dd2e727d97e24
        A/table-images/TABLE-1-page-10-1.png: bf6e6a2431cdeb9f7adcc2ed4cf9d1e1eba7e71d32510812f721df2b616b2cf6
        A/table-images/page-23.png: b0a4a8738909b4af82e7ee744018f6a0035710e3b3e0c615f3698660530f6deb
        A/table-images/TABLE-1-page-12-1.png: aaa222424674006b94677660a3f212c021610d00929e5a13ba768574a548c89d
        A/table-images/page-22.png: 8a93b3b270ed07b4abd783ca20b80803f20996c744db689b70d80f1330212e63
        A/table-images/page-26.png: 7fc5b2715840e64bbe2f539e090e8cfd5510d6e2fd32a673ab3de4929d9e5293
        A/table-images/page-25.png: 4df6374f62ce7e628fd73e12cfe84042bc6c899581727a0dcc1252bd3702b387
        A/table-images/page-19.png: ef31ed036918e340afc58f9be6354af6dd3c077873baafeed96b8e110c0ca9f7
        A/table-images/TABLE-1-page-14-1.png: 47194780199948960bd0f0f9fd96629697e00b22fbaf38604372c23d5bd421b0
        A/table-images/page-18.png: dbb0251a1c4c3a8df17d604ddf40433a39397d3f19887910e89cfa3ef02b7c3e
        A/table-images/page-24.png: e9eaa04e89f07abc30466b751d51b0c9ee32e5a96c3cfa9e2ae1e9ef5e99aea3
        A/clauses/window-11/raw.json: 259114d6e41778ac5fbdc3570be03961b77319ceb827af859eafb26ed888371b
        A/clauses/window-11/prompt.txt: 7341d221b88b706ace515ffc97b8c3f54b5a968a78cce07b91704dc962a57814
        A/clauses/window-11/meta.json: 85c2b233c57c49137dd104d847e9bb773d0942fa62c2e9a09c337d8c53008f31
        A/clauses/window-16/raw.json: 9debda0846c126839af7dd0f3707c1d18322123b07fa65658f366f624556b5c6
        A/clauses/window-16/prompt.txt: 1edbf3d13f355775b67b06d80fc0489e9b985ebaadb8c36b1f93f0d1f2a9922d
        A/clauses/window-16/meta.json: 3ca1d1dd3cbe598abe8fcc3e5701e5ddcac9d8a2f805940a88544e26517b2a65
        A/clauses/window-20/raw.json: e615f03a1765efdf7ad1cce4d39540ac5ada56824af1e6c01073090be1435008
        A/clauses/window-20/prompt.txt: ebcf264445aa71d2d258e8b604b43f4a6f119fce4ad28910f242bdc20f0f79ee
        A/clauses/window-20/meta.json: 66eca953f9f2894e17f6a3771478ccf7c016f7d355eca3400cc4ee3d961ae962
        A/clauses/window-18/raw.json: 1f10035e8cd530221ac1d47655836662c4cb614f94ac4435ad03766c93da85f5
        A/clauses/window-18/prompt.txt: fa7d1207b9c5006f949ffcf9d7525c1737c8dffce08b678dcd0fe3312c0c2e95
        A/clauses/window-18/meta.json: 96df0093280ab17eddec5d7bd6e3338771ff558171184c329dc1d1cd1fcacffe
        A/clauses/window-19/raw.json: 22845d01a9f3cc2e7344948c7e743f6a3b640a45c7de0aa166c585e4658115f1
        A/clauses/window-19/prompt.txt: 504feef63ae7dd4169286183039a32220c3a0f54d89a89c06eb7a314c0e52950
        A/clauses/window-19/meta.json: 8f141c1fea02cf8276caab2d9223016b4f214efa2f450bf7d6d29035d7415cf4
        A/clauses/window-21/raw.json: 9fe3e42d0c21c934f69015f84e278ee3c08da1205df8b27ac9f493bc86535737
        A/clauses/window-21/prompt.txt: 0e445b8e1a7a6cbacb33ca61cc4529d882fc36b604f4a06866df6728a5514b87
        A/clauses/window-21/meta.json: f4c464a90ff3485faab92c9f723bdbbd3bcd39ad8eabbaf9db13753ba5915978
        A/clauses/window-17/raw.json: 50cc6120d795ac0092dd9835a7d20b20fd6ebf833ef3f54c8f50243f39613759
        A/clauses/window-17/prompt.txt: fa5038233cefb88489b037ae9bcb85a22b130d3ee18ebc2ed6c6269775ea9394
        A/clauses/window-17/meta.json: 232d9efa1f4001541ee88623e86d006eea95bbf2efcc044cf7d12b7e2aa1def3
        A/clauses/window-10/raw.json: dc2c3986d610f277fb042fd193d4243007cc8b44a6d58f9578f50e2c9b535ce9
        A/clauses/window-10/prompt.txt: 609090f5a462041f631e43ba33bc28115fb64f6e9bff1b304eaeb7775f73a363
        A/clauses/window-10/meta.json: 5ed4eae6c56f8652dede1c83d1e292a3b7a9a0b9be41ed560cb263cbad863037
        A/clauses/window-03/raw.json: ce24bbbe4f0e2e5655e4fd76f56a006879f7bd953274831bdb0d74feb3dad28d
        A/clauses/window-03/prompt.txt: 7debf495ce11e1a5d5320a44b632065a2fc608084c58371f028c7096aedb6190
        A/clauses/window-03/meta.json: 24c33e6e90c500b80f528a3715bec6bef29a56f0b698fb2b7a13416295afa63d
        A/clauses/window-04/raw.json: 885393174a23acf5bc241b87407a8e061ee4f9418af6aca0c8a174e43470711a
        A/clauses/window-04/prompt.txt: de1e42537da09edf03cb49bbd55c2a6da87e385bc1a340a9933f4df28dfd656f
        A/clauses/window-04/meta.json: afd19e31940f796dc1e740ffb05770070a3d4206fe7db97ddb7974fe3a76fe32
        A/clauses/window-05/raw.json: 890c347b81017dd193115042c14dd718780536a0bac072769661314ca1fd7c5f
        A/clauses/window-05/prompt.txt: e93c9174155697b0781ba494440d622334991109ba297b2c2fe9b14fe038e4e0
        A/clauses/window-05/meta.json: 348b8ee9034be61ab997b8f54680bc3c92a204479caf23aeaeeeadbaebf18ac7
        A/clauses/window-02/raw.json: 1dcbbce69ae86a343b652ac9e79b2e81190398c538b67c7e354c4aa76484dd91
        A/clauses/window-02/prompt.txt: e3eb2e034f8799acc70deb634484482e9879b8a8176ecafc9829d80f796918ba
        A/clauses/window-02/meta.json: 587e8da34899c71e533e5fd38678b508cc96e0e623c6dcab34f618389a439aab
        A/clauses/window-15/raw.json: b058304c75eff20cc016deec34d636de18687465b6aeb431002ecf47fd62615f
        A/clauses/window-15/prompt.txt: a185294e31c5cc64279ba37c72cac9fb7d66154073022581cd47fdbfa3af5cf3
        A/clauses/window-15/meta.json: e0169a0748323eeb6ccbdf8329e564b3d0827fc6c9f27c6b1fda888109745eb9
        A/clauses/window-12/raw.json: 95efc648a7db17df6509a8835c8eaacb0c85341244dcf24e58b98d4dd70eb299
        A/clauses/window-12/prompt.txt: 5f52ba9222067339f9d84d04992dc3bd8ee0acf5d12fb50a2bcb3ac346b589d7
        A/clauses/window-12/meta.json: f51a239e0bcdf48e9b491a39f61c341e5f9cee9095e0544449a1b2fe1d6472e8
        A/clauses/window-22/raw.json: 8e6b42dcf2773aab902ab154ac3f7948675cfca6ba4575cea5122d5f1672ab58
        A/clauses/window-22/prompt.txt: f1ed7a660c3263c6b9bd380b6774b8f908daf79b75453bcbe20f65f5c049a227
        A/clauses/window-22/meta.json: eee53495f5e05bb7262e6e0f48f058f58c55c3fa65eab3bd90ee5f6ae5feb3d5
        A/clauses/window-13/raw.json: db3af900c05f53a8bbd897a6fa376eaf2a30e10969a5bd30835bf40c0fe1a7d1
        A/clauses/window-13/prompt.txt: 8c747ae876d5152a6d4812fabde2bb0665fb2aec113d187b55fb3aab2e7364a0
        A/clauses/window-13/meta.json: a52bb86ec73f86573a99406cb44ed56dee53eed9faa495141c3a9caf47737aca
        A/clauses/window-14/raw.json: 79bfa3caf4bd7736668a5d0a84c6a05215f88e16c226e833dbf00e823302bac1
        A/clauses/window-14/prompt.txt: d0e16ae5a08e7e2cf8fcf04a09bf5ce5b8937a677fbeb15568193dcd86a70e5c
        A/clauses/window-14/meta.json: 7af8511bec66f6174196768507284bf03e096e9e46ffde77de9de83c2435653b
        A/clauses/window-09/raw.json: 6932b417f341049486739fef316e2c9fb147d547e8ff63da48c0d054ab867ad0
        A/clauses/window-09/prompt.txt: af361c72a3c79cd4f093205fdac8ae518a384e3c6c46e148acf9474cf6f7e9f1
        A/clauses/window-09/meta.json: 799fedfb2af306ef3ef0d7040ff169dab7fae2d6f6d35ad866c14470c1b9a69f
        A/clauses/window-07/raw.json: 5e586fafd780f422c434b714bacc31e54cfab840c0d5851b17c5e6495a996c18
        A/clauses/window-07/prompt.txt: 8d7b1543864ba373db4db150722a9f90a65c4377ab36d033c8418534a538341f
        A/clauses/window-07/meta.json: 0cf0786b99f2860cc90c53b74e934c550c1ca40250a3533d8026a42d6ffc6e14
        A/clauses/window-01/raw.json: 1619d5b3f708d0835b329e28a0a5afd2b3cb7e040c12e56714c091f8823af130
        A/clauses/window-01/prompt.txt: 3ffa01d9d6d5e980c6530a993d22ff2395b1c95b7519d16e9fb518ec500106c9
        A/clauses/window-01/meta.json: 65fac61dbb3695f752de6b5725f96926a51ada5287e47882dd89f2b43566a18d
        A/clauses/window-06/raw.json: 9f4cd08c9aa186dee0ac17fdcba1b10d9df65702866082621034a47a8877b55a
        A/clauses/window-06/prompt.txt: f014c4f2da81fe33628a0a7fc47116ba06eec2e9b4893b4c420f36996964ec6c
        A/clauses/window-06/meta.json: 3dcd299dab54212737c8a42e113533a74512a19a29f39d3992d4115efb9486e4
        A/clauses/window-08/raw.json: 61ee8b7769d874f8fc62e6db47aa7424f815a0761ef281a9c01ee9ebe4db80a6
        A/clauses/window-08/prompt.txt: 0e8c75d99de24521cbb9efbccd4bbd63e119312f63d6aa3b83becd540149cb32
        A/clauses/window-08/meta.json: 9eb965932a2ae9fdb8914007b440412f6b03ff4cbce343e1218112d504c99553
        A/tables/TABLE-1-page-14-5/raw.json: b01b5aae378a5ce7765b01cf94de7374dc9a51a0a76c6b1eccb3957f626ed846
        A/tables/TABLE-1-page-14-5/prompt.txt: c9bc32b9355e63811b1c5e94ccf84e15570d39dc47a6330cb1fde32766bb374a
        A/tables/TABLE-1-page-14-5/meta.json: b75bbc078ae07eaa9d09730028d36a8ccac221e596a7c227fcb1402da6f1c8ee
        A/tables/TABLE-1-page-10-3/raw.json: 2e8656090418d878a9c31cfe079d1f9d6887892e85f8de5eb7e53e81f0c8c275
        A/tables/TABLE-1-page-10-3/prompt.txt: f922e40208c412894e6c3a169e8a990e0ebb5825ef2d401c912006f6c6924af8
        A/tables/TABLE-1-page-10-3/meta.json: cbe9e6f258e750779f5865cd8238977108d72d4b5fa10ac3a745165795790c09
        A/tables/TABLE-4-page-19-8/raw.json: 1161f39533fb498c2645dab4cda8391fc8b1a4171bd4251eb2511629ba18170e
        A/tables/TABLE-4-page-19-8/prompt.txt: 24537bf367072813136eac4438090acf94815e318c39314e563c80b53c36cf39
        A/tables/TABLE-4-page-19-8/meta.json: 6f6685ace04dbaa8144bfeba3d5b85595bfbc0251d54f2b9e30ebf307181ba9a
        A/tables/TABLE-1-page-6-1/raw.json: b9c000a6b8f069fcb60633668822404eda537c01648455c867ca19f81756a676
        A/tables/TABLE-1-page-6-1/prompt.txt: 1251f6a510192075e0054f04ebc415f7465abb09f561fee4c8e0dd035db8f58d
        A/tables/TABLE-1-page-6-1/meta.json: 2960b50dc641b752cb991e3370097f02f5a4dd5942c0001d12e067659263f223
        A/tables/TABLE-5-page-19-9/raw.json: 3850ea20973f3a0c3cf42cde2ae25e08edac34b9ec814a05275f3e5254520cbb
        A/tables/TABLE-5-page-19-9/prompt.txt: 395e8eca999b824e58621e03d2499099666a33fa81c1420df675d50a24e05a55
        A/tables/TABLE-5-page-19-9/meta.json: 50722483f2107c0e2a9bac8e3148d5e4d3329146e79df75f5622d4291575f211
        A/tables/TABLE-1-page-12-4/raw.json: bcb98d5f9168125b923db732560d64189367d8aa78a49a86f18bf4320f0a4e14
        A/tables/TABLE-1-page-12-4/prompt.txt: 9c1e572c156857b24805fe37307a0d7b541e056ff97418e8698a47538e3d6b30
        A/tables/TABLE-1-page-12-4/meta.json: 857db4d0ebee9fb18122ec2fe99f53a7395dd0d8bc1322a02e8dc85f95c7dd55
        A/tables/TABLE-3-page-18-7/raw.json: ba91ef6dd7c8fc6e577c76d3d82b13ac613a847ea77b40f7459e43ab4831c9d6
        A/tables/TABLE-3-page-18-7/prompt.txt: 6ae5be97cf84f9632b1c1317f6282362897a5740035299a40076feccce10f5c4
        A/tables/TABLE-3-page-18-7/meta.json: ad15cbfc306a1b4dc17108599d8daf4ddc96ba878bb39b95267a2ee24d1eb1eb
        A/tables/TABLE-6-page-24-12/raw.json: 1808277df0f821ae420ba36ea39c813831c0ab4e83c7cefd437e48a2bc3af7bb
        A/tables/TABLE-6-page-24-12/prompt.txt: d36a8aceb5101bd4888f63890750545a18869622ba218b704941cc081691e3b4
        A/tables/TABLE-6-page-24-12/meta.json: 8d75e771b907da1046ccbb1961a819a12f438ef1d44308d1b145503f40994ed9
        A/tables/TABLE-6-page-25-13/raw.json: dfcf2484d20149654cf72b42679df895f79f58a49dd03b5f3b695e525b4732e2
        A/tables/TABLE-6-page-25-13/prompt.txt: e1296d83a880237503cf505dbf464d3ead501c0874c2d942c9b40fb0f33965e0
        A/tables/TABLE-6-page-25-13/meta.json: 4ef361038956112dc739904ec25fb39e51251b9dc4ad22ed07e4962bab486475
        A/tables/TABLE-6-page-22-10/raw.json: 7ed60231e7014f8bfa1f9b4ae2f4140b41938e62f7db7a6b54e7bd4b6c5e3a78
        A/tables/TABLE-6-page-22-10/prompt.txt: 0409fde5f1bb026ffc9d093d7ac68b0963b67597f8e7299c8458fa2f4fa34690
        A/tables/TABLE-6-page-22-10/meta.json: 938fec774c0e3d8879cdce00cab9507cd7bd718a6c7b80c98f6897e59b933d99
        A/tables/TABLE-2-page-18-6/raw.json: c89b441f315d8580dae87bc75f9724d9fbfceccf1f1aa9ca656a19a556554272
        A/tables/TABLE-2-page-18-6/prompt.txt: 7ffb938e6930c5ef674fa6689eaf3569ac5cd8c89ca4a6e7c596112d861db4fb
        A/tables/TABLE-2-page-18-6/meta.json: 604db3f41dd8c923042c8a0053502938b8ff916aeab48b0d35f776e5a60f48e4
        A/tables/TABLE-1-page-8-2/raw.json: 4501c48da8867bb6237cd0979173e89d8d26ff90eeb988d6a7b8f067b7f134ae
        A/tables/TABLE-1-page-8-2/prompt.txt: 247c8be56649ab04d6b38503bb902f4d5077090b6d071b48cc3e605acd3d1f55
        A/tables/TABLE-1-page-8-2/meta.json: ffb8548c91fc51d191de89fb3aecc99eab182313629ae682fdcb4fa3f570dfab
        A/tables/TABLE-6-page-23-11/raw.json: eb58deccc0a4dd61dcd06edaee7dbf2b763433741ad413d879d3889c06e61c18
        A/tables/TABLE-6-page-23-11/prompt.txt: 050439e805ab8cd3e76f85d5e9abad9b7775f9f9dee63a44eebb63b88c67c577
        A/tables/TABLE-6-page-23-11/meta.json: 128c42dc179fa8c6d83cec24f6f52df301e0f494aeb2a17083f8bd4c810d7b5d
        A/tables/TABLE-7-page-26-14/raw.json: 34fff3d833ee7e6ad0588d92484d02508079ccca6a9c1fff8fa36eab182fe44c
        A/tables/TABLE-7-page-26-14/prompt.txt: 03b95aa5b9be007b96cdabeab4df8f32504f65040c18f848fd324844418dfb17
        A/tables/TABLE-7-page-26-14/meta.json: 1fdae880405c63ce72cd26020e110047e50b92e788bb3ee60e0bd2de9d3049be
        B/passages.json: 09d2c994d55b81ca69667dcee73c60d70bc3470531b43b241e87a3cbdc01073a
        B/raw.json: 0638b5e895963eb09b7c3b3d4ce47296e996c8a88b820fef3482e8612c3d8e18
        B/source-units.json: 40272cd921b00057348700d814c810ab12aef6b2c4aae5ca185c06edd7ceb4c0
        B/full-source-units.json: cd7e3689948e965071d4031a4a978472d9e04be90e4cd1675519ed3eefef4442
        B/meta.json: 1355f866be24f77b9140b3146ed68384b3488386b89497ac5b4c640ef6601c86
        B/table-images/page-14.png: 12d5c7ea4c61e5451e2d91f6646df017a0212f1e019d1aebf999e4a11cebb99d
        B/table-images/TABLE-6-page-23-1.png: a3ad243faad6c08dc8caa72263a899c6e92547b7d413218307b075c7416fe0ec
        B/table-images/page-12.png: 8a02e0a1087a5cb08b5919a92d33be9af96411e1221037dfdb3b039d7cbc1224
        B/table-images/page-10.png: 67cbe27343fa46cbca638e3f8779f3741cf8796ae2d6e3747cd88b8cdc91a0ac
        B/table-images/TABLE-6-page-25-1.png: a6c3dfa440cc69b5269b0e39685eb12169541f54b4647fef0c282d37bd81a7db
        B/table-images/TABLE-2-page-18-1.png: cb656cd8647867d8096bb909e3875a28434c7880796741287d8dd2e727d97e24
        B/table-images/TABLE-5-page-19-2.png: 717534c22eacb1bb8b83e6bcd25940780ffcee0107cecd6552b81d11bd73203a
        B/table-images/TABLE-6-page-22-1.png: e580e50ae4f9a12e5e17da9af4ae1d450ce11a1e2e618c947978d6d0a1e5f663
        B/table-images/TABLE-6-page-24-1.png: 5a1bbe2ef18c3c944f739df1aceada392690e230be0eacd2a200a7c3818a6a30
        B/table-images/TABLE-1-page-6-1.png: 137fb7681d0632c4e5193d490658de60bad2657291093ab926c494fbf41b578b
        B/table-images/page-6.png: 89057005b2331a1e5ad74ab38bc7ebf40a4f98400a1d1aec8689939d7ab11eea
        B/table-images/TABLE-1-page-8-1.png: b06d2493c0dd7cc485edf4cc1cc0e10456864b378593b092369606254387b285
        B/table-images/page-8.png: 4c568faa175ebfb13a23c7325991a19e298cfdca03bc6f51a4dd8df7af4001dc
        B/table-images/TABLE-7-page-26-1.png: f1757634ab2590963cc36e4e876d3b3258c0b848e11c3421c4d87184b64a4d29
        B/table-images/manifest.json: 91f299c10ff94dee260293288210259608642083dc3885d5d5d547f9fff98cb3
        B/table-images/TABLE-4-page-19-1.png: 2d9df642b3eea9c7c1adf85826deac2500259d47d5453615c29cdc21d018d8c9
        B/table-images/TABLE-3-page-18-2.png: cb656cd8647867d8096bb909e3875a28434c7880796741287d8dd2e727d97e24
        B/table-images/TABLE-1-page-10-1.png: bf6e6a2431cdeb9f7adcc2ed4cf9d1e1eba7e71d32510812f721df2b616b2cf6
        B/table-images/page-23.png: b0a4a8738909b4af82e7ee744018f6a0035710e3b3e0c615f3698660530f6deb
        B/table-images/TABLE-1-page-12-1.png: aaa222424674006b94677660a3f212c021610d00929e5a13ba768574a548c89d
        B/table-images/page-22.png: 8a93b3b270ed07b4abd783ca20b80803f20996c744db689b70d80f1330212e63
        B/table-images/page-26.png: 7fc5b2715840e64bbe2f539e090e8cfd5510d6e2fd32a673ab3de4929d9e5293
        B/table-images/page-25.png: 4df6374f62ce7e628fd73e12cfe84042bc6c899581727a0dcc1252bd3702b387
        B/table-images/page-19.png: ef31ed036918e340afc58f9be6354af6dd3c077873baafeed96b8e110c0ca9f7
        B/table-images/TABLE-1-page-14-1.png: 47194780199948960bd0f0f9fd96629697e00b22fbaf38604372c23d5bd421b0
        B/table-images/page-18.png: dbb0251a1c4c3a8df17d604ddf40433a39397d3f19887910e89cfa3ef02b7c3e
        B/table-images/page-24.png: e9eaa04e89f07abc30466b751d51b0c9ee32e5a96c3cfa9e2ae1e9ef5e99aea3
        B/clauses/window-11/raw.json: 6e0d22eccd81467a4cee39fb83f59b76b4a60d172f14fb18d97af332e904066e
        B/clauses/window-11/prompt.txt: 7341d221b88b706ace515ffc97b8c3f54b5a968a78cce07b91704dc962a57814
        B/clauses/window-11/meta.json: 241d16addfb5a45305131b83f8924f12db3c8b6cfa0a158801f804ae6f147fd2
        B/clauses/window-16/raw.json: 6f04d037a21030622013c06586e9eb2c5212bfcd7b32286f58a4ef89764744ee
        B/clauses/window-16/prompt.txt: 1edbf3d13f355775b67b06d80fc0489e9b985ebaadb8c36b1f93f0d1f2a9922d
        B/clauses/window-16/meta.json: 69301453f175d143e807b1e8821b22d49479f726f05031f3323b80df441add95
        B/clauses/window-20/raw.json: 424e3922e5574268e384a72c70995a9994a0b7137327cf7cbd873d7090a4da75
        B/clauses/window-20/prompt.txt: ebcf264445aa71d2d258e8b604b43f4a6f119fce4ad28910f242bdc20f0f79ee
        B/clauses/window-20/meta.json: 6db9771ff556bd1b47a29af6a0be41f37ef4310b93651f5835ba470b91a21651
        B/clauses/window-18/raw.json: 1c26b556c6fb42b3dd03da2a8128da5bd143d523a6085f7ccbd4a90dd12e7c66
        B/clauses/window-18/prompt.txt: fa7d1207b9c5006f949ffcf9d7525c1737c8dffce08b678dcd0fe3312c0c2e95
        B/clauses/window-18/meta.json: 63e8a07f220cffe2af7a1ff907e535ff181364495225b13586ec3865f40fc1a8
        B/clauses/window-19/raw.json: 32da06bd4218bf49491c9752fc09e211ee75ee185746ad329568a7814b472fd3
        B/clauses/window-19/prompt.txt: 504feef63ae7dd4169286183039a32220c3a0f54d89a89c06eb7a314c0e52950
        B/clauses/window-19/meta.json: b3f226023053c3efa5c92c6dfa99c1d3150d6f6651438be7587f323d7b6ef5ad
        B/clauses/window-21/raw.json: 76539fa408a33115dee6802026ef2c67f9b789e805a70a62027de4664902bd1d
        B/clauses/window-21/prompt.txt: 0e445b8e1a7a6cbacb33ca61cc4529d882fc36b604f4a06866df6728a5514b87
        B/clauses/window-21/meta.json: 607f6a2c739eed71484ee3102fb7748195a87b3c4c58e680c1ae312b90c97230
        B/clauses/window-17/raw.json: 96e1aa93a77f46ed4dc4a5564c68a6f13900f56beeba970f32d03b7b5e268713
        B/clauses/window-17/prompt.txt: fa5038233cefb88489b037ae9bcb85a22b130d3ee18ebc2ed6c6269775ea9394
        B/clauses/window-17/meta.json: ea87b6ee6df12e70c864ae6bdacc95e0625f0ad7882912d5324fca6f7eb14d19
        B/clauses/window-10/raw.json: dc2c3986d610f277fb042fd193d4243007cc8b44a6d58f9578f50e2c9b535ce9
        B/clauses/window-10/prompt.txt: 609090f5a462041f631e43ba33bc28115fb64f6e9bff1b304eaeb7775f73a363
        B/clauses/window-10/meta.json: 82fca6579faf2ff33c0b1f55302fc18bb45272e2e91b3388d7b5c6862ad73350
        B/clauses/window-03/raw.json: 084d15f94b16f7052766822e5564e2ca7addaacf1ae00f96b1fc0a44c7b9505a
        B/clauses/window-03/prompt.txt: 7debf495ce11e1a5d5320a44b632065a2fc608084c58371f028c7096aedb6190
        B/clauses/window-03/meta.json: bddffa1fb780586bebacfa2980f397a95e8d3678ef43d9c3d9e18e1b763cacc7
        B/clauses/window-04/raw.json: 14e69a264ff7c55be5e3ef970262162652753df92d68ea8f7c54de1c07999cd2
        B/clauses/window-04/prompt.txt: de1e42537da09edf03cb49bbd55c2a6da87e385bc1a340a9933f4df28dfd656f
        B/clauses/window-04/meta.json: 4b366bd34694dceafd7b7058f08abc08fe8493b5dc359a6bc40e65b0dc0ed891
        B/clauses/window-05/raw.json: 6fd66a21b568056457b20f99daa191aa210ef2dada4025a65a410eefd1c2d32a
        B/clauses/window-05/prompt.txt: e93c9174155697b0781ba494440d622334991109ba297b2c2fe9b14fe038e4e0
        B/clauses/window-05/meta.json: 1a9c59521c1f472c61380a3de9bb1111ccf6e4629c4c7f99f42ded8261ac7308
        B/clauses/window-02/raw.json: 689d20af2c7190a59c21ff44cb73aa646f435aef22087a48743c83568b816009
        B/clauses/window-02/prompt.txt: e3eb2e034f8799acc70deb634484482e9879b8a8176ecafc9829d80f796918ba
        B/clauses/window-02/meta.json: c4aa73656d376d58da345bd4d0386aa4d3ce90ddd80078a9019eec2e96a4cc57
        B/clauses/window-15/raw.json: dada5a58c71c58a2b6b1f032bcd165b14b5b86298c77cce0d1aec8bb9007b3c0
        B/clauses/window-15/prompt.txt: a185294e31c5cc64279ba37c72cac9fb7d66154073022581cd47fdbfa3af5cf3
        B/clauses/window-15/meta.json: b6084050dfc1d79f842bc3ca8b832dcfe3ee75f2f6ec472e99d6cd0f002f5f42
        B/clauses/window-12/raw.json: a59387ccc78a8afe24f4474f2cd53d60e402a1c23428f4be6ab4285b83006a6e
        B/clauses/window-12/prompt.txt: 5f52ba9222067339f9d84d04992dc3bd8ee0acf5d12fb50a2bcb3ac346b589d7
        B/clauses/window-12/meta.json: 966d8d8d39a57508857d9aa4a2c17213c64ef7d8be03351ccf25cfe313fa073f
        B/clauses/window-22/raw.json: 90868f275d6205d21a887abca2cdf635ae4f07b53459c9c07ea2b74eb1ce6a02
        B/clauses/window-22/prompt.txt: f1ed7a660c3263c6b9bd380b6774b8f908daf79b75453bcbe20f65f5c049a227
        B/clauses/window-22/meta.json: e771eca4b6f8277dd9fb49e0b22f602788046ec05bc43698d93e82dcf3083f2a
        B/clauses/window-13/raw.json: 07c30c9183c36018a2bc36e1c9ee85808ad959c680062e53008b28502a187e57
        B/clauses/window-13/prompt.txt: 8c747ae876d5152a6d4812fabde2bb0665fb2aec113d187b55fb3aab2e7364a0
        B/clauses/window-13/meta.json: 2f2e65759a67bc30eefdddaed1451db6f122245c4453ecb3d8d5dc8f56e8b424
        B/clauses/window-14/raw.json: 43f3d698feebb89681b6bdfc35cb7c7a1d02411a98bf242d394a60ff0e9f344a
        B/clauses/window-14/prompt.txt: d0e16ae5a08e7e2cf8fcf04a09bf5ce5b8937a677fbeb15568193dcd86a70e5c
        B/clauses/window-14/meta.json: 618e26527330bd7538f0c9d9d1f88863ee193d989232aff67c48477d80159a01
        B/clauses/window-09/raw.json: 4c118e8a4627d98f93cfee2f132c3eee58769ac53a31c0f9805caff3273a64af
        B/clauses/window-09/prompt.txt: af361c72a3c79cd4f093205fdac8ae518a384e3c6c46e148acf9474cf6f7e9f1
        B/clauses/window-09/meta.json: 2f584318f49bb16960c76bfa5a9cd12b38927d0b159389bd4119d99d2e1ab13e
        B/clauses/window-07/raw.json: 3ba511464f27ff909c90c7f6deb9a6efa61a3db5128f14d600a7dd422e0993b7
        B/clauses/window-07/prompt.txt: 8d7b1543864ba373db4db150722a9f90a65c4377ab36d033c8418534a538341f
        B/clauses/window-07/meta.json: 575b4a9d005232fb1f3f83d7a8d649b23591ded680fda1afc73123e9dbfcb71b
        B/clauses/window-01/raw.json: cacc01880b14d5135bab2ef1ff1af407b92cecefab87838da4b7a746776bcfc9
        B/clauses/window-01/prompt.txt: 3ffa01d9d6d5e980c6530a993d22ff2395b1c95b7519d16e9fb518ec500106c9
        B/clauses/window-01/meta.json: c933eb508baaa9c8322c38dd79bf090b2854693be4e4115514a541f2457608ba
        B/clauses/window-06/raw.json: 90a8557aa3849b98d314dde4c42725c0e2616b1943d1d44b98cb6b1a389a9011
        B/clauses/window-06/prompt.txt: f014c4f2da81fe33628a0a7fc47116ba06eec2e9b4893b4c420f36996964ec6c
        B/clauses/window-06/meta.json: e7ea03fbd794581ddf90a108acd174d954987c078eafa09620a8868a95a3cd54
        B/clauses/window-08/raw.json: ee0ecc27e152c996f0eeaadd2e97d1f72f2cf7ba5d2a78e9d08863adea5605cf
        B/clauses/window-08/prompt.txt: 0e8c75d99de24521cbb9efbccd4bbd63e119312f63d6aa3b83becd540149cb32
        B/clauses/window-08/meta.json: fe03c4ef6e32c4b457c8b0c040181389a16a0d09d47f8c00153c0c023860c768
        B/tables/TABLE-1-page-14-5/raw.json: 9ba6b654abb312857bb7a1028ed621ce52d0a16642b2df1ecd725ca489b8fe9d
        B/tables/TABLE-1-page-14-5/prompt.txt: c9bc32b9355e63811b1c5e94ccf84e15570d39dc47a6330cb1fde32766bb374a
        B/tables/TABLE-1-page-14-5/meta.json: e1bff789653a8d93ebcc5f43ff6d82c670ff0a9325c9306c20e21b59ca97ae47
        B/tables/TABLE-1-page-10-3/raw.json: 76fd666281fef580b483f6cd715a12c4eb57b1e0517cd54e22dcc9b046881b8a
        B/tables/TABLE-1-page-10-3/prompt.txt: f922e40208c412894e6c3a169e8a990e0ebb5825ef2d401c912006f6c6924af8
        B/tables/TABLE-1-page-10-3/meta.json: 8ccc2e6e8bb01260d7c35ebbbb77c885685ae45666d46374534fd166a565a588
        B/tables/TABLE-4-page-19-8/raw.json: 1161f39533fb498c2645dab4cda8391fc8b1a4171bd4251eb2511629ba18170e
        B/tables/TABLE-4-page-19-8/prompt.txt: 24537bf367072813136eac4438090acf94815e318c39314e563c80b53c36cf39
        B/tables/TABLE-4-page-19-8/meta.json: 9631a465e56b6b591ff62e077b9bd00a6336394b07c49758b438d8dac16afdc9
        B/tables/TABLE-1-page-6-1/raw.json: ce59335fe86007265e8ae918b6eb873cb7a061338341df1825f2bd84ad00adb0
        B/tables/TABLE-1-page-6-1/prompt.txt: 1251f6a510192075e0054f04ebc415f7465abb09f561fee4c8e0dd035db8f58d
        B/tables/TABLE-1-page-6-1/meta.json: 8938d6eee9316be0d789646cc4e0103c154353463f67cf475d65952fb1a8d188
        B/tables/TABLE-5-page-19-9/raw.json: 307d74044e1a7def3b93a6aed2a24d1211ee9c073df803b7bf314372b81428ae
        B/tables/TABLE-5-page-19-9/prompt.txt: 395e8eca999b824e58621e03d2499099666a33fa81c1420df675d50a24e05a55
        B/tables/TABLE-5-page-19-9/meta.json: f87723101f5d5158e37bb02c8efee9cd69104f2f2e7530ae3ad0b890e4dff5e6
        B/tables/TABLE-1-page-12-4/raw.json: 66663ea86ab8f96f5dfdfb02822929912b67ef39a7caa02f8af18ab7fc378d34
        B/tables/TABLE-1-page-12-4/prompt.txt: 9c1e572c156857b24805fe37307a0d7b541e056ff97418e8698a47538e3d6b30
        B/tables/TABLE-1-page-12-4/meta.json: 7b003bb6a07d66eff0d463cb1e14cd14444ef9f90e7ccfb8318978dcafa45242
        B/tables/TABLE-3-page-18-7/raw.json: 28573236f6a525e49364bac412cce840ac066e2c0a2f84db06e09b9ccb1f166f
        B/tables/TABLE-3-page-18-7/prompt.txt: 6ae5be97cf84f9632b1c1317f6282362897a5740035299a40076feccce10f5c4
        B/tables/TABLE-3-page-18-7/meta.json: 19caa4428bcbfebb86178928f30789b2849b4a9ae57de96ee0929ef20d6671ce
        B/tables/TABLE-6-page-24-12/raw.json: 96047ca76eaaa8a2c686245c7e104f2a75390237fd66cabc8f0f61e1769b679c
        B/tables/TABLE-6-page-24-12/prompt.txt: d36a8aceb5101bd4888f63890750545a18869622ba218b704941cc081691e3b4
        B/tables/TABLE-6-page-24-12/meta.json: 766b22e59b7633e08749e982c77fb490d3d92d78dae9dc8e8585fba15361138d
        B/tables/TABLE-6-page-25-13/raw.json: 4582a1b95888348e66d5b420769360bbd8f2f8a3e82007c80e9b70ae9cc3600e
        B/tables/TABLE-6-page-25-13/prompt.txt: e1296d83a880237503cf505dbf464d3ead501c0874c2d942c9b40fb0f33965e0
        B/tables/TABLE-6-page-25-13/meta.json: 093201a6e9ce450ddcb653c80c4bdd07cd0b65469884c8762898026d8b3e0aad
        B/tables/TABLE-6-page-22-10/raw.json: db9784c3b6b7342343a64000940cdd2dcf7ccad37c3c266091c2c3a231a99706
        B/tables/TABLE-6-page-22-10/prompt.txt: 0409fde5f1bb026ffc9d093d7ac68b0963b67597f8e7299c8458fa2f4fa34690
        B/tables/TABLE-6-page-22-10/meta.json: 9ad03adb2171417b11591b412a199f5cecdbdef61ce27986807d8659df4c4f7c
        B/tables/TABLE-2-page-18-6/raw.json: 37ec5cc9ee4c28dc35ac008d9e2a12d553ca7b740eea232204100bd59923ce67
        B/tables/TABLE-2-page-18-6/prompt.txt: 7ffb938e6930c5ef674fa6689eaf3569ac5cd8c89ca4a6e7c596112d861db4fb
        B/tables/TABLE-2-page-18-6/meta.json: ab111562cdfb9c7f3209e3c4aa65848b768f362fe06ffba2b099c01ab497d101
        B/tables/TABLE-1-page-8-2/raw.json: 58509ed1355f2bdb511c99ec9b8b0b12fb85d53839232acf3c12ae319b0498fc
        B/tables/TABLE-1-page-8-2/prompt.txt: 247c8be56649ab04d6b38503bb902f4d5077090b6d071b48cc3e605acd3d1f55
        B/tables/TABLE-1-page-8-2/meta.json: f5d1fd1e362e6539bfa4295cc0b63069cea799bd1b5d41ce3934eb532d49add8
        B/tables/TABLE-6-page-23-11/raw.json: 7223c8457c23f78356d0737bb955f5494736739f4f51c978cbab6bada908f0f0
        B/tables/TABLE-6-page-23-11/prompt.txt: 050439e805ab8cd3e76f85d5e9abad9b7775f9f9dee63a44eebb63b88c67c577
        B/tables/TABLE-6-page-23-11/meta.json: ea5e4a6c7ea6c52f504c33a499be79375d23152dfc9e800f2678efe876a7008e
        B/tables/TABLE-7-page-26-14/raw.json: 4637f67bf78700fa555548611235847e0416703abe1bab133abbfa128186373a
        B/tables/TABLE-7-page-26-14/prompt.txt: 03b95aa5b9be007b96cdabeab4df8f32504f65040c18f848fd324844418dfb17
        B/tables/TABLE-7-page-26-14/meta.json: 9c1d4191b6c0da434a7422cf26e8ee9e821d7d9b253a64597a19a4a171a3d0e3
      code:
        relationship_review.py: ab52eac5603e2f4080aa82e51ec2d579714fe7aeecc6cc376f345c9001157135
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
      pdf_sha256: 1e0ddf98a41068c3306d0356e708c9e06e6a8e29aee9ba8f28cca59497060866
      source_review: _compare/relationships-2026-11-16/review-current/Coppens2002
      source_status_sha256: b23efd9d623a174e8b3db29c3ee463c334a29227e35da9b8cbb59c60abbec094
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R009
    exposure:
      text: crossed aphasia
    outcome:
      text: constructional apraxia type (left-hemisphere vs right-hemisphere features)
    analysis_label: Constructional praxis lateralization
    relation: association
    evidence_ids:
    - P26-S1-C7
    - P26-S1-C8
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
      pdf_sha256: 1e0ddf98a41068c3306d0356e708c9e06e6a8e29aee9ba8f28cca59497060866
      source_review: _compare/relationships-2026-11-16/review-current/Coppens2002
      source_status_sha256: b23efd9d623a174e8b3db29c3ee463c334a29227e35da9b8cbb59c60abbec094
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Unresolved source passage P3-S2-C11
      - Unresolved source passage P3-S2-C12
      - Accounting without a linked unit P3-S2-C5
      - Unaccounted source passage P3-S2-C5
      - Accounting without a linked unit P17-S2-C14
      - Accounting without a linked unit P17-S2-C15
      - Accounting without a linked unit P18-S1-C1
      - Unaccounted source passage P18-S1-C1
      - Unaccounted source passage P17-S2-C14
      - Unaccounted source passage P17-S2-C15
      - Accounting without a linked unit P20-S1-C2
      - Accounting without a linked unit P20-S1-C3
      - Accounting without a linked unit P20-S1-C7
      - Unaccounted source passage P20-S1-C2
      - Unaccounted source passage P20-S1-C3
      - Unaccounted source passage P20-S1-C7
      - Result passage disposed without unit P20-S2-C4
      - Result passage disposed without unit P21-S1-C3
      - Accounting without a linked unit P21-S2-C14
      - Unaccounted source passage P21-S2-C14
      - Result passage disposed without unit P21-S2-C15
      - Accounting without a linked unit P21-S2-C16
      - Unaccounted source passage P21-S2-C16
      - Accounting without a linked unit P26-S1-C7
      - Unaccounted source passage P26-S1-C7
      - Result passage disposed without unit P26-S1-C11
      - Accounting without a linked unit P26-S1-C12
      - Result passage disposed without unit P26-S2-C3
      - Unaccounted source passage P26-S1-C12
      - Accounting without a linked unit P26-S2-C9
      - Unaccounted source passage P26-S2-C9
      - Result passage disposed without unit P27-S1-C5
      - Accounting without a linked unit P27-S2-C6
      - Unaccounted source passage P27-S2-C6
      - Result passage disposed without unit P29-S1-C5
      - Accounting without a linked unit P33-S2-C10
      - Accounting without a linked unit P33-S2-C8
      - Accounting without a linked unit P33-S2-C9
      - Unaccounted source passage P33-S2-C9
      - Unaccounted source passage P33-S2-C10
      - Unaccounted source passage P33-S2-C8
      unattached_null_or_qualifier_ids:
      - P20-S2-C3
      - P27-S1-C5
      - P30-S2-C13
      suppressed_nonrepresented_units: 44
      default_disposition_count_requires_completeness_check: 520
      unselected_timing_passages: []
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P18-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P19-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P19-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P20-S1-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P21-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P21-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P21-S2-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P21-S2-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P21-S2-C14
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P26-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P27-S2-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P27-S2-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P28-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P28-S2-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: tested_personal_effects
        source_id: P1-S1-C2
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P17-S1-C2
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P17-S1-C7
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P18-S1-C4
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P19-S1-C2
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P19-S1-C6
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P28-S1-C6
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: analysed_sample
        source_ids:
        - P1-S1-C1
        - P6-S1-C1
        - P17-S1-C9
        - P17-S2-C12
        - P18-S1-C4
        - P18-S1-C6
        - P18-S1-C7
        - P19-S1-C2
        - P19-S1-C4
        - P19-S1-C5
        - P19-S1-C6
        - P20-S1-C3
        - P21-S2-C9
        - P26-S1-C7
        - P26-S2-C12
        - P29-S1-C5
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: outcome_definition
        source_ids:
        - P5-S1-C12
        - P5-S1-C13
        - P5-S2-C5
        - P21-S1-C4
        - P21-S1-C6
        - P21-S1-C7
        - P21-S2-C4
        - P21-S2-C9
        - P26-S1-C7
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: limitations
        source_ids:
        - P5-S1-C14
        - P5-S1-C15
        - P5-S1-C16
        - P16-S2-C8
        - P21-S1-C11
        - P21-S1-C12
        - P21-S1-C14
        - P21-S2-C10
        - P26-S1-C10
        - P26-S2-C3
        - P26-S2-C6
        - P27-S1-C5
        - P27-S1-C6
        - P27-S1-C8
        - P27-S2-C2
        - P27-S2-C3
        - P27-S2-C4
        - P28-S1-C1
        - P28-S1-C4
        - P28-S2-C12
        - P28-S2-C13
        - P29-S1-C2
        - P29-S1-C11
        - P31-S1-C5
        - P31-S1-C10
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: personal_factors
        source_ids:
        - P1-S1-C2
        - P4-S2-C3
        - P5-S1-C6
        - P5-S1-C8
        - P5-S1-C9
        - P5-S1-C10
        - P5-S1-C11
        - P17-S1-C2
        - P17-S1-C7
        - P17-S1-C10
        - P17-S1-C11
        - P27-S2-C5
        - P28-S1-C5
        - P29-S1-C5
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: tested_personal_effects
        source_ids:
        - P1-S1-C4
        - P17-S2-C14
        - P17-S2-C15
        - P18-S1-C1
        - P18-S1-C2
        - P18-S1-C3
        - P18-S1-C6
        - P18-S1-C7
        - P19-S1-C4
        - P19-S1-C5
        - P20-S1-C3
        - P27-S2-C6
        - P27-S2-C8
        - P28-S1-C5
        - P29-S1-C7
        - P29-S1-C8
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: descriptive_personal_factors
        source_ids:
        - P1-S1-C2
        - P3-S2-C3
        - P3-S2-C4
        - P3-S2-C6
        - P3-S2-C7
        - P4-S2-C3
        - P5-S1-C6
        - P5-S1-C8
        - P5-S1-C9
        - P5-S1-C10
        - P5-S1-C11
        - P6-S1-C1
        - P16-S1-C2
        - P16-S1-C3
        - P16-S1-C4
        - P16-S1-C5
        - P16-S1-C6
        - P16-S1-C7
        - P17-S1-C10
        - P17-S1-C11
        - P17-S1-C12
        - P17-S1-C13
        - P17-S1-C14
        - P17-S1-C15
        - P17-S1-C16
        - P17-S1-C17
        - P17-S1-C18
        - P17-S1-C19
        - P18-S1-C6
        - P18-S1-C7
        - P19-S1-C4
        - P20-S1-C7
        - P20-S1-C8
        - P20-S2-C5
        - P20-S2-C6
        - P20-S2-C10
        - P20-S2-C12
        - P20-S2-C13
        - P26-S1-C1
        - P26-S1-C3
        - P26-S2-C12
        - P27-S1-C9
        - P27-S2-C5
        - P29-S1-C5
        - P29-S1-C7
        - P31-S1-C13
        - P31-S1-C14
        - P31-S1-C15
        - P31-S1-C16
        - P31-S1-C17
        - P31-S2-C5
        - P31-S2-C8
        - P31-S2-C9
        - P33-S1-C9
        - P33-S1-C14
        - P33-S1-C19
        - P33-S1-C20
        - P33-S1-C21
        - P33-S2-C10
        - P33-S2-C11
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - analysed_sample
      - imaging_timing
      - outcome_definition
      - validation
      - limitations
      - personal_factors
      - tested_personal_effects
      - adjustment_roles
      - explicitly_not_adjusted
      - descriptive_personal_factors
      unclassified_extraction_ids:
      - P16-S3-C3
      table_review_required:
      - TABLE-1-page-10-3
      - TABLE-1-page-12-4
      - TABLE-1-page-14-5
      - TABLE-1-page-6-1
      - TABLE-1-page-8-2
      - TABLE-2-page-18-6
      - TABLE-3-page-18-7
      - TABLE-4-page-19-8
      - TABLE-5-page-19-9
      - TABLE-6-page-22-10
      - TABLE-6-page-23-11
      - TABLE-6-page-24-12
      - TABLE-6-page-25-13
      - TABLE-7-page-26-14
      unlinked_tables:
      - TABLE-1-page-10-3
      - TABLE-1-page-12-4
      - TABLE-1-page-14-5
      - TABLE-1-page-6-1
      - TABLE-1-page-8-2
      - TABLE-5-page-19-9
      - TABLE-6-page-22-10
      - TABLE-6-page-23-11
      - TABLE-6-page-24-12
      - TABLE-6-page-25-13
      - TABLE-7-page-26-14
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
      pdf_sha256: 1e0ddf98a41068c3306d0356e708c9e06e6a8e29aee9ba8f28cca59497060866
      source_review: _compare/relationships-2026-11-16/review-current/Coppens2002
      source_status_sha256: b23efd9d623a174e8b3db29c3ee463c334a29227e35da9b8cbb59c60abbec094
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C3
      disposition: represented
      result_indexes:
      - 0
      reason: States CA population is comparable to LHA population.
    - source_id: P1-S1-C4
      disposition: represented
      result_indexes:
      - 1
      reason: Males more likely to show familial sinistrality.
    - source_id: P1-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: General observation about reporting of right-hemisphere symptoms.
    - source_id: P4-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Case inclusion detail.
    - source_id: P4-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Case inclusion detail.
    - source_id: P4-S2-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Case inclusion detail.
    - source_id: P4-S2-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Case inclusion detail.
    - source_id: P5-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Case inclusion detail.
    - source_id: P5-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Case inclusion detail.
    - source_id: P5-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Case inclusion detail.
    - source_id: P5-S2-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Methodological detail on aphasia labeling.
    - source_id: P17-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statistical method limitation.
    - source_id: P17-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive statistic (mean age).
    - source_id: P17-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive statistic (gender ratio).
    - source_id: P17-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive statistic (aphasia distribution).
    - source_id: P17-S1-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive statistic (aphasia distribution).
    - source_id: P17-S1-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive observation of age differences between aphasia types.
    - source_id: P17-S1-C15
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive statistics for age by aphasia type.
    - source_id: P17-S1-C16
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive statistic (familial sinistrality frequency).
    - source_id: P17-S1-C17
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive statistic (familial sinistrality frequency).
    - source_id: P17-S1-C18
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive statistic (subtype frequency).
    - source_id: P17-S1-C19
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive statistic (subtype frequency).
    - source_id: P17-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive statistic (oral/written skills).
    - source_id: P17-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive statistic (oral/written skills).
    - source_id: P17-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive statistic (oral/written skills).
    - source_id: P17-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive statistic (oral/written discrepancy).
    - source_id: P17-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive statistic (apraxia frequency).
    - source_id: P17-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive statistic (apraxia types).
    - source_id: P17-S2-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive statistic (neglect frequency).
    - source_id: P17-S2-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of analysis variables.
    - source_id: P17-S2-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to Table 2.
    - source_id: P17-S2-C14
      disposition: represented
      result_indexes:
      - 2
      reason: No age difference between males and females.
    - source_id: P17-S2-C15
      disposition: represented
      result_indexes:
      - 2
      reason: No differences between males and females for subtype, oral/written discrepancy,
        apraxia, or neglect.
    - source_id: P18-S1-C1
      disposition: represented
      result_indexes:
      - 2
      reason: No differences between males and females for subtype, oral/written discrepancy,
        apraxia, or neglect.
    - source_id: P18-S1-C2
      disposition: represented
      result_indexes:
      - 1
      reason: Significant difference in frequency of familial sinistrality between
        genders.
    - source_id: P18-S1-C3
      disposition: represented
      result_indexes:
      - 1
      reason: Familial sinistrality more frequent in males.
    - source_id: P18-S1-C6
      disposition: represented
      result_indexes:
      - 3
      reason: No significant age difference between CA patients with or without familial
        sinistrality.
    - source_id: P18-S1-C7
      disposition: represented
      result_indexes:
      - 3
      reason: No difference based on CA subtype, oral/written discrepancy, apraxia,
        or neglect for familial sinistrality.
    - source_id: P19-S1-C1
      disposition: represented
      result_indexes:
      - 3
      reason: No difference based on CA subtype, oral/written discrepancy, apraxia,
        or neglect for familial sinistrality.
    - source_id: P19-S1-C4
      disposition: represented
      result_indexes:
      - 4
      reason: No age difference between CA subtypes.
    - source_id: P19-S1-C5
      disposition: represented
      result_indexes:
      - 4
      reason: No significant differences between subtypes for oral/written discrepancy,
        apraxia, or neglect.
    - source_id: P19-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statistical limitation due to sample size.
    - source_id: P19-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Listing features where analysis could not be performed.
    - source_id: P20-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement on non-significant results.
    - source_id: P20-S1-C3
      disposition: represented
      result_indexes:
      - 5
      - 6
      reason: No difference in aphasia type distribution across gender or oral/written
        discrepancy.
    - source_id: P20-S1-C7
      disposition: represented
      result_indexes:
      - 0
      reason: Mean age of CA patients similar to LHA.
    - source_id: P20-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison of mean ages.
    - source_id: P20-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Contradiction of prior studies on age.
    - source_id: P20-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation on age difference between Broca's and Wernicke's aphasia.
    - source_id: P20-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation on age difference between aphasia types.
    - source_id: P20-S1-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison of aphasia distribution with prior report.
    - source_id: P20-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion on Broca aphasia frequency.
    - source_id: P20-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion on Broca aphasia frequency.
    - source_id: P20-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive gender ratio.
    - source_id: P20-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison of gender ratio with prior reports.
    - source_id: P20-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Contradiction of prior report on gender.
    - source_id: P20-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of gender and lateralization hypothesis.
    - source_id: P20-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement on population characteristics.
    - source_id: P20-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison of familial sinistrality rate with prior report.
    - source_id: P20-S2-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive statistic for familial sinistrality.
    - source_id: P20-S2-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation on subtype distribution.
    - source_id: P20-S2-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison of subtype distribution with prior report.
    - source_id: P20-S2-C16
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive subtype percentages.
    - source_id: P21-S1-C3
      disposition: represented
      result_indexes:
      - 0
      reason: CA patients comparable to LHA in age, gender, and aphasia type.
    - source_id: P21-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive statistic (oral/written equivalence).
    - source_id: P21-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive statistic (oral/written discrepancy).
    - source_id: P21-S1-C15
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement on apraxia frequency discrepancies.
    - source_id: P21-S2-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive statistics for specific apraxia types.
    - source_id: P21-S2-C15
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison of apraxia figures with prior reviews.
    - source_id: P21-S2-C16
      disposition: represented
      result_indexes:
      - 8
      reason: Oral apraxia more prevalent than limb apraxia.
    - source_id: P25-S1-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of prevalence of constructional apraxia.
    - source_id: P26-S1-C7
      disposition: represented
      result_indexes:
      - 9
      reason: Distribution of constructional apraxia types (L vs R features).
    - source_id: P26-S1-C8
      disposition: represented
      result_indexes:
      - 9
      reason: Constructional praxis lateralizes with language skills.
    - source_id: P26-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement on inability to compute apraxia of speech frequency.
    - source_id: P26-S1-C12
      disposition: represented
      result_indexes:
      - 10
      reason: Apraxia of speech associated with Broca's aphasia.
    - source_id: P27-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation on reporting of right-hemisphere signs.
    - source_id: P27-S2-C6
      disposition: represented
      result_indexes:
      - 2
      reason: No significant differences between males and females in CA symptomatology.
    - source_id: P27-S2-C8
      disposition: represented
      result_indexes:
      - 1
      reason: Males have a significantly higher probability of familial sinistrality.
    - source_id: P28-S1-C5
      disposition: represented
      result_indexes:
      - 3
      reason: No symptom differences identified when familial sinistrality is the
        independent variable.
    - source_id: P28-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of familial sinistrality in males vs females.
    - source_id: P28-S1-C14
      disposition: represented
      result_indexes:
      - 3
      reason: Familial sinistrality not more likely to entail anomalous CA cases.
    - source_id: P28-S2-C3
      disposition: represented
      result_indexes:
      - 4
      reason: CA subtype did not yield significant differences between major symptoms.
    - source_id: P29-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement on data analysis.
    - source_id: P29-S1-C5
      disposition: represented
      result_indexes:
      - 0
      reason: CA patients comparable to LHA in age, gender, and aphasia type.
    - source_id: P29-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Summary of findings on praxis and right-hemisphere symptoms.
    - source_id: P29-S1-C7
      disposition: represented
      result_indexes:
      - 2
      - 3
      - 4
      reason: Gender, familial sinistrality, and CA type do not influence CA symptomatology.
    - source_id: P29-S1-C8
      disposition: represented
      result_indexes:
      - 1
      reason: Males have significantly higher probability of positive familial sinistrality.
    unresolved_coverage:
    - source_id: P17-S2-C12
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P17-S2-C13
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P20-S2-C8
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P26-S1-C8
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P26-S1-C12
      disposition: unresolved
      reason: Unknown result index; not accepted as coverage
    - source_id: P20-S1-C15
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P26-S2-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P26-S2-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P26-S2-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P28-S2-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P28-S2-C14
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P28-S2-C15
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P28-S3-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P29-S2-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P30-S2-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P30-S2-C13
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P30-S2-C18
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P31-S1-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P31-S1-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P31-S1-C26
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P33-S1-C14
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P33-S1-C19
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P33-S1-C20
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P33-S1-C21
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P33-S2-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P33-S2-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C5
    - P4-S2-C6
    - P4-S2-C8
    - P4-S2-C11
    - P4-S2-C12
    - P5-S1-C1
    - P5-S1-C2
    - P5-S1-C4
    - P5-S2-C13
    - P17-S1-C5
    - P17-S1-C10
    - P17-S1-C11
    - P17-S1-C12
    - P17-S1-C13
    - P17-S1-C14
    - P17-S1-C15
    - P17-S1-C16
    - P17-S1-C17
    - P17-S1-C18
    - P17-S1-C19
    - P17-S2-C4
    - P17-S2-C5
    - P17-S2-C6
    - P17-S2-C8
    - P17-S2-C9
    - P17-S2-C10
    - P17-S2-C11
    - P19-S1-C8
    - P19-S1-C9
    - P20-S1-C2
    - P20-S1-C8
    - P20-S1-C9
    - P20-S1-C10
    - P20-S1-C12
    - P20-S1-C14
    - P20-S1-C15
    - P20-S2-C3
    - P20-S2-C4
    - P20-S2-C5
    - P20-S2-C6
    - P20-S2-C7
    - P20-S2-C9
    - P20-S2-C10
    - P20-S2-C12
    - P20-S2-C13
    - P20-S2-C14
    - P20-S2-C16
    - P21-S1-C3
    - P21-S1-C6
    - P21-S1-C7
    - P21-S1-C15
    - P21-S2-C14
    - P21-S2-C15
    - P25-S1-C13
    - P26-S1-C11
    - P26-S2-C3
    - P26-S2-C4
    - P26-S2-C9
    - P27-S1-C5
    - P28-S1-C8
    - P28-S1-C14
    - P28-S2-C9
    - P28-S2-C14
    - P28-S2-C15
    - P28-S3-C2
    - P29-S1-C1
    - P29-S1-C6
    - P29-S2-C3
    - P30-S2-C9
    - P30-S2-C13
    - P30-S2-C18
    - P31-S1-C4
    - P31-S1-C6
    - P31-S1-C26
    - P33-S1-C14
    - P33-S1-C19
    - P33-S1-C20
    - P33-S1-C21
    - P33-S2-C8
    - P33-S2-C10
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-10-3
    - TABLE-1-page-12-4
    - TABLE-1-page-14-5
    - TABLE-1-page-6-1
    - TABLE-1-page-8-2
    - TABLE-2-page-18-6
    - TABLE-3-page-18-7
    - TABLE-4-page-19-8
    - TABLE-5-page-19-9
    - TABLE-6-page-22-10
    - TABLE-6-page-23-11
    - TABLE-6-page-24-12
    - TABLE-6-page-25-13
    - TABLE-7-page-26-14
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample: []
      recruited_sample:
      - P1-S1-C1
      - P4-S1-C9
      - P17-S1-C9
      - P21-S2-C4
      - P25-S2-C4
      - P26-S2-C12
      - P29-S1-C5
      eligibility:
      - P4-S1-C10
      - P4-S2-C4
      - P4-S2-C10
      - P4-S2-C11
      - P17-S2-C7
      - P21-S1-C2
      - P21-S2-C5
      - P21-S2-C7
      imaging_provenance:
      - P31-S1-C8
      imaging_timing: []
      outcome_timing:
      - P5-S1-C17
      - P5-S2-C3
      - P5-S2-C4
      - P5-S2-C7
      - P21-S1-C13
      - P21-S2-C8
      - P33-S1-C10
      - P33-S1-C11
      outcome_definition: []
      validation: []
      analysis_restrictions:
      - P17-S1-C5
      - P19-S1-C8
      - P19-S1-C9
      - P20-S1-C11
      - P21-S1-C14
      dependent_variable_statement:
      - P1-S1-C2
      - P4-S1-C9
      - P17-S1-C2
      - P17-S1-C7
      limitations: []
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles: []
      explicitly_not_adjusted: []
      descriptive_personal_factors: []
    outcome_type: both_reported
    imaging_vs_outcome: not_stated
    validation_type: none_described
    window_merge: Union of selected IDs; differing window enums retained conservatively
      as both/mixed. Not verified study-level facts.
    held_selections:
    - slot: dependent_variable_statement
      source_id: P18-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P19-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P19-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P20-S1-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P21-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P21-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P21-S2-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P21-S2-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P21-S2-C14
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P26-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P27-S2-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P27-S2-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P28-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P28-S2-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: tested_personal_effects
      source_id: P1-S1-C2
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P17-S1-C2
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P17-S1-C7
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P18-S1-C4
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P19-S1-C2
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P19-S1-C6
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P28-S1-C6
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: analysed_sample
      source_ids:
      - P1-S1-C1
      - P6-S1-C1
      - P17-S1-C9
      - P17-S2-C12
      - P18-S1-C4
      - P18-S1-C6
      - P18-S1-C7
      - P19-S1-C2
      - P19-S1-C4
      - P19-S1-C5
      - P19-S1-C6
      - P20-S1-C3
      - P21-S2-C9
      - P26-S1-C7
      - P26-S2-C12
      - P29-S1-C5
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: outcome_definition
      source_ids:
      - P5-S1-C12
      - P5-S1-C13
      - P5-S2-C5
      - P21-S1-C4
      - P21-S1-C6
      - P21-S1-C7
      - P21-S2-C4
      - P21-S2-C9
      - P26-S1-C7
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: limitations
      source_ids:
      - P5-S1-C14
      - P5-S1-C15
      - P5-S1-C16
      - P16-S2-C8
      - P21-S1-C11
      - P21-S1-C12
      - P21-S1-C14
      - P21-S2-C10
      - P26-S1-C10
      - P26-S2-C3
      - P26-S2-C6
      - P27-S1-C5
      - P27-S1-C6
      - P27-S1-C8
      - P27-S2-C2
      - P27-S2-C3
      - P27-S2-C4
      - P28-S1-C1
      - P28-S1-C4
      - P28-S2-C12
      - P28-S2-C13
      - P29-S1-C2
      - P29-S1-C11
      - P31-S1-C5
      - P31-S1-C10
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: personal_factors
      source_ids:
      - P1-S1-C2
      - P4-S2-C3
      - P5-S1-C6
      - P5-S1-C8
      - P5-S1-C9
      - P5-S1-C10
      - P5-S1-C11
      - P17-S1-C2
      - P17-S1-C7
      - P17-S1-C10
      - P17-S1-C11
      - P27-S2-C5
      - P28-S1-C5
      - P29-S1-C5
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: tested_personal_effects
      source_ids:
      - P1-S1-C4
      - P17-S2-C14
      - P17-S2-C15
      - P18-S1-C1
      - P18-S1-C2
      - P18-S1-C3
      - P18-S1-C6
      - P18-S1-C7
      - P19-S1-C4
      - P19-S1-C5
      - P20-S1-C3
      - P27-S2-C6
      - P27-S2-C8
      - P28-S1-C5
      - P29-S1-C7
      - P29-S1-C8
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: descriptive_personal_factors
      source_ids:
      - P1-S1-C2
      - P3-S2-C3
      - P3-S2-C4
      - P3-S2-C6
      - P3-S2-C7
      - P4-S2-C3
      - P5-S1-C6
      - P5-S1-C8
      - P5-S1-C9
      - P5-S1-C10
      - P5-S1-C11
      - P6-S1-C1
      - P16-S1-C2
      - P16-S1-C3
      - P16-S1-C4
      - P16-S1-C5
      - P16-S1-C6
      - P16-S1-C7
      - P17-S1-C10
      - P17-S1-C11
      - P17-S1-C12
      - P17-S1-C13
      - P17-S1-C14
      - P17-S1-C15
      - P17-S1-C16
      - P17-S1-C17
      - P17-S1-C18
      - P17-S1-C19
      - P18-S1-C6
      - P18-S1-C7
      - P19-S1-C4
      - P20-S1-C7
      - P20-S1-C8
      - P20-S2-C5
      - P20-S2-C6
      - P20-S2-C10
      - P20-S2-C12
      - P20-S2-C13
      - P26-S1-C1
      - P26-S1-C3
      - P26-S2-C12
      - P27-S1-C9
      - P27-S2-C5
      - P29-S1-C5
      - P29-S1-C7
      - P31-S1-C13
      - P31-S1-C14
      - P31-S1-C15
      - P31-S1-C16
      - P31-S1-C17
      - P31-S2-C5
      - P31-S2-C8
      - P31-S2-C9
      - P33-S1-C9
      - P33-S1-C14
      - P33-S1-C19
      - P33-S1-C20
      - P33-S1-C21
      - P33-S2-C10
      - P33-S2-C11
      reason: Runaway selection (>8 passages); entire slot requires source review
    policy: All slots and enums remain unverified. Held selections are not evidence
      of absence. Original responses are preserved in frame/chunk-*/attempt-*/raw.json.
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
      pdf_sha256: 1e0ddf98a41068c3306d0356e708c9e06e6a8e29aee9ba8f28cca59497060866
      review_sha256: 3d3639b15bf67edde5fd481a6aacd66b70c50bd9fcec6baabfc53381f1004181
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
      - P26-S1-C7
      - P26-S1-C8
      source_result: Among 55 cases of reported constructional apraxia in patients
        with crossed aphasia, 22 exhibited features typical of left-hemisphere lesions,
        9 exhibited features typical of right-hemisphere lesions, 2 showed both, and
        22 were undetermined. The authors conclude that these figures suggest constructional
        praxis lateralizes with language skills.
      result_status: detected
      patient_measurement: non_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis corresponds to the distribution of constructional
            apraxia types (left vs. right hemisphere features) in the crossed aphasia
            population, as described in P26-S1-C7 and P26-S1-C8. The proposed core
            correctly identifies this as the specific analysis being reviewed.
          source_ids:
          - P26-S1-C7
          - P26-S1-C8
        direction:
          answer: fits
          reason: The source states that 22 patients showed left-hemisphere features
            compared to 9 with right-hemisphere features, leading to the conclusion
            that constructional praxis lateralizes with language skills. The proposed
            core correctly captures this direction (association with language lateralization)
            and the specific counts.
          source_ids:
          - P26-S1-C7
          - P26-S1-C8
        construct:
          answer: fits
          reason: The exposure is crossed aphasia, and the outcome is the type of
            constructional apraxia (left vs. right hemisphere features). The measurement
            is based on clinical descriptions and drawings (cube), which is a non-imaging
            clinical assessment, not diffusion or functional imaging. The proposed
            core correctly identifies the exposure, outcome, and measurement method.
          source_ids:
          - P26-S1-C3
          - P25-S1-C6
          - P26-S1-C7
        qualifications:
          answer: fits
          reason: The proposed core includes the specific counts (22 L, 9 R, 2 both,
            22 undetermined) which are material to the interpretation of the 'lateralization'
            claim. It also includes limitations regarding the nonstandardized nature
            of the data and the potential for right-hemisphere features to overshadow
            left-hemisphere ones in severe cases, which are present in the source
            (P26-S1-C9, P29-S1-C11).
          source_ids:
          - P26-S1-C7
          - P26-S1-C9
          - P29-S1-C11
        missing_material_caveat:
          answer: fits
          reason: The core includes the necessary caveats about the variability in
            definition of constructional apraxia and the nonstandardized case descriptions.
            It does not omit any material qualifier that would change the interpretation
            of the lateralization finding.
          source_ids:
          - P25-S1-C5
          - P29-S1-C11
          - P26-S1-C9
      optional_pending:
      - Sample size requires source confirmation; it has not been transcribed.
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Sample size requires source confirmation; it has not been transcribed.
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Sample size requires source confirmation; it has not been transcribed.
    normalizations:
    - field: sample.n
      original: 115
      action: not_transcribed
      reason: Not supported by selected quotations
    analysis_identity:
      id: R009
      exposure:
        text: crossed aphasia
      outcome:
        text: constructional apraxia type (left-hemisphere vs right-hemisphere features)
      analysis_label: Constructional praxis lateralization
      relation: association
      evidence_ids:
      - P26-S1-C7
      - P26-S1-C8
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
        pdf_sha256: 1e0ddf98a41068c3306d0356e708c9e06e6a8e29aee9ba8f28cca59497060866
        source_review: _compare/relationships-2026-11-16/review-current/Coppens2002
        source_status_sha256: b23efd9d623a174e8b3db29c3ee463c334a29227e35da9b8cbb59c60abbec094
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P5-S2-C3:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 1e0ddf98a41068c3306d0356e708c9e06e6a8e29aee9ba8f28cca59497060866
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 17dad08d6e6b1c365d4916fa9d39bf59265b32616268b4ec438520e64b0b6f38
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P5-S2-C3
          page: 5
          text_layer_sha256: 17dad08d6e6b1c365d4916fa9d39bf59265b32616268b4ec438520e64b0b6f38
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Whenever

          possible, the diagnosis in the subacute period was used (i.e., 3 weeks to
          2 months

          postonset).'
        anchor_text: 'Whenever

          possible, the diagnosis in the subacute period was used (i.e., 3 weeks to
          2 months

          postonset).'
        excluded_fragments: []
        image_sha256: c52fd38813bf529ad47d19d5e5828b66549b079787dce8e98ee87c79c0594df6
        transcription: '. Whenever

          possible, the diagnosis in the subacute period was used (i.e., 3 weeks to
          2 months

          postonset)'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 26
  quote: 'Among the 55 cases (57.9% of patients assessed) of reported constructional
    apraxia,

    22 patients performed similarly to typical left-hemisphere stroke patients, 9
    patients

    similarly to a typical right-hemisphere lesion, 2 patients showed both left- and
    right-

    hemisphere features, and the type of constructional apraxia could not be determined

    in the remaining 22 patients.'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-23'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
