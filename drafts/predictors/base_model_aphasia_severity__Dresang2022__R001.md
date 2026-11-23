---
id: base_model_aphasia_severity
name: Base model for chronic aphasia severity
kind: predictor
findings:
- id: f1
  target: chronic_aphasia_severity
  target_kind: impairment
  claim: More time post-stroke, less total lesion volume, and younger age at stroke
    were associated with milder chronic aphasia.
  direction: likely
  relationship: correlational
  method: behavioral_only
  sample:
    n: 17
    population: adults with a single left-hemisphere ischemic stroke
    phase: not_reported
    time_post_onset: chronic stage (>6 months post-stroke)
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - modest sample size
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: A linear regression model using log-transformed months
    post-stroke onset, total lesion volume, and age at time of stroke. measured as
    a base model before adding genetic or neurophysiological biomarkers. Additional
    metadata has not been transcribed; review the pending-field flags before approval.
    PDF image reading (P4-S1-C3, two-model agreement, human verification pending):
    . Participants were 19 subjects with a single

    left-hemisphere ischemic stroke that occurred >6 months

    prior to participation Original text-layer quotation is preserved below. PDF image
    reading (P4-S1-C8, two-model agreement, human verification pending): This resulted
    in a final sample of 17 participants Original text-layer quotation is preserved
    below.'
  imaging_details:
    reference_space: not_reported
    atlases_used: []
  lesion_mapping: {}
  provenance:
    extracted_by: model:gemma4:31b
    extracted_on: '2026-11-23'
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
    - proposed_concept:chronic_aphasia_severity
  citation: '@Dresang2022'
  source_passages:
  - section: Original source P5-S3-C5
    page: 5
    quote: "More time post-stroke\n(β = 1.18, SE = .21, t = 5.73, P < .001), less\
      \ total lesion\nvolume (β = \x01.07, SE = .003, t = \x0124.47, P < .001),\n\
      and younger age at stroke (β = \x01.77, SE = .02, t = \x0142.27,\nP < .001)\
      \ were associated with milder chronic aphasia."
    supports: claim
  - section: Original source P5-S1-C7
    page: 5
    quote: 'First, a base model included

      factors of interest that are common predictors of aphasia,

      including time post-stroke (log-transformed months post-

      stroke onset; LogMPO), age at time of stroke, and total le-

      sion volume (LesVol).'
    supports: method
  - section: Original source P4-S1-C3
    page: 4
    quote: 'Participants were 19 subjects with a single

      left-hemisphere ischemic stroke that occurred >6 months

      prior to participation.'
    supports: sample
  - section: Original source P4-S1-C8
    page: 4
    quote: This resulted in a ﬁnal sample of 17 participants.
    supports: sample
  - section: Original source P4-S1-C1
    page: 4
    quote: '

      Aphasia Quotient (WAB-AQ37), served as a metric for the

      degree to which language functions recovered post-stroke.'
    supports: method
  - section: Original source P8-S1-C2
    page: 8
    quote: 'A potential limitation of this study is the modest sample

      size used to examine the behavioral effects of a genetic

      polymorphism.'
    supports: limitation
predictor_type: clinical
short_definition: A linear regression model using log-transformed months post-stroke
  onset, total lesion volume, and age at time of stroke.
assessment:
- Western Aphasia Battery Aphasia Quotient
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-23'
relationship_review:
  paper: Dresang2022
  proposal_id: R001
  review_status_sha256: 4b88d30842b38b6be7e5d4a3d400fe3040d2db2711b5a4e660ee293e54309a0b
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 7e68256764564860667022ee47dffce68dd81acb827d14161c732fb89e38c1ec
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 7e68256764564860667022ee47dffce68dd81acb827d14161c732fb89e38c1ec
        A/passages.json: 05361ca184be159b0c5acd34e74f7d21fec838b18b09da7b77cd5bbebae7099d
        A/raw.json: ce90ab38c84b75032e00a3dec5d4eb96d33d51b1843de66ed28139a4c9bf47b3
        A/source-units.json: 9fe055540ee01c422dc07d1484b7398c09ae43920e85a18d88971140a3f2d17e
        A/full-source-units.json: 728b5e920ecf69d796b52e09e5c61720ef6a8cf46f3de49039bbed06f0b0d754
        A/meta.json: d7f95832658863835d3cd1ada718eb020bade7d3549f6135ca8af5698e8ab3c8
        A/table-images/TABLE-1-page-3-1.png: ba360da06ad3e75126bde5c2d7eda09337703adcfca10c6fa215605f8b68c554
        A/table-images/page-3.png: 56f47c9f5d428b40a9e8060e6a624f65f31011926d1e0d635b6f761ddcb442b8
        A/table-images/page-6.png: a548392d2598c10724e095117c3df977928ca6d53eba5c02b293e6ad9c5b7dea
        A/table-images/TABLE-2-page-6-1.png: 8e54e02ee93884aec92450e94ea5d4d02d4f65c3ba716f510592553491a0dcc2
        A/table-images/manifest.json: d37778de9cf0ab8873e60de9ef7c41ddfe15ee249eed318bade3a2241d84909f
        A/clauses/window-03/raw.json: 547c6ae26bcfd1a5b78067de712abfff024dd778d25703889eee8c7d5be92e1a
        A/clauses/window-03/prompt.txt: 241e51d22806ad3ef5f6609f52e6e92963235c8155792e4174d3cbed6fcc1ae0
        A/clauses/window-03/meta.json: de7ad66941ad3d2b0a06bc0dca67d6214e40cd8aede3f3af51d3ac37c702c9dd
        A/clauses/window-04/raw.json: 05a93d1f0073762de82d5f4ec646fcee83911f09bbbb7c42ba266c10b7508f7a
        A/clauses/window-04/prompt.txt: af9e08b603da2566e81dd9bc7deda0d9896c77cc0165e87a8687c2c91767eb54
        A/clauses/window-04/meta.json: 955c5cf0f61355c2e2d5ff56b89407725aace0a1650d559a90514c9a09b913c0
        A/clauses/window-05/raw.json: 17d98aa08da9f4a5a61e0751e460aac290d1492b9a95144bb003178bc076aa8d
        A/clauses/window-05/prompt.txt: bbd8e6d622925fc847ec699297a24a39184258a9781a9296b2f3e017fd9b968e
        A/clauses/window-05/meta.json: 74740d3065fa910a95517ca2cfb1421af0dc4a4e5195ffa99f2b644d1e825766
        A/clauses/window-02/raw.json: 5661672f3468e25217d9490dfa974d6d201c2a071d564b81e66dccfa6521abea
        A/clauses/window-02/prompt.txt: e7e60747bddb67a0067a63754e0c609bb7847ee7d91ccc5eee890f4038bd2d44
        A/clauses/window-02/meta.json: f759c5e8482e011f41a80701c40d72ac98edb775de55b2edee68877a4972378a
        A/clauses/window-07/raw.json: 0f92014d3bb5f1b4be1ae97f8a5797fcc68c23c74cc6d30ef9618fadefa1161f
        A/clauses/window-07/prompt.txt: 7c5af40a96653a7977e2e785b17729c9185739732865affc18b9e3312fc74d73
        A/clauses/window-07/meta.json: 38ca7aa07a5883c15068b4290445125eaed75535d96bfca690b312d1a5640132
        A/clauses/window-01/raw.json: f0bc1eef1040933b3b3b21ab57d04f5a2f70cddaea6f544389c756bc00865a27
        A/clauses/window-01/prompt.txt: ea8dd527defdd019c3f20f3af7dcbe6bf9921871880354e62313c8cb45e491ec
        A/clauses/window-01/meta.json: e5faee545d981e48b588e428d06f2183c1da5d9f3167db6a9172a041f42f7e87
        A/clauses/window-06/raw.json: 6ed6744827b94017afa12602b88fe882613be9cadbd54bcc0cbb888188a73b45
        A/clauses/window-06/prompt.txt: b250653d589a694f80a625344c369efbf52ef7441d7231d4f98477dd33f93cd0
        A/clauses/window-06/meta.json: 35ae7d3d2d6b4be70d5ce7fe409663c577f38e50d5b0d68696f8b237a391d680
        A/tables/TABLE-2-page-6-2/raw.json: a042815eb727cbfd3dc97ed87cdafd721f02657fe4173d6af4ecc43bdab59b86
        A/tables/TABLE-2-page-6-2/prompt.txt: 6ceef2d3039d11821ece1648e5455c1d053bd51e7772f2283991e3333cf537ea
        A/tables/TABLE-2-page-6-2/meta.json: e257d5203e4bb75ed2fa0b3d8f75b82b6930567b93fe3c3682e02ce1190697f4
        A/tables/TABLE-1-page-3-1/raw.json: dda9761efffc5768eaf29c82629ec00685a534e83b3b075e557db4ab0417d567
        A/tables/TABLE-1-page-3-1/prompt.txt: f53beacab1eca3f5b9a1015137f2608751b298426d43b3003f796c8513dec730
        A/tables/TABLE-1-page-3-1/meta.json: 584c11a4ec385c91bc0027640be8c5d0c32f799ea358ca6d805a107fd46a6387
        B/passages.json: 05361ca184be159b0c5acd34e74f7d21fec838b18b09da7b77cd5bbebae7099d
        B/raw.json: 0ada9ca50f1152925c6735eaebe326d5374738672de51c5f09436d6c77662009
        B/source-units.json: 9fe055540ee01c422dc07d1484b7398c09ae43920e85a18d88971140a3f2d17e
        B/full-source-units.json: 728b5e920ecf69d796b52e09e5c61720ef6a8cf46f3de49039bbed06f0b0d754
        B/meta.json: dbe451df022e373d114051115ab813b9a99811d4e4f6095f0d5b7329e209e777
        B/table-images/TABLE-1-page-3-1.png: ba360da06ad3e75126bde5c2d7eda09337703adcfca10c6fa215605f8b68c554
        B/table-images/page-3.png: 56f47c9f5d428b40a9e8060e6a624f65f31011926d1e0d635b6f761ddcb442b8
        B/table-images/page-6.png: a548392d2598c10724e095117c3df977928ca6d53eba5c02b293e6ad9c5b7dea
        B/table-images/TABLE-2-page-6-1.png: 8e54e02ee93884aec92450e94ea5d4d02d4f65c3ba716f510592553491a0dcc2
        B/table-images/manifest.json: 7744024c6be387874ddbe86786773fd5d96679608829549907a22cb44707073c
        B/clauses/window-03/raw.json: 074606f2eb830b4e5c926dd6b47ff45e9ec168676456b914cf41afbb92d89975
        B/clauses/window-03/prompt.txt: 241e51d22806ad3ef5f6609f52e6e92963235c8155792e4174d3cbed6fcc1ae0
        B/clauses/window-03/meta.json: 2339f8416fa346173fcea86d8fe9af414aaa171e2ba9f0aa983d2db84ddca508
        B/clauses/window-04/raw.json: e866ea2437ebaef7113305a382f504f1bd3bcb16e98d68a4ca47073a4e168849
        B/clauses/window-04/prompt.txt: af9e08b603da2566e81dd9bc7deda0d9896c77cc0165e87a8687c2c91767eb54
        B/clauses/window-04/meta.json: ddea7969a438ae1a4b856de0e1b613a5deb5023745913012d945d1fdc2a4d7ea
        B/clauses/window-05/raw.json: fadad8bd40a3710f85189611e50f95226ca96563fc165e2abd899f0a7cfc0f58
        B/clauses/window-05/prompt.txt: bbd8e6d622925fc847ec699297a24a39184258a9781a9296b2f3e017fd9b968e
        B/clauses/window-05/meta.json: 4e55aae89e91a4ca9dd7e104e4484fc7293b9d3991dd01c2b5b972a137f66e5f
        B/clauses/window-02/raw.json: d42efdf01e523365d04e493a0773458205094102ce1f7c997886c47d701a6809
        B/clauses/window-02/prompt.txt: e7e60747bddb67a0067a63754e0c609bb7847ee7d91ccc5eee890f4038bd2d44
        B/clauses/window-02/meta.json: d9331fe208193a1aa8833daadc7ef9a536b9c5afa3b498d86246d3abeea81285
        B/clauses/window-07/raw.json: 3554af8e1c6a898560c1e6cc4fe4c66129dd8d0dd62f02f32abc3e55fafff432
        B/clauses/window-07/prompt.txt: 7c5af40a96653a7977e2e785b17729c9185739732865affc18b9e3312fc74d73
        B/clauses/window-07/meta.json: a65b60e6d0a10910cdf1edd2e7501dfc939fec44ff4be8b7a958405d05aef605
        B/clauses/window-01/raw.json: d482f1de050b1c175c407ad0738c309bdcf39fb5032a5bc28304f42ae3cde1ff
        B/clauses/window-01/prompt.txt: ea8dd527defdd019c3f20f3af7dcbe6bf9921871880354e62313c8cb45e491ec
        B/clauses/window-01/meta.json: 70fae9966e83bf0cabc6829a25d22938f449dde561b9b0d517e99378cd3d482d
        B/clauses/window-06/raw.json: 9555a6c2b62a20e40d72c8492aa74174fa0119766cb431d09654e6f46c7e8782
        B/clauses/window-06/prompt.txt: b250653d589a694f80a625344c369efbf52ef7441d7231d4f98477dd33f93cd0
        B/clauses/window-06/meta.json: 8f417d1858e71adc9c21efae4cf06363b410626811dc57fc4967456b79a44de1
        B/tables/TABLE-2-page-6-2/raw.json: 1712a3cdefb771b73c8bcba8879384e6c0a365c14c3126964c3928e5f71df842
        B/tables/TABLE-2-page-6-2/prompt.txt: 6ceef2d3039d11821ece1648e5455c1d053bd51e7772f2283991e3333cf537ea
        B/tables/TABLE-2-page-6-2/meta.json: 55665df9c077ed42460777d8f6324b40ab96e68970546a9a4d8256c1456655e1
        B/tables/TABLE-1-page-3-1/raw.json: 33bb6533844fda0aa5110fb8162a967986e0cb35af722888ce02db04fda14e24
        B/tables/TABLE-1-page-3-1/prompt.txt: f53beacab1eca3f5b9a1015137f2608751b298426d43b3003f796c8513dec730
        B/tables/TABLE-1-page-3-1/meta.json: 7a006ae5bdfd444e2cc948a04171072bdca37228e0059a72191cc44eca68677e
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
      pdf_sha256: 7e68256764564860667022ee47dffce68dd81acb827d14161c732fb89e38c1ec
      source_review: _compare/relationships-2026-11-16/review-current/Dresang2022
      source_status_sha256: aead4113a6660eb37b82d710b4d27f001286413d90ca54f0e08f453e120bdfbe
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R001
    exposure:
      text: time post-stroke, total lesion volume, and age at stroke
    outcome:
      text: chronic aphasia severity
    analysis_label: Base model regression
    relation: association
    evidence_ids:
    - P5-S3-C5
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
      pdf_sha256: 7e68256764564860667022ee47dffce68dd81acb827d14161c732fb89e38c1ec
      source_review: _compare/relationships-2026-11-16/review-current/Dresang2022
      source_status_sha256: aead4113a6660eb37b82d710b4d27f001286413d90ca54f0e08f453e120bdfbe
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Accounting without a linked unit P1-S1-C14
      - Accounting without a linked unit P1-S1-C15
      - Accounting without a linked unit P1-S2-C3
      - Unaccounted source passage P1-S2-C3
      - Unaccounted source passage P1-S1-C14
      - Unaccounted source passage P1-S1-C15
      - Result passage disposed without unit P5-S1-C4
      - Result passage disposed without unit P5-S2-C2
      - Result passage disposed without unit P5-S2-C5
      - Result passage disposed without unit P5-S2-C11
      - Result passage disposed without unit P5-S3-C2
      - Result passage disposed without unit P5-S3-C3
      - Accounting without a linked unit P5-S3-C5
      - Accounting without a linked unit P5-S3-C6
      - Result passage disposed without unit P5-S3-C7
      - Result passage disposed without unit P6-S1-C1
      - Result passage disposed without unit P6-S1-C4
      - Unaccounted source passage P5-S3-C5
      - Unaccounted source passage P5-S3-C6
      - Result passage disposed without unit P7-S1-C4
      - Result passage disposed without unit P7-S2-C5
      - Result passage disposed without unit P7-S2-C8
      - Result passage disposed without unit P7-S3-C3
      - Unresolved source passage P8-S2-C1
      unattached_null_or_qualifier_ids:
      - P1-S1-C14
      - P5-S2-C2
      - P5-S3-C2
      - P6-S1-C4
      suppressed_nonrepresented_units: 12
      default_disposition_count_requires_completeness_check: 141
      unselected_timing_passages:
      - P1-S1-C11
      - P4-S1-C3
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P6-S1-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C13
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: tested_personal_effects
        source_id: P5-S1-C8
        reason: No current-result classification; a covariate description is not an
          individual test
      empty_frame_slots_require_confirmation:
      - personal_factors
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-3-1
      - TABLE-2-page-6-2
      unlinked_tables:
      - TABLE-1-page-3-1
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P4-S1
        - P4-S3
        - P6-S1
        - P6-S2
        - P7-S1
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 7e68256764564860667022ee47dffce68dd81acb827d14161c732fb89e38c1ec
      source_review: _compare/relationships-2026-11-16/review-current/Dresang2022
      source_status_sha256: aead4113a6660eb37b82d710b4d27f001286413d90ca54f0e08f453e120bdfbe
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C14
      disposition: represented
      result_indexes:
      - 1
      reason: States Val66Val carriers showed less aphasia severity than Val66Met
        carriers after controlling for lesion volume and time.
    - source_id: P1-S1-C15
      disposition: represented
      result_indexes:
      - 2
      - 3
      - 4
      reason: Reports associations between severity and age, cortical excitability,
        and neuroplasticity for Val66Val carriers.
    - source_id: P1-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Abstract fragment continuing a sentence about Val66Met carriers.
    - source_id: P1-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion statement.
    - source_id: P1-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion statement.
    - source_id: P5-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Safety statement regarding cTBS tolerance.
    - source_id: P5-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Explanation for excluding certain interactions due to variance.
    - source_id: P5-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Collinearity check (VIF) results.
    - source_id: P5-S2-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Genotype distribution counts.
    - source_id: P5-S3-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Demographic comparison between BDNF groups.
    - source_id: P5-S3-C3
      disposition: represented
      result_indexes:
      - 0
      reason: States base model predictors accounted for significant variance.
    - source_id: P5-S3-C5
      disposition: represented
      result_indexes:
      - 0
      reason: Details associations of time post-stroke, lesion volume, and age with
        aphasia severity.
    - source_id: P5-S3-C6
      disposition: represented
      result_indexes:
      - 1
      - 8
      reason: Reports BDNF main effect and improvement in model fit.
    - source_id: P6-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Introductory sentence to interaction results.
    - source_id: P6-S1-C4
      disposition: represented
      result_indexes:
      - 6
      reason: States Age x BDNF interaction improved predictions.
    - source_id: P6-S1-C5
      disposition: represented
      result_indexes:
      - 2
      reason: Describes the effect of age on severity across BDNF groups.
    - source_id: P6-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of post-hoc analysis method.
    - source_id: P6-S1-C7
      disposition: represented
      result_indexes:
      - 2
      reason: Specifies interaction effect driven by younger age at CVA.
    - source_id: P6-S1-C9
      disposition: represented
      result_indexes:
      - 7
      reason: States cortical excitability and its interaction with BDNF improved
        model fit.
    - source_id: P6-S1-C10
      disposition: represented
      result_indexes:
      - 3
      reason: Reports opposite associations of cortical excitability with WAB-AQ for
        Val66Val vs Val66Met.
    - source_id: P6-S1-C12
      disposition: represented
      result_indexes:
      - 9
      reason: States stimulation-induced neuroplasticity and its interaction with
        BDNF improved predictions.
    - source_id: P6-S1-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Fragment referring to Table 2.
    - source_id: P6-S1-C16
      disposition: represented
      result_indexes:
      - 6
      - 7
      - 8
      - 9
      reason: Table 2 providing Adjusted R2 and p-values for all model comparisons.
    - source_id: P7-S1-C1
      disposition: represented
      result_indexes:
      - 4
      reason: Reports MEP suppression in both BDNF genotypes.
    - source_id: P7-S1-C2
      disposition: represented
      result_indexes:
      - 4
      reason: Reports stronger MEP suppression effect for Val66Met carriers.
    - source_id: P7-S1-C5
      disposition: repeated
      result_indexes:
      - 1
      reason: Restatement of BDNF main effect in discussion.
    - source_id: P7-S1-C9
      disposition: repeated
      result_indexes:
      - 1
      reason: Restatement of BDNF main effect in discussion.
    - source_id: P7-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: General summary of interaction findings.
    - source_id: P7-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Introductory sentence to age interaction.
    - source_id: P7-S2-C5
      disposition: represented
      result_indexes:
      - 2
      reason: Describes worse outcomes for Val66Met carriers below age 50.
    - source_id: P7-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about indicators being informative for Val66Met.
    - source_id: P7-S2-C9
      disposition: represented
      result_indexes:
      - 3
      reason: Restates opposite patterns of cortical excitability for the two genotypes.
    - source_id: P7-S3-C1
      disposition: represented
      result_indexes:
      - 4
      reason: Associates greater stimulation-induced neuroplasticity with greater
        aphasia severity for Val66Met.
    - source_id: P7-S3-C2
      disposition: represented
      result_indexes:
      - 4
      reason: States stimulation-induced neuroplasticity was not associated with severity
        for Val66Val.
    - source_id: P8-S1-C11
      disposition: repeated
      result_indexes:
      - 1
      reason: Conclusion restatement of BDNF main effect.
    - source_id: P8-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Conclusion summary of interactions.
    - source_id: P8-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion statement.
    unresolved_coverage:
    - source_id: P6-S1-C12
      disposition: unresolved
      reason: Unknown result index; not accepted as coverage
    - source_id: P6-S1-C16
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P5-S3-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P7-S1-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P7-S1-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P7-S1-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P7-S2-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P7-S3-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S1-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S1-C12
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S2-C1
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S2-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S2-C3
    - P1-S2-C4
    - P1-S2-C5
    - P5-S1-C4
    - P5-S2-C2
    - P5-S2-C5
    - P5-S2-C11
    - P5-S3-C2
    - P5-S3-C3
    - P5-S3-C7
    - P6-S1-C1
    - P6-S1-C6
    - P6-S1-C13
    - P7-S1-C4
    - P7-S1-C5
    - P7-S1-C6
    - P7-S1-C8
    - P7-S2-C3
    - P7-S2-C4
    - P7-S2-C7
    - P7-S2-C8
    - P7-S3-C3
    - P8-S1-C3
    - P8-S1-C11
    - P8-S1-C12
    - P8-S2-C1
    - P8-S2-C2
    - P8-S2-C3
    - P8-S2-C10
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
      - P4-S1-C8
      recruited_sample:
      - P4-S1-C3
      eligibility:
      - P4-S1-C3
      - P4-S1-C6
      - P4-S1-C7
      imaging_provenance:
      - P4-S2-C6
      imaging_timing:
      - P4-S1-C12
      - P4-S3-C6
      outcome_timing:
      - P4-S1-C12
      - P4-S3-C6
      outcome_definition:
      - P4-S1-C9
      - P3-S2-C4
      validation:
      - P5-S2-C7
      analysis_restrictions:
      - P5-S2-C2
      dependent_variable_statement:
      - P5-S1-C5
      - P5-S1-C10
      limitations:
      - P8-S1-C2
      - P8-S1-C10
      personal_factors: []
      tested_personal_effects:
      - P6-S1-C10
      - P6-S1-C13
      - P7-S1-C5
      - P7-S2-C9
      adjustment_roles:
      - P1-S1-C14
      - P5-S1-C7
      - P5-S1-C11
      - P5-S1-C12
      - P6-S2-C1
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P3-S2-C5
      - P5-S2-C12
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: internal_cross_validation
    held_selections:
    - slot: dependent_variable_statement
      source_id: P6-S1-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C13
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: tested_personal_effects
      source_id: P5-S1-C8
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
      pdf_sha256: 7e68256764564860667022ee47dffce68dd81acb827d14161c732fb89e38c1ec
      review_sha256: 4b88d30842b38b6be7e5d4a3d400fe3040d2db2711b5a4e660ee293e54309a0b
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
      - P5-S3-C5
      source_result: In the base linear regression model predicting chronic aphasia
        severity (WAB-AQ), more time post-stroke, less total lesion volume, and younger
        age at stroke were significantly associated with milder aphasia (higher WAB-AQ).
      result_status: detected
      patient_measurement: non_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis corresponds to the 'base model' described
            in P5-S1-C7 and P5-S3-C3, which includes LogMPO, LesVol, and AgeCVA as
            predictors of WAB-AQ. The proposed core correctly identifies this specific
            model configuration.
          source_ids:
          - P5-S1-C7
          - P5-S3-C3
          - P5-S3-C5
        direction:
          answer: fits
          reason: The source P5-S3-C5 explicitly states that more time post-stroke,
            less total lesion volume, and younger age at stroke were associated with
            milder chronic aphasia. The proposed claim preserves this directionality
            (milder aphasia = higher WAB-AQ).
          source_ids:
          - P5-S3-C5
        construct:
          answer: fits
          reason: The exposure (time post-stroke, lesion volume, age at stroke) and
            outcome (chronic aphasia severity via WAB-AQ) are correctly identified.
            The patient measurement is non-imaging (behavioral/clinical), as the base
            model relies on demographic and lesion volume data, not direct patient
            imaging metrics like diffusion or functional activation, although lesion
            volume likely derives from imaging, the measurement unit in the model
            is the volume metric itself, not a tract overlap or voxel label. The source
            confirms WAB-AQ is the outcome (P4-S1-C9).
          source_ids:
          - P5-S1-C7
          - P4-S1-C9
          - P5-S3-C5
        qualifications:
          answer: fits
          reason: The qualification that this is a base model before adding genetic/neurophysiological
            biomarkers is supported by P5-S1-C8 and P5-S1-C9, which describe the base
            model as the starting point for subsequent analyses involving BDNF and
            MEPs.
          source_ids:
          - P5-S1-C8
          - P5-S1-C9
        missing_material_caveat:
          answer: fits
          reason: The draft includes the limitation of modest sample size (P8-S1-C2).
            No other material caveats regarding the base model's validity or interpretation
            are omitted that would change the core finding of association.
          source_ids:
          - P8-S1-C2
      optional_pending: []
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    normalizations: []
    analysis_identity:
      id: R001
      exposure:
        text: time post-stroke, total lesion volume, and age at stroke
      outcome:
        text: chronic aphasia severity
      analysis_label: Base model regression
      relation: association
      evidence_ids:
      - P5-S3-C5
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
        pdf_sha256: 7e68256764564860667022ee47dffce68dd81acb827d14161c732fb89e38c1ec
        source_review: _compare/relationships-2026-11-16/review-current/Dresang2022
        source_status_sha256: aead4113a6660eb37b82d710b4d27f001286413d90ca54f0e08f453e120bdfbe
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P5-S3-C5:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 7e68256764564860667022ee47dffce68dd81acb827d14161c732fb89e38c1ec
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: d5d96b8c99ae7a75059ba2602dcb7febe3b9b3152b9ab754141f76616456c812
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P5-S3-C5
          page: 5
          text_layer_sha256: d5d96b8c99ae7a75059ba2602dcb7febe3b9b3152b9ab754141f76616456c812
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: "More time post-stroke\n(β = 1.18, SE = .21, t = 5.73, P <\
          \ .001), less total lesion\nvolume (β = \x01.07, SE = .003, t = \x0124.47,\
          \ P < .001),\nand younger age at stroke (β = \x01.77, SE = .02, t = \x01\
          42.27,\nP < .001) were associated with milder chronic aphasia."
        anchor_text: "More time post-stroke\n(β = 1.18, SE = .21, t = 5.73, P < .001),\
          \ less total lesion\nvolume (β = \x01.07, SE = .003, t = \x0124.47, P <\
          \ .001),\nand younger age at stroke (β = \x01.77, SE = .02, t = \x0142.27,\n\
          P < .001) were associated with milder chronic aphasia."
        excluded_fragments: []
      P4-S1-C3:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 7e68256764564860667022ee47dffce68dd81acb827d14161c732fb89e38c1ec
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 2146c22510c0e1a74d35f1464862199c73ff2506fb1388be44999e56282984d4
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P4-S1-C3
          page: 4
          text_layer_sha256: 2146c22510c0e1a74d35f1464862199c73ff2506fb1388be44999e56282984d4
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Participants were 19 subjects with a single

          left-hemisphere ischemic stroke that occurred >6 months

          prior to participation.'
        anchor_text: 'Participants were 19 subjects with a single

          left-hemisphere ischemic stroke that occurred >6 months

          prior to participation.'
        excluded_fragments: []
        image_sha256: 25717f39a02f55a2e1a30015769cad1ced066fc9dc053c29a5339f2ac32b783b
        transcription: '. Participants were 19 subjects with a single

          left-hemisphere ischemic stroke that occurred >6 months

          prior to participation'
      P4-S1-C8:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 7e68256764564860667022ee47dffce68dd81acb827d14161c732fb89e38c1ec
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 7c1f9b55402da4a24a72108cb325caeabbe806c6d7cde109a2196fcf3d4b8317
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P4-S1-C8
          page: 4
          text_layer_sha256: 7c1f9b55402da4a24a72108cb325caeabbe806c6d7cde109a2196fcf3d4b8317
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: This resulted in a ﬁnal sample of 17 participants.
        anchor_text: This resulted in a ﬁnal sample of 17 participants.
        excluded_fragments: []
        image_sha256: 12e8461feec14e734deadfcaef46b6c14a041700b71ae1178736dbd8a54ce732
        transcription: This resulted in a final sample of 17 participants
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 5
  quote: "More time post-stroke\n(β = 1.18, SE = .21, t = 5.73, P < .001), less total\
    \ lesion\nvolume (β = \x01.07, SE = .003, t = \x0124.47, P < .001),\nand younger\
    \ age at stroke (β = \x01.77, SE = .02, t = \x0142.27,\nP < .001) were associated\
    \ with milder chronic aphasia."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-23'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
