---
id: wmh_atr_forceps_minor_volume
name: WMH volume in the ATR and forceps minor cluster
kind: network
findings:
- id: f1
  target: processing_speed_executive_functioning
  target_kind: impairment
  claim: WMH volume in the forceps minor and ATR explained two to three times more
    variance in processing speed and executive functioning than total WMH volume.
  direction: likely
  relationship: correlational
  method: LSM
  sample:
    n: not_reported
    population: memory clinic patients with small vessel disease (SVD)
    phase: not_reported
    time_post_onset: cross-sectional
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - cross-sectional lesion-symptom mapping does not prove causality
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Patient lesion overlap with population/reference tract
    templates for the anterior thalamic radiation (ATR) and forceps minor, with sum
    lesion volume calculated for each ROI. finding is independent of total lesion
    burden. Additional metadata has not been transcribed; review the pending-field
    flags before approval.'
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
    - not_transcribed:sample.n
    - proposed_concept:processing_speed_executive_functioning
  citation: '@Biesbroek2017'
  source_passages:
  - section: Original source P6-S2-C7
    page: 6
    quote: 'In this analysis, WMH volume in the forceps minor and ATR explained two
      to three times more variance in

      processing speed and executive functioning than total WMH volume [64].'
    supports: claim
  - section: Original source P6-S2-C6
    page: 6
    quote: 'In one particular study in memory clinic patients with SVD, the

      variance in cognitive functioning explained by regional and total WMH volume
      were additionally directly compared

      [64].'
    supports: sample
  - section: Original source P5-S1-C10
    page: 5
    quote: 'In the ROI-based approach, the sum lesion volume is

      calculated for each ROI (for example, a specific cortical gyrus, a subcortical
      nucleus or a white matter tract) and

      subsequently related to cognitive functioning using statistical models.'
    supports: method
  - section: Original source P6-S3-C7
    page: 6
    quote: 'As such, the observed associations between WMH and lacune location and
      cognitive function-

      ing in cross-sectional lesion–symptom mapping studies do not prove causality.'
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-20'
relationship_review:
  paper: Biesbroek2017
  proposal_id: R024
  review_status_sha256: 911e35bf4806eea150d96d358eb72d4544f378a25f66178a000e02e581e2aaad
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 3ea3ce26a31cec57a11d684730925dbff173d0b8a14a5666a8a89e0b8bc35f30
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 3ea3ce26a31cec57a11d684730925dbff173d0b8a14a5666a8a89e0b8bc35f30
        A/passages.json: 0c23784af28e5024949fa7c35005333972be1082bc497f5274536016cf51f178
        A/raw.json: 46650387199a6cb3d4c0977a6cd933e81e35e61cf4ac3d5964f1db8a956faccf
        A/source-units.json: fcc08b243e0f8e0375e7184a572ac7892f8115b21136bbfecd1c3150a7b9f80c
        A/full-source-units.json: f6b0741d5b4ae36cce37bd08f7c06040499dd73f64e34578324202de6b973247
        A/meta.json: 897cbf06513cf3297fc7a6a402efb53856c7c7b410e11c738b8ae6daf8b3d65d
        A/table-images/TABLE-1-page-7-1.png: 1cc18339916106b9746a16730d4e055b5e1450fc4e5a8b7c26d6d95b078a7905
        A/table-images/page-7.png: 4e44ae552a28b5db5cd661b56946ee29b683b9d3c8434ce177b22bc231d08f35
        A/table-images/TABLE-1-page-8-1.png: 1bd224c793a9e4168bcaaa6bff10d57d45a3dd788d99088b162b88516c069239
        A/table-images/page-8.png: 0ce7c08a671cbf56f2e2652611c4bc9ce9917fd49bbe8e95d2d1605b2d1898b6
        A/table-images/manifest.json: e55303c6e44a8c313389cb6ca24e5a6fc9eecdbca70a1e09e18fb0576c60f64d
        A/clauses/window-03/raw.json: 20a665d7fdf7ce63ce86d8d105ca2631426c7eb33048546a8a270c5cbf5c5f53
        A/clauses/window-03/prompt.txt: 6ad3ac63c72e6b1c1502c78e581ed2ffaa5d94d7c0d96ceef1237bc777d2c141
        A/clauses/window-03/meta.json: 43fccc7ea184636cb2cd0caf135c6fc9efd3e238dea7531155cde57638357a4f
        A/clauses/window-04/raw.json: 4d35e47b7cde590b50426b1b279e77b8cf6d2e4c78f0bce7c731dce94bb74add
        A/clauses/window-04/prompt.txt: d410703fa9618aa174d65fef26cd20749ec8e1cd693a688cefa08e326f7a9580
        A/clauses/window-04/meta.json: 451a8259eec95d1a05a52728f9caa09e78bfa7d95457435c4e508942e423b662
        A/clauses/window-05/raw.json: 4705445feba1e5e5af35b48bd183f882c85981d7aebc83563879e61a3282a4f5
        A/clauses/window-05/prompt.txt: c840cdc29018dc8515a3e055ab1bfb39d9d58261fff24ad9f433f6db79378de4
        A/clauses/window-05/meta.json: 457dbc78c31cd70392d7a45e926f16e607373e866be4d79e0ed06f8d1bf5d6e2
        A/clauses/window-02/raw.json: 5723e8d5a33fa14053a7f5a7731ac816e76a86dad2b5e4d928d9f42b4b0cf927
        A/clauses/window-02/prompt.txt: d9eb9052a19e5c3f305c2cd4fc3e074f49f62564576a7e49bc880fe254924d99
        A/clauses/window-02/meta.json: af29ec8f85ddbe0d5b757e9ac550b506b23ea2956efaa08767176b8a264712d6
        A/clauses/window-07/raw.json: 64a11547734b0f302e5217f0df765f0d3bbeb1cda7fb6bb5fb7226c69169a489
        A/clauses/window-07/prompt.txt: e033d7480a2b08c61d20f7f75720c7a3b890056119094894a1138d909685ed16
        A/clauses/window-07/meta.json: 9104f82ac0828e93d6103679168928c4a863f992be1c2fb4619255b6a13d84b1
        A/clauses/window-01/raw.json: 3f522df453fdbbc1ce20f5c7a917607cd9437e943bd0aa4584b03007dada4058
        A/clauses/window-01/prompt.txt: 09fdec285048b8af19b73accbb4777171e8b987b0ca4ac51da1777f845f74bd7
        A/clauses/window-01/meta.json: f0eab81293ab4098934ab77efac769551e7643f75623153348743febef656d8a
        A/clauses/window-06/raw.json: cee664601a7bebeeaecb68d67f6cdbbcc157d21f746131eb6d8f4b1d385a63f0
        A/clauses/window-06/prompt.txt: 1e601b0ed9e3e3c7a24d4309c874528d79e9ebe2a032340068f71e84ee1b3e7f
        A/clauses/window-06/meta.json: 3582de875f44b5b7cfaee0f0967312939d785fa26ffbd2ecb2301ebd4d70a793
        A/clauses/window-08/raw.json: 17af73307293fa22b25401e563268cb27ca59bb5b9fe97b6bda224ab441c895f
        A/clauses/window-08/prompt.txt: ebe70d8ad297dd7b0648cc0f8ac48256a4ba52760f8d773e025f1d6f2a31ebe1
        A/clauses/window-08/meta.json: 0aebe634369f73f47f2886e85be14e10cce25b9a88268eca9db6b850d7f56f5f
        A/tables/TABLE-1-page-7-1/raw.json: 109dd9a169c6e773d31f68ef92ca904be2223396d43f45889da314a5b09f432c
        A/tables/TABLE-1-page-7-1/prompt.txt: 767d6e12160422da693fbca0c4804200cf8fb78e526cfea4cdee801959a6d198
        A/tables/TABLE-1-page-7-1/meta.json: 3a9a0e5cf40f116de218d23d57196f36c3d1960855911ae3520a0c873a916bab
        A/tables/TABLE-1-page-8-2/raw.json: 00270cfbe37cc771a1442e34cf05676b84f84299e0a081470470171f10c8bcf9
        A/tables/TABLE-1-page-8-2/prompt.txt: cfaf826853407fc9f3a74b43e9e4701e539f7ca55d7f87017fdef7cfc766d35c
        A/tables/TABLE-1-page-8-2/meta.json: 694c4094b89333c6e8be582451b222cf41046bff764f3392c1bac01f9f2d5da8
        B/passages.json: 0c23784af28e5024949fa7c35005333972be1082bc497f5274536016cf51f178
        B/raw.json: 3a9af053fa14e94902c1018ddb58d76708f0befe35c01e361ba47d47278e9b08
        B/source-units.json: fcc08b243e0f8e0375e7184a572ac7892f8115b21136bbfecd1c3150a7b9f80c
        B/full-source-units.json: f6b0741d5b4ae36cce37bd08f7c06040499dd73f64e34578324202de6b973247
        B/meta.json: b4358407c2bbafb386ca0b15f57bbcc9df1a39206d5719ccf486390ce138badc
        B/table-images/TABLE-1-page-7-1.png: 1cc18339916106b9746a16730d4e055b5e1450fc4e5a8b7c26d6d95b078a7905
        B/table-images/page-7.png: 4e44ae552a28b5db5cd661b56946ee29b683b9d3c8434ce177b22bc231d08f35
        B/table-images/TABLE-1-page-8-1.png: 1bd224c793a9e4168bcaaa6bff10d57d45a3dd788d99088b162b88516c069239
        B/table-images/page-8.png: 0ce7c08a671cbf56f2e2652611c4bc9ce9917fd49bbe8e95d2d1605b2d1898b6
        B/table-images/manifest.json: d7932d8df30879b2aec43f8552f5947945087da80d92a1e30ae0ebe19f5adff3
        B/clauses/window-03/raw.json: 13205a65b9642e7a94fdcd35b9a9e5f618e2d4fdf1c0d27fc16263f1e0a5c7f8
        B/clauses/window-03/prompt.txt: 6ad3ac63c72e6b1c1502c78e581ed2ffaa5d94d7c0d96ceef1237bc777d2c141
        B/clauses/window-03/meta.json: 256976a40a5333dc7212ff7bc6ea48279e457ac0c2c99b59dcf99ff795d82204
        B/clauses/window-04/raw.json: d19a26fc86859d7a22d7c3431a78147ae72f5291b733276ec904c507f04fdd81
        B/clauses/window-04/prompt.txt: d410703fa9618aa174d65fef26cd20749ec8e1cd693a688cefa08e326f7a9580
        B/clauses/window-04/meta.json: fdbe75d379d212977ff49f7cf8c7a0174e9437b75d472ba453cdda54b7e9d786
        B/clauses/window-05/raw.json: c1e1012420e9d872f885672e77d5811ee29a9a7324588100145aad7f19b85a5d
        B/clauses/window-05/prompt.txt: c840cdc29018dc8515a3e055ab1bfb39d9d58261fff24ad9f433f6db79378de4
        B/clauses/window-05/meta.json: cde2c8ae26ca2a71cb6ab1bafa6f3169f4fe072619beb9fd2870513d4feb2399
        B/clauses/window-02/raw.json: 561e9c7fb564354b6c74b0571f92860831d505db1936740fa5f00f71e46052cf
        B/clauses/window-02/prompt.txt: d9eb9052a19e5c3f305c2cd4fc3e074f49f62564576a7e49bc880fe254924d99
        B/clauses/window-02/meta.json: ea65b22e2ff17a975e465a3a8ae4d9a1b39968716dddb6aa40144fdf8a0f2dab
        B/clauses/window-07/raw.json: 63fe495750830600377728e14084d99a12b9ec67e081b565573637149ea67d4c
        B/clauses/window-07/prompt.txt: e033d7480a2b08c61d20f7f75720c7a3b890056119094894a1138d909685ed16
        B/clauses/window-07/meta.json: 550dc4d1625f2098cfdc986d159b17a4a5f0d4ce109c4d0db9800a5845d873dc
        B/clauses/window-01/raw.json: 646faa3084f4d7cd9b78a691a3bb33f56a1a96af105e89b89b46f03ab8e25961
        B/clauses/window-01/prompt.txt: 09fdec285048b8af19b73accbb4777171e8b987b0ca4ac51da1777f845f74bd7
        B/clauses/window-01/meta.json: d3f2bb198ca6d4e4a40fe5be3a29db90aaf0390717e818ca0f1b2d80403483d7
        B/clauses/window-06/raw.json: 976ab2cc0b24d5da117e32837d4dbaa1ab4f2ee4732280a53acbab6d0d84373d
        B/clauses/window-06/prompt.txt: 1e601b0ed9e3e3c7a24d4309c874528d79e9ebe2a032340068f71e84ee1b3e7f
        B/clauses/window-06/meta.json: 7a06b652857a2f94e32f004a6c1dc20678b0c2dcba2ef9af6ce3f27a05734e05
        B/clauses/window-08/raw.json: 1e6c8bfae4f2dd7406a6ec672339e56f11b2bc7607ceaf5a540590d31e206c8e
        B/clauses/window-08/prompt.txt: ebe70d8ad297dd7b0648cc0f8ac48256a4ba52760f8d773e025f1d6f2a31ebe1
        B/clauses/window-08/meta.json: 37242725661462a91e5951ddc972de84357aa854654d03226a383fb49fb4d4ed
        B/tables/TABLE-1-page-7-1/raw.json: 1197e66ebeb808273878d35a3e1343b897c890d5e1e987a1addf13b281c8bdc5
        B/tables/TABLE-1-page-7-1/prompt.txt: 767d6e12160422da693fbca0c4804200cf8fb78e526cfea4cdee801959a6d198
        B/tables/TABLE-1-page-7-1/meta.json: ff49ff7bbf59df079b255586be85bc4452aacc6e7776fbb84b10a87bb7d39342
        B/tables/TABLE-1-page-8-2/raw.json: 3deb24c399a6b25f0c45622d1cd0132d55013a807b66b5f2a25ef41408d908d9
        B/tables/TABLE-1-page-8-2/prompt.txt: cfaf826853407fc9f3a74b43e9e4701e539f7ca55d7f87017fdef7cfc766d35c
        B/tables/TABLE-1-page-8-2/meta.json: 44d2979f7c313ca574c3c9807a7d9e8fa42b0592b26014a9d810024f2bc01468
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
      pdf_sha256: 3ea3ce26a31cec57a11d684730925dbff173d0b8a14a5666a8a89e0b8bc35f30
      source_review: _compare/relationships-2026-11-16/review-current/Biesbroek2017
      source_status_sha256: 34341d5358490fa0c88b440d4c8f7ad2d181dd00a175e5dce1f7a43e46ff3cbd
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R024
    exposure:
      text: WMH volume in the forceps minor and ATR
    outcome:
      text: processing speed and executive functioning
    analysis_label: Variance comparison
    relation: sensitivity
    evidence_ids:
    - P6-S2-C7
    qualifier_ids:
    - P6-S2-C6
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 3ea3ce26a31cec57a11d684730925dbff173d0b8a14a5666a8a89e0b8bc35f30
      source_review: _compare/relationships-2026-11-16/review-current/Biesbroek2017
      source_status_sha256: 34341d5358490fa0c88b440d4c8f7ad2d181dd00a175e5dce1f7a43e46ff3cbd
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues: []
      unattached_null_or_qualifier_ids:
      - P10-S1-C4
      - P10-S1-C5
      suppressed_nonrepresented_units: 1
      default_disposition_count_requires_completeness_check: 186
      unselected_timing_passages: []
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: limitations
        source_ids:
        - P2-S1-C3
        - P2-S1-C4
        - P2-S1-C5
        - P2-S1-C8
        - P3-S2-C11
        - P3-S2-C12
        - P3-S2-C13
        - P4-S1-C12
        - P6-S3-C4
        - P6-S3-C7
        - P9-S3-C9
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - limitations
      - personal_factors
      - tested_personal_effects
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-7-1
      - TABLE-1-page-8-2
      unlinked_tables:
      - TABLE-1-page-7-1
      - TABLE-1-page-8-2
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P4-S1
        - P5-S1
        - P6-S2
        - P8-S1
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 3ea3ce26a31cec57a11d684730925dbff173d0b8a14a5666a8a89e0b8bc35f30
      source_review: _compare/relationships-2026-11-16/review-current/Biesbroek2017
      source_status_sha256: 34341d5358490fa0c88b440d4c8f7ad2d181dd00a175e5dce1f7a43e46ff3cbd
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P9-S2-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discusses cohort size requirements for hypothesis-free mapping.
    - source_id: P10-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient case history description.
    - source_id: P10-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient case history description.
    - source_id: P10-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient case history description.
    - source_id: P10-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient risk factor description.
    - source_id: P10-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient medical history description.
    - source_id: P10-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient clinical measurement.
    - source_id: P10-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient clinical examination.
    - source_id: P10-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient cognitive assessment results.
    - source_id: P10-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient diagnosis.
    - source_id: P10-S1-C15
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient-specific quantitative imaging data.
    - source_id: P10-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient-specific quantitative imaging data.
    - source_id: P11-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion statement.
    - source_id: P11-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: General summary of review findings.
    unresolved_coverage: []
    pending_source_ids:
    - P9-S2-C11
    - P10-S1-C3
    - P10-S1-C4
    - P10-S1-C5
    - P10-S1-C6
    - P10-S1-C7
    - P10-S1-C8
    - P10-S1-C9
    - P10-S1-C10
    - P10-S1-C11
    - P10-S1-C15
    - P10-S2-C2
    - P11-S1-C9
    - P11-S2-C6
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-7-1
    - TABLE-1-page-8-2
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P5-S2-C9
      - P7-S1-C5
      - P8-S1-C2
      recruited_sample:
      - P5-S2-C9
      eligibility:
      - P5-S2-C9
      imaging_provenance:
      - P4-S1-C11
      - P5-S1-C7
      - P8-S1-C5
      imaging_timing:
      - P6-S2-C11
      outcome_timing:
      - P6-S2-C11
      outcome_definition:
      - P5-S3-C2
      validation:
      - P11-S2-C3
      analysis_restrictions:
      - P6-S2-C5
      - P7-S1-C3
      dependent_variable_statement:
      - P6-S1-C6
      - P6-S1-C10
      - P6-S1-C12
      - P6-S2-C7
      limitations: []
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P4-S1-C15
      - P6-S2-C5
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P7-S1-C5
      - P8-S1-C2
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: none_described
    held_selections:
    - slot: limitations
      source_ids:
      - P2-S1-C3
      - P2-S1-C4
      - P2-S1-C5
      - P2-S1-C8
      - P3-S2-C11
      - P3-S2-C12
      - P3-S2-C13
      - P4-S1-C12
      - P6-S3-C4
      - P6-S3-C7
      - P9-S3-C9
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
      pdf_sha256: 3ea3ce26a31cec57a11d684730925dbff173d0b8a14a5666a8a89e0b8bc35f30
      review_sha256: 911e35bf4806eea150d96d358eb72d4544f378a25f66178a000e02e581e2aaad
      code_sha256: c4650d24fa3e36e6f317cb65cc7626277a28936a7cdf5d07248d4b1e5bfa09aa
      source_helpers_sha256: e0e0f295e5efa1fdb4e9e8c84ca491d062df3aefe8ca8b4d9ca85fcb6d4c9082
      converter_sha256: 048f1e35905528676837a00b1b2406b1c97cb1eb47c48d63f121a5c00cc0afeb
      table_helpers_sha256: 78e562e9725fc484d6a12279ea710856dfd1d9aa13ee178d0358e9c0acdd2c8c
      mapper_budget: 2500
      reviewer_budget: 1600
      approved: false
      visual:
        models:
        - gemma4:31b
        - qwen3.8:27b
        digests:
        - 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        - 47951e4a666180bc2aedfc93c169472f2de783696fe196efbf063f5730ecf163
        code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
        layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
    approved: false
    core_review:
      own_result_source_ids:
      - P6-S2-C7
      source_result: In a specific study of memory clinic patients with SVD, WMH volume
        in the forceps minor and ATR explained two to three times more variance in
        processing speed and executive functioning than total WMH volume.
      result_status: model_comparison
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The source explicitly describes a variance comparison between regional
            WMH volume (ATR/forceps minor) and total WMH volume for the same outcomes
            (processing speed and executive functioning) in the same population (memory
            clinic SVD patients).
          source_ids:
          - P6-S2-C6
          - P6-S2-C7
        direction:
          answer: fits
          reason: The source states that regional volume explained 'two to three times
            more variance' than total volume, which aligns with the draft's claim
            of greater explanatory power for the specific tracts.
          source_ids:
          - P6-S2-C7
        construct:
          answer: fits
          reason: The exposure is correctly identified as WMH volume in ATR and forceps
            minor. The outcome is processing speed and executive functioning. The
            method is described as ROI-based analysis (sum lesion volume in ROIs),
            which corresponds to template_lesion_overlap (patient lesions overlaid
            on reference tract maps), not patient_diffusion.
          source_ids:
          - P5-S1-C10
          - P6-S2-C7
        qualifications:
          answer: fits
          reason: The draft includes the qualification that the finding is independent
            of total lesion burden, which is supported by the context that the variance
            comparison specifically contrasts regional volume against total volume,
            and the broader section notes that associations were independent of global
            lesion volume in most studies.
          source_ids:
          - P6-S2-C5
          - P6-S2-C6
        missing_material_caveat:
          answer: fits
          reason: The draft includes the limitation that cross-sectional design does
            not prove causality, which is a material caveat explicitly stated in the
            source (P6-S3-C7). No other material caveats are omitted that would change
            the interpretation of this specific variance comparison.
          source_ids:
          - P6-S3-C7
      optional_pending: []
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    normalizations:
    - field: bucket
      original: predictors
      action: route_from_kind
      value: regions
    analysis_identity:
      id: R024
      exposure:
        text: WMH volume in the forceps minor and ATR
      outcome:
        text: processing speed and executive functioning
      analysis_label: Variance comparison
      relation: sensitivity
      evidence_ids:
      - P6-S2-C7
      qualifier_ids:
      - P6-S2-C6
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 3ea3ce26a31cec57a11d684730925dbff173d0b8a14a5666a8a89e0b8bc35f30
        source_review: _compare/relationships-2026-11-16/review-current/Biesbroek2017
        source_status_sha256: 34341d5358490fa0c88b440d4c8f7ad2d181dd00a175e5dce1f7a43e46ff3cbd
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings: {}
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 6
  quote: 'In this analysis, WMH volume in the forceps minor and ATR explained two
    to three times more variance in

    processing speed and executive functioning than total WMH volume [64].'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-20'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
