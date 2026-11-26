---
id: left_slf
name: left SLF cluster
kind: network
findings:
- id: f1
  target: aphasia_severity_and_cognition
  target_kind: impairment
  claim: white matter integrity of the left superior longitudinal fasciculus (SLF) was positively correlated with the aphasia quotient (AQ), performance quotient (PQ), and cortical quotient (CQ)
  direction: likely
  relationship: correlational
  method: DTI
  sample:
    n: 18
    population: right-handed Chinese native speakers with acute aphasia following a single left-hemisphere ischemic or hemorrhagic stroke
    phase: not_reported
    time_post_onset: MRI performed for an average of 9.7 ± 5.3 days after stroke; aphasia persistent at day 1 post-stroke
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - relatively small sample size
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: fractional anisotropy (FA) of the left superior longitudinal fasciculus (SLF) measured via tract-based spatial statistics (TBSS). correlations were analyzed using mean FA values from significantly different clusters identified via TBSS. Additional metadata has not been transcribed; review the pending-field flags before approval. PDF image reading (P2-S3-C6, two-model agreement, human verification pending): Materials and Methods


    Subjects


    Eighteen aphasia patients (all right-handed, six females; age, 53.67 ± 13.66 years) were recruited from admission at the Fuzhou Hospital Original text-layer quotation is preserved below. PDF image reading (P2-S3-C7, two-model agreement, human verification pending): . Patients were recruited retrospec-

    tively according to the following criteria: (1) first stroke

    occurred in the left hemisphere; (2) age of >18 and

    <85 years; (3) Chinese native speaker; (4) aphasia per-

    sistent at day 1 post-stroke; and (5) right-handed Original text-layer quotation is preserved below. PDF image reading (P3-S1-C2, two-model agreement, human verification pending): . All patients experienced a single left-hemisphere

    ischemic (n = 16) or hemorrhagic (n = 2) stroke (lesion

    size: 30.60 ± 42.23 cm³) and underwent MRI for an

    average of 9.7 ± 5.3 days after stroke (Table 1) Original text-layer quotation is preserved below. Publication correction (human verification pending): TBSS-defined SLF mean FA correlations; corrected the method from LSM to DTI.'
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
    - proposed_concept:aphasia_severity_and_cognition
    - publication_correction_pending_human_verification
  citation: '@Yang2017'
  source_passages:
  - section: Original source P1-S1-C7
    page: 1
    quote: 'In addition, WM integrity of the left IFOF and SLF showed

      a positive correlation with aphasia quotient, performance

      quotient, and cortical quotient, respectively.'
    supports: claim
  - section: Original source P4-S2-C10
    page: 4
    quote: 'The left SLF were pos-

      itively correlated with the AQ (R = 0.5630, P = 0.0150),

      Fig. 1 Distribution of the lesion areas of all patients.'
    supports: claim
  - section: Original source P5-S1-C1
    page: 5
    quote: '

      PQ (R = 0.4848, P = 0.0414) and CQ (R = 0.5351,

      P = 0.0221) scores, respectively.'
    supports: claim
  - section: Original source P2-S3-C6
    page: 2
    quote: 'Materials and Methods

      Subjects

      Eighteen aphasia patients (all right-handed, six females;

      age, 53.67 ± 13.66 years) were recruited from admission

      at the Fuzhou Hospital.'
    supports: sample
  - section: Original source P2-S3-C7
    page: 2
    quote: 'Patients were recruited retrospec-

      tively according to the following criteria: (1) ﬁrst stroke

      occurred in the left hemisphere; (2) age of [18 and

      \85 years; (3) Chinese native speaker; (4) aphasia per-

      sistent at day 1 post-stroke; and (5) right-handed.'
    supports: sample
  - section: Original source P3-S1-C2
    page: 3
    quote: 'All patients experienced a single left-hemisphere

      ischemic (n = 16) or hemorrhagic (n = 2) stroke (lesion

      size: 30.60 ± 42.23 cm3) and underwent MRI for an

      average of 9.7 ± 5.3 days after stroke (Table 1).'
    supports: sample
  - section: Original source P3-S1-C2
    page: 3
    quote: 'All patients experienced a single left-hemisphere

      ischemic (n = 16) or hemorrhagic (n = 2) stroke (lesion

      size: 30.60 ± 42.23 cm3) and underwent MRI for an

      average of 9.7 ± 5.3 days after stroke (Table 1).'
    supports: method
  - section: Original source P4-S2-C2
    page: 4
    quote: 'Correlations between the mean FA values from the sig-

      niﬁcantly different clusters and clinical scores including

      AQ, PQ and CQ were analyzed.'
    supports: method
  - section: Original source P6-S1-C11
    page: 6
    quote: 'First, the

      sample size was relatively small for studies involving

      abnormal WM integrity in aphasia.'
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-26'
relationship_review:
  paper: Yang2017
  proposal_id: R003
  review_status_sha256: 9d8b62fedb301e33d6df69e6c15dadc86200d206dcef61e8a3b63c938ffc49d1
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: c496e5bcfef9f3c2f1c2d118e283e170fb02c4c4143c562cbb78343319fa139c
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: c496e5bcfef9f3c2f1c2d118e283e170fb02c4c4143c562cbb78343319fa139c
        A/passages.json: 36e0fbe8898ad363617fa9b08f55f4ade0ac0ff6f04f1ca5705bbeb151820a49
        A/raw.json: 21435fdea96f17e838be6d98280bbcbb3efee10643a852de5b0b7dcd1f4b706e
        A/source-units.json: 5ee6f983696121f7810fbf6007880618e525f1c23df8f5af1caf1c3040b79102
        A/full-source-units.json: 3b306e371dc5c798021aaaa47a66c335c0134a888e2edd26dbb742339bff3f3f
        A/meta.json: 33c9b4bd49c3e3ca767c7ea62309fd2e040c3a2161ce87b201cbd280034b371a
        A/table-images/TABLE-1-page-3-1.png: f0e749c2651c5ce6ad3f0bfc957b45416e65ab457410a20eebf435d73e7b8633
        A/table-images/page-3.png: 5d74b7fc51ce83c35b2ad8c0f9f9f0f35da813c5156b38959743dcc72918c8c4
        A/table-images/page-5.png: 44eed6beecc95bd73fd78e8f11fbd2433d91fb624dd5d76de2cafaa266983b9a
        A/table-images/manifest.json: b7cfc083004e5b8a87deb4ed2ecdeed34cd14944fcb3f6e23b8a79b92c43ea57
        A/table-images/TABLE-2-page-5-1.png: 70a5ef7b48d52a94718d1bf1eb1345159b07e5925fd1fac82cf52ee0a504c539
        A/clauses/window-03/raw.json: e507a92b1f28d87fdac0361195a889d6670b6fb5fcc9f4ecc2866b4d112c2584
        A/clauses/window-03/prompt.txt: af33d039f543fa9f44cc7023475bdca1ff7b16ea72a82e15b71b66592c360799
        A/clauses/window-03/meta.json: 80adbbb848fce82bbc68109eabe3b6e4b6996bdaef7988c3a46998f062e0fa74
        A/clauses/window-04/raw.json: e42ae116a2d35dbf35341998c87fbe700c4ada309f980aa3b77eb1bf1bf83498
        A/clauses/window-04/prompt.txt: 2b4d26f3d44a8db7ad44c69906d69169945f48d3e0c9a9f30541704371e1dab1
        A/clauses/window-04/meta.json: 3ed4b7d680acd9787841d7c09a91955e72264b7c8e935e56c3e1d41e207a2737
        A/clauses/window-05/raw.json: 7941c2bd8b4dcf06fd321a73f8ce8071f38a4597bc1f86cdcc84caa40712b8b4
        A/clauses/window-05/prompt.txt: ca6a999b3f523ed2b39b82935f00552bd00c86281a6928e8654acb3a9a5043f7
        A/clauses/window-05/meta.json: 2ead45016ca6a2329f64c5a6aef3c3cae47a5e6a0ca37bbebfe9e8e8820b63f1
        A/clauses/window-02/raw.json: 3a2a13715f54b5abb4871f3b7f5fbb23db92d6da8c03e7013091a59da4ed21e8
        A/clauses/window-02/prompt.txt: 476414b52ef450e9681f5fad3f172ecd8a773e187b35f255bcf878499b19a0f4
        A/clauses/window-02/meta.json: 86b3091353ecb2fd164f72c908512ecd0fbadca39640a8656db602cdcb2cb4e6
        A/clauses/window-01/raw.json: a46396dc4350b9c74cb0c903e526ef8814bcf499789cda078e47e0c5c4d5bcfb
        A/clauses/window-01/prompt.txt: a73fbd8ad714b16f4c84ded5401789c952f6270bbbd820d4443b18acd8a85e84
        A/clauses/window-01/meta.json: d77f0d3685904aefd348f4846933533d80272b59b8c47317d76ec1f21b5784fb
        A/tables/TABLE-2-page-5-2/raw.json: 8b35a2eca05e205cfcd8d056ec81ecf9182f6250973e45f01e4118c8862a561c
        A/tables/TABLE-2-page-5-2/prompt.txt: 9beded6d4540b530ab67ebe047402c8a43091caae41d05f4fe93a572f6cadf2b
        A/tables/TABLE-2-page-5-2/meta.json: 02cbfa224565408fc23c32adb0bb4412d2fd43def50b31853c15061bb031176f
        A/tables/TABLE-1-page-3-1/raw.json: 3cf7c22b21870a039cf70dae72a9f45af0626bcadc4f15ec1a0f706ad95726b3
        A/tables/TABLE-1-page-3-1/prompt.txt: a38afbcf5703e45ebfb6cc4953b5dc5dac7ca1599a5ec0dcf162267e82c68373
        A/tables/TABLE-1-page-3-1/meta.json: 1eba8433c137177cfbb64083f0aae1849e1b9b3e5eb7751e1e1b6f5447667ae5
        B/passages.json: 36e0fbe8898ad363617fa9b08f55f4ade0ac0ff6f04f1ca5705bbeb151820a49
        B/raw.json: ba46201fc24473b10457069fe21a7b00a781f5b2551f8b6e97fa2b73ead0aeb2
        B/source-units.json: 5ee6f983696121f7810fbf6007880618e525f1c23df8f5af1caf1c3040b79102
        B/full-source-units.json: 3b306e371dc5c798021aaaa47a66c335c0134a888e2edd26dbb742339bff3f3f
        B/meta.json: 76e0e248c37e84186aa0156d6883a741b94e03d72b06dfd314313202f5c0ef35
        B/table-images/TABLE-1-page-3-1.png: f0e749c2651c5ce6ad3f0bfc957b45416e65ab457410a20eebf435d73e7b8633
        B/table-images/page-3.png: 5d74b7fc51ce83c35b2ad8c0f9f9f0f35da813c5156b38959743dcc72918c8c4
        B/table-images/page-5.png: 44eed6beecc95bd73fd78e8f11fbd2433d91fb624dd5d76de2cafaa266983b9a
        B/table-images/manifest.json: cd2390286633ab69b24dcb4fd0188376d41fd7a099f5eefec8b6772feff0dc78
        B/table-images/TABLE-2-page-5-1.png: 70a5ef7b48d52a94718d1bf1eb1345159b07e5925fd1fac82cf52ee0a504c539
        B/clauses/window-03/raw.json: b9837e1fa416ad11df46625463118dcb09a08636f4de75e30b114c517cb341f4
        B/clauses/window-03/prompt.txt: af33d039f543fa9f44cc7023475bdca1ff7b16ea72a82e15b71b66592c360799
        B/clauses/window-03/meta.json: 12483d2cb987c9ae2ae39798cb416164a123ea9d26e71a74019d45f380d65805
        B/clauses/window-04/raw.json: 2d2d9344dc094d685086e1c4ebd4b6694aac1b354e5c171bfde844035a865250
        B/clauses/window-04/prompt.txt: 2b4d26f3d44a8db7ad44c69906d69169945f48d3e0c9a9f30541704371e1dab1
        B/clauses/window-04/meta.json: 6ac674b610fb30ebb784024c9b964d14cec4261e6d93aa5062c265f9a76c73ac
        B/clauses/window-05/raw.json: a243e895f77fbb533f9c629e3f47ad2d10ece347040613cf684c936f5b8e662c
        B/clauses/window-05/prompt.txt: ca6a999b3f523ed2b39b82935f00552bd00c86281a6928e8654acb3a9a5043f7
        B/clauses/window-05/meta.json: 1a812ae23f0808737f5ce5b5507fd531062340b0554c163e997481545a111dde
        B/clauses/window-02/raw.json: 07ab00492fe6e4f861656c6170d00332fd743a664679b8e0d7c70b755f992822
        B/clauses/window-02/prompt.txt: 476414b52ef450e9681f5fad3f172ecd8a773e187b35f255bcf878499b19a0f4
        B/clauses/window-02/meta.json: 9571b297cd3345ac880a7624703928852c3dfed46dd11264b45d49896339577a
        B/clauses/window-01/raw.json: 96a2709435ac3e9399141af03bc3c11bed6439006b5b7c1dd99b032452291f79
        B/clauses/window-01/prompt.txt: a73fbd8ad714b16f4c84ded5401789c952f6270bbbd820d4443b18acd8a85e84
        B/clauses/window-01/meta.json: af6bdc8e1cfa17c626837759d4ea8c295285924464052db93a44ddad15d1d146
        B/tables/TABLE-2-page-5-2/raw.json: d5e204b4026f593443a46f482337155bb36ff476907da4b433372c284affff59
        B/tables/TABLE-2-page-5-2/prompt.txt: 9beded6d4540b530ab67ebe047402c8a43091caae41d05f4fe93a572f6cadf2b
        B/tables/TABLE-2-page-5-2/meta.json: 48e931fd4c214422ca686bf2e65dace95847beaae0b9e0873d9380fb80142807
        B/tables/TABLE-1-page-3-1/raw.json: 62fc3321ee4563b845a04496c600e4c3ed0ec7ffcbc67bff3e359cc5339e435a
        B/tables/TABLE-1-page-3-1/prompt.txt: a38afbcf5703e45ebfb6cc4953b5dc5dac7ca1599a5ec0dcf162267e82c68373
        B/tables/TABLE-1-page-3-1/meta.json: 743627bef78900c1265e31de438dc39119e1ee72f37fca7b4f0553ac7674b495
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
      pdf_sha256: c496e5bcfef9f3c2f1c2d118e283e170fb02c4c4143c562cbb78343319fa139c
      source_review: _compare/relationships-2026-11-16/review-current/Yang2017
      source_status_sha256: c3635759e4a103e638dd37d1d80fb05d36d999e17bc3c18683974b00c34bdaa2
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R003
    exposure:
      text: left SLF WM integrity (FA)
    outcome:
      text: aphasia quotient (AQ), performance quotient (PQ), and cortical quotient (CQ)
    analysis_label: Linear correlation analysis (SLF)
    relation: association
    evidence_ids:
    - P1-S1-C7
    - P5-S1-C1
    - P6-S2-C5
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
      pdf_sha256: c496e5bcfef9f3c2f1c2d118e283e170fb02c4c4143c562cbb78343319fa139c
      source_review: _compare/relationships-2026-11-16/review-current/Yang2017
      source_status_sha256: c3635759e4a103e638dd37d1d80fb05d36d999e17bc3c18683974b00c34bdaa2
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P1-S1-C7
      - Result passage disposed without unit P4-S2-C5
      - Result passage disposed without unit P4-S2-C10
      - Accounting without a linked unit P4-S2-C8
      - Accounting without a linked unit P4-S2-C9
      - Accounting without a linked unit P5-S1-C1
      - Accounting without a linked unit P5-S1-C2
      - Result passage disposed without unit P5-S1-C5
      - Unaccounted source passage P4-S2-C8
      - Unaccounted source passage P5-S1-C1
      - Unaccounted source passage P4-S2-C9
      - Unaccounted source passage P5-S1-C2
      - Accounting without a linked unit P6-S1-C1
      - Accounting without a linked unit P6-S1-C3
      - Unaccounted source passage P6-S1-C1
      - Unaccounted source passage P6-S1-C3
      - Result passage disposed without unit P7-S1-C1
      unattached_null_or_qualifier_ids:
      - P4-S2-C4
      - P4-S2-C5
      suppressed_nonrepresented_units: 3
      default_disposition_count_requires_completeness_check: 87
      unselected_timing_passages:
      - P1-S1-C3
      - P2-S3-C6
      - P2-S3-C7
      - P3-S1-C13
      - P5-S2-C2
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P5-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: descriptive_personal_factors
        source_ids:
        - P1-S1-C3
        - P2-S3-C6
        - P2-S3-C7
        - P3-S1-C2
        - P3-S1-C3
        - P3-S1-C13
        - P3-S1-C15
        - P3-S1-C16
        - P3-S1-C17
        - P4-S2-C5
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - validation
      - analysis_restrictions
      - personal_factors
      - tested_personal_effects
      - adjustment_roles
      - explicitly_not_adjusted
      - descriptive_personal_factors
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-3-1
      - TABLE-2-page-5-2
      unlinked_tables:
      - TABLE-1-page-3-1
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness. Figures are not automatically interpreted.
        caption_candidate_units:
        - P4-S1
        - P4-S2
        - P5-S2
        - P6-S1
        - P6-S2
      approval: Not performed. Structural checks and model selections do not establish semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: c496e5bcfef9f3c2f1c2d118e283e170fb02c4c4143c562cbb78343319fa139c
      source_review: _compare/relationships-2026-11-16/review-current/Yang2017
      source_status_sha256: c3635759e4a103e638dd37d1d80fb05d36d999e17bc3c18683974b00c34bdaa2
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C6
      disposition: represented
      result_indexes:
      - 0
      reason: Reports decreased WM integrity in left IFOF/ILF, UF, and SLF in aphasic patients.
    - source_id: P1-S1-C7
      disposition: represented
      result_indexes:
      - 1
      - 2
      reason: Reports positive correlation of left IFOF and SLF integrity with AQ, PQ, and CQ.
    - source_id: P4-S2-C4
      disposition: represented
      result_indexes:
      - 3
      reason: Describes the mixed model used to examine interaction between AQ and PQ.
    - source_id: P4-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Contains demographic comparison results (non-significant differences).
    - source_id: P4-S2-C7
      disposition: represented
      result_indexes:
      - 0
      reason: States four WM tracts had lower FA values in patients.
    - source_id: P4-S2-C8
      disposition: represented
      result_indexes:
      - 0
      reason: Specifies decreased FA in left IFOF, ILF, UF, and SLF.
    - source_id: P4-S2-C9
      disposition: represented
      result_indexes:
      - 1
      reason: Provides specific correlation values for left IFOF with AQ, PQ, and CQ.
    - source_id: P4-S2-C10
      disposition: unresolved
      result_indexes: []
      reason: Sentence is truncated in provided text; does not contain a complete finding.
    - source_id: P5-S1-C1
      disposition: represented
      result_indexes:
      - 2
      reason: Provides specific correlation values for left SLF with AQ, PQ, and CQ.
    - source_id: P5-S1-C2
      disposition: represented
      result_indexes:
      - 3
      reason: Reports no interaction effect between AQ and PQ associated with FA in IFOF and SLF.
    - source_id: P5-S1-C5
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of decreased WM integrity in ventral and dorsal pathways.
    - source_id: P5-S1-C7
      disposition: repeated
      result_indexes:
      - 1
      - 2
      reason: Restatement of positive correlations for SLF and IFOF with AQ, PQ, and CQ.
    - source_id: P5-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discusses consistency with previous studies.
    - source_id: P5-S2-C4
      disposition: represented
      result_indexes:
      - 0
      reason: Specifies decreased FA in the anterior segment of the SLF.
    - source_id: P5-S2-C12
      disposition: repeated
      result_indexes:
      - 0
      reason: Figure 2 caption restating lower FA in patients.
    - source_id: P6-S1-C1
      disposition: repeated
      result_indexes:
      - 2
      reason: Restatement of SLF association with AQ and PQ.
    - source_id: P6-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of the SLF's role in phonological processing.
    - source_id: P6-S1-C3
      disposition: repeated
      result_indexes:
      - 0
      - 1
      reason: Restatement of decreased FA in IFOF/ILF and its association with AQ and PQ.
    - source_id: P6-S1-C8
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of decreased FA in the UF.
    - source_id: P6-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion linking UF damage to semantic processing based on previous studies.
    - source_id: P6-S2-C5
      disposition: represented
      result_indexes:
      - 1
      - 2
      reason: Figure 3 caption stating positive correlations for IFOF and SLF with AQ, PQ, and CQ.
    - source_id: P7-S1-C1
      disposition: repeated
      result_indexes:
      - 0
      reason: Conclusion restating reduction in FA in SLF and IFL/IFOF.
    - source_id: P7-S1-C3
      disposition: repeated
      result_indexes:
      - 1
      - 2
      reason: Conclusion restating that impaired WM integrity contributed to language and cognitive status.
    unresolved_coverage: []
    pending_source_ids:
    - P4-S2-C4
    - P4-S2-C5
    - P4-S2-C10
    - P5-S1-C5
    - P5-S1-C7
    - P5-S2-C3
    - P5-S2-C4
    - P5-S2-C12
    - P6-S1-C1
    - P6-S1-C2
    - P6-S1-C3
    - P6-S1-C8
    - P6-S1-C9
    - P7-S1-C1
    - P7-S1-C3
    pending_policy: Every result passage without direct candidate evidence remains pending, including model-labelled background and restatements; those labels never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-3-1
    - TABLE-2-page-5-2
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P1-S1-C3
      - P3-S1-C13
      recruited_sample:
      - P1-S1-C3
      - P3-S1-C13
      eligibility:
      - P2-S3-C7
      - P2-S3-C8
      - P3-S1-C3
      imaging_provenance:
      - P4-S1-C7
      - P5-S2-C10
      imaging_timing:
      - P3-S1-C2
      - P3-S1-C18
      outcome_timing:
      - P3-S1-C2
      outcome_definition:
      - P3-S1-C6
      - P3-S1-C7
      - P3-S1-C8
      - P3-S1-C11
      - P3-S1-C12
      validation: []
      analysis_restrictions: []
      dependent_variable_statement:
      - P4-S1-C15
      - P4-S2-C2
      limitations:
      - P6-S1-C11
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles: []
      explicitly_not_adjusted: []
      descriptive_personal_factors: []
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P5-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for inspection only
    - slot: descriptive_personal_factors
      source_ids:
      - P1-S1-C3
      - P2-S3-C6
      - P2-S3-C7
      - P3-S1-C2
      - P3-S1-C3
      - P3-S1-C13
      - P3-S1-C15
      - P3-S1-C16
      - P3-S1-C17
      - P4-S2-C5
      reason: Runaway selection (>8 passages); entire slot requires source review
    policy: All slots and enums remain unverified. Held selections are not evidence of absence. Original response is preserved in frame/raw.json.
  approved: false
  source_check:
    profile: agent-repair
    scope: Agent corrected this draft against the original paper. The original automated attempt is retained as historical provenance and does not verify this revised version. Human PDF review and approval remain required. TBSS-defined SLF mean FA correlations; corrected the method from LSM to DTI.
    binding:
      source_pdf_sha256: c496e5bcfef9f3c2f1c2d118e283e170fb02c4c4143c562cbb78343319fa139c
      original_source_sha256: 957355db4de7876d0b4c610a30a3f0412a2fa9d40a58cf8a55f1e4d9cfdb2c71
      repair_audit: logs/publication/draft-repairs-2026-11-26.json
      agent_repair_approved: false
    approved: false
    pending_details:
    - Detailed statistics, atlas/reference-space and structured confounder metadata not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Specific R and P values for SLF correlations are not transcribed in the draft but are present in source P4-S2-C10 and P5-S1-C1.
    normalizations: []
    analysis_identity:
      id: R003
      exposure:
        text: left SLF WM integrity (FA)
      outcome:
        text: aphasia quotient (AQ), performance quotient (PQ), and cortical quotient (CQ)
      analysis_label: Linear correlation analysis (SLF)
      relation: association
      evidence_ids:
      - P1-S1-C7
      - P5-S1-C1
      - P6-S2-C5
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
        pdf_sha256: c496e5bcfef9f3c2f1c2d118e283e170fb02c4c4143c562cbb78343319fa139c
        source_review: _compare/relationships-2026-11-16/review-current/Yang2017
        source_status_sha256: c3635759e4a103e638dd37d1d80fb05d36d999e17bc3c18683974b00c34bdaa2
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P2-S3-C6:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: c496e5bcfef9f3c2f1c2d118e283e170fb02c4c4143c562cbb78343319fa139c
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 2f0fec5fcbbe578b028c96062e60529cc144c1deb5d996878f61a71e77382bca
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S3-C6
          page: 2
          text_layer_sha256: 2f0fec5fcbbe578b028c96062e60529cc144c1deb5d996878f61a71e77382bca
          models: &id001
          - gemma4:31b
          - qwen3.8:27b
          model_digests: &id002
          - 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
          - 47951e4a666180bc2aedfc93c169472f2de783696fe196efbf063f5730ecf163
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Materials and Methods

          Subjects

          Eighteen aphasia patients (all right-handed, six females;

          age, 53.67 ± 13.66 years) were recruited from admission

          at the Fuzhou Hospital.'
        anchor_text: 'Materials and Methods

          Subjects

          Eighteen aphasia patients (all right-handed, six females;

          age, 53.67 ± 13.66 years) were recruited from admission

          at the Fuzhou Hospital.'
        excluded_fragments: []
        image_sha256: 4d171f75be90ec92b44c89138e5a067b376fb17d601322a50119f381f222fd0d
        transcription: 'Materials and Methods


          Subjects


          Eighteen aphasia patients (all right-handed, six females; age, 53.67 ± 13.66 years) were recruited from admission at the Fuzhou Hospital'
      P2-S3-C7:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: c496e5bcfef9f3c2f1c2d118e283e170fb02c4c4143c562cbb78343319fa139c
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 7ea3f1bf02c638b19f89666f1c9e87adc49e2da9f97360da1bcc774c4f8ddfe2
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S3-C7
          page: 2
          text_layer_sha256: 7ea3f1bf02c638b19f89666f1c9e87adc49e2da9f97360da1bcc774c4f8ddfe2
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Patients were recruited retrospec-

          tively according to the following criteria: (1) ﬁrst stroke

          occurred in the left hemisphere; (2) age of [18 and

          \85 years; (3) Chinese native speaker; (4) aphasia per-

          sistent at day 1 post-stroke; and (5) right-handed.'
        anchor_text: 'Patients were recruited retrospec-

          tively according to the following criteria: (1) ﬁrst stroke

          occurred in the left hemisphere; (2) age of [18 and

          \85 years; (3) Chinese native speaker; (4) aphasia per-

          sistent at day 1 post-stroke; and (5) right-handed.'
        excluded_fragments: []
        image_sha256: ccdcafd535ed65eeefda2d7eac06f6f96e9267e57c41c81f560d22fa8803788d
        transcription: '. Patients were recruited retrospec-

          tively according to the following criteria: (1) first stroke

          occurred in the left hemisphere; (2) age of >18 and

          <85 years; (3) Chinese native speaker; (4) aphasia per-

          sistent at day 1 post-stroke; and (5) right-handed'
      P3-S1-C2:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: c496e5bcfef9f3c2f1c2d118e283e170fb02c4c4143c562cbb78343319fa139c
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: aec0b2be7bba49fc1f2ae62b5bdf0475cb08cc2d916e833f4c7bf842398bf33e
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S1-C2
          page: 3
          text_layer_sha256: aec0b2be7bba49fc1f2ae62b5bdf0475cb08cc2d916e833f4c7bf842398bf33e
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'All patients experienced a single left-hemisphere

          ischemic (n = 16) or hemorrhagic (n = 2) stroke (lesion

          size: 30.60 ± 42.23 cm3) and underwent MRI for an

          average of 9.7 ± 5.3 days after stroke (Table 1).'
        anchor_text: 'All patients experienced a single left-hemisphere

          ischemic (n = 16) or hemorrhagic (n = 2) stroke (lesion

          size: 30.60 ± 42.23 cm3) and underwent MRI for an

          average of 9.7 ± 5.3 days after stroke (Table 1).'
        excluded_fragments: []
        image_sha256: 39aca7ffe94c89dea203290fc7835ebe89d94bfdc4bc3b6036e36de3ffe18668
        transcription: '. All patients experienced a single left-hemisphere

          ischemic (n = 16) or hemorrhagic (n = 2) stroke (lesion

          size: 30.60 ± 42.23 cm³) and underwent MRI for an

          average of 9.7 ± 5.3 days after stroke (Table 1)'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
    publication_correction:
      date: '2026-11-26T00:24:06.569756+00:00'
      by: agent:source-repair
      approved: false
      human_verification_required: true
      original_source_sha256: 957355db4de7876d0b4c610a30a3f0412a2fa9d40a58cf8a55f1e4d9cfdb2c71
      source_pdf_sha256: c496e5bcfef9f3c2f1c2d118e283e170fb02c4c4143c562cbb78343319fa139c
      pdf_pages:
      - 4
      - 5
      note: TBSS-defined SLF mean FA correlations; corrected the method from LSM to DTI.
      audit: logs/publication/draft-repairs-2026-11-26.json
    checked_by: agent:source-repair (human approval pending)
    date: '2026-11-26'
    corrections:
    - TBSS-defined SLF mean FA correlations; corrected the method from LSM to DTI.
    original_scope: Independent model text review of core meaning; not human approval or complete PDF verification
    original_core_review:
      own_result_source_ids:
      - P1-S1-C7
      - P5-S1-C1
      source_result: 'The study reports a positive correlation between the white matter integrity (FA) of the left superior longitudinal fasciculus (SLF) and three clinical scores: aphasia quotient (AQ), performance quotient (PQ), and cortical quotient (CQ) in patients with acute aphasia. The correlations were derived from mean FA values extracted from significantly different clusters identified via TBSS.'
      result_status: detected
      patient_measurement: voxel_tissue
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis is a linear correlation between left SLF FA and clinical quotients (AQ, PQ, CQ). The source explicitly describes this analysis in P1-S1-C7 and P5-S1-C1, and the method is confirmed in P4-S2-C2 as using mean FA from significant clusters.
          source_ids:
          - P1-S1-C7
          - P5-S1-C1
          - P4-S2-C2
        direction:
          answer: fits
          reason: The source states 'positive correlation' in P1-S1-C7 and P5-S1-C1. The proposed draft claims a positive correlation. The direction is consistent.
          source_ids:
          - P1-S1-C7
          - P5-S1-C1
        construct:
          answer: fits
          reason: Exposure is left SLF FA (P1-S1-C7, P5-S1-C1). Outcome is AQ, PQ, CQ (P1-S1-C7, P5-S1-C1). The measurement is FA from TBSS clusters (P4-S2-C2). The draft correctly identifies these constructs.
          source_ids:
          - P1-S1-C7
          - P5-S1-C1
          - P4-S2-C2
        qualifications:
          answer: fits
          reason: The draft includes the qualification that correlations were analyzed using mean FA values from significantly different clusters identified via TBSS. This matches the method described in P4-S2-C2 and P4-S2-C9/P5-S1-C1.
          source_ids:
          - P4-S2-C2
          - P4-S2-C9
          - P5-S1-C1
        missing_material_caveat:
          answer: fits
          reason: The draft includes the limitation of small sample size (P6-S1-C11). No other material caveats regarding the specific correlation analysis (e.g., adjustment for covariates) are present in the source for this specific result; the source describes unadjusted linear correlations.
          source_ids:
          - P6-S1-C11
      optional_pending:
      - Specific R and P values for SLF correlations are not transcribed in the draft but are present in source P4-S2-C10 and P5-S1-C1.
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    original_profile: core
    original_binding:
      profile: core
      version: core-source-check-v3
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      checker_model: qwen3.8:27b
      checker_digest: 47951e4a666180bc2aedfc93c169472f2de783696fe196efbf063f5730ecf163
      host: http://localhost:11434
      pdf_sha256: c496e5bcfef9f3c2f1c2d118e283e170fb02c4c4143c562cbb78343319fa139c
      review_sha256: 9d8b62fedb301e33d6df69e6c15dadc86200d206dcef61e8a3b63c938ffc49d1
      code_sha256: c4650d24fa3e36e6f317cb65cc7626277a28936a7cdf5d07248d4b1e5bfa09aa
      source_helpers_sha256: e0e0f295e5efa1fdb4e9e8c84ca491d062df3aefe8ca8b4d9ca85fcb6d4c9082
      converter_sha256: 048f1e35905528676837a00b1b2406b1c97cb1eb47c48d63f121a5c00cc0afeb
      table_helpers_sha256: 78e562e9725fc484d6a12279ea710856dfd1d9aa13ee178d0358e9c0acdd2c8c
      mapper_budget: 2500
      reviewer_budget: 1600
      approved: false
      visual:
        models: *id001
        digests: *id002
        code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
        layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
reviewer_marks:
- id: relationship-source-check
  page: 1
  quote: 'In addition, WM integrity of the left IFOF and SLF showed

    a positive correlation with aphasia quotient, performance

    quotient, and cortical quotient, respectively.'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-26'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor roles, all qualifiers, source audit issues and main-PDF tables/figures; check missing results. This model proposal is not verified.'
- id: publication-source-repair-2026-11-26
  status: pending
  by: agent:source-repair
  date: '2026-11-26'
  note: TBSS-defined SLF mean FA correlations; corrected the method from LSM to DTI. Original automated review applies to the original version; verify the corrected finding against the cited pages before approval.
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
