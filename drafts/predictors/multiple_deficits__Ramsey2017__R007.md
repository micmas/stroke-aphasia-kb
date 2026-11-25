---
id: multiple_deficits
name: occurrence of multiple deficits
kind: predictor
findings:
- id: f1
  target: attention_recovery
  target_kind: prognosis
  claim: after accounting for the severity of the initial deficit, the occurrence
    of multiple deficits negatively impacted attention recovery
  direction: unlikely
  relationship: correlational
  method: behavioral_only
  sample:
    n: not_reported
    population: first-time stroke patients with heterogeneous lesions
    phase: not_reported
    time_post_onset: sub-acute (approximately two weeks) to three months post-stroke
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - the behavioral battery was a trade-off between completeness and feasibility
  - some domains were coarsely sampled (e.g., executive function)
  - social cognition, emotions, and theory of mind were not measured
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: The number of behavioral domains (language, spatial
    memory, verbal memory, visual-field attention, and motor) showing impairment,
    defined as a score two standard deviations below the mean of healthy controls.
    adjusted for severity of the initial deficit; adjusted for education, age, hours
    of therapy, and lesion size. Additional metadata has not been transcribed; review
    the pending-field flags before approval.'
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
    - not_transcribed:sample.n
    - proposed_concept:attention_recovery
  citation: '@Ramsey2017'
  source_passages:
  - section: Original source P1-S1-C18
    page: 1
    quote: "Finally, after accounting for the severity of the initial deficit, language\
      \ and visual memory \nrecovery was worse for those with lower levels of education,\
      \ while the occurrence of multiple deficits negatively impacted \nattention\
      \ recovery."
    supports: claim
  - section: Original source P2-S1-C9
    page: 2
    quote: "Results\nSubjects (n =​ 172) with a first symptomatic stroke anywhere\
      \ in the \nbrain and clinical evidence of any neurological impairment were pro­\n\
      spectively recruited, with n =​ 132 meeting post-enrolment inclusion \ncriteria."
    supports: sample
  - section: Original source P4-S1-C8
    page: 4
    quote: "For each \npatient, we entered the number of deficits as a moderator variable\
      \ \nin a regression analysis that used the sub-acute scores to predict \nthe\
      \ three-month scores."
    supports: method
  - section: Original source P4-S1-C7
    page: 4
    quote: "The effects of education, age, hours of \ntherapy and lesion size, which\
      \ correlates with the number of deficits \n(r =​ 0.22, P =​ 0.012), were added\
      \ as covariates of interest."
    supports: confounders
  - section: Original source P8-S3-C12
    page: 8
    quote: "Patients with a score two standard deviations below the mean of controls\
      \ \nwere identified as having a deficit, while patients with ‘no deficit’ had\
      \ scores \nwithin two standard deviations of healthy controls."
    supports: method
  - section: Original source P6-S2-C12
    page: 6
    quote: 'Another limitation is that the behavioural battery was a trade-

      off between completeness and feasibility.'
    supports: limitation
  - section: Original source P6-S2-C13
    page: 6
    quote: "Some domains were either \ncoarsely sampled (for example, executive function),\
      \ while others, \nincluding social cognition, emotions and theory of mind, were\
      \ not \nmeasured at all."
    supports: limitation
predictor_type: clinical
short_definition: The number of behavioral domains (language, spatial memory, verbal
  memory, visual-field attention, and motor) showing impairment, defined as a score
  two standard deviations below the mean of healthy controls.
assessment:
- 44 neuropsychological tests
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-25'
relationship_review:
  paper: Ramsey2017
  proposal_id: R007
  review_status_sha256: c36a88e587d223852996450f88f386b2a0bfdfc53fb0255f3b3c0ebc6cd974f0
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: dd2fb9fbb469ef382090372171f0fb42e0c4336fd5b0902af0605f2b4bff7356
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: dd2fb9fbb469ef382090372171f0fb42e0c4336fd5b0902af0605f2b4bff7356
        A/passages.json: 81beb922f9078fba046646d200366d6855fb1af9630a45fc002c873afde64a90
        A/raw.json: 377fea7b13a9f8dbb049d492bbc7e7f431d99759aabc11dd327ebef7c208276f
        A/source-units.json: 6bfd1e0973b693a49c16495f4ce0372cb3e6b064c84d42101b1ce79840bcf6ee
        A/full-source-units.json: e98dcc43a4f47aba77aebe1449705ca618ee50b8f5d5d60a260917f9c852082e
        A/meta.json: 90e68bc90fd7f2191c6c3c8d7f80831e8542f362d33dfe536577048d7c732f2e
        A/table-images/TABLE-1-page-3-1.png: 95d28ee39008cb0adeb8740f578c63cf3b75f10741b86eb3815118e0bb7499df
        A/table-images/page-3.png: 869dce142b191fa16199c78a8225f6a8174608bd6989d0089532f17386ba7f8d
        A/table-images/page-6.png: a8f011ec4474e42af1177fefd83a6d84f3137cc4b4db80cfad737b1f5ec2adbb
        A/table-images/TABLE-2-page-6-1.png: e21a13d2ce6c7f1b887cd87f08e2cbaea58e2d243cd41210e28ea8938d12aed5
        A/table-images/manifest.json: 8dfd4179ecfbaa5ce54804374ed4839715dca99c6ca6ff4b1b14d7fb2ed817e4
        A/clauses/window-10/raw.json: 36385aa25ce893b9cd4186589a35bb6fa1e1190a9e904d27ef47a361f5c4e4a2
        A/clauses/window-10/prompt.txt: d01547d0a4e822ed8261c216759b07e6db986d1e7379d5227a44578cb58ff2a0
        A/clauses/window-10/meta.json: 0f15a3de11c98de67b1b471131bd71b3714fdaa2e59f6436505f33c69e104f3c
        A/clauses/window-03/raw.json: b718bcb720c3ccc38755c493d7b5873fd10e9e1d871f8b4d83cb5155e0356061
        A/clauses/window-03/prompt.txt: bf217425950dadd5200b645ff66474c17fe4072c5942fcea19c811a7a33e825b
        A/clauses/window-03/meta.json: 425da8e128a4a29984884dda9e2691bcaa2511c1e8f06e95939ce6fff016044f
        A/clauses/window-04/raw.json: 62823fa24b28d89678209d127b14f3958f1fa388edeb31c7f3b17d1b659748cc
        A/clauses/window-04/prompt.txt: 10ddc2f43da6c059338fdf2c8195df7d910c047eea5c7668e46067e780cd5a57
        A/clauses/window-04/meta.json: 7fd78d41e47d9d8587c29c588048b52f808e86462741557c14e0c3f4bfefa9ca
        A/clauses/window-05/raw.json: 3db0ce3e4a4bc5d166b0d6c41630930d1a80e349323a71e2ce14cf5d75e45bc7
        A/clauses/window-05/prompt.txt: a38a97a022b2fc3de9d6490c81e0bd156e44f5e9f22c3f852af54ba862ec5d3e
        A/clauses/window-05/meta.json: afd6a17aee204fdb3c8ded9740f42ef141364e3b84db65f718bfdb7c29ff18a1
        A/clauses/window-02/raw.json: 7693d16e131cb2714e8caab36e481c2e37fe1aacd8ff27a46650dfad64e2e147
        A/clauses/window-02/prompt.txt: 78e76138e6f4d505c90ab2c36c77992d128f32d421e0bbe13f3b6703b8009862
        A/clauses/window-02/meta.json: 2883e76e2ffd0592a9c739eb30be81c444c86d01f8e10d7571ef8fa19872a1f7
        A/clauses/window-09/raw.json: cf9e0a02a433e093488c5f499dc3544b5386acdab6a244a51296777af4dd24a0
        A/clauses/window-09/prompt.txt: f6a89593295a7b75776d8ca06041d77232f16bc399a325572621a265e2c29c24
        A/clauses/window-09/meta.json: 50e5bdd33f33ccc810086ea436985e416f7c6c08110e448787081eacd973cb15
        A/clauses/window-07/raw.json: 5321ec81afe6332b5b647d450c06532277aee387052423f67605066a758f2e1e
        A/clauses/window-07/prompt.txt: 030ad432ce141ab52da6f2463dc2cf62d607cdddc18bb456bbb574502a897f7b
        A/clauses/window-07/meta.json: 5ee50c516c543054ea9b1e092d5804f0824e77f2558955f90b8b78075745a6ba
        A/clauses/window-01/raw.json: e96d4837db4c5451797f2bd25d35cdbed0d3356fed9ffb15ef0dba5630f943b4
        A/clauses/window-01/prompt.txt: 5be6347b2faebf4fe1015464de83b30b17ccecb30772ca72d0f249b1ed653daf
        A/clauses/window-01/meta.json: 8368271891e640a2c3c38300d41606fa338b5eb57eee974e1774efecd96db2db
        A/clauses/window-06/raw.json: 4cdf310161d9a0a7f6725e67eee07da4742b96af8df6b8fccdff6661116536a5
        A/clauses/window-06/prompt.txt: 7294829e6feada05427910d0fa077409a74eeb372d084b49157cebc6f35a9b2f
        A/clauses/window-06/meta.json: 5275eb45d9290b517e26b49ca00e768e779bda9453c1511b0758b0a74587357f
        A/clauses/window-08/raw.json: 980f4c068e4453fb646409a5ae6ff13f8fefb49dce12065152fb87c5d6ea65e1
        A/clauses/window-08/prompt.txt: 53aafff913f3eefa002ba551a5533fd132a9d38a25ac726e1bb1e528f5a4459b
        A/clauses/window-08/meta.json: 659155b8d390fa3e9bf521f5ddedcbd5622e59805bdc7d7213ba4b2513d36e4f
        A/tables/TABLE-2-page-6-2/raw.json: efba70f5f1cd9c16390e8e5d775f9d48c26ea4425668f73d6f1a4721ff86a955
        A/tables/TABLE-2-page-6-2/prompt.txt: 4ef0574bed8d4a35b5681bad82d5e129ace272b1bf8739d50a1148554f5640ed
        A/tables/TABLE-2-page-6-2/meta.json: 9e37b5e16150fa879cbd63d705cd29f70299d866a5cff3934814fd63698ea98b
        A/tables/TABLE-1-page-3-1/raw.json: 6c849e262d51b48f18d887072c3c76c535419497952d53dffcae1568144fff8b
        A/tables/TABLE-1-page-3-1/prompt.txt: c5017af8deab40a475289593e0bfc1ed85d0eae4d20e1eac59be6c3a35b3e8ad
        A/tables/TABLE-1-page-3-1/meta.json: 6bb059e8e4006c9a2febb4c8b3e5a1cf7d615fdba64effa128bcd88d1bbf1bfe
        B/passages.json: 81beb922f9078fba046646d200366d6855fb1af9630a45fc002c873afde64a90
        B/raw.json: 973a9b89152740b45f4d6e0e915489b4e1a11cf2f050a7410b0e0f19af95584e
        B/source-units.json: 6bfd1e0973b693a49c16495f4ce0372cb3e6b064c84d42101b1ce79840bcf6ee
        B/full-source-units.json: e98dcc43a4f47aba77aebe1449705ca618ee50b8f5d5d60a260917f9c852082e
        B/meta.json: e06d89b4716530479a6a33945d201bc0747cab63438836fa34a4e6c49318eeb1
        B/table-images/TABLE-1-page-3-1.png: 95d28ee39008cb0adeb8740f578c63cf3b75f10741b86eb3815118e0bb7499df
        B/table-images/page-3.png: 869dce142b191fa16199c78a8225f6a8174608bd6989d0089532f17386ba7f8d
        B/table-images/page-6.png: a8f011ec4474e42af1177fefd83a6d84f3137cc4b4db80cfad737b1f5ec2adbb
        B/table-images/TABLE-2-page-6-1.png: e21a13d2ce6c7f1b887cd87f08e2cbaea58e2d243cd41210e28ea8938d12aed5
        B/table-images/manifest.json: b66a145ab28a91e327004419477521cd258d24ee301c323b5afb052ad03fff3e
        B/clauses/window-10/raw.json: eafacb4acef8bd591422f15b6943afec13bae8ad175ae7a437b5165cd7d2b88d
        B/clauses/window-10/prompt.txt: d01547d0a4e822ed8261c216759b07e6db986d1e7379d5227a44578cb58ff2a0
        B/clauses/window-10/meta.json: 8dccaf43029777b97234517b0d870c8e11f108abbc1e8faf1b9977bca68d2934
        B/clauses/window-03/raw.json: 25530ed915c32a7f0adae89f5c0d13ff8901f55c7e8c8cbae34454580a3ede88
        B/clauses/window-03/prompt.txt: bf217425950dadd5200b645ff66474c17fe4072c5942fcea19c811a7a33e825b
        B/clauses/window-03/meta.json: a31b6f9d70c7f914d0ac403cfaf1573e3de183e11432dafd820d0ae96d9fadb9
        B/clauses/window-04/raw.json: ebd8b1fc855f7b12c2af6ac47fe24eee5eedd1c28b31bb4684f1c811579ae4a1
        B/clauses/window-04/prompt.txt: 10ddc2f43da6c059338fdf2c8195df7d910c047eea5c7668e46067e780cd5a57
        B/clauses/window-04/meta.json: e563355d714bdeaf5317b6512e6ed7a32423c2bdc3638e6a11be0926f9116d24
        B/clauses/window-05/raw.json: ed9cc8f00f3fcd9ab6dd6b9bd7dca28660fa1267fef4374aa7cbaca1e8fae87a
        B/clauses/window-05/prompt.txt: a38a97a022b2fc3de9d6490c81e0bd156e44f5e9f22c3f852af54ba862ec5d3e
        B/clauses/window-05/meta.json: d586d4c5afba9e94391d12423a03d4a1b7e2db103159969ce4d76c658bfd5137
        B/clauses/window-02/raw.json: f23067661247c2760a9b1a95c79ee68122d2299cb9a64bbcc208a5f6794e9743
        B/clauses/window-02/prompt.txt: 78e76138e6f4d505c90ab2c36c77992d128f32d421e0bbe13f3b6703b8009862
        B/clauses/window-02/meta.json: 3523cc0925e1b1578a255dc44101be8c9de2097118ecd76652073f4ab3ab652a
        B/clauses/window-09/raw.json: 03c4fabede002642399352fb1fb422dc9670404335874a2ca4124a5b60300dd4
        B/clauses/window-09/prompt.txt: f6a89593295a7b75776d8ca06041d77232f16bc399a325572621a265e2c29c24
        B/clauses/window-09/meta.json: e6c8d4283c8e5feb6d6457af6d71bb573a678f142d6e1662cef001edf6b5ec19
        B/clauses/window-07/raw.json: 99267fb80ae668312124e9bdcff12eeb11de04ad98d438673355cfe275709ae6
        B/clauses/window-07/prompt.txt: 030ad432ce141ab52da6f2463dc2cf62d607cdddc18bb456bbb574502a897f7b
        B/clauses/window-07/meta.json: 92b5a254b4f5b8ecd84c5c0a7f086ec6e8bdf30a9420ec7384da64ebb34b7ab8
        B/clauses/window-01/raw.json: b9adb2619a9f7e02fabb7dcdba40c80ab178283195008efb7aec8def1b080864
        B/clauses/window-01/prompt.txt: 5be6347b2faebf4fe1015464de83b30b17ccecb30772ca72d0f249b1ed653daf
        B/clauses/window-01/meta.json: f5f1d86e35cf58045c6213395028914bb509b1d8a8eb8e62ea1255fa6b166e99
        B/clauses/window-06/raw.json: 2cbe3f06ca15dd465402783af8174d37556c39cb40155b2e4dd5a8b5249d33f7
        B/clauses/window-06/prompt.txt: 7294829e6feada05427910d0fa077409a74eeb372d084b49157cebc6f35a9b2f
        B/clauses/window-06/meta.json: fc224b26eb883884cc8ba7ab0fa04f6613a5313f6097a4b75e98e4c687518394
        B/clauses/window-08/raw.json: 43efc6878b24879d2c638c74b246289444180c0c38a62f7820c0ce7b2fd37e80
        B/clauses/window-08/prompt.txt: 53aafff913f3eefa002ba551a5533fd132a9d38a25ac726e1bb1e528f5a4459b
        B/clauses/window-08/meta.json: 777511abed566e2e444db4df857f8b2d968eef1fb32e5d1951b88fd219242502
        B/tables/TABLE-2-page-6-2/raw.json: 1a718a1a7aed9d6fc89871fd75f7edff4ed0c8b6c26c1b6dfd00070479b5d1af
        B/tables/TABLE-2-page-6-2/prompt.txt: 4ef0574bed8d4a35b5681bad82d5e129ace272b1bf8739d50a1148554f5640ed
        B/tables/TABLE-2-page-6-2/meta.json: c5e89c123c11b4003c7cd194e83954de31dedee86cfa8491e63cfdfe71c45a9f
        B/tables/TABLE-1-page-3-1/raw.json: aff8fee74e5b761f5678c8b0ba630113b30c052a351d5ccf645dbb751a804e12
        B/tables/TABLE-1-page-3-1/prompt.txt: c5017af8deab40a475289593e0bfc1ed85d0eae4d20e1eac59be6c3a35b3e8ad
        B/tables/TABLE-1-page-3-1/meta.json: 10914cdbf7a6d49f78a60e9fc5b622b1fd57238d913a15e9873c5433a00cc6af
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
      pdf_sha256: dd2fb9fbb469ef382090372171f0fb42e0c4336fd5b0902af0605f2b4bff7356
      source_review: _compare/relationships-2026-11-16/review-current/Ramsey2017
      source_status_sha256: 4c5ae3a652cd3d15d7e37174bfe3fe8f69e82a987e011577f4a59c6b3248cc01
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R007
    exposure:
      text: occurrence of multiple deficits
    outcome:
      text: attention recovery
    analysis_label: Personal factors and recovery (adjusted)
    relation: sensitivity
    evidence_ids:
    - P1-S1-C18
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
      pdf_sha256: dd2fb9fbb469ef382090372171f0fb42e0c4336fd5b0902af0605f2b4bff7356
      source_review: _compare/relationships-2026-11-16/review-current/Ramsey2017
      source_status_sha256: 4c5ae3a652cd3d15d7e37174bfe3fe8f69e82a987e011577f4a59c6b3248cc01
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P1-S1-C15
      - Result passage disposed without unit P1-S1-C16
      - Result passage disposed without unit P1-S1-C17
      - Result passage disposed without unit P1-S1-C18
      - Result passage disposed without unit P2-S2-C3
      - Result passage disposed without unit P2-S2-C10
      - Result passage disposed without unit P2-S2-C11
      - Result passage disposed without unit P2-S2-C4
      - Result passage disposed without unit P2-S3-C11
      - Result passage disposed without unit P2-S3-C12
      - Result passage disposed without unit P2-S3-C13
      - Accounting without a linked unit P2-S4-C2
      - Result passage disposed without unit P2-S4-C4
      - Unaccounted source passage P2-S4-C2
      - Result passage disposed without unit P3-S2-C10
      - Accounting without a linked unit P3-S2-C6
      - Accounting without a linked unit P3-S2-C7
      - Accounting without a linked unit P3-S2-C8
      - Accounting without a linked unit P4-S1-C4
      - Accounting without a linked unit P4-S1-C6
      - Accounting without a linked unit P4-S1-C7
      - Unaccounted source passage P3-S2-C8
      - Unaccounted source passage P4-S1-C6
      - Unaccounted source passage P3-S2-C6
      - Unaccounted source passage P4-S1-C4
      - Unaccounted source passage P3-S2-C7
      - Unaccounted source passage P4-S1-C7
      - Accounting without a linked unit P4-S2-C12
      - Accounting without a linked unit P4-S2-C6
      - Accounting without a linked unit P4-S3-C3
      - Accounting without a linked unit P4-S3-C6
      - Accounting without a linked unit P4-S3-C8
      - Unaccounted source passage P4-S3-C6
      - Unaccounted source passage P4-S2-C6
      - Unaccounted source passage P4-S3-C3
      - Unaccounted source passage P4-S3-C8
      - Unaccounted source passage P4-S2-C12
      - Accounting without a linked unit P4-S3-C12
      - Accounting without a linked unit P4-S3-C13
      - Accounting without a linked unit P4-S3-C14
      - Accounting without a linked unit P4-S3-C15
      - Accounting without a linked unit P4-S4-C7
      - Accounting without a linked unit P5-S1-C3
      - Accounting without a linked unit P5-S1-C4
      - Unaccounted source passage P4-S3-C15
      - Unaccounted source passage P4-S3-C14
      - Unaccounted source passage P4-S4-C7
      - Unaccounted source passage P5-S1-C3
      - Unaccounted source passage P5-S1-C4
      - Unaccounted source passage P4-S3-C12
      - Unaccounted source passage P4-S3-C13
      - Accounting without a linked unit P5-S1-C9
      - Result passage disposed without unit P5-S2-C2
      - Result passage disposed without unit P5-S2-C7
      - Unaccounted source passage P5-S1-C9
      - Accounting without a linked unit P6-S1-C13
      - Accounting without a linked unit P6-S1-C4
      - Accounting without a linked unit P6-S1-C5
      - Accounting without a linked unit P6-S1-C6
      - Accounting without a linked unit P6-S1-C7
      - Unaccounted source passage P6-S1-C4
      - Unaccounted source passage P6-S1-C7
      - Unaccounted source passage P6-S1-C5
      - Unaccounted source passage P6-S1-C6
      - Unaccounted source passage P6-S1-C13
      - Accounting without a linked unit P6-S2-C4
      - Accounting without a linked unit P6-S2-C5
      - Accounting without a linked unit P7-S1-C4
      - Result passage disposed without unit P7-S1-C6
      - Unaccounted source passage P7-S1-C4
      - Unaccounted source passage P6-S2-C4
      - Unaccounted source passage P6-S2-C5
      - Result passage disposed without unit P8-S2-C8
      unattached_null_or_qualifier_ids:
      - P3-S2-C6
      - P3-S2-C7
      - P3-S2-C8
      - P3-S2-C10
      - P4-S1-C4
      - P4-S1-C6
      - P6-S1-C6
      - P7-S1-C4
      - P7-S1-C6
      suppressed_nonrepresented_units: 2
      default_disposition_count_requires_completeness_check: 194
      unselected_timing_passages:
      - P1-S1-C14
      - P2-S2-C2
      - P5-S3-C10
      - P7-S1-C11
      - P7-S2-C4
      - P7-S2-C12
      - P8-S1-C6
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P4-S1-C14
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S3-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S3-C12
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S3-C13
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S3-C14
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C13
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S3-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P7-S2-C13
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: tested_personal_effects
        source_id: P3-S1-C10
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P4-S2-C7
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: eligibility
        source_ids:
        - P2-S1-C9
        - P2-S1-C12
        - P7-S1-C16
        - P7-S1-C17
        - P7-S1-C18
        - P7-S1-C19
        - P7-S1-C20
        - P7-S2-C4
        - P7-S2-C5
        - P7-S2-C6
        - P7-S2-C7
        - P7-S2-C8
        - P7-S2-C9
        - P7-S2-C10
        - P7-S2-C11
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: personal_factors
        source_ids:
        - P2-S1-C8
        - P3-S1-C10
        - P4-S1-C7
        - P4-S1-C10
        - P4-S2-C6
        - P4-S2-C7
        - P4-S2-C9
        - P6-S2-C5
        - P7-S1-C4
        - P7-S1-C8
        - P8-S4-C8
        - P8-S4-C9
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - eligibility
      - validation
      - analysis_restrictions
      - personal_factors
      - explicitly_not_adjusted
      unclassified_extraction_ids:
      - P5-S1-C13
      table_review_required:
      - TABLE-1-page-3-1
      - TABLE-2-page-6-2
      unlinked_tables: []
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P2-S2
        - P2-S3
        - P2-S4
        - P3-S1
        - P3-S2
        - P3-S3
        - P4-S1
        - P4-S2
        - P4-S3
        - P4-S4
        - P5-S1
        - P5-S3
        - P7-S1
        - P7-S3
        - P8-S3
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: dd2fb9fbb469ef382090372171f0fb42e0c4336fd5b0902af0605f2b4bff7356
      source_review: _compare/relationships-2026-11-16/review-current/Ramsey2017
      source_status_sha256: 4c5ae3a652cd3d15d7e37174bfe3fe8f69e82a987e011577f4a59c6b3248cc01
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C15
      disposition: represented
      result_indexes:
      - 0
      reason: Directly states impairment is described by clusters of correlated deficits.
    - source_id: P1-S1-C16
      disposition: represented
      result_indexes:
      - 1
      reason: Describes similarity of recovery across domains and timing.
    - source_id: P1-S1-C17
      disposition: represented
      result_indexes:
      - 2
      - 3
      - 4
      reason: Links specific white matter tracts to poor recovery in attention, language,
        and motor domains.
    - source_id: P1-S1-C18
      disposition: represented
      result_indexes:
      - 5
      - 6
      reason: Reports effects of education and multiple deficits on recovery after
        accounting for initial deficit.
    - source_id: P2-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive statistic of lesion volume range.
    - source_id: P2-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of Figure 1 lesion overlap.
    - source_id: P2-S2-C7
      disposition: represented
      result_indexes:
      - 7
      reason: Reports PCA variance and component loadings at two weeks.
    - source_id: P2-S2-C8
      disposition: represented
      result_indexes:
      - 7
      reason: Reports PCA variance and structure at three and twelve months.
    - source_id: P2-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: General observation of initial clusters.
    - source_id: P2-S2-C11
      disposition: represented
      result_indexes:
      - 8
      reason: States correlation between language and memory was similar across time
        points.
    - source_id: P2-S3-C2
      disposition: represented
      result_indexes:
      - 9
      reason: Reports loss of correlation between spatial memory, attention, and motor
        deficits over time.
    - source_id: P2-S3-C3
      disposition: represented
      result_indexes:
      - 9
      reason: Confirms weakened relationship of the spatial memory/motor/attention
        cluster at 12 months.
    - source_id: P2-S3-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Restatement of PCA results.
    - source_id: P2-S3-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison with prior NIH Stroke Scale studies.
    - source_id: P2-S3-C11
      disposition: represented
      result_indexes:
      - 10
      reason: States acute impairment predicts amount of recovery.
    - source_id: P2-S3-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Qualitative description of relative recovery.
    - source_id: P2-S3-C13
      disposition: represented
      result_indexes:
      - 10
      reason: Provides correlation coefficients for acute impairment and change in
        impairment.
    - source_id: P2-S4-C2
      disposition: represented
      result_indexes:
      - 10
      reason: Provides significance (P < 0.001) for acute impairment and change correlation.
    - source_id: P2-S4-C4
      disposition: represented
      result_indexes:
      - 11
      reason: Provides recovery ratios for language, spatial memory, and attention.
    - source_id: P2-S4-C5
      disposition: represented
      result_indexes:
      - 11
      reason: Provides recovery ratio for motor function.
    - source_id: P3-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: General summary of recovery similarity.
    - source_id: P3-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: General summary of recovery time course.
    - source_id: P3-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: General observation on complete recovery frequency.
    - source_id: P3-S1-C11
      disposition: represented
      result_indexes:
      - 14
      reason: Reports significance and variance explained by domain models.
    - source_id: P3-S1-C12
      disposition: represented
      result_indexes:
      - 14
      reason: Identifies sub-acute score as the strongest predictor.
    - source_id: P3-S1-C13
      disposition: represented
      result_indexes:
      - 15
      - 16
      reason: Identifies lesion size and education as predictors for language and
        spatial memory.
    - source_id: P3-S2-C2
      disposition: represented
      result_indexes:
      - 12
      reason: Reports null result for differences between domains in recovery ratios.
    - source_id: P3-S2-C3
      disposition: represented
      result_indexes:
      - 13
      reason: Reports significant difference in recovery to normal range for motor
        vs others.
    - source_id: P3-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement on time course similarity.
    - source_id: P3-S2-C6
      disposition: represented
      result_indexes:
      - 17
      reason: Reports significant interaction between deficit/no-deficit groups over
        time.
    - source_id: P3-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Qualitative description of late improvements.
    - source_id: P3-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation that differences remained significant at 12 months.
    - source_id: P3-S2-C10
      disposition: represented
      result_indexes:
      - 17
      reason: Reports ANOVA main effect of time and lack of domain interaction.
    - source_id: P4-S1-C4
      disposition: represented
      result_indexes:
      - 18
      reason: Reports non-significance of age and therapy in models.
    - source_id: P4-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive distribution of deficits.
    - source_id: P4-S1-C9
      disposition: represented
      result_indexes:
      - 19
      - 20
      reason: Reports negative interaction of multiple deficits with attention and
        spatial memory.
    - source_id: P4-S1-C10
      disposition: represented
      result_indexes:
      - 21
      reason: Reports main effect of multiple deficits on language deficit magnitude.
    - source_id: P4-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: General observation that multiple deficits only affected cognitive domains.
    - source_id: P4-S1-C12
      disposition: represented
      result_indexes:
      - 22
      reason: Reports lack of interaction effects for motor deficits.
    - source_id: P4-S1-C14
      disposition: represented
      result_indexes:
      - 23
      reason: Reports attention as a moderator for language recovery.
    - source_id: P4-S2-C2
      disposition: represented
      result_indexes:
      - 23
      - 24
      reason: Reports significant interactions between language, attention, spatial
        memory, and motor function.
    - source_id: P4-S2-C3
      disposition: represented
      result_indexes:
      - 24
      reason: Reports unidirectional influence of language on verbal memory and motor
        on attention.
    - source_id: P4-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: General summary of moderation effects.
    - source_id: P4-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: General summary of lack of moderation in cognitive cluster.
    - source_id: P4-S3-C6
      disposition: represented
      result_indexes:
      - 25
      reason: Reports improvement in language prediction using unflipped components.
    - source_id: P4-S3-C8
      disposition: represented
      result_indexes:
      - 26
      reason: Links specific lesion locations (frontal vs temporo-parietal-occipital)
        to language outcomes.
    - source_id: P4-S3-C11
      disposition: represented
      result_indexes:
      - 27
      reason: Links specific white matter tracts to poor language outcome.
    - source_id: P4-S3-C12
      disposition: represented
      result_indexes:
      - 28
      - 29
      reason: Reports improved prediction of motor and attention scores using flipped
        lesions.
    - source_id: P4-S3-C13
      disposition: represented
      result_indexes:
      - 28
      reason: Links dorsal CST damage to worse motor outcomes.
    - source_id: P4-S3-C15
      disposition: represented
      result_indexes:
      - 30
      reason: Links isolated cortical motor/sensory damage to good outcomes.
    - source_id: P5-S1-C3
      disposition: represented
      result_indexes:
      - 29
      reason: Links specific white matter and cortical lesions to worse attention
        recovery.
    - source_id: P5-S1-C4
      disposition: represented
      result_indexes:
      - 29
      reason: Links SLF II, III and arcuate fasciculus to attention recovery.
    - source_id: P5-S1-C5
      disposition: represented
      result_indexes:
      - 31
      reason: Reports no predictive effect of lesion topography on memory outcome.
    - source_id: P5-S1-C9
      disposition: represented
      result_indexes:
      - 32
      reason: Reports positive association between white matter damage and poor outcomes
        for language, attention, and motor function.
    - source_id: P6-S1-C13
      disposition: represented
      result_indexes:
      - 32
      reason: Restates white matter damage variance in recovery of language, attention,
        and motor function.
    - source_id: P7-S1-C4
      disposition: represented
      result_indexes:
      - 33
      reason: Reports no relationship between recovery and age in this sample.
    - source_id: P8-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of within-domain PCA results.
    - source_id: P8-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of attention domain PCA.
    - source_id: P8-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of attention domain PCA.
    - source_id: P8-S2-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of attention domain PCA.
    - source_id: P8-S2-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of motor PCA.
    - source_id: P8-S2-C16
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of rotation choice for PCA.
    - source_id: P8-S3-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of correlation method validation.
    unresolved_coverage:
    - source_id: P4-S2-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P4-S2-C12
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P4-S3-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P4-S3-C14
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P5-S1-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P5-S1-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P5-S2-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P5-S2-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P5-S3-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P5-S3-C13
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P6-S1-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P6-S1-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P6-S2-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P6-S2-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P6-S2-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P7-S1-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P7-S1-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S2-C17
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P2-S2-C3
    - P2-S2-C4
    - P2-S2-C10
    - P2-S3-C4
    - P2-S3-C5
    - P2-S3-C12
    - P2-S3-C13
    - P3-S1-C3
    - P3-S1-C5
    - P3-S1-C6
    - P3-S2-C4
    - P3-S2-C7
    - P3-S2-C8
    - P4-S1-C6
    - P4-S1-C11
    - P4-S2-C4
    - P4-S2-C5
    - P4-S2-C6
    - P4-S2-C12
    - P4-S3-C3
    - P4-S3-C14
    - P5-S1-C6
    - P5-S1-C7
    - P5-S2-C2
    - P5-S2-C7
    - P5-S3-C11
    - P5-S3-C13
    - P6-S1-C6
    - P6-S1-C7
    - P6-S2-C2
    - P6-S2-C4
    - P6-S2-C5
    - P7-S1-C6
    - P7-S1-C8
    - P8-S2-C8
    - P8-S2-C9
    - P8-S2-C10
    - P8-S2-C11
    - P8-S2-C13
    - P8-S2-C16
    - P8-S2-C17
    - P8-S3-C3
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-3-1
    - TABLE-2-page-6-2
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P2-S2-C2
      recruited_sample:
      - P2-S1-C9
      - P7-S1-C10
      eligibility: []
      imaging_provenance:
      - P2-S1-C11
      - P8-S1-C15
      imaging_timing:
      - P2-S1-C10
      - P8-S1-C4
      outcome_timing:
      - P2-S1-C10
      - P8-S1-C4
      outcome_definition:
      - P2-S4-C3
      - P8-S3-C10
      validation: []
      analysis_restrictions: []
      dependent_variable_statement:
      - P3-S1-C10
      - P4-S1-C8
      - P4-S2-C9
      - P8-S4-C9
      limitations:
      - P6-S2-C6
      - P6-S2-C12
      - P6-S2-C13
      - P7-S1-C3
      - P7-S1-C4
      - P7-S1-C5
      personal_factors: []
      tested_personal_effects:
      - P4-S1-C10
      - P4-S2-C6
      - P6-S2-C5
      - P7-S1-C8
      adjustment_roles:
      - P3-S1-C10
      - P4-S1-C7
      - P4-S1-C10
      - P4-S2-C9
      - P6-S3-C3
      - P8-S4-C9
      - P8-S5-C8
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P2-S1-C8
      - P2-S2-C2
      - P7-S1-C3
    outcome_type: both_reported
    imaging_vs_outcome: mixed
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P4-S1-C14
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S3-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S3-C12
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S3-C13
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S3-C14
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C13
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S3-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P7-S2-C13
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: tested_personal_effects
      source_id: P3-S1-C10
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P4-S2-C7
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: eligibility
      source_ids:
      - P2-S1-C9
      - P2-S1-C12
      - P7-S1-C16
      - P7-S1-C17
      - P7-S1-C18
      - P7-S1-C19
      - P7-S1-C20
      - P7-S2-C4
      - P7-S2-C5
      - P7-S2-C6
      - P7-S2-C7
      - P7-S2-C8
      - P7-S2-C9
      - P7-S2-C10
      - P7-S2-C11
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: personal_factors
      source_ids:
      - P2-S1-C8
      - P3-S1-C10
      - P4-S1-C7
      - P4-S1-C10
      - P4-S2-C6
      - P4-S2-C7
      - P4-S2-C9
      - P6-S2-C5
      - P7-S1-C4
      - P7-S1-C8
      - P8-S4-C8
      - P8-S4-C9
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
      pdf_sha256: dd2fb9fbb469ef382090372171f0fb42e0c4336fd5b0902af0605f2b4bff7356
      review_sha256: c36a88e587d223852996450f88f386b2a0bfdfc53fb0255f3b3c0ebc6cd974f0
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
      - P1-S1-C18
      source_result: After accounting for the severity of the initial deficit, the
        occurrence of multiple deficits negatively impacted attention recovery.
      result_status: detected
      patient_measurement: non_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The source (P1-S1-C18) describes the result of a model where multiple
            deficits predict attention recovery. The proposed core correctly identifies
            this as the analysis of interest, distinguishing it from the lesion topography
            analysis (P1-S1-C17) or the education analysis. The method is a regression/moderation
            analysis (P8-S4-C12, P8-S5-C4) predicting chronic scores from sub-acute
            scores and covariates.
          source_ids:
          - P1-S1-C18
          - P8-S4-C12
          - P8-S5-C4
        direction:
          answer: fits
          reason: The source states that multiple deficits 'negatively impacted' attention
            recovery. The proposed core uses the direction 'unlikely' (implying lower
            recovery/prognosis) which aligns with the negative impact described. The
            claim text explicitly preserves the 'negative' direction.
          source_ids:
          - P1-S1-C18
        construct:
          answer: fits
          reason: Exposure is 'occurrence of multiple deficits' (number of domains
            with impairment). Outcome is 'attention recovery' (change in attention
            scores). The measurement is behavioral (neuropsychological tests), not
            imaging-based. The source confirms attention was measured via behavioral
            tests (P8-S1-C12) and deficits were defined by behavioral scores (P8-S3-C12).
          source_ids:
          - P1-S1-C18
          - P8-S1-C12
          - P8-S3-C12
        qualifications:
          answer: fits
          reason: The source explicitly states 'after accounting for the severity
            of the initial deficit' (P1-S1-C18). The proposed core includes this as
            a qualification. It also lists other covariates (education, age, therapy,
            lesion size) which are mentioned in the methods (P4-S1-C7, P8-S4-C14)
            as part of the model structure, though the abstract highlights the initial
            deficit adjustment specifically for this finding. The core correctly frames
            these as adjustments.
          source_ids:
          - P1-S1-C18
          - P4-S1-C7
          - P8-S4-C14
        missing_material_caveat:
          answer: fits
          reason: The core includes the key limitation regarding the behavioral battery's
            trade-off (P6-S2-C12, P6-S2-C13). It does not omit the fact that this
            is a specific domain (attention) result, distinct from the language/visual
            memory results mentioned in the same sentence. The 'unlikely' direction
            captures the negative impact. No material caveat changing the interpretation
            of the association is missing.
          source_ids:
          - P6-S2-C12
          - P6-S2-C13
      optional_pending:
      - Sample size for the specific moderation analysis (n=43 mentioned in P8-S5-C4)
        is not transcribed in the core fields, but the general cohort size is available
        in source.
      - Specific statistical values (beta, p-value) for the multiple deficits effect
        are not transcribed.
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Sample size requires source confirmation; it has not been transcribed.
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Sample size for the specific moderation analysis (n=43 mentioned in P8-S5-C4)
      is not transcribed in the core fields, but the general cohort size is available
      in source.
    - Specific statistical values (beta, p-value) for the multiple deficits effect
      are not transcribed.
    normalizations:
    - field: sample.n
      original: 132
      action: not_transcribed
      reason: Not supported by selected quotations
    analysis_identity:
      id: R007
      exposure:
        text: occurrence of multiple deficits
      outcome:
        text: attention recovery
      analysis_label: Personal factors and recovery (adjusted)
      relation: sensitivity
      evidence_ids:
      - P1-S1-C18
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
        pdf_sha256: dd2fb9fbb469ef382090372171f0fb42e0c4336fd5b0902af0605f2b4bff7356
        source_review: _compare/relationships-2026-11-16/review-current/Ramsey2017
        source_status_sha256: 4c5ae3a652cd3d15d7e37174bfe3fe8f69e82a987e011577f4a59c6b3248cc01
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P2-S1-C9:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: dd2fb9fbb469ef382090372171f0fb42e0c4336fd5b0902af0605f2b4bff7356
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 13ae64d60035cafc536c854933dbed07b1e63b9f741093dee9ff74edd15e18c1
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S1-C9
          page: 2
          text_layer_sha256: 13ae64d60035cafc536c854933dbed07b1e63b9f741093dee9ff74edd15e18c1
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: "Results\nSubjects (n =​ 172) with a first symptomatic stroke\
          \ anywhere in the \nbrain and clinical evidence of any neurological impairment\
          \ were pro­\nspectively recruited, with n =​ 132 meeting post-enrolment\
          \ inclusion \ncriteria."
        anchor_text: "Results\nSubjects (n =​ 172) with a first symptomatic stroke\
          \ anywhere in the \nbrain and clinical evidence of any neurological impairment\
          \ were pro­\nspectively recruited, with n =​ 132 meeting post-enrolment\
          \ inclusion \ncriteria."
        excluded_fragments: []
        image_sha256: e0cd3143b5609aca98d5f7f9ac994b0dafd870a20c38876482fc272a8e8e3f06
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 1
  quote: "Finally, after accounting for the severity of the initial deficit, language\
    \ and visual memory \nrecovery was worse for those with lower levels of education,\
    \ while the occurrence of multiple deficits negatively impacted \nattention recovery."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-25'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
