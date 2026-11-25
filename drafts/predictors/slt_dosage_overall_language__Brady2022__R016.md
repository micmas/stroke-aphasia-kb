---
id: slt_dosage_overall_language
name: SLT dosage (total hours)
kind: predictor
findings:
- id: f1
  target_audit:
    status: behaviour_label_present
    category: behaviour_or_language_construct
    original_target: overall_language_ability
    reason: Label names a behaviour or language construct; its exact operational definition and measurement
      still need source review.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  outcome_measurement:
    status: needs_source_review
    instruments: []
    note: Outcome instrument/task is not yet verified for this finding. Do not infer it from the predictor
      or a paper-wide test list.
  target: overall_language_ability
  target_kind: impairment
  claim: In the early-SLT group (<= 3 months post-onset), the greatest overall-language
    gains occurred for 20-50 SLT-h; in the late-SLT group (> 3 months post-onset),
    the only significant overall-language gain occurred for > 50 SLT-h.
  direction: likely
  relationship: correlational
  method: meta-analysis
  sample:
    n: 959
    population: individuals with stroke-related aphasia
    phase: not_reported
    time_post_onset: from baseline to first post-intervention follow-up
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - predominantly English-speaking participants
  - reflects change from RCT baseline to first follow-up only
  - pre-randomization SLT and language change data were unavailable
  evidence_quality: meta-analysis
  strength: weak
  notes: 'Exposure measurement: Total hours of speech and language therapy (SLT) received,
    categorized into dosage brackets (e.g., 20-50 hours, >50 hours). early-SLT group
    defined as <= 3 months post-aphasia onset; late-SLT group defined as > 3 months
    post-aphasia onset; analysis adjusted for age, sex, aphasia severity, and time
    post-onset. Additional metadata has not been transcribed; review the pending-field
    flags before approval. PDF image reading (P2-S2-C4, two-model agreement, human
    verification pending): Results: 959 IPD (25 RCTs) were analyzed Original text-layer
    quotation is preserved below.'
  imaging_details:
    reference_space: not_reported
    atlases_used: []
  lesion_mapping: {}
  provenance:
    extracted_by: model:gemma4:31b
    extracted_on: '2026-11-20'
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
    - proposed_concept:overall_language_ability
  therapy:
    id: slt
    name: speech and language therapy
  citation: '@Brady2022'
  source_passages:
  - section: Original source P8-S1-C4
    page: 8
    quote: "The early-SLT group achieved their greatest over-\nall-language and functional\
      \ communication gains for 20–\n50 SLT-h; auditory comprehension gains were not\
      \ observed \nat any dosage."
    supports: claim
  - section: Original source P8-S1-C5
    page: 8
    quote: "The late-SLT group’s only significant over-\nall-language gain from baseline\
      \ occurred for > 50 SLT-h; \ngains in auditory comprehension were significant\
      \ for > 14 \nSLT-h with the greatest of these for > 50 SLT-h."
    supports: claim
  - section: Original source P2-S1-C9
    page: 2
    quote: "Data were dichotomized by age (⩽/> 65 years), aphasia severity (mild–moderate/\
      \ moderate–severe based on language \noutcomes’ median value), chronicity (⩽/> 3 months),\
      \ and sex subgroups."
    supports: confounders
  - section: Original source P4-S2-C6
    page: 4
    quote: "All remaining \nmeasures of that outcome (minority measures) were trans-\n\
      formed to match the anchor measure’s range and format, \nthus retaining the\
      \ clinical relevance of the anchor meas-\nures’ change score.19 Anchor measures\
      \ comprised the \nWestern aphasia battery-aphasia quotient (WAB-AQ)22 for \n\
      overall-language ability; the Aachen Aphasia test-token test \n(AAT-TT) scored\
      \ positively for auditory comprehension;23 \nand the Aachen Aphasia test-spontaneous\
      \ speech commu-\nnication (AAT-SSC) rating domain score for functional \ncommunication.23\n\
      SLT interventions targeting language recovery were cat-\negorized by regimen\
      \ (frequency, intensity, and dosage; \nSupplemental Material A)."
    supports: method
  - section: Original source P5-S1-C4
    page: 5
    quote: "We included prespecified potential confounders in the \nbase model (age,\
      \ sex, aphasia severity, and time post-onset) \nand simultaneously examined\
      \ the impact of IPD and lan-\nguage variables on the intervention effect."
    supports: confounders
  - section: Original source P2-S2-C4
    page: 2
    quote: 'Results: 959 IPD (25 RCTs) were analyzed.'
    supports: sample
  - section: Original source P9-S2-C8
    page: 9
    quote: "Language gains observed reflect the change from RCT \nbaseline to the\
      \ first follow-up only."
    supports: limitation
  - section: Original source P9-S3-C6
    page: 9
    quote: "Despite no \nlanguage restrictions, our predominantly English-speaking\
      \ \nparticipant data highlighted an underrepresentation of non-\nEnglish aphasia\
      \ research."
    supports: limitation
predictor_type: clinical
short_definition: Total hours of speech and language therapy (SLT) received, categorized
  into dosage brackets (e.g., 20-50 hours, >50 hours).
assessment:
- Western aphasia battery-aphasia quotient (WAB-AQ)
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-20'
relationship_review:
  paper: Brady2022
  proposal_id: R016
  review_status_sha256: 2c072f1d3d6796096337485830f5b0eb82f8afa37a43f0c8c71305987f9164d6
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: e949dbbd260ec0b118b5f7b73f911fb02f061b9e14e4b1cc7810746cb96f4f3b
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: e949dbbd260ec0b118b5f7b73f911fb02f061b9e14e4b1cc7810746cb96f4f3b
        A/passages.json: 773f5ca8a3a706b32759ddac48333601d7b82fcde30d855196161287cdb55ca7
        A/raw.json: d96c0c87bb49b6133810f89dbbd1fc35f3a6480165b7b2aff1b8db0f7aef99e3
        A/source-units.json: 151c93984c8ffcce10118ddfea89e02a7b62c5b46bbee36db6c05e79c5e54099
        A/full-source-units.json: 3394bcb10fb107aa0e293a024c5ae782f3dc1dd6c01d98cf6d6c1dfa239023fe
        A/meta.json: 1c880da8c9488f6787623f917a232e857df6116762a94a5b29f711ac84795da4
        A/table-images/TABLE-1-page-7-1.png: 223dd83ffbab85fbd8a68898d24583259ee7476891488ca144e3592fdf596b27
        A/table-images/TABLE-1-page-6-1.png: a9d3b8c603ebe302043f20109e46fe0f5df37a3b68f4c9223c54c04a00bdacd1
        A/table-images/page-6.png: 8f7c64713e6cdf860ad48d162e002e9330bb9685293ded785907446efcc1452c
        A/table-images/page-7.png: 8b9a7b34420b09982e84701ca4e8d52cf793f2f96cae6222783d04c44a5a9b0a
        A/table-images/manifest.json: 1fe765fc941df27f2e8f7d5c9cf19b92e9c42b5696aac3651dd823bf6c557b1a
        A/clauses/window-03/raw.json: c9898d5eb45cd436e1bc732d66728d12f81082ab892cb9cf85252bd79e2243aa
        A/clauses/window-03/prompt.txt: faa7585f255c177466dea6ec2cf10e3663f8fdc2915889df8f7ddd85bb1209d1
        A/clauses/window-03/meta.json: 5b47925afebb3bf433c762c96d059935a5c3523af9996cfab6db2ace60405a51
        A/clauses/window-04/raw.json: 17e6899f4fcf9ee416392b6b995fc391d4da3c0ddc79db8382d8b04a9b2d7524
        A/clauses/window-04/prompt.txt: 1e3ad51af5a349fdaab75046787f5489fc259ae5e3d754db8ec057f56ea12438
        A/clauses/window-04/meta.json: 591ffc39b8016b48d548796cea1c4216b79a183ad2ac0fc3ce4518ae87c9e80e
        A/clauses/window-05/raw.json: c82f682ca91a47ff0fffae2386ca1b3ac1319296a5c3bfcb10bb9aab2c5a8c4c
        A/clauses/window-05/prompt.txt: 817f242dca75f6f5d3b9fd7f2dabc0c0aee14370659a433a806a4693ac862c52
        A/clauses/window-05/meta.json: 76968b2d22df283e9f6dfb4b289e34d7f8a2ebe5891bf4c930f6d4c4d0ae86dd
        A/clauses/window-02/raw.json: 8189b2a710c323e0ebda30ae64767b80696f08bdd8950b451f7880b9d7c927bd
        A/clauses/window-02/prompt.txt: da55e2f9b8f1861f054fb2e613f311bcfa020a67bdf687056cbcd50ce304ade5
        A/clauses/window-02/meta.json: fb134cfff81a8e844320f38f58bdb393b5ebf87a13e6182f340ec096c7d36dfd
        A/clauses/window-07/raw.json: e1e462a75845155d471ad4bc5faf08053357689071324c22af7c7c13d443db05
        A/clauses/window-07/prompt.txt: 86d23f0835303c953c8ec96578d1bba45aa73026d1347a4e0e26242c7afafffa
        A/clauses/window-07/meta.json: 3dbb2dc64d9150f10166cde329bbe624e067ac667f43e62aeca6332fb0ed285c
        A/clauses/window-01/raw.json: edb1f3272fcae88412f3470d187d7542b1bb0cd1b1836e59e6916cbbff66cdac
        A/clauses/window-01/prompt.txt: 216f53b357170c3979f8697f1ba8a1c0f0572e747214054b4732d9449a1141e2
        A/clauses/window-01/meta.json: 2c1acb9d08cca8d6fab12ed77b83693cf7b1894c649c3d238e0df76dd4226889
        A/clauses/window-06/raw.json: 007f665de1c0d90e6b5166052be1945465eff0f47922adb342ed9bfd023c473d
        A/clauses/window-06/prompt.txt: 1a272b12444eaad8e47fb06046a42b6f46b3a079e69a0382ff0413b842194594
        A/clauses/window-06/meta.json: 30f45d7258b2007fb5a96b16cb282002934f7425151068a1af06e6ee2999e06f
        A/clauses/window-08/raw.json: 677e65e481a3dacff86ccb2d379589382ddd17eefd3540bb7a45678e4ff5f2e3
        A/clauses/window-08/prompt.txt: 19ae3199548d90f2ee189a43779cd124337d8f6d2b49d52c8f4afb9a7ba07aea
        A/clauses/window-08/meta.json: 18d4ed8c5dcb8ae718633d3323bf8c8a43f969928d6f5092dc3356acd449bc3c
        A/tables/TABLE-1-page-7-2/raw.json: 82049cda77d05b9baf6051550b023f4c32d63538451ae73130924ec1f3b942df
        A/tables/TABLE-1-page-7-2/prompt.txt: 8daf4a27859b8cf31a29690004becd1303dacd3e0a10f962c7505b0cf67328bb
        A/tables/TABLE-1-page-7-2/meta.json: 964b0fa288d13ad44b25902591576007b4745e117c6996345abef246a82f34c5
        A/tables/TABLE-1-page-6-1/raw.json: 4ea72566523edb55d0820d8ef1468efef919c38b08d64222ecaca26c183e8430
        A/tables/TABLE-1-page-6-1/prompt.txt: 66debc6036d508ec62b2033899ee210e5298606af77537491439a157c337bf38
        A/tables/TABLE-1-page-6-1/meta.json: 7da83c95ceed6215db0297b7bf0ca531c6ae48814dc08fbf50cba2760eb8fac8
        B/passages.json: 773f5ca8a3a706b32759ddac48333601d7b82fcde30d855196161287cdb55ca7
        B/raw.json: d2276eb148329f5bd4eebd8807fbe5d8679e7ce7fbaa5de75f5ee3777216d304
        B/source-units.json: 151c93984c8ffcce10118ddfea89e02a7b62c5b46bbee36db6c05e79c5e54099
        B/full-source-units.json: 3394bcb10fb107aa0e293a024c5ae782f3dc1dd6c01d98cf6d6c1dfa239023fe
        B/meta.json: 2d16075bc39d09fe88b574f29a7e98d78fafde560dd3f4847c8181da83d0d723
        B/table-images/TABLE-1-page-7-1.png: 223dd83ffbab85fbd8a68898d24583259ee7476891488ca144e3592fdf596b27
        B/table-images/TABLE-1-page-6-1.png: a9d3b8c603ebe302043f20109e46fe0f5df37a3b68f4c9223c54c04a00bdacd1
        B/table-images/page-6.png: 8f7c64713e6cdf860ad48d162e002e9330bb9685293ded785907446efcc1452c
        B/table-images/page-7.png: 8b9a7b34420b09982e84701ca4e8d52cf793f2f96cae6222783d04c44a5a9b0a
        B/table-images/manifest.json: 75717073c5512024352ee8c0098ea51cea79c363262cda0cd113401edd9fde93
        B/clauses/window-03/raw.json: b771c4c8e4c51930a435e7d8f28b2728f48a2a30cd1b1e1a0b7dc2c0fd5b4a98
        B/clauses/window-03/prompt.txt: faa7585f255c177466dea6ec2cf10e3663f8fdc2915889df8f7ddd85bb1209d1
        B/clauses/window-03/meta.json: e372ff27c2ae33071c888a83879ce582dec8ccb6e09e65ed7633901a69e605b0
        B/clauses/window-04/raw.json: 5956ccaccf5fd614b568f2e184ed71eb8cbeebe2f529ab6e7e1b180da37dd71f
        B/clauses/window-04/prompt.txt: 1e3ad51af5a349fdaab75046787f5489fc259ae5e3d754db8ec057f56ea12438
        B/clauses/window-04/meta.json: a4d2d3005a3f84728655da9fbc4dbcde85722705611ce531fd492cc7dcc76dbf
        B/clauses/window-05/raw.json: 265c093395d2fd278ead94b500c8546581f490d83dc47c2e716199002afdbce9
        B/clauses/window-05/prompt.txt: 817f242dca75f6f5d3b9fd7f2dabc0c0aee14370659a433a806a4693ac862c52
        B/clauses/window-05/meta.json: 7a8cdd60c9d862d40471c216eb99da796659505033fa3e68ee541b9b0b3a4bb4
        B/clauses/window-02/raw.json: 1bdee439113e6d007e39d6d3a63cf84a7b2b54d88a5b8107edb653b542218096
        B/clauses/window-02/prompt.txt: da55e2f9b8f1861f054fb2e613f311bcfa020a67bdf687056cbcd50ce304ade5
        B/clauses/window-02/meta.json: 4e5250746de250bb98028ac393e4cce475875178423116df8bb703fcbde5276b
        B/clauses/window-07/raw.json: 02e0ea0f2492d32a52ed22dd8d05064c68c67870c7fc9566d1e9d62b10fb264c
        B/clauses/window-07/prompt.txt: 86d23f0835303c953c8ec96578d1bba45aa73026d1347a4e0e26242c7afafffa
        B/clauses/window-07/meta.json: 1a65846a4afcd5df49ec2e5ab9f5b02afc011facbbc371066d1f3c136a415e43
        B/clauses/window-01/raw.json: ea52e0e6102c371f8e8a378c3b3e1c2af16a5d35bba17b16ed9368dd672b5dc1
        B/clauses/window-01/prompt.txt: 216f53b357170c3979f8697f1ba8a1c0f0572e747214054b4732d9449a1141e2
        B/clauses/window-01/meta.json: 7aac41bdd1fd980217783afd6eb70b0823559a8f793df39e9f92c4289ebbab35
        B/clauses/window-06/raw.json: c4e7e8063bfe791d5d7b656d1c315f0cdc4b070234f373aaebd5e9f15e6fd610
        B/clauses/window-06/prompt.txt: 1a272b12444eaad8e47fb06046a42b6f46b3a079e69a0382ff0413b842194594
        B/clauses/window-06/meta.json: f3bd82eb0f5fe10ab95e882590f99a0be11938cf0c2b37263ece321d4a7002fd
        B/clauses/window-08/raw.json: 677e65e481a3dacff86ccb2d379589382ddd17eefd3540bb7a45678e4ff5f2e3
        B/clauses/window-08/prompt.txt: 19ae3199548d90f2ee189a43779cd124337d8f6d2b49d52c8f4afb9a7ba07aea
        B/clauses/window-08/meta.json: 0dd468a13ca9292f6cfe1bd4fbb3033844d2d372c37a0dfa9f6a604ee689aa39
        B/tables/TABLE-1-page-7-2/raw.json: cd5ecef215d877f6fd2e6273bbd34c4785f674b7c6afc10df825d18b0edd28f6
        B/tables/TABLE-1-page-7-2/prompt.txt: 8daf4a27859b8cf31a29690004becd1303dacd3e0a10f962c7505b0cf67328bb
        B/tables/TABLE-1-page-7-2/meta.json: cc06d3a18bff6e25d27073c6b97e3af819653824ed374ffa9629b4ecc8a9540d
        B/tables/TABLE-1-page-6-1/raw.json: ee3505ae53b730b396818c468351aa28866046c18e23dc38773c6664d63e9998
        B/tables/TABLE-1-page-6-1/prompt.txt: 66debc6036d508ec62b2033899ee210e5298606af77537491439a157c337bf38
        B/tables/TABLE-1-page-6-1/meta.json: 16eaf2315cc830956d6682b3af19a6d244b47bbe1c8ba84100dd8814f7864738
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
      pdf_sha256: e949dbbd260ec0b118b5f7b73f911fb02f061b9e14e4b1cc7810746cb96f4f3b
      source_review: _compare/relationships-2026-11-16/review-current/Brady2022
      source_status_sha256: 293de3f879f6ad3a5c594ea25f2aa2c552e7da2bf2c71e9c94fc49b877cb38c8
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R016
    exposure:
      text: SLT dosage (total hours)
    outcome:
      text: overall-language ability
    analysis_label: Chronicity and SLT Dosage
    relation: association
    evidence_ids:
    - P8-S1-C4
    - P8-S1-C5
    qualifier_ids:
    - P6-S1-C3
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: e949dbbd260ec0b118b5f7b73f911fb02f061b9e14e4b1cc7810746cb96f4f3b
      source_review: _compare/relationships-2026-11-16/review-current/Brady2022
      source_status_sha256: 293de3f879f6ad3a5c594ea25f2aa2c552e7da2bf2c71e9c94fc49b877cb38c8
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P3-S1-C1
      - Result passage disposed without unit P10-S1-C1
      - Result passage disposed without unit P9-S2-C14
      - Result passage disposed without unit P9-S3-C10
      - Result passage disposed without unit P9-S3-C2
      - Result passage disposed without unit P9-S3-C9
      unattached_null_or_qualifier_ids: []
      suppressed_nonrepresented_units: 8
      default_disposition_count_requires_completeness_check: 148
      unselected_timing_passages:
      - P4-S2-C8
      - P5-S1-C7
      - P9-S2-C8
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P5-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: tested_personal_effects
        source_id: P2-S1-C4
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P2-S1-C9
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P4-S1-C1
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P5-S1-C5
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P9-S3-C3
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P9-S3-C5
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: outcome_timing
        source_ids:
        - P2-S1-C8
        - P4-S1-C1
        - P4-S2-C3
        - P4-S3-C9
        - P5-S1-C5
        - P5-S2-C3
        - P5-S3-C10
        - P8-S1-C1
        - P8-S1-C5
        - P8-S1-C6
        - P8-S1-C9
        - P8-S3-C9
        - P9-S1-C3
        - P9-S2-C4
        - P9-S2-C8
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: outcome_definition
        source_ids:
        - P2-S1-C8
        - P4-S1-C1
        - P4-S2-C3
        - P4-S3-C9
        - P5-S1-C5
        - P5-S2-C3
        - P5-S3-C10
        - P8-S1-C1
        - P8-S1-C5
        - P8-S1-C6
        - P8-S1-C9
        - P8-S3-C9
        - P9-S1-C3
        - P9-S2-C4
        - P9-S2-C8
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: limitations
        source_ids:
        - P3-S2-C2
        - P9-S2-C2
        - P9-S2-C5
        - P9-S2-C6
        - P9-S2-C7
        - P9-S2-C9
        - P9-S2-C10
        - P9-S2-C11
        - P9-S2-C12
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: tested_personal_effects
        source_ids:
        - P3-S1-C3
        - P3-S1-C4
        - P5-S2-C3
        - P5-S3-C5
        - P5-S3-C7
        - P8-S1-C8
        - P8-S1-C10
        - P8-S1-C13
        - P8-S1-C15
        - P8-S2-C10
        - P8-S2-C11
        - P8-S2-C12
        - P8-S2-C16
        - P8-S2-C19
        - P8-S2-C21
        - P8-S3-C3
        - P8-S3-C4
        - P8-S3-C6
        - P8-S3-C7
        - P9-S1-C2
        - P9-S1-C3
        - P9-S1-C4
        - P9-S1-C5
        - P9-S1-C6
        - P9-S3-C10
        - P10-S1-C1
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - imaging_provenance
      - imaging_timing
      - outcome_timing
      - outcome_definition
      - validation
      - limitations
      - tested_personal_effects
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-6-1
      - TABLE-1-page-7-2
      unlinked_tables: []
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units: []
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: e949dbbd260ec0b118b5f7b73f911fb02f061b9e14e4b1cc7810746cb96f4f3b
      source_review: _compare/relationships-2026-11-16/review-current/Brady2022
      source_status_sha256: 293de3f879f6ad3a5c594ea25f2aa2c552e7da2bf2c71e9c94fc49b877cb38c8
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P2-S2-C5
      disposition: represented
      result_indexes:
      - 0
      reason: Directly reports language gains for working-age and older participants
        by intensity.
    - source_id: P2-S2-C6
      disposition: represented
      result_indexes:
      - 1
      reason: Reports similarity in frequency and dosage for best gains across age
        groups.
    - source_id: P2-S2-C7
      disposition: represented
      result_indexes:
      - 1
      reason: Reports chronicity-based gains for overall-language.
    - source_id: P2-S2-C8
      disposition: represented
      result_indexes:
      - 2
      - 18
      - 20
      reason: Reports severity-based gains for various outcomes by frequency.
    - source_id: P2-S2-C9
      disposition: represented
      result_indexes:
      - 27
      - 28
      - 29
      reason: Reports sex-based gains by intensity.
    - source_id: P3-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion statement about treatment response.
    - source_id: P3-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion about variation in response.
    - source_id: P3-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Summary of subgroup trends.
    - source_id: P3-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Summary of subgroup trends.
    - source_id: P5-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: General summary of greatest gains across subgroups.
    - source_id: P5-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Section header.
    - source_id: P5-S2-C5
      disposition: represented
      result_indexes:
      - 0
      reason: Reports overall-language gains by frequency for age groups.
    - source_id: P5-S2-C6
      disposition: represented
      result_indexes:
      - 1
      reason: Reports absence of auditory comprehension gains for low frequency.
    - source_id: P5-S2-C7
      disposition: represented
      result_indexes:
      - 1
      reason: Reports significant auditory comprehension gains for age groups by frequency.
    - source_id: P5-S2-C8
      disposition: represented
      result_indexes:
      - 2
      reason: Reports functional communication gains by frequency for age groups.
    - source_id: P5-S2-C10
      disposition: represented
      result_indexes:
      - 3
      - 4
      reason: Reports overall-language and auditory comprehension gains for working-age
        by intensity.
    - source_id: P5-S2-C11
      disposition: represented
      result_indexes:
      - 3
      - 4
      reason: Reports overall-language and auditory comprehension gains for older
        participants by intensity.
    - source_id: P5-S2-C12
      disposition: represented
      result_indexes:
      - 5
      reason: Reports functional communication gains by intensity for age groups.
    - source_id: P5-S2-C14
      disposition: represented
      result_indexes:
      - 6
      reason: Reports overall-language gains by dosage for age groups.
    - source_id: P5-S3-C1
      disposition: repeated
      result_indexes:
      - 6
      reason: Restatement of overall-language dosage gains.
    - source_id: P5-S3-C2
      disposition: represented
      result_indexes:
      - 7
      reason: Reports auditory comprehension gains by dosage for age groups.
    - source_id: P5-S3-C3
      disposition: represented
      result_indexes:
      - 8
      reason: Reports functional communication gains by dosage for age groups.
    - source_id: P5-S3-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Section header.
    - source_id: P5-S3-C5
      disposition: represented
      result_indexes:
      - 9
      reason: Reports overall-language gains by frequency for early rehabilitation.
    - source_id: P5-S3-C6
      disposition: represented
      result_indexes:
      - 10
      - 11
      reason: Reports auditory comprehension and functional communication gains for
        early rehabilitation by frequency.
    - source_id: P5-S3-C7
      disposition: represented
      result_indexes:
      - 9
      - 10
      reason: Reports overall-language and auditory comprehension gains for late rehabilitation
        by frequency.
    - source_id: P5-S3-C8
      disposition: represented
      result_indexes:
      - 11
      reason: Reports absence of functional communication gains for late rehabilitation.
    - source_id: P5-S3-C10
      disposition: represented
      result_indexes:
      - 12
      reason: Reports overall-language gains for early rehabilitation by intensity.
    - source_id: P5-S3-C11
      disposition: represented
      result_indexes:
      - 12
      reason: Reports overall-language gains for late rehabilitation by intensity.
    - source_id: P5-S3-C12
      disposition: represented
      result_indexes:
      - 13
      reason: Reports auditory comprehension gains by intensity for chronicity.
    - source_id: P8-S1-C1
      disposition: represented
      result_indexes:
      - 13
      reason: Reports auditory comprehension gains regardless of timing by intensity.
    - source_id: P8-S1-C2
      disposition: represented
      result_indexes:
      - 14
      reason: Reports functional communication gains for early vs late rehabilitation
        by intensity.
    - source_id: P8-S1-C4
      disposition: represented
      result_indexes:
      - 15
      - 16
      reason: Reports overall-language and functional communication gains for early
        rehabilitation by dosage.
    - source_id: P8-S1-C5
      disposition: represented
      result_indexes:
      - 15
      - 16
      reason: Reports overall-language and auditory comprehension gains for late rehabilitation
        by dosage.
    - source_id: P8-S1-C6
      disposition: represented
      result_indexes:
      - 17
      reason: Reports absence of functional communication gains for late rehabilitation
        by dosage.
    - source_id: P8-S1-C8
      disposition: represented
      result_indexes:
      - 18
      - 19
      - 20
      reason: Reports moderate-severe aphasia gains by frequency.
    - source_id: P8-S1-C9
      disposition: represented
      result_indexes:
      - 19
      reason: Reports auditory comprehension gains for moderate-severe aphasia by
        frequency.
    - source_id: P8-S1-C10
      disposition: represented
      result_indexes:
      - 18
      - 20
      reason: Reports mild-moderate aphasia gains by frequency.
    - source_id: P8-S1-C13
      disposition: represented
      result_indexes:
      - 21
      reason: Reports overall-language gains for moderate-severe aphasia by intensity.
    - source_id: P8-S1-C14
      disposition: represented
      result_indexes:
      - 22
      reason: Reports auditory comprehension gains for moderate-severe aphasia by
        intensity.
    - source_id: P8-S1-C15
      disposition: represented
      result_indexes:
      - 21
      reason: Reports overall-language gains for mild-moderate aphasia by intensity.
    - source_id: P8-S1-C16
      disposition: represented
      result_indexes:
      - 23
      reason: Reports functional communication gains for mild-moderate aphasia by
        intensity.
    - source_id: P8-S1-C19
      disposition: represented
      result_indexes:
      - 24
      reason: Reports overall-language gains for moderate-severe aphasia by dosage.
    - source_id: P8-S2-C3
      disposition: repeated
      result_indexes:
      - 24
      reason: Restatement of overall-language dosage gains for moderate-severe.
    - source_id: P8-S2-C4
      disposition: represented
      result_indexes:
      - 24
      reason: Reports overall-language gains for mild-moderate aphasia by dosage.
    - source_id: P8-S2-C5
      disposition: represented
      result_indexes:
      - 25
      reason: Reports absence of auditory comprehension gains for mild-moderate aphasia
        by dosage.
    - source_id: P8-S2-C6
      disposition: represented
      result_indexes:
      - 25
      - 26
      reason: Reports auditory comprehension and functional communication gains for
        moderate-severe aphasia by dosage.
    - source_id: P8-S2-C7
      disposition: represented
      result_indexes:
      - 26
      reason: Reports functional communication gains for mild-moderate aphasia by
        dosage.
    - source_id: P8-S2-C10
      disposition: represented
      result_indexes:
      - 27
      reason: Reports overall-language gains for females by frequency.
    - source_id: P8-S2-C11
      disposition: represented
      result_indexes:
      - 27
      - 29
      reason: Reports overall-language and functional communication gains for males
        by frequency.
    - source_id: P8-S2-C12
      disposition: represented
      result_indexes:
      - 29
      reason: Reports functional communication gains for females by frequency.
    - source_id: P8-S2-C13
      disposition: represented
      result_indexes:
      - 28
      reason: Reports auditory comprehension gains for both sexes by frequency.
    - source_id: P8-S2-C14
      disposition: represented
      result_indexes:
      - 28
      reason: Reports absence of auditory comprehension gains for low frequency by
        sex.
    - source_id: P8-S2-C16
      disposition: represented
      result_indexes:
      - 30
      - 31
      - 32
      reason: Reports overall-language, functional communication, and auditory comprehension
        gains for females by intensity.
    - source_id: P8-S2-C17
      disposition: represented
      result_indexes:
      - 31
      reason: Reports auditory comprehension gains for females by intensity.
    - source_id: P8-S2-C18
      disposition: represented
      result_indexes:
      - 30
      reason: Reports overall-language gains for females by intensity.
    - source_id: P8-S2-C19
      disposition: represented
      result_indexes:
      - 30
      - 31
      - 32
      reason: Reports overall-language, auditory comprehension, and functional communication
        gains for males by intensity.
    - source_id: P8-S2-C20
      disposition: repeated
      result_indexes:
      - 30
      - 31
      reason: Restatement of male gains by intensity.
    - source_id: P8-S2-C21
      disposition: represented
      result_indexes:
      - 31
      reason: Reports absence of auditory comprehension gains for males at low intensity.
    - source_id: P8-S3-C3
      disposition: represented
      result_indexes:
      - 33
      reason: Reports overall-language gains for both sexes by dosage.
    - source_id: P8-S3-C4
      disposition: represented
      result_indexes:
      - 34
      reason: Reports auditory comprehension gains for both sexes by dosage.
    - source_id: P8-S3-C5
      disposition: represented
      result_indexes:
      - 34
      reason: Reports absence of auditory comprehension gains for low dosage by sex.
    - source_id: P8-S3-C6
      disposition: represented
      result_indexes:
      - 35
      reason: Reports functional communication gains for females by dosage.
    - source_id: P8-S3-C7
      disposition: represented
      result_indexes:
      - 35
      reason: Reports functional communication gains for males by dosage.
    - source_id: P6-S1-C3
      disposition: represented
      result_indexes:
      - 0
      - 1
      - 2
      - 3
      - 4
      - 5
      - 6
      - 7
      - 8
      - 9
      - 10
      - 11
      - 12
      - 13
      - 14
      - 15
      - 16
      - 17
      - 18
      - 19
      - 20
      - 21
      - 22
      - 23
      - 24
      - 25
      - 26
      - 27
      - 28
      - 29
      - 30
      - 31
      - 32
      - 33
      - 34
      - 35
      reason: Indispensable table containing the primary data for all subgroup associations.
    - source_id: P7-S1-C1
      disposition: represented
      result_indexes:
      - 2
      - 5
      - 8
      - 11
      - 14
      - 17
      - 20
      - 23
      - 26
      - 29
      - 32
      - 35
      reason: Indispensable table continuation for functional communication outcomes.
    unresolved_coverage:
    - source_id: P5-S2-C4
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P5-S3-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P5-S3-C4
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P8-S1-C19
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P6-S1-C3
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P7-S1-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P8-S1-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S1-C17
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S3-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S1-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S1-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S1-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S1-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S1-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S2-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S2-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S2-C14
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S3-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S3-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S3-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S3-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S1-C1
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P2-S2-C5
    - P2-S2-C6
    - P2-S2-C7
    - P2-S2-C8
    - P2-S2-C9
    - P3-S1-C1
    - P3-S1-C2
    - P3-S1-C3
    - P3-S1-C4
    - P5-S2-C3
    - P8-S1-C11
    - P8-S1-C17
    - P8-S3-C9
    - P9-S1-C2
    - P9-S1-C3
    - P9-S1-C4
    - P9-S1-C5
    - P9-S1-C6
    - P9-S2-C4
    - P9-S2-C10
    - P9-S2-C14
    - P9-S3-C2
    - P9-S3-C6
    - P9-S3-C9
    - P9-S3-C10
    - P10-S1-C1
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-6-1
    - TABLE-1-page-7-2
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P2-S2-C4
      recruited_sample:
      - P2-S1-C5
      eligibility:
      - P4-S1-C3
      - P4-S1-C5
      - P4-S1-C6
      - P4-S1-C8
      - P4-S2-C8
      imaging_provenance: []
      imaging_timing: []
      outcome_timing: []
      outcome_definition: []
      validation: []
      analysis_restrictions:
      - P4-S1-C6
      dependent_variable_statement:
      - P2-S1-C4
      - P2-S1-C8
      - P4-S1-C1
      - P4-S3-C4
      limitations: []
      personal_factors:
      - P2-S1-C4
      - P2-S1-C9
      - P4-S2-C2
      - P5-S1-C4
      - P5-S1-C5
      - P5-S1-C7
      tested_personal_effects: []
      adjustment_roles:
      - P2-S1-C3
      - P2-S1-C8
      - P3-S3-C2
      - P5-S1-C4
      - P9-S2-C11
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P2-S1-C9
      - P4-S2-C2
      - P5-S1-C7
      - P5-S2-C2
    outcome_type: both_reported
    imaging_vs_outcome: not_stated
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P5-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: tested_personal_effects
      source_id: P2-S1-C4
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P2-S1-C9
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P4-S1-C1
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P5-S1-C5
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P9-S3-C3
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P9-S3-C5
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: outcome_timing
      source_ids:
      - P2-S1-C8
      - P4-S1-C1
      - P4-S2-C3
      - P4-S3-C9
      - P5-S1-C5
      - P5-S2-C3
      - P5-S3-C10
      - P8-S1-C1
      - P8-S1-C5
      - P8-S1-C6
      - P8-S1-C9
      - P8-S3-C9
      - P9-S1-C3
      - P9-S2-C4
      - P9-S2-C8
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: outcome_definition
      source_ids:
      - P2-S1-C8
      - P4-S1-C1
      - P4-S2-C3
      - P4-S3-C9
      - P5-S1-C5
      - P5-S2-C3
      - P5-S3-C10
      - P8-S1-C1
      - P8-S1-C5
      - P8-S1-C6
      - P8-S1-C9
      - P8-S3-C9
      - P9-S1-C3
      - P9-S2-C4
      - P9-S2-C8
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: limitations
      source_ids:
      - P3-S2-C2
      - P9-S2-C2
      - P9-S2-C5
      - P9-S2-C6
      - P9-S2-C7
      - P9-S2-C9
      - P9-S2-C10
      - P9-S2-C11
      - P9-S2-C12
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: tested_personal_effects
      source_ids:
      - P3-S1-C3
      - P3-S1-C4
      - P5-S2-C3
      - P5-S3-C5
      - P5-S3-C7
      - P8-S1-C8
      - P8-S1-C10
      - P8-S1-C13
      - P8-S1-C15
      - P8-S2-C10
      - P8-S2-C11
      - P8-S2-C12
      - P8-S2-C16
      - P8-S2-C19
      - P8-S2-C21
      - P8-S3-C3
      - P8-S3-C4
      - P8-S3-C6
      - P8-S3-C7
      - P9-S1-C2
      - P9-S1-C3
      - P9-S1-C4
      - P9-S1-C5
      - P9-S1-C6
      - P9-S3-C10
      - P10-S1-C1
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
      pdf_sha256: e949dbbd260ec0b118b5f7b73f911fb02f061b9e14e4b1cc7810746cb96f4f3b
      review_sha256: 2c072f1d3d6796096337485830f5b0eb82f8afa37a43f0c8c71305987f9164d6
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
      - P8-S1-C4
      - P8-S1-C5
      source_result: In the early-SLT group (≤3 months post-onset), the greatest overall-language
        gains were observed for 20–50 SLT-h. In the late-SLT group (>3 months post-onset),
        the only significant overall-language gain from baseline occurred for >50
        SLT-h.
      result_status: detected
      patient_measurement: non_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis corresponds to the 'Chronicity and SLT Dosage'
            subgroup analysis described in the source. P8-S1-C4 and P8-S1-C5 explicitly
            detail the findings for early vs. late SLT groups regarding dosage and
            overall-language ability, matching the proposed core's focus.
          source_ids:
          - P8-S1-C4
          - P8-S1-C5
          - P2-S1-C9
        direction:
          answer: fits
          reason: The source states that greatest gains for early-SLT were at 20-50h
            and the only significant gain for late-SLT was at >50h. The proposed claim
            accurately reflects these specific dosage thresholds associated with significant
            or greatest gains, preserving the detected association direction.
          source_ids:
          - P8-S1-C4
          - P8-S1-C5
        construct:
          answer: fits
          reason: Exposure is SLT dosage (total hours), outcome is overall-language
            ability (measured by WAB-AQ as per P4-S2-C6), and population is stroke-related
            aphasia. The measurement is non-imaging (clinical language assessment),
            correctly identified as non_imaging rather than diffusion or template
            overlap.
          source_ids:
          - P4-S2-C6
          - P2-S1-C7
          - P8-S1-C4
        qualifications:
          answer: fits
          reason: The proposed core includes the critical qualifiers defining the
            subgroups (early ≤3 months, late >3 months) and the adjustment covariates
            (age, sex, severity, time post-onset). It also includes relevant limitations
            regarding English predominance and baseline-to-follow-up timing.
          source_ids:
          - P2-S1-C9
          - P5-S1-C4
          - P9-S2-C8
          - P9-S3-C6
        missing_material_caveat:
          answer: fits
          reason: No material caveats are omitted that would change the interpretation.
            The distinction between 'greatest gains' (early) and 'only significant
            gain' (late) is preserved. The limitation regarding pre-randomization
            SLT data unavailability is included.
          source_ids:
          - P9-S2-C9
          - P8-S1-C4
          - P8-S1-C5
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
      id: R016
      exposure:
        text: SLT dosage (total hours)
      outcome:
        text: overall-language ability
      analysis_label: Chronicity and SLT Dosage
      relation: association
      evidence_ids:
      - P8-S1-C4
      - P8-S1-C5
      qualifier_ids:
      - P6-S1-C3
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: e949dbbd260ec0b118b5f7b73f911fb02f061b9e14e4b1cc7810746cb96f4f3b
        source_review: _compare/relationships-2026-11-16/review-current/Brady2022
        source_status_sha256: 293de3f879f6ad3a5c594ea25f2aa2c552e7da2bf2c71e9c94fc49b877cb38c8
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P2-S2-C4:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: e949dbbd260ec0b118b5f7b73f911fb02f061b9e14e4b1cc7810746cb96f4f3b
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 8d2e6f92ae711bf0ef4855b6f42ae8110a94cf9ce39c41ab30fc5af56a4ced09
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S2-C4
          page: 2
          text_layer_sha256: 8d2e6f92ae711bf0ef4855b6f42ae8110a94cf9ce39c41ab30fc5af56a4ced09
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Results: 959 IPD (25 RCTs) were analyzed.'
        anchor_text: 'Results: 959 IPD (25 RCTs) were analyzed.'
        excluded_fragments: []
        image_sha256: 2be8d83b892950a065b34685d433445829f2d2b84a02f4d2a49fde651b7f04bc
        transcription: 'Results: 959 IPD (25 RCTs) were analyzed'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 8
  quote: "The early-SLT group achieved their greatest over-\nall-language and functional\
    \ communication gains for 20–\n50 SLT-h; auditory comprehension gains were not\
    \ observed \nat any dosage."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-20'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
