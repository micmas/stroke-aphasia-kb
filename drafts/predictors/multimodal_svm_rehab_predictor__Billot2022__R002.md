---
id: multimodal_svm_rehab_predictor
name: Multimodal SVM Predictor
kind: predictor
findings:
- id: f1
  target: rehabilitation_responsiveness
  target_kind: prognosis
  claim: A support vector machine model combining aphasia severity, demographics,
    FA, percentage of spared gray matter tissue, and resting-state fMRI connectivity
    performed significantly better in predicting responsiveness to language rehabilitation
    than any model trained on an individual feature set.
  direction: likely
  relationship: correlational
  method: MVPA
  sample:
    n: 55
    population: individuals with chronic poststroke aphasia due to a single left-hemisphere
      stroke
    phase: not_reported
    time_post_onset: prediction based on pretreatment baseline assessments for response
      after 12 weeks of language treatment
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Small sample size
  - Leave-one-out cross-validation was used for both feature selection and model training/validation
    on the same sample set
  - Different types of language treatments were administered across three sites
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: A support vector machine model trained on a combination
    of aphasia severity (AQ), demographics, average fractional anisotropy (FA) in
    12 tracts of interest, percentage of spared tissue in 69 left-hemisphere gray
    matter regions (AAL atlas), and resting-state fMRI connectivity (bivariate Fisher-transformed
    Pearson correlations between 50 bilateral AAL regions). Responsiveness was defined
    as a cutoff of 25 percentage points change in accuracy on treatment probes; The
    optimal model performed significantly better than a model trained on all available
    feature sets combined. Additional metadata has not been transcribed; review the
    pending-field flags before approval. PDF image reading (P1-S1-C13, two-model agreement,
    human verification pending): METHODS: Fifty-five individuals with chronic poststroke
    aphasia underwent a battery of standardized assessments and structural and functional
    magnetic resonance imaging scans, and received 12 weeks of language treatment
    Original text-layer quotation is preserved below. PDF image reading (P3-S2-C3,
    two-model agreement, human verification pending): . Participants were

    classified into responders (n=33) and nonresponders (n=22)

    based on a cutoff of 25 percentage points change in accuracy

    (Figure 3 and Supplemental Material) Original text-layer quotation is preserved
    below. Reconcile this new analysis with earlier drafts and source-review decisions
    for the paper; new candidate IDs do not carry earlier decisions forward.'
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
    - proposed_concept:rehabilitation_responsiveness
  citation: '@Billot2022'
  source_passages:
  - section: Original source P1-S1-C13
    page: 1
    quote: "METHODS: Fifty-five individuals with chronic poststroke aphasia underwent\
      \ a battery of standardized assessments and \nstructural and functional magnetic\
      \ resonance imaging scans, and received 12 weeks of language treatment."
    supports: sample
  - section: Original source P1-S1-C15
    page: 1
    quote: "RESULTS: The best prediction performance was achieved by a support vector\
      \ machine model trained on aphasia severity, \ndemographics, measures of anatomic\
      \ integrity and resting-state functional connectivity (F1=0.94)."
    supports: claim
  - section: Original source P1-S2-C3
    page: 1
    quote: "This model resulted in \na significantly superior prediction performance\
      \ compared with support vector machine models trained on all feature sets \n\
      (F1=0.82, P<0.001) or a single feature set (F1 range=0.68–0.84, P<0.001)."
    supports: claim
  - section: Original source P2-S2-C6
    page: 2
    quote: "Participants\nParticipants were 55 individuals (37 male) with chronic\
      \ post-\nstroke aphasia due to a single left-hemisphere stroke (mean \nage =58.8\
      \ years, mean time poststroke onset =59.0 months, \nmean education =15.8 years)."
    supports: sample
  - section: Original source P3-S1-C5
    page: 3
    quote: "MRI Data Preprocessing\nSeveral brain structural and functional measures\
      \ were calcu-\nlated including (1) lesion volume extracted through in-house\
      \ \nMATLAB scripts9 from lesion masks manually drawn using \nMRIcron software38\
      \ and normalized to MNI space, (2) the integ-\nrity of gray and white matter\
      \ regions calculated by computing \nthe percentage of spared tissue in 69 left-hemisphere\
      \ gray \nmatter regions of the Automated Anatomical Labeling atlas,39 \nand\
      \ 36 white matter tracts of the BCBToolKit40 probabilistic \natlas, respectively,\
      \ (3) average fractional anisotropy (FA) in 12 \ntracts of interest, computed\
      \ from diffusion tensor imaging data \npreprocessed using the Advanced Diffusion\
      \ Preprocessing \nPipeline41 and the Northwestern University Neuroimaging Data\
      \ \nArchive,42 and converted to tracts using the Automated Fiber \nQuantification\
      \ software (deterministic tractography),43 and (4) \nresting-state functional\
      \ MRI (rs-fMRI) connectivity, involving \nthe rs-fMRI data first preprocessed\
      \ in fMRIPrep version 1.4.1, \na Nipype-based tool,44 and then through the CONN\
      \ toolbox45 \nto extract bivariate Fisher-transformed Pearson correlations \n\
      between 50 bilateral anatomic regions of interest specified \nusing the Automated\
      \ Anatomical Labeling atlas 3,46 resulting \nin 625 pairwise correlations per\
      \ individual."
    supports: method
  - section: Original source P3-S2-C3
    page: 3
    quote: "Participants were \nclassified into responders (n=33) and nonresponders\
      \ (n=22) \nbased on a cutoff of 25 percentage points change in accuracy \n(Figure 3\
      \ and Supplemental Material)."
    supports: claim
  - section: Original source P5-S1-C6
    page: 5
    quote: "The optimal \nSVM model included aphasia severity, demographics, \nFA,\
      \ percentage of spared tissue in gray matter regions \nand resting-state fMRI\
      \ connectivity, and performed sig-\nnificantly better than any of the models\
      \ trained on an \nindividual feature set (P<0.001)."
    supports: claim
  - section: Original source P7-S3-C6
    page: 7
    quote: "Ideally, we should use k-fold cross-validation in all com-\nputer experiments,\
      \ but we used leave-one-out cross-val-\nidation for both feature selection and\
      \ model training and \nvalidation steps."
    supports: limitation
  - section: Original source P7-S3-C7
    page: 7
    quote: "Furthermore, the samples used in both \nsteps should be different, but\
      \ we used the same set of \nsamples in both steps."
    supports: limitation
predictor_type: imaging_metric
short_definition: A support vector machine model trained on a combination of aphasia
  severity (AQ), demographics, average fractional anisotropy (FA) in 12 tracts of
  interest, percentage of spared tissue in 69 left-hemisphere gray matter regions
  (AAL atlas), and resting-state fMRI connectivity (bivariate Fisher-transformed Pearson
  correlations between 50 bilateral AAL regions).
assessment:
- Western Aphasia Battery—Revised
- T1-weighted MRI
- Diffusion Tensor Imaging
- resting-state fMRI
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-20'
relationship_review:
  paper: Billot2022
  proposal_id: R002
  review_status_sha256: 099adf505dd74730725750668810b97638779c0e3edd48dfae011dee1b619e38
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 1e6a0688da54c3f918aa2181f40dcf54da1a145eed8cdfd86117aa81323b1297
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 1e6a0688da54c3f918aa2181f40dcf54da1a145eed8cdfd86117aa81323b1297
        A/passages.json: 7d2862b7dabf29c7f8ad1ef6a59155f819764f0b18427d5c467d08a82f483979
        A/raw.json: 8020dc530458fb610259f15b700cf043c8972def275c220ba0b98dc3831e4e39
        A/source-units.json: e78b8faaede5efeb9d38be3f72f7d53f013d29954db75901ec9394ed40eef707
        A/full-source-units.json: c674c18c0b3ab19a986f4d5998fcd8154bb45d0ffab1da14ad33674d2463b640
        A/meta.json: 3d6269f8dc7a758d6ad428a41555e8f9fc5bc6ec815c6d84ac0a26a565db56f7
        A/table-images/manifest.json: 399c92d78198173c73610222a18f0811a8405ebefd5afff49daab5726989f5b9
        A/clauses/window-03/raw.json: c976e36cf9957081ddb19d295e1a5ac36042898dfc390af301e4381d56205436
        A/clauses/window-03/prompt.txt: 7adf50864a090b39702db486b1cd8edd8ef72665f8eb5fce9588ffbb012b0b46
        A/clauses/window-03/meta.json: 21f5a83dd1b96acaa39929920f2920d7b6ac2338b21ba7c6402d6ba257532d48
        A/clauses/window-04/raw.json: f73c8f4b349371edceefbbe018f02d6c7d3a51d947fdc92038624e58ff3f98d2
        A/clauses/window-04/prompt.txt: 7f88cb74517026a297d65083ad496ff90966846faca7e5f3a779a73877ffd705
        A/clauses/window-04/meta.json: a92405bbc98abf3228f519c72e4880a132e36343c38c885534e83a7e7c3dd61d
        A/clauses/window-05/raw.json: 39e11a640bf54428e7108916d10189b8972c7e9dd746a78fdb9e584e74c359d0
        A/clauses/window-05/prompt.txt: 3be9714e448e98c5f34a85f85c802f8a2d4cbe816ffb5bf016564b24e59c6d90
        A/clauses/window-05/meta.json: 624442dcbfdd0dc901977576652d740ccc5b30c00fc4c5a5186ac0f7cd4e4827
        A/clauses/window-02/raw.json: 9d3a59ad54599b65ce0bb29565f9c9aeb4178c74caf785887a13f7fe1d59294b
        A/clauses/window-02/prompt.txt: ece1bcea42584ac1636fcb58222d1e027b0648f8c5dd15ad3e66c06e714a9a1c
        A/clauses/window-02/meta.json: c4bfdfd4219c1f7bc3964ee44bd0b196ac563c27c2a516669100c41d367aca00
        A/clauses/window-01/raw.json: 615036bf40fcc9e4793b5d073c8400b051fe2589b05b19ff5c1bae258f85bf23
        A/clauses/window-01/prompt.txt: 3e1debc994097ad767b463bef56c4e85b97b61e97feddbf56371b2de66250769
        A/clauses/window-01/meta.json: beed0907d3f3161d5e86b8b36aed6863f45ff68b20945c436e1ed946451793a3
        B/passages.json: 7d2862b7dabf29c7f8ad1ef6a59155f819764f0b18427d5c467d08a82f483979
        B/raw.json: 74de5a001c270ffb09b491d3ec1e7de6b924a7f34b162ccad434dd45d4b82a3b
        B/source-units.json: e78b8faaede5efeb9d38be3f72f7d53f013d29954db75901ec9394ed40eef707
        B/full-source-units.json: c674c18c0b3ab19a986f4d5998fcd8154bb45d0ffab1da14ad33674d2463b640
        B/meta.json: d574d4020b7eb0f41180bbe8811f4f639f04506d71ca5e5de0462186b83cc945
        B/table-images/manifest.json: 399c92d78198173c73610222a18f0811a8405ebefd5afff49daab5726989f5b9
        B/clauses/window-03/raw.json: 0cb74ae012503c9d4097f1f9b41e559ad927430b2246212083a2c29c95c33bee
        B/clauses/window-03/prompt.txt: 7adf50864a090b39702db486b1cd8edd8ef72665f8eb5fce9588ffbb012b0b46
        B/clauses/window-03/meta.json: 9910048f9c0c33e3d59def4d96b5ab81d3e84de30068765c48219952782c7e8e
        B/clauses/window-04/raw.json: a6f85522cd640a419d4b6344f56f5a23999b0669c4266f8e3a19595eb72993aa
        B/clauses/window-04/prompt.txt: 7f88cb74517026a297d65083ad496ff90966846faca7e5f3a779a73877ffd705
        B/clauses/window-04/meta.json: e5f96c782d996f0a9e79898636f2e6b99155c346ae260b70f3821a7d821f0381
        B/clauses/window-05/raw.json: f7cfe3af3df26b28acaa63a8639a72ae75f9257f1a39c0efdbbef8c166f82247
        B/clauses/window-05/prompt.txt: 3be9714e448e98c5f34a85f85c802f8a2d4cbe816ffb5bf016564b24e59c6d90
        B/clauses/window-05/meta.json: 905b3d83259fb751c4b6096fa6b01035856bcee999435144a7fac55cd2fd69b1
        B/clauses/window-02/raw.json: 357f177df2be64d739654f7f1eeede1341fecad086d57fdeba2bf45db2ed2961
        B/clauses/window-02/prompt.txt: ece1bcea42584ac1636fcb58222d1e027b0648f8c5dd15ad3e66c06e714a9a1c
        B/clauses/window-02/meta.json: 960674753f14db22bddd1ebeb2e3a1960a64176ef7bbf8a4a44ce9cf5f24d572
        B/clauses/window-01/raw.json: 7c5431af1425d9ecc4a0de8a74038c6389a82c2f33bb71f3cda2dc28b5fbbce2
        B/clauses/window-01/prompt.txt: 3e1debc994097ad767b463bef56c4e85b97b61e97feddbf56371b2de66250769
        B/clauses/window-01/meta.json: 51f9c35d35dfd528349bdcef77805cd95ba1eac3c47a562ef920d9d2e3e6f7ee
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
      pdf_sha256: 1e6a0688da54c3f918aa2181f40dcf54da1a145eed8cdfd86117aa81323b1297
      source_review: _compare/relationships-2026-11-16/review-current/Billot2022
      source_status_sha256: a529a4360b3223c4f1dcf7ea828d1526f82d0bcb3a091bf726269feffa1cc9ba
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R002
    exposure:
      text: combination of aphasia severity, demographics, FA, percentage spared in
        gray matter regions and resting-state fMRI connectivity
    outcome:
      text: responsiveness to rehabilitation in chronic poststroke aphasia
    analysis_label: SVM Model Comparison (Optimal vs Single Feature)
    relation: model_comparison
    evidence_ids:
    - P1-S2-C3
    - P5-S1-C6
    - P6-S2-C4
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
      pdf_sha256: 1e6a0688da54c3f918aa2181f40dcf54da1a145eed8cdfd86117aa81323b1297
      source_review: _compare/relationships-2026-11-16/review-current/Billot2022
      source_status_sha256: a529a4360b3223c4f1dcf7ea828d1526f82d0bcb3a091bf726269feffa1cc9ba
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P4-S1-C3
      - Result passage disposed without unit P7-S3-C4
      unattached_null_or_qualifier_ids: []
      suppressed_nonrepresented_units: 6
      default_disposition_count_requires_completeness_check: 105
      unselected_timing_passages:
      - P1-S1-C13
      - P2-S2-C6
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P5-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: tested_personal_effects
        source_id: P1-S1-C14
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P2-S1-C8
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P2-S2-C2
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P3-S1-C5
        reason: No current-result classification; a covariate description is not an
          individual test
      empty_frame_slots_require_confirmation:
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required: []
      unlinked_tables: []
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P2-S2
        - P3-S2
        - P4-S1
        - P4-S2
        - P5-S2
        - P6-S1
        - P6-S2
        - P7-S1
        - P7-S3
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 1e6a0688da54c3f918aa2181f40dcf54da1a145eed8cdfd86117aa81323b1297
      source_review: _compare/relationships-2026-11-16/review-current/Billot2022
      source_status_sha256: a529a4360b3223c4f1dcf7ea828d1526f82d0bcb3a091bf726269feffa1cc9ba
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C15
      disposition: represented
      result_indexes:
      - 0
      reason: States best prediction performance achieved by SVM on specific feature
        set.
    - source_id: P1-S2-C3
      disposition: represented
      result_indexes:
      - 1
      - 2
      reason: Compares optimal model to all-feature and single-feature models.
    - source_id: P1-S2-C4
      disposition: represented
      result_indexes:
      - 3
      reason: Identifies best RF model based on RS data.
    - source_id: P4-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes PCA variance of cognitive composite scores, not a clinical
        relationship.
    - source_id: P4-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: References figures showing evaluation metrics.
    - source_id: P4-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: References figures showing F1 score distributions.
    - source_id: P5-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: DOI information.
    - source_id: P5-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: References supplemental tables.
    - source_id: P5-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: References supplemental table for statistical comparisons.
    - source_id: P5-S1-C5
      disposition: represented
      result_indexes:
      - 0
      reason: Reports maximum accuracy, F1, precision, and recall for SVM models.
    - source_id: P5-S1-C6
      disposition: represented
      result_indexes:
      - 0
      - 1
      reason: Defines optimal SVM feature set and its superiority over single feature
        models.
    - source_id: P5-S1-C7
      disposition: represented
      result_indexes:
      - 0
      reason: Reports classification count (51/55) for the best performing model.
    - source_id: P5-S1-C8
      disposition: represented
      result_indexes:
      - 8
      reason: Notes that top 10 SVM models included structural integrity and RS data.
    - source_id: P5-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes composition of top SVM models.
    - source_id: P5-S1-C10
      disposition: represented
      result_indexes:
      - 2
      reason: Compares all-feature SVM model to optimal SVM model.
    - source_id: P5-S1-C11
      disposition: represented
      result_indexes:
      - 6
      reason: Reports performance of individual SVM models (AQ and RS).
    - source_id: P5-S2-C1
      disposition: repeated
      result_indexes:
      - 6
      reason: Restates individual feature performance.
    - source_id: P5-S2-C2
      disposition: represented
      result_indexes:
      - 7
      reason: Compares top RF models to SVM models.
    - source_id: P5-S2-C3
      disposition: represented
      result_indexes:
      - 3
      - 4
      reason: Identifies optimal RF models and their performance.
    - source_id: P5-S2-C4
      disposition: represented
      result_indexes:
      - 4
      reason: Reports classification count (46/55) for top RF models.
    - source_id: P5-S2-C5
      disposition: represented
      result_indexes:
      - 8
      reason: Notes RS inclusion in top RF models.
    - source_id: P5-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Restates that all-feature RF model did not improve performance.
    - source_id: P6-S1-C2
      disposition: represented
      result_indexes:
      - 4
      reason: States all-feature RF model did not improve performance compared to
        optimal subset.
    - source_id: P6-S1-C3
      disposition: represented
      result_indexes:
      - 8
      reason: Identifies RS as predominant feature in top models.
    - source_id: P6-S1-C6
      disposition: repeated
      result_indexes:
      - 1
      reason: Restates that combined subsets outperform single types or all types.
    - source_id: P6-S1-C7
      disposition: represented
      result_indexes:
      - 8
      reason: Identifies RS, anatomical integrity, and aphasia severity as consistently
        important.
    - source_id: P6-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of benefit of combining functional and structural MRI.
    - source_id: P6-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion on combining all data types.
    - source_id: P6-S2-C4
      disposition: represented
      result_indexes:
      - 1
      reason: States single feature set models were significantly lower than optimal
        combination.
    - source_id: P7-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion on feature combinations.
    - source_id: P7-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion on variable importance.
    - source_id: P7-S1-C4
      disposition: represented
      result_indexes:
      - 8
      reason: States RS connectivity strongly predicts response.
    - source_id: P7-S1-C5
      disposition: represented
      result_indexes:
      - 8
      reason: States RS data contributed to all top performing models.
    - source_id: P7-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion on functional reorganization and language network.
    - source_id: P7-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion on spared tissue regions.
    - source_id: P7-S1-C9
      disposition: represented
      result_indexes:
      - 7
      reason: States algorithm choice influences performance.
    - source_id: P7-S2-C2
      disposition: represented
      result_indexes:
      - 7
      reason: States SVM models resulted in higher prediction performance than RF.
    - source_id: P7-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion on multifactorial nature of recovery.
    - source_id: P7-S3-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Analysis of site-information as a feature.
    - source_id: P7-S3-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of responder counts per site.
    - source_id: P7-S3-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Conclusion on site influence.
    unresolved_coverage: []
    pending_source_ids:
    - P4-S1-C3
    - P4-S2-C4
    - P4-S2-C5
    - P5-S1-C2
    - P5-S1-C3
    - P5-S1-C4
    - P5-S1-C8
    - P5-S1-C9
    - P5-S2-C1
    - P5-S2-C6
    - P6-S1-C6
    - P6-S1-C7
    - P6-S1-C9
    - P6-S1-C10
    - P7-S1-C2
    - P7-S1-C3
    - P7-S1-C6
    - P7-S1-C7
    - P7-S1-C9
    - P7-S2-C5
    - P7-S3-C3
    - P7-S3-C4
    - P7-S3-C5
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review: []
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P2-S2-C9
      recruited_sample:
      - P2-S2-C8
      - P2-S2-C10
      eligibility:
      - P2-S2-C12
      imaging_provenance:
      - P3-S1-C5
      imaging_timing:
      - P3-S2-C6
      outcome_timing:
      - P3-S2-C6
      outcome_definition:
      - P3-S2-C3
      - P4-S2-C6
      validation:
      - P4-S1-C6
      analysis_restrictions:
      - P7-S3-C2
      dependent_variable_statement:
      - P1-S1-C14
      - P2-S2-C1
      - P3-S1-C8
      - P4-S1-C6
      limitations:
      - P7-S2-C9
      - P7-S3-C3
      - P7-S3-C6
      - P7-S3-C7
      personal_factors:
      - P4-S2-C10
      tested_personal_effects:
      - P1-S1-C15
      - P5-S1-C5
      - P5-S1-C6
      - P5-S1-C11
      - P6-S1-C7
      - P7-S1-C4
      - P7-S2-C5
      adjustment_roles:
      - P4-S1-C5
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P2-S2-C6
      - P4-S2-C10
    outcome_type: change_from_baseline
    imaging_vs_outcome: precedes_outcome
    validation_type: internal_cross_validation
    held_selections:
    - slot: dependent_variable_statement
      source_id: P5-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: tested_personal_effects
      source_id: P1-S1-C14
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P2-S1-C8
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P2-S2-C2
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P3-S1-C5
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
      pdf_sha256: 1e6a0688da54c3f918aa2181f40dcf54da1a145eed8cdfd86117aa81323b1297
      review_sha256: 099adf505dd74730725750668810b97638779c0e3edd48dfae011dee1b619e38
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
      - P1-S2-C3
      - P5-S1-C6
      - P6-S2-C4
      source_result: The optimal SVM model, trained on a combination of aphasia severity,
        demographics, fractional anisotropy (FA), percentage of spared gray matter
        tissue, and resting-state fMRI connectivity, achieved a significantly superior
        prediction performance (F1=0.94) compared to SVM models trained on any single
        feature set (F1 range 0.68–0.84, P<0.001) or all feature sets combined (F1=0.82,
        P<0.001).
      result_status: model_comparison
      patient_measurement: multiple
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis is a model comparison between an optimal multimodal
            SVM and single-feature SVMs. The source explicitly states the optimal
            model (combining specific features) outperformed single-feature models
            (P<0.001). The draft correctly identifies this as a model comparison where
            the combination is superior.
          source_ids:
          - P1-S2-C3
          - P5-S1-C6
          - P6-S2-C4
        direction:
          answer: fits
          reason: The direction of the finding is that the combined model performs
            better (higher F1) than single-feature models. The draft's claim that
            the combined model 'performed significantly better' aligns with the source's
            'significantly superior prediction performance'.
          source_ids:
          - P1-S2-C3
          - P5-S1-C6
        construct:
          answer: fits
          reason: The exposure is correctly identified as the combination of specific
            features (aphasia severity, demographics, FA, % spared GM, rs-fMRI). The
            outcome is responsiveness to rehabilitation. The patient measurement is
            'multiple' because the model uses a combination of behavioral, demographic,
            and multimodal neuroimaging data (structural and functional), not a single
            modality like template_lesion_overlap or patient_diffusion alone. The
            source confirms the use of these specific inputs in P5-S1-C6.
          source_ids:
          - P5-S1-C6
          - P3-S1-C5
        qualifications:
          answer: fits
          reason: The draft includes the qualification that the model outperformed
            the 'all feature sets' model, which is a key finding in the source (P5-S1-C10,
            P6-S1-C2). It also notes the definition of responsiveness (25% cutoff).
            The draft does not incorrectly claim the single features were non-significant,
            but rather that the combination was superior.
          source_ids:
          - P5-S1-C10
          - P6-S1-C2
          - P3-S2-C3
        missing_material_caveat:
          answer: fits
          reason: The draft includes limitations regarding small sample size and LOOCV
            usage, which are material caveats mentioned in the source (P7-S2-C9, P7-S3-C6,
            P7-S3-C7). No material caveats that change the interpretation of the model
            comparison are omitted.
          source_ids:
          - P7-S2-C9
          - P7-S3-C6
          - P7-S3-C7
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
      id: R002
      exposure:
        text: combination of aphasia severity, demographics, FA, percentage spared
          in gray matter regions and resting-state fMRI connectivity
      outcome:
        text: responsiveness to rehabilitation in chronic poststroke aphasia
      analysis_label: SVM Model Comparison (Optimal vs Single Feature)
      relation: model_comparison
      evidence_ids:
      - P1-S2-C3
      - P5-S1-C6
      - P6-S2-C4
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
        pdf_sha256: 1e6a0688da54c3f918aa2181f40dcf54da1a145eed8cdfd86117aa81323b1297
        source_review: _compare/relationships-2026-11-16/review-current/Billot2022
        source_status_sha256: a529a4360b3223c4f1dcf7ea828d1526f82d0bcb3a091bf726269feffa1cc9ba
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P1-S1-C13:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 1e6a0688da54c3f918aa2181f40dcf54da1a145eed8cdfd86117aa81323b1297
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 0dede0cad3eb121e171bff683759e442bf146c9158092830e8456d6998c999af
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P1-S1-C13
          page: 1
          text_layer_sha256: 0dede0cad3eb121e171bff683759e442bf146c9158092830e8456d6998c999af
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "METHODS: Fifty-five individuals with chronic poststroke aphasia\
          \ underwent a battery of standardized assessments and \nstructural and functional\
          \ magnetic resonance imaging scans, and received 12 weeks of language treatment."
        anchor_text: "METHODS: Fifty-five individuals with chronic poststroke aphasia\
          \ underwent a battery of standardized assessments and \nstructural and functional\
          \ magnetic resonance imaging scans, and received 12 weeks of language treatment."
        excluded_fragments: []
        image_sha256: 3b2fee009bc6b8c5c90f0b082225f26dc90497e1d7bad8297a5941c3249af244
        transcription: 'METHODS: Fifty-five individuals with chronic poststroke aphasia
          underwent a battery of standardized assessments and structural and functional
          magnetic resonance imaging scans, and received 12 weeks of language treatment'
      P2-S2-C6:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 1e6a0688da54c3f918aa2181f40dcf54da1a145eed8cdfd86117aa81323b1297
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 7eb5ce8b1b158f3ac1f9c3c0cba42d843c44d30c19ac53f14a9588b751050738
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S2-C6
          page: 2
          text_layer_sha256: 7eb5ce8b1b158f3ac1f9c3c0cba42d843c44d30c19ac53f14a9588b751050738
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: "Participants\nParticipants were 55 individuals (37 male) with\
          \ chronic post-\nstroke aphasia due to a single left-hemisphere stroke (mean\
          \ \nage =58.8 years, mean time poststroke onset =59.0 months, \nmean education\
          \ =15.8 years)."
        anchor_text: "Participants\nParticipants were 55 individuals (37 male) with\
          \ chronic post-\nstroke aphasia due to a single left-hemisphere stroke (mean\
          \ \nage =58.8 years, mean time poststroke onset =59.0 months, \nmean education\
          \ =15.8 years)."
        excluded_fragments: []
        image_sha256: f49526698c20d05b53505f735f78f81e35a70d09f63ac004efcc3b4e3d8f1ef9
      P3-S2-C3:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 1e6a0688da54c3f918aa2181f40dcf54da1a145eed8cdfd86117aa81323b1297
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 78b8da799afc943df585dcdb54f3b6f1f0817c47fb98f65a86f1a5aa49818c94
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S2-C3
          page: 3
          text_layer_sha256: 78b8da799afc943df585dcdb54f3b6f1f0817c47fb98f65a86f1a5aa49818c94
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "Participants were \nclassified into responders (n=33) and\
          \ nonresponders (n=22) \nbased on a cutoff of 25 percentage points change\
          \ in accuracy \n(Figure 3 and Supplemental Material)."
        anchor_text: "Participants were \nclassified into responders (n=33) and nonresponders\
          \ (n=22) \nbased on a cutoff of 25 percentage points change in accuracy\
          \ \n(Figure 3 and Supplemental Material)."
        excluded_fragments: []
        image_sha256: 72f90c4674fa58a4a55711f6d451c2a351b02a71b5b1b1a6cb526fdbb489b873
        transcription: '. Participants were

          classified into responders (n=33) and nonresponders (n=22)

          based on a cutoff of 25 percentage points change in accuracy

          (Figure 3 and Supplemental Material)'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 1
  quote: "METHODS: Fifty-five individuals with chronic poststroke aphasia underwent\
    \ a battery of standardized assessments and \nstructural and functional magnetic\
    \ resonance imaging scans, and received 12 weeks of language treatment."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-20'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
