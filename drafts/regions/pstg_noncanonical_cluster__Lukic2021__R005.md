---
id: pstg_noncanonical_cluster
name: posterior superior temporal gyrus (pSTG) cluster
kind: network
findings:
- id: f1
  target: noncanonical_sentence_processing
  target_kind: impairment
  claim: Damage to the left posterior superior temporal gyrus (pSTG) is associated
    with impaired processing of syntactically complex, noncanonical sentences across
    both production and comprehension domains, when adjusted for performance on canonical
    sentences.
  direction: likely
  relationship: correlational
  method: VLSM
  sample:
    n: 76
    population: individuals with chronic stroke-induced aphasia resulting from a single
      left hemisphere thrombo-embolic or hemorrhagic event
    phase: not_reported
    time_post_onset: chronic phase (8 to 209 months post-stroke)
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - univariate analysis
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Patient lesion overlap with the left posterior superior
    temporal gyrus (pSTG), analyzed via voxel-based lesion-symptom mapping. adjusted
    for performance on canonical sentences; analysis included covariates for age,
    months post onset, education, sex, handedness, and total lesion volume. Additional
    metadata has not been transcribed; review the pending-field flags before approval.
    PDF image reading (P3-S1-C6, two-model agreement, human verification pending):
    Participants


    Participants included 76 individuals (50 males) with stroke-induced aphasia, resulting
    from a single left hemisphere thrombo-embolic or hemorrhagic event Original text-layer
    quotation is preserved below. PDF image reading (P3-S1-C10, two-model agreement,
    human verification pending): . Months post-stroke ranged from 8 to

    209 months (M = 58.53 months; SD = 50.28) Original text-layer quotation is preserved
    below.'
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
    - proposed_concept:noncanonical_sentence_processing
  citation: '@Lukic2021'
  source_passages:
  - section: Original source P1-S2-C5
    page: 1
    quote: "Processing of syntactically complex, noncanonical (adjusted for canoni-\
      \ \ncal), sentences was associated with damage to the pSTG across domains, with\
      \ additional damage to the pMTG \nand IPL associated with impaired sentence\
      \ comprehension, suggesting that the pSTG is crucial for computing \nnoncanonical\
      \ sentences across domains and that the pMTG, and IPL are necessary for re-analysis\
      \ of thematic \nroles as required for resolution of long-distance dependencies."
    supports: claim
  - section: Original source P2-S1-C5
    page: 2
    quote: "Processing complex syntax is associ- \nated with posterior temporal lesions\
      \ across domains."
    supports: claim
  - section: Original source P8-S1-C10
    page: 8
    quote: "Finally, we observed that processing of syntactically complex, non- \n\
      canonical, sentences, when adjusted for canonical sentences, is associ- \nated\
      \ with damage to the left pSTG for both production and comprehen- \nsion, and\
      \ additionally the pMTG, AG/pSMG, parietal operculum, and the \n"
    supports: claim
  - section: Original source P3-S1-C6
    page: 3
    quote: "Participants \nParticipants included 76 individuals (50 males) with stroke-induced\
      \ \naphasia, resulting from a single left hemisphere thrombo-embolic or \nhemorrhagic\
      \ event."
    supports: sample
  - section: Original source P3-S1-C10
    page: 3
    quote: "Months post-stroke ranged from 8 to \n209 months ( M = 58.53 months; SD\
      \ = 50.28)."
    supports: sample
  - section: Original source P4-S1-C13
    page: 4
    quote: "Lastly, VLSM analyses on syntacti- \ncally complex sentences for both\
      \ production and comprehension (ad- \njusted for performance on canonical sentences)\
      \ were performed."
    supports: method
  - section: Original source P4-S1-C9
    page: 4
    quote: "Age, months post \nonset, education, sex, and handedness were included\
      \ as covariates in all \nVLSM analyses."
    supports: method
  - section: Original source P4-S1-C10
    page: 4
    quote: "The total lesion volume was automatically calculated \nfrom the lesion\
      \ masks and served as a covariate in the analysis."
    supports: method
  - section: Original source P8-S4-C7
    page: 8
    quote: "We also note that \nthese critical regions associated with each domain\
      \ were identiﬁed using \nunivariate lesion-symptom mapping analyses, and that\
      \ univariate VLSM \nin tandem with multivariate approaches (e.g., SVR-LSM) could\
      \ further \nstrengthen and conﬁrm ﬁndings from this study ( Ivanova et al.,\
      \ 2020 )."
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-24'
relationship_review:
  paper: Lukic2021
  proposal_id: R005
  review_status_sha256: f1162e7eb59aed58140f5991818de9b7c29360bf240f8c3278101ea7c035a3c1
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 5b8c766ec50e1f475662bde96048342caf0191f627957e85771f9c3ef821adaa
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 5b8c766ec50e1f475662bde96048342caf0191f627957e85771f9c3ef821adaa
        A/passages.json: c570ca7db32631eeb6c391804b605154c0a0e636c1b69af5cbad5b45139d3f0a
        A/raw.json: a3307ea074a376da6473b8e18dfa43c65298aa2430ad81682a36be1b42b8e3fc
        A/source-units.json: 8290263375e4fc5d886e7cd445ea08b012f3880ea6837d8af23f4a2b7fc37732
        A/full-source-units.json: e2bea843a5d1d8094a63b52079d4b278419ee13ad98c35ae342c9684f19ab615
        A/meta.json: 5ff5f3dc15b4a158598cc254e6849fa5c029cc15c06d5f7119c088a25b3b9bdf
        A/table-images/page-6.png: e4d79f34d0425a72133db56eb69dec73785f2c72bce51c2516f23bf17da211c2
        A/table-images/page-7.png: b061fdb5a6452af917392291f764a4504a0f3466a3c77b9d6a229a59271feb9e
        A/table-images/page-5.png: 1cd89146a52aa9e012ee5c08c52395eff4d7e0b42157e174d1e70e4fe9d835a0
        A/table-images/page-4.png: 4a040700c9b1748734ba0e91455b049eab5c28f30f033dbb18d0502209b25cbb
        A/table-images/TABLE-1-page-4-1.png: 613e1b0f0d0e06134be1f228789ec914320988ea9e88658c49a4f21059357e06
        A/table-images/TABLE-3-page-6-1.png: 57ad2bfe2eeba7286cea1436644a16e29a6953de2ae608c414e146df79debfbf
        A/table-images/manifest.json: 6edfa857a3704368fe40c495de93bd1309983291b190d9ff15d13f810c4be592
        A/table-images/TABLE-4-page-7-1.png: 9ace0a04ea0085a1b65729647e273e8757508736603ebe8eb85292f2695ffe9d
        A/table-images/TABLE-2-page-5-1.png: aa7e8f64e4e4f9242078642027b8d3e115131b84cb9196ec1216b6f1c18f8690
        A/clauses/window-03/raw.json: 8ac181503f03b842e118261e39ab1393976fc9a8dfacbcd8f31935fb1647f4f7
        A/clauses/window-03/prompt.txt: b82349a5a5532afcb28fd1bf23328391a76c5a5d4a8f7cf40b1332391faddf20
        A/clauses/window-03/meta.json: 5c493ea7e7f8e443b18713db138468941a8c60ac1f48ab5dcd98c7aeba44d64f
        A/clauses/window-04/raw.json: 3f608e49045241d6716cb8e6823a4cde2a38b9562b38c8591d910ee07ad883ef
        A/clauses/window-04/prompt.txt: 9060b1639ab343924246db207d8b13d39493e476ca481f8fecb0417465efda2c
        A/clauses/window-04/meta.json: e3a4d6e0e79ed8e84677cef29892d8b7d557bbc09a60faf676e01679c2f2b553
        A/clauses/window-05/raw.json: 8c74e4732e8cec26d58f5bc517c13861dcf1c1c24a66b4c47d214fa2b97d47b2
        A/clauses/window-05/prompt.txt: 6d0fa9b86b3bcdc88b5c8117809cbc84bed77a29805e97cc2f462f6084c9c140
        A/clauses/window-05/meta.json: 1342eb7c4de6efb7a445cc06149f110bfcad6014766562d506a921ab5f3fc67d
        A/clauses/window-02/raw.json: ff6a6b7d9b950ea529a3d6cfc24d7ce69e60f7234ceae531b090df3bddc76fa7
        A/clauses/window-02/prompt.txt: ef74cd86686930b6a0f8a7b5bfc411b7324a07b02b28f9f1a86cc0b38194fb14
        A/clauses/window-02/meta.json: 836716a39e8e0c96d4323b3b9a4a9725759778e5875d5fd875d674e143fb4800
        A/clauses/window-07/raw.json: 7818e62e7a58bebdaad31de0b2aa6f4c8b239d855c540a55b46d9dbb17c86435
        A/clauses/window-07/prompt.txt: 340ecb2ef4c4b11790e506616d4b83c667945b6246ccc7d74f334416540ed4da
        A/clauses/window-07/meta.json: ed936fbb6a6cf92fb3709c6df667e8bc369cc73af0024f8f7ea891cf64e938e9
        A/clauses/window-01/raw.json: a04f8c0029df512eba2ddef95ee2c86820c08240f057965f9af14ce337829c54
        A/clauses/window-01/prompt.txt: 6527109ebb9e35da1605cdac7cfbc42d9dfc10482c5a8f29c033fd6269140457
        A/clauses/window-01/meta.json: f78f477f21b8eb9f6fd416de8d0a396f2b0eafbe1242f41749c8c10215c6ef0e
        A/clauses/window-06/raw.json: 4f50e9f27294f9c34ac282809418660d2a842292d046c60cfd612939cc90897e
        A/clauses/window-06/prompt.txt: 4a4f1d117ef4a85735bfcc7f32b1da76f68e11effd0bba537dbdff5e864510c6
        A/clauses/window-06/meta.json: 4a5002b1416e752a36eb5bb3b2a435b556c26498e6c94145b097a383058b46d1
        A/tables/TABLE-2-page-5-2/raw.json: 1d522ec38da54956209e652cf66b62e14050fa54d7397486972311592271a6dd
        A/tables/TABLE-2-page-5-2/prompt.txt: 1e606dcc5555b1166df437b5d43489751c9fc436abc95c391b88662072c9bd3e
        A/tables/TABLE-2-page-5-2/meta.json: de87d59b848293435bc91a918e438c1f53abb268488e50759c3193d6acd81727
        A/tables/TABLE-3-page-6-3/raw.json: 946a0bcdd1f1733efa31a119320354a154e0d751aef448aba9200fbace190b3d
        A/tables/TABLE-3-page-6-3/prompt.txt: fd710f2f3ea85c142ed226933ec3dc4e7a747a0fb8301635800cd3860ef20b4a
        A/tables/TABLE-3-page-6-3/meta.json: d5d95a42cc627362cb801f96b15b389da71036a1c0d789a5c443fdb7306945c0
        A/tables/TABLE-4-page-7-4/raw.json: dd6a96ae37e2f0be63b9a6c8c9955339179306272030f437d456da9a04af20a2
        A/tables/TABLE-4-page-7-4/prompt.txt: d1cc0bd528fb4ff962327871ad581cd0e311fb21034aa108d1b5b1f163e0d41d
        A/tables/TABLE-4-page-7-4/meta.json: 1ef60509235f6d99c45e16b09eb9dacb3db9b03d84e93d03aa638826307c25ba
        A/tables/TABLE-1-page-4-1/raw.json: 635e2b870f5feb974e5c60d32cb7074b37aaf2f92f0b81c77b3f4d96cf77b948
        A/tables/TABLE-1-page-4-1/prompt.txt: e1df3a5da3048a62a18686a2d4d47e640b5581ec78a1ed06d2d69b27a0724d0f
        A/tables/TABLE-1-page-4-1/meta.json: 430aba10c4b5ffa54c77ca6ab906a85affc10ee8a8549cd16a2c5b4f9d9ff666
        B/passages.json: c570ca7db32631eeb6c391804b605154c0a0e636c1b69af5cbad5b45139d3f0a
        B/raw.json: 5eaad2c788fe4822a038e52c7cf129186fc5476337d700b4bdefeb52c57be846
        B/source-units.json: 8290263375e4fc5d886e7cd445ea08b012f3880ea6837d8af23f4a2b7fc37732
        B/full-source-units.json: e2bea843a5d1d8094a63b52079d4b278419ee13ad98c35ae342c9684f19ab615
        B/meta.json: 0a800b0061687fc65e8599f3f25a3389eed28f04e4f7638ccebb122ccbf05a1b
        B/table-images/page-6.png: e4d79f34d0425a72133db56eb69dec73785f2c72bce51c2516f23bf17da211c2
        B/table-images/page-7.png: b061fdb5a6452af917392291f764a4504a0f3466a3c77b9d6a229a59271feb9e
        B/table-images/page-5.png: 1cd89146a52aa9e012ee5c08c52395eff4d7e0b42157e174d1e70e4fe9d835a0
        B/table-images/page-4.png: 4a040700c9b1748734ba0e91455b049eab5c28f30f033dbb18d0502209b25cbb
        B/table-images/TABLE-1-page-4-1.png: 613e1b0f0d0e06134be1f228789ec914320988ea9e88658c49a4f21059357e06
        B/table-images/TABLE-3-page-6-1.png: 57ad2bfe2eeba7286cea1436644a16e29a6953de2ae608c414e146df79debfbf
        B/table-images/manifest.json: ac7da0112ee520bf49d410a8974e865ea65e44bf19e74627efe53d4f4c8cc9b9
        B/table-images/TABLE-4-page-7-1.png: 9ace0a04ea0085a1b65729647e273e8757508736603ebe8eb85292f2695ffe9d
        B/table-images/TABLE-2-page-5-1.png: aa7e8f64e4e4f9242078642027b8d3e115131b84cb9196ec1216b6f1c18f8690
        B/clauses/window-03/raw.json: 0199982327d4779537ab1f1b9f5c88cba33165fe1d7765dc87404da998158400
        B/clauses/window-03/prompt.txt: b82349a5a5532afcb28fd1bf23328391a76c5a5d4a8f7cf40b1332391faddf20
        B/clauses/window-03/meta.json: e768cbb4c9ede26f1fdb2ff4379668ec5d7d55c5bcd21bfef1cd828476eb02bb
        B/clauses/window-04/raw.json: 1a93390abef359fd461e31b75631883113aa6e09a15eb4d148a1f31df5119b21
        B/clauses/window-04/prompt.txt: 9060b1639ab343924246db207d8b13d39493e476ca481f8fecb0417465efda2c
        B/clauses/window-04/meta.json: 84370cbd39241e6e4fc5fb8a3a0410f89d44d77047fd793fb163c558ce6ad48b
        B/clauses/window-05/raw.json: fc1e2e915c2bd7f06bf952b6eb6b03a16b56b99f8feefe0b187b10bde37db223
        B/clauses/window-05/prompt.txt: 6d0fa9b86b3bcdc88b5c8117809cbc84bed77a29805e97cc2f462f6084c9c140
        B/clauses/window-05/meta.json: 9bd0084568db53632645f8f6d83fbb7ed6d4f6d3b70dd956fb420d2f2b426bb8
        B/clauses/window-02/raw.json: c19f56a7de0c8f75bc5dea8578f8d94ded9014b679313cc2a31efe192bea8a53
        B/clauses/window-02/prompt.txt: ef74cd86686930b6a0f8a7b5bfc411b7324a07b02b28f9f1a86cc0b38194fb14
        B/clauses/window-02/meta.json: f66475dfe778c12177d72b0e5742e61de7d1a64f0f8b76525e5926ab62127726
        B/clauses/window-07/raw.json: 8c3fefc74efef3af618602e5b2939298ce2e5c0d595c4dca60eba244eef814eb
        B/clauses/window-07/prompt.txt: 340ecb2ef4c4b11790e506616d4b83c667945b6246ccc7d74f334416540ed4da
        B/clauses/window-07/meta.json: 4b0bbcf3d2cfd6656b63fe0df35303c89b3d4925d6067ef01bf7a85ab9746963
        B/clauses/window-01/raw.json: 2e507cedd393f1b20f093802d2d0645618fb8179cebdf19e81fd899808513cd6
        B/clauses/window-01/prompt.txt: 6527109ebb9e35da1605cdac7cfbc42d9dfc10482c5a8f29c033fd6269140457
        B/clauses/window-01/meta.json: a5cbcd81de1f81d46e60e656e88505cfd7eaf88997e85ce16715a6cf6b428111
        B/clauses/window-06/raw.json: 1c0eac4dcb1a8ee859e88d80ba7aa1a908f7f3aef9a14dc192bc725bcd05f014
        B/clauses/window-06/prompt.txt: 4a4f1d117ef4a85735bfcc7f32b1da76f68e11effd0bba537dbdff5e864510c6
        B/clauses/window-06/meta.json: e3df210b8c2a383b236ff841e46e138715556f8d45a0b2581dad3b64ad9229ac
        B/tables/TABLE-2-page-5-2/raw.json: 6963e4adfd048e07b074f45d72f04d2d9281c910a338556434a94b24fe5964d6
        B/tables/TABLE-2-page-5-2/prompt.txt: 1e606dcc5555b1166df437b5d43489751c9fc436abc95c391b88662072c9bd3e
        B/tables/TABLE-2-page-5-2/meta.json: 8364cacb868647e786a09c423689e516b55ba24aa1cb895ea735442ba993935c
        B/tables/TABLE-3-page-6-3/raw.json: 4b0eb646eb3d67bb4ddd23f1a0c1a6054e9626af8b525f7965a46ef34702a7cf
        B/tables/TABLE-3-page-6-3/prompt.txt: fd710f2f3ea85c142ed226933ec3dc4e7a747a0fb8301635800cd3860ef20b4a
        B/tables/TABLE-3-page-6-3/meta.json: e994d5c098a63293e106f19adf859a236af5d2f6b0e8caf7e34bc4bd0d3031a1
        B/tables/TABLE-4-page-7-4/raw.json: 723b48e13c51b7e3a69420d765fbf6d4905c83940f31cafd52e59f204eb4ab9a
        B/tables/TABLE-4-page-7-4/prompt.txt: d1cc0bd528fb4ff962327871ad581cd0e311fb21034aa108d1b5b1f163e0d41d
        B/tables/TABLE-4-page-7-4/meta.json: 263931a7f432895d8bb162d511e23788ac9093ff0ce0b8796a026505d488908d
        B/tables/TABLE-1-page-4-1/raw.json: 635e2b870f5feb974e5c60d32cb7074b37aaf2f92f0b81c77b3f4d96cf77b948
        B/tables/TABLE-1-page-4-1/prompt.txt: e1df3a5da3048a62a18686a2d4d47e640b5581ec78a1ed06d2d69b27a0724d0f
        B/tables/TABLE-1-page-4-1/meta.json: b795b348ea398f452a643a72fdd431e5ef2844b24778c41fa93d928b6256b893
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
      pdf_sha256: 5b8c766ec50e1f475662bde96048342caf0191f627957e85771f9c3ef821adaa
      source_review: _compare/relationships-2026-11-16/review-current/Lukic2021
      source_status_sha256: c336e3ed1acefcf9518fa372a40f2c30990f03e97803df80bab035471cd821c8
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R005
    exposure:
      text: left hemisphere lesions
    outcome:
      text: noncanonical sentence processing (across domains)
    analysis_label: VLSM (adjusted for canonical sentences)
    relation: association
    evidence_ids:
    - P1-S2-C5
    - P2-S1-C5
    - P8-S1-C10
    qualifier_ids:
    - P4-S1-C13
    - P5-S2-C3
    - P6-S1-C9
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 5b8c766ec50e1f475662bde96048342caf0191f627957e85771f9c3ef821adaa
      source_review: _compare/relationships-2026-11-16/review-current/Lukic2021
      source_status_sha256: c336e3ed1acefcf9518fa372a40f2c30990f03e97803df80bab035471cd821c8
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P1-S3-C3
      - Result passage disposed without unit P2-S1-C4
      - Result passage disposed without unit P2-S1-C5
      - Result passage disposed without unit P4-S2-C4
      - Result passage disposed without unit P4-S2-C13
      - Accounting without a linked unit P4-S3-C3
      - Accounting without a linked unit P4-S3-C4
      - Result passage disposed without unit P4-S3-C5
      - Accounting without a linked unit P4-S3-C7
      - Unresolved source passage P4-S3-C8
      - Unaccounted source passage P4-S3-C3
      - Unaccounted source passage P4-S3-C4
      - Unaccounted source passage P4-S3-C7
      - Result passage disposed without unit P5-S2-C9
      - Result passage disposed without unit P6-S2-C3
      - Accounting without a linked unit P8-S1-C10
      - Accounting without a linked unit P8-S1-C7
      - Accounting without a linked unit P8-S2-C1
      - Accounting without a linked unit P8-S2-C5
      - Accounting without a linked unit P8-S2-C8
      - Accounting without a linked unit P8-S3-C1
      - Unaccounted source passage P8-S1-C7
      - Unaccounted source passage P8-S2-C5
      - Unaccounted source passage P8-S2-C8
      - Unaccounted source passage P8-S1-C10
      - Unaccounted source passage P8-S2-C1
      - Unaccounted source passage P8-S3-C1
      - Result passage disposed without unit P8-S4-C4
      - Result passage disposed without unit P8-S4-C5
      - Result passage disposed without unit P8-S4-C9
      - Result passage disposed without unit P8-S5-C2
      - Result passage disposed without unit P8-S5-C4
      unattached_null_or_qualifier_ids: []
      suppressed_nonrepresented_units: 7
      default_disposition_count_requires_completeness_check: 140
      unselected_timing_passages:
      - P1-S1-C5
      - P3-S1-C9
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P5-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C12
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C13
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P4-S1-C14
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: adjustment_roles
        source_ids:
        - P4-S1-C9
        - P4-S1-C10
        - P4-S1-C11
        - P4-S1-C12
        - P4-S1-C13
        - P5-S1-C4
        - P5-S1-C8
        - P5-S1-C9
        - P5-S1-C10
        - P5-S1-C11
        - P6-S1-C12
        - P6-S1-C13
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - validation
      - personal_factors
      - tested_personal_effects
      - adjustment_roles
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-4-1
      - TABLE-2-page-5-2
      - TABLE-3-page-6-3
      - TABLE-4-page-7-4
      unlinked_tables:
      - TABLE-1-page-4-1
      - TABLE-2-page-5-2
      - TABLE-3-page-6-3
      - TABLE-4-page-7-4
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P3-S2
        - P4-S1
        - P4-S2
        - P4-S3
        - P5-S2
        - P6-S1
        - P7-S1
        - P8-S1
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 5b8c766ec50e1f475662bde96048342caf0191f627957e85771f9c3ef821adaa
      source_review: _compare/relationships-2026-11-16/review-current/Lukic2021
      source_status_sha256: c336e3ed1acefcf9518fa372a40f2c30990f03e97803df80bab035471cd821c8
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C6
      disposition: represented
      result_indexes:
      - 0
      reason: Supports shared regions across domains.
    - source_id: P1-S2-C2
      disposition: represented
      result_indexes:
      - 0
      reason: Supports shared regions across domains.
    - source_id: P1-S2-C3
      disposition: represented
      result_indexes:
      - 1
      reason: Supports comprehension-specific lesions.
    - source_id: P1-S2-C4
      disposition: represented
      result_indexes:
      - 2
      - 3
      reason: Supports critical regions for production vs comprehension.
    - source_id: P1-S2-C5
      disposition: represented
      result_indexes:
      - 4
      - 5
      reason: Supports noncanonical sentence processing associations.
    - source_id: P2-S1-C4
      disposition: repeated
      result_indexes:
      - 2
      - 3
      reason: Restatement of production/comprehension deficits.
    - source_id: P2-S1-C5
      disposition: represented
      result_indexes:
      - 4
      reason: Supports complex syntax association with posterior temporal lesions.
    - source_id: P3-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Demographic comparison between sites.
    - source_id: P3-S1-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Demographic comparison of time post-stroke.
    - source_id: P3-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Demographic comparison of severity between sites.
    - source_id: P4-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of VLSM permutation tests.
    - source_id: P4-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to Table 1.
    - source_id: P4-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive statistics for SPPT.
    - source_id: P4-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive mean performance for canonical vs noncanonical production.
    - source_id: P4-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive statistics for SCT.
    - source_id: P4-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive mean performance for canonical vs noncanonical comprehension.
    - source_id: P4-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive statistics for verb processing.
    - source_id: P4-S2-C10
      disposition: represented
      result_indexes:
      - 8
      reason: Logistic regression on production vs comprehension impairment.
    - source_id: P4-S2-C11
      disposition: represented
      result_indexes:
      - 9
      reason: Logistic regression on canonicity impairment.
    - source_id: P4-S2-C12
      disposition: represented
      result_indexes:
      - 10
      reason: Logistic regression on verb production vs comprehension.
    - source_id: P4-S3-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of lesion overlap map.
    - source_id: P4-S3-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of lesion volume by region.
    - source_id: P4-S3-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to Table 2.
    - source_id: P4-S3-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to Figure 2.
    - source_id: P4-S3-C7
      disposition: represented
      result_indexes:
      - 0
      reason: Supports shared regions for production and comprehension.
    - source_id: P4-S3-C8
      disposition: represented
      result_indexes:
      - 1
      reason: Supports comprehension-specific damage.
    - source_id: P5-S1-C11
      disposition: represented
      result_indexes:
      - 1
      reason: Supports comprehension-specific damage.
    - source_id: P5-S1-C12
      disposition: represented
      result_indexes:
      - 3
      reason: Supports comprehension over production association.
    - source_id: P5-S1-C13
      disposition: represented
      result_indexes:
      - 2
      reason: Supports production over comprehension association.
    - source_id: P5-S2-C1
      disposition: represented
      result_indexes:
      - 3
      reason: Supports comprehension over production association.
    - source_id: P5-S2-C2
      disposition: represented
      result_indexes:
      - 2
      reason: Supports production over comprehension association.
    - source_id: P5-S2-C3
      disposition: represented
      result_indexes:
      - 5
      reason: Supports noncanonical comprehension association.
    - source_id: P5-S2-C4
      disposition: represented
      result_indexes:
      - 6
      reason: Supports noncanonical production trend.
    - source_id: P5-S2-C9
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of shared regions.
    - source_id: P5-S2-C10
      disposition: represented
      result_indexes:
      - 0
      reason: Supports shared regions for production and comprehension.
    - source_id: P6-S2-C3
      disposition: repeated
      result_indexes:
      - 2
      - 3
      reason: Restatement of distinct neural correlates.
    - source_id: P6-S2-C4
      disposition: represented
      result_indexes:
      - 2
      reason: Supports production-specific regions.
    - source_id: P6-S2-C6
      disposition: represented
      result_indexes:
      - 3
      reason: Supports comprehension-specific regions.
    - source_id: P8-S1-C4
      disposition: repeated
      result_indexes:
      - 2
      reason: Restatement of lack of IPL role in production.
    - source_id: P8-S1-C7
      disposition: represented
      result_indexes:
      - 7
      reason: Null effect of frontal lesions.
    - source_id: P8-S1-C10
      disposition: represented
      result_indexes:
      - 4
      - 5
      reason: Supports noncanonical processing associations.
    - source_id: P8-S2-C1
      disposition: represented
      result_indexes:
      - 5
      reason: Supports noncanonical comprehension association.
    - source_id: P8-S2-C5
      disposition: represented
      result_indexes:
      - 5
      reason: Supports noncanonical comprehension association.
    - source_id: P8-S3-C1
      disposition: repeated
      result_indexes:
      - 7
      reason: Restatement of IFG null effect.
    - source_id: P8-S4-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of statistical power in frontal regions.
    - source_id: P8-S4-C5
      disposition: repeated
      result_indexes:
      - 7
      reason: Restatement of IFG null effect.
    - source_id: P8-S5-C2
      disposition: represented
      result_indexes:
      - 7
      reason: Null effect of IFG on sentence processing.
    unresolved_coverage:
    - source_id: P4-S3-C6
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P5-S2-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P1-S3-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P4-S2-C13
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S2-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S3-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S4-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S5-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C6
    - P1-S3-C3
    - P2-S1-C4
    - P3-S1-C12
    - P3-S1-C13
    - P3-S2-C2
    - P4-S1-C8
    - P4-S2-C4
    - P4-S2-C5
    - P4-S2-C6
    - P4-S2-C7
    - P4-S2-C8
    - P4-S2-C9
    - P4-S2-C13
    - P4-S3-C3
    - P4-S3-C4
    - P4-S3-C5
    - P4-S3-C8
    - P5-S1-C12
    - P5-S1-C13
    - P5-S2-C9
    - P6-S2-C3
    - P8-S1-C4
    - P8-S2-C8
    - P8-S3-C1
    - P8-S3-C7
    - P8-S4-C4
    - P8-S4-C5
    - P8-S4-C9
    - P8-S5-C4
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-4-1
    - TABLE-2-page-5-2
    - TABLE-3-page-6-3
    - TABLE-4-page-7-4
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P3-S1-C6
      recruited_sample:
      - P3-S1-C7
      eligibility:
      - P3-S1-C6
      imaging_provenance:
      - P3-S3-C5
      - P3-S3-C6
      imaging_timing:
      - P3-S1-C10
      outcome_timing:
      - P3-S1-C10
      outcome_definition:
      - P3-S2-C4
      - P3-S2-C5
      - P3-S2-C6
      - P3-S2-C7
      - P3-S2-C8
      - P4-S1-C5
      validation: []
      analysis_restrictions:
      - P4-S1-C11
      - P4-S1-C12
      - P4-S1-C13
      dependent_variable_statement:
      - P4-S1-C11
      - P4-S1-C12
      - P4-S1-C13
      limitations:
      - P8-S1-C8
      - P8-S4-C4
      - P8-S4-C5
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles: []
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P3-S1-C9
      - P3-S1-C10
      - P3-S1-C11
      - P3-S1-C12
      - P3-S1-C13
      - P3-S1-C15
      - P3-S2-C1
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P5-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C12
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C13
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P4-S1-C14
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: adjustment_roles
      source_ids:
      - P4-S1-C9
      - P4-S1-C10
      - P4-S1-C11
      - P4-S1-C12
      - P4-S1-C13
      - P5-S1-C4
      - P5-S1-C8
      - P5-S1-C9
      - P5-S1-C10
      - P5-S1-C11
      - P6-S1-C12
      - P6-S1-C13
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
      pdf_sha256: 5b8c766ec50e1f475662bde96048342caf0191f627957e85771f9c3ef821adaa
      review_sha256: f1162e7eb59aed58140f5991818de9b7c29360bf240f8c3278101ea7c035a3c1
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
      - P2-S1-C5
      - P8-S1-C10
      source_result: VLSM analysis of syntactically complex, noncanonical sentences
        (adjusted for canonical sentences) revealed that damage to the left posterior
        superior temporal gyrus (pSTG) was associated with impaired processing across
        both production and comprehension domains. Additional regions (pMTG, AG/pSMG,
        parietal operculum, insula) were associated with comprehension specifically.
      result_status: detected
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis corresponds to the VLSM of noncanonical sentence
            performance adjusted for canonical sentence performance, as described
            in P4-S1-C13 and P8-S1-C10. The draft correctly identifies this specific
            model.
          source_ids:
          - P4-S1-C13
          - P8-S1-C10
        direction:
          answer: fits
          reason: The source states that damage to pSTG is associated with processing
            of noncanonical sentences (implied impairment given the context of lesion-symptom
            mapping and 'impaired' in P1-S2-C5). The draft claims 'associated with
            impaired processing', which preserves the direction of the detected association.
          source_ids:
          - P1-S2-C5
          - P8-S1-C10
        construct:
          answer: fits
          reason: Exposure is left hemisphere lesions (specifically pSTG), outcome
            is noncanonical sentence processing (production and comprehension). The
            method is VLSM. The patient measurement is correctly identified as template_lesion_overlap
            (lesion masks overlaid on template space), not patient_diffusion.
          source_ids:
          - P3-S4-C8
          - P3-S4-C9
          - P4-S1-C13
        qualifications:
          answer: fits
          reason: The draft includes the critical qualification 'adjusted for performance
            on canonical sentences' and lists the standard covariates (age, time post-stroke,
            etc.) which are stated in P4-S1-C9. It also notes the univariate nature
            of the analysis as a limitation.
          source_ids:
          - P4-S1-C13
          - P4-S1-C9
          - P8-S4-C7
        missing_material_caveat:
          answer: fits
          reason: 'The draft captures the main caveats: the adjustment for canonical
            sentences and the univariate method limitation. It does not omit material
            caveats that would change the interpretation of the pSTG finding for noncanonical
            sentences.'
          source_ids:
          - P8-S4-C7
          - P4-S1-C13
      optional_pending:
      - Specific p-values or cluster sizes for the pSTG cluster in the noncanonical
        analysis are not transcribed in the draft, but the qualitative association
        is clear from the text.
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Specific p-values or cluster sizes for the pSTG cluster in the noncanonical
      analysis are not transcribed in the draft, but the qualitative association is
      clear from the text.
    normalizations: []
    analysis_identity:
      id: R005
      exposure:
        text: left hemisphere lesions
      outcome:
        text: noncanonical sentence processing (across domains)
      analysis_label: VLSM (adjusted for canonical sentences)
      relation: association
      evidence_ids:
      - P1-S2-C5
      - P2-S1-C5
      - P8-S1-C10
      qualifier_ids:
      - P4-S1-C13
      - P5-S2-C3
      - P6-S1-C9
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 5b8c766ec50e1f475662bde96048342caf0191f627957e85771f9c3ef821adaa
        source_review: _compare/relationships-2026-11-16/review-current/Lukic2021
        source_status_sha256: c336e3ed1acefcf9518fa372a40f2c30990f03e97803df80bab035471cd821c8
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P3-S1-C6:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 5b8c766ec50e1f475662bde96048342caf0191f627957e85771f9c3ef821adaa
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 6db90d8efe8d5a70da1f07adea1233ab75a16fc7ec67968910ea1e2b7b06680f
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S1-C6
          page: 3
          text_layer_sha256: 6db90d8efe8d5a70da1f07adea1233ab75a16fc7ec67968910ea1e2b7b06680f
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "Participants \nParticipants included 76 individuals (50 males)\
          \ with stroke-induced \naphasia, resulting from a single left hemisphere\
          \ thrombo-embolic or \nhemorrhagic event."
        anchor_text: "Participants \nParticipants included 76 individuals (50 males)\
          \ with stroke-induced \naphasia, resulting from a single left hemisphere\
          \ thrombo-embolic or \nhemorrhagic event."
        excluded_fragments: []
        image_sha256: 23dacc2b3e76173ce8140e61577337c3a5e551364850f0f36642944973107336
        transcription: 'Participants


          Participants included 76 individuals (50 males) with stroke-induced aphasia,
          resulting from a single left hemisphere thrombo-embolic or hemorrhagic event'
      P3-S1-C10:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 5b8c766ec50e1f475662bde96048342caf0191f627957e85771f9c3ef821adaa
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 64cd39d41df9c54805d0b16676f67645a9e4e177951c44ceb5acbf91432645f2
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S1-C10
          page: 3
          text_layer_sha256: 64cd39d41df9c54805d0b16676f67645a9e4e177951c44ceb5acbf91432645f2
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "Months post-stroke ranged from 8 to \n209 months ( M = 58.53\
          \ months; SD = 50.28)."
        anchor_text: "Months post-stroke ranged from 8 to \n209 months ( M = 58.53\
          \ months; SD = 50.28)."
        excluded_fragments: []
        image_sha256: efe0f4aa3b2ef7499bb866dc242175f9669578b5e2566042e8dd68ed4ac66928
        transcription: '. Months post-stroke ranged from 8 to

          209 months (M = 58.53 months; SD = 50.28)'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 1
  quote: "Processing of syntactically complex, noncanonical (adjusted for canoni-\
    \ \ncal), sentences was associated with damage to the pSTG across domains, with\
    \ additional damage to the pMTG \nand IPL associated with impaired sentence comprehension,\
    \ suggesting that the pSTG is crucial for computing \nnoncanonical sentences across\
    \ domains and that the pMTG, and IPL are necessary for re-analysis of thematic\
    \ \nroles as required for resolution of long-distance dependencies."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-24'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
