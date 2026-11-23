---
id: brocas_area
name: Broca's area cluster
kind: network
findings:
- id: f1
  target: apraxia_of_speech
  target_kind: impairment
  claim: The presence of apraxia of speech was associated with hypoperfusion and/or
    infarct of Broca's area.
  direction: likely
  relationship: correlational
  method: LSM
  sample:
    n: not_reported
    population: adults with first-ever, non-lacunar, ischaemic stroke affecting the
      left MCA territory
    phase: not_reported
    time_post_onset: concurrent; MRI and behavioural testing performed within 24 hours
      of stroke onset
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - bedside testing may have missed subtle apraxia of speech
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Presence of dense ischaemia (high signal on DWI) and/or
    hypoperfusion (defined as >2.5 s delay in time to peak arrival of contrast in
    at least 25% of the region relative to the homologous intact hemisphere on PWI)
    in the posterior inferior frontal gyrus. association held regardless of whether
    patients had insular damage; apraxia of speech was defined by >10% total errors
    in each oral task, variable off-target attempts, distorted groping articulation,
    and impaired prosody not due to dysarthria. Additional metadata has not been transcribed;
    review the pending-field flags before approval.'
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
    - proposed_concept:apraxia_of_speech
  citation: '@Hillis2004'
  source_passages:
  - section: Original source P3-S4-C2
    page: 3
    quote: 'Instead, the presence of apraxia of speech was associated with

      hypoperfusion and/or infarct of Broca''s area [c2(1) = 46.4;

      P < 0.00001; Table 3], but not with other regions evaluated.'
    supports: claim
  - section: Original source P4-S1-C1
    page: 4
    quote: '

      insular damage, providing further evidence that the insular

      damage was independent of the apraxia of speech, i.e. there

      was a strong association between apraxia of speech and

      abnormality in Broca''s area in patients with insular damage

      [c2(1) = 28.1; P < 0.00001] and in patients without insular

      damage [c2(1) = 22.4; P < 0.00001] (Table 4).'
    supports: claim
  - section: Original source P2-S3-C7
    page: 2
    quote: 'A battery of speech and language tests was

      administered to each patient to identify the presence or

      absence of apraxia of speech, and MRI scans were obtained,

      both within 24 h of onset of stroke, to minimize the

      contribution of reorganization after brain injury.'
    supports: method
  - section: Original source P2-S3-C8
    page: 2
    quote: 'Methods

      Subjects

      Subjects were adults with ®rst ever, non-lacunar, ischaemic stroke

      affecting the left MCA territory as determined by MRI.'
    supports: sample
  - section: Original source P3-S2-C9
    page: 3
    quote: 'A neuroradiologist and two technicians, without knowledge of

      the speech and language test results, identi®ed the presence or

      absence of abnormality on DWI and/or PWI in ®ve regions of

      interest on PWI: left insula, posterior inferior frontal gyrus

      (Broca''s area), precentral gyrus, postcentral gyrus and posterior

      superior temporal lobe (Wernicke''s area).'
    supports: method
  - section: Original source P3-S2-C10
    page: 3
    quote: 'Hypoperfused regions

      were de®ned as regions in which at least 25% of the region

      showed >2.5 s delay in time to peak arrival of contrast in that

      region,

      relative

      to

      the

      homologous

      region

      in

      the

      intact

      hemisphere,

      since

      such

      regions

      correspond

      to

      dysfunctional

      tissue (Barber et al., 1998; Hillis et al., 2001, 2002, 2003a).'
    supports: method
  - section: Original source P3-S1-C11
    page: 3
    quote: 'Apraxia of speech was de®ned as: (i) >10% total errors in each

      oral task (to avoid including those with normal speech, but

      occasional stumbling on a word); (ii) variable off-target attempts

      at articulating words; (iii) distorted, groping articulation; and (iv)

      impaired speech prosody, not attributable to muscle weakness,

      slowness or reduced range of movement of the muscles controlling

      speech articulation and phonation (i.e. not due to dysarthria).'
    supports: claim
  - section: Original source P3-S2-C4
    page: 3
    quote: 'Thus, it should be recognized that our tests may have missed

      subtle apraxia of speech (in patients with or without insular damage).'
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-24'
relationship_review:
  paper: Hillis2004
  proposal_id: R007
  review_status_sha256: 46f6d31154b4f0732a94482b6c77a72ade5f29eb51a2e0e16ebb781930ec552b
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 0634d439a2868eeba60a02214ef2aed6aa3e0cfb24e6d2f6573fb6419844b183
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 0634d439a2868eeba60a02214ef2aed6aa3e0cfb24e6d2f6573fb6419844b183
        A/passages.json: 354956721103fe18175efc68f053d8b36cafd1e21b5f30ef527fdb3db1368ee7
        A/raw.json: 713be954a277822c6605279e99c481382421be18bf5a4cce13c9a7db0b23fd25
        A/source-units.json: 4d631d022dec1b658e993b1379ade729349317afeef0bdfc7873582cfe1d9b65
        A/full-source-units.json: 2b2edc2664e43e46f20b7b94344ed6ccee8b45ae7cf0e7a724457009277cad5d
        A/meta.json: 2595b05b9090dd935a7c764b77a8268f08047fbff539cc3b04eb934a2566ee13
        A/table-images/TABLE-1-page-3-1.png: 23727e7dd8c7ef0b3f0ac77c405b7b2a1d212e890105c37cbc560d95ada8ea36
        A/table-images/page-3.png: 53080c11c64dc8a9679d4c0591f7cf72ad5e02f7ad266cf16c6bdaedbbdf1b1d
        A/table-images/page-6.png: 0e6974c811c8d802627563457f5b2167135a5cb0e8360889f0a02e6173426306
        A/table-images/page-5.png: eb767f5074378d155c1b2cf62d45fe4099974648cb11e17ae4fccce10c0ab8e7
        A/table-images/page-4.png: 240e9624620ae785181ae8c76da8bc2a3b88117afaf51dc4f55916e1d2d8a1d6
        A/table-images/TABLE-1-page-4-1.png: 10d16603ead7effa0eca3a3a891b6ab1c171a3faebeba83a644799da3a8574c0
        A/table-images/TABLE-4-page-6-1.png: 525c94378880a8f82ce55d9535337205edb44c119c482e2df6cb786d9e6b2034
        A/table-images/manifest.json: 4e47c61e7cbf222605d0138293dae435c3f976be14cd5bf7534a78f2d88b13c4
        A/table-images/TABLE-3-page-5-2.png: a1d17b92bbb89ddfc603a6af34f9c76e0cf2dfe7fa26d2687a87324e4a31ba33
        A/table-images/TABLE-2-page-5-1.png: b2992c3f6e82d5ae2c977026dc5fa915bf283c7192918db560aa4181d40d0ec6
        A/clauses/window-03/raw.json: 63de0f0b4e550fbf703d4c8378e84ad6509ae777373fc9a047a1696b5a57ca39
        A/clauses/window-03/prompt.txt: f41bb613d99740b14e39bece1dc08d8e24b79141ea6523a104bc9b1f6e90bc0e
        A/clauses/window-03/meta.json: c2bcdec1a8d305289e34c7a005e2d3d31ae45cbc5dd06b7204bd9afadd16124f
        A/clauses/window-04/raw.json: 9aa403f156391084112410561207fdfaa7624c47d515e97f5952cd2dc9ad637f
        A/clauses/window-04/prompt.txt: 5f990649a7bcae478e064b8f4b2ef9435014d368bd1a9a38822ce28b30913985
        A/clauses/window-04/meta.json: dcf1eca0770812e9c0353dfdee3b2c73666d1d1b03003c783dcca45281e9deb1
        A/clauses/window-05/raw.json: 0d9a9d3903a6d0d58c6d2515380eeeaa00d072b74a0113dbb9cc37904691efba
        A/clauses/window-05/prompt.txt: cc9f09549f7a434ca1d1b48a7037b60fdc154d987823770bf520acd3a7626ad4
        A/clauses/window-05/meta.json: a4989456d1ea7efef7c39aa64df589486f359fe92b82e0ee6299399cdafd8254
        A/clauses/window-02/raw.json: 84de532ed8c6f0bf1a99468de75ea1d3b9f92a116a25f4413d5b17a2d7e271e3
        A/clauses/window-02/prompt.txt: 966947df0feeb62f948524c670279b11cb1fa39cfaec8946956ca8654996d10f
        A/clauses/window-02/meta.json: cea7e5a60cfd6bb6803171e6f06bf17cfe7a12349c447a11edec281d12bd2af2
        A/clauses/window-01/raw.json: 511f71964a789b1d70578fc28942ff239ee83bb8ea9f4474b35f91583f7f9398
        A/clauses/window-01/prompt.txt: 3cc4fafcaba12f3ad6d64e2265a83bf458f5ba20f0db2b0a9f2c4983a610f613
        A/clauses/window-01/meta.json: 4bd83e4f03994262e7abc8bd8624a0f24627befa5dc428a70e5fbbd19cfb7f93
        A/clauses/window-06/raw.json: 8e0a2ff969167b7758e4d67fed9c1d889d385f0e1f8798f93490c519ed9e542f
        A/clauses/window-06/prompt.txt: 18ad37b8aeaf6ede053fe70da6e2f89ee59df661f2f0c64641b9c698aa2215f0
        A/clauses/window-06/meta.json: 71261df4d9494e72580f836b4f87e6b8b56fc9ae9e8f617165c3fd8f3ca21ce2
        A/tables/TABLE-4-page-6-5/raw.json: ead01ff9cbeb28622414e228bb64b060305c6f0ec34c021a9e244a13d48fbb0f
        A/tables/TABLE-4-page-6-5/prompt.txt: e5ab531bf5e96e2b82c10df53378a5b1186a6fcaf330da0efcb3711405e6de7d
        A/tables/TABLE-4-page-6-5/meta.json: f0118fcb02d4fe7e15ed3ec1c23a51629e48bc24cb0de8cf4806e25bab0bec2b
        A/tables/TABLE-3-page-5-4/raw.json: 9569083b0f03d49e41bd4336f9af86054adc9aff34ee9e5d1d18389775c7f5fd
        A/tables/TABLE-3-page-5-4/prompt.txt: 1c2802f0eaf0404d9093e971dfe2c8b0af1d4d623b6230d4ffb9f9bdc5cdee0f
        A/tables/TABLE-3-page-5-4/meta.json: 1fc57cfa986697429419227effdb0a63f059c0bfbd5d2d494c5f32aaa6e6ffc1
        A/tables/TABLE-2-page-5-3/raw.json: 3e4bf296c0e5ef15d8d92bbb0781df44951b2c03ab99c76ceb8798a337bb3bbc
        A/tables/TABLE-2-page-5-3/prompt.txt: 1bf422b9f81db68c18201ad8031bb9d92ab235914a6fd4239c22a935a61804aa
        A/tables/TABLE-2-page-5-3/meta.json: 0f2a42a3cdffad5912850b53d0cd1e360e6993bd50703bd6914108303be6bd10
        A/tables/TABLE-1-page-4-2/raw.json: 600940a3b36d33f21451ff40577b3aa4210710045b4d7936de4f00f1c54dd87f
        A/tables/TABLE-1-page-4-2/prompt.txt: 8b27d91fa4aceaec52f0abab74d6c0c7c2b6e660c67254772d5ad63ac8cc9b11
        A/tables/TABLE-1-page-4-2/meta.json: db95b398daecae17a26a6b574d466b4c53446950ad2728610814f64911101ea3
        A/tables/TABLE-1-page-3-1/raw.json: 42c1bf6e32dbae8b5d187225d02f6a38681c1567d5ff84223379eeaea794e58d
        A/tables/TABLE-1-page-3-1/prompt.txt: fe183543f1b958cf1803128118f6478f59963e7f66fb3330f7836fd50bacc487
        A/tables/TABLE-1-page-3-1/meta.json: f3591fa41251bca82b3700519bc1551549e5e8edb1d31d4bdcaaef81c3c62abc
        B/passages.json: 354956721103fe18175efc68f053d8b36cafd1e21b5f30ef527fdb3db1368ee7
        B/raw.json: f947b623731cbb7017d36132d2c936c27a47ded1cd028f8c3648700436e7fa80
        B/source-units.json: 4d631d022dec1b658e993b1379ade729349317afeef0bdfc7873582cfe1d9b65
        B/full-source-units.json: 2b2edc2664e43e46f20b7b94344ed6ccee8b45ae7cf0e7a724457009277cad5d
        B/meta.json: 37e4b1804736db7a862b771406cec2c3f1f11df0fbc42e191c6ff23332ad0f70
        B/table-images/TABLE-1-page-3-1.png: 23727e7dd8c7ef0b3f0ac77c405b7b2a1d212e890105c37cbc560d95ada8ea36
        B/table-images/page-3.png: 53080c11c64dc8a9679d4c0591f7cf72ad5e02f7ad266cf16c6bdaedbbdf1b1d
        B/table-images/page-6.png: 0e6974c811c8d802627563457f5b2167135a5cb0e8360889f0a02e6173426306
        B/table-images/page-5.png: eb767f5074378d155c1b2cf62d45fe4099974648cb11e17ae4fccce10c0ab8e7
        B/table-images/page-4.png: 240e9624620ae785181ae8c76da8bc2a3b88117afaf51dc4f55916e1d2d8a1d6
        B/table-images/TABLE-1-page-4-1.png: 10d16603ead7effa0eca3a3a891b6ab1c171a3faebeba83a644799da3a8574c0
        B/table-images/TABLE-4-page-6-1.png: 525c94378880a8f82ce55d9535337205edb44c119c482e2df6cb786d9e6b2034
        B/table-images/manifest.json: 204ed9c04c847cbf8d0562fcbfc405d6035a6fc8d7b882eea50f0a131bbe43e1
        B/table-images/TABLE-3-page-5-2.png: a1d17b92bbb89ddfc603a6af34f9c76e0cf2dfe7fa26d2687a87324e4a31ba33
        B/table-images/TABLE-2-page-5-1.png: b2992c3f6e82d5ae2c977026dc5fa915bf283c7192918db560aa4181d40d0ec6
        B/clauses/window-03/raw.json: 37660a7480971c86050b88de818fe9e41b2362f993cadae5da0bf514bb29355a
        B/clauses/window-03/prompt.txt: f41bb613d99740b14e39bece1dc08d8e24b79141ea6523a104bc9b1f6e90bc0e
        B/clauses/window-03/meta.json: 873354adcf9f30c7ea82d6154fdbea960373cd6455f566da75499b6728bc4a64
        B/clauses/window-04/raw.json: 06ae445572065f0d024c4c213f149261f714c59e4446c8434f3dc9a762c4c143
        B/clauses/window-04/prompt.txt: 5f990649a7bcae478e064b8f4b2ef9435014d368bd1a9a38822ce28b30913985
        B/clauses/window-04/meta.json: 9a23f613787ab227477ffa2985819fedbd75bd43e8255979ca882c95b51b35e9
        B/clauses/window-05/raw.json: 95e6545db220fb53563e2782ba4b157aadf59ddaf4a3319e55639b6ad549359f
        B/clauses/window-05/prompt.txt: cc9f09549f7a434ca1d1b48a7037b60fdc154d987823770bf520acd3a7626ad4
        B/clauses/window-05/meta.json: 9e08a5477632f72ce52cb8f21f7a4d8c29453c9eecad444532f77c2a1fff9cb2
        B/clauses/window-02/raw.json: 4921683d10676290b41de0fa1bcc09e36cbedecac5651c3c446f654e13d0e323
        B/clauses/window-02/prompt.txt: 966947df0feeb62f948524c670279b11cb1fa39cfaec8946956ca8654996d10f
        B/clauses/window-02/meta.json: b9698b87eb6e7cb032a52c3a64c59316a3e545e546cf7cda3c0f1e3a8918e16a
        B/clauses/window-01/raw.json: 8633b06ff5c35da713777e70f39e28da2a26685ef40e7322329491bbcf83a6fa
        B/clauses/window-01/prompt.txt: 3cc4fafcaba12f3ad6d64e2265a83bf458f5ba20f0db2b0a9f2c4983a610f613
        B/clauses/window-01/meta.json: f4088d44cbcd33fca29cc6b694f73570029d3af0fede25510240fcdb1e663bcf
        B/clauses/window-06/raw.json: bc0858b94e3e6d4363b38513a25f24559bfa8ac2b6c543c583a67e8c0a601935
        B/clauses/window-06/prompt.txt: 18ad37b8aeaf6ede053fe70da6e2f89ee59df661f2f0c64641b9c698aa2215f0
        B/clauses/window-06/meta.json: 6b8c82779e6f7fe481efde2a5f1a73829ba07c1253b451affb3a356e3244b687
        B/tables/TABLE-4-page-6-5/raw.json: ead01ff9cbeb28622414e228bb64b060305c6f0ec34c021a9e244a13d48fbb0f
        B/tables/TABLE-4-page-6-5/prompt.txt: e5ab531bf5e96e2b82c10df53378a5b1186a6fcaf330da0efcb3711405e6de7d
        B/tables/TABLE-4-page-6-5/meta.json: 019a0c86b8befc5f57a079dbd4cc0776eb9ea3d014321530f8a677d787c40fa8
        B/tables/TABLE-3-page-5-4/raw.json: 9569083b0f03d49e41bd4336f9af86054adc9aff34ee9e5d1d18389775c7f5fd
        B/tables/TABLE-3-page-5-4/prompt.txt: 1c2802f0eaf0404d9093e971dfe2c8b0af1d4d623b6230d4ffb9f9bdc5cdee0f
        B/tables/TABLE-3-page-5-4/meta.json: a33a46c7cc13ba0cc90bb40111a760f2c0b3e59ebd95e49fed5e772dbeff871b
        B/tables/TABLE-2-page-5-3/raw.json: 3e4bf296c0e5ef15d8d92bbb0781df44951b2c03ab99c76ceb8798a337bb3bbc
        B/tables/TABLE-2-page-5-3/prompt.txt: 1bf422b9f81db68c18201ad8031bb9d92ab235914a6fd4239c22a935a61804aa
        B/tables/TABLE-2-page-5-3/meta.json: 37978370f2b8ac8315dceedb0401e02826a08da628fed8fc5c0a33fb3546eaea
        B/tables/TABLE-1-page-4-2/raw.json: 600940a3b36d33f21451ff40577b3aa4210710045b4d7936de4f00f1c54dd87f
        B/tables/TABLE-1-page-4-2/prompt.txt: 8b27d91fa4aceaec52f0abab74d6c0c7c2b6e660c67254772d5ad63ac8cc9b11
        B/tables/TABLE-1-page-4-2/meta.json: 4513444f7a275876356a0d51fda5267e8b050007debd542bd0ff6384705f3d89
        B/tables/TABLE-1-page-3-1/raw.json: 387be5d2ecb8e3818b97f735cb6098404b1f2f5e9447cf6608b1e60ed3794cf2
        B/tables/TABLE-1-page-3-1/prompt.txt: fe183543f1b958cf1803128118f6478f59963e7f66fb3330f7836fd50bacc487
        B/tables/TABLE-1-page-3-1/meta.json: 4947b0464271a36907f183a78e11fb18044d2bd9bb1c8c3efcab30659b69ff01
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
      pdf_sha256: 0634d439a2868eeba60a02214ef2aed6aa3e0cfb24e6d2f6573fb6419844b183
      source_review: _compare/relationships-2026-11-16/review-current/Hillis2004
      source_status_sha256: c5c17a08cc3f835d0db761c9215f4a10d3b9670834e0357352d6d4f7453d2624
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R007
    exposure:
      text: hypoperfusion and/or infarct of Broca's area
    outcome:
      text: apraxia of speech
    analysis_label: Dysfunctional tissue analysis (DWI/PWI) of Broca's area
    relation: association
    evidence_ids:
    - P3-S4-C2
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
      pdf_sha256: 0634d439a2868eeba60a02214ef2aed6aa3e0cfb24e6d2f6573fb6419844b183
      source_review: _compare/relationships-2026-11-16/review-current/Hillis2004
      source_status_sha256: c5c17a08cc3f835d0db761c9215f4a10d3b9670834e0357352d6d4f7453d2624
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Accounting without a linked unit P1-S2-C2
      - Accounting without a linked unit P1-S2-C3
      - Unaccounted source passage P1-S2-C3
      - Unaccounted source passage P1-S2-C2
      - Result passage disposed without unit P3-S1-C8
      - Result passage disposed without unit P3-S1-C9
      - Result passage disposed without unit P3-S2-C2
      - Accounting without a linked unit P3-S3-C10
      - Accounting without a linked unit P3-S3-C12
      - Result passage disposed without unit P3-S3-C2
      - Accounting without a linked unit P3-S3-C6
      - Accounting without a linked unit P3-S3-C7
      - Accounting without a linked unit P3-S3-C9
      - Accounting without a linked unit P3-S4-C1
      - Unaccounted source passage P3-S3-C7
      - Unaccounted source passage P3-S3-C9
      - Unaccounted source passage P3-S3-C6
      - Unaccounted source passage P3-S4-C1
      - Unaccounted source passage P3-S3-C12
      - Unaccounted source passage P3-S3-C10
      - Result passage disposed without unit P6-S1-C1
      - Result passage disposed without unit P6-S1-C2
      - Result passage disposed without unit P7-S1-C7
      - Accounting without a linked unit P7-S2-C5
      - Unaccounted source passage P7-S2-C5
      - Accounting without a linked unit P7-S3-C2
      - Accounting without a linked unit P7-S3-C3
      - Accounting without a linked unit P7-S3-C5
      - Accounting without a linked unit P7-S3-C6
      - Accounting without a linked unit P7-S3-C8
      - Accounting without a linked unit P7-S3-C9
      - Unaccounted source passage P7-S3-C5
      - Unaccounted source passage P7-S3-C6
      - Unaccounted source passage P7-S3-C3
      - Unaccounted source passage P7-S3-C9
      - Unaccounted source passage P7-S3-C2
      - Unaccounted source passage P7-S3-C8
      unattached_null_or_qualifier_ids:
      - P3-S3-C10
      - P5-S3-C4
      - P7-S1-C7
      - P7-S2-C5
      suppressed_nonrepresented_units: 5
      default_disposition_count_requires_completeness_check: 117
      unselected_timing_passages:
      - P2-S3-C6
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P3-S3-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P3-S3-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P3-S3-C12
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P3-S4-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P3-S4-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S1-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P3-S1-C6
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P3-S2-C2
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      empty_frame_slots_require_confirmation:
      - validation
      - analysis_restrictions
      - personal_factors
      - tested_personal_effects
      - adjustment_roles
      - explicitly_not_adjusted
      unclassified_extraction_ids:
      - P5-S1-C13
      - P5-S3-C4
      table_review_required:
      - TABLE-1-page-3-1
      - TABLE-1-page-4-2
      - TABLE-2-page-5-3
      - TABLE-3-page-5-4
      - TABLE-4-page-6-5
      unlinked_tables:
      - TABLE-1-page-3-1
      - TABLE-1-page-4-2
      - TABLE-2-page-5-3
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P3-S3
        - P4-S1
        - P6-S1
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 0634d439a2868eeba60a02214ef2aed6aa3e0cfb24e6d2f6573fb6419844b183
      source_review: _compare/relationships-2026-11-16/review-current/Hillis2004
      source_status_sha256: c5c17a08cc3f835d0db761c9215f4a10d3b9670834e0357352d6d4f7453d2624
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S2-C2
      disposition: represented
      result_indexes:
      - 0
      - 1
      - 2
      reason: Summary of null associations between apraxia of speech and insular regions.
    - source_id: P1-S2-C3
      disposition: represented
      result_indexes:
      - 6
      reason: Summary of association between apraxia of speech and left posterior
        inferior frontal gyrus (Broca's area).
    - source_id: P3-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes normative data scores for control subjects.
    - source_id: P3-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes interjudge reliability for test scoring.
    - source_id: P3-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes interjudge reliability for apraxia scoring.
    - source_id: P3-S3-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes interjudge reliability for imaging identification.
    - source_id: P3-S3-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes mean volume of dense ischaemia/infarction.
    - source_id: P3-S3-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes mean volume of hypoperfusion.
    - source_id: P3-S3-C9
      disposition: represented
      result_indexes:
      - 0
      reason: Reports null association between apraxia of speech and left insula damage
        on DWI.
    - source_id: P3-S3-C10
      disposition: represented
      result_indexes:
      - 1
      - 2
      reason: Reports null associations between apraxia of speech and DWI abnormalities
        in anterior insula and superior tip of precentral gyrus of the insula.
    - source_id: P3-S3-C12
      disposition: represented
      result_indexes:
      - 3
      - 4
      - 5
      reason: Introduces the analysis of dysfunctional brain tissue (DWI/PWI).
    - source_id: P3-S4-C1
      disposition: represented
      result_indexes:
      - 3
      - 4
      - 5
      reason: Reports null associations between apraxia of speech and dysfunction
        of left insula, anterior insula, and superior tip of precentral gyrus of the
        insula.
    - source_id: P3-S4-C2
      disposition: represented
      result_indexes:
      - 6
      reason: Reports significant association between apraxia of speech and dysfunction
        of Broca's area.
    - source_id: P3-S4-C3
      disposition: represented
      result_indexes:
      - 7
      reason: States results were identical for patients with or without insular damage.
    - source_id: P4-S1-C1
      disposition: represented
      result_indexes:
      - 7
      reason: Provides specific chi-square results for Broca's area association stratified
        by insular damage.
    - source_id: P5-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes specific patient counts of exceptions.
    - source_id: P5-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes specific patient counts of exceptions.
    - source_id: P5-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes specific patient counts of exceptions.
    - source_id: P5-S1-C5
      disposition: repeated
      result_indexes:
      - 6
      reason: Restatement of the association between apraxia of speech and Broca's
        area dysfunction.
    - source_id: P5-S3-C3
      disposition: repeated
      result_indexes:
      - 6
      reason: Restatement of the association between apraxia of speech and Broca's
        area dysfunction.
    - source_id: P5-S3-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discusses the possibility of other essential areas based on exceptional
        cases.
    - source_id: P6-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes specific patient counts of exceptions.
    - source_id: P6-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes specific patient counts of exceptions.
    - source_id: P7-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes specific patient counts of exceptions.
    - source_id: P7-S2-C5
      disposition: repeated
      result_indexes:
      - 6
      reason: Restatement of the significant association between Broca's area and
        apraxia of speech.
    - source_id: P7-S2-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about MCA stenosis leading to insular damage and hypoperfusion.
    - source_id: P7-S3-C2
      disposition: repeated
      result_indexes:
      - 6
      reason: Restatement of the association between Broca's area and apraxia of speech.
    unresolved_coverage: []
    pending_source_ids:
    - P1-S2-C2
    - P1-S2-C3
    - P3-S1-C8
    - P3-S1-C9
    - P3-S2-C2
    - P3-S3-C2
    - P3-S3-C6
    - P3-S3-C7
    - P3-S3-C12
    - P3-S4-C3
    - P5-S1-C2
    - P5-S1-C3
    - P5-S1-C4
    - P5-S1-C5
    - P5-S3-C3
    - P5-S3-C4
    - P6-S1-C1
    - P6-S1-C2
    - P7-S1-C7
    - P7-S2-C5
    - P7-S2-C12
    - P7-S3-C2
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-3-1
    - TABLE-1-page-4-2
    - TABLE-2-page-5-3
    - TABLE-3-page-5-4
    - TABLE-4-page-6-5
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P2-S3-C6
      recruited_sample:
      - P2-S3-C6
      eligibility:
      - P2-S4-C2
      imaging_provenance:
      - P3-S2-C5
      - P3-S2-C9
      imaging_timing:
      - P2-S3-C7
      - P3-S2-C5
      outcome_timing:
      - P2-S3-C7
      outcome_definition:
      - P3-S1-C11
      validation: []
      analysis_restrictions: []
      dependent_variable_statement:
      - P3-S3-C3
      limitations:
      - P3-S2-C4
      - P3-S3-C5
      - P7-S3-C10
      - P7-S3-C11
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles: []
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P3-S1-C6
      - P3-S1-C7
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: internal_cross_validation
    held_selections:
    - slot: dependent_variable_statement
      source_id: P3-S3-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P3-S3-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P3-S3-C12
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P3-S4-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P3-S4-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S1-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P3-S1-C6
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P3-S2-C2
      reason: No validation-design cue; inspect the source rather than inferring a
        design
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
      pdf_sha256: 0634d439a2868eeba60a02214ef2aed6aa3e0cfb24e6d2f6573fb6419844b183
      review_sha256: 46f6d31154b4f0732a94482b6c77a72ade5f29eb51a2e0e16ebb781930ec552b
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
      - P3-S4-C2
      source_result: The presence of apraxia of speech was associated with hypoperfusion
        and/or infarct of Broca's area (c2(1) = 46.4; P < 0.00001), but not with other
        regions evaluated. This association was observed in patients with and without
        insular damage.
      result_status: detected
      patient_measurement: voxel_tissue
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis corresponds to the association between apraxia
            of speech and dysfunction in Broca's area, as described in P3-S4-C2. The
            proposed core correctly identifies this specific relationship.
          source_ids:
          - P3-S4-C2
        direction:
          answer: fits
          reason: The source explicitly states that apraxia of speech was associated
            with hypoperfusion and/or infarct of Broca's area. The proposed core correctly
            reflects this detected association.
          source_ids:
          - P3-S4-C2
        construct:
          answer: fits
          reason: The exposure (hypoperfusion/infarct of Broca's area) and outcome
            (apraxia of speech) are correctly identified. The measurement method (DWI/PWI)
            is accurately described in the definition and method fields.
          source_ids:
          - P3-S4-C2
          - P3-S2-C5
          - P3-S2-C9
        qualifications:
          answer: fits
          reason: The qualification that the association held regardless of insular
            damage is correctly included, as supported by P4-S1-C1. The definition
            of apraxia of speech is also accurately captured.
          source_ids:
          - P4-S1-C1
          - P3-S1-C11
        missing_material_caveat:
          answer: fits
          reason: The limitation regarding bedside testing potentially missing subtle
            apraxia of speech is included. No other material caveats that would change
            the interpretation of this specific association are omitted.
          source_ids:
          - P3-S2-C4
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
      original: 80
      action: not_transcribed
      reason: Not supported by selected quotations
    analysis_identity:
      id: R007
      exposure:
        text: hypoperfusion and/or infarct of Broca's area
      outcome:
        text: apraxia of speech
      analysis_label: Dysfunctional tissue analysis (DWI/PWI) of Broca's area
      relation: association
      evidence_ids:
      - P3-S4-C2
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
        pdf_sha256: 0634d439a2868eeba60a02214ef2aed6aa3e0cfb24e6d2f6573fb6419844b183
        source_review: _compare/relationships-2026-11-16/review-current/Hillis2004
        source_status_sha256: c5c17a08cc3f835d0db761c9215f4a10d3b9670834e0357352d6d4f7453d2624
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
  page: 3
  quote: 'Instead, the presence of apraxia of speech was associated with

    hypoperfusion and/or infarct of Broca''s area [c2(1) = 46.4;

    P < 0.00001; Table 3], but not with other regions evaluated.'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-24'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
