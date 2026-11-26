---
id: left_stg_tpj_cluster
name: left superior temporal gyrus and temporo-parietal junction cluster
kind: network
findings:
- id: f1
  target: aphasia_severity
  target_kind: impairment
  claim: A cluster of ADC decrease in the left superior temporal gyrus and left temporo-parietal
    junction was associated with greater aphasia severity at three months post-stroke.
  direction: likely
  relationship: correlational
  method: VBM
  sample:
    n: 19
    population: French native speakers with first-ever left middle cerebral artery
      territory stroke and persistent aphasia at day 1
    phase: not_reported
    time_post_onset: ADC measured at 24 hours post-stroke; outcome measured at 3 months
      post-stroke
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Small sample size limiting generalizability
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: voxel-based decrease in Apparent Diffusion Coefficient
    (ADC) measured 24 hours post-stroke. Analysis was age-corrected; Results remained
    stable when adding gender and educational level as covariates. Additional metadata
    has not been transcribed; review the pending-field flags before approval. PDF
    image reading (P3-S2-C11, two-model agreement, human verification pending): Results


    We included 19 patients in the study Original text-layer quotation is preserved
    below. PDF image reading (P2-S2-C9, two-model agreement, human verification pending):
    ART scores were recorded at the acute phase (at day 1 post stroke = ART 1; at
    day 7 post stroke = ART 7) and the chronic phase (at 3 months post stroke = ART
    M3; at 6 months post stroke = ART M6) Original text-layer quotation is preserved
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
    - proposed_concept:aphasia_severity
  citation: '@Zavanone2018'
  source_passages:
  - section: Original source P4-S1-C7
    page: 4
    quote: 'Brain areas related to long-term aphasia outcome

      The regions associated with greater aphasia severity evaluated with

      the ART at three months were also located in a single cluster, mainly at

      the level of the left superior temporal gyrus (STG) and reached the left

      temporo-parietal junction (Figs. 2B, 3B, Table 2).'
    supports: claim
  - section: Original source P2-S1-C2
    page: 2
    quote: 'We aimed to identify these critical brain regions using Apparent

      Diﬀusion Coeﬃcient (ADC) maps derived from routine diﬀusion-

      weighted imaging (DWI) magnetic resonance imaging (MRI) obtained

      24 h after stroke onset in aphasic patients.'
    supports: method
  - section: Original source P3-S1-C10
    page: 3
    quote: 'Voxel-based analysis

      We performed a voxel-based multiple regression analysis using

      SPM8 with the smoothed, normalized images with language scores as

      variables of interest (ART scores: ART 7, ART M3, ART M6) and age as a

      confounding variable.'
    supports: method
  - section: Original source P2-S2-C5
    page: 2
    quote: 'Subjects

      Patients admitted to the stroke unit of Pitié-Salpêtrière Hospital

      were prospectively recruited according to the following criteria: (i)

      presence of their ﬁrst-ever stroke in the left middle cerebral territory,

      (ii) age ≥18 years and < 85 years, (iii) French native speaker, (iv)

      persistent aphasia at day 1 post stroke (≥1 point in the language items

      of the Aphasia Rapid Test [ART]), (v) no contraindications for MRI, (vi)

      no severe white matter lesions (Fazekas score < 3) and (vii) right-

      handedness.'
    supports: sample
  - section: Original source P3-S2-C11
    page: 3
    quote: 'Results

      We included 19 patients in the study.'
    supports: sample
  - section: Original source P2-S2-C9
    page: 2
    quote: 'ART scores were recorded at the acute phase (at day 1 post

      stroke = ART 1; at day 7 post stroke = ART 7) and the chronic phase

      (at 3 months post stroke = ART M3; at 6 months post stroke = ART

      M6).'
    supports: claim
  - section: Original source P5-S1-C3
    page: 5
    quote: 'When adding gender and educational level as supplementary cov-

      ariates, the localization of the signiﬁcant clusters did not change (see

      Supplementary Table 3 and Supplementary Fig. 1-panels A, B and C).'
    supports: confounders
  - section: Original source P6-S1-C5
    page: 6
    quote: 'First, the number of subjects was

      relatively small, limiting the generalizability of the results.'
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-26'
relationship_review:
  paper: Zavanone2018
  proposal_id: R003
  review_status_sha256: 91c945f1a328fb2993d8d8a26eebccfe7ae840be1b04427021c8d2380aab2cb3
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: c332dcbc410f4d93f904af2ab354ca3efe61cecf4a05dae78504a88a0820040f
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: c332dcbc410f4d93f904af2ab354ca3efe61cecf4a05dae78504a88a0820040f
        A/passages.json: 76e3794aa3011ea93ea56fa6054ccc187b48c0cae51e8920ae441482c1df9aa0
        A/raw.json: 8ad8e34be2caa1085d4f27b5635094a9481ecf29d56866da3eda1b93abdfd415
        A/source-units.json: a9496eb4e95a6f5f210b52d1bafc1fba9ebb7ee84c87593eb4c60b3764f09d47
        A/full-source-units.json: 688f6ade05ac5ad5f862586374a3c5d3328b4e2affd24792c90b2512baed0aca
        A/meta.json: 7dd5890098fd513b51d74c1acf1fd1b0bd022565d7ea081690e76610d021e47d
        A/table-images/TABLE-1-page-2-1.png: a58e67b1753f13a36755e9590fad27c5f24601b0dc9e65362bf8003f6164ea72
        A/table-images/page-2.png: a02a1e5a0587eab6855ab6bf069effbd72a3e7cdf32b1a44bc024db0f2be63f1
        A/table-images/page-4.png: 531f0bfc89b44a500a268d50b47d4bb482eb2295a599c4a4a8cf05e426e432aa
        A/table-images/manifest.json: 861d6f488ead2061b299eb28639bf0b5c3efb7012ac907b8e2d9ed3070e9c0a4
        A/table-images/TABLE-2-page-4-1.png: 3257551b6dc0275478dae236700f24d5b71d79932ed47dbc0a7e491bdb1da1ae
        A/clauses/window-03/raw.json: c5ea9d6f20963d24b76bbb73095ef2f2c46297ec2281b5a1ced31f5eec2912f2
        A/clauses/window-03/prompt.txt: 751481f284541b0b4a550339f7ba436d1aa89b5701a656db9c59491d8d24ece9
        A/clauses/window-03/meta.json: 2b4ec5ebbec46b3acf18c169fdeceaba1d89a3e7614b800dc95282033a2dd275
        A/clauses/window-04/raw.json: 21b4c17a78888f2ceb0cab7b1babaa3e34e250468fab1ee9bbc31381b395109c
        A/clauses/window-04/prompt.txt: b90dbc7702e47375ccc85468f926b6b98f7a4fe80f010b6c90867da2eb43d1a1
        A/clauses/window-04/meta.json: a28573edfed3943f3232bd2dcfe100fee5a001a876296f6f6119b76803332f9f
        A/clauses/window-05/raw.json: b7a4907a4d522e7a89c2b63b29bbe31cd717950250b94783009f7fd50827f1ba
        A/clauses/window-05/prompt.txt: 92a1a856ace774bc9dd87a0653ea3077dbcf8caa8a1729ab1aa5a67b9d8e28b0
        A/clauses/window-05/meta.json: 3f7b8748d42df6039e05b5c87c6adb35fc2e01fd0ed9c75d1fb965f9649632f8
        A/clauses/window-02/raw.json: 1df5a48ab5c236bef4af752bc0cda9e515d528be65d6806e76c49a6479152466
        A/clauses/window-02/prompt.txt: bc9266a5d0385bc2be12ce4d2fcd3bfa8d36f8d75439f57efb1ddaaf1f0daeed
        A/clauses/window-02/meta.json: b0777583c377faaa098f0d77a890f9976657ed6613fc9b84982bb39341675eb4
        A/clauses/window-01/raw.json: 4fc9a8bfc9b0b8725182ec802c540e9bfa37e29f1dadffc761620e7a7d30ddaf
        A/clauses/window-01/prompt.txt: f784141ac0bc38260f028d3b2ab8ee30ba0b962b5ff10ae173f862cc1b270f4e
        A/clauses/window-01/meta.json: 2c15d8adcd6fd16ae53fbb2ca02d799200e08070eb2b255fa9843fd5ee7a6490
        A/clauses/window-06/raw.json: 283d30fbb23fa431bc310543b17effca934729d9618313ddbb106eba834dbdd3
        A/clauses/window-06/prompt.txt: b3444b3b94f2760c5138f5a5097791e07f70ade954a2c7599bb34b5a7053ff47
        A/clauses/window-06/meta.json: d50c2b4848e1bbec29ff37ae7c22905a573efba99635ed0a3fda23959e979980
        A/tables/TABLE-1-page-2-1/raw.json: ed520312ac41303928d85e02c141125d1c9edc384301b8722c0b630add92436f
        A/tables/TABLE-1-page-2-1/prompt.txt: 17dc515554aa13953dc025ed9b9766625d54267f4b9f813ea30c9a379a0b4889
        A/tables/TABLE-1-page-2-1/meta.json: 82ef792eddcd902ebaaf119fab6cbf85e1a07c21babfeb959a9bc2004c2cdbe8
        A/tables/TABLE-2-page-4-2/raw.json: 91bcade0703576f25e7b2a03d8eb42de55036c171eecb97b3f13c21e864263ef
        A/tables/TABLE-2-page-4-2/prompt.txt: 57d5c21dcd88056112d322233422c0fddee665036b9070998887cefad3a1f685
        A/tables/TABLE-2-page-4-2/meta.json: cbc3bb58d050aa3662a2aeceff6a093bb540d6bdd44bc9c4a2c2a7bec7f00fcb
        B/passages.json: 76e3794aa3011ea93ea56fa6054ccc187b48c0cae51e8920ae441482c1df9aa0
        B/raw.json: 32ca2a0a9990c2da3d6d9482480b7b908d399cba26fd884e917585b4663e4dfd
        B/source-units.json: a9496eb4e95a6f5f210b52d1bafc1fba9ebb7ee84c87593eb4c60b3764f09d47
        B/full-source-units.json: 688f6ade05ac5ad5f862586374a3c5d3328b4e2affd24792c90b2512baed0aca
        B/meta.json: f47db9a56cfe929e0c504abcb8774e359ab9779f577c6cdee5fc0bf1ae2a110b
        B/table-images/TABLE-1-page-2-1.png: a58e67b1753f13a36755e9590fad27c5f24601b0dc9e65362bf8003f6164ea72
        B/table-images/page-2.png: a02a1e5a0587eab6855ab6bf069effbd72a3e7cdf32b1a44bc024db0f2be63f1
        B/table-images/page-4.png: 531f0bfc89b44a500a268d50b47d4bb482eb2295a599c4a4a8cf05e426e432aa
        B/table-images/manifest.json: be1cf699951f292f84e5e9a28093398d3dff5ca89b3a8d31493eb5e6a3e946fd
        B/table-images/TABLE-2-page-4-1.png: 3257551b6dc0275478dae236700f24d5b71d79932ed47dbc0a7e491bdb1da1ae
        B/clauses/window-03/raw.json: c221a939d498696bb40db62b20e1a4a46c92d43f519b997f5d572a07e07a1b7b
        B/clauses/window-03/prompt.txt: 751481f284541b0b4a550339f7ba436d1aa89b5701a656db9c59491d8d24ece9
        B/clauses/window-03/meta.json: 35059eda7481f98a8e48fdc4776344106a3cabaed91b0a143c566e47dc84abff
        B/clauses/window-04/raw.json: 9c67539fa17b0e551d8ecdbf076b7a8128bf53b9991b54d25e10b866ea3ac833
        B/clauses/window-04/prompt.txt: b90dbc7702e47375ccc85468f926b6b98f7a4fe80f010b6c90867da2eb43d1a1
        B/clauses/window-04/meta.json: ca5b8d82dced9fe48d53db595f23a4179487fbc9229459db82af8302b4aa5f1c
        B/clauses/window-05/raw.json: 5f2af99052a0a07fd66cfef6aa97f2450b849606547f8eb91f8b38b3f8186616
        B/clauses/window-05/prompt.txt: 92a1a856ace774bc9dd87a0653ea3077dbcf8caa8a1729ab1aa5a67b9d8e28b0
        B/clauses/window-05/meta.json: d65114ee6f9c863084cb68f2d071ee0bfba2a15b78e5354447c16843cf8c4c26
        B/clauses/window-02/raw.json: 6ef59eab1765ab887d5a17aaa4b70dbc58dc10b62ec94f85f68d743cfa6890fb
        B/clauses/window-02/prompt.txt: bc9266a5d0385bc2be12ce4d2fcd3bfa8d36f8d75439f57efb1ddaaf1f0daeed
        B/clauses/window-02/meta.json: 8df984776c67644bb8737d786c08d9dc3f93a0247b4daa7fe97489d5d6736085
        B/clauses/window-01/raw.json: e5fa1c4a64e8e5b12127b9062d67365cb6187c9802ee38dc774a74ef5360917f
        B/clauses/window-01/prompt.txt: f784141ac0bc38260f028d3b2ab8ee30ba0b962b5ff10ae173f862cc1b270f4e
        B/clauses/window-01/meta.json: 38fa958e884820bae4ded526ce56652977c5f201fa1747306ff920acfb66c78a
        B/clauses/window-06/raw.json: e18073b71b294d149430cee124126a91de2bf4a6dc853219c0baf8e7104896da
        B/clauses/window-06/prompt.txt: b3444b3b94f2760c5138f5a5097791e07f70ade954a2c7599bb34b5a7053ff47
        B/clauses/window-06/meta.json: c32f4a5886717ee360e68878d60a7236c1769e5862f91bcb2b40f05f48e64dd7
        B/tables/TABLE-1-page-2-1/raw.json: 248cb62faff0013e0cd6fec8397bc4c8afc02c8884c8db08415f97c1ba4713de
        B/tables/TABLE-1-page-2-1/prompt.txt: 17dc515554aa13953dc025ed9b9766625d54267f4b9f813ea30c9a379a0b4889
        B/tables/TABLE-1-page-2-1/meta.json: e328583cb616ef46e2d9b63f8c9935071e73de9219c2c549b8944cabdc146702
        B/tables/TABLE-2-page-4-2/raw.json: 29f6a2a0257bac27d8824be30ae7ca66551ba313e5cc0814b0468d2363f212b6
        B/tables/TABLE-2-page-4-2/prompt.txt: 57d5c21dcd88056112d322233422c0fddee665036b9070998887cefad3a1f685
        B/tables/TABLE-2-page-4-2/meta.json: 0869a95e1c9cd04390b55223ccfa39e37fe988aa825dad1bc3d15b2e1ac57408
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
      pdf_sha256: c332dcbc410f4d93f904af2ab354ca3efe61cecf4a05dae78504a88a0820040f
      source_review: _compare/relationships-2026-11-16/review-current/Zavanone2018
      source_status_sha256: 432555854ddad981e39598598a5c47a3d17ab84ba6ea2d0650c08d752b609d52
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R003
    exposure:
      text: ADC decrease in left superior temporal gyrus (STG) and left temporo-parietal
        junction
    outcome:
      text: aphasia severity at 3 months (ART M3)
    analysis_label: voxel-based regression (long-term 3m)
    relation: association
    evidence_ids:
    - P4-S1-C7
    qualifier_ids:
    - P4-S2-C12
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: c332dcbc410f4d93f904af2ab354ca3efe61cecf4a05dae78504a88a0820040f
      source_review: _compare/relationships-2026-11-16/review-current/Zavanone2018
      source_status_sha256: 432555854ddad981e39598598a5c47a3d17ab84ba6ea2d0650c08d752b609d52
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P3-S2-C12
      - Result passage disposed without unit P3-S2-C14
      - Result passage disposed without unit P3-S2-C15
      - Result passage disposed without unit P3-S2-C18
      - Result passage disposed without unit P3-S2-C19
      - Unresolved source passage P3-S2-C20
      - Result passage disposed without unit P3-S3-C10
      - Result passage disposed without unit P3-S3-C8
      - Accounting without a linked unit P4-S1-C2
      - Accounting without a linked unit P4-S1-C3
      - Accounting without a linked unit P4-S1-C5
      - Accounting without a linked unit P4-S1-C6
      - Accounting without a linked unit P4-S1-C7
      - Unaccounted source passage P4-S1-C3
      - Unaccounted source passage P4-S1-C6
      - Unaccounted source passage P4-S1-C5
      - Unaccounted source passage P4-S1-C2
      - Unaccounted source passage P4-S1-C7
      - Result passage disposed without unit P5-S1-C3
      - Result passage disposed without unit P5-S1-C4
      - Result passage disposed without unit P5-S1-C5
      - Result passage disposed without unit P5-S1-C6
      - Result passage disposed without unit P5-S1-C7
      - Result passage disposed without unit P5-S1-C8
      - Result passage disposed without unit P5-S3-C3
      unattached_null_or_qualifier_ids:
      - P5-S1-C3
      - P5-S1-C4
      suppressed_nonrepresented_units: 14
      default_disposition_count_requires_completeness_check: 130
      unselected_timing_passages:
      - P2-S2-C5
      - P2-S2-C10
      - P3-S2-C13
      - P4-S2-C10
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P4-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P3-S2-C3
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      empty_frame_slots_require_confirmation:
      - validation
      - personal_factors
      - tested_personal_effects
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-2-1
      - TABLE-2-page-4-2
      unlinked_tables:
      - TABLE-1-page-2-1
      - TABLE-2-page-4-2
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P3-S2
        - P3-S3
        - P4-S1
        - P4-S2
        - P5-S1
        - P5-S3
        - P6-S2
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: c332dcbc410f4d93f904af2ab354ca3efe61cecf4a05dae78504a88a0820040f
      source_review: _compare/relationships-2026-11-16/review-current/Zavanone2018
      source_status_sha256: 432555854ddad981e39598598a5c47a3d17ab84ba6ea2d0650c08d752b609d52
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S2-C2
      disposition: represented
      result_indexes:
      - 0
      - 1
      - 2
      - 3
      - 4
      reason: Summary of findings regarding different streams for acute vs chronic
        outcomes.
    - source_id: P3-S2-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive statistic of EHI.
    - source_id: P3-S2-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive statistic of therapy sessions.
    - source_id: P3-S2-C15
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive count of patients withdrawn from therapy.
    - source_id: P3-S2-C18
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of infarct probability map.
    - source_id: P3-S2-C19
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of infarct location.
    - source_id: P3-S3-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive overlap count in insula.
    - source_id: P3-S3-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of supplementary lesions.
    - source_id: P3-S3-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of lesion visibility.
    - source_id: P4-S1-C2
      disposition: represented
      result_indexes:
      - 0
      reason: Identifies posterior insula cluster for ART 7.
    - source_id: P4-S1-C3
      disposition: represented
      result_indexes:
      - 0
      reason: Identifies Rolandic operculum and white matter for ART 7.
    - source_id: P4-S1-C5
      disposition: represented
      result_indexes:
      - 1
      reason: Links ART 7 area to UF and IFOF (ventral pathway).
    - source_id: P4-S1-C6
      disposition: represented
      result_indexes:
      - 1
      reason: Confirms ventral stream via fiber tracking for ART 7.
    - source_id: P4-S1-C7
      disposition: represented
      result_indexes:
      - 2
      reason: Identifies STG and temporo-parietal junction for ART M3.
    - source_id: P4-S1-C8
      disposition: represented
      result_indexes:
      - 2
      reason: Notes extension to temporo-parietal white matter for ART M3.
    - source_id: P4-S1-C9
      disposition: represented
      result_indexes:
      - 3
      reason: Notes more pronounced area for ART M6.
    - source_id: P4-S1-C10
      disposition: represented
      result_indexes:
      - 4
      reason: Links ART M6 area to both ventral and dorsal pathways.
    - source_id: P4-S1-C11
      disposition: represented
      result_indexes:
      - 4
      reason: Confirms both streams via fiber tracking for ART M6.
    - source_id: P4-S1-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation of shift in figures.
    - source_id: P5-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of area shift.
    - source_id: P5-S1-C2
      disposition: represented
      result_indexes:
      - 1
      - 4
      reason: Synthesizes ventral stream for initial and both streams for poor outcome.
    - source_id: P5-S1-C3
      disposition: represented
      result_indexes:
      - 6
      reason: Null effect of gender and education on cluster localization.
    - source_id: P5-S1-C4
      disposition: represented
      result_indexes:
      - 7
      reason: Strengthened results when adding therapy as covariate.
    - source_id: P5-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion summary of findings.
    - source_id: P5-S1-C6
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of ART 7 findings.
    - source_id: P5-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison to infarct map.
    - source_id: P5-S1-C8
      disposition: repeated
      result_indexes:
      - 1
      reason: Restatement of ventral stream disconnection.
    - source_id: P5-S2-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: General discussion of disconnection concept.
    - source_id: P5-S3-C2
      disposition: repeated
      result_indexes:
      - 2
      - 3
      reason: Restatement of chronic stage localization.
    - source_id: P5-S3-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of STG role.
    - source_id: P6-S1-C1
      disposition: repeated
      result_indexes:
      - 2
      - 3
      reason: Restatement of STG association with long-term outcome.
    - source_id: P6-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement of significance.
    unresolved_coverage:
    - source_id: P5-S1-C4
      disposition: unresolved
      reason: Unknown result index; not accepted as coverage
    - source_id: P5-S3-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P5-S3-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S2-C2
    - P3-S2-C12
    - P3-S2-C14
    - P3-S2-C15
    - P3-S2-C18
    - P3-S2-C19
    - P3-S3-C8
    - P3-S3-C10
    - P3-S3-C11
    - P4-S1-C8
    - P4-S1-C13
    - P5-S1-C1
    - P5-S1-C2
    - P5-S1-C5
    - P5-S1-C6
    - P5-S1-C7
    - P5-S1-C8
    - P5-S2-C12
    - P5-S3-C2
    - P5-S3-C3
    - P5-S3-C5
    - P5-S3-C12
    - P6-S1-C1
    - P6-S2-C4
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-2-1
    - TABLE-2-page-4-2
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P2-S3-C4
      recruited_sample:
      - P2-S2-C5
      eligibility:
      - P2-S2-C5
      imaging_provenance:
      - P2-S1-C5
      - P3-S2-C2
      imaging_timing:
      - P2-S1-C2
      - P3-S1-C5
      outcome_timing:
      - P1-S1-C2
      - P2-S2-C9
      - P3-S1-C10
      - P4-S1-C2
      - P4-S1-C7
      - P4-S1-C9
      - P5-S1-C6
      outcome_definition:
      - P2-S2-C6
      - P2-S2-C7
      - P2-S2-C8
      - P2-S2-C11
      - P2-S2-C12
      validation: []
      analysis_restrictions:
      - P3-S1-C11
      - P3-S1-C12
      dependent_variable_statement:
      - P3-S1-C10
      - P3-S2-C10
      limitations:
      - P6-S1-C5
      - P6-S1-C6
      - P6-S1-C7
      - P6-S1-C8
      - P6-S1-C9
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P3-S1-C10
      - P3-S2-C10
      - P5-S1-C3
      - P5-S1-C4
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P2-S3-C5
    outcome_type: both_reported
    imaging_vs_outcome: precedes_outcome
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P4-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P3-S2-C3
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
      pdf_sha256: c332dcbc410f4d93f904af2ab354ca3efe61cecf4a05dae78504a88a0820040f
      review_sha256: 91c945f1a328fb2993d8d8a26eebccfe7ae840be1b04427021c8d2380aab2cb3
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
      - P4-S1-C7
      source_result: Voxel-based regression analysis identified a single cluster in
        the left superior temporal gyrus (STG) and left temporo-parietal junction
        where ADC decrease was associated with greater aphasia severity at 3 months
        (ART M3). This association was age-corrected and remained stable when gender
        and educational level were added as covariates.
      result_status: detected
      patient_measurement: voxel_tissue
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis corresponds to the voxel-based regression
            of ADC maps against ART M3 scores, as described in P4-S1-C7 and P3-S1-C10.
            The proposed core correctly identifies this specific outcome (3-month
            aphasia) and method.
          source_ids:
          - P4-S1-C7
          - P3-S1-C10
        direction:
          answer: fits
          reason: The source states that regions associated with 'greater aphasia
            severity' were located in the left STG/TPJ (P4-S1-C7). The proposed core
            claims an association with 'greater aphasia severity', preserving the
            direction of the detected effect.
          source_ids:
          - P4-S1-C7
        construct:
          answer: fits
          reason: The exposure is correctly identified as ADC decrease in the specified
            anatomical regions. The outcome is aphasia severity measured by ART at
            3 months. The method is voxel-based regression. The patient measurement
            is voxel-based tissue analysis (ADC maps), not template overlap (which
            was a secondary step for tract identification).
          source_ids:
          - P4-S1-C7
          - P3-S1-C10
          - P2-S2-C6
        qualifications:
          answer: fits
          reason: The proposed core includes the qualification that results remained
            stable when adding gender and educational level as covariates (P5-S1-C3).
            It also notes age correction (P3-S1-C10). These are correctly applied
            to the specific analysis.
          source_ids:
          - P5-S1-C3
          - P3-S1-C10
        missing_material_caveat:
          answer: fits
          reason: The small sample size limitation is included. The distinction between
            the primary voxel-based analysis and the subsequent tract overlap analysis
            is maintained by not conflating the two. No material caveats that change
            the interpretation of the association are omitted.
          source_ids:
          - P6-S1-C5
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
      id: R003
      exposure:
        text: ADC decrease in left superior temporal gyrus (STG) and left temporo-parietal
          junction
      outcome:
        text: aphasia severity at 3 months (ART M3)
      analysis_label: voxel-based regression (long-term 3m)
      relation: association
      evidence_ids:
      - P4-S1-C7
      qualifier_ids:
      - P4-S2-C12
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: c332dcbc410f4d93f904af2ab354ca3efe61cecf4a05dae78504a88a0820040f
        source_review: _compare/relationships-2026-11-16/review-current/Zavanone2018
        source_status_sha256: 432555854ddad981e39598598a5c47a3d17ab84ba6ea2d0650c08d752b609d52
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P2-S2-C5:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: c332dcbc410f4d93f904af2ab354ca3efe61cecf4a05dae78504a88a0820040f
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 73554f879cc18e83db21b1c8fc72828f55e308e02f27435ad3b5a28e57dbfc17
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S2-C5
          page: 2
          text_layer_sha256: 73554f879cc18e83db21b1c8fc72828f55e308e02f27435ad3b5a28e57dbfc17
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: 'Subjects

          Patients admitted to the stroke unit of Pitié-Salpêtrière Hospital

          were prospectively recruited according to the following criteria: (i)

          presence of their ﬁrst-ever stroke in the left middle cerebral territory,

          (ii) age ≥18 years and < 85 years, (iii) French native speaker, (iv)

          persistent aphasia at day 1 post stroke (≥1 point in the language items

          of the Aphasia Rapid Test [ART]), (v) no contraindications for MRI, (vi)

          no severe white matter lesions (Fazekas score < 3) and (vii) right-

          handedness.'
        anchor_text: 'Subjects

          Patients admitted to the stroke unit of Pitié-Salpêtrière Hospital

          were prospectively recruited according to the following criteria: (i)

          presence of their ﬁrst-ever stroke in the left middle cerebral territory,

          (ii) age ≥18 years and < 85 years, (iii) French native speaker, (iv)

          persistent aphasia at day 1 post stroke (≥1 point in the language items

          of the Aphasia Rapid Test [ART]), (v) no contraindications for MRI, (vi)

          no severe white matter lesions (Fazekas score < 3) and (vii) right-

          handedness.'
        excluded_fragments: []
        image_sha256: 8af253781789348015eda511b479f4dcec9d4d07406eb2259f4924f724fc2e69
      P3-S2-C11:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: c332dcbc410f4d93f904af2ab354ca3efe61cecf4a05dae78504a88a0820040f
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 85d62df60de613c345fd96fcaf480afa6ba04830839d144147f10dd59c076288
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S2-C11
          page: 3
          text_layer_sha256: 85d62df60de613c345fd96fcaf480afa6ba04830839d144147f10dd59c076288
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Results

          We included 19 patients in the study.'
        anchor_text: 'Results

          We included 19 patients in the study.'
        excluded_fragments: []
        image_sha256: e9509a196ea3850cd3c9175534ab8ca6abff0ce80b77d4e8db33713c9fbbf7aa
        transcription: 'Results


          We included 19 patients in the study'
      P2-S2-C9:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: c332dcbc410f4d93f904af2ab354ca3efe61cecf4a05dae78504a88a0820040f
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 4ec8a00ee33dc7c0019062f5859e9e34422a637fb3d993eeb0a5685b07757309
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S2-C9
          page: 2
          text_layer_sha256: 4ec8a00ee33dc7c0019062f5859e9e34422a637fb3d993eeb0a5685b07757309
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'ART scores were recorded at the acute phase (at day 1 post

          stroke = ART 1; at day 7 post stroke = ART 7) and the chronic phase

          (at 3 months post stroke = ART M3; at 6 months post stroke = ART

          M6).'
        anchor_text: 'ART scores were recorded at the acute phase (at day 1 post

          stroke = ART 1; at day 7 post stroke = ART 7) and the chronic phase

          (at 3 months post stroke = ART M3; at 6 months post stroke = ART

          M6).'
        excluded_fragments: []
        image_sha256: d4c47b4f368f1c60416c9dea172d9fb800df2cf3baaed1a412407e1448e179dc
        transcription: ART scores were recorded at the acute phase (at day 1 post
          stroke = ART 1; at day 7 post stroke = ART 7) and the chronic phase (at
          3 months post stroke = ART M3; at 6 months post stroke = ART M6)
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 4
  quote: 'Brain areas related to long-term aphasia outcome

    The regions associated with greater aphasia severity evaluated with

    the ART at three months were also located in a single cluster, mainly at

    the level of the left superior temporal gyrus (STG) and reached the left

    temporo-parietal junction (Figs. 2B, 3B, Table 2).'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-26'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
