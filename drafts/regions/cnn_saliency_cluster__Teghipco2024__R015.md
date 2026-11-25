---
id: cnn_saliency_cluster
name: CNN saliency cluster
kind: network
findings:
- id: f1
  target: lesion_size
  target_kind: impairment
  claim: Patient subgroups identified by CNN saliency map clustering were not associated
    with lesion size.
  direction: no_effect
  relationship: correlational
  method: MVPA
  sample:
    n: not_reported
    population: individuals with chronic left strokes
    phase: not_reported
    time_post_onset: mean 3.2 +/- 3.7 years post-stroke
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - imaging data was downsampled to 8 mm voxel size
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Patient subgroups identified by consensus clustering
    of Grad-CAM++ feature saliency maps generated from a 3D CNN trained to predict
    severe aphasia using whole-brain morphometry and lesion anatomy. subgroups were
    analyzed separately for severe and non-severe aphasia predictions. Additional
    metadata has not been transcribed; review the pending-field flags before approval.
    PDF image reading (P2-S4-C9, two-model agreement, human verification pending):
    Methods

    Participants

    Two-hundred and thirteen individuals (age = 57.98 +/- 11.34, 62% male) with chronic
    left strokes (mean years post-stroke = 3.2 +/- 3.7) that participated in studies
    conducted at the Center for the Study of Aphasia Recovery (C-STAR) were analyzed
    retrospectively in the present work Original text-layer quotation is preserved
    below.'
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
    - proposed_concept:lesion_size
  citation: '@Teghipco2024'
  source_passages:
  - section: Original source P10-S2-C6
    page: 10
    quote: 'Finally, we found that patient subgroups were not associated with

      lesion size, as hinted by the lesion outlines in Figs. 9 and 10.'
    supports: claim
  - section: Original source P2-S4-C9
    page: 2
    quote: 'Methods

      Participants

      Two-hundred and thirteen individuals (age = 57.98 +/−11.34, 62% male)

      with chronic left strokes (mean years post-stroke = 3.2 +/−3.7) that par-

      ticipated in studies conducted at the Center for the Study of Aphasia

      Recovery (C-STAR) were analyzed retrospectively in the present work.'
    supports: sample
  - section: Original source P6-S1-C12
    page: 6
    quote: 'Subtyping distinct brain patterns through deep learning

      Unsupervised learning of Grad-CAM++ maps was used to explore the

      heterogeneity of brain patterns learned by the CNN.'
    supports: method
  - section: Original source P14-S3-C5
    page: 14
    quote: 'An important caveat to the results we present is that our data was

      downsampled to a lower resolution than typical to many neuroimaging

      analyses to make deep learning with nested cross-validation tractable.'
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-25'
relationship_review:
  paper: Teghipco2024
  proposal_id: R015
  review_status_sha256: 8d7a558e52be5e3f0e45ec8e054dd1acdc5ec2f388b22878efa73fb39271f0a0
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 68f566e52924f65d6d4df2e0ebeb371b036a1588ed2e049de3bacdd06a582486
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 68f566e52924f65d6d4df2e0ebeb371b036a1588ed2e049de3bacdd06a582486
        A/passages.json: c06cfbc3bb3352b657053369ea37a612b9b24933327720f37964abda6e5115b5
        A/raw.json: cf87b2f3c698298c2bf4e8eb5c85dbcb46c290bb5f5f6be292f35343d8b473f4
        A/source-units.json: 2631cbc5d79eb889a1c2263c29f1f7657545f872336b99274ec09c1da7525cdc
        A/full-source-units.json: b11082cc481e9d55d6e549d25a79b7fddf37bc2c8eef78fcbaed500f6d560874
        A/meta.json: 5196318206734bd688ad3310f41d15f10b952be258fc2bff73a0d34c3a9a74fd
        A/table-images/manifest.json: e815aec10b7790e6aed35caa1115821f9159e2228d275573e66bd61ba0f30528
        A/clauses/window-11/raw.json: ce2f2a9b49e8b855ccfe3e03ec35deacf2c9245962e711b69e42190af6de04df
        A/clauses/window-11/prompt.txt: 512522dd3cbb91d378d8966c47cc4778cecdd50b67231f9887179d8213ce61cc
        A/clauses/window-11/meta.json: a5f501ba03573b8e7f01f6561e41b41c54c6e185c748a1dd08aba6002f837b01
        A/clauses/window-10/raw.json: ff9aae52c38968db455bc01d542ef8395fc97a2ef9dbc02b510d2d309b4b0b4f
        A/clauses/window-10/prompt.txt: f575bb923f692e367762bf655e57b599636dec4c6fd53c6dbc5b5e913e0575ac
        A/clauses/window-10/meta.json: a90f23277e27c0807b2bf4adf1fb648cf706dd79c821a6adf67c486205b05e9d
        A/clauses/window-03/raw.json: 8a88c4942ac7ed02d4b9e33d90e645de3bd6321e35918e67fbb33a20fbeca439
        A/clauses/window-03/prompt.txt: 359ba5a6a9128beb6330ed0875144b7bf291d24680361d765348082e8828ab52
        A/clauses/window-03/meta.json: 161adfc4e33fdba0f585a0f9d485c3b0a44f32f968a87fcc20b4e9226836ad71
        A/clauses/window-04/raw.json: eaeb1ad05bfabb9bd016eb378cf3e528de1a9edc526245dad23f9ffdf95a899e
        A/clauses/window-04/prompt.txt: 7a1d15944c999737e26f3c9802536d6ceb07a17ac1bf7c94323a886c4a9e68bd
        A/clauses/window-04/meta.json: a060675d22b24808494d7e46149a9843ea2ecf3f1adfddc49db80cc0654549ec
        A/clauses/window-05/raw.json: d3c74da1bd98985ed0b24e396f204d18cef2701d5a6862a127b27a81396f1bb0
        A/clauses/window-05/prompt.txt: 2cd809aa2a16dfe5a499c4ec4faa8c0c7f85ceb73963abb01cca740d13b11c7c
        A/clauses/window-05/meta.json: 80286123e656706ffd3637d8b45f44fbdb55898483a4dfb9d48bab385ca81f4d
        A/clauses/window-02/raw.json: 7b72c3d13974b5d4b7a33cf911b303d4643bd208d8f98eff8417c0a9a0dc9d3b
        A/clauses/window-02/prompt.txt: 2ec18f1d2394850a8507ecfa0419b68ea4ada10578f789c34c99e92bbcb41383
        A/clauses/window-02/meta.json: 0573f8c26f791e9049dc1eeb5a079fc027d25b40de5715692b1dfdfa163d441a
        A/clauses/window-15/raw.json: 671bab39181210c7355808c57da6247dccba8f7ab3b0d484c728d4a70f345307
        A/clauses/window-15/prompt.txt: 6fc36bd7587e3ec5b8e3f9c0b81073a0c4b03a0aac64252c2674978d3fad1cfd
        A/clauses/window-15/meta.json: 8c17b51ba54b057df8f78e36ee366be1bb6d616695ad2983dfb900a2639332a0
        A/clauses/window-12/raw.json: e78d5bde00c51de2dedd87002276702d3a7cae3ebd07db23fece18a7f21d0e48
        A/clauses/window-12/prompt.txt: 9681155bd67c550f8c215760a45f145f5dc7e0dfca9a2acacc5f4997f67c4e08
        A/clauses/window-12/meta.json: 72d33441b3ea0572b3f0f8c4ae4ec82cd625c3b0dbd1e48f6b8ef8b865254822
        A/clauses/window-13/raw.json: 67d0f1e025cf4a1c22119d49e93558bbdecad802ff8ea278482d74928537d3a6
        A/clauses/window-13/prompt.txt: cb5fc11a2183db525246fb245d34292535b64ff82274348871b8b1b01de1deaf
        A/clauses/window-13/meta.json: b96ceb33a99ac7b7e9dfa0990ffc2ded51e4c0edf2bc11c73b51a7fe35f6fef2
        A/clauses/window-14/raw.json: 7984b7a49c9121e102c927d7d2971804ff01e594a78e6c3ae4452082b42a270f
        A/clauses/window-14/prompt.txt: a631b63008961d2d52e7f06807cbbf46f860cb5389d043cd9a47e7154274e2d6
        A/clauses/window-14/meta.json: 0b8f30d2b654097ee1e338211714ab5377444ba6259b58f20c030315dc436c88
        A/clauses/window-09/raw.json: ea3bca0a42693391ebf8373a430509c256fdb31cefdc7bbc82a7bc77473890cf
        A/clauses/window-09/prompt.txt: 0f06f7bda51528383e0180595260149a4e805ffe7b908f71ea558bbedef5c87d
        A/clauses/window-09/meta.json: 9b8a3b8753a0900c07abb5869369059a06a29c7ba68e848f3fb2d2b77c00ae31
        A/clauses/window-07/raw.json: 5e274cd4643c85479711f720878138dec78f00c8faef5c1a1ace5af5752c51e7
        A/clauses/window-07/prompt.txt: 71f61c30165e5cfda5ce9f05f30f2bd9fdb392f5449c9756bd998daef2ca3652
        A/clauses/window-07/meta.json: 6169b59458ae496dd1ab355aec4f18a1ec63a57c3a303fded1c57a30c8613a5c
        A/clauses/window-01/raw.json: 1d31aaf24b8036047ad77970aba3a6ed94a27fdc45fda634c4b3cbe3a7f29f47
        A/clauses/window-01/prompt.txt: babb14f1c7009ffe6826084bda0a075f1950cd712dc71adc96ad5484142fb79b
        A/clauses/window-01/meta.json: bb42e0b2598a98f11244e642e139c4d88b8b7eee5316d2a7100c839f2a5e6550
        A/clauses/window-06/raw.json: cbfc6c2db3a9bf18128f132250910ae553149fc41fe41699e56bb79678072631
        A/clauses/window-06/prompt.txt: 6c98a32c79a6bb94dd9af387ddb75c6927ded0c536e003a15ba49f1656343f05
        A/clauses/window-06/meta.json: bf1a01a7e587bda45d8dc967193ce4dde46d2a7cee9bae022d1f86f637a6c870
        A/clauses/window-08/raw.json: 175aa0ae3a9999ea7253e173969acc5b5c99357492c4eed7853531a4ff91b290
        A/clauses/window-08/prompt.txt: 113748b6319f625fbb477213926ca75376f671f8e06353c23105cde8568b04d5
        A/clauses/window-08/meta.json: 5bc9513525b3c04bf3de64b5ce7c3e3d71885377b7e63227480b6b37e6958223
        B/passages.json: c06cfbc3bb3352b657053369ea37a612b9b24933327720f37964abda6e5115b5
        B/raw.json: 0c880d1ba17ff50d0b12f5ccc45f0cee57d4797c7736d3dc1c23947f3ed214bf
        B/source-units.json: 2631cbc5d79eb889a1c2263c29f1f7657545f872336b99274ec09c1da7525cdc
        B/full-source-units.json: b11082cc481e9d55d6e549d25a79b7fddf37bc2c8eef78fcbaed500f6d560874
        B/meta.json: cf52c9db88db536a731a06c144eb506595c4a8532d31b6ed5d67fd925a2210c5
        B/table-images/manifest.json: e815aec10b7790e6aed35caa1115821f9159e2228d275573e66bd61ba0f30528
        B/clauses/window-11/raw.json: 64c7fe1c85b4a5c8017e2219f155b55fa1307049aa70fdb1a27c2ff5fffe22d7
        B/clauses/window-11/prompt.txt: 512522dd3cbb91d378d8966c47cc4778cecdd50b67231f9887179d8213ce61cc
        B/clauses/window-11/meta.json: 65a1c87864a40185c715a11780c32832488123fd5688358a684e395c84e4b3e5
        B/clauses/window-10/raw.json: 6c5a04c3b4d8c2b4b303db510f3a475a3bfa9d56157dd247a38a8b4a18ae9366
        B/clauses/window-10/prompt.txt: f575bb923f692e367762bf655e57b599636dec4c6fd53c6dbc5b5e913e0575ac
        B/clauses/window-10/meta.json: 84c99a8d7590b85c10a902b876541ca5176fd19b43cf599fab5e169c74c7a564
        B/clauses/window-03/raw.json: 0162dbe3990c6c51f449c34bdd5879bc71336d9fb40523df044121f42e0da01b
        B/clauses/window-03/prompt.txt: 359ba5a6a9128beb6330ed0875144b7bf291d24680361d765348082e8828ab52
        B/clauses/window-03/meta.json: a6b64d63d4146b5352a6bcc31a45411077ca483cc2fc555e6ab9f99477551142
        B/clauses/window-04/raw.json: 156574b436ca76e052d25f258e03c312bf46cc12ed69a9b8bd13b6c24d4347ee
        B/clauses/window-04/prompt.txt: 7a1d15944c999737e26f3c9802536d6ceb07a17ac1bf7c94323a886c4a9e68bd
        B/clauses/window-04/meta.json: 170d16b9b5662e8f65e5d8664697dbfd55b794869a56b009af526d564e139b43
        B/clauses/window-05/raw.json: bb2b4b935c2882405ff9ea7468c8b4bac2c5725ded2a6275d7a1f5d6b7eca83e
        B/clauses/window-05/prompt.txt: 2cd809aa2a16dfe5a499c4ec4faa8c0c7f85ceb73963abb01cca740d13b11c7c
        B/clauses/window-05/meta.json: f6e56e3da6eacfe0d56b7e15b2b58f5e473a014658ef15b59bb87e848ed78092
        B/clauses/window-02/raw.json: 59e7a1157712aa3113f613036b0440078dea1f5a5b451dbf67a628c12ccccbe7
        B/clauses/window-02/prompt.txt: 2ec18f1d2394850a8507ecfa0419b68ea4ada10578f789c34c99e92bbcb41383
        B/clauses/window-02/meta.json: 7f4568540b08c60aa6df584c5204126ec4a5fa2d247898cef03abe26e3f6525e
        B/clauses/window-15/raw.json: 4e0d7d61296eb428d20ce992b64bcd347d238347c021266780d0483557515d4f
        B/clauses/window-15/prompt.txt: 6fc36bd7587e3ec5b8e3f9c0b81073a0c4b03a0aac64252c2674978d3fad1cfd
        B/clauses/window-15/meta.json: ea6045a3128cf4f8aa5f09eda503d8ce7efdba4142ff9c45e604187d67bed829
        B/clauses/window-12/raw.json: f9c17fbcdaaa7759ad62a2d374a6401b79cc8cceb9a6a1b3321c2a388646954c
        B/clauses/window-12/prompt.txt: 9681155bd67c550f8c215760a45f145f5dc7e0dfca9a2acacc5f4997f67c4e08
        B/clauses/window-12/meta.json: 86a42a052591e98a76a71ded9cbe97f43c7ee6a8c170ab88d624e16c1ee943e2
        B/clauses/window-13/raw.json: 88ddb683e89a5b9b2956b4fd50055ba15c3b90e68d40d7932634c462de306f48
        B/clauses/window-13/prompt.txt: cb5fc11a2183db525246fb245d34292535b64ff82274348871b8b1b01de1deaf
        B/clauses/window-13/meta.json: 253016e93c59db38d64004e1e2e051b6d02badf484c2e64bdc571e97535a255f
        B/clauses/window-14/raw.json: 57fd6c28e74ee8ac74098c94f1086c474df4a3e1bacbde5e9702bb79c4258b66
        B/clauses/window-14/prompt.txt: a631b63008961d2d52e7f06807cbbf46f860cb5389d043cd9a47e7154274e2d6
        B/clauses/window-14/meta.json: 7a306bd456d7e974e79de2e6bea9a47faf6ee81bbbb4c982054ec015332eca15
        B/clauses/window-09/raw.json: 6e52ddd8cdedca9452a69968622a33f06d4b58b7f8e0fa511011f00972e8df73
        B/clauses/window-09/prompt.txt: 0f06f7bda51528383e0180595260149a4e805ffe7b908f71ea558bbedef5c87d
        B/clauses/window-09/meta.json: e43483b1a6ff540ed332660f23b5a3673a01aaa25641661e238312aa40443d8f
        B/clauses/window-07/raw.json: 2d15fa3ae61befee4ffebfe96bedbc83d22181f9d437d141cfd61eb7c1f9b782
        B/clauses/window-07/prompt.txt: 71f61c30165e5cfda5ce9f05f30f2bd9fdb392f5449c9756bd998daef2ca3652
        B/clauses/window-07/meta.json: 69edded4ef7d4f80891ee04b4a81c534cb4c60d25a9991f80165435f47017c14
        B/clauses/window-01/raw.json: 74f46a2d1d7ce9c54d7518ff4eca4a0490582b25bd3f3d907eafc5e6f866ca3d
        B/clauses/window-01/prompt.txt: babb14f1c7009ffe6826084bda0a075f1950cd712dc71adc96ad5484142fb79b
        B/clauses/window-01/meta.json: 7197aab25d60f30713364c74accc66da2969e501c4b293600a40799240e10196
        B/clauses/window-06/raw.json: 09bebd26ea4eff5478bea0419bdcdbd05465e12e8b89969cfe5a335a645f4a7e
        B/clauses/window-06/prompt.txt: 6c98a32c79a6bb94dd9af387ddb75c6927ded0c536e003a15ba49f1656343f05
        B/clauses/window-06/meta.json: 491eef951140a4520247e5d915dedde966220ba13a74d206575336bf9e76e93f
        B/clauses/window-08/raw.json: 2515e4361758dc11c794c7878d7dbcf83e0cafe5260de4ad7be207b02cf45095
        B/clauses/window-08/prompt.txt: 113748b6319f625fbb477213926ca75376f671f8e06353c23105cde8568b04d5
        B/clauses/window-08/meta.json: d114124c8f0d2bc6d48edd579c3f972a3a993789a0f3b09dc8c71937afbd8d7f
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
      pdf_sha256: 68f566e52924f65d6d4df2e0ebeb371b036a1588ed2e049de3bacdd06a582486
      source_review: _compare/relationships-2026-11-16/review-current/Teghipco2024
      source_status_sha256: a66d207d1868c70d5cc8a5a7f906ef8735578b25ffbd7dd4f807506d98abc295
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R015
    exposure:
      text: CNN saliency clusters
    outcome:
      text: lesion size
    analysis_label: Subgroup morphometry vs lesion size
    relation: association
    evidence_ids:
    - P10-S2-C6
    - P13-S2-C11
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
      pdf_sha256: 68f566e52924f65d6d4df2e0ebeb371b036a1588ed2e049de3bacdd06a582486
      source_review: _compare/relationships-2026-11-16/review-current/Teghipco2024
      source_status_sha256: a66d207d1868c70d5cc8a5a7f906ef8735578b25ffbd7dd4f807506d98abc295
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P1-S1-C5
      - Result passage disposed without unit P1-S1-C6
      - Result passage disposed without unit P1-S1-C7
      - Result passage disposed without unit P1-S1-C8
      - Result passage disposed without unit P1-S1-C9
      - Result passage disposed without unit P1-S2-C8
      - Result passage disposed without unit P1-S2-C9
      - Accounting without a linked unit P2-S4-C5
      - Accounting without a linked unit P2-S4-C6
      - Accounting without a linked unit P2-S4-C7
      - Unaccounted source passage P2-S4-C7
      - Unaccounted source passage P2-S4-C6
      - Unaccounted source passage P2-S4-C5
      - Accounting without a linked unit P5-S1-C9
      - Unaccounted source passage P5-S1-C9
      - Accounting without a linked unit P6-S4-C2
      - Accounting without a linked unit P6-S4-C3
      - Accounting without a linked unit P6-S4-C4
      - Accounting without a linked unit P6-S4-C5
      - Unaccounted source passage P6-S4-C5
      - Unaccounted source passage P6-S4-C3
      - Unaccounted source passage P6-S4-C2
      - Unaccounted source passage P6-S4-C4
      - Result passage disposed without unit P7-S1-C11
      - Accounting without a linked unit P7-S1-C12
      - 'window 7: invalid/duplicate disposition P7-S1-C5'
      - Result passage disposed without unit P7-S1-C6
      - Accounting without a linked unit P7-S1-C7
      - Accounting without a linked unit P7-S1-C8
      - Accounting without a linked unit P7-S2-C2
      - Unaccounted source passage P7-S1-C12
      - Unaccounted source passage P7-S2-C2
      - Unaccounted source passage P7-S1-C8
      - Unaccounted source passage P7-S1-C7
      - Result passage disposed without unit P8-S1-C1
      - Result passage disposed without unit P8-S1-C2
      - Result passage disposed without unit P10-S1-C2
      - Result passage disposed without unit P10-S1-C3
      - Result passage disposed without unit P10-S1-C4
      - Accounting without a linked unit P9-S1-C10
      - Accounting without a linked unit P9-S2-C3
      - Unaccounted source passage P9-S2-C3
      - Unaccounted source passage P9-S1-C10
      - Result passage disposed without unit P10-S2-C6
      - Result passage disposed without unit P11-S1-C1
      - Result passage disposed without unit P11-S1-C2
      - Result passage disposed without unit P11-S1-C4
      - Result passage disposed without unit P11-S1-C11
      - Result passage disposed without unit P11-S1-C5
      - Result passage disposed without unit P11-S1-C6
      - Result passage disposed without unit P11-S1-C7
      - Result passage disposed without unit P11-S1-C8
      - Result passage disposed without unit P11-S2-C1
      - Result passage disposed without unit P12-S1-C2
      - Result passage disposed without unit P12-S2-C3
      - Result passage disposed without unit P12-S2-C4
      - Result passage disposed without unit P12-S2-C5
      - Result passage disposed without unit P12-S2-C11
      - Result passage disposed without unit P13-S1-C1
      - Result passage disposed without unit P14-S1-C3
      - Result passage disposed without unit P14-S1-C4
      - Result passage disposed without unit P14-S1-C5
      - Result passage disposed without unit P14-S1-C7
      - Result passage disposed without unit P14-S2-C3
      - Result passage disposed without unit P14-S2-C6
      unattached_null_or_qualifier_ids:
      - P1-S1-C6
      - P7-S1-C12
      - P7-S2-C2
      - P11-S1-C6
      - P11-S2-C3
      - P12-S2-C3
      - P14-S1-C3
      - P14-S2-C3
      - P14-S3-C9
      suppressed_nonrepresented_units: 58
      default_disposition_count_requires_completeness_check: 301
      unselected_timing_passages:
      - P2-S4-C9
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P5-S1-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S4-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S1-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S1-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S1-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S1-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S1-C12
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P4-S2-C4
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P7-S1-C10
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P8-S1-C1
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P8-S1-C10
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P9-S1-C1
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P9-S1-C5
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P11-S1-C1
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: adjustment_roles
        source_ids:
        - P4-S1-C10
        - P5-S1-C10
        - P5-S1-C11
        - P7-S1-C10
        - P7-S1-C11
        - P7-S1-C12
        - P8-S1-C10
        - P8-S1-C1
        - P9-S1-C5
        - P10-S1-C11
        - P11-S1-C1
        - P11-S1-C2
        - P12-S1-C11
        - P13-S1-C12
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - personal_factors
      - tested_personal_effects
      - adjustment_roles
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required: []
      unlinked_tables: []
      source_anomalies:
      - evidence_id: P7-S1-C7
        as_printed: p = 5.26
        reason: Printed p-value outside [0,1]; verify PDF, never correct automatically
      - evidence_id: P7-S1-C8
        as_printed: p = 7.28
        reason: Printed p-value outside [0,1]; verify PDF, never correct automatically
      - evidence_id: P8-S3-C2
        as_printed: p = 6.55
        reason: Printed p-value outside [0,1]; verify PDF, never correct automatically
      - evidence_id: P8-S3-C2
        as_printed: p = 2.49
        reason: Printed p-value outside [0,1]; verify PDF, never correct automatically
      - evidence_id: P9-S1-C4
        as_printed: p = 9.25
        reason: Printed p-value outside [0,1]; verify PDF, never correct automatically
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P3-S1
        - P4-S1
        - P4-S4
        - P4-S5
        - P5-S1
        - P5-S3
        - P6-S4
        - P6-S5
        - P7-S1
        - P7-S2
        - P8-S1
        - P8-S2
        - P8-S3
        - P8-S4
        - P9-S1
        - P9-S2
        - P9-S3
        - P10-S1
        - P10-S2
        - P10-S3
        - P11-S2
        - P12-S1
        - P12-S2
        - P13-S2
        - P14-S4
        - P14-S5
        - P15-S1
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 68f566e52924f65d6d4df2e0ebeb371b036a1588ed2e049de3bacdd06a582486
      source_review: _compare/relationships-2026-11-16/review-current/Teghipco2024
      source_status_sha256: a66d207d1868c70d5cc8a5a7f906ef8735578b25ffbd7dd4f807506d98abc295
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C5
      disposition: represented
      result_indexes:
      - 1
      reason: CNNs achieve higher balanced accuracy and F1 scores than SVMs.
    - source_id: P1-S1-C6
      disposition: represented
      result_indexes:
      - 4
      reason: Parity occurs when SVMs access CNN features.
    - source_id: P1-S1-C7
      disposition: represented
      result_indexes:
      - 2
      reason: CNNs leverage distributed patterns while SVMs focus on lesion area.
    - source_id: P1-S1-C8
      disposition: represented
      result_indexes:
      - 3
      reason: CNN saliencies reveal distinct morphometry patterns.
    - source_id: P1-S1-C9
      disposition: represented
      result_indexes:
      - 3
      reason: Predictions depend on ipsilateral and contralateral features outside
        lesion.
    - source_id: P1-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Conclusion statement summarizing findings.
    - source_id: P1-S2-C8
      disposition: repeated
      result_indexes:
      - 1
      reason: Restatement of CNN accuracy over traditional methods.
    - source_id: P1-S2-C9
      disposition: repeated
      result_indexes:
      - 3
      reason: Restatement of CNN identifying complex spatial patterns.
    - source_id: P1-S3-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about AI tools providing new information.
    - source_id: P2-S4-C5
      disposition: represented
      result_indexes:
      - 1
      reason: CNNs achieve significantly higher predictive accuracy than SVMs.
    - source_id: P2-S4-C6
      disposition: represented
      result_indexes:
      - 2
      reason: CNN focuses on regions outside the lesion that SVM misses.
    - source_id: P2-S4-C7
      disposition: represented
      result_indexes:
      - 3
      reason: CNN leverages patterns consistent among subgroups.
    - source_id: P5-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of SVM tuning results in supplementary data.
    - source_id: P5-S3-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of Figure 2 illustrative patterns.
    - source_id: P5-S3-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of Figure 2 AUC.
    - source_id: P5-S3-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of Figure 2 patterns not captured by conventional models.
    - source_id: P6-S1-C1
      disposition: repeated
      result_indexes:
      - 1
      reason: Restatement that CNN outperformed SVMs.
    - source_id: P6-S4-C2
      disposition: represented
      result_indexes:
      - 0
      reason: CNN achieved moderate-to-high accuracy.
    - source_id: P6-S4-C3
      disposition: represented
      result_indexes:
      - 0
      reason: Median accuracy for severe aphasia was 0.88.
    - source_id: P6-S4-C4
      disposition: represented
      result_indexes:
      - 0
      reason: Median class accuracy for nonsevere aphasia was 0.67.
    - source_id: P6-S4-C5
      disposition: represented
      result_indexes:
      - 0
      reason: Precision reflects tendency towards false positives.
    - source_id: P6-S4-C6
      disposition: represented
      result_indexes:
      - 0
      reason: Precision score of 0.59.
    - source_id: P6-S4-C7
      disposition: represented
      result_indexes:
      - 0
      reason: Median F1 was 0.7.
    - source_id: P6-S4-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Implementation detail (PyTorch).
    - source_id: P6-S4-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Permutation test p-value for model robustness.
    - source_id: P6-S4-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement on feature structure consistency.
    - source_id: P6-S4-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: t-SNE clustering description.
    - source_id: P6-S5-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: t-SNE visualization description.
    - source_id: P7-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation on lesion size and predictions.
    - source_id: P7-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation on misclassifications.
    - source_id: P7-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Linear SVMs outperformed nonlinear SVMs.
    - source_id: P7-S1-C7
      disposition: represented
      result_indexes:
      - 1
      reason: Linear SVMs had significantly worse F1 scores than CNNs.
    - source_id: P7-S1-C8
      disposition: represented
      result_indexes:
      - 1
      reason: SVMs mean accuracy was worse than CNNs.
    - source_id: P7-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Linear SVMs outperformed other SVMs with PCA/ICA.
    - source_id: P7-S1-C12
      disposition: represented
      result_indexes:
      - 5
      reason: PCA vs ICA conferred no significant benefit on F1 or accuracy.
    - source_id: P7-S2-C2
      disposition: represented
      result_indexes:
      - 5
      reason: Dimensionality reduction did not improve SVM performance.
    - source_id: P7-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation on class-specific accuracy (non-severe vs severe).
    - source_id: P8-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation on SVM minority class accuracy.
    - source_id: P8-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison of CNN recall vs SVM precision.
    - source_id: P8-S1-C5
      disposition: represented
      result_indexes:
      - 6
      reason: Weighted average did not meaningfully outperform CNN on F1.
    - source_id: P8-S1-C6
      disposition: represented
      result_indexes:
      - 6
      reason: No significant difference between ensemble set and CNN.
    - source_id: P8-S1-C9
      disposition: represented
      result_indexes:
      - 7
      reason: Stacked models improved over SVM but not significantly over CNN.
    - source_id: P8-S1-C10
      disposition: represented
      result_indexes:
      - 7
      reason: Stacked model F1 marginally better than CNN, not statistically significant.
    - source_id: P8-S2-C2
      disposition: represented
      result_indexes:
      - 7
      reason: Stacked model mean class accuracy difference was insignificant.
    - source_id: P8-S3-C2
      disposition: represented
      result_indexes:
      - 8
      reason: SHAP and deep SHAP maps more similar to each other than to Grad-CAM++.
    - source_id: P9-S1-C4
      disposition: represented
      result_indexes:
      - 9
      reason: SVMs on Grad-CAM++ achieved significantly higher F1 than on deep SHAP.
    - source_id: P9-S1-C8
      disposition: represented
      result_indexes:
      - 10
      reason: Grad-CAM++ saliency higher in left hemisphere for nonsevere predictions.
    - source_id: P9-S1-C9
      disposition: represented
      result_indexes:
      - 10
      reason: Saliency higher in right hemisphere for severe predictions.
    - source_id: P9-S1-C10
      disposition: represented
      result_indexes:
      - 11
      reason: SVM SHAP saliency higher in lesion for severe, perilesional/extralesional
        for nonsevere.
    - source_id: P9-S2-C1
      disposition: represented
      result_indexes:
      - 11
      reason: Saliency low for homolog ROIs, relatively higher for severe predictions.
    - source_id: P9-S2-C3
      disposition: represented
      result_indexes:
      - 12
      reason: CNN on lesion anatomy alone leads to significantly worse performance.
    - source_id: P10-S1-C4
      disposition: represented
      result_indexes:
      - 13
      reason: Subgroups exhibited bilateral patterns.
    - source_id: P10-S1-C5
      disposition: represented
      result_indexes:
      - 13
      reason: Severe subgroups 1, 3, 5 showed right hemisphere saliency.
    - source_id: P10-S1-C6
      disposition: represented
      result_indexes:
      - 13
      reason: Nonsevere subgroup 6 showed right-lateralized saliency.
    - source_id: P10-S1-C7
      disposition: represented
      result_indexes:
      - 13
      reason: Nonsevere subgroup 6 similar to severe subgroup 2.
    - source_id: P10-S1-C8
      disposition: represented
      result_indexes:
      - 13
      reason: Subgroups of different classes exhibited similar saliency patterns.
    - source_id: P10-S1-C9
      disposition: represented
      result_indexes:
      - 13
      reason: Severe subgroup 4 (right temporoccipital) vs nonsevere subgroup 4 (left
        temporoccipital).
    - source_id: P10-S2-C6
      disposition: represented
      result_indexes:
      - 14
      reason: Patient subgroups not associated with lesion size.
    - source_id: P10-S2-C1
      disposition: represented
      result_indexes:
      - 15
      reason: Variability grounded in language subsystems and non-language systems/aging.
    - source_id: P10-S2-C2
      disposition: represented
      result_indexes:
      - 15
      reason: Frontal/temporal cortex associated with semantics, reading, speech,
        lexical-semantics.
    - source_id: P10-S2-C3
      disposition: represented
      result_indexes:
      - 15
      reason: Superior parietal cortex associated with response inhibition, object/spatial
        processing.
    - source_id: P10-S2-C4
      disposition: represented
      result_indexes:
      - 15
      reason: Frontal/temporal pole associated with decision making, age, and brain
        disorders.
    - source_id: P13-S1-C4
      disposition: repeated
      result_indexes:
      - 10
      reason: Restatement of contralateral features for severe, ipsilateral for nonsevere.
    - source_id: P13-S1-C5
      disposition: repeated
      result_indexes:
      - 10
      reason: Restatement of right hemisphere as predictor of severe aphasia.
    - source_id: P13-S2-C11
      disposition: repeated
      result_indexes:
      - 14
      reason: Restatement that lesion size did not differ among subgroups.
    - source_id: P14-S1-C2
      disposition: repeated
      result_indexes:
      - 15
      reason: Restatement of language process associations.
    - source_id: P14-S1-C3
      disposition: repeated
      result_indexes:
      - 15
      reason: Restatement of language process associations.
    - source_id: P14-S1-C4
      disposition: repeated
      result_indexes:
      - 15
      reason: Restatement of language process associations.
    - source_id: P14-S1-C5
      disposition: repeated
      result_indexes:
      - 15
      reason: Restatement of higher-level cognition/aging associations.
    unresolved_coverage:
    - source_id: P9-S2-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P8-S2-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S2-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S2-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S3-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S3-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S3-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S3-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S1-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S1-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S2-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S1-C1
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S1-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S1-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S1-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S1-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S1-C12
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C1
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S2-C1
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S2-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S1-C1
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S1-C2
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
    - source_id: P12-S2-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S2-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S1-C1
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S1-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S1-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S1-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S1-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S1-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S1-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S2-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S2-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S2-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S2-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S2-C12
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P14-S1-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P14-S1-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P14-S2-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P14-S2-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P14-S3-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C10
    - P1-S2-C8
    - P1-S2-C9
    - P1-S3-C2
    - P5-S1-C9
    - P5-S3-C3
    - P5-S3-C4
    - P5-S3-C5
    - P6-S1-C1
    - P6-S4-C5
    - P6-S4-C11
    - P6-S4-C12
    - P6-S4-C13
    - P6-S4-C14
    - P6-S5-C2
    - P7-S1-C2
    - P7-S1-C3
    - P7-S1-C6
    - P7-S1-C11
    - P7-S2-C3
    - P8-S1-C1
    - P8-S1-C2
    - P8-S2-C3
    - P8-S2-C4
    - P8-S2-C8
    - P8-S3-C3
    - P8-S3-C4
    - P8-S3-C5
    - P8-S3-C6
    - P9-S1-C2
    - P9-S1-C5
    - P9-S2-C6
    - P10-S1-C1
    - P10-S1-C2
    - P10-S1-C3
    - P10-S1-C10
    - P10-S1-C11
    - P10-S2-C1
    - P11-S1-C1
    - P11-S1-C2
    - P11-S1-C6
    - P11-S1-C7
    - P11-S1-C8
    - P11-S1-C11
    - P11-S2-C1
    - P11-S2-C3
    - P12-S1-C1
    - P12-S2-C3
    - P12-S2-C4
    - P12-S2-C5
    - P12-S2-C6
    - P12-S2-C7
    - P12-S2-C10
    - P13-S1-C1
    - P13-S1-C2
    - P13-S1-C3
    - P13-S1-C6
    - P13-S1-C8
    - P13-S1-C11
    - P13-S2-C6
    - P13-S2-C8
    - P13-S2-C9
    - P13-S2-C10
    - P13-S2-C12
    - P14-S1-C6
    - P14-S1-C7
    - P14-S2-C3
    - P14-S2-C6
    - P14-S3-C9
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review: []
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P2-S4-C9
      recruited_sample:
      - P2-S4-C9
      eligibility:
      - P2-S4-C9
      imaging_provenance:
      - P3-S1-C6
      imaging_timing:
      - P3-S1-C5
      outcome_timing:
      - P3-S1-C5
      outcome_definition:
      - P2-S5-C4
      - P3-S1-C2
      validation:
      - P3-S2-C6
      - P4-S1-C12
      - P4-S2-C5
      - P4-S2-C10
      - P5-S1-C11
      - P6-S1-C11
      analysis_restrictions:
      - P14-S3-C5
      dependent_variable_statement:
      - P2-S4-C4
      - P3-S1-C3
      - P4-S4-C6
      - P5-S1-C7
      limitations:
      - P14-S3-C5
      - P14-S3-C6
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles: []
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P2-S4-C9
      - P13-S2-C4
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: internal_cross_validation
    held_selections:
    - slot: dependent_variable_statement
      source_id: P5-S1-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S4-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S1-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S1-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S1-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S1-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S1-C12
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P4-S2-C4
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P7-S1-C10
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P8-S1-C1
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P8-S1-C10
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P9-S1-C1
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P9-S1-C5
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P11-S1-C1
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: adjustment_roles
      source_ids:
      - P4-S1-C10
      - P5-S1-C10
      - P5-S1-C11
      - P7-S1-C10
      - P7-S1-C11
      - P7-S1-C12
      - P8-S1-C10
      - P8-S1-C1
      - P9-S1-C5
      - P10-S1-C11
      - P11-S1-C1
      - P11-S1-C2
      - P12-S1-C11
      - P13-S1-C12
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
      pdf_sha256: 68f566e52924f65d6d4df2e0ebeb371b036a1588ed2e049de3bacdd06a582486
      review_sha256: 8d7a558e52be5e3f0e45ec8e054dd1acdc5ec2f388b22878efa73fb39271f0a0
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
      - P10-S2-C6
      - P13-S2-C11
      source_result: The study performed consensus clustering on CNN feature saliency
        maps (Grad-CAM++) to identify subgroups of patients with similar morphometry
        patterns. An ANOVA was conducted to test for differences in lesion size among
        these subgroups. The results indicated that patient subgroups were not associated
        with lesion size, as the ANOVA was not statistically significant for both
        severe (F(6,108) = 0.77, p = 0.6) and non-severe (F(5,110) = 0.67, p = 0.65)
        aphasia groups.
      result_status: not_detected
      patient_measurement: voxel_tissue
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis correctly identifies the comparison of lesion
            size across subgroups derived from CNN saliency clustering. The source
            explicitly describes this as a final analysis to map heterogeneity and
            test associations with lesion size (P10-S2-C6, P13-S2-C11).
          source_ids:
          - P10-S2-C6
          - P13-S2-C11
          - P11-S1-C1
        direction:
          answer: fits
          reason: The claim of 'no_effect' (no association) is faithful to the source,
            which reports non-significant ANOVA results (p > 0.05) for lesion size
            differences among subgroups. This is a legitimate null result, not a robustness
            check of another association.
          source_ids:
          - P10-S2-C6
          - P11-S1-C1
          - P13-S2-C11
        construct:
          answer: fits
          reason: The exposure is correctly identified as CNN saliency clusters (derived
            from Grad-CAM++ maps). The outcome is lesion size. The patient measurement
            is voxel_tissue, as the subgroups are defined by morphometry patterns
            (tissue integrity/volumes) in the brain, not by diffusion tractography
            or template overlap. The source confirms the use of morphometry and lesion
            anatomy (P1-S1-C4, P6-S1-C12).
          source_ids:
          - P1-S1-C4
          - P6-S1-C12
          - P10-S2-C6
        qualifications:
          answer: fits
          reason: The qualification that subgroups were analyzed separately for severe
            and non-severe aphasia is supported by the source, which reports separate
            ANOVAs for these groups (P11-S1-C1). The limitation regarding downsampling
            to 8mm is also correctly noted (P14-S3-C5).
          source_ids:
          - P11-S1-C1
          - P14-S3-C5
        missing_material_caveat:
          answer: fits
          reason: No material caveats are missing. The null result is clearly stated,
            and the context of the study (chronic stroke, specific imaging resolution)
            is captured. The distinction between this null result and the main positive
            finding (CNN outperforming SVM) is maintained.
          source_ids:
          - P10-S2-C6
          - P13-S2-C11
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
      original: 213
      action: not_transcribed
      reason: Not supported by selected quotations
    analysis_identity:
      id: R015
      exposure:
        text: CNN saliency clusters
      outcome:
        text: lesion size
      analysis_label: Subgroup morphometry vs lesion size
      relation: association
      evidence_ids:
      - P10-S2-C6
      - P13-S2-C11
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
        pdf_sha256: 68f566e52924f65d6d4df2e0ebeb371b036a1588ed2e049de3bacdd06a582486
        source_review: _compare/relationships-2026-11-16/review-current/Teghipco2024
        source_status_sha256: a66d207d1868c70d5cc8a5a7f906ef8735578b25ffbd7dd4f807506d98abc295
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P2-S4-C9:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 68f566e52924f65d6d4df2e0ebeb371b036a1588ed2e049de3bacdd06a582486
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 1c9c0355a33acf9c8636c28ae15cdd7c3ed0d03a2862dfec708474ec5f4c150f
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S4-C9
          page: 2
          text_layer_sha256: 1c9c0355a33acf9c8636c28ae15cdd7c3ed0d03a2862dfec708474ec5f4c150f
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Methods

          Participants

          Two-hundred and thirteen individuals (age = 57.98 +/−11.34, 62% male)

          with chronic left strokes (mean years post-stroke = 3.2 +/−3.7) that par-

          ticipated in studies conducted at the Center for the Study of Aphasia

          Recovery (C-STAR) were analyzed retrospectively in the present work.'
        anchor_text: 'Methods

          Participants

          Two-hundred and thirteen individuals (age = 57.98 +/−11.34, 62% male)

          with chronic left strokes (mean years post-stroke = 3.2 +/−3.7) that par-

          ticipated in studies conducted at the Center for the Study of Aphasia

          Recovery (C-STAR) were analyzed retrospectively in the present work.'
        excluded_fragments: []
        image_sha256: a2aacf7e1a8b79005d9806366636cb3b81e79fe3c1c8cfda5838df3b238227ba
        transcription: 'Methods

          Participants

          Two-hundred and thirteen individuals (age = 57.98 +/- 11.34, 62% male) with
          chronic left strokes (mean years post-stroke = 3.2 +/- 3.7) that participated
          in studies conducted at the Center for the Study of Aphasia Recovery (C-STAR)
          were analyzed retrospectively in the present work'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 10
  quote: 'Finally, we found that patient subgroups were not associated with

    lesion size, as hinted by the lesion outlines in Figs. 9 and 10.'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-25'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
