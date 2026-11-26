---
id: race_atrophy_naming_outcome
name: race or estimated atrophy
kind: predictor
findings:
- id: f1
  target: naming_outcome
  target_kind: prognosis
  claim: Adding white or black race or estimated atrophy as an independent variable in logistic regression did not improve the models, and none of these variables were independently associated with the achievement of the highest quartile of object naming.
  direction: no_effect
  relationship: correlational
  method: structural_MRI
  sample:
    n: 42
    population: adults who sustained a single left hemisphere ischemic stroke resulting in aphasia
    phase: not_reported
    time_post_onset: Not transcribed; confirm from the original PDF population and timing passages.
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Relatively small sample size
  - Convenience sample
  - Unable to control for amount or type of language rehabilitation
  - Absence of information about initial severity
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Patient race (white/Caucasian or black/African American) or estimated brain atrophy (measured as the ratio of brain volume to CSF volume in the right hemisphere only). Analysis was performed using multivariable logistic regression; Outcome was dichotomized as achievement of the highest quartile of object naming. Additional metadata has not been transcribed; review the pending-field flags before approval. PDF image reading (P2-S1-C9, two-model agreement, human verification pending): Methods


    Participants

    We carried out a cross-sectional study of a convenience sample of a consecutive series of 42 adults who had sustained a single left hemisphere ischemic stroke resulting in aphasia, were at least 3 months after the onset of stroke, and were evaluated at Johns Hopkins Hospital or Johns Hopkins Bayview Medical Center between December 2007 and July 2011. Original text-layer quotation is preserved below. Publication correction (human verification pending): Observational MRI-derived leukoaraiosis/atrophy and clinical predictor analysis. No randomized allocation; structural MRI measurement and logistic regression are retained.'
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
    - not_transcribed:sample.time_post_onset
    - proposed_concept:naming_outcome
    - publication_correction_pending_human_verification
  citation: '@Wright2018'
  source_passages:
  - section: Original source P4-S1-C4
    page: 4
    quote: 'Adding white or black race or estimated atrophy as an in-

      dependent variable in logistic regression did not improve the

      models, and none of these variables were independently as-

      sociated with outcome.'
    supports: claim
  - section: Original source P2-S1-C9
    page: 2
    quote: 'Methods

      Participants

      We carried out a cross-sectional study of a convenience sample

      of a consecutive series of 42 adults who had sustained a single

      left hemisphere ischemic stroke resulting in aphasia, were at

      least 3 months after the onset of stroke, and were evaluated at

      Johns Hopkins Hospital or Johns Hopkins Bayview Medical

      Center between December 2007 and July 2011.'
    supports: sample
  - section: Original source P2-S2-C6
    page: 2
    quote: 'Participants were studied 3

      to 157 (mean ± SD 39 ± 36, median 28, mode 12) months after

      stroke.'
    supports: sample
  - section: Original source P3-S2-C11
    page: 3
    quote: 'We repeated analyses to include race and

      estimated atrophy (ratio of brain volume to CSF volume in

      the RH only) to determine whether race or estimated brain

      atrophy, which might be related to leukoaraiosis, could ac-

      count for the eﬀects of leukoaraiosis.'
    supports: method
  - section: Original source P5-S2-C2
    page: 5
    quote: 'Limitations of the study include the relatively small sample

      size, which limited our ability to comprehensively evaluate

      the eﬀect of lesion location and all possible comorbid

      conditions that can aﬀect outcome.'
    supports: limitation
  - section: Original source P5-S2-C3
    page: 5
    quote: 'We also were not able to

      control for the amount or type of language rehabilitation.'
    supports: limitation
  - section: Original source P6-S1-C7
    page: 6
    quote: 'Finally, the absence of information about initial severity is

      a limitation.'
    supports: limitation
  design: cross-sectional
predictor_type: demographic
short_definition: Patient race (white/Caucasian or black/African American) or estimated brain atrophy (measured as the ratio of brain volume to CSF volume in the right hemisphere only).
assessment: []
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-26'
relationship_review:
  paper: Wright2018
  proposal_id: R006
  review_status_sha256: c12440dab75a08373eecbd87db1ec08477ea3c15d3a690b70e6df36cea48f953
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 44181aa9e7d17350c10f110fa7a6bc511170a3d011ab874f556aa91e16a32b10
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 44181aa9e7d17350c10f110fa7a6bc511170a3d011ab874f556aa91e16a32b10
        A/passages.json: a0c5ac0138fe939a52852275da0dd669190231334264768a176f3e8392e3946b
        A/raw.json: 8da1a941fa4d9ff20fd975fdd3af8d112f9f38b8ee443a4b64ad005ce23e7c9d
        A/source-units.json: a8aafd57cee36a560a28c1fc54a7cd63cef5287bee63e0867d419868d5214273
        A/full-source-units.json: 7ca2b9f7c21f85e3a2b24d972704d1f36669da1749dcedac5f72610cfee40417
        A/meta.json: 33a2566810a0a1e89a2ef17cb9ed6734b0b583cb3a592abf08f89c1a860721c0
        A/table-images/page-5.png: 58380f477be717b6a45b494b7a8623891f88601758f281abfb9997d2f030dccb
        A/table-images/page-4.png: 66528a64c36a9a83cf9b571b7d2094597304507663eff3514acee75246a9ce8b
        A/table-images/TABLE-1-page-4-1.png: e8566f1589626d2d5e00aa5b08c6acf311192152105e094d816c123858aee1f7
        A/table-images/manifest.json: 8d970d627679a6638947aeeaafdf7546e7ee8b8c02c36a365ea26c922f455deb
        A/table-images/TABLE-2-page-5-1.png: 9749ad44019c379f99f94a3d98cbbfb763b04a3f1f9719c86af6f0c3af713d61
        A/clauses/window-03/raw.json: a559ef5141e427149e4d968692a998453893654cc8477eeed44714af16571139
        A/clauses/window-03/prompt.txt: 1a0ce06516ce4fe30c919c54ca8d3f49ba714e55479304803d66045c93c41828
        A/clauses/window-03/meta.json: da71599135e17986e78fbf2d2dc83da6129a335159f410d37f8a7c148bcaabc7
        A/clauses/window-04/raw.json: 9a54cf4dbb0ff23a146d30f4440d10770973ff45cb8912d99ab1dd326e38771f
        A/clauses/window-04/prompt.txt: 80d5912e8939ff1ddba916a9c815c00117e1f628befee3a362a19f4f26c2bcde
        A/clauses/window-04/meta.json: c9ab5ffe0e79ec1fd74c874dc1a0ae2749c95084d019ad5d0e1e49737f9e23b7
        A/clauses/window-05/raw.json: 7d2971daf36960cbc2347718f94fd2e43c51b0f3a92361da656ed8d69a8921aa
        A/clauses/window-05/prompt.txt: e6476a8cddb902f5596e84df011c15f519e8fdb05ed5f176c19c95732090dd24
        A/clauses/window-05/meta.json: 2e2926c002e8163c758511961f5050fd36e3b60a477d165c4c371e5503375271
        A/clauses/window-02/raw.json: bf63c1ecac4c7140f52902dee7ea999d331e0957d2f1313642b827ec2b190424
        A/clauses/window-02/prompt.txt: 96b12207280ce2c09ea8c693bc84d0824cae4a348c55456e33506aa1cd436d0b
        A/clauses/window-02/meta.json: 90d3d415dfe13e8930db633eb4e231e0ddbb784586477ba864e378aff1564984
        A/clauses/window-01/raw.json: 307259b2b3168eb9b9ba36f6154ef491f433eb47978ec8cd83af49a491bc7615
        A/clauses/window-01/prompt.txt: 46929e67a92c58c3b830f9ad4171e8375f39f7808c11edef24f32dfc8521623c
        A/clauses/window-01/meta.json: 0b16351d8645426135dae53014b4d02781d21e39fe176fd9eca4f1f82d6ffc00
        A/tables/TABLE-2-page-5-2/raw.json: db326efdb6fe268b7e2dc3647b39c12908d119ae5ad001044589c7374f28a8db
        A/tables/TABLE-2-page-5-2/prompt.txt: 607bd2c421887e8e014c65090725d04a2debfa6ec317f98bfd4755cd6c3e6d55
        A/tables/TABLE-2-page-5-2/meta.json: 0add64bab6ced88cf40ef5e61f3e983694841d1640a43520f0959e967bdd012b
        A/tables/TABLE-1-page-4-1/raw.json: 7804110f8292ca6dfb90ec37d290e535c62ec799c8b10e00e1e47eb619c4cbc8
        A/tables/TABLE-1-page-4-1/prompt.txt: 1703ec120607fe733a9d7d812c3bbb0c72dc41d6706b199af75d72ce682e3c54
        A/tables/TABLE-1-page-4-1/meta.json: 175ccb3efb542335ba2211431abb117228af5be49cf52e244edf77633bb10c55
        B/passages.json: a0c5ac0138fe939a52852275da0dd669190231334264768a176f3e8392e3946b
        B/raw.json: b2e9cde10dfa2344fe77411c5296b512762f6d87947da463cb5e92fb8a26e631
        B/source-units.json: a8aafd57cee36a560a28c1fc54a7cd63cef5287bee63e0867d419868d5214273
        B/full-source-units.json: 7ca2b9f7c21f85e3a2b24d972704d1f36669da1749dcedac5f72610cfee40417
        B/meta.json: 69950c62af5bdb40c9af6a3de67252b1e73107fcf9d31548e8ca5d82d6a4e8d6
        B/table-images/page-5.png: 58380f477be717b6a45b494b7a8623891f88601758f281abfb9997d2f030dccb
        B/table-images/page-4.png: 66528a64c36a9a83cf9b571b7d2094597304507663eff3514acee75246a9ce8b
        B/table-images/TABLE-1-page-4-1.png: e8566f1589626d2d5e00aa5b08c6acf311192152105e094d816c123858aee1f7
        B/table-images/manifest.json: ecd559e8cad5b77e5055c2456609e814adaffdfd447ced450a62c350a66bdf0e
        B/table-images/TABLE-2-page-5-1.png: 9749ad44019c379f99f94a3d98cbbfb763b04a3f1f9719c86af6f0c3af713d61
        B/clauses/window-03/raw.json: 5c1134db213f18a9b6f944b4a09258621c27e413c31232b6249ea0d9a3bb150c
        B/clauses/window-03/prompt.txt: 1a0ce06516ce4fe30c919c54ca8d3f49ba714e55479304803d66045c93c41828
        B/clauses/window-03/meta.json: 6e47b80ba18c35f31d14ec7be3e89dc46efd5fd3bac06606adaad17597282568
        B/clauses/window-04/raw.json: 67fa2320b5b87d71910cfc4c90ab38c7bd404062654a37d9d26488e979b1130a
        B/clauses/window-04/prompt.txt: 80d5912e8939ff1ddba916a9c815c00117e1f628befee3a362a19f4f26c2bcde
        B/clauses/window-04/meta.json: beb8c780e4ad73a269b09d77657808caa535f775e2a81446aeb9d7c7d3b684b2
        B/clauses/window-05/raw.json: 7d2971daf36960cbc2347718f94fd2e43c51b0f3a92361da656ed8d69a8921aa
        B/clauses/window-05/prompt.txt: e6476a8cddb902f5596e84df011c15f519e8fdb05ed5f176c19c95732090dd24
        B/clauses/window-05/meta.json: 2d0322e0817ea42fcbd935e362a15c1cc6dcd8a9050b9fd160c060769d9ed4ed
        B/clauses/window-02/raw.json: d3ca0819be9b081bb1dda0fa0c38253b32498e270659bda4c4835765bb10eaef
        B/clauses/window-02/prompt.txt: 96b12207280ce2c09ea8c693bc84d0824cae4a348c55456e33506aa1cd436d0b
        B/clauses/window-02/meta.json: 30e88b56ce57e4bbf389589f0ec9208bb40c4596fb24e54c17c1197f20445e9b
        B/clauses/window-01/raw.json: 5634c22344204247e1ec6ff3611bb57c615381e2265ddaec5ff50c8f22fd145e
        B/clauses/window-01/prompt.txt: 46929e67a92c58c3b830f9ad4171e8375f39f7808c11edef24f32dfc8521623c
        B/clauses/window-01/meta.json: 0a8ff90fe8a4029461479c8f427eb793fc8039bfca8ba5f2691c221d2e52f49e
        B/tables/TABLE-2-page-5-2/raw.json: 1c46452ec42e5d8c4a58797aeb4286dc76c134e5af20932ba500133a1dc272af
        B/tables/TABLE-2-page-5-2/prompt.txt: 607bd2c421887e8e014c65090725d04a2debfa6ec317f98bfd4755cd6c3e6d55
        B/tables/TABLE-2-page-5-2/meta.json: b40da700b01e0edbb2efe76dc7ca20ae68520632b81593670472f83db205b0f0
        B/tables/TABLE-1-page-4-1/raw.json: 0f36053d992834dd862ebe9b6fbf06637b89bb696f208fb0e3dd3664ce7babb6
        B/tables/TABLE-1-page-4-1/prompt.txt: 1703ec120607fe733a9d7d812c3bbb0c72dc41d6706b199af75d72ce682e3c54
        B/tables/TABLE-1-page-4-1/meta.json: 02fee8a44c1e863bdcb13c244c9a604f61bcb1e63ae7d3eb4e0c5d860ac8552e
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
      pdf_sha256: 44181aa9e7d17350c10f110fa7a6bc511170a3d011ab874f556aa91e16a32b10
      source_review: _compare/relationships-2026-11-16/review-current/Wright2018
      source_status_sha256: 8776e7e002241f180102cda9ef0b15eff637ef8fbce24016e00e7218267b8d99
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R006
    exposure:
      text: race or estimated atrophy
    outcome:
      text: naming outcome
    analysis_label: Multivariable logistic regression (Race/Atrophy adjustment)
    relation: association
    evidence_ids:
    - P4-S1-C4
    qualifier_ids:
    - P3-S2-C11
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 44181aa9e7d17350c10f110fa7a6bc511170a3d011ab874f556aa91e16a32b10
      source_review: _compare/relationships-2026-11-16/review-current/Wright2018
      source_status_sha256: 8776e7e002241f180102cda9ef0b15eff637ef8fbce24016e00e7218267b8d99
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P3-S1-C5
      - Result passage disposed without unit P3-S1-C7
      - Result passage disposed without unit P3-S2-C10
      - 'window 6: invalid/duplicate disposition P6-S1-C7'
      unattached_null_or_qualifier_ids: []
      suppressed_nonrepresented_units: 14
      default_disposition_count_requires_completeness_check: 85
      unselected_timing_passages:
      - P2-S1-C9
      - P2-S2-C7
      - P6-S1-C4
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P4-S1-C1
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: dependent_variable_statement
        source_id: P4-S1-C3
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C1
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: dependent_variable_statement
        source_id: P5-S2-C2
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: validation
        source_id: P6-S1-C11
        reason: No validation-design cue; inspect the source rather than inferring a design
      - slot: tested_personal_effects
        source_id: P3-S2-C11
        reason: No current-result classification; a covariate description is not an individual test
      empty_frame_slots_require_confirmation:
      - validation
      - personal_factors
      unclassified_extraction_ids:
      - P4-S1-C12
      table_review_required:
      - TABLE-1-page-4-1
      - TABLE-2-page-5-2
      unlinked_tables:
      - TABLE-1-page-4-1
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness. Figures are not automatically interpreted.
        caption_candidate_units: []
      approval: Not performed. Structural checks and model selections do not establish semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 44181aa9e7d17350c10f110fa7a6bc511170a3d011ab874f556aa91e16a32b10
      source_review: _compare/relationships-2026-11-16/review-current/Wright2018
      source_status_sha256: 8776e7e002241f180102cda9ef0b15eff637ef8fbce24016e00e7218267b8d99
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C7
      disposition: represented
      result_indexes:
      - 0
      reason: Reports correlation between leukoaraiosis and naming/fluency.
    - source_id: P1-S1-C8
      disposition: represented
      result_indexes:
      - 1
      reason: Reports association between severe leukoaraiosis and failure to achieve highest quartile.
    - source_id: P1-S1-C9
      disposition: represented
      result_indexes:
      - 2
      reason: Reports independent association after controlling for covariates.
    - source_id: P2-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes risk factor prevalence in the population.
    - source_id: P3-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the CHS rating scale and process.
    - source_id: P3-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports interrater agreement (kappa) for imaging.
    - source_id: P3-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Defines the threshold for severe white matter changes.
    - source_id: P3-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discusses collinearity of comorbid conditions.
    - source_id: P3-S3-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: References Table 1 for demographics.
    - source_id: P3-S3-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports null differences in demographics between outcome groups.
    - source_id: P3-S3-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports association between object naming and other WAB scores.
    - source_id: P3-S3-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports null differences in race between outcome groups.
    - source_id: P3-S3-C8
      disposition: represented
      result_indexes:
      - 0
      reason: Reports univariate correlation results.
    - source_id: P3-S3-C9
      disposition: represented
      result_indexes:
      - 1
      reason: Reports dichotomized association results.
    - source_id: P3-S3-C10
      disposition: represented
      result_indexes:
      - 10
      reason: Reports full model predictive performance.
    - source_id: P4-S1-C1
      disposition: represented
      result_indexes:
      - 2
      - 11
      reason: Reports independent association and reduced model performance.
    - source_id: P4-S1-C2
      disposition: represented
      result_indexes:
      - 3
      reason: Reports results when lesion volume replaces STG damage.
    - source_id: P4-S1-C3
      disposition: represented
      result_indexes:
      - 4
      reason: Reports independent predictors for word fluency.
    - source_id: P4-S1-C4
      disposition: represented
      result_indexes:
      - 5
      reason: Reports null effect of race/atrophy in logistic models.
    - source_id: P4-S1-C5
      disposition: represented
      result_indexes:
      - 6
      reason: Reports null effect of race on leukoaraiosis and naming.
    - source_id: P4-S1-C6
      disposition: represented
      result_indexes:
      - 7
      reason: Reports null correlation between atrophy and naming.
    - source_id: P4-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports correlation between atrophy and age.
    - source_id: P4-S1-C8
      disposition: represented
      result_indexes:
      - 8
      reason: Reports Wilcoxon rank-sum test results.
    - source_id: P4-S1-C9
      disposition: repeated
      result_indexes:
      - 0
      - 1
      - 2
      reason: Restatement of results in discussion.
    - source_id: P4-S1-C10
      disposition: repeated
      result_indexes:
      - 2
      reason: Restatement of independent association in discussion.
    - source_id: P6-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports null difference in time since onset between groups.
    - source_id: P6-S1-C9
      disposition: repeated
      result_indexes:
      - 2
      reason: Restatement of prognostic value in discussion.
    - source_id: P6-S1-C10
      disposition: repeated
      result_indexes:
      - 2
      reason: Restatement of independence from lesion volume and time.
    unresolved_coverage:
    - source_id: P4-S1-C1
      disposition: unresolved
      reason: Unknown result index; not accepted as coverage
    pending_source_ids:
    - P2-S2-C10
    - P3-S1-C5
    - P3-S1-C7
    - P3-S1-C9
    - P3-S2-C10
    - P3-S3-C4
    - P3-S3-C5
    - P3-S3-C6
    - P3-S3-C7
    - P4-S1-C7
    - P4-S1-C9
    - P4-S1-C10
    - P6-S1-C6
    - P6-S1-C9
    - P6-S1-C10
    pending_policy: Every result passage without direct candidate evidence remains pending, including model-labelled background and restatements; those labels never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-4-1
    - TABLE-2-page-5-2
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P2-S2-C9
      recruited_sample:
      - P2-S2-C9
      eligibility:
      - P2-S2-C2
      - P2-S2-C3
      - P2-S2-C5
      imaging_provenance:
      - P3-S1-C5
      imaging_timing:
      - P1-S1-C4
      - P2-S2-C2
      - P3-S1-C5
      outcome_timing:
      - P1-S1-C3
      - P2-S2-C2
      - P2-S2-C6
      outcome_definition:
      - P2-S2-C13
      - P2-S3-C2
      validation: []
      analysis_restrictions:
      - P2-S3-C3
      - P3-S2-C7
      dependent_variable_statement:
      - P1-S1-C5
      - P2-S3-C2
      - P3-S2-C2
      - P3-S2-C8
      limitations:
      - P5-S2-C2
      - P5-S2-C3
      - P5-S2-C5
      - P5-S2-C5
      - P6-S1-C4
      - P6-S1-C7
      - P6-S1-C8
      - P6-S1-C9
      personal_factors: []
      tested_personal_effects:
      - P4-S1-C4
      - P4-S1-C5
      - P4-S1-C6
      adjustment_roles:
      - P1-S1-C5
      - P3-S2-C8
      - P3-S2-C9
      - P3-S2-C11
      - P4-S1-C4
      - P5-S1-C1
      - P6-S1-C5
      explicitly_not_adjusted:
      - P2-S2-C11
      descriptive_personal_factors:
      - P2-S2-C7
      - P2-S2-C8
      - P2-S2-C9
      - P2-S2-C10
      - P5-S1-C6
    outcome_type: status_at_assessment
    imaging_vs_outcome: precedes_outcome
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P4-S1-C1
      reason: Requires a Methods outcome definition; model selection retained for inspection only
    - slot: dependent_variable_statement
      source_id: P4-S1-C3
      reason: Requires a Methods outcome definition; model selection retained for inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C1
      reason: Requires a Methods outcome definition; model selection retained for inspection only
    - slot: dependent_variable_statement
      source_id: P5-S2-C2
      reason: Requires a Methods outcome definition; model selection retained for inspection only
    - slot: validation
      source_id: P6-S1-C11
      reason: No validation-design cue; inspect the source rather than inferring a design
    - slot: tested_personal_effects
      source_id: P3-S2-C11
      reason: No current-result classification; a covariate description is not an individual test
    policy: All slots and enums remain unverified. Held selections are not evidence of absence. Original response is preserved in frame/raw.json.
  approved: false
  source_check:
    profile: agent-repair
    scope: Agent corrected this draft against the original paper. The original automated attempt is retained as historical provenance and does not verify this revised version. Human PDF review and approval remain required. Observational MRI-derived leukoaraiosis/atrophy and clinical predictor analysis. No randomized allocation; structural MRI measurement and logistic regression are retained.
    binding:
      source_pdf_sha256: 44181aa9e7d17350c10f110fa7a6bc511170a3d011ab874f556aa91e16a32b10
      original_source_sha256: c11ceeb2dd8317c3471d4271022a2f0a455ea5542251d5364a2ce549f817746c
      repair_audit: logs/publication/draft-repairs-2026-11-26.json
      agent_repair_approved: false
    approved: false
    pending_details:
    - 'sample.time_post_onset: source confirmation required; original proposed wording remains in the audit.'
    - Detailed statistics, atlas/reference-space and structured confounder metadata not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - sample.time_post_onset
    - exact_p_values_for_race_atrophy
    normalizations:
    - field: sample.time_post_onset
      original: evaluated 3 to 157 months after stroke
      action: not_transcribed
      reason: 'Numbers not grounded in usable selected source readings: 157'
    analysis_identity:
      id: R006
      exposure:
        text: race or estimated atrophy
      outcome:
        text: naming outcome
      analysis_label: Multivariable logistic regression (Race/Atrophy adjustment)
      relation: association
      evidence_ids:
      - P4-S1-C4
      qualifier_ids:
      - P3-S2-C11
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 44181aa9e7d17350c10f110fa7a6bc511170a3d011ab874f556aa91e16a32b10
        source_review: _compare/relationships-2026-11-16/review-current/Wright2018
        source_status_sha256: 8776e7e002241f180102cda9ef0b15eff637ef8fbce24016e00e7218267b8d99
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P2-S1-C9:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 44181aa9e7d17350c10f110fa7a6bc511170a3d011ab874f556aa91e16a32b10
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 69e5cf2e9de519dcb90b5e3af875cf8eec37d330d65f7d7bfc34fbf2dbd7594a
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S1-C9
          page: 2
          text_layer_sha256: 69e5cf2e9de519dcb90b5e3af875cf8eec37d330d65f7d7bfc34fbf2dbd7594a
          models: &id001
          - gemma4:31b
          - qwen3.8:27b
          model_digests: &id002
          - 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
          - 47951e4a666180bc2aedfc93c169472f2de783696fe196efbf063f5730ecf163
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Methods

          Participants

          We carried out a cross-sectional study of a convenience sample

          of a consecutive series of 42 adults who had sustained a single

          left hemisphere ischemic stroke resulting in aphasia, were at

          least 3 months after the onset of stroke, and were evaluated at

          Johns Hopkins Hospital or Johns Hopkins Bayview Medical

          Center between December 2007 and July 2011.'
        anchor_text: 'Methods

          Participants

          We carried out a cross-sectional study of a convenience sample

          of a consecutive series of 42 adults who had sustained a single

          left hemisphere ischemic stroke resulting in aphasia, were at

          least 3 months after the onset of stroke, and were evaluated at

          Johns Hopkins Hospital or Johns Hopkins Bayview Medical

          Center between December 2007 and July 2011.'
        excluded_fragments: []
        image_sha256: 14209b93262d8f75c4c35d1a616d859928f5e552ba7f4bf5af2b5380d4d982be
        transcription: 'Methods


          Participants

          We carried out a cross-sectional study of a convenience sample of a consecutive series of 42 adults who had sustained a single left hemisphere ischemic stroke resulting in aphasia, were at least 3 months after the onset of stroke, and were evaluated at Johns Hopkins Hospital or Johns Hopkins Bayview Medical Center between December 2007 and July 2011.'
      P2-S2-C6:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 44181aa9e7d17350c10f110fa7a6bc511170a3d011ab874f556aa91e16a32b10
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 687df9946a1124a2898e4adeda23aeab9f1f595124a50d1b83302e3393d8842b
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S2-C6
          page: 2
          text_layer_sha256: 687df9946a1124a2898e4adeda23aeab9f1f595124a50d1b83302e3393d8842b
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: 'Participants were studied 3

          to 157 (mean ± SD 39 ± 36, median 28, mode 12) months after

          stroke.'
        anchor_text: 'Participants were studied 3

          to 157 (mean ± SD 39 ± 36, median 28, mode 12) months after

          stroke.'
        excluded_fragments: []
        image_sha256: 23dfd1a51b5bf9c99470dad49632aac4d6b31dbf2bcedea60aca425ffbab78ea
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
    publication_correction:
      date: '2026-11-26T00:24:06.569756+00:00'
      by: agent:source-repair
      approved: false
      human_verification_required: true
      original_source_sha256: c11ceeb2dd8317c3471d4271022a2f0a455ea5542251d5364a2ce549f817746c
      source_pdf_sha256: 44181aa9e7d17350c10f110fa7a6bc511170a3d011ab874f556aa91e16a32b10
      pdf_pages:
      - 2
      - 3
      - 4
      note: Observational MRI-derived leukoaraiosis/atrophy and clinical predictor analysis. No randomized allocation; structural MRI measurement and logistic regression are retained.
      audit: logs/publication/draft-repairs-2026-11-26.json
    checked_by: agent:source-repair (human approval pending)
    date: '2026-11-26'
    corrections:
    - Observational MRI-derived leukoaraiosis/atrophy and clinical predictor analysis. No randomized allocation; structural MRI measurement and logistic regression are retained.
    original_scope: Independent model text review of core meaning; not human approval or complete PDF verification
    original_core_review:
      own_result_source_ids:
      - P4-S1-C4
      source_result: Adding white or black race or estimated atrophy as an independent variable in logistic regression did not improve the models, and none of these variables were independently associated with the outcome (achievement of the highest quartile of object naming).
      result_status: not_detected
      patient_measurement: non_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The source (P4-S1-C4) describes the result of adding race and estimated atrophy to the logistic regression model. The proposed core correctly identifies this as a test of these specific variables within the multivariable model context established in P3-S2-C11.
          source_ids:
          - P4-S1-C4
          - P3-S2-C11
        direction:
          answer: fits
          reason: The source states that the variables were 'not independently associated' and 'did not improve the models'. The proposed core uses 'no_effect' to represent this lack of detected association, which is faithful to the null finding reported in the source.
          source_ids:
          - P4-S1-C4
        construct:
          answer: fits
          reason: The exposure (race, estimated atrophy) and outcome (naming outcome, specifically highest quartile of object naming) are correctly identified. The patient measurement is non_imaging (demographic and volumetric ratio), distinct from the imaging-based leukoaraiosis or lesion overlap measures.
          source_ids:
          - P4-S1-C4
          - P3-S2-C11
        qualifications:
          answer: fits
          reason: The proposed core includes the necessary qualifications that the analysis was multivariable logistic regression and the outcome was dichotomized. It correctly frames the result as a null finding for these specific covariates.
          source_ids:
          - P3-S2-C11
          - P4-S1-C4
        missing_material_caveat:
          answer: fits
          reason: The core captures the essential null result. While the source notes that atrophy correlated with leukoaraiosis (P4-S1-C6), the specific claim in P4-S1-C4 is that they did not account for the effect or improve the model. The core reflects this specific finding without omitting material caveats that would change the interpretation of the null result for these variables.
          source_ids:
          - P4-S1-C4
      optional_pending:
      - sample.time_post_onset
      - exact_p_values_for_race_atrophy
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
      pdf_sha256: 44181aa9e7d17350c10f110fa7a6bc511170a3d011ab874f556aa91e16a32b10
      review_sha256: c12440dab75a08373eecbd87db1ec08477ea3c15d3a690b70e6df36cea48f953
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
  page: 4
  quote: 'Adding white or black race or estimated atrophy as an in-

    dependent variable in logistic regression did not improve the

    models, and none of these variables were independently as-

    sociated with outcome.'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-26'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor roles, all qualifiers, source audit issues and main-PDF tables/figures; check missing results. This model proposal is not verified.'
- id: publication-source-repair-2026-11-26
  status: pending
  by: agent:source-repair
  date: '2026-11-26'
  note: Observational MRI-derived leukoaraiosis/atrophy and clinical predictor analysis. No randomized allocation; structural MRI measurement and logistic regression are retained. Original automated review applies to the original version; verify the corrected finding against the cited pages before approval.
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
