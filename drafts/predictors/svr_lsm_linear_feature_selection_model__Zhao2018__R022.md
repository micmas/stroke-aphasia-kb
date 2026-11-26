---
id: svr_lsm_linear_feature_selection_model
name: Linear SVR-LSM model with feature selection
kind: predictor
findings:
- id: f1
  target: moca_score
  target_kind: impairment
  claim: The linear SVR-LSM model with feature selection outperformed nonlinear and
    linear models without feature selection in predicting MoCA scores.
  direction: likely
  relationship: correlational
  method: MVPA
  sample:
    n: 410
    population: acute ischemic stroke patients
    phase: not_reported
    time_post_onset: cognitive assessment performed three to six months after stroke
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Findings may not be generalizable to patients with large cerebral infarcts due
    to a high proportion of small infarcts in the cohort (median volume 2.3 ml)
  - Global cognitive functioning was assessed using MoCA rather than detailed neuropsychological
    testing
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: A linear support vector regression-based lesion-symptom
    mapping model that incorporates feature selection to exclude noise voxels prior
    to training on patient lesion maps. Model performance was compared across four
    configurations: nonlinear and linear SVR-LSM, both with and without feature selection;
    The model was trained and tested on the same data. Additional metadata has not
    been transcribed; review the pending-field flags before approval. PDF image reading
    (P2-S2-C5, two-model agreement, human verification pending): . Finally, 410 patients
    were included in this study

    (See Supplementary Figure S1, the flow-chart of the

    patient recruitment) Original text-layer quotation is preserved below. PDF image
    reading (P11-S2-C9, two-model agreement, human verification pending): . It should
    be noted

    that we included many patients with relatively small

    infarcts (median volume 2.3 ml), which may in part be

    due to some of the exclusion criteria of the CU-STRIDE

    cohort (e.g. patients who died before assessment of who

    were incommunicable were not included) Original text-layer quotation is preserved
    below.'
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
    - proposed_concept:moca_score
  citation: '@Zhao2018'
  source_passages:
  - section: Original source P11-S2-C3
    page: 11
    quote: 'As can be appreciated from the results

      and information in the online supplementary materials,

      the linear model with feature selection outperformed

      the other models, which is why this model was selected

      for the current study in statistical inference (See

      Supplementary Method for more details).'
    supports: claim
  - section: Original source P11-S2-C2
    page: 11
    quote: 'Then we selected four candidate SVR-LSM

      models (nonlinear and linear SVR-LSM with and with-

      out feature selection) and compared their prediction

      performance and reproducibility on the same training

      and testing data.'
    supports: method
  - section: Original source P2-S2-C5
    page: 2
    quote: 'Finally, 410 patients were included in this study

      (See Supplementary Figure S1, the ﬂow-chart of the

      patient recruitment).'
    supports: sample
  - section: Original source P1-S1-C4
    page: 1
    quote: 'Montreal Cognitive Assessment at three to six months after stroke was
      used to assess

      global cognitive functioning and cognitive domains (memory, language, attention,
      executive and visuospatial function).'
    supports: method
  - section: Original source P11-S2-C9
    page: 11
    quote: 'It should be noted

      that we included many patients with relatively small

      infarcts (median volume 2.3 ml), which may in part be

      due to some of the exclusion criteria of the CU-STRIDE

      cohort (e.g. patients who died before assessment of who

      were incommunicable were not included).'
    supports: limitation
  - section: Original source P11-S3-C4
    page: 11
    quote: 'Second, we used the

      MoCA instead of detailed neuropsychological testing

      to assess global cognitive functioning and cognitive

      domains performance.'
    supports: limitation
predictor_type: imaging_metric
short_definition: A linear support vector regression-based lesion-symptom mapping
  model that incorporates feature selection to exclude noise voxels prior to training
  on patient lesion maps.
assessment:
- Montreal Cognitive Assessment (MoCA)
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-26'
relationship_review:
  paper: Zhao2018
  proposal_id: R022
  review_status_sha256: 6247b650f0e01031fee72f5d4a825b2941d43b1449bd8583fada283122828995
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: e6ff8e77b0302d8bbde76970bf8372c5669188243c84c97db9eaf98aaed77f98
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: e6ff8e77b0302d8bbde76970bf8372c5669188243c84c97db9eaf98aaed77f98
        A/passages.json: b444fb9aa75fb0115caff4c239d17092c5419db134a2d51347ed83761a73eebc
        A/raw.json: ec8ad080ae73d0c9ca16f394622c027eb6bba12703d1fdec490a6f4fa09ec9eb
        A/source-units.json: 276dfea357609afe4d3be173eb6c72b429db6e04dd76d2793a3995a2f51a23f4
        A/full-source-units.json: 1c65cbd13d47e62b5078bfa5d85826069b263b4d0ff059b575d457e3e145a74a
        A/meta.json: 979dd475f405b1ba0c55201876f9f1f2094d0721a52c33337a72658dfdc6ae00
        A/table-images/TABLE-S4-page-4-1.png: 36c558a22264c6973e867c344188ceb1d0249c8a783b08228989b7969f93f368
        A/table-images/TABLE-4-page-10-1.png: a87f07c3f4752233617b7ecf81385279c9316b9a04314ac9d28f1394d2f6ee6d
        A/table-images/page-10.png: dc4bc44a6532c38f7f58b139f835f12682de84d6249b0e8c43bfdac5b9c756ec
        A/table-images/TABLE-3-page-8-1.png: 93e3f3b6903611da94a5599d2da0c237c3f3d6bd1806916ce0f0e4ce94222d48
        A/table-images/page-7.png: 39397264f289b34919530ae60a946c19d6123785041fa980c602779aa183c106
        A/table-images/TABLE-1-page-4-2.png: fe0507a1056edc32500efd761aa5b0c0418fa07a2340cce4527751e6f6f68cf7
        A/table-images/page-4.png: 0b8f22d26d53258d45dbd65afa47acbfcd49b7c701f46b7dd64ae17e6698c098
        A/table-images/page-8.png: 77ad8c707a2b67da54b8cfa67bdce9206a2a444d856a9fc279d28b19388dec12
        A/table-images/manifest.json: 51c7f4b65297a2e5e38b677463978a437f278d71b46e52a8847121206ed9c2f2
        A/table-images/TABLE-2-page-7-1.png: 11b0270dcb5a31da5d030214d97f2644a34fda91bcf17cfe8016ee9ad6b777bb
        A/clauses/window-03/raw.json: 12e83a54131af435e9e2e608c5cc253c32191626376a190d4eaef425a7489149
        A/clauses/window-03/prompt.txt: 7b81812744d2ab4b932042992af72d6661b7ea5a0d79b3d30c5e436a1e68bfd2
        A/clauses/window-03/meta.json: 2dee005f459b95bc67443fad32e0180121d0c5ac81a3a22b085b73f8a68843f8
        A/clauses/window-04/raw.json: 9b8351d7ce7b30c7f5b4d767e814df47ed5ced26e30fdfe2ca225d527ab9a011
        A/clauses/window-04/prompt.txt: e09c2ae43e05a6e5d422064092049a7c762f557efd6ae78583c6756bd3122330
        A/clauses/window-04/meta.json: 5dba7afa571a1674abd73e04843930beb95fb766aa60d27f9c617cf5f205fe80
        A/clauses/window-05/raw.json: a5a29fb609ebd56f46c961f3a7d48c4138758dc17b3cd77dd0880fd3a18d504f
        A/clauses/window-05/prompt.txt: 9d9d54ed48c5cff45ba35a7874c174766d2790c729bf078fb7e213309ec34112
        A/clauses/window-05/meta.json: e74eb7d1fea88456db96bbe37b4d4edfae97c0dcd5b866e8b3b7fb6c253b6fa0
        A/clauses/window-02/raw.json: b4896162ba3540f1905effd3d7504d59462ad5c613cc275b397b6c24df2efaf0
        A/clauses/window-02/prompt.txt: d6e95125f81b6be64e45f92b3cb0580a38ddd31b52ff70a371751746b48d9b15
        A/clauses/window-02/meta.json: f6116cebddc2a57f6b0d049a54e13a7aa035b4294ef298e4596c207172472926
        A/clauses/window-07/raw.json: 79ed5a869c7126fd96c3b1d9840578feae1dba24705aed0744b9edc2fda86a85
        A/clauses/window-07/prompt.txt: d7992fe5bde7363aa90b112b836427c0b1cd561bb9fac9be4a478e8008ecd388
        A/clauses/window-07/meta.json: fed47c3ab8236f9bb55ae16aedb55310de68a28410dd00b8f7966a8a3d0c31f6
        A/clauses/window-01/raw.json: 6cd694b95586fb1856a30ac2585163f758fc3954aa426e2261b06c3e69a56445
        A/clauses/window-01/prompt.txt: afc9452689c6602004d820b6f6dd6a7cf834c55bedabc76066047c6f7a45714a
        A/clauses/window-01/meta.json: cc8503fb48d6caf620d0798daf54f620c58aac785e5505e29a1fc934e27d9b51
        A/clauses/window-06/raw.json: 39ac45569ced1b1a09abeed1282e2e2aacf407f2e95b3d309c8e8418b847e8bf
        A/clauses/window-06/prompt.txt: 5e197b4e9485960e7f1652894c7c899d609635a19dea7b695c0ff9b241812a8a
        A/clauses/window-06/meta.json: 77ae62982d5bfafbd80d0b59fd22aa5c86a1082a48e68f9b400dd0260f5197bf
        A/tables/TABLE-1-page-4-2/raw.json: 58dbf2a3f129a441476acba1dd2e2464da36e86acac74e62f60de2debe4b40f3
        A/tables/TABLE-1-page-4-2/prompt.txt: b1c3795a2dcd0b06a2a87f6c973f560dc2ee687c7b51866879ed5f91b68e9440
        A/tables/TABLE-1-page-4-2/meta.json: 0125f6ed748e1eff38b050d0bf11626ec52636c19acb11944cb2bcd5cdda25d6
        A/tables/TABLE-3-page-8-4/raw.json: f8ac90358ef882399c7301047d831dbd5bc355d27a32b9bb28095ed9f0cc7b17
        A/tables/TABLE-3-page-8-4/prompt.txt: eb858d27102e5be60eb9fd5ed0719f6a1676b7e6c9995c57d8785c8d4d85d544
        A/tables/TABLE-3-page-8-4/meta.json: 32beb2d4221b5676af6281bbf05c24ec57bffc44a280e261a6e86f2a6389461d
        A/tables/TABLE-2-page-7-3/raw.json: b310c14bdd24a353e69e850197400126982ea281a5888032f090ef16216c0299
        A/tables/TABLE-2-page-7-3/prompt.txt: 4cb613a1660b3e3e2de328f2edefe639f61494eab5c108083c1203b9794ff75f
        A/tables/TABLE-2-page-7-3/meta.json: 970d0f4f20f4129eb1288a93a32e27111d0cc48683b28cd2e150eaaa6bf4446b
        A/tables/TABLE-S4-page-4-1/raw.json: d5d53a94b1479430d3a8af6e5255d7aaa5ae4b4d5bbee02c2700fcb5aceba893
        A/tables/TABLE-S4-page-4-1/prompt.txt: 17258ea2306d1e4f49b2edcc4f21c9e8caf000f11bbd35054bbd7a104195bc3e
        A/tables/TABLE-S4-page-4-1/meta.json: 0005b2e2506d3d2fc044e4ba7fb40e50ee24094008f054e254474d817329b1ff
        A/tables/TABLE-4-page-10-5/raw.json: 52b14cd0e078609deb9b72ab3cae6a991e8ba2c7c69abba544a9dfc57523ccf5
        A/tables/TABLE-4-page-10-5/prompt.txt: f7198c96a2a1c138995dbd828c58bea4c1520e298cf019ddc71173d1e81899ec
        A/tables/TABLE-4-page-10-5/meta.json: 8a387fbcc14c98e8a2aec60534d1e23ddb9f274e98d4ffab15d849dfbc6657d2
        B/passages.json: b444fb9aa75fb0115caff4c239d17092c5419db134a2d51347ed83761a73eebc
        B/raw.json: 47b4c0cedc1c3e394ae420a24f5a5e954cfa01737dc6f34852a8edad89c41017
        B/source-units.json: 276dfea357609afe4d3be173eb6c72b429db6e04dd76d2793a3995a2f51a23f4
        B/full-source-units.json: 1c65cbd13d47e62b5078bfa5d85826069b263b4d0ff059b575d457e3e145a74a
        B/meta.json: 8e9d56f540782077e0bda315c2c7a76db83145d0e23d40eddd5db78b8a27ba7c
        B/table-images/TABLE-S4-page-4-1.png: 36c558a22264c6973e867c344188ceb1d0249c8a783b08228989b7969f93f368
        B/table-images/TABLE-4-page-10-1.png: a87f07c3f4752233617b7ecf81385279c9316b9a04314ac9d28f1394d2f6ee6d
        B/table-images/page-10.png: dc4bc44a6532c38f7f58b139f835f12682de84d6249b0e8c43bfdac5b9c756ec
        B/table-images/TABLE-3-page-8-1.png: 93e3f3b6903611da94a5599d2da0c237c3f3d6bd1806916ce0f0e4ce94222d48
        B/table-images/page-7.png: 39397264f289b34919530ae60a946c19d6123785041fa980c602779aa183c106
        B/table-images/TABLE-1-page-4-2.png: fe0507a1056edc32500efd761aa5b0c0418fa07a2340cce4527751e6f6f68cf7
        B/table-images/page-4.png: 0b8f22d26d53258d45dbd65afa47acbfcd49b7c701f46b7dd64ae17e6698c098
        B/table-images/page-8.png: 77ad8c707a2b67da54b8cfa67bdce9206a2a444d856a9fc279d28b19388dec12
        B/table-images/manifest.json: f84e96b3764973f79961e9489588e09a272f37aca6036abfd8eb8df15ea93065
        B/table-images/TABLE-2-page-7-1.png: 11b0270dcb5a31da5d030214d97f2644a34fda91bcf17cfe8016ee9ad6b777bb
        B/clauses/window-03/raw.json: c81878663a8101a0614fdd782d67ac7bdca2767cf68d42f741c0e015f7795d7e
        B/clauses/window-03/prompt.txt: 7b81812744d2ab4b932042992af72d6661b7ea5a0d79b3d30c5e436a1e68bfd2
        B/clauses/window-03/meta.json: c84cf2d80c19525b83cf1a78579111bc8c017975bb33399229f83a49389fbd45
        B/clauses/window-04/raw.json: 7de4a4aca31d9f7a88eff99126e0d9be682995d2c865db97994644ffe2f8184c
        B/clauses/window-04/prompt.txt: e09c2ae43e05a6e5d422064092049a7c762f557efd6ae78583c6756bd3122330
        B/clauses/window-04/meta.json: df128e54ebf772acaa23da7f1c85018564f184e4ee5fa6add58d73dd925520ec
        B/clauses/window-05/raw.json: 8ca21bb19ccda45946016bcd021cd401d6d1a10f6812d485f34d2cf69412050d
        B/clauses/window-05/prompt.txt: 9d9d54ed48c5cff45ba35a7874c174766d2790c729bf078fb7e213309ec34112
        B/clauses/window-05/meta.json: 3c1db30b0bb0c33eedbcd7287a843c99a0af66b01a44124d3f78ac4f9e9536ce
        B/clauses/window-02/raw.json: d518b24233cd319429156e5c3edf2a136d2065ee7861d13b78002ec6c4922c02
        B/clauses/window-02/prompt.txt: d6e95125f81b6be64e45f92b3cb0580a38ddd31b52ff70a371751746b48d9b15
        B/clauses/window-02/meta.json: fed0d35c5de032d7e5908b485ac8b8930d691cc080738f82b4b4e83701ec7276
        B/clauses/window-07/raw.json: 79ed5a869c7126fd96c3b1d9840578feae1dba24705aed0744b9edc2fda86a85
        B/clauses/window-07/prompt.txt: d7992fe5bde7363aa90b112b836427c0b1cd561bb9fac9be4a478e8008ecd388
        B/clauses/window-07/meta.json: 09468917fc90b40109cbbc117cb3472d5c3bd1377dda7149c100d3ce016d5689
        B/clauses/window-01/raw.json: 1f357d4f910aca941cbf9cf23d06a04ad9790c304b5c55ba9e387500230e7f0c
        B/clauses/window-01/prompt.txt: afc9452689c6602004d820b6f6dd6a7cf834c55bedabc76066047c6f7a45714a
        B/clauses/window-01/meta.json: 1ccc37a42089418c8f544e9c3544efe65da15a9257c7f8298364bac57858c540
        B/clauses/window-06/raw.json: 55f96b68fd91f4555f492f7d9ed6ea4efcea17509ef37f30d8c393682fe24d82
        B/clauses/window-06/prompt.txt: 5e197b4e9485960e7f1652894c7c899d609635a19dea7b695c0ff9b241812a8a
        B/clauses/window-06/meta.json: 5fb934851adb5ef3f926e261f965977c5176a46715eff0fd39fca33a1729a08d
        B/tables/TABLE-1-page-4-2/raw.json: 2dfa0012523e63553dca35fb6fc6a71a5b35c09ebb53d5420286a6090a710166
        B/tables/TABLE-1-page-4-2/prompt.txt: b1c3795a2dcd0b06a2a87f6c973f560dc2ee687c7b51866879ed5f91b68e9440
        B/tables/TABLE-1-page-4-2/meta.json: 5a8406347b920d4baed149655acf04362d1a1c148598928ca5edd1191afe4937
        B/tables/TABLE-3-page-8-4/raw.json: 85d8a74aaae638f19ed7672f573fa81ba7c62702dcf8a49b40140ca690dc0a3a
        B/tables/TABLE-3-page-8-4/prompt.txt: eb858d27102e5be60eb9fd5ed0719f6a1676b7e6c9995c57d8785c8d4d85d544
        B/tables/TABLE-3-page-8-4/meta.json: 83ca81bbcce678816c3bb4fb816e049b6f15ab56c3d43f550b677e5d0035f517
        B/tables/TABLE-2-page-7-3/raw.json: 4ad973c269a24b6f6f35215833d8b3c471aac236f5c8ef2df7f5bb91e3b25ab4
        B/tables/TABLE-2-page-7-3/prompt.txt: 4cb613a1660b3e3e2de328f2edefe639f61494eab5c108083c1203b9794ff75f
        B/tables/TABLE-2-page-7-3/meta.json: 6408cb7614ca0f7dd2f8359deb935a3b133d4afe44bb40e657e9294d2b912375
        B/tables/TABLE-S4-page-4-1/raw.json: 2dfa0012523e63553dca35fb6fc6a71a5b35c09ebb53d5420286a6090a710166
        B/tables/TABLE-S4-page-4-1/prompt.txt: 17258ea2306d1e4f49b2edcc4f21c9e8caf000f11bbd35054bbd7a104195bc3e
        B/tables/TABLE-S4-page-4-1/meta.json: b272edff80c2bd3070ae309d04cffe0de057bfc58fe04907a0fbf42644b7b706
        B/tables/TABLE-4-page-10-5/raw.json: af1e97b3a9ce5e9ee300c945381e46ab60657c5581e5c7d34fe47df438ee4f25
        B/tables/TABLE-4-page-10-5/prompt.txt: f7198c96a2a1c138995dbd828c58bea4c1520e298cf019ddc71173d1e81899ec
        B/tables/TABLE-4-page-10-5/meta.json: 8d52cbc334d4fcfa7b1a1b90d0a512aa1fd0e27805c54ce658d7d4e1c153b303
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
      pdf_sha256: e6ff8e77b0302d8bbde76970bf8372c5669188243c84c97db9eaf98aaed77f98
      source_review: _compare/relationships-2026-11-16/review-current/Zhao2018
      source_status_sha256: ccafca348dc20088fc09b293c598d3010f394acc8ddd6391a5677e8e0a946618
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R022
    exposure:
      text: linear model with feature selection
    outcome:
      text: prediction of MoCA scores
    analysis_label: SVR-LSM Model Comparison
    relation: model_comparison
    evidence_ids:
    - P11-S2-C3
    qualifier_ids:
    - P11-S2-C2
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: e6ff8e77b0302d8bbde76970bf8372c5669188243c84c97db9eaf98aaed77f98
      source_review: _compare/relationships-2026-11-16/review-current/Zhao2018
      source_status_sha256: ccafca348dc20088fc09b293c598d3010f394acc8ddd6391a5677e8e0a946618
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P3-S3-C10
      - Result passage disposed without unit P3-S3-C11
      - Result passage disposed without unit P3-S3-C6
      - Result passage disposed without unit P4-S1-C6
      - Result passage disposed without unit P4-S1-C12
      - Result passage disposed without unit P4-S2-C8
      - Accounting without a linked unit P5-S1-C2
      - Accounting without a linked unit P5-S1-C3
      - Accounting without a linked unit P5-S1-C4
      - Unaccounted source passage P5-S1-C4
      - Unaccounted source passage P5-S1-C2
      - Unaccounted source passage P5-S1-C3
      - Result passage disposed without unit P7-S1-C3
      - Result passage disposed without unit P7-S1-C4
      - Result passage disposed without unit P7-S1-C5
      - Result passage disposed without unit P7-S1-C6
      - Accounting without a linked unit P7-S1-C8
      - Accounting without a linked unit P7-S1-C9
      - Accounting without a linked unit P7-S2-C1
      - Accounting without a linked unit P7-S2-C2
      - Accounting without a linked unit P7-S2-C6
      - Accounting without a linked unit P7-S2-C8
      - Accounting without a linked unit P7-S3-C2
      - Unaccounted source passage P7-S3-C2
      - Unaccounted source passage P7-S2-C6
      - Unaccounted source passage P7-S2-C8
      - Unaccounted source passage P7-S1-C8
      - Unaccounted source passage P7-S1-C9
      - Unaccounted source passage P7-S2-C2
      - Unaccounted source passage P7-S2-C1
      - Result passage disposed without unit P10-S1-C1
      - Result passage disposed without unit P10-S1-C3
      - Result passage disposed without unit P11-S2-C1
      - Result passage disposed without unit P11-S2-C3
      - Result passage disposed without unit P11-S2-C7
      - Accounting without a linked unit P11-S3-C3
      - Unaccounted source passage P11-S3-C3
      unattached_null_or_qualifier_ids:
      - P7-S1-C9
      - P7-S2-C1
      - P11-S2-C7
      suppressed_nonrepresented_units: 21
      default_disposition_count_requires_completeness_check: 118
      unselected_timing_passages:
      - P1-S1-C3
      - P2-S1-C5
      - P5-S1-C8
      - P11-S2-C10
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P4-S1-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S2-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S2-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S2-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: limitations
        source_ids:
        - P5-S1-C11
        - P5-S1-C12
        - P11-S1-C4
        - P11-S1-C5
        - P11-S2-C6
        - P11-S2-C7
        - P11-S2-C8
        - P11-S2-C9
        - P11-S2-C11
        - P11-S3-C2
        - P11-S3-C3
        - P11-S3-C4
        - P11-S3-C5
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - limitations
      - personal_factors
      - tested_personal_effects
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-4-2
      - TABLE-2-page-7-3
      - TABLE-3-page-8-4
      - TABLE-4-page-10-5
      - TABLE-S4-page-4-1
      unlinked_tables:
      - TABLE-1-page-4-2
      - TABLE-4-page-10-5
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P3-S3
        - P4-S1
        - P4-S2
        - P5-S1
        - P5-S2
        - P6-S1
        - P7-S1
        - P7-S2
        - P9-S1
        - P11-S1
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: e6ff8e77b0302d8bbde76970bf8372c5669188243c84c97db9eaf98aaed77f98
      source_review: _compare/relationships-2026-11-16/review-current/Zhao2018
      source_status_sha256: ccafca348dc20088fc09b293c598d3010f394acc8ddd6391a5677e8e0a946618
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C6
      disposition: represented
      result_indexes:
      - 0
      reason: Identifies strategic structures for global cognitive impairment.
    - source_id: P1-S1-C7
      disposition: represented
      result_indexes:
      - 1
      reason: Identifies strategic networks for cognitive domains.
    - source_id: P3-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes model adjustment for prediction accuracy.
    - source_id: P3-S3-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive statistic of median AIL volume.
    - source_id: P3-S3-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive statement on lesion prevalence.
    - source_id: P3-S3-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive statement on lesion size topologies.
    - source_id: P4-S1-C1
      disposition: represented
      result_indexes:
      - 2
      reason: Identifies voxel clusters associated with total MoCA.
    - source_id: P4-S1-C4
      disposition: represented
      result_indexes:
      - 3
      reason: Specifies significant regions for global cognition.
    - source_id: P4-S1-C5
      disposition: represented
      result_indexes:
      - 4
      reason: Identifies significant clusters for cognitive domains.
    - source_id: P4-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about discrepant regions.
    - source_id: P4-S1-C7
      disposition: represented
      result_indexes:
      - 5
      reason: Associates left dorsal cortical regions with language.
    - source_id: P4-S1-C8
      disposition: represented
      result_indexes:
      - 6
      reason: Associates right temporal/left occipital regions with language.
    - source_id: P4-S1-C9
      disposition: represented
      result_indexes:
      - 7
      - 8
      reason: Associates left hemispheric lesions with memory/executive and right
        parietal with attention/visuospatial.
    - source_id: P4-S1-C10
      disposition: represented
      result_indexes:
      - 9
      reason: Associates cerebellum lesions with attention.
    - source_id: P4-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to tables.
    - source_id: P4-S1-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to figure.
    - source_id: P4-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to patient counts/lesion size.
    - source_id: P4-S2-C3
      disposition: represented
      result_indexes:
      - 10
      reason: Associates total MoCA with specific left hemisphere structures.
    - source_id: P4-S2-C4
      disposition: represented
      result_indexes:
      - 11
      reason: Identifies most significant ROIs for total MoCA.
    - source_id: P4-S2-C5
      disposition: represented
      result_indexes:
      - 12
      reason: Null finding for total lesion volume in multivariate SVR-ROI for total
        MoCA.
    - source_id: P4-S2-C6
      disposition: represented
      result_indexes:
      - 13
      reason: Associates left AIC with multiple cognitive domains.
    - source_id: P4-S2-C7
      disposition: represented
      result_indexes:
      - 14
      reason: Associates total lesion volume with visuospatial function.
    - source_id: P4-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement on reproduction of results.
    - source_id: P5-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement on reproduction of results.
    - source_id: P5-S1-C2
      disposition: represented
      result_indexes:
      - 15
      reason: Associates left dorsal cortical regions with memory and language.
    - source_id: P5-S1-C3
      disposition: represented
      result_indexes:
      - 16
      reason: Associates basal ganglia with language (inverse/less).
    - source_id: P5-S1-C4
      disposition: represented
      result_indexes:
      - 17
      reason: Associates left hemispheric regions with memory and executive function.
    - source_id: P6-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes voxel exclusion criteria.
    - source_id: P7-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement on corroboration.
    - source_id: P7-S1-C3
      disposition: repeated
      result_indexes:
      - 3
      - 11
      reason: Restatement of strategic regions for global cognition.
    - source_id: P7-S1-C4
      disposition: repeated
      result_indexes:
      - 3
      - 11
      reason: Restatement of strategic regions for global cognition.
    - source_id: P7-S1-C5
      disposition: repeated
      result_indexes:
      - 11
      reason: Restatement of AIC significance for total MoCA.
    - source_id: P7-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement on domain maps.
    - source_id: P7-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement on overlap of regions.
    - source_id: P7-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement on distinctions.
    - source_id: P7-S1-C9
      disposition: repeated
      result_indexes:
      - 5
      - 6
      - 7
      - 8
      - 14
      reason: Restatement of domain-specific associations.
    - source_id: P7-S2-C1
      disposition: repeated
      result_indexes:
      - 14
      reason: Restatement of total infarct volume association with visuospatial function.
    - source_id: P7-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation on hemispheric distribution of substrates.
    - source_id: P7-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement on SVR-LSM voxel patient counts.
    - source_id: P7-S2-C10
      disposition: represented
      result_indexes:
      - 18
      reason: Table 2 results for global cognition.
    - source_id: P7-S3-C1
      disposition: repeated
      result_indexes:
      - 18
      reason: Part of Table 2.
    - source_id: P7-S3-C2
      disposition: represented
      result_indexes:
      - 18
      reason: Qualifies Table 2 significance threshold.
    - source_id: P8-S1-C3
      disposition: represented
      result_indexes:
      - 19
      - 20
      reason: Table 3 results for cognitive domains.
    - source_id: P8-S1-C4
      disposition: represented
      result_indexes:
      - 19
      - 20
      reason: Qualifies Table 3 significance threshold.
    - source_id: P10-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement on patient counts for SVR-LSM.
    - source_id: P10-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement on SVR-ROI patient counts.
    - source_id: P11-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement on convergence of results.
    - source_id: P11-S1-C12
      disposition: represented
      result_indexes:
      - 22
      reason: Reports poor performance of original nonlinear SVR-LSM.
    - source_id: P11-S2-C1
      disposition: repeated
      result_indexes:
      - 22
      reason: Restatement of poor nonlinear model performance.
    - source_id: P11-S2-C3
      disposition: represented
      result_indexes:
      - 21
      reason: Linear model with feature selection outperformed others.
    unresolved_coverage:
    - source_id: P7-S2-C10
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P7-S3-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P7-S3-C2
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P8-S1-C3
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P8-S1-C4
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P11-S2-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S2-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S3-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P3-S2-C3
    - P3-S3-C6
    - P3-S3-C10
    - P3-S3-C11
    - P4-S1-C6
    - P4-S1-C12
    - P4-S1-C13
    - P4-S2-C2
    - P4-S2-C8
    - P5-S1-C1
    - P6-S1-C8
    - P7-S1-C2
    - P7-S1-C3
    - P7-S1-C4
    - P7-S1-C5
    - P7-S1-C6
    - P7-S1-C7
    - P7-S1-C8
    - P7-S1-C9
    - P7-S2-C1
    - P7-S2-C2
    - P7-S2-C8
    - P10-S1-C1
    - P10-S1-C3
    - P11-S1-C2
    - P11-S1-C12
    - P11-S2-C4
    - P11-S2-C7
    - P11-S3-C3
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-4-2
    - TABLE-2-page-7-3
    - TABLE-3-page-8-4
    - TABLE-4-page-10-5
    - TABLE-S4-page-4-1
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P2-S2-C5
      recruited_sample:
      - P2-S1-C5
      eligibility:
      - P2-S2-C3
      imaging_provenance:
      - P2-S2-C7
      - P2-S3-C1
      - P2-S3-C2
      imaging_timing:
      - P2-S2-C3
      - P2-S2-C7
      outcome_timing:
      - P1-S1-C4
      - P2-S2-C3
      outcome_definition:
      - P2-S2-C6
      - P1-S1-C4
      validation:
      - P11-S2-C2
      analysis_restrictions:
      - P3-S2-C10
      - P3-S3-C2
      dependent_variable_statement:
      - P3-S1-C7
      - P3-S1-C8
      - P3-S2-C5
      - P3-S2-C6
      limitations: []
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P3-S1-C9
      - P3-S2-C5
      - P6-S1-C5
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P4-S2-C10
    outcome_type: status_at_assessment
    imaging_vs_outcome: precedes_outcome
    validation_type: internal_cross_validation
    held_selections:
    - slot: dependent_variable_statement
      source_id: P4-S1-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S2-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S2-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S2-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: limitations
      source_ids:
      - P5-S1-C11
      - P5-S1-C12
      - P11-S1-C4
      - P11-S1-C5
      - P11-S2-C6
      - P11-S2-C7
      - P11-S2-C8
      - P11-S2-C9
      - P11-S2-C11
      - P11-S3-C2
      - P11-S3-C3
      - P11-S3-C4
      - P11-S3-C5
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
      pdf_sha256: e6ff8e77b0302d8bbde76970bf8372c5669188243c84c97db9eaf98aaed77f98
      review_sha256: 6247b650f0e01031fee72f5d4a825b2941d43b1449bd8583fada283122828995
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
      - P11-S2-C3
      source_result: The linear SVR-LSM model with feature selection outperformed
        the other three candidate models (nonlinear with/without feature selection,
        linear without feature selection) in predicting MoCA scores, leading to its
        selection for the study's statistical inference.
      result_status: model_comparison
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The source explicitly describes a comparison of four SVR-LSM model
            configurations (linear/nonlinear, with/without feature selection) to determine
            which performed best for predicting MoCA scores. The draft correctly identifies
            this as a model comparison analysis.
          source_ids:
          - P11-S2-C2
          - P11-S2-C3
        direction:
          answer: fits
          reason: The source states the linear model with feature selection 'outperformed
            the other models'. The draft's claim that it 'outperformed nonlinear and
            linear models without feature selection' accurately reflects the direction
            of the result (superiority of the selected model).
          source_ids:
          - P11-S2-C3
        construct:
          answer: fits
          reason: The exposure is correctly identified as the linear model with feature
            selection. The outcome is MoCA scores. The patient measurement is template_lesion_overlap,
            as the SVR-LSM method involves overlaying patient lesion maps on a template
            (MNI-152) to determine voxel-wise associations, rather than using patient-specific
            diffusion tractography or raw regional volumes as the primary independent
            variable in the voxelwise analysis.
          source_ids:
          - P11-S2-C3
          - P3-S1-C7
          - P3-S1-C3
        qualifications:
          answer: fits
          reason: The draft includes the qualification that the model was trained
            and tested on the same data, which is supported by P11-S2-C2 ('compared
            their prediction performance and reproducibility on the same training
            and testing data'). It also correctly lists the comparison of four configurations.
          source_ids:
          - P11-S2-C2
        missing_material_caveat:
          answer: fits
          reason: The draft includes relevant limitations regarding generalizability
            to large infarcts and the use of MoCA. No material caveats that would
            change the interpretation of the model comparison result are omitted.
          source_ids:
          - P11-S2-C9
          - P11-S3-C4
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
      id: R022
      exposure:
        text: linear model with feature selection
      outcome:
        text: prediction of MoCA scores
      analysis_label: SVR-LSM Model Comparison
      relation: model_comparison
      evidence_ids:
      - P11-S2-C3
      qualifier_ids:
      - P11-S2-C2
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: e6ff8e77b0302d8bbde76970bf8372c5669188243c84c97db9eaf98aaed77f98
        source_review: _compare/relationships-2026-11-16/review-current/Zhao2018
        source_status_sha256: ccafca348dc20088fc09b293c598d3010f394acc8ddd6391a5677e8e0a946618
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P2-S2-C5:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: e6ff8e77b0302d8bbde76970bf8372c5669188243c84c97db9eaf98aaed77f98
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 7da2718ea1479bc40dfbe2ad62f73258577ab4021d8025a8cc2e6b698751935d
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S2-C5
          page: 2
          text_layer_sha256: 7da2718ea1479bc40dfbe2ad62f73258577ab4021d8025a8cc2e6b698751935d
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Finally, 410 patients were included in this study

          (See Supplementary Figure S1, the ﬂow-chart of the

          patient recruitment).'
        anchor_text: 'Finally, 410 patients were included in this study

          (See Supplementary Figure S1, the ﬂow-chart of the

          patient recruitment).'
        excluded_fragments: []
        image_sha256: 803cbc0933d3b06b9e7ae8b8e94a91aba86bda51643f400ba166b6483b640a2d
        transcription: '. Finally, 410 patients were included in this study

          (See Supplementary Figure S1, the flow-chart of the

          patient recruitment)'
      P11-S2-C9:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: e6ff8e77b0302d8bbde76970bf8372c5669188243c84c97db9eaf98aaed77f98
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 3baf2936725413624738ed8aaf565cc7dfe34c6390cd77c77b39acedfecdac35
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P11-S2-C9
          page: 11
          text_layer_sha256: 3baf2936725413624738ed8aaf565cc7dfe34c6390cd77c77b39acedfecdac35
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'It should be noted

          that we included many patients with relatively small

          infarcts (median volume 2.3 ml), which may in part be

          due to some of the exclusion criteria of the CU-STRIDE

          cohort (e.g. patients who died before assessment of who

          were incommunicable were not included).'
        anchor_text: 'It should be noted

          that we included many patients with relatively small

          infarcts (median volume 2.3 ml), which may in part be

          due to some of the exclusion criteria of the CU-STRIDE

          cohort (e.g. patients who died before assessment of who

          were incommunicable were not included).'
        excluded_fragments: []
        image_sha256: 0555f398ea7b02869a312ea3d59b4e6ece81f671c7eb58cb76c3881b7e9d6d0b
        transcription: '. It should be noted

          that we included many patients with relatively small

          infarcts (median volume 2.3 ml), which may in part be

          due to some of the exclusion criteria of the CU-STRIDE

          cohort (e.g. patients who died before assessment of who

          were incommunicable were not included)'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 11
  quote: 'As can be appreciated from the results

    and information in the online supplementary materials,

    the linear model with feature selection outperformed

    the other models, which is why this model was selected

    for the current study in statistical inference (See

    Supplementary Method for more details).'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-26'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
