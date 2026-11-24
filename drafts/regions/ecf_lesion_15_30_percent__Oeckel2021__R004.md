---
id: ecf_lesion_15_30_percent
name: extreme capsule cluster (15-30% lesion)
kind: network
findings:
- id: f1
  target: aphasia
  target_kind: impairment
  claim: Stroke patients with 15-30% extreme capsule (ECF) lesion were at greater
    odds to be affected with aphasia than those without ECF lesions, after adjusting
    for arcuate fascicle (AF) lesions, stroke volume, age, and gender.
  direction: likely
  relationship: correlational
  method: LSM
  sample:
    n: 123
    population: Patients with acute left-hemispheric ischaemic infarcts without lesions
      in the functional ROIs of the language network (Stanford atlas).
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
  - Small sample size of aphasia cases (n=18).
  - The ECF template may overlap with the uncinate fascicle and inferior frontal-occipital
    fascicle, making them not conceptually differentiable.
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Patient lesion overlap of 15% to 30% of the slice
    plane of a reference extreme capsule (ECF) fibre template generated through global
    fibre tractography. Adjusted for AF lesions, stroke volume, age (cut-off 70 years),
    and gender. Additional metadata has not been transcribed; review the pending-field
    flags before approval. PDF image reading (P8-S1-C7, two-model agreement, human
    verification pending): . The subgroups

    with 15–30% ECF lesion (OR = 18.31, 95% confidence

    interval: 1.86–180.77, P = 0.013) as well as patients with

    >30% ECF lesion (OR = 15.32, 95% confidence interval:

    2.31–101.57, P = 0.005) showed the same risk of apha-

    sia Original text-layer quotation is preserved below. PDF image reading (P5-S2-C8,
    two-model agreement, human verification pending): Results


    The study cohort consisted of 123 patients with acute left-hemispheric ischaemic
    infarcts without lesions in the functional ROIs of the language network Original
    text-layer quotation is preserved below. PDF image reading (P8-S3-C2, two-model
    agreement, human verification pending): . The size of the study

    cohort of 123 stroke patients including 18 (14.6%) with

    aphasia may be considered as a study limitation Original text-layer quotation
    is preserved below. Reconcile this new analysis with earlier drafts and source-review
    decisions for the paper; new candidate IDs do not carry earlier decisions forward.'
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
    - not_transcribed:sample.time_post_onset
    - prior_paper_decisions_reconciliation_pending
    - proposed_concept:aphasia
  citation: '@Oeckel2021'
  source_passages:
  - section: Original source P8-S1-C7
    page: 8
    quote: 'The

      subgroups

      with 15–30% ECF lesion (OR ¼ 18.31, 95% confidence

      interval: 1.86–180.77, P ¼ 0.013) as well as patients with

      >30% ECF lesion (OR ¼ 15.32, 95% confidence interval:

      2.31–101.57, P ¼ 0.005) showed the same risk of apha-

      sia.'
    supports: claim
  - section: Original source P5-S2-C6
    page: 5
    quote: 'We used multivari-

      ate logistic regression to estimate the odds ratio (OR) of

      aphasia, associated with ECF lesions compared with no

      ECF lesions, adjusting for AF lesions, stroke volume as a

      continuous variable, age (dichotomous with cut-off at

      70 years) and gender.'
    supports: method
  - section: Original source P5-S2-C8
    page: 5
    quote: 'Results

      The study cohort consisted of 123 patients with acute

      left-hemispheric ischaemic infarcts without lesions in the

      functional ROIs of the language network.'
    supports: method
  - section: Original source P5-S1-C10
    page: 5
    quote: 'Assuming that associ-

      ation fibres are discontinued as soon as the lesion overlaps

      with at least one slice of an ROI, we computed the max-

      imum percentage of overlap across the slices of ECF and

      AF ROIs for each patient.'
    supports: method
  - section: Original source P5-S2-C8
    page: 5
    quote: 'Results

      The study cohort consisted of 123 patients with acute

      left-hemispheric ischaemic infarcts without lesions in the

      functional ROIs of the language network.'
    supports: sample
  - section: Original source P8-S2-C5
    page: 8
    quote: 'There is an on-

      going

      discussion

      about

      the

      correct

      naming

      of

      the

      language-related ventral tracts running through the ex-

      treme capsule, consisting of uncinate fascicle, inferior

      frontal-occipital fascicle and ECF.14,41 We took great care

      to separate the ECF but are well aware that the three

      tracts anatomically overlap within the extreme capsule,42

      and thus may be not really differentiable conceptually.'
    supports: limitation
  - section: Original source P8-S3-C2
    page: 8
    quote: 'The size of the study

      cohort of 123 stroke patients including 18 (14.6%) with

      aphasia

      may

      be

      considered

      as

      a

      study

      limitation.'
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-25'
relationship_review:
  paper: Oeckel2021
  proposal_id: R004
  review_status_sha256: e40b450799a23d12f927332c099bf0f5e5e4f9bab51f289dc5f74e4c0db7ae88
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 00103d75e25b594a6d03d2307f95a3a74e4b0e05673537ffd7c34149926a91ec
    original_review_binding:
      version: relationship-review-v5
      input_hashes:
        pdf: 00103d75e25b594a6d03d2307f95a3a74e4b0e05673537ffd7c34149926a91ec
        A/passages.json: 98a0dd62439e67dd17651b68d9b3b8d4c8019340226a70c501f9e9b95d63df9b
        A/raw.json: bc00e8fd7bc55a6fd1667e12dc098fc67d644116344cf9cd8dfd5bb5d42a651a
        A/source-units.json: da8df2b6522ecc2653e879d21bffc8e79c7382deefdf99c815473313ebbfef88
        A/full-source-units.json: 1c36c2b449a4a34be91732632952d46ffd9a362de2356ed2b83a85298ad05653
        A/meta.json: f682fd601bdb2ed394553e838a0272b57edf50fea69a6cf8e79187a8a8a82fa2
        A/table-images/TABLE-1-page-6-1.png: 0fccdc779d75a0a12d6c5e29b9b25ca8ccad012e531af42a6a53fca15d4468ca
        A/table-images/page-6.png: 2bc4e973c062e464c8ca9722105d7c6a142b09696febabecd3af99e8480b9c3f
        A/table-images/page-7.png: 5f967699aa5cf7b899378be2414da2cf82e8e9f3681b5ac832063df6fe7bdb2d
        A/table-images/manifest.json: 67523da4d010c6fb88b0c40b32af1ab9d009996083b81dd03ef70569872de400
        A/table-images/TABLE-2-page-6-2.png: 7c6006e02512fa45f62fc1b40d6055f904280a9f1fdf2d2c94347109b80b83a7
        A/table-images/TABLE-3-page-7-1.png: 938bb44b6178918eb664b2b5cffcbaf7f23fd55fca04c6ca993985a826ddd452
        A/clauses/window-03/raw.json: c93fee4a477e9019fb71c3234663be9dea9cc05c9c0117b3e8237eba7687a41a
        A/clauses/window-03/prompt.txt: ee36d78bc10edb3726a2a7d77d16447b64e236212522b824c3ec36a52549fae9
        A/clauses/window-03/meta.json: eec2770de8b95e7cc9cc25c1f2aa543dbd3a6d30cdd3fc4a5346f815d91edff2
        A/clauses/window-04/raw.json: 0ace9af37d34fdccc670708f5df4cb3f443543854c10379b7bba63e4539a14cf
        A/clauses/window-04/prompt.txt: 61e141a125386b4228eda533cd8239488c8c22d4c32977d9034b77c1ffdfb947
        A/clauses/window-04/meta.json: 480a37dd972fbfcdd03f3ff8244bc8e850ed0b3f8dce27b0120c0abdbc6245ed
        A/clauses/window-05/raw.json: 94c9cb32b2d0e1e4bad7e5e1a606cb704edf8ce7635740da9d707fc65202b69b
        A/clauses/window-05/prompt.txt: 589d4b88e6bd66e7684e656d3031a7c11d8091090295dfb3579351959db11cb0
        A/clauses/window-05/meta.json: 9b5d1be5e0d536f8ebac520c926deb389ec0ef681e3828b77cb6bfd2c57f1ec5
        A/clauses/window-02/raw.json: 0955627a83a2d8aee00600c4b935acc3ca38718c90123ed0a9d8c54b887151a7
        A/clauses/window-02/prompt.txt: 25be8a247985763b0588469832c407dd62350180405f83366a10ef2d91998dda
        A/clauses/window-02/meta.json: 9f2468b7eef0a656598ddf59c939043d9db957297c38b030489225b379464ba6
        A/clauses/window-01/raw.json: 4a6ccf498c03519fe85cf95c4cc4a22d49b9d73467281627bbd9d7755d0c5afe
        A/clauses/window-01/prompt.txt: aa187670107125f94b43d569708e91fe73c46a0d9b9ba1c0f776eb3a42a71125
        A/clauses/window-01/meta.json: 0b3ccced2d14e7487fba02aaa93b1e0baa893f8871d03bb728a9e073159a7e6f
        A/tables/TABLE-1-page-6-1/raw.json: e8e979f14f3ff4129dc9fb091c26cdf6ac9d43855006981210376aa04e3c1f7e
        A/tables/TABLE-1-page-6-1/prompt.txt: 40674e6e9a0b1aee6b2fdee07cc862e7b495b0fc149d87986d41675261bf1c16
        A/tables/TABLE-1-page-6-1/meta.json: 5440b775cbd8355abe89f798f7b8934239631d80b9fa9bbfe8c814016098af1e
        A/tables/TABLE-2-page-6-2/raw.json: a3a450872d6cd90d356fca6485c9153cc818f04e2fd2460818ccdffcd5f4143e
        A/tables/TABLE-2-page-6-2/prompt.txt: cd39e5d0194fa64b276a57665e72b295337aa2b1da8742a9ecb85fb1f29c6687
        A/tables/TABLE-2-page-6-2/meta.json: c6e6050b99eb5ae288ac4aeaaf9f8bf9565c5c8d2eb7813ee96dc7968e1d3256
        A/tables/TABLE-3-page-7-3/raw.json: b3e894714d445eae4dbbb1840659ddfc00e1d0a8ff9f41381c1eea85fececaaa
        A/tables/TABLE-3-page-7-3/prompt.txt: 77580ba5208221cda6408221bb003f6067853dbee9e5e39f78043de0ccefa507
        A/tables/TABLE-3-page-7-3/meta.json: 404c5c9dbea341eac162b0700a3274536d22e6de716472b523d81ccf528a4cb0
        B/passages.json: 98a0dd62439e67dd17651b68d9b3b8d4c8019340226a70c501f9e9b95d63df9b
        B/raw.json: e190dea628b1feab883bb5866bba088335ecbdd59d6102d82f5031af49c3ae8d
        B/source-units.json: da8df2b6522ecc2653e879d21bffc8e79c7382deefdf99c815473313ebbfef88
        B/full-source-units.json: 1c36c2b449a4a34be91732632952d46ffd9a362de2356ed2b83a85298ad05653
        B/meta.json: 052ac617616b26f357c76c99a43b5d68f540b7672fb7c16033490a7f12221d7b
        B/table-images/TABLE-1-page-6-1.png: 0fccdc779d75a0a12d6c5e29b9b25ca8ccad012e531af42a6a53fca15d4468ca
        B/table-images/page-6.png: 2bc4e973c062e464c8ca9722105d7c6a142b09696febabecd3af99e8480b9c3f
        B/table-images/page-7.png: 5f967699aa5cf7b899378be2414da2cf82e8e9f3681b5ac832063df6fe7bdb2d
        B/table-images/manifest.json: eea8d456f39556209d717179e2bc8deb650afb3a92cc3c09af29b0cb33d49fed
        B/table-images/TABLE-2-page-6-2.png: 7c6006e02512fa45f62fc1b40d6055f904280a9f1fdf2d2c94347109b80b83a7
        B/table-images/TABLE-3-page-7-1.png: 938bb44b6178918eb664b2b5cffcbaf7f23fd55fca04c6ca993985a826ddd452
        B/clauses/window-03/raw.json: 56ef04d32decd754e5e0a750e5900fff16d3624f9030ecf21435414ba841505b
        B/clauses/window-03/prompt.txt: ee36d78bc10edb3726a2a7d77d16447b64e236212522b824c3ec36a52549fae9
        B/clauses/window-03/meta.json: c600a443b650e67d23df9c1d233060e73de1efc9397ececa9dc35fd385372d23
        B/clauses/window-04/raw.json: 0f5422ee33434548c85ff80508b46a2089f20b793eb2bc3175d17654843e86c4
        B/clauses/window-04/prompt.txt: 61e141a125386b4228eda533cd8239488c8c22d4c32977d9034b77c1ffdfb947
        B/clauses/window-04/meta.json: 7bb639867d87771f843e26609e241e5b3e3e8a7ec77b1b672f52bc1beaec77fa
        B/clauses/window-05/raw.json: 16bfe5aca4bfe8ce6ec99e7595f6de758d10a7e81e50a251bb75d6631d055855
        B/clauses/window-05/prompt.txt: 589d4b88e6bd66e7684e656d3031a7c11d8091090295dfb3579351959db11cb0
        B/clauses/window-05/meta.json: 620196de33753bc1c4905ac827d1373021220c267dd1271f474a79e2ecb58ae4
        B/clauses/window-02/raw.json: 7f04a366270b0c1c8574a40d23c5fd400c039e42df0124afd92b18a7ae0437fa
        B/clauses/window-02/prompt.txt: 25be8a247985763b0588469832c407dd62350180405f83366a10ef2d91998dda
        B/clauses/window-02/meta.json: 67715306043d9c43625fe9614b417213e07d595a939d3c76d2a8c06ce28acaa7
        B/clauses/window-01/raw.json: 3677c09cf603d458ba1b8f810831ab3be5c5f2103551d39e2791fac6613497a1
        B/clauses/window-01/prompt.txt: aa187670107125f94b43d569708e91fe73c46a0d9b9ba1c0f776eb3a42a71125
        B/clauses/window-01/meta.json: 32bd95c79ddfad87dc70c5c988515cc947097b1201d9916831f950a3d170556f
        B/tables/TABLE-1-page-6-1/raw.json: 5533df29580c17d18bc92ebf3fcf4d07cc212fbfbe88f04c3ab92644b596ce82
        B/tables/TABLE-1-page-6-1/prompt.txt: 40674e6e9a0b1aee6b2fdee07cc862e7b495b0fc149d87986d41675261bf1c16
        B/tables/TABLE-1-page-6-1/meta.json: 786a1742f7a496124183eb2e7d6da1e1dff729b134950971823ffe54f71dd59b
        B/tables/TABLE-2-page-6-2/raw.json: 168374d5ebb4245d2dd3d46ffaaff3bc7f5108a7890d1e1a99b88c8cc1c85070
        B/tables/TABLE-2-page-6-2/prompt.txt: cd39e5d0194fa64b276a57665e72b295337aa2b1da8742a9ecb85fb1f29c6687
        B/tables/TABLE-2-page-6-2/meta.json: 8b9d180ac06e8153a8a499f75b646d74b1c7b1d8ef9c6731b9b2c1d08d1baa45
        B/tables/TABLE-3-page-7-3/raw.json: 61682513384c8a0a709af8001a280285f3271bcb3cb4264066091ffcda82b4f4
        B/tables/TABLE-3-page-7-3/prompt.txt: 77580ba5208221cda6408221bb003f6067853dbee9e5e39f78043de0ccefa507
        B/tables/TABLE-3-page-7-3/meta.json: 735ba3c736212d1cc5be3fabc598fefa65c0588b6d60d58081e6553ff8530152
      code:
        relationship_review.py: 6d0359072ca11a7569362fe49703755a98b4207ba814fcd311161c48936053ed
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
      pdf_sha256: 00103d75e25b594a6d03d2307f95a3a74e4b0e05673537ffd7c34149926a91ec
      source_review: _compare/relationships-2026-11-16/review-current/Oeckel2021
      source_status_sha256: e962120d69715a0ab035dbd15b292b7425053d5972a9ad35530a2842640c3c0f
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R004
    exposure:
      text: ECF lesion 15-30%
    outcome:
      text: aphasia
    analysis_label: multivariate logistic regression
    relation: sensitivity
    evidence_ids:
    - P8-S1-C7
    qualifier_ids:
    - P5-S2-C6
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 00103d75e25b594a6d03d2307f95a3a74e4b0e05673537ffd7c34149926a91ec
      source_review: _compare/relationships-2026-11-16/review-current/Oeckel2021
      source_status_sha256: e962120d69715a0ab035dbd15b292b7425053d5972a9ad35530a2842640c3c0f
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P7-S1-C3
      - Result passage disposed without unit P7-S1-C4
      - Result passage disposed without unit P7-S1-C5
      - Result passage disposed without unit P7-S1-C6
      - Result passage disposed without unit P8-S1-C1
      - Result passage disposed without unit P8-S1-C2
      - Result passage disposed without unit P8-S1-C3
      - Result passage disposed without unit P8-S3-C11
      - Result passage disposed without unit P8-S3-C13
      unattached_null_or_qualifier_ids: []
      suppressed_nonrepresented_units: 7
      default_disposition_count_requires_completeness_check: 111
      unselected_timing_passages:
      - P1-S1-C3
      - P3-S1-C7
      - P3-S1-C8
      - P3-S1-C9
      - P3-S2-C2
      - P3-S2-C4
      - P3-S2-C5
      - P5-S2-C8
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P1-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P1-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S3-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S2-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: analysed_sample
        source_ids:
        - P1-S1-C3
        - P3-S2-C4
        - P3-S2-C6
        - P5-S2-C8
        - P6-S1-C1
        - P7-S1-C4
        - P8-S1-C2
        - P8-S1-C10
        - P8-S3-C2
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: eligibility
        source_ids:
        - P1-S1-C3
        - P2-S2-C5
        - P3-S1-C2
        - P3-S1-C3
        - P3-S1-C4
        - P3-S1-C8
        - P3-S1-C9
        - P3-S2-C2
        - P3-S2-C3
        - P3-S2-C6
        - P5-S1-C13
        - P5-S2-C8
        - P8-S1-C12
        - P8-S2-C10
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: imaging_provenance
        source_ids:
        - P1-S1-C4
        - P3-S1-C1
        - P3-S3-C5
        - P4-S1-C10
        - P4-S1-C11
        - P4-S1-C12
        - P5-S2-C10
        - P5-S2-C11
        - P5-S2-C12
        - P8-S1-C17
        - P8-S2-C7
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: outcome_definition
        source_ids:
        - P1-S1-C4
        - P1-S1-C5
        - P1-S1-C6
        - P3-S2-C7
        - P3-S2-C8
        - P5-S1-C9
        - P5-S1-C10
        - P5-S1-C13
        - P7-S1-C2
        - P8-S1-C14
        - P8-S3-C9
        - P8-S3-C12
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - analysed_sample
      - eligibility
      - imaging_provenance
      - outcome_definition
      - validation
      - tested_personal_effects
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-6-1
      - TABLE-2-page-6-2
      - TABLE-3-page-7-3
      unlinked_tables:
      - TABLE-1-page-6-1
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P3-S2
        - P3-S3
        - P4-S1
        - P5-S1
        - P5-S2
        - P7-S1
        - P8-S1
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 00103d75e25b594a6d03d2307f95a3a74e4b0e05673537ffd7c34149926a91ec
      source_review: _compare/relationships-2026-11-16/review-current/Oeckel2021
      source_status_sha256: e962120d69715a0ab035dbd15b292b7425053d5972a9ad35530a2842640c3c0f
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C5
      disposition: represented
      result_indexes:
      - 2
      reason: Reports adjusted OR for ECF lesion >15%.
    - source_id: P1-S1-C6
      disposition: represented
      result_indexes:
      - 6
      reason: Reports null association for AF lesions >15%.
    - source_id: P3-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes patient exclusion due to testing impossibility.
    - source_id: P3-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes ambiguous categorization of patients.
    - source_id: P3-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes allocation of ambiguous patients to non-aphasia group.
    - source_id: P7-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes aphasia diagnosis counts.
    - source_id: P7-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes cohort demographics.
    - source_id: P7-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes prevalence of ECF and AF lesions.
    - source_id: P7-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Defines median split threshold.
    - source_id: P7-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes mean stroke volume.
    - source_id: P8-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes stroke onset timing.
    - source_id: P8-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports aphasia prevalence.
    - source_id: P8-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports no difference in timing intervals.
    - source_id: P8-S1-C5
      disposition: represented
      result_indexes:
      - 0
      - 1
      reason: Reports univariate significance for ECF and null for AF.
    - source_id: P8-S1-C6
      disposition: represented
      result_indexes:
      - 2
      reason: Reports adjusted OR for ECF lesion >15%.
    - source_id: P8-S1-C7
      disposition: represented
      result_indexes:
      - 3
      - 4
      reason: Reports adjusted OR for ECF subgroups.
    - source_id: P8-S1-C8
      disposition: represented
      result_indexes:
      - 6
      reason: Reports adjusted OR for AF lesions >15%.
    - source_id: P8-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports lack of interaction between ECF and AF.
    - source_id: P8-S1-C12
      disposition: repeated
      result_indexes:
      - 0
      - 2
      reason: Restatement of ECF association in discussion.
    - source_id: P8-S1-C13
      disposition: repeated
      result_indexes:
      - 2
      reason: Restatement of adjusted OR for ECF >15%.
    - source_id: P8-S1-C14
      disposition: repeated
      result_indexes:
      - 1
      - 6
      reason: Restatement of AF null findings.
    - source_id: P8-S1-C15
      disposition: represented
      result_indexes:
      - 7
      - 8
      - 9
      reason: Reports lack of independent association for volume, gender, and age.
    - source_id: P8-S2-C4
      disposition: repeated
      result_indexes:
      - 0
      - 2
      reason: Restatement of ECF association.
    - source_id: P8-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discusses cut-off sensitivity.
    - source_id: P8-S3-C3
      disposition: repeated
      result_indexes:
      - 0
      - 2
      reason: Restatement of ECF association.
    - source_id: P8-S3-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discusses specificity of patient selection.
    - source_id: P8-S3-C13
      disposition: repeated
      result_indexes:
      - 0
      - 2
      reason: Conclusion restating ECF effect.
    - source_id: P9-S2-C3
      disposition: repeated
      result_indexes:
      - 0
      - 2
      reason: Conclusion restating ECF relevance.
    - source_id: P9-S2-C4
      disposition: repeated
      result_indexes:
      - 2
      - 6
      reason: Conclusion restating ECF as independent predictor vs AF.
    unresolved_coverage:
    - source_id: P8-S1-C15
      disposition: unresolved
      reason: Unknown result index; not accepted as coverage
    pending_source_ids:
    - P3-S2-C5
    - P3-S2-C9
    - P3-S2-C10
    - P7-S1-C2
    - P7-S1-C3
    - P7-S1-C4
    - P7-S1-C5
    - P7-S1-C6
    - P8-S1-C1
    - P8-S1-C2
    - P8-S1-C3
    - P8-S1-C9
    - P8-S1-C12
    - P8-S1-C13
    - P8-S1-C14
    - P8-S2-C4
    - P8-S2-C9
    - P8-S3-C3
    - P8-S3-C11
    - P8-S3-C13
    - P9-S2-C3
    - P9-S2-C4
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-6-1
    - TABLE-2-page-6-2
    - TABLE-3-page-7-3
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample: []
      recruited_sample:
      - P1-S1-C3
      - P3-S1-C7
      - P5-S2-C8
      - P6-S1-C1
      - P7-S1-C4
      - P8-S1-C2
      - P8-S1-C10
      - P8-S2-C10
      eligibility: []
      imaging_provenance: []
      imaging_timing:
      - P3-S1-C4
      - P8-S1-C3
      - P8-S2-C10
      outcome_timing:
      - P3-S1-C4
      - P5-S2-C9
      - P7-S1-C1
      - P8-S1-C3
      - P8-S2-C10
      outcome_definition: []
      validation: []
      analysis_restrictions:
      - P2-S2-C5
      - P3-S1-C2
      - P3-S1-C3
      - P3-S2-C6
      - P8-S3-C8
      dependent_variable_statement:
      - P1-S1-C4
      - P3-S2-C7
      - P5-S1-C10
      - P5-S2-C6
      limitations:
      - P8-S3-C2
      - P8-S3-C4
      - P8-S3-C5
      - P8-S3-C7
      - P8-S3-C8
      personal_factors:
      - P5-S1-C11
      - P6-S1-C1
      - P7-S1-C3
      - P8-S1-C15
      tested_personal_effects: []
      adjustment_roles:
      - P5-S1-C11
      - P5-S2-C6
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P1-S1-C3
      - P3-S2-C2
      - P5-S1-C11
      - P6-S1-C1
      - P7-S1-C3
      - P8-S1-C15
      - P8-S3-C2
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: none_described
    window_merge: Union of selected IDs; differing window enums retained conservatively
      as both/mixed. Not verified study-level facts.
    held_selections:
    - slot: dependent_variable_statement
      source_id: P1-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P1-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S3-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S2-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: analysed_sample
      source_ids:
      - P1-S1-C3
      - P3-S2-C4
      - P3-S2-C6
      - P5-S2-C8
      - P6-S1-C1
      - P7-S1-C4
      - P8-S1-C2
      - P8-S1-C10
      - P8-S3-C2
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: eligibility
      source_ids:
      - P1-S1-C3
      - P2-S2-C5
      - P3-S1-C2
      - P3-S1-C3
      - P3-S1-C4
      - P3-S1-C8
      - P3-S1-C9
      - P3-S2-C2
      - P3-S2-C3
      - P3-S2-C6
      - P5-S1-C13
      - P5-S2-C8
      - P8-S1-C12
      - P8-S2-C10
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: imaging_provenance
      source_ids:
      - P1-S1-C4
      - P3-S1-C1
      - P3-S3-C5
      - P4-S1-C10
      - P4-S1-C11
      - P4-S1-C12
      - P5-S2-C10
      - P5-S2-C11
      - P5-S2-C12
      - P8-S1-C17
      - P8-S2-C7
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: outcome_definition
      source_ids:
      - P1-S1-C4
      - P1-S1-C5
      - P1-S1-C6
      - P3-S2-C7
      - P3-S2-C8
      - P5-S1-C9
      - P5-S1-C10
      - P5-S1-C13
      - P7-S1-C2
      - P8-S1-C14
      - P8-S3-C9
      - P8-S3-C12
      reason: Runaway selection (>8 passages); entire slot requires source review
    policy: All slots and enums remain unverified. Held selections are not evidence
      of absence. Original responses are preserved in frame/chunk-*/attempt-*/raw.json.
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
      pdf_sha256: 00103d75e25b594a6d03d2307f95a3a74e4b0e05673537ffd7c34149926a91ec
      review_sha256: e40b450799a23d12f927332c099bf0f5e5e4f9bab51f289dc5f74e4c0db7ae88
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
      - P8-S1-C7
      source_result: In a multivariate logistic regression analysis of 123 patients
        with acute left-hemispheric ischaemic stroke, patients with 15–30% lesion
        overlap of the extreme capsule (ECF) had significantly greater odds of aphasia
        (OR 18.31, 95% CI 1.86–180.77, P = 0.013) compared to those without ECF lesions,
        after adjusting for arcuate fascicle lesions, stroke volume, age, and gender.
      result_status: detected
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis corresponds to the multivariate logistic regression
            subgroup analysis for ECF lesions in the 15–30% range, as described in
            P8-S1-C7 and P5-S2-C6. The model includes the specified covariates (AF,
            stroke volume, age, gender).
          source_ids:
          - P8-S1-C7
          - P5-S2-C6
        direction:
          answer: fits
          reason: The source explicitly states that patients with 15–30% ECF lesions
            showed a significant risk of aphasia (OR 18.31, P=0.013). The draft claim
            that they were 'at greater odds' aligns with this detected positive association.
          source_ids:
          - P8-S1-C7
        construct:
          answer: fits
          reason: The exposure is correctly identified as ECF lesion overlap (15-30%)
            measured via template overlap (P5-S1-C10, P8-S2-C7). The outcome is aphasia
            defined by the Token Test (P3-S2-C8). The method is multivariate logistic
            regression (P5-S2-C6).
          source_ids:
          - P5-S1-C10
          - P3-S2-C8
          - P5-S2-C6
        qualifications:
          answer: fits
          reason: The draft correctly includes the adjustment for AF lesions, stroke
            volume, age, and gender, which are the covariates specified in the multivariate
            model (P5-S2-C6). It also correctly notes the limitation regarding the
            anatomical overlap of ECF with other tracts (P8-S2-C5) and the small sample
            size (P8-S3-C2).
          source_ids:
          - P5-S2-C6
          - P8-S2-C5
          - P8-S3-C2
        missing_material_caveat:
          answer: fits
          reason: 'The draft captures the key limitations: the arbitrary nature of
            the 15% cut-off (median split) and the potential confounding by overlapping
            tracts (uncinate/IFOF). The ''proof-of-concept'' nature and lack of external
            validation are also relevant but the core statistical interpretation is
            preserved.'
          source_ids:
          - P8-S2-C8
          - P8-S2-C5
          - P8-S3-C4
      optional_pending:
      - 'sample.time_post_onset: Source P7-S1-C1 indicates mean 3.93 days, range 0-10
        days, but this was not transcribed into the draft fields.'
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - 'sample.time_post_onset: source confirmation required; original proposed wording
      remains in the audit.'
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - 'sample.time_post_onset: Source P7-S1-C1 indicates mean 3.93 days, range 0-10
      days, but this was not transcribed into the draft fields.'
    normalizations:
    - field: bucket
      original: predictors
      action: route_from_kind
      value: regions
    - field: sample.time_post_onset
      original: Assessment performed within 10 days after first-time stroke.
      action: not_transcribed
      reason: 'Numbers not grounded in usable selected source readings: 1E+1'
    analysis_identity:
      id: R004
      exposure:
        text: ECF lesion 15-30%
      outcome:
        text: aphasia
      analysis_label: multivariate logistic regression
      relation: sensitivity
      evidence_ids:
      - P8-S1-C7
      qualifier_ids:
      - P5-S2-C6
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 00103d75e25b594a6d03d2307f95a3a74e4b0e05673537ffd7c34149926a91ec
        source_review: _compare/relationships-2026-11-16/review-current/Oeckel2021
        source_status_sha256: e962120d69715a0ab035dbd15b292b7425053d5972a9ad35530a2842640c3c0f
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P8-S1-C7:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 00103d75e25b594a6d03d2307f95a3a74e4b0e05673537ffd7c34149926a91ec
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: a4419730f12e0c915d93bf4ffdc75604e3178446d7ab6f209cdc954fe254c8dc
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P8-S1-C7
          page: 8
          text_layer_sha256: a4419730f12e0c915d93bf4ffdc75604e3178446d7ab6f209cdc954fe254c8dc
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'The

          subgroups

          with 15–30% ECF lesion (OR ¼ 18.31, 95% confidence

          interval: 1.86–180.77, P ¼ 0.013) as well as patients with

          >30% ECF lesion (OR ¼ 15.32, 95% confidence interval:

          2.31–101.57, P ¼ 0.005) showed the same risk of apha-

          sia.'
        anchor_text: 'The

          subgroups

          with 15–30% ECF lesion (OR ¼ 18.31, 95% confidence

          interval: 1.86–180.77, P ¼ 0.013) as well as patients with

          >30% ECF lesion (OR ¼ 15.32, 95% confidence interval:

          2.31–101.57, P ¼ 0.005) showed the same risk of apha-

          sia.'
        excluded_fragments: []
        image_sha256: 4b40dd679d2ac2ed9f2d042ce369f9d8624156e533c553aece2f023028d5ba00
        transcription: '. The subgroups

          with 15–30% ECF lesion (OR = 18.31, 95% confidence

          interval: 1.86–180.77, P = 0.013) as well as patients with

          >30% ECF lesion (OR = 15.32, 95% confidence interval:

          2.31–101.57, P = 0.005) showed the same risk of apha-

          sia'
      P5-S2-C8:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 00103d75e25b594a6d03d2307f95a3a74e4b0e05673537ffd7c34149926a91ec
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 70f4507168f56bce3f8e0d30f1606bf24fec5ab9c1b0cebe32a80c121aa54aa9
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P5-S2-C8
          page: 5
          text_layer_sha256: 70f4507168f56bce3f8e0d30f1606bf24fec5ab9c1b0cebe32a80c121aa54aa9
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Results

          The study cohort consisted of 123 patients with acute

          left-hemispheric ischaemic infarcts without lesions in the

          functional ROIs of the language network.'
        anchor_text: 'Results

          The study cohort consisted of 123 patients with acute

          left-hemispheric ischaemic infarcts without lesions in the

          functional ROIs of the language network.'
        excluded_fragments: []
        image_sha256: 8e16c790551a5cdbd12551799b59db8c588bde20cd5a2158bca91602088193f6
        transcription: 'Results


          The study cohort consisted of 123 patients with acute left-hemispheric ischaemic
          infarcts without lesions in the functional ROIs of the language network'
      P8-S3-C2:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 00103d75e25b594a6d03d2307f95a3a74e4b0e05673537ffd7c34149926a91ec
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 0d404f96472acf5b742b6e56599e91d017c47df3e5388bbaf02b5d57afed56b8
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P8-S3-C2
          page: 8
          text_layer_sha256: 0d404f96472acf5b742b6e56599e91d017c47df3e5388bbaf02b5d57afed56b8
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'The size of the study

          cohort of 123 stroke patients including 18 (14.6%) with

          aphasia

          may

          be

          considered

          as

          a

          study

          limitation.'
        anchor_text: 'The size of the study

          cohort of 123 stroke patients including 18 (14.6%) with

          aphasia

          may

          be

          considered

          as

          a

          study

          limitation.'
        excluded_fragments: []
        image_sha256: cbd0fe7fc7a852dd3525a3511e3447869a068260fc4ac3117c0c7193b146c4fc
        transcription: '. The size of the study

          cohort of 123 stroke patients including 18 (14.6%) with

          aphasia may be considered as a study limitation'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 8
  quote: 'The

    subgroups

    with 15–30% ECF lesion (OR ¼ 18.31, 95% confidence

    interval: 1.86–180.77, P ¼ 0.013) as well as patients with

    >30% ECF lesion (OR ¼ 15.32, 95% confidence interval:

    2.31–101.57, P ¼ 0.005) showed the same risk of apha-

    sia.'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-25'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
