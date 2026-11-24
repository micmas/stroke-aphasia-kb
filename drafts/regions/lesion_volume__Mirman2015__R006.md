---
id: lesion_volume
name: lesion volume
kind: classical
findings:
- id: f1
  target: semantic_recognition_factor
  target_kind: impairment
  claim: Larger lesion volumes were associated with poorer performance on the Semantic
    Recognition factor.
  direction: likely
  relationship: correlational
  method: LSM
  sample:
    n: 99
    population: individuals with chronic language deficits (aphasia) following left
      hemisphere stroke
    phase: not_reported
    time_post_onset: at least 1 month post onset of aphasia
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - The study only included individuals with left hemisphere lesions.
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Total volume of the lesion as measured by structural
    neuroimaging (MRI or CT). The Semantic Recognition factor was derived via factor
    analysis with varimax rotation from 17 language measures including verbal and
    non-verbal comprehension. Additional metadata has not been transcribed; review
    the pending-field flags before approval. PDF image reading (P2-S2-C4, two-model
    agreement, human verification pending): . Similar to

    the nineteenth century studies that produced the classical Broca-

    Wernicke-Lichtheim model, this study examined individuals

    with neurogenic language disorders, but on an unprecedented

    scale: 99 individuals with chronic language deficits (aphasia)

    following left hemisphere stroke were assessed on 17 different

    measures covering a wide range of language functions, including

    speech perception, spoken word production, verbal and

    non-verbal semantic cognition and short-term memory¹⁵. Original text-layer quotation
    is preserved below. PDF image reading (P7-S1-C6, two-model agreement, human verification
    pending): . To be included in this study, participants had to be at least 1 month
    post onset of aphasia secondary to stroke, living at home, medically stable without
    major psychiatric or neurological co-morbidities and have been premorbidly right
    handed Original text-layer quotation is preserved below.'
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
    - proposed_concept:semantic_recognition_factor
  citation: '@Mirman2015'
  source_passages:
  - section: Original source P2-S4-C2
    page: 2
    quote: "The factor scores tended to be negatively correlated with lesion\nvolume:\
      \ larger lesions were associated with poorer performance\non the Semantic Recognition\
      \ factor (Kendall rank correlation:\nt ¼ \x02 0.23, Po0.001), the Speech Production\
      \ factor (t ¼ \x02 0.19,\nPo0.01) and the Semantic Errors factor (t ¼ \x02 0.18,\
      \ Po0.01),\nalthough not on the Speech Recognition factor (t ¼ \x02 0.06,\n\
      P40.3)."
    supports: claim
  - section: Original source P2-S2-C4
    page: 2
    quote: 'Similar to

      the nineteenth century studies that produced the classical Broca–

      Wernicke–Lichtheim model, this study examined individuals

      with neurogenic language disorders, but on an unprecedented

      scale: 99 individuals with chronic language deﬁcits (aphasia)

      following left hemisphere stroke were assessed on 17 different

      measures covering a wide range of language functions, including

      speech

      perception,

      spoken

      word

      production,

      verbal

      and

      non-verbal

      semantic

      cognition

      and

      short-term

      memory15.'
    supports: sample
  - section: Original source P7-S1-C6
    page: 7
    quote: 'To be included in this study, participants had to be at least

      1 month post onset of aphasia secondary to stroke, living at home, medically
      stable

      without major psychiatric or neurological co-morbidities and have been

      premorbidly right handed.'
    supports: sample
  - section: Original source P7-S1-C7
    page: 7
    quote: 'Participants were also required to have English as the

      primary language, adequate vision and hearing (with or without correction) and

      computed tomography (CT) or magnetic resonance imaging (MRI) conﬁrmed left

      hemisphere cortical lesion.'
    supports: sample
  - section: Original source P2-S3-C3
    page: 2
    quote: 'The ﬁrst factor had high loadings from tests that

      require

      recognition

      of

      semantic

      relationships

      or

      matches,

      including verbal comprehension (word-to-picture matching and

      synonym judgments) and non-verbal comprehension (picture

      association judgments).'
    supports: method
  - section: Original source P2-S3-C4
    page: 2
    quote: 'These tests all require extracting task-

      appropriate semantic content from pictures or words but do not

      require substantial additional processing, as might be necessary

      for categorical inference or semantically driven word production;

      hence, we call this factor ‘Semantic Recognition’.'
    supports: method
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-25'
relationship_review:
  paper: Mirman2015
  proposal_id: R006
  review_status_sha256: 75fd932db527a11d274cf29f83f520b484ea01d524a20a20453893e8ee050c87
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 086cd71672de291d7fc249576e894bc389e0c27b7cadc981d6d2b703f7e80694
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 086cd71672de291d7fc249576e894bc389e0c27b7cadc981d6d2b703f7e80694
        A/passages.json: c29d0ea0a5648303b49e48576e1a9b9704f2ee49bcc85476233f90c031496733
        A/raw.json: 4133da0c4e869d0d847413fda30321fddac14c808c078f72b98dc5bf3ce14769
        A/source-units.json: 54f54dfe07948c3e5da721234ecbabf9a2ec9d88e86afc879892eade212f7d8b
        A/full-source-units.json: a41fd7bf8578d7f817c340799d6807dab7f776bfd85a6a45e58fabd8f4ac3590
        A/meta.json: 6fa7088e720d023d5b639892b4c30ed0d46c4e87be4a4a5f43317f5b76850c74
        A/table-images/manifest.json: 0783a7f538a3dbee5a2710237a2ad8683c0be90a72baeede916850c0ae0c567c
        A/clauses/window-03/raw.json: 31ffaf2ec6a4126345fb781dace7538c5a2c79d182afeb45e7013a73f1a9e08f
        A/clauses/window-03/prompt.txt: d931ad3a21e8272b7f63221c91336b7c2ffc40bb62f4948abfc7cea7a09a489f
        A/clauses/window-03/meta.json: 77306375ee36f8a5fdf12de759c9453e1cc4e7e1ed605c591a0afae5815ae788
        A/clauses/window-04/raw.json: 921320dbad1ff25e6ea3ff725d6375120c7bc3143e4074639c1c71ae3a434d9d
        A/clauses/window-04/prompt.txt: c8cb7950ddbd83452943ef53ed4381a2c07ff65b8d8f7af8d027d0c566f426a3
        A/clauses/window-04/meta.json: dbfc4967993725ce626e84bda6a4b4b8f8f52137ccc0badf32910d7f6cd4c8bd
        A/clauses/window-05/raw.json: 4d695b77f6f9193bea715d85b6cf520becb2fb3b7f6028fd1eff0f5b10f147e5
        A/clauses/window-05/prompt.txt: 6c380a0c13433c107d70de5ffac471af31f6d798f44b22d77f5a1926b25abd72
        A/clauses/window-05/meta.json: d420d729d78441bfbb1fed147044d0d8b72559555105647ebd0fa462390158db
        A/clauses/window-02/raw.json: fbfd33c703d0e421dd641d7e15b6e7ad51b5b97bf2ce856414121e557fa4a4dd
        A/clauses/window-02/prompt.txt: 31c183a4a54cd9ab4758779eb66ad4d0a0ebfa38672cea0a746a8384ea68580f
        A/clauses/window-02/meta.json: 052b70d51b35685aa36f1efd3c9bef07c0fc8cf0ab89ca44f4a33f83d395ff5a
        A/clauses/window-07/raw.json: e71a7d3fd73f34d9a15e0049f2606f54a5f68d273af5eab9965ac3792f389d5c
        A/clauses/window-07/prompt.txt: b3ab0951af9b2f94f9e9bc1f2663288f5770e34c800e2e1ef17b65fd2e41ac44
        A/clauses/window-07/meta.json: 2cdb312957f6b673d8668370fdfe1f0d0695fde46f6427e9084650d2c4bbb2d9
        A/clauses/window-01/raw.json: 878278ab24b22c8bbf5228abe4ecf2725fe6a8bc3c9af9eb5dcad15f1039ee0a
        A/clauses/window-01/prompt.txt: 7f8f04588cfbb115e792119644eba481230b0fd10f3878477f91215c6f7f49a0
        A/clauses/window-01/meta.json: 4131a3c613073ffcbf9bb773eacb4707df7d30c221ab6b1ff6d8a7bcbff50816
        A/clauses/window-06/raw.json: 324b00e2ed293a2a91e91345b633380bdfa355924b7b5df35a1f65eed1f6afb9
        A/clauses/window-06/prompt.txt: e5059c1d91b07c5ed53100746ee989d7c38c8ed554e00626eda91e636fdd4aeb
        A/clauses/window-06/meta.json: b35c68ad495f9b88e3942a3a5377706b15b52ad66f953d8c60e318913134e56d
        B/passages.json: c29d0ea0a5648303b49e48576e1a9b9704f2ee49bcc85476233f90c031496733
        B/raw.json: eb4b94ec30cfc1ac8c64fef78116bc1805d0a4e4bc630b09046c88ed0bcc07a6
        B/source-units.json: 54f54dfe07948c3e5da721234ecbabf9a2ec9d88e86afc879892eade212f7d8b
        B/full-source-units.json: a41fd7bf8578d7f817c340799d6807dab7f776bfd85a6a45e58fabd8f4ac3590
        B/meta.json: 839ea2c95e32419fdbb09fd2fad370012b68485d56744e38c89e2e97d20abfc6
        B/table-images/manifest.json: 0783a7f538a3dbee5a2710237a2ad8683c0be90a72baeede916850c0ae0c567c
        B/clauses/window-03/raw.json: 449a2f811376fb0abb3eb70c568f516fe975d4a05a9714a85caf7a2866b0d3b4
        B/clauses/window-03/prompt.txt: d931ad3a21e8272b7f63221c91336b7c2ffc40bb62f4948abfc7cea7a09a489f
        B/clauses/window-03/meta.json: 2c4669900e9d2009a7b64a9ac2e5029325e04490a23d1c7fd08b9d3170bf8081
        B/clauses/window-04/raw.json: e36eab5a1f19c83bcb68fca979ad38e18108f4ec2e117d69366a3995ee3396cc
        B/clauses/window-04/prompt.txt: c8cb7950ddbd83452943ef53ed4381a2c07ff65b8d8f7af8d027d0c566f426a3
        B/clauses/window-04/meta.json: 7f8560228084967a469998d1467de079fc2be6991310dca8628c8bc8fb2b01bf
        B/clauses/window-05/raw.json: 40e41b48822def97cfed4b7bd05d2173bdff47ccfc1ad6c04da7105e4fe3fb70
        B/clauses/window-05/prompt.txt: 6c380a0c13433c107d70de5ffac471af31f6d798f44b22d77f5a1926b25abd72
        B/clauses/window-05/meta.json: c410dc37e84e5678bc9ac5d1613a348ecea43ff6757a6109239642106d167713
        B/clauses/window-02/raw.json: 72e4de0a7d9bdc6342aa7ee48d913bbe82d8ede9b87940e130d56a16de289215
        B/clauses/window-02/prompt.txt: 31c183a4a54cd9ab4758779eb66ad4d0a0ebfa38672cea0a746a8384ea68580f
        B/clauses/window-02/meta.json: fc62d9e791d6125e085d80a01fd5adc2a4fa7077459dcffccf9d996eb116088b
        B/clauses/window-07/raw.json: 3390c1ed59391a7e0e8b9fe785b854dc77085da290da238df5592542bdfe19fb
        B/clauses/window-07/prompt.txt: b3ab0951af9b2f94f9e9bc1f2663288f5770e34c800e2e1ef17b65fd2e41ac44
        B/clauses/window-07/meta.json: fa2dfe929fc2305477b920e4da753bed208f5e77b4c7474fc1a1998326052c35
        B/clauses/window-01/raw.json: 904a934cdc08c5de26eed1a7ed67175f61d9da05fa5e291b1de1306de0f0d186
        B/clauses/window-01/prompt.txt: 7f8f04588cfbb115e792119644eba481230b0fd10f3878477f91215c6f7f49a0
        B/clauses/window-01/meta.json: 73ca89e23ad4f469228340982d3a975ea198984530a027030685487e79e0fe3c
        B/clauses/window-06/raw.json: 8733f2ef95c643ddd7e9c89952555a1a8e45fb3cdd4e80590dbd7f3ac0434ebe
        B/clauses/window-06/prompt.txt: e5059c1d91b07c5ed53100746ee989d7c38c8ed554e00626eda91e636fdd4aeb
        B/clauses/window-06/meta.json: 307df8e61ba6cb27cdbdcae41aa670f9060ed439be49e83b2d44edc9f4421dc6
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
      pdf_sha256: 086cd71672de291d7fc249576e894bc389e0c27b7cadc981d6d2b703f7e80694
      source_review: _compare/relationships-2026-11-16/review-current/Mirman2015
      source_status_sha256: 0d2fa8bc751f9bdb0220eafb58fdf7f509c74ef4b1bf53838446c1bb1357e07b
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R006
    exposure:
      text: lesion volume
    outcome:
      text: Semantic Recognition factor performance
    analysis_label: Lesion Volume Correlation
    relation: association
    evidence_ids:
    - P2-S4-C2
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
      pdf_sha256: 086cd71672de291d7fc249576e894bc389e0c27b7cadc981d6d2b703f7e80694
      source_review: _compare/relationships-2026-11-16/review-current/Mirman2015
      source_status_sha256: 0d2fa8bc751f9bdb0220eafb58fdf7f509c74ef4b1bf53838446c1bb1357e07b
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P1-S1-C6
      - Result passage disposed without unit P2-S2-C9
      - Result passage disposed without unit P2-S2-C12
      - Accounting without a linked unit P2-S3-C10
      - Accounting without a linked unit P2-S3-C12
      - Accounting without a linked unit P2-S3-C3
      - Accounting without a linked unit P2-S3-C5
      - Accounting without a linked unit P2-S3-C7
      - Accounting without a linked unit P2-S3-C9
      - Accounting without a linked unit P2-S4-C2
      - Unaccounted source passage P2-S3-C7
      - Unaccounted source passage P2-S3-C12
      - Unaccounted source passage P2-S3-C5
      - Unaccounted source passage P2-S3-C9
      - Unaccounted source passage P2-S3-C10
      - Unaccounted source passage P2-S4-C2
      - Unaccounted source passage P2-S3-C3
      - Result passage disposed without unit P2-S4-C5
      - Result passage disposed without unit P2-S4-C6
      - Result passage disposed without unit P2-S4-C9
      - Result passage disposed without unit P4-S1-C4
      - Result passage disposed without unit P4-S1-C5
      - Result passage disposed without unit P4-S1-C7
      - Accounting without a linked unit P4-S2-C3
      - Result passage disposed without unit P5-S1-C1
      - Result passage disposed without unit P5-S1-C4
      - Result passage disposed without unit P5-S1-C5
      - Unaccounted source passage P4-S2-C3
      - Result passage disposed without unit P5-S1-C11
      - Result passage disposed without unit P5-S1-C6
      - Result passage disposed without unit P5-S1-C7
      - Result passage disposed without unit P5-S2-C3
      - Result passage disposed without unit P5-S2-C5
      - Result passage disposed without unit P5-S2-C10
      - Result passage disposed without unit P5-S3-C2
      - Result passage disposed without unit P5-S3-C4
      - Result passage disposed without unit P5-S3-C6
      - Result passage disposed without unit P6-S1-C10
      - Result passage disposed without unit P6-S1-C6
      - Result passage disposed without unit P6-S1-C9
      - Result passage disposed without unit P6-S2-C8
      - Accounting without a linked unit P6-S3-C3
      - Accounting without a linked unit P6-S3-C4
      - Accounting without a linked unit P6-S3-C6
      - Accounting without a linked unit P6-S3-C9
      - Accounting without a linked unit P6-S4-C1
      - Unaccounted source passage P6-S3-C6
      - Unaccounted source passage P6-S3-C3
      - Unaccounted source passage P6-S4-C1
      - Unaccounted source passage P6-S3-C4
      - Unaccounted source passage P6-S3-C9
      - Result passage disposed without unit P7-S2-C6
      - Result passage disposed without unit P7-S2-C10
      - Result passage disposed without unit P7-S2-C7
      - Result passage disposed without unit P7-S2-C9
      - Result passage disposed without unit P7-S3-C2
      - Result passage disposed without unit P7-S3-C3
      - Result passage disposed without unit P7-S3-C6
      - Result passage disposed without unit P7-S3-C7
      - Accounting without a linked unit P7-S3-C9
      - Accounting without a linked unit P7-S4-C1
      - Accounting without a linked unit P7-S4-C2
      - Accounting without a linked unit P7-S4-C3
      - Accounting without a linked unit P7-S4-C4
      - Accounting without a linked unit P7-S4-C8
      - Accounting without a linked unit P7-S4-C9
      - Unaccounted source passage P7-S4-C2
      - Unaccounted source passage P7-S4-C9
      - Unaccounted source passage P7-S3-C9
      - Unaccounted source passage P7-S4-C8
      - Unaccounted source passage P7-S4-C4
      - Unaccounted source passage P7-S4-C1
      - Unaccounted source passage P7-S4-C3
      - Accounting without a linked unit P7-S5-C2
      - Result passage disposed without unit P8-S2-C2
      - Unaccounted source passage P7-S5-C2
      unattached_null_or_qualifier_ids:
      - P2-S3-C9
      - P2-S3-C10
      - P4-S1-C7
      - P5-S2-C3
      - P5-S3-C4
      - P7-S5-C2
      suppressed_nonrepresented_units: 19
      default_disposition_count_requires_completeness_check: 129
      unselected_timing_passages:
      - P2-S2-C4
      - P2-S2-C11
      - P7-S1-C3
      - P7-S1-C6
      - P7-S1-C12
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: validation
        source_id: P3-S1-C1
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P7-S1-C5
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      empty_frame_slots_require_confirmation:
      - validation
      - personal_factors
      - tested_personal_effects
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required: []
      unlinked_tables: []
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P2-S3
        - P2-S4
        - P3-S1
        - P4-S1
        - P4-S2
        - P5-S1
        - P5-S3
        - P7-S6
        - P8-S2
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 086cd71672de291d7fc249576e894bc389e0c27b7cadc981d6d2b703f7e80694
      source_review: _compare/relationships-2026-11-16/review-current/Mirman2015
      source_status_sha256: 0d2fa8bc751f9bdb0220eafb58fdf7f509c74ef4b1bf53838446c1bb1357e07b
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Abstract summary of general findings
    - source_id: P1-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Abstract summary of general findings
    - source_id: P2-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: General summary of results
    - source_id: P2-S2-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Factor analysis thresholding criteria
    - source_id: P2-S3-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of factor loadings
    - source_id: P2-S3-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of factor loadings
    - source_id: P2-S3-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of factor loadings
    - source_id: P2-S3-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of factor loadings
    - source_id: P2-S3-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Correlation between behavioral scores
    - source_id: P2-S3-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Variance captured by model
    - source_id: P2-S4-C2
      disposition: represented
      result_indexes:
      - 6
      - 7
      - 8
      - 9
      reason: Reports correlations between lesion volume and factor scores
    - source_id: P2-S4-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion about cognitive architecture
    - source_id: P2-S4-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion about cognitive architecture
    - source_id: P2-S4-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion about cognitive architecture
    - source_id: P2-S4-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to figure
    - source_id: P3-S1-C1
      disposition: represented
      result_indexes:
      - 0
      reason: Links ATL lesions to semantic errors
    - source_id: P4-S1-C4
      disposition: represented
      result_indexes:
      - 2
      reason: Null finding for ATL and semantic recognition
    - source_id: P4-S1-C5
      disposition: represented
      result_indexes:
      - 1
      reason: Identifies white matter region for semantic recognition
    - source_id: P4-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Anatomical description of the identified region
    - source_id: P4-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Anatomical description of the identified region
    - source_id: P4-S1-C11
      disposition: represented
      result_indexes:
      - 3
      reason: Identifies region for speech production
    - source_id: P4-S2-C3
      disposition: represented
      result_indexes:
      - 4
      reason: Identifies region for speech recognition
    - source_id: P5-S1-C1
      disposition: represented
      result_indexes:
      - 4
      reason: Identifies region for speech recognition
    - source_id: P5-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of behavioral evidence
    - source_id: P5-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of general findings
    - source_id: P5-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of general findings
    - source_id: P5-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of general findings
    - source_id: P5-S1-C8
      disposition: repeated
      result_indexes:
      - 0
      - 1
      reason: Restatement of ATL and white matter findings in discussion
    - source_id: P5-S1-C11
      disposition: repeated
      result_indexes:
      - 3
      reason: Restatement of speech production region
    - source_id: P5-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of null findings for Broca's area
    - source_id: P5-S2-C5
      disposition: repeated
      result_indexes:
      - 4
      reason: Restatement of speech recognition region
    - source_id: P5-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: General discussion of specialization
    - source_id: P5-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: General discussion of dissociation
    - source_id: P5-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of task complexity
    - source_id: P5-S3-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of test loadings
    - source_id: P5-S3-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of anatomical proximity
    - source_id: P5-S3-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to figure
    - source_id: P5-S3-C7
      disposition: represented
      result_indexes:
      - 3
      - 4
      reason: Source for VLSM t-map figure
    - source_id: P6-S1-C2
      disposition: represented
      result_indexes:
      - 0
      reason: Links ATL lesions to semantic errors
    - source_id: P6-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of factor analysis results
    - source_id: P6-S1-C7
      disposition: repeated
      result_indexes:
      - 2
      reason: Restatement of null finding for ATL and semantic recognition
    - source_id: P6-S1-C8
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of ATL and semantic errors
    - source_id: P6-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion about neuroanatomical basis
    - source_id: P6-S1-C10
      disposition: repeated
      result_indexes:
      - 1
      reason: Restatement of white matter bottleneck for semantic recognition
    - source_id: P6-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of connectivity roles
    - source_id: P6-S3-C3
      disposition: repeated
      result_indexes:
      - 0
      - 2
      reason: Restatement of ATL findings and multimodal deficits
    - source_id: P6-S3-C6
      disposition: repeated
      result_indexes:
      - 1
      reason: Restatement of white matter lesion effect
    - source_id: P6-S4-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of other regions
    - source_id: P6-S4-C2
      disposition: repeated
      result_indexes:
      - 1
      reason: Restatement of white matter bottleneck effect
    - source_id: P6-S4-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of redundant hubs
    - source_id: P6-S4-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of frontal lobe heterogeneity
    - source_id: P6-S4-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion
    - source_id: P7-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion
    - source_id: P7-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive test data
    - source_id: P7-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive test data
    - source_id: P7-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive test data
    - source_id: P7-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive test data
    - source_id: P7-S3-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive test data
    - source_id: P7-S3-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive test data
    - source_id: P7-S3-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive test data
    - source_id: P7-S3-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive test data
    - source_id: P7-S3-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive test data
    - source_id: P7-S3-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive test data
    - source_id: P7-S4-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive test data
    - source_id: P7-S4-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive test data
    - source_id: P7-S4-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive test data
    - source_id: P7-S4-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive test data
    - source_id: P7-S4-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive test data
    - source_id: P7-S4-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive test data
    - source_id: P7-S4-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Variance captured by model
    - source_id: P7-S5-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of factor loadings
    - source_id: P8-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of lesion volume control method
    - source_id: P8-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Validation of correction method
    unresolved_coverage:
    - source_id: P2-S4-C2
      disposition: unresolved
      reason: Unknown result index; not accepted as coverage
    - source_id: P5-S3-C7
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P6-S4-C2
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P6-S2-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P6-S3-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P6-S3-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P6-S3-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C6
    - P1-S1-C7
    - P2-S2-C9
    - P2-S2-C12
    - P2-S3-C3
    - P2-S3-C5
    - P2-S3-C7
    - P2-S3-C9
    - P2-S3-C10
    - P2-S3-C12
    - P2-S4-C4
    - P2-S4-C5
    - P2-S4-C6
    - P2-S4-C9
    - P4-S1-C6
    - P4-S1-C7
    - P5-S1-C4
    - P5-S1-C5
    - P5-S1-C6
    - P5-S1-C7
    - P5-S1-C8
    - P5-S1-C11
    - P5-S2-C3
    - P5-S2-C5
    - P5-S2-C8
    - P5-S2-C9
    - P5-S2-C10
    - P5-S3-C2
    - P5-S3-C4
    - P5-S3-C6
    - P6-S1-C6
    - P6-S1-C7
    - P6-S1-C8
    - P6-S1-C9
    - P6-S1-C10
    - P6-S2-C2
    - P6-S2-C8
    - P6-S3-C3
    - P6-S3-C4
    - P6-S3-C6
    - P6-S3-C9
    - P6-S3-C10
    - P6-S4-C1
    - P6-S4-C4
    - P6-S4-C5
    - P6-S4-C9
    - P7-S1-C1
    - P7-S2-C6
    - P7-S2-C7
    - P7-S2-C9
    - P7-S2-C10
    - P7-S3-C2
    - P7-S3-C3
    - P7-S3-C6
    - P7-S3-C7
    - P7-S3-C8
    - P7-S3-C9
    - P7-S4-C1
    - P7-S4-C2
    - P7-S4-C3
    - P7-S4-C4
    - P7-S4-C8
    - P7-S4-C9
    - P7-S4-C13
    - P7-S5-C2
    - P8-S1-C7
    - P8-S2-C2
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review: []
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P2-S2-C4
      - P7-S1-C10
      recruited_sample:
      - P2-S2-C4
      - P7-S1-C10
      eligibility:
      - P7-S1-C6
      - P7-S1-C7
      - P7-S1-C8
      imaging_provenance:
      - P7-S5-C6
      - P7-S5-C7
      - P7-S5-C8
      - P7-S5-C9
      - P7-S5-C10
      - P7-S5-C11
      - P8-S2-C3
      imaging_timing:
      - P7-S1-C11
      outcome_timing:
      - P7-S1-C11
      outcome_definition:
      - P2-S2-C4
      - P7-S2-C3
      validation: []
      analysis_restrictions:
      - P7-S6-C7
      dependent_variable_statement:
      - P8-S1-C1
      limitations:
      - P6-S4-C3
      - P6-S4-C4
      - P6-S4-C5
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P2-S4-C3
      - P8-S1-C2
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P7-S1-C10
      - P7-S1-C11
      - P7-S1-C12
      - P7-S1-C13
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: repeated_patients
    held_selections:
    - slot: validation
      source_id: P3-S1-C1
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P7-S1-C5
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
      pdf_sha256: 086cd71672de291d7fc249576e894bc389e0c27b7cadc981d6d2b703f7e80694
      review_sha256: 75fd932db527a11d274cf29f83f520b484ea01d524a20a20453893e8ee050c87
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
      - P2-S4-C2
      source_result: 'The source reports that factor scores tended to be negatively
        correlated with lesion volume, specifically stating that larger lesions were
        associated with poorer performance on the Semantic Recognition factor (Kendall
        rank correlation: t = -0.23, P < 0.001).'
      result_status: detected
      patient_measurement: regional_lesion_load
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis R006 correctly identifies the correlation
            between lesion volume and the Semantic Recognition factor as described
            in P2-S4-C2. The source explicitly links these variables in a single sentence,
            distinguishing this from the VLSM analyses which control for lesion volume.
          source_ids:
          - P2-S4-C2
          - P2-S3-C4
        direction:
          answer: fits
          reason: The source states 'larger lesions were associated with poorer performance',
            which corresponds to a negative correlation. The draft's claim 'Larger
            lesion volumes were associated with poorer performance' preserves this
            direction accurately.
          source_ids:
          - P2-S4-C2
        construct:
          answer: fits
          reason: The exposure is correctly identified as lesion volume (total lesion
            load). The outcome is the Semantic Recognition factor, which is defined
            in P2-S3-C3 and P2-S3-C4 as a composite of verbal and non-verbal comprehension
            tests. The method is a correlation (Kendall rank), not a voxel-wise mapping,
            which the draft correctly labels as 'LSM' (likely referring to the broader
            Lesion-Symptom Mapping context or a generic label, but the relationship
            is correctly identified as correlational).
          source_ids:
          - P2-S4-C2
          - P2-S3-C3
          - P2-S3-C4
        qualifications:
          answer: fits
          reason: The draft includes the qualification that the factor was derived
            via factor analysis with varimax rotation from 17 measures, which is supported
            by P2-S2-C5 and P2-S3-C3. The limitation regarding left hemisphere lesions
            is also correctly included based on P6-S4-C3 and P7-S1-C7.
          source_ids:
          - P2-S2-C5
          - P2-S3-C3
          - P6-S4-C3
        missing_material_caveat:
          answer: fits
          reason: No material caveats are missing. The source notes that this correlation
            is distinct from the VLSM results (which control for volume), but the
            draft is specifically about the volume correlation, so the VLSM null findings
            are not a caveat for this specific claim. The left hemisphere restriction
            is included.
          source_ids:
          - P2-S4-C2
          - P6-S4-C3
      optional_pending:
      - Specific statistical values (t = -0.23, P < 0.001) are not transcribed in
        the draft but are present in the source.
      - Details of the specific tests comprising the Semantic Recognition factor (e.g.,
        word-to-picture matching) are summarized in the qualification but not itemized.
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Specific statistical values (t = -0.23, P < 0.001) are not transcribed in the
      draft but are present in the source.
    - Details of the specific tests comprising the Semantic Recognition factor (e.g.,
      word-to-picture matching) are summarized in the qualification but not itemized.
    normalizations:
    - field: bucket
      original: predictors
      action: route_from_kind
      value: regions
    analysis_identity:
      id: R006
      exposure:
        text: lesion volume
      outcome:
        text: Semantic Recognition factor performance
      analysis_label: Lesion Volume Correlation
      relation: association
      evidence_ids:
      - P2-S4-C2
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
        pdf_sha256: 086cd71672de291d7fc249576e894bc389e0c27b7cadc981d6d2b703f7e80694
        source_review: _compare/relationships-2026-11-16/review-current/Mirman2015
        source_status_sha256: 0d2fa8bc751f9bdb0220eafb58fdf7f509c74ef4b1bf53838446c1bb1357e07b
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P2-S4-C2:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 086cd71672de291d7fc249576e894bc389e0c27b7cadc981d6d2b703f7e80694
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 14cb33a71aa71fd5181c4da147f3f366b0dc820a82749438ff3a83e30ddbf566
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S4-C2
          page: 2
          text_layer_sha256: 14cb33a71aa71fd5181c4da147f3f366b0dc820a82749438ff3a83e30ddbf566
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: "The factor scores tended to be negatively correlated with\
          \ lesion\nvolume: larger lesions were associated with poorer performance\n\
          on the Semantic Recognition factor (Kendall rank correlation:\nt ¼ \x02\
          \ 0.23, Po0.001), the Speech Production factor (t ¼ \x02 0.19,\nPo0.01)\
          \ and the Semantic Errors factor (t ¼ \x02 0.18, Po0.01),\nalthough not\
          \ on the Speech Recognition factor (t ¼ \x02 0.06,\nP40.3)."
        anchor_text: "The factor scores tended to be negatively correlated with lesion\n\
          volume: larger lesions were associated with poorer performance\non the Semantic\
          \ Recognition factor (Kendall rank correlation:\nt ¼ \x02 0.23, Po0.001),\
          \ the Speech Production factor (t ¼ \x02 0.19,\nPo0.01) and the Semantic\
          \ Errors factor (t ¼ \x02 0.18, Po0.01),\nalthough not on the Speech Recognition\
          \ factor (t ¼ \x02 0.06,\nP40.3)."
        excluded_fragments: []
      P2-S2-C4:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 086cd71672de291d7fc249576e894bc389e0c27b7cadc981d6d2b703f7e80694
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: d7ad3ab275d1f5d5f6309f253cedd557b11c4713806fa1d0712b5f444dc7cdcd
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S2-C4
          page: 2
          text_layer_sha256: d7ad3ab275d1f5d5f6309f253cedd557b11c4713806fa1d0712b5f444dc7cdcd
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Similar to

          the nineteenth century studies that produced the classical Broca–

          Wernicke–Lichtheim model, this study examined individuals

          with neurogenic language disorders, but on an unprecedented

          scale: 99 individuals with chronic language deﬁcits (aphasia)

          following left hemisphere stroke were assessed on 17 different

          measures covering a wide range of language functions, including

          speech

          perception,

          spoken

          word

          production,

          verbal

          and

          non-verbal

          semantic

          cognition

          and

          short-term

          memory15.'
        anchor_text: 'Similar to

          the nineteenth century studies that produced the classical Broca–

          Wernicke–Lichtheim model, this study examined individuals

          with neurogenic language disorders, but on an unprecedented

          scale: 99 individuals with chronic language deﬁcits (aphasia)

          following left hemisphere stroke were assessed on 17 different

          measures covering a wide range of language functions, including

          speech

          perception,

          spoken

          word

          production,

          verbal

          and

          non-verbal

          semantic

          cognition

          and

          short-term

          memory15.'
        excluded_fragments: []
        image_sha256: 290f9c1e5e4463cb88ed9e277f7fd9004e376465245f9734729cf6a0049d6036
        transcription: '. Similar to

          the nineteenth century studies that produced the classical Broca-

          Wernicke-Lichtheim model, this study examined individuals

          with neurogenic language disorders, but on an unprecedented

          scale: 99 individuals with chronic language deficits (aphasia)

          following left hemisphere stroke were assessed on 17 different

          measures covering a wide range of language functions, including

          speech perception, spoken word production, verbal and

          non-verbal semantic cognition and short-term memory¹⁵.'
      P7-S1-C6:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 086cd71672de291d7fc249576e894bc389e0c27b7cadc981d6d2b703f7e80694
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 1e5e7098c679b052b790815d6aac56d7dfaedc87153f83b2c62bd51f9db55405
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P7-S1-C6
          page: 7
          text_layer_sha256: 1e5e7098c679b052b790815d6aac56d7dfaedc87153f83b2c62bd51f9db55405
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'To be included in this study, participants had to be at least

          1 month post onset of aphasia secondary to stroke, living at home, medically
          stable

          without major psychiatric or neurological co-morbidities and have been

          premorbidly right handed.'
        anchor_text: 'To be included in this study, participants had to be at least

          1 month post onset of aphasia secondary to stroke, living at home, medically
          stable

          without major psychiatric or neurological co-morbidities and have been

          premorbidly right handed.'
        excluded_fragments: []
        image_sha256: 7c779925c124a8f9940f78d0a6fa6bb3ea7f64f97c93746545e65fc3c9e50643
        transcription: . To be included in this study, participants had to be at least
          1 month post onset of aphasia secondary to stroke, living at home, medically
          stable without major psychiatric or neurological co-morbidities and have
          been premorbidly right handed
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 2
  quote: "The factor scores tended to be negatively correlated with lesion\nvolume:\
    \ larger lesions were associated with poorer performance\non the Semantic Recognition\
    \ factor (Kendall rank correlation:\nt ¼ \x02 0.23, Po0.001), the Speech Production\
    \ factor (t ¼ \x02 0.19,\nPo0.01) and the Semantic Errors factor (t ¼ \x02 0.18,\
    \ Po0.01),\nalthough not on the Speech Recognition factor (t ¼ \x02 0.06,\nP40.3)."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-25'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
