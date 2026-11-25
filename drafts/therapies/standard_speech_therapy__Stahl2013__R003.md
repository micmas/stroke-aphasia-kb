---
id: standard_speech_therapy
name: standard speech therapy
kind: therapy
findings:
- id: f1
  target: non_formulaic_speech_production
  target_kind: impairment
  claim: Patients receiving standard therapy improved their production of non-formulaic
    speech, in contrast to patients receiving singing or rhythmic therapy, who did
    not.
  direction: likely
  relationship: treatment_response
  method: behavioral_only
  sample:
    n: 15
    population: Not transcribed; confirm from the original PDF population and timing
      passages.
    phase: not_reported
    time_post_onset: Measured before and after 6 weeks of treatment.
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Small sample size (n=15 total across three groups).
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Speech therapy that did not include singing, rhythmic
    speech, or training with formulaic phrases, consisting of elements such as multi-modal
    stimulation, simplifying strategies, phonetic/phonemic approaches, tactile-kinaesthetic
    speech-motor treatment, and communicative-pragmatic approaches. The improvement
    in non-formulaic speech is described as a training transfer to the production
    of unknown phrases. Additional metadata has not been transcribed; review the pending-field
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
    - not_transcribed:sample.population
    - proposed_concept:non_formulaic_speech_production
  therapy:
    id: standard_speech_therapy
    name: standard speech therapy
  citation: '@Stahl2013'
  source_passages:
  - section: Original source P1-S2-C5
    page: 1
    quote: 'They did, however, improve their production of non-formulaic speech,

      in contrast to singing and rhythmic therapy patients, who did not.'
    supports: claim
  - section: Original source P8-S1-C4
    page: 8
    quote: 'For the pro-

      duction of non-formulaic lyrics, the results yielded the reverse

      pattern: only standard therapy patients improved (M = 6.21,

      95% CI [3.96, 8.47]), which was not the case with singing and

      rhythmic therapy patients (M = −0.36, 95% CI [−2.62, 1.90];

      M = −0.50, 95% CI [−2.76, 1.76]).'
    supports: claim
  - section: Original source P8-S2-C10
    page: 8
    quote: 'Panel (B): standard therapy

      patients improved their production of non-formulaic speech (“Bright forest,

      there at the boat, thin like oak. . .”), in contrast to singing and rhythmic

      therapy patients, who did not.'
    supports: claim
  - section: Original source P8-S2-C11
    page: 8
    quote: 'Hence, only standard therapy patients showed

      a training transfer to the production of unknown phrases.'
    supports: claim
  - section: Original source P2-S3-C8
    page: 2
    quote: Fifteen stroke patients were included in the study.
    supports: sample
  - section: Original source P2-S3-C13
    page: 2
    quote: 'To restrict inﬂuences related

      to spontaneous recovery, all patients were at least 6 months post-

      infarction at the time of testing, suggesting a chronic post-stroke

      stage.'
    supports: sample
  - section: Original source P3-S2-C16
    page: 3
    quote: 'In standard therapy, patients attended

      speech therapy that did not include singing, rhythmic speech,

      or training with formulaic phrases.'
    supports: sample
  - section: Original source P6-S1-C8
    page: 6
    quote: 'All patients underwent three

      1-h long, weekly training sessions, over a period of 6 weeks.'
    supports: method
  - section: Original source P6-S2-C13
    page: 6
    quote: 'For the purpose of standardizing speech therapy, an

      experienced clinical linguist was asked to compose commonly

      used elements in the treatment of non-ﬂuent aphasia and apraxia

      of speech.'
    supports: method
  - section: Original source P6-S2-C15
    page: 6
    quote: 'The most frequent ele-

      ments applied include: multi-modal stimulation (receptive: cate-

      gorization, word-picture matching; expressive: repetition, reading

      aloud, naming, writing); simplifying strategies (“reduced syntax

      therapy”; Springer et al., 2000); phonetic or phonemic approach

      (“minimal contrast treatment”; Wambaugh et al., 1996); tactile-

      kinaesthetic speech-motor treatment (“prompts for restructuring

      '
    supports: method
  - section: Original source P6-S3-C1
    page: 6
    quote: 'therapy”; Springer et al., 2000); phonetic or phonemic approach

      (“minimal contrast treatment”; Wambaugh et al., 1996); tactile-

      kinaesthetic speech-motor treatment (“prompts for restructuring

      oral and muscular phonetic targets”; Square-Storer and Hayden,

      1989); and communicative-pragmatic approach (“promoting

      aphasics’ communicative effectiveness”; Davis and Wilcox, 1985).'
    supports: method
  - section: Original source P7-S2-C9
    page: 7
    quote: 'Articulatory quality was denoted as

      the percentage of correct syllables in each condition.'
    supports: method
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-25'
relationship_review:
  paper: Stahl2013
  proposal_id: R003
  review_status_sha256: 31f9f54b9fced7bd95bc6dd6138a079e97da4417760958919c722b666b6ab8ec
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 4d6f39b654a42bd162658c3b70546f73bc72f8bd249ee1d0d9a12468af0db177
    original_review_binding:
      version: relationship-review-v5
      input_hashes:
        pdf: 4d6f39b654a42bd162658c3b70546f73bc72f8bd249ee1d0d9a12468af0db177
        A/passages.json: 5b4c48cd8154f46fac9ebd4cc1c524f1908b7f05dc6e783a46ce04285caf6753
        A/raw.json: 3afc44b0560dcda2ecbed6e3e93ff1e829665e8d11f3a824a7c51c46873d213f
        A/source-units.json: db7af196b55b8ab6f1870d177861f0ee723a5e5bc02b8677a2bceba44b8e8532
        A/full-source-units.json: c06770fce10bb954eb64d4cbe695f8380bf8f3e224ddf593854d981f112ab1e7
        A/meta.json: f5ce199380f3864536bac856c9429ea6ff62f06e1c9b45209bdcbf37d0a26ba7
        A/table-images/TABLE-5-page-9-2.png: 39741739f5e0d0237f8fec5e381973cb4fc864b8a33bbc7443d6f2f19edd32f2
        A/table-images/TABLE-1-page-3-1.png: f80b341a465596cd130fd639695ba9cb4acb95aba890d5f81e0faddfbc72af6c
        A/table-images/TABLE-4-page-9-1.png: 39741739f5e0d0237f8fec5e381973cb4fc864b8a33bbc7443d6f2f19edd32f2
        A/table-images/page-3.png: 6fa5c22b28207c1f4fca0f2556a5ed8a38de8392b73b5216e5d9e8773f8aef42
        A/table-images/page-5.png: 6022bb4f63e7566747ce5ef73602f592b5acce92bc52f02de2b26e4069cbc601
        A/table-images/page-4.png: 6694df46850026252c3fbeb4e8ea3d529f759f4b647eedabaff5ac3268a9bb43
        A/table-images/page-9.png: be808f7a2f08ae9a1cf432b328337cbc52b1574fee7f89dd9f9cb9c1977bce7e
        A/table-images/manifest.json: 9586a3a9f19919f46c4061b470e39c184aec75e78ead99036a2b7665e5cd0155
        A/table-images/TABLE-2-page-4-1.png: e5a2677e4d2e651f60578e482376667da88d354f3a4bf1cb4b4e983c0de1c896
        A/table-images/TABLE-3-page-5-1.png: dedd2ac6598ca47152fd93cf04a82dc40b0645171e638a8be651b6f2065edb81
        A/clauses/window-11/raw.json: 3b6369f8a60c3cac716f26386dfad72b09fe30fc763d7e1e0b7a459c62293eb5
        A/clauses/window-11/prompt.txt: c5d16367db496109d9612faf2e1ecd1fb67f33208804b0059eed4eaf8e1e9c85
        A/clauses/window-11/meta.json: d6ad255f9d98d8b85b20e547ebb80b4d437ec1aca81fe6d6ca2a55ba9eead799
        A/clauses/window-10/raw.json: cc04070f5b72934b62aff75080eebb2cadab1925b3d54cfea201972b0433bfe5
        A/clauses/window-10/prompt.txt: dad14067f86a90affaa485c2ac0ce7c961b1bae43ad60c1a9752bb3c8e12c810
        A/clauses/window-10/meta.json: 3d92beaf1202d977ef9edf2518110ffa282d75ef6d410f852cc919ad3fc8682b
        A/clauses/window-03/raw.json: 9450beed7464783548c2402255575869a471fe87dfc9eee757126e98050f8bab
        A/clauses/window-03/prompt.txt: f1469ee1e69a4843abe4c0a25d92766c8db2bd57cb3076d651c3af64d2418f38
        A/clauses/window-03/meta.json: 4c8677e61c319aa5b7842decaa41c5e58d9aebf5093d90f23ff574dfb7668fca
        A/clauses/window-04/raw.json: 4fdb0800f03e8e1acc9982ba6bd76a65f76e9c1c179d3f8fa49e13a3f020b6a3
        A/clauses/window-04/prompt.txt: 29a6eb8cd9a4326a5ee6e002103673d34323290b7717140f224e8406a36932be
        A/clauses/window-04/meta.json: 6822d8d20ddc9499c0cf13324054fcf7b539bad0664391b452a6a9f77c64380c
        A/clauses/window-05/raw.json: 8f143e915c39fcc3b176af0ff3d1d384efedebe5728190eb327ae7c7bbeaec99
        A/clauses/window-05/prompt.txt: f5c0ae1b1d347fbbd665ea182ef2c2377ab665bbe0af008ffc4371a726d55a97
        A/clauses/window-05/meta.json: e5c743c805f9dabe86adc34edf11654df00165a3ec78c5b88d3004c7eef0fc0e
        A/clauses/window-02/raw.json: a565c308274c867125178685c7efa600f24f31549b65062daad02abf512cb955
        A/clauses/window-02/prompt.txt: f1323d5a6b8c2df29f17d4b81b0ed44555871539f824eb4c7b137493b9a96238
        A/clauses/window-02/meta.json: 859d381cd3748cfe2919304ac293e093648fb0dc934eba4df85272faacaec2f5
        A/clauses/window-12/raw.json: 027642f047fe960c38f0c3f72d1c4a1a01aca5f0b6f7e300edd20587b58e0994
        A/clauses/window-12/prompt.txt: 6b44db02517bf4f68c5ed1f11c2157a82e3edb6ad10b21c419fb3e449d98c5fe
        A/clauses/window-12/meta.json: 938d55fffcf253ba6e3c85560c65fe2ddeaca43e2de8448b7930f17c8cef530e
        A/clauses/window-13/raw.json: 3a95a81e73b998534aafa20583788ee34ca90a418526fad8b260ba797cb9d551
        A/clauses/window-13/prompt.txt: a3b6fca1b58712c2523e27907b6947f74d3e9ac7ca26d86476be1ef51575d6a3
        A/clauses/window-13/meta.json: fb5da00297c4ce49d81eab6617cfe79e5f82dd91dfe924b437a220e84f3b24cf
        A/clauses/window-09/raw.json: ce41ed6faa4decc6a07de8b865294e8a8dfdfd3983d61cae3d202c0950e44f02
        A/clauses/window-09/prompt.txt: 9c828b6f304ab81b380678fd712665728518e56b101eb3a0bed6349227a6e9b6
        A/clauses/window-09/meta.json: 8797a4728487fda17468336c5d3c0bb49a01070b8487ea9d3cabf783018ba53a
        A/clauses/window-07/raw.json: a5b40a1b684ee243d65282bf041ba6aebc4f527a4a2e0ee51823e94e1fe41b0e
        A/clauses/window-07/prompt.txt: a308093ca6b5d01cb477c4db40872b406d05751e6f26f92ac11707f651a79f27
        A/clauses/window-07/meta.json: c2b2e1b46d871177e16dc97a8348dc6a4f6b3dae917e89f1962b69dd9b1f25d9
        A/clauses/window-01/raw.json: 115a47a10220c38d06e5ed09c77800c5284b2afb73b962ce15ce9d8c575bc13a
        A/clauses/window-01/prompt.txt: afb1193c640f7b67d72a33e591e10042bcd0243c9abcf08ec65bb41cbd7ac8dc
        A/clauses/window-01/meta.json: e664bf900364eb7aa572cbea99dd2bd5fb6f3081b26cf58f35e101f6ed02ee06
        A/clauses/window-06/raw.json: 99a08c6c52ee7c7524d5be518053cb2a26eb09e34ba6f5ca14b961c24a6e9f08
        A/clauses/window-06/prompt.txt: 9e1c56d48dd7688be17ca34a6123463e1e0dd3e013616e39563315b4bbc14fa7
        A/clauses/window-06/meta.json: a347d221ee285991993c3b060976abc4196012a6e24f3234e96bc11faf30ab7f
        A/clauses/window-08/raw.json: b0f8c505c4dc3620db2aad6ab6ecb8d4c758bc768b9c6a66e1d5ec51bbb48980
        A/clauses/window-08/prompt.txt: 5b72ee6544c98e03723da3cc607049130d0f02fbfccb66673a14c883f931f1de
        A/clauses/window-08/meta.json: 7dcd26bae85c8aba9bb7ef228c4d7b78a4c1bec66481eef1655c7d9d63fcdb34
        A/tables/TABLE-3-page-5-3/raw.json: ab319351403949c2b3e072843ef11bdba64af11afca75e65f463be33b318f3b3
        A/tables/TABLE-3-page-5-3/prompt.txt: dc98f51b576a5ec88d16fcdc107eb1a5adeec0b94418234c32dac326eca3d005
        A/tables/TABLE-3-page-5-3/meta.json: f59cd862fe74b7168df5c6245b1481a9840ad152c0e0309994efc1cacbe4bf07
        A/tables/TABLE-1-page-3-1/raw.json: cbb2a75e5834875593b0fc0014603391f7d8478300d0b6d3af7dcce2665a8b80
        A/tables/TABLE-1-page-3-1/prompt.txt: 9f3a3a2528a593c1d55cfdb616c00bb7a6e410c2e5f71a6c1425f8d205b32c63
        A/tables/TABLE-1-page-3-1/meta.json: 134d35e5e6d0fc2b1820b16e98a7150404f94fa4623d52948af34ff6af8479df
        A/tables/TABLE-5-page-9-5/raw.json: 4b010b2924e00cff92c9afce5a5341158be147e45797c7814312c3cfa244fd40
        A/tables/TABLE-5-page-9-5/prompt.txt: 3c9091140ccedc1ee2d824b6273f30b9dd75032b0d723abce006f608027bfa97
        A/tables/TABLE-5-page-9-5/meta.json: a64d3f053e7e016579f944fad994792cda4848a660a04abb71e25ab38dd26f2e
        A/tables/TABLE-4-page-9-4/raw.json: ff471aff32a67b97715ef89d133de41bae04a67c38aa19cb40f888808e36f5a5
        A/tables/TABLE-4-page-9-4/prompt.txt: d5f442666e8d28d64eb12177f00eff10d6877aaae93566b59cfd0a178b6f9734
        A/tables/TABLE-4-page-9-4/meta.json: 2280a4ce85cc49d2b1fd9037f4c99291a03bf54ee0f70041f1cf3b740996357a
        A/tables/TABLE-2-page-4-2/raw.json: 368452f0891e7f504766dc140b9b3e3cee9a522d191566a5330ffd925d11819f
        A/tables/TABLE-2-page-4-2/prompt.txt: 3499cac91423ccccf6c8b7e0b5eac79112d20b719938fb067ea8b58bd5e67cbf
        A/tables/TABLE-2-page-4-2/meta.json: 4e1a66e1d29b5b8b4270c2b14364ec0aaae1e642b5ac753ede8944da202ce9b7
        B/passages.json: 5b4c48cd8154f46fac9ebd4cc1c524f1908b7f05dc6e783a46ce04285caf6753
        B/raw.json: 0ae0e61e192006682dfc72f0c48d518dda285160495a39bb48fe2b9d4f7355c5
        B/source-units.json: db7af196b55b8ab6f1870d177861f0ee723a5e5bc02b8677a2bceba44b8e8532
        B/full-source-units.json: c06770fce10bb954eb64d4cbe695f8380bf8f3e224ddf593854d981f112ab1e7
        B/meta.json: 641228d0108a758d5e46aedcfbb54acc01bd81bcbd29f8d21a92fa8c9f1d7ee4
        B/table-images/TABLE-5-page-9-2.png: 39741739f5e0d0237f8fec5e381973cb4fc864b8a33bbc7443d6f2f19edd32f2
        B/table-images/TABLE-1-page-3-1.png: f80b341a465596cd130fd639695ba9cb4acb95aba890d5f81e0faddfbc72af6c
        B/table-images/TABLE-4-page-9-1.png: 39741739f5e0d0237f8fec5e381973cb4fc864b8a33bbc7443d6f2f19edd32f2
        B/table-images/page-3.png: 6fa5c22b28207c1f4fca0f2556a5ed8a38de8392b73b5216e5d9e8773f8aef42
        B/table-images/page-5.png: 6022bb4f63e7566747ce5ef73602f592b5acce92bc52f02de2b26e4069cbc601
        B/table-images/page-4.png: 6694df46850026252c3fbeb4e8ea3d529f759f4b647eedabaff5ac3268a9bb43
        B/table-images/page-9.png: be808f7a2f08ae9a1cf432b328337cbc52b1574fee7f89dd9f9cb9c1977bce7e
        B/table-images/manifest.json: bfb2961d00a26d26da4de2c2b24c286906ff46a5fc86df5b32d98247c2eb0106
        B/table-images/TABLE-2-page-4-1.png: e5a2677e4d2e651f60578e482376667da88d354f3a4bf1cb4b4e983c0de1c896
        B/table-images/TABLE-3-page-5-1.png: dedd2ac6598ca47152fd93cf04a82dc40b0645171e638a8be651b6f2065edb81
        B/clauses/window-11/raw.json: 108d769e78bb97ef45dfb1eebaed9b61b5e11cc5e08214eed0987fa1be4a9a66
        B/clauses/window-11/prompt.txt: c5d16367db496109d9612faf2e1ecd1fb67f33208804b0059eed4eaf8e1e9c85
        B/clauses/window-11/meta.json: 74d9269f6569aab281574c49551630b50d8cef9d1184278e16d369f1a3a986e3
        B/clauses/window-10/raw.json: 534e58957fba2ff48856556406e2186e4ef101225215f1be6fb5c0a1b26285ef
        B/clauses/window-10/prompt.txt: dad14067f86a90affaa485c2ac0ce7c961b1bae43ad60c1a9752bb3c8e12c810
        B/clauses/window-10/meta.json: 2fd05bfbc6db9b879f50f17f983c9a6c18197974557082d72c4d4a06063976e9
        B/clauses/window-03/raw.json: e7a631f2bebb38b1df3f56e6a7b3a73948129a5711ef5dd4bfbfd8f27a25e766
        B/clauses/window-03/prompt.txt: f1469ee1e69a4843abe4c0a25d92766c8db2bd57cb3076d651c3af64d2418f38
        B/clauses/window-03/meta.json: b24f003aac7f8929ec52ef757851c0613558dc109be6e85133e546935e2bc451
        B/clauses/window-04/raw.json: 36c77d1871734d54e6a893e58fda0d2be7201098806ffa4da2ecdc5afe3df1b6
        B/clauses/window-04/prompt.txt: 29a6eb8cd9a4326a5ee6e002103673d34323290b7717140f224e8406a36932be
        B/clauses/window-04/meta.json: f0c8fb7b249fefa33340e8b45d0dc2aa99bb74a94b780fdb2b6677180960ad31
        B/clauses/window-05/raw.json: 51e4f89a91c1a0b69b068ac24d917680b571a24473c268b3ce1690b5269f3086
        B/clauses/window-05/prompt.txt: f5c0ae1b1d347fbbd665ea182ef2c2377ab665bbe0af008ffc4371a726d55a97
        B/clauses/window-05/meta.json: 300a635f1c191e41cc59bda736aa2e1fed5f7b103b2744d8c2bf4dba593837ec
        B/clauses/window-02/raw.json: 73771c2a2da3856ea90713b28f9cfb2d35aeecfe9066fd45721f7cc81cd48f51
        B/clauses/window-02/prompt.txt: f1323d5a6b8c2df29f17d4b81b0ed44555871539f824eb4c7b137493b9a96238
        B/clauses/window-02/meta.json: 03b269c3ceb32453b59c0b587fde66fd504f074dd821bb19a2b3b2360e6c3044
        B/clauses/window-12/raw.json: 3acd351a43fba92a476ef846a439eac7c88b9d2524efdf7bb9906c72cade1064
        B/clauses/window-12/prompt.txt: 6b44db02517bf4f68c5ed1f11c2157a82e3edb6ad10b21c419fb3e449d98c5fe
        B/clauses/window-12/meta.json: 54e8a682ecbe734141f36860a7b12433613f5de7626c35cafa8c56b29e22afbd
        B/clauses/window-13/raw.json: eff8e5a3b12bd0fce22e2fb74566c12dc6065e79518b2c6f718b7c6b10a81ae0
        B/clauses/window-13/prompt.txt: a3b6fca1b58712c2523e27907b6947f74d3e9ac7ca26d86476be1ef51575d6a3
        B/clauses/window-13/meta.json: 288b315119834b7851e54d683919804e9f6a0e423d2f48e49fe6491a94e76291
        B/clauses/window-09/raw.json: 1bf2c16fef5c71c83bd415fefc991fc4246fee5063da022fdf8602735272956a
        B/clauses/window-09/prompt.txt: 9c828b6f304ab81b380678fd712665728518e56b101eb3a0bed6349227a6e9b6
        B/clauses/window-09/meta.json: 4f97f1f9b15a7ec8178197ae748b0c943ecca225e490ab461fc26283acadabf4
        B/clauses/window-07/raw.json: e960f53ea0c529f1b10bcb0719ef1448f6ab60649a8be95f6aea040416a52603
        B/clauses/window-07/prompt.txt: a308093ca6b5d01cb477c4db40872b406d05751e6f26f92ac11707f651a79f27
        B/clauses/window-07/meta.json: 9dc2895db9102dbc66c32445206f3c88ae1908290de7dcaa2e4b0ec3610044c8
        B/clauses/window-01/raw.json: 75a0d0d46efd71a9aa9086c0ba460e54bd1c5a7ae0f02200a1c6d3ca0dab6a7a
        B/clauses/window-01/prompt.txt: afb1193c640f7b67d72a33e591e10042bcd0243c9abcf08ec65bb41cbd7ac8dc
        B/clauses/window-01/meta.json: f24a7dfcd122b98aa34bdca8a40431dde37882cbf15424ec7e106a8207469d6f
        B/clauses/window-06/raw.json: da2306e3b82fdbf315e535b90f29405dc9bd399892617bc58f3b19709a35ca02
        B/clauses/window-06/prompt.txt: 9e1c56d48dd7688be17ca34a6123463e1e0dd3e013616e39563315b4bbc14fa7
        B/clauses/window-06/meta.json: 208cc90dd2826d1a1f4ab98aa881f55731f4b936b0d98a9039535298c9044b43
        B/clauses/window-08/raw.json: f1f44d6c9d0d7257188df3dde227581a740a3aa2c24f79fd334eab1e58d80ec2
        B/clauses/window-08/prompt.txt: 5b72ee6544c98e03723da3cc607049130d0f02fbfccb66673a14c883f931f1de
        B/clauses/window-08/meta.json: 37bbcdcd9a5822f4451b2b19db624296f8529d87f4f4756c363e0f2708cc44e0
        B/tables/TABLE-3-page-5-3/raw.json: 3cd3c0f75f069c650ec1709e9ffec65ad348184d6f275f9894a23c1499e91305
        B/tables/TABLE-3-page-5-3/prompt.txt: dc98f51b576a5ec88d16fcdc107eb1a5adeec0b94418234c32dac326eca3d005
        B/tables/TABLE-3-page-5-3/meta.json: b3cc79d786474215d3a2048db9949152ea42ab7984660fc4d9f70d64cad4dd0a
        B/tables/TABLE-1-page-3-1/raw.json: 3e2677ed4b9add02e3d9b65265f321f88bb0a9f26f93fa26ac4f717e209931c6
        B/tables/TABLE-1-page-3-1/prompt.txt: 9f3a3a2528a593c1d55cfdb616c00bb7a6e410c2e5f71a6c1425f8d205b32c63
        B/tables/TABLE-1-page-3-1/meta.json: 2063a76f6a8bbf12a94b1fd564a7abedef40d45974de83612910d7f8fee1573b
        B/tables/TABLE-5-page-9-5/raw.json: 2c169c89e444ada65e309cca577764451be968b1afd4c587abe8da0be9781569
        B/tables/TABLE-5-page-9-5/prompt.txt: 3c9091140ccedc1ee2d824b6273f30b9dd75032b0d723abce006f608027bfa97
        B/tables/TABLE-5-page-9-5/meta.json: 3ed426f8112d790d3b9afd63a3104f673a5c7fc4b004dace186661546d84a660
        B/tables/TABLE-4-page-9-4/raw.json: ff471aff32a67b97715ef89d133de41bae04a67c38aa19cb40f888808e36f5a5
        B/tables/TABLE-4-page-9-4/prompt.txt: d5f442666e8d28d64eb12177f00eff10d6877aaae93566b59cfd0a178b6f9734
        B/tables/TABLE-4-page-9-4/meta.json: ae9d7ed36ab62820c833da5e8207e28666c55881e818a1c075ca0bba84d5f4c0
        B/tables/TABLE-2-page-4-2/raw.json: 2bfa1b9fcc85b3d5849a9b3bdaec31cdc67c3bf8a80f1b7a33f411942aea34d2
        B/tables/TABLE-2-page-4-2/prompt.txt: 3499cac91423ccccf6c8b7e0b5eac79112d20b719938fb067ea8b58bd5e67cbf
        B/tables/TABLE-2-page-4-2/meta.json: bb711473c0dd0c9a98fb47bc4bfc43c72edcd2431e32b5364d3c43f9cac05570
      code:
        relationship_review.py: 6d0359072ca11a7569362fe49703755a98b4207ba814fcd311161c48936053ed
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
      pdf_sha256: 4d6f39b654a42bd162658c3b70546f73bc72f8bd249ee1d0d9a12468af0db177
      source_review: _compare/relationships-2026-11-16/review-current/Stahl2013
      source_status_sha256: dc13b8d7d733534c0359481078227acf7a706b4dc8515e5a51d611ddafcad9f5
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R003
    exposure:
      text: standard therapy
    outcome:
      text: production of non-formulaic lyrics
    analysis_label: Treatment efficacy on non-formulaic lyrics
    relation: treatment_effect
    evidence_ids:
    - P1-S2-C5
    - P8-S1-C4
    - P8-S2-C10
    qualifier_ids:
    - P8-S2-C11
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 4d6f39b654a42bd162658c3b70546f73bc72f8bd249ee1d0d9a12468af0db177
      source_review: _compare/relationships-2026-11-16/review-current/Stahl2013
      source_status_sha256: dc13b8d7d733534c0359481078227acf7a706b4dc8515e5a51d611ddafcad9f5
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P1-S1-C13
      - Accounting without a linked unit P1-S2-C4
      - Accounting without a linked unit P1-S2-C5
      - Unaccounted source passage P1-S2-C4
      - Unaccounted source passage P1-S2-C5
      - Accounting without a linked unit P2-S1-C2
      - Unaccounted source passage P2-S1-C2
      - Result passage disposed without unit P5-S1-C10
      - Accounting without a linked unit P5-S2-C4
      - Accounting without a linked unit P5-S2-C7
      - Result passage disposed without unit P5-S2-C8
      - Unaccounted source passage P5-S2-C4
      - Unaccounted source passage P5-S2-C7
      - Result passage disposed without unit P5-S3-C15
      - 'window 17: invalid/duplicate disposition P7-S3-C3'
      - Accounting without a linked unit P7-S3-C6
      - Accounting without a linked unit P7-S3-C7
      - Unaccounted source passage P7-S3-C7
      - Unaccounted source passage P7-S3-C6
      - Accounting without a linked unit P8-S1-C3
      - Accounting without a linked unit P8-S1-C4
      - Accounting without a linked unit P8-S1-C5
      - Unaccounted source passage P8-S1-C4
      - Unaccounted source passage P8-S1-C3
      - Unaccounted source passage P8-S1-C5
      - Result passage disposed without unit P9-S1-C6
      - Result passage disposed without unit P9-S3-C7
      - Result passage disposed without unit P9-S3-C9
      - Result passage disposed without unit P10-S1-C3
      - Result passage disposed without unit P10-S2-C10
      - Result passage disposed without unit P10-S2-C7
      - Result passage disposed without unit P10-S2-C9
      - Result passage disposed without unit P10-S2-C12
      - Result passage disposed without unit P10-S2-C13
      - Result passage disposed without unit P10-S2-C15
      - Result passage disposed without unit P10-S2-C16
      - Result passage disposed without unit P10-S3-C3
      - Result passage disposed without unit P11-S1-C1
      - Result passage disposed without unit P11-S1-C2
      - Result passage disposed without unit P11-S1-C4
      - Accounting without a linked unit P11-S1-C6
      - Unaccounted source passage P11-S1-C6
      unattached_null_or_qualifier_ids:
      - P1-S2-C5
      - P3-S2-C8
      - P5-S2-C7
      - P7-S3-C6
      - P7-S4-C3
      - P8-S1-C4
      - P8-S1-C5
      - P9-S3-C9
      suppressed_nonrepresented_units: 22
      default_disposition_count_requires_completeness_check: 273
      unselected_timing_passages:
      - P1-S1-C9
      - P2-S3-C10
      - P2-S3-C13
      - P6-S1-C6
      - P6-S3-C3
      - P6-S3-C4
      - P6-S3-C5
      - P6-S3-C8
      - P6-S4-C5
      - P9-S1-C9
      - P9-S3-C19
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P1-S1-C13
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P1-S2-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P1-S2-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P2-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S3-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S3-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S3-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S4-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C14
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S2-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S3-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S3-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S3-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: tested_personal_effects
        source_id: P1-S3-C8
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P1-S3-C9
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: analysed_sample
        source_ids:
        - P1-S1-C9
        - P1-S3-C5
        - P2-S3-C8
        - P3-S1-C2
        - P4-S1-C2
        - P5-S3-C18
        - P5-S4-C1
        - P6-S1-C1
        - P9-S1-C9
        - P9-S4-C2
        - P10-S1-C1
        - P10-S2-C9
        - P11-S1-C4
        - P11-S1-C5
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: recruited_sample
        source_ids:
        - P1-S1-C9
        - P1-S3-C5
        - P2-S3-C8
        - P3-S1-C2
        - P4-S1-C2
        - P5-S1-C3
        - P5-S3-C18
        - P5-S4-C1
        - P6-S1-C1
        - P9-S1-C9
        - P9-S3-C19
        - P10-S1-C12
        - P11-S1-C4
        - P11-S1-C5
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: outcome_timing
        source_ids:
        - P1-S2-C3
        - P2-S3-C6
        - P2-S3-C13
        - P3-S2-C17
        - P6-S3-C3
        - P6-S3-C4
        - P6-S3-C5
        - P6-S3-C8
        - P6-S4-C6
        - P7-S1-C4
        - P7-S1-C6
        - P7-S1-C9
        - P7-S3-C7
        - P8-S1-C2
        - P9-S1-C2
        - P9-S1-C5
        - P11-S1-C6
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: outcome_definition
        source_ids:
        - P1-S1-C13
        - P1-S2-C4
        - P1-S2-C5
        - P1-S3-C6
        - P1-S3-C8
        - P2-S1-C2
        - P2-S3-C6
        - P3-S1-C5
        - P3-S1-C6
        - P4-S1-C3
        - P4-S1-C4
        - P4-S1-C5
        - P4-S1-C6
        - P5-S1-C12
        - P6-S3-C3
        - P6-S3-C5
        - P6-S3-C8
        - P7-S1-C7
        - P7-S2-C9
        - P7-S3-C5
        - P8-S1-C12
        - P8-S2-C4
        - P9-S1-C2
        - P9-S1-C5
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: limitations
        source_ids:
        - P2-S2-C9
        - P6-S3-C9
        - P6-S3-C10
        - P6-S3-C12
        - P6-S4-C2
        - P6-S4-C3
        - P6-S4-C4
        - P9-S3-C14
        - P9-S3-C15
        - P9-S3-C16
        - P9-S3-C19
        - P10-S1-C4
        - P10-S1-C6
        - P10-S1-C13
        - P10-S2-C6
        - P10-S2-C14
        - P11-S1-C14
        - P11-S2-C2
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: descriptive_personal_factors
        source_ids:
        - P1-S1-C9
        - P1-S3-C5
        - P1-S3-C7
        - P1-S3-C8
        - P1-S3-C9
        - P2-S3-C10
        - P2-S3-C11
        - P2-S3-C12
        - P3-S1-C2
        - P3-S2-C3
        - P4-S1-C2
        - P4-S1-C7
        - P5-S1-C3
        - P6-S1-C3
        - P6-S1-C5
        - P6-S1-C6
        - P9-S1-C9
        - P9-S3-C19
        - P10-S1-C1
        - P10-S2-C10
        - P10-S2-C12
        - P11-S1-C2
        - P11-S1-C3
        - P11-S1-C4
        - P11-S1-C5
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - analysed_sample
      - recruited_sample
      - outcome_timing
      - outcome_definition
      - validation
      - limitations
      - explicitly_not_adjusted
      - descriptive_personal_factors
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-3-1
      - TABLE-2-page-4-2
      - TABLE-3-page-5-3
      - TABLE-4-page-9-4
      - TABLE-5-page-9-5
      unlinked_tables:
      - TABLE-1-page-3-1
      - TABLE-3-page-5-3
      - TABLE-4-page-9-4
      - TABLE-5-page-9-5
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P3-S2
        - P8-S1
        - P11-S1
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 4d6f39b654a42bd162658c3b70546f73bc72f8bd249ee1d0d9a12468af0db177
      source_review: _compare/relationships-2026-11-16/review-current/Stahl2013
      source_status_sha256: dc13b8d7d733534c0359481078227acf7a706b4dc8515e5a51d611ddafcad9f5
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C11
      disposition: represented
      result_indexes:
      - 0
      reason: States singing and rhythmic speech are similarly effective for non-fluent
        aphasia.
    - source_id: P1-S1-C13
      disposition: represented
      result_indexes:
      - 0
      reason: Qualifies progress in formulaic phrases for singing and rhythmic therapy.
    - source_id: P1-S2-C3
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of progress timing and stability.
    - source_id: P1-S2-C4
      disposition: represented
      result_indexes:
      - 1
      reason: States standard therapy patients made less progress in formulaic phrases.
    - source_id: P1-S2-C5
      disposition: represented
      result_indexes:
      - 2
      - 3
      reason: Contrasts improvement in non-formulaic speech (standard therapy) vs
        lack thereof (singing/rhythmic).
    - source_id: P2-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Refers to pilot work results.
    - source_id: P2-S4-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Demographic/diagnostic count of speech disorders.
    - source_id: P3-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive of lesion sites.
    - source_id: P3-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive of right hemisphere status.
    - source_id: P5-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive of stimulus word transition frequencies.
    - source_id: P5-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison of stimulus lyrics, not clinical outcome.
    - source_id: P5-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Null findings on stimulus characteristics.
    - source_id: P5-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive of lyric meter.
    - source_id: P5-S3-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Pilot patient result on rhythmic accompaniments.
    - source_id: P5-S3-C15
      disposition: background_or_descriptive
      result_indexes: []
      reason: Pilot work difficulty level.
    - source_id: P6-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Group comparability demographics.
    - source_id: P6-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Null difference in baseline language scores.
    - source_id: P6-S1-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Pilot work result on progress timing.
    - source_id: P6-S1-C16
      disposition: background_or_descriptive
      result_indexes: []
      reason: Pilot work result on metrical syllables.
    - source_id: P7-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Learning effects during a single session (not long-term treatment).
    - source_id: P7-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Null finding on testing-induced long-term effects.
    - source_id: P7-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Pilot work on playback intensity.
    - source_id: P7-S2-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive of scoring percentages.
    - source_id: P7-S2-C15
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive of scoring percentages.
    - source_id: P7-S2-C16
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive of scoring percentages.
    - source_id: P7-S3-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive of scoring percentages.
    - source_id: P7-S3-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Inter-rater reliability.
    - source_id: P7-S3-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Null differences in pitch accuracy.
    - source_id: P7-S3-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Null correlation between pitch accuracy and recovery.
    - source_id: P7-S4-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Normality tests for ANCOVA.
    - source_id: P7-S4-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Alpha level specification.
    - source_id: P7-S4-C5
      disposition: represented
      result_indexes:
      - 0
      - 1
      - 2
      - 3
      reason: Reports significant interaction of time, treatment, and lyrics.
    - source_id: P7-S4-C6
      disposition: represented
      result_indexes:
      - 0
      reason: Reports strong increases in formulaic lyrics for singing/rhythmic therapy.
    - source_id: P8-S1-C1
      disposition: represented
      result_indexes:
      - 0
      reason: Provides mean increase for singing and rhythmic therapy on formulaic
        lyrics.
    - source_id: P8-S1-C2
      disposition: represented
      result_indexes:
      - 0
      reason: Qualifies stability of formulaic lyric effects over 3 months.
    - source_id: P8-S1-C3
      disposition: represented
      result_indexes:
      - 1
      reason: Reports smaller increase for standard therapy on formulaic lyrics.
    - source_id: P8-S1-C4
      disposition: represented
      result_indexes:
      - 2
      - 3
      reason: Reports improvement in non-formulaic lyrics for standard therapy only.
    - source_id: P8-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Null interaction for modality and treatment group.
    - source_id: P8-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Null interaction between time and baseline scores.
    - source_id: P8-S2-C1
      disposition: represented
      result_indexes:
      - 4
      reason: Reports higher continuous phonation during singing vs rhythmic speech.
    - source_id: P8-S2-C2
      disposition: represented
      result_indexes:
      - 4
      reason: Qualifies phonation result as independent of prior therapy.
    - source_id: P8-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive of fundamental frequency variances.
    - source_id: P8-S2-C6
      disposition: repeated
      result_indexes:
      - 0
      - 1
      - 2
      - 3
      reason: Restatement of significant interaction (p < 0.001).
    - source_id: P8-S2-C7
      disposition: represented
      result_indexes:
      - 0
      reason: Restatement of formulaic phrase improvement for singing/rhythmic therapy.
    - source_id: P8-S2-C9
      disposition: represented
      result_indexes:
      - 1
      reason: Restatement of less progress for standard therapy in formulaic phrases.
    - source_id: P8-S2-C10
      disposition: represented
      result_indexes:
      - 2
      - 3
      reason: Restatement of non-formulaic speech improvement for standard therapy
        only.
    - source_id: P8-S3-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of ANCOVA adjustment.
    - source_id: P9-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison of frequency variances (not treatment effect).
    - source_id: P9-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Null finding on treatment effect on frequency variance.
    - source_id: P9-S2-C2
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of similar effectiveness of singing and rhythmic speech.
    - source_id: P9-S2-C3
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of progress in formulaic phrases.
    - source_id: P9-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation on switching between modalities.
    - source_id: P9-S2-C8
      disposition: repeated
      result_indexes:
      - 2
      - 3
      reason: Restatement of training transfer to unknown phrases (standard therapy
        only).
    - source_id: P9-S2-C13
      disposition: represented
      result_indexes:
      - 4
      reason: Restatement of increased phonation during singing.
    - source_id: P9-S2-C14
      disposition: represented
      result_indexes:
      - 4
      reason: Restatement that phonation result is independent of prior therapy.
    - source_id: P9-S2-C15
      disposition: represented
      result_indexes:
      - 4
      reason: Null finding on long-term effect of singing on phonatory quality.
    - source_id: P9-S3-C7
      disposition: represented
      result_indexes:
      - 5
      reason: Null finding on singing's long-term effect on prosody.
    - source_id: P9-S3-C8
      disposition: represented
      result_indexes:
      - 5
      reason: Null finding on treatment effect on vocal fundamental frequency variability.
    - source_id: P9-S3-C9
      disposition: represented
      result_indexes:
      - 5
      reason: Null finding on treatment effect on amount of prosody.
    - source_id: P9-S3-C11
      disposition: represented
      result_indexes:
      - 6
      reason: Reports increased frequency variability during rhythmic speech vs singing.
    - source_id: P10-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement on statistical significance.
    - source_id: P10-S2-C3
      disposition: repeated
      result_indexes:
      - 0
      - 2
      - 3
      reason: Restatement of differential effects on formulaic vs non-formulaic speech.
    - source_id: P10-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation of lower pre-treatment averages in rhythmic group.
    - source_id: P10-S2-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation about a specific patient's effect on baseline.
    - source_id: P10-S3-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation on individual formulaic repertoires.
    - source_id: P11-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation on individual patient variation.
    - source_id: P11-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation on independence from external cues.
    unresolved_coverage:
    - source_id: P7-S4-C4
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P8-S2-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P8-S3-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P9-S2-C2
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P9-S2-C15
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P8-S1-C14
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S2-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S2-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S2-C16
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S2-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S2-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S2-C13
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S2-C15
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S2-C16
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C13
    - P1-S2-C3
    - P2-S1-C2
    - P2-S4-C5
    - P3-S2-C8
    - P3-S2-C9
    - P5-S1-C10
    - P5-S2-C4
    - P5-S2-C7
    - P5-S2-C8
    - P5-S3-C4
    - P5-S3-C15
    - P6-S1-C6
    - P6-S1-C7
    - P6-S1-C13
    - P6-S1-C16
    - P7-S1-C8
    - P7-S1-C9
    - P7-S2-C4
    - P7-S2-C14
    - P7-S2-C15
    - P7-S2-C16
    - P7-S3-C2
    - P7-S3-C4
    - P7-S3-C6
    - P7-S3-C7
    - P7-S4-C3
    - P7-S4-C5
    - P7-S4-C6
    - P8-S1-C2
    - P8-S1-C5
    - P8-S1-C6
    - P8-S2-C2
    - P8-S2-C5
    - P8-S2-C6
    - P8-S2-C11
    - P9-S1-C6
    - P9-S1-C7
    - P9-S2-C3
    - P9-S2-C5
    - P9-S2-C8
    - P9-S2-C9
    - P9-S2-C14
    - P9-S2-C16
    - P10-S1-C3
    - P10-S2-C3
    - P10-S2-C7
    - P10-S2-C9
    - P10-S2-C10
    - P10-S2-C12
    - P10-S2-C13
    - P10-S2-C15
    - P10-S2-C16
    - P10-S3-C3
    - P11-S1-C1
    - P11-S1-C2
    - P11-S1-C4
    - P11-S1-C5
    - P11-S1-C6
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-3-1
    - TABLE-2-page-4-2
    - TABLE-3-page-5-3
    - TABLE-4-page-9-4
    - TABLE-5-page-9-5
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample: []
      recruited_sample: []
      eligibility:
      - P1-S1-C9
      - P2-S3-C10
      - P2-S3-C11
      - P2-S3-C12
      - P3-S1-C4
      - P9-S1-C9
      - P10-S1-C1
      imaging_provenance:
      - P2-S2-C5
      - P3-S2-C5
      - P11-S2-C2
      imaging_timing:
      - P2-S2-C5
      - P3-S2-C5
      outcome_timing: []
      outcome_definition: []
      validation: []
      analysis_restrictions:
      - P6-S2-C11
      - P7-S1-C13
      - P7-S1-C14
      - P7-S2-C13
      - P10-S1-C4
      - P10-S2-C13
      dependent_variable_statement:
      - P1-S3-C6
      - P1-S3-C8
      - P5-S1-C12
      - P6-S3-C3
      limitations: []
      personal_factors:
      - P4-S1-C7
      tested_personal_effects:
      - P9-S1-C7
      - P9-S2-C5
      - P9-S2-C14
      adjustment_roles:
      - P1-S1-C10
      - P6-S1-C3
      - P7-S3-C10
      - P8-S1-C7
      - P8-S2-C12
      - P10-S2-C11
      explicitly_not_adjusted: []
      descriptive_personal_factors: []
    outcome_type: both_reported
    imaging_vs_outcome: mixed
    validation_type: none_described
    window_merge: Union of selected IDs; differing window enums retained conservatively
      as both/mixed. Not verified study-level facts.
    held_selections:
    - slot: dependent_variable_statement
      source_id: P1-S1-C13
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P1-S2-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P1-S2-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P2-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S3-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S3-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S3-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S4-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C14
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S2-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S3-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S3-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S3-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: tested_personal_effects
      source_id: P1-S3-C8
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P1-S3-C9
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: analysed_sample
      source_ids:
      - P1-S1-C9
      - P1-S3-C5
      - P2-S3-C8
      - P3-S1-C2
      - P4-S1-C2
      - P5-S3-C18
      - P5-S4-C1
      - P6-S1-C1
      - P9-S1-C9
      - P9-S4-C2
      - P10-S1-C1
      - P10-S2-C9
      - P11-S1-C4
      - P11-S1-C5
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: recruited_sample
      source_ids:
      - P1-S1-C9
      - P1-S3-C5
      - P2-S3-C8
      - P3-S1-C2
      - P4-S1-C2
      - P5-S1-C3
      - P5-S3-C18
      - P5-S4-C1
      - P6-S1-C1
      - P9-S1-C9
      - P9-S3-C19
      - P10-S1-C12
      - P11-S1-C4
      - P11-S1-C5
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: outcome_timing
      source_ids:
      - P1-S2-C3
      - P2-S3-C6
      - P2-S3-C13
      - P3-S2-C17
      - P6-S3-C3
      - P6-S3-C4
      - P6-S3-C5
      - P6-S3-C8
      - P6-S4-C6
      - P7-S1-C4
      - P7-S1-C6
      - P7-S1-C9
      - P7-S3-C7
      - P8-S1-C2
      - P9-S1-C2
      - P9-S1-C5
      - P11-S1-C6
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: outcome_definition
      source_ids:
      - P1-S1-C13
      - P1-S2-C4
      - P1-S2-C5
      - P1-S3-C6
      - P1-S3-C8
      - P2-S1-C2
      - P2-S3-C6
      - P3-S1-C5
      - P3-S1-C6
      - P4-S1-C3
      - P4-S1-C4
      - P4-S1-C5
      - P4-S1-C6
      - P5-S1-C12
      - P6-S3-C3
      - P6-S3-C5
      - P6-S3-C8
      - P7-S1-C7
      - P7-S2-C9
      - P7-S3-C5
      - P8-S1-C12
      - P8-S2-C4
      - P9-S1-C2
      - P9-S1-C5
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: limitations
      source_ids:
      - P2-S2-C9
      - P6-S3-C9
      - P6-S3-C10
      - P6-S3-C12
      - P6-S4-C2
      - P6-S4-C3
      - P6-S4-C4
      - P9-S3-C14
      - P9-S3-C15
      - P9-S3-C16
      - P9-S3-C19
      - P10-S1-C4
      - P10-S1-C6
      - P10-S1-C13
      - P10-S2-C6
      - P10-S2-C14
      - P11-S1-C14
      - P11-S2-C2
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: descriptive_personal_factors
      source_ids:
      - P1-S1-C9
      - P1-S3-C5
      - P1-S3-C7
      - P1-S3-C8
      - P1-S3-C9
      - P2-S3-C10
      - P2-S3-C11
      - P2-S3-C12
      - P3-S1-C2
      - P3-S2-C3
      - P4-S1-C2
      - P4-S1-C7
      - P5-S1-C3
      - P6-S1-C3
      - P6-S1-C5
      - P6-S1-C6
      - P9-S1-C9
      - P9-S3-C19
      - P10-S1-C1
      - P10-S2-C10
      - P10-S2-C12
      - P11-S1-C2
      - P11-S1-C3
      - P11-S1-C4
      - P11-S1-C5
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
      pdf_sha256: 4d6f39b654a42bd162658c3b70546f73bc72f8bd249ee1d0d9a12468af0db177
      review_sha256: 31f9f54b9fced7bd95bc6dd6138a079e97da4417760958919c722b666b6ab8ec
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
      - P1-S2-C5
      - P8-S1-C4
      - P8-S2-C10
      source_result: Standard therapy patients showed a significant improvement in
        the production of non-formulaic lyrics (M = 6.21, 95% CI [3.96, 8.47]), whereas
        patients in singing and rhythmic therapy groups did not show significant improvement
        (M = -0.36, 95% CI [-2.62, 1.90]; M = -0.50, 95% CI [-2.76, 1.76]). This pattern
        was identified as a training transfer to unknown phrases, distinct from the
        formulaic phrase improvements seen in the other groups.
      result_status: detected
      patient_measurement: non_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis correctly identifies the specific outcome
            (non-formulaic lyrics) and the specific treatment group (standard therapy)
            from the repeated measures ANCOVA results. The source explicitly contrasts
            this group's performance on non-formulaic lyrics with the other groups.
          source_ids:
          - P8-S1-C4
          - P8-S2-C10
        direction:
          answer: fits
          reason: The claim that standard therapy patients improved while others did
            not is supported by the confidence intervals in P8-S1-C4, where the standard
            therapy CI [3.96, 8.47] excludes zero, while the CIs for singing and rhythmic
            therapy include zero. The direction of the effect (improvement vs. no
            change) is preserved.
          source_ids:
          - P8-S1-C4
          - P1-S2-C5
        construct:
          answer: fits
          reason: The exposure is correctly defined as standard therapy (excluding
            singing/rhythm/formulaic training) per P3-S2-C16. The outcome is non-formulaic
            speech production, measured as percentage of correct syllables (P7-S2-C9).
            The patient measurement is behavioral (non-imaging), as the study explicitly
            states it does not include neuroimaging (P11-S2-C2).
          source_ids:
          - P3-S2-C16
          - P7-S2-C9
          - P11-S2-C2
        qualifications:
          answer: fits
          reason: The draft includes the qualification that this improvement represents
            a 'training transfer to the production of unknown phrases,' which is explicitly
            stated in P8-S2-C11. The distinction between formulaic and non-formulaic
            is maintained.
          source_ids:
          - P8-S2-C11
          - P3-S2-C18
        missing_material_caveat:
          answer: fits
          reason: The draft notes the small sample size. The source mentions that
            the experiment did not include a control treatment for rhythmic therapy
            (P10-S1-C4), but this is a limitation of the overall study design rather
            than a specific caveat that negates the finding for standard therapy on
            non-formulaic lyrics. The finding is robust within the reported ANCOVA
            interaction.
          source_ids:
          - P10-S1-C4
          - P9-S3-C19
      optional_pending:
      - 'sample.population: source confirmation required; original proposed wording
        remains in the audit.'
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - 'sample.population: source confirmation required; original proposed wording
      remains in the audit.'
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - 'sample.population: source confirmation required; original proposed wording
      remains in the audit.'
    normalizations:
    - field: sample.population
      original: Patients with chronic non-fluent aphasia (Broca's or global aphasia)
        and left-hemispheric stroke (mostly left middle cerebral artery ischemia),
        aged 40-72 years, with at least 6 months post-infarction at the time of testing.
      action: not_transcribed
      reason: 'Numbers not grounded in usable selected source readings: 4E+1, 72'
    analysis_identity:
      id: R003
      exposure:
        text: standard therapy
      outcome:
        text: production of non-formulaic lyrics
      analysis_label: Treatment efficacy on non-formulaic lyrics
      relation: treatment_effect
      evidence_ids:
      - P1-S2-C5
      - P8-S1-C4
      - P8-S2-C10
      qualifier_ids:
      - P8-S2-C11
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 4d6f39b654a42bd162658c3b70546f73bc72f8bd249ee1d0d9a12468af0db177
        source_review: _compare/relationships-2026-11-16/review-current/Stahl2013
        source_status_sha256: dc13b8d7d733534c0359481078227acf7a706b4dc8515e5a51d611ddafcad9f5
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P2-S3-C13:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 4d6f39b654a42bd162658c3b70546f73bc72f8bd249ee1d0d9a12468af0db177
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 91b99c836c8e7ec9abed7afca6e8167d273db428925d8dfdae2492e9e6e2c0c6
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S3-C13
          page: 2
          text_layer_sha256: 91b99c836c8e7ec9abed7afca6e8167d273db428925d8dfdae2492e9e6e2c0c6
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: 'To restrict inﬂuences related

          to spontaneous recovery, all patients were at least 6 months post-

          infarction at the time of testing, suggesting a chronic post-stroke

          stage.'
        anchor_text: 'To restrict inﬂuences related

          to spontaneous recovery, all patients were at least 6 months post-

          infarction at the time of testing, suggesting a chronic post-stroke

          stage.'
        excluded_fragments: []
        image_sha256: 89085e2cffb8841c066399bf51145557dd9d417c68e1925fcccae06b26ab1899
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 1
  quote: 'They did, however, improve their production of non-formulaic speech,

    in contrast to singing and rhythmic therapy patients, who did not.'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-25'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
