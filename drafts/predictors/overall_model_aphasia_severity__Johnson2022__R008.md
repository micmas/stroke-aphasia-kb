---
id: overall_model_aphasia_severity
name: Overall Model
kind: predictor
findings:
- id: f1
  target_audit:
    status: behaviour_label_present
    category: behaviour_or_language_construct
    original_target: aphasia_severity_residuals
    reason: Label names a behaviour or language construct; its exact operational definition and measurement
      still need source review.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  outcome_measurement:
    status: identified
    instruments:
    - name: Western Aphasia Battery–Revised
      subtest: Aphasia Quotient
    metric: Residual AQ after accounting for lesion volume and damage to critical regions
    definition_source:
      citation: '@Johnson2022'
      page: 3
      quote: "Inclusion criteria for this analysis were deﬁned prior to\ndata analysis and were as follows:\
        \ availability of aphasia\nseverity\nscores\nas\nindicated\nby\na\nWestern\nAphasia\nBatteryeRevised\
        \ (Kertesz, 2007) (WAB-R) Aphasia Quotient\n(WAB-AQ), structural neuroimaging data obtained within\
        \ 6\nmonths of language testing (M ¼ 6.0 ± 19.4 days; range ¼ 0e163\ndays), 21e85 years old, pre-morbidly\
        \ right-handed, and in the\nchronic stage of recovery (\x026 months post-onset) following a\nleft\
        \ hemisphere stroke (M ¼ 38.5 ± 45.9; range ¼ 6e212)."
      basis: Published source passage
    note: Measurement metadata identified from source evidence; finding remains unapproved. Residualized
      study outcome, not raw AQ.
  target: aphasia_severity_residuals
  target_kind: impairment
  claim: A combined model of non-linguistic cognitive ability, time post-stroke, age
    at stroke, and white matter hyperintensity extent significantly predicted aphasia
    severity residuals after accounting for lesion volume and damage to critical language
    regions.
  direction: likely
  relationship: correlational
  method: MVPA
  sample:
    n: 106
    population: individuals in the chronic stage of recovery from a left-hemisphere
      stroke
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
  - Retrospective study design
  - Use of residual values may compromise ease of interpretability
  - Potential for change in exercise rate or health factors between case history completion
    and assessment (up to 6 months)
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: A combined prediction model using non-linguistic cognitive
    ability (WAIS Matrices score), time post-stroke, age at stroke, and extent of
    white matter hyperintensities (Fazekas score). The model predicted residuals from
    a univariate linear regression that accounted for total lesion volume and proportion
    damage to critical language areas (posterior insula and SLF-A tract). Additional
    metadata has not been transcribed; review the pending-field flags before approval.
    PDF image reading (P7-S1-C4, two-model agreement, human verification pending):
    Stepwise regression with leave-one-out cross

    validation results: Overall Model


    A total of 106 participants had all data available and were

    included in the Overall Model Original text-layer quotation is preserved below.'
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
    - not_transcribed:sample.time_post_onset
    - proposed_concept:aphasia_severity_residuals
  citation: '@Johnson2022'
  source_passages:
  - section: Original source P7-S1-C8
    page: 7
    quote: 'The Overall

      Model explained 27% of the variance in residual WAB AQ

      scores controlled for lesion to critical language regions (Adj.

      R2 ¼ .27, F (16.6,101) ¼ 10.8), P < .00001).'
    supports: claim
  - section: Original source P7-S1-C9
    page: 7
    quote: 'The correlation be-

      tween actual and predicted values for this model was statis-

      tically signiﬁcant (r ¼ .45, P < .00001).'
    supports: claim
  - section: Original source P7-S1-C6
    page: 7
    quote: 'The dependent variable was

      aphasia severity after accounting for proportion damage to

      critical language areas and lesion volume, consistent with the

      two previous models.'
    supports: method
  - section: Original source P7-S1-C4
    page: 7
    quote: 'Stepwise regression with leave-one-out cross

      validation results: Overall Model

      A total of 106 participants had all data available and were

      included in the Overall Model.'
    supports: sample
  - section: Original source P7-S1-C5
    page: 7
    quote: 'The independent variables

      included in the model were: WAIS score, time post-stroke, age

      at stroke, and the extent of WMH.'
    supports: method
  - section: Original source P3-S3-C7
    page: 3
    quote: "Inclusion criteria for this analysis were deﬁned prior to\ndata analysis\
      \ and were as follows: availability of aphasia\nseverity\nscores\nas\nindicated\n\
      by\na\nWestern\nAphasia\nBatteryeRevised (Kertesz, 2007) (WAB-R) Aphasia Quotient\n\
      (WAB-AQ), structural neuroimaging data obtained within 6\nmonths of language\
      \ testing (M ¼ 6.0 ± 19.4 days; range ¼ 0e163\ndays), 21e85 years old, pre-morbidly\
      \ right-handed, and in the\nchronic stage of recovery (\x026 months post-onset)\
      \ following a\nleft hemisphere stroke (M ¼ 38.5 ± 45.9; range ¼ 6e212)."
    supports: sample
  - section: Original source P12-S1-C4
    page: 12
    quote: 'Limitations

      Due to the retrospective nature of the present study, there are

      several limitations that should be considered when inter-

      preting the results.'
    supports: limitation
  - section: Original source P12-S1-C9
    page: 12
    quote: 'It is important to note that our approach of using residual

      values from the linear regression predicting aphasia severity

      from damage as the dependent variables in the three models

      yields

      results

      that

      compromise

      ease

      of

      interpretability.'
    supports: limitation
predictor_type: imaging_metric
short_definition: A combined prediction model using non-linguistic cognitive ability
  (WAIS Matrices score), time post-stroke, age at stroke, and extent of white matter
  hyperintensities (Fazekas score).
assessment:
- Western Aphasia Battery-Revised (WAB-R) Aphasia Quotient (WAB-AQ)
- Wechsler Adult Intelligence Scale (WAIS) Matrices sub-test
- Fazekas scale
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-24'
relationship_review:
  paper: Johnson2022
  proposal_id: R008
  review_status_sha256: c6314df68e680bd80afc11fa17d6e197aaa4f2755be1a8e092f1e8d5943419d5
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 74eaee46da40fe72780c9ad086be4e9d062e3f6acd55eb11e1f6e24bc9f6a525
    original_review_binding:
      version: relationship-review-v5
      input_hashes:
        pdf: 74eaee46da40fe72780c9ad086be4e9d062e3f6acd55eb11e1f6e24bc9f6a525
        A/passages.json: 41197b1101998f2c5cfa6c9231df15f4ae36c1bb9edd3ab4430d0c3b67efda97
        A/raw.json: fcecdd7cf91cc9e0bb873ae637a7aaa959a635201724aaf182f2334bbea337b1
        A/source-units.json: ad27a943bcbee21e12558403eedf31ddd5bccd56c9ece92bb6eeb1cc7ebae2a0
        A/full-source-units.json: ad27a943bcbee21e12558403eedf31ddd5bccd56c9ece92bb6eeb1cc7ebae2a0
        A/meta.json: 05225f4353d9b312c38f0d411fe0aff343ca1e0766e1789ee34cfa61a994b539
        A/table-images/manifest.json: 9abfd8a54e78c09c24165d4ca0625e68a3f402d2e57fbba9d097f1d057712f1d
        A/clauses/window-11/raw.json: 822e318aa9990819b7c438f597b4493d78757befa7c956c81958ec6b0db1530c
        A/clauses/window-11/prompt.txt: 3e302495b8e500e93d8cc0f83641dbed01b263b44edd607475d372c8535fb433
        A/clauses/window-11/meta.json: 292195462d0b6d21a8fea765cfa0ed28fd2f1d739de5c993558b2f4cea4524d4
        A/clauses/window-16/raw.json: b87640fd16f375e8a71a96cd6768164bf03ab4026caae7b717481c292c20a6ae
        A/clauses/window-16/prompt.txt: c8e6ae34c1757c823d700aa7b98c88875595558bb5b4d006f2d2536ea974bfa7
        A/clauses/window-16/meta.json: fa1b947d1952b3fe351364eac1af881a2507991352f14cc63ab18e3f0ff2eeb0
        A/clauses/window-18/raw.json: 7c55fad665875c64620326456399276f4ffed30c81f8d351030361c4e839d6e3
        A/clauses/window-18/prompt.txt: a549e2a17eef70b6e26ce982197bd5631a3d7efd4c874acd4638ad391d9aea17
        A/clauses/window-18/meta.json: 06ed8e4147bb00f08fd74ff990002c24df683e38971b016a3ab367f465d479a1
        A/clauses/window-19/raw.json: 24e316b840e4002c6d6682a9c9f8fff7b6e88cb8ca79da87a64b8c6d560b120c
        A/clauses/window-19/prompt.txt: 51321b8cb6cb54d1c3a02a21f6177c2ef9bdd860090826499ad618d422479cf2
        A/clauses/window-19/meta.json: 3fe6458af717c74e3babab9b69fa2a9bb765b7ebf4c4f5e57198d3a50d35e58d
        A/clauses/window-17/raw.json: d3ed9fb940c3d5b8c3a5df062abbcd634c4fe98d0654b01ad4deea3f983a02d4
        A/clauses/window-17/prompt.txt: d64d04eb2660e44e075352fd02d9e6bc6b23e49dda8387e2bcd4dfec79d546b3
        A/clauses/window-17/meta.json: 2666e7e66f21de84046c26f48cf9975291f6fcf202c6619711817d6e96694627
        A/clauses/window-10/raw.json: 66f9dbcd31c9af71dfd3bf43c256ea4a603f2850c8586f77edbda81eec5ace9f
        A/clauses/window-10/prompt.txt: c6ab65c677cb9ad2d89fd76b98e1efbd0e4a0da251e7048046bf51e30777392e
        A/clauses/window-10/meta.json: ede0f3def458bef7eba40ebd9c8bc004f77ab7767caba9cbe8227ea11e7c8fc5
        A/clauses/window-03/raw.json: 62e7b9488dcc4dde7e9e4f4b442bd52855fb599ee45ede2331a465325f8fbde9
        A/clauses/window-03/prompt.txt: f54e47566906962ef49f64935e69a2ec46ae11f51eb07286570b64dc3ccdeaaa
        A/clauses/window-03/meta.json: 17301b778fe08d6e6560fd5080da4104be551b1d17fc7af294f8ff14ee39540c
        A/clauses/window-04/raw.json: fa460acc77dc542ade1d71dd88cedc4a12a61a6ab36696f5318099de64744a55
        A/clauses/window-04/prompt.txt: 63d516d6b22634559606ffe13893abdc6387c125caab4db79fd119ef4e087223
        A/clauses/window-04/meta.json: 938e7be9bc57408e408222d459931c00686e562a5c9b4f46b024bbd02f22cf7a
        A/clauses/window-05/raw.json: 77863c14690111f1dcc8461d1098ea388fca27ec780d9d4c25e1420bd8dac62a
        A/clauses/window-05/prompt.txt: c89f476c094b8518e26ea483812aa1756f9f735bff1160944e40392cc0b088f9
        A/clauses/window-05/meta.json: ec4ee260107190689b2eb8395fe2a553b41ef3a8d2d0d31f309e59684219af24
        A/clauses/window-02/raw.json: 8fdf3d4e2d1101359fae1912527baff44a122f3529dbc26bc0edd9f3b7a91d0e
        A/clauses/window-02/prompt.txt: b1b0eae76329039b04fb5006177636f478868785a63a72170b14d2b8cb323edd
        A/clauses/window-02/meta.json: 35c56c9c0e317dbe4d5553ba0845d7b989524434c68ff642465bdae72341794c
        A/clauses/window-15/raw.json: 9b0cda77f98dacdf60389caad0c020f783199b117889f1b2e9551b1a41520955
        A/clauses/window-15/prompt.txt: a4edac751acbefc094fbb672b4dc746f38808343d50651cd1994c54907b951c3
        A/clauses/window-15/meta.json: 3f3badf75700af7c8be186444a0045bac72cf085835744fd817b05f8b61bf719
        A/clauses/window-12/raw.json: 86883c5d70ed29d768b452aa55433f224ff8f02759bd442f0a3495de3857ab94
        A/clauses/window-12/prompt.txt: 2e356ddc53826d1391831b02c31645e9b7f0617717fb2aa58180eb32584e8e5c
        A/clauses/window-12/meta.json: 045d77a845a719a394d6c1c26db72f908a86e8874614ed4e0ab0022f0834ee74
        A/clauses/window-13/raw.json: 0ca77e94b081866525844dec35ef80ac664d9f1642b1b3ca211413f231c3d32f
        A/clauses/window-13/prompt.txt: 3358227e64bff47efbf07dde73a04a8703336e28a3265798ac15ab844b363c69
        A/clauses/window-13/meta.json: ab24aec8a9f9a4a0b7af409259983488b8e5f378cab1cd1a845391ea8e9f73c2
        A/clauses/window-14/raw.json: 0256bdf41d9dac2c608ff2e50d49ff2f7f8db35c068346638a9195e10cff163c
        A/clauses/window-14/prompt.txt: d1211c0406df9c1969a8ae3290efb4871aa442f21cd6cd225b505cda56796d78
        A/clauses/window-14/meta.json: 738ab4923c9675db4127930ea599a1feacf9ca68a50d42bd07a6ed7818716e54
        A/clauses/window-09/raw.json: 9adbabb9813d21491f8936a2fa36e5f1d33fb15183a1ae6410016e6d90a33798
        A/clauses/window-09/prompt.txt: 31151af7123b2f9a779d2a2c233e7b75d9af5f4cbb43c5f5f4fe4a92a83f695f
        A/clauses/window-09/meta.json: 26c62036027e49ce7279f92876409574f6609012030f772089618de947919f7a
        A/clauses/window-07/raw.json: b8d594737c925f4d5df967788fd188749960e0994c4810a19838b37c28ab5159
        A/clauses/window-07/prompt.txt: 467d9de46f1b301d70fd87831af3bc388bb112e4e19ae18f6a41a9641e4c0ebb
        A/clauses/window-07/meta.json: c0a012a92ed0763dcdc139f5620340e3d32022901a710a7d90ac5b440ef7561d
        A/clauses/window-01/raw.json: e4e2ef244463d45c069b77ef9029c2c37036a2e5e22af9fbc49f5ee0eddf2cd0
        A/clauses/window-01/prompt.txt: 1fd46b4561c4fe973a6e54d3d92f7832df3e69e122a4ac73a4fac26f0dbeaaaa
        A/clauses/window-01/meta.json: fbc66eb00a8805b1c2169be16c18433d73723613dba8c642297d068282617bbc
        A/clauses/window-06/raw.json: 18d57997b048e73a631789d0e0e4fe04149fdd8bf2c250074997b6cd538e43a0
        A/clauses/window-06/prompt.txt: 3df6a05f1000e2af51e28826fe71153d76723d3b32c13d907c1f4c2917c236dc
        A/clauses/window-06/meta.json: 3db8b7ad4a78f5862ed81a66050fbdc906b21e8e3b6d8b921aefbfdc5ae03743
        A/clauses/window-08/raw.json: 18494bda579eba6220972b9869ca121649c94b8618e489e0ac453a863deab389
        A/clauses/window-08/prompt.txt: 8db86c497653e6cdaf2b254d2da9a03a96c267b6f9d2321dfcf6334683a15553
        A/clauses/window-08/meta.json: abf450500235206db43ca17b02668db36d19ab9724bba7dcf8676a885b349353
        B/passages.json: 41197b1101998f2c5cfa6c9231df15f4ae36c1bb9edd3ab4430d0c3b67efda97
        B/raw.json: 959575af13cd8b8ae0da689554ec36a51fbc9e966215e897ce91f6066c292e7c
        B/source-units.json: ad27a943bcbee21e12558403eedf31ddd5bccd56c9ece92bb6eeb1cc7ebae2a0
        B/full-source-units.json: ad27a943bcbee21e12558403eedf31ddd5bccd56c9ece92bb6eeb1cc7ebae2a0
        B/meta.json: a46b5302531d9aeb99eb0ce304172ae535abf4b5d74f7250d2f7618c47eed42c
        B/table-images/manifest.json: 9abfd8a54e78c09c24165d4ca0625e68a3f402d2e57fbba9d097f1d057712f1d
        B/clauses/window-11/raw.json: e4ea2f56097927fccbfafd7328909046ae72fd29ffb81fe53675a15d8d5cdf5b
        B/clauses/window-11/prompt.txt: 3e302495b8e500e93d8cc0f83641dbed01b263b44edd607475d372c8535fb433
        B/clauses/window-11/meta.json: 6c25bacef9cd8fcf4744789e9d60bf6a485aaa2050cb362927c1deffc57e4981
        B/clauses/window-16/raw.json: 532762b912d99608dc6fc65ab827b9c91e7f1363b540e7d90cf8d6f26048ff80
        B/clauses/window-16/prompt.txt: c8e6ae34c1757c823d700aa7b98c88875595558bb5b4d006f2d2536ea974bfa7
        B/clauses/window-16/meta.json: 2a3e50257855209ad398a83d3251c38d6397bf6585668f885a677f7b6987a179
        B/clauses/window-18/raw.json: f807ee20f3361ca69fcce150d76b0d08171a29802605fcf7c1f57d1f1a53ffd4
        B/clauses/window-18/prompt.txt: a549e2a17eef70b6e26ce982197bd5631a3d7efd4c874acd4638ad391d9aea17
        B/clauses/window-18/meta.json: bbf6791caa3806b6d36bdccd1c2398371badaf85a53640d8508c2e980ab0640f
        B/clauses/window-19/raw.json: 14ac1910489831c2a7460f07029941ad00f89a5dd5d10cf1a66bed2977c06e74
        B/clauses/window-19/prompt.txt: 51321b8cb6cb54d1c3a02a21f6177c2ef9bdd860090826499ad618d422479cf2
        B/clauses/window-19/meta.json: 9993e3dacbd09ddfe10ee13ddb11285c0e758b71deae9d8caa30299b39c85707
        B/clauses/window-17/raw.json: d62d3d52da00ee2d0c18506c31526fadcd2c0626547abe09ad820562aca3d7d0
        B/clauses/window-17/prompt.txt: d64d04eb2660e44e075352fd02d9e6bc6b23e49dda8387e2bcd4dfec79d546b3
        B/clauses/window-17/meta.json: fa9771eb16ad43398fae87244b5730caf611b71761d64f7bbf900e41289d0aa3
        B/clauses/window-10/raw.json: 8cc04d0f4f54fcbbb7b7a3a83bf2970144724db41a60e544df30b0573f733a83
        B/clauses/window-10/prompt.txt: c6ab65c677cb9ad2d89fd76b98e1efbd0e4a0da251e7048046bf51e30777392e
        B/clauses/window-10/meta.json: 8a9c8f4017d89108cab674e6fc1291ad9b009975b0a0fe537287d270f9d216ae
        B/clauses/window-03/raw.json: 6f067134f73a2173b452b812fb134979fe4e28ba9d310a25a311d285ebd4e5b5
        B/clauses/window-03/prompt.txt: f54e47566906962ef49f64935e69a2ec46ae11f51eb07286570b64dc3ccdeaaa
        B/clauses/window-03/meta.json: 3175fad2d399139801f27c0e78fa3bc028fa7be141477010c92152d488092220
        B/clauses/window-04/raw.json: 01126077f297c9a938aa92a85274ce7a66bcf04fba5cb3dc4d9c3107e7ec17d1
        B/clauses/window-04/prompt.txt: 63d516d6b22634559606ffe13893abdc6387c125caab4db79fd119ef4e087223
        B/clauses/window-04/meta.json: 18e3db0eb76408f174d5219ea8b42ca9a95bece717378ec206c4b97275a83a34
        B/clauses/window-05/raw.json: eef60426755d9836711d57cc9e26fa781f062e82b7ce49a8683ec36aaf986b91
        B/clauses/window-05/prompt.txt: c89f476c094b8518e26ea483812aa1756f9f735bff1160944e40392cc0b088f9
        B/clauses/window-05/meta.json: 5e9c0b5ef2d7a6c0f05c4d4e9329c53f1651f5788e9779c381ba6a2aa793a3a9
        B/clauses/window-02/raw.json: 9c201f72aeadc7357122dbc1f7137726e78dd8f29f6d2ca06d1218ed48a849b1
        B/clauses/window-02/prompt.txt: b1b0eae76329039b04fb5006177636f478868785a63a72170b14d2b8cb323edd
        B/clauses/window-02/meta.json: 4ca4f4e3fdc0d801e608c929beb0e4dd93ba703ddf94b1faed882929d6050b5f
        B/clauses/window-15/raw.json: 3333a87c70e68bd4d5a4a41ea18146a96c3d7528ae821bf465984ffceb952136
        B/clauses/window-15/prompt.txt: a4edac751acbefc094fbb672b4dc746f38808343d50651cd1994c54907b951c3
        B/clauses/window-15/meta.json: 6f28e1ad08c6c57b7cd58b0f923e7e26ba0cc166039bc8516cd66dd985bc4644
        B/clauses/window-12/raw.json: dc8905fe31fa03876c28b92250156b44f6514202994f419e2e89efedc3e84295
        B/clauses/window-12/prompt.txt: 2e356ddc53826d1391831b02c31645e9b7f0617717fb2aa58180eb32584e8e5c
        B/clauses/window-12/meta.json: 3e3ccb4d32f7b26c14819bc42b95c00172efe27b732ed565db5852b991586487
        B/clauses/window-13/raw.json: e1c21a666b5f212a58d2e8d397587209c4685e7b7dae82c154c2fa60eaf14c51
        B/clauses/window-13/prompt.txt: 3358227e64bff47efbf07dde73a04a8703336e28a3265798ac15ab844b363c69
        B/clauses/window-13/meta.json: f9e545a4d95a8454f24a5b4f293ab49e5682a7fd2e200beb199c5a26db6fb023
        B/clauses/window-14/raw.json: 51a85d343dc7eb138e699d8d873bfbaf70c49170c790be9edc0855117d3502ed
        B/clauses/window-14/prompt.txt: d1211c0406df9c1969a8ae3290efb4871aa442f21cd6cd225b505cda56796d78
        B/clauses/window-14/meta.json: d3c1d26f669c563638633502ae5aa2c4224d5b3099c4a6c8eac6448afe73a1d1
        B/clauses/window-09/raw.json: ea85ab2abd7a576554e1b2c94a8b1e7f701a575863166504bf745d6e9c3680c1
        B/clauses/window-09/prompt.txt: 31151af7123b2f9a779d2a2c233e7b75d9af5f4cbb43c5f5f4fe4a92a83f695f
        B/clauses/window-09/meta.json: b8fc72387162fafe4e8c7121ac2e76a3982aacf3a56ef1dc300c0e16a3c7d236
        B/clauses/window-07/raw.json: effcb1b9ea3cce2c6ab643ad244389b7cf6f1e6c961c7dc58e8f701846184d1e
        B/clauses/window-07/prompt.txt: 467d9de46f1b301d70fd87831af3bc388bb112e4e19ae18f6a41a9641e4c0ebb
        B/clauses/window-07/meta.json: 7ebc6ab6a9e1ceeb9a00b9cf02dbd008c0dd9e86786055a84c9af3a7b3efb2b2
        B/clauses/window-01/raw.json: 7ed5b060727bf2460ecb070c7e824627b3bcee748df11f80c4e83ccbf4304b13
        B/clauses/window-01/prompt.txt: 1fd46b4561c4fe973a6e54d3d92f7832df3e69e122a4ac73a4fac26f0dbeaaaa
        B/clauses/window-01/meta.json: 96afd5b6c5c7c416844ff6b2a9b09e6213d44c97ef174ac1382979a6152e69c7
        B/clauses/window-06/raw.json: 78c3234f5efccf9023ca14e5d8406125ba6716e29f46c9e4d389533a9faee3b5
        B/clauses/window-06/prompt.txt: 3df6a05f1000e2af51e28826fe71153d76723d3b32c13d907c1f4c2917c236dc
        B/clauses/window-06/meta.json: 1e4d96ee0bbed8b84a716017b04e7769775f1e1078e5b01cf2e6395984dd41a5
        B/clauses/window-08/raw.json: 330d863af2f31a337efc4d92040cfb12d469ee76b889df7b6f66b2760c37ca32
        B/clauses/window-08/prompt.txt: 8db86c497653e6cdaf2b254d2da9a03a96c267b6f9d2321dfcf6334683a15553
        B/clauses/window-08/meta.json: 8186cee2ce415acd954d2d0efb834055037be5294415c46e6a0cc30dc124ee68
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
      pdf_sha256: 74eaee46da40fe72780c9ad086be4e9d062e3f6acd55eb11e1f6e24bc9f6a525
      source_review: _compare/relationships-2026-11-16/review-current/Johnson2022
      source_status_sha256: 2335f24de7dd6066d19cb711304977d5fa1f777ec738c88be954fde112457a8e
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R008
    exposure:
      text: combined health and demographic factors
    outcome:
      text: aphasia severity (residuals after accounting for lesion size and location)
    analysis_label: Overall Model
    relation: performance
    evidence_ids:
    - P7-S1-C8
    - P7-S1-C9
    qualifier_ids:
    - P7-S1-C6
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 74eaee46da40fe72780c9ad086be4e9d062e3f6acd55eb11e1f6e24bc9f6a525
      source_review: _compare/relationships-2026-11-16/review-current/Johnson2022
      source_status_sha256: 2335f24de7dd6066d19cb711304977d5fa1f777ec738c88be954fde112457a8e
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Accounting without a linked unit P4-S2-C2
      - Unaccounted source passage P4-S2-C2
      - Accounting without a linked unit P6-S2-C4
      - Unaccounted source passage P6-S2-C4
      - Accounting without a linked unit P6-S2-C8
      - Accounting without a linked unit P6-S3-C5
      - Unaccounted source passage P6-S2-C8
      - Unaccounted source passage P6-S3-C5
      - Result passage disposed without unit P6-S3-C11
      - Accounting without a linked unit P6-S3-C7
      - Unaccounted source passage P6-S3-C7
      - Result passage disposed without unit P7-S1-C9
      - Accounting without a linked unit P8-S1-C5
      - Accounting without a linked unit P8-S1-C6
      - Unaccounted source passage P8-S1-C6
      - Unaccounted source passage P8-S1-C5
      - Result passage disposed without unit P10-S2-C11
      - Accounting without a linked unit P10-S3-C1
      - Result passage disposed without unit P10-S3-C4
      - Unaccounted source passage P10-S3-C1
      - Accounting without a linked unit P11-S2-C8
      - Unaccounted source passage P11-S2-C8
      - Result passage disposed without unit P12-S1-C7
      - Result passage disposed without unit P12-S3-C4
      unattached_null_or_qualifier_ids:
      - P10-S3-C1
      - P10-S3-C4
      - P11-S2-C8
      - P12-S3-C4
      suppressed_nonrepresented_units: 11
      default_disposition_count_requires_completeness_check: 281
      unselected_timing_passages:
      - P1-S1-C5
      - P3-S3-C3
      - P6-S3-C9
      - P12-S1-C12
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P1-S2-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P1-S2-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P1-S2-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S2-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S2-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S3-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S3-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S1-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S1-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S2-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S2-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S3-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S1-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S2-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S3-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S3-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S3-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S4-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S1-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S1-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P15-S3-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P4-S1-C13
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P4-S2-C2
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P6-S1-C6
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: tested_personal_effects
        source_id: P3-S2-C7
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P8-S1-C11
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P9-S2-C9
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P11-S1-C10
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: analysed_sample
        source_ids:
        - P1-S1-C6
        - P3-S3-C7
        - P4-S1-C11
        - P4-S2-C8
        - P5-S1-C11
        - P5-S2-C13
        - P6-S2-C10
        - P6-S3-C9
        - P7-S1-C4
        - P8-S1-C4
        - P9-S1-C6
        - P9-S1-C7
        - P9-S1-C9
        - P11-S2-C8
        - P12-S1-C5
        - P12-S2-C12
        - P15-S3-C7
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: recruited_sample
        source_ids:
        - P1-S1-C5
        - P3-S3-C5
        - P3-S3-C10
        - P4-S2-C8
        - P5-S2-C12
        - P7-S1-C11
        - P9-S1-C9
        - P11-S1-C3
        - P12-S1-C5
        - P12-S2-C12
        - P15-S3-C18
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: imaging_provenance
        source_ids:
        - P1-S1-C5
        - P4-S2-C6
        - P4-S2-C7
        - P5-S1-C1
        - P5-S1-C2
        - P5-S2-C6
        - P6-S2-C5
        - P7-S1-C12
        - P9-S1-C10
        - P10-S1-C4
        - P15-S3-C7
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: outcome_definition
        source_ids:
        - P1-S1-C6
        - P1-S2-C4
        - P1-S2-C5
        - P1-S2-C6
        - P3-S3-C7
        - P5-S1-C8
        - P5-S1-C13
        - P5-S2-C3
        - P5-S2-C4
        - P6-S1-C5
        - P6-S1-C6
        - P6-S3-C4
        - P6-S3-C10
        - P7-S1-C6
        - P9-S1-C3
        - P9-S1-C6
        - P9-S1-C8
        - P10-S1-C4
        - P10-S2-C3
        - P10-S2-C11
        - P10-S3-C1
        - P10-S3-C4
        - P11-S1-C10
        - P11-S2-C8
        - P15-S3-C7
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: limitations
        source_ids:
        - P10-S3-C4
        - P11-S2-C8
        - P12-S1-C4
        - P12-S1-C10
        - P12-S2-C2
        - P12-S2-C3
        - P12-S2-C5
        - P12-S2-C6
        - P12-S2-C7
        - P12-S2-C9
        - P12-S2-C10
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: personal_factors
        source_ids:
        - P1-S2-C4
        - P1-S2-C5
        - P1-S2-C6
        - P3-S2-C10
        - P3-S3-C1
        - P3-S4-C5
        - P4-S1-C6
        - P4-S1-C7
        - P5-S3-C2
        - P5-S3-C3
        - P6-S3-C2
        - P6-S3-C7
        - P6-S3-C9
        - P7-S1-C5
        - P7-S1-C7
        - P8-S1-C3
        - P9-S1-C6
        - P10-S2-C4
        - P10-S2-C10
        - P10-S3-C1
        - P11-S1-C3
        - P11-S1-C10
        - P11-S2-C8
        - P11-S3-C7
        - P11-S3-C8
        - P11-S3-C11
        - P11-S4-C3
        - P11-S4-C4
        - P12-S2-C2
        - P12-S2-C4
        - P12-S2-C10
        - P12-S3-C2
        - P12-S3-C3
        - P15-S3-C18
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: tested_personal_effects
        source_ids:
        - P1-S2-C4
        - P1-S2-C5
        - P1-S2-C6
        - P6-S3-C5
        - P6-S3-C6
        - P6-S3-C7
        - P7-S1-C1
        - P7-S1-C2
        - P7-S1-C7
        - P7-S1-C8
        - P8-S1-C5
        - P8-S1-C6
        - P9-S1-C1
        - P9-S1-C9
        - P10-S2-C11
        - P10-S3-C1
        - P11-S2-C8
        - P11-S3-C4
        - P11-S3-C6
        - P11-S3-C9
        - P11-S4-C4
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: adjustment_roles
        source_ids:
        - P1-S1-C6
        - P3-S2-C6
        - P3-S4-C5
        - P5-S1-C12
        - P6-S1-C5
        - P6-S2-C7
        - P6-S3-C4
        - P6-S3-C5
        - P6-S3-C6
        - P6-S3-C10
        - P7-S1-C1
        - P7-S1-C6
        - P7-S1-C8
        - P9-S1-C5
        - P10-S3-C1
        - P11-S1-C10
        - P11-S2-C8
        - P11-S3-C4
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: descriptive_personal_factors
        source_ids:
        - P1-S2-C4
        - P3-S3-C7
        - P3-S3-C11
        - P3-S3-C12
        - P3-S4-C3
        - P3-S4-C4
        - P4-S1-C8
        - P4-S1-C9
        - P4-S1-C10
        - P4-S2-C8
        - P5-S3-C2
        - P5-S3-C3
        - P6-S2-C10
        - P6-S3-C9
        - P9-S1-C6
        - P10-S2-C4
        - P11-S1-C3
        - P11-S3-C7
        - P11-S3-C8
        - P11-S3-C11
        - P12-S3-C2
        - P15-S3-C18
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - analysed_sample
      - recruited_sample
      - imaging_provenance
      - outcome_timing
      - outcome_definition
      - limitations
      - personal_factors
      - tested_personal_effects
      - adjustment_roles
      - explicitly_not_adjusted
      - descriptive_personal_factors
      unclassified_extraction_ids:
      - P3-S4-C5
      - P11-S2-C12
      table_review_required: []
      unlinked_tables: []
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P4-S1
        - P5-S3
        - P6-S1
        - P6-S2
        - P6-S3
        - P7-S1
        - P8-S1
        - P9-S1
        - P9-S2
        - P10-S3
        - P11-S3
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 74eaee46da40fe72780c9ad086be4e9d062e3f6acd55eb11e1f6e24bc9f6a525
      source_review: _compare/relationships-2026-11-16/review-current/Johnson2022
      source_status_sha256: 2335f24de7dd6066d19cb711304977d5fa1f777ec738c88be954fde112457a8e
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S2-C3
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of LSM results in abstract.
    - source_id: P1-S2-C4
      disposition: repeated
      result_indexes:
      - 2
      - 3
      reason: Restatement of Demographic and Health model results in abstract.
    - source_id: P1-S2-C5
      disposition: repeated
      result_indexes:
      - 6
      - 7
      reason: Restatement of Overall model results in abstract.
    - source_id: P1-S2-C6
      disposition: repeated
      result_indexes:
      - 10
      reason: Restatement of Final model variance in abstract.
    - source_id: P4-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes ANOVA for sampling bias, not a clinical relationship.
    - source_id: P5-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports reliability of Fazekas ratings.
    - source_id: P5-S3-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes data transformation (log transformation).
    - source_id: P5-S3-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes regression assumptions.
    - source_id: P6-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Mentions existence of correlation matrix.
    - source_id: P6-S2-C4
      disposition: represented
      result_indexes:
      - 0
      reason: Establishes LSM association between SLF and posterior insula and severity.
    - source_id: P6-S2-C8
      disposition: represented
      result_indexes:
      - 1
      reason: Reports variance explained by Lesion Model.
    - source_id: P6-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes scatterplots.
    - source_id: P6-S3-C5
      disposition: represented
      result_indexes:
      - 2
      reason: Identifies significant predictors in Demographic Model.
    - source_id: P6-S3-C6
      disposition: represented
      result_indexes:
      - 3
      reason: Reports variance explained by Demographic Model.
    - source_id: P6-S3-C7
      disposition: represented
      result_indexes:
      - 3
      reason: Reports correlation for Demographic Model.
    - source_id: P6-S3-C11
      disposition: represented
      result_indexes:
      - 4
      reason: Identifies significant effect of Fazekas scores in Health Model.
    - source_id: P7-S1-C1
      disposition: represented
      result_indexes:
      - 5
      reason: Reports variance explained by Health Model.
    - source_id: P7-S1-C2
      disposition: represented
      result_indexes:
      - 5
      reason: Reports correlation for Health Model.
    - source_id: P7-S1-C7
      disposition: represented
      result_indexes:
      - 6
      reason: Identifies significant effects in Overall Model.
    - source_id: P7-S1-C8
      disposition: represented
      result_indexes:
      - 7
      reason: Reports variance explained by Overall Model.
    - source_id: P7-S1-C9
      disposition: represented
      result_indexes:
      - 7
      reason: Reports correlation for Overall Model.
    - source_id: P7-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes figure labels.
    - source_id: P8-S1-C5
      disposition: represented
      result_indexes:
      - 10
      reason: Reports variance and correlation for Final Model.
    - source_id: P8-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes scatterplots.
    - source_id: P9-S1-C1
      disposition: represented
      result_indexes:
      - 8
      reason: Identifies significant variables in Final Model.
    - source_id: P9-S1-C2
      disposition: represented
      result_indexes:
      - 9
      reason: Identifies non-significant variables in Final Model.
    - source_id: P10-S1-C4
      disposition: repeated
      result_indexes:
      - 0
      reason: Discussion restatement of SLF-A association.
    - source_id: P10-S2-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: General discussion on including age in models.
    - source_id: P10-S3-C1
      disposition: represented
      result_indexes:
      - 6
      reason: Reports that age at stroke is no longer significant when included with
        health factors (sensitivity/adjusted result).
    - source_id: P10-S3-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: General discussion on time post-stroke.
    - source_id: P11-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of participant motivation.
    - source_id: P11-S2-C8
      disposition: repeated
      result_indexes:
      - 2
      reason: Discussion restatement of cognitive reserve association.
    - source_id: P11-S3-C4
      disposition: repeated
      result_indexes:
      - 2
      reason: Discussion restatement of WAIS score association.
    - source_id: P11-S3-C6
      disposition: repeated
      result_indexes:
      - 4
      reason: Discussion restatement of WMH association.
    - source_id: P11-S3-C9
      disposition: represented
      result_indexes:
      - 11
      reason: Reports correlation between WAIS and Fazekas.
    - source_id: P11-S3-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: General discussion on health factors co-occurring with WMH.
    - source_id: P11-S4-C4
      disposition: represented
      result_indexes:
      - 12
      reason: Reports null association between exercise rate and WMH.
    - source_id: P12-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of sample representativeness.
    - source_id: P12-S3-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion about overall health.
    unresolved_coverage:
    - source_id: P9-S1-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S1-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S2-C3
    - P1-S2-C4
    - P1-S2-C5
    - P1-S2-C6
    - P4-S2-C2
    - P5-S2-C10
    - P5-S3-C5
    - P5-S3-C6
    - P6-S1-C3
    - P6-S2-C9
    - P7-S1-C12
    - P8-S1-C6
    - P9-S1-C9
    - P9-S1-C10
    - P10-S1-C4
    - P10-S2-C11
    - P10-S3-C1
    - P10-S3-C4
    - P11-S1-C3
    - P11-S2-C8
    - P11-S3-C4
    - P11-S3-C6
    - P11-S3-C11
    - P12-S1-C7
    - P12-S3-C4
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
      analysed_sample: []
      recruited_sample: []
      eligibility:
      - P3-S3-C7
      - P3-S3-C9
      - P5-S1-C11
      - P12-S1-C12
      imaging_provenance: []
      imaging_timing:
      - P3-S3-C7
      outcome_timing: []
      outcome_definition: []
      validation:
      - P5-S2-C14
      - P6-S1-C11
      - P6-S3-C9
      - P7-S1-C4
      analysis_restrictions:
      - P5-S1-C12
      - P12-S1-C10
      dependent_variable_statement:
      - P3-S2-C6
      - P3-S2-C7
      - P5-S1-C8
      - P5-S1-C13
      limitations: []
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles: []
      explicitly_not_adjusted: []
      descriptive_personal_factors: []
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: mixed
    window_merge: Union of selected IDs; differing window enums retained conservatively
      as both/mixed. Not verified study-level facts.
    held_selections:
    - slot: dependent_variable_statement
      source_id: P1-S2-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P1-S2-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P1-S2-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S2-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S2-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S3-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S3-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S1-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S1-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S2-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S2-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S3-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S1-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S2-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S3-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S3-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S3-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S4-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S1-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S1-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P15-S3-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P4-S1-C13
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P4-S2-C2
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P6-S1-C6
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: tested_personal_effects
      source_id: P3-S2-C7
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P8-S1-C11
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P9-S2-C9
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P11-S1-C10
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: analysed_sample
      source_ids:
      - P1-S1-C6
      - P3-S3-C7
      - P4-S1-C11
      - P4-S2-C8
      - P5-S1-C11
      - P5-S2-C13
      - P6-S2-C10
      - P6-S3-C9
      - P7-S1-C4
      - P8-S1-C4
      - P9-S1-C6
      - P9-S1-C7
      - P9-S1-C9
      - P11-S2-C8
      - P12-S1-C5
      - P12-S2-C12
      - P15-S3-C7
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: recruited_sample
      source_ids:
      - P1-S1-C5
      - P3-S3-C5
      - P3-S3-C10
      - P4-S2-C8
      - P5-S2-C12
      - P7-S1-C11
      - P9-S1-C9
      - P11-S1-C3
      - P12-S1-C5
      - P12-S2-C12
      - P15-S3-C18
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: imaging_provenance
      source_ids:
      - P1-S1-C5
      - P4-S2-C6
      - P4-S2-C7
      - P5-S1-C1
      - P5-S1-C2
      - P5-S2-C6
      - P6-S2-C5
      - P7-S1-C12
      - P9-S1-C10
      - P10-S1-C4
      - P15-S3-C7
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: outcome_definition
      source_ids:
      - P1-S1-C6
      - P1-S2-C4
      - P1-S2-C5
      - P1-S2-C6
      - P3-S3-C7
      - P5-S1-C8
      - P5-S1-C13
      - P5-S2-C3
      - P5-S2-C4
      - P6-S1-C5
      - P6-S1-C6
      - P6-S3-C4
      - P6-S3-C10
      - P7-S1-C6
      - P9-S1-C3
      - P9-S1-C6
      - P9-S1-C8
      - P10-S1-C4
      - P10-S2-C3
      - P10-S2-C11
      - P10-S3-C1
      - P10-S3-C4
      - P11-S1-C10
      - P11-S2-C8
      - P15-S3-C7
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: limitations
      source_ids:
      - P10-S3-C4
      - P11-S2-C8
      - P12-S1-C4
      - P12-S1-C10
      - P12-S2-C2
      - P12-S2-C3
      - P12-S2-C5
      - P12-S2-C6
      - P12-S2-C7
      - P12-S2-C9
      - P12-S2-C10
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: personal_factors
      source_ids:
      - P1-S2-C4
      - P1-S2-C5
      - P1-S2-C6
      - P3-S2-C10
      - P3-S3-C1
      - P3-S4-C5
      - P4-S1-C6
      - P4-S1-C7
      - P5-S3-C2
      - P5-S3-C3
      - P6-S3-C2
      - P6-S3-C7
      - P6-S3-C9
      - P7-S1-C5
      - P7-S1-C7
      - P8-S1-C3
      - P9-S1-C6
      - P10-S2-C4
      - P10-S2-C10
      - P10-S3-C1
      - P11-S1-C3
      - P11-S1-C10
      - P11-S2-C8
      - P11-S3-C7
      - P11-S3-C8
      - P11-S3-C11
      - P11-S4-C3
      - P11-S4-C4
      - P12-S2-C2
      - P12-S2-C4
      - P12-S2-C10
      - P12-S3-C2
      - P12-S3-C3
      - P15-S3-C18
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: tested_personal_effects
      source_ids:
      - P1-S2-C4
      - P1-S2-C5
      - P1-S2-C6
      - P6-S3-C5
      - P6-S3-C6
      - P6-S3-C7
      - P7-S1-C1
      - P7-S1-C2
      - P7-S1-C7
      - P7-S1-C8
      - P8-S1-C5
      - P8-S1-C6
      - P9-S1-C1
      - P9-S1-C9
      - P10-S2-C11
      - P10-S3-C1
      - P11-S2-C8
      - P11-S3-C4
      - P11-S3-C6
      - P11-S3-C9
      - P11-S4-C4
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: adjustment_roles
      source_ids:
      - P1-S1-C6
      - P3-S2-C6
      - P3-S4-C5
      - P5-S1-C12
      - P6-S1-C5
      - P6-S2-C7
      - P6-S3-C4
      - P6-S3-C5
      - P6-S3-C6
      - P6-S3-C10
      - P7-S1-C1
      - P7-S1-C6
      - P7-S1-C8
      - P9-S1-C5
      - P10-S3-C1
      - P11-S1-C10
      - P11-S2-C8
      - P11-S3-C4
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: descriptive_personal_factors
      source_ids:
      - P1-S2-C4
      - P3-S3-C7
      - P3-S3-C11
      - P3-S3-C12
      - P3-S4-C3
      - P3-S4-C4
      - P4-S1-C8
      - P4-S1-C9
      - P4-S1-C10
      - P4-S2-C8
      - P5-S3-C2
      - P5-S3-C3
      - P6-S2-C10
      - P6-S3-C9
      - P9-S1-C6
      - P10-S2-C4
      - P11-S1-C3
      - P11-S3-C7
      - P11-S3-C8
      - P11-S3-C11
      - P12-S3-C2
      - P15-S3-C18
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
      pdf_sha256: 74eaee46da40fe72780c9ad086be4e9d062e3f6acd55eb11e1f6e24bc9f6a525
      review_sha256: c6314df68e680bd80afc11fa17d6e197aaa4f2755be1a8e092f1e8d5943419d5
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
      - P7-S1-C8
      - P7-S1-C9
      source_result: The Overall Model (N=106) significantly predicted aphasia severity
        residuals (variance unexplained by lesion volume and critical region damage)
        using a combination of WAIS Matrices scores, time post-stroke, age at stroke,
        and total Fazekas scores (Adj. R2 = .27, P < .00001; r = .45, P < .00001).
      result_status: detected
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The draft correctly identifies the 'Overall Model' as the specific
            analysis, matching the source description of combining significant predictors
            from Demographic and Health models (P7-S1-C4, P7-S1-C5).
          source_ids:
          - P7-S1-C4
          - P7-S1-C5
        direction:
          answer: fits
          reason: The draft claims a significant prediction, which aligns with the
            source reporting significant model performance (P < .00001) and significant
            correlation (r = .45). The direction of the relationship (prediction of
            severity) is preserved.
          source_ids:
          - P7-S1-C8
          - P7-S1-C9
        construct:
          answer: fits
          reason: The exposure (combined health/demographic factors) and outcome (aphasia
            severity residuals) are correctly identified. The patient measurement
            is correctly classified as template_lesion_overlap because the residuals
            are derived from a model using lesion volume and proportion damage to
            critical regions identified via JHU atlas overlap, not patient-specific
            diffusion tractography.
          source_ids:
          - P7-S1-C6
          - P5-S1-C9
          - P5-S2-C2
        qualifications:
          answer: fits
          reason: The draft includes the critical qualification that the outcome is
            residuals after accounting for lesion volume and location, which is the
            defining feature of this model as described in P7-S1-C6 and P12-S1-C9.
          source_ids:
          - P7-S1-C6
          - P12-S1-C9
        missing_material_caveat:
          answer: fits
          reason: The draft includes the limitation regarding the use of residual
            values compromising interpretability (P12-S1-C9) and the retrospective
            nature (P12-S1-C4). No material caveats changing the interpretation of
            the model's performance are omitted.
          source_ids:
          - P12-S1-C4
          - P12-S1-C9
      optional_pending:
      - sample.time_post_onset
      - exact_statistical_values
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
    - exact_statistical_values
    normalizations:
    - field: sample.time_post_onset
      original: chronic stage of recovery (at least 6 months post-onset); imaging
        obtained within 6 months of language testing
      action: not_transcribed
      reason: 'Numbers not grounded in usable selected source readings: 6'
    analysis_identity:
      id: R008
      exposure:
        text: combined health and demographic factors
      outcome:
        text: aphasia severity (residuals after accounting for lesion size and location)
      analysis_label: Overall Model
      relation: performance
      evidence_ids:
      - P7-S1-C8
      - P7-S1-C9
      qualifier_ids:
      - P7-S1-C6
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 74eaee46da40fe72780c9ad086be4e9d062e3f6acd55eb11e1f6e24bc9f6a525
        source_review: _compare/relationships-2026-11-16/review-current/Johnson2022
        source_status_sha256: 2335f24de7dd6066d19cb711304977d5fa1f777ec738c88be954fde112457a8e
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P7-S1-C8:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 74eaee46da40fe72780c9ad086be4e9d062e3f6acd55eb11e1f6e24bc9f6a525
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: d2229d92be14a786a47cb31cb57ea004d4f6e039bfa3520b55e1f91e0fd655f3
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P7-S1-C8
          page: 7
          text_layer_sha256: d2229d92be14a786a47cb31cb57ea004d4f6e039bfa3520b55e1f91e0fd655f3
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: 'The Overall

          Model explained 27% of the variance in residual WAB AQ

          scores controlled for lesion to critical language regions (Adj.

          R2 ¼ .27, F (16.6,101) ¼ 10.8), P < .00001).'
        anchor_text: 'The Overall

          Model explained 27% of the variance in residual WAB AQ

          scores controlled for lesion to critical language regions (Adj.

          R2 ¼ .27, F (16.6,101) ¼ 10.8), P < .00001).'
        excluded_fragments: []
        image_sha256: a13448fee21655489f162c743cd2fc6a3cdc1a15efc3ab1d8902c6313c585433
      P7-S1-C9:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 74eaee46da40fe72780c9ad086be4e9d062e3f6acd55eb11e1f6e24bc9f6a525
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 2a064f5431b6118c259d504c8fe855dd9330c2257e2054ec7a03e237b34765ee
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P7-S1-C9
          page: 7
          text_layer_sha256: 2a064f5431b6118c259d504c8fe855dd9330c2257e2054ec7a03e237b34765ee
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: 'The correlation be-

          tween actual and predicted values for this model was statis-

          tically signiﬁcant (r ¼ .45, P < .00001).'
        anchor_text: 'The correlation be-

          tween actual and predicted values for this model was statis-

          tically signiﬁcant (r ¼ .45, P < .00001).'
        excluded_fragments: []
        image_sha256: e09fa0351cc25b637bdb8486754221b148b4170ceaeca262481a74c88af6a885
      P7-S1-C4:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 74eaee46da40fe72780c9ad086be4e9d062e3f6acd55eb11e1f6e24bc9f6a525
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 735cae4cad5bb77c0a06be2deeabd00ec155e66aee9a19197a8d9b05f6c0988a
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P7-S1-C4
          page: 7
          text_layer_sha256: 735cae4cad5bb77c0a06be2deeabd00ec155e66aee9a19197a8d9b05f6c0988a
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Stepwise regression with leave-one-out cross

          validation results: Overall Model

          A total of 106 participants had all data available and were

          included in the Overall Model.'
        anchor_text: 'Stepwise regression with leave-one-out cross

          validation results: Overall Model

          A total of 106 participants had all data available and were

          included in the Overall Model.'
        excluded_fragments: []
        image_sha256: 933956294410cfd01bb7f20d6b16e35e710318cf100405e13e9cb3fa82503224
        transcription: 'Stepwise regression with leave-one-out cross

          validation results: Overall Model


          A total of 106 participants had all data available and were

          included in the Overall Model'
      P3-S3-C7:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 74eaee46da40fe72780c9ad086be4e9d062e3f6acd55eb11e1f6e24bc9f6a525
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: d6efc599494a4c0ee3691c4c257e24fb9cf74e23fa0497ce9fd62cbcb38d44cc
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S3-C7
          page: 3
          text_layer_sha256: d6efc599494a4c0ee3691c4c257e24fb9cf74e23fa0497ce9fd62cbcb38d44cc
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: "Inclusion criteria for this analysis were deﬁned prior to\n\
          data analysis and were as follows: availability of aphasia\nseverity\nscores\n\
          as\nindicated\nby\na\nWestern\nAphasia\nBatteryeRevised (Kertesz, 2007)\
          \ (WAB-R) Aphasia Quotient\n(WAB-AQ), structural neuroimaging data obtained\
          \ within 6\nmonths of language testing (M ¼ 6.0 ± 19.4 days; range ¼ 0e163\n\
          days), 21e85 years old, pre-morbidly right-handed, and in the\nchronic stage\
          \ of recovery (\x026 months post-onset) following a\nleft hemisphere stroke\
          \ (M ¼ 38.5 ± 45.9; range ¼ 6e212)."
        anchor_text: "Inclusion criteria for this analysis were deﬁned prior to\n\
          data analysis and were as follows: availability of aphasia\nseverity\nscores\n\
          as\nindicated\nby\na\nWestern\nAphasia\nBatteryeRevised (Kertesz, 2007)\
          \ (WAB-R) Aphasia Quotient\n(WAB-AQ), structural neuroimaging data obtained\
          \ within 6\nmonths of language testing (M ¼ 6.0 ± 19.4 days; range ¼ 0e163\n\
          days), 21e85 years old, pre-morbidly right-handed, and in the\nchronic stage\
          \ of recovery (\x026 months post-onset) following a\nleft hemisphere stroke\
          \ (M ¼ 38.5 ± 45.9; range ¼ 6e212)."
        excluded_fragments: []
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 7
  quote: 'The Overall

    Model explained 27% of the variance in residual WAB AQ

    scores controlled for lesion to critical language regions (Adj.

    R2 ¼ .27, F (16.6,101) ¼ 10.8), P < .00001).'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-24'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
