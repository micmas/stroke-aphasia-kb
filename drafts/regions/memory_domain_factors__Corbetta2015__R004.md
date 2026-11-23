---
id: memory_domain_factors
name: memory domain factors
kind: network
findings:
- id: f1
  target: memory_impairment
  target_kind: impairment
  claim: 'Within the memory domain, two factors explained 66% of the variance: one
    factor for visuospatial memory and a different factor for verbal memory; these
    two factors were correlated and did not differentiate the side of the lesion.'
  direction: likely
  relationship: correlational
  method: behavioral_only
  sample:
    n: 98
    population: first-time stroke patients with heterogeneous lesions
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
  - The analysis of memory factors was based on a subset of the total sample (n=98)
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Principal component analysis (PCA) with oblique rotation
    performed on behavioral test scores within the memory domain, including measures
    of immediate and delayed recall, recognition, and familiarity for both verbal
    and spatial memory. The two memory factors were correlated; The factors did not
    differentiate the side of the lesion. Additional metadata has not been transcribed;
    review the pending-field flags before approval. PDF image reading (P3-S2-C10,
    two-model agreement, human verification pending): RESULTS


    Subjects (n = 172) with a first symptomatic stroke, ischemic or hemorrhagic, anywhere
    in the brain and clinical evidence of any neurological impairment were prospectively
    recruited, with n = 132 meeting post-enrollment inclusion criteria (see Experimental
    Procedures and Supplemental Information for details about subjects, Figure S1
    for enrollment flowchart) Original text-layer quotation is preserved below. PDF
    image reading (P14-S2-C15, two-model agreement, human verification pending): .
    (2) First symptomatic stroke, ischemic or hemorrhagic Original text-layer quotation
    is preserved below.'
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
    - not_transcribed:sample.time_post_onset
    - proposed_concept:memory_impairment
  citation: '@Corbetta2015'
  source_passages:
  - section: Original source P4-S3-C10
    page: 4
    quote: 'In the memory domain (n = 98), two factors explained 66% of

      the variance: visuospatial memory loaded on one factor with cor-

      relations among tasks between r = 0.68 and 0.80 (Figure 2G), and

      verbal memory loaded on a different factor with correlations

      among tasks between r = 0.74 and 0.93 (Figure 2H).'
    supports: claim
  - section: Original source P4-S4-C3
    page: 4
    quote: 'The two memory factors were correlated and did not

      differentiate the side of the lesion (Figure 2I).'
    supports: claim
  - section: Original source P3-S2-C10
    page: 3
    quote: 'RESULTS

      Subjects (n = 172) with a ﬁrst symptomatic stroke, ischemic or

      hemorrhagic, anywhere in the brain and clinical evidence of

      any neurological impairment were prospectively recruited, with

      n = 132 meeting post-enrollment inclusion criteria (see Experi-

      mental Procedures and Supplemental Information for details

      about subjects, Figure S1 for enrollment ﬂowchart).'
    supports: sample
  - section: Original source P3-S3-C2
    page: 3
    quote: 'This report concen-

      trates on the acute neurobehavioral assessment (mean 13 ±

      4.9 days) and structural MRI studies (Figure 1 for experimental

      design).'
    supports: method
  - section: Original source P3-S3-C7
    page: 3
    quote: 'The Memory battery separately

      examined verbal and spatial memory, and in each domain imme-

      diate and delayed recall, recognition, and familiarity.'
    supports: method
  - section: Original source P4-S2-C7
    page: 4
    quote: 'A PCA with oblique rotation was run separately on the behav-

      ioral data for each domain (e.g., motor, language, attention,

      memory) (Table 1).'
    supports: method
  - section: Original source P14-S2-C15
    page: 14
    quote: '(2) First symp-

      tomatic stroke, ischemic or hemorrhagic.'
    supports: sample
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-23'
relationship_review:
  paper: Corbetta2015
  proposal_id: R004
  review_status_sha256: 9c574d7b8509dff745747042828cbe11b405a1a6132cb876077c0eed0c344e75
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: a0dd390561996aeeca449d85e827d3dc2d7ea0f2af2c8c6f2234ace8f68f5220
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: a0dd390561996aeeca449d85e827d3dc2d7ea0f2af2c8c6f2234ace8f68f5220
        A/passages.json: 407057e2622bb2ac2654bcd8b3487d3b1515870cb737b64e0c56461fd5341703
        A/raw.json: e1dfa40729a168bac720bcd577f3cbc580f686c6aaa3145922ec5abd74f0861e
        A/source-units.json: 9982de826807cb94029e34467e99d4a8265bba62493f2f8527c59ea456d5a76d
        A/full-source-units.json: 8d1b360c27e9fc37a2944cec74ac5bb7d10835d4c7d3803e6d553649cc6546ca
        A/meta.json: 841f530ff253488c235fababcc120c100f20273789d95bfa164c302457cfa6ab
        A/table-images/TABLE-1-page-6-1.png: 79e3457df3d6e2928f9c09f0c96c1fac19f87c793fb7d8f4ebece93558a3029f
        A/table-images/page-6.png: b63b5a508f0e1e072743db0844a979c24beb5305a5a01b74e62a818afb721b86
        A/table-images/TABLE-1-page-6-2.png: 7c9cb0ec0ec35f8a2df0a754eaf4932423ce44a89b5a51e3c5b87d1fd2e5c7ae
        A/table-images/manifest.json: d564242aaf4ee799cf82b10512c5746812db6e8495f8b4d56f52eebc2aae043b
        A/clauses/window-11/raw.json: 4ac97247e2c0ff34603e4f1f0c0e3b44fa93efc698f206a2fc9ea5381a6aa3a7
        A/clauses/window-11/prompt.txt: 2545d3dc40c57bbf581a521fd6c58ac3e6d498fc937737c1e0344d52d7cb8981
        A/clauses/window-11/meta.json: bb3f98440428ed853087d213495f541e27b2debd74900206a0c3032d95f5e7ea
        A/clauses/window-10/raw.json: 704d23ad026663aabb71ca0e83b5b4e93c2fa509eab98eccde61d56e4c657ea4
        A/clauses/window-10/prompt.txt: 0fe6101cdb292dcc290fcc8699d63a2ff9a67badf04d9a353143a6fe26b96f3d
        A/clauses/window-10/meta.json: f16fc88046402dd49be79b536116bf099de1cdd56e0a65b803b6f42cd6b9be76
        A/clauses/window-03/raw.json: e077ea229c9892ce41b901d96a00a603ee78b4159d6c455e8341ddd2a3b55335
        A/clauses/window-03/prompt.txt: 67cf71f2cd85bad58e5ee2ab8edf524d2eabad5f6277e07e175ce1be1658b348
        A/clauses/window-03/meta.json: 3de8ba3c7a835351ab2bf781514bca4dc26dd4ce1b67d8bb35301b0a59fc57d4
        A/clauses/window-04/raw.json: f547dbc98212005288fc8e080463c540e077f7ea612fb482d5d2d937f2556e5b
        A/clauses/window-04/prompt.txt: 643cd6ce345a2813170d97099bfc1d43f1c689e780d7716abed8432a751674c0
        A/clauses/window-04/meta.json: 3ed744439df582fe094714574d52e2ec3eb058e7ea6f7aea07ccbd6608c390c0
        A/clauses/window-05/raw.json: 600c8e2fb3f2845f9e42ea760652514b4a28dbdb8947327468a6483f6a1813af
        A/clauses/window-05/prompt.txt: 6ea385a07f33f132840367d4d1e909e5f2c134602d15b803b4c1ba2c4ef5fe3b
        A/clauses/window-05/meta.json: 13c23feecb6cf4442faabd1925c98a6934e869c5a352eb179c7253c8ed61e98b
        A/clauses/window-02/raw.json: 99ac6f02374606c69e279ed4e0ebd7aedbba35c1796541124f365ff12a7bdf26
        A/clauses/window-02/prompt.txt: a5c81e5f9c7f5b47202c18ba03ca25f613b56c65ab937c061a8fe188f4d2acc5
        A/clauses/window-02/meta.json: f3f7c7542007449dc4894a53342e07ac79f38faa2df6cc641fa598dfc74831d5
        A/clauses/window-12/raw.json: 5841deb53ad22c0d91e33b6eaa20fe5865ab5cd31c6ab0c06a3a284ddadb200d
        A/clauses/window-12/prompt.txt: ee119a44bafa6982af32811af45e57e6fc9c44711848137dae7a0f694e4438d0
        A/clauses/window-12/meta.json: 80ff973759ad047fb77d76c659b1a0f5e1241ffe15a9705071b15c4e2ac73ec6
        A/clauses/window-13/raw.json: 8bf41d3d31d123a2e3b8abb39f446330446335f3e4b6fca1c3d79df0fa6b7a02
        A/clauses/window-13/prompt.txt: d2efb6f35a82af1faca853bd4a22d95ee7154ad7bca8df567bb49ee6a8ef1e94
        A/clauses/window-13/meta.json: 970ba40bc86aa0a7e252071a51aaf432743d53b5a8a22fc980274851923b848c
        A/clauses/window-09/raw.json: 6485e4d895306ab8d80d23fead1c1a3bb7fab7c0afe101d407489510593d4323
        A/clauses/window-09/prompt.txt: 6749ee42d160677ebe506cd9ed0ffba966fbc9f0d954bd5bfd2dbbba33261b11
        A/clauses/window-09/meta.json: d15a5cb8af5b3e454b30114616d883d5d044417b46880d1d4f3849a90c493b6b
        A/clauses/window-07/raw.json: 3445253c6497bedd3f9d5584d5a4ca6e28444b9103f858ed8dba4f727210b0c3
        A/clauses/window-07/prompt.txt: 84a582dbb07dac1f248b378232c503e621f40b0a039b22e52dd9c86486e78595
        A/clauses/window-07/meta.json: fdf25e9f07be64f3753145a4fb2cde67eb5b3c959b5832b579fd9ca3904673da
        A/clauses/window-01/raw.json: 1d34b41363b1ae1861eb0a162fe452f85a7ea7cb303c9d404be24ec4ca94903e
        A/clauses/window-01/prompt.txt: fdcc4301758acabdb9dc3413038c0cc2d515aab1279e4305563062297dadd0bc
        A/clauses/window-01/meta.json: 4e39967591179eef3948e880aaa0150e8fc816025ccdde8c7cb91cf06e1140e1
        A/clauses/window-06/raw.json: 6b326339788f9d65685bda8ba925e03fe8cbcd9c1a0099c41c61a001e96a38cd
        A/clauses/window-06/prompt.txt: a5312b50f3eebb1d2bee66e0ceb659b702f9da3e177c789d2188a8065773d219
        A/clauses/window-06/meta.json: 0a87c8bed43147b418d4fcec78fe63d8f419ca664aa9c7c0585d9ed284f36f07
        A/clauses/window-08/raw.json: 0574d1f44d8e331be0617b77d454610e928e492c2b466f0f354b339890e2f242
        A/clauses/window-08/prompt.txt: 00efa64d80792308c89dd72ca3887b493aa2f402ced4c921fed0032591c60350
        A/clauses/window-08/meta.json: 0d2f09e75d621fb176f0dd73ebc09559fd6cabfe8d9f0654e80d1c3e06069687
        A/tables/TABLE-1-page-6-1/raw.json: 9f8cbbd2356fc259731365d97605834b2b8ea5241189ac134675d03127ec603e
        A/tables/TABLE-1-page-6-1/prompt.txt: 92b4e5f93683139b4fa00e98b49b7801779cc172b811ed836d61463c6531a2f6
        A/tables/TABLE-1-page-6-1/meta.json: e6798dea17c4a43734ee7a4a3012cbec264ebd74adf50e578692562f05145388
        A/tables/TABLE-1-page-6-2/raw.json: eb73ef9bd4b3015b0dabfc2626f36cbc5afa0cf7c132abd0c47e0bb4cae836a7
        A/tables/TABLE-1-page-6-2/prompt.txt: e0bbd9c0c95f7d7980f53a42dc083650e1773ffc6ca00e95ac80033c2f856541
        A/tables/TABLE-1-page-6-2/meta.json: 02f98c956695c65e419badab090b3ddff12594debdf7b8a6c6a792d5ef2cd7fd
        B/passages.json: 407057e2622bb2ac2654bcd8b3487d3b1515870cb737b64e0c56461fd5341703
        B/raw.json: 191daacf1f47f9279c8e58307ca4179c4deb503f8e6e4a46a1ad321115979df3
        B/source-units.json: 9982de826807cb94029e34467e99d4a8265bba62493f2f8527c59ea456d5a76d
        B/full-source-units.json: 8d1b360c27e9fc37a2944cec74ac5bb7d10835d4c7d3803e6d553649cc6546ca
        B/meta.json: 6e11fa972f00ac3f4a32c0427d96d748bad3c00e3c5a37c9e83836bd84fc9785
        B/table-images/TABLE-1-page-6-1.png: 79e3457df3d6e2928f9c09f0c96c1fac19f87c793fb7d8f4ebece93558a3029f
        B/table-images/page-6.png: b63b5a508f0e1e072743db0844a979c24beb5305a5a01b74e62a818afb721b86
        B/table-images/TABLE-1-page-6-2.png: 7c9cb0ec0ec35f8a2df0a754eaf4932423ce44a89b5a51e3c5b87d1fd2e5c7ae
        B/table-images/manifest.json: 1ae345831f9fff2d6ee677281a74b282abbcbc8e39d580da11a3f91bad9ebaf8
        B/clauses/window-11/raw.json: 48ce91a9efbcedfa7bbf1311e0cd1d2355cbd3dd2a78693233e69930183cc1e8
        B/clauses/window-11/prompt.txt: 2545d3dc40c57bbf581a521fd6c58ac3e6d498fc937737c1e0344d52d7cb8981
        B/clauses/window-11/meta.json: 65ccffbb4513df9069453ada9e688732b2b243e2778c2bd4ca70828c9eb5c611
        B/clauses/window-10/raw.json: 11a40d0864d529166a441b129571f0299a783edbd2b08389803ccf91657019fd
        B/clauses/window-10/prompt.txt: 0fe6101cdb292dcc290fcc8699d63a2ff9a67badf04d9a353143a6fe26b96f3d
        B/clauses/window-10/meta.json: 53df2698cdc9c79eb62440cce63986bb153e20bc218ef6bb9859ef98d5ce4c14
        B/clauses/window-03/raw.json: d9cf37f744ce9bdfa9d1fb4dd7c8c20d6c212763628abb9e66c4916618976f76
        B/clauses/window-03/prompt.txt: 67cf71f2cd85bad58e5ee2ab8edf524d2eabad5f6277e07e175ce1be1658b348
        B/clauses/window-03/meta.json: b0045fa3c0ab1581422fa19684ee66d4737eebb94f9727f3c9af0bae7287dabd
        B/clauses/window-04/raw.json: 1a951a0bdfa03b41cada0dbfacf7314c04fd4fef2cbd370b3645cceeb827e7c2
        B/clauses/window-04/prompt.txt: 643cd6ce345a2813170d97099bfc1d43f1c689e780d7716abed8432a751674c0
        B/clauses/window-04/meta.json: f38f6d342919f99f1cf35d61175ac34b278172b8e647dfdb6045843e4b9c3f50
        B/clauses/window-05/raw.json: 430a4eeb05767fb83cd0330abc225983a68b6a340006284bb03367423151cf0d
        B/clauses/window-05/prompt.txt: 6ea385a07f33f132840367d4d1e909e5f2c134602d15b803b4c1ba2c4ef5fe3b
        B/clauses/window-05/meta.json: 634c816f6eb4437b6fc8693daaabc09db5aaf6b2270ecd0d9685ca4fef56b090
        B/clauses/window-02/raw.json: de4edca2054b6c634be91aa0c9ed742d8463f83f9674a3728eb10fda7f0038c8
        B/clauses/window-02/prompt.txt: a5c81e5f9c7f5b47202c18ba03ca25f613b56c65ab937c061a8fe188f4d2acc5
        B/clauses/window-02/meta.json: e242b665e49dceb7c6786912307ad7ef0d237690625f3fe761f2666c6b6500d1
        B/clauses/window-12/raw.json: a49c70c5fde43ec9f3287f5e620cf1bc77afc5db55dc66dd8c37e95fc98f147d
        B/clauses/window-12/prompt.txt: ee119a44bafa6982af32811af45e57e6fc9c44711848137dae7a0f694e4438d0
        B/clauses/window-12/meta.json: 299bcd92d972e272ef857b5a61e52f87177ed7c0a55bf074e904239f67cf5b2d
        B/clauses/window-13/raw.json: d57c8176c0ab6b96d34a680061c2d3e737c8302cc42dada6d94b880398fd8150
        B/clauses/window-13/prompt.txt: d2efb6f35a82af1faca853bd4a22d95ee7154ad7bca8df567bb49ee6a8ef1e94
        B/clauses/window-13/meta.json: 5efcd5ab0f18832d58438a94bfc31cdfbe3524e8f74a462660c886355467f737
        B/clauses/window-09/raw.json: e07105e8b62372000b1cbe7c7749b9b7e33439ecdb696275b99afcbef99719f2
        B/clauses/window-09/prompt.txt: 6749ee42d160677ebe506cd9ed0ffba966fbc9f0d954bd5bfd2dbbba33261b11
        B/clauses/window-09/meta.json: fb048281de74041fa907f7e7a858043bdda8b68e6f6ed7e34d1b6bc2a79f63a4
        B/clauses/window-07/raw.json: 4f4072aa9fc469f7f42d9871c427965c1728d7a8f68e4aab9d89581ca279683f
        B/clauses/window-07/prompt.txt: 84a582dbb07dac1f248b378232c503e621f40b0a039b22e52dd9c86486e78595
        B/clauses/window-07/meta.json: 49a4b3ea1fdd0004fa7774210647b68f36be4262c72887458261ecb003715c91
        B/clauses/window-01/raw.json: 27a2e2b30870a8c398da84fd031e8c7e2e02fc6038a39288a749134071a691b9
        B/clauses/window-01/prompt.txt: fdcc4301758acabdb9dc3413038c0cc2d515aab1279e4305563062297dadd0bc
        B/clauses/window-01/meta.json: 4b5be1613966c66c46ac546dffc9f89fd2e5edc6b04a14cdf18ca53cf25a2205
        B/clauses/window-06/raw.json: afc3b1b3fdcfea94e5220c6f3ae361767a727c86854819358af9088bfa440361
        B/clauses/window-06/prompt.txt: a5312b50f3eebb1d2bee66e0ceb659b702f9da3e177c789d2188a8065773d219
        B/clauses/window-06/meta.json: 862e9d019a68a8dd243b2d87cb83bcc4fe9bd90b99de83fc7ec6fc7d7ff2d3fd
        B/clauses/window-08/raw.json: 7b4b2dba8d7dcac0f231d6e07e97df21e4856c5758c733bb406bcf78188f36fe
        B/clauses/window-08/prompt.txt: 00efa64d80792308c89dd72ca3887b493aa2f402ced4c921fed0032591c60350
        B/clauses/window-08/meta.json: ac52eb6189654e891ad5f38dce5a0659ccdb956367723869d58aae6f98765a6d
        B/tables/TABLE-1-page-6-1/raw.json: 4296fdb3362d008ff4a277280d21c6ddece23453c7dc64657e384e1e4b0ffb20
        B/tables/TABLE-1-page-6-1/prompt.txt: 92b4e5f93683139b4fa00e98b49b7801779cc172b811ed836d61463c6531a2f6
        B/tables/TABLE-1-page-6-1/meta.json: 4e13e2cad5832b21ed8b659bf5e8a82d649404398d494c0bbd8a9c34c0d9b8a2
        B/tables/TABLE-1-page-6-2/raw.json: 7f2251320146433d8298748cca9248e4e04b7501e07c73534c0c7175ff575162
        B/tables/TABLE-1-page-6-2/prompt.txt: e0bbd9c0c95f7d7980f53a42dc083650e1773ffc6ca00e95ac80033c2f856541
        B/tables/TABLE-1-page-6-2/meta.json: b8a5d6cc7784cade179b2694413134b5a257b451fc4d02648fc08e578f2cebef
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
      pdf_sha256: a0dd390561996aeeca449d85e827d3dc2d7ea0f2af2c8c6f2234ace8f68f5220
      source_review: _compare/relationships-2026-11-16/review-current/Corbetta2015
      source_status_sha256: 2096b379feb67ded892915a08230532ac0b1c5f3fa56fd9c62eca585dc93c850
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R004
    exposure:
      text: stroke
    outcome:
      text: visuospatial and verbal memory
    analysis_label: Within-Domain Factor Analysis (Memory)
    relation: association
    evidence_ids:
    - P4-S3-C10
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
      pdf_sha256: a0dd390561996aeeca449d85e827d3dc2d7ea0f2af2c8c6f2234ace8f68f5220
      source_review: _compare/relationships-2026-11-16/review-current/Corbetta2015
      source_status_sha256: 2096b379feb67ded892915a08230532ac0b1c5f3fa56fd9c62eca585dc93c850
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P1-S1-C1
      - Result passage disposed without unit P1-S1-C4
      - Accounting without a linked unit P2-S1-C12
      - Accounting without a linked unit P2-S1-C13
      - Accounting without a linked unit P2-S1-C14
      - Unaccounted source passage P2-S1-C13
      - Unaccounted source passage P2-S1-C12
      - Unaccounted source passage P2-S1-C14
      - Accounting without a linked unit P4-S1-C10
      - Accounting without a linked unit P4-S1-C6
      - Accounting without a linked unit P4-S1-C7
      - Accounting without a linked unit P4-S1-C8
      - Accounting without a linked unit P4-S1-C9
      - Unaccounted source passage P4-S1-C10
      - Unaccounted source passage P4-S1-C9
      - Unaccounted source passage P4-S1-C6
      - Unaccounted source passage P4-S1-C8
      - Unaccounted source passage P4-S1-C7
      - Result passage disposed without unit P4-S1-C11
      - Accounting without a linked unit P4-S2-C10
      - Accounting without a linked unit P4-S2-C11
      - Accounting without a linked unit P4-S2-C2
      - Accounting without a linked unit P4-S2-C9
      - Accounting without a linked unit P4-S3-C1
      - Accounting without a linked unit P4-S3-C2
      - Unaccounted source passage P4-S2-C10
      - Unaccounted source passage P4-S2-C11
      - Unaccounted source passage P4-S3-C2
      - Unaccounted source passage P4-S2-C2
      - Unaccounted source passage P4-S3-C1
      - Unaccounted source passage P4-S2-C9
      - Result passage disposed without unit P4-S3-C9
      - Accounting without a linked unit P4-S4-C5
      - Accounting without a linked unit P6-S1-C1
      - Accounting without a linked unit P6-S1-C2
      - Accounting without a linked unit P6-S1-C3
      - Accounting without a linked unit P6-S1-C5
      - Accounting without a linked unit P6-S1-C6
      - Accounting without a linked unit P6-S1-C7
      - Unaccounted source passage P6-S1-C3
      - Unaccounted source passage P6-S1-C7
      - Unaccounted source passage P6-S1-C5
      - Unaccounted source passage P6-S1-C1
      - Unaccounted source passage P4-S4-C5
      - Unaccounted source passage P6-S1-C6
      - Unaccounted source passage P6-S1-C2
      - Unresolved source passage P6-S1-C16
      - Result passage disposed without unit P7-S1-C6
      - Result passage disposed without unit P7-S2-C12
      - Result passage disposed without unit P7-S2-C13
      - Result passage disposed without unit P7-S3-C2
      - Result passage disposed without unit P7-S3-C3
      - Result passage disposed without unit P7-S3-C4
      - Result passage disposed without unit P8-S1-C11
      - Result passage disposed without unit P8-S1-C8
      - Result passage disposed without unit P9-S1-C8
      - Accounting without a linked unit P9-S2-C2
      - Accounting without a linked unit P9-S2-C3
      - Accounting without a linked unit P9-S2-C4
      - Result passage disposed without unit P9-S2-C6
      - Result passage disposed without unit P9-S2-C7
      - Accounting without a linked unit P9-S2-C9
      - Unaccounted source passage P9-S2-C9
      - Unaccounted source passage P9-S2-C2
      - Unaccounted source passage P9-S2-C3
      - Unaccounted source passage P9-S2-C4
      - Result passage disposed without unit P10-S1-C1
      - 'window 13: invalid/duplicate disposition P9-S2-C11'
      - Result passage disposed without unit P10-S1-C9
      - Result passage disposed without unit P11-S1-C5
      - Accounting without a linked unit P11-S2-C11
      - Accounting without a linked unit P11-S2-C14
      - Unaccounted source passage P11-S2-C14
      - Unaccounted source passage P11-S2-C11
      - Result passage disposed without unit P11-S3-C4
      - Result passage disposed without unit P12-S1-C1
      - Result passage disposed without unit P12-S1-C3
      - Result passage disposed without unit P12-S1-C4
      - Result passage disposed without unit P12-S1-C5
      - Result passage disposed without unit P12-S1-C6
      - Result passage disposed without unit P12-S1-C7
      - Result passage disposed without unit P12-S1-C8
      - Result passage disposed without unit P12-S1-C10
      - Result passage disposed without unit P12-S2-C3
      - Result passage disposed without unit P12-S2-C4
      - Result passage disposed without unit P12-S2-C5
      - Result passage disposed without unit P12-S2-C6
      - Result passage disposed without unit P12-S2-C7
      - Result passage disposed without unit P12-S2-C8
      - Result passage disposed without unit P12-S3-C16
      - Result passage disposed without unit P12-S4-C2
      - Result passage disposed without unit P13-S1-C10
      - Accounting without a linked unit P13-S1-C9
      - Accounting without a linked unit P13-S2-C4
      - Accounting without a linked unit P13-S2-C5
      - Accounting without a linked unit P13-S2-C6
      - Accounting without a linked unit P13-S3-C6
      - Accounting without a linked unit P13-S3-C7
      - Unaccounted source passage P13-S2-C4
      - Unaccounted source passage P13-S2-C5
      - Unaccounted source passage P13-S1-C9
      - Unaccounted source passage P13-S3-C7
      - Unaccounted source passage P13-S3-C6
      - Unaccounted source passage P13-S2-C6
      - Result passage disposed without unit P13-S3-C8
      - Accounting without a linked unit P14-S1-C8
      - Result passage disposed without unit P14-S2-C4
      - Unaccounted source passage P14-S1-C8
      - Result passage disposed without unit P14-S4-C7
      unattached_null_or_qualifier_ids:
      - P4-S1-C6
      - P7-S3-C2
      - P11-S1-C5
      - P12-S1-C7
      suppressed_nonrepresented_units: 21
      default_disposition_count_requires_completeness_check: 239
      unselected_timing_passages:
      - P2-S1-C9
      - P4-S1-C3
      - P7-S3-C6
      - P14-S2-C18
      - P14-S3-C11
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: validation
        source_id: P15-S1-C4
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: eligibility
        source_ids:
        - P14-S2-C12
        - P14-S2-C13
        - P14-S2-C14
        - P14-S2-C15
        - P14-S2-C16
        - P14-S2-C17
        - P14-S2-C18
        - P14-S3-C6
        - P14-S3-C7
        - P14-S3-C8
        - P14-S3-C9
        - P14-S3-C10
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - eligibility
      - validation
      - personal_factors
      - tested_personal_effects
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-6-1
      - TABLE-1-page-6-2
      unlinked_tables: []
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P3-S2
        - P3-S3
        - P4-S2
        - P4-S3
        - P4-S4
        - P5-S1
        - P6-S1
        - P7-S1
        - P7-S2
        - P7-S3
        - P8-S1
        - P8-S2
        - P9-S1
        - P9-S2
        - P9-S3
        - P10-S1
        - P11-S1
        - P11-S2
        - P12-S1
        - P12-S2
        - P13-S2
        - P13-S3
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: a0dd390561996aeeca449d85e827d3dc2d7ea0f2af2c8c6f2234ace8f68f5220
      source_review: _compare/relationships-2026-11-16/review-current/Corbetta2015
      source_status_sha256: 2096b379feb67ded892915a08230532ac0b1c5f3fa56fd9c62eca585dc93c850
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C1
      disposition: repeated
      result_indexes:
      - 13
      reason: Restatement of findings in summary
    - source_id: P1-S1-C4
      disposition: repeated
      result_indexes:
      - 13
      reason: Restatement of findings in summary
    - source_id: P2-S1-C12
      disposition: repeated
      result_indexes:
      - 5
      reason: Summary restatement of across-domain factor analysis
    - source_id: P2-S1-C13
      disposition: repeated
      result_indexes:
      - 11
      reason: Summary restatement of white matter contribution
    - source_id: P2-S1-C14
      disposition: repeated
      result_indexes:
      - 8
      reason: Summary restatement of variance explained by location
    - source_id: P4-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Demographic matching to healthy controls
    - source_id: P4-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Demographic matching to healthy controls
    - source_id: P4-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Demographic comparison to source population
    - source_id: P4-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Demographic matching to source population
    - source_id: P4-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Demographic comparison to source population
    - source_id: P4-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Clinical representativeness comparison
    - source_id: P4-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Clinical representativeness comparison
    - source_id: P4-S2-C9
      disposition: represented
      result_indexes:
      - 0
      reason: Identifies motor factors and variance
    - source_id: P4-S2-C10
      disposition: represented
      result_indexes:
      - 0
      reason: Identifies correlation between motor tests
    - source_id: P4-S2-C11
      disposition: repeated
      result_indexes:
      - 1
      reason: Restatement of language variance
    - source_id: P4-S3-C1
      disposition: represented
      result_indexes:
      - 1
      reason: Identifies language factor variance
    - source_id: P4-S3-C2
      disposition: represented
      result_indexes:
      - 1
      reason: Identifies language factor correlations
    - source_id: P4-S3-C3
      disposition: represented
      result_indexes:
      - 1
      reason: Identifies correlation between speech and comprehension
    - source_id: P4-S3-C6
      disposition: represented
      result_indexes:
      - 2
      reason: Identifies factors in aphasic patients
    - source_id: P4-S3-C7
      disposition: represented
      result_indexes:
      - 2
      reason: Conclusion on separate comprehension/production deficits
    - source_id: P4-S3-C8
      disposition: repeated
      result_indexes:
      - 2
      reason: Restatement of language correlations
    - source_id: P4-S3-C9
      disposition: repeated
      result_indexes:
      - 2
      reason: Restatement of language correlations
    - source_id: P4-S3-C10
      disposition: represented
      result_indexes:
      - 3
      reason: Identifies memory factors and variance
    - source_id: P4-S4-C2
      disposition: repeated
      result_indexes:
      - 3
      reason: Restatement of memory factor lack of separation
    - source_id: P4-S4-C3
      disposition: repeated
      result_indexes:
      - 3
      reason: Restatement of memory factor correlation
    - source_id: P4-S4-C4
      disposition: represented
      result_indexes:
      - 4
      reason: Identifies attention factors and variance
    - source_id: P4-S4-C5
      disposition: represented
      result_indexes:
      - 4
      reason: Identifies visual field bias factor
    - source_id: P6-S1-C1
      disposition: represented
      result_indexes:
      - 4
      reason: Qualifies visual field bias factor
    - source_id: P6-S1-C2
      disposition: represented
      result_indexes:
      - 4
      reason: Identifies sustained attention factor
    - source_id: P6-S1-C3
      disposition: represented
      result_indexes:
      - 4
      reason: Identifies attention shifting factor
    - source_id: P6-S1-C5
      disposition: represented
      result_indexes:
      - 6
      reason: Lateralization of language and spatial attention
    - source_id: P6-S1-C6
      disposition: represented
      result_indexes:
      - 6
      reason: Lateralization of motor deficits
    - source_id: P6-S1-C7
      disposition: represented
      result_indexes:
      - 6
      reason: Lateralization of memory and attention
    - source_id: P6-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: General summary of within-domain analysis
    - source_id: P6-S1-C12
      disposition: represented
      result_indexes:
      - 5
      reason: Identifies uber-factors variance
    - source_id: P6-S1-C13
      disposition: represented
      result_indexes:
      - 5
      reason: Identifies components of uber-factor 1
    - source_id: P6-S1-C14
      disposition: represented
      result_indexes:
      - 5
      reason: Identifies components of uber-factor 2
    - source_id: P6-S1-C15
      disposition: represented
      result_indexes:
      - 5
      reason: Identifies components of uber-factor 3
    - source_id: P6-S1-C12
      disposition: represented
      result_indexes:
      - 5
      reason: Identifies uber-factors variance
    - source_id: P7-S1-C2
      disposition: represented
      result_indexes:
      - 6
      reason: Lateralization of uber-factors
    - source_id: P7-S1-C6
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of within-domain correlation
    - source_id: P7-S1-C7
      disposition: repeated
      result_indexes:
      - 4
      reason: Restatement of attention correlations
    - source_id: P7-S1-C8
      disposition: repeated
      result_indexes:
      - 4
      reason: Restatement of general performance factor
    - source_id: P7-S1-C9
      disposition: repeated
      result_indexes:
      - 4
      reason: Restatement of sustained attention necessity
    - source_id: P7-S1-C10
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of walking correlation
    - source_id: P7-S1-C11
      disposition: repeated
      result_indexes:
      - 5
      reason: Restatement of uber-factor 1 correlation
    - source_id: P7-S1-C12
      disposition: repeated
      result_indexes:
      - 5
      reason: Restatement of uber-factors 2 and 3
    - source_id: P7-S2-C2
      disposition: repeated
      result_indexes:
      - 5
      reason: Restatement of uber-factors 2 and 3
    - source_id: P7-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Methodological statement about PCA on raw scores
    - source_id: P7-S2-C4
      disposition: repeated
      result_indexes:
      - 5
      reason: Restatement of three main factors
    - source_id: P7-S2-C5
      disposition: repeated
      result_indexes:
      - 5
      reason: Restatement of factor 1 components
    - source_id: P7-S2-C6
      disposition: repeated
      result_indexes:
      - 5
      reason: Restatement of factor 2 components
    - source_id: P7-S2-C7
      disposition: repeated
      result_indexes:
      - 5
      reason: Restatement of factor 3 components
    - source_id: P7-S2-C8
      disposition: repeated
      result_indexes:
      - 5
      reason: Summary of three main axes of impairment
    - source_id: P7-S2-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive of lesion localization
    - source_id: P7-S2-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive of cortical lesion distribution
    - source_id: P7-S3-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive of lesion classification percentages
    - source_id: P7-S3-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive of average lesion volume
    - source_id: P8-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Introductory statement to results
    - source_id: P8-S1-C9
      disposition: represented
      result_indexes:
      - 7
      reason: Lesion volume variance < 20%
    - source_id: P8-S1-C10
      disposition: represented
      result_indexes:
      - 8
      reason: Variance explained by location for different factors
    - source_id: P8-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: General observation on distributed damage
    - source_id: P8-S1-C12
      disposition: represented
      result_indexes:
      - 9
      reason: Anatomical association for motor deficits
    - source_id: P8-S1-C13
      disposition: represented
      result_indexes:
      - 9
      reason: Anatomical association for language deficits
    - source_id: P8-S1-C14
      disposition: represented
      result_indexes:
      - 9
      reason: White matter involvement in language deficits
    - source_id: P8-S2-C3
      disposition: represented
      result_indexes:
      - 9
      reason: Anatomical association for visuospatial biases
    - source_id: P8-S2-C4
      disposition: represented
      result_indexes:
      - 9
      reason: Anatomical association for memory deficits
    - source_id: P9-S1-C1
      disposition: represented
      result_indexes:
      - 9
      reason: Anatomical association for spatial memory
    - source_id: P9-S1-C6
      disposition: represented
      result_indexes:
      - 10
      reason: Regions associated with multiple domain deficits
    - source_id: P9-S2-C4
      disposition: represented
      result_indexes:
      - 11
      reason: Regression between domains affected and tracts damaged
    - source_id: P9-S3-C3
      disposition: repeated
      result_indexes:
      - 12
      reason: Restatement of lesion volume control
    - source_id: P9-S3-C6
      disposition: represented
      result_indexes:
      - 12
      reason: Correlation structure unchanged after volume regression
    - source_id: P9-S3-C7
      disposition: represented
      result_indexes:
      - 12
      reason: Conclusion that volume did not contribute to clusters
    - source_id: P10-S1-C1
      disposition: represented
      result_indexes:
      - 13
      reason: Similar correlation structure for subcortical/cortical groups
    - source_id: P10-S1-C5
      disposition: represented
      result_indexes:
      - 13
      reason: Conclusion that matrices are not different
    - source_id: P11-S2-C11
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of within-domain correlation
    - source_id: P11-S3-C1
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of motor factor variance
    - source_id: P12-S1-C4
      disposition: repeated
      result_indexes:
      - 1
      reason: Restatement of language factor variance
    - source_id: P12-S3-C1
      disposition: repeated
      result_indexes:
      - 5
      reason: Restatement of behavioral clusters
    - source_id: P12-S3-C5
      disposition: represented
      result_indexes:
      - 12
      reason: Restatement of lesion volume control
    - source_id: P12-S3-C6
      disposition: represented
      result_indexes:
      - 12
      reason: Restatement of volume effect on variance
    - source_id: P13-S1-C9
      disposition: represented
      result_indexes:
      - 7
      reason: Restatement of lesion volume variance < 20%
    - source_id: P13-S1-C10
      disposition: represented
      result_indexes:
      - 8
      reason: Restatement of variance explained by location
    - source_id: P13-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Theoretical explanation of cognitive function distribution
    unresolved_coverage:
    - source_id: P6-S1-C12
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P7-S1-C12
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P9-S3-C3
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P11-S3-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P12-S3-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P13-S2-C2
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P7-S3-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P7-S3-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S1-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S1-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S2-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S2-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S2-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S2-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S2-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S2-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S3-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S3-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S1-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S1-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S1-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C13
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S2-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S2-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S2-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S2-C14
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S3-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S1-C1
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S1-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S1-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S1-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S1-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S1-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S1-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S1-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S2-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S2-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S2-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S2-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S2-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S2-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S2-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S2-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S2-C12
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S2-C13
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S3-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S3-C16
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S4-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S2-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S2-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S2-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S3-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S3-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S3-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P14-S1-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P14-S1-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P14-S2-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P14-S4-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P15-S1-C1
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C1
    - P1-S1-C4
    - P2-S1-C12
    - P2-S1-C13
    - P2-S1-C14
    - P4-S1-C6
    - P4-S1-C7
    - P4-S1-C8
    - P4-S1-C9
    - P4-S1-C10
    - P4-S1-C11
    - P4-S2-C2
    - P4-S2-C11
    - P4-S3-C3
    - P4-S3-C8
    - P4-S3-C9
    - P4-S4-C2
    - P4-S4-C3
    - P6-S1-C1
    - P6-S1-C7
    - P6-S1-C8
    - P7-S1-C6
    - P7-S1-C7
    - P7-S1-C8
    - P7-S1-C9
    - P7-S1-C10
    - P7-S1-C11
    - P7-S2-C2
    - P7-S2-C3
    - P7-S2-C4
    - P7-S2-C5
    - P7-S2-C6
    - P7-S2-C7
    - P7-S2-C8
    - P7-S2-C12
    - P7-S2-C13
    - P7-S3-C2
    - P7-S3-C3
    - P7-S3-C4
    - P7-S3-C5
    - P8-S1-C8
    - P8-S1-C11
    - P8-S1-C14
    - P9-S1-C7
    - P9-S1-C8
    - P9-S2-C2
    - P9-S2-C3
    - P9-S2-C6
    - P9-S2-C7
    - P9-S2-C8
    - P9-S2-C9
    - P9-S3-C5
    - P9-S3-C8
    - P10-S1-C2
    - P10-S1-C4
    - P10-S1-C9
    - P11-S1-C5
    - P11-S1-C13
    - P11-S2-C6
    - P11-S2-C8
    - P11-S2-C9
    - P11-S2-C11
    - P11-S2-C14
    - P11-S3-C4
    - P12-S1-C1
    - P12-S1-C3
    - P12-S1-C4
    - P12-S1-C5
    - P12-S1-C6
    - P12-S1-C7
    - P12-S1-C8
    - P12-S1-C9
    - P12-S1-C10
    - P12-S2-C3
    - P12-S2-C4
    - P12-S2-C5
    - P12-S2-C6
    - P12-S2-C7
    - P12-S2-C8
    - P12-S2-C9
    - P12-S2-C10
    - P12-S2-C12
    - P12-S2-C13
    - P12-S3-C11
    - P12-S3-C16
    - P12-S4-C2
    - P13-S2-C4
    - P13-S2-C5
    - P13-S2-C6
    - P13-S3-C6
    - P13-S3-C7
    - P13-S3-C8
    - P14-S1-C8
    - P14-S1-C10
    - P14-S2-C4
    - P14-S4-C7
    - P15-S1-C1
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-6-1
    - TABLE-1-page-6-2
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P4-S1-C3
      recruited_sample:
      - P2-S1-C9
      - P3-S2-C10
      eligibility: []
      imaging_provenance:
      - P2-S1-C10
      - P14-S3-C14
      - P15-S1-C14
      - P15-S1-C15
      imaging_timing:
      - P3-S2-C11
      - P3-S3-C2
      outcome_timing:
      - P3-S2-C11
      outcome_definition:
      - P15-S1-C11
      validation: []
      analysis_restrictions:
      - P9-S2-C5
      dependent_variable_statement:
      - P7-S3-C9
      - P13-S1-C7
      - P15-S1-C11
      limitations:
      - P14-S1-C2
      - P14-S1-C5
      - P14-S1-C6
      - P14-S1-C7
      - P14-S1-C10
      - P14-S1-C11
      - P14-S1-C12
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P9-S2-C13
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P4-S1-C6
      - P4-S1-C8
      - P4-S1-C10
      - P11-S1-C6
      - P11-S2-C8
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: internal_cross_validation
    held_selections:
    - slot: validation
      source_id: P15-S1-C4
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: eligibility
      source_ids:
      - P14-S2-C12
      - P14-S2-C13
      - P14-S2-C14
      - P14-S2-C15
      - P14-S2-C16
      - P14-S2-C17
      - P14-S2-C18
      - P14-S3-C6
      - P14-S3-C7
      - P14-S3-C8
      - P14-S3-C9
      - P14-S3-C10
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
      pdf_sha256: a0dd390561996aeeca449d85e827d3dc2d7ea0f2af2c8c6f2234ace8f68f5220
      review_sha256: 9c574d7b8509dff745747042828cbe11b405a1a6132cb876077c0eed0c344e75
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
      - P4-S3-C10
      source_result: 'In the memory domain (n=98), a within-domain PCA with oblique
        rotation identified two factors explaining 66% of the variance: one for visuospatial
        memory and one for verbal memory. These factors were correlated and did not
        differentiate the side of the lesion.'
      result_status: detected
      patient_measurement: non_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis is the Within-Domain Factor Analysis for the
            memory domain, as described in P4-S3-C10. The proposed core correctly
            identifies this as a PCA on behavioral scores, not a lesion-behavior mapping
            or tractography analysis.
          source_ids:
          - P4-S3-C10
          - P4-S2-C7
          - P14-S4-C3
        direction:
          answer: fits
          reason: The source reports the detection of two distinct factors (visuospatial
            and verbal) that explain variance. The proposed core accurately reflects
            this 'detected' structure. The 'likely' direction in the proposed core
            is acceptable for a descriptive factor analysis result, though 'detected'
            is more precise for the status.
          source_ids:
          - P4-S3-C10
        construct:
          answer: fits
          reason: The exposure is 'stroke' (population), and the outcome is 'visuospatial
            and verbal memory' factors. The measurement is behavioral (non_imaging),
            as the PCA is performed on test scores, not imaging data. The proposed
            core correctly identifies the method as behavioral_only.
          source_ids:
          - P4-S3-C10
          - P3-S3-C7
          - P14-S4-C3
        qualifications:
          answer: fits
          reason: The proposed core includes the qualifications that the factors were
            correlated and did not differentiate lesion side, which are explicitly
            stated in P4-S3-C10 and P4-S4-C3. It also notes the sample size (n=98).
          source_ids:
          - P4-S3-C10
          - P4-S4-C3
        missing_material_caveat:
          answer: fits
          reason: No material caveats are missing. The core correctly limits the claim
            to the memory domain and the specific sample size. The timing is flagged
            as pending, which is appropriate given the source window's focus on acute
            assessment but lack of explicit timing in the specific evidence ID.
          source_ids:
          - P4-S3-C10
          - P3-S3-C2
      optional_pending:
      - 'sample.time_post_onset: source confirmation required; original proposed wording
        remains in the audit.'
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
    - 'sample.time_post_onset: source confirmation required; original proposed wording
      remains in the audit.'
    normalizations:
    - field: bucket
      original: impairments
      action: route_from_kind
      value: regions
    - field: sample.time_post_onset
      original: acute neurobehavioral assessment (mean 13 ± 4.9 days post-stroke)
      action: not_transcribed
      reason: 'Numbers not grounded in usable selected source readings: 13, 4.9'
    analysis_identity:
      id: R004
      exposure:
        text: stroke
      outcome:
        text: visuospatial and verbal memory
      analysis_label: Within-Domain Factor Analysis (Memory)
      relation: association
      evidence_ids:
      - P4-S3-C10
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
        pdf_sha256: a0dd390561996aeeca449d85e827d3dc2d7ea0f2af2c8c6f2234ace8f68f5220
        source_review: _compare/relationships-2026-11-16/review-current/Corbetta2015
        source_status_sha256: 2096b379feb67ded892915a08230532ac0b1c5f3fa56fd9c62eca585dc93c850
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P3-S2-C10:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: a0dd390561996aeeca449d85e827d3dc2d7ea0f2af2c8c6f2234ace8f68f5220
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: ab8a46deeb4fec1000c1edeac7a0e53d291d43d31b76738c2992f3f49b29d3d5
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S2-C10
          page: 3
          text_layer_sha256: ab8a46deeb4fec1000c1edeac7a0e53d291d43d31b76738c2992f3f49b29d3d5
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'RESULTS

          Subjects (n = 172) with a ﬁrst symptomatic stroke, ischemic or

          hemorrhagic, anywhere in the brain and clinical evidence of

          any neurological impairment were prospectively recruited, with

          n = 132 meeting post-enrollment inclusion criteria (see Experi-

          mental Procedures and Supplemental Information for details

          about subjects, Figure S1 for enrollment ﬂowchart).'
        anchor_text: 'RESULTS

          Subjects (n = 172) with a ﬁrst symptomatic stroke, ischemic or

          hemorrhagic, anywhere in the brain and clinical evidence of

          any neurological impairment were prospectively recruited, with

          n = 132 meeting post-enrollment inclusion criteria (see Experi-

          mental Procedures and Supplemental Information for details

          about subjects, Figure S1 for enrollment ﬂowchart).'
        excluded_fragments: []
        image_sha256: bac9964b4641e48398666a85b13d40fa67077d731cade921e18aba276608dc48
        transcription: 'RESULTS


          Subjects (n = 172) with a first symptomatic stroke, ischemic or hemorrhagic,
          anywhere in the brain and clinical evidence of any neurological impairment
          were prospectively recruited, with n = 132 meeting post-enrollment inclusion
          criteria (see Experimental Procedures and Supplemental Information for details
          about subjects, Figure S1 for enrollment flowchart)'
      P3-S3-C2:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: a0dd390561996aeeca449d85e827d3dc2d7ea0f2af2c8c6f2234ace8f68f5220
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: ece1f4b40d9acfca583958e79ceebf421d2d34d97a4bd40cbcbcda6d7393f28f
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S3-C2
          page: 3
          text_layer_sha256: ece1f4b40d9acfca583958e79ceebf421d2d34d97a4bd40cbcbcda6d7393f28f
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: 'This report concen-

          trates on the acute neurobehavioral assessment (mean 13 ±

          4.9 days) and structural MRI studies (Figure 1 for experimental

          design).'
        anchor_text: 'This report concen-

          trates on the acute neurobehavioral assessment (mean 13 ±

          4.9 days) and structural MRI studies (Figure 1 for experimental

          design).'
        excluded_fragments: []
        image_sha256: 3c166cfd7f6b61e5135e32954de303bfa90140ce7cd369e6c02006fcd378a8b8
      P14-S2-C15:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: a0dd390561996aeeca449d85e827d3dc2d7ea0f2af2c8c6f2234ace8f68f5220
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: e4659583a415f0c5109caac12f966b9b1a68c7279be7b793a6ced0ae70aef75e
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P14-S2-C15
          page: 14
          text_layer_sha256: e4659583a415f0c5109caac12f966b9b1a68c7279be7b793a6ced0ae70aef75e
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: '(2) First symp-

          tomatic stroke, ischemic or hemorrhagic.'
        anchor_text: '(2) First symp-

          tomatic stroke, ischemic or hemorrhagic.'
        excluded_fragments: []
        image_sha256: 1d238b307f7658d40d4bc798038e35b2627b37b7f7c0ce5aec6d1e0cfddc1002
        transcription: . (2) First symptomatic stroke, ischemic or hemorrhagic
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 4
  quote: 'In the memory domain (n = 98), two factors explained 66% of

    the variance: visuospatial memory loaded on one factor with cor-

    relations among tasks between r = 0.68 and 0.80 (Figure 2G), and

    verbal memory loaded on a different factor with correlations

    among tasks between r = 0.74 and 0.93 (Figure 2H).'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-23'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
