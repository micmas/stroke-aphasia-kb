---
id: bdae_embedded_sentences
name: BDAE embedded sentences task
kind: predictor
findings:
- id: f1
  target: phonology_working_memory_capacity
  target_kind: impairment
  claim: The BDAE embedded sentences task loaded fairly evenly across four factors,
    with primary loading on the Phonology/Working Memory Capacity factor, and secondary
    loading on Comprehension and Executive Function.
  direction: likely
  relationship: correlational
  method: behavioral_only
  sample:
    n: 38
    population: native English speakers with chronic left hemisphere stroke (>6 months)
    phase: not_reported
    time_post_onset: concurrent
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - not_transcribed
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Participant chooses 1 of 4 pictures described by a
    grammatically complex, auditorily-presented sentence from the Boston Diagnostic
    Aphasia Examination. loading was analyzed via principal components factor analysis
    of the correlation matrix using Varimax rotation with Kaiser normalization. Additional
    metadata has not been transcribed; review the pending-field flags before approval.
    PDF image reading (P2-S1-C6, two-model agreement, human verification pending):
    Methods


    Participants


    Thirty-eight native English speakers with chronic LH stroke (>6 months) participated
    in the study Original text-layer quotation is preserved below.'
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
    - proposed_concept:phonology_working_memory_capacity
  citation: '@Lacey2017'
  source_passages:
  - section: Original source P3-S1-C4
    page: 3
    quote: "Boston Diagnostic Aphasia Examination (BDAE; \nexcerpts)16: The embedded\
      \ sentences, semantic probe, \nand complex ideational material subtests of the\
      \ BDAE \nwere used."
    supports: claim
  - section: Original source P3-S1-C5
    page: 3
    quote: "The embedded sentences subtest requires the \nparticipant to choose 1\
      \ of 4 pictures described by a gram-\nmatically complex, auditorily-presented\
      \ sentence."
    supports: claim
  - section: Original source P5-S1-C8
    page: 5
    quote: "The Boston \nDiagnostic Aphasia Examination embedded sentences task, \n\
      a classic test that putatively assesses grammatical compre-\nhension, loaded\
      \ fairly evenly across the four factors, with \nprimary loading on the Phonology/Working\
      \ Memory \nCapacity factor, and secondary on Comprehension and \nExecutive Function\
      \ (factors 1, 2, 3, 4: .36, .42, .51, .41)."
    supports: claim
  - section: Original source P2-S1-C6
    page: 2
    quote: "Methods\nParticipants\nThirty-eight native English speakers with chronic\
      \ LH \nstroke (>6 months) participated in the study."
    supports: sample
  - section: Original source P3-S1-C8
    page: 3
    quote: "Factor Analysis Methods\nRaw scores on all 25 behavioral tests were entered\
      \ into a \nprincipal components factor analysis of the correlation \nmatrix\
      \ in SPSS 21."
    supports: method
  - section: Original source P3-S1-C10
    page: 3
    quote: "Varimax \nrotation with Kaiser normalization was used to create \northogonal\
      \ factors and the rotated component matrix was \nused to examine the loading\
      \ of each test on the extracted \nfactors."
    supports: method
predictor_type: behavioural
short_definition: Participant chooses 1 of 4 pictures described by a grammatically
  complex, auditorily-presented sentence from the Boston Diagnostic Aphasia Examination.
assessment:
- Boston Diagnostic Aphasia Examination
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-24'
relationship_review:
  paper: Lacey2017
  proposal_id: R010
  review_status_sha256: c687be4a054bff4824a3c1e2e99f1f03f4e4adbcb089669e16289e9f7c975888
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 66c7b22c8dbf0f2aba222be01d7a27a41f4d5a9485815ed30ce6c7b072c5a57a
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 66c7b22c8dbf0f2aba222be01d7a27a41f4d5a9485815ed30ce6c7b072c5a57a
        A/passages.json: fbb2f05aace5668f9b4400499d5cc77d7445c74e73361bf09f8a4f3c8e35dda6
        A/raw.json: 362ee3b11c3a52e9c7881cfc3f246134e5d5600cfc02c536912318ed510ed55e
        A/source-units.json: 83471cdab22896e7bc793067e1ef37e048465d700b5766d3c45ce63626c32419
        A/full-source-units.json: 03291c080445fd0c5de34392fe9ca832399a1066d5502c9a78507260c59422a1
        A/meta.json: c7783d07ec94dede40a0665a4959d99c36cd79028374b0d963b8d2b667688a21
        A/table-images/TABLE-1-page-2-1.png: 8bd3a3d68dd95dea07e62a8aed9938d69d0ce30ef939a355263fd4f851a112eb
        A/table-images/page-2.png: 32124f4419929d353fe45ea4b59b83d89d5733cf56b6bcb7d3c602de1a24c05d
        A/table-images/page-6.png: 05f3c0461578424dd8b250c69435a9c59d7e25aefd26ac14fa628dc1c18704ed
        A/table-images/TABLE-2-page-6-1.png: 06d4d9ab25ebda86a2185d15602ab7c9961cb2923fc6a9d40439b74938c3aafd
        A/table-images/manifest.json: 2b53308dbf0b9a67a4506d4980a9c3bd7bc22b40d18430576a2f6c49074e7156
        A/clauses/window-03/raw.json: 70a2822500dd2fe2e8fd9289fc757428d5b4039595db4d347f3b091b9c91df4b
        A/clauses/window-03/prompt.txt: 6c5dc035c82648eef1318ae69d85983a59d87d6045c71924c2bc82d84599d29d
        A/clauses/window-03/meta.json: c32ab58f98e6cfbe8d12690f343db8ef6d425bac41337490dcec877fc852b876
        A/clauses/window-04/raw.json: 993b840596f820609efa4fff6f079ed240c0a15a41e70a892240c9fd2cb04471
        A/clauses/window-04/prompt.txt: f2531c1d5865a95d3238788c73c5d5d5cfd853429880b4e9c98dec366259bb5b
        A/clauses/window-04/meta.json: 7b71debee8a95b18e72ffc074fd01be234c6437f95021809d6cf7f2093a10f94
        A/clauses/window-05/raw.json: beeb50dd0365f127b4b25bd1a83f10add6d2b4c81628279818042f45bed69d01
        A/clauses/window-05/prompt.txt: 4be6d5c17216d7ba3929fd33d07508e123a39de5941b5b6961407c944be4e2dc
        A/clauses/window-05/meta.json: 48514cd07d8a9ef04fd79bc1f61bf909faf68e883f725a289789b6549b41c14b
        A/clauses/window-02/raw.json: 8db1666bf3ed697e84c5a33d66e4f21b19b6205e062b348b7db5d152b37515f1
        A/clauses/window-02/prompt.txt: 28f6a62e90b4b77ce853f1a24f1a4933bc8b27e11850bd56fa8299c9d0775159
        A/clauses/window-02/meta.json: 3a3cd353077ca7182ea75bcc9cfab7de5b3d12440d4c6ba609e144379c0c66d6
        A/clauses/window-01/raw.json: 16ea7fd5f7689994595721ac655519e36de3ac6c1dca1a30d8c7d0e2ea28ceb3
        A/clauses/window-01/prompt.txt: 5f567c1ce00205630a1c169c9852085f05d6fa16533022981ae72628c9c3351f
        A/clauses/window-01/meta.json: 3593b28c9280abcb571751f35bddb39076df00664b09afd0f489d7c72fa72494
        A/clauses/window-06/raw.json: 23f089321e210366ae25bcafedcf4c78101e0f66a1680ce2aa3c7eb36b7f0d35
        A/clauses/window-06/prompt.txt: 57a37a8f5d5b4df94884a271cb64c8211176c3b91ead3d9aa2cc34e554cbbd2f
        A/clauses/window-06/meta.json: 5c037d1909aa89791926e4def8fa331816e18672fff7df847e5d2d4c951a327a
        A/tables/TABLE-1-page-2-1/raw.json: a7299869171830ca4ed1a6d0c8d4f9f0da86397e75b3940bbbac8dca4a58921c
        A/tables/TABLE-1-page-2-1/prompt.txt: 3e878d2edd5a2c5eb3d297d5f1a9cd957c0d1a331120698d7d505eb358eee230
        A/tables/TABLE-1-page-2-1/meta.json: 70e91e20b76ef31a87702083d8fef8ef5e02734e359aecccbf527bfffad88dee
        A/tables/TABLE-2-page-6-2/raw.json: cfb65d9bac5920a559001af16a9f71e8850a616f6caf77b443789282ea9a0549
        A/tables/TABLE-2-page-6-2/prompt.txt: b833b3cab6c7c718baa9f1c8d95bcd97df2f586a73c0750e9ed029b378085f7f
        A/tables/TABLE-2-page-6-2/meta.json: 24b54905a9f0742c7ea001bff1deeb1f3d6476131e1166aedfde0a77fb5f6605
        B/passages.json: fbb2f05aace5668f9b4400499d5cc77d7445c74e73361bf09f8a4f3c8e35dda6
        B/raw.json: 4a8a2f9f4fec53d5fbb9db112154bb0a0776919e13d41b572bda86b51b26bb38
        B/source-units.json: 83471cdab22896e7bc793067e1ef37e048465d700b5766d3c45ce63626c32419
        B/full-source-units.json: 03291c080445fd0c5de34392fe9ca832399a1066d5502c9a78507260c59422a1
        B/meta.json: ff303ba5fdfa87b655d53f715aac0f115d1bf40f7efc7f073f205c65cc3e5334
        B/table-images/TABLE-1-page-2-1.png: 8bd3a3d68dd95dea07e62a8aed9938d69d0ce30ef939a355263fd4f851a112eb
        B/table-images/page-2.png: 32124f4419929d353fe45ea4b59b83d89d5733cf56b6bcb7d3c602de1a24c05d
        B/table-images/page-6.png: 05f3c0461578424dd8b250c69435a9c59d7e25aefd26ac14fa628dc1c18704ed
        B/table-images/TABLE-2-page-6-1.png: 06d4d9ab25ebda86a2185d15602ab7c9961cb2923fc6a9d40439b74938c3aafd
        B/table-images/manifest.json: d40ad50a758150f2610bfab8e5ab661ece89166efa3ec5e11afd3f5b1cbd01c5
        B/clauses/window-03/raw.json: bc6f9385e4c67ca7bd2a2613906fa4a44240e14c7a981d95a7e1e712f58c38e0
        B/clauses/window-03/prompt.txt: 6c5dc035c82648eef1318ae69d85983a59d87d6045c71924c2bc82d84599d29d
        B/clauses/window-03/meta.json: a39f784edc9fcc50e99bb3f52f8e1da9aa1359d76c7777a75017aa4356ba4cc4
        B/clauses/window-04/raw.json: 003f1a5801823ec53463525b13b082fba2af6ff52b318878bb82230130204cf9
        B/clauses/window-04/prompt.txt: f2531c1d5865a95d3238788c73c5d5d5cfd853429880b4e9c98dec366259bb5b
        B/clauses/window-04/meta.json: 785a361a8c948409ac2cd156eb8d0c1f2c7b6c751e8a798db4ac60395a2b7bbf
        B/clauses/window-05/raw.json: 83ebff123e335ca860314f84c8dfebebac7cfd98fcd0181ebc2ae1a2af033314
        B/clauses/window-05/prompt.txt: 4be6d5c17216d7ba3929fd33d07508e123a39de5941b5b6961407c944be4e2dc
        B/clauses/window-05/meta.json: ce6ec67e2476fe60c3b99cf0194cf4eb74f9ffca3b036e80318560278ff28390
        B/clauses/window-02/raw.json: 76e0506c2e89f12e6839bdbec7cf4d9e67199bc5fe1692f3fced201068f00ac7
        B/clauses/window-02/prompt.txt: 28f6a62e90b4b77ce853f1a24f1a4933bc8b27e11850bd56fa8299c9d0775159
        B/clauses/window-02/meta.json: 4fdbe5cae1909992b6681e45b43d4af237ac995f4a457b3130bdb757bf718413
        B/clauses/window-01/raw.json: 17aa7e929340cf199640817c56164e752c16e489b70bb2fe655f6b062caee7dd
        B/clauses/window-01/prompt.txt: 5f567c1ce00205630a1c169c9852085f05d6fa16533022981ae72628c9c3351f
        B/clauses/window-01/meta.json: 299e065b39d20b3ad468ccc5349657097719f5a7226e1a7fcac90bbe96327ce3
        B/clauses/window-06/raw.json: 8b52d34feec4a24274aaf5c0aae149ded43def351cc5fd72502a2953846a032a
        B/clauses/window-06/prompt.txt: 57a37a8f5d5b4df94884a271cb64c8211176c3b91ead3d9aa2cc34e554cbbd2f
        B/clauses/window-06/meta.json: d81914fd4de6e2e471d1e1c67076a3eaea86181bdc87c435d15ae6efad9b1725
        B/tables/TABLE-1-page-2-1/raw.json: a7e18a221de3e3f88080c3623da75534727d9deabc75d90c3d03bcf19e78f86f
        B/tables/TABLE-1-page-2-1/prompt.txt: 3e878d2edd5a2c5eb3d297d5f1a9cd957c0d1a331120698d7d505eb358eee230
        B/tables/TABLE-1-page-2-1/meta.json: 09afacab2e725b277ff29f49d6e684568234cf3354b1145bf68a9164c49951ba
        B/tables/TABLE-2-page-6-2/raw.json: 0daddc50fe180b7b223cb687e9a813463c8ec58e84474f2593f215a32cd3abb8
        B/tables/TABLE-2-page-6-2/prompt.txt: b833b3cab6c7c718baa9f1c8d95bcd97df2f586a73c0750e9ed029b378085f7f
        B/tables/TABLE-2-page-6-2/meta.json: 269be995603d47d7222e7d34f13396bcb94084f88278b6398cd1178c0e71554b
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
      pdf_sha256: 66c7b22c8dbf0f2aba222be01d7a27a41f4d5a9485815ed30ce6c7b072c5a57a
      source_review: _compare/relationships-2026-11-16/review-current/Lacey2017
      source_status_sha256: 505a2ff9a5d7b1bfb91afc1ed1278e7cfa2f5647b13f4babc41ddd49803f1d4e
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R010
    exposure:
      text: BDAE embedded sentences task
    outcome:
      text: Phonology/Working Memory Capacity factor (primary), Comprehension and
        Executive Function (secondary)
    analysis_label: Factor Loading Analysis
    relation: association
    evidence_ids:
    - P5-S1-C8
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
      pdf_sha256: 66c7b22c8dbf0f2aba222be01d7a27a41f4d5a9485815ed30ce6c7b072c5a57a
      source_review: _compare/relationships-2026-11-16/review-current/Lacey2017
      source_status_sha256: 505a2ff9a5d7b1bfb91afc1ed1278e7cfa2f5647b13f4babc41ddd49803f1d4e
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Accounting without a linked unit P1-S2-C16
      - Result passage disposed without unit P1-S2-C17
      - Accounting without a linked unit P1-S2-C18
      - Result passage disposed without unit P1-S2-C19
      - Result passage disposed without unit P1-S2-C21
      - Unresolved source passage P2-S2-C15
      - Unaccounted source passage P1-S2-C18
      - Unaccounted source passage P1-S2-C16
      - Result passage disposed without unit P4-S1-C6
      - Result passage disposed without unit P4-S1-C7
      - Result passage disposed without unit P4-S1-C8
      - Result passage disposed without unit P4-S1-C9
      - Result passage disposed without unit P4-S2-C1
      - Result passage disposed without unit P4-S2-C2
      - Result passage disposed without unit P4-S2-C3
      - Result passage disposed without unit P5-S1-C2
      - Result passage disposed without unit P5-S1-C3
      - Result passage disposed without unit P5-S1-C7
      - Result passage disposed without unit P5-S2-C2
      - Result passage disposed without unit P5-S2-C3
      - Result passage disposed without unit P5-S2-C9
      - Result passage disposed without unit P5-S2-C13
      - Result passage disposed without unit P5-S2-C14
      - Result passage disposed without unit P5-S3-C3
      - Result passage disposed without unit P5-S3-C4
      - Result passage disposed without unit P6-S2-C1
      - Result passage disposed without unit P7-S1-C1
      - Result passage disposed without unit P7-S1-C4
      - Result passage disposed without unit P7-S2-C3
      - Accounting without a linked unit P7-S2-C6
      - Accounting without a linked unit P7-S3-C1
      - Accounting without a linked unit P7-S3-C2
      - Accounting without a linked unit P7-S3-C4
      - Accounting without a linked unit P7-S3-C5
      - Unaccounted source passage P7-S3-C1
      - Unaccounted source passage P7-S3-C2
      - Unaccounted source passage P7-S3-C5
      - Unaccounted source passage P7-S2-C6
      - Unaccounted source passage P7-S3-C4
      unattached_null_or_qualifier_ids:
      - P1-S2-C17
      - P5-S1-C7
      - P7-S1-C4
      suppressed_nonrepresented_units: 24
      default_disposition_count_requires_completeness_check: 105
      unselected_timing_passages:
      - P1-S2-C12
      - P2-S1-C6
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P5-S2-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P6-S2-C1
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P6-S2-C3
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: limitations
        source_ids:
        - P2-S1-C8
        - P3-S2-C8
        - P3-S2-C9
        - P4-S1-C4
        - P5-S3-C3
        - P7-S1-C2
        - P7-S1-C3
        - P7-S2-C2
        - P7-S2-C3
        - P8-S1-C2
        - P8-S1-C3
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - validation
      - limitations
      - personal_factors
      - tested_personal_effects
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-2-1
      - TABLE-2-page-6-2
      unlinked_tables:
      - TABLE-1-page-2-1
      - TABLE-2-page-6-2
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
        - P5-S2
        - P5-S3
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 66c7b22c8dbf0f2aba222be01d7a27a41f4d5a9485815ed30ce6c7b072c5a57a
      source_review: _compare/relationships-2026-11-16/review-current/Lacey2017
      source_status_sha256: 505a2ff9a5d7b1bfb91afc1ed1278e7cfa2f5647b13f4babc41ddd49803f1d4e
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S2-C16
      disposition: represented
      result_indexes:
      - 0
      reason: Identifies the 4 factors extracted by PCA.
    - source_id: P1-S2-C17
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about test loadings without specifying which tests
        or factors.
    - source_id: P1-S2-C18
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about lesion mapping results.
    - source_id: P1-S2-C19
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about correspondence to neural models.
    - source_id: P1-S2-C21
      disposition: background_or_descriptive
      result_indexes: []
      reason: Conclusion statement summarizing the study's general finding.
    - source_id: P4-S1-C6
      disposition: represented
      result_indexes:
      - 0
      reason: States PCA yielded four factors accounting for 81% variance.
    - source_id: P4-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about factor correspondence to language processes.
    - source_id: P4-S1-C8
      disposition: represented
      result_indexes:
      - 1
      reason: Lists tests loading onto factor 1 (Word Finding/Fluency).
    - source_id: P4-S1-C9
      disposition: represented
      result_indexes:
      - 2
      reason: Lists tests loading onto factor 2 (Comprehension).
    - source_id: P4-S2-C1
      disposition: repeated
      result_indexes:
      - 2
      reason: Restatement of factor 2 label.
    - source_id: P4-S2-C2
      disposition: represented
      result_indexes:
      - 3
      reason: Lists tests loading onto factor 3 (Phonology/Working Memory Capacity).
    - source_id: P4-S2-C3
      disposition: repeated
      result_indexes:
      - 4
      reason: Restatement of factor 4 label.
    - source_id: P4-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Technical detail about PCA convergence.
    - source_id: P5-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Introductory sentence to loading differences.
    - source_id: P5-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about pure measures loading specifically.
    - source_id: P5-S1-C4
      disposition: represented
      result_indexes:
      - 5
      reason: Specific loading of naming tasks on Word Finding/Fluency.
    - source_id: P5-S1-C5
      disposition: represented
      result_indexes:
      - 6
      reason: Specific loading of letter fluency on factors 1 and 4.
    - source_id: P5-S1-C6
      disposition: represented
      result_indexes:
      - 7
      - 8
      reason: Specific loadings of auditory comprehension tests on factors 1 and 3.
    - source_id: P5-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Introductory sentence to unexpected loadings.
    - source_id: P5-S1-C8
      disposition: represented
      result_indexes:
      - 9
      reason: Specific loading of BDAE embedded sentences task.
    - source_id: P5-S1-C9
      disposition: represented
      result_indexes:
      - 10
      reason: Specific loading of Pyramids and Palm Trees test.
    - source_id: P5-S1-C10
      disposition: repeated
      result_indexes:
      - 11
      reason: Describes the analysis used for demographic correlations.
    - source_id: P5-S1-C11
      disposition: represented
      result_indexes:
      - 11
      reason: Reports null relationship between demographics and factor scores.
    - source_id: P5-S2-C1
      disposition: repeated
      result_indexes:
      - 11
      reason: Lists demographic factors used in correlation.
    - source_id: P5-S2-C2
      disposition: repeated
      result_indexes:
      - 11
      reason: Restates null result (P > .10).
    - source_id: P5-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about SVR-LSM results.
    - source_id: P5-S2-C4
      disposition: represented
      result_indexes:
      - 12
      reason: Associates Word Finding/Fluency deficits with IFG and anterior insula.
    - source_id: P5-S2-C5
      disposition: represented
      result_indexes:
      - 12
      reason: Associates Word Finding/Fluency deficits with dorsal parietal white
        matter.
    - source_id: P5-S2-C6
      disposition: represented
      result_indexes:
      - 13
      reason: Associates Comprehension deficits with superior temporal cortex.
    - source_id: P5-S2-C7
      disposition: represented
      result_indexes:
      - 14
      reason: Associates Phonology/Working Memory deficits with ventral motor/somatosensory
        cortex, supramarginal gyrus, and posterior planum temporale.
    - source_id: P5-S2-C8
      disposition: represented
      result_indexes:
      - 15
      reason: Associates Executive Function deficits with middle frontal gyrus, dorsal
        Rolandic cortex, and posterior frontal white matter.
    - source_id: P5-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement about lack of overlap between maps.
    - source_id: P5-S2-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion summary of findings.
    - source_id: P5-S2-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about test loadings.
    - source_id: P5-S2-C15
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about tests relying on multiple factors.
    - source_id: P5-S3-C3
      disposition: repeated
      result_indexes:
      - 3
      reason: Restatement of WAB repetition loading on Phonology/Working Memory.
    - source_id: P5-S3-C4
      disposition: repeated
      result_indexes:
      - 9
      reason: Restatement of BDAE embedded sentences loading on all 4 factors.
    - source_id: P6-S2-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison to prior studies.
    - source_id: P7-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about differences from prior studies.
    - source_id: P7-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of 'speech quanta' in other studies.
    - source_id: P7-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison of digit span loadings between studies.
    - source_id: P7-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about similarity of factors across labs.
    - source_id: P7-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about MCA distribution and language processes.
    - source_id: P7-S1-C7
      disposition: repeated
      result_indexes:
      - 12
      reason: Restates association of IFG lesions with Word Finding/Fluency.
    - source_id: P7-S2-C2
      disposition: repeated
      result_indexes:
      - 5
      reason: Restates naming tasks loading on Word Finding/Fluency.
    - source_id: P7-S2-C3
      disposition: repeated
      result_indexes:
      - 6
      reason: Restates category/letter fluency relying on Executive Function and Word
        Finding/Fluency.
    - source_id: P7-S2-C6
      disposition: repeated
      result_indexes:
      - 13
      reason: Restates localization of comprehension anterior to Heschl's gyrus.
    - source_id: P7-S3-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of sentence-level comprehension.
    - source_id: P7-S3-C2
      disposition: repeated
      result_indexes:
      - 14
      reason: Restates Phonology/Working Memory map consistency with dorsal stream.
    - source_id: P7-S3-C3
      disposition: repeated
      result_indexes:
      - 14
      reason: Restates mapping of phonology factors to parietal areas.
    - source_id: P7-S3-C4
      disposition: repeated
      result_indexes:
      - 15
      reason: Restates association of Executive Function with frontoparietal network.
    - source_id: P7-S3-C5
      disposition: repeated
      result_indexes:
      - 15
      reason: Restates association of Executive Function with superior longitudinal
        fasciculus.
    - source_id: P8-S1-C1
      disposition: repeated
      result_indexes:
      - 10
      reason: Restates Pyramids and Palm Trees loading on Executive factor.
    unresolved_coverage:
    - source_id: P5-S1-C10
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P5-S1-C11
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P5-S2-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P5-S2-C15
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    pending_source_ids:
    - P1-S2-C16
    - P1-S2-C17
    - P1-S2-C18
    - P1-S2-C19
    - P1-S2-C21
    - P4-S1-C7
    - P4-S2-C1
    - P4-S2-C3
    - P4-S2-C6
    - P5-S1-C2
    - P5-S1-C3
    - P5-S1-C7
    - P5-S2-C2
    - P5-S2-C3
    - P5-S2-C9
    - P5-S2-C13
    - P5-S2-C14
    - P5-S3-C3
    - P5-S3-C4
    - P6-S2-C1
    - P7-S1-C1
    - P7-S1-C2
    - P7-S1-C3
    - P7-S1-C4
    - P7-S1-C5
    - P7-S1-C7
    - P7-S2-C2
    - P7-S2-C3
    - P7-S2-C6
    - P7-S3-C1
    - P7-S3-C2
    - P7-S3-C3
    - P7-S3-C4
    - P7-S3-C5
    - P8-S1-C1
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-2-1
    - TABLE-2-page-6-2
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P2-S1-C6
      recruited_sample:
      - P2-S1-C6
      eligibility:
      - P2-S1-C6
      - P2-S1-C7
      imaging_provenance:
      - P3-S1-C11
      imaging_timing:
      - P3-S1-C11
      outcome_timing:
      - P3-S1-C11
      outcome_definition:
      - P1-S2-C13
      - P1-S2-C14
      - P3-S1-C8
      - P3-S2-C5
      - P4-S1-C6
      - P5-S2-C3
      validation: []
      analysis_restrictions:
      - P4-S1-C4
      dependent_variable_statement:
      - P1-S2-C13
      - P1-S2-C14
      - P3-S2-C5
      limitations: []
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P4-S1-C2
      - P5-S1-C10
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P2-S3-C6
      - P5-S1-C10
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: internal_cross_validation
    held_selections:
    - slot: dependent_variable_statement
      source_id: P5-S2-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P6-S2-C1
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P6-S2-C3
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: limitations
      source_ids:
      - P2-S1-C8
      - P3-S2-C8
      - P3-S2-C9
      - P4-S1-C4
      - P5-S3-C3
      - P7-S1-C2
      - P7-S1-C3
      - P7-S2-C2
      - P7-S2-C3
      - P8-S1-C2
      - P8-S1-C3
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
      pdf_sha256: 66c7b22c8dbf0f2aba222be01d7a27a41f4d5a9485815ed30ce6c7b072c5a57a
      review_sha256: c687be4a054bff4824a3c1e2e99f1f03f4e4adbcb089669e16289e9f7c975888
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
      - P5-S1-C8
      source_result: The Boston Diagnostic Aphasia Examination embedded sentences
        task loaded fairly evenly across the four factors, with a primary loading
        on the Phonology/Working Memory Capacity factor and secondary loadings on
        Comprehension and Executive Function.
      result_status: detected
      patient_measurement: non_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis is the factor loading of the BDAE embedded
            sentences task within the principal components analysis, as described
            in P5-S1-C8. The proposed core correctly identifies this specific analysis
            and its outcome (loading pattern).
          source_ids:
          - P5-S1-C8
          - P3-S1-C8
        direction:
          answer: fits
          reason: The source states the task loaded 'fairly evenly' with 'primary
            loading on the Phonology/Working Memory Capacity factor'. The proposed
            core claim accurately reflects this direction and magnitude of association
            (loading) without misrepresenting it as a null or a different significant
            outcome.
          source_ids:
          - P5-S1-C8
        construct:
          answer: fits
          reason: The exposure is correctly identified as the BDAE embedded sentences
            task. The outcome is the factor loading on the Phonology/Working Memory
            Capacity factor (primary) and others (secondary). The patient measurement
            is non-imaging (behavioral test scores), which is correct for a factor
            analysis of behavioral data. The source explicitly distinguishes this
            from the subsequent lesion-symptom mapping (imaging) analysis.
          source_ids:
          - P3-S1-C4
          - P3-S1-C5
          - P5-S1-C8
        qualifications:
          answer: fits
          reason: The proposed core includes the qualification that the loading was
            analyzed via principal components factor analysis with Varimax rotation.
            This matches the method described in P3-S1-C8 and P3-S1-C10. No material
            qualifiers are lost.
          source_ids:
          - P3-S1-C8
          - P3-S1-C10
        missing_material_caveat:
          answer: fits
          reason: The source notes that the task loaded 'fairly evenly' across factors,
            which is captured in the claim. The discussion in P5-S3-C4 reinforces
            this complexity. No material caveats regarding the interpretation of this
            specific loading pattern are omitted from the proposed core.
          source_ids:
          - P5-S1-C8
          - P5-S3-C4
      optional_pending:
      - Specific loading values (.36, .42, .51, .41) are not transcribed in the core
        claim but are present in P5-S1-C8.
      - The exact number of factors extracted (4) is mentioned in P4-S1-C6 but not
        explicitly in the core claim, though implied by 'four factors'.
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Specific loading values (.36, .42, .51, .41) are not transcribed in the core
      claim but are present in P5-S1-C8.
    - The exact number of factors extracted (4) is mentioned in P4-S1-C6 but not explicitly
      in the core claim, though implied by 'four factors'.
    normalizations: []
    analysis_identity:
      id: R010
      exposure:
        text: BDAE embedded sentences task
      outcome:
        text: Phonology/Working Memory Capacity factor (primary), Comprehension and
          Executive Function (secondary)
      analysis_label: Factor Loading Analysis
      relation: association
      evidence_ids:
      - P5-S1-C8
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
        pdf_sha256: 66c7b22c8dbf0f2aba222be01d7a27a41f4d5a9485815ed30ce6c7b072c5a57a
        source_review: _compare/relationships-2026-11-16/review-current/Lacey2017
        source_status_sha256: 505a2ff9a5d7b1bfb91afc1ed1278e7cfa2f5647b13f4babc41ddd49803f1d4e
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P2-S1-C6:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 66c7b22c8dbf0f2aba222be01d7a27a41f4d5a9485815ed30ce6c7b072c5a57a
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 626e738f381c10063a097ef0a7f796e80c068afc1548fc9ca52cb03d05377ebd
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S1-C6
          page: 2
          text_layer_sha256: 626e738f381c10063a097ef0a7f796e80c068afc1548fc9ca52cb03d05377ebd
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "Methods\nParticipants\nThirty-eight native English speakers\
          \ with chronic LH \nstroke (>6 months) participated in the study."
        anchor_text: "Methods\nParticipants\nThirty-eight native English speakers\
          \ with chronic LH \nstroke (>6 months) participated in the study."
        excluded_fragments: []
        image_sha256: 5b6bb669df99f3ef85217974b11ae4b1569eeec11879f1c490b8f8ea2ef1f0df
        transcription: 'Methods


          Participants


          Thirty-eight native English speakers with chronic LH stroke (>6 months)
          participated in the study'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 3
  quote: "Boston Diagnostic Aphasia Examination (BDAE; \nexcerpts)16: The embedded\
    \ sentences, semantic probe, \nand complex ideational material subtests of the\
    \ BDAE \nwere used."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-24'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
