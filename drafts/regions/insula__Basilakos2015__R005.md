---
id: insula
name: insula cluster
kind: network
findings:
- id: f1
  target_audit:
    status: behaviour_label_present
    category: behaviour_or_language_construct
    original_target: aos_speech_errors
    reason: Label names a behaviour or language construct; its exact operational definition and measurement
      still need source review.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  outcome_measurement:
    status: needs_source_review
    instruments: []
    note: Outcome instrument/task is not yet verified for this finding. Do not infer it from the predictor
      or a paper-wide test list.
  target: aos_speech_errors
  target_kind: impairment
  claim: Damage to the insula was not a significant predictor for the severity of
    speech errors characteristic of apraxia of speech (AOS), although it was a significant
    predictor for speech errors that can occur in aphasia.
  direction: no_effect
  relationship: correlational
  method: LSM
  sample:
    n: 43
    population: patients with a single left-hemisphere ischemic stroke
    phase: not_reported
    time_post_onset: chronic phase of recovery (>6 months post stroke)
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - The Johns Hopkins University atlas used for ROI analysis does not divide the insula
    into specific sub-regions
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: continuous quantification of structural damage measured
    by hypointense signal on chronic T1-weighted MRI, standardized by z-scores based
    on the patient''s right-hemisphere image intensity. analysis used Freedman–Lane
    regression to remove variability explained by errors that could also occur in
    aphasia; T1-signal intensity was used as a continuous measure of anatomic damage
    rather than binary lesion masks. Additional metadata has not been transcribed;
    review the pending-field flags before approval. PDF image reading (P2-S2-C6, two-model
    agreement, human verification pending): All were tested at the chronic phase of
    recovery (ie, >6 months post stroke; mean month post onset, 52.5±38.9) Original
    text-layer quotation is preserved below. Reconcile this new analysis with earlier
    drafts and source-review decisions for the paper; new candidate IDs do not carry
    earlier decisions forward.'
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
    - proposed_concept:aos_speech_errors
  citation: '@Basilakos2015'
  source_passages:
  - section: Original source P5-S1-C3
    page: 5
    quote: "It has also been used in many \nstudies to explicitly describe and further\
      \ localize production \ndeficits in AOS19 and progressive AOS.16–18,20\nAlthough\
      \ previous work has localized AOS to the left SPGI \nof the insula12,13 or the\
      \ left IFG,10,11 this study provides con-\nverging evidence between the neuroanatomical\
      \ underpinnings \nof severity ratings of AOS using the ASRS and neuroimag-\n\
      ing findings with recent investigations into the localiza-\ntion of poststroke\
      \ AOS19 and primary progressive apraxia of \nspeech.16–20 We did not find evidence\
      \ of insula involvement in \npredicting AOS, similar to recent studies with\
      \ primary pro-\ngressive apraxia of speech.17,18 Furthermore, a recent func-\n\
      tional MRI study in neurologically intact individuals15 found \nthat the SPGI\
      \ is not involved in complex articulation tasks as \npreviously suggested by\
      \ patient data.12,13 Clearly, our methods \nwere sufficient for detecting statistically\
      \ significant results in \nthe insula, as damage to this area was a significant\
      \ predictor \nfor speech errors that can occur in aphasia but did not survive\
      \ \nthresholding for severity of speech errors that are character-\nistic of\
      \ AOS."
    supports: claim
  - section: Original source P1-S2-C5
    page: 1
    quote: "Methods—Forty-three patients with history of a single left-hemisphere\
      \ stroke underwent comprehensive speech and \nlanguage testing."
    supports: sample
  - section: Original source P2-S2-C6
    page: 2
    quote: "All were tested at the chronic phase of recovery (ie, >6 months post \n\
      stroke; mean month post onset, 52.5±38.9)."
    supports: sample
  - section: Original source P3-S2-C5
    page: 3
    quote: "Because stroke is associated \nwith hypointense signal on chronic T1-MRI,31\
      \ this method of analysis \nuses hypointense signal as a continuous quantification\
      \ of structural dam-\nage to predict behavior."
    supports: method
  - section: Original source P3-S2-C10
    page: 3
    quote: "Lesion Symptom Mapping Analysis\nWe conducted Freedman–Lane regression\
      \ where each behavioral \nvariable acted as a nuisance regressor for the other\
      \ using Matlab rou-\ntines developed by Ged Ridgway.35 Of note, we chose to\
      \ use a regres-\nsion analysis, as opposed to logistic regression or ANCOVA\
      \ because \nwe used images with continuous voxel-based measures instead of \n"
    supports: method
  - section: Original source P5-S1-C5
    page: 5
    quote: "The Johns Hopkins University atlas does \nnot divide the insula into specific\
      \ regions; rather, the entirety \nof the insula boundary is included in the\
      \ Johns Hopkins \nUniversity atlas’s insula ROI."
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-20'
relationship_review:
  paper: Basilakos2015
  proposal_id: R005
  review_status_sha256: a1379c8c7b8bd0a0208e2f467a73dd93d11ea2c6272f616c669947f768a6176f
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 0aab187171d50dda12559003dd6f8fc1b500aa589d5e28c9e9d9814780bff658
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 0aab187171d50dda12559003dd6f8fc1b500aa589d5e28c9e9d9814780bff658
        A/passages.json: e615ce9c556d4ff6945441af8ffd66eebdd4a6efaab42cdc80c4bd6ea303ed0d
        A/raw.json: 44e1d679a9a73b353a4931406a1c5a4c7917eb8fe20b91fb562c56175151ae61
        A/source-units.json: 95ad10504948e5e9461392d110ec6993f2eb052167d0bf218323c521f8218f4d
        A/full-source-units.json: d74f866129515749dc2e8d0b2c953917c10fff5cd20e4e6659dba632520626cb
        A/meta.json: e90809a44e79fc63107d411be4ec1b6ab41926d2511ed5edb3e9d87c9f58e946
        A/table-images/page-4.png: 7ba72a3ee4ca6335c438892166622a3330ad6d24b82656df036d4f6069455047
        A/table-images/TABLE-1-page-4-1.png: 5374acc4f24a052195d80b6d4ec80aaffe9aed2aa9673c7bba470c62b6d6d75c
        A/table-images/TABLE-2-page-4-2.png: 3c09df02c35528172df051dd8c74613bb95aa4e064c764e061f03be0d37dd86a
        A/table-images/manifest.json: fc2bc35a8e3dbd79251fa7756846901a72a6ee2b4bcc6641b110812511d53a6f
        A/clauses/window-03/raw.json: e577844794fa9e2af294b76fa6f849cf7bfd032360980a72aa05f2d6ced7f0c3
        A/clauses/window-03/prompt.txt: d8f2ac04e7c7418114bbb878d289463ae122429c15a075d4c8fd3a14e19d54ab
        A/clauses/window-03/meta.json: d25c315d418fdc3ad89afd921c5e20881b498c476589cb0e549cc822677be755
        A/clauses/window-04/raw.json: 92faeac149e6a6c56700b62bd4aeeedbac61366cdc39eb8f38ea7f047878d99d
        A/clauses/window-04/prompt.txt: cdf24b71fcdb70b97c4b499d5a4932acdb4ea7f8f5b03bc2b0461800afd51ce6
        A/clauses/window-04/meta.json: aea0c8d16594d8d8cf5efa8bbec74d9bd883c44e43fcd15ffb7180817de4df4e
        A/clauses/window-05/raw.json: c885919e271877174257a6ac9e9bd2f157585fcb9268d936f9ca97aedf530f5f
        A/clauses/window-05/prompt.txt: 18095a4649f1dcd6003a4065d0656259fb206f4b3332b0a621c2cedf16332dfd
        A/clauses/window-05/meta.json: e6d05127173e08367a71c489c4add59a82d5b4b2ab3a47986e55c587e94d69fd
        A/clauses/window-02/raw.json: 4d8324abfba3a70695862838842f8412ce6b8377f1b19d2b9a1c45e5b37bbb99
        A/clauses/window-02/prompt.txt: 159775385366e3fff3c02965d27ed01b629d77c2299131da74b58391b97f1ffe
        A/clauses/window-02/meta.json: dbc059edca013d37a995994b47dc2ac73d2b2d83d38b06efaf462dab5d3331b5
        A/clauses/window-01/raw.json: fd5a84e15a53a8ddda5f06fc1bebfac8b0e69e62f06c331173f296cc81338f80
        A/clauses/window-01/prompt.txt: 44d14ff9d4a00fe36b5a2f104c86141694f55388376675b1f1ab44f0d0e735d7
        A/clauses/window-01/meta.json: c628aa8df7218d14ec76fb1b693fdc33982234c28716f81bb47797437eb29a82
        A/tables/TABLE-1-page-4-1/raw.json: dd8b2a71a2768b1e7a1b59ac8d61b1f39b3c2b5cec500aff8f121309dc063485
        A/tables/TABLE-1-page-4-1/prompt.txt: 84e9736ee9afd6ac25b24ca5ea3d3d7cf7f54ae3e7f992149aa13ef08634faa1
        A/tables/TABLE-1-page-4-1/meta.json: 321f3dc2f726bdcf7a13858b5311824978c1beda1093fba878e6fd8c02fa9dbc
        A/tables/TABLE-2-page-4-2/raw.json: 52c0edb25a00adc1d7dcae83f8e3ad3be4a154ba7f064029f899af4f79b59439
        A/tables/TABLE-2-page-4-2/prompt.txt: 113df11589cb1f2e53cd263540586e37eacb2059fb1ded5cc3fb9d3fae95c559
        A/tables/TABLE-2-page-4-2/meta.json: f2dd42c803267ef2c0a7ccf18d9fc3f40b0135487ae3f2f29681233f709f5854
        B/passages.json: e615ce9c556d4ff6945441af8ffd66eebdd4a6efaab42cdc80c4bd6ea303ed0d
        B/raw.json: f4f243801fcdb501941b8d10c98644c0f9eaa43d7494f8c73bd259ba4ea28d54
        B/source-units.json: 95ad10504948e5e9461392d110ec6993f2eb052167d0bf218323c521f8218f4d
        B/full-source-units.json: d74f866129515749dc2e8d0b2c953917c10fff5cd20e4e6659dba632520626cb
        B/meta.json: 51113af63fc4ace1a54cbdb51a99a6c6347832a0741fe540c44282ec1b2bda03
        B/table-images/page-4.png: 7ba72a3ee4ca6335c438892166622a3330ad6d24b82656df036d4f6069455047
        B/table-images/TABLE-1-page-4-1.png: 5374acc4f24a052195d80b6d4ec80aaffe9aed2aa9673c7bba470c62b6d6d75c
        B/table-images/TABLE-2-page-4-2.png: 3c09df02c35528172df051dd8c74613bb95aa4e064c764e061f03be0d37dd86a
        B/table-images/manifest.json: fde97216a4558f377f84b8fc462e29a4255b46c0ebe68dbd94f262770bf654cc
        B/clauses/window-03/raw.json: 936657335ddb24eceb748cca642b8aa0ac07cfc6a790766e69fddcc163d8eb8d
        B/clauses/window-03/prompt.txt: d8f2ac04e7c7418114bbb878d289463ae122429c15a075d4c8fd3a14e19d54ab
        B/clauses/window-03/meta.json: d885e0663d7d07c1837fc4369cbc7ec564928b675ab9a41baa124b8b826186ca
        B/clauses/window-04/raw.json: b3d35261ef38cd88109516ac8124f664ee9e0c2ca79fe4aae66339534a74a477
        B/clauses/window-04/prompt.txt: cdf24b71fcdb70b97c4b499d5a4932acdb4ea7f8f5b03bc2b0461800afd51ce6
        B/clauses/window-04/meta.json: 676c63d7af3f444be053c4518e5dc92cb21c21e47b929457c17a3446c50d0f56
        B/clauses/window-05/raw.json: c885919e271877174257a6ac9e9bd2f157585fcb9268d936f9ca97aedf530f5f
        B/clauses/window-05/prompt.txt: 18095a4649f1dcd6003a4065d0656259fb206f4b3332b0a621c2cedf16332dfd
        B/clauses/window-05/meta.json: 86106b791ff7549d4b4bcc83ade9a2457d99105a8554d13b34d0c45091d61ea8
        B/clauses/window-02/raw.json: c9792fca995e585f638d65399727728550220e2d0cd463e1f246edc071d5ff39
        B/clauses/window-02/prompt.txt: 159775385366e3fff3c02965d27ed01b629d77c2299131da74b58391b97f1ffe
        B/clauses/window-02/meta.json: ba232e07d9da259803af4dda4e01ac1735c8037fc44de419435b9d1843a37d58
        B/clauses/window-01/raw.json: 721ef39d44299923a349fff27ad785e4b35cc533cd25034721aa05543da5cac8
        B/clauses/window-01/prompt.txt: 44d14ff9d4a00fe36b5a2f104c86141694f55388376675b1f1ab44f0d0e735d7
        B/clauses/window-01/meta.json: e43c5051befea505266d79f12a75bc3a7c5097dab2a27772ca46d4ef5a406d29
        B/tables/TABLE-1-page-4-1/raw.json: 325ed506c0951e866295e5a1d24b2e6144fe76c4a7b283abf8aca52199ee6ebc
        B/tables/TABLE-1-page-4-1/prompt.txt: 84e9736ee9afd6ac25b24ca5ea3d3d7cf7f54ae3e7f992149aa13ef08634faa1
        B/tables/TABLE-1-page-4-1/meta.json: a0845aa4c7b1a51a6fc5eb8c2302ce6fbdb395805bddc8f61d394a57d7ca5495
        B/tables/TABLE-2-page-4-2/raw.json: 9ad23a835abf2c6f3601a8bc5046f2f486f2d4ff26eed314d9a314df9be9e4cb
        B/tables/TABLE-2-page-4-2/prompt.txt: 113df11589cb1f2e53cd263540586e37eacb2059fb1ded5cc3fb9d3fae95c559
        B/tables/TABLE-2-page-4-2/meta.json: a4c8927207a00bf1ce4e22ffeee68315e9daea90fa3f2250da655bab2f1af6ce
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
      pdf_sha256: 0aab187171d50dda12559003dd6f8fc1b500aa589d5e28c9e9d9814780bff658
      source_review: _compare/relationships-2026-11-16/review-current/Basilakos2015
      source_status_sha256: 654b36e894ff29f6b12fd959374e0412cb03a2af4a9e02539020e762a91daf9e
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R005
    exposure:
      text: damage to the insula
    outcome:
      text: severity of speech errors characteristic of AOS
    analysis_label: ROI analysis
    relation: association
    evidence_ids:
    - P5-S1-C3
    qualifier_ids:
    - P5-S1-C3
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 0aab187171d50dda12559003dd6f8fc1b500aa589d5e28c9e9d9814780bff658
      source_review: _compare/relationships-2026-11-16/review-current/Basilakos2015
      source_status_sha256: 654b36e894ff29f6b12fd959374e0412cb03a2af4a9e02539020e762a91daf9e
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Accounting without a linked unit P1-S2-C8
      - Accounting without a linked unit P1-S2-C9
      - Result passage disposed without unit P2-S2-C8
      - Result passage disposed without unit P3-S1-C3
      - Unaccounted source passage P1-S2-C8
      - Unaccounted source passage P1-S2-C9
      - Result passage disposed without unit P3-S3-C10
      - Result passage disposed without unit P3-S3-C11
      - Result passage disposed without unit P3-S3-C12
      - Result passage disposed without unit P3-S3-C13
      - Result passage disposed without unit P3-S3-C14
      - Result passage disposed without unit P4-S1-C3
      - Result passage disposed without unit P5-S2-C5
      unattached_null_or_qualifier_ids:
      - P3-S3-C11
      - P3-S3-C14
      suppressed_nonrepresented_units: 9
      default_disposition_count_requires_completeness_check: 93
      unselected_timing_passages: []
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P3-S4-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P3-S4-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P3-S4-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P2-S4-C1
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P3-S1-C3
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      empty_frame_slots_require_confirmation:
      - validation
      - personal_factors
      - tested_personal_effects
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-4-1
      - TABLE-2-page-4-2
      unlinked_tables: []
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P2-S2
        - P2-S4
        - P3-S4
        - P4-S2
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 0aab187171d50dda12559003dd6f8fc1b500aa589d5e28c9e9d9814780bff658
      source_review: _compare/relationships-2026-11-16/review-current/Basilakos2015
      source_status_sha256: 654b36e894ff29f6b12fd959374e0412cb03a2af4a9e02539020e762a91daf9e
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S2-C8
      disposition: represented
      result_indexes:
      - 0
      reason: States brain damage associated with AOS was most strongly associated
        with cortical motor and somatosensory areas.
    - source_id: P1-S2-C9
      disposition: represented
      result_indexes:
      - 1
      reason: States deficits attributed to AOS or aphasia associated with temporal
        lobe and inferior precentral frontal regions.
    - source_id: P2-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes patient demographics (aphasia type/severity).
    - source_id: P2-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports mean Western Aphasia Battery scores.
    - source_id: P3-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports inter-rater reliability coefficient.
    - source_id: P3-S3-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports number of patients classified with AOS.
    - source_id: P3-S3-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports number of AOS patients without aphasia.
    - source_id: P3-S3-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports aphasia classification for AOS patients.
    - source_id: P3-S3-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports number of patients with concomitant dysarthria.
    - source_id: P3-S3-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports number of patients with aphasia only or no deficits.
    - source_id: P3-S4-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports number of voxels surviving thresholding.
    - source_id: P3-S4-C5
      disposition: represented
      result_indexes:
      - 2
      reason: Identifies small region where damage predicted both AOS and aphasic
        errors.
    - source_id: P3-S4-C9
      disposition: represented
      result_indexes:
      - 0
      - 1
      reason: Describes distribution of clusters for AOS-specific and aphasic speech
        errors.
    - source_id: P4-S1-C3
      disposition: repeated
      result_indexes:
      - 0
      - 1
      reason: General conclusion restating that AOS and aphasia result from unique
        patterns of damage.
    - source_id: P4-S1-C4
      disposition: represented
      result_indexes:
      - 0
      reason: Identifies cortical motor and somatosensory areas as predictors of AOS
        errors.
    - source_id: P4-S2-C1
      disposition: represented
      result_indexes:
      - 3
      reason: Table 1 identifies insula as an ROI associated with aphasia.
    - source_id: P4-S2-C4
      disposition: repeated
      result_indexes:
      - 3
      reason: Example of superior temporal gyrus association with aphasia.
    - source_id: P4-S2-C10
      disposition: repeated
      result_indexes:
      - 0
      reason: Example of precentral gyrus association with AOS.
    - source_id: P5-S1-C3
      disposition: represented
      result_indexes:
      - 3
      - 4
      reason: States insula predicted aphasia errors but not AOS errors.
    - source_id: P5-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes general lesion coverage of the left hemisphere.
    - source_id: P5-S1-C7
      disposition: represented
      result_indexes:
      - 6
      reason: States study did not replicate IFGpo as crucial for AOS.
    - source_id: P5-S1-C8
      disposition: repeated
      result_indexes:
      - 5
      - 6
      reason: Provides voxel percentages for IFGpo in AOS and aphasia clusters.
    - source_id: P5-S2-C3
      disposition: represented
      result_indexes:
      - 5
      - 6
      reason: Quantifies IFGpo contribution to aphasia and AOS clusters.
    - source_id: P5-S2-C5
      disposition: repeated
      result_indexes:
      - 0
      reason: Conclusion implicating cortical motor and somatosensory areas in AOS.
    unresolved_coverage: []
    pending_source_ids:
    - P2-S2-C7
    - P2-S2-C8
    - P3-S1-C3
    - P3-S3-C10
    - P3-S3-C11
    - P3-S3-C12
    - P3-S3-C13
    - P3-S3-C14
    - P3-S4-C3
    - P4-S1-C3
    - P4-S2-C4
    - P4-S2-C10
    - P5-S1-C4
    - P5-S1-C7
    - P5-S1-C8
    - P5-S2-C5
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-4-1
    - TABLE-2-page-4-2
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P2-S2-C2
      recruited_sample:
      - P2-S2-C3
      eligibility:
      - P2-S2-C3
      - P2-S2-C4
      - P2-S2-C5
      imaging_provenance:
      - P3-S1-C4
      - P3-S4-C8
      imaging_timing:
      - P2-S2-C6
      outcome_timing:
      - P2-S2-C6
      outcome_definition:
      - P2-S2-C6
      - P2-S2-C12
      - P2-S3-C3
      - P2-S3-C5
      - P2-S3-C6
      - P2-S3-C9
      validation: []
      analysis_restrictions:
      - P3-S3-C1
      - P3-S3-C2
      dependent_variable_statement:
      - P1-S2-C7
      - P3-S3-C8
      limitations:
      - P4-S1-C5
      - P4-S1-C6
      - P4-S1-C7
      - P5-S1-C4
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P3-S3-C1
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P2-S2-C2
      - P2-S2-C7
      - P2-S2-C8
      - P3-S3-C10
      - P3-S3-C12
      - P3-S3-C13
      - P3-S3-C14
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: internal_cross_validation
    held_selections:
    - slot: dependent_variable_statement
      source_id: P3-S4-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P3-S4-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P3-S4-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P2-S4-C1
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P3-S1-C3
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
      pdf_sha256: 0aab187171d50dda12559003dd6f8fc1b500aa589d5e28c9e9d9814780bff658
      review_sha256: a1379c8c7b8bd0a0208e2f467a73dd93d11ea2c6272f616c669947f768a6176f
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
      - P5-S1-C3
      source_result: The study found no evidence of insula involvement in predicting
        the severity of speech errors characteristic of AOS, although damage to the
        insula was a significant predictor for speech errors that can occur in aphasia.
        This null result for AOS was observed despite the method's demonstrated sensitivity
        to detect significant results in the insula for aphasia-related errors.
      result_status: not_detected
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis corresponds to the ROI analysis of the insula
            regarding AOS-specific errors, as described in P5-S1-C3 and P5-S1-C6.
            The source explicitly discusses the lack of evidence for insula involvement
            in AOS prediction within the context of the ROI analysis.
          source_ids:
          - P5-S1-C3
          - P5-S1-C6
        direction:
          answer: fits
          reason: The draft correctly identifies the result as a null finding ('no_effect'
            / 'not a significant predictor') for AOS-specific errors, while correctly
            noting the significant association for aphasia errors. This preserves
            the distinction between the detected association for aphasia and the undetected
            association for AOS.
          source_ids:
          - P5-S1-C3
        construct:
          answer: fits
          reason: The exposure (insula damage) and outcome (AOS speech error severity)
            are correctly identified. The patient measurement is correctly classified
            as template_lesion_overlap, as the analysis involved overlaying patient
            lesion maps (derived from T1 signal intensity) onto reference atlas ROIs
            (JHU atlas), rather than using patient-specific diffusion tractography
            or raw voxel tissue values as the primary metric for the ROI claim.
          source_ids:
          - P5-S1-C3
          - P5-S1-C5
          - P3-S2-C4
        qualifications:
          answer: fits
          reason: The draft includes the critical qualification that the method was
            sensitive enough to detect insula damage for aphasia errors, which supports
            the validity of the null result for AOS. It also correctly notes the limitation
            regarding the JHU atlas not dividing the insula into sub-regions.
          source_ids:
          - P5-S1-C3
          - P5-S1-C5
        missing_material_caveat:
          answer: fits
          reason: No material caveats are missing. The draft captures the key context
            that the null result is specific to AOS errors and contrasts it with the
            positive finding for aphasia errors, which is essential for interpreting
            the null result as a specific lack of association rather than a methodological
            failure.
          source_ids:
          - P5-S1-C3
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
      id: R005
      exposure:
        text: damage to the insula
      outcome:
        text: severity of speech errors characteristic of AOS
      analysis_label: ROI analysis
      relation: association
      evidence_ids:
      - P5-S1-C3
      qualifier_ids:
      - P5-S1-C3
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 0aab187171d50dda12559003dd6f8fc1b500aa589d5e28c9e9d9814780bff658
        source_review: _compare/relationships-2026-11-16/review-current/Basilakos2015
        source_status_sha256: 654b36e894ff29f6b12fd959374e0412cb03a2af4a9e02539020e762a91daf9e
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P2-S2-C6:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 0aab187171d50dda12559003dd6f8fc1b500aa589d5e28c9e9d9814780bff658
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 8b02e5e913afb8df19486a1b47083f520ca25c6492b2732c26abbf3404a75bd7
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S2-C6
          page: 2
          text_layer_sha256: 8b02e5e913afb8df19486a1b47083f520ca25c6492b2732c26abbf3404a75bd7
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "All were tested at the chronic phase of recovery (ie, >6 months\
          \ post \nstroke; mean month post onset, 52.5±38.9)."
        anchor_text: "All were tested at the chronic phase of recovery (ie, >6 months\
          \ post \nstroke; mean month post onset, 52.5±38.9)."
        excluded_fragments: []
        image_sha256: 136915b60d0c1bb428b6c6d8c375520815c07b67696da300813e37c8682c03a9
        transcription: All were tested at the chronic phase of recovery (ie, >6 months
          post stroke; mean month post onset, 52.5±38.9)
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 5
  quote: "It has also been used in many \nstudies to explicitly describe and further\
    \ localize production \ndeficits in AOS19 and progressive AOS.16–18,20\nAlthough\
    \ previous work has localized AOS to the left SPGI \nof the insula12,13 or the\
    \ left IFG,10,11 this study provides con-\nverging evidence between the neuroanatomical\
    \ underpinnings \nof severity ratings of AOS using the ASRS and neuroimag-\ning\
    \ findings with recent investigations into the localiza-\ntion of poststroke AOS19\
    \ and primary progressive apraxia of \nspeech.16–20 We did not find evidence of\
    \ insula involvement in \npredicting AOS, similar to recent studies with primary\
    \ pro-\ngressive apraxia of speech.17,18 Furthermore, a recent func-\ntional MRI\
    \ study in neurologically intact individuals15 found \nthat the SPGI is not involved\
    \ in complex articulation tasks as \npreviously suggested by patient data.12,13\
    \ Clearly, our methods \nwere sufficient for detecting statistically significant\
    \ results in \nthe insula, as damage to this area was a significant predictor\
    \ \nfor speech errors that can occur in aphasia but did not survive \nthresholding\
    \ for severity of speech errors that are character-\nistic of AOS."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-20'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
