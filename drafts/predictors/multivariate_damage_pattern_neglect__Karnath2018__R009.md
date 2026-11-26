---
id: multivariate_damage_pattern_neglect
name: multivariate damage pattern predictor
kind: predictor
findings:
- id: f1
  target: spatial_neglect
  target_kind: impairment
  claim: Karnath2018 reports, based on Smith et al. (2013), that patterns of damage were more predictive of spatial neglect than the best-performing single voxel
  direction: likely
  relationship: synthesis
  method: narrative_review
  sample:
    n: not_reported
    population: 'Participants in the studies summarized by Karnath2018; this record is a secondary review report, not a newly recruited cohort. Primary source: Smith et al. (2013).'
    phase: not_reported
    time_post_onset: Varies across reviewed studies; see cited primary study and source passages.
  statistics:
    threshold: not_applicable_review_synthesis
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - finding is reported within a narrative review of a prior study (Smith et al., 2013)
  evidence_quality: narrative-review
  strength: weak
  notes: 'Reclassified as a secondary review report, explicitly attributing the result to Smith et al. (2013). This is not a new primary sample or independent replication; quantitative estimates and study-level attribution require human verification against the primary publication. Source repair (unapproved): Reclassified as a secondary review report, explicitly attributing the result to Smith et al. (2013). This is not a new primary sample or independent replication; quantitative estimates and study-level attribution require human verification against the primary publication.'
  imaging_details:
    reference_space: not_applicable
    atlases_used: []
  lesion_mapping: {}
  provenance:
    extracted_by: agent:source-repair
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
    - not_transcribed:sample.n
    - proposed_concept:spatial_neglect
    - agent_source_repair_pending_human_review
  citation: '@Karnath2018'
  source_passages:
  - section: Original source P7-S2-C3
    page: 7
    quote: 'In a large sample of

      right hemispheric stroke patients, they found patterns of damage more

      predictive of spatial neglect than the best-performing single voxel.'
    supports: claim
  - section: Original source P7-S1-C15
    page: 7
    quote: 'In a large sample of

      '
    supports: sample
  - section: Original source P6-S3-C8
    page: 6
    quote: 'Multivariate lesion analysis with machine learning algorithms

      Unlike VLBM''s mass-univariate testing approach, machine learning

      based lesion analysis offers a multivariate approach to lesion analysis.'
    supports: method
  design: narrative-review
predictor_type: imaging_metric
short_definition: multivariate patterns of structural damage (lesion status of multiple voxels) in the brain
assessment: []
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-24'
relationship_review:
  paper: Karnath2018
  proposal_id: R009
  approved: false
  original_core_review:
    paper: Karnath2018
    proposal_id: R009
    review_status_sha256: 1fbc9305ad0a2f592e05e317766596032c7b6e691efb6c3ba2125c242408e7f0
    review_binding:
      version: candidate-inventory-v1
      input_hashes:
        pdf: dbbf5db9f646e5ed67190025aea75aff5c20f899e9304ffa7b67f2d7641a12b8
      original_review_binding:
        version: relationship-review-v4
        input_hashes:
          pdf: dbbf5db9f646e5ed67190025aea75aff5c20f899e9304ffa7b67f2d7641a12b8
          A/passages.json: a7ef357c214c37c4e6ff921b063b689faf618f39d8e4f410a5aad6fa98313b1a
          A/raw.json: d1fefd9177998f06722a4998458a81647ec6a9192c427ff55adb89f8e56ea440
          A/source-units.json: 0b37ebf3adee7a5434171808b481506031269d29260804822cbdb49284bfb3b6
          A/full-source-units.json: 8c1ad66527454a0ed883d0bf8d0d94981ea1a915fd599fd36cce01954d7e296a
          A/meta.json: 46f48df6e3c5ae4ea7b343cef1ce3461a5167b9b3faa63c1310f6b213176be5a
          A/table-images/manifest.json: ab5b9fa5e5738ee57af1f7a67291b70cf6c39bc94a18b73ae17551a5ed764f87
          A/clauses/window-11/raw.json: ba65b808fc7ca28970f57805b899a697ae3f1094f437ba5ec775e2b48e2d5515
          A/clauses/window-11/prompt.txt: 48823ef4591a16826e8d78c7492feed9a8fe3a62b067746f72d2c47ee5f61072
          A/clauses/window-11/meta.json: 31b798098edb5b8d216cd7147d08682cc097a59178cb38e1fc26b6a8a8a0a4ec
          A/clauses/window-10/raw.json: 2b53690fe3728ba24db45d895a8bd6f5d6a0688b714141bce131553d0fd034a8
          A/clauses/window-10/prompt.txt: e7930c5abb3e94e850630bdbf0e9b3343d5666aa4a772b2f7a57ffd636f51d3f
          A/clauses/window-10/meta.json: 8f0ff0ca98f3b58156b13bd7fb9df0db2568a5bda5189b7ba36420b12480b5a7
          A/clauses/window-03/raw.json: bff13fdd5409741a93a93772a55ec8b99da50286c3d8c8fdc3ded40efe6b63dc
          A/clauses/window-03/prompt.txt: f3ebd14700cc8c5060ca6edde62c35f9aaf9cc293e6e934b9f371c472e1214ae
          A/clauses/window-03/meta.json: f3449c1b553a10a9009c72490d6d0f9a342a07cafb305090e2d000ac7ed3a3dc
          A/clauses/window-04/raw.json: 6c717bdbf7d195ea5a56e4fefbef67b04cfaf385f045c076d9195bea43ef19fe
          A/clauses/window-04/prompt.txt: 48061db2d32f824e28d38b35bdb22dca802e6eb7bc9dcee19e18e12328a835cd
          A/clauses/window-04/meta.json: 1dff8a775128debccaa031eb09ec1db4e4d472a1e7890da3669744af7c585136
          A/clauses/window-05/raw.json: e9697c35ba6f1c25bdfd2dec916cd135f774ea8731e7094e4de6ac8f840aad60
          A/clauses/window-05/prompt.txt: e512beb45931f6ea695361c9c07ef95ba0b2c165540aa651d30ee0e995e28e3e
          A/clauses/window-05/meta.json: 732c95f9a2057dec30489680541b52c13297850487f0fceaa3d641562f782963
          A/clauses/window-02/raw.json: 1f0af08f96ee227fb877d3c302cf9d55f17a5b01555fbbe122337ffd95316061
          A/clauses/window-02/prompt.txt: 79519d404926eb73ba82fbd05bb352f2ad4256b15feb2f349f2c8cf3012552fb
          A/clauses/window-02/meta.json: d45d56ca432520154ce81c3e82f1c6d68e0d627bf29cad10b75c6587207a6c84
          A/clauses/window-12/raw.json: 9418fa57efc0507f3a75bd89171c423584277403e7a8f6ce49c780ca8bb5f599
          A/clauses/window-12/prompt.txt: 182954004d179ca9355c66012fdbf2e955e3d18751b2a840fd0d8b07b03c9f81
          A/clauses/window-12/meta.json: a68bdac99b111268035530710d2449e99e6d4dcb174f6922625d233ac4b9f256
          A/clauses/window-09/raw.json: 1b53295af2532f5e21ecc20c1e81ee62d83df853576e0d77f33886f9eadd1fcc
          A/clauses/window-09/prompt.txt: 9dc4ab65efa54b689ce5bfe1d48e2fb42c32176cf7889a6af99593d3d7339d7f
          A/clauses/window-09/meta.json: 7ae8a464f9703d30957c061e098e33702a6fc916e88f0b7c283b862184562c98
          A/clauses/window-07/raw.json: e48b06a514299b149dc19af4f961a8f0f3eb3be7dcca622fd77994c15ec7506f
          A/clauses/window-07/prompt.txt: d553e7a64945a1f7371e4193ce4e71becfe5576b91e0a2e3c2c5ac418654e52f
          A/clauses/window-07/meta.json: 78dc81a52245b40ab1793c22d96409b2ac0ecc52073c4585aa2bd1af7e462d82
          A/clauses/window-01/raw.json: 34e88a9bac868638e56a251639be5e82d22877e2257a01a0fe4075829e33ff87
          A/clauses/window-01/prompt.txt: 84b3e222547768364f39605a8c7290111dd2c1ef8a664f4315bc3bc8aa08a303
          A/clauses/window-01/meta.json: b8fe90b54847f0e062bf3337cb38ec10ff16c782856425a5c9b8e166d783091d
          A/clauses/window-06/raw.json: e02444d67355a8630b2b82b0f335366c03294b447ecde47f362885597c400ada
          A/clauses/window-06/prompt.txt: f3fa1828d9bc777db524c65657a207c39080908e9bca29b5837d0ec8e802728b
          A/clauses/window-06/meta.json: 6b553fb15def952220ab7e03c50538d9d477a12726cb45f2444fa5a9599c53b7
          A/clauses/window-08/raw.json: d65615e9a875d79e96cf839205c6152385081e793e651b4b2855a28591e701bb
          A/clauses/window-08/prompt.txt: 650bd9c37008f9af4d8c3969857cd4a2d2880e9273bb919b85321925c69bdf90
          A/clauses/window-08/meta.json: f3c64559ddac1aef34956120e850baa712292a787dc276571fa7c4f6c9d8b9b6
          B/passages.json: a7ef357c214c37c4e6ff921b063b689faf618f39d8e4f410a5aad6fa98313b1a
          B/raw.json: c4068a9f59ca03fbbc52bc1d099d3af3f077058a829dd45cd175d3a5f7ee6a6c
          B/source-units.json: 0b37ebf3adee7a5434171808b481506031269d29260804822cbdb49284bfb3b6
          B/full-source-units.json: 8c1ad66527454a0ed883d0bf8d0d94981ea1a915fd599fd36cce01954d7e296a
          B/meta.json: bb81b1aa338c269abbc062c2de2137dcdda694645ac07b88ef07270b8a0b21a1
          B/table-images/manifest.json: ab5b9fa5e5738ee57af1f7a67291b70cf6c39bc94a18b73ae17551a5ed764f87
          B/clauses/window-11/raw.json: b3fd779b587afa6064074782532ebe0dc8d18c95a7ae5e4a3af36f72405934d5
          B/clauses/window-11/prompt.txt: 48823ef4591a16826e8d78c7492feed9a8fe3a62b067746f72d2c47ee5f61072
          B/clauses/window-11/meta.json: 5f4b07c9d7d5fe9b23e97eb83ea7b42859d87ee227b6a425a81203d793e4f995
          B/clauses/window-10/raw.json: 2fe16ff4e81eb16b2b318cb44271896500e3efa9f2441d18567c1ed2c45b7cc0
          B/clauses/window-10/prompt.txt: e7930c5abb3e94e850630bdbf0e9b3343d5666aa4a772b2f7a57ffd636f51d3f
          B/clauses/window-10/meta.json: ae43901d51709075e10da86ac1ffd4ea55bbf0aeb2a122f5bc787f2c387c8eb5
          B/clauses/window-03/raw.json: ade098eecf3af3e0dd0cfda3eba6e357b4307a0efb3aadbb93453a37ed8c8f77
          B/clauses/window-03/prompt.txt: f3ebd14700cc8c5060ca6edde62c35f9aaf9cc293e6e934b9f371c472e1214ae
          B/clauses/window-03/meta.json: 9bb268613a20403624684b27174d66ff64c75e81ce09e320510b8c8f7fb0fb9e
          B/clauses/window-04/raw.json: 91b1b8cbec9721116841c142c555c9f0e27f163b01c8577f2994ea0a95bc961c
          B/clauses/window-04/prompt.txt: 48061db2d32f824e28d38b35bdb22dca802e6eb7bc9dcee19e18e12328a835cd
          B/clauses/window-04/meta.json: a20f46d71c7b91db58bd3aa9b9166121e5dc8532d1834007c6affffc0ac8a87e
          B/clauses/window-05/raw.json: 4267ef32dcd47cecd480df5df9f27539e182a6234f5b74ff0e5f0bfa3ea26f3f
          B/clauses/window-05/prompt.txt: e512beb45931f6ea695361c9c07ef95ba0b2c165540aa651d30ee0e995e28e3e
          B/clauses/window-05/meta.json: fc277f44d90bb4e8b4e8654685e4c040ee5c2d046a02860bae07fcc12b8bde88
          B/clauses/window-02/raw.json: 79c2c938d74f2d40bdcdd8e0cad45d15f6fec09944e1eac6a2d1e4b034c01158
          B/clauses/window-02/prompt.txt: 79519d404926eb73ba82fbd05bb352f2ad4256b15feb2f349f2c8cf3012552fb
          B/clauses/window-02/meta.json: 1c073fbe843b169210869f8408ae7e39cc166e5058b6fe14e092eda40ea0d8a5
          B/clauses/window-12/raw.json: ca5dcbca76437ff4b2a820caf6247b4f8dbcd363fdb489941f77920a470fc742
          B/clauses/window-12/prompt.txt: 182954004d179ca9355c66012fdbf2e955e3d18751b2a840fd0d8b07b03c9f81
          B/clauses/window-12/meta.json: a579153b93fbe69bc509550bde3866ceb6ca6a36f62967d7ee44e1d145d8c65e
          B/clauses/window-09/raw.json: d136793833ea893ca63edcb6a5329b9c032c27ab0d110724568efda7e5916d48
          B/clauses/window-09/prompt.txt: 9dc4ab65efa54b689ce5bfe1d48e2fb42c32176cf7889a6af99593d3d7339d7f
          B/clauses/window-09/meta.json: 4c1f819e12065aeeaae3909ababdf745a54505ab360fe9a03ccac64191577def
          B/clauses/window-07/raw.json: b5531e1b3861e298ce1f7beedffdeeb7629412c738511a54643af81926d0b506
          B/clauses/window-07/prompt.txt: d553e7a64945a1f7371e4193ce4e71becfe5576b91e0a2e3c2c5ac418654e52f
          B/clauses/window-07/meta.json: 6a79cba4e99e1ef293a2726458407a1355ce7166140fb87fd3526921a1b3cbce
          B/clauses/window-01/raw.json: 2127cd9e72bd63606d81319ae8765e703014b4573dbd4e8ecfa24b82323fe68c
          B/clauses/window-01/prompt.txt: 84b3e222547768364f39605a8c7290111dd2c1ef8a664f4315bc3bc8aa08a303
          B/clauses/window-01/meta.json: 152c18a59bc5e715066089b244762faa9e9c9f42d61ea0ae2e5e0d06f28e9303
          B/clauses/window-06/raw.json: b5630622b11dbe858405de270fab1a9e198b382d2b8499a4626355c16026d01c
          B/clauses/window-06/prompt.txt: f3fa1828d9bc777db524c65657a207c39080908e9bca29b5837d0ec8e802728b
          B/clauses/window-06/meta.json: 1da574b858d1b407c2e9a3455b2425c70e5e870b2d6cf68578f10d13ade60e26
          B/clauses/window-08/raw.json: 81367da46ded7ff27f1cde7848eb08f5846eac3425cd213636797415db3a3781
          B/clauses/window-08/prompt.txt: 650bd9c37008f9af4d8c3969857cd4a2d2880e9273bb919b85321925c69bdf90
          B/clauses/window-08/meta.json: 0b4ed316c51528db3c1db6c1c4b5e4396f4141da327da661dc61c8b475fe1817
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
        pdf_sha256: dbbf5db9f646e5ed67190025aea75aff5c20f899e9304ffa7b67f2d7641a12b8
        source_review: _compare/relationships-2026-11-16/review-current/Karnath2018
        source_status_sha256: 06714d9285acb35e66412583a1166bdee53028f03385fee771ec530bffc2b5f2
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
      packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
    proposal:
      id: R009
      exposure:
        text: patterns of damage (multivariate)
      outcome:
        text: spatial neglect
      analysis_label: Multivariate vs single voxel prediction (spatial neglect)
      relation: model_comparison
      evidence_ids:
      - P7-S2-C3
      qualifier_ids:
      - P7-S1-C15
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: dbbf5db9f646e5ed67190025aea75aff5c20f899e9304ffa7b67f2d7641a12b8
        source_review: _compare/relationships-2026-11-16/review-current/Karnath2018
        source_status_sha256: 06714d9285acb35e66412583a1166bdee53028f03385fee771ec530bffc2b5f2
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    audit:
      original_audit:
        coverage_issues:
        - Result passage disposed without unit P6-S2-C7
        - Accounting without a linked unit P7-S4-C6
        - Accounting without a linked unit P7-S4-C7
        - Accounting without a linked unit P7-S4-C8
        - Accounting without a linked unit P7-S4-C9
        - Unaccounted source passage P7-S4-C6
        - Unaccounted source passage P7-S4-C7
        - Unaccounted source passage P7-S4-C9
        - Unaccounted source passage P7-S4-C8
        unattached_null_or_qualifier_ids:
        - P2-S4-C11
        suppressed_nonrepresented_units: 5
        default_disposition_count_requires_completeness_check: 279
        unselected_timing_passages: []
        personal_effect_slots_without_result_classification: []
        held_frame_selections:
        - slot: dependent_variable_statement
          source_id: P7-S2-C6
          reason: Requires a Methods outcome definition; model selection retained for inspection only
        - slot: validation
          source_id: P3-S2-C15
          reason: No validation-design cue; inspect the source rather than inferring a design
        - slot: validation
          source_id: P3-S2-C16
          reason: No validation-design cue; inspect the source rather than inferring a design
        - slot: validation
          source_id: P6-S4-C3
          reason: No validation-design cue; inspect the source rather than inferring a design
        - slot: validation
          source_id: P7-S1-C5
          reason: No validation-design cue; inspect the source rather than inferring a design
        - slot: validation
          source_id: P7-S2-C7
          reason: No validation-design cue; inspect the source rather than inferring a design
        - slot: imaging_provenance
          source_ids:
          - P2-S2-C5
          - P4-S1-C3
          - P4-S1-C4
          - P4-S1-C14
          - P5-S1-C4
          - P5-S1-C7
          - P5-S2-C8
          - P5-S2-C12
          - P5-S2-C13
          - P5-S4-C9
          - P6-S1-C6
          - P6-S2-C9
          - P6-S4-C5
          - P7-S2-C7
          reason: Runaway selection (>8 passages); entire slot requires source review
        - slot: analysis_restrictions
          source_ids:
          - P3-S1-C12
          - P3-S3-C6
          - P3-S3-C7
          - P6-S1-C8
          - P6-S1-C9
          - P6-S2-C3
          - P6-S2-C4
          - P6-S2-C5
          - P7-S1-C12
          reason: Runaway selection (>8 passages); entire slot requires source review
        - slot: limitations
          source_ids:
          - P1-S1-C5
          - P1-S2-C4
          - P1-S2-C5
          - P2-S1-C10
          - P2-S3-C8
          - P2-S3-C10
          - P2-S3-C12
          - P2-S3-C14
          - P3-S1-C13
          - P3-S2-C8
          - P3-S2-C9
          - P3-S2-C10
          - P3-S2-C11
          - P3-S2-C12
          - P3-S2-C13
          - P3-S3-C10
          - P3-S3-C11
          - P3-S4-C10
          - P4-S3-C3
          - P4-S3-C8
          - P4-S3-C9
          - P4-S3-C10
          - P4-S3-C11
          - P4-S3-C12
          - P4-S3-C13
          - P5-S4-C5
          - P5-S4-C6
          - P6-S1-C7
          - P6-S1-C10
          - P6-S1-C11
          - P6-S2-C2
          - P6-S2-C3
          - P6-S2-C4
          - P6-S2-C5
          - P6-S3-C2
          - P6-S3-C7
          - P7-S3-C4
          - P7-S3-C5
          - P7-S3-C7
          - P7-S3-C10
          - P7-S3-C11
          - P7-S3-C12
          - P8-S1-C3
          - P8-S1-C4
          - P8-S1-C5
          - P8-S1-C6
          - P8-S1-C7
          - P8-S1-C9
          - P8-S1-C10
          - P8-S1-C11
          reason: Runaway selection (>8 passages); entire slot requires source review
        empty_frame_slots_require_confirmation:
        - imaging_provenance
        - analysis_restrictions
        - limitations
        - personal_factors
        - tested_personal_effects
        - explicitly_not_adjusted
        - descriptive_personal_factors
        unclassified_extraction_ids: []
        table_review_required: []
        unlinked_tables: []
        source_anomalies: []
        visual_review_required:
          scope: All main-paper figures and table crops
          note: Automatic crops and matching transcriptions do not certify visual completeness. Figures are not automatically interpreted.
          caption_candidate_units:
          - P3-S4
          - P4-S3
          - P4-S4
          - P5-S1
          - P5-S4
          - P6-S1
          - P6-S3
          - P6-S4
          - P7-S1
          - P7-S4
        approval: Not performed. Structural checks and model selections do not establish semantic correctness.
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: dbbf5db9f646e5ed67190025aea75aff5c20f899e9304ffa7b67f2d7641a12b8
        source_review: _compare/relationships-2026-11-16/review-current/Karnath2018
        source_status_sha256: 06714d9285acb35e66412583a1166bdee53028f03385fee771ec530bffc2b5f2
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
      coverage:
      - source_id: P2-S4-C7
        disposition: represented
        result_indexes:
        - 0
        reason: Establishes that permutation thresholding controls familywise error and shows Bonferroni is overly conservative.
      - source_id: P2-S4-C8
        disposition: represented
        result_indexes:
        - 1
        reason: Describes the primary weakness (slowness) of permutation thresholding.
      - source_id: P2-S4-C10
        disposition: background_or_descriptive
        result_indexes: []
        reason: Discusses the conservative nature of the approach and its utility in large studies.
      - source_id: P2-S4-C11
        disposition: background_or_descriptive
        result_indexes: []
        reason: Discusses the limitation of leveraging only extreme statistical scores.
      - source_id: P4-S4-C7
        disposition: background_or_descriptive
        result_indexes: []
        reason: Figure caption describing the orientation of collateral damage.
      - source_id: P6-S2-C7
        disposition: represented
        result_indexes:
        - 6
        reason: Links hub injury to widespread cognitive deficits.
      - source_id: P6-S3-C9
        disposition: background_or_descriptive
        result_indexes: []
        reason: Introduces the concept of multivariate lesion analysis.
      - source_id: P6-S3-C10
        disposition: background_or_descriptive
        result_indexes: []
        reason: Illustrates a hypothetical example of multivariate vs univariate performance.
      - source_id: P6-S3-C11
        disposition: background_or_descriptive
        result_indexes: []
        reason: Illustrates a hypothetical multivariate solution.
      - source_id: P7-S1-C3
        disposition: background_or_descriptive
        result_indexes: []
        reason: Introduces the example of spatial neglect prediction.
      - source_id: P7-S4-C6
        disposition: background_or_descriptive
        result_indexes: []
        reason: Figure caption describing univariate failure in spatial neglect classification.
      - source_id: P7-S4-C8
        disposition: background_or_descriptive
        result_indexes: []
        reason: Figure caption describing multivariate success in spatial neglect classification.
      - source_id: P7-S4-C9
        disposition: background_or_descriptive
        result_indexes: []
        reason: Figure caption stating the hyperplane accurately classifies most individuals.
      - source_id: P3-S3-C11
        disposition: represented
        result_indexes:
        - 2
        reason: States that combined correction factors reduced misplacement markedly.
      - source_id: P3-S3-C10
        disposition: represented
        result_indexes:
        - 3
        reason: Reports that misplacement bias is smaller with a specific lesion affection criterion.
      - source_id: P4-S2-C13
        disposition: represented
        result_indexes:
        - 4
        reason: States rsfMRI network disruptions are predictive of outcomes.
      - source_id: P4-S3-C2
        disposition: represented
        result_indexes:
        - 5
        reason: States rsfMRI and structural lesion information provide synergistic benefits.
      - source_id: P6-S2-C12
        disposition: represented
        result_indexes:
        - 7
        reason: Reports successful prediction of deficits using connection metrics.
      - source_id: P7-S2-C3
        disposition: represented
        result_indexes:
        - 8
        reason: Reports patterns of damage are more predictive than single voxels for spatial neglect.
      - source_id: P7-S2-C4
        disposition: represented
        result_indexes:
        - 9
        reason: Reports multiple brain regions provide more predictive information than single regions.
      - source_id: P7-S2-C8
        disposition: represented
        result_indexes:
        - 10
        reason: Reports multivariate mapping is superior to mass-univariate in brain networks.
      - source_id: P8-S1-C2
        disposition: represented
        result_indexes:
        - 11
        reason: Reports multivariate sparse canonical correlations perform better than mass-univariate non-parametric mapping.
      unresolved_coverage:
      - source_id: P3-S3-C11
        disposition: unresolved
        reason: Coverage source was not requested or was repeated; not accepted as coverage
      - source_id: P3-S3-C10
        disposition: unresolved
        reason: Coverage source was not requested or was repeated; not accepted as coverage
      - source_id: P4-S2-C13
        disposition: unresolved
        reason: Coverage source was not requested or was repeated; not accepted as coverage
      - source_id: P4-S3-C2
        disposition: unresolved
        reason: Coverage source was not requested or was repeated; not accepted as coverage
      - source_id: P6-S2-C12
        disposition: unresolved
        reason: Coverage source was not requested or was repeated; not accepted as coverage
      - source_id: P7-S2-C3
        disposition: unresolved
        reason: Coverage source was not requested or was repeated; not accepted as coverage
      - source_id: P7-S2-C4
        disposition: unresolved
        reason: Coverage source was not requested or was repeated; not accepted as coverage
      - source_id: P7-S2-C8
        disposition: unresolved
        reason: Coverage source was not requested or was repeated; not accepted as coverage
      - source_id: P8-S1-C2
        disposition: unresolved
        reason: Coverage source was not requested or was repeated; not accepted as coverage
      pending_source_ids:
      - P2-S4-C10
      - P2-S4-C11
      - P4-S4-C7
      - P6-S3-C9
      - P6-S3-C10
      - P6-S3-C11
      - P7-S1-C3
      - P7-S4-C6
      - P7-S4-C8
      - P7-S4-C9
      pending_policy: Every result passage without direct candidate evidence remains pending, including model-labelled background and restatements; those labels never certify completeness.
      tables_requiring_review: []
      paper_complete: false
      approved: false
      policy: New candidates require independent source checks; coverage dispositions are model suggestions. No original outputs changed.
    study_frame:
      slots:
        analysed_sample:
        - P3-S2-C15
        - P4-S4-C4
        - P5-S3-C9
        - P6-S1-C4
        - P7-S2-C7
        - P7-S2-C9
        recruited_sample:
        - P2-S3-C3
        - P4-S4-C4
        - P5-S3-C9
        - P6-S1-C4
        - P7-S2-C3
        - P7-S2-C9
        eligibility:
        - P2-S3-C3
        imaging_provenance: []
        imaging_timing:
        - P4-S1-C11
        - P7-S2-C12
        outcome_timing:
        - P7-S2-C12
        outcome_definition:
        - P7-S1-C10
        - P7-S2-C5
        validation:
        - P7-S1-C8
        analysis_restrictions: []
        dependent_variable_statement:
        - P6-S2-C12
        - P6-S2-C15
        - P7-S1-C11
        - P7-S2-C5
        limitations: []
        personal_factors: []
        tested_personal_effects: []
        adjustment_roles:
        - P3-S1-C12
        - P3-S3-C5
        - P3-S3-C6
        - P3-S3-C7
        - P3-S4-C10
        - P7-S3-C8
        explicitly_not_adjusted: []
        descriptive_personal_factors: []
      outcome_type: both_reported
      imaging_vs_outcome: mixed
      validation_type: internal_cross_validation
      held_selections:
      - slot: dependent_variable_statement
        source_id: P7-S2-C6
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: validation
        source_id: P3-S2-C15
        reason: No validation-design cue; inspect the source rather than inferring a design
      - slot: validation
        source_id: P3-S2-C16
        reason: No validation-design cue; inspect the source rather than inferring a design
      - slot: validation
        source_id: P6-S4-C3
        reason: No validation-design cue; inspect the source rather than inferring a design
      - slot: validation
        source_id: P7-S1-C5
        reason: No validation-design cue; inspect the source rather than inferring a design
      - slot: validation
        source_id: P7-S2-C7
        reason: No validation-design cue; inspect the source rather than inferring a design
      - slot: imaging_provenance
        source_ids:
        - P2-S2-C5
        - P4-S1-C3
        - P4-S1-C4
        - P4-S1-C14
        - P5-S1-C4
        - P5-S1-C7
        - P5-S2-C8
        - P5-S2-C12
        - P5-S2-C13
        - P5-S4-C9
        - P6-S1-C6
        - P6-S2-C9
        - P6-S4-C5
        - P7-S2-C7
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: analysis_restrictions
        source_ids:
        - P3-S1-C12
        - P3-S3-C6
        - P3-S3-C7
        - P6-S1-C8
        - P6-S1-C9
        - P6-S2-C3
        - P6-S2-C4
        - P6-S2-C5
        - P7-S1-C12
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: limitations
        source_ids:
        - P1-S1-C5
        - P1-S2-C4
        - P1-S2-C5
        - P2-S1-C10
        - P2-S3-C8
        - P2-S3-C10
        - P2-S3-C12
        - P2-S3-C14
        - P3-S1-C13
        - P3-S2-C8
        - P3-S2-C9
        - P3-S2-C10
        - P3-S2-C11
        - P3-S2-C12
        - P3-S2-C13
        - P3-S3-C10
        - P3-S3-C11
        - P3-S4-C10
        - P4-S3-C3
        - P4-S3-C8
        - P4-S3-C9
        - P4-S3-C10
        - P4-S3-C11
        - P4-S3-C12
        - P4-S3-C13
        - P5-S4-C5
        - P5-S4-C6
        - P6-S1-C7
        - P6-S1-C10
        - P6-S1-C11
        - P6-S2-C2
        - P6-S2-C3
        - P6-S2-C4
        - P6-S2-C5
        - P6-S3-C2
        - P6-S3-C7
        - P7-S3-C4
        - P7-S3-C5
        - P7-S3-C7
        - P7-S3-C10
        - P7-S3-C11
        - P7-S3-C12
        - P8-S1-C3
        - P8-S1-C4
        - P8-S1-C5
        - P8-S1-C6
        - P8-S1-C7
        - P8-S1-C9
        - P8-S1-C10
        - P8-S1-C11
        reason: Runaway selection (>8 passages); entire slot requires source review
      policy: All slots and enums remain unverified. Held selections are not evidence of absence. Original response is preserved in frame/raw.json.
    approved: false
    source_check:
      profile: core
      scope: Independent model text review of core meaning; not human approval or complete PDF verification
      binding:
        profile: core
        version: core-source-check-v3
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        checker_model: qwen3.8:27b
        checker_digest: 47951e4a666180bc2aedfc93c169472f2de783696fe196efbf063f5730ecf163
        host: http://localhost:11434
        pdf_sha256: dbbf5db9f646e5ed67190025aea75aff5c20f899e9304ffa7b67f2d7641a12b8
        review_sha256: 1fbc9305ad0a2f592e05e317766596032c7b6e691efb6c3ba2125c242408e7f0
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
        - P7-S2-C3
        source_result: In a large sample of right hemispheric stroke patients, patterns of damage were found to be more predictive of spatial neglect than the best-performing single voxel.
        result_status: model_comparison
        patient_measurement: template_lesion_overlap
        checks:
          analysis_identity:
            answer: fits
            reason: The source (P7-S2-C3) explicitly describes a comparison where multivariate patterns of damage were found to be more predictive than the best-performing single voxel. This matches the proposed 'model_comparison' status and the specific analysis label.
            source_ids:
            - P7-S2-C3
            - P7-S2-C4
          direction:
            answer: fits
            reason: The source states that multivariate patterns were 'more predictive' than single voxels. The proposed claim 'patterns of damage were more predictive of spatial neglect than the best-performing single voxel' accurately preserves this direction of superiority.
            source_ids:
            - P7-S2-C3
          construct:
            answer: fits
            reason: The exposure is 'patterns of damage' (multivariate lesion status) and the outcome is 'spatial neglect'. The source confirms this relationship in the context of right hemispheric stroke patients. The patient measurement is correctly identified as template_lesion_overlap (lesion status overlaid on templates/voxels), not patient_diffusion, as the analysis relies on structural lesion maps rather than diffusion tractography in the patients themselves.
            source_ids:
            - P7-S2-C3
            - P7-S1-C14
          qualifications:
            answer: fits
            reason: The proposed draft includes the qualification 'compared to the best-performing single voxel', which is the core constraint of the finding in P7-S2-C3. It also notes the population (right hemispheric stroke) and the context (narrative review of Smith et al., 2013).
            source_ids:
            - P7-S2-C3
            - P7-S1-C15
          missing_material_caveat:
            answer: fits
            reason: The draft correctly identifies that this is a finding reported within a narrative review of a prior study (Smith et al., 2013), which is a material caveat regarding the evidence quality and origin. No other material caveats from the source passages appear to be omitted that would change the interpretation of this specific comparison.
            source_ids:
            - P7-S1-C14
            - P7-S2-C3
        optional_pending:
        - Specific statistical metrics (e.g., AUC, accuracy) for the multivariate vs single voxel comparison are not transcribed.
        - Specific sample size N for the Smith et al. (2013) study is not transcribed.
        verdict: draft
        reason: All five core checks fit the source.
        material_issues: []
      pending_details:
      - Detailed statistics, atlas/reference-space and structured confounder metadata not transcribed.
      - Recovery phase is not classified; use the reported timing words.
      - Evidence-strength rating is a conservative draft placeholder pending human review.
      - Specific statistical metrics (e.g., AUC, accuracy) for the multivariate vs single voxel comparison are not transcribed.
      - Specific sample size N for the Smith et al. (2013) study is not transcribed.
      normalizations: []
      analysis_identity:
        id: R009
        exposure:
          text: patterns of damage (multivariate)
        outcome:
          text: spatial neglect
        analysis_label: Multivariate vs single voxel prediction (spatial neglect)
        relation: model_comparison
        evidence_ids:
        - P7-S2-C3
        qualifier_ids:
        - P7-S1-C15
        context_ids: []
        table_ids: []
        approved: false
        status: requires_source_review
        flags:
        - new_model_candidate_not_verified
        candidate_discovery:
          model: gemma4:31b
          model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
          pdf_sha256: dbbf5db9f646e5ed67190025aea75aff5c20f899e9304ffa7b67f2d7641a12b8
          source_review: _compare/relationships-2026-11-16/review-current/Karnath2018
          source_status_sha256: 06714d9285acb35e66412583a1166bdee53028f03385fee771ec530bffc2b5f2
          code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
          version: candidate-inventory-v1
      paper_complete: false
      visual_prose_readings: {}
      remaining:
      - Human PDF review and approval
      - Pending metadata enrichment
      - Main Results, figures and tables completeness check
  original_publication_entry:
    id: multivariate_damage_pattern_neglect
    name: multivariate damage pattern predictor
    kind: predictor
    findings:
    - id: f1
      target: spatial_neglect
      target_kind: impairment
      claim: patterns of damage were more predictive of spatial neglect than the best-performing single voxel
      direction: likely
      relationship: correlational
      method: MVPA
      sample:
        n: not_reported
        population: right hemispheric stroke patients
        phase: not_reported
        time_post_onset: not_transcribed
      statistics:
        threshold: not_transcribed
      confounders_controlled: []
      confounders_not_controlled: []
      region_definition:
        kind: not_reported
        description: Not transcribed; see source passages and claim.
      author_limitations:
      - finding is reported within a narrative review of a prior study (Smith et al., 2013)
      evidence_quality: cohort
      strength: weak
      notes: 'Exposure measurement: multivariate patterns of structural damage (lesion status of multiple voxels) in the brain. compared to the best-performing single voxel. Additional metadata has not been transcribed; review the pending-field flags before approval.'
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
        - not_transcribed:sample.n
        - proposed_concept:spatial_neglect
      citation: '@Karnath2018'
      source_passages:
      - section: Original source P7-S2-C3
        page: 7
        quote: 'In a large sample of

          right hemispheric stroke patients, they found patterns of damage more

          predictive of spatial neglect than the best-performing single voxel.'
        supports: claim
      - section: Original source P7-S1-C15
        page: 7
        quote: 'In a large sample of

          '
        supports: sample
      - section: Original source P6-S3-C8
        page: 6
        quote: 'Multivariate lesion analysis with machine learning algorithms

          Unlike VLBM''s mass-univariate testing approach, machine learning

          based lesion analysis offers a multivariate approach to lesion analysis.'
        supports: method
    predictor_type: imaging_metric
    short_definition: multivariate patterns of structural damage (lesion status of multiple voxels) in the brain
    assessment: []
    schema_version: '2.8'
    status: draft
    created_by: agent:relationship-converter
    created_on: '2026-11-24'
    relationship_review:
      paper: Karnath2018
      proposal_id: R009
      review_status_sha256: 1fbc9305ad0a2f592e05e317766596032c7b6e691efb6c3ba2125c242408e7f0
      review_binding:
        version: candidate-inventory-v1
        input_hashes:
          pdf: dbbf5db9f646e5ed67190025aea75aff5c20f899e9304ffa7b67f2d7641a12b8
        original_review_binding:
          version: relationship-review-v4
          input_hashes:
            pdf: dbbf5db9f646e5ed67190025aea75aff5c20f899e9304ffa7b67f2d7641a12b8
            A/passages.json: a7ef357c214c37c4e6ff921b063b689faf618f39d8e4f410a5aad6fa98313b1a
            A/raw.json: d1fefd9177998f06722a4998458a81647ec6a9192c427ff55adb89f8e56ea440
            A/source-units.json: 0b37ebf3adee7a5434171808b481506031269d29260804822cbdb49284bfb3b6
            A/full-source-units.json: 8c1ad66527454a0ed883d0bf8d0d94981ea1a915fd599fd36cce01954d7e296a
            A/meta.json: 46f48df6e3c5ae4ea7b343cef1ce3461a5167b9b3faa63c1310f6b213176be5a
            A/table-images/manifest.json: ab5b9fa5e5738ee57af1f7a67291b70cf6c39bc94a18b73ae17551a5ed764f87
            A/clauses/window-11/raw.json: ba65b808fc7ca28970f57805b899a697ae3f1094f437ba5ec775e2b48e2d5515
            A/clauses/window-11/prompt.txt: 48823ef4591a16826e8d78c7492feed9a8fe3a62b067746f72d2c47ee5f61072
            A/clauses/window-11/meta.json: 31b798098edb5b8d216cd7147d08682cc097a59178cb38e1fc26b6a8a8a0a4ec
            A/clauses/window-10/raw.json: 2b53690fe3728ba24db45d895a8bd6f5d6a0688b714141bce131553d0fd034a8
            A/clauses/window-10/prompt.txt: e7930c5abb3e94e850630bdbf0e9b3343d5666aa4a772b2f7a57ffd636f51d3f
            A/clauses/window-10/meta.json: 8f0ff0ca98f3b58156b13bd7fb9df0db2568a5bda5189b7ba36420b12480b5a7
            A/clauses/window-03/raw.json: bff13fdd5409741a93a93772a55ec8b99da50286c3d8c8fdc3ded40efe6b63dc
            A/clauses/window-03/prompt.txt: f3ebd14700cc8c5060ca6edde62c35f9aaf9cc293e6e934b9f371c472e1214ae
            A/clauses/window-03/meta.json: f3449c1b553a10a9009c72490d6d0f9a342a07cafb305090e2d000ac7ed3a3dc
            A/clauses/window-04/raw.json: 6c717bdbf7d195ea5a56e4fefbef67b04cfaf385f045c076d9195bea43ef19fe
            A/clauses/window-04/prompt.txt: 48061db2d32f824e28d38b35bdb22dca802e6eb7bc9dcee19e18e12328a835cd
            A/clauses/window-04/meta.json: 1dff8a775128debccaa031eb09ec1db4e4d472a1e7890da3669744af7c585136
            A/clauses/window-05/raw.json: e9697c35ba6f1c25bdfd2dec916cd135f774ea8731e7094e4de6ac8f840aad60
            A/clauses/window-05/prompt.txt: e512beb45931f6ea695361c9c07ef95ba0b2c165540aa651d30ee0e995e28e3e
            A/clauses/window-05/meta.json: 732c95f9a2057dec30489680541b52c13297850487f0fceaa3d641562f782963
            A/clauses/window-02/raw.json: 1f0af08f96ee227fb877d3c302cf9d55f17a5b01555fbbe122337ffd95316061
            A/clauses/window-02/prompt.txt: 79519d404926eb73ba82fbd05bb352f2ad4256b15feb2f349f2c8cf3012552fb
            A/clauses/window-02/meta.json: d45d56ca432520154ce81c3e82f1c6d68e0d627bf29cad10b75c6587207a6c84
            A/clauses/window-12/raw.json: 9418fa57efc0507f3a75bd89171c423584277403e7a8f6ce49c780ca8bb5f599
            A/clauses/window-12/prompt.txt: 182954004d179ca9355c66012fdbf2e955e3d18751b2a840fd0d8b07b03c9f81
            A/clauses/window-12/meta.json: a68bdac99b111268035530710d2449e99e6d4dcb174f6922625d233ac4b9f256
            A/clauses/window-09/raw.json: 1b53295af2532f5e21ecc20c1e81ee62d83df853576e0d77f33886f9eadd1fcc
            A/clauses/window-09/prompt.txt: 9dc4ab65efa54b689ce5bfe1d48e2fb42c32176cf7889a6af99593d3d7339d7f
            A/clauses/window-09/meta.json: 7ae8a464f9703d30957c061e098e33702a6fc916e88f0b7c283b862184562c98
            A/clauses/window-07/raw.json: e48b06a514299b149dc19af4f961a8f0f3eb3be7dcca622fd77994c15ec7506f
            A/clauses/window-07/prompt.txt: d553e7a64945a1f7371e4193ce4e71becfe5576b91e0a2e3c2c5ac418654e52f
            A/clauses/window-07/meta.json: 78dc81a52245b40ab1793c22d96409b2ac0ecc52073c4585aa2bd1af7e462d82
            A/clauses/window-01/raw.json: 34e88a9bac868638e56a251639be5e82d22877e2257a01a0fe4075829e33ff87
            A/clauses/window-01/prompt.txt: 84b3e222547768364f39605a8c7290111dd2c1ef8a664f4315bc3bc8aa08a303
            A/clauses/window-01/meta.json: b8fe90b54847f0e062bf3337cb38ec10ff16c782856425a5c9b8e166d783091d
            A/clauses/window-06/raw.json: e02444d67355a8630b2b82b0f335366c03294b447ecde47f362885597c400ada
            A/clauses/window-06/prompt.txt: f3fa1828d9bc777db524c65657a207c39080908e9bca29b5837d0ec8e802728b
            A/clauses/window-06/meta.json: 6b553fb15def952220ab7e03c50538d9d477a12726cb45f2444fa5a9599c53b7
            A/clauses/window-08/raw.json: d65615e9a875d79e96cf839205c6152385081e793e651b4b2855a28591e701bb
            A/clauses/window-08/prompt.txt: 650bd9c37008f9af4d8c3969857cd4a2d2880e9273bb919b85321925c69bdf90
            A/clauses/window-08/meta.json: f3c64559ddac1aef34956120e850baa712292a787dc276571fa7c4f6c9d8b9b6
            B/passages.json: a7ef357c214c37c4e6ff921b063b689faf618f39d8e4f410a5aad6fa98313b1a
            B/raw.json: c4068a9f59ca03fbbc52bc1d099d3af3f077058a829dd45cd175d3a5f7ee6a6c
            B/source-units.json: 0b37ebf3adee7a5434171808b481506031269d29260804822cbdb49284bfb3b6
            B/full-source-units.json: 8c1ad66527454a0ed883d0bf8d0d94981ea1a915fd599fd36cce01954d7e296a
            B/meta.json: bb81b1aa338c269abbc062c2de2137dcdda694645ac07b88ef07270b8a0b21a1
            B/table-images/manifest.json: ab5b9fa5e5738ee57af1f7a67291b70cf6c39bc94a18b73ae17551a5ed764f87
            B/clauses/window-11/raw.json: b3fd779b587afa6064074782532ebe0dc8d18c95a7ae5e4a3af36f72405934d5
            B/clauses/window-11/prompt.txt: 48823ef4591a16826e8d78c7492feed9a8fe3a62b067746f72d2c47ee5f61072
            B/clauses/window-11/meta.json: 5f4b07c9d7d5fe9b23e97eb83ea7b42859d87ee227b6a425a81203d793e4f995
            B/clauses/window-10/raw.json: 2fe16ff4e81eb16b2b318cb44271896500e3efa9f2441d18567c1ed2c45b7cc0
            B/clauses/window-10/prompt.txt: e7930c5abb3e94e850630bdbf0e9b3343d5666aa4a772b2f7a57ffd636f51d3f
            B/clauses/window-10/meta.json: ae43901d51709075e10da86ac1ffd4ea55bbf0aeb2a122f5bc787f2c387c8eb5
            B/clauses/window-03/raw.json: ade098eecf3af3e0dd0cfda3eba6e357b4307a0efb3aadbb93453a37ed8c8f77
            B/clauses/window-03/prompt.txt: f3ebd14700cc8c5060ca6edde62c35f9aaf9cc293e6e934b9f371c472e1214ae
            B/clauses/window-03/meta.json: 9bb268613a20403624684b27174d66ff64c75e81ce09e320510b8c8f7fb0fb9e
            B/clauses/window-04/raw.json: 91b1b8cbec9721116841c142c555c9f0e27f163b01c8577f2994ea0a95bc961c
            B/clauses/window-04/prompt.txt: 48061db2d32f824e28d38b35bdb22dca802e6eb7bc9dcee19e18e12328a835cd
            B/clauses/window-04/meta.json: a20f46d71c7b91db58bd3aa9b9166121e5dc8532d1834007c6affffc0ac8a87e
            B/clauses/window-05/raw.json: 4267ef32dcd47cecd480df5df9f27539e182a6234f5b74ff0e5f0bfa3ea26f3f
            B/clauses/window-05/prompt.txt: e512beb45931f6ea695361c9c07ef95ba0b2c165540aa651d30ee0e995e28e3e
            B/clauses/window-05/meta.json: fc277f44d90bb4e8b4e8654685e4c040ee5c2d046a02860bae07fcc12b8bde88
            B/clauses/window-02/raw.json: 79c2c938d74f2d40bdcdd8e0cad45d15f6fec09944e1eac6a2d1e4b034c01158
            B/clauses/window-02/prompt.txt: 79519d404926eb73ba82fbd05bb352f2ad4256b15feb2f349f2c8cf3012552fb
            B/clauses/window-02/meta.json: 1c073fbe843b169210869f8408ae7e39cc166e5058b6fe14e092eda40ea0d8a5
            B/clauses/window-12/raw.json: ca5dcbca76437ff4b2a820caf6247b4f8dbcd363fdb489941f77920a470fc742
            B/clauses/window-12/prompt.txt: 182954004d179ca9355c66012fdbf2e955e3d18751b2a840fd0d8b07b03c9f81
            B/clauses/window-12/meta.json: a579153b93fbe69bc509550bde3866ceb6ca6a36f62967d7ee44e1d145d8c65e
            B/clauses/window-09/raw.json: d136793833ea893ca63edcb6a5329b9c032c27ab0d110724568efda7e5916d48
            B/clauses/window-09/prompt.txt: 9dc4ab65efa54b689ce5bfe1d48e2fb42c32176cf7889a6af99593d3d7339d7f
            B/clauses/window-09/meta.json: 4c1f819e12065aeeaae3909ababdf745a54505ab360fe9a03ccac64191577def
            B/clauses/window-07/raw.json: b5531e1b3861e298ce1f7beedffdeeb7629412c738511a54643af81926d0b506
            B/clauses/window-07/prompt.txt: d553e7a64945a1f7371e4193ce4e71becfe5576b91e0a2e3c2c5ac418654e52f
            B/clauses/window-07/meta.json: 6a79cba4e99e1ef293a2726458407a1355ce7166140fb87fd3526921a1b3cbce
            B/clauses/window-01/raw.json: 2127cd9e72bd63606d81319ae8765e703014b4573dbd4e8ecfa24b82323fe68c
            B/clauses/window-01/prompt.txt: 84b3e222547768364f39605a8c7290111dd2c1ef8a664f4315bc3bc8aa08a303
            B/clauses/window-01/meta.json: 152c18a59bc5e715066089b244762faa9e9c9f42d61ea0ae2e5e0d06f28e9303
            B/clauses/window-06/raw.json: b5630622b11dbe858405de270fab1a9e198b382d2b8499a4626355c16026d01c
            B/clauses/window-06/prompt.txt: f3fa1828d9bc777db524c65657a207c39080908e9bca29b5837d0ec8e802728b
            B/clauses/window-06/meta.json: 1da574b858d1b407c2e9a3455b2425c70e5e870b2d6cf68578f10d13ade60e26
            B/clauses/window-08/raw.json: 81367da46ded7ff27f1cde7848eb08f5846eac3425cd213636797415db3a3781
            B/clauses/window-08/prompt.txt: 650bd9c37008f9af4d8c3969857cd4a2d2880e9273bb919b85321925c69bdf90
            B/clauses/window-08/meta.json: 0b4ed316c51528db3c1db6c1c4b5e4396f4141da327da661dc61c8b475fe1817
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
          pdf_sha256: dbbf5db9f646e5ed67190025aea75aff5c20f899e9304ffa7b67f2d7641a12b8
          source_review: _compare/relationships-2026-11-16/review-current/Karnath2018
          source_status_sha256: 06714d9285acb35e66412583a1166bdee53028f03385fee771ec530bffc2b5f2
          code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
          version: candidate-inventory-v1
        packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      proposal:
        id: R009
        exposure:
          text: patterns of damage (multivariate)
        outcome:
          text: spatial neglect
        analysis_label: Multivariate vs single voxel prediction (spatial neglect)
        relation: model_comparison
        evidence_ids:
        - P7-S2-C3
        qualifier_ids:
        - P7-S1-C15
        context_ids: []
        table_ids: []
        approved: false
        status: requires_source_review
        flags:
        - new_model_candidate_not_verified
        candidate_discovery:
          model: gemma4:31b
          model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
          pdf_sha256: dbbf5db9f646e5ed67190025aea75aff5c20f899e9304ffa7b67f2d7641a12b8
          source_review: _compare/relationships-2026-11-16/review-current/Karnath2018
          source_status_sha256: 06714d9285acb35e66412583a1166bdee53028f03385fee771ec530bffc2b5f2
          code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
          version: candidate-inventory-v1
      audit:
        original_audit:
          coverage_issues:
          - Result passage disposed without unit P6-S2-C7
          - Accounting without a linked unit P7-S4-C6
          - Accounting without a linked unit P7-S4-C7
          - Accounting without a linked unit P7-S4-C8
          - Accounting without a linked unit P7-S4-C9
          - Unaccounted source passage P7-S4-C6
          - Unaccounted source passage P7-S4-C7
          - Unaccounted source passage P7-S4-C9
          - Unaccounted source passage P7-S4-C8
          unattached_null_or_qualifier_ids:
          - P2-S4-C11
          suppressed_nonrepresented_units: 5
          default_disposition_count_requires_completeness_check: 279
          unselected_timing_passages: []
          personal_effect_slots_without_result_classification: []
          held_frame_selections:
          - slot: dependent_variable_statement
            source_id: P7-S2-C6
            reason: Requires a Methods outcome definition; model selection retained for inspection only
          - slot: validation
            source_id: P3-S2-C15
            reason: No validation-design cue; inspect the source rather than inferring a design
          - slot: validation
            source_id: P3-S2-C16
            reason: No validation-design cue; inspect the source rather than inferring a design
          - slot: validation
            source_id: P6-S4-C3
            reason: No validation-design cue; inspect the source rather than inferring a design
          - slot: validation
            source_id: P7-S1-C5
            reason: No validation-design cue; inspect the source rather than inferring a design
          - slot: validation
            source_id: P7-S2-C7
            reason: No validation-design cue; inspect the source rather than inferring a design
          - slot: imaging_provenance
            source_ids:
            - P2-S2-C5
            - P4-S1-C3
            - P4-S1-C4
            - P4-S1-C14
            - P5-S1-C4
            - P5-S1-C7
            - P5-S2-C8
            - P5-S2-C12
            - P5-S2-C13
            - P5-S4-C9
            - P6-S1-C6
            - P6-S2-C9
            - P6-S4-C5
            - P7-S2-C7
            reason: Runaway selection (>8 passages); entire slot requires source review
          - slot: analysis_restrictions
            source_ids:
            - P3-S1-C12
            - P3-S3-C6
            - P3-S3-C7
            - P6-S1-C8
            - P6-S1-C9
            - P6-S2-C3
            - P6-S2-C4
            - P6-S2-C5
            - P7-S1-C12
            reason: Runaway selection (>8 passages); entire slot requires source review
          - slot: limitations
            source_ids:
            - P1-S1-C5
            - P1-S2-C4
            - P1-S2-C5
            - P2-S1-C10
            - P2-S3-C8
            - P2-S3-C10
            - P2-S3-C12
            - P2-S3-C14
            - P3-S1-C13
            - P3-S2-C8
            - P3-S2-C9
            - P3-S2-C10
            - P3-S2-C11
            - P3-S2-C12
            - P3-S2-C13
            - P3-S3-C10
            - P3-S3-C11
            - P3-S4-C10
            - P4-S3-C3
            - P4-S3-C8
            - P4-S3-C9
            - P4-S3-C10
            - P4-S3-C11
            - P4-S3-C12
            - P4-S3-C13
            - P5-S4-C5
            - P5-S4-C6
            - P6-S1-C7
            - P6-S1-C10
            - P6-S1-C11
            - P6-S2-C2
            - P6-S2-C3
            - P6-S2-C4
            - P6-S2-C5
            - P6-S3-C2
            - P6-S3-C7
            - P7-S3-C4
            - P7-S3-C5
            - P7-S3-C7
            - P7-S3-C10
            - P7-S3-C11
            - P7-S3-C12
            - P8-S1-C3
            - P8-S1-C4
            - P8-S1-C5
            - P8-S1-C6
            - P8-S1-C7
            - P8-S1-C9
            - P8-S1-C10
            - P8-S1-C11
            reason: Runaway selection (>8 passages); entire slot requires source review
          empty_frame_slots_require_confirmation:
          - imaging_provenance
          - analysis_restrictions
          - limitations
          - personal_factors
          - tested_personal_effects
          - explicitly_not_adjusted
          - descriptive_personal_factors
          unclassified_extraction_ids: []
          table_review_required: []
          unlinked_tables: []
          source_anomalies: []
          visual_review_required:
            scope: All main-paper figures and table crops
            note: Automatic crops and matching transcriptions do not certify visual completeness. Figures are not automatically interpreted.
            caption_candidate_units:
            - P3-S4
            - P4-S3
            - P4-S4
            - P5-S1
            - P5-S4
            - P6-S1
            - P6-S3
            - P6-S4
            - P7-S1
            - P7-S4
          approval: Not performed. Structural checks and model selections do not establish semantic correctness.
        candidate_discovery:
          model: gemma4:31b
          model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
          pdf_sha256: dbbf5db9f646e5ed67190025aea75aff5c20f899e9304ffa7b67f2d7641a12b8
          source_review: _compare/relationships-2026-11-16/review-current/Karnath2018
          source_status_sha256: 06714d9285acb35e66412583a1166bdee53028f03385fee771ec530bffc2b5f2
          code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
          version: candidate-inventory-v1
        coverage:
        - source_id: P2-S4-C7
          disposition: represented
          result_indexes:
          - 0
          reason: Establishes that permutation thresholding controls familywise error and shows Bonferroni is overly conservative.
        - source_id: P2-S4-C8
          disposition: represented
          result_indexes:
          - 1
          reason: Describes the primary weakness (slowness) of permutation thresholding.
        - source_id: P2-S4-C10
          disposition: background_or_descriptive
          result_indexes: []
          reason: Discusses the conservative nature of the approach and its utility in large studies.
        - source_id: P2-S4-C11
          disposition: background_or_descriptive
          result_indexes: []
          reason: Discusses the limitation of leveraging only extreme statistical scores.
        - source_id: P4-S4-C7
          disposition: background_or_descriptive
          result_indexes: []
          reason: Figure caption describing the orientation of collateral damage.
        - source_id: P6-S2-C7
          disposition: represented
          result_indexes:
          - 6
          reason: Links hub injury to widespread cognitive deficits.
        - source_id: P6-S3-C9
          disposition: background_or_descriptive
          result_indexes: []
          reason: Introduces the concept of multivariate lesion analysis.
        - source_id: P6-S3-C10
          disposition: background_or_descriptive
          result_indexes: []
          reason: Illustrates a hypothetical example of multivariate vs univariate performance.
        - source_id: P6-S3-C11
          disposition: background_or_descriptive
          result_indexes: []
          reason: Illustrates a hypothetical multivariate solution.
        - source_id: P7-S1-C3
          disposition: background_or_descriptive
          result_indexes: []
          reason: Introduces the example of spatial neglect prediction.
        - source_id: P7-S4-C6
          disposition: background_or_descriptive
          result_indexes: []
          reason: Figure caption describing univariate failure in spatial neglect classification.
        - source_id: P7-S4-C8
          disposition: background_or_descriptive
          result_indexes: []
          reason: Figure caption describing multivariate success in spatial neglect classification.
        - source_id: P7-S4-C9
          disposition: background_or_descriptive
          result_indexes: []
          reason: Figure caption stating the hyperplane accurately classifies most individuals.
        - source_id: P3-S3-C11
          disposition: represented
          result_indexes:
          - 2
          reason: States that combined correction factors reduced misplacement markedly.
        - source_id: P3-S3-C10
          disposition: represented
          result_indexes:
          - 3
          reason: Reports that misplacement bias is smaller with a specific lesion affection criterion.
        - source_id: P4-S2-C13
          disposition: represented
          result_indexes:
          - 4
          reason: States rsfMRI network disruptions are predictive of outcomes.
        - source_id: P4-S3-C2
          disposition: represented
          result_indexes:
          - 5
          reason: States rsfMRI and structural lesion information provide synergistic benefits.
        - source_id: P6-S2-C12
          disposition: represented
          result_indexes:
          - 7
          reason: Reports successful prediction of deficits using connection metrics.
        - source_id: P7-S2-C3
          disposition: represented
          result_indexes:
          - 8
          reason: Reports patterns of damage are more predictive than single voxels for spatial neglect.
        - source_id: P7-S2-C4
          disposition: represented
          result_indexes:
          - 9
          reason: Reports multiple brain regions provide more predictive information than single regions.
        - source_id: P7-S2-C8
          disposition: represented
          result_indexes:
          - 10
          reason: Reports multivariate mapping is superior to mass-univariate in brain networks.
        - source_id: P8-S1-C2
          disposition: represented
          result_indexes:
          - 11
          reason: Reports multivariate sparse canonical correlations perform better than mass-univariate non-parametric mapping.
        unresolved_coverage:
        - source_id: P3-S3-C11
          disposition: unresolved
          reason: Coverage source was not requested or was repeated; not accepted as coverage
        - source_id: P3-S3-C10
          disposition: unresolved
          reason: Coverage source was not requested or was repeated; not accepted as coverage
        - source_id: P4-S2-C13
          disposition: unresolved
          reason: Coverage source was not requested or was repeated; not accepted as coverage
        - source_id: P4-S3-C2
          disposition: unresolved
          reason: Coverage source was not requested or was repeated; not accepted as coverage
        - source_id: P6-S2-C12
          disposition: unresolved
          reason: Coverage source was not requested or was repeated; not accepted as coverage
        - source_id: P7-S2-C3
          disposition: unresolved
          reason: Coverage source was not requested or was repeated; not accepted as coverage
        - source_id: P7-S2-C4
          disposition: unresolved
          reason: Coverage source was not requested or was repeated; not accepted as coverage
        - source_id: P7-S2-C8
          disposition: unresolved
          reason: Coverage source was not requested or was repeated; not accepted as coverage
        - source_id: P8-S1-C2
          disposition: unresolved
          reason: Coverage source was not requested or was repeated; not accepted as coverage
        pending_source_ids:
        - P2-S4-C10
        - P2-S4-C11
        - P4-S4-C7
        - P6-S3-C9
        - P6-S3-C10
        - P6-S3-C11
        - P7-S1-C3
        - P7-S4-C6
        - P7-S4-C8
        - P7-S4-C9
        pending_policy: Every result passage without direct candidate evidence remains pending, including model-labelled background and restatements; those labels never certify completeness.
        tables_requiring_review: []
        paper_complete: false
        approved: false
        policy: New candidates require independent source checks; coverage dispositions are model suggestions. No original outputs changed.
      study_frame:
        slots:
          analysed_sample:
          - P3-S2-C15
          - P4-S4-C4
          - P5-S3-C9
          - P6-S1-C4
          - P7-S2-C7
          - P7-S2-C9
          recruited_sample:
          - P2-S3-C3
          - P4-S4-C4
          - P5-S3-C9
          - P6-S1-C4
          - P7-S2-C3
          - P7-S2-C9
          eligibility:
          - P2-S3-C3
          imaging_provenance: []
          imaging_timing:
          - P4-S1-C11
          - P7-S2-C12
          outcome_timing:
          - P7-S2-C12
          outcome_definition:
          - P7-S1-C10
          - P7-S2-C5
          validation:
          - P7-S1-C8
          analysis_restrictions: []
          dependent_variable_statement:
          - P6-S2-C12
          - P6-S2-C15
          - P7-S1-C11
          - P7-S2-C5
          limitations: []
          personal_factors: []
          tested_personal_effects: []
          adjustment_roles:
          - P3-S1-C12
          - P3-S3-C5
          - P3-S3-C6
          - P3-S3-C7
          - P3-S4-C10
          - P7-S3-C8
          explicitly_not_adjusted: []
          descriptive_personal_factors: []
        outcome_type: both_reported
        imaging_vs_outcome: mixed
        validation_type: internal_cross_validation
        held_selections:
        - slot: dependent_variable_statement
          source_id: P7-S2-C6
          reason: Requires a Methods outcome definition; model selection retained for inspection only
        - slot: validation
          source_id: P3-S2-C15
          reason: No validation-design cue; inspect the source rather than inferring a design
        - slot: validation
          source_id: P3-S2-C16
          reason: No validation-design cue; inspect the source rather than inferring a design
        - slot: validation
          source_id: P6-S4-C3
          reason: No validation-design cue; inspect the source rather than inferring a design
        - slot: validation
          source_id: P7-S1-C5
          reason: No validation-design cue; inspect the source rather than inferring a design
        - slot: validation
          source_id: P7-S2-C7
          reason: No validation-design cue; inspect the source rather than inferring a design
        - slot: imaging_provenance
          source_ids:
          - P2-S2-C5
          - P4-S1-C3
          - P4-S1-C4
          - P4-S1-C14
          - P5-S1-C4
          - P5-S1-C7
          - P5-S2-C8
          - P5-S2-C12
          - P5-S2-C13
          - P5-S4-C9
          - P6-S1-C6
          - P6-S2-C9
          - P6-S4-C5
          - P7-S2-C7
          reason: Runaway selection (>8 passages); entire slot requires source review
        - slot: analysis_restrictions
          source_ids:
          - P3-S1-C12
          - P3-S3-C6
          - P3-S3-C7
          - P6-S1-C8
          - P6-S1-C9
          - P6-S2-C3
          - P6-S2-C4
          - P6-S2-C5
          - P7-S1-C12
          reason: Runaway selection (>8 passages); entire slot requires source review
        - slot: limitations
          source_ids:
          - P1-S1-C5
          - P1-S2-C4
          - P1-S2-C5
          - P2-S1-C10
          - P2-S3-C8
          - P2-S3-C10
          - P2-S3-C12
          - P2-S3-C14
          - P3-S1-C13
          - P3-S2-C8
          - P3-S2-C9
          - P3-S2-C10
          - P3-S2-C11
          - P3-S2-C12
          - P3-S2-C13
          - P3-S3-C10
          - P3-S3-C11
          - P3-S4-C10
          - P4-S3-C3
          - P4-S3-C8
          - P4-S3-C9
          - P4-S3-C10
          - P4-S3-C11
          - P4-S3-C12
          - P4-S3-C13
          - P5-S4-C5
          - P5-S4-C6
          - P6-S1-C7
          - P6-S1-C10
          - P6-S1-C11
          - P6-S2-C2
          - P6-S2-C3
          - P6-S2-C4
          - P6-S2-C5
          - P6-S3-C2
          - P6-S3-C7
          - P7-S3-C4
          - P7-S3-C5
          - P7-S3-C7
          - P7-S3-C10
          - P7-S3-C11
          - P7-S3-C12
          - P8-S1-C3
          - P8-S1-C4
          - P8-S1-C5
          - P8-S1-C6
          - P8-S1-C7
          - P8-S1-C9
          - P8-S1-C10
          - P8-S1-C11
          reason: Runaway selection (>8 passages); entire slot requires source review
        policy: All slots and enums remain unverified. Held selections are not evidence of absence. Original response is preserved in frame/raw.json.
      approved: false
      source_check:
        profile: core
        scope: Independent model text review of core meaning; not human approval or complete PDF verification
        binding:
          profile: core
          version: core-source-check-v3
          model: gemma4:31b
          model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
          checker_model: qwen3.8:27b
          checker_digest: 47951e4a666180bc2aedfc93c169472f2de783696fe196efbf063f5730ecf163
          host: http://localhost:11434
          pdf_sha256: dbbf5db9f646e5ed67190025aea75aff5c20f899e9304ffa7b67f2d7641a12b8
          review_sha256: 1fbc9305ad0a2f592e05e317766596032c7b6e691efb6c3ba2125c242408e7f0
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
          - P7-S2-C3
          source_result: In a large sample of right hemispheric stroke patients, patterns of damage were found to be more predictive of spatial neglect than the best-performing single voxel.
          result_status: model_comparison
          patient_measurement: template_lesion_overlap
          checks:
            analysis_identity:
              answer: fits
              reason: The source (P7-S2-C3) explicitly describes a comparison where multivariate patterns of damage were found to be more predictive than the best-performing single voxel. This matches the proposed 'model_comparison' status and the specific analysis label.
              source_ids:
              - P7-S2-C3
              - P7-S2-C4
            direction:
              answer: fits
              reason: The source states that multivariate patterns were 'more predictive' than single voxels. The proposed claim 'patterns of damage were more predictive of spatial neglect than the best-performing single voxel' accurately preserves this direction of superiority.
              source_ids:
              - P7-S2-C3
            construct:
              answer: fits
              reason: The exposure is 'patterns of damage' (multivariate lesion status) and the outcome is 'spatial neglect'. The source confirms this relationship in the context of right hemispheric stroke patients. The patient measurement is correctly identified as template_lesion_overlap (lesion status overlaid on templates/voxels), not patient_diffusion, as the analysis relies on structural lesion maps rather than diffusion tractography in the patients themselves.
              source_ids:
              - P7-S2-C3
              - P7-S1-C14
            qualifications:
              answer: fits
              reason: The proposed draft includes the qualification 'compared to the best-performing single voxel', which is the core constraint of the finding in P7-S2-C3. It also notes the population (right hemispheric stroke) and the context (narrative review of Smith et al., 2013).
              source_ids:
              - P7-S2-C3
              - P7-S1-C15
            missing_material_caveat:
              answer: fits
              reason: The draft correctly identifies that this is a finding reported within a narrative review of a prior study (Smith et al., 2013), which is a material caveat regarding the evidence quality and origin. No other material caveats from the source passages appear to be omitted that would change the interpretation of this specific comparison.
              source_ids:
              - P7-S1-C14
              - P7-S2-C3
          optional_pending:
          - Specific statistical metrics (e.g., AUC, accuracy) for the multivariate vs single voxel comparison are not transcribed.
          - Specific sample size N for the Smith et al. (2013) study is not transcribed.
          verdict: draft
          reason: All five core checks fit the source.
          material_issues: []
        pending_details:
        - Detailed statistics, atlas/reference-space and structured confounder metadata not transcribed.
        - Recovery phase is not classified; use the reported timing words.
        - Evidence-strength rating is a conservative draft placeholder pending human review.
        - Specific statistical metrics (e.g., AUC, accuracy) for the multivariate vs single voxel comparison are not transcribed.
        - Specific sample size N for the Smith et al. (2013) study is not transcribed.
        normalizations: []
        analysis_identity:
          id: R009
          exposure:
            text: patterns of damage (multivariate)
          outcome:
            text: spatial neglect
          analysis_label: Multivariate vs single voxel prediction (spatial neglect)
          relation: model_comparison
          evidence_ids:
          - P7-S2-C3
          qualifier_ids:
          - P7-S1-C15
          context_ids: []
          table_ids: []
          approved: false
          status: requires_source_review
          flags:
          - new_model_candidate_not_verified
          candidate_discovery:
            model: gemma4:31b
            model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
            pdf_sha256: dbbf5db9f646e5ed67190025aea75aff5c20f899e9304ffa7b67f2d7641a12b8
            source_review: _compare/relationships-2026-11-16/review-current/Karnath2018
            source_status_sha256: 06714d9285acb35e66412583a1166bdee53028f03385fee771ec530bffc2b5f2
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
      page: 7
      quote: 'In a large sample of

        right hemispheric stroke patients, they found patterns of damage more

        predictive of spatial neglect than the best-performing single voxel.'
      status: pending
      by: agent:relationship-converter
      date: '2026-11-24'
      note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor roles, all qualifiers, source audit issues and main-PDF tables/figures; check missing results. This model proposal is not verified.'
  original_mapping:
    decision: draft
    reason: The source describes a specific finding from Smith et al. (2013) where a multivariate model of damage patterns was more predictive of spatial neglect than the best-performing single voxel in a large sample of right hemispheric stroke patients.
    bucket: predictors
    entity_id: multivariate_damage_pattern_neglect
    name: multivariate damage pattern predictor
    kind: predictor
    predictor_type: imaging_metric
    definition: multivariate patterns of structural damage (lesion status of multiple voxels) in the brain
    assessment: []
    target: spatial_neglect
    target_kind: impairment
    claim: patterns of damage were more predictive of spatial neglect than the best-performing single voxel
    direction: likely
    method: MVPA
    relationship: correlational
    therapy: null
    sample_n: null
    population: right hemispheric stroke patients
    timing: not_transcribed
    qualifications:
    - compared to the best-performing single voxel
    limitations:
    - finding is reported within a narrative review of a prior study (Smith et al., 2013)
    optional_pending: []
    evidence_quality: cohort
    passages:
    - source_id: P7-S2-C3
      supports: claim
    - source_id: P7-S1-C15
      supports: sample
    - source_id: P6-S3-C8
      supports: method
  original_attempt:
    binding:
      profile: core
      version: core-source-check-v3
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      checker_model: qwen3.8:27b
      checker_digest: 47951e4a666180bc2aedfc93c169472f2de783696fe196efbf063f5730ecf163
      host: http://localhost:11434
      pdf_sha256: dbbf5db9f646e5ed67190025aea75aff5c20f899e9304ffa7b67f2d7641a12b8
      review_sha256: 1fbc9305ad0a2f592e05e317766596032c7b6e691efb6c3ba2125c242408e7f0
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
    proposal: R009
    status: draft
    reason: All five core checks fit the source.
    material_issues: []
    path: drafts/predictors/multivariate_damage_pattern_neglect__Karnath2018__R009.md
    seconds_this_run: 111.91130945799523
  source_check:
    profile: agent-repair
    scope: Agent source reconstruction; original model reviews do not certify the changed record. No independent model pass or human approval.
    approved: false
    paper_complete: false
    binding:
      pdf_sha256: dbbf5db9f646e5ed67190025aea75aff5c20f899e9304ffa7b67f2d7641a12b8
      original_mapping_sha256: 9c9f39524ad516e8fdb42834cc99976d23168f238a9630ca4d30debb59377539
      original_status_sha256: be88ae519e5bdbb4710ad618331b8de3c9fcaa2f59514f19a79cd182d2ac24a6
      evidence_sha256: 1fe03a7858e2c0619360925a382c4a7c8eb22dd92699fd695c60acd3a8aa9df7
    publication_correction:
      by: agent:source-repair
      date: '2026-11-26T02:05:16.806224+00:00'
      pdf_pages:
      - 1
      - 7
      note: Reclassified as a secondary review report, explicitly attributing the result to Smith et al. (2013). This is not a new primary sample or independent replication; quantitative estimates and study-level attribution require human verification against the primary publication.
      approved: false
      audit: logs/publication/draft-repairs-2026-11-26-round2.json
    remaining:
    - Human source review and approval
    - Full paper completeness review
reviewer_marks:
- id: relationship-source-check
  page: 7
  quote: 'In a large sample of

    right hemispheric stroke patients, they found patterns of damage more

    predictive of spatial neglect than the best-performing single voxel.'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-24'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor roles, all qualifiers, source audit issues and main-PDF tables/figures; check missing results. This model proposal is not verified.'
- id: source-repair-round2
  status: pending
  by: agent:source-repair
  date: '2026-11-26'
  note: Reclassified as a secondary review report, explicitly attributing the result to Smith et al. (2013). This is not a new primary sample or independent replication; quantitative estimates and study-level attribution require human verification against the primary publication.
---

# Source review required

This repaired draft remains unapproved. Original outputs and review provenance are preserved.
