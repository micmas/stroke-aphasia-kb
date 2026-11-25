---
id: early_depressive_symptoms
name: early depressive symptoms
kind: predictor
findings:
- id: f1
  target: late_depressive_symptoms
  target_kind: impairment
  claim: participants with depressive symptoms within the first week were somewhat
    more likely to have depressive symptoms at 12 months, compared to participants
    without such symptoms within the first week
  direction: likely
  relationship: correlational
  method: behavioral_only
  sample:
    n: 142
    population: ischaemic stroke survivors
    phase: not_reported
    time_post_onset: concurrent association between first week and 12 months post-stroke
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - majority of participants had mild neurological deficits (NIHSS ≤6 at day 3 to
    7)
  - did not adjust for previous history of depression or treatment for depression
    during the study
  - participants without MADRS scores at all three time points were excluded
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: presence of depressive symptoms (MADRS score ≥7) measured
    within the first week (3 to 7 days, ± 1 day) post-stroke. MADRS scores were dichotomised
    into present (≥7) or absent (<7). Additional metadata has not been transcribed;
    review the pending-field flags before approval.'
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
    - proposed_concept:late_depressive_symptoms
  citation: '@Sewell2025'
  source_passages:
  - section: Original source P3-S1-C10
    page: 3
    quote: "Likelihood of experiencing depressive symptoms at later time points based\
      \ \non depressive symptom status at earlier time points\nLogistic regression\
      \ models demonstrated that participants with \ndepressive symptoms within the\
      \ first week were somewhat more likely \nto have depressive symptoms, compared\
      \ to participants without such \nsymptoms within the first week, at both 3 months\
      \ (OR 2.78, 95% CI \n[1.39, 5.59]; p = 0.004) and 12 months (OR 2.07, 95% CI\
      \ [1.02, 4.18]; p \n= 0.044)."
    supports: claim
  - section: Original source P2-S3-C2
    page: 2
    quote: "The National Institutes of Health Stroke Scale \n(NIHSS) was used to evaluate\
      \ stroke severity within the first week (day 3 \nto 7, ± 1 day).20 The Montgomery-Åsberg\
      \ Depression Rating Scale \n(MADRS)21 was utilised to determine depressive symptom\
      \ status at each \ntime point: within the first week (3 to 7 days, ± 1 day),\
      \ at 3 months (± 7 \ndays) and at 12 months (± 7 days) following stroke."
    supports: method
  - section: Original source P2-S3-C5
    page: 2
    quote: "Total MADRS scores were dichotomised into depressive symptoms \n‘present’\
      \ (score ≥7) or ‘absent’ (score < 7)."
    supports: method
  - section: Original source P2-S4-C8
    page: 2
    quote: "Statistical analyses were conducted using Stata version 16.1.27\nResults\n\
      Participants\nOf the 142 ischaemic stroke survivors, 96 (67.6%) were male; mean\
      \ \nage at stroke was 67 (SD = 13), range 27 to 91 years."
    supports: sample
  - section: Original source P2-S2-C7
    page: 2
    quote: "Eligibility criteria required partic­\nipants to be diagnosed with acute\
      \ ischaemic stroke, aged 18 years or \nolder, English-speaking, and with no\
      \ significant disability prior to their \nstroke as determined by a modified\
      \ Rankin Scale (mRS) score ≤2.19\nAdditional inclusion criteria for thrombolysis\
      \ were required for partic­\nipants recruited through the START EXTEND arm.18\n\
      Measures\nData collected on admission included: age, sex, prior history of stroke\
      \ \nand premorbid disability."
    supports: sample
  - section: Original source P5-S1-C1
    page: 5
    quote: "\nJournal of Stroke and Cerebrovascular Diseases 34 (2025) 108197\n5\n\
      Study limitations\nOur sample had a lower mean age at stroke and lower proportion\
      \ of \nfemales compared with national figures published by the Australian \n\
      Stroke Clinical Registry (mean age = 73 years, SD = 13; females 45%).51\nAll\
      \ our participants had ischaemic stroke, consistent with the inclusion \ncriteria,\
      \ whereas only 70% of registry patients had ischaemic stroke.51\nDespite efforts\
      \ to support the inclusion of patients with severe neuro­\nlogical impairments,\
      \ the majority of participants in this cohort had an \nNIHSS score ≤6 at day\
      \ 3 to 7, indicating mild neurological deficits.52\nNext, the MADRS yields scores\
      \ which produce a continuous variable; \nhowever, in our study the scores were\
      \ dichotomised."
    supports: limitation
  - section: Original source P5-S1-C5
    page: 5
    quote: "Last, our study does not report, nor adjust for, participants who \nhad\
      \ previously had depression, or who received treatment for depres­\nsion during\
      \ the study."
    supports: limitation
  - section: Original source P5-S1-C4
    page: 5
    quote: "Further, participants from \nthe larger cohort for whom a MADRS score\
      \ was not recorded at all three \ntime points were excluded for analysis in\
      \ this particular study; this may \ncontribute to biased inferences from findings\
      \ and impact on general­\nisability."
    supports: limitation
predictor_type: clinical
short_definition: presence of depressive symptoms (MADRS score ≥7) measured within
  the first week (3 to 7 days, ± 1 day) post-stroke
assessment:
- Montgomery-Åsberg Depression Rating Scale
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-25'
relationship_review:
  paper: Sewell2025
  proposal_id: R003
  review_status_sha256: 1c581c428dfa0df96071ecfb25e12385932d727caea3453b82f7b4038b6460b6
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 2ff4924a20fb1db57ab84d972482c37ce1531fd4758fe92bafdc6f13d175a9f7
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 2ff4924a20fb1db57ab84d972482c37ce1531fd4758fe92bafdc6f13d175a9f7
        A/passages.json: 2569a6fe8c342e5e6bd5606dc182ea589c8b35753814ea78a7050fafa27fabfe
        A/raw.json: 94cdc21b5f12f8b25fa053d4bdbbddd5c3e54d3d039e696191f2a153c991f4d7
        A/source-units.json: 60e88076c660bc1bd1ab8e8445ff387040f26795e4b9b3ff79c711a03f07a2d9
        A/full-source-units.json: 3766b61d5b37e79e90f50680ee78734d0903eccbb1199a43baac52ff521afc46
        A/meta.json: 17300372f36e0c75fe99459c8843d5e99949ea28e16557a9e8a85729d2c6faeb
        A/table-images/TABLE-1-page-3-1.png: 8c24153377a49ccad7b45d180a5dd91b62da0f34c3fd82190ac5b0d0d147092e
        A/table-images/page-3.png: 2830f76151060403251a4b364eccfe6f6edde541dd856d30ab7f7ab359187250
        A/table-images/page-4.png: de08d5e27c381f62980c055356b489ea455a98dc34d2111ad4481ac5a20c61d5
        A/table-images/TABLE-3-page-4-2.png: dae3ddc166b8cf33a48562572d3c5174fa606103a944f5ea8a3c2aaea354edd6
        A/table-images/manifest.json: 162620577314fe5885c807c55b041693b678986240d8abc76fee1096ac7647da
        A/table-images/TABLE-2-page-4-1.png: bb30411ba11508d0a864176938c5bebe917c502331418c74a58bfe775126e93d
        A/clauses/window-03/raw.json: f2b7627392ca373699071cbf5e991eb804ca4fc4383b6a1270c49ed02df11e1d
        A/clauses/window-03/prompt.txt: 10aa18139a040d39257369bcca8a88310fd3aafbbeafedd650777a06639c2d5a
        A/clauses/window-03/meta.json: 4fbb7225087d13aed168782b6a3e8ffa2b79fc59c13b96e2bf974d81d7876b82
        A/clauses/window-04/raw.json: 7e52c6aa2ce6d161805facd20b20ecb939a7167c07e0990168d9c996e11fab17
        A/clauses/window-04/prompt.txt: da4c6f9a1a61e34e8941ba5baf5284c640d06054c03c9ba482e8dd9410ac53b1
        A/clauses/window-04/meta.json: ed7cc19efdde3bfc1926779db5a6cbc7ca427333aa8e2562b5f5f2b53efd5c3a
        A/clauses/window-05/raw.json: 7ff1d1363224d0271bc304d7758f080c61875a9ce5b38be36f9818e4c6909344
        A/clauses/window-05/prompt.txt: 95debe1cd4f49603d372a45063635fa81f6c5020fb5ca0e2c471630219eaada5
        A/clauses/window-05/meta.json: 1443ef4c1984fe46004e8ea8c353024214c5dc4aa6e54bb9a87cee73ba266bd4
        A/clauses/window-02/raw.json: 33026ca5099cae4a16d6d2e8668d66211bbe9b6d44d5ab4a0920f49a05f01736
        A/clauses/window-02/prompt.txt: f233107c16edde04b8c664b210eac94d20c26beb065d9507a0a9e6138df17983
        A/clauses/window-02/meta.json: 78766a5bfaadc25fff609fc6c993d0852f5383d8c46b0f9cbb490c8d484dbd40
        A/clauses/window-01/raw.json: 1579db0741e8d7ab660b8e617ed04199406563ce852dc9462ef0561cc73284a4
        A/clauses/window-01/prompt.txt: b77f4db4be064f062658f19f2784890b007170c15355a00f9a623c7b6527a824
        A/clauses/window-01/meta.json: beac22a3029e1a254089880f04a012db3baeee3779850f32f3efcc4cda1dcc94
        A/tables/TABLE-1-page-3-1/raw.json: bdc40b7ecef4c38f48cd3003c1725ac6f3fa5b62d85286d2d1b8caf695b3c11b
        A/tables/TABLE-1-page-3-1/prompt.txt: b384aec910f232ba0188e6f00d2ecc63b62c1eac495d1acf5f3fe0b2de9dbf6e
        A/tables/TABLE-1-page-3-1/meta.json: 535bc9ad52fa79382c11b06aa120632c68e4adb32986468366cf0c67fd9c83f1
        A/tables/TABLE-3-page-4-3/raw.json: 0537e6f471dffbdc16f990ca5f1403057a48d0acd286bdd2f6f0121491961c87
        A/tables/TABLE-3-page-4-3/prompt.txt: 855021c6c147f5715a86d9f5963b21943c3e390b9f6b4be15f60c401650d131a
        A/tables/TABLE-3-page-4-3/meta.json: d4453bf352491d8a8e1044a3fd062cb7139600176c9e51dde0451446cf32e53d
        A/tables/TABLE-2-page-4-2/raw.json: 04106308cbb9084cf1d44d41b451c5eac43356dd7511e3d9afb3f346734f52a2
        A/tables/TABLE-2-page-4-2/prompt.txt: 1faf342daa204c5c1fc05df56b141ac24aaba6bf571afc7b82870c2d5b2657ca
        A/tables/TABLE-2-page-4-2/meta.json: 5eb6b890d529d1f195ed48bdae5882ebd68979549199277acf87df6227253f5d
        B/passages.json: 2569a6fe8c342e5e6bd5606dc182ea589c8b35753814ea78a7050fafa27fabfe
        B/raw.json: ee541d8bf608b93131234148681b3e79a6d2612e058fdf351102ba0abe36ec7d
        B/source-units.json: 60e88076c660bc1bd1ab8e8445ff387040f26795e4b9b3ff79c711a03f07a2d9
        B/full-source-units.json: 3766b61d5b37e79e90f50680ee78734d0903eccbb1199a43baac52ff521afc46
        B/meta.json: 3ee0e9835a2e5e4c0e17caaf92488706d733f0d3c3ae9a5ea9ffe83bc2c3813d
        B/table-images/TABLE-1-page-3-1.png: 8c24153377a49ccad7b45d180a5dd91b62da0f34c3fd82190ac5b0d0d147092e
        B/table-images/page-3.png: 2830f76151060403251a4b364eccfe6f6edde541dd856d30ab7f7ab359187250
        B/table-images/page-4.png: de08d5e27c381f62980c055356b489ea455a98dc34d2111ad4481ac5a20c61d5
        B/table-images/TABLE-3-page-4-2.png: dae3ddc166b8cf33a48562572d3c5174fa606103a944f5ea8a3c2aaea354edd6
        B/table-images/manifest.json: e5ba254cd47c4038c64643762ded970af2509bc9e03f492cb88cf4d9f2b5c5d8
        B/table-images/TABLE-2-page-4-1.png: bb30411ba11508d0a864176938c5bebe917c502331418c74a58bfe775126e93d
        B/clauses/window-03/raw.json: 8a558db6f88e8822fb2dfb6abd69511cd84d051fe9fc958b406605f8e66cb7ed
        B/clauses/window-03/prompt.txt: 10aa18139a040d39257369bcca8a88310fd3aafbbeafedd650777a06639c2d5a
        B/clauses/window-03/meta.json: b2440031e66ee9373874e5aa0697c86b57b64881765f43a8b5faba78ea983e33
        B/clauses/window-04/raw.json: afe02a68d3a21699497874eb911d00d54f705fcb1c6aab864daffe006ab5a071
        B/clauses/window-04/prompt.txt: da4c6f9a1a61e34e8941ba5baf5284c640d06054c03c9ba482e8dd9410ac53b1
        B/clauses/window-04/meta.json: 03e812b0348b41abfe16e420442c296a04436e2121685b5ac57a2f221d8ffb76
        B/clauses/window-05/raw.json: 7ff1d1363224d0271bc304d7758f080c61875a9ce5b38be36f9818e4c6909344
        B/clauses/window-05/prompt.txt: 95debe1cd4f49603d372a45063635fa81f6c5020fb5ca0e2c471630219eaada5
        B/clauses/window-05/meta.json: a290733d4c97840941d3d26364e54da06bc5b9a8a41c2cfbc37599559aa25e9b
        B/clauses/window-02/raw.json: b38516a52872c503861b7054e722db139287f2bdcca73e0eef9a0681319219a9
        B/clauses/window-02/prompt.txt: f233107c16edde04b8c664b210eac94d20c26beb065d9507a0a9e6138df17983
        B/clauses/window-02/meta.json: dc92037f199f8e064f6a89fa339dec7bd1dea691f5b8d588fc0142e9ef69043d
        B/clauses/window-01/raw.json: 7742f1c14d608802e4abd590125b41aac8ab4791263be7c54ce51050aea6a6f4
        B/clauses/window-01/prompt.txt: b77f4db4be064f062658f19f2784890b007170c15355a00f9a623c7b6527a824
        B/clauses/window-01/meta.json: 79d5b7e4865c21178cb668a02f1bf28206e07def7f31292b13916c4f96a6a0df
        B/tables/TABLE-1-page-3-1/raw.json: e23475e4d16414113f41d15505bbbf2aedbb1f4ee7cb8318647c26b2f19e700f
        B/tables/TABLE-1-page-3-1/prompt.txt: b384aec910f232ba0188e6f00d2ecc63b62c1eac495d1acf5f3fe0b2de9dbf6e
        B/tables/TABLE-1-page-3-1/meta.json: 2b7a83ecee6c8b04c21ae0ad8c57162ced1d4fb292180dd5d6365955e939d511
        B/tables/TABLE-3-page-4-3/raw.json: acfe26eba878e20954434c41180fcc301783877c1fbc191b6436dc77efbd0677
        B/tables/TABLE-3-page-4-3/prompt.txt: 855021c6c147f5715a86d9f5963b21943c3e390b9f6b4be15f60c401650d131a
        B/tables/TABLE-3-page-4-3/meta.json: 42047a6f24d514cdc5dfbd02fa644c93ebad0e4fefa1f268a84db352ce86b6d5
        B/tables/TABLE-2-page-4-2/raw.json: 64ce6b97c728aed717adc116fccc634c00ebd5d6f24462d9f489d804e129dafd
        B/tables/TABLE-2-page-4-2/prompt.txt: 1faf342daa204c5c1fc05df56b141ac24aaba6bf571afc7b82870c2d5b2657ca
        B/tables/TABLE-2-page-4-2/meta.json: c71246f5dc5ffec8ecb97a15936071145ef194275c8113538f2d15c92336bb35
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
      pdf_sha256: 2ff4924a20fb1db57ab84d972482c37ce1531fd4758fe92bafdc6f13d175a9f7
      source_review: _compare/relationships-2026-11-16/review-current/Sewell2025
      source_status_sha256: 94da2b62846f0f5cb091869d54c4cc2c57e3aa9858a759f26ab129b631878c25
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R003
    exposure:
      text: depressive symptoms within the first week
    outcome:
      text: depressive symptoms at 12 months
    analysis_label: Logistic regression of early and later depressive symptoms (first
      week vs 12 months)
    relation: association
    evidence_ids:
    - P3-S1-C10
    - P4-S3-C4
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
      pdf_sha256: 2ff4924a20fb1db57ab84d972482c37ce1531fd4758fe92bafdc6f13d175a9f7
      source_review: _compare/relationships-2026-11-16/review-current/Sewell2025
      source_status_sha256: 94da2b62846f0f5cb091869d54c4cc2c57e3aa9858a759f26ab129b631878c25
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P1-S2-C6
      - Accounting without a linked unit P1-S2-C8
      - Unaccounted source passage P1-S2-C8
      - Result passage disposed without unit P2-S4-C10
      - Result passage disposed without unit P2-S4-C11
      - Result passage disposed without unit P2-S4-C9
      - Result passage disposed without unit P3-S1-C3
      - Result passage disposed without unit P3-S1-C4
      - Result passage disposed without unit P3-S1-C5
      - Result passage disposed without unit P3-S1-C6
      - Result passage disposed without unit P3-S1-C7
      - Result passage disposed without unit P3-S1-C8
      - Result passage disposed without unit P3-S2-C2
      - Result passage disposed without unit P3-S2-C3
      - Result passage disposed without unit P3-S2-C4
      - Result passage disposed without unit P3-S2-C5
      - Accounting without a linked unit P3-S2-C8
      - Result passage disposed without unit P3-S3-C8
      - Result passage disposed without unit P4-S2-C3
      - Unaccounted source passage P3-S2-C8
      - Result passage disposed without unit P4-S2-C10
      unattached_null_or_qualifier_ids:
      - P3-S2-C3
      - P3-S2-C8
      - P4-S2-C8
      suppressed_nonrepresented_units: 7
      default_disposition_count_requires_completeness_check: 79
      unselected_timing_passages:
      - P2-S2-C3
      - P2-S2-C7
      - P5-S1-C1
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P3-S1-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P3-S1-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P3-S1-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      empty_frame_slots_require_confirmation:
      - imaging_provenance
      - imaging_timing
      - validation
      - personal_factors
      - tested_personal_effects
      - adjustment_roles
      unclassified_extraction_ids:
      - P2-S4-C12
      table_review_required:
      - TABLE-1-page-3-1
      - TABLE-2-page-4-2
      - TABLE-3-page-4-3
      unlinked_tables: []
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P3-S1
        - P4-S2
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 2ff4924a20fb1db57ab84d972482c37ce1531fd4758fe92bafdc6f13d175a9f7
      source_review: _compare/relationships-2026-11-16/review-current/Sewell2025
      source_status_sha256: 94da2b62846f0f5cb091869d54c4cc2c57e3aa9858a759f26ab129b631878c25
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the proportion of participants experiencing change in status,
        not a measured association or performance result.
    - source_id: P1-S2-C7
      disposition: represented
      result_indexes:
      - 0
      reason: States no association between time and frequency of depressive symptoms.
    - source_id: P1-S2-C8
      disposition: represented
      result_indexes:
      - 3
      reason: States 3-month symptoms increase likelihood of 12-month symptoms.
    - source_id: P2-S4-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Demographic data (previous history of stroke).
    - source_id: P2-S4-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Demographic data (pre-stroke disability).
    - source_id: P2-S4-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Clinical baseline data (NIHSS score).
    - source_id: P3-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Clinical baseline data (NIHSS IQR).
    - source_id: P3-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive MADRS scores at time points.
    - source_id: P3-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive prevalence of symptoms.
    - source_id: P3-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive prevalence of symptoms at specific time points.
    - source_id: P3-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive flow of participants.
    - source_id: P3-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive prevalence at 12 months.
    - source_id: P3-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive overlap of symptoms across time points.
    - source_id: P3-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive change in symptom status.
    - source_id: P3-S1-C9
      disposition: represented
      result_indexes:
      - 0
      reason: Reports no evidence of association between time post-stroke and presence
        of symptoms.
    - source_id: P3-S1-C10
      disposition: represented
      result_indexes:
      - 1
      - 2
      reason: Reports association between first week symptoms and symptoms at 3 and
        12 months.
    - source_id: P3-S1-C11
      disposition: represented
      result_indexes:
      - 3
      reason: Reports association between 3-month and 12-month symptoms.
    - source_id: P3-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion summary of findings.
    - source_id: P3-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive observation of symptom change.
    - source_id: P3-S2-C4
      disposition: repeated
      result_indexes:
      - 3
      reason: Restatement of 3-month to 12-month association.
    - source_id: P3-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive observation of symptom change.
    - source_id: P3-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive observation of symptom change.
    - source_id: P3-S3-C8
      disposition: repeated
      result_indexes:
      - 3
      reason: Restatement of 3-month to 12-month association.
    - source_id: P4-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of guidelines.
    - source_id: P4-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive count from Figure 1.
    - source_id: P4-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive count from Figure 1.
    - source_id: P4-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive count from Figure 1.
    - source_id: P5-S1-C8
      disposition: repeated
      result_indexes:
      - 3
      reason: Restatement of association between 3-month and 12-month symptoms.
    - source_id: P5-S2-C7
      disposition: repeated
      result_indexes:
      - 3
      reason: Conclusion restatement of 3-month to 12-month association.
    unresolved_coverage: []
    pending_source_ids:
    - P1-S2-C6
    - P2-S4-C9
    - P2-S4-C10
    - P2-S4-C11
    - P3-S1-C1
    - P3-S1-C2
    - P3-S1-C3
    - P3-S1-C4
    - P3-S1-C5
    - P3-S1-C6
    - P3-S1-C7
    - P3-S1-C8
    - P3-S2-C2
    - P3-S2-C3
    - P3-S2-C5
    - P3-S2-C8
    - P4-S2-C3
    - P4-S2-C8
    - P4-S2-C9
    - P4-S2-C10
    - P5-S1-C8
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-3-1
    - TABLE-2-page-4-2
    - TABLE-3-page-4-3
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P2-S4-C9
      recruited_sample:
      - P2-S2-C3
      - P2-S2-C6
      eligibility:
      - P2-S2-C7
      imaging_provenance: []
      imaging_timing: []
      outcome_timing:
      - P1-S1-C9
      - P2-S3-C2
      - P3-S1-C2
      outcome_definition:
      - P1-S1-C10
      - P2-S3-C5
      - P4-S2-C7
      validation: []
      analysis_restrictions:
      - P5-S1-C4
      dependent_variable_statement:
      - P2-S4-C3
      - P2-S4-C5
      limitations:
      - P5-S1-C1
      - P5-S1-C2
      - P5-S1-C4
      - P5-S1-C5
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles: []
      explicitly_not_adjusted:
      - P5-S1-C5
      descriptive_personal_factors:
      - P2-S4-C9
      - P3-S4-C1
    outcome_type: both_reported
    imaging_vs_outcome: not_stated
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P3-S1-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P3-S1-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P3-S1-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
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
      pdf_sha256: 2ff4924a20fb1db57ab84d972482c37ce1531fd4758fe92bafdc6f13d175a9f7
      review_sha256: 1c581c428dfa0df96071ecfb25e12385932d727caea3453b82f7b4038b6460b6
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
      - P3-S1-C10
      source_result: Logistic regression demonstrated that participants with depressive
        symptoms within the first week were somewhat more likely to have depressive
        symptoms at 12 months compared to those without such symptoms (OR 2.07, 95%
        CI [1.02, 4.18], p = 0.044).
      result_status: detected
      patient_measurement: non_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis correctly identifies the logistic regression
            model comparing depressive symptom status at the first week versus 12
            months, as described in P3-S1-C10 and P2-S4-C6.
          source_ids:
          - P3-S1-C10
          - P2-S4-C6
        direction:
          answer: fits
          reason: The source explicitly states that participants with early symptoms
            were 'more likely' to have symptoms at 12 months (OR 2.07), which aligns
            with the proposed direction of 'likely' and the claim of increased likelihood.
          source_ids:
          - P3-S1-C10
        construct:
          answer: fits
          reason: The exposure (early depressive symptoms) and outcome (late depressive
            symptoms) are correctly identified. The measurement is non-imaging (MADRS
            clinical assessment), not diffusion or lesion overlap, as the study uses
            a rating scale rather than neuroimaging metrics for the primary association.
          source_ids:
          - P1-S1-C9
          - P2-S3-C2
        qualifications:
          answer: fits
          reason: The proposed draft includes the critical qualification that MADRS
            scores were dichotomized (≥7 vs <7), which is a material methodological
            detail affecting the interpretation of the binary outcome.
          source_ids:
          - P1-S1-C10
          - P2-S3-C5
        missing_material_caveat:
          answer: fits
          reason: The draft includes relevant limitations such as the exclusion of
            participants without complete data and the lack of adjustment for prior
            depression history, which are material caveats found in the source limitations
            section.
          source_ids:
          - P5-S1-C4
          - P5-S1-C5
      optional_pending:
      - Specific odds ratio and confidence interval values
      - P-value exactness
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Specific odds ratio and confidence interval values
    - P-value exactness
    normalizations: []
    analysis_identity:
      id: R003
      exposure:
        text: depressive symptoms within the first week
      outcome:
        text: depressive symptoms at 12 months
      analysis_label: Logistic regression of early and later depressive symptoms (first
        week vs 12 months)
      relation: association
      evidence_ids:
      - P3-S1-C10
      - P4-S3-C4
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
        pdf_sha256: 2ff4924a20fb1db57ab84d972482c37ce1531fd4758fe92bafdc6f13d175a9f7
        source_review: _compare/relationships-2026-11-16/review-current/Sewell2025
        source_status_sha256: 94da2b62846f0f5cb091869d54c4cc2c57e3aa9858a759f26ab129b631878c25
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P2-S2-C7:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 2ff4924a20fb1db57ab84d972482c37ce1531fd4758fe92bafdc6f13d175a9f7
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: e16863a4bae015bdad85378c10e995cf2848f2f388d2de8b54473138e0b0ea7e
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S2-C7
          page: 2
          text_layer_sha256: e16863a4bae015bdad85378c10e995cf2848f2f388d2de8b54473138e0b0ea7e
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: "Eligibility criteria required partic­\nipants to be diagnosed\
          \ with acute ischaemic stroke, aged 18 years or \nolder, English-speaking,\
          \ and with no significant disability prior to their \nstroke as determined\
          \ by a modified Rankin Scale (mRS) score ≤2.19\nAdditional inclusion criteria\
          \ for thrombolysis were required for partic­\nipants recruited through the\
          \ START EXTEND arm.18\nMeasures\nData collected on admission included: age,\
          \ sex, prior history of stroke \nand premorbid disability."
        anchor_text: "Eligibility criteria required partic­\nipants to be diagnosed\
          \ with acute ischaemic stroke, aged 18 years or \nolder, English-speaking,\
          \ and with no significant disability prior to their \nstroke as determined\
          \ by a modified Rankin Scale (mRS) score ≤2.19\nAdditional inclusion criteria\
          \ for thrombolysis were required for partic­\nipants recruited through the\
          \ START EXTEND arm.18\nMeasures\nData collected on admission included: age,\
          \ sex, prior history of stroke \nand premorbid disability."
        excluded_fragments: []
        image_sha256: 43552f13d8a97698b5f10726dbe2336e7cabc686ee02654ddd37cb3a2dab8adf
      P5-S1-C1:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 2ff4924a20fb1db57ab84d972482c37ce1531fd4758fe92bafdc6f13d175a9f7
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 3949ce01672ddcd1a20a75162d8932ede8f0b04237aa0ff2a5f744eb9be409af
          exclusions_sha256: 898a54307108dcbd08def3e8c3c1f84d6c7a2c12d17f1a33698d654323c9b152
          source_id: P5-S1-C1
          page: 5
          text_layer_sha256: 1e1593b75f43cad02a6f8c72a7dd52233bf030eedc79311bf62f9fbbe5d98cda
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: "\nJournal of Stroke and Cerebrovascular Diseases 34 (2025)\
          \ 108197\n5\nStudy limitations\nOur sample had a lower mean age at stroke\
          \ and lower proportion of \nfemales compared with national figures published\
          \ by the Australian \nStroke Clinical Registry (mean age = 73 years, SD\
          \ = 13; females 45%).51\nAll our participants had ischaemic stroke, consistent\
          \ with the inclusion \ncriteria, whereas only 70% of registry patients had\
          \ ischaemic stroke.51\nDespite efforts to support the inclusion of patients\
          \ with severe neuro­\nlogical impairments, the majority of participants\
          \ in this cohort had an \nNIHSS score ≤6 at day 3 to 7, indicating mild\
          \ neurological deficits.52\nNext, the MADRS yields scores which produce\
          \ a continuous variable; \nhowever, in our study the scores were dichotomised."
        anchor_text: "Study limitations\nOur sample had a lower mean age at stroke\
          \ and lower proportion of \nfemales compared with national figures published\
          \ by the Australian \nStroke Clinical Registry (mean age = 73 years, SD\
          \ = 13; females 45%).51\nAll our participants had ischaemic stroke, consistent\
          \ with the inclusion \ncriteria, whereas only 70% of registry patients had\
          \ ischaemic stroke.51\nDespite efforts to support the inclusion of patients\
          \ with severe neuro­\nlogical impairments, the majority of participants\
          \ in this cohort had an \nNIHSS score ≤6 at day 3 to 7, indicating mild\
          \ neurological deficits.52\nNext, the MADRS yields scores which produce\
          \ a continuous variable; \nhowever, in our study the scores were dichotomised."
        excluded_fragments:
        - where: leading
          text: Journal of Stroke and Cerebrovascular Diseases 34 (2025) 108197
          furniture_line: Journal of Stroke and Cerebrovascular Diseases 34 (2025)
            108197
          bbox:
          - 378.2
          - 33.7
          - 558.3
          - 44.1
          rule: repeated margin line
        - where: leading
          text: '5'
          furniture_line: '5'
          bbox:
          - 296.2
          - 754.5
          - 299.8
          - 764.9
          rule: repeated margin line
        image_sha256: ae5382f5e123a9748212f3e1578ddbc3bee5a8e1b1b20e9332e2eda38239dda3
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 3
  quote: "Likelihood of experiencing depressive symptoms at later time points based\
    \ \non depressive symptom status at earlier time points\nLogistic regression models\
    \ demonstrated that participants with \ndepressive symptoms within the first week\
    \ were somewhat more likely \nto have depressive symptoms, compared to participants\
    \ without such \nsymptoms within the first week, at both 3 months (OR 2.78, 95%\
    \ CI \n[1.39, 5.59]; p = 0.004) and 12 months (OR 2.07, 95% CI [1.02, 4.18]; p\
    \ \n= 0.044)."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-25'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
