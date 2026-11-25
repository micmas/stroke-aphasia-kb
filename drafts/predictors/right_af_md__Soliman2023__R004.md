---
id: right_af_md
name: right AF MD
kind: predictor
findings:
- id: f1
  target: repetition
  target_kind: impairment
  claim: A significant correlation was found between mean diffusivity (MD) of the
    right arcuate fasciculus (AF) and repetition impairment.
  direction: likely
  relationship: correlational
  method: tractography
  sample:
    n: not_reported
    population: Right-handed native Arabic speakers with first-ever left hemispheric
      ischemic stroke and post-stroke aphasia
    phase: not_reported
    time_post_onset: Subacute stage (mean 3.07 weeks post-stroke onset)
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Small sample size
  - Right AF was analyzed as a whole tract without segmenting different parts
  - CSD performed with b=1000 and 32 directions
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Average mean diffusivity (MD) of the right arcuate
    fasciculus (AF) extracted via constrained spherical deconvolution (CSD)-based
    tractography using a two-ROI approach. Partial correlation adjusted for age, lesion
    volume, and risk factors. Additional metadata has not been transcribed; review
    the pending-field flags before approval. PDF image reading (P3-S1-C9, two-model
    agreement, human verification pending): . The mean time ± SD from stroke onset
    to MRI scan was 3.07 ± 0.91 weeks (range: 2–4 weeks).


    3.2. Original text-layer quotation is preserved below.'
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
    - proposed_concept:repetition
  citation: '@Soliman2023'
  source_passages:
  - section: Original source P1-S2-C5
    page: 1
    quote: "Additionally, a significant correlation was found \nbetween MD of the\
      \ right AF and repetition."
    supports: claim
  - section: Original source P3-S2-C5
    page: 3
    quote: "In the \nright hemisphere, only a significant correlation was found between\
      \ MD \nof the AF and repetition (r = 0.740, p = .004) Table 4. \n4."
    supports: claim
  - section: Original source P6-S2-C7
    page: 6
    quote: "A significant correlation between the increase in the MD of the right\
      \ \nAF and repetition impairment was noted in our data (r = 0.740, p =\n.004)."
    supports: claim
  - section: Original source P7-S1-C8
    page: 7
    quote: "On the other hand, repetition impairment was \nrelated to the injury of\
      \ the right AF."
    supports: claim
  - section: Original source P3-S1-C3
    page: 3
    quote: "Partial \ncorrelations were performed between the diffusion measures (that\
      \ \nshowed significant difference between the two groups) of the dissected \n\
      tracts at both sides, and the different language components with elimi­\nnation\
      \ the effect of the age, lesion volume and the risk factors."
    supports: method
  - section: Original source P2-S2-C11
    page: 2
    quote: "Patients were included \nbased on the following criteria: i) first ever\
      \ left hemispheric ischemic \nstroke, ii) within the first month post-stroke,\
      \ iii) right handed patients, \niv) conscious patients and can tolerate the\
      \ MRI examination."
    supports: sample
  - section: Original source P3-S1-C9
    page: 3
    quote: "The mean time ± SD \nfrom stroke onset to MRI scan was 3.07 ± 0.91 weeks\
      \ (range: 2–4 \nweeks). \n3.2."
    supports: sample
  - section: Original source P2-S4-C8
    page: 2
    quote: "Dissection of dorsal stream (AF) and ventral stream \n(IFOF, ILF and UF)\
      \ tracts as well as the FAT for all participants was \nachieved bilaterally,\
      \ using a two-ROI approach [25]."
    supports: method
  - section: Original source P6-S3-C8
    page: 6
    quote: "Limitations \nThe small sample size is a main limitation of this study."
    supports: limitation
  - section: Original source P6-S3-C12
    page: 6
    quote: "Another technical limitation is that we performed \nCSD using b value\
      \ = 1000 with 32 diffusion directions, being more \nconvenient to the clinical\
      \ practice."
    supports: limitation
  - section: Original source P6-S3-C14
    page: 6
    quote: "Additionally, we did not dissect the different \nAF segments but rather\
      \ relied on the whole AF tract."
    supports: limitation
predictor_type: imaging_metric
short_definition: Average mean diffusivity (MD) of the right arcuate fasciculus (AF)
  extracted via constrained spherical deconvolution (CSD)-based tractography using
  a two-ROI approach.
assessment:
- Hemispheric Stroke Scale (HSS) language subset
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-25'
relationship_review:
  paper: Soliman2023
  proposal_id: R004
  review_status_sha256: cbbacfda59e710cc5fe43efa8c957fe49f4eb7de3d16b42117aa0689795a5fee
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 37264b297e95b9dc7a53d1234db05b4103bf0cab0f8f90e84d82c7a162c4afe4
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 37264b297e95b9dc7a53d1234db05b4103bf0cab0f8f90e84d82c7a162c4afe4
        A/passages.json: 1007f7b729d232916913e92a68971e9f28d3cee67cde6cc610a9505a5d951c98
        A/raw.json: dccc92e60ee492809f0862fdce2f1fe0892bd04874e5ebca10a9d88250249cd6
        A/source-units.json: ebfbc66c18425fe489f2e937d866d9feb76cca50cec1e59f8aba29acc5bb296b
        A/full-source-units.json: 60d695bd54edcc5fb8942485c5339e1786caf9cb4a5bbded5ca521c1fe34b71f
        A/meta.json: 4522e1c58bebfa7ab1de4bdfbfae2e2b5ed2f760e1c6a39c624d513fba349201
        A/table-images/TABLE-1-page-3-1.png: 52e95b160f3afb8c9963a8a4f3896c2d73330c93bf4518286ca8d42e19d7c74f
        A/table-images/page-3.png: b6ce59a491504182871d066b31896ca1884d40463f101aaeda8b35f6a7fbd270
        A/table-images/page-6.png: d65644919243e6fce4a31fb159de6e257cfb7efa1f453b94136bd1b783197bc7
        A/table-images/page-5.png: b12480e55bd9cd081a82280947f6be8795f2cf12d1cb1571e382c29619a1df9d
        A/table-images/TABLE-4-page-6-1.png: 6c0dd27127dfb2eb0ee6abeea4e54a55bf25fc95030ae60375f00e7524b359ff
        A/table-images/manifest.json: 6c08e76f006fff6c14a94b6201f72fcf151f23d18e4bc81a5fee7c5e3b7c30d2
        A/table-images/TABLE-3-page-5-2.png: f09d8a67398eb7c22ed79dc1694de5a21b15a3b44bf583ca48cd9945de299aca
        A/table-images/TABLE-2-page-5-1.png: ac5d4c740961b57607aa4e347768dff0ea9cc5c00cb3d6acdf11384e422a1c06
        A/clauses/window-03/raw.json: 7c4f4ffd6a44c15a3d6f1b063319f2dad6fff8f8ca18d6e179f542dad85b506b
        A/clauses/window-03/prompt.txt: 6219d07cc01031d2dd45aae7b44fd5185929ab10ae6cd6029607bfc73c95e77f
        A/clauses/window-03/meta.json: bdd868fa31d0a0072043cacdfa0eff063c504fdd5e576c6cb84e72b1aee5b8cf
        A/clauses/window-04/raw.json: 0b58f7c6d226b86b91d42ae7588ae2e069d4c36fcbbbcaa9ed24f987af2fe351
        A/clauses/window-04/prompt.txt: 74bc6519e0be06ee5c3f7670c96bdd3f9390f1b599e22381a258884fe4b00c13
        A/clauses/window-04/meta.json: 1cf2fe72c00b1857982be69bba8dcecfe11e353a5be297ba348a648a198e1c68
        A/clauses/window-05/raw.json: c7708eb605d1d24070220698308e403bd542b9b4807055dac51690c6ccea5a3b
        A/clauses/window-05/prompt.txt: 15c9a0f7dd0a1b6a25ee898f642a654d4230f6b436887e5cad3d8de2e5cf4e12
        A/clauses/window-05/meta.json: 02d12aacb8c5bdf00bbd6893f830963c0a3406051dcf6019c7d368fc2c7d09ef
        A/clauses/window-02/raw.json: 73b44d5668eb1bdfa7772441660629965d085003ddaa6bd1d7262c9cd7501910
        A/clauses/window-02/prompt.txt: bfd7ff60e6afecc5a126e89ec6a2b35009c4f5aea45386672f4d3a7c926bbb0e
        A/clauses/window-02/meta.json: d36b036076725199572265c3b84bb0bb6f9d58a137a32b4d90d497a6b556b3d5
        A/clauses/window-07/raw.json: abfccf841b4e91339852eacf75a6f85353791dd775d71805ee814138caf9bad0
        A/clauses/window-07/prompt.txt: 7b2da9953ec075dcfba35bcff6da5c7ff361553b6da39735a74825ddead3da49
        A/clauses/window-07/meta.json: 6ab6cfc2328f0475cfc6646e3dc6734de1130ae31356440752dd047c4b93ed62
        A/clauses/window-01/raw.json: 7f28803dc2346dcc65e41fedfc4db241a8f07937032a12672dff74640b8e04b4
        A/clauses/window-01/prompt.txt: 77c41f83787376a0033550bb3292b17e4719402789c859afb8b2f59820859f3c
        A/clauses/window-01/meta.json: baa86d25be777581228f7db20733c80d9a6992bbe4f647e004d0f09a035d079f
        A/clauses/window-06/raw.json: bdcd4a47a0d3b32cb11c7f53f8f7456131a5411837193f11fa87ccb102899026
        A/clauses/window-06/prompt.txt: 7c0b686121c784bfbcff2b92c8fb9028d61ac076dbc6a3724c0ba9f8bcad5ff3
        A/clauses/window-06/meta.json: 96ec6fb6482d2732724b293f71558501592b517a27bbb161240abdba08e85c48
        A/tables/TABLE-4-page-6-4/raw.json: 1c6e0f1d6fe254d4ed5bfd9961600ada04fedec62bd6f76105b61f88aa07ad34
        A/tables/TABLE-4-page-6-4/prompt.txt: 40c7078af2bc37d08d697cc69cd3e672200e8301cbae9bcdf0e36e44ca4cfd40
        A/tables/TABLE-4-page-6-4/meta.json: 64612b4a46ac0afa22e9c8b4db817c5dd0012f8cc5ca08396cd56ce369f126a3
        A/tables/TABLE-3-page-5-3/raw.json: d17a1fbea517b09ca4d76218ec2b6361cf6da80c0de2cd4c197b4b4bdbac2981
        A/tables/TABLE-3-page-5-3/prompt.txt: 3d56a20c53d2f43e11d5028c72bea7995fb95049fad257789d9196ce9ff31d2a
        A/tables/TABLE-3-page-5-3/meta.json: eccf5f3f6508e19634ced569fadf3cb3bf79222b864fbd56919cd5f6c59861f6
        A/tables/TABLE-2-page-5-2/raw.json: b59b068390bf8b450bc6d67badd0d390374ba8dbacfb6a5020690cfb1bd051c9
        A/tables/TABLE-2-page-5-2/prompt.txt: c196360cd446895abe33ed3ebb1aff42d3a8d3fa54a24933b0e4fd3a7369257c
        A/tables/TABLE-2-page-5-2/meta.json: ca22a9e8136c8fd9f589acdb35f3dd064663c28b5969ba33e850135894360db3
        A/tables/TABLE-1-page-3-1/raw.json: a65fee307dced801b931cfab4fd883311d5c5927f5fa87c641c24e8220160d35
        A/tables/TABLE-1-page-3-1/prompt.txt: 89c2af37f4bd995bca75c2f4e33253a1fb99316c0a6c54a7174df8c8d7c9669b
        A/tables/TABLE-1-page-3-1/meta.json: 070d1d55fd5a2da08b5cbb558adfe3c7754c506936e4524e12574340283ef401
        B/passages.json: 1007f7b729d232916913e92a68971e9f28d3cee67cde6cc610a9505a5d951c98
        B/raw.json: 61fa4194dfa9ee05b9c4897e0ed9c0f3c258efe87a9a6f31059c23d830740a55
        B/source-units.json: ebfbc66c18425fe489f2e937d866d9feb76cca50cec1e59f8aba29acc5bb296b
        B/full-source-units.json: 60d695bd54edcc5fb8942485c5339e1786caf9cb4a5bbded5ca521c1fe34b71f
        B/meta.json: 29c5dea01b4cd520755b719062e7fb663f676530159e21fffa9bb82843a3e579
        B/table-images/TABLE-1-page-3-1.png: 52e95b160f3afb8c9963a8a4f3896c2d73330c93bf4518286ca8d42e19d7c74f
        B/table-images/page-3.png: b6ce59a491504182871d066b31896ca1884d40463f101aaeda8b35f6a7fbd270
        B/table-images/page-6.png: d65644919243e6fce4a31fb159de6e257cfb7efa1f453b94136bd1b783197bc7
        B/table-images/page-5.png: b12480e55bd9cd081a82280947f6be8795f2cf12d1cb1571e382c29619a1df9d
        B/table-images/TABLE-4-page-6-1.png: 6c0dd27127dfb2eb0ee6abeea4e54a55bf25fc95030ae60375f00e7524b359ff
        B/table-images/manifest.json: 38d8149c024385bdd4f5f81e9cb4a636ce12f02976e70c8f67eae011a32e752e
        B/table-images/TABLE-3-page-5-2.png: f09d8a67398eb7c22ed79dc1694de5a21b15a3b44bf583ca48cd9945de299aca
        B/table-images/TABLE-2-page-5-1.png: ac5d4c740961b57607aa4e347768dff0ea9cc5c00cb3d6acdf11384e422a1c06
        B/clauses/window-03/raw.json: e2649b2331b26798bbe72a3b1004464bcf36eb1493e32515ebdbaa622dfdf21e
        B/clauses/window-03/prompt.txt: 6219d07cc01031d2dd45aae7b44fd5185929ab10ae6cd6029607bfc73c95e77f
        B/clauses/window-03/meta.json: b5b172c84369466e228929e72e41aef8a17e9dec9922a7c93f8ad175f72e90b9
        B/clauses/window-04/raw.json: 7ddb98593bb08a4406c63966f80f4ea5ffc836cdc93fae4917ecc036ab6349c4
        B/clauses/window-04/prompt.txt: 74bc6519e0be06ee5c3f7670c96bdd3f9390f1b599e22381a258884fe4b00c13
        B/clauses/window-04/meta.json: 3749a7ddb9100b087c3b6ff4a066f69bbd4cf46de42411dccee30bce285b92d1
        B/clauses/window-05/raw.json: 5c320a4391d9be30f4ec9d61433cadcb63e62b1dce0acea34ad4bac6b2e3654c
        B/clauses/window-05/prompt.txt: 15c9a0f7dd0a1b6a25ee898f642a654d4230f6b436887e5cad3d8de2e5cf4e12
        B/clauses/window-05/meta.json: e2dd661dbcec2391bcaca96926276d746cb89168f00fd30edcd4dce40ee8499d
        B/clauses/window-02/raw.json: 771d753bd0aa1171d9ced8c174c8550f494db95bc73d5f2c07fce4950084a7f0
        B/clauses/window-02/prompt.txt: bfd7ff60e6afecc5a126e89ec6a2b35009c4f5aea45386672f4d3a7c926bbb0e
        B/clauses/window-02/meta.json: 7c3a046538332945fcb7bb40fb3071534f16dee182316d061b759779ad5328ef
        B/clauses/window-07/raw.json: 22b4275218a3e2373f029119d71189bed7ee6a18ac04c94f12d8db58f17f8020
        B/clauses/window-07/prompt.txt: 7b2da9953ec075dcfba35bcff6da5c7ff361553b6da39735a74825ddead3da49
        B/clauses/window-07/meta.json: f37aba415a1335c8e1a0bc0f8ac9a5ff0d535fae339d2551b6e9c63784a3f8b8
        B/clauses/window-01/raw.json: 62e4b5c78e4aa24df756bb911873b661547b1658c769a69c0e0ca901d3b4b3e0
        B/clauses/window-01/prompt.txt: 77c41f83787376a0033550bb3292b17e4719402789c859afb8b2f59820859f3c
        B/clauses/window-01/meta.json: 21648ca451ce9c6d497c06ad16990a0170c5db04b739c9f370e6558feca09189
        B/clauses/window-06/raw.json: 6a9e454ae0d95684e94404a65328492aedd1d2ba3ff7b5ee099bf60449c78436
        B/clauses/window-06/prompt.txt: 7c0b686121c784bfbcff2b92c8fb9028d61ac076dbc6a3724c0ba9f8bcad5ff3
        B/clauses/window-06/meta.json: cfd66fe8471df779d043d9ebf35282d7a3ac820017aa73bc14a610ed6956fb0d
        B/tables/TABLE-4-page-6-4/raw.json: 8321ef65cc7670a9005ee945df8f5d6886250695ef3fe34720f3426b67889ee2
        B/tables/TABLE-4-page-6-4/prompt.txt: 40c7078af2bc37d08d697cc69cd3e672200e8301cbae9bcdf0e36e44ca4cfd40
        B/tables/TABLE-4-page-6-4/meta.json: 902f40b6aa4014d232ebab79f56355c880026d098d974c111de0a160dd3a8c43
        B/tables/TABLE-3-page-5-3/raw.json: d17a1fbea517b09ca4d76218ec2b6361cf6da80c0de2cd4c197b4b4bdbac2981
        B/tables/TABLE-3-page-5-3/prompt.txt: 3d56a20c53d2f43e11d5028c72bea7995fb95049fad257789d9196ce9ff31d2a
        B/tables/TABLE-3-page-5-3/meta.json: 7382fe41547001cdf7889b1ec7a2bb45bfe0610dbca8fa842e40cfc3cb01a304
        B/tables/TABLE-2-page-5-2/raw.json: b59b068390bf8b450bc6d67badd0d390374ba8dbacfb6a5020690cfb1bd051c9
        B/tables/TABLE-2-page-5-2/prompt.txt: c196360cd446895abe33ed3ebb1aff42d3a8d3fa54a24933b0e4fd3a7369257c
        B/tables/TABLE-2-page-5-2/meta.json: 1d2e8f9ef01283fbdc8f5b12c67a28ab0b5634f9512b954e8903b87f5068fe79
        B/tables/TABLE-1-page-3-1/raw.json: d99ca248f31ec5c5de1eec915ff0bbf21cdd0d6f6555379a5f798c573c5100a8
        B/tables/TABLE-1-page-3-1/prompt.txt: 89c2af37f4bd995bca75c2f4e33253a1fb99316c0a6c54a7174df8c8d7c9669b
        B/tables/TABLE-1-page-3-1/meta.json: 6c7c863cfd733ed2128647afa8570511a157cab7020afdcfc10b6f45eb6018c2
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
      pdf_sha256: 37264b297e95b9dc7a53d1234db05b4103bf0cab0f8f90e84d82c7a162c4afe4
      source_review: _compare/relationships-2026-11-16/review-current/Soliman2023
      source_status_sha256: a2957b53b29853bef8e48d0e4675a836cee52660f89ce2088d87d685526e7c55
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R004
    exposure:
      text: MD of the right AF
    outcome:
      text: repetition
    analysis_label: Partial correlation between diffusion measures and language components
      (Right Hemisphere)
    relation: association
    evidence_ids:
    - P1-S2-C5
    - P3-S2-C5
    - P6-S2-C7
    - P7-S1-C8
    qualifier_ids:
    - P3-S1-C3
    - P6-S4-C3
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 37264b297e95b9dc7a53d1234db05b4103bf0cab0f8f90e84d82c7a162c4afe4
      source_review: _compare/relationships-2026-11-16/review-current/Soliman2023
      source_status_sha256: a2957b53b29853bef8e48d0e4675a836cee52660f89ce2088d87d685526e7c55
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P3-S1-C11
      - Result passage disposed without unit P3-S1-C13
      - Result passage disposed without unit P3-S1-C8
      - Result passage disposed without unit P6-S2-C13
      - Result passage disposed without unit P6-S3-C11
      - Result passage disposed without unit P7-S1-C2
      - Result passage disposed without unit P7-S1-C10
      - Accounting without a linked unit P7-S1-C7
      - Accounting without a linked unit P7-S1-C8
      - Unaccounted source passage P7-S1-C7
      - Unaccounted source passage P7-S1-C8
      unattached_null_or_qualifier_ids: []
      suppressed_nonrepresented_units: 2
      default_disposition_count_requires_completeness_check: 160
      unselected_timing_passages:
      - P1-S1-C6
      - P2-S2-C10
      - P3-S1-C7
      - P6-S3-C10
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P5-S2-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S2-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P6-S3-C6
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      empty_frame_slots_require_confirmation:
      - tested_personal_effects
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-3-1
      - TABLE-2-page-5-2
      - TABLE-3-page-5-3
      - TABLE-4-page-6-4
      unlinked_tables:
      - TABLE-1-page-3-1
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P3-S1
        - P3-S2
        - P3-S3
        - P4-S1
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 37264b297e95b9dc7a53d1234db05b4103bf0cab0f8f90e84d82c7a162c4afe4
      source_review: _compare/relationships-2026-11-16/review-current/Soliman2023
      source_status_sha256: a2957b53b29853bef8e48d0e4675a836cee52660f89ce2088d87d685526e7c55
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C12
      disposition: represented
      result_indexes:
      - 0
      reason: States significant lower FA and higher MD/RD in patients' WM tracts
        in left hemisphere.
    - source_id: P1-S1-C13
      disposition: represented
      result_indexes:
      - 1
      reason: States significant differences in diffusion measures in the right hemisphere.
    - source_id: P1-S1-C15
      disposition: represented
      result_indexes:
      - 2
      reason: Reports correlations between comprehension and FA of left AF and left
        ILF.
    - source_id: P1-S2-C5
      disposition: represented
      result_indexes:
      - 3
      reason: Reports correlation between MD of right AF and repetition.
    - source_id: P2-S3-C16
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes exclusion of one participant due to corrupted images.
    - source_id: P2-S3-C17
      disposition: background_or_descriptive
      result_indexes: []
      reason: States no subject excluded after visual inspection.
    - source_id: P3-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports no significant difference in age between groups.
    - source_id: P3-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes lesion overlay map distribution.
    - source_id: P3-S1-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes non-reconstructed tracts.
    - source_id: P3-S1-C16
      disposition: represented
      result_indexes:
      - 0
      reason: Details reduction in FA and increase in RD of left AF, ILF, and FAT.
    - source_id: P3-S1-C17
      disposition: represented
      result_indexes:
      - 0
      reason: Details increase in MD of left ILF and IFOF.
    - source_id: P3-S2-C2
      disposition: represented
      result_indexes:
      - 1
      reason: Details right hemisphere differences in MD, AD of AF and MD, RD of ILF.
    - source_id: P3-S2-C3
      disposition: represented
      result_indexes:
      - 2
      reason: Reports correlation between FA of left AF and comprehension.
    - source_id: P3-S2-C4
      disposition: represented
      result_indexes:
      - 2
      reason: Reports correlation between FA of left ILF and comprehension.
    - source_id: P3-S2-C5
      disposition: represented
      result_indexes:
      - 3
      reason: Reports correlation between MD of right AF and repetition.
    - source_id: P4-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes an individual patient's imaging findings.
    - source_id: P5-S1-C4
      disposition: represented
      result_indexes:
      - 0
      reason: Restates reduction of FA and increase in RD of AF, ILF, and FAT in lesional
        hemisphere.
    - source_id: P5-S1-C5
      disposition: represented
      result_indexes:
      - 0
      reason: Restates increases in MD of left ILF and IFOF.
    - source_id: P5-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discusses inconsistency with prior study (Ivanova et al).
    - source_id: P5-S2-C7
      disposition: represented
      result_indexes:
      - 2
      reason: Restates correlation between FA of left AF and comprehension.
    - source_id: P6-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discusses other studies' findings on AF injury.
    - source_id: P6-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discusses other reports on AF and repetition.
    - source_id: P6-S1-C4
      disposition: represented
      result_indexes:
      - 2
      reason: Restates correlation between FA of left ILF and comprehension.
    - source_id: P6-S1-C8
      disposition: represented
      result_indexes:
      - 4
      reason: Reports no significant correlation between FAT diffusion measures and
        aphasia.
    - source_id: P6-S1-C13
      disposition: represented
      result_indexes:
      - 1
      reason: Restates right hemisphere increases in MD of AF/ILF, AD of AF, and RD
        of ILF.
    - source_id: P6-S2-C3
      disposition: represented
      result_indexes:
      - 1
      reason: Reports significant increase in AD of right FAT.
    - source_id: P6-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports non-significant decrease in FA and increase in MD/RD of right
        FAT.
    - source_id: P6-S2-C7
      disposition: represented
      result_indexes:
      - 3
      reason: Restates correlation between MD of right AF and repetition.
    - source_id: P6-S2-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: States no other significant correlations were noted apart from AF.
    - source_id: P6-S2-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discusses age as a potential confounder.
    - source_id: P6-S3-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about contralateral WM changes being suggestive of
        degeneration.
    - source_id: P7-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion about the ability to extract measures.
    - source_id: P7-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion about RD driving changes in lesional hemisphere.
    - source_id: P7-S1-C7
      disposition: repeated
      result_indexes:
      - 2
      reason: Restates that left AF and left ILF injury relate to comprehension.
    - source_id: P7-S1-C8
      disposition: repeated
      result_indexes:
      - 3
      reason: Restates that repetition impairment relates to right AF injury.
    - source_id: P7-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion that contralateral WM changes suggest a degenerative
        process.
    unresolved_coverage: []
    pending_source_ids:
    - P2-S3-C16
    - P2-S3-C17
    - P3-S1-C8
    - P3-S1-C11
    - P3-S1-C13
    - P3-S2-C2
    - P4-S1-C2
    - P5-S2-C2
    - P6-S1-C2
    - P6-S1-C3
    - P6-S2-C5
    - P6-S2-C11
    - P6-S2-C13
    - P6-S3-C11
    - P7-S1-C2
    - P7-S1-C4
    - P7-S1-C7
    - P7-S1-C10
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-3-1
    - TABLE-2-page-5-2
    - TABLE-3-page-5-3
    - TABLE-4-page-6-4
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P2-S2-C13
      - P2-S2-C14
      recruited_sample:
      - P2-S2-C10
      - P2-S2-C11
      - P2-S2-C12
      - P2-S2-C13
      - P2-S2-C14
      eligibility:
      - P2-S2-C11
      - P2-S2-C12
      imaging_provenance:
      - P2-S3-C8
      - P2-S3-C9
      - P2-S3-C10
      imaging_timing:
      - P2-S2-C11
      - P3-S1-C9
      outcome_timing:
      - P2-S2-C11
      - P3-S1-C9
      outcome_definition:
      - P2-S3-C5
      - P2-S3-C6
      - P2-S3-C7
      validation:
      - P5-S2-C6
      analysis_restrictions:
      - P3-S1-C2
      - P3-S1-C4
      dependent_variable_statement:
      - P1-S1-C11
      - P2-S2-C6
      - P3-S1-C3
      limitations:
      - P6-S3-C8
      - P6-S3-C10
      - P6-S3-C12
      - P6-S3-C13
      - P6-S3-C14
      - P6-S3-C15
      personal_factors:
      - P3-S1-C7
      - P3-S1-C9
      - P3-S2-C6
      - P6-S2-C14
      tested_personal_effects: []
      adjustment_roles:
      - P3-S1-C3
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P2-S2-C15
      - P3-S1-C7
      - P3-S1-C9
      - P3-S2-C6
      - P6-S2-C14
    outcome_type: both_reported
    imaging_vs_outcome: concurrent
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P5-S2-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S2-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P6-S3-C6
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
      pdf_sha256: 37264b297e95b9dc7a53d1234db05b4103bf0cab0f8f90e84d82c7a162c4afe4
      review_sha256: cbbacfda59e710cc5fe43efa8c957fe49f4eb7de3d16b42117aa0689795a5fee
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
      - P3-S2-C5
      - P6-S2-C7
      - P7-S1-C8
      source_result: A significant positive partial correlation (r = 0.740, p = .004)
        was found between the mean diffusivity (MD) of the right arcuate fasciculus
        (AF) and repetition impairment in post-stroke aphasic patients. This analysis
        was performed in the right hemisphere, adjusting for age, lesion volume, and
        risk factors. The result is reported as a detected association.
      result_status: detected
      patient_measurement: patient_diffusion
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis correctly identifies the partial correlation
            between right AF MD and repetition. The source explicitly states this
            correlation in P1-S2-C5, P3-S2-C5, P6-S2-C7, and P7-S1-C8. The method
            is confirmed as a partial correlation in P3-S1-C3.
          source_ids:
          - P1-S2-C5
          - P3-S2-C5
          - P6-S2-C7
          - P7-S1-C8
          - P3-S1-C3
        direction:
          answer: fits
          reason: The source reports a positive correlation (r = 0.740) between MD
            and repetition impairment (P3-S2-C5). The proposed draft describes this
            as a 'significant correlation' and 'likely' direction, which is faithful
            to the detected positive association. It does not claim a null effect
            or reverse the direction.
          source_ids:
          - P3-S2-C5
          - P6-S2-C7
        construct:
          answer: fits
          reason: The exposure is correctly identified as MD of the right AF. The
            outcome is repetition impairment. The measurement method is CSD-based
            tractography extracting diffusion measures from dissected tracts (P2-S4-C8,
            P2-S4-C9). The patient measurement is patient_diffusion because the analysis
            uses diffusion metrics (MD) extracted from the patients' own tractography,
            not template overlap or atlas metadata.
          source_ids:
          - P1-S1-C8
          - P2-S4-C8
          - P2-S4-C9
          - P3-S2-C5
        qualifications:
          answer: fits
          reason: The draft includes the qualification that the correlation was adjusted
            for age, lesion volume, and risk factors, which matches P3-S1-C3. It also
            includes limitations regarding small sample size (P6-S3-C8), whole AF
            tract analysis (P6-S3-C14), and CSD parameters (P6-S3-C12). These are
            material qualifiers present in the source.
          source_ids:
          - P3-S1-C3
          - P6-S3-C8
          - P6-S3-C14
          - P6-S3-C12
        missing_material_caveat:
          answer: fits
          reason: No material caveats are missing. The draft acknowledges the small
            sample size and the specific technical limitations of the CSD acquisition
            and tract dissection. The unresolved image reading for P3-S1-C7 (age)
            does not affect the core relationship of MD and repetition, as the age
            difference was non-significant (P3-S1-C8) and the correlation was adjusted
            for age anyway.
          source_ids:
          - P6-S3-C8
          - P6-S3-C14
          - P6-S3-C12
      optional_pending:
      - Exact sample size N for the correlation analysis (16 or 17) is not explicitly
        transcribed in the provided window, though 17 patients were enrolled and 1
        excluded from diffusion analysis.
      - Specific p-value threshold used for the correlation (Bonferroni corrected)
        is mentioned in P3-S1-C4 but the exact adjusted alpha is not transcribed.
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Sample size requires source confirmation; it has not been transcribed.
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Exact sample size N for the correlation analysis (16 or 17) is not explicitly
      transcribed in the provided window, though 17 patients were enrolled and 1 excluded
      from diffusion analysis.
    - Specific p-value threshold used for the correlation (Bonferroni corrected) is
      mentioned in P3-S1-C4 but the exact adjusted alpha is not transcribed.
    normalizations:
    - field: sample.n
      original: 17
      action: not_transcribed
      reason: Not supported by selected quotations
    analysis_identity:
      id: R004
      exposure:
        text: MD of the right AF
      outcome:
        text: repetition
      analysis_label: Partial correlation between diffusion measures and language
        components (Right Hemisphere)
      relation: association
      evidence_ids:
      - P1-S2-C5
      - P3-S2-C5
      - P6-S2-C7
      - P7-S1-C8
      qualifier_ids:
      - P3-S1-C3
      - P6-S4-C3
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 37264b297e95b9dc7a53d1234db05b4103bf0cab0f8f90e84d82c7a162c4afe4
        source_review: _compare/relationships-2026-11-16/review-current/Soliman2023
        source_status_sha256: a2957b53b29853bef8e48d0e4675a836cee52660f89ce2088d87d685526e7c55
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P3-S1-C9:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 37264b297e95b9dc7a53d1234db05b4103bf0cab0f8f90e84d82c7a162c4afe4
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: da3b1f4d6b248275a24fce4386abdecba48f5c7e2bd1da819b69123ec5bb4a9a
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S1-C9
          page: 3
          text_layer_sha256: da3b1f4d6b248275a24fce4386abdecba48f5c7e2bd1da819b69123ec5bb4a9a
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "The mean time ± SD \nfrom stroke onset to MRI scan was 3.07\
          \ ± 0.91 weeks (range: 2–4 \nweeks). \n3.2."
        anchor_text: "The mean time ± SD \nfrom stroke onset to MRI scan was 3.07\
          \ ± 0.91 weeks (range: 2–4 \nweeks). \n3.2."
        excluded_fragments: []
        image_sha256: 1e0f88b5738ade21d4878be5368b3b86f1a4762a59b7e11986eeadb3b61f5a45
        transcription: '. The mean time ± SD from stroke onset to MRI scan was 3.07
          ± 0.91 weeks (range: 2–4 weeks).


          3.2.'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 1
  quote: "Additionally, a significant correlation was found \nbetween MD of the right\
    \ AF and repetition."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-25'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
