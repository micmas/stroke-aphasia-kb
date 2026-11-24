---
id: hippocampal_integrity_untr_o
name: hippocampal integrity and untrained material success
kind: predictor
findings:
- id: f1
  target: untrained_language_materials_success
  target_kind: prognosis
  claim: Neither reduced volume of the left hippocampus, fractional anisotropy reductions
    in hippocampus adjacent areas, nor infarct proximity were correlated with improved
    naming of untrained language materials.
  direction: no_effect
  relationship: correlational
  method: DTI
  sample:
    n: 10
    population: chronic post-stroke aphasia patients with moderate to severe anomia
      due to a single first-time infarct (primarily MCA)
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
  - Small sample size (N=10)
  - Results cannot be generalized to patients with severe apraxia of speech
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Proximity of MCA occlusion (measured by most proximal
    anatomical region infarcted), left hippocampus volume (measured by T1-weighted
    volumetric ROI analysis), and surrounding white matter integrity (measured by
    mean fractional anisotropy in an expanded ROI minus the hippocampal ROI). The
    lack of correlation for untrained materials is contrasted with significant correlations
    found for trained materials. Additional metadata has not been transcribed; review
    the pending-field flags before approval. PDF image reading (P2-S2-C12, two-model
    agreement, human verification pending): Materials and methods


    Ten consecutively recruited patients (3 women, 7 men; all right-handed, mean age
    50.6 ± 9.2 years, range 34–67; time since stroke 5.42 ± 1.9 years, range 1.8–9.4;
    years of education 12.7 ± 4.6, range 8–20; Table 1 ) with chronic post-stroke
    aphasia due to a single first- Original text-layer quotation is preserved below.
    PDF image reading (P2-S4-C6, two-model agreement, human verification pending):
    . Treatment outcome on both sets

    was assessed immediately after the training (post) and 8 months after the

    training (follow-up), with three runs per picture, respectively Original text-layer
    quotation is preserved below.'
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
    - proposed_concept:untrained_language_materials_success
  therapy:
    id: intensive_naming_treatment
    name: intensive naming treatment
  citation: '@Meinzer2010'
  source_passages:
  - section: Original source P5-S4-C5
    page: 5
    quote: 'Neither reduced volume of

      the left hippocampus and FA-reductions in hippocampus adjacent

      areas, nor infarct proximity was correlated with improved naming of

      UnTrO (proximity: post r=−0.04, p=0.9, follow-up: r−0.22,

      p=0.54; volumetry: post r=−0.02, p=0.96, follow-up: r=0.25,

      p=0.47; ﬁber integrity r=0.14, p=0.69, follow-up: r=0.31,

      p=0.37).'
    supports: claim
  - section: Original source P1-S2-C4
    page: 1
    quote: 'No

      correlations were found for untrained language materials, underlining the speciﬁcity
      of our results for

      training-induced recovery.'
    supports: claim
  - section: Original source P2-S2-C12
    page: 2
    quote: 'Materials and methods

      Ten consecutively recruited patients (3 women, 7 men; all right-

      handed, mean age 50.6±9.2 years, range 34–67; time since stroke

      5.42±1.9 years, range 1.8–9.4; years of education 12.7±4.6, range

      8–20; Table 1) with chronic post-stroke aphasia due to a single ﬁrst-

      '
    supports: sample
  - section: Original source P2-S2-C7
    page: 2
    quote: 'Structural integrity of the hippocampus was determined by means of

      volumetric assessments based on T1-weighted MR scans.'
    supports: method
  - section: Original source P2-S2-C8
    page: 2
    quote: 'Fractional

      anisotropy (FA) maps were derived from diffusion tensor imaging

      (DTI) (Le Bihan, 2003).'
    supports: method
  - section: Original source P2-S4-C6
    page: 2
    quote: 'Treatment outcome on both sets

      was assessed immediately after the training (post) and 8 months after

      the training (follow-up), with three runs per picture, respectively.'
    supports: method
  - section: Original source P7-S4-C7
    page: 7
    quote: 'Thus, our

      results cannot be generalized to patients with severe apraxia of

      speech.'
    supports: limitation
predictor_type: imaging_metric
short_definition: Proximity of MCA occlusion (measured by most proximal anatomical
  region infarcted), left hippocampus volume (measured by T1-weighted volumetric ROI
  analysis), and surrounding white matter integrity (measured by mean fractional anisotropy
  in an expanded ROI minus the hippocampal ROI).
assessment:
- T1-weighted MRI volumetry
- Diffusion Tensor Imaging (DTI) fractional anisotropy
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-25'
relationship_review:
  paper: Meinzer2010
  proposal_id: R004
  review_status_sha256: babd656ad39ec51fa4f70b1d67f8f2d74eff8072b575f7475d48afa42632c63b
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 701ce86728e6b5609ddd53daf9d0c6d8061611f73a80143b6362429019266509
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 701ce86728e6b5609ddd53daf9d0c6d8061611f73a80143b6362429019266509
        A/passages.json: f671ac88ac9e7cd7f6e9fa8995f8a55da35ce67b66ce08866cf92d4189d4dc95
        A/raw.json: 39e1a33d56e735a170f61bf8768d60bd91f9a935d114e6bb395706fc03e6597d
        A/source-units.json: ee5e010eddeb02d8f59e9298a765b372cdca12163aa0d52f4a7f31d62f7ef8f3
        A/full-source-units.json: c6142a4bad82af922768e07eae91f82bca28a9a3987345fe7bc05a8a2ab0f04d
        A/meta.json: 0f99b3da6b44414b09616ddf39cc690488a2e0a85d31165b6646d231a7eb96f6
        A/table-images/TABLE-1-page-3-1.png: 38cf81e618ef2f20c1c169840aa9f52147dbb1ef1b4da13671bc220a5706ca8b
        A/table-images/page-3.png: 1bfdae7a5de1f6ceb6be5b21f56da9c3ff36b66a6ec49284f71d7138df08fe8b
        A/table-images/page-6.png: c1ece83ff9c61f0436fd5057c26e9b0d323210ae2ee50b676a11032665bd072e
        A/table-images/TABLE-2-page-6-1.png: c64f29d898a10e8311ed10ca55e3210fc13e0eceaa2b245f798e7e60b148639b
        A/table-images/manifest.json: 09cef0dde585f7db158f80fafbe9380baf3e0c85e9c4b353ed8c8bbe8ceaaa2c
        A/clauses/window-03/raw.json: 48e87a1faf3c767e14ac2bd78db92f758537cf342c8ba6ae887ed31b580ec2a5
        A/clauses/window-03/prompt.txt: 2d5848123076923e07d6dbc23d4aa1d0fe80b48d5a9d8a6a430096aea1d8e674
        A/clauses/window-03/meta.json: 641f12027b02431a4e6b99deda5d026252da24b45c87e3a5f42d21a62acceb56
        A/clauses/window-04/raw.json: 042a0783ba121173ccb37cbf52838a9bf2a4091376b6ad89fda4a23c02ae2a34
        A/clauses/window-04/prompt.txt: 24d53724b0c9029ddae3cef96b31514c1bce13c95dea83707d6c2405607399fd
        A/clauses/window-04/meta.json: ee822ff8f2dde4769b1f4d8f5db0b9e8351177289fa8722c62026a4f1ca2336d
        A/clauses/window-05/raw.json: 2e057882bc5438045aa625083c5bc1cb126e4695096af5a1b6bcf5dcf541efa2
        A/clauses/window-05/prompt.txt: 62e9b5e38b83e165cee308e0888b06a46740e877f228c8ed53a1e3ed7806e21d
        A/clauses/window-05/meta.json: 220457d2b18233f2169b8a860c9686c525b7f36fc2d5eeec5821e7f089c6f82a
        A/clauses/window-02/raw.json: 41573da3645758be78dc42d995b61df0b81ec8bda4eb85a977e81a0abf593966
        A/clauses/window-02/prompt.txt: 268a479f65a93c6023baee8ba9a6b6c6ef68b3b5a51687e39b78eb1bf594fb30
        A/clauses/window-02/meta.json: e1664c636feee3a6994a1f3e9c5ad34213c28dce8b99249299ef173b1979bfa7
        A/clauses/window-07/raw.json: cd7463470012da79268565211c117b026c79fcb8b2e18705b176689c3d9afe7b
        A/clauses/window-07/prompt.txt: b18c72d4fd2cd9d0d8a6b88ab5679292f79540ab7d801138494140a7b935c112
        A/clauses/window-07/meta.json: ba2a1aba7b8d0fbc4eb26224fcd8905118913e6cf977df4ab338ff03229d6317
        A/clauses/window-01/raw.json: dcc9812ccceb5f0b41f0e932e3b62d67d88e21370de386952042dda1989dd5c7
        A/clauses/window-01/prompt.txt: fb339127d52f9bfdb4abd93f3e5e102a5a4634a490132180cfc5e8492b6afa90
        A/clauses/window-01/meta.json: 09c8a5f466a1d89dcc7514095744458a1280ff631465ca671461499acea6882e
        A/clauses/window-06/raw.json: 58a99a9c32eb1e0b66c2d21f3cfbf28c71963f8300da0827fc194757a7f9698c
        A/clauses/window-06/prompt.txt: 543fd8023ec7c59de99b63e9e67ecb31cba0e51a55f32b702badd2552e3f136b
        A/clauses/window-06/meta.json: 7f2bc5374ecafbad3fefa768d9bb7c8482daf236e207524af1a6da4b611ef6d3
        A/tables/TABLE-2-page-6-2/raw.json: 3f81b3486ad33e3f534db3038c6811e80c698e6868d4f65fb84ce6f8ab3219b5
        A/tables/TABLE-2-page-6-2/prompt.txt: a2ebdde752490f33a9c003f6799089d659a347db1e3323321c5acb280097c6c5
        A/tables/TABLE-2-page-6-2/meta.json: 1a7e60b2d89e8e1cbbd53c01e143c5cfbc9c11418a1a7f87ae9f40e830a57f27
        A/tables/TABLE-1-page-3-1/raw.json: 4e3b8b8d448c87ac089cfd07ccde091fabe14388a8baa6a16e842c83d6239162
        A/tables/TABLE-1-page-3-1/prompt.txt: 8afaba71c34743cf2d23dfc436adf7bf468c015386eba35e5dc26eded7180c61
        A/tables/TABLE-1-page-3-1/meta.json: cdc9ec3d4176a50fdc43ec8632339cc11f9cbce434b6c2e13ba430891d0b03ac
        B/passages.json: f671ac88ac9e7cd7f6e9fa8995f8a55da35ce67b66ce08866cf92d4189d4dc95
        B/raw.json: c473c04b80cdc512ed4d964415d8ce39ea4d6325d4f90e7713cf4004c01c53f9
        B/source-units.json: ee5e010eddeb02d8f59e9298a765b372cdca12163aa0d52f4a7f31d62f7ef8f3
        B/full-source-units.json: c6142a4bad82af922768e07eae91f82bca28a9a3987345fe7bc05a8a2ab0f04d
        B/meta.json: 6fc2f4448aa2424a1a3192630fa749805e5db7c0c47b5b5b038376e9b603a5c0
        B/table-images/TABLE-1-page-3-1.png: 38cf81e618ef2f20c1c169840aa9f52147dbb1ef1b4da13671bc220a5706ca8b
        B/table-images/page-3.png: 1bfdae7a5de1f6ceb6be5b21f56da9c3ff36b66a6ec49284f71d7138df08fe8b
        B/table-images/page-6.png: c1ece83ff9c61f0436fd5057c26e9b0d323210ae2ee50b676a11032665bd072e
        B/table-images/TABLE-2-page-6-1.png: c64f29d898a10e8311ed10ca55e3210fc13e0eceaa2b245f798e7e60b148639b
        B/table-images/manifest.json: 4faf4aaa3d7c0862eb9dd249ca1ebcb5ae5630590c8631711d61c77a88fbca47
        B/clauses/window-03/raw.json: a9ef3a4cc6696f3824931bb48a0b5486cf5afec821c3689295c909ad2daf8305
        B/clauses/window-03/prompt.txt: 2d5848123076923e07d6dbc23d4aa1d0fe80b48d5a9d8a6a430096aea1d8e674
        B/clauses/window-03/meta.json: bab946a6778eb000e5e800150d2afd877f646d3028a9a6c023ca188e58e61aa8
        B/clauses/window-04/raw.json: 26486f73256596ddcdbaf4794cac80d2f39fef10f160a0c42d17c4e24a1d2dda
        B/clauses/window-04/prompt.txt: 24d53724b0c9029ddae3cef96b31514c1bce13c95dea83707d6c2405607399fd
        B/clauses/window-04/meta.json: 831be203a4b5c227798757ca1df8616efb12b72016983694b08f9eb233c93318
        B/clauses/window-05/raw.json: 97588acf8642b0969622d9a49b6fb8744486cb57bed49a7b8777a7b40847db45
        B/clauses/window-05/prompt.txt: 62e9b5e38b83e165cee308e0888b06a46740e877f228c8ed53a1e3ed7806e21d
        B/clauses/window-05/meta.json: c9515ae9bf522465874156934f79097ff6e29cc015469bf91f471564aee6404a
        B/clauses/window-02/raw.json: fb988e0e8dd17fa6e50831656a3a1fc0c6880f4578f8eb0a2e3001b69503ba98
        B/clauses/window-02/prompt.txt: 268a479f65a93c6023baee8ba9a6b6c6ef68b3b5a51687e39b78eb1bf594fb30
        B/clauses/window-02/meta.json: abf2dc0a72425d9161c9feda0b63ce6476c6bd6d332d31c930599f1ac6ed03f2
        B/clauses/window-07/raw.json: 3aa4cbb4325836f412f8ed99cf071f3132d8a6ec1d1d0500aa2c73518b839398
        B/clauses/window-07/prompt.txt: b18c72d4fd2cd9d0d8a6b88ab5679292f79540ab7d801138494140a7b935c112
        B/clauses/window-07/meta.json: 06b5ae5c6e6ea6a24a2db2c382d88fc6b2fd10918fb664b5397ee787acfacbab
        B/clauses/window-01/raw.json: b63e2d0167d744a5f14d2b3dc3e9ee5cf8a37b0062e71e091dec9d397fdf22bf
        B/clauses/window-01/prompt.txt: fb339127d52f9bfdb4abd93f3e5e102a5a4634a490132180cfc5e8492b6afa90
        B/clauses/window-01/meta.json: a27747d256dd7345f01f74743ace6e0b1a9850f66303fe9263a4d228e43df88f
        B/clauses/window-06/raw.json: 359f87280ccdea043e14c6960f62c251c37a94b4afb89a18da9207cea0f54d8f
        B/clauses/window-06/prompt.txt: 543fd8023ec7c59de99b63e9e67ecb31cba0e51a55f32b702badd2552e3f136b
        B/clauses/window-06/meta.json: fbe064a02f258af3b869264072ffde06ace971fbcf6e9b66102d28374d1f53f7
        B/tables/TABLE-2-page-6-2/raw.json: 5bf8eaf95c9158269a896915bae05739e7ec374a89a4b7d7e14a8ff5e780bc69
        B/tables/TABLE-2-page-6-2/prompt.txt: a2ebdde752490f33a9c003f6799089d659a347db1e3323321c5acb280097c6c5
        B/tables/TABLE-2-page-6-2/meta.json: 7ef7949065734d446c71b1b1577fd764eef078a793065867abcb2d7bc239410b
        B/tables/TABLE-1-page-3-1/raw.json: bb1cf1ef6af50d7c72ce6868b4a75acec0fa216960bf51b11d1f4b760c7ffebf
        B/tables/TABLE-1-page-3-1/prompt.txt: 8afaba71c34743cf2d23dfc436adf7bf468c015386eba35e5dc26eded7180c61
        B/tables/TABLE-1-page-3-1/meta.json: 37ef598c55dd75281efdc712e5f81d33930ac5bdaaaeabb006157642ac175f1a
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
      pdf_sha256: 701ce86728e6b5609ddd53daf9d0c6d8061611f73a80143b6362429019266509
      source_review: _compare/relationships-2026-11-16/review-current/Meinzer2010
      source_status_sha256: c46cb438a0c8c94b28bf350a19e70b328e10f13cb89c84a231291b3f326f3a72
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R004
    exposure:
      text: proximity of MCA occlusion, left hippocampus volume, and surrounding white
        matter integrity
    outcome:
      text: language training success for untrained language materials (UnTrO)
    analysis_label: Specificity of structural correlations for trained materials
    relation: association
    evidence_ids:
    - P1-S2-C4
    - P5-S4-C5
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
      pdf_sha256: 701ce86728e6b5609ddd53daf9d0c6d8061611f73a80143b6362429019266509
      source_review: _compare/relationships-2026-11-16/review-current/Meinzer2010
      source_status_sha256: c46cb438a0c8c94b28bf350a19e70b328e10f13cb89c84a231291b3f326f3a72
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P5-S2-C12
      - Result passage disposed without unit P5-S2-C13
      - Result passage disposed without unit P6-S1-C1
      - Result passage disposed without unit P7-S1-C2
      - Result passage disposed without unit P7-S1-C6
      - Result passage disposed without unit P7-S3-C6
      - Accounting without a linked unit P7-S3-C8
      - Unaccounted source passage P7-S3-C8
      unattached_null_or_qualifier_ids: []
      suppressed_nonrepresented_units: 8
      default_disposition_count_requires_completeness_check: 152
      unselected_timing_passages:
      - P1-S1-C5
      - P2-S2-C12
      - P2-S3-C1
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P5-S4-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S4-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S4-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P5-S2-C6
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P5-S2-C7
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: imaging_provenance
        source_ids:
        - P4-S1-C4
        - P4-S1-C5
        - P4-S1-C6
        - P4-S1-C7
        - P4-S1-C8
        - P4-S1-C9
        - P4-S2-C5
        - P4-S2-C6
        - P4-S2-C7
        - P4-S2-C8
        - P4-S2-C9
        - P4-S2-C10
        - P4-S2-C11
        - P5-S1-C1
        - P5-S1-C2
        - P5-S1-C3
        - P5-S1-C4
        - P5-S1-C5
        - P5-S1-C6
        - P5-S1-C7
        - P5-S1-C8
        - P5-S1-C9
        - P5-S1-C10
        - P5-S1-C11
        - P5-S1-C12
        - P5-S1-C13
        - P5-S1-C14
        - P5-S2-C3
        - P5-S2-C5
        - P5-S2-C6
        - P5-S2-C7
        - P6-S1-C6
        - P7-S1-C5
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - imaging_provenance
      - validation
      - personal_factors
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-3-1
      - TABLE-2-page-6-2
      unlinked_tables: []
      source_anomalies:
      - evidence_id: P5-S3-C10
        as_printed: p=91
        reason: Printed p-value outside [0,1]; verify PDF, never correct automatically
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P3-S2
        - P4-S1
        - P4-S2
        - P5-S1
        - P5-S4
        - P6-S1
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 701ce86728e6b5609ddd53daf9d0c6d8061611f73a80143b6362429019266509
      source_review: _compare/relationships-2026-11-16/review-current/Meinzer2010
      source_status_sha256: c46cb438a0c8c94b28bf350a19e70b328e10f13cb89c84a231291b3f326f3a72
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S2-C3
      disposition: represented
      result_indexes:
      - 0
      - 1
      - 2
      - 3
      - 4
      - 5
      - 6
      reason: States correlations of training success with proximity, hippocampal
        integrity, and null results for lesion size, overall integrity, and control
        region.
    - source_id: P1-S2-C4
      disposition: represented
      result_indexes:
      - 3
      reason: States null correlations for untrained materials.
    - source_id: P2-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes a prior study (Menke et al., 2009).
    - source_id: P2-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes a prior study (Menke et al., 2009).
    - source_id: P4-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: States the intent to assess if proximity is explained by hippocampal
        damage.
    - source_id: P5-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes correlation between different Gaussian kernels used for FA-LIs.
    - source_id: P5-S2-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: States patients tolerated procedures well.
    - source_id: P5-S2-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: States no complaints about motivation.
    - source_id: P5-S3-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: States VAMS scores were within normal range.
    - source_id: P5-S3-C3
      disposition: represented
      result_indexes:
      - 7
      reason: Reports null correlations between VAMS motivation and treatment outcome.
    - source_id: P5-S3-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports general improvement in naming (TIME effect) rather than a relationship
        between an exposure and outcome.
    - source_id: P5-S3-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports interaction between object type and time.
    - source_id: P5-S3-C6
      disposition: represented
      result_indexes:
      - 4
      - 8
      reason: Reports null correlations for duration of aphasia and lesion size with
        TrO success.
    - source_id: P5-S3-C7
      disposition: represented
      result_indexes:
      - 9
      reason: Reports null correlation for speech apraxia severity.
    - source_id: P5-S3-C8
      disposition: represented
      result_indexes:
      - 10
      reason: Reports null correlation for education.
    - source_id: P5-S3-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes patient classification by anomia subtype.
    - source_id: P5-S3-C10
      disposition: represented
      result_indexes:
      - 11
      reason: Reports null correlations for anomia subtype weights.
    - source_id: P5-S3-C12
      disposition: represented
      result_indexes:
      - 0
      reason: Reports that proximal infarcts resulted in smaller treatment gains.
    - source_id: P5-S4-C1
      disposition: represented
      result_indexes:
      - 0
      reason: Repeats finding that proximal infarcts correlate with smaller gains.
    - source_id: P5-S4-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes volumetric size reductions observed in patients.
    - source_id: P5-S4-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes FA-reductions observed in patients.
    - source_id: P5-S4-C4
      disposition: represented
      result_indexes:
      - 1
      - 2
      reason: Reports correlations of volume and FA-reductions with TrO performance
        and retention.
    - source_id: P5-S4-C5
      disposition: represented
      result_indexes:
      - 3
      reason: Reports null correlations for proximity, volume, and FA with UnTrO naming.
    - source_id: P5-S4-C6
      disposition: represented
      result_indexes:
      - 5
      - 6
      reason: Reports null correlations for entire hemisphere FA and control ROI.
    - source_id: P5-S4-C7
      disposition: represented
      result_indexes:
      - 13
      reason: Reports correlation between hippocampal volume impairment and hemisphere
        FA-reductions.
    - source_id: P5-S4-C8
      disposition: represented
      result_indexes:
      - 14
      reason: Reports negative correlation between infarct proximity and volume reductions.
    - source_id: P6-S1-C1
      disposition: represented
      result_indexes:
      - 14
      - 15
      reason: Reports correlations of proximity with volume and FA-reductions.
    - source_id: P6-S1-C2
      disposition: represented
      result_indexes:
      - 16
      reason: Reports null correlations of lesion size with proximity, overall FA,
        and control ROI.
    - source_id: P7-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes observed volume reductions.
    - source_id: P7-S1-C3
      disposition: repeated
      result_indexes:
      - 0
      - 1
      reason: Restates associations between proximity/volume loss and naming improvement.
    - source_id: P7-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes observed FA-reductions.
    - source_id: P7-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Compares FA-reductions to prior findings.
    - source_id: P7-S1-C8
      disposition: repeated
      result_indexes:
      - 2
      reason: Restates correlation between FA-reductions and naming improvement.
    - source_id: P7-S1-C9
      disposition: repeated
      result_indexes:
      - 3
      reason: Restates null correlations for untrained items.
    - source_id: P7-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discusses mechanisms of UnTrO improvement.
    - source_id: P7-S2-C7
      disposition: repeated
      result_indexes:
      - 4
      - 5
      - 6
      reason: Restates null correlations for lesion size, overall FA, and control
        ROI.
    - source_id: P7-S2-C8
      disposition: repeated
      result_indexes:
      - 7
      - 9
      - 10
      - 11
      reason: Restates null correlations for anomia type, apraxia, education, and
        motivation.
    - source_id: P7-S3-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: States neurologist did not observe cystic defects.
    - source_id: P7-S3-C8
      disposition: repeated
      result_indexes:
      - 13
      reason: Restates correlation between hippocampal impairment and FA-reductions.
    - source_id: P7-S4-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discusses general response of lexical-semantic deficits to phonological
        approaches.
    unresolved_coverage:
    - source_id: P5-S3-C12
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P6-S1-C2
      disposition: unresolved
      reason: Unknown result index; not accepted as coverage
    pending_source_ids:
    - P2-S1-C7
    - P2-S1-C8
    - P4-S1-C3
    - P5-S2-C5
    - P5-S2-C12
    - P5-S2-C13
    - P5-S3-C2
    - P5-S3-C4
    - P5-S3-C5
    - P5-S3-C9
    - P5-S4-C2
    - P5-S4-C3
    - P7-S1-C2
    - P7-S1-C3
    - P7-S1-C6
    - P7-S1-C7
    - P7-S1-C8
    - P7-S1-C9
    - P7-S2-C6
    - P7-S2-C7
    - P7-S2-C8
    - P7-S3-C6
    - P7-S4-C2
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-3-1
    - TABLE-2-page-6-2
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P2-S3-C1
      recruited_sample:
      - P2-S3-C1
      eligibility:
      - P2-S3-C1
      - P2-S3-C4
      - P7-S4-C6
      imaging_provenance: []
      imaging_timing:
      - P3-S1-C7
      outcome_timing:
      - P2-S4-C6
      - P5-S2-C10
      outcome_definition:
      - P2-S2-C11
      - P5-S2-C10
      validation: []
      analysis_restrictions:
      - P5-S2-C6
      - P5-S2-C7
      dependent_variable_statement:
      - P2-S2-C11
      - P5-S2-C10
      limitations:
      - P7-S4-C7
      personal_factors: []
      tested_personal_effects:
      - P5-S3-C3
      - P5-S3-C6
      - P5-S3-C7
      - P5-S3-C8
      - P5-S3-C10
      - P7-S2-C7
      - P7-S2-C8
      adjustment_roles:
      - P5-S2-C11
      explicitly_not_adjusted:
      - P7-S2-C7
      descriptive_personal_factors:
      - P2-S3-C1
      - P3-S3-C1
    outcome_type: both_reported
    imaging_vs_outcome: precedes_outcome
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P5-S4-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S4-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S4-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P5-S2-C6
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P5-S2-C7
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: imaging_provenance
      source_ids:
      - P4-S1-C4
      - P4-S1-C5
      - P4-S1-C6
      - P4-S1-C7
      - P4-S1-C8
      - P4-S1-C9
      - P4-S2-C5
      - P4-S2-C6
      - P4-S2-C7
      - P4-S2-C8
      - P4-S2-C9
      - P4-S2-C10
      - P4-S2-C11
      - P5-S1-C1
      - P5-S1-C2
      - P5-S1-C3
      - P5-S1-C4
      - P5-S1-C5
      - P5-S1-C6
      - P5-S1-C7
      - P5-S1-C8
      - P5-S1-C9
      - P5-S1-C10
      - P5-S1-C11
      - P5-S1-C12
      - P5-S1-C13
      - P5-S1-C14
      - P5-S2-C3
      - P5-S2-C5
      - P5-S2-C6
      - P5-S2-C7
      - P6-S1-C6
      - P7-S1-C5
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
      pdf_sha256: 701ce86728e6b5609ddd53daf9d0c6d8061611f73a80143b6362429019266509
      review_sha256: babd656ad39ec51fa4f70b1d67f8f2d74eff8072b575f7475d48afa42632c63b
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
      - P1-S2-C4
      - P5-S4-C5
      source_result: No statistically significant correlations were found between
        the proximity of the MCA occlusion, left hippocampus volume reduction, or
        fractional anisotropy (FA) reductions in hippocampus-adjacent white matter
        and language training success for untrained materials (UnTrO). This null result
        is presented to demonstrate the specificity of the significant correlations
        observed for trained materials.
      result_status: not_detected
      patient_measurement: multiple
      checks:
        analysis_identity:
          answer: fits
          reason: 'The selected analysis R004 correctly identifies the specific statistical
            comparison: the correlation of structural predictors (proximity, volume,
            FA) with the outcome for untrained materials (UnTrO). The source passages
            P1-S2-C4 and P5-S4-C5 explicitly report this null finding, distinguishing
            it from the positive findings for trained materials.'
          source_ids:
          - P1-S2-C4
          - P5-S4-C5
        direction:
          answer: fits
          reason: The proposed core correctly characterizes the result as 'no_effect'
            (no statistically detected association). The source data in P5-S4-C5 lists
            p-values > 0.05 for all predictors regarding UnTrO, confirming the absence
            of a significant correlation. The direction is faithful to the null finding.
          source_ids:
          - P5-S4-C5
          - P1-S2-C4
        construct:
          answer: fits
          reason: The exposure (MCA proximity, left hippocampus volume, surrounding
            white matter integrity) and outcome (UnTrO success) are correctly identified.
            The patient measurement is 'multiple' because the analysis aggregates
            three distinct structural metrics (proximity score, volumetric LI, FA
            LI) rather than a single imaging modality or template overlap. The method
            is correctly identified as correlational.
          source_ids:
          - P5-S4-C5
          - P2-S2-C11
          - P4-S1-C4
          - P4-S1-C13
        qualifications:
          answer: fits
          reason: The qualification that the null result for untrained materials is
            contrasted with significant correlations for trained materials is accurate
            and supported by P1-S2-C4 ('underlining the specificity of our results
            for training-induced recovery') and P5-S4-C4 (which reports the significant
            correlations for TrO). This context is essential for interpreting the
            null as a specificity check rather than a general lack of effect.
          source_ids:
          - P1-S2-C4
          - P5-S4-C4
          - P5-S4-C5
        missing_material_caveat:
          answer: fits
          reason: The proposed core includes the limitation regarding severe apraxia
            of speech (P7-S4-C7) and the small sample size. No material caveats that
            would change the interpretation of the null result for UnTrO are omitted.
            The distinction between trained and untrained materials is preserved.
          source_ids:
          - P7-S4-C7
          - P2-S2-C12
      optional_pending:
      - sample.time_post_onset
      - exact_p_values_for_untr_o
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
    - exact_p_values_for_untr_o
    normalizations:
    - field: sample.time_post_onset
      original: measured immediately after 2 weeks of intensive therapy and at 8 months
        follow-up
      action: not_transcribed
      reason: 'Numbers not grounded in usable selected source readings: 2'
    analysis_identity:
      id: R004
      exposure:
        text: proximity of MCA occlusion, left hippocampus volume, and surrounding
          white matter integrity
      outcome:
        text: language training success for untrained language materials (UnTrO)
      analysis_label: Specificity of structural correlations for trained materials
      relation: association
      evidence_ids:
      - P1-S2-C4
      - P5-S4-C5
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
        pdf_sha256: 701ce86728e6b5609ddd53daf9d0c6d8061611f73a80143b6362429019266509
        source_review: _compare/relationships-2026-11-16/review-current/Meinzer2010
        source_status_sha256: c46cb438a0c8c94b28bf350a19e70b328e10f13cb89c84a231291b3f326f3a72
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P2-S2-C12:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 701ce86728e6b5609ddd53daf9d0c6d8061611f73a80143b6362429019266509
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: d9e8f5bd077818f13ec61db0d777a2638b389e6373e683c5bbeba7f7d126d176
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S2-C12
          page: 2
          text_layer_sha256: de64c88c739caccce1efe9476a70851b27d475ff0f856c854e549ed1b9a30c22
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Materials and methods

          Ten consecutively recruited patients (3 women, 7 men; all right-

          handed, mean age 50.6±9.2 years, range 34–67; time since stroke

          5.42±1.9 years, range 1.8–9.4; years of education 12.7±4.6, range

          8–20; Table 1) with chronic post-stroke aphasia due to a single ﬁrst-

          '
        anchor_text: 'Materials and methods

          Ten consecutively recruited patients (3 women, 7 men; all right-

          handed, mean age 50.6±9.2 years, range 34–67; time since stroke

          5.42±1.9 years, range 1.8–9.4; years of education 12.7±4.6, range

          8–20; Table 1) with chronic post-stroke aphasia due to a single ﬁrst-'
        excluded_fragments: []
        image_sha256: d32a234e66d90975831e7628efe87f61c86b80577ddfac0e23cd96a49025fd15
        transcription: 'Materials and methods


          Ten consecutively recruited patients (3 women, 7 men; all right-handed,
          mean age 50.6 ± 9.2 years, range 34–67; time since stroke 5.42 ± 1.9 years,
          range 1.8–9.4; years of education 12.7 ± 4.6, range 8–20; Table 1 ) with
          chronic post-stroke aphasia due to a single first-'
      P2-S4-C6:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 701ce86728e6b5609ddd53daf9d0c6d8061611f73a80143b6362429019266509
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 12ee25459e1e11a547c021fcd92e7effa0b540b32a727319267dcd7536044ba1
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S4-C6
          page: 2
          text_layer_sha256: 12ee25459e1e11a547c021fcd92e7effa0b540b32a727319267dcd7536044ba1
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Treatment outcome on both sets

          was assessed immediately after the training (post) and 8 months after

          the training (follow-up), with three runs per picture, respectively.'
        anchor_text: 'Treatment outcome on both sets

          was assessed immediately after the training (post) and 8 months after

          the training (follow-up), with three runs per picture, respectively.'
        excluded_fragments: []
        image_sha256: 6133b591b4057dd2df666124f46b1cdf4094e86dfd5eb622e0e1a1e4d8c6f073
        transcription: '. Treatment outcome on both sets

          was assessed immediately after the training (post) and 8 months after the

          training (follow-up), with three runs per picture, respectively'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 5
  quote: 'Neither reduced volume of

    the left hippocampus and FA-reductions in hippocampus adjacent

    areas, nor infarct proximity was correlated with improved naming of

    UnTrO (proximity: post r=−0.04, p=0.9, follow-up: r−0.22,

    p=0.54; volumetry: post r=−0.02, p=0.96, follow-up: r=0.25,

    p=0.47; ﬁber integrity r=0.14, p=0.69, follow-up: r=0.31,

    p=0.37).'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-25'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
