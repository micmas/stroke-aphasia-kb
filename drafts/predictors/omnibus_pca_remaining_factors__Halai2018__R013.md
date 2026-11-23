---
id: omnibus_pca_remaining_factors
name: omnibus PCA remaining factors
kind: predictor
findings:
- id: f1
  target: tissue_concentration
  target_kind: impairment
  claim: The remaining factors from the omnibus PCA (excluding phonological working
    memory, semantic ability, and speech quanta) did not correlate significantly with
    T1-weighted tissue concentration.
  direction: no_effect
  relationship: correlational
  method: VBCM
  sample:
    n: not_reported
    population: chronic stroke patients with impairment in producing and/or understanding
      spoken language
    phase: not_reported
    time_post_onset: at least 12 months post-stroke at the time of scanning and assessment
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - VBCM assumes that lower T1-weighted intensity is related to tissue damage or atrophy
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Patient factor scores from an omnibus principal component
    analysis (PCA) that fused naming error types and neuropsychological test results,
    specifically those factors excluding phonological working memory, semantic ability,
    and speech quanta. analysis included lesion volume, age, and years of education
    as nuisance regressors. Additional metadata has not been transcribed; review the
    pending-field flags before approval. PDF image reading (P2-S4-C7, two-model agreement,
    human verification pending): . All patients were at least 12 months post-

    stroke at the time of scanning and assessment, were native English

    speakers with normal or corrected-to-normal hearing and vision (see

    Supplementary Table 1 for demographic details) Original text-layer quotation is
    preserved below.'
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
    - proposed_concept:tissue_concentration
  citation: '@Halai2018'
  source_passages:
  - section: Original source P5-S2-C7
    page: 5
    quote: 'The remaining factors did not correlate signiﬁcantly with tissue con-

      centration.

      3.5.'
    supports: claim
  - section: Original source P5-S1-C11
    page: 5
    quote: 'The omnibus PCA components were simultaneously entered for le-

      sion analysis which included lesion volume, age and years in education

      as nuisance regressors.'
    supports: method
  - section: Original source P2-S4-C4
    page: 2
    quote: 'Participants

      Fifty-one chronic stroke patients (either ischaemic or haemorrhagic)

      were recruited into the current study, who had impairment in produ-

      cing and/or understanding spoken language.'
    supports: sample
  - section: Original source P2-S4-C7
    page: 2
    quote: 'All patients were at least 12 months post-

      stroke at the time of scanning and assessment, were native English

      speakers with normal or corrected-to-normal hearing and vision (see

      Supplementary Table 1 for demographic details).'
    supports: sample
  - section: Original source P3-S4-C13
    page: 3
    quote: 'For the neural correlate ana-

      lysis, we are assuming that lower T1-weighted intensity is related to

      tissue damage or atrophy.'
    supports: limitation
predictor_type: imaging_metric
short_definition: Patient factor scores from an omnibus principal component analysis
  (PCA) that fused naming error types and neuropsychological test results, specifically
  those factors excluding phonological working memory, semantic ability, and speech
  quanta.
assessment: []
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-24'
relationship_review:
  paper: Halai2018
  proposal_id: R013
  review_status_sha256: 7dc8462aa8a4cfa0d568cf199e6df0968194f7b14bf3e89547d730838069a35c
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 7f20273b9607c3fad8b845f8237d1af68da141e992b478b1fa2c5773b653677c
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 7f20273b9607c3fad8b845f8237d1af68da141e992b478b1fa2c5773b653677c
        A/passages.json: d9f7af594538f7fa7f04922efed095e191b11da0c25f57a56f672ebcaa2aa351
        A/raw.json: d0a9005a5401a35601bd1cee795d328feaedfad581f2fad2f51c457e4127cafe
        A/source-units.json: d62cfc67a913de8f0453114c9781a515011e17f1ecce6b491f8b3ac413064e17
        A/full-source-units.json: 44a6e9f8d49db495251b661f852a862b50ec3c9456e6bee76a33504ec5c48819
        A/meta.json: e33b4b05dc21f253a2da16d62a2862128db3e795fddd64e9139f1ada4a9be38b
        A/table-images/TABLE-1-page-5-2.png: 49e96cda1d3a19d3c3d83635ac20ed65f43bbf643a5b3521f53f3fc83af27b07
        A/table-images/page-6.png: f28496116c228bf5104bfe1c04113a61b9564ba9287bf6b9c54fa64d83cc5f7a
        A/table-images/page-7.png: 6bf1a2edf71e05a0f347c975fbc6304383bc4d617746da38ac8cab36ab1e3147
        A/table-images/page-5.png: 41168cb538c66026755c89305301f1b68c116be04723e702522fc51e5186efcf
        A/table-images/TABLE-3-page-6-1.png: 631ac7a156be13f8e2bbcb3224acefa39bdfffeeef27801d843b3e938adb0f27
        A/table-images/manifest.json: 7f6bf900265e395267c79dcf456215b02f02c041e6a7abb879cc6e1ea67f9711
        A/table-images/TABLE-4-page-7-1.png: 8fb0fad9337e4be2cde00ce6ccbaffc4d09ed10857b47a5c8f67706eae2343e9
        A/table-images/TABLE-2-page-5-1.png: de20f05a37fe2b940fbabee8447edce03d09700f18c2aaec6d6564b5cc2249b3
        A/clauses/window-03/raw.json: 4d296282dab4c31cd5830d290af77f75ce6fa53479cace27eed43bf5a3d417cb
        A/clauses/window-03/prompt.txt: 31574cbfa99403bb18ba62d32cf449d5159a173edcb005f8abb60ca7b11f7fb2
        A/clauses/window-03/meta.json: 5000fc7f836434d451338cff70c7151e8f4c94102dcdc8997684366a82505d49
        A/clauses/window-04/raw.json: ac330531a6675f5c6adf873d38a69a005f7a506b28246c0b318a298c71c9db40
        A/clauses/window-04/prompt.txt: 87b3b56ee04f0850754a8935522555d2a22edeab413687fec79f9dd85b1064a4
        A/clauses/window-04/meta.json: aa4e28dc66130150e04378bf252c3c9893dafb0a44119e4235852cb75616660f
        A/clauses/window-05/raw.json: c5a28a62e094744857d1cd7189e9a927e2225794dc7f894172e09ff79fa06cd3
        A/clauses/window-05/prompt.txt: aad84bb87de9f4f0c9a15e34db443506f21ca5c0816a43dbb6b23b03686acc7b
        A/clauses/window-05/meta.json: a352c89faaca3143d94426512407dd83b0b0000b589846f83e92a74cf09c628e
        A/clauses/window-02/raw.json: a9b422d96cd1906b1e4f47050e0435017f34d467d7be3dc9d9cbb379dc64d061
        A/clauses/window-02/prompt.txt: 15765a0aeaa1c09fc1a2bade36e710501ba5cb9c47ba1c505c4e7539d61578dd
        A/clauses/window-02/meta.json: 0162b4a8caf8fc9ea77fef4c024a32dafafcfef46c493ab36517e3759e813b3d
        A/clauses/window-07/raw.json: 091a3a4d8ae513c0e01824e82bba5b98262c74f35ed9e37242a848a02c0e74da
        A/clauses/window-07/prompt.txt: 8f2e264f58c2a18d7bff261eaf7814160fe1915730118316143285484ce62c9a
        A/clauses/window-07/meta.json: 10fa65c968976738b8af20d811c52f2d025db6455b2eb724722a900898cafb67
        A/clauses/window-01/raw.json: a6b4c4704cf53b2bd89821ddd308e4444b0a42b9d247ce338155afbf3afd000b
        A/clauses/window-01/prompt.txt: 571f3400443648311a8a140a733bc0631dd25295f7cab9600e82f507396a705a
        A/clauses/window-01/meta.json: c3bbc451e9d3210145064c29a62fffe53cb5e68757c8d6bbdb53f490a7bcbd5a
        A/clauses/window-06/raw.json: ec5b71ef2481d0796224730373cc90c1abb5a681da3e65ba7cb20a7a8ce93305
        A/clauses/window-06/prompt.txt: b3b502fdbcecd1eedb0648bcfc54ca36504aab86fdae8168a130b047dffbf25d
        A/clauses/window-06/meta.json: 8969cfcefb25095eef4c3584688379f218afedac13b1589031b9db1eb3b5e27b
        A/clauses/window-08/raw.json: 3d8c291f1c6eb86702a7450439bcb43ca524c71502a16eb977e98816752d1565
        A/clauses/window-08/prompt.txt: 44a842de962fc37b6141171e5fe1011e44e2929082c7ee177584498c6fe568d2
        A/clauses/window-08/meta.json: 5cfb611b562fe654e35eea0e9802942cd00abc48f0f51862f036927a45fe7671
        A/tables/TABLE-3-page-6-3/raw.json: 7283dcb40df65f1658306a7e8f54cc5a639c881f2392dcabe5adc3181288c2ec
        A/tables/TABLE-3-page-6-3/prompt.txt: 82f4c61ac6429e76090e8cb97d693cf55edfd52d69ddc22eed9565120bfdf021
        A/tables/TABLE-3-page-6-3/meta.json: 8ab919943689c3c433d0057c4844a4d94bbf7d737c1a2a44b37e6f8f7d18a5b7
        A/tables/TABLE-1-page-5-2/raw.json: 3caaa8e8d0597f192696af475d8e76023ea8a7054cacee3338a7301629385f7a
        A/tables/TABLE-1-page-5-2/prompt.txt: 06f2371ec00e647d314f93ce5b4bf866406072b9f4c0e581804d42aacea6db9b
        A/tables/TABLE-1-page-5-2/meta.json: e7cb32970ac10111e3654b6379b3e0ba30d09367904236cf72d9b7daed5b52c0
        A/tables/TABLE-2-page-5-1/raw.json: 7b2c00c573e44812ca85d621689d8ea6f2418823bf39f8578fad50450ad9e441
        A/tables/TABLE-2-page-5-1/prompt.txt: 39628e577f8f1ad78c21ef322dd676d37158abd212948895ac3f7060113c73c5
        A/tables/TABLE-2-page-5-1/meta.json: 36ef14469913f6b47ed5822f894a5159e311ae906121b6f4c7afc843a12ac2b9
        A/tables/TABLE-4-page-7-4/raw.json: 11955ab3d967ff9fcd24ef008fc4d7c07a3bf3ddddd5b6ae79b932f24a15f03c
        A/tables/TABLE-4-page-7-4/prompt.txt: 6464e8dc229fc2513feeb410c9e0540a81676474d8ef3e74c4a8fdef09b408f0
        A/tables/TABLE-4-page-7-4/meta.json: 0fe3db84ffc3af70d64375c4a000dea046306fa8b534865921757f3ce9747782
        B/passages.json: d9f7af594538f7fa7f04922efed095e191b11da0c25f57a56f672ebcaa2aa351
        B/raw.json: 13d76868b07ddd8bd0b7f8e34c951432fffa8a46d2421e407b3f2aba4c1b3e9c
        B/source-units.json: d62cfc67a913de8f0453114c9781a515011e17f1ecce6b491f8b3ac413064e17
        B/full-source-units.json: 44a6e9f8d49db495251b661f852a862b50ec3c9456e6bee76a33504ec5c48819
        B/meta.json: f6b6d3899bfcf7f0d803a2d7c42e054999696f466d4938248ee74a7f9278abc2
        B/table-images/TABLE-1-page-5-2.png: 49e96cda1d3a19d3c3d83635ac20ed65f43bbf643a5b3521f53f3fc83af27b07
        B/table-images/page-6.png: f28496116c228bf5104bfe1c04113a61b9564ba9287bf6b9c54fa64d83cc5f7a
        B/table-images/page-7.png: 6bf1a2edf71e05a0f347c975fbc6304383bc4d617746da38ac8cab36ab1e3147
        B/table-images/page-5.png: 41168cb538c66026755c89305301f1b68c116be04723e702522fc51e5186efcf
        B/table-images/TABLE-3-page-6-1.png: 631ac7a156be13f8e2bbcb3224acefa39bdfffeeef27801d843b3e938adb0f27
        B/table-images/manifest.json: 0d2438a498d26ce16adae8c28204de608dba386ca79b1337ca6b7f5201abf59a
        B/table-images/TABLE-4-page-7-1.png: 8fb0fad9337e4be2cde00ce6ccbaffc4d09ed10857b47a5c8f67706eae2343e9
        B/table-images/TABLE-2-page-5-1.png: de20f05a37fe2b940fbabee8447edce03d09700f18c2aaec6d6564b5cc2249b3
        B/clauses/window-03/raw.json: fbf66420b3834575042522feadf0359d0bc4790ed55dae370d1dc18ae8b69832
        B/clauses/window-03/prompt.txt: 31574cbfa99403bb18ba62d32cf449d5159a173edcb005f8abb60ca7b11f7fb2
        B/clauses/window-03/meta.json: c793acde4a4378237ce1384588f3898859cdbcf0e3aa09298e66ecce5e374061
        B/clauses/window-04/raw.json: 45759878ef53f378caf31379af60b08af92f895557c0bbe73202a446b30aae64
        B/clauses/window-04/prompt.txt: 87b3b56ee04f0850754a8935522555d2a22edeab413687fec79f9dd85b1064a4
        B/clauses/window-04/meta.json: f34cf6522d7088eac9042dad768bb2048f60110dda08a3103a775ccb5bcdf314
        B/clauses/window-05/raw.json: 2a63abf45a07d2604f37803d10fa938e5d3a2432faa9f2c39159ec5358dead08
        B/clauses/window-05/prompt.txt: aad84bb87de9f4f0c9a15e34db443506f21ca5c0816a43dbb6b23b03686acc7b
        B/clauses/window-05/meta.json: 831e8d6e38840b2d479a3df644b748457881105d5de2d9a19d74d0ce21e1242f
        B/clauses/window-02/raw.json: f9d31d976b1e1455d09762e7b94710e42525d68f8ed7a007ff53ae3f604dd9e0
        B/clauses/window-02/prompt.txt: 15765a0aeaa1c09fc1a2bade36e710501ba5cb9c47ba1c505c4e7539d61578dd
        B/clauses/window-02/meta.json: 9a092c976064b295e5f932aa8b56cdc8269c6b56829cfd0c1b522303e439fa58
        B/clauses/window-07/raw.json: 0d52d04cab3210a41e7288d4f69c1415eecd9cea499827d4ba1e16217c46b245
        B/clauses/window-07/prompt.txt: 8f2e264f58c2a18d7bff261eaf7814160fe1915730118316143285484ce62c9a
        B/clauses/window-07/meta.json: 05c228254ddc78c3235cb94ced5af6c85a0f00bff5d1ca1a244d3f3b2e8bb736
        B/clauses/window-01/raw.json: c91061056d6e7673cbaa13a8e7be5f543cdfa92ac810efc73eaf1bd5bd9410d4
        B/clauses/window-01/prompt.txt: 571f3400443648311a8a140a733bc0631dd25295f7cab9600e82f507396a705a
        B/clauses/window-01/meta.json: c0dec8ea80add5d8aeec42ddadbdab9ac4166d6aa0b0cac299f46d8938d04e56
        B/clauses/window-06/raw.json: 2bb9b8a38625502d690f195ebf8be27f96013ef74fad2ed9fdd8115c5e4e4996
        B/clauses/window-06/prompt.txt: b3b502fdbcecd1eedb0648bcfc54ca36504aab86fdae8168a130b047dffbf25d
        B/clauses/window-06/meta.json: 64b5ae99799f6fe7ccfb7c3a9285e4262871ff8d335b4ec45ef530754938c0fc
        B/clauses/window-08/raw.json: 8fb935288519ee541ea4c6cca545ca0787f285fe701e0aba88a8f097fec3880b
        B/clauses/window-08/prompt.txt: 44a842de962fc37b6141171e5fe1011e44e2929082c7ee177584498c6fe568d2
        B/clauses/window-08/meta.json: 36a4199ff579fdfda09030b82365bdff82be9aa8c8b1ecaa0da0553545eddda9
        B/tables/TABLE-3-page-6-3/raw.json: b9a57712fa74dd93afe5ec9871502e1e5a9dfcb5af1ebbaae0e8f453ee804d81
        B/tables/TABLE-3-page-6-3/prompt.txt: 82f4c61ac6429e76090e8cb97d693cf55edfd52d69ddc22eed9565120bfdf021
        B/tables/TABLE-3-page-6-3/meta.json: 27bcde50df968370869f8e50d186f16ffd26b2d226fa4a550db3f85fa37ed0d3
        B/tables/TABLE-1-page-5-2/raw.json: b7cc47ee2ff2a3bf02f1a74e1f54ba12205f3191bd1b1092401dfeaaa8767f19
        B/tables/TABLE-1-page-5-2/prompt.txt: 06f2371ec00e647d314f93ce5b4bf866406072b9f4c0e581804d42aacea6db9b
        B/tables/TABLE-1-page-5-2/meta.json: 6ca57d9a578fd0efa2bf5fc6b2f00d8137192faa9e731d7463697fd06c3fde6c
        B/tables/TABLE-2-page-5-1/raw.json: 5ba7313cdc8ae97e370f781b800c305619f27f011d4ff8a786e9dfa0da790dc1
        B/tables/TABLE-2-page-5-1/prompt.txt: 39628e577f8f1ad78c21ef322dd676d37158abd212948895ac3f7060113c73c5
        B/tables/TABLE-2-page-5-1/meta.json: d0f2cc21b2cac2cf87c64cddad93bec16462c2b5a153592398f951cfa51409d9
        B/tables/TABLE-4-page-7-4/raw.json: 7d7380c88d55f6421f18d790781f12a2cb91370d87ec180d08ed219c1b982362
        B/tables/TABLE-4-page-7-4/prompt.txt: 6464e8dc229fc2513feeb410c9e0540a81676474d8ef3e74c4a8fdef09b408f0
        B/tables/TABLE-4-page-7-4/meta.json: 1a645ea19c5af8e32ac58d40feb469aec4818eb97e90e86cb840f753985ea9d9
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
      pdf_sha256: 7f20273b9607c3fad8b845f8237d1af68da141e992b478b1fa2c5773b653677c
      source_review: _compare/relationships-2026-11-16/review-current/Halai2018
      source_status_sha256: 54e46bb8c91a9ff1af88573d9198dfa480a15e8bb9258c75d3cd50cf0da2f994
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R013
    exposure:
      text: remaining factors (excluding phonological working memory, semantic ability,
        speech quanta)
    outcome:
      text: tissue concentration
    analysis_label: VBCM (omnibus PCA factors)
    relation: association
    evidence_ids:
    - P5-S2-C7
    qualifier_ids:
    - P5-S1-C11
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 7f20273b9607c3fad8b845f8237d1af68da141e992b478b1fa2c5773b653677c
      source_review: _compare/relationships-2026-11-16/review-current/Halai2018
      source_status_sha256: 54e46bb8c91a9ff1af88573d9198dfa480a15e8bb9258c75d3cd50cf0da2f994
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P1-S1-C11
      - Result passage disposed without unit P1-S1-C9
      - Accounting without a linked unit P1-S2-C3
      - Accounting without a linked unit P1-S2-C4
      - Accounting without a linked unit P1-S2-C5
      - Unaccounted source passage P1-S2-C4
      - Unaccounted source passage P1-S2-C3
      - Unaccounted source passage P1-S2-C5
      - Result passage disposed without unit P3-S1-C5
      - Result passage disposed without unit P4-S1-C10
      - Result passage disposed without unit P4-S1-C8
      - Result passage disposed without unit P4-S1-C9
      - Result passage disposed without unit P5-S1-C13
      - Accounting without a linked unit P5-S2-C4
      - Accounting without a linked unit P5-S2-C5
      - Accounting without a linked unit P5-S2-C6
      - Accounting without a linked unit P5-S2-C7
      - Unaccounted source passage P5-S2-C6
      - Unaccounted source passage P5-S2-C4
      - Unaccounted source passage P5-S2-C7
      - Unaccounted source passage P5-S2-C5
      - Result passage disposed without unit P6-S1-C2
      - Result passage disposed without unit P6-S1-C3
      - Accounting without a linked unit P6-S1-C6
      - Accounting without a linked unit P6-S1-C9
      - Unaccounted source passage P6-S1-C9
      - Unaccounted source passage P6-S1-C6
      - Result passage disposed without unit P6-S1-C11
      - Result passage disposed without unit P6-S2-C3
      - Result passage disposed without unit P6-S3-C5
      - Result passage disposed without unit P7-S1-C2
      - Result passage disposed without unit P7-S1-C7
      - Result passage disposed without unit P7-S2-C3
      - Result passage disposed without unit P7-S2-C5
      - Result passage disposed without unit P7-S2-C7
      - Result passage disposed without unit P7-S2-C8
      - Result passage disposed without unit P7-S2-C9
      - Result passage disposed without unit P7-S2-C10
      - Result passage disposed without unit P8-S1-C2
      - Result passage disposed without unit P8-S1-C4
      - Accounting without a linked unit P8-S1-C5
      - Accounting without a linked unit P8-S1-C6
      - Accounting without a linked unit P8-S1-C8
      - Accounting without a linked unit P8-S1-C9
      - Accounting without a linked unit P8-S2-C2
      - Unaccounted source passage P8-S1-C5
      - Unaccounted source passage P8-S1-C8
      - Unaccounted source passage P8-S2-C2
      - Unaccounted source passage P8-S1-C9
      - Unaccounted source passage P8-S1-C6
      unattached_null_or_qualifier_ids:
      - P5-S2-C7
      - P6-S1-C11
      - P6-S2-C3
      - P7-S1-C2
      - P8-S1-C9
      suppressed_nonrepresented_units: 23
      default_disposition_count_requires_completeness_check: 153
      unselected_timing_passages:
      - P2-S4-C4
      - P2-S4-C8
      - P2-S4-C9
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P4-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P6-S1-C3
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      empty_frame_slots_require_confirmation:
      - validation
      - personal_factors
      - tested_personal_effects
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-5-2
      - TABLE-2-page-5-1
      - TABLE-3-page-6-3
      - TABLE-4-page-7-4
      unlinked_tables:
      - TABLE-1-page-5-2
      - TABLE-2-page-5-1
      - TABLE-3-page-6-3
      - TABLE-4-page-7-4
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P4-S1
        - P4-S2
        - P4-S3
        - P5-S1
        - P6-S1
        - P6-S3
        - P7-S3
        - P8-S1
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 7f20273b9607c3fad8b845f8237d1af68da141e992b478b1fa2c5773b653677c
      source_review: _compare/relationships-2026-11-16/review-current/Halai2018
      source_status_sha256: 54e46bb8c91a9ff1af88573d9198dfa480a15e8bb9258c75d3cd50cf0da2f994
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the components obtained from the first PCA, not a measured
        relationship.
    - source_id: P1-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the factors revealed by the omnibus PCA, not a measured relationship.
    - source_id: P1-S2-C3
      disposition: repeated
      result_indexes:
      - 4
      - 13
      reason: Abstract restatement of findings.
    - source_id: P1-S2-C4
      disposition: repeated
      result_indexes:
      - 5
      - 6
      - 14
      reason: Abstract restatement of findings.
    - source_id: P1-S2-C5
      disposition: repeated
      result_indexes:
      - 10
      - 11
      - 12
      reason: Abstract restatement of findings.
    - source_id: P3-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes error category variance for collapsing purposes.
    - source_id: P4-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes lesion overlap map.
    - source_id: P4-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes voxel overlap count.
    - source_id: P4-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes hemisphere confinement of results.
    - source_id: P4-S1-C12
      disposition: represented
      result_indexes:
      - 0
      - 1
      reason: Provides the threshold qualifications for the VBCM analysis.
    - source_id: P4-S1-C13
      disposition: represented
      result_indexes:
      - 0
      - 1
      reason: Directly reports the neural correlates for phonological and omission
        errors.
    - source_id: P4-S1-C14
      disposition: represented
      result_indexes: []
      reason: Null finding for other categories in individual analysis.
    - source_id: P4-S1-C15
      disposition: represented
      result_indexes:
      - 2
      reason: Reports result for simultaneous all-error model.
    - source_id: P4-S2-C1
      disposition: repeated
      result_indexes:
      - 2
      reason: Restatement of simultaneous all-error model result.
    - source_id: P4-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes PCA variance explained.
    - source_id: P4-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes Factor 1 loadings.
    - source_id: P4-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes Factor 2 loadings.
    - source_id: P4-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes Factor 3 loadings.
    - source_id: P4-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes Factor 4 loadings.
    - source_id: P4-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes Factor 5 loadings.
    - source_id: P4-S2-C11
      disposition: represented
      result_indexes:
      - 3
      reason: Reports significant cluster for OmErr in simultaneous VBCM.
    - source_id: P4-S2-C12
      disposition: represented
      result_indexes:
      - 3
      reason: Specifies the anatomical location for the OmErr correlation.
    - source_id: P4-S3-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes omnibus PCA variance explained.
    - source_id: P4-S3-C6
      disposition: repeated
      result_indexes:
      - 0
      - 1
      reason: Figure legend restating individual error results.
    - source_id: P4-S3-C8
      disposition: repeated
      result_indexes:
      - 3
      reason: Figure legend restating OmErr result.
    - source_id: P4-S3-C9
      disposition: represented
      result_indexes: []
      reason: Null findings for Factors 1-4 in simultaneous VBCM.
    - source_id: P5-S1-C3
      disposition: represented
      result_indexes:
      - 4
      reason: Reports relationship between phonological ability and PhonErr.
    - source_id: P5-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes semantic ability factor.
    - source_id: P5-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes phonological working memory factor.
    - source_id: P5-S1-C6
      disposition: represented
      result_indexes:
      - 5
      - 6
      reason: Reports negative loading of omission errors with semantic and working
        memory factors.
    - source_id: P5-S1-C7
      disposition: represented
      result_indexes:
      - 7
      reason: Reports relationship between speech quanta and dysfluency errors.
    - source_id: P5-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes executive-demanding factor.
    - source_id: P5-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes auditory discrimination and circumlocution factors.
    - source_id: P5-S1-C10
      disposition: represented
      result_indexes:
      - 8
      reason: Reports complex loading of SemErr across four factors.
    - source_id: P5-S1-C13
      disposition: represented
      result_indexes:
      - 9
      - 10
      - 11
      reason: Identifies the three factors with significant lesion correlates.
    - source_id: P5-S2-C4
      disposition: represented
      result_indexes:
      - 9
      reason: Specifies anatomical correlate for phonological working memory factor.
    - source_id: P5-S2-C5
      disposition: represented
      result_indexes:
      - 10
      reason: Specifies anatomical correlate for speech quanta factor.
    - source_id: P5-S2-C6
      disposition: represented
      result_indexes:
      - 11
      reason: Specifies anatomical correlate for semantic ability factor.
    - source_id: P5-S2-C7
      disposition: represented
      result_indexes:
      - 12
      reason: Reports null results for remaining factors.
    - source_id: P6-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about previous studies.
    - source_id: P6-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Hypothesis about alternative outcomes.
    - source_id: P6-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement about replication capability.
    - source_id: P6-S1-C6
      disposition: represented
      result_indexes:
      - 13
      - 14
      reason: Reports replication of Walker et al. results for phonological and semantic
        errors.
    - source_id: P6-S1-C9
      disposition: represented
      result_indexes:
      - 15
      reason: Reports result for semantic error model with receptive semantic control.
    - source_id: P6-S1-C11
      disposition: represented
      result_indexes:
      - 16
      reason: Reports result for phonological error model with receptive phonology
        control.
    - source_id: P6-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes replication of Mirman et al. four-factor solution.
    - source_id: P6-S3-C4
      disposition: repeated
      result_indexes:
      - 3
      reason: Figure legend restating omission error result.
    - source_id: P6-S3-C5
      disposition: repeated
      result_indexes:
      - 7
      reason: Figure legend restating dysfluency error result.
    - source_id: P7-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes effect of re-integrating cognitive measures on factor solution.
    - source_id: P7-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Restatement of the five principal components of error patterns.
    - source_id: P7-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Restatement of the seven fused factors.
    - source_id: P7-S2-C7
      disposition: repeated
      result_indexes: []
      reason: Discussion restatement of circumlocution factor independence.
    - source_id: P7-S2-C8
      disposition: repeated
      result_indexes:
      - 4
      reason: Discussion restatement of phonological error alignment.
    - source_id: P7-S2-C9
      disposition: repeated
      result_indexes:
      - 7
      reason: Discussion restatement of speech fluency and dysfluent errors.
    - source_id: P7-S2-C11
      disposition: repeated
      result_indexes:
      - 5
      - 6
      - 8
      reason: Discussion restatement of complex relationships for omission and semantic
        errors.
    - source_id: P7-S2-C12
      disposition: repeated
      result_indexes:
      - 9
      - 10
      - 11
      reason: Discussion restatement of unique lesion correlates.
    - source_id: P7-S3-C1
      disposition: repeated
      result_indexes:
      - 9
      - 10
      - 11
      reason: Discussion restatement of anatomical locations.
    - source_id: P7-S3-C4
      disposition: repeated
      result_indexes:
      - 2
      - 3
      reason: Discussion restatement of omission error association with ATL.
    - source_id: P8-S1-C2
      disposition: repeated
      result_indexes:
      - 8
      reason: Discussion restatement of semantic error complexity.
    - source_id: P8-S2-C2
      disposition: repeated
      result_indexes:
      - 3
      reason: Discussion restatement of omission factor survival in ATL.
    unresolved_coverage:
    - source_id: P4-S1-C14
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P4-S3-C9
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P7-S2-C7
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P7-S1-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P7-S2-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P7-S3-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S1-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S1-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S1-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S1-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S1-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S2-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C9
    - P1-S1-C11
    - P1-S2-C3
    - P1-S2-C4
    - P1-S2-C5
    - P3-S1-C5
    - P4-S1-C8
    - P4-S1-C9
    - P4-S1-C10
    - P4-S1-C12
    - P4-S1-C14
    - P4-S2-C1
    - P4-S2-C3
    - P4-S2-C5
    - P4-S2-C6
    - P4-S2-C7
    - P4-S2-C8
    - P4-S2-C10
    - P4-S3-C2
    - P4-S3-C6
    - P4-S3-C8
    - P4-S3-C9
    - P5-S1-C4
    - P5-S1-C5
    - P5-S1-C8
    - P5-S1-C9
    - P5-S1-C13
    - P6-S1-C1
    - P6-S1-C2
    - P6-S1-C3
    - P6-S2-C3
    - P6-S3-C4
    - P6-S3-C5
    - P7-S1-C2
    - P7-S1-C7
    - P7-S2-C3
    - P7-S2-C5
    - P7-S2-C7
    - P7-S2-C8
    - P7-S2-C9
    - P7-S2-C10
    - P7-S2-C11
    - P7-S2-C12
    - P7-S3-C1
    - P7-S3-C4
    - P7-S3-C6
    - P8-S1-C2
    - P8-S1-C4
    - P8-S1-C5
    - P8-S1-C6
    - P8-S1-C8
    - P8-S1-C9
    - P8-S2-C2
    - P8-S2-C10
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-5-2
    - TABLE-2-page-5-1
    - TABLE-3-page-6-3
    - TABLE-4-page-7-4
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P2-S4-C12
      recruited_sample:
      - P2-S4-C4
      eligibility:
      - P2-S4-C4
      - P2-S4-C5
      - P2-S4-C6
      - P2-S4-C7
      - P2-S4-C10
      imaging_provenance:
      - P3-S4-C3
      imaging_timing:
      - P2-S4-C7
      outcome_timing:
      - P2-S4-C7
      outcome_definition:
      - P3-S2-C3
      - P3-S2-C12
      validation: []
      analysis_restrictions:
      - P2-S4-C6
      - P3-S3-C4
      - P4-S1-C2
      - P4-S1-C3
      - P4-S1-C4
      - P6-S2-C3
      dependent_variable_statement:
      - P3-S4-C12
      - P4-S1-C1
      - P4-S1-C2
      - P4-S1-C3
      limitations:
      - P8-S2-C3
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P4-S1-C6
      - P5-S1-C11
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P2-S4-C8
      - P2-S4-C9
      - P2-S4-C10
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: repeated_patients
    held_selections:
    - slot: dependent_variable_statement
      source_id: P4-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P6-S1-C3
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
      pdf_sha256: 7f20273b9607c3fad8b845f8237d1af68da141e992b478b1fa2c5773b653677c
      review_sha256: 7dc8462aa8a4cfa0d568cf199e6df0968194f7b14bf3e89547d730838069a35c
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
      - P5-S2-C7
      source_result: In the VBCM analysis using omnibus PCA factors, the factors corresponding
        to phonological working memory, semantic ability, and speech quanta showed
        significant correlations with tissue concentration. The remaining factors
        (including those related to executive demand, auditory discrimination, and
        circumlocution) did not reveal significant clusters or correlations with tissue
        concentration.
      result_status: not_detected
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis R013 correctly identifies the VBCM analysis
            of omnibus PCA factors. The source (P5-S2-C7) explicitly states that 'The
            remaining factors did not correlate significantly with tissue concentration,'
            distinguishing them from the three factors that did (P5-S1-C13). The draft
            correctly isolates the null result for the non-significant factors.
          source_ids:
          - P5-S2-C7
          - P5-S1-C13
          - P4-S1-C4
        direction:
          answer: fits
          reason: The source states the remaining factors 'did not correlate significantly'.
            The draft claims 'did not correlate significantly' and uses 'no_effect'
            direction, which accurately reflects a null finding (no statistically
            detected association) without claiming proof of zero effect.
          source_ids:
          - P5-S2-C7
        construct:
          answer: fits
          reason: The exposure is correctly defined as the 'remaining factors' from
            the omnibus PCA (excluding the three significant ones). The outcome is
            'tissue concentration' (T1-weighted signal intensity), which is the correct
            measure for VBCM as described in P3-S4-C12. The method is VBCM. The patient
            measurement is template_lesion_overlap (VBCM uses T1 intensity/lesion
            overlap on standard space, not patient-specific tractography or diffusion
            metrics).
          source_ids:
          - P5-S2-C7
          - P3-S4-C12
          - P4-S1-C4
        qualifications:
          answer: fits
          reason: The draft includes the qualification that lesion volume, age, and
            years of education were entered as nuisance regressors (P5-S1-C11). This
            is a material qualifier for the VBCM analysis. The draft correctly identifies
            the specific factors excluded from the 'remaining' group (phonological
            working memory, semantic ability, speech quanta) based on P5-S1-C13 and
            P5-S2-C7.
          source_ids:
          - P5-S1-C11
          - P5-S1-C13
          - P5-S2-C7
        missing_material_caveat:
          answer: fits
          reason: The draft includes the limitation that VBCM assumes lower T1 intensity
            relates to tissue damage/atrophy (P3-S4-C13). No other material caveats
            regarding the null result for these specific factors appear to be missing.
            The distinction between the significant and non-significant factors is
            preserved.
          source_ids:
          - P3-S4-C13
          - P5-S2-C7
      optional_pending:
      - Specific anatomical locations for the non-significant factors are not detailed
        in the source text provided, only that they did not reveal significant clusters.
      - Exact p-values or threshold details for the non-significant factors are not
        transcribed, as they were below the significance threshold.
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Sample size requires source confirmation; it has not been transcribed.
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Specific anatomical locations for the non-significant factors are not detailed
      in the source text provided, only that they did not reveal significant clusters.
    - Exact p-values or threshold details for the non-significant factors are not
      transcribed, as they were below the significance threshold.
    normalizations:
    - field: sample.n
      original: 46
      action: not_transcribed
      reason: Not supported by selected quotations
    analysis_identity:
      id: R013
      exposure:
        text: remaining factors (excluding phonological working memory, semantic ability,
          speech quanta)
      outcome:
        text: tissue concentration
      analysis_label: VBCM (omnibus PCA factors)
      relation: association
      evidence_ids:
      - P5-S2-C7
      qualifier_ids:
      - P5-S1-C11
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 7f20273b9607c3fad8b845f8237d1af68da141e992b478b1fa2c5773b653677c
        source_review: _compare/relationships-2026-11-16/review-current/Halai2018
        source_status_sha256: 54e46bb8c91a9ff1af88573d9198dfa480a15e8bb9258c75d3cd50cf0da2f994
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P2-S4-C7:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 7f20273b9607c3fad8b845f8237d1af68da141e992b478b1fa2c5773b653677c
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: ba356f5f4a060779413b005c4fee7cc1a13166cd2ede44ddb46d5227b1b3547f
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S4-C7
          page: 2
          text_layer_sha256: ba356f5f4a060779413b005c4fee7cc1a13166cd2ede44ddb46d5227b1b3547f
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'All patients were at least 12 months post-

          stroke at the time of scanning and assessment, were native English

          speakers with normal or corrected-to-normal hearing and vision (see

          Supplementary Table 1 for demographic details).'
        anchor_text: 'All patients were at least 12 months post-

          stroke at the time of scanning and assessment, were native English

          speakers with normal or corrected-to-normal hearing and vision (see

          Supplementary Table 1 for demographic details).'
        excluded_fragments: []
        image_sha256: 605141396dbad7374971a8fe11094cfb10f2ff36b71aa5a5d5b3421347c44914
        transcription: '. All patients were at least 12 months post-

          stroke at the time of scanning and assessment, were native English

          speakers with normal or corrected-to-normal hearing and vision (see

          Supplementary Table 1 for demographic details)'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 5
  quote: 'The remaining factors did not correlate signiﬁcantly with tissue con-

    centration.

    3.5.'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-24'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
