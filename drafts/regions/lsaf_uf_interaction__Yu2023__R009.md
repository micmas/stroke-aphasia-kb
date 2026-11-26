---
id: lsaf_uf_interaction
name: left LSAF and UF interaction cluster
kind: network
findings:
- id: f1
  target: language_performance
  target_kind: impairment
  claim: No interaction effect of the integrity of the left LSAF and UF on language
    performance was found.
  direction: no_effect
  relationship: correlational
  method: DTI
  sample:
    n: not_reported
    population: patients with acute/subacute post-stroke aphasia
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
  - DTI tractography sensitivity to artifacts around the sinuses may affect UF measurement
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Interaction effect of the structural integrity (measured
    by mean fractional anisotropy and fiber number via DTI tractography) of the left
    long segment of the arcuate fasciculus (LSAF) and the left uncinate fasciculus
    (UF). Analysis performed via multiple linear regression; Adjusted for sex, age,
    educational level, time post stroke, and lesion volume. Additional metadata has
    not been transcribed; review the pending-field flags before approval.'
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
    - not_transcribed:sample.n
    - not_transcribed:sample.time_post_onset
    - proposed_concept:language_performance
  citation: '@Yu2023'
  source_passages:
  - section: Original source P1-S2-C5
    page: 1
    quote: 'In addition, no interaction effect of the integrity of the left LSAF and
      UF on language performance

      was found (p > 0.05).'
    supports: claim
  - section: Original source P9-S1-C2
    page: 9
    quote: 'Furthermore, the results showed

      no interaction effects of the integrity of the left LSAF and UF on language
      performance

      (p > 0.05).'
    supports: claim
  - section: Original source P4-S1-C3
    page: 4
    quote: 'Participants

      Thirty-sixparticipants(27males/9females, agerange: 25–78years, meanage: 53.31±
      12.37years;

      mean duration of education: 10.78 ± 3.48 years; mean time since stroke: 36.56
      ± 28.25 days) with

      acute/subacute PSA were recruited according to the following inclusion criteria:
      first-ever left hemi-

      spheric stroke (i.e., infarction or hemorrhage) with normal consciousness, time
      post-stroke less than 90

      days, age between 18–80 years, right-handedness and native Chinese speakers,
      the consistent presence

      of various types of aphasia (aphasia quotient value < 93.8), collaborating to
      complete a language

      faculties assessment and magnetic resonance imaging (MRI) scan.'
    supports: sample
  - section: Original source P5-S2-C8
    page: 5
    quote: 'In addition, multiple linear regression analysis was also

      implemented to investigate the associations between language performance and
      the integrity

      of the LSAF/UF.'
    supports: method
  - section: Original source P5-S2-C9
    page: 5
    quote: 'Demographic and stroke-related variables, including sex, age, educational

      level, time post of stroke, and lesion volume, were selected as confounding
      variables.'
    supports: confounders
  - section: Original source P14-S1-C4
    page: 14
    quote: 'Finally, the UF is more difﬁcult to measure successfully given

      the sensitivity of the diffusion sequence to artifacts around the sinuses [58],
      which can be

      observed in our patients with the heterogeneity of the UF reconstructed by DTI
      tractography.'
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-26'
relationship_review:
  paper: Yu2023
  proposal_id: R009
  review_status_sha256: 1c1b3a515a934314d7d338e0448263b1d5c52fa253f65f9ec95201d52516328c
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 6dbf400a356a1ad0078d9d36156ad9dbd70fbf223606aaa812f81fd7e2174cd8
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 6dbf400a356a1ad0078d9d36156ad9dbd70fbf223606aaa812f81fd7e2174cd8
        A/passages.json: 6d3239f83fcf3e28001cc9f3d9570f0f10fa1facd2c49886d453f1a80e78397b
        A/raw.json: 7cb11fabe757baabbadf9b4db2b6685d58e16f149b8f3baa1844ed6516a53b65
        A/source-units.json: 139a17398b9b267ca8cbe0d41e99de84c0a9e775f742831ea044df8e87e602d7
        A/full-source-units.json: db656de68eb0c1afe383f338042032ab34060e9ce6d8ceabde4dffb5e7747f0d
        A/meta.json: 5051aebce624398772f4f1cadf217b469ba7cf4139a50b360fda4a125059c6c9
        A/table-images/TABLE-3-page-9-1.png: c64ad1a61ed8efe3940199fda0e01ca0753947c81caa2227411c2a92e86cb832
        A/table-images/TABLE-1-page-7-1.png: d0a4219f169a3f8080c3905d2b0cb04f1c4ad5ac7f85d54d7f85d363218742a5
        A/table-images/TABLE-1-page-6-1.png: f1c6b4f2210a8eb4effc6e7d33ac9f2d473d0ab86e8776978797f3ddf0566019
        A/table-images/page-6.png: 9812b3a3bc7e58c277b582df1a78425245cd46880e1aaa99077845cb13e19482
        A/table-images/page-7.png: c7c136c02dccc07233932721f0b1aa1228124ba0f622da4172d8043c24b26a10
        A/table-images/page-9.png: 441d5512b60ecc15b326ea7a79c73da34a4dd62adff2d0e788f1490f6e9c89ea
        A/table-images/manifest.json: 1d0c0a1890e8237411f1494269394d635d205aebdad09e10af65cc38cf7631c7
        A/table-images/TABLE-2-page-7-3.png: d0a4219f169a3f8080c3905d2b0cb04f1c4ad5ac7f85d54d7f85d363218742a5
        A/table-images/TABLE-2-page-7-2.png: d0a4219f169a3f8080c3905d2b0cb04f1c4ad5ac7f85d54d7f85d363218742a5
        A/clauses/window-03/raw.json: b9b9255aa785bfba3ca8a3474ae98825f858f1e1b9af683f62411a4db07ce740
        A/clauses/window-03/prompt.txt: f33daee926ad324a12f75549c419d4222bfe9b767c07373892bb108f550ce206
        A/clauses/window-03/meta.json: 533ca4e9c69d9f1ef79a4e1538cc581d0cfaef402ef184132f61cc596aa84517
        A/clauses/window-04/raw.json: 3999d5e01cec0b132319c821e5303ae1b25890127db34d465ca4c63f5cf17301
        A/clauses/window-04/prompt.txt: 36f5ee11ae48d05af58c5d45c9b1a9bd97e58d20b8044a1ebae7f9d41d3f5493
        A/clauses/window-04/meta.json: 0017f213b3ee5084edb188f8d6ea9e76b3f9de6d2fdf9c8ac0cd3c923e364377
        A/clauses/window-05/raw.json: 61b44c124d34b66246109180a06ccfa52ac1c3abf000aa2dbe1d515601514686
        A/clauses/window-05/prompt.txt: 602f2fa95a8ecae0d8092dc4ba3371121f46a40299715fbb846062919bda783a
        A/clauses/window-05/meta.json: 00bd9afbfd3ce02e6d4d8d0d989ddc70bac3f5131571d1ccb406e9da1b7cc69a
        A/clauses/window-02/raw.json: a9448812a49c211a8af65dce92a9ae74f1781ea04aa8baf523d1bfd9557c2cc9
        A/clauses/window-02/prompt.txt: e6475859438eb0f35c3c128f9411a4e612c70ca45a611e78b36e2e1cdadf5030
        A/clauses/window-02/meta.json: 32395bc1d1d5cddeabee76df10fb6cc9979f151b567875a20eac83b1d5ea592e
        A/clauses/window-07/raw.json: 219c57a050ac77197fd1dba0678e65d93c8b29095ba04336433682168654f6b4
        A/clauses/window-07/prompt.txt: ceaf2bcff78e96bcb6994de2447938c6af8c9f9213702a9eb485e5c1113e2a6f
        A/clauses/window-07/meta.json: 6cd0be5484f6c2506d93930e96d758295c1bab2334011ffa7bd4d98839cf491f
        A/clauses/window-01/raw.json: c7f471bc9f9d989124590ddaa1422c84763d599086c466531479672545441d69
        A/clauses/window-01/prompt.txt: c7922d50c0d7b94dabc05a0312e379f4299752ee82addf775199f5b9fabcf9dd
        A/clauses/window-01/meta.json: b4cff83c7d35e99632d6a6fbd00a5f7810a9507f5579ddb55c1013860c85c3a0
        A/clauses/window-06/raw.json: 3cd97118955493ebf910ec0123bea044ed3ca42cbf4b5ea695a940bd1c89eb27
        A/clauses/window-06/prompt.txt: b1cf745ca1f0b1df13f4f5afebf89cc0c9162e944e290c071ef24574ff2aacd6
        A/clauses/window-06/meta.json: 65616d1243b48adc0e5497479407eaecfe5830771a610e374684cd37fb5f99b5
        A/tables/TABLE-1-page-7-2/raw.json: 4ec16e42dac73a9c33a0a5d1a04f2779e8d137580ad2a915325e9aa2e9533166
        A/tables/TABLE-1-page-7-2/prompt.txt: b1816512be90a1cdf7fedefd76e5dec7c4b39f7705d0cef3412de53aa0ff1683
        A/tables/TABLE-1-page-7-2/meta.json: 2da68968599a1d3fcbe33b718b76305dbd370223f34d5c71c5b8910e8d921e87
        A/tables/TABLE-1-page-6-1/raw.json: 396bdd986088e868146510bff4f388919cc5222cea1ae4a8f7bc3354a602c0c6
        A/tables/TABLE-1-page-6-1/prompt.txt: b3234e7f7475029ec969f662ab978d35b7013bbd5ccbdde1d715248cd1fa525e
        A/tables/TABLE-1-page-6-1/meta.json: eae4bf6955c3f49de79e47485144cc459c5edfe72f6eaac164d35fa4bd292632
        A/tables/TABLE-3-page-9-5/raw.json: 18095c0b258d0bce30fddea956f5e2da511d33e8d6e9f5fcd0761e8746fdfd6d
        A/tables/TABLE-3-page-9-5/prompt.txt: e8a2a518254dedd1006733ef6cf7a0a40913a99229e814c48a4b19fdc3bad0fb
        A/tables/TABLE-3-page-9-5/meta.json: 97ef423fde2d37f752c6a91f35267fe4ff4b2d6539b74179225d8329c9ae783e
        A/tables/TABLE-2-page-7-3/raw.json: 67272192e55d4b38c05611b475d3678b1929e2371a21bb54fddd879ce94d570d
        A/tables/TABLE-2-page-7-3/prompt.txt: 9c08cbca6a6d3aa3e869af380b9b91a6458c8c00c164cc9269302270ebbc14be
        A/tables/TABLE-2-page-7-3/meta.json: b9219f4dc89fd67940e0ea45e7f8c305cc5da6f8759c33f054c470c639e58e2f
        A/tables/TABLE-2-page-7-4/raw.json: 67272192e55d4b38c05611b475d3678b1929e2371a21bb54fddd879ce94d570d
        A/tables/TABLE-2-page-7-4/prompt.txt: 9c08cbca6a6d3aa3e869af380b9b91a6458c8c00c164cc9269302270ebbc14be
        A/tables/TABLE-2-page-7-4/meta.json: 6bd1cb417e8eb2dfe2ac813f312e407bd3012ed54606c38febc046172e4c2dd1
        B/passages.json: 6d3239f83fcf3e28001cc9f3d9570f0f10fa1facd2c49886d453f1a80e78397b
        B/raw.json: 5373b226a0a53915982137d6b462b7ea90cf599b5c2115121005ac8835c83803
        B/source-units.json: 139a17398b9b267ca8cbe0d41e99de84c0a9e775f742831ea044df8e87e602d7
        B/full-source-units.json: db656de68eb0c1afe383f338042032ab34060e9ce6d8ceabde4dffb5e7747f0d
        B/meta.json: a41b25e59848d84fd881d658576f5476382dcb6cf76f5c60022fc304ac28c9a6
        B/table-images/TABLE-3-page-9-1.png: c64ad1a61ed8efe3940199fda0e01ca0753947c81caa2227411c2a92e86cb832
        B/table-images/TABLE-1-page-7-1.png: d0a4219f169a3f8080c3905d2b0cb04f1c4ad5ac7f85d54d7f85d363218742a5
        B/table-images/TABLE-1-page-6-1.png: f1c6b4f2210a8eb4effc6e7d33ac9f2d473d0ab86e8776978797f3ddf0566019
        B/table-images/page-6.png: 9812b3a3bc7e58c277b582df1a78425245cd46880e1aaa99077845cb13e19482
        B/table-images/page-7.png: c7c136c02dccc07233932721f0b1aa1228124ba0f622da4172d8043c24b26a10
        B/table-images/page-9.png: 441d5512b60ecc15b326ea7a79c73da34a4dd62adff2d0e788f1490f6e9c89ea
        B/table-images/manifest.json: 4f0a7f1ebc3bf1f2b48b79a896a679a952c0f9527d903c63c5443058558eac2f
        B/table-images/TABLE-2-page-7-3.png: d0a4219f169a3f8080c3905d2b0cb04f1c4ad5ac7f85d54d7f85d363218742a5
        B/table-images/TABLE-2-page-7-2.png: d0a4219f169a3f8080c3905d2b0cb04f1c4ad5ac7f85d54d7f85d363218742a5
        B/clauses/window-03/raw.json: 74018f8f0a389914268d6ea73c8efaf1687f2da0fe20268de3c01a8aaa9b6343
        B/clauses/window-03/prompt.txt: f33daee926ad324a12f75549c419d4222bfe9b767c07373892bb108f550ce206
        B/clauses/window-03/meta.json: 185622f4a254abb64f0a225a4528893172565f3c585003caae9f331c03f988e9
        B/clauses/window-04/raw.json: 062996c3543fd1221b8d411308975e5fb23821ecb25d85ffb0b3f75b0e08f2d7
        B/clauses/window-04/prompt.txt: 36f5ee11ae48d05af58c5d45c9b1a9bd97e58d20b8044a1ebae7f9d41d3f5493
        B/clauses/window-04/meta.json: 5b31812ccea72826472e3e738207839e4f65c2f1e3e76ecb2ebfe8b18bcc613e
        B/clauses/window-05/raw.json: 57dd77ea8df3054ea9fe46ec56e93783b4a873a44e6fe7b745b0cc90f5319613
        B/clauses/window-05/prompt.txt: 602f2fa95a8ecae0d8092dc4ba3371121f46a40299715fbb846062919bda783a
        B/clauses/window-05/meta.json: 52a2d77632b35b0cb1434aae3063eec48972a21b9f4a0ec5219f593962d5f103
        B/clauses/window-02/raw.json: a44669906c87e1a17939ae6625ba561f3c072ebcbaf96b42b27f67e9aebeaed6
        B/clauses/window-02/prompt.txt: e6475859438eb0f35c3c128f9411a4e612c70ca45a611e78b36e2e1cdadf5030
        B/clauses/window-02/meta.json: cf126863a976f240ccc54100af2bb01c229e647848b6a097521aeb239db50074
        B/clauses/window-07/raw.json: 2cc1630327640adbcbfded5d67f3db1f7fb3ccae18e94642fe07dfff2b12f392
        B/clauses/window-07/prompt.txt: ceaf2bcff78e96bcb6994de2447938c6af8c9f9213702a9eb485e5c1113e2a6f
        B/clauses/window-07/meta.json: 93bd0ca380e777d918bb1376d691a06eb76d0d0f5aeb288acbf8fcd9f83893de
        B/clauses/window-01/raw.json: 090243c71a3a5658790df9916723832dd0d5addd28706cf3c21f823e66fad113
        B/clauses/window-01/prompt.txt: c7922d50c0d7b94dabc05a0312e379f4299752ee82addf775199f5b9fabcf9dd
        B/clauses/window-01/meta.json: 17da89bf244d04b9934e159d507a9b52f06d0f7a4e15f7c05163445f5ffa25f8
        B/clauses/window-06/raw.json: 27265f455c8b2e3ffba9840833fb18ba76446129041377feee65521e68731aef
        B/clauses/window-06/prompt.txt: b1cf745ca1f0b1df13f4f5afebf89cc0c9162e944e290c071ef24574ff2aacd6
        B/clauses/window-06/meta.json: 7dd710edb09cae1862e40b22f850a8273e2f50d6837ac4df606d167f870de67c
        B/tables/TABLE-1-page-7-2/raw.json: 2f1776c2da3992484271599a7db27c529e2ab84492572997a7083f50498acd78
        B/tables/TABLE-1-page-7-2/prompt.txt: b1816512be90a1cdf7fedefd76e5dec7c4b39f7705d0cef3412de53aa0ff1683
        B/tables/TABLE-1-page-7-2/meta.json: 8ec4a25f55603be39f86c7b560b541bc2868d2308a7b65c173f0f23472338c31
        B/tables/TABLE-1-page-6-1/raw.json: 4df8dc68324f710b98ec07750bb1bd0350186dd6906dc702c4eb0e2eef92298d
        B/tables/TABLE-1-page-6-1/prompt.txt: b3234e7f7475029ec969f662ab978d35b7013bbd5ccbdde1d715248cd1fa525e
        B/tables/TABLE-1-page-6-1/meta.json: 6779a5eb2ee36c916074233917c369276a2d207018f7d45d7f64fa7420dea5a9
        B/tables/TABLE-3-page-9-5/raw.json: 66e2a921c6bebe007b8e575c206c9425693d09ea443b890baa547e3e9a86da45
        B/tables/TABLE-3-page-9-5/prompt.txt: e8a2a518254dedd1006733ef6cf7a0a40913a99229e814c48a4b19fdc3bad0fb
        B/tables/TABLE-3-page-9-5/meta.json: 55e1bcf51b8c6f1c01d5fc05dbc7e3881989b0da17a2feac7f905ecbee7f40fe
        B/tables/TABLE-2-page-7-3/raw.json: b6002a0fcc3d0599f97791226cfce8f4b556c38ff62caafe5ac65e3e8c9f7c88
        B/tables/TABLE-2-page-7-3/prompt.txt: 9c08cbca6a6d3aa3e869af380b9b91a6458c8c00c164cc9269302270ebbc14be
        B/tables/TABLE-2-page-7-3/meta.json: d922bdb6bfb37e629beaf70d2b33acf5742d6f0f7fbe551b8d3e4c847cec4647
        B/tables/TABLE-2-page-7-4/raw.json: b6002a0fcc3d0599f97791226cfce8f4b556c38ff62caafe5ac65e3e8c9f7c88
        B/tables/TABLE-2-page-7-4/prompt.txt: 9c08cbca6a6d3aa3e869af380b9b91a6458c8c00c164cc9269302270ebbc14be
        B/tables/TABLE-2-page-7-4/meta.json: dbbc5a4deb4b888c44042c963dbf617e9499db0620b0a650b97c731978c9008d
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
      pdf_sha256: 6dbf400a356a1ad0078d9d36156ad9dbd70fbf223606aaa812f81fd7e2174cd8
      source_review: _compare/relationships-2026-11-16/review-current/Yu2023
      source_status_sha256: f1ff3cb38a4521931e0ff449f3b0ec4708e7f70cfb828a5da073a8b1449007da
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R009
    exposure:
      text: integrity of the left LSAF and UF (interaction)
    outcome:
      text: language performance
    analysis_label: Multiple linear regression analysis
    relation: association
    evidence_ids:
    - P1-S2-C5
    - P9-S1-C2
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
      pdf_sha256: 6dbf400a356a1ad0078d9d36156ad9dbd70fbf223606aaa812f81fd7e2174cd8
      source_review: _compare/relationships-2026-11-16/review-current/Yu2023
      source_status_sha256: f1ff3cb38a4521931e0ff449f3b0ec4708e7f70cfb828a5da073a8b1449007da
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Accounting without a linked unit P7-S1-C6
      - Accounting without a linked unit P7-S2-C2
      - Accounting without a linked unit P7-S2-C3
      - Accounting without a linked unit P7-S2-C5
      - Accounting without a linked unit P8-S1-C5
      - Unaccounted source passage P8-S1-C5
      - Unaccounted source passage P7-S2-C5
      - Unaccounted source passage P7-S2-C2
      - Unaccounted source passage P7-S1-C6
      - Unaccounted source passage P7-S2-C3
      - Result passage disposed without unit P9-S1-C3
      - Result passage disposed without unit P9-S1-C7
      - Result passage disposed without unit P9-S1-C8
      - Result passage disposed without unit P10-S1-C12
      - Result passage disposed without unit P11-S1-C1
      - Result passage disposed without unit P12-S2-C2
      - Result passage disposed without unit P12-S2-C8
      - Result passage disposed without unit P14-S1-C8
      - Result passage disposed without unit P14-S1-C9
      unattached_null_or_qualifier_ids:
      - P7-S2-C5
      - P14-S1-C1
      - P14-S1-C9
      suppressed_nonrepresented_units: 6
      default_disposition_count_requires_completeness_check: 168
      unselected_timing_passages:
      - P4-S1-C4
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P1-S2-C4
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
        source_id: P9-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P12-S1-C11
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      empty_frame_slots_require_confirmation:
      - validation
      - personal_factors
      - tested_personal_effects
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-6-1
      - TABLE-1-page-7-2
      - TABLE-2-page-7-3
      - TABLE-2-page-7-4
      - TABLE-3-page-9-5
      unlinked_tables:
      - TABLE-1-page-6-1
      - TABLE-1-page-7-2
      - TABLE-2-page-7-3
      - TABLE-2-page-7-4
      - TABLE-3-page-9-5
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P3-S1
        - P7-S2
        - P8-S1
        - P9-S1
        - P10-S1
        - P12-S2
        - P13-S1
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 6dbf400a356a1ad0078d9d36156ad9dbd70fbf223606aaa812f81fd7e2174cd8
      source_review: _compare/relationships-2026-11-16/review-current/Yu2023
      source_status_sha256: f1ff3cb38a4521931e0ff449f3b0ec4708e7f70cfb828a5da073a8b1449007da
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S2-C3
      disposition: represented
      result_indexes:
      - 0
      reason: States positive association between left LSAF diffusion indices and
        language scores.
    - source_id: P1-S2-C4
      disposition: represented
      result_indexes:
      - 5
      reason: States independent positive association between left LSAF mean FA and
        language subsets.
    - source_id: P1-S2-C5
      disposition: represented
      result_indexes:
      - 8
      reason: Reports no interaction effect of LSAF and UF on language performance.
    - source_id: P7-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the lack of correlation between demographics/stroke variables
        and language performance.
    - source_id: P7-S2-C2
      disposition: represented
      result_indexes:
      - 0
      - 1
      - 3
      reason: Reports correlations for lesion volume, left LSAF, and right LSAF/UF.
    - source_id: P7-S2-C3
      disposition: represented
      result_indexes:
      - 2
      reason: Reports no significant correlation for left UF.
    - source_id: P7-S2-C5
      disposition: represented
      result_indexes:
      - 4
      reason: Reports partial correlation results for left LSAF controlling for lesion
        volume.
    - source_id: P8-S1-C5
      disposition: represented
      result_indexes:
      - 5
      reason: Confirms positive association between left LSAF mean FA and language
        subsets.
    - source_id: P8-S1-C6
      disposition: represented
      result_indexes:
      - 6
      reason: Reports positive relation of left LSAF fiber number to AQ and comprehension.
    - source_id: P8-S1-C7
      disposition: represented
      result_indexes:
      - 7
      reason: Reports no significant association for left UF in regression.
    - source_id: P8-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Introductory phrase to the lack of correlation with other metrics.
    - source_id: P9-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports no correlation between demographics/clinical metrics and language
        assessment.
    - source_id: P9-S1-C2
      disposition: represented
      result_indexes:
      - 8
      reason: Confirms no interaction effects of LSAF and UF.
    - source_id: P9-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports collinearity analysis (VIF).
    - source_id: P9-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive statistics of lesion volumes.
    - source_id: P9-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of lesion overlay map.
    - source_id: P10-S1-C5
      disposition: repeated
      result_indexes:
      - 0
      - 5
      reason: Restatement of LSAF importance in discussion.
    - source_id: P10-S1-C6
      disposition: repeated
      result_indexes:
      - 8
      reason: Restatement of no interaction effect in discussion.
    - source_id: P10-S1-C12
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of correlation results in discussion.
    - source_id: P11-S1-C1
      disposition: repeated
      result_indexes:
      - 0
      - 5
      reason: Restatement of LSAF results in discussion.
    - source_id: P11-S1-C4
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of LSAF correlation with speech, repetition, and fluency.
    - source_id: P11-S2-C13
      disposition: repeated
      result_indexes:
      - 0
      - 2
      - 5
      - 7
      reason: General summary of LSAF vs UF influence.
    - source_id: P12-S1-C12
      disposition: represented
      result_indexes:
      - 9
      reason: Reports leftward distribution of LSAF fiber number.
    - source_id: P12-S2-C1
      disposition: represented
      result_indexes:
      - 10
      reason: Reports bilateral distribution of UF fiber number.
    - source_id: P12-S2-C2
      disposition: repeated
      result_indexes:
      - 0
      - 2
      - 5
      - 7
      reason: Restatement of LSAF vs UF roles in discussion.
    - source_id: P12-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Explains inability to distinguish UF and IFOF effects due to co-occurrence.
    - source_id: P14-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of limitation regarding LSAF and EmC co-occurrence.
    - source_id: P14-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of limitation regarding UF measurement artifacts.
    - source_id: P14-S1-C8
      disposition: repeated
      result_indexes:
      - 0
      - 2
      - 5
      - 7
      reason: Conclusion restating LSAF importance over UF.
    - source_id: P14-S1-C9
      disposition: repeated
      result_indexes:
      - 8
      reason: Conclusion restating no functional interaction between LSAF and UF.
    unresolved_coverage:
    - source_id: P12-S2-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    pending_source_ids:
    - P7-S1-C6
    - P8-S1-C8
    - P9-S1-C1
    - P9-S1-C3
    - P9-S1-C7
    - P9-S1-C8
    - P10-S1-C5
    - P10-S1-C6
    - P10-S1-C12
    - P11-S1-C1
    - P11-S1-C4
    - P11-S2-C13
    - P12-S2-C2
    - P12-S2-C8
    - P14-S1-C1
    - P14-S1-C4
    - P14-S1-C8
    - P14-S1-C9
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-6-1
    - TABLE-1-page-7-2
    - TABLE-2-page-7-3
    - TABLE-2-page-7-4
    - TABLE-3-page-9-5
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P4-S1-C3
      recruited_sample:
      - P1-S1-C7
      - P4-S1-C3
      eligibility:
      - P4-S1-C3
      - P4-S1-C4
      imaging_provenance:
      - P4-S2-C6
      - P4-S2-C7
      - P4-S2-C8
      - P5-S1-C6
      imaging_timing:
      - P4-S1-C3
      outcome_timing:
      - P4-S1-C3
      outcome_definition:
      - P4-S1-C6
      - P4-S1-C7
      - P4-S2-C4
      validation: []
      analysis_restrictions:
      - P14-S1-C3
      dependent_variable_statement:
      - P5-S2-C8
      - P7-S2-C4
      - P8-S1-C4
      limitations:
      - P13-S1-C9
      - P13-S1-C10
      - P14-S1-C1
      - P14-S1-C2
      - P14-S1-C3
      - P14-S1-C4
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P5-S2-C9
      - P7-S2-C4
      - P7-S2-C5
      - P9-S1-C6
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P4-S1-C3
      - P5-S2-C13
      - P5-S2-C14
      - P5-S2-C15
      - P6-S1-C1
      - P6-S1-C6
      - P7-S1-C3
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P1-S2-C4
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
      source_id: P9-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P12-S1-C11
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
      pdf_sha256: 6dbf400a356a1ad0078d9d36156ad9dbd70fbf223606aaa812f81fd7e2174cd8
      review_sha256: 1c1b3a515a934314d7d338e0448263b1d5c52fa253f65f9ec95201d52516328c
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
      - P1-S2-C5
      - P9-S1-C2
      source_result: The multiple linear regression analysis found no significant
        interaction effect of the integrity of the left LSAF and UF on language performance
        (p > 0.05).
      result_status: not_detected
      patient_measurement: patient_diffusion
      checks:
        analysis_identity:
          answer: fits
          reason: The source explicitly states that multiple linear regression was
            used to investigate the effects of the integrity of the left LSAF/UF on
            language performance, and specifically reports the result regarding the
            interaction effect (P1-S2-C5, P9-S1-C2).
          source_ids:
          - P1-S2-C5
          - P9-S1-C2
          - P5-S2-C8
        direction:
          answer: fits
          reason: The source states 'no interaction effect... was found (p > 0.05)',
            which corresponds to a null result (no_effect) in the proposed core. The
            direction is correctly identified as a lack of detected association for
            the interaction term.
          source_ids:
          - P1-S2-C5
          - P9-S1-C2
        construct:
          answer: fits
          reason: The exposure is correctly identified as the interaction of left
            LSAF and UF integrity. The outcome is language performance. The measurement
            is patient_diffusion, as the integrity is measured via DTI tractography
            (FA and fiber number) in the patients, not template overlap.
          source_ids:
          - P1-S2-C5
          - P5-S1-C6
          - P5-S2-C3
        qualifications:
          answer: fits
          reason: The proposed core includes the method (multiple linear regression)
            and the adjustment variables (sex, age, education, time post stroke, lesion
            volume) which are listed as confounding variables in the methods section
            (P5-S2-C9). The limitation regarding UF measurement artifacts is also
            correctly included.
          source_ids:
          - P5-S2-C8
          - P5-S2-C9
          - P14-S1-C4
        missing_material_caveat:
          answer: fits
          reason: The core captures the null result and the relevant methodological
            context. No material caveats that would change the interpretation of the
            null interaction effect are omitted.
          source_ids:
          - P1-S2-C5
          - P9-S1-C2
      optional_pending:
      - Sample size requires source confirmation; it has not been transcribed.
      - 'sample.time_post_onset: source confirmation required; original proposed wording
        remains in the audit.'
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Sample size requires source confirmation; it has not been transcribed.
    - 'sample.time_post_onset: source confirmation required; original proposed wording
      remains in the audit.'
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Sample size requires source confirmation; it has not been transcribed.
    - 'sample.time_post_onset: source confirmation required; original proposed wording
      remains in the audit.'
    normalizations:
    - field: bucket
      original: predictors
      action: route_from_kind
      value: regions
    - field: sample.n
      original: 36
      action: not_transcribed
      reason: Not supported by selected quotations
    - field: sample.time_post_onset
      original: time post-stroke less than 90 days
      action: not_transcribed
      reason: 'Numbers not grounded in usable selected source readings: 9E+1'
    analysis_identity:
      id: R009
      exposure:
        text: integrity of the left LSAF and UF (interaction)
      outcome:
        text: language performance
      analysis_label: Multiple linear regression analysis
      relation: association
      evidence_ids:
      - P1-S2-C5
      - P9-S1-C2
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
        pdf_sha256: 6dbf400a356a1ad0078d9d36156ad9dbd70fbf223606aaa812f81fd7e2174cd8
        source_review: _compare/relationships-2026-11-16/review-current/Yu2023
        source_status_sha256: f1ff3cb38a4521931e0ff449f3b0ec4708e7f70cfb828a5da073a8b1449007da
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P4-S1-C3:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 6dbf400a356a1ad0078d9d36156ad9dbd70fbf223606aaa812f81fd7e2174cd8
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: a195361f9c073a2161ba35f5ccf144bdf4395aa6be84a8bd80040494ae1b8ac9
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P4-S1-C3
          page: 4
          text_layer_sha256: a195361f9c073a2161ba35f5ccf144bdf4395aa6be84a8bd80040494ae1b8ac9
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: 'Participants

          Thirty-sixparticipants(27males/9females, agerange: 25–78years, meanage:
          53.31± 12.37years;

          mean duration of education: 10.78 ± 3.48 years; mean time since stroke:
          36.56 ± 28.25 days) with

          acute/subacute PSA were recruited according to the following inclusion criteria:
          first-ever left hemi-

          spheric stroke (i.e., infarction or hemorrhage) with normal consciousness,
          time post-stroke less than 90

          days, age between 18–80 years, right-handedness and native Chinese speakers,
          the consistent presence

          of various types of aphasia (aphasia quotient value < 93.8), collaborating
          to complete a language

          faculties assessment and magnetic resonance imaging (MRI) scan.'
        anchor_text: 'Participants

          Thirty-sixparticipants(27males/9females, agerange: 25–78years, meanage:
          53.31± 12.37years;

          mean duration of education: 10.78 ± 3.48 years; mean time since stroke:
          36.56 ± 28.25 days) with

          acute/subacute PSA were recruited according to the following inclusion criteria:
          first-ever left hemi-

          spheric stroke (i.e., infarction or hemorrhage) with normal consciousness,
          time post-stroke less than 90

          days, age between 18–80 years, right-handedness and native Chinese speakers,
          the consistent presence

          of various types of aphasia (aphasia quotient value < 93.8), collaborating
          to complete a language

          faculties assessment and magnetic resonance imaging (MRI) scan.'
        excluded_fragments: []
        image_sha256: c603ba7f8e28c844d89a7866a38f79ecfebab7e533bca68c3410f5a14960be5a
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 1
  quote: 'In addition, no interaction effect of the integrity of the left LSAF and
    UF on language performance

    was found (p > 0.05).'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-26'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
