---
id: pre_treatment_semantic_deficit
name: pre-treatment semantic deficit
kind: predictor
findings:
- id: f1
  target_audit:
    status: behaviour_label_present
    category: behaviour_or_language_construct
    original_target: pca_treatment_response
    reason: Label names a behaviour or language construct; its exact operational definition and measurement
      still need source review.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  outcome_measurement:
    status: needs_source_review
    instruments: []
    note: Outcome instrument/task is not yet verified for this finding. Do not infer it from the predictor
      or a paper-wide test list.
  target: pca_treatment_response
  target_kind: prognosis
  claim: a trend towards a negative relationship was found between a semantic deficit
    and response to treatment
  direction: unlikely
  relationship: correlational
  method: behavioral_only
  sample:
    n: not_reported
    population: right-handed, English-speaking individuals with aphasia following
      a single left-hemisphere cerebrovascular accident, at least 1 year post-onset,
      with a naming impairment (BNT < 75%)
    phase: not_reported
    time_post_onset: pre-treatment assessment and concurrent response during treatment
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - small sample size limits the power of the analysis
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: measured as the difference in performance between
    the version with semantic distractors (''a'') and the version without semantic
    distractors (''b'') of the Spoken Word–Written Word subtest of the PALPA. response
    to treatment was defined as the mean performance on probes during treatment sessions
    across all lists treated per participant; the finding is described as a trend
    (p = .065, one-tailed). Additional metadata has not been transcribed; review the
    pending-field flags before approval. PDF image reading (P4-S2-C4, two-model agreement,
    human verification pending): . All participants were right-handed, English-speaking
    individuals who had experienced a single left-hemisphere cerebrovascular accident
    and were at least 1 year post-onset at the time of enrolment Original text-layer
    quotation is preserved below. PDF image reading (P4-S2-C6, two-model agreement,
    human verification pending): . All participants had a

    naming impairment defined by less than 75% accuracy on the Boston Naming Test

    (BNT) (Goodglass et al., 2001) Original text-layer quotation is preserved below.'
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
    - proposed_concept:pca_treatment_response
  therapy:
    id: pca_treatment
    name: phonological components analysis treatment
  citation: '@Leonard2008'
  source_passages:
  - section: Original source P14-S1-C4
    page: 14
    quote: 'Finally, a trend towards a

      negative relationship (p 5 .065, one-tailed) between treatment performance and
      a

      semantic deficit (as measured by the difference in performance on the ‘‘a’’
      (with

      semantic distractors) and ‘‘b’’ (without semantic distractors) versions of the
      Spoken

      Word – Written Word subtest (PALPA 52)), was found.'
    supports: claim
  - section: Original source P13-S1-C5
    page: 13
    quote: 'Response to treatment was defined as the mean performance on probes during

      treatment sessions across all lists treated, per participant.'
    supports: method
  - section: Original source P4-S2-C4
    page: 4
    quote: 'All participants were right-handed, English-speaking individuals who had

      experienced a single left-hemisphere cerebrovascular accident and were at least
      1 year

      post-onset at the time of enrolment.'
    supports: sample
  - section: Original source P4-S2-C6
    page: 4
    quote: 'All participants had a

      naming impairment defined by less than 75% accuracy on the Boston Naming Test

      (BNT) (Goodglass et al., 2001).'
    supports: sample
  - section: Original source P14-S1-C5
    page: 14
    quote: 'Despite the good range in

      response to treatment evidenced by the participants (4.3–88.3% correct), it
      is

      acknowledged that due to the small sample size, the power of this analysis is
      limited.'
    supports: limitation
  - section: Original source P22-S1-C6
    page: 22
    quote: 'There was a positive trend noted in the correlational analysis between
      word

      repetition and response to treatment and a negative trend between a lexical
      semantic

      deficit and response to treatment.'
    supports: claim
predictor_type: behavioural
short_definition: measured as the difference in performance between the version with
  semantic distractors ('a') and the version without semantic distractors ('b') of
  the Spoken Word–Written Word subtest of the PALPA
assessment:
- PALPA Spoken Word–Written Word subtest
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-24'
relationship_review:
  paper: Leonard2008
  proposal_id: R007
  review_status_sha256: 79af570d069c68d2d60ab5fc77b8bedf41538ddace3ab6263d5c88d98be279aa
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: b2c3f70ccce9e12b75df84d02ec4f2080528b4ffccb3686a0465427365c25ff8
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: b2c3f70ccce9e12b75df84d02ec4f2080528b4ffccb3686a0465427365c25ff8
        A/passages.json: 639db63dbcaf8bcdbd68ee48c694c289a8c978d2328bbccb22ea41932ce76156
        A/raw.json: 494ec80683b8584c9a8e0a7c1fcdf1f987ef554fae2604985ae937beeeeb793f
        A/source-units.json: 064a3c7c45bf5b3be81b410ccd9aa4bc13bb38cfc10eeee0a2cf10977e51228d
        A/full-source-units.json: 7b76426dc0677ba643bc715e3444af872bace2d60f2228b53ebd0e70734f7b08
        A/meta.json: 525d021789ab5ca352f4564ad6724fe1c5a7a7188d29a17c8136eba9d78507de
        A/table-images/TABLE-6-page-21-3.png: 8ce09228d143c00104a6ebef90ef4a1c02ab90616283cfe600c28b6394182d62
        A/table-images/TABLE-1-page-5-1.png: 7d2b9ea7c6fd2b6066c0a7e0de957c0810870f06cefe1dee29d445a573d21522
        A/table-images/TABLE-5-page-21-2.png: 8ce09228d143c00104a6ebef90ef4a1c02ab90616283cfe600c28b6394182d62
        A/table-images/page-6.png: 639255ee453b679d9644d36e12ad9a960b3f28c1b909c6d0e8ae80003f6d087b
        A/table-images/page-7.png: 659b1788fe5c1fe23df13bc41960a4ebf9aec190688199c9a11052ce5a52e8c8
        A/table-images/page-5.png: 5559cfe2f49d999acec817dc58c06473edfcefc89b29ce7e869be5df4a340ef7
        A/table-images/TABLE-2-page-6-1.png: b9f35c4708d287e691c0f17f300f95f5bab69e2760118580ae758bee48f5f2aa
        A/table-images/manifest.json: 717a179b2f51c155ce83a80483be5768b60408b3cd7b5dcc3241db8a35d002c7
        A/table-images/page-21.png: be82e93938da5a354fd334ab3783b99bbe10f207ff0c4c89b95c1fbf0039dcfc
        A/table-images/TABLE-4-page-21-1.png: 8ce09228d143c00104a6ebef90ef4a1c02ab90616283cfe600c28b6394182d62
        A/table-images/TABLE-3-page-7-1.png: b1ff88d49263d317552ab712ee964b2323d9d6c1c4be5df3695b110d752c3bce
        A/clauses/window-03/raw.json: 7d6a3e683c77bc80fdd13170d50f2d2025a231035d0ce8562188b1d8504939d8
        A/clauses/window-03/prompt.txt: 2dc99494486f29d364c25c2932b35d80c5d3b3f5bfd659f081e4f38e3b9c3775
        A/clauses/window-03/meta.json: a4857704360ce86b7ecd5f2c45561a60ba46658a67bac5eca11ef43152674afc
        A/clauses/window-04/raw.json: 65960f9bce3e82dab6b73c67f7f194e3a8192216cdedefa4ba6a1586ebc4dc40
        A/clauses/window-04/prompt.txt: 475d42e2f635da50cdb4a85002ae90b1c813eb612d7e1cfb87b23b26c7053ede
        A/clauses/window-04/meta.json: 78b1c406bd4627d9b38926307b680bb5de65d2d4a12d0cbe1c73db0e9bba6800
        A/clauses/window-05/raw.json: d8aeb866d5d9df0c802158e6150cf3b3ee79a005f0bd089858ed9e23426ace7b
        A/clauses/window-05/prompt.txt: b879ac032e946172ea6c037d0bb3e9bd09b9902091add59eda3031835ff4f6ed
        A/clauses/window-05/meta.json: 0e4f1569490de0d0ee3321d461f6a92b56e10d4c8a2041c5b87e00fc4bdaa830
        A/clauses/window-02/raw.json: 3ed48b8b5dbb55b6846052d4aa78432434c993e3b658f6fee420c040231fb48a
        A/clauses/window-02/prompt.txt: 5c6d5410a2923d2984dff234912dad1fd0633a577cb544fe20c1f9cff4f8ccf1
        A/clauses/window-02/meta.json: a7fa88f935ad6f9ab47ce316ef6936eceec39f2857ad5904655d1e1898dab59e
        A/clauses/window-09/raw.json: dd34666d930cdc1b391913fc55f69fdf64a455d65b41c5af9375755bb7184ce7
        A/clauses/window-09/prompt.txt: 5d9e91d0ecec5043b736d3f4e2361498823d1faabe4c10e809f280c78bc92885
        A/clauses/window-09/meta.json: 034858f5cab25fa106ae1dc8b4f8b0af2fb45e1c0ec87f8ef525703c1d5a958e
        A/clauses/window-07/raw.json: 6977678dbce5f7f13a7008f6c684b48caab4fa4cb2c3b0128078dc6042889b31
        A/clauses/window-07/prompt.txt: d987069d0124a9f272d39c21a9f486eec5050a093f67cb7f84800fdf17c21cec
        A/clauses/window-07/meta.json: 9ca4e143ac2eb463b514c76d018260f319afbc795001407e8bcbb3f8c854472f
        A/clauses/window-01/raw.json: 7dcaec5ffc1b49420cb115263ef34442734442771169e14f5ac41fc0c5fc4d44
        A/clauses/window-01/prompt.txt: 186a322efa4e48088ea0f90b44997b40c03211bcf6facc8a905e1752bdd82dad
        A/clauses/window-01/meta.json: 0fac6f3a3f91a6c9cb63e1bf5c26383a4f37d1b103e6cad4201f163fae1877a7
        A/clauses/window-06/raw.json: 3e23d05f0c37b088df32d29c3c95f1472ccacd8a9bfda2c9935512c2a6dd8be0
        A/clauses/window-06/prompt.txt: 65ec4038082886706787e08ad3bd7ae3a3170589512e1b3cb0cb4cb8e6c71583
        A/clauses/window-06/meta.json: 81a9da6da76c25ec65b3490433193b649d637460ebb96f10f56047b4e93d3e6d
        A/clauses/window-08/raw.json: 564d724e8e961b64d9bdbc9b345b30dd1cfc2fb167bf2933c8f7ecfe730d8c20
        A/clauses/window-08/prompt.txt: 71c33d1d041d6e52586c9778353533001b01cc9b6ced4e679a959831c8907de6
        A/clauses/window-08/meta.json: 6bcf634b7b56ee6a73a5534cd01852106fd0b9b8c0a37b7f65e0dc0ef1108640
        A/tables/TABLE-1-page-5-1/raw.json: 1a1adf92bd3a82ed7f543994d8283148e1f5d5ce7b2fd1766a9b11a599bd0e04
        A/tables/TABLE-1-page-5-1/prompt.txt: 974fe91b48f1d53fab2a04d94ff5ca9e396fc20a934621bf0df6c33fca3f732f
        A/tables/TABLE-1-page-5-1/meta.json: 1b2b79e2b883736d3b2a64d55bf52046997e00a8adc7e2e5cc0a5cb90b6889e9
        A/tables/TABLE-2-page-6-2/raw.json: 8f044435b6cbfe355d6369576f404e11b9e5dfd244c706bd73b1dad4ebee37e8
        A/tables/TABLE-2-page-6-2/prompt.txt: cf3a36b09c9a165505bd232b2c43b00e3efb5f5b13ddc93be14f06c6c2241764
        A/tables/TABLE-2-page-6-2/meta.json: 7745029085044529301fa30172b4be12a63165c0a7b5a2fd9bdfec3a76ee8ff8
        A/tables/TABLE-5-page-21-5/raw.json: 4d20e59af81f13474e58fa3ae7507d5901291f35a225f87e2054d3f2995b264c
        A/tables/TABLE-5-page-21-5/prompt.txt: cd03419f16bc6967d0fc4fb80a624c5e16d98863cc9a7fa898a97b28932f6026
        A/tables/TABLE-5-page-21-5/meta.json: ab1fe25da491a1f248f8e207677786784cdeb7b9c4adf3a911cdeb5fde175611
        A/tables/TABLE-3-page-7-3/raw.json: a1cd360d4ad35302a4ceb09e0c1a5b3d2761b6673612a4f4f2f9c3d5a8261226
        A/tables/TABLE-3-page-7-3/prompt.txt: 14337a5192f9e244a51fcfb3d5be85cb4e3bc7351292579f91dc0c859324ea53
        A/tables/TABLE-3-page-7-3/meta.json: 6f904925482dbebe91760794b5e898da85dc40d421b56ac3f5a66d4120b10625
        A/tables/TABLE-6-page-21-6/raw.json: 94d06bdf8554914b3601b8e306d02e073172b5a9930b6aa5ba53570a79a0af83
        A/tables/TABLE-6-page-21-6/prompt.txt: cfe19ceb2c2fb2c9c6161efa608c7553251f45c85359ff19dc39e193de5395e5
        A/tables/TABLE-6-page-21-6/meta.json: 1bb57c24351da3a1031d843ef683c4d8ff38840011db573ae8b03bd5e64b2316
        A/tables/TABLE-4-page-21-4/raw.json: abd95bdd7f2826c5d0221023da70054a33d7707f825aacb0e6d8beed628fd6aa
        A/tables/TABLE-4-page-21-4/prompt.txt: 8d070fd0c9cda065e3b7f4ff38a8a51f49563d591d857c6d6118a0e6e9636213
        A/tables/TABLE-4-page-21-4/meta.json: 1e0a1acbfd2262948fcbf7a4774b5caca57ae0cd6c9f4c113e524be90a2d8f73
        B/passages.json: 639db63dbcaf8bcdbd68ee48c694c289a8c978d2328bbccb22ea41932ce76156
        B/raw.json: 97a691804bb34374d6f5292735e92cd9cb37f37d23fc46fdbfa53a6f0115d3a4
        B/source-units.json: 064a3c7c45bf5b3be81b410ccd9aa4bc13bb38cfc10eeee0a2cf10977e51228d
        B/full-source-units.json: 7b76426dc0677ba643bc715e3444af872bace2d60f2228b53ebd0e70734f7b08
        B/meta.json: f08ab7962b20a5bd4470b16fb23c47da5b95d0fdcd8741b6f6c69d4f3e614aa1
        B/table-images/TABLE-6-page-21-3.png: 8ce09228d143c00104a6ebef90ef4a1c02ab90616283cfe600c28b6394182d62
        B/table-images/TABLE-1-page-5-1.png: 7d2b9ea7c6fd2b6066c0a7e0de957c0810870f06cefe1dee29d445a573d21522
        B/table-images/TABLE-5-page-21-2.png: 8ce09228d143c00104a6ebef90ef4a1c02ab90616283cfe600c28b6394182d62
        B/table-images/page-6.png: 639255ee453b679d9644d36e12ad9a960b3f28c1b909c6d0e8ae80003f6d087b
        B/table-images/page-7.png: 659b1788fe5c1fe23df13bc41960a4ebf9aec190688199c9a11052ce5a52e8c8
        B/table-images/page-5.png: 5559cfe2f49d999acec817dc58c06473edfcefc89b29ce7e869be5df4a340ef7
        B/table-images/TABLE-2-page-6-1.png: b9f35c4708d287e691c0f17f300f95f5bab69e2760118580ae758bee48f5f2aa
        B/table-images/manifest.json: 5a1b912717283a86bbc0f7ecef00d244e610230624c295465d878bc84446c65b
        B/table-images/page-21.png: be82e93938da5a354fd334ab3783b99bbe10f207ff0c4c89b95c1fbf0039dcfc
        B/table-images/TABLE-4-page-21-1.png: 8ce09228d143c00104a6ebef90ef4a1c02ab90616283cfe600c28b6394182d62
        B/table-images/TABLE-3-page-7-1.png: b1ff88d49263d317552ab712ee964b2323d9d6c1c4be5df3695b110d752c3bce
        B/clauses/window-03/raw.json: 994a0721f9138f201df113266bdefd188e826fc569acb658138e9e3e307da9cd
        B/clauses/window-03/prompt.txt: 2dc99494486f29d364c25c2932b35d80c5d3b3f5bfd659f081e4f38e3b9c3775
        B/clauses/window-03/meta.json: fcd3c43cd0e2eba0633d91f4e9e3bf4d021d623a27e3d18ded009bb674668ac7
        B/clauses/window-04/raw.json: c6ef9ad0459d87b9c72f33780f910a78ba7d590b3c29a203468f124b6140925f
        B/clauses/window-04/prompt.txt: 475d42e2f635da50cdb4a85002ae90b1c813eb612d7e1cfb87b23b26c7053ede
        B/clauses/window-04/meta.json: 3b638e5cd113ec8362f944f30f898295ad8663cc1bbe10fc584e72d511fe2ab3
        B/clauses/window-05/raw.json: a213853f7f3ab1c0989ed91718b8aa5c245a22db308e0e7ef5b3cc7039b74a4d
        B/clauses/window-05/prompt.txt: b879ac032e946172ea6c037d0bb3e9bd09b9902091add59eda3031835ff4f6ed
        B/clauses/window-05/meta.json: 12ea28bf8ea2980c2dd9807f3c0b074ef2fb5b76fb2fcdda2055c3bf5074b0b1
        B/clauses/window-02/raw.json: a3e713903b0fc081a9ac4d4030a10e6f89bd140bd686e721c52510cb201fae74
        B/clauses/window-02/prompt.txt: 5c6d5410a2923d2984dff234912dad1fd0633a577cb544fe20c1f9cff4f8ccf1
        B/clauses/window-02/meta.json: c136b6e45611aa5a2dcc262d6dfb172f2e3d3966fcf082f7c25e3b1813dc70a8
        B/clauses/window-09/raw.json: 5e9b17f7d87406e58e296daf87eb5c93cdf58b2fd9d965545714bd7eb2caf4a8
        B/clauses/window-09/prompt.txt: 5d9e91d0ecec5043b736d3f4e2361498823d1faabe4c10e809f280c78bc92885
        B/clauses/window-09/meta.json: 710d702c6d11f1d0d13293fa090d0700be6979e758a0097cc5fc20c846c996a6
        B/clauses/window-07/raw.json: 00f06f3a71e4a88e31b039a91be2c1b187a72518ce0fb2543c0f23d727301d0c
        B/clauses/window-07/prompt.txt: d987069d0124a9f272d39c21a9f486eec5050a093f67cb7f84800fdf17c21cec
        B/clauses/window-07/meta.json: 17148c3707d3a914b12d49778aebdc65c074dc9fd9e2b162acc168d37a6b4621
        B/clauses/window-01/raw.json: 2d793cb6ddda466d8d2ed97b8c82f642272c3fdba638bbcb51c10d338cfd67de
        B/clauses/window-01/prompt.txt: 186a322efa4e48088ea0f90b44997b40c03211bcf6facc8a905e1752bdd82dad
        B/clauses/window-01/meta.json: b8dfb2c577887c119bd5050dc5db762c43c9571d563239fe1db5ba879f2cbae5
        B/clauses/window-06/raw.json: efef346b67ce159cc9dba8de54a1c138752abf52ef267d6db108d8a261707b22
        B/clauses/window-06/prompt.txt: 65ec4038082886706787e08ad3bd7ae3a3170589512e1b3cb0cb4cb8e6c71583
        B/clauses/window-06/meta.json: a178b7829bbf2659d16941a60d4eebee0787374adc858c356ef4dfca206ecbc3
        B/clauses/window-08/raw.json: 3cc5d900df5c49ff0049889502fc4e5beac942d28307f6709c9c3ce689fa83dd
        B/clauses/window-08/prompt.txt: 71c33d1d041d6e52586c9778353533001b01cc9b6ced4e679a959831c8907de6
        B/clauses/window-08/meta.json: ab0f8622a668e32ab18c79b7e900ddd2bf5b1ae6510f937f23c958e9c148e737
        B/tables/TABLE-1-page-5-1/raw.json: 3ac6b4e222aaa9d8689d1d1cf2fcaa73d2854b08526258b54cc8517e4f798600
        B/tables/TABLE-1-page-5-1/prompt.txt: 974fe91b48f1d53fab2a04d94ff5ca9e396fc20a934621bf0df6c33fca3f732f
        B/tables/TABLE-1-page-5-1/meta.json: 4fc5d8bc7c9704343e8b7fd36a2f06809acb812a6d1a91d6e5f8fcf54d2772a4
        B/tables/TABLE-2-page-6-2/raw.json: eab4439efd9ac294dea38a8a6ce26deb4a5f919509b6e56af3c55f64c40e83be
        B/tables/TABLE-2-page-6-2/prompt.txt: cf3a36b09c9a165505bd232b2c43b00e3efb5f5b13ddc93be14f06c6c2241764
        B/tables/TABLE-2-page-6-2/meta.json: 5fed9a4d2f8adca6a459be16de23d342e53b820fc73274842f7a9ca3c970150c
        B/tables/TABLE-5-page-21-5/raw.json: 4d20e59af81f13474e58fa3ae7507d5901291f35a225f87e2054d3f2995b264c
        B/tables/TABLE-5-page-21-5/prompt.txt: cd03419f16bc6967d0fc4fb80a624c5e16d98863cc9a7fa898a97b28932f6026
        B/tables/TABLE-5-page-21-5/meta.json: 64ee2b4947674b447894e6d50d54fae77b4ed4832dd87a4c5784340bc7174d7a
        B/tables/TABLE-3-page-7-3/raw.json: 9e5e648b09bee2bc2626c84f3ab58b510eee22b88c4fc0f414214d45426bf236
        B/tables/TABLE-3-page-7-3/prompt.txt: 14337a5192f9e244a51fcfb3d5be85cb4e3bc7351292579f91dc0c859324ea53
        B/tables/TABLE-3-page-7-3/meta.json: 6804690ec616a483ba9bb457e2de8ac95017e476dab2e98f386cfda52a4e06a9
        B/tables/TABLE-6-page-21-6/raw.json: 5a9aa4b307bf91b50440e14487cb4f9a5e5d97da81ac35db1c137cd3a4b6fc54
        B/tables/TABLE-6-page-21-6/prompt.txt: cfe19ceb2c2fb2c9c6161efa608c7553251f45c85359ff19dc39e193de5395e5
        B/tables/TABLE-6-page-21-6/meta.json: bbdd42dad6f22827f2847bbd405dcefd80b4f6eb9ce6d8813f2b42267105fba5
        B/tables/TABLE-4-page-21-4/raw.json: 5982a53380528af61595dcbdb985e77ece803182ed52d52aa6f3137740c77a82
        B/tables/TABLE-4-page-21-4/prompt.txt: 8d070fd0c9cda065e3b7f4ff38a8a51f49563d591d857c6d6118a0e6e9636213
        B/tables/TABLE-4-page-21-4/meta.json: 6ebddd9ca47f3e6cba12a14e825866e4088bc030e50c30411f5f435c4f32f914
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
      pdf_sha256: b2c3f70ccce9e12b75df84d02ec4f2080528b4ffccb3686a0465427365c25ff8
      source_review: _compare/relationships-2026-11-16/review-current/Leonard2008
      source_status_sha256: d2dea00e3bb2a3398a94bfa63945d0c01d0d747b53d267782c2ce9c33eafd058
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R007
    exposure:
      text: pre-treatment semantic deficit (PALPA 52 difference)
    outcome:
      text: response to PCA treatment
    analysis_label: Pre-treatment semantic deficit and treatment response
    relation: association
    evidence_ids:
    - P14-S1-C4
    - P22-S1-C6
    - P22-S1-C8
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
      pdf_sha256: b2c3f70ccce9e12b75df84d02ec4f2080528b4ffccb3686a0465427365c25ff8
      source_review: _compare/relationships-2026-11-16/review-current/Leonard2008
      source_status_sha256: d2dea00e3bb2a3398a94bfa63945d0c01d0d747b53d267782c2ce9c33eafd058
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P4-S2-C5
      - Result passage disposed without unit P7-S1-C3
      - Unresolved source passage P8-S2-C9
      - Accounting without a linked unit P10-S1-C10
      - Accounting without a linked unit P10-S1-C13
      - Accounting without a linked unit P10-S2-C3
      - Accounting without a linked unit P10-S2-C4
      - Accounting without a linked unit P10-S2-C5
      - Accounting without a linked unit P10-S2-C6
      - Accounting without a linked unit P10-S2-C7
      - Unaccounted source passage P10-S2-C5
      - Unaccounted source passage P10-S2-C4
      - Unaccounted source passage P10-S2-C3
      - Unaccounted source passage P10-S2-C7
      - Unaccounted source passage P10-S2-C6
      - Unaccounted source passage P10-S1-C10
      - Unaccounted source passage P10-S1-C13
      - Result passage disposed without unit P11-S1-C1
      - Result passage disposed without unit P11-S1-C10
      - Result passage disposed without unit P11-S1-C11
      - Result passage disposed without unit P11-S1-C2
      - Result passage disposed without unit P11-S1-C8
      - Result passage disposed without unit P11-S1-C9
      - Accounting without a linked unit P12-S1-C10
      - Accounting without a linked unit P12-S1-C6
      - Result passage disposed without unit P12-S1-C7
      - Unaccounted source passage P12-S1-C6
      - Unaccounted source passage P12-S1-C10
      - Accounting without a linked unit P13-S1-C3
      - Result passage disposed without unit P13-S1-C8
      - Result passage disposed without unit P13-S1-C9
      - Accounting without a linked unit P14-S1-C1
      - Accounting without a linked unit P14-S1-C2
      - Accounting without a linked unit P14-S1-C3
      - Unaccounted source passage P14-S1-C1
      - Unaccounted source passage P14-S1-C3
      - Unaccounted source passage P14-S1-C2
      - Unaccounted source passage P13-S1-C3
      - Result passage disposed without unit P14-S1-C8
      - Result passage disposed without unit P20-S1-C7
      - Result passage disposed without unit P22-S1-C9
      - Result passage disposed without unit P22-S2-C4
      - Result passage disposed without unit P22-S2-C5
      unattached_null_or_qualifier_ids:
      - P8-S1-C1
      - P10-S2-C3
      - P10-S2-C7
      - P11-S1-C2
      - P11-S1-C7
      - P11-S1-C8
      - P11-S1-C11
      - P13-S1-C2
      - P14-S1-C8
      - P22-S2-C5
      suppressed_nonrepresented_units: 21
      default_disposition_count_requires_completeness_check: 197
      unselected_timing_passages:
      - P4-S2-C1
      - P4-S2-C4
      - P7-S1-C9
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P14-S1-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P14-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P20-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P21-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P22-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P10-S1-C3
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P10-S1-C4
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P10-S1-C7
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P10-S1-C10
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: tested_personal_effects
        source_id: P13-S1-C4
        reason: No current-result classification; a covariate description is not an
          individual test
      empty_frame_slots_require_confirmation:
      - imaging_provenance
      - imaging_timing
      - validation
      - analysis_restrictions
      - personal_factors
      - adjustment_roles
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-5-1
      - TABLE-2-page-6-2
      - TABLE-3-page-7-3
      - TABLE-4-page-21-4
      - TABLE-5-page-21-5
      - TABLE-6-page-21-6
      unlinked_tables:
      - TABLE-1-page-5-1
      - TABLE-3-page-7-3
      - TABLE-4-page-21-4
      - TABLE-5-page-21-5
      - TABLE-6-page-21-6
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P8-S2
        - P9-S1
        - P10-S2
        - P11-S1
        - P11-S2
        - P12-S1
        - P13-S1
        - P14-S1
        - P15-S1
        - P16-S1
        - P17-S1
        - P18-S1
        - P19-S1
        - P20-S1
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: b2c3f70ccce9e12b75df84d02ec4f2080528b4ffccb3686a0465427365c25ff8
      source_review: _compare/relationships-2026-11-16/review-current/Leonard2008
      source_status_sha256: d2dea00e3bb2a3398a94bfa63945d0c01d0d747b53d267782c2ce9c33eafd058
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P2-S1-C6
      disposition: represented
      result_indexes:
      - 0
      reason: States 7 of 10 individuals demonstrated notable treatment effects.
    - source_id: P2-S1-C7
      disposition: represented
      result_indexes:
      - 1
      - 2
      reason: Reports maintenance of gains and generalisation to untreated items.
    - source_id: P4-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes aphasia classification of participants.
    - source_id: P4-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes visual perceptual abilities of participants.
    - source_id: P4-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes hearing screening results.
    - source_id: P5-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports pre-treatment Pyramids and Palm Trees Test scores.
    - source_id: P5-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Categorizes participants by semantic representation integrity.
    - source_id: P5-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports pre-treatment Spoken Word-Picture Matching scores.
    - source_id: P5-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports pre-treatment Written Word-Picture Matching scores.
    - source_id: P6-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports pre-treatment lexical semantic processing scores.
    - source_id: P6-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Interprets pre-treatment semantic impairment.
    - source_id: P6-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports pre-treatment BNT and PNT scores.
    - source_id: P6-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports pre-treatment word repetition and reading scores.
    - source_id: P6-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Compares pre-treatment repetition/reading to naming.
    - source_id: P6-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes pre-treatment naming error types.
    - source_id: P6-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes pre-treatment naming error types for specific patients.
    - source_id: P6-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes pre-treatment naming error types for specific patients.
    - source_id: P7-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Interprets pre-treatment error patterns.
    - source_id: P7-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Summarizes pre-treatment deficit levels.
    - source_id: P7-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Interprets pre-treatment deficit for P9.
    - source_id: P7-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Interprets pre-treatment deficit for P9.
    - source_id: P7-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Refers to Table 3 (pre-treatment error types).
    - source_id: P8-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes treatment list construction for P1.
    - source_id: P10-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports inter-rater reliability for scoring.
    - source_id: P10-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports inter-rater reliability for therapy administration.
    - source_id: P10-S1-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes baseline stability.
    - source_id: P10-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes baseline variability for P6 and P8.
    - source_id: P10-S2-C4
      disposition: represented
      result_indexes:
      - 0
      reason: Identifies six participants with robust treatment effects.
    - source_id: P10-S2-C5
      disposition: represented
      result_indexes:
      - 0
      reason: Identifies treatment effects for P6 on Lists 1 and 2.
    - source_id: P10-S2-C6
      disposition: represented
      result_indexes:
      - 0
      reason: Notes loss of experimental control for P6 List 3.
    - source_id: P10-S2-C7
      disposition: represented
      result_indexes:
      - 0
      reason: Identifies participants (7, 9, 10) who did not demonstrate treatment
        effect.
    - source_id: P11-S1-C1
      disposition: represented
      result_indexes:
      - 0
      reason: Confirms lack of treatment effect for P7, P9, P10.
    - source_id: P11-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Explains reason for treatment termination (below 40% threshold).
    - source_id: P11-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes statistical method (2 SD band) for treatment effect.
    - source_id: P11-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Explains why List 1 was excluded from 2 SD analysis for most.
    - source_id: P11-S1-C8
      disposition: represented
      result_indexes:
      - 0
      reason: Statistically supports improvement for Lists 2 and 3 for most participants.
    - source_id: P11-S1-C9
      disposition: represented
      result_indexes:
      - 0
      reason: Notes P6's high 2 SD value for List 3.
    - source_id: P11-S1-C10
      disposition: represented
      result_indexes:
      - 0
      reason: Statistically supports improvement for P6 and P8 List 1.
    - source_id: P11-S1-C11
      disposition: represented
      result_indexes:
      - 1
      reason: Statistically supports maintenance of effects at 4-week follow-up.
    - source_id: P11-S1-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Explains inability to calculate effect size for some List 1s.
    - source_id: P12-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Continues explanation of baseline variability.
    - source_id: P12-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports large averaged effect sizes per Busk and Serlin criteria.
    - source_id: P12-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports effect sizes range from large to small per Beeson and Robey.
    - source_id: P12-S1-C10
      disposition: represented
      result_indexes:
      - 2
      reason: Reports significant PNT difference for P2, P3, P4.
    - source_id: P13-S1-C1
      disposition: represented
      result_indexes:
      - 2
      reason: Reports significant PNT change for P10.
    - source_id: P13-S1-C2
      disposition: represented
      result_indexes:
      - 2
      reason: Qualifies P10's PNT change as difficult to interpret due to low scores.
    - source_id: P13-S1-C3
      disposition: represented
      result_indexes:
      - 2
      reason: Reports significant group analysis of PNT scores for those with treatment
        effect.
    - source_id: P14-S1-C1
      disposition: represented
      result_indexes:
      - 3
      - 4
      reason: Reports significant correlations between treatment response and BNT
        and Oral Reading.
    - source_id: P14-S1-C2
      disposition: represented
      result_indexes:
      - 3
      - 4
      reason: Interprets BNT and Oral Reading correlations.
    - source_id: P14-S1-C3
      disposition: represented
      result_indexes:
      - 5
      reason: Reports positive trend between treatment performance and Word Repetition.
    - source_id: P14-S1-C4
      disposition: represented
      result_indexes:
      - 6
      reason: Reports negative trend between treatment performance and semantic deficit.
    - source_id: P15-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes changes in independent component generation across lists.
    - source_id: P15-S1-C2
      disposition: represented
      result_indexes:
      - 7
      reason: Associates independent component generation (>=50%) with treatment improvement.
    - source_id: P15-S1-C5
      disposition: represented
      result_indexes:
      - 0
      reason: Restates effectiveness of the approach.
    - source_id: P16-S1-C2
      disposition: represented
      result_indexes:
      - 0
      reason: Restates 7 of 10 participants showed improvement.
    - source_id: P16-S1-C3
      disposition: represented
      result_indexes:
      - 1
      reason: Restates maintenance of effects at 1-month follow-up.
    - source_id: P17-S1-C7
      disposition: represented
      result_indexes:
      - 7
      reason: Restates association between independent generation and treatment effect.
    - source_id: P18-S1-C1
      disposition: represented
      result_indexes:
      - 7
      reason: Restates association between independent generation and treatment effect.
    - source_id: P18-S1-C4
      disposition: represented
      result_indexes:
      - 2
      reason: Restates generalisation to untreated items for P2, P3, P4.
    - source_id: P20-S1-C6
      disposition: represented
      result_indexes:
      - 3
      reason: Restates significant relation between BNT and treatment response.
    - source_id: P20-S1-C7
      disposition: represented
      result_indexes:
      - 3
      reason: Notes non-improvers had most severe naming impairments.
    - source_id: P21-S1-C1
      disposition: represented
      result_indexes:
      - 3
      reason: Restates non-improvers had most severe naming impairments.
    - source_id: P21-S1-C2
      disposition: represented
      result_indexes:
      - 4
      reason: Restates positive relation between oral reading and treatment response.
    - source_id: P22-S1-C6
      disposition: represented
      result_indexes:
      - 5
      - 6
      reason: Restates trends for word repetition and lexical semantic deficit.
    - source_id: P22-S1-C7
      disposition: represented
      result_indexes:
      - 5
      reason: Interprets word repetition trend.
    - source_id: P22-S1-C8
      disposition: represented
      result_indexes:
      - 6
      reason: Interprets lexical semantic deficit trend.
    - source_id: P22-S2-C4
      disposition: represented
      result_indexes:
      - 8
      reason: States aphasia type was not a major factor in success.
    - source_id: P22-S2-C5
      disposition: represented
      result_indexes:
      - 8
      reason: Notes both fluent and nonfluent patients were among non-successful group.
    - source_id: P22-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion restating effectiveness.
    - source_id: P22-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion about strengthening lexical system.
    - source_id: P22-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion about future comparative studies.
    unresolved_coverage:
    - source_id: P15-S1-C5
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P22-S1-C7
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P22-S1-C8
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P13-S1-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S1-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P14-S1-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P14-S1-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P18-S1-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P22-S1-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P4-S2-C5
    - P4-S2-C7
    - P4-S2-C8
    - P5-S1-C7
    - P5-S1-C9
    - P5-S1-C11
    - P5-S1-C12
    - P6-S1-C1
    - P6-S1-C2
    - P6-S1-C3
    - P6-S1-C4
    - P6-S1-C5
    - P6-S1-C8
    - P6-S1-C9
    - P6-S1-C10
    - P7-S1-C2
    - P7-S1-C3
    - P7-S1-C4
    - P7-S1-C5
    - P7-S2-C4
    - P8-S1-C1
    - P10-S1-C5
    - P10-S1-C10
    - P10-S1-C13
    - P10-S2-C3
    - P10-S2-C6
    - P10-S2-C7
    - P11-S1-C1
    - P11-S1-C2
    - P11-S1-C6
    - P11-S1-C7
    - P11-S1-C8
    - P11-S1-C9
    - P11-S1-C10
    - P11-S1-C13
    - P12-S1-C1
    - P12-S1-C6
    - P12-S1-C7
    - P13-S1-C2
    - P13-S1-C8
    - P13-S1-C9
    - P14-S1-C5
    - P14-S1-C8
    - P15-S1-C1
    - P16-S1-C2
    - P18-S1-C5
    - P20-S1-C7
    - P22-S1-C9
    - P22-S2-C7
    - P22-S2-C8
    - P22-S2-C9
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-5-1
    - TABLE-2-page-6-2
    - TABLE-3-page-7-3
    - TABLE-4-page-21-4
    - TABLE-5-page-21-5
    - TABLE-6-page-21-6
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P2-S1-C5
      recruited_sample:
      - P1-S2-C4
      eligibility:
      - P4-S2-C4
      - P4-S2-C5
      - P4-S2-C6
      - P4-S2-C7
      - P4-S2-C8
      - P5-S1-C3
      imaging_provenance: []
      imaging_timing: []
      outcome_timing:
      - P2-S1-C3
      - P11-S1-C11
      - P16-S1-C3
      outcome_definition:
      - P2-S1-C4
      - P10-S1-C11
      - P12-S1-C8
      validation: []
      analysis_restrictions: []
      dependent_variable_statement:
      - P10-S1-C12
      - P13-S1-C5
      limitations:
      - P14-S1-C5
      personal_factors: []
      tested_personal_effects:
      - P14-S1-C2
      - P14-S1-C3
      - P14-S1-C4
      - P20-S1-C6
      - P21-S1-C2
      - P22-S1-C6
      adjustment_roles: []
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P4-S2-C1
      - P4-S2-C2
      - P4-S2-C4
      - P4-S2-C5
      - P5-S2-C5
    outcome_type: both_reported
    imaging_vs_outcome: precedes_outcome
    validation_type: internal_cross_validation
    held_selections:
    - slot: dependent_variable_statement
      source_id: P14-S1-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P14-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P20-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P21-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P22-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P10-S1-C3
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P10-S1-C4
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P10-S1-C7
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P10-S1-C10
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: tested_personal_effects
      source_id: P13-S1-C4
      reason: No current-result classification; a covariate description is not an
        individual test
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
      pdf_sha256: b2c3f70ccce9e12b75df84d02ec4f2080528b4ffccb3686a0465427365c25ff8
      review_sha256: 79af570d069c68d2d60ab5fc77b8bedf41538ddace3ab6263d5c88d98be279aa
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
      - P14-S1-C4
      - P22-S1-C6
      - P22-S1-C8
      source_result: A trend towards a negative relationship (p = .065, one-tailed)
        was found between treatment performance and a semantic deficit, measured as
        the difference in performance on the 'a' (with semantic distractors) and 'b'
        (without semantic distractors) versions of the Spoken Word–Written Word subtest
        of the PALPA (PALPA 52). This indicates that greater semantic deficit was
        associated with poorer response to treatment.
      result_status: detected_only_at_relaxed_threshold
      patient_measurement: non_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis corresponds to the correlational analysis
            described in P13-S1-C4 and P14-S1-C4, examining the relationship between
            pre-treatment test scores and response to treatment. The specific measure
            identified is the PALPA 52 difference, matching the source description.
          source_ids:
          - P13-S1-C4
          - P14-S1-C4
        direction:
          answer: fits
          reason: The source explicitly states a 'negative relationship' (P14-S1-C4)
            and P22-S1-C6 confirms a 'negative trend between a lexical semantic deficit
            and response to treatment'. The proposed draft correctly identifies this
            as a negative association (greater deficit -> poorer response).
          source_ids:
          - P14-S1-C4
          - P22-S1-C6
        construct:
          answer: fits
          reason: The exposure is correctly identified as the semantic deficit measured
            by the difference between PALPA 52 versions 'a' and 'b' (P14-S1-C4). The
            outcome is response to PCA treatment, defined as mean performance on probes
            during treatment (P13-S1-C5). The measurement is behavioral (non-imaging),
            not diffusion or template overlap.
          source_ids:
          - P14-S1-C4
          - P13-S1-C5
        qualifications:
          answer: fits
          reason: The draft correctly includes the qualification that this is a 'trend'
            (p = .065, one-tailed) rather than a significant finding at conventional
            thresholds, and notes the limited power due to small sample size (P14-S1-C5).
            It does not overstate the finding as a definitive significant association.
          source_ids:
          - P14-S1-C4
          - P14-S1-C5
        missing_material_caveat:
          answer: fits
          reason: The draft includes the key caveats regarding the trend status and
            sample size limitations. No material caveats from the source passages
            regarding this specific analysis appear to be omitted.
          source_ids:
          - P14-S1-C5
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
      original: 10
      action: not_transcribed
      reason: Not supported by selected quotations
    analysis_identity:
      id: R007
      exposure:
        text: pre-treatment semantic deficit (PALPA 52 difference)
      outcome:
        text: response to PCA treatment
      analysis_label: Pre-treatment semantic deficit and treatment response
      relation: association
      evidence_ids:
      - P14-S1-C4
      - P22-S1-C6
      - P22-S1-C8
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
        pdf_sha256: b2c3f70ccce9e12b75df84d02ec4f2080528b4ffccb3686a0465427365c25ff8
        source_review: _compare/relationships-2026-11-16/review-current/Leonard2008
        source_status_sha256: d2dea00e3bb2a3398a94bfa63945d0c01d0d747b53d267782c2ce9c33eafd058
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P4-S2-C4:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: b2c3f70ccce9e12b75df84d02ec4f2080528b4ffccb3686a0465427365c25ff8
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 3727ea63a17e8e2956d7f596acae361427ef86cc2f0c8d91dbd9aa1b4d8102d6
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P4-S2-C4
          page: 4
          text_layer_sha256: 3727ea63a17e8e2956d7f596acae361427ef86cc2f0c8d91dbd9aa1b4d8102d6
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'All participants were right-handed, English-speaking individuals
          who had

          experienced a single left-hemisphere cerebrovascular accident and were at
          least 1 year

          post-onset at the time of enrolment.'
        anchor_text: 'All participants were right-handed, English-speaking individuals
          who had

          experienced a single left-hemisphere cerebrovascular accident and were at
          least 1 year

          post-onset at the time of enrolment.'
        excluded_fragments: []
        image_sha256: 1afce58c11aa3b598f57af1c849ee0dbb2bcbfd32b6624b108f68331ab60bfcf
        transcription: . All participants were right-handed, English-speaking individuals
          who had experienced a single left-hemisphere cerebrovascular accident and
          were at least 1 year post-onset at the time of enrolment
      P4-S2-C6:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: b2c3f70ccce9e12b75df84d02ec4f2080528b4ffccb3686a0465427365c25ff8
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 3e6fa9e2f3a96ca518fe53383942b499cb98e9983a4d29d577e9159b89769708
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P4-S2-C6
          page: 4
          text_layer_sha256: 3e6fa9e2f3a96ca518fe53383942b499cb98e9983a4d29d577e9159b89769708
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'All participants had a

          naming impairment defined by less than 75% accuracy on the Boston Naming
          Test

          (BNT) (Goodglass et al., 2001).'
        anchor_text: 'All participants had a

          naming impairment defined by less than 75% accuracy on the Boston Naming
          Test

          (BNT) (Goodglass et al., 2001).'
        excluded_fragments: []
        image_sha256: 64712b8765e64eb9db173dc43d97a54f031c60dcb3500aeabb2e616c98479a89
        transcription: '. All participants had a

          naming impairment defined by less than 75% accuracy on the Boston Naming
          Test

          (BNT) (Goodglass et al., 2001)'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 14
  quote: 'Finally, a trend towards a

    negative relationship (p 5 .065, one-tailed) between treatment performance and
    a

    semantic deficit (as measured by the difference in performance on the ‘‘a’’ (with

    semantic distractors) and ‘‘b’’ (without semantic distractors) versions of the
    Spoken

    Word – Written Word subtest (PALPA 52)), was found.'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-24'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
