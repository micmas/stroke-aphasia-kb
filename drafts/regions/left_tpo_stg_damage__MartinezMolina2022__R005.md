---
id: left_tpo_stg_damage
name: left TPO-STG damage
kind: network
findings:
- id: f1
  target_audit:
    status: behaviour_label_present
    category: behaviour_or_language_construct
    original_target: spontaneous_singing
    reason: Label names a behaviour or language construct; its exact operational definition and measurement
      still need source review.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  outcome_measurement:
    status: needs_source_review
    instruments: []
    note: Outcome instrument/task is not yet verified for this finding. Do not infer it from the predictor
      or a paper-wide test list.
  target: spontaneous_singing
  target_kind: impairment
  claim: greater damage in the left TPO-STG was the only predictor of poor spontaneous
    singing
  direction: likely
  relationship: correlational
  method: LSM
  sample:
    n: 43
    population: chronic stroke patients with aphasia
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
  - lack of a standardized protocol for evaluating singing abilities in post-stroke
    aphasia
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: percentage of damage to the left temporal pole-superior
    temporal gyrus (TPO-STG) region. identified via stepwise regression; adjusted
    for age, sex, handedness, education, years of choir singing, Montreal Battery
    of Evaluation of Amusia, BDAE severity rating, time since stroke, lesion size,
    lesion laterality, and damage to 22 other grey matter regions in the vocal motor
    production network. Additional metadata has not been transcribed; review the pending-field
    flags before approval. PDF image reading (P6-S1-C2, two-model agreement, human
    verification pending): Only patients with complete behavioural measurements were
    included in the analyses (spontaneous speech, N= 45; spontaneous singing, N=43;
    cued repetition, N= 44) (see Supplementary Methods for details) Original text-layer
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
    - not_transcribed:sample.time_post_onset
    - proposed_concept:spontaneous_singing
  citation: '@MartinezMolina2022'
  source_passages:
  - section: Original source P7-S1-C2
    page: 7
    quote: 'The stepwise regression showed that

      greater damage in the left TPO-STG was the only predictor

      of poor spontaneous singing [R2 = 0.233, β = −49.36,

      F(1,39) = 11.86, P , 0.001].'
    supports: claim
  - section: Original source P6-S2-C12
    page: 6
    quote: 'Finally, a stepwise regression was performed with WPM

      in spontaneous singing as the dependent variable to deter-

      mine the most important predictors for spontaneous singing

      in aphasia.'
    supports: method
  - section: Original source P6-S2-C13
    page: 6
    quote: 'Age, sex, handedness, education, years of choir

      singing, Montreal Battery of Evaluation of Amusia, BDAE

      severity rating, time since stroke, lesion size and lesion lat-

      erality as well as the percentage of damage in each patient

      to 23 GM regions (Supplementary Table 2) involved in vocal

      motor production (singing and speech) were included as in-

      dependent variables.'
    supports: method
  - section: Original source P3-S3-C2
    page: 3
    quote: 'Inclusion criteria were time since stroke

      ≥6 months; at least minor non-ﬂuent aphasia due to stroke

      assessed

      by

      Boston

      Diagnostic

      Aphasia

      Examination

      (BDAE) Aphasia Severity Rating (severity score: 1–5; score

      ≤4); age ≥18 years; Finnish-speaking; no hearing deﬁcit

      Table 1 Summary of demographic, musical, clinical,

      WAB-R indices and task performance data for all

      chronic stroke patients with aphasia (N = 45)

      Demographic information

      Age (years)

      64.4 (10.2)

      Sex (female/male)

      25/20

      Handedness (right/left/both)

      39/5/1

      Education (years)

      14.3 (4.1)

      Musical background

      Choir singing (years)

      3.6 (9.4)

      MBEA (rhythm and scale)

      22.7 (4.2)

      Clinical information

      Lesion size (cm3)

      95.8 (87.6)

      Lesion laterality (left/bilateral)

      34/11

      Time since stroke (years)

      9.0 (7.7)

      BDAE severity score

      3.0 (1.4)

      WAB indices

      Spontaneous speech (max. score 20)

      12.9 (7.1)

      Repetition (max. score 10)

      6.5 (3.5)

      Naming (max. score 10)

      6.2 (3.6)

      Spontaneous speech (CPM)

      Question (Sunday) + Picture description

      (argument and picnic tasks)

      30.8 (25.5)

      Spontaneous singing (WPM)

      Spontaneous singing

      42.0 (28.8)

      Cued repetition (WPM)

      Spoken phrases

      46.0 (27.1)

      Sung phrases

      23.9 (14.5)

      Mean (SD) data are presented unless otherwise indicated.'
    supports: sample
  - section: Original source P6-S1-C2
    page: 6
    quote: 'Only patients with complete behavioural measurements

      were included in the analyses (spontaneous speech, N =

      45; spontaneous singing, N = 43; cued repetition, N = 44)

      (see Supplementary Methods for details).'
    supports: sample
  - section: Original source P5-S1-C7
    page: 5
    quote: 'Given the lack of a standardized protocol for evalu-

      ating singing abilities in post-stroke aphasia, this song was

      selected due to its great popularity and simple melodic and

      rhythmic structure to maximize word retrieval even in the

      patients with more severe aphasia, thus making it more com-

      parable with spontaneous speech.'
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-24'
relationship_review:
  paper: MartinezMolina2022
  proposal_id: R005
  review_status_sha256: 2c3fe5dde1c201f9ba883f870641ec86a0c09a2f8e534dcf3a1ca866711a7378
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 3c9ebfc511946defdf73d257b7b19aee74b41c11c7326c25cc5632f322709398
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 3c9ebfc511946defdf73d257b7b19aee74b41c11c7326c25cc5632f322709398
        A/passages.json: 4abe94f48478f829e9763b763e3fad9cf70f5f89cbdc1a2125e53b773af9913d
        A/raw.json: 27c18edefb9055099f136612e812286446d322da7c99c95e7d551b94558a24c4
        A/source-units.json: f299b4567fd2d4fd62b8002636ba0cb69a0db349875e00fd3e6e74e2e91cba10
        A/full-source-units.json: 7ed1005f0c042f8107e6b4c46722af9c666cae1a3f922c660ff42867181b3688
        A/meta.json: 3298986572ddd28280b0074fdea147e2cf5a4fddb04c55106e3c0e674090ed16
        A/table-images/TABLE-1-page-3-1.png: d9731f71aa3464ee7ea88a87c3565663d7627b6b125bad7c5b5436525bd2ebbd
        A/table-images/page-3.png: 087658a0f3626ab516e85e7bbe664a5e33c73ab05dd7960b90e81bcc4bfa1102
        A/table-images/manifest.json: 82e759e7daf57749fc8a049a0759816507b64aaf717228b33026d03ebbbed0e8
        A/clauses/window-03/raw.json: acd00be8169e99bfee8a977e1ba66b326615074cdebb49a4d2a784ec2453ad2a
        A/clauses/window-03/prompt.txt: 0123722dbdfa40a346b6afddb1d49ae5cd47d331eaf201ba6b1d650f0c85dc76
        A/clauses/window-03/meta.json: 3608b2343bbc78bac5d25d3c23018bedb8b265ffd74248814f8d3a4a2d629a1a
        A/clauses/window-04/raw.json: 4e8519c29bcf5a502448ece5068bf1aa9f552dce585e8d3de041da213e429156
        A/clauses/window-04/prompt.txt: ec36055ca06cd94b64b6ece99fdfea9a732d1e368b38bab9d4d78fb0f4f0fbf1
        A/clauses/window-04/meta.json: 3e34e6c5c865a5834a78c3095a7f58b97080b720131739798909097745639a56
        A/clauses/window-05/raw.json: 01dd58903994baf5f580ee83f54aaad7dd528699e72246a915c1758fd0eed1b8
        A/clauses/window-05/prompt.txt: 355df906e5900139c3d942fd2d37733ffa4aeba63d7dd0340c6b956d72b37e3b
        A/clauses/window-05/meta.json: bfc1de1e387c804a84c46ca3da2e637bebcc9b3cfb576eb7812a390f8ae954e3
        A/clauses/window-02/raw.json: 4a5149f5c8be564089d2ae0dff17c54c41bd3753439eeedeec884a796084b083
        A/clauses/window-02/prompt.txt: beb6274154196706e765eb870482053e0c2e4f9258c1859dca8f23c9990e7ebb
        A/clauses/window-02/meta.json: ee245b0663820420b730fdfdc3155627d4228e7bee2dac93d55e524174256d7f
        A/clauses/window-01/raw.json: 135318ae2975acd4e23b2983415d0787043a967719665d0ea87f384247ca5ba0
        A/clauses/window-01/prompt.txt: 469d6be1f8970c0aafbab84d3f867728b4cdef08b7b816b071d800e7e0a22058
        A/clauses/window-01/meta.json: f03fbd0820c8be925c837a71675fb1249c9e2c0124b1860dcb9c663c1134aa63
        A/tables/TABLE-1-page-3-1/raw.json: 07eed290d34f52637010f4866234de3c1b62b754e4e47290da695aa317acd985
        A/tables/TABLE-1-page-3-1/prompt.txt: 548ee26be9bcbb59d5b5e97423002e0b027d206031ecce62e63feb21b0fa88d0
        A/tables/TABLE-1-page-3-1/meta.json: d19808be8d4bd887f846bd3f32161ae89ebeaeeeda2697c52931ec4afe3952b3
        B/passages.json: 4abe94f48478f829e9763b763e3fad9cf70f5f89cbdc1a2125e53b773af9913d
        B/raw.json: dff99958df1a2f393c11e95ae1cc29b0f5fb90ac6a88bd858a99602fddc3ce0a
        B/source-units.json: f299b4567fd2d4fd62b8002636ba0cb69a0db349875e00fd3e6e74e2e91cba10
        B/full-source-units.json: 7ed1005f0c042f8107e6b4c46722af9c666cae1a3f922c660ff42867181b3688
        B/meta.json: f8aeca6931cb77895fedcc0d349d4a27634054f846b1b5e92f1b79b32330fbf3
        B/table-images/TABLE-1-page-3-1.png: d9731f71aa3464ee7ea88a87c3565663d7627b6b125bad7c5b5436525bd2ebbd
        B/table-images/page-3.png: 087658a0f3626ab516e85e7bbe664a5e33c73ab05dd7960b90e81bcc4bfa1102
        B/table-images/manifest.json: 92b68eecd3c49c7d892e47346a71797a8ca78379dfe4b849a54edb98f781a060
        B/clauses/window-03/raw.json: 287a2e49753d02d420ca6f37075aca7fe18c5f434ea3016b7a3cab29b7a3ab41
        B/clauses/window-03/prompt.txt: 0123722dbdfa40a346b6afddb1d49ae5cd47d331eaf201ba6b1d650f0c85dc76
        B/clauses/window-03/meta.json: aa823b06d5e9ad8ca6f4c39125e20e7420f2cfeadaa0b19e0ae10e73b0e0a5e0
        B/clauses/window-04/raw.json: 54e9d1bcfa1334c30c0948c7bfd0252f7e050bbb06422d68e6eb5b3a5005853a
        B/clauses/window-04/prompt.txt: ec36055ca06cd94b64b6ece99fdfea9a732d1e368b38bab9d4d78fb0f4f0fbf1
        B/clauses/window-04/meta.json: 8fbe6db841b43fb3bb8a07d8db14db1aa0e8f72a54ef8d45dbff432a85efcc28
        B/clauses/window-05/raw.json: e262f550d6e66cba8dc8a85de5c3eaaa39438a6238c8447d06bb6ab4aebe2636
        B/clauses/window-05/prompt.txt: 355df906e5900139c3d942fd2d37733ffa4aeba63d7dd0340c6b956d72b37e3b
        B/clauses/window-05/meta.json: fa5d158c8d05023278a9f1133bd110e794cba7651629b84be2104d0ef2bb81bf
        B/clauses/window-02/raw.json: 734f12855f149e229a7cb230a1f569a7389b503b90fb600ab32ecd71fa3699fa
        B/clauses/window-02/prompt.txt: beb6274154196706e765eb870482053e0c2e4f9258c1859dca8f23c9990e7ebb
        B/clauses/window-02/meta.json: db89925082bdcd38c47e4d3d519dc00480537dc0387e1e2d93cae01313cc2168
        B/clauses/window-01/raw.json: ff0c317d767780923d4f917c9e919a1e0b089b8216038f919178bf0e4f88f5f3
        B/clauses/window-01/prompt.txt: 469d6be1f8970c0aafbab84d3f867728b4cdef08b7b816b071d800e7e0a22058
        B/clauses/window-01/meta.json: 8568568c2e229ec0aac5e0dccc8a43604f8b3a3789f5f29cffed1587b1cd89f5
        B/tables/TABLE-1-page-3-1/raw.json: bf71f9923f556000c33a60a66b2aebd7cbe01b28019e03f3d349b307cd300b49
        B/tables/TABLE-1-page-3-1/prompt.txt: 548ee26be9bcbb59d5b5e97423002e0b027d206031ecce62e63feb21b0fa88d0
        B/tables/TABLE-1-page-3-1/meta.json: 1fd5542cab23e123190947b4dc235bbc5da30b673abdfb4a8c3083b081df7661
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
      pdf_sha256: 3c9ebfc511946defdf73d257b7b19aee74b41c11c7326c25cc5632f322709398
      source_review: _compare/relationships-2026-11-16/review-current/MartinezMolina2022
      source_status_sha256: 2cf59670d387042dac2a4af06397911c9764573761bc1c9a8f9f5e4aeecc739c
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R005
    exposure:
      text: greater damage in the left TPO-STG
    outcome:
      text: poor spontaneous singing
    analysis_label: stepwise regression
    relation: association
    evidence_ids:
    - P7-S1-C2
    qualifier_ids:
    - P6-S2-C12
    - P6-S2-C13
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 3c9ebfc511946defdf73d257b7b19aee74b41c11c7326c25cc5632f322709398
      source_review: _compare/relationships-2026-11-16/review-current/MartinezMolina2022
      source_status_sha256: 2cf59670d387042dac2a4af06397911c9764573761bc1c9a8f9f5e4aeecc739c
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Accounting without a linked unit P1-S1-C6
      - Accounting without a linked unit P1-S1-C7
      - Accounting without a linked unit P1-S1-C8
      - Accounting without a linked unit P1-S1-C9
      - Unaccounted source passage P1-S1-C6
      - Unaccounted source passage P1-S1-C8
      - Unaccounted source passage P1-S1-C7
      - Unaccounted source passage P1-S1-C9
      - Result passage disposed without unit P4-S1-C7
      - Accounting without a linked unit P4-S1-C8
      - Unaccounted source passage P4-S1-C8
      - Result passage disposed without unit P7-S2-C2
      - Result passage disposed without unit P8-S1-C3
      - Result passage disposed without unit P8-S1-C7
      - Accounting without a linked unit P8-S2-C5
      - Accounting without a linked unit P8-S3-C2
      - Unaccounted source passage P8-S3-C2
      - Unaccounted source passage P8-S2-C5
      unattached_null_or_qualifier_ids: []
      suppressed_nonrepresented_units: 5
      default_disposition_count_requires_completeness_check: 99
      unselected_timing_passages:
      - P3-S2-C7
      - P3-S3-C2
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P3-S2-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S2-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S2-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S2-C12
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P3-S2-C6
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: tested_personal_effects
        source_id: P3-S2-C3
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P6-S2-C13
        reason: No current-result classification; a covariate description is not an
          individual test
      empty_frame_slots_require_confirmation:
      - validation
      - analysis_restrictions
      - personal_factors
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-3-1
      unlinked_tables: []
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P4-S1
        - P5-S1
        - P6-S3
        - P7-S1
        - P7-S2
        - P8-S1
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 3c9ebfc511946defdf73d257b7b19aee74b41c11c7326c25cc5632f322709398
      source_review: _compare/relationships-2026-11-16/review-current/MartinezMolina2022
      source_status_sha256: 2cf59670d387042dac2a4af06397911c9764573761bc1c9a8f9f5e4aeecc739c
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C6
      disposition: repeated
      result_indexes:
      - 0
      - 2
      reason: Restatement of SVR-LSM results for speech and repetition.
    - source_id: P1-S1-C7
      disposition: repeated
      result_indexes:
      - 1
      reason: Restatement of SVR-LSM results for spontaneous singing.
    - source_id: P1-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: General summary statement of VBM and SVR-LSM findings.
    - source_id: P1-S1-C9
      disposition: repeated
      result_indexes:
      - 10
      reason: Restatement of VBM results for dysfluent singers.
    - source_id: P4-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive overlap map information.
    - source_id: P4-S1-C8
      disposition: repeated
      result_indexes:
      - 0
      - 1
      - 2
      - 3
      reason: Figure legend describing SVR-LSM results.
    - source_id: P6-S3-C2
      disposition: represented
      result_indexes:
      - 0
      reason: Primary result for spontaneous speech SVR-LSM.
    - source_id: P6-S3-C3
      disposition: represented
      result_indexes:
      - 1
      reason: Primary result for spontaneous singing SVR-LSM.
    - source_id: P6-S3-C4
      disposition: represented
      result_indexes:
      - 2
      reason: Primary result for cued repetition SVR-LSM.
    - source_id: P6-S3-C5
      disposition: represented
      result_indexes:
      - 3
      reason: Primary result for singing repetition SVR-LSM.
    - source_id: P7-S1-C2
      disposition: represented
      result_indexes:
      - 4
      reason: Primary result for stepwise regression.
    - source_id: P7-S1-C3
      disposition: represented
      result_indexes:
      - 5
      reason: Primary result for spontaneous speech VBM.
    - source_id: P7-S1-C4
      disposition: represented
      result_indexes:
      - 6
      reason: Primary result for spontaneous singing VBM.
    - source_id: P7-S1-C5
      disposition: represented
      result_indexes:
      - 7
      - 8
      reason: Primary result for cued repetition VBM.
    - source_id: P7-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive statement regarding lack of differences in demographics/clinical
        data.
    - source_id: P7-S1-C7
      disposition: represented
      result_indexes:
      - 10
      reason: Primary result for VBM in dysfluent singers.
    - source_id: P7-S1-C8
      disposition: represented
      result_indexes:
      - 11
      reason: Primary null result for VBM in fluent singers/controls.
    - source_id: P7-S1-C10
      disposition: represented
      result_indexes:
      - 12
      reason: Primary result for lesion load comparison.
    - source_id: P7-S1-C12
      disposition: repeated
      result_indexes:
      - 0
      - 1
      reason: Discussion restatement of SVR-LSM results.
    - source_id: P7-S1-C13
      disposition: repeated
      result_indexes:
      - 4
      reason: Discussion restatement of stepwise regression.
    - source_id: P7-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: General summary statement of VBM results.
    - source_id: P7-S2-C3
      disposition: repeated
      result_indexes:
      - 10
      - 12
      reason: Discussion restatement of VBM and lesion load results.
    - source_id: P7-S2-C5
      disposition: repeated
      result_indexes:
      - 0
      - 1
      reason: Discussion restatement of SVR-LSM results.
    - source_id: P8-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: General discussion of overlap in lesion patterns.
    - source_id: P8-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Qualitative comparison of lesion pattern sizes.
    - source_id: P8-S1-C5
      disposition: repeated
      result_indexes:
      - 3
      reason: Discussion restatement of singing repetition result.
    - source_id: P8-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Qualitative description of VBM cluster locations.
    - source_id: P8-S2-C3
      disposition: repeated
      result_indexes:
      - 10
      reason: Discussion restatement of VBM in dysfluent singers.
    - source_id: P8-S2-C5
      disposition: repeated
      result_indexes:
      - 4
      reason: Discussion restatement of stepwise regression.
    - source_id: P8-S3-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement on laterality of VBM results.
    unresolved_coverage:
    - source_id: P7-S1-C10
      disposition: unresolved
      reason: Unknown result index; not accepted as coverage
    - source_id: P7-S2-C3
      disposition: unresolved
      reason: Unknown result index; not accepted as coverage
    pending_source_ids:
    - P1-S1-C6
    - P1-S1-C7
    - P1-S1-C8
    - P1-S1-C9
    - P4-S1-C7
    - P4-S1-C8
    - P7-S1-C6
    - P7-S1-C12
    - P7-S1-C13
    - P7-S2-C2
    - P7-S2-C3
    - P7-S2-C5
    - P8-S1-C3
    - P8-S1-C4
    - P8-S1-C5
    - P8-S1-C7
    - P8-S2-C3
    - P8-S2-C5
    - P8-S3-C2
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-3-1
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P3-S3-C2
      - P5-S1-C3
      - P6-S1-C2
      recruited_sample:
      - P3-S3-C2
      - P5-S1-C3
      eligibility:
      - P3-S3-C2
      - P4-S1-C1
      - P4-S1-C2
      imaging_provenance:
      - P6-S1-C3
      imaging_timing:
      - P3-S1-C3
      outcome_timing:
      - P3-S2-C2
      outcome_definition:
      - P3-S2-C2
      - P5-S1-C6
      - P5-S1-C9
      - P6-S1-C1
      validation: []
      analysis_restrictions: []
      dependent_variable_statement:
      - P3-S2-C2
      - P3-S2-C3
      - P3-S2-C4
      - P3-S2-C7
      limitations:
      - P8-S1-C1
      - P8-S1-C4
      - P8-S3-C4
      personal_factors: []
      tested_personal_effects:
      - P7-S1-C2
      adjustment_roles:
      - P4-S1-C9
      - P5-S2-C3
      - P6-S2-C4
      - P6-S2-C10
      - P6-S2-C13
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P3-S3-C2
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P3-S2-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S2-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S2-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S2-C12
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P3-S2-C6
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: tested_personal_effects
      source_id: P3-S2-C3
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P6-S2-C13
      reason: No current-result classification; a covariate description is not an
        individual test
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
      pdf_sha256: 3c9ebfc511946defdf73d257b7b19aee74b41c11c7326c25cc5632f322709398
      review_sha256: 2c3fe5dde1c201f9ba883f870641ec86a0c09a2f8e534dcf3a1ca866711a7378
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
      - P7-S1-C2
      source_result: The stepwise regression analysis identified greater damage in
        the left TPO-STG as the sole predictor of poor spontaneous singing (measured
        in WPM) in chronic stroke patients with aphasia, after adjusting for clinical,
        demographic, and lesion load covariates.
      result_status: detected
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The source P7-S1-C2 explicitly describes a stepwise regression where
            'greater damage in the left TPO-STG was the only predictor of poor spontaneous
            singing'. This matches the selected analysis label and evidence.
          source_ids:
          - P7-S1-C2
          - P6-S2-C12
        direction:
          answer: fits
          reason: The source states 'greater damage... was the only predictor of poor
            spontaneous singing', which aligns with the proposed claim direction of
            'greater damage... associated with poor spontaneous singing'.
          source_ids:
          - P7-S1-C2
        construct:
          answer: fits
          reason: The exposure is 'damage in the left TPO-STG' (lesion overlap with
            template region) and the outcome is 'spontaneous singing' (WPM). The method
            is stepwise regression. The patient measurement is correctly identified
            as template_lesion_overlap (percentage of damage to a defined region),
            not patient_diffusion.
          source_ids:
          - P7-S1-C2
          - P6-S2-C13
        qualifications:
          answer: fits
          reason: The proposed draft includes the necessary qualifications that the
            result was identified via stepwise regression and adjusted for specific
            covariates (age, sex, etc., and damage to other GM regions). P6-S2-C13
            lists these covariates, and P7-S1-C2 confirms the result is the 'only
            predictor' in this model.
          source_ids:
          - P6-S2-C13
          - P7-S1-C2
        missing_material_caveat:
          answer: fits
          reason: The draft includes the limitation regarding the lack of a standardized
            protocol for evaluating singing abilities (P5-S1-C7). No other material
            caveats that change the interpretation of this specific regression result
            appear to be missing from the provided source window.
          source_ids:
          - P5-S1-C7
      optional_pending:
      - sample.time_post_onset
      - exact_covariate_list_verification
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
    - sample.time_post_onset
    - exact_covariate_list_verification
    normalizations:
    - field: bucket
      original: predictors
      action: route_from_kind
      value: regions
    - field: sample.time_post_onset
      original: chronic stage (time since stroke >= 6 months)
      action: not_transcribed
      reason: 'Numbers not grounded in usable selected source readings: 6'
    analysis_identity:
      id: R005
      exposure:
        text: greater damage in the left TPO-STG
      outcome:
        text: poor spontaneous singing
      analysis_label: stepwise regression
      relation: association
      evidence_ids:
      - P7-S1-C2
      qualifier_ids:
      - P6-S2-C12
      - P6-S2-C13
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 3c9ebfc511946defdf73d257b7b19aee74b41c11c7326c25cc5632f322709398
        source_review: _compare/relationships-2026-11-16/review-current/MartinezMolina2022
        source_status_sha256: 2cf59670d387042dac2a4af06397911c9764573761bc1c9a8f9f5e4aeecc739c
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P3-S3-C2:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 3c9ebfc511946defdf73d257b7b19aee74b41c11c7326c25cc5632f322709398
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 09901ea98390627b962a2407eabd347299315dd2216d86b7a7d855e6836862a2
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S3-C2
          page: 3
          text_layer_sha256: 09901ea98390627b962a2407eabd347299315dd2216d86b7a7d855e6836862a2
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: 'Inclusion criteria were time since stroke

          ≥6 months; at least minor non-ﬂuent aphasia due to stroke

          assessed

          by

          Boston

          Diagnostic

          Aphasia

          Examination

          (BDAE) Aphasia Severity Rating (severity score: 1–5; score

          ≤4); age ≥18 years; Finnish-speaking; no hearing deﬁcit

          Table 1 Summary of demographic, musical, clinical,

          WAB-R indices and task performance data for all

          chronic stroke patients with aphasia (N = 45)

          Demographic information

          Age (years)

          64.4 (10.2)

          Sex (female/male)

          25/20

          Handedness (right/left/both)

          39/5/1

          Education (years)

          14.3 (4.1)

          Musical background

          Choir singing (years)

          3.6 (9.4)

          MBEA (rhythm and scale)

          22.7 (4.2)

          Clinical information

          Lesion size (cm3)

          95.8 (87.6)

          Lesion laterality (left/bilateral)

          34/11

          Time since stroke (years)

          9.0 (7.7)

          BDAE severity score

          3.0 (1.4)

          WAB indices

          Spontaneous speech (max. score 20)

          12.9 (7.1)

          Repetition (max. score 10)

          6.5 (3.5)

          Naming (max. score 10)

          6.2 (3.6)

          Spontaneous speech (CPM)

          Question (Sunday) + Picture description

          (argument and picnic tasks)

          30.8 (25.5)

          Spontaneous singing (WPM)

          Spontaneous singing

          42.0 (28.8)

          Cued repetition (WPM)

          Spoken phrases

          46.0 (27.1)

          Sung phrases

          23.9 (14.5)

          Mean (SD) data are presented unless otherwise indicated.'
        anchor_text: 'Inclusion criteria were time since stroke

          ≥6 months; at least minor non-ﬂuent aphasia due to stroke

          assessed

          by

          Boston

          Diagnostic

          Aphasia

          Examination

          (BDAE) Aphasia Severity Rating (severity score: 1–5; score

          ≤4); age ≥18 years; Finnish-speaking; no hearing deﬁcit

          Table 1 Summary of demographic, musical, clinical,

          WAB-R indices and task performance data for all

          chronic stroke patients with aphasia (N = 45)

          Demographic information

          Age (years)

          64.4 (10.2)

          Sex (female/male)

          25/20

          Handedness (right/left/both)

          39/5/1

          Education (years)

          14.3 (4.1)

          Musical background

          Choir singing (years)

          3.6 (9.4)

          MBEA (rhythm and scale)

          22.7 (4.2)

          Clinical information

          Lesion size (cm3)

          95.8 (87.6)

          Lesion laterality (left/bilateral)

          34/11

          Time since stroke (years)

          9.0 (7.7)

          BDAE severity score

          3.0 (1.4)

          WAB indices

          Spontaneous speech (max. score 20)

          12.9 (7.1)

          Repetition (max. score 10)

          6.5 (3.5)

          Naming (max. score 10)

          6.2 (3.6)

          Spontaneous speech (CPM)

          Question (Sunday) + Picture description

          (argument and picnic tasks)

          30.8 (25.5)

          Spontaneous singing (WPM)

          Spontaneous singing

          42.0 (28.8)

          Cued repetition (WPM)

          Spoken phrases

          46.0 (27.1)

          Sung phrases

          23.9 (14.5)

          Mean (SD) data are presented unless otherwise indicated.'
        excluded_fragments: []
        image_sha256: 1b5d13be9f539a6629eb0136e9bd015d59aefe4d26014e29c8bfc87eb69a921a
      P6-S1-C2:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 3c9ebfc511946defdf73d257b7b19aee74b41c11c7326c25cc5632f322709398
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: f7b76e585f06045508b9a7d5bb302d4036a3d50447ce842224870f4f9a732b49
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P6-S1-C2
          page: 6
          text_layer_sha256: f7b76e585f06045508b9a7d5bb302d4036a3d50447ce842224870f4f9a732b49
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Only patients with complete behavioural measurements

          were included in the analyses (spontaneous speech, N =

          45; spontaneous singing, N = 43; cued repetition, N = 44)

          (see Supplementary Methods for details).'
        anchor_text: 'Only patients with complete behavioural measurements

          were included in the analyses (spontaneous speech, N =

          45; spontaneous singing, N = 43; cued repetition, N = 44)

          (see Supplementary Methods for details).'
        excluded_fragments: []
        image_sha256: 5c61cceac94e47e861552d0b170098e30b029793ddff03203864fa331cab5d4b
        transcription: Only patients with complete behavioural measurements were included
          in the analyses (spontaneous speech, N= 45; spontaneous singing, N=43; cued
          repetition, N= 44) (see Supplementary Methods for details)
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 7
  quote: 'The stepwise regression showed that

    greater damage in the left TPO-STG was the only predictor

    of poor spontaneous singing [R2 = 0.233, β = −49.36,

    F(1,39) = 11.86, P , 0.001].'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-24'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
