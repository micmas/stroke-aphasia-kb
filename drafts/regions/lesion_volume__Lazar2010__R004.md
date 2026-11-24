---
id: lesion_volume
name: lesion volume
kind: classical
findings:
- id: f1
  target: achieved_delta_wab
  target_kind: prognosis
  claim: In a multiple-regression model predicting aphasia recovery (change in WAB
    scores from baseline to 90 days), the estimated regression coefficient for lesion
    volume was not significant.
  direction: no_effect
  relationship: correlational
  method: behavioral_only
  sample:
    n: not_reported
    population: Right-handed patients with first-time, left hemisphere ischemic strokes
      and mild-to-moderate aphasia
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
  - Excludes individuals with severe comprehension deficits due to consent restrictions
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Lesion volume estimated in cubic centimeters as the
    product of maximal perpendicular diameters of the diffusion-weighted imaging lesion
    in cm multiplied by the number of 0.5-cm slices divided by 2. Analyzed as an independent
    variable alongside age and initial WAB score (WABinitial); The model overall was
    highly predictive (R2=0.83), but the specific coefficient for lesion volume was
    not significant. Additional metadata has not been transcribed; review the pending-field
    flags before approval.'
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
    - not_transcribed:sample.time_post_onset
    - proposed_concept:achieved_delta_wab
  citation: '@Lazar2010'
  source_passages:
  - section: Original source P1-S3-C3
    page: 1
    quote: "To\ndetermine whether initial aphasia severity predicts change in aphasia\n\
      scores (achieved \x01WAB\x03[WAB3 mo\x02WABinitial]) and whether the\nrelation\
      \ is proportional, we performed a regression analysis of\naphasia recovery (achieved\
      \ \x01WAB) with WABinitial, age, and lesion\nvolume as independent variables\
      \ and the change score as the\ndependent variable."
    supports: method
  - section: Original source P1-S3-C4
    page: 1
    quote: "Lesion volume was estimated in cubic centime-\nters: lesion volume\x03\
      [product of maximal perpendicular diameters of\nthe diffusion-weighted imaging\
      \ lesion in cm]\x05[number of 0.5-cm\nslices]/2, a reasonably reliable method\
      \ compared with automated\nmethods.9 Testing procedures and results for motor\
      \ function and the\nmethods for the visual-spatial tasks have been described\
      \ elsewhere.4,10\nResults\nThere were 118 patients in the PARIS database during\
      \ the\nstudy period, of whom 21 had aphasia on the baseline PARIS\nReceived\
      \ December 23, 2009; final revision received March 22, 2010; accepted March\
      \ 23, 2010."
    supports: method
  - section: Original source P2-S1-C4
    page: 2
    quote: 'All were right-handed

      with first-time, left hemisphere ischemic strokes.'
    supports: sample
  - section: Original source P2-S1-C13
    page: 2
    quote: 'The

      regression coefficient was significant for WABinitial; the

      estimated regression coefficients of lesion volume and age,

      however, were not significant.'
    supports: claim
  - section: Original source P1-S2-C5
    page: 1
    quote: "Initial assessment occurred 24 to 72 hours after stroke onset\n(mean\x03\
      2.1 days; SD\x031.3); the follow-up examination took place at\n90 days (mean\x03\
      93.1 days; SD\x0318.8) after the qualifying stroke\nbecause it was thought that\
      \ most spontaneous recovery occurs by this\npoint.6 The aphasia examination,\
      \ derived from standardized subtests\nfrom the Western Aphasia Battery (WAB),7\
      \ consisted of the evalu-\nation of comprehension (“yes/no questions,” “auditory\
      \ word recog-\nnition,” “sequential commands”), repetition, and naming (“object\n\
      naming,” “word fluency,” “responsive speech”) and were chosen\nbecause of their\
      \ high respective intraindividual reliabilities of 88%,\n97%, and 92%.8 Each\
      \ of the 3 spheres of function yielded a possible\nscore of 10, with a composite\
      \ perfect score of 30 (WABmax)."
    supports: sample
  - section: Original source P3-S3-C5
    page: 3
    quote: 'We were unable to address the question regarding recovery

      from severe aphasia because of consent restrictions imposed

      by local law.'
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-24'
relationship_review:
  paper: Lazar2010
  proposal_id: R004
  review_status_sha256: 7e025600185b586241f7abb1739fd965418be48b047b0d8dabcf54c1724765d8
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 0bceab696230c2d051c5e7e4e087f85f368c3c892092000e3c3fe9cd07267f9b
    original_review_binding:
      version: relationship-review-v5
      input_hashes:
        pdf: 0bceab696230c2d051c5e7e4e087f85f368c3c892092000e3c3fe9cd07267f9b
        A/passages.json: 49b2da57324175e94efd93e103ebf850eecce2b0be5060e8f273cd2e8b57f4f4
        A/raw.json: b06e27f22d78076db89fe3afe6565538106cf81a259fb8fd02dc79488128b025
        A/source-units.json: d5453b609d67ee0479394c695cf34006b510bc5d2b62790e07c2bf8b33eb9f6c
        A/full-source-units.json: 7811becb616cb520b0ed71b6cf79f06d7f7e2bb6073499bbfa198d1e68a378c5
        A/meta.json: 42fc08a8e018c3c9c9aa9b4bddf6fd69b0d8ddb60b12d03dab57a7509e8069d7
        A/table-images/TABLE-1-page-2-1.png: 72695d53de9d15da10eca1cf791d5440d9a6ddaaae12f749ab6aa9c20b42dc44
        A/table-images/page-2.png: 29f98e6bdc2b6d85da14a1f9113b36fc709ea52145097af08b2180cdf95856c0
        A/table-images/TABLE-2-page-2-2.png: 72695d53de9d15da10eca1cf791d5440d9a6ddaaae12f749ab6aa9c20b42dc44
        A/table-images/manifest.json: 94cffe3d03c14c4d045510059495533a84425c3ab05d5db00f9c338e0d491a69
        A/clauses/window-03/raw.json: 9cbdf75c1083ff39a4c28b387ec02edaf11b0220e434b0799d884a68ee0778c6
        A/clauses/window-03/prompt.txt: c61d67c8bc7b87beb1a7dc37e37b9ead0a08fe7640d56fa173b8262e02f61607
        A/clauses/window-03/meta.json: b6cf150394ce40d0277376def3a5b82c9dc0bac1189b7bb08c3b2b88027daf08
        A/clauses/window-02/raw.json: 198950f1f4f31f76ccb73e2d99cb3f5df94d6bea9fa073c793a7591e467e6939
        A/clauses/window-02/prompt.txt: afec8fdf2941b4af89a59e7a998900e174a05b434e30b7ac1d975c62d438abb5
        A/clauses/window-02/meta.json: f4890660a43e3bd2f99fd769430b1b3d8e064878f3e8ca569cc2b0852c9b27d0
        A/clauses/window-01/raw.json: 75eabd7b1031a156cee71d12cda72d5be2598ed115df95eb264e87e948a41ea5
        A/clauses/window-01/prompt.txt: 1b72c22933ed0f6c572a2243e09cb7b2a65f9bb979c9933a6bcd1cf318c986c3
        A/clauses/window-01/meta.json: 612fb5a21a7af03a38ab237367d0032e52d6e19013baf1f431de8be9c6a3112b
        A/tables/TABLE-1-page-2-1/raw.json: 1695f3a07f092a1741de2df1543a6ab65e23fdb8c73c134082f066d6b3af94a3
        A/tables/TABLE-1-page-2-1/prompt.txt: b852229c4745da05422dbf8100fed964a18693e84e8e7379bfb82ee52582793f
        A/tables/TABLE-1-page-2-1/meta.json: c392e49d8119d7a04ec614f109e49747c0508fe9158cd76d2e9bf74778861b4b
        A/tables/TABLE-2-page-2-2/raw.json: eb7ced3bd1eecb3ce859174e82c3ab2517c1eb43b497fce19d7d0cb5c09ac4a9
        A/tables/TABLE-2-page-2-2/prompt.txt: 9e30821ce354722a2fe377112da8d80e7c8b6ea29c7760235f89f030dc5aad75
        A/tables/TABLE-2-page-2-2/meta.json: aa4ec10e7436c2fa92496189b628637c0b1dd37d8338cb719ba952c11ab8c2ed
        B/passages.json: 49b2da57324175e94efd93e103ebf850eecce2b0be5060e8f273cd2e8b57f4f4
        B/raw.json: 1e96d1b81befbaf801814d8e829292533bbd5e44ef6e8691b432e23755da36d6
        B/source-units.json: d5453b609d67ee0479394c695cf34006b510bc5d2b62790e07c2bf8b33eb9f6c
        B/full-source-units.json: 7811becb616cb520b0ed71b6cf79f06d7f7e2bb6073499bbfa198d1e68a378c5
        B/meta.json: 357468fbd2c67b325b0e481bbb50f93324bbc89807652fb46d3d622c3e98d6ef
        B/table-images/TABLE-1-page-2-1.png: 72695d53de9d15da10eca1cf791d5440d9a6ddaaae12f749ab6aa9c20b42dc44
        B/table-images/page-2.png: 29f98e6bdc2b6d85da14a1f9113b36fc709ea52145097af08b2180cdf95856c0
        B/table-images/TABLE-2-page-2-2.png: 72695d53de9d15da10eca1cf791d5440d9a6ddaaae12f749ab6aa9c20b42dc44
        B/table-images/manifest.json: 453362c09b5a62eda23cd995460ff1930e06e8d028c3b54e35767b7cd1a87cc8
        B/clauses/window-03/raw.json: 02f6559910da5087aeffea3e983dcbb8efafcd36cbc61b174c0bccd397d25296
        B/clauses/window-03/prompt.txt: c61d67c8bc7b87beb1a7dc37e37b9ead0a08fe7640d56fa173b8262e02f61607
        B/clauses/window-03/meta.json: 5b54849cc2ec2364f18af30f23daa0ad5fd1f622ba14293fb347d6ea61e0d543
        B/clauses/window-02/raw.json: 42c3b413a55ca070cc816c98991da4f039905e17fbbb39ae68fcce79c2f53ad2
        B/clauses/window-02/prompt.txt: afec8fdf2941b4af89a59e7a998900e174a05b434e30b7ac1d975c62d438abb5
        B/clauses/window-02/meta.json: ff210a4acf95941571e8249ec10e10c39a85668447f028edd0bc3fe6919a1dea
        B/clauses/window-01/raw.json: 37dc6e0507093880a2ffb020d2db700412f64fdefa9baa3bc241dd2d07889679
        B/clauses/window-01/prompt.txt: 1b72c22933ed0f6c572a2243e09cb7b2a65f9bb979c9933a6bcd1cf318c986c3
        B/clauses/window-01/meta.json: c341c9278d15cbfb70882ffa6641f4f3c6fe2b59aa432c30f7c334d096412934
        B/tables/TABLE-1-page-2-1/raw.json: 089d9b94cfeb5d7c1fe8be4d678402229bf3c30185107b31ca1c0e82a55a6ed2
        B/tables/TABLE-1-page-2-1/prompt.txt: b852229c4745da05422dbf8100fed964a18693e84e8e7379bfb82ee52582793f
        B/tables/TABLE-1-page-2-1/meta.json: 90055470db84d285c3b4cf235f5c4ac9ec8f08e537437a0b95b1b5d2218092f8
        B/tables/TABLE-2-page-2-2/raw.json: aabbe7edd8a6abe3d776bc019fcdff948dd70bed5edd5287eeacd9b9e4d74397
        B/tables/TABLE-2-page-2-2/prompt.txt: 9e30821ce354722a2fe377112da8d80e7c8b6ea29c7760235f89f030dc5aad75
        B/tables/TABLE-2-page-2-2/meta.json: e0f9c9c67e95fb91ff88fbb0e9a6b996ef9aa9f5cd8f3653589dc2e3cb37fce8
      code:
        relationship_review.py: 6d0359072ca11a7569362fe49703755a98b4207ba814fcd311161c48936053ed
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
      pdf_sha256: 0bceab696230c2d051c5e7e4e087f85f368c3c892092000e3c3fe9cd07267f9b
      source_review: _compare/relationships-2026-11-16/review-current/Lazar2010
      source_status_sha256: dd3e3e84cc4880138183cd4891bffec73ab217d8db73575ac1cf879e63056377
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R004
    exposure:
      text: lesion volume
    outcome:
      text: achieved ΔWAB
    analysis_label: Multiple-regression analysis of aphasia recovery
    relation: association
    evidence_ids:
    - P2-S1-C13
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
      pdf_sha256: 0bceab696230c2d051c5e7e4e087f85f368c3c892092000e3c3fe9cd07267f9b
      source_review: _compare/relationships-2026-11-16/review-current/Lazar2010
      source_status_sha256: dd3e3e84cc4880138183cd4891bffec73ab217d8db73575ac1cf879e63056377
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P1-S1-C11
      - Result passage disposed without unit P2-S1-C7
      - Result passage disposed without unit P2-S1-C8
      - Result passage disposed without unit P3-S1-C1
      - Accounting without a linked unit P3-S3-C12
      - Result passage disposed without unit P3-S3-C3
      - Unaccounted source passage P3-S3-C12
      unattached_null_or_qualifier_ids:
      - P3-S3-C9
      suppressed_nonrepresented_units: 5
      default_disposition_count_requires_completeness_check: 56
      unselected_timing_passages:
      - P1-S1-C8
      - P1-S2-C3
      - P2-S1-C3
      - P2-S1-C4
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P2-S1-C12
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P2-S2-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P2-S2-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: tested_personal_effects
        source_id: P2-S2-C9
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: outcome_definition
        source_ids:
        - P1-S1-C7
        - P1-S1-C9
        - P1-S2-C1
        - P1-S3-C3
        - P2-S1-C12
        - P2-S2-C8
        - P2-S2-C9
        - P3-S1-C1
        - P3-S2-C6
        - P3-S4-C3
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: personal_factors
        source_ids:
        - P2-S1-C3
        - P2-S1-C5
        - P2-S1-C6
        - P2-S1-C10
        - P2-S1-C12
        - P2-S1-C13
        - P2-S2-C3
        - P2-S2-C6
        - P3-S3-C8
        - P3-S3-C9
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - outcome_definition
      - validation
      - personal_factors
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-2-1
      - TABLE-2-page-2-2
      unlinked_tables:
      - TABLE-1-page-2-1
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units: []
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 0bceab696230c2d051c5e7e4e087f85f368c3c892092000e3c3fe9cd07267f9b
      source_review: _compare/relationships-2026-11-16/review-current/Lazar2010
      source_status_sha256: dd3e3e84cc4880138183cd4891bffec73ab217d8db73575ac1cf879e63056377
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C10
      disposition: represented
      result_indexes:
      - 5
      reason: States WABinitial is highly correlated with ΔWAB and recovery is proportional
        (0.73 of maximal potential).
    - source_id: P1-S1-C11
      disposition: repeated
      result_indexes:
      - 5
      reason: Restatement of the predictable and proportional relation.
    - source_id: P2-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Provides mean baseline aphasia score.
    - source_id: P2-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Provides mean 90-day aphasia score.
    - source_id: P2-S1-C9
      disposition: represented
      result_indexes:
      - 0
      reason: Reports statistically significant improvement from baseline to follow-up.
    - source_id: P2-S1-C10
      disposition: represented
      result_indexes:
      - 8
      reason: Reports significant difference in WABinitial between those receiving
        and not receiving therapy.
    - source_id: P2-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes mean scores across language spheres at baseline.
    - source_id: P2-S1-C12
      disposition: represented
      result_indexes:
      - 1
      reason: Reports overall R2 for the linear-regression model.
    - source_id: P2-S1-C13
      disposition: represented
      result_indexes:
      - 2
      - 3
      - 4
      reason: Identifies significant coefficient for WABinitial and non-significant
        coefficients for lesion volume and age.
    - source_id: P2-S1-C14
      disposition: represented
      result_indexes:
      - 2
      reason: States WABinitial alone accounted for 81% of variance.
    - source_id: P2-S1-C15
      disposition: represented
      result_indexes:
      - 5
      reason: Links y-intercept to proportional relation between achieved and potential
        ΔWAB.
    - source_id: P2-S2-C2
      disposition: represented
      result_indexes:
      - 5
      reason: Provides mean potential and achieved ΔWAB and the 0.73 proportional
        relation.
    - source_id: P2-S2-C3
      disposition: represented
      result_indexes:
      - 6
      reason: Reports predictability (R2) for those who received therapy vs those
        who did not.
    - source_id: P2-S2-C4
      disposition: represented
      result_indexes:
      - 7
      reason: Reports mean proportions of recovery for naming, repetition, and comprehension.
    - source_id: P3-S1-C1
      disposition: repeated
      result_indexes:
      - 2
      reason: Discussion restatement that recovery is predicted by initial severity.
    - source_id: P3-S1-C2
      disposition: repeated
      result_indexes:
      - 5
      reason: Discussion restatement of proportional relation.
    - source_id: P3-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discusses the likelihood of proportionality in untreated vs treated
        patients.
    - source_id: P3-S3-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports internal consistency (coefficient theta) of the WAB.
    - source_id: P3-S3-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discusses potential impact of therapy intensity.
    - source_id: P3-S3-C12
      disposition: repeated
      result_indexes:
      - 5
      reason: Restates that relation between actual and potential recovery accounted
        for ~80% of variance.
    unresolved_coverage: []
    pending_source_ids:
    - P1-S1-C11
    - P2-S1-C7
    - P2-S1-C8
    - P2-S1-C11
    - P3-S1-C1
    - P3-S1-C2
    - P3-S1-C8
    - P3-S3-C3
    - P3-S3-C9
    - P3-S3-C12
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-2-1
    - TABLE-2-page-2-2
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P1-S1-C8
      - P1-S3-C4
      - P2-S1-C3
      - P3-S1-C1
      recruited_sample:
      - P1-S2-C3
      - P2-S1-C3
      eligibility:
      - P1-S2-C3
      - P1-S2-C4
      - P2-S1-C1
      - P3-S1-C1
      imaging_provenance:
      - P1-S3-C4
      imaging_timing:
      - P1-S2-C5
      - P3-S3-C12
      outcome_timing:
      - P1-S2-C5
      - P2-S1-C8
      - P2-S1-C9
      - P2-S2-C9
      - P3-S1-C1
      - P3-S2-C6
      - P3-S4-C3
      outcome_definition: []
      validation: []
      analysis_restrictions:
      - P3-S3-C5
      dependent_variable_statement:
      - P1-S1-C9
      - P1-S3-C3
      - P3-S4-C3
      limitations:
      - P3-S2-C8
      - P3-S2-C10
      - P3-S3-C5
      - P3-S3-C6
      - P3-S3-C8
      - P3-S3-C9
      - P3-S3-C11
      - P3-S3-C12
      personal_factors: []
      tested_personal_effects:
      - P2-S1-C10
      - P2-S1-C13
      adjustment_roles:
      - P1-S3-C3
      - P2-S1-C12
      - P2-S1-C13
      - P2-S2-C8
      - P3-S3-C7
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P1-S2-C3
      - P2-S1-C3
      - P2-S1-C4
      - P2-S1-C5
      - P2-S1-C6
      - P2-S2-C6
      - P3-S1-C1
      - P3-S3-C9
    outcome_type: both_reported
    imaging_vs_outcome: precedes_outcome
    validation_type: none_described
    window_merge: Union of selected IDs; differing window enums retained conservatively
      as both/mixed. Not verified study-level facts.
    held_selections:
    - slot: dependent_variable_statement
      source_id: P2-S1-C12
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P2-S2-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P2-S2-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: tested_personal_effects
      source_id: P2-S2-C9
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: outcome_definition
      source_ids:
      - P1-S1-C7
      - P1-S1-C9
      - P1-S2-C1
      - P1-S3-C3
      - P2-S1-C12
      - P2-S2-C8
      - P2-S2-C9
      - P3-S1-C1
      - P3-S2-C6
      - P3-S4-C3
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: personal_factors
      source_ids:
      - P2-S1-C3
      - P2-S1-C5
      - P2-S1-C6
      - P2-S1-C10
      - P2-S1-C12
      - P2-S1-C13
      - P2-S2-C3
      - P2-S2-C6
      - P3-S3-C8
      - P3-S3-C9
      reason: Runaway selection (>8 passages); entire slot requires source review
    policy: All slots and enums remain unverified. Held selections are not evidence
      of absence. Original responses are preserved in frame/chunk-*/attempt-*/raw.json.
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
      pdf_sha256: 0bceab696230c2d051c5e7e4e087f85f368c3c892092000e3c3fe9cd07267f9b
      review_sha256: 7e025600185b586241f7abb1739fd965418be48b047b0d8dabcf54c1724765d8
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
      - P2-S1-C13
      source_result: In a multiple-regression analysis predicting achieved change
        in WAB scores (achieved ΔWAB) from baseline to 90 days, the estimated regression
        coefficient for lesion volume was not significant, whereas the coefficient
        for initial WAB score (WABinitial) was significant.
      result_status: not_detected
      patient_measurement: non_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis is the multiple-regression model predicting
            achieved ΔWAB using WABinitial, lesion volume, and age as independent
            variables, as described in P1-S3-C3 and P2-S1-C12/C13.
          source_ids:
          - P1-S3-C3
          - P2-S1-C12
          - P2-S1-C13
        direction:
          answer: fits
          reason: The source explicitly states that the estimated regression coefficient
            for lesion volume was not significant (P2-S1-C13). The draft's 'no_effect'
            direction correctly reflects this lack of a statistically detected association
            in the adjusted model.
          source_ids:
          - P2-S1-C13
        construct:
          answer: fits
          reason: The exposure is lesion volume (estimated from DWI, P1-S3-C4) and
            the outcome is achieved ΔWAB (change in aphasia scores, P1-S3-C3). The
            draft correctly identifies these constructs. The patient measurement is
            non_imaging (behavioral WAB scores), not imaging-based, despite the lesion
            volume being derived from imaging.
          source_ids:
          - P1-S3-C3
          - P1-S3-C4
          - P2-S1-C13
        qualifications:
          answer: fits
          reason: The draft includes the qualification that lesion volume was analyzed
            alongside age and initial WAB score, and that the overall model was predictive
            (R2=0.83) but the specific coefficient was not significant. This accurately
            reflects the source context in P2-S1-C12 and P2-S1-C13.
          source_ids:
          - P2-S1-C12
          - P2-S1-C13
        missing_material_caveat:
          answer: fits
          reason: The draft includes the limitation regarding severe comprehension
            deficits (P3-S3-C5). No other material caveats that would change the interpretation
            of the null result for lesion volume are omitted. The therapy status is
            noted in the source but not a primary caveat for the regression coefficient's
            null status in the main model.
          source_ids:
          - P3-S3-C5
      optional_pending:
      - Sample size (n=21) is mentioned in P1-S1-C8 and P2-S1-C1 but not explicitly
        transcribed in the draft's sample_n field; confirm if required for final approval.
      - Specific timing details (mean 2.1 days baseline, 93.1 days follow-up) are
        in P1-S2-C5 but not transcribed in the draft's timing field.
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Sample size requires source confirmation; it has not been transcribed.
    - 'sample.time_post_onset: source confirmation required; original proposed wording
      remains in the audit.'
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Sample size (n=21) is mentioned in P1-S1-C8 and P2-S1-C1 but not explicitly
      transcribed in the draft's sample_n field; confirm if required for final approval.
    - Specific timing details (mean 2.1 days baseline, 93.1 days follow-up) are in
      P1-S2-C5 but not transcribed in the draft's timing field.
    normalizations:
    - field: bucket
      original: predictors
      action: route_from_kind
      value: regions
    - field: sample.n
      original: 21
      action: not_transcribed
      reason: Not supported by selected quotations
    - field: sample.time_post_onset
      original: Initial assessment 24 to 72 hours after stroke onset; follow-up at
        90 days
      action: not_transcribed
      reason: 'Numbers not grounded in usable selected source readings: 24, 72, 9E+1'
    analysis_identity:
      id: R004
      exposure:
        text: lesion volume
      outcome:
        text: achieved ΔWAB
      analysis_label: Multiple-regression analysis of aphasia recovery
      relation: association
      evidence_ids:
      - P2-S1-C13
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
        pdf_sha256: 0bceab696230c2d051c5e7e4e087f85f368c3c892092000e3c3fe9cd07267f9b
        source_review: _compare/relationships-2026-11-16/review-current/Lazar2010
        source_status_sha256: dd3e3e84cc4880138183cd4891bffec73ab217d8db73575ac1cf879e63056377
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P1-S3-C3:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 0bceab696230c2d051c5e7e4e087f85f368c3c892092000e3c3fe9cd07267f9b
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 244cce1aa69ba2d5decf278a802b1b876d91708fab6636f6c0092ac6ade84657
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P1-S3-C3
          page: 1
          text_layer_sha256: 244cce1aa69ba2d5decf278a802b1b876d91708fab6636f6c0092ac6ade84657
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: "To\ndetermine whether initial aphasia severity predicts change\
          \ in aphasia\nscores (achieved \x01WAB\x03[WAB3 mo\x02WABinitial]) and whether\
          \ the\nrelation is proportional, we performed a regression analysis of\n\
          aphasia recovery (achieved \x01WAB) with WABinitial, age, and lesion\nvolume\
          \ as independent variables and the change score as the\ndependent variable."
        anchor_text: "To\ndetermine whether initial aphasia severity predicts change\
          \ in aphasia\nscores (achieved \x01WAB\x03[WAB3 mo\x02WABinitial]) and whether\
          \ the\nrelation is proportional, we performed a regression analysis of\n\
          aphasia recovery (achieved \x01WAB) with WABinitial, age, and lesion\nvolume\
          \ as independent variables and the change score as the\ndependent variable."
        excluded_fragments: []
      P1-S3-C4:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 0bceab696230c2d051c5e7e4e087f85f368c3c892092000e3c3fe9cd07267f9b
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: d609db04659bb29e54c38af6df91f459df349e9b31b6f60c2177b54a3b1045ae
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P1-S3-C4
          page: 1
          text_layer_sha256: d609db04659bb29e54c38af6df91f459df349e9b31b6f60c2177b54a3b1045ae
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: "Lesion volume was estimated in cubic centime-\nters: lesion\
          \ volume\x03[product of maximal perpendicular diameters of\nthe diffusion-weighted\
          \ imaging lesion in cm]\x05[number of 0.5-cm\nslices]/2, a reasonably reliable\
          \ method compared with automated\nmethods.9 Testing procedures and results\
          \ for motor function and the\nmethods for the visual-spatial tasks have\
          \ been described elsewhere.4,10\nResults\nThere were 118 patients in the\
          \ PARIS database during the\nstudy period, of whom 21 had aphasia on the\
          \ baseline PARIS\nReceived December 23, 2009; final revision received March\
          \ 22, 2010; accepted March 23, 2010."
        anchor_text: "Lesion volume was estimated in cubic centime-\nters: lesion\
          \ volume\x03[product of maximal perpendicular diameters of\nthe diffusion-weighted\
          \ imaging lesion in cm]\x05[number of 0.5-cm\nslices]/2, a reasonably reliable\
          \ method compared with automated\nmethods.9 Testing procedures and results\
          \ for motor function and the\nmethods for the visual-spatial tasks have\
          \ been described elsewhere.4,10\nResults\nThere were 118 patients in the\
          \ PARIS database during the\nstudy period, of whom 21 had aphasia on the\
          \ baseline PARIS\nReceived December 23, 2009; final revision received March\
          \ 22, 2010; accepted March 23, 2010."
        excluded_fragments: []
      P1-S2-C5:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 0bceab696230c2d051c5e7e4e087f85f368c3c892092000e3c3fe9cd07267f9b
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 4692fe9c7ac745f012a87d0d7791a0155405de9ef016df50c57964e0af983602
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P1-S2-C5
          page: 1
          text_layer_sha256: 4692fe9c7ac745f012a87d0d7791a0155405de9ef016df50c57964e0af983602
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: "Initial assessment occurred 24 to 72 hours after stroke onset\n\
          (mean\x032.1 days; SD\x031.3); the follow-up examination took place at\n\
          90 days (mean\x0393.1 days; SD\x0318.8) after the qualifying stroke\nbecause\
          \ it was thought that most spontaneous recovery occurs by this\npoint.6\
          \ The aphasia examination, derived from standardized subtests\nfrom the\
          \ Western Aphasia Battery (WAB),7 consisted of the evalu-\nation of comprehension\
          \ (“yes/no questions,” “auditory word recog-\nnition,” “sequential commands”),\
          \ repetition, and naming (“object\nnaming,” “word fluency,” “responsive\
          \ speech”) and were chosen\nbecause of their high respective intraindividual\
          \ reliabilities of 88%,\n97%, and 92%.8 Each of the 3 spheres of function\
          \ yielded a possible\nscore of 10, with a composite perfect score of 30\
          \ (WABmax)."
        anchor_text: "Initial assessment occurred 24 to 72 hours after stroke onset\n\
          (mean\x032.1 days; SD\x031.3); the follow-up examination took place at\n\
          90 days (mean\x0393.1 days; SD\x0318.8) after the qualifying stroke\nbecause\
          \ it was thought that most spontaneous recovery occurs by this\npoint.6\
          \ The aphasia examination, derived from standardized subtests\nfrom the\
          \ Western Aphasia Battery (WAB),7 consisted of the evalu-\nation of comprehension\
          \ (“yes/no questions,” “auditory word recog-\nnition,” “sequential commands”),\
          \ repetition, and naming (“object\nnaming,” “word fluency,” “responsive\
          \ speech”) and were chosen\nbecause of their high respective intraindividual\
          \ reliabilities of 88%,\n97%, and 92%.8 Each of the 3 spheres of function\
          \ yielded a possible\nscore of 10, with a composite perfect score of 30\
          \ (WABmax)."
        excluded_fragments: []
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 1
  quote: "To\ndetermine whether initial aphasia severity predicts change in aphasia\n\
    scores (achieved \x01WAB\x03[WAB3 mo\x02WABinitial]) and whether the\nrelation\
    \ is proportional, we performed a regression analysis of\naphasia recovery (achieved\
    \ \x01WAB) with WABinitial, age, and lesion\nvolume as independent variables and\
    \ the change score as the\ndependent variable."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-24'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
