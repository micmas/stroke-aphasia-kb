---
id: phonological_vs_semantic_retrieval_segregation
name: phonological and semantic retrieval segregation cluster
kind: network
findings:
- id: f1
  target: phonological_vs_semantic_retrieval_operations
  target_kind: impairment
  claim: There was no spatial overlap between the voxels associated with phonological
    errors and those associated with semantic errors in object naming, demonstrating
    that the brain segregates these retrieval operations in word production.
  direction: no_effect
  relationship: correlational
  method: VLSM
  sample:
    n: 106
    population: individuals with diverse profiles of aphasia secondary to stroke
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
  - poor lesion coverage in the posterior inferior temporal gyrus/fusiform area may
    have limited power to detect effects there
  - lesion characterization likely underestimates the extent of functional tissue
    damage
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Comparison of voxel-based lesion-symptom mapping (VLSM)
    maps for phonological naming errors (non-word errors) and semantic naming errors
    (real-word responses semantically related to the target) in object naming. phonological
    errors were defined as all non-word errors regardless of phonemic overlap with
    the target; semantic errors were defined as real word responses semantically related
    to the target; overlap analysis used a lenient FDR threshold of q = 0.05. Additional
    metadata has not been transcribed; review the pending-field flags before approval.
    PDF image reading (P3-S3-C2, two-model agreement, human verification pending):
    . Of the 142 individuals enrolled, 106 qualified for the

    current study Original text-layer quotation is preserved below.'
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
    - not_transcribed:sample.time_post_onset
    - proposed_concept:phonological_vs_semantic_retrieval_operations
  citation: '@Schwartz2012'
  source_passages:
  - section: Original source P1-S1-C10
    page: 1
    quote: 'In a separate analysis, we compared the lesion maps for phonological and
      semantic errors and determined that

      there was no spatial overlap, demonstrating that the brain segregates phonological
      and semantic retrieval operations in word

      production.'
    supports: claim
  - section: Original source P11-S1-C3
    page: 11
    quote: 'No voxels were associated with both semantic errors and

      phonological errors, i.e. the overlap was zero.'
    supports: claim
  - section: Original source P11-S2-C5
    page: 11
    quote: 'Phonological errors voxels and semantic errors voxels did not over-

      lap, despite the fact that both are manifestations of impairment by

      the same participants on the same task.'
    supports: claim
  - section: Original source P11-S2-C10
    page: 11
    quote: No voxels were signiﬁcant in both analyses.
    supports: claim
  - section: Original source P3-S3-C1
    page: 3
    quote: 'The inclusion criteria were as follows: at least 1 month post-onset of

      aphasia secondary to stroke, living at home, medically stable without

      major psychiatric or neurological co-morbidities, premorbid right hand-

      edness, English as primary language, adequate vision and hearing

      (with or without correction) and CT or MRI conﬁrmed left hemisphere

      cortical lesion.'
    supports: sample
  - section: Original source P3-S3-C2
    page: 3
    quote: 'Of the 142 individuals enrolled, 106 qualiﬁed for the

      current study.'
    supports: sample
  - section: Original source P4-S2-C11
    page: 4
    quote: 'In short, the analysis of phonological errors involved all and only

      Philadelphia Naming Test non-word errors.'
    supports: method
  - section: Original source P4-S3-C3
    page: 4
    quote: 'These are real word responses that are semantically,

      and not phonologically, related to the target.'
    supports: method
  - section: Original source P5-S2-C11
    page: 5
    quote: 'For analyses

      with one dependent variable (e.g. phonological errors) and one inde-

      pendent variable (lesion status), a t-test was performed at each voxel

      comparing scores on the dependent variable between patients with

      and without lesions in that voxel.'
    supports: method
  - section: Original source P6-S3-C14
    page: 6
    quote: 'The overlap analyses used a more lenient FDR threshold

      (q = 0.05) to avoid underestimating overlap.'
    supports: method
  - section: Original source P14-S1-C1
    page: 14
    quote: '

      The characterization of the lesions in this study likely underes-

      timates the extent of functional tissue damage.'
    supports: limitation
  - section: Original source P11-S2-C3
    page: 11
    quote: 'However, owing to the poor lesion

      coverage in the posterior inferior temporal gyrus/fusiform area,

      there was not sufﬁcient power to detect effects there.'
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-25'
relationship_review:
  paper: Schwartz2012
  proposal_id: R003
  review_status_sha256: fe3f6b3213144baf063144c24d628a2d2bbff829e01ad23f846dfc458380b042
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: eef25a7d563cba481de7f96cc58b9bab94911cf24c78f703022dd4cbcbd0f8ea
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: eef25a7d563cba481de7f96cc58b9bab94911cf24c78f703022dd4cbcbd0f8ea
        A/passages.json: 918dcc2fdad8099fe36b680b8006653b2fa673ae422938d81847d2a90b429ac3
        A/raw.json: 3e71e58317dbbe7b6d2419701f90c4a1c970a0e7e2a8f43ce81484009032ece3
        A/source-units.json: cbe10a587c92ef5a55029762716a0f1da9dba5ef16f3c8f25b8f56224f95f2b9
        A/full-source-units.json: abfb52c545442ca61d8c6bff526bd871c278179293412ab9e2b455ed6d84a2d8
        A/meta.json: dbc5ce8b4e286bc869d4a9d6da5c49fa561292fd5d2d596240698a7b22ad37f7
        A/table-images/TABLE-1-page-3-1.png: 74ee041f4b7aad555af62ed4e43c13484bd0ea7f2ec5baf20ada4cda064f55f8
        A/table-images/page-3.png: eb89bed24ae950e94d80cebad65d4ee81ef9ce6ceb0dc4d22d10f83d48dd55c3
        A/table-images/page-7.png: 627af055edcb6d3b8952ed5a8eff678ebb2b902d035b13ce2300ef5298a43da3
        A/table-images/manifest.json: 434227f41b50d9e0fef6cad3b2add4001406e6bc81415a4a4457d12b6e9539a9
        A/table-images/TABLE-2-page-7-1.png: 8377847181eb4edfebb0a6fa8e323d4bf52ad708fff94670863d4ee7f7426f94
        A/clauses/window-11/raw.json: 3950aa49e42345f16dbe2c8a404bb60ef71c70739549475c0b46a9fed02ce6fc
        A/clauses/window-11/prompt.txt: 859920adac210bb1bf15faa9d76ee9df83e1d018bf9219ca1f862f37358a99b3
        A/clauses/window-11/meta.json: a919ed7bf314a0e1f4fd8153e0b6c42631235b38ebb144d076488310d9ae0c3d
        A/clauses/window-10/raw.json: 10d0165b43c8ca355f38a9704b023ad9b1e25f768bc9789a88eca633c9d6300d
        A/clauses/window-10/prompt.txt: b2138acabcfeea600ff9b43abbd8835babbd024bfe6d5ef05bcade04fc593716
        A/clauses/window-10/meta.json: b8f6702062ea793762a58ea85b8939bd04c118846d92579467b511229f041b45
        A/clauses/window-03/raw.json: d202e77210e80b2bd396d67b3c2d6eb265f9b8af11b3a37861a2664298438bae
        A/clauses/window-03/prompt.txt: 03b898c94597f44eddd5a92d7e1b1ff9f27d01468aeecbea6afecffb5bbfdb5c
        A/clauses/window-03/meta.json: af23bb13d4ce8ac2583d6a92609102d52e0edf66c4d2a807e516675c2490b9b4
        A/clauses/window-04/raw.json: d2f05d870eca5ebbe542d46b1d8699d3c543eb3ba00d79635eab5b0496e73e1b
        A/clauses/window-04/prompt.txt: 8f61e92c90e8c4a2d80aae4a05e1db324ea9c943a1a722dae6518ffe596418b2
        A/clauses/window-04/meta.json: 22ed2ca5b6a83f63116f70af22773f0aaee9d2c071af3b1734ece4f6167d921a
        A/clauses/window-05/raw.json: 115e78c6eabfcf94b1aed70e65b393595dc14d35a83f95a8f1039efd42a81bc3
        A/clauses/window-05/prompt.txt: 0b2dd07351752d5a25fa00d76a08835a00101829a31a4eb232606cde5d6397c7
        A/clauses/window-05/meta.json: d1f7b9f74c77d18e6ee55feeac2c6391717a8ed789df308624d7df34d2c9e0cf
        A/clauses/window-02/raw.json: 0fb12b89e99cf8ff2cd5a1d884ee67893d108f90ba47347a9f81bd9e6fac4bd4
        A/clauses/window-02/prompt.txt: 0ac56bee15842d545675f451c7461987f4714e65528fc7ef1ba3b483b12947d5
        A/clauses/window-02/meta.json: 39ec5b931dd646df4345e4d59af1ca18dce679935019a040bbc985e443045496
        A/clauses/window-12/raw.json: fb20bc6c33bc64cace86caeda2024a39f7a59c6a5bd704fdfde802f7061d9a79
        A/clauses/window-12/prompt.txt: 6747db9b8c5aaad88e7f6da93bbf79bae24e5ff2224b7237f01d030d9793eec2
        A/clauses/window-12/meta.json: 94de0f50168af00dcef415d5330eaba81585a264f36234a92f6a5073b2502836
        A/clauses/window-09/raw.json: 310978e277fa24d7b3a2d583e7e022d4b88012b623f526bfe2380c8c8a2cf4e1
        A/clauses/window-09/prompt.txt: 0c444277a58814c608579b8099bdac21367e5e86c7872d843558895fdc0ab885
        A/clauses/window-09/meta.json: c120087542175ef759db198585d924252283c2c2934bdac4f64147da8b724195
        A/clauses/window-07/raw.json: 3ce7dcdde28c8d63953612056aaff0fc7022e3e8295e032de5ca267967aa8f6a
        A/clauses/window-07/prompt.txt: 84c70d4fdf53c85626b7fba72fa1766b6e6690631007ba47815a49bb7edd3453
        A/clauses/window-07/meta.json: 48e51fd2c7f3af68da8db23dbe19ddb78fa73d0f5c6b9de3270a89889814b036
        A/clauses/window-01/raw.json: 4087ba785fc514238b2c335d9c355d4da05ee4e6603bf84ec149a09fcbcf1f7b
        A/clauses/window-01/prompt.txt: e0578f2760de4278e7ecf2f3b985d98633f26435c0c5a5b82dd37c6e3fc030f5
        A/clauses/window-01/meta.json: 074ba2434d769679ae4745bdf4afd8f5d9e1145c4acb1b8d308242e53b4c5e45
        A/clauses/window-06/raw.json: 9bef8368d4d3f641b295d1a3e8a38bf3535303ab07770e8246f99a9d5c266e64
        A/clauses/window-06/prompt.txt: e892f7259d4abc8e8fd40647a603cf54b515b3734ab07a8252d46c4ce7dde316
        A/clauses/window-06/meta.json: e0c353918efb7aed74e18cb321eeea6400dda51b6e92a9615af677f91a8efb69
        A/clauses/window-08/raw.json: 0a07261aa2a3a6e3454e2048d0f2e9724d99e3dd78c0f4e034e32a5168f0db48
        A/clauses/window-08/prompt.txt: 236bb177832365d430910565ecc0a21c8178a2cb965e66036c0d3c903bf27471
        A/clauses/window-08/meta.json: de94cba8721d7255b8f436927f49576182979942961aeea0fb768c4417a93c44
        A/tables/TABLE-1-page-3-1/raw.json: fe73081f46df27d56dc5a906af4648e9632bb1dbb91622de27305db151f61e48
        A/tables/TABLE-1-page-3-1/prompt.txt: 8a53c82d3c3ef72dd0e99cf5509d083e511f6893535ae2ff72368f76f3c29189
        A/tables/TABLE-1-page-3-1/meta.json: bb5d8f6af6a09f6e7696c493ffc5f61d5791bec043ee4085e2f65ca55418f6c6
        A/tables/TABLE-2-page-7-2/raw.json: 2f14fdcbab8a0ce6fc550f64fa76177002bb0aee93058df0ac754a38299aa4a9
        A/tables/TABLE-2-page-7-2/prompt.txt: 66c380f547d817f3d0f17c34e856118aba17fdd3aa0c6292fce2372898a3c6e0
        A/tables/TABLE-2-page-7-2/meta.json: b93ff4af4c7e89f79685bdbf3aebe50f971a95138a7becce99d214ec8c2f6825
        B/passages.json: 918dcc2fdad8099fe36b680b8006653b2fa673ae422938d81847d2a90b429ac3
        B/raw.json: eca5963cfa7ee48f9120b090b06b249b3ae35f382a5c399bd6e8af525cc2a97a
        B/source-units.json: cbe10a587c92ef5a55029762716a0f1da9dba5ef16f3c8f25b8f56224f95f2b9
        B/full-source-units.json: abfb52c545442ca61d8c6bff526bd871c278179293412ab9e2b455ed6d84a2d8
        B/meta.json: d52bed8d3f947d83a256229fbe0ccd22d153b0ce61596bf0fad01fb82b8c9267
        B/table-images/TABLE-1-page-3-1.png: 74ee041f4b7aad555af62ed4e43c13484bd0ea7f2ec5baf20ada4cda064f55f8
        B/table-images/page-3.png: eb89bed24ae950e94d80cebad65d4ee81ef9ce6ceb0dc4d22d10f83d48dd55c3
        B/table-images/page-7.png: 627af055edcb6d3b8952ed5a8eff678ebb2b902d035b13ce2300ef5298a43da3
        B/table-images/manifest.json: 600456b8eef32acb668fc000089ecaa4cb40f41f53b041a6f483b948e7b26312
        B/table-images/TABLE-2-page-7-1.png: 8377847181eb4edfebb0a6fa8e323d4bf52ad708fff94670863d4ee7f7426f94
        B/clauses/window-11/raw.json: bf7675bbe89ef06c4d6102ea0f0c453f9897e497210829eb8b6c9d146f67be41
        B/clauses/window-11/prompt.txt: 859920adac210bb1bf15faa9d76ee9df83e1d018bf9219ca1f862f37358a99b3
        B/clauses/window-11/meta.json: 34e3fdbdfb671560944f6982aca8b96b58a99836a028a5c9136d08643d1bf6e7
        B/clauses/window-10/raw.json: 205a105f10f5acd7a7e93299af62a03714cdc5b45985279cc94f8452cba386af
        B/clauses/window-10/prompt.txt: b2138acabcfeea600ff9b43abbd8835babbd024bfe6d5ef05bcade04fc593716
        B/clauses/window-10/meta.json: 7592439d59959d154f94258ed6a7ffa1d9639352ef8e9797a99bc0e8d2f48c78
        B/clauses/window-03/raw.json: 54c5e164eb47ef8271261b091056472e8b0d47a1497f2df77571e12723718faa
        B/clauses/window-03/prompt.txt: 03b898c94597f44eddd5a92d7e1b1ff9f27d01468aeecbea6afecffb5bbfdb5c
        B/clauses/window-03/meta.json: a886cb198b770deda0c65254cc6dbb73fb7f8a4b34ce3278bf2c859e0cbff8d9
        B/clauses/window-04/raw.json: a590ee0c4a736c012b1976c9a2d937b1f9cb1e6154b6412e67dc0d2a9ac1fffa
        B/clauses/window-04/prompt.txt: 8f61e92c90e8c4a2d80aae4a05e1db324ea9c943a1a722dae6518ffe596418b2
        B/clauses/window-04/meta.json: aaa4ba01f86e12a7554de1b992eb9c172dd032a2b18786df62a8bb69d6e7e5cb
        B/clauses/window-05/raw.json: 8d557bb593228efbf88abba6f45e0954c7b7559f0a0b25a30406cd08d296549b
        B/clauses/window-05/prompt.txt: 0b2dd07351752d5a25fa00d76a08835a00101829a31a4eb232606cde5d6397c7
        B/clauses/window-05/meta.json: 7360f70e166603203066d5e1af829ae61d838ef53372e8cb1cbaec975772ac32
        B/clauses/window-02/raw.json: 23d6b482b421700efd2ad96903e36e4c87f125757d0dcc4f503345ca3120f554
        B/clauses/window-02/prompt.txt: 0ac56bee15842d545675f451c7461987f4714e65528fc7ef1ba3b483b12947d5
        B/clauses/window-02/meta.json: b8dbf641cdc2a7ff5fb7ba2ff9b25f88988563237d87e8aa24f4f3f7a405a4df
        B/clauses/window-12/raw.json: e8832504ac1c18a65fbc89b49f700db4eb5101cb8e0cb14448f29cf78d4656d9
        B/clauses/window-12/prompt.txt: 6747db9b8c5aaad88e7f6da93bbf79bae24e5ff2224b7237f01d030d9793eec2
        B/clauses/window-12/meta.json: 0f4e08312a73eaf3f7101c87824f05ebad37d6c7bbe73adb5938004be51b85ee
        B/clauses/window-09/raw.json: 8ca24a9b91c9dc5578815070b3cb94cda1eaf22284b0d66b7471df066b9dcd9d
        B/clauses/window-09/prompt.txt: 0c444277a58814c608579b8099bdac21367e5e86c7872d843558895fdc0ab885
        B/clauses/window-09/meta.json: 5d189d22c5848689f2549c7355b19ad2305aa15288cbde6cf01e0bf5e24f7208
        B/clauses/window-07/raw.json: 83a40c995b831656138af8ae72b90431b00418cb0d0b43c9b75fbaa27a50d23f
        B/clauses/window-07/prompt.txt: 84c70d4fdf53c85626b7fba72fa1766b6e6690631007ba47815a49bb7edd3453
        B/clauses/window-07/meta.json: 99c0a46780f0b21762175b7552827d8e978e53678e6198cc40f1f3a76361694d
        B/clauses/window-01/raw.json: e72aeb6df0a2f1939960c618aafe231cef62f11b4021cdce6bb96c90427aa549
        B/clauses/window-01/prompt.txt: e0578f2760de4278e7ecf2f3b985d98633f26435c0c5a5b82dd37c6e3fc030f5
        B/clauses/window-01/meta.json: 2fd9e5cf2b958e17ba4f709587f37a85766d20ee2b1a6bc39c9dc44ed2ccdfd1
        B/clauses/window-06/raw.json: e019983e39e4cfa30f8c55620453d1d231df2ce96a60e3a6f14bf4d0d79f4bb1
        B/clauses/window-06/prompt.txt: e892f7259d4abc8e8fd40647a603cf54b515b3734ab07a8252d46c4ce7dde316
        B/clauses/window-06/meta.json: ffe001febdb0110ea4aec3f6251d40a0954eff5fe41eb168095efd7d61d63552
        B/clauses/window-08/raw.json: 4efc247cc1fee240800aceb94adce72f11c360b3ec302d5e92d734da9a4a52bf
        B/clauses/window-08/prompt.txt: 236bb177832365d430910565ecc0a21c8178a2cb965e66036c0d3c903bf27471
        B/clauses/window-08/meta.json: d6cadc0522437271bb0f769b0f3302d783f5106fd8aa5c324797fdf3dfcf4808
        B/tables/TABLE-1-page-3-1/raw.json: 503935a7e1cff62bb7f0100ca9d090df9b991e9c6d019b0e21b4aface18a1910
        B/tables/TABLE-1-page-3-1/prompt.txt: 8a53c82d3c3ef72dd0e99cf5509d083e511f6893535ae2ff72368f76f3c29189
        B/tables/TABLE-1-page-3-1/meta.json: 7fcd171cbe0f3dc0ca96e3d18b2288ac6414d36c62af0220f13923c42ce7c4b0
        B/tables/TABLE-2-page-7-2/raw.json: 83b41671a4eb2b9148fd5580fc20be29457a3a11fd2fa5af93e46f49b50b5e5b
        B/tables/TABLE-2-page-7-2/prompt.txt: 66c380f547d817f3d0f17c34e856118aba17fdd3aa0c6292fce2372898a3c6e0
        B/tables/TABLE-2-page-7-2/meta.json: 0cc6f8d2e9f3be65ad1c1f081dc4e407adadf8108c68655cf55a79cae3e8c145
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
      pdf_sha256: eef25a7d563cba481de7f96cc58b9bab94911cf24c78f703022dd4cbcbd0f8ea
      source_review: _compare/relationships-2026-11-16/review-current/Schwartz2012
      source_status_sha256: 08d95cd15ffb07482f2b21a8bf34f1e44e8d0686e4ad7f157f10b2b03aad3a68
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R003
    exposure:
      text: lesion location
    outcome:
      text: phonological vs semantic retrieval operations
    analysis_label: Comparison of phonological and semantic error lesion maps
    relation: association
    evidence_ids:
    - P1-S1-C10
    - P11-S1-C3
    - P11-S2-C5
    - P11-S2-C10
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
      pdf_sha256: eef25a7d563cba481de7f96cc58b9bab94911cf24c78f703022dd4cbcbd0f8ea
      source_review: _compare/relationships-2026-11-16/review-current/Schwartz2012
      source_status_sha256: 08d95cd15ffb07482f2b21a8bf34f1e44e8d0686e4ad7f157f10b2b03aad3a68
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P1-S1-C10
      - Accounting without a linked unit P1-S1-C7
      - Accounting without a linked unit P1-S1-C8
      - Unaccounted source passage P1-S1-C8
      - Unaccounted source passage P1-S1-C7
      - 'window 2: invalid/duplicate disposition P3-S2-C2'
      - Result passage disposed without unit P5-S2-C6
      - Result passage disposed without unit P5-S4-C1
      - Result passage disposed without unit P5-S4-C3
      - Result passage disposed without unit P6-S1-C1
      - Result passage disposed without unit P6-S1-C2
      - Result passage disposed without unit P6-S1-C3
      - Accounting without a linked unit P6-S1-C4
      - Result passage disposed without unit P6-S1-C6
      - Unaccounted source passage P6-S1-C4
      - Result passage disposed without unit P6-S1-C11
      - Result passage disposed without unit P6-S1-C12
      - Result passage disposed without unit P6-S1-C9
      - Result passage disposed without unit P6-S2-C6
      - Result passage disposed without unit P6-S2-C7
      - 'window 8: invalid/duplicate disposition P6-S3-C14'
      - Result passage disposed without unit P10-S1-C2
      - Result passage disposed without unit P11-S1-C10
      - Result passage disposed without unit P11-S1-C12
      - Accounting without a linked unit P11-S1-C3
      - Accounting without a linked unit P11-S1-C7
      - Accounting without a linked unit P11-S1-C9
      - Unaccounted source passage P11-S1-C7
      - Unaccounted source passage P11-S1-C3
      - Unaccounted source passage P11-S1-C9
      - Accounting without a linked unit P11-S2-C10
      - Accounting without a linked unit P11-S2-C2
      - Accounting without a linked unit P11-S2-C5
      - Unaccounted source passage P11-S2-C5
      - Unaccounted source passage P11-S2-C10
      - Unaccounted source passage P11-S2-C2
      - Result passage disposed without unit P12-S1-C9
      - Result passage disposed without unit P12-S2-C2
      - Accounting without a linked unit P12-S3-C6
      - Unaccounted source passage P12-S3-C6
      - Result passage disposed without unit P13-S1-C5
      - Accounting without a linked unit P13-S1-C7
      - Result passage disposed without unit P13-S3-C2
      - Unaccounted source passage P13-S1-C7
      - Unresolved source passage P13-S4-C3
      - Accounting without a linked unit P14-S1-C10
      - Result passage disposed without unit P14-S1-C5
      - Result passage disposed without unit P14-S1-C6
      - Unaccounted source passage P14-S1-C10
      unattached_null_or_qualifier_ids:
      - P6-S1-C9
      - P11-S2-C5
      - P13-S1-C5
      suppressed_nonrepresented_units: 10
      default_disposition_count_requires_completeness_check: 255
      unselected_timing_passages:
      - P3-S2-C9
      - P3-S3-C1
      - P3-S3-C5
      - P3-S3-C6
      - P12-S1-C1
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P6-S2-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S2-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P5-S2-C5
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: outcome_definition
        source_ids:
        - P4-S2-C12
        - P4-S3-C5
        - P4-S3-C10
        - P4-S3-C11
        - P5-S2-C11
        - P6-S1-C4
        - P6-S1-C5
        - P6-S1-C11
        - P7-S2-C10
        - P7-S2-C11
        - P11-S1-C10
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: limitations
        source_ids:
        - P6-S2-C8
        - P6-S2-C9
        - P13-S3-C3
        - P13-S3-C4
        - P13-S3-C9
        - P13-S3-C10
        - P13-S4-C1
        - P13-S4-C2
        - P13-S4-C3
        - P14-S1-C1
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: personal_factors
        source_ids:
        - P3-S3-C1
        - P3-S3-C4
        - P3-S3-C5
        - P3-S3-C6
        - P5-S4-C1
        - P5-S4-C2
        - P5-S4-C5
        - P5-S4-C6
        - P6-S1-C4
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - outcome_definition
      - validation
      - limitations
      - personal_factors
      - tested_personal_effects
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-3-1
      - TABLE-2-page-7-2
      unlinked_tables:
      - TABLE-1-page-3-1
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P5-S3
        - P6-S2
        - P6-S4
        - P7-S1
        - P7-S2
        - P7-S3
        - P8-S1
        - P9-S1
        - P10-S1
        - P11-S2
        - P14-S1
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: eef25a7d563cba481de7f96cc58b9bab94911cf24c78f703022dd4cbcbd0f8ea
      source_review: _compare/relationships-2026-11-16/review-current/Schwartz2012
      source_status_sha256: 08d95cd15ffb07482f2b21a8bf34f1e44e8d0686e4ad7f157f10b2b03aad3a68
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C7
      disposition: represented
      result_indexes:
      - 0
      reason: Establishes correlation of lesion status with phonological error rates
        in dorsal stream.
    - source_id: P1-S1-C8
      disposition: represented
      result_indexes:
      - 0
      reason: Qualifies the specific dorsal stream areas (premotor, pre/postcentral
        gyri, SMG).
    - source_id: P1-S1-C10
      disposition: represented
      result_indexes:
      - 2
      reason: Reports no spatial overlap between phonological and semantic error lesion
        maps.
    - source_id: P3-S2-C3
      disposition: represented
      result_indexes:
      - 1
      reason: Identifies association of semantic errors with mid-to-anterior middle
        temporal gyrus and temporal pole.
    - source_id: P5-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes lesion map smoothness.
    - source_id: P5-S4-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports mean aphasia quotient.
    - source_id: P5-S4-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes diagnosis of mild anomic aphasia for specific participants.
    - source_id: P5-S4-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes clinical observations of word retrieval symptoms.
    - source_id: P5-S4-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Provides breakdown of aphasia subtypes.
    - source_id: P5-S4-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports count of participants with apraxia of speech.
    - source_id: P6-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports total count of phonological errors.
    - source_id: P6-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports proportion of errors from non-apraxic patients.
    - source_id: P6-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports percentage of target-related errors.
    - source_id: P6-S1-C4
      disposition: represented
      result_indexes: []
      reason: This is a behavioral correlation (frequency/length), not a lesion-symptom
        relationship as requested.
    - source_id: P6-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports mean error proportions by group.
    - source_id: P6-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports error specificity ratio by group.
    - source_id: P6-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports correlation with aphasia severity.
    - source_id: P6-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports null effect of group in ANOVA.
    - source_id: P6-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports mean auditory discrimination error score.
    - source_id: P6-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports mean auditory discrimination errors by group.
    - source_id: P6-S1-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports null effect of group in ANOVA.
    - source_id: P6-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes lesion coverage.
    - source_id: P6-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes lesion coverage.
    - source_id: P6-S2-C10
      disposition: represented
      result_indexes:
      - 0
      reason: Reports total significant voxels for phonological errors.
    - source_id: P6-S2-C11
      disposition: represented
      result_indexes:
      - 0
      reason: Identifies concentration in postcentral gyrus.
    - source_id: P6-S2-C12
      disposition: represented
      result_indexes:
      - 0
      reason: Identifies peak t-value in precentral gyrus.
    - source_id: P6-S2-C13
      disposition: represented
      result_indexes:
      - 0
      reason: Identifies significant voxels in white matter.
    - source_id: P6-S2-C15
      disposition: represented
      result_indexes:
      - 0
      reason: Identifies significant voxels in Rolandic operculum.
    - source_id: P6-S3-C5
      disposition: represented
      result_indexes:
      - 0
      reason: Identifies significant voxels in supramarginal gyrus.
    - source_id: P6-S3-C6
      disposition: represented
      result_indexes:
      - 0
      reason: Identifies significant voxels in insula.
    - source_id: P6-S3-C7
      disposition: represented
      result_indexes:
      - 0
      reason: Identifies significant voxels in inferior frontal gyrus.
    - source_id: P6-S3-C10
      disposition: represented
      result_indexes:
      - 0
      reason: Reports null result for pSTG and pSTS.
    - source_id: P6-S3-C12
      disposition: represented
      result_indexes:
      - 0
      reason: Reports negligible involvement of area Spt.
    - source_id: P6-S4-C1
      disposition: represented
      result_indexes:
      - 0
      reason: Reports expansion of clusters at relaxed threshold.
    - source_id: P6-S4-C2
      disposition: represented
      result_indexes:
      - 0
      reason: Reports Spt voxel count at relaxed threshold.
    - source_id: P7-S1-C1
      disposition: represented
      result_indexes:
      - 0
      reason: Qualifies STG voxels as contiguous with SMG cluster.
    - source_id: P7-S1-C2
      disposition: represented
      result_indexes:
      - 0
      reason: Confirms null result for pSTG and pSTS.
    - source_id: P7-S1-C3
      disposition: represented
      result_indexes:
      - 0
      reason: Summarizes concentration in anterior dorsal stream.
    - source_id: P7-S1-C10
      disposition: represented
      result_indexes:
      - 6
      - 7
      reason: States both secondary analyses produced anterior-centered maps.
    - source_id: P7-S1-C11
      disposition: represented
      result_indexes:
      - 6
      reason: Reports voxel count for lesion size regression analysis.
    - source_id: P7-S1-C12
      disposition: represented
      result_indexes:
      - 6
      reason: Identifies concentrations in postcentral gyrus, SMG, and insula for
        lesion size regression.
    - source_id: P7-S1-C13
      disposition: represented
      result_indexes:
      - 7
      reason: Reports voxel count for non-apraxic sample analysis.
    - source_id: P7-S1-C14
      disposition: represented
      result_indexes:
      - 7
      reason: Identifies concentration in SMG and postcentral gyrus for non-apraxic
        sample.
    - source_id: P7-S2-C8
      disposition: represented
      result_indexes:
      - 4
      reason: Reports 29% overlap between arcuate fasciculus mask and phonological
        error map.
    - source_id: P7-S2-C10
      disposition: represented
      result_indexes:
      - 3
      reason: Reports total significant voxels for auditory discrimination errors.
    - source_id: P7-S2-C11
      disposition: represented
      result_indexes:
      - 3
      reason: Identifies band from Spt/pSTG through SMG, pre/postcentral gyri to IFG.
    - source_id: P7-S2-C12
      disposition: represented
      result_indexes:
      - 3
      reason: Identifies superior extension in pre/postcentral gyri.
    - source_id: P7-S3-C2
      disposition: represented
      result_indexes:
      - 3
      reason: Identifies voxels along STG and pSTS.
    - source_id: P7-S3-C3
      disposition: represented
      result_indexes:
      - 3
      reason: Identifies voxels in planum temporale.
    - source_id: P7-S3-C4
      disposition: represented
      result_indexes:
      - 3
      reason: Reports 68% of Spt mask is significant for auditory discrimination errors.
    - source_id: P7-S3-C6
      disposition: represented
      result_indexes:
      - 4
      reason: Reports 15,015 shared voxels between auditory discrimination and phonological
        errors.
    - source_id: P7-S3-C7
      disposition: represented
      result_indexes:
      - 4
      reason: Quantifies shared voxels as 55% of auditory and 23% of phonological
        totals.
    - source_id: P11-S1-C3
      disposition: represented
      result_indexes:
      - 2
      reason: Reports zero overlap between semantic and phonological error voxels.
    - source_id: P11-S1-C7
      disposition: represented
      result_indexes:
      - 4
      reason: Reports 55% of auditory discrimination voxels also associated with phonological
        errors.
    - source_id: P11-S2-C5
      disposition: represented
      result_indexes:
      - 2
      reason: States phonological and semantic error voxels did not overlap.
    - source_id: P11-S2-C10
      disposition: represented
      result_indexes:
      - 2
      reason: Confirms no voxels were significant in both semantic and phonological
        analyses.
    - source_id: P12-S1-C10
      disposition: represented
      result_indexes:
      - 3
      reason: Confirms involvement of pSTG and Spt in auditory discrimination errors.
    unresolved_coverage:
    - source_id: P6-S1-C4
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P6-S3-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P6-S3-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P6-S3-C13
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P6-S3-C15
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P7-S1-C15
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P7-S1-C16
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P7-S3-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P7-S3-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S1-C1
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S1-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S1-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S1-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C1
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C12
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C13
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S2-C1
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S2-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S2-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S1-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S1-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S2-C1
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S2-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S3-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S4-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S1-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S1-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S2-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S3-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P14-S1-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P14-S1-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P14-S1-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P14-S1-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P14-S1-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C8
    - P5-S2-C6
    - P5-S4-C1
    - P5-S4-C2
    - P5-S4-C3
    - P5-S4-C5
    - P5-S4-C6
    - P6-S1-C1
    - P6-S1-C2
    - P6-S1-C3
    - P6-S1-C4
    - P6-S1-C6
    - P6-S1-C7
    - P6-S1-C8
    - P6-S1-C9
    - P6-S1-C11
    - P6-S1-C12
    - P6-S1-C13
    - P6-S2-C6
    - P6-S2-C7
    - P6-S2-C13
    - P6-S3-C8
    - P6-S3-C11
    - P6-S3-C13
    - P6-S3-C15
    - P6-S4-C1
    - P6-S4-C2
    - P7-S1-C1
    - P7-S1-C2
    - P7-S1-C15
    - P7-S1-C16
    - P7-S3-C5
    - P7-S3-C8
    - P9-S1-C1
    - P9-S1-C2
    - P9-S1-C3
    - P10-S1-C2
    - P11-S1-C1
    - P11-S1-C9
    - P11-S1-C10
    - P11-S1-C12
    - P11-S1-C13
    - P11-S2-C1
    - P11-S2-C2
    - P11-S2-C8
    - P12-S1-C9
    - P12-S1-C11
    - P12-S2-C1
    - P12-S2-C2
    - P12-S3-C6
    - P12-S4-C4
    - P13-S1-C5
    - P13-S1-C7
    - P13-S2-C3
    - P13-S3-C2
    - P14-S1-C4
    - P14-S1-C5
    - P14-S1-C6
    - P14-S1-C9
    - P14-S1-C10
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-3-1
    - TABLE-2-page-7-2
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P3-S3-C2
      recruited_sample:
      - P3-S2-C5
      eligibility:
      - P3-S2-C5
      - P3-S3-C1
      - P3-S3-C2
      - P3-S3-C3
      - P3-S3-C7
      - P3-S3-C8
      - P4-S3-C12
      imaging_provenance:
      - P4-S4-C5
      - P5-S1-C4
      - P5-S1-C6
      - P5-S1-C9
      - P5-S1-C11
      - P5-S2-C2
      - P7-S2-C5
      - P10-S1-C8
      imaging_timing:
      - P3-S2-C6
      outcome_timing:
      - P3-S2-C5
      outcome_definition: []
      validation: []
      analysis_restrictions:
      - P5-S2-C10
      - P5-S3-C2
      - P6-S3-C14
      - P7-S1-C4
      - P7-S1-C6
      - P7-S1-C13
      dependent_variable_statement:
      - P5-S2-C11
      - P5-S2-C12
      - P4-S3-C6
      - P4-S3-C11
      limitations: []
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P3-S2-C3
      - P4-S4-C4
      - P5-S2-C12
      - P5-S3-C2
      - P6-S1-C8
      - P6-S1-C13
      - P7-S1-C5
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P3-S3-C4
      - P3-S3-C5
      - P3-S3-C6
      - P5-S4-C1
      - P5-S4-C2
      - P5-S4-C5
      - P5-S4-C6
      - P6-S1-C4
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P6-S2-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S2-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P5-S2-C5
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: outcome_definition
      source_ids:
      - P4-S2-C12
      - P4-S3-C5
      - P4-S3-C10
      - P4-S3-C11
      - P5-S2-C11
      - P6-S1-C4
      - P6-S1-C5
      - P6-S1-C11
      - P7-S2-C10
      - P7-S2-C11
      - P11-S1-C10
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: limitations
      source_ids:
      - P6-S2-C8
      - P6-S2-C9
      - P13-S3-C3
      - P13-S3-C4
      - P13-S3-C9
      - P13-S3-C10
      - P13-S4-C1
      - P13-S4-C2
      - P13-S4-C3
      - P14-S1-C1
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: personal_factors
      source_ids:
      - P3-S3-C1
      - P3-S3-C4
      - P3-S3-C5
      - P3-S3-C6
      - P5-S4-C1
      - P5-S4-C2
      - P5-S4-C5
      - P5-S4-C6
      - P6-S1-C4
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
      pdf_sha256: eef25a7d563cba481de7f96cc58b9bab94911cf24c78f703022dd4cbcbd0f8ea
      review_sha256: fe3f6b3213144baf063144c24d628a2d2bbff829e01ad23f846dfc458380b042
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
      - P1-S1-C10
      - P11-S1-C3
      - P11-S2-C5
      - P11-S2-C10
      source_result: The study performed a voxel-based lesion-symptom mapping (VLSM)
        analysis comparing the anatomical substrates for phonological errors (non-word
        errors) and semantic errors (real-word errors) in object naming. The analysis
        found zero spatial overlap between the voxels associated with phonological
        errors and those associated with semantic errors, supporting the hypothesis
        that the brain segregates these retrieval operations.
      result_status: not_detected
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis is the comparison of VLSM maps for phonological
            vs semantic errors. The source explicitly describes this as a separate
            analysis to determine spatial overlap (P1-S1-C10, P3-S2-C4). The proposed
            core correctly identifies this specific comparison.
          source_ids:
          - P1-S1-C10
          - P3-S2-C4
          - P11-S1-C3
        direction:
          answer: fits
          reason: The source states 'no spatial overlap' and 'overlap was zero' (P1-S1-C10,
            P11-S1-C3, P11-S2-C10). The proposed core uses 'no_effect' to describe
            the lack of overlap, which is the correct interpretation of a null finding
            in this context (absence of shared voxels).
          source_ids:
          - P1-S1-C10
          - P11-S1-C3
          - P11-S2-C10
        construct:
          answer: fits
          reason: The exposure is lesion location (via VLSM), and the outcome is the
            distinction between phonological and semantic retrieval operations. The
            patient measurement is correctly identified as template_lesion_overlap,
            as the analysis involves overlaying lesion maps derived from patient data
            onto a template (MNI/Colin27) to check for voxel intersection. The definitions
            of phonological (non-word) and semantic (real-word) errors are consistent
            with the source (P4-S2-C11, P4-S3-C3).
          source_ids:
          - P4-S2-C11
          - P4-S3-C3
          - P5-S1-C11
          - P11-S2-C5
        qualifications:
          answer: fits
          reason: The proposed core includes the critical qualification that the overlap
            analysis used a lenient FDR threshold (q=0.05) to avoid underestimating
            overlap (P5-S2-C15, P6-S3-C14). It also correctly notes the definitions
            of the error types. The limitation regarding poor lesion coverage in posterior
            inferior temporal gyrus is also included.
          source_ids:
          - P5-S2-C15
          - P6-S3-C14
          - P11-S2-C3
        missing_material_caveat:
          answer: fits
          reason: 'The core includes the relevant limitations: the lenient threshold
            used for the overlap test and the power limitation in specific posterior
            regions. The general limitation about lesion characterization underestimating
            functional damage is also included. No material caveats that would change
            the interpretation of the null overlap are missing.'
          source_ids:
          - P11-S2-C3
          - P14-S1-C1
          - P5-S2-C15
      optional_pending:
      - sample.time_post_onset
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
    normalizations:
    - field: sample.time_post_onset
      original: at least 1 month post-onset of aphasia
      action: not_transcribed
      reason: 'Numbers not grounded in usable selected source readings: 1'
    analysis_identity:
      id: R003
      exposure:
        text: lesion location
      outcome:
        text: phonological vs semantic retrieval operations
      analysis_label: Comparison of phonological and semantic error lesion maps
      relation: association
      evidence_ids:
      - P1-S1-C10
      - P11-S1-C3
      - P11-S2-C5
      - P11-S2-C10
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
        pdf_sha256: eef25a7d563cba481de7f96cc58b9bab94911cf24c78f703022dd4cbcbd0f8ea
        source_review: _compare/relationships-2026-11-16/review-current/Schwartz2012
        source_status_sha256: 08d95cd15ffb07482f2b21a8bf34f1e44e8d0686e4ad7f157f10b2b03aad3a68
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P3-S3-C1:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: eef25a7d563cba481de7f96cc58b9bab94911cf24c78f703022dd4cbcbd0f8ea
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 7d51c1433b78167881b2aace58c99e988280f169cf10b4911c375af84b02fbc4
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S3-C1
          page: 3
          text_layer_sha256: 7d51c1433b78167881b2aace58c99e988280f169cf10b4911c375af84b02fbc4
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: 'The inclusion criteria were as follows: at least 1 month post-onset
          of

          aphasia secondary to stroke, living at home, medically stable without

          major psychiatric or neurological co-morbidities, premorbid right hand-

          edness, English as primary language, adequate vision and hearing

          (with or without correction) and CT or MRI conﬁrmed left hemisphere

          cortical lesion.'
        anchor_text: 'The inclusion criteria were as follows: at least 1 month post-onset
          of

          aphasia secondary to stroke, living at home, medically stable without

          major psychiatric or neurological co-morbidities, premorbid right hand-

          edness, English as primary language, adequate vision and hearing

          (with or without correction) and CT or MRI conﬁrmed left hemisphere

          cortical lesion.'
        excluded_fragments: []
        image_sha256: 5f4bfd1556e8e47705993a4319cec2be46814b219ff91fc157b7f8e9f07cef9c
      P3-S3-C2:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: eef25a7d563cba481de7f96cc58b9bab94911cf24c78f703022dd4cbcbd0f8ea
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: ce29f38ee4728c0ad27539233dc9a8b363196d1c8fef3c1a20c28f0d27a0af4a
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S3-C2
          page: 3
          text_layer_sha256: ce29f38ee4728c0ad27539233dc9a8b363196d1c8fef3c1a20c28f0d27a0af4a
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Of the 142 individuals enrolled, 106 qualiﬁed for the

          current study.'
        anchor_text: 'Of the 142 individuals enrolled, 106 qualiﬁed for the

          current study.'
        excluded_fragments: []
        image_sha256: 821fc113b94e6a5ab6883beab5e51e10cafcec2251aa77738a534f1f38645583
        transcription: '. Of the 142 individuals enrolled, 106 qualified for the

          current study'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 1
  quote: 'In a separate analysis, we compared the lesion maps for phonological and
    semantic errors and determined that

    there was no spatial overlap, demonstrating that the brain segregates phonological
    and semantic retrieval operations in word

    production.'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-25'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
