---
id: thalamic_infarct_volume
name: thalamic infarct volume
kind: predictor
findings:
- id: f1
  target: naming_impairment_severity
  target_kind: impairment
  claim: There was no significant correlation between the volume of thalamic infarct
    and the severity of naming impairment.
  direction: no_effect
  relationship: correlational
  method: LSM
  sample:
    n: 10
    population: patients with isolated left thalamic infarcts
    phase: not_reported
    time_post_onset: MRI and cognitive testing performed within 24 to 48 hours of
      symptom onset
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - low spatial resolution of DWI scans prevented determination of which specific
    thalamic nuclei were affected
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Volume of infarct measured by manual modification
    of a threshold of >30% intensity increase from the unaffected area on diffusion-weighted
    imaging (DWI). analysis performed on the subset of patients with left thalamic
    lesions. Additional metadata has not been transcribed; review the pending-field
    flags before approval. PDF image reading (P3-S2-C3, two-model agreement, human
    verification pending): A subset of 10 participants had isolated left thalamic
    infarct

    (infarct limited to the thalamus); (6 men and 4 women) and

    10 participants had isolated right thalamic lesions (8 men and

    2 women) Original text-layer quotation is preserved below. PDF image reading (P3-S1-C7,
    two-model agreement, human verification pending): . All participants were admitted
    and

    received MRI within 24 h of symptom onset Original text-layer quotation is preserved
    below.'
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
    - proposed_concept:naming_impairment_severity
  citation: '@Sebastian2014'
  source_passages:
  - section: Original source P4-S3-C7
    page: 4
    quote: 'Fur-

      ther, there was no signiﬁcant correlation between volume of thal-

      amic infarct and severity of the naming impairment ( ρ = −0.098;

      Frontiers in Neurology | Stroke

      November 2014 | Volume 5 | Article 231 | 4


      '
    supports: claim
  - section: Original source P3-S2-C12
    page: 3
    quote: 'To measure the volume of infarct for each patient, a threshold

      of >30% intensity increase from the unaffected area in the DWI

      was applied, and a neurologist (KO), blinded to the behavioral

      data, manually modiﬁed the boundary of the thresholded area to

      remove false-positive and false-negative areas on RoiEditor1 (51).'
    supports: method
  - section: Original source P3-S2-C3
    page: 3
    quote: 'A subset of 10 participants had isolated left thalamic infarct

      (infarct limited to the thalamus); (6 men and 4 women) and

      10 participants had isolated right thalamic lesions (8 men and

      2 women).'
    supports: sample
  - section: Original source P3-S1-C7
    page: 3
    quote: 'All participants were admitted and

      received MRI within 24 h of symptom onset.'
    supports: method
  - section: Original source P3-S3-C10
    page: 3
    quote: 'White matter hyperintensities were rated

      using the Cardiovascular Health Study (CHS) rating scale (rang-

      ing from 0 to 9, with 9 being “most extensive”). 0 was considered

      “none”; scores of 1–3 were considered“mild”; 3–6“moderate,”and

      7–9 “severe.”

      TEST BATTERY

      All participants received testing within 48 h from admission to the

      hospital.'
    supports: method
  - section: Original source P3-S2-C5
    page: 3
    quote: 'We were

      unable to determine which thalamic nuclei were affected due to the

      low spatial resolution of the DWI scans relative to thalamic nuclei.'
    supports: limitation
predictor_type: imaging_metric
short_definition: Volume of infarct measured by manual modification of a threshold
  of >30% intensity increase from the unaffected area on diffusion-weighted imaging
  (DWI).
assessment:
- oral naming of black and white pictures
- oral naming of objects with tactile input
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-25'
relationship_review:
  paper: Sebastian2014
  proposal_id: R005
  review_status_sha256: 15304b086aa046487f0664d2886e7ad4102d507070155d4bfe361c1f26d4c9da
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 2bcfe7ba9dff472faeb5095d27c65d17947145be08cb9d8f31586651ffcd9836
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 2bcfe7ba9dff472faeb5095d27c65d17947145be08cb9d8f31586651ffcd9836
        A/passages.json: 12688c0cabbd4c46bd9616bbffdc33abd5dad966f3d7d90ee5f1ef62ad8f34c1
        A/raw.json: 95268bc7a94c76de55ea84377e680889906d6abe0f1990030c7f7b1b1328f9cd
        A/source-units.json: 8d92bb826eb84f9f8cb6781ce12ce65c04bcb34107e4a65308dfb2a2b6000875
        A/full-source-units.json: bc8c995f79ff08e11d7cfdce3805509b9d31aebb03e4071313008f230bebba6f
        A/meta.json: fb1a723602f038844744002132f88c3e65c7f4f7b63ccdb457be4058e8959d92
        A/table-images/page-6.png: 00865cb11a3172205da94e17d673361c2eb5b3458ff2e5ed76c6d7e249be97d5
        A/table-images/page-4.png: 6aa57928e9d2f52e2e1bda0666f1de1e8c01a2d368af639c92faafd452b1ec17
        A/table-images/TABLE-1-page-4-1.png: 322f6ed6303795b2335a49fe219ea40c0be9cf03aa25a1fc635ea0c855373919
        A/table-images/TABLE-3-page-6-1.png: fc5edbc3eeca53e50ff9114c551c19c4872858a639bd061260af16981025a5f2
        A/table-images/TABLE-4-page-6-2.png: d6d5830aadc98bf57b79b86ec56b467bb7657958fb4d221e133af542102f487b
        A/table-images/TABLE-2-page-4-2.png: 0f8c827ffb119159ba08e27d753dfd5c99a929021371b035fb0706b042ab3c0d
        A/table-images/manifest.json: 45137971390ff09726fb52e9350fac0f1c32966b8003cd3c7b22294b6e421603
        A/clauses/window-03/raw.json: 57140d7f2dd34d50efef548982e9e10c6eab31c03e63bb265d7c045da404ee89
        A/clauses/window-03/prompt.txt: 14080d1547075174b251b708c62a048fcef1dea1fd46c69f6284dbb87dbd5283
        A/clauses/window-03/meta.json: 96126b2edf9e552b550d5b07e4b8bd0c04250cb2a157a94dfaf1bb459e267c95
        A/clauses/window-04/raw.json: 2d31631ec5947d354b1834c7893456f385618bf57ca17113374c5644c025e52b
        A/clauses/window-04/prompt.txt: 28ff1122b7e014862e854b1d3982115922f1bc57c8baf98f7948f6864ceddfc4
        A/clauses/window-04/meta.json: 426357aaec1cdc99048875e636069263e2c82e9f06845d8f3bd37fd949aaa1d7
        A/clauses/window-05/raw.json: 4becb2447209fefbd611dc23414129a9ed92b5a16a6f78b25b718a5b3fd1e15e
        A/clauses/window-05/prompt.txt: bde43a48ecbe33adf0e70f0bc8cdef93eff43ff2dece660de306ccbbd475b404
        A/clauses/window-05/meta.json: a4d058c6e4d61b6f4a4b340c3dcbcd76610e1f97d83b7dffc9914b70a3022d48
        A/clauses/window-02/raw.json: b609e9e4ab57032de3d0c4a13f40620b6cdf4946e94d251fee2bac5b4ec14a27
        A/clauses/window-02/prompt.txt: 51325a87c1a321c4806bb80e891823bbcb64c1f35e6b4fb3577d349165026535
        A/clauses/window-02/meta.json: afab922f6bdf97393e1205c00263fb6639cc0fbf3bfb477bc98f34a22c43b4e5
        A/clauses/window-07/raw.json: 5cc1f2b733dedc3500f1042c474c9c2920b5dab9562bc976ca5fadad0988126e
        A/clauses/window-07/prompt.txt: f799b801b7597e153fa89f00b44a538f5a45d151cd64242c27177d1b7957d094
        A/clauses/window-07/meta.json: 2706d02781b0f43f53a80e5e0f2e5427738f15c3f704e878bdbece5a6a4b6522
        A/clauses/window-01/raw.json: 846a9f2f32d842591f93bed2bc2f1d5e4153cbc8f701a9dcd4d7e3f48e080e55
        A/clauses/window-01/prompt.txt: bf5c12fe67f409cc89d3f6a557b9846ac93b8c863a34600ad590005930046a35
        A/clauses/window-01/meta.json: 42e358ec803455041b67ee458189626dddac3715c39e326b04f72b6971d0b0d6
        A/clauses/window-06/raw.json: 8f20f384723f32e69a8d3ace2487f4be68fd1ab2342e9859392cf71489f430fa
        A/clauses/window-06/prompt.txt: e4a852bc2be0fd310a918be3699969a0b2812ab0420614f82edeaf61acd59a96
        A/clauses/window-06/meta.json: 4ab2d0cba8b274095bf96ecfeabe33a84197d970b96b3af33f7f85dde789df7e
        A/tables/TABLE-4-page-6-4/raw.json: b034d6aa022ba4df25013b3fbe9859e68a19bac66a6be2d979a7a7eae135fca8
        A/tables/TABLE-4-page-6-4/prompt.txt: 3d6d9d01f11ea1160c8c47e80fb85d801ff65eeff7e62d143b460cd67b887a92
        A/tables/TABLE-4-page-6-4/meta.json: 94bb05aff885661a98538aa1c3375547f63d3e896b23bf7d6971c0440f8544fa
        A/tables/TABLE-3-page-6-3/raw.json: 8d9cf25d38ab0761c54f8e63ffa9726b1242608ce12d654abc65758b8c7ab5c2
        A/tables/TABLE-3-page-6-3/prompt.txt: ec02c56a30de1cf2d9ac3e547649b87aa5731f56cd5a620e2a74d6f26f9ea32f
        A/tables/TABLE-3-page-6-3/meta.json: 8e9bdec2f0d60b5ca68da7ee45703ff941860997e5c3cbfff5d8014c69d8cfe5
        A/tables/TABLE-1-page-4-1/raw.json: 9b9f7a27b26c9b551225dc411f73d1335540ea17805832ae4b6ebc76853d5284
        A/tables/TABLE-1-page-4-1/prompt.txt: 148f2311a879a96bfafc14d298773fab0bb747655f97f90d637dd8d36d6efcdb
        A/tables/TABLE-1-page-4-1/meta.json: b3cfcea82ce712be096f9ddda321dadabd3e91e28ba8535ca55be22032789542
        A/tables/TABLE-2-page-4-2/raw.json: 072eda190e8aceb225d248d4d1efa32aa7dc377b8983900e737b6bc35a60b25d
        A/tables/TABLE-2-page-4-2/prompt.txt: 3cf3912df1f709865c90a83f349787a291117ff01ea81ad973be7db2c3aab2f7
        A/tables/TABLE-2-page-4-2/meta.json: 8748ca907868b3fce41ed1a37d1e885dc5573f334d0311305b4b347ca88ef234
        B/passages.json: 12688c0cabbd4c46bd9616bbffdc33abd5dad966f3d7d90ee5f1ef62ad8f34c1
        B/raw.json: e87ddfb581d2e0fef7b98e5adad4baf9dc6106bab4fcad0e6f4dd262a1284da9
        B/source-units.json: 8d92bb826eb84f9f8cb6781ce12ce65c04bcb34107e4a65308dfb2a2b6000875
        B/full-source-units.json: bc8c995f79ff08e11d7cfdce3805509b9d31aebb03e4071313008f230bebba6f
        B/meta.json: 4e4fd7e795d403352534abad3611b18699a243c4e51a6654ba3b680c1e9d67e4
        B/table-images/page-6.png: 00865cb11a3172205da94e17d673361c2eb5b3458ff2e5ed76c6d7e249be97d5
        B/table-images/page-4.png: 6aa57928e9d2f52e2e1bda0666f1de1e8c01a2d368af639c92faafd452b1ec17
        B/table-images/TABLE-1-page-4-1.png: 322f6ed6303795b2335a49fe219ea40c0be9cf03aa25a1fc635ea0c855373919
        B/table-images/TABLE-3-page-6-1.png: fc5edbc3eeca53e50ff9114c551c19c4872858a639bd061260af16981025a5f2
        B/table-images/TABLE-4-page-6-2.png: d6d5830aadc98bf57b79b86ec56b467bb7657958fb4d221e133af542102f487b
        B/table-images/TABLE-2-page-4-2.png: 0f8c827ffb119159ba08e27d753dfd5c99a929021371b035fb0706b042ab3c0d
        B/table-images/manifest.json: b140099f9e95231f9aff4058564f4521a3c22a0be9fc9d95f988334eb8af0a51
        B/clauses/window-03/raw.json: 62522fbd726bde09de4d4870eb3dcfd79e19f739c3aec0b90af69e9616769f9c
        B/clauses/window-03/prompt.txt: 14080d1547075174b251b708c62a048fcef1dea1fd46c69f6284dbb87dbd5283
        B/clauses/window-03/meta.json: fe9754e509856af0046e3fd2ba8dedb866bc0bafce818ff7bea8758c271d3387
        B/clauses/window-04/raw.json: 3bdf03c60e261ea7470a175e06e7fe5cac4bfaedb4b591a116ec8e9264d71d6e
        B/clauses/window-04/prompt.txt: 28ff1122b7e014862e854b1d3982115922f1bc57c8baf98f7948f6864ceddfc4
        B/clauses/window-04/meta.json: f9bae5391d67c28c6e2d257660fd83a5e335fb11d5ddf4e5aad879a0ed0923b3
        B/clauses/window-05/raw.json: b9bd63883f703e8ead09a41e0a349630494d9320eb9102636d2aa5a94f4d8da3
        B/clauses/window-05/prompt.txt: bde43a48ecbe33adf0e70f0bc8cdef93eff43ff2dece660de306ccbbd475b404
        B/clauses/window-05/meta.json: e1154efb24b74195350653ecf298e0c06849fd23a23680262493c92908027f1f
        B/clauses/window-02/raw.json: 2a145c8a3c1a71cb568b834e7c5cc8c9b9ef79bc57ad3aa3fe510a5a2d9ee1cd
        B/clauses/window-02/prompt.txt: 51325a87c1a321c4806bb80e891823bbcb64c1f35e6b4fb3577d349165026535
        B/clauses/window-02/meta.json: 3c153476cdabbdb31cc6600cd22689d2dbcb3f024ac3b6bb2c63e2253a0ab6fc
        B/clauses/window-07/raw.json: 5cc1f2b733dedc3500f1042c474c9c2920b5dab9562bc976ca5fadad0988126e
        B/clauses/window-07/prompt.txt: f799b801b7597e153fa89f00b44a538f5a45d151cd64242c27177d1b7957d094
        B/clauses/window-07/meta.json: 6efac984905867af2df7c7a8e7f9db8f9f38e7b34355f626f7f31839bb8db1f6
        B/clauses/window-01/raw.json: 88884a7a618b5c253ec4cf7670c1d7e502526afddeb53d503ee03e0d738a2138
        B/clauses/window-01/prompt.txt: bf5c12fe67f409cc89d3f6a557b9846ac93b8c863a34600ad590005930046a35
        B/clauses/window-01/meta.json: 04d5f50ade80f1a176c324f7a37f1eb7e59e559ef00be8395013635f12102a24
        B/clauses/window-06/raw.json: 11eecb40a04ccd7c5eb23dfcb1acac9b633da44e479f65e72012addfeb1c92f3
        B/clauses/window-06/prompt.txt: e4a852bc2be0fd310a918be3699969a0b2812ab0420614f82edeaf61acd59a96
        B/clauses/window-06/meta.json: 9ffc33bf9f97019ee8706bf2b91169286c22bc98a9548b6173dab13f78b2b695
        B/tables/TABLE-4-page-6-4/raw.json: 9c934d7cad09e81e85ccffd99c298a83b9ff0f682733abbb602c8e5299d17ddf
        B/tables/TABLE-4-page-6-4/prompt.txt: 3d6d9d01f11ea1160c8c47e80fb85d801ff65eeff7e62d143b460cd67b887a92
        B/tables/TABLE-4-page-6-4/meta.json: bc4169595a2e0ee4c25665c980e5efa24f9d4864671dcb4c0f7e258e71dcfbb8
        B/tables/TABLE-3-page-6-3/raw.json: de2013ae3f21e1781117469eaace755a6ff4257ed9bb8332c5f218ab4699c3e4
        B/tables/TABLE-3-page-6-3/prompt.txt: ec02c56a30de1cf2d9ac3e547649b87aa5731f56cd5a620e2a74d6f26f9ea32f
        B/tables/TABLE-3-page-6-3/meta.json: bfa1203866c805817a0a327ea3643bfe081c4a6ec121794bee959107dce887ab
        B/tables/TABLE-1-page-4-1/raw.json: fe55e8318ea09d7f2bc4260477f736ed2e30f47241143c1775e13e315b44679a
        B/tables/TABLE-1-page-4-1/prompt.txt: 148f2311a879a96bfafc14d298773fab0bb747655f97f90d637dd8d36d6efcdb
        B/tables/TABLE-1-page-4-1/meta.json: 18d5f617177cb8466ab19e1f97378557cb351af232721657b204f9702320d060
        B/tables/TABLE-2-page-4-2/raw.json: 9e64ff1f2e37cbd54b8f0ec970a61ebd9b3a127bf034d0b191eca029eb55f961
        B/tables/TABLE-2-page-4-2/prompt.txt: 3cf3912df1f709865c90a83f349787a291117ff01ea81ad973be7db2c3aab2f7
        B/tables/TABLE-2-page-4-2/meta.json: 501d7330a1223ed109c8bb7c833703123d7316c81c3023e4c4121c9b4b2b9c66
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
      pdf_sha256: 2bcfe7ba9dff472faeb5095d27c65d17947145be08cb9d8f31586651ffcd9836
      source_review: _compare/relationships-2026-11-16/review-current/Sebastian2014
      source_status_sha256: 45b140731764cb66224f7c734338e63e088966a541eb4164f4852da7800f648b
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R005
    exposure:
      text: volume of thalamic infarct
    outcome:
      text: severity of naming impairment
    analysis_label: Correlation between naming impairment severity and thalamic infarct
      volume
    relation: association
    evidence_ids:
    - P4-S3-C7
    - P5-S1-C4
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
      pdf_sha256: 2bcfe7ba9dff472faeb5095d27c65d17947145be08cb9d8f31586651ffcd9836
      source_review: _compare/relationships-2026-11-16/review-current/Sebastian2014
      source_status_sha256: 45b140731764cb66224f7c734338e63e088966a541eb4164f4852da7800f648b
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Accounting without a linked unit P3-S2-C15
      - Accounting without a linked unit P4-S2-C5
      - Unaccounted source passage P4-S2-C5
      - Unaccounted source passage P3-S2-C15
      - Result passage disposed without unit P4-S2-C7
      - Result passage disposed without unit P4-S2-C8
      - Result passage disposed without unit P4-S2-C9
      - Result passage disposed without unit P4-S3-C4
      - Result passage disposed without unit P4-S3-C5
      - Accounting without a linked unit P4-S3-C6
      - Accounting without a linked unit P4-S3-C7
      - Result passage disposed without unit P5-S1-C4
      - Result passage disposed without unit P5-S1-C5
      - Result passage disposed without unit P5-S1-C6
      - Result passage disposed without unit P5-S1-C7
      - Accounting without a linked unit P5-S1-C8
      - Unaccounted source passage P4-S3-C6
      - Unaccounted source passage P5-S1-C8
      - Unaccounted source passage P4-S3-C7
      - Result passage disposed without unit P5-S1-C11
      - Result passage disposed without unit P5-S1-C9
      - Result passage disposed without unit P6-S2-C3
      - Result passage disposed without unit P6-S2-C4
      - Result passage disposed without unit P7-S1-C13
      unattached_null_or_qualifier_ids:
      - P6-S2-C3
      suppressed_nonrepresented_units: 13
      default_disposition_count_requires_completeness_check: 141
      unselected_timing_passages:
      - P1-S1-C8
      - P3-S1-C6
      - P3-S2-C4
      - P3-S2-C7
      - P6-S2-C12
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P5-S1-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P3-S2-C13
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      empty_frame_slots_require_confirmation:
      - validation
      - personal_factors
      - tested_personal_effects
      - adjustment_roles
      - explicitly_not_adjusted
      unclassified_extraction_ids:
      - P1-S2-C13
      table_review_required:
      - TABLE-1-page-4-1
      - TABLE-2-page-4-2
      - TABLE-3-page-6-3
      - TABLE-4-page-6-4
      unlinked_tables:
      - TABLE-1-page-4-1
      - TABLE-2-page-4-2
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P4-S2
        - P5-S1
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 2bcfe7ba9dff472faeb5095d27c65d17947145be08cb9d8f31586651ffcd9836
      source_review: _compare/relationships-2026-11-16/review-current/Sebastian2014
      source_status_sha256: 45b140731764cb66224f7c734338e63e088966a541eb4164f4852da7800f648b
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S2-C2
      disposition: represented
      result_indexes:
      - 0
      - 1
      reason: Reports that aphasia occurred in left thalamic infarcts without cortical
        hypoperfusion, while neglect occurred only with cortical hypoperfusion.
    - source_id: P3-S2-C15
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes inter-observer reliability of infarct volume measurement.
    - source_id: P4-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: References demographic tables.
    - source_id: P4-S2-C5
      disposition: represented
      result_indexes:
      - 0
      reason: Provides count of aphasia in left thalamic lesion group.
    - source_id: P4-S2-C6
      disposition: represented
      result_indexes:
      - 0
      reason: States four of five aphasic patients had normal cortical perfusion.
    - source_id: P4-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes speech fluency of aphasic patients.
    - source_id: P4-S2-C8
      disposition: represented
      result_indexes:
      - 0
      reason: Details naming deficits and associated normal cortical perfusion.
    - source_id: P4-S2-C9
      disposition: represented
      result_indexes:
      - 0
      reason: Details naming/comprehension impairment and associated cortical hypoperfusion.
    - source_id: P4-S2-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the location of hypoperfusion in aphasic cases.
    - source_id: P4-S3-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes counts of patients without aphasia.
    - source_id: P4-S3-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes a patient without language deficit who had hypoperfusion.
    - source_id: P4-S3-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes location of hypoperfusion in a non-aphasic patient.
    - source_id: P4-S3-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Lists other neurological deficits.
    - source_id: P4-S3-C6
      disposition: represented
      result_indexes:
      - 0
      reason: Reports no association between left cortical hypoperfusion and naming
        or comprehension impairment.
    - source_id: P4-S3-C7
      disposition: represented
      result_indexes:
      - 4
      reason: Reports no significant correlation between thalamic infarct volume and
        naming impairment severity.
    - source_id: P5-S1-C4
      disposition: represented
      result_indexes:
      - 4
      - 5
      reason: Reports no significant correlation between thalamic infarct volume and
        naming or comprehension impairment severity.
    - source_id: P5-S1-C5
      disposition: represented
      result_indexes:
      - 1
      reason: Reports count of neglect in right thalamic lesions.
    - source_id: P5-S1-C6
      disposition: represented
      result_indexes:
      - 1
      reason: States both neglect patients had cortical hypoperfusion.
    - source_id: P5-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the area of hypoperfusion in neglect cases.
    - source_id: P5-S1-C8
      disposition: represented
      result_indexes:
      - 1
      reason: Reports chi-square result for association between neglect and cortical
        hypoperfusion.
    - source_id: P5-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Lists other neurological deficits.
    - source_id: P5-S1-C10
      disposition: represented
      result_indexes:
      - 2
      - 3
      reason: Reports correlation of neglect severity with hypoperfusion volume (positive)
        and thalamic lesion volume (null).
    - source_id: P5-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes distribution of lesions.
    - source_id: P5-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: States insufficient data to determine association with white matter
        intensities.
    - source_id: P6-S2-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of thalamus's role in language via cortical influence.
    - source_id: P6-S2-C3
      disposition: repeated
      result_indexes:
      - 1
      reason: Restates that 2/10 right thalamic patients had neglect and both had
        hypoperfusion.
    - source_id: P6-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Explains the cause of the observed delay in PWI.
    - source_id: P6-S2-C5
      disposition: repeated
      result_indexes:
      - 2
      - 3
      reason: Restates correlation of neglect severity with hypoperfusion volume over
        infarct volume.
    - source_id: P6-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the arterial territory of lesions in neglect patients.
    - source_id: P7-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: References prior study on white matter disease and neglect.
    - source_id: P7-S1-C11
      disposition: repeated
      result_indexes:
      - 1
      reason: Summary statement that some neglect is due to cortical hypoperfusion.
    - source_id: P7-S1-C13
      disposition: repeated
      result_indexes:
      - 0
      reason: Summary statement that this mechanism was not identified in thalamic
        aphasia.
    unresolved_coverage: []
    pending_source_ids:
    - P3-S2-C15
    - P4-S2-C4
    - P4-S2-C5
    - P4-S2-C7
    - P4-S2-C8
    - P4-S2-C9
    - P4-S2-C13
    - P4-S3-C2
    - P4-S3-C3
    - P4-S3-C4
    - P4-S3-C5
    - P5-S1-C5
    - P5-S1-C6
    - P5-S1-C7
    - P5-S1-C9
    - P5-S1-C11
    - P5-S1-C12
    - P6-S2-C1
    - P6-S2-C3
    - P6-S2-C4
    - P6-S2-C5
    - P6-S2-C9
    - P7-S1-C6
    - P7-S1-C11
    - P7-S1-C13
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-4-1
    - TABLE-2-page-4-2
    - TABLE-3-page-6-3
    - TABLE-4-page-6-4
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P3-S1-C6
      recruited_sample:
      - P3-S1-C6
      eligibility:
      - P3-S1-C8
      imaging_provenance:
      - P3-S2-C9
      imaging_timing:
      - P3-S1-C7
      - P3-S2-C8
      outcome_timing:
      - P3-S3-C11
      outcome_definition:
      - P3-S3-C5
      validation: []
      analysis_restrictions:
      - P4-S2-C1
      dependent_variable_statement:
      - P4-S2-C2
      - P4-S2-C3
      limitations:
      - P6-S2-C6
      - P6-S2-C11
      - P7-S2-C2
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles: []
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P3-S2-C4
      - P5-S1-C12
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P5-S1-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P3-S2-C13
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
      pdf_sha256: 2bcfe7ba9dff472faeb5095d27c65d17947145be08cb9d8f31586651ffcd9836
      review_sha256: 15304b086aa046487f0664d2886e7ad4102d507070155d4bfe361c1f26d4c9da
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
      - P4-S3-C7
      - P5-S1-C4
      source_result: In patients with isolated left thalamic infarcts, there was no
        significant correlation between the volume of thalamic infarct and the severity
        of naming impairment (Spearman's rho = -0.098, p = 0.79).
      result_status: not_detected
      patient_measurement: regional_lesion_load
      checks:
        analysis_identity:
          answer: fits
          reason: The source explicitly describes a Spearman's rank correlation between
            thalamic infarct volume and naming impairment severity in the left thalamic
            lesion group (P4-S3-C7, P5-S1-C4). The proposed core correctly identifies
            this specific analysis.
          source_ids:
          - P4-S3-C7
          - P5-S1-C4
          - P4-S2-C3
        direction:
          answer: fits
          reason: The source reports a non-significant correlation (p=0.79). The proposed
            core characterizes this as 'no_effect' (no statistically detected association),
            which is faithful to the null result. It does not claim a zero effect,
            but rather the absence of a detected association.
          source_ids:
          - P4-S3-C7
          - P5-S1-C4
        construct:
          answer: fits
          reason: The exposure is correctly identified as thalamic infarct volume,
            measured via DWI thresholding (P3-S2-C12). The outcome is naming impairment
            severity, assessed via oral naming tasks (P3-S3-C13). The population is
            restricted to left thalamic infarcts (P3-S2-C3). The measurement is regional
            lesion load (volume), not template overlap or patient diffusion tractography.
          source_ids:
          - P3-S2-C12
          - P3-S3-C13
          - P3-S2-C3
        qualifications:
          answer: fits
          reason: The core correctly restricts the finding to the subset of patients
            with left thalamic lesions. The source explicitly separates left and right
            thalamic groups, and this correlation is reported for the left group (P4-S3-C7).
          source_ids:
          - P4-S3-C7
          - P3-S2-C3
        missing_material_caveat:
          answer: fits
          reason: The core includes the limitation regarding low spatial resolution
            of DWI preventing nuclear identification (P3-S2-C5). No other material
            caveats that would change the interpretation of this specific null correlation
            are omitted. The small sample size (n=10) is inherent to the group definition
            and the null result is reported as such.
          source_ids:
          - P3-S2-C5
          - P3-S2-C3
      optional_pending:
      - Exact Spearman rho value (-0.098) and p-value (0.79) not transcribed in core
        fields
      - Specific naming subtests contributing to 'severity' score not fully detailed
        in core assessment list
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Exact Spearman rho value (-0.098) and p-value (0.79) not transcribed in core
      fields
    - Specific naming subtests contributing to 'severity' score not fully detailed
      in core assessment list
    normalizations: []
    analysis_identity:
      id: R005
      exposure:
        text: volume of thalamic infarct
      outcome:
        text: severity of naming impairment
      analysis_label: Correlation between naming impairment severity and thalamic
        infarct volume
      relation: association
      evidence_ids:
      - P4-S3-C7
      - P5-S1-C4
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
        pdf_sha256: 2bcfe7ba9dff472faeb5095d27c65d17947145be08cb9d8f31586651ffcd9836
        source_review: _compare/relationships-2026-11-16/review-current/Sebastian2014
        source_status_sha256: 45b140731764cb66224f7c734338e63e088966a541eb4164f4852da7800f648b
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P3-S2-C3:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 2bcfe7ba9dff472faeb5095d27c65d17947145be08cb9d8f31586651ffcd9836
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 2997421b8a3261c9188bb2354f0d399a3e537bad55e5944f52bcff5dac326f8a
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S2-C3
          page: 3
          text_layer_sha256: 2997421b8a3261c9188bb2354f0d399a3e537bad55e5944f52bcff5dac326f8a
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'A subset of 10 participants had isolated left thalamic infarct

          (infarct limited to the thalamus); (6 men and 4 women) and

          10 participants had isolated right thalamic lesions (8 men and

          2 women).'
        anchor_text: 'A subset of 10 participants had isolated left thalamic infarct

          (infarct limited to the thalamus); (6 men and 4 women) and

          10 participants had isolated right thalamic lesions (8 men and

          2 women).'
        excluded_fragments: []
        image_sha256: 39efa1c3f4cb0756d5e82f1412d8e75915ccee55f9dc71cd1792b2a1b3f86ea1
        transcription: 'A subset of 10 participants had isolated left thalamic infarct

          (infarct limited to the thalamus); (6 men and 4 women) and

          10 participants had isolated right thalamic lesions (8 men and

          2 women)'
      P3-S1-C7:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 2bcfe7ba9dff472faeb5095d27c65d17947145be08cb9d8f31586651ffcd9836
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: ab1585d6a3297bb1666b9813d619935366c0266c78fbb8534f544412904b30a9
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S1-C7
          page: 3
          text_layer_sha256: ab1585d6a3297bb1666b9813d619935366c0266c78fbb8534f544412904b30a9
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'All participants were admitted and

          received MRI within 24 h of symptom onset.'
        anchor_text: 'All participants were admitted and

          received MRI within 24 h of symptom onset.'
        excluded_fragments: []
        image_sha256: aebb61d716fc602163b96d530334d6a74588dac6e0f7c4fb735c4728ef2ed089
        transcription: '. All participants were admitted and

          received MRI within 24 h of symptom onset'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 4
  quote: 'Fur-

    ther, there was no signiﬁcant correlation between volume of thal-

    amic infarct and severity of the naming impairment ( ρ = −0.098;

    Frontiers in Neurology | Stroke

    November 2014 | Volume 5 | Article 231 | 4


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
