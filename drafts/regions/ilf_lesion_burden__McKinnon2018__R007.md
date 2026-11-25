---
id: ilf_lesion_burden
name: ILF lesion burden
kind: network
findings:
- id: f1
  target_audit:
    status: behaviour_label_present
    category: behaviour_or_language_construct
    original_target: semantic_paraphasias
    reason: Label names a behaviour or language construct; its exact operational definition and measurement
      still need source review.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  outcome_measurement:
    status: identified
    instruments:
    - name: Philadelphia Naming Test
    metric: Semantic paraphasias as percentage of attempted responses; averaged over two sessions
    definition_source:
      citation: '@McKinnon2018'
      page: 3
      quote: "The PNT results from both sessions were \naveraged, and semantic and phonemic paraphasias\
        \ were expressed as a percentage of naming attempts excluding \nthe number of no responses since\
        \ we were interested in semantic and phonemic paraphasias when naming was \nattempted."
      basis: Published source passage
    note: Measurement metadata identified from source evidence; finding remains unapproved.
  target: semantic_paraphasias
  target_kind: impairment
  claim: ILF lesion burden was associated with the percentage of semantic paraphasias
  direction: likely
  relationship: correlational
  method: LSM
  sample:
    n: not_reported
    population: right-handed native English speakers with a history of a single previous
      ischemic stroke in the left hemisphere
    phase: not_reported
    time_post_onset: chronic post-stroke aphasia (at least 6 months before enrollment)
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - small sample size
  - ILF location also highly overlaps with the location of the IFOF
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Patient lesion overlap with the third quartile of
    the JHU ILF ROI. semantic paraphasias expressed as a percentage of naming attempts
    excluding no responses. Additional metadata has not been transcribed; review the
    pending-field flags before approval. PDF image reading (P2-S3-C12, two-model agreement,
    human verification pending): . They were right-handed native English speakers
    with a history of a single previous ischemic stroke in the left hemisphere at
    least 6 months before enrollment Original text-layer quotation is preserved below.'
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
    - proposed_concept:semantic_paraphasias
  citation: '@McKinnon2018'
  source_passages:
  - section: Original source P7-S1-C7
    page: 7
    quote: "It is important to highlight that ILF lesion burden was associated with\
      \ the percentage of semantic paraphasias \n(r = 0.56, p < 0.05)."
    supports: claim
  - section: Original source P4-S2-C9
    page: 4
    quote: "White matter lesion overlap was calculated as the cross-section between\
      \ the manually delineated lesion mask \nand the third quartile of the JHU SLF\
      \ and ILF ROIs."
    supports: method
  - section: Original source P2-S3-C10
    page: 2
    quote: "We studied 32 participants with chronic post-stroke aphasia (age: 57 ± 11 y,\
      \ time post-stroke: \n35 ± 30 mos, gender: 8 women)."
    supports: sample
  - section: Original source P2-S3-C12
    page: 2
    quote: "They were right-handed native English speakers with a history of a single\
      \ previous ischemic \nstroke in the left hemisphere at least 6 months before\
      \ enrollment."
    supports: sample
  - section: Original source P3-S1-C4
    page: 3
    quote: "The PNT results from both sessions were \naveraged, and semantic and phonemic\
      \ paraphasias were expressed as a percentage of naming attempts excluding \n\
      the number of no responses since we were interested in semantic and phonemic\
      \ paraphasias when naming was \nattempted."
    supports: confounders
  - section: Original source P9-S2-C7
    page: 9
    quote: "It is a limitation of this study that only the ILF and the SLF were studied\
      \ in a small number of cases with-\nout the assessment of other tracts and other\
      \ naming errors related to the multiple subnetworks that form the \ndual stream\
      \ system."
    supports: limitation
  - section: Original source P9-S2-C11
    page: 9
    quote: "Similarly, the posterior location of the ILF also highly overlaps with\
      \ the \nlocation of the IFOF."
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-25'
relationship_review:
  paper: McKinnon2018
  proposal_id: R007
  review_status_sha256: 769f9dfe804092fcb0c19e5644eda528e69ca3cf1acfb97910f04c99003b1bbb
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: c141c56e0b5b299191f71db4af857a81a8ba5ecf06c956be1d89c30435ebf061
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: c141c56e0b5b299191f71db4af857a81a8ba5ecf06c956be1d89c30435ebf061
        A/passages.json: 9dc9f4cf9c5fbc715a7825eb76954786670bc8fb83f3d26cbdde6bc073e9c577
        A/raw.json: 53ae0816cdbdabcedc4403a6fd88bd82fdbbe726643927e630fcbe981f5ba2ab
        A/source-units.json: a16bc14c74a9500441f19f54f884fbc30afb0e6eeed074b3e015e5f90ce4bc8b
        A/full-source-units.json: 752c7a3f7c8929110f89bc92f0ba8dbfe28eea348d88af1f22524dd31e8a516e
        A/meta.json: 8b039803dd63eb48066a0f78563371c6a5c0f263401b80552ceec293e6938463
        A/table-images/TABLE-1-page-6-1.png: 7cda6a108993b77af1078ec5b8a4bfd804975178a034711805e33b1f48c61bb7
        A/table-images/page-6.png: aff27333a1b68f000050cb5d529754e304371f09a0ff839d5ff6b1bd34069342
        A/table-images/manifest.json: ee867223fb6086cca0314355043f612d32c5d14e0e715b32e532a8d2b7fa8dda
        A/table-images/TABLE-2-page-6-2.png: 2b1d2984ff34aa5f182fa8d0ddf551be67d0b713b2fe84cbd507e6f510af5c70
        A/clauses/window-03/raw.json: 82b1a0511e644e9ff522f066cae54016fbc7649e4c538389ab9e8fd7d20304e1
        A/clauses/window-03/prompt.txt: e0a71dcc13252413e99d2f6f3e8de65e9b21747cb5e50fb0ff6305baf480f7bb
        A/clauses/window-03/meta.json: 153f1db8bcb55f429b334f27bcb882a145dd9059ffb8cb245409c972f7dd56b7
        A/clauses/window-04/raw.json: 73caed22e33c4c4c259be978f483e43b3dc887f61434f5ccf09ba190b3688f97
        A/clauses/window-04/prompt.txt: a48f99c4930352c1b8457aa178b6640b435122b85e78634a5f87d7280a702a5c
        A/clauses/window-04/meta.json: e2812ef2512c0e1a828259a29c3e85320a393d562cff5db570515d96bc610a73
        A/clauses/window-05/raw.json: 277d12ae948996e9cce21585b88ac24603e6a9c635a13a953049c81b4ff8e1df
        A/clauses/window-05/prompt.txt: 3a4064689cf93eb44db404beed0d362947b2e500ce38cc44930da555eb178a1e
        A/clauses/window-05/meta.json: 3d444d0d318a31015784eb99063a00aa437a1e1b5ab4d48e5cabc6b9e80f9032
        A/clauses/window-02/raw.json: 8a6234a1fa92c097f470c60e42aa0cf0bbf5a6bbbdc64d87039245b58f1fd261
        A/clauses/window-02/prompt.txt: ba143af475bb52b4fb7f5af213ed39941fe8a3b4b2751cfda85289de75949f92
        A/clauses/window-02/meta.json: 6104cb1b80145e2f4f61db72f8e4d35542c3ed55f4b5c17f2fe962b891676fc6
        A/clauses/window-09/raw.json: e31b5912340a9559c8e2196261760f4b326776bd94a570a041d17d5c2885c604
        A/clauses/window-09/prompt.txt: 3f7e1e31248bf504a5af4fb1c3c125fec210352293fd19b0df11d95787e9d73d
        A/clauses/window-09/meta.json: 852b06da19117a23691ad9e950c04e78a55671dae2757eadebcf0f5343a4b0ff
        A/clauses/window-07/raw.json: b3ed0817b45a450fd67a9aac66098b9cee39627d775656cd8b7bccefe5429bcc
        A/clauses/window-07/prompt.txt: 42a2f9a1cc2640647bbe913c046aa30794671e90d2cbbfa8e516b1c472ca2083
        A/clauses/window-07/meta.json: c3c77d3595aae08d64af240d30af993b6054735bd34b94bee4cfa6983a7d9ec3
        A/clauses/window-01/raw.json: 5765c9319f711c9f1f14c6c5edbaa9d6201672956d34abc4a6873f0e2861b80e
        A/clauses/window-01/prompt.txt: 5ce98b7cd6ddf9ca4291f6cf5c7ac0a631caf1ececd620105d818ece47821f0b
        A/clauses/window-01/meta.json: 7ba33950a7d6e37c6f5e0e84219c4590894deddbdcfccc6475bb53cb99af7ae9
        A/clauses/window-06/raw.json: 3256d07f5ffa97af69b41bfc198682ac35d12cdf249110af36e1abc7e9b24b3a
        A/clauses/window-06/prompt.txt: 502d8fc56fff47d6f3a623fcf60a58e3ead5151ac9346d2d23d5fca999e87d90
        A/clauses/window-06/meta.json: 6628b05908b38e926c5b5591522dd302439d372affb0346fa0556a435b9725e2
        A/clauses/window-08/raw.json: f3974b1f3514429b79dd97c0098134744147cfb56ab0c5193d3d3fe2b928769a
        A/clauses/window-08/prompt.txt: eaccb19aebb351f7348b2f49d80b2ec31bc1fb99c77e9880b73f42104bc91e61
        A/clauses/window-08/meta.json: 659325bc700ea49461103519e21d7aa5b4d5428f0847a1fa45f63022d74e05d1
        A/tables/TABLE-1-page-6-1/raw.json: a50604a973d811a36a551fd5211130c9eb59016d6d53e4547562714bbbaf7b5e
        A/tables/TABLE-1-page-6-1/prompt.txt: 2507b7350878255be6c7f262019dff934e3a552ec18dc80eb6c8596ed2bb5258
        A/tables/TABLE-1-page-6-1/meta.json: 539fb35150492dacb2ee9813891d3980628337f0c7a0483a60e2ff5875cc9367
        A/tables/TABLE-2-page-6-2/raw.json: 425f56d650f826dbef9e28cd22d0dd53617d6f3e1eb2ee08e0d2bd3c8684023e
        A/tables/TABLE-2-page-6-2/prompt.txt: 6b5a3fc4dd85359ff7bb7925132d52872a3540f3db77e75a06fe10e544466ea0
        A/tables/TABLE-2-page-6-2/meta.json: a6e6f5ad7764f8d79a2d3bfb759d4ff4004a8659a566eeb97f823df696e04fee
        B/passages.json: 9dc9f4cf9c5fbc715a7825eb76954786670bc8fb83f3d26cbdde6bc073e9c577
        B/raw.json: 3e8f4f18af1fdc0d405a09b3a77621cb6cf55d25cf45e7a1563f69a1054bcd0d
        B/source-units.json: a16bc14c74a9500441f19f54f884fbc30afb0e6eeed074b3e015e5f90ce4bc8b
        B/full-source-units.json: 752c7a3f7c8929110f89bc92f0ba8dbfe28eea348d88af1f22524dd31e8a516e
        B/meta.json: 93543ae8420caf7b69286084b000877e564204b2b985d2d3d358b6de76c1ca62
        B/table-images/TABLE-1-page-6-1.png: 7cda6a108993b77af1078ec5b8a4bfd804975178a034711805e33b1f48c61bb7
        B/table-images/page-6.png: aff27333a1b68f000050cb5d529754e304371f09a0ff839d5ff6b1bd34069342
        B/table-images/manifest.json: 8c75f89b52be741ec23346ebf99b08f82fcd5f7629d17f81eff9706fd2ccad12
        B/table-images/TABLE-2-page-6-2.png: 2b1d2984ff34aa5f182fa8d0ddf551be67d0b713b2fe84cbd507e6f510af5c70
        B/clauses/window-03/raw.json: f1bec83140e4ce2fdcb860d9cac20bbb307321083ef4b42985df0a16c194c62b
        B/clauses/window-03/prompt.txt: e0a71dcc13252413e99d2f6f3e8de65e9b21747cb5e50fb0ff6305baf480f7bb
        B/clauses/window-03/meta.json: 9209838635586662210948daf89b984f55609535513e0e1f7e90c86d1661e0c3
        B/clauses/window-04/raw.json: 2e4e8cfaec947b6936de70e8d518c89be8bcc99554d6f83662435fd3daeb3347
        B/clauses/window-04/prompt.txt: a48f99c4930352c1b8457aa178b6640b435122b85e78634a5f87d7280a702a5c
        B/clauses/window-04/meta.json: 011453fea961d157f62f3b0c3b0d2f398c0f5f1439614c6884daba7419b8c664
        B/clauses/window-05/raw.json: c5e47d3fb7050cd2c9a63dc26ce822cdd63fd89ad23230a40aa74d27b0f8bad2
        B/clauses/window-05/prompt.txt: 3a4064689cf93eb44db404beed0d362947b2e500ce38cc44930da555eb178a1e
        B/clauses/window-05/meta.json: 4870357be836111a9a3ae2c257c1b839e264bf16eb7c8417f393c4cb11f17df3
        B/clauses/window-02/raw.json: 69cdd8425dfc9c82615988bf6d81d15f8c6d82ea430d0ad7467949b5617cb81d
        B/clauses/window-02/prompt.txt: ba143af475bb52b4fb7f5af213ed39941fe8a3b4b2751cfda85289de75949f92
        B/clauses/window-02/meta.json: 1157e123e856a5e26888866b60b6c6dfbab9c86318b3a9d2a553b8f7e488eadc
        B/clauses/window-09/raw.json: be7ebb11a203b9ba965745d2b2f5cfd32421d5a7d4f812dcab1fb11d52b67d2f
        B/clauses/window-09/prompt.txt: 3f7e1e31248bf504a5af4fb1c3c125fec210352293fd19b0df11d95787e9d73d
        B/clauses/window-09/meta.json: e682e845b876f47455bee7869d21af1a8bbf07bd92bfb4b40ec888b373e7863b
        B/clauses/window-07/raw.json: 3f1095208ca55349d9f184a9395e0957b8233cb523b0ff4057abe6acc555d17d
        B/clauses/window-07/prompt.txt: 42a2f9a1cc2640647bbe913c046aa30794671e90d2cbbfa8e516b1c472ca2083
        B/clauses/window-07/meta.json: 1d80134c3973aa761786c819667c84dd54d08637676f8b4eb902ee508097aade
        B/clauses/window-01/raw.json: 80d1bdcf634a7b2d13a781991e00dc50dc541a45b0ecba969530498fd9f77293
        B/clauses/window-01/prompt.txt: 5ce98b7cd6ddf9ca4291f6cf5c7ac0a631caf1ececd620105d818ece47821f0b
        B/clauses/window-01/meta.json: e011b067e42e5e4ecf05bc64475d6fb8f82e35c9ab659e8f824e7380dc17313b
        B/clauses/window-06/raw.json: 0526181fceb5c2a544dc10344681dd09f6d52a989dcaf86b4520f436e1e65b98
        B/clauses/window-06/prompt.txt: 502d8fc56fff47d6f3a623fcf60a58e3ead5151ac9346d2d23d5fca999e87d90
        B/clauses/window-06/meta.json: 635dfb4519aa7d0fb5a06ee3246d798b1e303a8bad6b4fd17fb180a3db60f8e7
        B/clauses/window-08/raw.json: f2f4496b8fb65de329ae80662c0e60b107f198c7fd1554a8fb3635d05eca3a85
        B/clauses/window-08/prompt.txt: eaccb19aebb351f7348b2f49d80b2ec31bc1fb99c77e9880b73f42104bc91e61
        B/clauses/window-08/meta.json: d208bcf9c41204b8f233bed3ab4510bec476b62db482fa96bb87b5b4281b7854
        B/tables/TABLE-1-page-6-1/raw.json: e41e5c0743e901448aceb205cc187c89d8eeaf077d200d8e961381f5c9fb7152
        B/tables/TABLE-1-page-6-1/prompt.txt: 2507b7350878255be6c7f262019dff934e3a552ec18dc80eb6c8596ed2bb5258
        B/tables/TABLE-1-page-6-1/meta.json: f543204bec76c796c757ae6833711881fc74af2924f81c5db340895a35b1723e
        B/tables/TABLE-2-page-6-2/raw.json: 5bf151d0009c498c47573311ab46bc287d7406be00dec3c5541c3ce6c6560061
        B/tables/TABLE-2-page-6-2/prompt.txt: 6b5a3fc4dd85359ff7bb7925132d52872a3540f3db77e75a06fe10e544466ea0
        B/tables/TABLE-2-page-6-2/meta.json: 75a9df23c11748f32390d0a3a64041385d7938d790d484d11c048b4760dccfa7
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
      pdf_sha256: c141c56e0b5b299191f71db4af857a81a8ba5ecf06c956be1d89c30435ebf061
      source_review: _compare/relationships-2026-11-16/review-current/McKinnon2018
      source_status_sha256: 2d5a25773d515e944f57fd5347a9767f904bef0165e7945ffbd0cd249ebaf18d
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R007
    exposure:
      text: ILF lesion burden
    outcome:
      text: percentage of semantic paraphasias
    analysis_label: Lesion burden analysis
    relation: association
    evidence_ids:
    - P7-S1-C7
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
      pdf_sha256: c141c56e0b5b299191f71db4af857a81a8ba5ecf06c956be1d89c30435ebf061
      source_review: _compare/relationships-2026-11-16/review-current/McKinnon2018
      source_status_sha256: 2d5a25773d515e944f57fd5347a9767f904bef0165e7945ffbd0cd249ebaf18d
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Accounting without a linked unit P5-S2-C12
      - Accounting without a linked unit P5-S2-C13
      - Accounting without a linked unit P5-S2-C14
      - Accounting without a linked unit P5-S2-C15
      - Unaccounted source passage P5-S2-C15
      - Unaccounted source passage P5-S2-C13
      - Unaccounted source passage P5-S2-C14
      - Unaccounted source passage P5-S2-C12
      - Result passage disposed without unit P5-S2-C18
      - Result passage disposed without unit P6-S1-C1
      - Result passage disposed without unit P6-S1-C2
      - Accounting without a linked unit P6-S1-C5
      - Unaccounted source passage P6-S1-C5
      - Result passage disposed without unit P6-S1-C10
      - Result passage disposed without unit P6-S1-C11
      - Result passage disposed without unit P6-S1-C12
      - Result passage disposed without unit P6-S1-C9
      - Result passage disposed without unit P7-S1-C10
      - Accounting without a linked unit P7-S1-C12
      - Accounting without a linked unit P7-S1-C5
      - Accounting without a linked unit P7-S1-C6
      - Accounting without a linked unit P7-S1-C7
      - 'window 7: invalid/duplicate disposition P7-S1-C8'
      - Accounting without a linked unit P7-S1-C9
      - Unaccounted source passage P7-S1-C9
      - Unaccounted source passage P7-S1-C12
      - Unaccounted source passage P7-S1-C6
      - Unaccounted source passage P7-S1-C7
      - Unaccounted source passage P7-S1-C5
      - Accounting without a linked unit P7-S2-C11
      - Accounting without a linked unit P7-S2-C4
      - Accounting without a linked unit P7-S2-C5
      - Accounting without a linked unit P7-S2-C6
      - Accounting without a linked unit P8-S1-C2
      - Accounting without a linked unit P8-S1-C3
      - Unaccounted source passage P8-S1-C2
      - Unaccounted source passage P7-S2-C4
      - Unaccounted source passage P7-S2-C5
      - Unaccounted source passage P7-S2-C6
      - Unaccounted source passage P8-S1-C3
      - Unaccounted source passage P7-S2-C11
      - Result passage disposed without unit P9-S1-C11
      - Accounting without a linked unit P9-S3-C12
      - Result passage disposed without unit P9-S3-C8
      - Unaccounted source passage P9-S3-C12
      unattached_null_or_qualifier_ids:
      - P5-S2-C18
      - P6-S1-C4
      - P6-S1-C12
      - P7-S1-C10
      - P7-S2-C4
      - P7-S2-C5
      - P7-S2-C6
      suppressed_nonrepresented_units: 6
      default_disposition_count_requires_completeness_check: 180
      unselected_timing_passages:
      - P1-S1-C9
      - P2-S3-C12
      - P2-S3-C14
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P6-S1-C13
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S2-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P6-S1-C11
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: limitations
        source_ids:
        - P9-S2-C7
        - P9-S2-C10
        - P9-S2-C11
        - P9-S3-C4
        - P9-S3-C5
        - P9-S3-C6
        - P10-S1-C2
        - P10-S1-C3
        - P10-S1-C5
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - validation
      - limitations
      - personal_factors
      - tested_personal_effects
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-6-1
      - TABLE-2-page-6-2
      unlinked_tables:
      - TABLE-2-page-6-2
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P3-S2
        - P4-S1
        - P4-S3
        - P5-S1
        - P5-S2
        - P5-S3
        - P6-S1
        - P7-S1
        - P7-S2
        - P8-S1
        - P8-S2
        - P8-S3
        - P9-S3
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: c141c56e0b5b299191f71db4af857a81a8ba5ecf06c956be1d89c30435ebf061
      source_review: _compare/relationships-2026-11-16/review-current/McKinnon2018
      source_status_sha256: 2d5a25773d515e944f57fd5347a9767f904bef0165e7945ffbd0cd249ebaf18d
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C11
      disposition: repeated
      result_indexes:
      - 0
      - 3
      reason: Abstract restatement of results found in Tables 1 and 2.
    - source_id: P5-S2-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive statistics of aphasia severity.
    - source_id: P5-S2-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive statistics of naming accuracy.
    - source_id: P5-S2-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive statistics of paraphasia frequency.
    - source_id: P5-S2-C15
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive results of the Pyramids and Palm Trees Test.
    - source_id: P5-S2-C18
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive count of subjects with identifiable tracts.
    - source_id: P6-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive count of subjects with identifiable tracts.
    - source_id: P6-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive statement about tract co-occurrence.
    - source_id: P6-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to Tables 1 and 2.
    - source_id: P6-S1-C5
      disposition: represented
      result_indexes:
      - 0
      reason: Reports association between ILF AWF and semantic paraphasias.
    - source_id: P6-S1-C7
      disposition: represented
      result_indexes:
      - 1
      reason: Reports association between ILF FA and semantic paraphasias.
    - source_id: P6-S1-C8
      disposition: represented
      result_indexes:
      - 2
      reason: Reports null association between SLF metrics and semantic paraphasias.
    - source_id: P6-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of sample size and power.
    - source_id: P6-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of statistical power.
    - source_id: P6-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of random sampling analysis.
    - source_id: P6-S1-C12
      disposition: repeated
      result_indexes:
      - 2
      reason: Restatement of null association between SLF and semantic paraphasias.
    - source_id: P7-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison of effect sizes (Fisher r-to-z) rather than a primary association.
    - source_id: P7-S1-C2
      disposition: represented
      result_indexes:
      - 3
      reason: Reports association between SLF AWF and phonemic paraphasias.
    - source_id: P7-S1-C4
      disposition: represented
      result_indexes:
      - 4
      reason: Reports weak association between SLF FA and phonemic paraphasias.
    - source_id: P7-S1-C5
      disposition: represented
      result_indexes:
      - 5
      reason: Reports null association between ILF metrics and phonemic paraphasias.
    - source_id: P7-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison of effect sizes (Fisher r-to-z).
    - source_id: P7-S1-C7
      disposition: represented
      result_indexes:
      - 6
      reason: Reports association between ILF lesion burden and semantic paraphasias.
    - source_id: P7-S1-C9
      disposition: represented
      result_indexes:
      - 7
      - 8
      reason: Reports results of lesion-adjusted linear models.
    - source_id: P7-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports correlation between AWF and FA and stepwise regression model
        selection.
    - source_id: P7-S1-C12
      disposition: represented
      result_indexes:
      - 9
      reason: Reports association between infra-Sylvian gray matter necrosis and semantic
        paraphasias.
    - source_id: P7-S2-C3
      disposition: represented
      result_indexes:
      - 10
      reason: Reports null result for gray matter damage when corrected for AWF.
    - source_id: P7-S2-C4
      disposition: represented
      result_indexes:
      - 11
      reason: Reports significant result for AWF when adjusted for gray matter necrosis.
    - source_id: P7-S2-C5
      disposition: represented
      result_indexes:
      - 12
      reason: Reports null association between supra-Sylvian gray matter and phonemic
        paraphasias.
    - source_id: P7-S2-C6
      disposition: represented
      result_indexes:
      - 13
      - 14
      reason: Reports association between SLF AWF and SMG necrosis, and null association
        between SMG necrosis and phonemic paraphasias.
    - source_id: P7-S2-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Section header.
    - source_id: P8-S1-C2
      disposition: repeated
      result_indexes:
      - 0
      - 5
      reason: Discussion restatement of double dissociation.
    - source_id: P8-S1-C3
      disposition: repeated
      result_indexes:
      - 3
      - 2
      reason: Discussion restatement of double dissociation.
    - source_id: P8-S2-C8
      disposition: repeated
      result_indexes:
      - 3
      - 0
      reason: Discussion restatement of results.
    - source_id: P8-S3-C4
      disposition: repeated
      result_indexes:
      - 3
      reason: Discussion restatement of SLF AWF association.
    - source_id: P9-S1-C11
      disposition: repeated
      result_indexes:
      - 0
      - 3
      reason: Discussion restatement of posterior tract associations.
    - source_id: P9-S2-C6
      disposition: repeated
      result_indexes:
      - 0
      - 3
      reason: Discussion conclusion about posterior damage.
    - source_id: P9-S3-C8
      disposition: repeated
      result_indexes:
      - 0
      reason: Discussion restatement of ILF AWF association.
    - source_id: P9-S3-C12
      disposition: repeated
      result_indexes:
      - 3
      reason: Discussion restatement of SLF AWF association.
    unresolved_coverage: []
    pending_source_ids:
    - P1-S1-C11
    - P5-S2-C12
    - P5-S2-C13
    - P5-S2-C14
    - P5-S2-C15
    - P5-S2-C18
    - P6-S1-C1
    - P6-S1-C2
    - P6-S1-C4
    - P6-S1-C9
    - P6-S1-C10
    - P6-S1-C11
    - P6-S1-C12
    - P7-S1-C1
    - P7-S1-C6
    - P7-S1-C10
    - P7-S2-C11
    - P8-S1-C2
    - P8-S1-C3
    - P8-S2-C8
    - P8-S3-C4
    - P9-S1-C11
    - P9-S2-C6
    - P9-S3-C8
    - P9-S3-C12
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-6-1
    - TABLE-2-page-6-2
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P2-S3-C10
      recruited_sample:
      - P2-S3-C11
      eligibility:
      - P2-S3-C12
      - P2-S3-C14
      imaging_provenance:
      - P3-S2-C4
      - P4-S2-C2
      - P4-S2-C6
      - P4-S2-C9
      - P5-S1-C8
      - P5-S1-C9
      imaging_timing:
      - P2-S3-C10
      outcome_timing:
      - P2-S3-C10
      outcome_definition:
      - P2-S4-C10
      - P2-S4-C11
      - P2-S4-C12
      - P3-S1-C4
      validation: []
      analysis_restrictions:
      - P4-S2-C2
      - P4-S2-C9
      - P5-S1-C9
      - P7-S1-C8
      dependent_variable_statement:
      - P5-S2-C5
      limitations: []
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P5-S2-C5
      - P7-S1-C8
      - P7-S2-C4
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P2-S3-C10
      - P2-S3-C12
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P6-S1-C13
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S2-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P6-S1-C11
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: limitations
      source_ids:
      - P9-S2-C7
      - P9-S2-C10
      - P9-S2-C11
      - P9-S3-C4
      - P9-S3-C5
      - P9-S3-C6
      - P10-S1-C2
      - P10-S1-C3
      - P10-S1-C5
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
      pdf_sha256: c141c56e0b5b299191f71db4af857a81a8ba5ecf06c956be1d89c30435ebf061
      review_sha256: 769f9dfe804092fcb0c19e5644eda528e69ca3cf1acfb97910f04c99003b1bbb
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
      - P7-S1-C7
      source_result: ILF lesion burden was associated with the percentage of semantic
        paraphasias (r = 0.56, p < 0.05).
      result_status: detected
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The source P7-S1-C7 explicitly reports the association between ILF
            lesion burden and semantic paraphasias. The proposed core correctly identifies
            this specific analysis, distinct from the tract-based microstructure analyses
            (AWF/FA) which are discussed in adjacent passages but are separate predictors.
          source_ids:
          - P7-S1-C7
          - P7-S1-C8
        direction:
          answer: fits
          reason: The source reports a positive correlation (r = 0.56), indicating
            that higher lesion burden is associated with a higher percentage of semantic
            paraphasias. The proposed core uses the direction 'likely' which is a
            valid qualitative representation of a detected positive association without
            specifying the sign, or potentially implying the expected direction of
            impairment. It does not contradict the source.
          source_ids:
          - P7-S1-C7
        construct:
          answer: fits
          reason: The exposure is correctly identified as ILF lesion burden, defined
            in P4-S2-C9 as the cross-section between the lesion mask and the third
            quartile of the JHU ILF ROI. The outcome is the percentage of semantic
            paraphasias, defined in P3-S1-C4 as a percentage of naming attempts excluding
            no responses. The method is a linear model/correlation as per P5-S2-C4
            and P7-S1-C7.
          source_ids:
          - P4-S2-C9
          - P3-S1-C4
          - P7-S1-C7
        qualifications:
          answer: fits
          reason: The proposed core includes the qualification that semantic paraphasias
            are expressed as a percentage of naming attempts excluding no responses,
            which matches P3-S1-C4. It also includes limitations regarding sample
            size and IFOF overlap (P9-S2-C7, P9-S2-C11). The core does not incorrectly
            claim this is the primary result or omit material caveats about the specific
            measurement definition.
          source_ids:
          - P3-S1-C4
          - P9-S2-C7
          - P9-S2-C11
        missing_material_caveat:
          answer: fits
          reason: The core captures the essential definition of the exposure (lesion
            overlap) and outcome (percentage of attempts). While the source notes
            that this association was used to justify controlling for lesion burden
            in subsequent models (P7-S1-C8), the core is describing the standalone
            finding of the association itself, which is valid. No material caveat
            that changes the interpretation of this specific correlation is omitted.
          source_ids:
          - P7-S1-C7
          - P7-S1-C8
      optional_pending:
      - Sample size for this specific correlation (n=32 vs subset) is not explicitly
        transcribed in the core, though P2-S3-C10 mentions 32 participants generally.
      - Exact p-value and r-value are not transcribed in the core fields, only the
        qualitative association.
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Sample size requires source confirmation; it has not been transcribed.
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Sample size for this specific correlation (n=32 vs subset) is not explicitly
      transcribed in the core, though P2-S3-C10 mentions 32 participants generally.
    - Exact p-value and r-value are not transcribed in the core fields, only the qualitative
      association.
    normalizations:
    - field: sample.n
      original: 32
      action: not_transcribed
      reason: Not supported by selected quotations
    analysis_identity:
      id: R007
      exposure:
        text: ILF lesion burden
      outcome:
        text: percentage of semantic paraphasias
      analysis_label: Lesion burden analysis
      relation: association
      evidence_ids:
      - P7-S1-C7
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
        pdf_sha256: c141c56e0b5b299191f71db4af857a81a8ba5ecf06c956be1d89c30435ebf061
        source_review: _compare/relationships-2026-11-16/review-current/McKinnon2018
        source_status_sha256: 2d5a25773d515e944f57fd5347a9767f904bef0165e7945ffbd0cd249ebaf18d
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P2-S3-C10:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: c141c56e0b5b299191f71db4af857a81a8ba5ecf06c956be1d89c30435ebf061
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: c47965bb5154306ebc7b54aa95113505f6b0703c057a59be5d9dfabcfc9a351e
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S3-C10
          page: 2
          text_layer_sha256: c47965bb5154306ebc7b54aa95113505f6b0703c057a59be5d9dfabcfc9a351e
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: "We studied 32 participants with chronic post-stroke aphasia\
          \ (age: 57 ± 11 y, time post-stroke: \n35 ± 30 mos, gender: 8 women)."
        anchor_text: "We studied 32 participants with chronic post-stroke aphasia\
          \ (age: 57 ± 11 y, time post-stroke: \n35 ± 30 mos, gender: 8 women)."
        excluded_fragments: []
        image_sha256: 0ab483367f276b1283f6a2fec8c666068ffb3ecd9b16e3f7e32f23d74b8caa2f
      P2-S3-C12:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: c141c56e0b5b299191f71db4af857a81a8ba5ecf06c956be1d89c30435ebf061
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: b9473b03a5223721110e27fe31735fe31481cf77dd4f7a7ca1d02fa18091897e
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S3-C12
          page: 2
          text_layer_sha256: b9473b03a5223721110e27fe31735fe31481cf77dd4f7a7ca1d02fa18091897e
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "They were right-handed native English speakers with a history\
          \ of a single previous ischemic \nstroke in the left hemisphere at least\
          \ 6 months before enrollment."
        anchor_text: "They were right-handed native English speakers with a history\
          \ of a single previous ischemic \nstroke in the left hemisphere at least\
          \ 6 months before enrollment."
        excluded_fragments: []
        image_sha256: a732920746bb173ed4314ef29d55075b6c688b0ce1429a1d175f537a42dffcba
        transcription: . They were right-handed native English speakers with a history
          of a single previous ischemic stroke in the left hemisphere at least 6 months
          before enrollment
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 7
  quote: "It is important to highlight that ILF lesion burden was associated with\
    \ the percentage of semantic paraphasias \n(r = 0.56, p < 0.05)."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-25'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
