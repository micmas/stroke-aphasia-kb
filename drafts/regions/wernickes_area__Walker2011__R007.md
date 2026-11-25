---
id: wernickes_area
name: Wernicke's area cluster
kind: network
findings:
- id: f1
  target: semantic_error_scores
  target_kind: impairment
  claim: Lesions in voxels of the pSTG/pMTG generally identified with Wernicke's area
    had no measurable impact on semantic error scores (SemPlus).
  direction: no_effect
  relationship: correlational
  method: VLSM
  sample:
    n: 64
    population: individuals with confirmed left hemisphere stroke and clinically apparent
      aphasia
    phase: not_reported
    time_post_onset: chronic phase (mean 68 months post-stroke; 59 of 64 subjects
      at least 6 months post-stroke)
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - The finding is specific to chronic patients and may differ from acute stroke presentations.
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Patient lesion overlap with voxels in the posterior
    superior temporal gyrus (pSTG) and posterior middle temporal gyrus (pMTG) generally
    identified with Wernicke''s area. The semantic error measure (SemPlus) was broadly
    defined to include synonyms, category coordinates, superordinates, subordinates,
    strongly associated responses, non-noun single-word errors (verbs/adjectives),
    mixed errors, and semantic circumlocutions. Additional metadata has not been transcribed;
    review the pending-field flags before approval. PDF image reading (P3-S4-C6, two-model
    agreement, human verification pending): Participants


    Participants were 64 individuals (42% females; 48% African American) with confirmed
    left hemisphere stroke, who currently or initially presented with clinically apparent
    aphasia Original text-layer quotation is preserved below. PDF image reading (P3-S4-C9,
    two-model agreement, human verification pending): . Their mean

    number of months post–stroke at time of PNT performance was 68

    (range 1–381) Original text-layer quotation is preserved below. PDF image reading
    (P3-S4-C10, two-model agreement, human verification pending): . The most acute
    patient performed the PNT 6 weeks

    post-stroke and was imaged 8 weeks post-stroke; 59 of 64 subjects

    were at least 6 months post Original text-layer quotation is preserved below.'
  imaging_details:
    reference_space: not_reported
    atlases_used: []
  lesion_mapping: {}
  provenance:
    extracted_by: model:gemma4:31b
    extracted_on: '2026-11-26'
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
    - proposed_concept:semantic_error_scores
  citation: '@Walker2011'
  source_passages:
  - section: Original source P9-S2-C6
    page: 9
    quote: 'Instead, as in Schwartz

      et al. (2009), we found that voxels in the pSTG/pMTG generally

      identiﬁed with Wernicke’s area yielded very low t-values, indicat-

      ing that lesions had no measurable impact on semantic error

      scores.'
    supports: claim
  - section: Original source P3-S4-C6
    page: 3
    quote: 'Participants

      Participants were 64 individuals (42% females; 48% African

      American) with conﬁrmed left hemisphere stroke, who currently

      or initially presented with clinically apparent aphasia.'
    supports: sample
  - section: Original source P3-S4-C9
    page: 3
    quote: 'Their mean

      number of months post–stroke at time of PNT performance was 68

      (range 1–381).'
    supports: sample
  - section: Original source P3-S4-C10
    page: 3
    quote: 'The most acute patient performed the PNT 6 weeks

      post-stroke and was imaged 8 weeks post-stroke; 59 of 64 subjects

      were at least 6 months post.'
    supports: sample
  - section: Original source P5-S1-C15
    page: 5
    quote: 'A t-test comparing SemPlus scores

      between patients with and without lesions was performed at each

      voxel using the VoxBo brain imaging package (www.voxbo.org).

      '
    supports: method
  - section: Original source P4-S2-C2
    page: 4
    quote: 'Starting with

      the restrictive semantic error set analyzed in Schwartz et al.

      (2009) – substituted nouns that were synonyms, category coordi-

      nates, superordinates, subordinates, or strongly associated re-

      sponses to targets – we added from the naming response corpus

      non-noun, single-word errors that named an associated action

      (verb) or non-pictured feature (adjective) of the target.'
    supports: claim
  - section: Original source P4-S2-C3
    page: 4
    quote: 'Phonologi-

      cal overlap was not considered, so mixed (semantic plus phonolog-

      ical) errors were also included.'
    supports: claim
  - section: Original source P4-S2-C4
    page: 4
    quote: 'Finally, circumlocutions and other

      multi-word descriptions were included in SemPlus if three experi-

      enced aphasia researchers agreed that the semantic content of the

      utterance indicated at least partial access to the semantic repre-

      sentation of the target.'
    supports: claim
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-26'
relationship_review:
  paper: Walker2011
  proposal_id: R007
  review_status_sha256: 25effce4dfef35a4146c1c41a0a7b85139882df23847faeee9a3a3cc6867cbd8
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: d95039d49e60c7e416291ea53fddd868225c2b1786b91dcd74f40737a9f8cecc
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: d95039d49e60c7e416291ea53fddd868225c2b1786b91dcd74f40737a9f8cecc
        A/passages.json: 7ca3eba238185735fbae6ce63a2e9d5f3b513ec7adeebc2470e472ee7664a407
        A/raw.json: a9200dd017e28c6d93f9a493f23577d011043745fcf15cce6fbe7c544eb48f4a
        A/source-units.json: 537e9589a54ba10ff963aeb6ef0ec66f56a95310a6823b9340b1bd89a8a2dcb7
        A/full-source-units.json: 28782feb3650666b05f7c7d6346d1159e65e42d3c21ca88c39fb7e7b25fa0539
        A/meta.json: 151b5908e7c670c138a562f508cb67a4ffec77d14789424e4b2cd44f38c6ff29
        A/table-images/TABLE-1-page-5-1.png: 667204cc7a1e674c93990fea33a059a35f8b53a093e421c165a77435bf5e2786
        A/table-images/page-5.png: b4ded1ae3e99ca261d0f93107a0aecf28b84e81496033eed46e4caadbefd251a
        A/table-images/manifest.json: 57582e1b2c76cb0f62520d3c2ddb36ba7596ad8765246f7d84c7e6cb6124852d
        A/table-images/TABLE-2-page-5-2.png: 4d69f1579d6228fead909749424f87b8d19296d76a49c347b5c3dda05f475281
        A/clauses/window-11/raw.json: 381aa396b741cdbfe50213112a3e6fca57efe4f22fa7c51dbf88b4239bb5dac5
        A/clauses/window-11/prompt.txt: b9d1c3d2cd3a7f962d224a05947535c7d6c7f3744fcab0768d3f9b53390518b4
        A/clauses/window-11/meta.json: 405c5cda24a3cf5cb5ccb742a23988fb955257c7132551a6a0a2e81d3e2f6301
        A/clauses/window-10/raw.json: ee698f636712d75a3d335e982bb06ba1119bddda437fc19c8e8b67acd79f8892
        A/clauses/window-10/prompt.txt: 4a530b2912d51283facfcb33f4fa32278e37e1fbcd0ad1d7ccd8b992ff7064a5
        A/clauses/window-10/meta.json: d0c868e193fa791077b313ffd54d07eb4287fe4eea1d4b91c101f5e7fafd545b
        A/clauses/window-03/raw.json: 233974d6b7e19aab49586110fd51e50e4ad4b960a2c8f935a82405e1f60f7929
        A/clauses/window-03/prompt.txt: 65e851ca94e25c57ddf8e5165ed4b0b3aea2bf95fc94eaf8b8fd8b11a3bc390a
        A/clauses/window-03/meta.json: 0ff3b0d67d77aaab96ab68618bab7caf749cf0be61d8408f1f81ea0167d97998
        A/clauses/window-04/raw.json: 25df1bfd38cedc92d35bcae639772d438e61716b114c355928437d8b7306035d
        A/clauses/window-04/prompt.txt: 79e357289c2e8e49b2332d41334dc8af0de0d49a4e5b7ae0f205d36953f3284b
        A/clauses/window-04/meta.json: 4e9499b7dce32a1a94ecca58fb7f39e6dd3cb2fc189bdcb296abe35ef003b813
        A/clauses/window-05/raw.json: 497f46fdd2f378da9bd8174fd8447059af2eb185cd116034d5f87f07de4c284f
        A/clauses/window-05/prompt.txt: ed1b453acefe8bdf6603f5f19e92f31343155afc62cdf2a02408065ce9f5f7e7
        A/clauses/window-05/meta.json: 7974059846b89a4a1b492fa8f8768bb037cafaa43f4181d68f3247d5296600d9
        A/clauses/window-02/raw.json: 5fbdac7752505324a786c2c326553aab8fc8e97ab15b13e83127371365a6f176
        A/clauses/window-02/prompt.txt: 347f820dac77c81570cae5671588b0d4bf63bb787fba2e220e0f956cae75bf63
        A/clauses/window-02/meta.json: ac4b29fc470d59007aec15158c5131f843e66206d6cafc434bfa4227a77cda22
        A/clauses/window-12/raw.json: 4b6fe26f6124d0179bafa660398a0ab64286fca53cad9b3a5ca78db8742069a4
        A/clauses/window-12/prompt.txt: 92b831565cab2b93c9f0ea022e8e2b47251b46d78a3930de32aa3e206318f5cb
        A/clauses/window-12/meta.json: a2cb073b3e26ef0fc222ef3c20d80f9c31bc6a937b92652af6f583b812c53bbf
        A/clauses/window-09/raw.json: ae6fd3dd6f5c64d96d25e62b18426cae19cdb621cd63d36046f68653df4819d8
        A/clauses/window-09/prompt.txt: b51bc885a184fbf9e6621cac5cda0c9ac0e57693b4675f27c62ea2a1e6c425ee
        A/clauses/window-09/meta.json: a489cfd60c3124a995b9250f42d2bd20e6d9e0724f36ff41d61f80aa0cd625f5
        A/clauses/window-07/raw.json: 2124689b9f9de842ec9a2d2179890c204d05531f48c4c6c1a78d62bf723670b6
        A/clauses/window-07/prompt.txt: 9ddd61196f0fd7b29d22b55f50aa9b7023d2cef9095d11c23abaefb3e1127839
        A/clauses/window-07/meta.json: 097e7a7aabf4fd81c29c6d7e9aaf1d1d7f30408488cdf1de07a286d19540bebe
        A/clauses/window-01/raw.json: c36871e8bab7823347fba1a334e880105671bc5ea931dba674f7c257c7e467a7
        A/clauses/window-01/prompt.txt: 1d3218348f235f36c377b874fe0ccf89290bc9977e831ae467bfbdb00e2fe30a
        A/clauses/window-01/meta.json: 0c158c7900b0b75eb9a42c8122295ff48a55edb687c0c90343943a0de4f48034
        A/clauses/window-06/raw.json: f4adda6cedf3b5ac014fa5e08181bc0749aceab484c86a61ebb6cb2646d97889
        A/clauses/window-06/prompt.txt: 7d7ae51c3ae8b81013125ae2e6e05f9886b3e09437206ae2db45e5c5f496a74d
        A/clauses/window-06/meta.json: 6eb3c09b6b0a64bdeb1ed1514d8f88ba81dcbf79924594fbe7bbbe1fba68274e
        A/clauses/window-08/raw.json: ff95c7b030e0f61a7104df5ad945b9b0ef9a4aca2b2ce7cadb11273e81d4103b
        A/clauses/window-08/prompt.txt: 097e9b6862fd1ecbfc239b3e6af9297f30bb488517bfb10aff35021e3d05f8f6
        A/clauses/window-08/meta.json: 592490dcdf5d685faaf096e10c58c4c7413ddf0f201951ec84d5aa7da4856c4a
        A/tables/TABLE-1-page-5-1/raw.json: f7315c4d4862dfc61e9a048ef2c818cc46f336587f7117ccafd9c10943a5c12f
        A/tables/TABLE-1-page-5-1/prompt.txt: b7a43330401a5c6b60bb0952d266d829af51af3754881fb623f5bd0f249273af
        A/tables/TABLE-1-page-5-1/meta.json: 5f9fea9401dc59c7a3863670fc346762f9f8faef8d39fb3def80a1453bd55caf
        A/tables/TABLE-2-page-5-2/raw.json: e054e91a88df15999a6c5044d2483e046ef3290ff6cf99906d43ed2e30f8be3c
        A/tables/TABLE-2-page-5-2/prompt.txt: ad551636af87247948cdaf2bf78af4cc6829a7fae7914722bfe4e568210989ec
        A/tables/TABLE-2-page-5-2/meta.json: ca218d4728cae33a0ce68e2dca6df4a0436294c3a1d1847ab3d3991883f851e6
        B/passages.json: 7ca3eba238185735fbae6ce63a2e9d5f3b513ec7adeebc2470e472ee7664a407
        B/raw.json: ea1dd0779cf43568f0547c7fe77f2352de2feba506ea88a6e35d7de05453292c
        B/source-units.json: 537e9589a54ba10ff963aeb6ef0ec66f56a95310a6823b9340b1bd89a8a2dcb7
        B/full-source-units.json: 28782feb3650666b05f7c7d6346d1159e65e42d3c21ca88c39fb7e7b25fa0539
        B/meta.json: e60de70185a35fc13fe866ff50fba4a735d930f91a471d55d4571c6a3d8b85d7
        B/table-images/TABLE-1-page-5-1.png: 667204cc7a1e674c93990fea33a059a35f8b53a093e421c165a77435bf5e2786
        B/table-images/page-5.png: b4ded1ae3e99ca261d0f93107a0aecf28b84e81496033eed46e4caadbefd251a
        B/table-images/manifest.json: 6c89c1bc891c11d4c5140de94de94f0425fed7276bf3561c9bc5980bfbac04da
        B/table-images/TABLE-2-page-5-2.png: 4d69f1579d6228fead909749424f87b8d19296d76a49c347b5c3dda05f475281
        B/clauses/window-11/raw.json: 387ae201cb5be2a11f81cf69453cae732918eee9b51dcd0ca71fb00dbb4ba05b
        B/clauses/window-11/prompt.txt: b9d1c3d2cd3a7f962d224a05947535c7d6c7f3744fcab0768d3f9b53390518b4
        B/clauses/window-11/meta.json: 10379104d6a84d973e9b4ee115e9f29a75af651161f13cf973147dad4921ebf7
        B/clauses/window-10/raw.json: 865119bdf7864d312b6c5ca654d5f778b53564c9fb016266d4bcef0853478655
        B/clauses/window-10/prompt.txt: 4a530b2912d51283facfcb33f4fa32278e37e1fbcd0ad1d7ccd8b992ff7064a5
        B/clauses/window-10/meta.json: d031fae8414d621c5346115e23c582614168eecf147fc8a235009c2ffffca256
        B/clauses/window-03/raw.json: 8f853d5915bd4c49cf7d708caa9104383dc8142ad38a950e0b631b0ca85b3dbe
        B/clauses/window-03/prompt.txt: 65e851ca94e25c57ddf8e5165ed4b0b3aea2bf95fc94eaf8b8fd8b11a3bc390a
        B/clauses/window-03/meta.json: c6b956ed5101b73d39dd8b597de747b82bcc9eea3bc0cca49ceecbfbfc65bb1f
        B/clauses/window-04/raw.json: ee89c28c9f6e8e23157400b55b83c5d8296e1f15e383cff2900ea14f22689ac7
        B/clauses/window-04/prompt.txt: 79e357289c2e8e49b2332d41334dc8af0de0d49a4e5b7ae0f205d36953f3284b
        B/clauses/window-04/meta.json: e7f8dbe3d8bf37cfbe902468b8c97ec584947a10e96cdf8ac8eed3f0b62a92be
        B/clauses/window-05/raw.json: 87b2b947391e99f2676461b5d6880f642ccfba43c8773c7098e75c9d835a11ab
        B/clauses/window-05/prompt.txt: ed1b453acefe8bdf6603f5f19e92f31343155afc62cdf2a02408065ce9f5f7e7
        B/clauses/window-05/meta.json: f770f0a9f587985f790e3cc298f8fefa274e54dc641b10376a0bb3bb7f97d13f
        B/clauses/window-02/raw.json: edc7012f1858c4ec0ab8aa7d9199f7d752c27da3a7f7131784c4af629280da04
        B/clauses/window-02/prompt.txt: 347f820dac77c81570cae5671588b0d4bf63bb787fba2e220e0f956cae75bf63
        B/clauses/window-02/meta.json: 9fbd9340eedc6edfbe1e329093348227c012ff636a14e2776915ddf2c43e906e
        B/clauses/window-12/raw.json: 943aff58f2818cfa38133d03ffa218789a22e9868b7e9c89706afb4e9a99581a
        B/clauses/window-12/prompt.txt: 92b831565cab2b93c9f0ea022e8e2b47251b46d78a3930de32aa3e206318f5cb
        B/clauses/window-12/meta.json: 2c12eab32aad11783349375c416a06df8d2b109b7085ca461598f0e08a8f46c7
        B/clauses/window-09/raw.json: 08e7799608d49bf1d0a9ffac99c2c8a79829a0d53b91700d9a6248033f2a8b6d
        B/clauses/window-09/prompt.txt: b51bc885a184fbf9e6621cac5cda0c9ac0e57693b4675f27c62ea2a1e6c425ee
        B/clauses/window-09/meta.json: 061d08ffadeaa7e1e268222fbc9f5182e08906f20cbeb3738387457c9d4829b2
        B/clauses/window-07/raw.json: 2013bd6d7dfac722fee0999e2c0274da4e07922cb6020df1a442b40242de0929
        B/clauses/window-07/prompt.txt: 9ddd61196f0fd7b29d22b55f50aa9b7023d2cef9095d11c23abaefb3e1127839
        B/clauses/window-07/meta.json: a741f23c3ab1170ae497dbf5d0c93bffa037443828177ae45c85316f1b8d1b16
        B/clauses/window-01/raw.json: fb406be324077eaade3738104a526ac9ce73b6369926327ca898a65c26230912
        B/clauses/window-01/prompt.txt: 1d3218348f235f36c377b874fe0ccf89290bc9977e831ae467bfbdb00e2fe30a
        B/clauses/window-01/meta.json: f8c305321cad0c0fcf46bfada8f1eee1738d0ee458da65677db88cf39ed572f0
        B/clauses/window-06/raw.json: eb2bc0b3452cf1a927bbb73ffb9636f22d80b5719ebfb4340c758b5604c12a28
        B/clauses/window-06/prompt.txt: 7d7ae51c3ae8b81013125ae2e6e05f9886b3e09437206ae2db45e5c5f496a74d
        B/clauses/window-06/meta.json: 3696ed241819656e4b22f4acc05cc0d494750d27ce48434bcbf69ff80049af22
        B/clauses/window-08/raw.json: 20d08d0571a47292faeecefce593a6ec64b25c3f2fd13301111214febec086dd
        B/clauses/window-08/prompt.txt: 097e9b6862fd1ecbfc239b3e6af9297f30bb488517bfb10aff35021e3d05f8f6
        B/clauses/window-08/meta.json: 9f78d57e94330b79cb054dc9dce69ac50228d6755008e86205e9b933d5ab7575
        B/tables/TABLE-1-page-5-1/raw.json: defe111e816d952848fa204cb7dd77388bbdaf5976c7a955fb0cdfff2c6909d2
        B/tables/TABLE-1-page-5-1/prompt.txt: b7a43330401a5c6b60bb0952d266d829af51af3754881fb623f5bd0f249273af
        B/tables/TABLE-1-page-5-1/meta.json: 2b90da767623792c88507915ce4dfd99206aa128ec38c7b0d71edd3041e793ee
        B/tables/TABLE-2-page-5-2/raw.json: de16cd7da5fe7db29ec2d72060254dfd66c262e9c7a0609938a72c13453d1ddc
        B/tables/TABLE-2-page-5-2/prompt.txt: ad551636af87247948cdaf2bf78af4cc6829a7fae7914722bfe4e568210989ec
        B/tables/TABLE-2-page-5-2/meta.json: eb1793bb02b46834b7622e3913bbebe6095883e70a796c8068ef7b0cbe0f334a
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
      pdf_sha256: d95039d49e60c7e416291ea53fddd868225c2b1786b91dcd74f40737a9f8cecc
      source_review: _compare/relationships-2026-11-16/review-current/Walker2011
      source_status_sha256: b594e95a0da18d991bc3093a78ac2bfc4760d8cddc86eab389d5245d9679dc1c
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R007
    exposure:
      text: lesions in Wernicke's area (pSTG/pMTG)
    outcome:
      text: semantic error scores
    analysis_label: VLSM of SemPlus errors (null finding)
    relation: association
    evidence_ids:
    - P9-S2-C6
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
      pdf_sha256: d95039d49e60c7e416291ea53fddd868225c2b1786b91dcd74f40737a9f8cecc
      source_review: _compare/relationships-2026-11-16/review-current/Walker2011
      source_status_sha256: b594e95a0da18d991bc3093a78ac2bfc4760d8cddc86eab389d5245d9679dc1c
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P1-S1-C12
      - Result passage disposed without unit P3-S2-C10
      - Result passage disposed without unit P5-S2-C8
      - Result passage disposed without unit P5-S2-C10
      - Result passage disposed without unit P5-S2-C13
      - Result passage disposed without unit P5-S2-C15
      - Result passage disposed without unit P5-S2-C16
      - Result passage disposed without unit P6-S1-C2
      - Result passage disposed without unit P6-S1-C3
      - Result passage disposed without unit P6-S1-C4
      - Result passage disposed without unit P6-S1-C10
      - Result passage disposed without unit P6-S1-C11
      - Result passage disposed without unit P6-S1-C16
      - Accounting without a linked unit P6-S1-C9
      - Accounting without a linked unit P6-S2-C7
      - Result passage disposed without unit P6-S2-C8
      - Accounting without a linked unit P7-S1-C1
      - Unaccounted source passage P6-S2-C7
      - Unaccounted source passage P6-S1-C9
      - Unaccounted source passage P7-S1-C1
      - Result passage disposed without unit P7-S1-C2
      - Result passage disposed without unit P7-S1-C3
      - Result passage disposed without unit P7-S1-C4
      - Result passage disposed without unit P7-S1-C5
      - Result passage disposed without unit P7-S1-C7
      - Result passage disposed without unit P7-S1-C8
      - Result passage disposed without unit P7-S1-C9
      - Result passage disposed without unit P9-S1-C10
      - Result passage disposed without unit P9-S3-C8
      - Result passage disposed without unit P9-S3-C9
      - Result passage disposed without unit P9-S4-C4
      - Result passage disposed without unit P9-S4-C5
      - Result passage disposed without unit P10-S3-C12
      - Result passage disposed without unit P10-S3-C3
      - Result passage disposed without unit P10-S4-C5
      - Result passage disposed without unit P10-S4-C6
      - Result passage disposed without unit P9-S4-C7
      - 'window 16: invalid/duplicate disposition P11-S2-C4'
      - Result passage disposed without unit P11-S2-C4
      - Result passage disposed without unit P11-S2-C6
      unattached_null_or_qualifier_ids:
      - P2-S1-C8
      - P2-S3-C4
      - P7-S1-C5
      - P7-S1-C7
      - P7-S1-C9
      suppressed_nonrepresented_units: 34
      default_disposition_count_requires_completeness_check: 247
      unselected_timing_passages:
      - P3-S4-C7
      - P9-S3-C4
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P5-S2-C13
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S2-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S2-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C12
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C15
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S2-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S2-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S2-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S1-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S2-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S2-C12
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S2-C13
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S2-C14
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P2-S1-C2
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P3-S2-C9
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P9-S1-C1
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: outcome_definition
        source_ids:
        - P4-S1-C14
        - P4-S1-C15
        - P4-S1-C16
        - P4-S2-C2
        - P4-S2-C3
        - P4-S2-C4
        - P4-S2-C5
        - P4-S2-C6
        - P4-S2-C7
        - P4-S2-C8
        - P4-S2-C9
        - P4-S2-C10
        - P9-S1-C2
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: analysis_restrictions
        source_ids:
        - P2-S1-C5
        - P2-S1-C6
        - P2-S1-C7
        - P2-S1-C8
        - P2-S1-C9
        - P2-S1-C10
        - P5-S1-C14
        - P5-S2-C5
        - P6-S1-C17
        - P7-S1-C5
        - P7-S1-C7
        - P7-S1-C11
        - P7-S2-C6
        - P7-S2-C8
        - P8-S1-C5
        - P8-S1-C6
        - P8-S1-C7
        - P8-S1-C8
        - P8-S2-C4
        - P8-S2-C5
        - P8-S2-C8
        - P9-S1-C5
        - P9-S1-C8
        - P9-S2-C11
        - P9-S2-C12
        - P9-S2-C13
        - P9-S2-C14
        - P9-S3-C11
        - P9-S4-C5
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: limitations
        source_ids:
        - P3-S3-C3
        - P3-S3-C4
        - P3-S3-C5
        - P3-S3-C6
        - P3-S3-C7
        - P3-S3-C8
        - P3-S3-C9
        - P3-S3-C10
        - P3-S3-C11
        - P5-S3-C7
        - P5-S3-C8
        - P5-S3-C9
        - P5-S3-C10
        - P6-S1-C5
        - P6-S1-C6
        - P6-S1-C7
        - P9-S3-C11
        - P9-S4-C6
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: adjustment_roles
        source_ids:
        - P2-S1-C6
        - P2-S1-C7
        - P4-S2-C7
        - P4-S3-C7
        - P5-S2-C5
        - P7-S1-C5
        - P7-S1-C7
        - P7-S1-C11
        - P7-S2-C6
        - P7-S2-C8
        - P8-S1-C5
        - P8-S1-C6
        - P8-S1-C7
        - P8-S1-C8
        - P8-S2-C4
        - P8-S2-C5
        - P8-S2-C8
        - P9-S1-C5
        - P9-S1-C8
        - P9-S2-C11
        - P9-S2-C12
        - P9-S2-C13
        - P9-S2-C14
        - P9-S3-C11
        - P9-S4-C5
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: descriptive_personal_factors
        source_ids:
        - P3-S4-C7
        - P3-S4-C8
        - P3-S4-C9
        - P3-S4-C10
        - P3-S4-C11
        - P4-S1-C6
        - P4-S1-C7
        - P4-S1-C8
        - P4-S1-C9
        - P4-S1-C10
        - P5-S2-C8
        - P5-S2-C9
        - P5-S2-C10
        - P5-S2-C11
        - P5-S2-C12
        - P5-S2-C13
        - P5-S2-C14
        - P5-S2-C15
        - P5-S2-C16
        - P5-S2-C17
        - P6-S1-C3
        - P6-S1-C4
        - P6-S1-C13
        - P6-S1-C14
        - P6-S1-C16
        - P6-S1-C17
        - P6-S1-C18
        - P6-S1-C19
        - P7-S1-C1
        - P7-S1-C2
        - P7-S1-C3
        - P7-S1-C4
        - P7-S1-C5
        - P7-S1-C6
        - P7-S1-C7
        - P7-S1-C8
        - P7-S1-C9
        - P7-S1-C10
        - P7-S1-C11
        - P7-S1-C12
        - P7-S1-C13
        - P7-S1-C15
        - P7-S2-C1
        - P7-S2-C6
        - P7-S2-C7
        - P7-S2-C8
        - P7-S2-C9
        - P7-S2-C12
        - P8-S1-C1
        - P8-S1-C2
        - P8-S1-C3
        - P8-S1-C4
        - P8-S1-C5
        - P8-S1-C6
        - P8-S1-C7
        - P8-S1-C8
        - P8-S1-C9
        - P8-S1-C10
        - P8-S1-C11
        - P8-S1-C12
        - P8-S1-C15
        - P8-S1-C16
        - P8-S2-C1
        - P8-S2-C4
        - P8-S2-C5
        - P8-S2-C8
        - P9-S1-C1
        - P9-S1-C2
        - P9-S1-C3
        - P9-S1-C4
        - P9-S1-C5
        - P9-S1-C6
        - P9-S1-C7
        - P9-S1-C8
        - P9-S1-C9
        - P9-S1-C10
        - P9-S2-C2
        - P9-S2-C3
        - P9-S2-C4
        - P9-S2-C5
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - outcome_definition
      - analysis_restrictions
      - limitations
      - personal_factors
      - tested_personal_effects
      - adjustment_roles
      - explicitly_not_adjusted
      - descriptive_personal_factors
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-5-1
      - TABLE-2-page-5-2
      unlinked_tables:
      - TABLE-1-page-5-1
      - TABLE-2-page-5-2
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P6-S1
        - P6-S2
        - P7-S1
        - P7-S2
        - P8-S1
        - P8-S2
        - P9-S1
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: d95039d49e60c7e416291ea53fddd868225c2b1786b91dcd74f40737a9f8cecc
      source_review: _compare/relationships-2026-11-16/review-current/Walker2011
      source_status_sha256: b594e95a0da18d991bc3093a78ac2bfc4760d8cddc86eab389d5245d9679dc1c
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C12
      disposition: repeated
      result_indexes: []
      reason: Abstract restatement of findings
    - source_id: P2-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes results of a previous study (Schwartz et al., 2009)
    - source_id: P2-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes results of a previous study (Schwartz et al., 2009)
    - source_id: P2-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes results of a previous study (Schwartz et al., 2009)
    - source_id: P2-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes results of a previous study (Schwartz et al., 2009)
    - source_id: P2-S3-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes results of a previous study (Schwartz et al., 2009)
    - source_id: P2-S3-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes results of a previous study (Schwartz et al., 2009)
    - source_id: P2-S3-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes results of a previous study (Schwartz et al., 2009)
    - source_id: P3-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes rationale for the current study's variable definition
    - source_id: P3-S4-C4
      disposition: repeated
      result_indexes: []
      reason: General summary statement
    - source_id: P4-S4-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes imaging quality
    - source_id: P5-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes reliability of a mapping method
    - source_id: P5-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive behavioral data
    - source_id: P5-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive behavioral data
    - source_id: P5-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive behavioral data
    - source_id: P5-S2-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Correlation between two dependent variables
    - source_id: P5-S2-C15
      disposition: background_or_descriptive
      result_indexes: []
      reason: Correlation between two dependent variables
    - source_id: P5-S2-C16
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive imaging coverage data
    - source_id: P6-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive imaging coverage data
    - source_id: P6-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive imaging coverage data
    - source_id: P6-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive imaging coverage data
    - source_id: P6-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive imaging coverage data
    - source_id: P6-S1-C9
      disposition: represented
      result_indexes:
      - 0
      reason: Establishes association between lesion status and SemPlus errors
    - source_id: P6-S1-C10
      disposition: represented
      result_indexes:
      - 0
      reason: Identifies clusters for the association
    - source_id: P6-S1-C11
      disposition: represented
      result_indexes:
      - 0
      reason: Identifies clusters for the association
    - source_id: P6-S1-C16
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive imaging overlap data
    - source_id: P6-S2-C7
      disposition: represented
      result_indexes:
      - 0
      reason: Provides peak t-value for the association
    - source_id: P6-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive patient count for peak voxels
    - source_id: P7-S1-C1
      disposition: represented
      result_indexes:
      - 0
      reason: Confirms strongest effects in ATL
    - source_id: P7-S1-C2
      disposition: represented
      result_indexes:
      - 0
      reason: Provides peak t-value for extra-ATL regions
    - source_id: P7-S1-C3
      disposition: represented
      result_indexes:
      - 0
      reason: Quantifies voxels in ATL
    - source_id: P7-S1-C4
      disposition: represented
      result_indexes:
      - 0
      reason: Describes extent of the ATL cluster
    - source_id: P7-S1-C5
      disposition: represented
      result_indexes:
      - 1
      reason: Establishes effect of controlling for PhonErr
    - source_id: P7-S1-C6
      disposition: represented
      result_indexes:
      - 1
      reason: Confirms ATL effect remains strong
    - source_id: P7-S1-C7
      disposition: represented
      result_indexes:
      - 2
      reason: Establishes effect of controlling for NVcomp
    - source_id: P7-S1-C8
      disposition: represented
      result_indexes:
      - 2
      reason: Confirms ATL cluster remains
    - source_id: P7-S1-C9
      disposition: represented
      result_indexes:
      - 2
      reason: Identifies loss of effect in PFC and pMTG
    - source_id: P7-S1-C10
      disposition: represented
      result_indexes:
      - 2
      reason: Conclusion regarding pre-lexical processes
    - source_id: P7-S1-C11
      disposition: represented
      result_indexes:
      - 3
      reason: Establishes analysis controlling for lesion volume
    - source_id: P7-S2-C6
      disposition: represented
      result_indexes:
      - 1
      reason: Provides peak t-value for PhonErr filtered analysis
    - source_id: P7-S2-C12
      disposition: represented
      result_indexes:
      - 2
      reason: Provides peak t-value for NVcomp filtered analysis
    - source_id: P8-S1-C1
      disposition: represented
      result_indexes:
      - 3
      reason: Identifies voxels associated with SemPlus after lesion volume control
    - source_id: P8-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes results of a previous study
    - source_id: P8-S1-C6
      disposition: represented
      result_indexes:
      - 4
      reason: Establishes association after factoring out BA 22
    - source_id: P8-S1-C7
      disposition: represented
      result_indexes:
      - 5
      reason: Establishes null effect after factoring out BA 21
    - source_id: P8-S1-C15
      disposition: represented
      result_indexes:
      - 3
      reason: Provides peak t-value for lesion volume filtered analysis
    - source_id: P9-S1-C4
      disposition: repeated
      result_indexes:
      - 0
      - 2
      reason: Discussion restatement of ATL association and NVcomp result
    - source_id: P9-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discusses the benefit of the new variable definition
    - source_id: P9-S1-C8
      disposition: repeated
      result_indexes:
      - 3
      reason: Discussion restatement of lesion volume control
    - source_id: P9-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discusses statistical power issues
    - source_id: P9-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Compares current study to original study's power
    - source_id: P9-S2-C2
      disposition: repeated
      result_indexes:
      - 3
      reason: Discussion restatement of lesion volume result
    - source_id: P9-S2-C6
      disposition: represented
      result_indexes:
      - 6
      reason: Establishes null effect in Wernicke's area
    - source_id: P9-S2-C7
      disposition: represented
      result_indexes:
      - 0
      reason: Identifies effects in anterior STG
    - source_id: P9-S2-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Correlation between BA 22 and BA 21 damage
    - source_id: P9-S2-C12
      disposition: repeated
      result_indexes:
      - 5
      reason: Discussion restatement of BA 21 factoring result
    - source_id: P9-S2-C13
      disposition: repeated
      result_indexes:
      - 4
      reason: Discussion restatement of BA 22 factoring result
    - source_id: P9-S3-C7
      disposition: repeated
      result_indexes:
      - 0
      reason: Discussion restatement of L-ATL indispensability
    - source_id: P9-S3-C8
      disposition: repeated
      result_indexes:
      - 6
      reason: Discussion restatement of Wernicke's area null result
    - source_id: P9-S3-C9
      disposition: repeated
      result_indexes:
      - 0
      reason: Discussion restatement of extra-ATL clusters
    - source_id: P9-S4-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: States that expectations for BA 37/45/46 were not confirmed
    - source_id: P9-S4-C5
      disposition: represented
      result_indexes:
      - 3
      reason: States extra-ATL clusters were eliminated by lesion volume control
    - source_id: P10-S3-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes results of a previous study (Antonucci et al., 2008)
    - source_id: P10-S3-C12
      disposition: repeated
      result_indexes:
      - 2
      reason: Discussion restatement of NVcomp result
    - source_id: P10-S4-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive behavioral data
    - source_id: P10-S4-C6
      disposition: represented
      result_indexes:
      - 2
      reason: Confirms NVcomp eliminated extra-ATL associations
    - source_id: P10-S4-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes lesion coverage limitations
    - source_id: P10-S4-C10
      disposition: represented
      result_indexes:
      - 0
      - 2
      reason: Confirms supra-threshold voxels in both un- and filtered analyses
    - source_id: P11-S2-C3
      disposition: repeated
      result_indexes:
      - 0
      - 2
      - 6
      reason: Summary restatement of L-ATL and BA 22 results
    - source_id: P11-S2-C4
      disposition: repeated
      result_indexes:
      - 3
      - 4
      - 5
      reason: Summary restatement of robustness results
    unresolved_coverage:
    - source_id: P1-S1-C12
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P3-S4-C4
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P7-S1-C6
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P7-S1-C10
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P7-S1-C11
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P8-S2-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S3-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S4-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S2-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C12
    - P2-S1-C8
    - P2-S1-C9
    - P2-S1-C10
    - P2-S2-C5
    - P2-S3-C4
    - P2-S3-C5
    - P2-S3-C7
    - P3-S2-C10
    - P3-S4-C4
    - P4-S4-C5
    - P5-S1-C11
    - P5-S2-C8
    - P5-S2-C9
    - P5-S2-C10
    - P5-S2-C13
    - P5-S2-C15
    - P5-S2-C16
    - P6-S1-C2
    - P6-S1-C3
    - P6-S1-C4
    - P6-S1-C5
    - P6-S1-C16
    - P6-S2-C7
    - P6-S2-C8
    - P7-S1-C2
    - P7-S1-C3
    - P7-S1-C4
    - P7-S2-C6
    - P7-S2-C12
    - P8-S1-C4
    - P8-S1-C15
    - P8-S2-C8
    - P9-S1-C4
    - P9-S1-C7
    - P9-S1-C8
    - P9-S1-C9
    - P9-S1-C10
    - P9-S2-C2
    - P9-S2-C7
    - P9-S2-C11
    - P9-S2-C12
    - P9-S2-C13
    - P9-S3-C7
    - P9-S3-C8
    - P9-S3-C9
    - P9-S3-C11
    - P9-S4-C4
    - P9-S4-C5
    - P9-S4-C7
    - P10-S3-C3
    - P10-S3-C12
    - P10-S4-C5
    - P10-S4-C6
    - P10-S4-C8
    - P10-S4-C10
    - P11-S2-C3
    - P11-S2-C4
    - P11-S2-C6
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-5-1
    - TABLE-2-page-5-2
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P3-S4-C6
      recruited_sample:
      - P4-S1-C6
      eligibility:
      - P3-S4-C6
      imaging_provenance:
      - P4-S1-C4
      - P4-S1-C5
      - P4-S3-C9
      imaging_timing:
      - P3-S4-C10
      outcome_timing:
      - P3-S4-C9
      outcome_definition: []
      validation:
      - P1-S1-C10
      analysis_restrictions: []
      dependent_variable_statement:
      - P2-S1-C5
      - P2-S1-C6
      - P5-S2-C5
      - P7-S1-C11
      limitations: []
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles: []
      explicitly_not_adjusted: []
      descriptive_personal_factors: []
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: internal_cross_validation
    held_selections:
    - slot: dependent_variable_statement
      source_id: P5-S2-C13
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S2-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S2-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C12
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C15
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S2-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S2-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S2-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S1-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S2-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S2-C12
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S2-C13
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S2-C14
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P2-S1-C2
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P3-S2-C9
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P9-S1-C1
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: outcome_definition
      source_ids:
      - P4-S1-C14
      - P4-S1-C15
      - P4-S1-C16
      - P4-S2-C2
      - P4-S2-C3
      - P4-S2-C4
      - P4-S2-C5
      - P4-S2-C6
      - P4-S2-C7
      - P4-S2-C8
      - P4-S2-C9
      - P4-S2-C10
      - P9-S1-C2
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: analysis_restrictions
      source_ids:
      - P2-S1-C5
      - P2-S1-C6
      - P2-S1-C7
      - P2-S1-C8
      - P2-S1-C9
      - P2-S1-C10
      - P5-S1-C14
      - P5-S2-C5
      - P6-S1-C17
      - P7-S1-C5
      - P7-S1-C7
      - P7-S1-C11
      - P7-S2-C6
      - P7-S2-C8
      - P8-S1-C5
      - P8-S1-C6
      - P8-S1-C7
      - P8-S1-C8
      - P8-S2-C4
      - P8-S2-C5
      - P8-S2-C8
      - P9-S1-C5
      - P9-S1-C8
      - P9-S2-C11
      - P9-S2-C12
      - P9-S2-C13
      - P9-S2-C14
      - P9-S3-C11
      - P9-S4-C5
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: limitations
      source_ids:
      - P3-S3-C3
      - P3-S3-C4
      - P3-S3-C5
      - P3-S3-C6
      - P3-S3-C7
      - P3-S3-C8
      - P3-S3-C9
      - P3-S3-C10
      - P3-S3-C11
      - P5-S3-C7
      - P5-S3-C8
      - P5-S3-C9
      - P5-S3-C10
      - P6-S1-C5
      - P6-S1-C6
      - P6-S1-C7
      - P9-S3-C11
      - P9-S4-C6
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: adjustment_roles
      source_ids:
      - P2-S1-C6
      - P2-S1-C7
      - P4-S2-C7
      - P4-S3-C7
      - P5-S2-C5
      - P7-S1-C5
      - P7-S1-C7
      - P7-S1-C11
      - P7-S2-C6
      - P7-S2-C8
      - P8-S1-C5
      - P8-S1-C6
      - P8-S1-C7
      - P8-S1-C8
      - P8-S2-C4
      - P8-S2-C5
      - P8-S2-C8
      - P9-S1-C5
      - P9-S1-C8
      - P9-S2-C11
      - P9-S2-C12
      - P9-S2-C13
      - P9-S2-C14
      - P9-S3-C11
      - P9-S4-C5
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: descriptive_personal_factors
      source_ids:
      - P3-S4-C7
      - P3-S4-C8
      - P3-S4-C9
      - P3-S4-C10
      - P3-S4-C11
      - P4-S1-C6
      - P4-S1-C7
      - P4-S1-C8
      - P4-S1-C9
      - P4-S1-C10
      - P5-S2-C8
      - P5-S2-C9
      - P5-S2-C10
      - P5-S2-C11
      - P5-S2-C12
      - P5-S2-C13
      - P5-S2-C14
      - P5-S2-C15
      - P5-S2-C16
      - P5-S2-C17
      - P6-S1-C3
      - P6-S1-C4
      - P6-S1-C13
      - P6-S1-C14
      - P6-S1-C16
      - P6-S1-C17
      - P6-S1-C18
      - P6-S1-C19
      - P7-S1-C1
      - P7-S1-C2
      - P7-S1-C3
      - P7-S1-C4
      - P7-S1-C5
      - P7-S1-C6
      - P7-S1-C7
      - P7-S1-C8
      - P7-S1-C9
      - P7-S1-C10
      - P7-S1-C11
      - P7-S1-C12
      - P7-S1-C13
      - P7-S1-C15
      - P7-S2-C1
      - P7-S2-C6
      - P7-S2-C7
      - P7-S2-C8
      - P7-S2-C9
      - P7-S2-C12
      - P8-S1-C1
      - P8-S1-C2
      - P8-S1-C3
      - P8-S1-C4
      - P8-S1-C5
      - P8-S1-C6
      - P8-S1-C7
      - P8-S1-C8
      - P8-S1-C9
      - P8-S1-C10
      - P8-S1-C11
      - P8-S1-C12
      - P8-S1-C15
      - P8-S1-C16
      - P8-S2-C1
      - P8-S2-C4
      - P8-S2-C5
      - P8-S2-C8
      - P9-S1-C1
      - P9-S1-C2
      - P9-S1-C3
      - P9-S1-C4
      - P9-S1-C5
      - P9-S1-C6
      - P9-S1-C7
      - P9-S1-C8
      - P9-S1-C9
      - P9-S1-C10
      - P9-S2-C2
      - P9-S2-C3
      - P9-S2-C4
      - P9-S2-C5
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
      pdf_sha256: d95039d49e60c7e416291ea53fddd868225c2b1786b91dcd74f40737a9f8cecc
      review_sha256: 25effce4dfef35a4146c1c41a0a7b85139882df23847faeee9a3a3cc6867cbd8
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
      - P9-S2-C6
      source_result: Voxels in the pSTG/pMTG generally identified with Wernicke's
        area yielded very low t-values, indicating that lesions had no measurable
        impact on semantic error scores (SemPlus).
      result_status: not_detected
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The source (P9-S2-C6) explicitly describes the VLSM analysis of
            SemPlus errors in the pSTG/pMTG region, matching the selected analysis
            label and evidence ID.
          source_ids:
          - P9-S2-C6
          - P5-S1-C15
        direction:
          answer: fits
          reason: The source states that lesions in this region 'yielded very low
            t-values, indicating that lesions had no measurable impact', which aligns
            with the 'no_effect' direction in the draft.
          source_ids:
          - P9-S2-C6
        construct:
          answer: fits
          reason: The exposure is correctly identified as lesions in Wernicke's area
            (pSTG/pMTG) and the outcome as semantic error scores (SemPlus). The patient
            measurement is correctly identified as template_lesion_overlap (VLSM),
            not patient_diffusion.
          source_ids:
          - P9-S2-C6
          - P4-S2-C2
          - P5-S1-C15
        qualifications:
          answer: fits
          reason: The draft correctly includes the qualification that the semantic
            error measure (SemPlus) was broadly defined, which is a key context for
            this null finding as described in P9-S2-C3 and P4-S2-C2.
          source_ids:
          - P9-S2-C3
          - P4-S2-C2
        missing_material_caveat:
          answer: fits
          reason: The draft includes the limitation that the finding is specific to
            chronic patients, which is a material caveat discussed in P9-S3-C4 and
            P9-S3-C6 regarding the discrepancy with acute stroke findings.
          source_ids:
          - P9-S3-C4
          - P9-S3-C6
      optional_pending: []
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    normalizations: []
    analysis_identity:
      id: R007
      exposure:
        text: lesions in Wernicke's area (pSTG/pMTG)
      outcome:
        text: semantic error scores
      analysis_label: VLSM of SemPlus errors (null finding)
      relation: association
      evidence_ids:
      - P9-S2-C6
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
        pdf_sha256: d95039d49e60c7e416291ea53fddd868225c2b1786b91dcd74f40737a9f8cecc
        source_review: _compare/relationships-2026-11-16/review-current/Walker2011
        source_status_sha256: b594e95a0da18d991bc3093a78ac2bfc4760d8cddc86eab389d5245d9679dc1c
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P3-S4-C6:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: d95039d49e60c7e416291ea53fddd868225c2b1786b91dcd74f40737a9f8cecc
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 613a9ba90ee187042bee816c8ba6e3e70c2971cec87f406cbf17fceedbeda27c
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S4-C6
          page: 3
          text_layer_sha256: 613a9ba90ee187042bee816c8ba6e3e70c2971cec87f406cbf17fceedbeda27c
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Participants

          Participants were 64 individuals (42% females; 48% African

          American) with conﬁrmed left hemisphere stroke, who currently

          or initially presented with clinically apparent aphasia.'
        anchor_text: 'Participants

          Participants were 64 individuals (42% females; 48% African

          American) with conﬁrmed left hemisphere stroke, who currently

          or initially presented with clinically apparent aphasia.'
        excluded_fragments: []
        image_sha256: 9d06a4a29a53de1f70d4133796d1f7d3e5a7b3c5ce73a267fdd1fe0d62af79b6
        transcription: 'Participants


          Participants were 64 individuals (42% females; 48% African American) with
          confirmed left hemisphere stroke, who currently or initially presented with
          clinically apparent aphasia'
      P3-S4-C9:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: d95039d49e60c7e416291ea53fddd868225c2b1786b91dcd74f40737a9f8cecc
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 517eb3c93fa7d6ad0654a9f523357e1cb91741fb3be462f3b84f34242ea993a6
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S4-C9
          page: 3
          text_layer_sha256: 517eb3c93fa7d6ad0654a9f523357e1cb91741fb3be462f3b84f34242ea993a6
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Their mean

          number of months post–stroke at time of PNT performance was 68

          (range 1–381).'
        anchor_text: 'Their mean

          number of months post–stroke at time of PNT performance was 68

          (range 1–381).'
        excluded_fragments: []
        image_sha256: 910eeaf351c4ea762cc53bf11a9ebe7316fa4490f0d0fb667bbe4e6a0adeb40f
        transcription: '. Their mean

          number of months post–stroke at time of PNT performance was 68

          (range 1–381)'
      P3-S4-C10:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: d95039d49e60c7e416291ea53fddd868225c2b1786b91dcd74f40737a9f8cecc
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: cec73c1dc415576ea178c6790653ab246fbd8c74db656f89a55dff652e19e8a3
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S4-C10
          page: 3
          text_layer_sha256: cec73c1dc415576ea178c6790653ab246fbd8c74db656f89a55dff652e19e8a3
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'The most acute patient performed the PNT 6 weeks

          post-stroke and was imaged 8 weeks post-stroke; 59 of 64 subjects

          were at least 6 months post.'
        anchor_text: 'The most acute patient performed the PNT 6 weeks

          post-stroke and was imaged 8 weeks post-stroke; 59 of 64 subjects

          were at least 6 months post.'
        excluded_fragments: []
        image_sha256: 07eb0212e1c0e85e19e40d4b942c6eb8954f43e4a27eaafb0a685f01b35e6855
        transcription: '. The most acute patient performed the PNT 6 weeks

          post-stroke and was imaged 8 weeks post-stroke; 59 of 64 subjects

          were at least 6 months post'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 9
  quote: 'Instead, as in Schwartz

    et al. (2009), we found that voxels in the pSTG/pMTG generally

    identiﬁed with Wernicke’s area yielded very low t-values, indicat-

    ing that lesions had no measurable impact on semantic error

    scores.'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-26'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
