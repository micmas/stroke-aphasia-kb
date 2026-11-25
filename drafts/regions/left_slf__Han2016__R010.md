---
id: left_slf
name: left superior longitudinal fasciculus
kind: tract
findings:
- id: f1
  target_audit:
    status: behaviour_label_present
    category: behaviour_or_language_construct
    original_target: phonological_encoding
    reason: Label names a behaviour or language construct; its exact operational definition and measurement
      still need source review.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  outcome_measurement:
    status: needs_source_review
    instruments: []
    note: Outcome instrument/task is not yet verified for this finding. Do not infer it from the predictor
      or a paper-wide test list.
  target: phonological_encoding
  target_kind: impairment
  claim: The integrity of the left superior longitudinal fasciculus is significantly
    associated with phonological encoding scores in oral picture naming and word reading,
    even when controlling for age, gender, education, total lesion volume, lesion
    volume in phonological-encoding-relevant gray matter regions, auditory lexical
    decision performance, and picture associative matching performance.
  direction: likely
  relationship: correlational
  method: LSM
  sample:
    n: 63
    population: right-handed stroke patients
    phase: not_reported
    time_post_onset: at least one-month post-onset
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Findings are constrained by the spatial scale of the JHU white-matter template
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Patient lesion overlap with a population tract template
    (lesion percentage) and mean fractional anisotropy (FA) values within the left
    superior longitudinal fasciculus template. Analysis performed on a subset of 63
    stroke patients; Phonological encoding in word reading was measured as the residual
    after regressing out word associative matching accuracy. Additional metadata has
    not been transcribed; review the pending-field flags before approval. PDF image
    reading (P3-S1-C9, two-model agreement, human verification pending): . They were
    all native Chinese

    speakers and were recruited from the China Rehabilitation

    Research Center based on the following inclusion criteria:

    willingness to participate; no previous brain injury or other

    neurological/psychiatric disease such as alcohol abuse

    or severe depression; at least one-month post-onset [dis-

    ease duration: mean = 7 months; standard deviation

    (SD) = 12; range 1–86]; ability to follow task instructions;

    and a relatively clear lesion profile (stroke and traumatic Original text-layer
    quotation is preserved below. PDF image reading (P3-S2-C9, two-model agreement,
    human verification pending): Administration of the Edinburgh Handedness Inventory
    (Oldfield 1971) revealed that all patients were right-handed Original text-layer
    quotation is preserved below.'
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
    - proposed_concept:phonological_encoding
  citation: '@Han2016'
  source_passages:
  - section: Original source P11-S1-C4
    page: 11
    quote: 'Finally, after introducing all the above control variables

      (age, gender, education, lesion volume in grey matter

      regions of VLSM signiﬁcant results, auditory lexical

      decision score, associative matching score and total lesion

      volume) as covariates together in one analysis, the pho-

      nological encoding scores still correlated signiﬁcantly with

      the integrity of the left SLF in the 63 stroke patients (lesion

      percentage:

      oral

      picture

      naming:

      partial

      r = -0.33,

      p \ 0.02; word reading: partial r = -0.45, p \ 6 9 10-4;

      mean FA: oral picture naming: partial r = 0.37, p \ 0.006;

      word reading: partial r = 0.41, p \ 0.002).'
    supports: claim
  - section: Original source P11-S1-C4
    page: 11
    quote: 'Finally, after introducing all the above control variables

      (age, gender, education, lesion volume in grey matter

      regions of VLSM signiﬁcant results, auditory lexical

      decision score, associative matching score and total lesion

      volume) as covariates together in one analysis, the pho-

      nological encoding scores still correlated signiﬁcantly with

      the integrity of the left SLF in the 63 stroke patients (lesion

      percentage:

      oral

      picture

      naming:

      partial

      r = -0.33,

      p \ 0.02; word reading: partial r = -0.45, p \ 6 9 10-4;

      mean FA: oral picture naming: partial r = 0.37, p \ 0.006;

      word reading: partial r = 0.41, p \ 0.002).'
    supports: method
  - section: Original source P10-S1-C4
    page: 10
    quote: 'Finally, the effects of SLF held up well when

      we considered only the 63 right-handed stroke patients, with

      total lesion volume value as a covariate (lesion percentage:

      oral picture naming partial r = -0.50, p\4 9 10-5; word

      reading partial r = -0.57, p \2 9 10-6; mean FA: oral

      picture naming partial r = 0.50, p\ 4 9 10-5; word reading

      partial r = 0.55, p\4 9 10-6).'
    supports: sample
  - section: Original source P3-S1-C9
    page: 3
    quote: 'They were all native Chinese

      speakers and were recruited from the China Rehabilitation

      Research Center based on the following inclusion criteria:

      willingness to participate; no previous brain injury or other

      neurological/psychiatric disease such as alcohol abuse

      or severe depression; at least one-month post-onset [dis-

      ease

      duration:

      mean = 7 months;

      standard

      deviation

      (SD) = 12; range 1–86]; ability to follow task instructions;

      and a relatively clear lesion proﬁle (stroke and traumatic

      '
    supports: sample
  - section: Original source P3-S2-C9
    page: 3
    quote: 'Administration of the Edinburgh Handedness Inventory

      (Oldﬁeld 1971) revealed that all patients were right-han-

      ded.'
    supports: sample
  - section: Original source P5-S2-C6
    page: 5
    quote: 'The index of white matter tract integrity

      We focused on the major tracts in a widely used human

      brain

      white-matter

      template,

      the

      ‘‘JHU

      white-matter

      tractography atlas’’ (25 % probability map) from FSL

      (http://www.fmrib.ox.ac.uk/fsl/data/atlas-descriptions.html

      #wm), which contains 20 main white matter bundles (see

      Table 1 for details).'
    supports: method
  - section: Original source P5-S3-C2
    page: 5
    quote: 'For each of the

      remaining 17 tracts, the lesion percentage (number of

      voxels with lesion divided by total number of voxels in the

      tract) was correlated with the patients’ phonological

      encoding scores in oral picture naming and word reading,

      partialing out total lesion volume.'
    supports: method
  - section: Original source P5-S3-C4
    page: 5
    quote: 'For the FA measure, the

      mean FA value of each of the 20 tracts in the template was

      obtained by averaging the FA values of all voxels in the

      tract.'
    supports: method
  - section: Original source P12-S1-C11
    page: 12
    quote: 'The current study is constrained by the spatial scale

      of the John Hopkins University white-matter template and

      can only be interpreted with the template tract, which was

      derived from tracking between regions-of-interest in the

      '
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-24'
relationship_review:
  paper: Han2016
  proposal_id: R010
  review_status_sha256: f7afd52802d9882ef0fe1a38be76c3f3e47ac87227a76588973adb0e0a7c75c5
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 6654810d9f8149b35bd5af1563259c384c0e6519a4fef656c6a1f0decf627d5b
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 6654810d9f8149b35bd5af1563259c384c0e6519a4fef656c6a1f0decf627d5b
        A/passages.json: c8c5cb13da612f289c4049235babe12656310158b897b1037a65ebbce5e1a304
        A/raw.json: fea5da7a4f4362d86ae6027ac18b2e99560ad552ffa0c13d80c54c3b28d7657c
        A/source-units.json: 864b14ee44a6378301200aa78f1ab9ca2985ae3d0feea05ca2414716611dbc4a
        A/full-source-units.json: d45b8b0b23cc5e9648bdbe9c082e644314cec9ea5574a923511f7faa877ba266
        A/meta.json: 3b9804f18c2c5aced515f3081e97246dc281c6da09d448b288e35228c85ddf44
        A/table-images/TABLE-1-page-6-1.png: 4a88b795bd69ce4af0fa7abd5b93dcff305ff4955fd3c2db504766ca257677ef
        A/table-images/page-6.png: 452d0e481b72aae7650e5b7f113739d97ce784e733cdb0218dd32dc1ad6c087a
        A/table-images/page-7.png: 4cae8765033e426df2c62ed9553557abfa06bf1d47262b945f8b8fcd62bc85c2
        A/table-images/manifest.json: 2c003180df4a2c09e1ee5f4bb0367cee713b3fbff21e28560e6afab30384bbe6
        A/table-images/TABLE-2-page-7-1.png: 04f7bfb3813a6d0e2a5f2c4d34b63f4ca30b7aa2fd986686eb4f7931899dd073
        A/clauses/window-03/raw.json: 0bc439d1ec9c26d989c2c1d83dc963c394d199365d2264857aa10d9343b0e4bb
        A/clauses/window-03/prompt.txt: 46bbcba0674e199eef038e1910af4eee942a122f7463f2146d9edabf13695dec
        A/clauses/window-03/meta.json: 8ecdf810fde9663ebae035ba214b4caa656d0fa939467787cd7018a433d265cf
        A/clauses/window-04/raw.json: dfbed8cb544c05d97094477c8c7dc0414d11bcf0b4c22c6ec149018170723c0b
        A/clauses/window-04/prompt.txt: f549b5469d591a3d102ca90fe19ba5801b1943089095b791e55b1b6f4d27ff64
        A/clauses/window-04/meta.json: eec1dddf1cc906ec831e768f8afd3810ba9d1373c5e973f54abd62e64a313cd8
        A/clauses/window-05/raw.json: b58649f15cbb29b1b95850d08fe6733f7a2b4f67b91102f5d57b5a97360c6e5d
        A/clauses/window-05/prompt.txt: 93121a1331ce794a9d0366884b4ff64c7c42cb2134e2995f6892bd856af6912d
        A/clauses/window-05/meta.json: a0e2d8ee0fc7ff62416020b676d4f6d1b2b8af8ff43dc24a648e143a6a395b7d
        A/clauses/window-02/raw.json: 27290c501778cdb08049804847a7361a0782980cd065012cb44cd873b2888a0c
        A/clauses/window-02/prompt.txt: ac3c40b1e31eca691d462ccb4ce342d23f80c906d628227ea89b5f8438d271c8
        A/clauses/window-02/meta.json: 9a4b932aa0ed3e82369e742a9f84ecd979819c46fc0baf203e8046a3ea6e66b4
        A/clauses/window-07/raw.json: 495383ac80a6a7895325def27697a3c8b4c340263c1d7fb3d53e7cdd64e90aba
        A/clauses/window-07/prompt.txt: 597513264ebb9e7560ddf954a78328efff8f5b4ba519f90aba3cae54e1ea469c
        A/clauses/window-07/meta.json: 028a2127ab6c3320eb7197d16a3ec21f0c02873eca8607aa78412e5b47d2518b
        A/clauses/window-01/raw.json: 3df4920b681f9329565cea35b981d806227b32c3bb549b2fc205f5c1f4f32c27
        A/clauses/window-01/prompt.txt: 4360832fc5884086363bcff51561a104da2d9bc5df339864ca01c244f72d971b
        A/clauses/window-01/meta.json: bfd20ed4d2faab0e690441d88c765f4d82b635b8eba83785a44d09018fe55538
        A/clauses/window-06/raw.json: d57beffc803eafa4b04172c7e52b9da77fb150aeed1161023fe1716c98890002
        A/clauses/window-06/prompt.txt: 08bf9a219696ba183db604c94bfb232851d5a8542c4dc476b00dc868c57676e1
        A/clauses/window-06/meta.json: 5bffc2a4452ce4a92882b5b90a101bb283125c54b7a8055e476edfc2d4e5ff3b
        A/clauses/window-08/raw.json: adce752555a94e0d1cfb7ed465f941356d70c7eef7760b91b1e7f8ac2e1e2715
        A/clauses/window-08/prompt.txt: d94e47c6308e298d7922cc7745d166bf6d253dfb7a37660ce30cb454b83b2c2c
        A/clauses/window-08/meta.json: 28318b7128c82aa0e00006002ceb525555722b118a59e9f2e6a515213f4d86b1
        A/tables/TABLE-1-page-6-1/raw.json: ba729a196cc419fdac76126c615e2091cf7f90f236c53d807b16c05f4bae0a13
        A/tables/TABLE-1-page-6-1/prompt.txt: 550dbe801824c03bb1fbc13140a2921fd1f4ebdbbcefb5e54e2a0be4b6b8f78b
        A/tables/TABLE-1-page-6-1/meta.json: f6124214be1e644f2fa4d5b772db9e63ee616052ad9fecc87cd0be0e3adfd7cd
        A/tables/TABLE-2-page-7-2/raw.json: 75816cb0d252130817ac16259ffd3c2e2fe241958d1f4cceea1067a6ffd7669f
        A/tables/TABLE-2-page-7-2/prompt.txt: 639e531fc7b6c345d804c4dd1a4dde86db7d5a264f4544bc9976faf81f539193
        A/tables/TABLE-2-page-7-2/meta.json: b8247c10a836443b91bcd7e459b627a70341a517d68534cb73fee43684fa255f
        B/passages.json: c8c5cb13da612f289c4049235babe12656310158b897b1037a65ebbce5e1a304
        B/raw.json: 6b48b9fa91bc0c98c5b9c72747756697d7ebf61863ac5cb0b4c5b12bfe511c78
        B/source-units.json: 864b14ee44a6378301200aa78f1ab9ca2985ae3d0feea05ca2414716611dbc4a
        B/full-source-units.json: d45b8b0b23cc5e9648bdbe9c082e644314cec9ea5574a923511f7faa877ba266
        B/meta.json: 3d1998fa62cc87f22646baf42881af643622758c1cf9332bd43bd57d7a5239a6
        B/table-images/TABLE-1-page-6-1.png: 4a88b795bd69ce4af0fa7abd5b93dcff305ff4955fd3c2db504766ca257677ef
        B/table-images/page-6.png: 452d0e481b72aae7650e5b7f113739d97ce784e733cdb0218dd32dc1ad6c087a
        B/table-images/page-7.png: 4cae8765033e426df2c62ed9553557abfa06bf1d47262b945f8b8fcd62bc85c2
        B/table-images/manifest.json: 15409e16fb64014408fe1f86182830e009647dfb52b226fe53aa2805ba252dd1
        B/table-images/TABLE-2-page-7-1.png: 04f7bfb3813a6d0e2a5f2c4d34b63f4ca30b7aa2fd986686eb4f7931899dd073
        B/clauses/window-03/raw.json: 8847852f3b9760bf8987dabaaf87a15cf73820efe0fb52bec15a901e8d36f860
        B/clauses/window-03/prompt.txt: 46bbcba0674e199eef038e1910af4eee942a122f7463f2146d9edabf13695dec
        B/clauses/window-03/meta.json: ac55e8b8fd9293ca9fffcb4ada3310254659f37a3f8c4c97b1742a75a73753a5
        B/clauses/window-04/raw.json: efd645cb701b5e29ba7c1cf879f95256e618ef8b8004d484efe975c42510a98c
        B/clauses/window-04/prompt.txt: f549b5469d591a3d102ca90fe19ba5801b1943089095b791e55b1b6f4d27ff64
        B/clauses/window-04/meta.json: ccc6eb13168597dbc76a2763ff7b75839abcc72aa7f53f34978cc929577bf414
        B/clauses/window-05/raw.json: dc83c90b869f5a679b2e3cf105cc88bbfb29b788d03d014cc02a132840db47f6
        B/clauses/window-05/prompt.txt: 93121a1331ce794a9d0366884b4ff64c7c42cb2134e2995f6892bd856af6912d
        B/clauses/window-05/meta.json: 8c1c8cf09008388480fc28b4cb8344cc34d9b76cb361319fb7519ff3dfa75309
        B/clauses/window-02/raw.json: c8c97a89289aad5b6f723e019da137fb7b1de761f7a7aa6343f03e1304bb7637
        B/clauses/window-02/prompt.txt: ac3c40b1e31eca691d462ccb4ce342d23f80c906d628227ea89b5f8438d271c8
        B/clauses/window-02/meta.json: 9f7de36b31e7374b3181a6d1e4e6d7a2ef50f1404731746f30de7781b5fa76bb
        B/clauses/window-07/raw.json: 8da297abc98b09db44cb5978030b95ab25df4ce2cac8c1b96a2223394ff2d4ca
        B/clauses/window-07/prompt.txt: 597513264ebb9e7560ddf954a78328efff8f5b4ba519f90aba3cae54e1ea469c
        B/clauses/window-07/meta.json: 7a6a4a92f9a27a5d56c55fe006dc54e72bf93f2c6ae04164c31d1cf947a7cfa5
        B/clauses/window-01/raw.json: ad2e1c1c1e2da4c26bb909bcdd5df2855d61c47b5d3ff3a85c2a90fffa98cb15
        B/clauses/window-01/prompt.txt: 4360832fc5884086363bcff51561a104da2d9bc5df339864ca01c244f72d971b
        B/clauses/window-01/meta.json: 88965d2599c2f05f01116cfbe6867460ff7e859188b339da0d54fe24ac7b3174
        B/clauses/window-06/raw.json: 80d90e1bba8fde1ea601e0bccc3ade69d1b2d8c22f3e902c4480a5bfab9153f3
        B/clauses/window-06/prompt.txt: 08bf9a219696ba183db604c94bfb232851d5a8542c4dc476b00dc868c57676e1
        B/clauses/window-06/meta.json: be1f7b27c31304dd3ab258d30143a7496f389a645d6503b9a1fdf6a884cc7f54
        B/clauses/window-08/raw.json: 6571e9089857d4c001798edf61e08766498e339789d770aa79e24b534cea4957
        B/clauses/window-08/prompt.txt: d94e47c6308e298d7922cc7745d166bf6d253dfb7a37660ce30cb454b83b2c2c
        B/clauses/window-08/meta.json: f65f2085acc972c7bfc2cf23905b9c6d46070e161f8a44d7a6d7b27cbc84eda3
        B/tables/TABLE-1-page-6-1/raw.json: 044887dc81caa7ae552f33c2f0cbfe1f6986ffa6e11190c831babc58567261e2
        B/tables/TABLE-1-page-6-1/prompt.txt: 550dbe801824c03bb1fbc13140a2921fd1f4ebdbbcefb5e54e2a0be4b6b8f78b
        B/tables/TABLE-1-page-6-1/meta.json: 76c79add7402c602d2b6ef1a1402751edc757bd5b7439072eae786b0358df627
        B/tables/TABLE-2-page-7-2/raw.json: 67a4778cf67093d65eab67d4e55752186ab5b41c6d21d1e3baa89a6b412cf592
        B/tables/TABLE-2-page-7-2/prompt.txt: 639e531fc7b6c345d804c4dd1a4dde86db7d5a264f4544bc9976faf81f539193
        B/tables/TABLE-2-page-7-2/meta.json: 6055e2a0ce0aecc5e81959ebb10dee75a1c18c3d3f240fa2cc5888284741679f
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
      pdf_sha256: 6654810d9f8149b35bd5af1563259c384c0e6519a4fef656c6a1f0decf627d5b
      source_review: _compare/relationships-2026-11-16/review-current/Han2016
      source_status_sha256: 85b4664fcda78422e76bab8fb861152733bd6b71fa57c7f89619d69ba1d5b85c
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R010
    exposure:
      text: left superior longitudinal fasciculus (SLF) integrity (lesion percentage
        and mean FA values)
    outcome:
      text: phonological encoding scores
    analysis_label: Convergence analysis (All control variables)
    relation: sensitivity
    evidence_ids:
    - P11-S1-C4
    qualifier_ids:
    - P11-S1-C4
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 6654810d9f8149b35bd5af1563259c384c0e6519a4fef656c6a1f0decf627d5b
      source_review: _compare/relationships-2026-11-16/review-current/Han2016
      source_status_sha256: 85b4664fcda78422e76bab8fb861152733bd6b71fa57c7f89619d69ba1d5b85c
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Accounting without a linked unit P1-S1-C7
      - Accounting without a linked unit P1-S1-C8
      - Result passage disposed without unit P1-S2-C1
      - Unaccounted source passage P1-S1-C8
      - Unaccounted source passage P1-S1-C7
      - Result passage disposed without unit P4-S1-C9
      - Result passage disposed without unit P4-S2-C8
      - Result passage disposed without unit P7-S2-C2
      - Result passage disposed without unit P7-S2-C3
      - Result passage disposed without unit P7-S2-C4
      - Result passage disposed without unit P7-S2-C5
      - Result passage disposed without unit P9-S1-C1
      - Result passage disposed without unit P11-S1-C1
      - Result passage disposed without unit P11-S1-C6
      - Result passage disposed without unit P11-S2-C3
      - Result passage disposed without unit P11-S2-C9
      - Result passage disposed without unit P11-S3-C3
      - Result passage disposed without unit P11-S3-C5
      - Accounting without a linked unit P11-S3-C8
      - Accounting without a linked unit P12-S1-C1
      - Accounting without a linked unit P12-S1-C2
      - Accounting without a linked unit P12-S1-C7
      - Result passage disposed without unit P12-S2-C5
      - Accounting without a linked unit P12-S2-C6
      - Unaccounted source passage P12-S1-C2
      - Unaccounted source passage P12-S1-C7
      - Unaccounted source passage P11-S3-C8
      - Unaccounted source passage P12-S2-C6
      - Unaccounted source passage P12-S1-C1
      - Result passage disposed without unit P12-S2-C10
      - Accounting without a linked unit P12-S2-C11
      - Unaccounted source passage P12-S2-C11
      unattached_null_or_qualifier_ids:
      - P1-S1-C8
      - P11-S2-C9
      - P11-S3-C5
      - P11-S3-C8
      suppressed_nonrepresented_units: 5
      default_disposition_count_requires_completeness_check: 174
      unselected_timing_passages:
      - P3-S2-C6
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P8-S1-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S1-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P3-S1-C6
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P5-S2-C13
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P5-S3-C2
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P5-S3-C7
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P6-S1-C3
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P7-S1-C4
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P7-S1-C6
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P7-S1-C7
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P7-S1-C8
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P7-S1-C9
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P7-S1-C10
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P7-S1-C11
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P10-S1-C3
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P10-S1-C5
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P10-S1-C6
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P11-S1-C4
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P11-S1-C6
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: adjustment_roles
        source_ids:
        - P1-S1-C8
        - P1-S2-C1
        - P3-S1-C3
        - P3-S1-C5
        - P3-S1-C6
        - P3-S1-C7
        - P5-S2-C13
        - P5-S3-C2
        - P5-S3-C5
        - P5-S3-C7
        - P7-S1-C5
        - P7-S1-C8
        - P7-S1-C9
        - P7-S1-C10
        - P7-S1-C11
        - P7-S1-C12
        - P7-S2-C1
        - P9-S1-C4
        - P9-S1-C5
        - P10-S1-C3
        - P10-S1-C4
        - P10-S1-C5
        - P10-S1-C6
        - P11-S1-C4
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - personal_factors
      - tested_personal_effects
      - adjustment_roles
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-6-1
      - TABLE-2-page-7-2
      unlinked_tables: []
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P7-S2
        - P8-S1
        - P9-S1
        - P10-S1
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 6654810d9f8149b35bd5af1563259c384c0e6519a4fef656c6a1f0decf627d5b
      source_review: _compare/relationships-2026-11-16/review-current/Han2016
      source_status_sha256: 85b4664fcda78422e76bab8fb861152733bd6b71fa57c7f89619d69ba1d5b85c
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C7
      disposition: repeated
      result_indexes:
      - 0
      - 1
      reason: Abstract restatement of SLF integrity predicting phonological encoding
        impairment.
    - source_id: P1-S1-C8
      disposition: repeated
      result_indexes:
      - 2
      - 3
      - 4
      - 5
      - 6
      - 7
      - 8
      - 9
      reason: Abstract restatement of SLF effects remaining significant after adjustment.
    - source_id: P1-S2-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes potential confounding factors.
    - source_id: P4-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement about consistency of result patterns across non-word error
        definitions.
    - source_id: P4-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of residual values summing to zero.
    - source_id: P5-S2-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of tract exclusion criteria.
    - source_id: P7-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive behavioral performance (accuracy).
    - source_id: P7-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive behavioral performance (nonword errors).
    - source_id: P7-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive behavioral performance (accuracy).
    - source_id: P7-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive behavioral performance (residual score).
    - source_id: P7-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Correlation between two behavioral measures, not an exposure-outcome
        relationship.
    - source_id: P7-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive behavioral performance (control tasks).
    - source_id: P7-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to lesion distribution figure.
    - source_id: P8-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive lesion distribution.
    - source_id: P8-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive lesion distribution.
    - source_id: P8-S1-C3
      disposition: represented
      result_indexes:
      - 0
      reason: Direct result of left SLF lesion percentage and phonological encoding.
    - source_id: P8-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Result not considered further due to opposite expected direction.
    - source_id: P8-S1-C5
      disposition: represented
      result_indexes:
      - 1
      reason: Direct result of left SLF mean FA and phonological encoding.
    - source_id: P8-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Association with left corticospinal tract (not the primary focus/SLF).
    - source_id: P9-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Continuation of P8-S1-C6.
    - source_id: P9-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Results not considered further due to opposite expected direction.
    - source_id: P9-S1-C4
      disposition: repeated
      result_indexes:
      - 2
      - 3
      - 4
      - 5
      - 6
      - 7
      - 8
      - 9
      reason: General statement that SLF prediction remained significant.
    - source_id: P9-S1-C5
      disposition: represented
      result_indexes:
      - 2
      reason: Specific results for demographic factor adjustment.
    - source_id: P10-S1-C1
      disposition: represented
      result_indexes:
      - 10
      reason: VLSM results for grey matter regions.
    - source_id: P10-S1-C3
      disposition: represented
      result_indexes:
      - 3
      reason: Specific results for grey matter adjustment.
    - source_id: P10-S1-C4
      disposition: represented
      result_indexes:
      - 4
      reason: Specific results for stroke-only cohort.
    - source_id: P10-S1-C5
      disposition: represented
      result_indexes:
      - 5
      reason: Association between SLF and auditory lexical decision.
    - source_id: P10-S1-C6
      disposition: repeated
      result_indexes:
      - 6
      reason: Restatement of results in Table 2.
    - source_id: P11-S1-C1
      disposition: represented
      result_indexes:
      - 6
      reason: Specific results for phonological perception control task adjustment.
    - source_id: P11-S1-C2
      disposition: represented
      result_indexes:
      - 7
      reason: Null result for SLF and picture associative matching.
    - source_id: P11-S1-C3
      disposition: represented
      result_indexes:
      - 8
      reason: Specific results for semantic control task adjustment.
    - source_id: P11-S1-C4
      disposition: represented
      result_indexes:
      - 9
      reason: Specific results for all-covariates convergence analysis.
    - source_id: P11-S2-C2
      disposition: repeated
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
      reason: Discussion restatement of SLF role.
    - source_id: P11-S3-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of VLSM approach.
    - source_id: P11-S3-C3
      disposition: repeated
      result_indexes:
      - 10
      reason: Discussion restatement of VLSM results.
    - source_id: P11-S3-C4
      disposition: repeated
      result_indexes:
      - 10
      reason: Discussion restatement of VLSM results.
    - source_id: P11-S3-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Null finding regarding posterior superior temporal gyrus.
    - source_id: P11-S3-C7
      disposition: repeated
      result_indexes:
      - 0
      - 1
      reason: Discussion restatement of SLF role.
    - source_id: P11-S3-C8
      disposition: repeated
      result_indexes:
      - 3
      reason: Discussion restatement of grey matter adjustment results.
    - source_id: P12-S1-C1
      disposition: repeated
      result_indexes:
      - 0
      - 1
      reason: Conclusion restatement of SLF prediction.
    - source_id: P12-S2-C5
      disposition: repeated
      result_indexes:
      - 0
      - 1
      reason: Discussion restatement of SLF role.
    - source_id: P12-S2-C6
      disposition: repeated
      result_indexes:
      - 5
      reason: Discussion restatement of SLF and auditory lexical decision.
    - source_id: P12-S2-C10
      disposition: repeated
      result_indexes:
      - 0
      - 1
      reason: Conclusion restatement of SLF necessity.
    - source_id: P12-S2-C11
      disposition: repeated
      result_indexes:
      - 0
      - 1
      reason: Conclusion restatement of SLF prediction.
    unresolved_coverage:
    - source_id: P11-S1-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S2-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S2-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S2-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S1-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S1-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C7
    - P1-S1-C8
    - P1-S2-C1
    - P4-S1-C9
    - P4-S2-C8
    - P5-S2-C14
    - P7-S2-C2
    - P7-S2-C3
    - P7-S2-C4
    - P7-S2-C5
    - P7-S2-C6
    - P7-S2-C7
    - P7-S2-C8
    - P8-S1-C1
    - P8-S1-C2
    - P8-S1-C4
    - P8-S1-C6
    - P9-S1-C1
    - P9-S1-C2
    - P9-S1-C4
    - P10-S1-C6
    - P11-S1-C6
    - P11-S2-C2
    - P11-S2-C3
    - P11-S2-C8
    - P11-S2-C9
    - P11-S3-C2
    - P11-S3-C3
    - P11-S3-C4
    - P11-S3-C5
    - P11-S3-C7
    - P11-S3-C8
    - P12-S1-C1
    - P12-S1-C2
    - P12-S1-C7
    - P12-S2-C5
    - P12-S2-C6
    - P12-S2-C10
    - P12-S2-C11
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-6-1
    - TABLE-2-page-7-2
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P3-S2-C6
      recruited_sample:
      - P3-S1-C8
      - P3-S1-C9
      eligibility:
      - P3-S1-C9
      imaging_provenance:
      - P5-S2-C6
      imaging_timing:
      - P4-S2-C15
      outcome_timing:
      - P3-S1-C9
      outcome_definition:
      - P3-S3-C2
      - P4-S1-C4
      - P4-S1-C6
      - P4-S1-C8
      - P4-S2-C4
      validation:
      - P3-S1-C5
      analysis_restrictions:
      - P5-S2-C14
      dependent_variable_statement:
      - P4-S2-C5
      - P4-S2-C6
      - P5-S2-C13
      limitations:
      - P12-S2-C2
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles: []
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P3-S2-C6
      - P3-S2-C7
      - P3-S2-C8
      - P3-S2-C9
      - P3-S2-C10
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: internal_cross_validation
    held_selections:
    - slot: dependent_variable_statement
      source_id: P8-S1-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S1-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P3-S1-C6
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P5-S2-C13
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P5-S3-C2
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P5-S3-C7
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P6-S1-C3
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P7-S1-C4
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P7-S1-C6
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P7-S1-C7
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P7-S1-C8
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P7-S1-C9
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P7-S1-C10
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P7-S1-C11
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P10-S1-C3
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P10-S1-C5
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P10-S1-C6
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P11-S1-C4
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P11-S1-C6
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: adjustment_roles
      source_ids:
      - P1-S1-C8
      - P1-S2-C1
      - P3-S1-C3
      - P3-S1-C5
      - P3-S1-C6
      - P3-S1-C7
      - P5-S2-C13
      - P5-S3-C2
      - P5-S3-C5
      - P5-S3-C7
      - P7-S1-C5
      - P7-S1-C8
      - P7-S1-C9
      - P7-S1-C10
      - P7-S1-C11
      - P7-S1-C12
      - P7-S2-C1
      - P9-S1-C4
      - P9-S1-C5
      - P10-S1-C3
      - P10-S1-C4
      - P10-S1-C5
      - P10-S1-C6
      - P11-S1-C4
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
      pdf_sha256: 6654810d9f8149b35bd5af1563259c384c0e6519a4fef656c6a1f0decf627d5b
      review_sha256: f7afd52802d9882ef0fe1a38be76c3f3e47ac87227a76588973adb0e0a7c75c5
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
      - P11-S1-C4
      source_result: In 63 stroke patients, the integrity of the left superior longitudinal
        fasciculus (SLF), measured by lesion percentage and mean fractional anisotropy
        (FA), remained significantly associated with phonological encoding scores
        in oral picture naming and word reading after controlling for a comprehensive
        set of covariates including age, gender, education, total lesion volume, lesion
        volume in phonological-encoding-relevant gray matter regions, auditory lexical
        decision performance, and picture associative matching performance.
      result_status: detected
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis (R010) corresponds to the 'convergence analysis'
            described in P11-S1-C4, which tests the association between left SLF integrity
            and phonological encoding in 63 stroke patients while controlling for
            all specified covariates. The proposed core correctly identifies this
            specific model and population.
          source_ids:
          - P11-S1-C4
          - P7-S1-C11
        direction:
          answer: fits
          reason: The source reports significant correlations (partial r values provided
            in P11-S1-C4) indicating a detected association. The proposed core states
            the association is 'significant' and 'likely', which aligns with the detected
            result. The direction of the relationship (integrity predicting encoding)
            is preserved.
          source_ids:
          - P11-S1-C4
        construct:
          answer: fits
          reason: The exposure is correctly identified as left SLF integrity (lesion
            percentage and mean FA). The outcome is phonological encoding scores.
            The patient measurement is correctly classified as template_lesion_overlap
            (lesion percentage) and patient_diffusion (mean FA), but the primary construct
            for the 'lesion' part is template overlap. The proposed core definition
            mentions both, which is accurate. The method is described as LSM in the
            core, but the source describes partial correlations; however, the core's
            'method' field is likely a schema artifact or shorthand for the statistical
            approach, and the 'definition' and 'claim' accurately reflect the partial
            correlation analysis. The key is that the exposure/outcome mapping is
            correct.
          source_ids:
          - P11-S1-C4
          - P5-S2-C6
          - P5-S3-C2
        qualifications:
          answer: fits
          reason: The proposed core includes the critical qualification that the analysis
            was performed on a subset of 63 stroke patients (P11-S1-C4, P7-S1-C12).
            It also notes the residual nature of the word reading measure. The limitation
            regarding the JHU template spatial scale is included. These are material
            qualifiers present in the source.
          source_ids:
          - P11-S1-C4
          - P7-S1-C12
          - P12-S1-C11
        missing_material_caveat:
          answer: fits
          reason: No material caveats are missing. The core correctly restricts the
            population to stroke patients for this specific convergence analysis,
            which is a key distinction from the initial 69-patient analysis. The template
            limitation is also captured.
          source_ids:
          - P11-S1-C4
          - P12-S1-C11
      optional_pending:
      - Specific partial r values and p-values for the convergence analysis are not
        transcribed in the core, but are present in P11-S1-C4.
      - The exact list of gray matter regions (premotor, pre/postcentral, supramarginal)
        is summarized in the core as 'phonological-encoding-relevant gray matter regions',
        which is acceptable for a qualitative draft but could be more specific.
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Specific partial r values and p-values for the convergence analysis are not
      transcribed in the core, but are present in P11-S1-C4.
    - The exact list of gray matter regions (premotor, pre/postcentral, supramarginal)
      is summarized in the core as 'phonological-encoding-relevant gray matter regions',
      which is acceptable for a qualitative draft but could be more specific.
    normalizations: []
    analysis_identity:
      id: R010
      exposure:
        text: left superior longitudinal fasciculus (SLF) integrity (lesion percentage
          and mean FA values)
      outcome:
        text: phonological encoding scores
      analysis_label: Convergence analysis (All control variables)
      relation: sensitivity
      evidence_ids:
      - P11-S1-C4
      qualifier_ids:
      - P11-S1-C4
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 6654810d9f8149b35bd5af1563259c384c0e6519a4fef656c6a1f0decf627d5b
        source_review: _compare/relationships-2026-11-16/review-current/Han2016
        source_status_sha256: 85b4664fcda78422e76bab8fb861152733bd6b71fa57c7f89619d69ba1d5b85c
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P3-S1-C9:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 6654810d9f8149b35bd5af1563259c384c0e6519a4fef656c6a1f0decf627d5b
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 46c061cf9bc7d5681c7f98aa4e9294a26ce4968dcafe2993e6b4994ff986e886
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S1-C9
          page: 3
          text_layer_sha256: 02a15a736d5ee0e0ddf8807f564238fb8f7621744bd5f942ab4d68d10d053bda
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'They were all native Chinese

          speakers and were recruited from the China Rehabilitation

          Research Center based on the following inclusion criteria:

          willingness to participate; no previous brain injury or other

          neurological/psychiatric disease such as alcohol abuse

          or severe depression; at least one-month post-onset [dis-

          ease

          duration:

          mean = 7 months;

          standard

          deviation

          (SD) = 12; range 1–86]; ability to follow task instructions;

          and a relatively clear lesion proﬁle (stroke and traumatic

          '
        anchor_text: 'They were all native Chinese

          speakers and were recruited from the China Rehabilitation

          Research Center based on the following inclusion criteria:

          willingness to participate; no previous brain injury or other

          neurological/psychiatric disease such as alcohol abuse

          or severe depression; at least one-month post-onset [dis-

          ease

          duration:

          mean = 7 months;

          standard

          deviation

          (SD) = 12; range 1–86]; ability to follow task instructions;

          and a relatively clear lesion proﬁle (stroke and traumatic'
        excluded_fragments: []
        image_sha256: 4314f51bb4c55bc1e75c7250a3d6e2ecf3954fe45f36287266ee7bb115a24a64
        transcription: '. They were all native Chinese

          speakers and were recruited from the China Rehabilitation

          Research Center based on the following inclusion criteria:

          willingness to participate; no previous brain injury or other

          neurological/psychiatric disease such as alcohol abuse

          or severe depression; at least one-month post-onset [dis-

          ease duration: mean = 7 months; standard deviation

          (SD) = 12; range 1–86]; ability to follow task instructions;

          and a relatively clear lesion profile (stroke and traumatic'
      P3-S2-C9:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 6654810d9f8149b35bd5af1563259c384c0e6519a4fef656c6a1f0decf627d5b
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: e0bc36ecf28b04b23029a474d66fca31d8d967009143e2bf0f1e5c095e538054
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S2-C9
          page: 3
          text_layer_sha256: e0bc36ecf28b04b23029a474d66fca31d8d967009143e2bf0f1e5c095e538054
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Administration of the Edinburgh Handedness Inventory

          (Oldﬁeld 1971) revealed that all patients were right-han-

          ded.'
        anchor_text: 'Administration of the Edinburgh Handedness Inventory

          (Oldﬁeld 1971) revealed that all patients were right-han-

          ded.'
        excluded_fragments: []
        image_sha256: d5495efffcb5bcfe4fdc6debf63f2355d1c99195ec9ed929f54bd4d65299330a
        transcription: Administration of the Edinburgh Handedness Inventory (Oldfield
          1971) revealed that all patients were right-handed
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 11
  quote: 'Finally, after introducing all the above control variables

    (age, gender, education, lesion volume in grey matter

    regions of VLSM signiﬁcant results, auditory lexical

    decision score, associative matching score and total lesion

    volume) as covariates together in one analysis, the pho-

    nological encoding scores still correlated signiﬁcantly with

    the integrity of the left SLF in the 63 stroke patients (lesion

    percentage:

    oral

    picture

    naming:

    partial

    r = -0.33,

    p \ 0.02; word reading: partial r = -0.45, p \ 6 9 10-4;

    mean FA: oral picture naming: partial r = 0.37, p \ 0.006;

    word reading: partial r = 0.41, p \ 0.002).'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-24'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
