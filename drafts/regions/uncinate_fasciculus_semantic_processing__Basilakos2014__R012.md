---
id: uncinate_fasciculus_semantic_processing
name: uncinate fasciculus
kind: classical
findings:
- id: f1
  target_audit:
    status: behaviour_label_present
    category: behaviour_or_language_construct
    original_target: semantic_processing
    reason: Label names a behaviour or language construct; its exact operational definition and measurement
      still need source review.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  outcome_measurement:
    status: needs_source_review
    instruments: []
    note: Outcome instrument/task is not yet verified for this finding. Do not infer it from the predictor
      or a paper-wide test list.
  target: semantic_processing
  target_kind: impairment
  claim: The integrity of the uncinate fasciculus is correlated with and is the best
    predictor of semantic processing scores.
  direction: likely
  relationship: correlational
  method: LSM
  sample:
    n: 76
    population: chronic post-stroke patients with aphasia following a single left-hemisphere
      ischemic stroke
    phase: not_reported
    time_post_onset: mean time post-stroke 35.57 months (range 6-276); imaging and
      assessment performed concurrently (within 1 month)
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - T1-signal intensity is an indirect measure of tissue integrity
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: mean T1-signal intensity Z-score within a region of
    interest defined by a white matter atlas. when used alone in Pearson correlation;
    best predictor in a stepwise regression model. Additional metadata has not been
    transcribed; review the pending-field flags before approval. PDF image reading
    (P2-S2-C2, two-model agreement, human verification pending): MATERIALS AND METHODS

    PARTICIPANTS

    This study included 76 patients (32 female, 73 right-handed) with chronic aphasia
    who have undergone language testing and MRI studies at the University of South
    Carolina’s Aphasia Lab over a follow-up period of 10 years Original text-layer
    quotation is preserved below. PDF image reading (P2-S2-C9, two-model agreement,
    human verification pending): The mean age of the patients was 61.35 years (SD
    = 12.67,

    range = 36–83), and the mean time post-stroke was 35.57 months

    (SD = 47.56, range = 6–276) Original text-layer quotation is preserved below.
    Reconcile this new analysis with earlier drafts and source-review decisions for
    the paper; new candidate IDs do not carry earlier decisions forward.'
  imaging_details:
    reference_space: not_reported
    atlases_used: []
  lesion_mapping: {}
  provenance:
    extracted_by: model:gemma4:31b
    extracted_on: '2026-11-20'
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
    - prior_paper_decisions_reconciliation_pending
    - proposed_concept:semantic_processing
  citation: '@Basilakos2014'
  source_passages:
  - section: Original source P5-S1-C1
    page: 5
    quote: '

      Basilakos et al.

      White matter damage and ﬂuency

      Semantic processing was correlated with the uncinate fasci-

      culus (r = 0.41, p < 0.001) and the aslant (r = 0.37, p < 0.008),

      but none of the remaining ROIs.'
    supports: claim
  - section: Original source P5-S1-C4
    page: 5
    quote: 'In the stepwise regression model,

      the uncinate fasciculus was found to the best predictor of seman-

      tic processing, F(1,55) = 11.3, p < 0.001, R2 = 0.16.'
    supports: claim
  - section: Original source P2-S2-C2
    page: 2
    quote: 'MATERIALS AND METHODS

      PARTICIPANTS

      This study included 76 patients (32 female, 73 right-handed) with

      chronic aphasia who have undergone language testing and MRI

      studies at the University of South Carolina’s Aphasia Lab over a

      follow-up period of 10 years.'
    supports: sample
  - section: Original source P2-S2-C3
    page: 2
    quote: 'Individuals were included if they had

      a history of one single, left-hemisphere ischemic stroke leading

      to neurological symptoms.'
    supports: sample
  - section: Original source P2-S2-C9
    page: 2
    quote: 'The mean age of the patients was 61.35 years (SD = 12.67,

      range = 36–83), and the mean time post-stroke was 35.57 months

      (SD = 47.56, range = 6–276).'
    supports: sample
  - section: Original source P2-S3-C10
    page: 2
    quote: 'MRI DATA COLLECTION

      All subjects underwent a structural brain anatomy assessment

      using a high-resolution T1-MRI performed at least 6 months after

      the stroke, in close chronological proximity with the language

      testing session (usually within the same day, but no longer than

      1 month apart).'
    supports: method
  - section: Original source P3-S2-C5
    page: 3
    quote: 'Region of interest analyses

      For each subject, we assessed the mean T1-signal intensity Z-score

      within the areas deﬁned by the following white matter regions

      selected as region of interests (ROIs): the ASAF, the uncinate fas-

      ciculus, and the white matter corresponding to the aslant tract.'
    supports: method
  - section: Original source P3-S2-C10
    page: 3
    quote: 'A white matter atlas constructed by Catani et al. (2012) was

      consulted to deﬁne the ASAF, ILF, and the uncinate fasciculus.'
    supports: method
  - section: Original source P2-S3-C6
    page: 2
    quote: 'The Pyramids and Palm

      Trees Test (Howard and Patterson, 1992) served as a non-verbal

      measuretoevaluatesemanticprocessing.'
    supports: method
  - section: Original source P5-S4-C2
    page: 5
    quote: 'Although T1-signal intensity is an indirect

      measure of tissue integrity (and is correlated with T2 hyperin-

      tensities, also an indirect measure of white matter integrity), T1

      images were used as due to better tissue contrast, these scans facil-

      itate more speciﬁc regional assessment of damage.'
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-20'
relationship_review:
  paper: Basilakos2014
  proposal_id: R012
  review_status_sha256: 78abd924bd0754c20b5e9286f8d55341d74f739f8d7d6d769bacd080bde7aa2b
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: ef936e4f2e06d05151975ac93052b5430b4a91bd28862b9a95907eea3746054f
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: ef936e4f2e06d05151975ac93052b5430b4a91bd28862b9a95907eea3746054f
        A/passages.json: 252fa20deef64fcaaa7bfb384be74d25163e7c8b05d3c59d4897072c0f5db518
        A/raw.json: 387d2a3d5d5d3ef774251e73bc434f770f041ff6d98492e3e884d5b2f6e6ade4
        A/source-units.json: 82c8714e90260ce76c6996c23079d876386e7b596c2b123af8a26f44e0207bf4
        A/full-source-units.json: e8eda30b82910da3c5eaab23e87726053ae325bac92dc3a1a78d365524d34076
        A/meta.json: ed8ea8b7751d09bfbf463facbbb50bf746ee6088764b0d90bc670a9bac6fb568
        A/table-images/TABLE-1-page-5-1.png: bca47854bb53f1e2ce90350c385018e34efe66e429f9087926476d75d0ce4105
        A/table-images/page-5.png: 43ad14d17b3ed01eb9a3a75981eda92605cea7e687365575f107a3338786a874
        A/table-images/manifest.json: 6e5a5a61f758c11750b2890d8b3428beda56ce4ad811a8c5b80f27720f6824a6
        A/clauses/window-03/raw.json: ca11d30d399af45c99dc8d881b9ed77b0e1ec7df167857b37595875564772893
        A/clauses/window-03/prompt.txt: 181dfcee0d359239f187947df7df97f6d55573eab86e15a6d3e5ea2b37107732
        A/clauses/window-03/meta.json: 216f744f7d427e6b764b107f8d0870979df442c022634bfc0a6b632d2cf04e0e
        A/clauses/window-04/raw.json: 7422d3550de3b67828bf30f7ae0e0fbfb06862e2ba63bf46768356788188f352
        A/clauses/window-04/prompt.txt: e3fa43602af596835929de79d9d1f8b6905830deb2960f292b6b3b2f26dd9558
        A/clauses/window-04/meta.json: 8bf017ec38b90faf11a5307fb1777d89c401d2bd713969a7149f997c13ebde58
        A/clauses/window-05/raw.json: 6acbd39096886c65726e747fdef9dac95381d8e8cd9ba8e3f31873b5fe024cac
        A/clauses/window-05/prompt.txt: 5a6b5b27c5ba5b6128d52a7c53b5b3ba1de9cea2e3c801184787944d341faddc
        A/clauses/window-05/meta.json: 9cb644007faa1e3e06d9ac729afd4fae91d4721cf0b8a2cd7be1f69e2212415e
        A/clauses/window-02/raw.json: d2270fe483faea4f1967586d9854b131231740168c20c9d7c30c38f5e7039dc3
        A/clauses/window-02/prompt.txt: 703a6b0dfdb4a2ea2debcee1f6a7cecee87f8f7c059988623e45ff7ea31abf62
        A/clauses/window-02/meta.json: 10db06c0c9f2f79857f93346375adeaf64164f7763d0bb14452729f54dd3e8b4
        A/clauses/window-01/raw.json: 97d959b578bb3265d366292cd954b13a5fec232581bab90e5c27c5849ee24af2
        A/clauses/window-01/prompt.txt: 076fbcef95c0f095298ef08747fbc74717598afca20be71051f556d858182183
        A/clauses/window-01/meta.json: 69d3b545fc50ad5591b99509e5fbc432dd35ac8545d22eed2922657a54e9e65d
        A/clauses/window-06/raw.json: 994b811ee046f32fbf2074900fc24a77067cf9ab24a15ea2dbc3b59bbb430b9d
        A/clauses/window-06/prompt.txt: 1e2f3b1636b37a8a8d16452e44703bbf64adff848071fa58c64317e81434af3a
        A/clauses/window-06/meta.json: 15ef8ca5afeffa27874c3a6437c8bbfec2f6f634f27b8e6ff475525d9094b4fe
        A/tables/TABLE-1-page-5-1/raw.json: d3681ab0ba84c974706238d6d0dce697c6b00a568b83bd41384a430099c0b788
        A/tables/TABLE-1-page-5-1/prompt.txt: f232de63e5dea046bd46f8eabdfbb1653d4430e9bf769b3eb3df2d382f2f709e
        A/tables/TABLE-1-page-5-1/meta.json: 064c9e7fbc6bc51db408a047d5f415f4cd3db24b9de6aeeb72246ec05f0793fb
        B/passages.json: 252fa20deef64fcaaa7bfb384be74d25163e7c8b05d3c59d4897072c0f5db518
        B/raw.json: 87529eec5eaff004b93dffa403c17e21c56727d65ba92d7c425c9a70e3f084b5
        B/source-units.json: 82c8714e90260ce76c6996c23079d876386e7b596c2b123af8a26f44e0207bf4
        B/full-source-units.json: e8eda30b82910da3c5eaab23e87726053ae325bac92dc3a1a78d365524d34076
        B/meta.json: 13fe066f33adfda82aa5d0c95138065a2015c4bb4f000c818e38101275a73658
        B/table-images/TABLE-1-page-5-1.png: bca47854bb53f1e2ce90350c385018e34efe66e429f9087926476d75d0ce4105
        B/table-images/page-5.png: 43ad14d17b3ed01eb9a3a75981eda92605cea7e687365575f107a3338786a874
        B/table-images/manifest.json: 936561cc2dad47e24590a38489e6518423ed328c9340ef3ad3beb76aa6e351aa
        B/clauses/window-03/raw.json: 109f53309bdc615d7670a313235eb16d586b62dba479d1091ac4da9f675ac2da
        B/clauses/window-03/prompt.txt: 181dfcee0d359239f187947df7df97f6d55573eab86e15a6d3e5ea2b37107732
        B/clauses/window-03/meta.json: 5b6a0386edfd3bd3473cdd6bf5ff96ae2609e7c7806007a085770ed4377e8f4a
        B/clauses/window-04/raw.json: d38af3752a80e46b6ca4758f2a8b525bf009c2ff10082a78d5bbd3425bbce833
        B/clauses/window-04/prompt.txt: e3fa43602af596835929de79d9d1f8b6905830deb2960f292b6b3b2f26dd9558
        B/clauses/window-04/meta.json: 9ad162c93330faeacde4cc56894369071584f281fadd8057398612df89087aca
        B/clauses/window-05/raw.json: 63e66e3b30105d737435063fe57637aeb9ac9836faee611a46aadf53bffd2b75
        B/clauses/window-05/prompt.txt: 5a6b5b27c5ba5b6128d52a7c53b5b3ba1de9cea2e3c801184787944d341faddc
        B/clauses/window-05/meta.json: 29f880b914b562897d0a10dd2f13ab127636a4f43918394d880e05212127b60a
        B/clauses/window-02/raw.json: 1828a8edc12287e4d719d0e65e42363fa26a05fb60df774a369991ee68dec98f
        B/clauses/window-02/prompt.txt: 703a6b0dfdb4a2ea2debcee1f6a7cecee87f8f7c059988623e45ff7ea31abf62
        B/clauses/window-02/meta.json: 59d99fce79bf516d86f18386aac1a563e98d951e7eceb6e853d40d9a90703137
        B/clauses/window-01/raw.json: 68ade726ce2951117b5f9e86996a26754913a4d36d887c78581e84a5526d8203
        B/clauses/window-01/prompt.txt: 076fbcef95c0f095298ef08747fbc74717598afca20be71051f556d858182183
        B/clauses/window-01/meta.json: d881a3e31a5a670d30eadd726336b15e91669af9370c824b242be906a5f929e9
        B/clauses/window-06/raw.json: 58f4b3b169873f77b8bb97f7219f1c63a1e41e360318a583a6fe0e2d499519b2
        B/clauses/window-06/prompt.txt: 1e2f3b1636b37a8a8d16452e44703bbf64adff848071fa58c64317e81434af3a
        B/clauses/window-06/meta.json: fe7c19dad36f27a0b6ce05755594b7f28aede1f5d9bdc19488700c1dd88e63a2
        B/tables/TABLE-1-page-5-1/raw.json: 4eb00387a7b0b29b5790a4e2ea6eaad199fc84ec8acb3729724b6cd397c1e93e
        B/tables/TABLE-1-page-5-1/prompt.txt: f232de63e5dea046bd46f8eabdfbb1653d4430e9bf769b3eb3df2d382f2f709e
        B/tables/TABLE-1-page-5-1/meta.json: 057337b13ef89d0b294e6573103b0dd7999fc56f70a2b46e0952b669c92b99b4
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
      pdf_sha256: ef936e4f2e06d05151975ac93052b5430b4a91bd28862b9a95907eea3746054f
      source_review: _compare/relationships-2026-11-16/review-current/Basilakos2014
      source_status_sha256: 94fe2915721833240400c299aaebdb918d5182d204e74443476227fcabcc5ce4
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R012
    exposure:
      text: uncinate fasciculus
    outcome:
      text: semantic processing
    analysis_label: Pearson correlation
    relation: association
    evidence_ids:
    - P5-S1-C1
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
      pdf_sha256: ef936e4f2e06d05151975ac93052b5430b4a91bd28862b9a95907eea3746054f
      source_review: _compare/relationships-2026-11-16/review-current/Basilakos2014
      source_status_sha256: 94fe2915721833240400c299aaebdb918d5182d204e74443476227fcabcc5ce4
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P1-S1-C8
      - Result passage disposed without unit P2-S3-C5
      - Result passage disposed without unit P2-S3-C7
      - Result passage disposed without unit P2-S3-C8
      - Result passage disposed without unit P2-S3-C9
      - 'window 4: invalid/duplicate disposition P3-S3-C11'
      - 'window 4: invalid/duplicate disposition P3-S3-C12'
      - 'window 4: invalid/duplicate disposition P3-S3-C13'
      - 'window 4: invalid/duplicate disposition P3-S3-C14'
      - Result passage disposed without unit P4-S1-C11
      - Result passage disposed without unit P4-S1-C15
      - Result passage disposed without unit P5-S1-C3
      unattached_null_or_qualifier_ids:
      - P1-S1-C8
      - P2-S3-C9
      - P4-S1-C15
      suppressed_nonrepresented_units: 6
      default_disposition_count_requires_completeness_check: 127
      unselected_timing_passages:
      - P2-S2-C2
      - P2-S2-C4
      - P2-S2-C7
      - P2-S2-C9
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P4-S1-C12
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S1-C13
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S2-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P5-S3-C3
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      empty_frame_slots_require_confirmation:
      - validation
      - personal_factors
      - tested_personal_effects
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-5-1
      unlinked_tables: []
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P3-S3
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: ef936e4f2e06d05151975ac93052b5430b4a91bd28862b9a95907eea3746054f
      source_review: _compare/relationships-2026-11-16/review-current/Basilakos2014
      source_status_sha256: 94fe2915721833240400c299aaebdb918d5182d204e74443476227fcabcc5ce4
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Abstract summary of findings
    - source_id: P1-S2-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Abstract summary of findings
    - source_id: P2-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Demographic data
    - source_id: P2-S3-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive statistics of outcome
    - source_id: P2-S3-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive statistics of outcome
    - source_id: P2-S3-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Demographic distribution of aphasia types
    - source_id: P2-S3-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient classification details
    - source_id: P3-S4-C4
      disposition: represented
      result_indexes:
      - 0
      - 1
      - 2
      - 3
      - 4
      - 5
      reason: Reports Pearson correlations for all ROIs and fluency
    - source_id: P3-S4-C5
      disposition: represented
      result_indexes:
      - 6
      reason: Reports Hotelling t results for ASAF/aslant overlap
    - source_id: P4-S1-C9
      disposition: represented
      result_indexes:
      - 6
      reason: Reports Hotelling t comparisons for ASAF/aslant overlap
    - source_id: P4-S1-C10
      disposition: represented
      result_indexes:
      - 7
      reason: Reports trend for ASAF/aslant overlap vs unique aslant ROI
    - source_id: P4-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Collinearity/VIF check
    - source_id: P4-S1-C12
      disposition: represented
      result_indexes:
      - 8
      reason: Reports stepwise regression Model 1 for fluency
    - source_id: P4-S1-C13
      disposition: represented
      result_indexes:
      - 9
      reason: Reports stepwise regression Model 2 for fluency
    - source_id: P4-S1-C14
      disposition: represented
      result_indexes:
      - 10
      reason: Reports null findings for remaining tracts in Model 2
    - source_id: P4-S1-C15
      disposition: background_or_descriptive
      result_indexes: []
      reason: Collinearity/VIF check
    - source_id: P5-S1-C1
      disposition: represented
      result_indexes:
      - 11
      - 12
      reason: Reports correlations for semantic processing
    - source_id: P5-S1-C2
      disposition: represented
      result_indexes:
      - 13
      reason: Reports non-significant correlations for semantic processing
    - source_id: P5-S1-C3
      disposition: represented
      result_indexes:
      - 14
      reason: Reports Hotelling t results for semantic processing
    - source_id: P5-S1-C4
      disposition: represented
      result_indexes:
      - 15
      reason: Reports stepwise regression for semantic processing
    - source_id: P5-S1-C5
      disposition: represented
      result_indexes:
      - 16
      reason: Reports null findings for remaining ROIs in semantic model
    - source_id: P5-S1-C9
      disposition: repeated
      result_indexes:
      - 8
      reason: Discussion restatement of regression result
    - source_id: P5-S1-C10
      disposition: repeated
      result_indexes:
      - 9
      reason: Discussion restatement of regression result
    - source_id: P5-S2-C9
      disposition: represented
      result_indexes:
      - 8
      - 9
      - 15
      reason: Table 1 summarizing regression results
    - source_id: P5-S3-C5
      disposition: represented
      result_indexes:
      - 17
      reason: Reports correlation between WPM and WAB fluency
    - source_id: P6-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Methodological comparison statement
    - source_id: P6-S1-C12
      disposition: repeated
      result_indexes:
      - 10
      reason: Discussion restatement of regression nulls
    - source_id: P6-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Theoretical interpretation
    - source_id: P7-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Theoretical explanation for null result
    - source_id: P7-S1-C8
      disposition: repeated
      result_indexes:
      - 15
      reason: Discussion restatement of semantic processing result
    - source_id: P7-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion statement
    unresolved_coverage: []
    pending_source_ids:
    - P1-S1-C8
    - P1-S2-C1
    - P2-S2-C9
    - P2-S3-C5
    - P2-S3-C7
    - P2-S3-C8
    - P2-S3-C9
    - P4-S1-C11
    - P4-S1-C15
    - P5-S1-C9
    - P5-S1-C10
    - P6-S1-C6
    - P6-S1-C12
    - P6-S2-C8
    - P7-S1-C7
    - P7-S1-C8
    - P7-S1-C12
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
      - P2-S2-C2
      recruited_sample:
      - P2-S2-C2
      eligibility:
      - P2-S2-C3
      - P2-S2-C4
      - P2-S2-C5
      - P2-S2-C6
      imaging_provenance:
      - P3-S2-C10
      - P3-S2-C11
      imaging_timing:
      - P2-S3-C10
      outcome_timing:
      - P2-S3-C10
      outcome_definition:
      - P2-S2-C13
      - P2-S2-C14
      - P2-S3-C5
      - P2-S3-C6
      - P2-S3-C7
      - P5-S3-C10
      validation: []
      analysis_restrictions:
      - P3-S3-C11
      - P3-S3-C13
      - P3-S4-C3
      dependent_variable_statement:
      - P3-S3-C6
      - P3-S3-C8
      limitations:
      - P5-S3-C1
      - P5-S3-C2
      - P5-S3-C8
      - P6-S1-C4
      - P6-S1-C6
      - P6-S1-C7
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P3-S3-C8
      explicitly_not_adjusted:
      - P3-S3-C9
      descriptive_personal_factors:
      - P2-S2-C9
      - P2-S3-C8
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P4-S1-C12
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S1-C13
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S2-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P5-S3-C3
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
      pdf_sha256: ef936e4f2e06d05151975ac93052b5430b4a91bd28862b9a95907eea3746054f
      review_sha256: 78abd924bd0754c20b5e9286f8d55341d74f739f8d7d6d769bacd080bde7aa2b
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
      - P5-S1-C1
      source_result: The study reports a significant positive correlation between
        the mean T1-signal intensity Z-score of the uncinate fasciculus ROI and semantic
        processing scores (Pyramids and Palm Trees Test) in chronic post-stroke aphasia
        patients (r = 0.41, p < 0.001). In a stepwise regression model, the uncinate
        fasciculus was identified as the best predictor of semantic processing.
      result_status: detected
      patient_measurement: voxel_tissue
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis R012 correctly identifies the Pearson correlation
            between uncinate fasciculus integrity and semantic processing. The source
            P5-S1-C1 explicitly states 'Semantic processing was correlated with the
            uncinate fasciculus (r = 0.41, p < 0.001)'. The proposed core includes
            the stepwise regression result (P5-S1-C4) as a qualification, which is
            consistent with the source describing the uncinate as the 'best predictor'
            in that model.
          source_ids:
          - P5-S1-C1
          - P5-S1-C4
          - P3-S3-C6
        direction:
          answer: fits
          reason: The source reports a positive correlation (r = 0.41). The proposed
            core uses the direction 'likely' which is a valid qualitative representation
            of a significant positive association in this context, preserving the
            detected nature of the relationship.
          source_ids:
          - P5-S1-C1
        construct:
          answer: fits
          reason: The exposure is correctly identified as the uncinate fasciculus.
            The outcome is semantic processing, measured by the Pyramids and Palm
            Trees Test (P2-S3-C6). The patient measurement is correctly identified
            as voxel_tissue (T1-signal intensity Z-score within an ROI defined by
            an atlas), not template_lesion_overlap or patient_diffusion. The source
            P3-S2-C5 and P3-S2-C10 confirm the use of T1 intensity Z-scores in atlas-defined
            ROIs.
          source_ids:
          - P3-S2-C5
          - P3-S2-C10
          - P2-S3-C6
          - P5-S1-C1
        qualifications:
          answer: fits
          reason: The proposed core includes qualifications 'when used alone in Pearson
            correlation' and 'best predictor in a stepwise regression model'. These
            accurately reflect the source findings in P5-S1-C1 (correlation) and P5-S1-C4
            (regression). The limitation regarding T1-signal intensity being an indirect
            measure is also correctly included.
          source_ids:
          - P5-S1-C1
          - P5-S1-C4
          - P5-S4-C2
        missing_material_caveat:
          answer: fits
          reason: The core includes the key limitation that T1-signal intensity is
            an indirect measure of tissue integrity (P5-S4-C2). No other material
            caveats that would change the interpretation of the specific uncinate-semantic
            processing association appear to be missing from the provided source window.
            The unresolved image-reading disagreements in P2-S3-C10 and P5-S3-C4 do
            not affect the core relationship's validity as they pertain to specific
            numeric transcriptions or MRI timing details that are not central to the
            qualitative claim of association.
          source_ids:
          - P5-S4-C2
      optional_pending:
      - Specific correlation coefficient r=0.41 and p-value not transcribed in core
        fields
      - Regression F-statistic and R-squared not transcribed in core fields
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Specific correlation coefficient r=0.41 and p-value not transcribed in core
      fields
    - Regression F-statistic and R-squared not transcribed in core fields
    normalizations:
    - field: bucket
      original: predictors
      action: route_from_kind
      value: regions
    analysis_identity:
      id: R012
      exposure:
        text: uncinate fasciculus
      outcome:
        text: semantic processing
      analysis_label: Pearson correlation
      relation: association
      evidence_ids:
      - P5-S1-C1
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
        pdf_sha256: ef936e4f2e06d05151975ac93052b5430b4a91bd28862b9a95907eea3746054f
        source_review: _compare/relationships-2026-11-16/review-current/Basilakos2014
        source_status_sha256: 94fe2915721833240400c299aaebdb918d5182d204e74443476227fcabcc5ce4
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P2-S2-C2:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: ef936e4f2e06d05151975ac93052b5430b4a91bd28862b9a95907eea3746054f
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 2e7b1eedb2bbea6cc9a36ef060f225b9932bcf2e604a4f352915d2b59685a61e
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S2-C2
          page: 2
          text_layer_sha256: 2e7b1eedb2bbea6cc9a36ef060f225b9932bcf2e604a4f352915d2b59685a61e
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'MATERIALS AND METHODS

          PARTICIPANTS

          This study included 76 patients (32 female, 73 right-handed) with

          chronic aphasia who have undergone language testing and MRI

          studies at the University of South Carolina’s Aphasia Lab over a

          follow-up period of 10 years.'
        anchor_text: 'MATERIALS AND METHODS

          PARTICIPANTS

          This study included 76 patients (32 female, 73 right-handed) with

          chronic aphasia who have undergone language testing and MRI

          studies at the University of South Carolina’s Aphasia Lab over a

          follow-up period of 10 years.'
        excluded_fragments: []
        image_sha256: e34703293b347dcb26f44756385ce77c82cc4b3c12c27cd0e21e10638cbf2574
        transcription: 'MATERIALS AND METHODS

          PARTICIPANTS

          This study included 76 patients (32 female, 73 right-handed) with chronic
          aphasia who have undergone language testing and MRI studies at the University
          of South Carolina’s Aphasia Lab over a follow-up period of 10 years'
      P2-S2-C9:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: ef936e4f2e06d05151975ac93052b5430b4a91bd28862b9a95907eea3746054f
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 7bdc91eddf55dd106c484d32d507ebbfc2f95a579597d2c7b77393f078e8015c
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S2-C9
          page: 2
          text_layer_sha256: 7bdc91eddf55dd106c484d32d507ebbfc2f95a579597d2c7b77393f078e8015c
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'The mean age of the patients was 61.35 years (SD = 12.67,

          range = 36–83), and the mean time post-stroke was 35.57 months

          (SD = 47.56, range = 6–276).'
        anchor_text: 'The mean age of the patients was 61.35 years (SD = 12.67,

          range = 36–83), and the mean time post-stroke was 35.57 months

          (SD = 47.56, range = 6–276).'
        excluded_fragments: []
        image_sha256: eaee2e172a7ac49e259085f296ede7349c5a5a812ce7a209fa286dd81213a626
        transcription: 'The mean age of the patients was 61.35 years (SD = 12.67,

          range = 36–83), and the mean time post-stroke was 35.57 months

          (SD = 47.56, range = 6–276)'
      P2-S3-C10:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: ef936e4f2e06d05151975ac93052b5430b4a91bd28862b9a95907eea3746054f
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 6a15ccf1265399638b3027c1261621ceeffd9e4e85a7c8b6694cb2c31f09797b
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S3-C10
          page: 2
          text_layer_sha256: 6a15ccf1265399638b3027c1261621ceeffd9e4e85a7c8b6694cb2c31f09797b
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: 'MRI DATA COLLECTION

          All subjects underwent a structural brain anatomy assessment

          using a high-resolution T1-MRI performed at least 6 months after

          the stroke, in close chronological proximity with the language

          testing session (usually within the same day, but no longer than

          1 month apart).'
        anchor_text: 'MRI DATA COLLECTION

          All subjects underwent a structural brain anatomy assessment

          using a high-resolution T1-MRI performed at least 6 months after

          the stroke, in close chronological proximity with the language

          testing session (usually within the same day, but no longer than

          1 month apart).'
        excluded_fragments: []
        image_sha256: 6beef55177dc4336804d61cea4e751828fe9befa04703963f2ad950ec109b681
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 5
  quote: '

    Basilakos et al.

    White matter damage and ﬂuency

    Semantic processing was correlated with the uncinate fasci-

    culus (r = 0.41, p < 0.001) and the aslant (r = 0.37, p < 0.008),

    but none of the remaining ROIs.'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-20'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
