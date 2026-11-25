---
id: singing_vs_speaking_ciu
name: singing versus speaking production
kind: classical
findings:
- id: f1
  target: speech_production_accuracy
  target_kind: impairment
  claim: The proportion of spoken CIUs relative to total words possible was significantly
    lower than the proportion of sung CIUs relative to total words in both patients.
  direction: likely
  relationship: correlational
  method: behavioral_only
  sample:
    n: 2
    population: patients with severe nonfluent (Broca's) aphasia following left-hemisphere
      ischemic stroke
    phase: not_reported
    time_post_onset: baseline (pre-treatment)
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - results based on two prototypical patients
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Comparison of the proportion of Correct Information
    Units (CIUs) produced while singing versus speaking the lyrics of at least two
    familiar songs. measured using lyrics of at least two familiar songs. Additional
    metadata has not been transcribed; review the pending-field flags before approval.'
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
    - proposed_concept:speech_production_accuracy
  citation: '@Schlaug2008'
  source_passages:
  - section: Original source P3-S2-C11
    page: 3
    quote: 'In addition, we assessed their ability to

      speak/sing the lyrics of familiar songs by analyzing the

      number of Correct Information Units (CIUs; correct,

      meaningful words) that each patient produced while

      singing and speaking compared to the total number of

      '
    supports: method
  - section: Original source P3-S3-C1
    page: 3
    quote: 'number of Correct Information Units (CIUs; correct,

      meaningful words) that each patient produced while

      singing and speaking compared to the total number of

      words for at least two familiar songs.'
    supports: method
  - section: Original source P4-S1-C3
    page: 4
    quote: 'The proportion of spo-

      ken CIUs/total words possible was significantly lower

      than the proportion of sung CIUs/total words in both

      patients.Although both patients actually received 75 ses-

      sions of MIT, the comparison between the two inter-

      ventions reported here was made after each patient had

      received 40 sessions of their originally assigned treat-

      ment (MIT and SRT respectively).'
    supports: claim
  - section: Original source P3-S2-C8
    page: 3
    quote: 'Both were diag-

      nosed with severe nonfluent aphasia (restricted verbal

      output, impaired naming and repetition, relatively

      unimpaired comprehension) as the result of a left-

      hemisphere ischemic stroke involving mainly the supe-

      rior division of the middle cerebral artery, and classified

      as having Broca’s aphasia.'
    supports: sample
  - section: Original source P7-S2-C2
    page: 7
    quote: 'Although caution should be exercised when making

      generalizations from results in two prototypical patients,

      we hope that our findings will serve as a source for fur-

      ther discussion on the efficacy of MIT, the neural corre-

      lates of MIT, and the choice of appropriate control

      interventions for MIT.'
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-25'
relationship_review:
  paper: Schlaug2008
  proposal_id: R008
  review_status_sha256: 9e06434f9a8666e79ff3a9017cbadbaacd61efa26b9fb52e6d4b023595c522eb
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 0d77b30100d6f663e9662da3a1677ee9cf0069050b35658a3441e72dd6501de0
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 0d77b30100d6f663e9662da3a1677ee9cf0069050b35658a3441e72dd6501de0
        A/passages.json: b93aca70d2ea3f94986bb56e3a986d949660c38ac128a7edd1f3432a79ac0fdd
        A/raw.json: 0f1f338ec93c5993e05fd6b83f529ee0c4fdfc77f22d70809e560bf09ee7022f
        A/source-units.json: bd62c99dab4a2f7927f8f61a23c23154a50fdb04fc52f720781e332e0e3f9edb
        A/full-source-units.json: 30c8790472d61a4d822d93eb1528d23e734e0ee0e351e8a5e96a8079fa6fccdb
        A/meta.json: 0ac3a06a9871c3b069f66290664b948e75870dfa4667a07181d81204f8704881
        A/table-images/TABLE-1-page-5-1.png: 25acb8369c012d6f54290239b0de8c6f3aca160f5804744335883ca1ff5b9dbe
        A/table-images/page-5.png: 5492d187319efad82c4c3f32affe55100fad77639d457f409f8645591937de48
        A/table-images/manifest.json: a4c66cefd02c2b40c176e3ad403c8b736596121599ff38e6b3a000b4c5dbf5f2
        A/clauses/window-03/raw.json: 33f1f59ac0d35ec17ec397887594fa97b31a8811a8fc5fbfa4a86879d32ce639
        A/clauses/window-03/prompt.txt: f98989bd4d30c3ef35d5f1daa2565c190bf4a6b8784e5d35071e4097131e2cfe
        A/clauses/window-03/meta.json: 4fa8135b4b84503b2951b479867778ad570160902224049a86849bc53d5ca95c
        A/clauses/window-04/raw.json: 52bf800c616fe68a14dbd5776a8fd3911ad2471e74b2770ed4b3d4af3143ac67
        A/clauses/window-04/prompt.txt: e7aaa414a9164d2045c46b07605073a481bebc3731e089f74705395a65d0b9df
        A/clauses/window-04/meta.json: ce64e863c7c4f496b7a73fe28461959057f3c18a3e7b3c4a3955317790aaec71
        A/clauses/window-05/raw.json: 54d3d6fe58fdbe43d22196099dc227ed2883e721f1f89245676cff90bbdeac96
        A/clauses/window-05/prompt.txt: f7ca35a80770d4c46108008cbb6dfa86237b4685cb37242db1234901828ece1d
        A/clauses/window-05/meta.json: 1afcf563699788849b9e796bf51d96321980b47b53a0c445419abb29debb211e
        A/clauses/window-02/raw.json: 1de97ac6135d21346adf9dd04d3fa0ad8a8cade1925b78a488ea2be5bdbd0675
        A/clauses/window-02/prompt.txt: 33a948fe85d526874c2f2dea102d30be0172e6a23c289caa0ace6a2454c5b747
        A/clauses/window-02/meta.json: 250dfaed954a25ca7f5f045fc0cc108488b03701d8ba99ca2599c7f3790955c2
        A/clauses/window-01/raw.json: 00475c37e79fb7dfcfeb50550eda613acce5dc63e12d76bd02ac414725198e40
        A/clauses/window-01/prompt.txt: 2d2df2104e4d899b39030765d46ef8d6b3747ab582fc1fe998ac01f05c263c5b
        A/clauses/window-01/meta.json: 3b82be5802de1ff898397c968abfaa02d820d7afa64fa4d24083611eee3992e4
        A/tables/TABLE-1-page-5-1/raw.json: 9234b2a0e3c33cb1ff35d1ab82a9cd0046ac2e5ffdd124dea41686d91742a8db
        A/tables/TABLE-1-page-5-1/prompt.txt: 3847079ae3ccbda9fd6794b3c1554215de16e22fa94c34416d315a04ed75986b
        A/tables/TABLE-1-page-5-1/meta.json: b7af1f0c5a92685d7690edf0d04104a30355c7d9c3be14f438bba96e1ef52661
        B/passages.json: b93aca70d2ea3f94986bb56e3a986d949660c38ac128a7edd1f3432a79ac0fdd
        B/raw.json: f4f54768732ace291933b556de265008ee80d3a108206e08ea278db0c3727fbb
        B/source-units.json: bd62c99dab4a2f7927f8f61a23c23154a50fdb04fc52f720781e332e0e3f9edb
        B/full-source-units.json: 30c8790472d61a4d822d93eb1528d23e734e0ee0e351e8a5e96a8079fa6fccdb
        B/meta.json: 0e971dee3f0e26efea439ff7c835f6bcf5bb630dd60e33e731d510bc649fd961
        B/table-images/TABLE-1-page-5-1.png: 25acb8369c012d6f54290239b0de8c6f3aca160f5804744335883ca1ff5b9dbe
        B/table-images/page-5.png: 5492d187319efad82c4c3f32affe55100fad77639d457f409f8645591937de48
        B/table-images/manifest.json: 2227bca00f78a33803119373df9a7dc997a196e69028f92400588c3a566c85e7
        B/clauses/window-03/raw.json: 547ec2f37e77b5f2fb484104ec916afae4ef97f7d083bdf9e51637f0648a030b
        B/clauses/window-03/prompt.txt: f98989bd4d30c3ef35d5f1daa2565c190bf4a6b8784e5d35071e4097131e2cfe
        B/clauses/window-03/meta.json: fdc0742a29ba7dc6020255ae7de6438b3e69f5750b6d29e0164f9239fc98e33d
        B/clauses/window-04/raw.json: 78fe5bc1d2241fc20f5b229288081ebad2e856e83a33c19f8026c895d29f04dd
        B/clauses/window-04/prompt.txt: e7aaa414a9164d2045c46b07605073a481bebc3731e089f74705395a65d0b9df
        B/clauses/window-04/meta.json: e986432da0767353f7fb6e1fed3e73d866fdeb8a9aa5f9eda04ad48e9b53dfc4
        B/clauses/window-05/raw.json: be95c3be9e7cfb52e86f4173f7720ce7e9b14355f91ef15bef45af943ece246e
        B/clauses/window-05/prompt.txt: f7ca35a80770d4c46108008cbb6dfa86237b4685cb37242db1234901828ece1d
        B/clauses/window-05/meta.json: 0b0506f207585492363ce3614c7e7144483a514f91ae77427199175d4d6da976
        B/clauses/window-02/raw.json: 98f0ff676b767fc0f7c0f9fa9d36967cebc25fe65bcf0c60a4c9c02515b49edf
        B/clauses/window-02/prompt.txt: 33a948fe85d526874c2f2dea102d30be0172e6a23c289caa0ace6a2454c5b747
        B/clauses/window-02/meta.json: c38463be9f559c403b9baaea52e2a7460c0493b900631092b608f7e8652e3f85
        B/clauses/window-01/raw.json: 008ee64ca9912c24a54c6498a4b9e45451689a845af8bf10a15eea42e8c3c51b
        B/clauses/window-01/prompt.txt: 2d2df2104e4d899b39030765d46ef8d6b3747ab582fc1fe998ac01f05c263c5b
        B/clauses/window-01/meta.json: 59372a1e93a86c36d20b7472f5713adf9bc3b4e4847874d7ad68a5b3d096d5a1
        B/tables/TABLE-1-page-5-1/raw.json: 0ca14eab81ba3e612740dda3b5c85ac77d8cba577d793b986da17652c32565d8
        B/tables/TABLE-1-page-5-1/prompt.txt: 3847079ae3ccbda9fd6794b3c1554215de16e22fa94c34416d315a04ed75986b
        B/tables/TABLE-1-page-5-1/meta.json: b09ed297db0cef6742a6bc8f8b09acb90b01c7882277cda1b1d4ff6809887cf9
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
      pdf_sha256: 0d77b30100d6f663e9662da3a1677ee9cf0069050b35658a3441e72dd6501de0
      source_review: _compare/relationships-2026-11-16/review-current/Schlaug2008
      source_status_sha256: bfd72b3948e33dddbdd8453668e41494f184f740707dbc01c33319163291cd42
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R008
    exposure:
      text: mode of production (singing vs speaking)
    outcome:
      text: proportion of Correct Information Units (CIUs)
    analysis_label: Baseline singing vs speaking
    relation: association
    evidence_ids:
    - P4-S1-C3
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
      pdf_sha256: 0d77b30100d6f663e9662da3a1677ee9cf0069050b35658a3441e72dd6501de0
      source_review: _compare/relationships-2026-11-16/review-current/Schlaug2008
      source_status_sha256: bfd72b3948e33dddbdd8453668e41494f184f740707dbc01c33319163291cd42
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Accounting without a linked unit P4-S3-C4
      - Accounting without a linked unit P4-S3-C5
      - Accounting without a linked unit P5-S1-C1
      - Accounting without a linked unit P5-S1-C3
      - Accounting without a linked unit P5-S1-C4
      - Accounting without a linked unit P5-S1-C5
      - Accounting without a linked unit P5-S1-C6
      - Unaccounted source passage P4-S3-C5
      - Unaccounted source passage P5-S1-C6
      - Unaccounted source passage P4-S3-C4
      - Unaccounted source passage P5-S1-C3
      - Unaccounted source passage P5-S1-C4
      - Unaccounted source passage P5-S1-C1
      - Unaccounted source passage P5-S1-C5
      - Result passage disposed without unit P5-S1-C7
      - Accounting without a linked unit P6-S1-C2
      - Accounting without a linked unit P6-S1-C3
      - Result passage disposed without unit P7-S2-C1
      - Unaccounted source passage P6-S1-C3
      - Unaccounted source passage P6-S1-C2
      unattached_null_or_qualifier_ids:
      - P4-S3-C5
      - P6-S1-C3
      - P7-S2-C1
      suppressed_nonrepresented_units: 1
      default_disposition_count_requires_completeness_check: 101
      unselected_timing_passages:
      - P3-S3-C2
      - P3-S3-C3
      - P4-S1-C5
      - P4-S1-C7
      - P4-S2-C14
      - P4-S3-C1
      - P5-S1-C2
      - P5-S1-C8
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P5-S2-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P7-S2-C2
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: outcome_timing
        source_ids:
        - P4-S1-C2
        - P4-S1-C5
        - P4-S1-C6
        - P4-S1-C7
        - P4-S3-C2
        - P5-S1-C1
        - P5-S1-C5
        - P5-S1-C6
        - P6-S1-C3
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - outcome_timing
      - validation
      - personal_factors
      - tested_personal_effects
      - adjustment_roles
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-5-1
      unlinked_tables:
      - TABLE-1-page-5-1
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P2-S2
        - P4-S2
        - P4-S3
        - P5-S1
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 0d77b30100d6f663e9662da3a1677ee9cf0069050b35658a3441e72dd6501de0
      source_review: _compare/relationships-2026-11-16/review-current/Schlaug2008
      source_status_sha256: bfd72b3948e33dddbdd8453668e41494f184f740707dbc01c33319163291cd42
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C5
      disposition: represented
      result_indexes:
      - 0
      reason: States MIT gains surpassed control-treated patient in propositional
        speech.
    - source_id: P1-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discusses theoretical mechanisms of MIT's effect.
    - source_id: P4-S1-C3
      disposition: represented
      result_indexes:
      - 7
      reason: Reports sung CIUs were significantly higher than spoken CIUs at baseline.
    - source_id: P4-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient classification/demographics.
    - source_id: P4-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Task performance accuracy, not a clinical outcome relationship.
    - source_id: P4-S3-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Baseline consistency statement.
    - source_id: P4-S3-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Null finding on repeat baseline assessments.
    - source_id: P4-S3-C5
      disposition: represented
      result_indexes:
      - 1
      reason: 'Reports significant improvement for Patient #1 after MIT.'
    - source_id: P5-S1-C1
      disposition: represented
      result_indexes:
      - 4
      reason: 'Describes fMRI changes in Patient #1 post-MIT.'
    - source_id: P5-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison of baseline characteristics.
    - source_id: P5-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Null finding on repeat baseline assessments.
    - source_id: P5-S1-C5
      disposition: represented
      result_indexes:
      - 2
      - 5
      reason: 'Reports behavioral improvement and fMRI changes for Patient #2 post-SRT.'
    - source_id: P5-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of imaging protocol.
    - source_id: P5-S1-C7
      disposition: represented
      result_indexes:
      - 6
      reason: 'Describes regional magnitude of activation changes post-MIT for Patient
        #2.'
    - source_id: P5-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Lesion description.
    - source_id: P6-S1-C1
      disposition: represented
      result_indexes:
      - 6
      reason: 'Compares activation magnitude between MIT and SRT for Patient #2.'
    - source_id: P6-S1-C2
      disposition: represented
      result_indexes:
      - 0
      reason: Direct comparison of MIT vs SRT behavioral and neural outcomes.
    - source_id: P6-S1-C3
      disposition: represented
      result_indexes:
      - 3
      reason: 'Reports further gains for Patient #2 after MIT.'
    - source_id: P7-S2-C1
      disposition: represented
      result_indexes:
      - 2
      reason: Confirms therapeutic effects of shared elements (SRT).
    unresolved_coverage: []
    pending_source_ids:
    - P1-S1-C6
    - P4-S1-C4
    - P4-S2-C9
    - P4-S3-C3
    - P4-S3-C4
    - P5-S1-C3
    - P5-S1-C4
    - P5-S1-C6
    - P5-S1-C8
    - P7-S2-C1
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-5-1
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P3-S2-C7
      - P3-S3-C2
      - P3-S3-C3
      - P4-S1-C1
      - P4-S2-C10
      recruited_sample:
      - P3-S2-C7
      eligibility:
      - P3-S2-C8
      - P3-S2-C9
      imaging_provenance:
      - P4-S2-C7
      imaging_timing:
      - P4-S1-C2
      - P4-S3-C2
      - P5-S1-C1
      - P5-S1-C5
      - P5-S1-C6
      outcome_timing: []
      outcome_definition:
      - P3-S2-C11
      - P4-S1-C7
      - P4-S1-C9
      - P5-S2-C4
      validation: []
      analysis_restrictions:
      - P3-S2-C3
      dependent_variable_statement:
      - P4-S1-C7
      limitations:
      - P7-S2-C2
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles: []
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P3-S3-C2
      - P3-S3-C3
    outcome_type: both_reported
    imaging_vs_outcome: mixed
    validation_type: repeated_patients
    held_selections:
    - slot: dependent_variable_statement
      source_id: P5-S2-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P7-S2-C2
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: outcome_timing
      source_ids:
      - P4-S1-C2
      - P4-S1-C5
      - P4-S1-C6
      - P4-S1-C7
      - P4-S3-C2
      - P5-S1-C1
      - P5-S1-C5
      - P5-S1-C6
      - P6-S1-C3
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
      pdf_sha256: 0d77b30100d6f663e9662da3a1677ee9cf0069050b35658a3441e72dd6501de0
      review_sha256: 9e06434f9a8666e79ff3a9017cbadbaacd61efa26b9fb52e6d4b023595c522eb
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
      - P4-S1-C3
      source_result: The proportion of spoken Correct Information Units (CIUs) relative
        to total words possible was significantly lower than the proportion of sung
        CIUs relative to total words in both patients at baseline.
      result_status: detected
      patient_measurement: non_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis R008 correctly identifies the baseline comparison
            of singing vs. speaking for CIUs. The source P4-S1-C3 explicitly states
            this comparison was made and found significant. The draft correctly identifies
            this as a behavioral comparison (non-imaging) rather than the fMRI results
            which are also present in the paper but distinct from this specific behavioral
            metric.
          source_ids:
          - P4-S1-C3
          - P3-S2-C11
          - P3-S3-C1
        direction:
          answer: fits
          reason: The source states spoken CIUs were significantly lower than sung
            CIUs. The draft claim states spoken CIUs were significantly lower than
            sung CIUs. The direction is preserved.
          source_ids:
          - P4-S1-C3
        construct:
          answer: fits
          reason: The exposure is mode of production (singing vs speaking). The outcome
            is proportion of CIUs. The measurement is behavioral (counting correct
            words in song lyrics). This matches the source description in P3-S2-C11
            and P3-S3-C1 where CIUs are defined as correct meaningful words produced
            while singing/speaking songs.
          source_ids:
          - P3-S2-C11
          - P3-S3-C1
          - P4-S1-C3
        qualifications:
          answer: fits
          reason: The draft includes the qualification that the measurement used lyrics
            of at least two familiar songs, which is supported by P3-S3-C1. It also
            includes the limitation of two prototypical patients, supported by P7-S2-C2.
            The timing is correctly identified as baseline (pre-treatment) as per
            P4-S1-C3 context and P4-S3-C3.
          source_ids:
          - P3-S3-C1
          - P7-S2-C2
          - P4-S1-C3
        missing_material_caveat:
          answer: fits
          reason: The draft captures the key limitation of the sample size (n=2) and
            the specific nature of the task (song lyrics). No other material caveats
            regarding this specific behavioral finding appear to be omitted that would
            change the interpretation of the baseline singing vs speaking difference.
          source_ids:
          - P7-S2-C2
          - P4-S1-C3
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
      original: impairments
      action: route_from_kind
      value: regions
    analysis_identity:
      id: R008
      exposure:
        text: mode of production (singing vs speaking)
      outcome:
        text: proportion of Correct Information Units (CIUs)
      analysis_label: Baseline singing vs speaking
      relation: association
      evidence_ids:
      - P4-S1-C3
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
        pdf_sha256: 0d77b30100d6f663e9662da3a1677ee9cf0069050b35658a3441e72dd6501de0
        source_review: _compare/relationships-2026-11-16/review-current/Schlaug2008
        source_status_sha256: bfd72b3948e33dddbdd8453668e41494f184f740707dbc01c33319163291cd42
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
  page: 3
  quote: 'In addition, we assessed their ability to

    speak/sing the lyrics of familiar songs by analyzing the

    number of Correct Information Units (CIUs; correct,

    meaningful words) that each patient produced while

    singing and speaking compared to the total number of

    '
  status: pending
  by: agent:relationship-converter
  date: '2026-11-25'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
