---
id: stroke_severity_hemiplegia
name: stroke severity (hemiplegia diagnoses)
kind: predictor
findings:
- id: f1
  target: aphasia_rate
  target_kind: impairment
  claim: A significant effect of stroke severity, as measured by diagnoses of hemiplegia,
    on aphasia rates was observed, and this effect was independent of sex.
  direction: likely
  relationship: correlational
  method: behavioral_only
  sample:
    n: not_reported
    population: stroke patients in a US American healthcare database (NIS)
    phase: not_reported
    time_post_onset: Data from 2011-2014
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Hemiplegia diagnoses are described as a 'somewhat crude proxy' for stroke severity
  - Data are summary data for participating states per year rather than individual
    patient data
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Measured as the number of hemiparesis/hemiplegia diagnoses
    using ICD-9 code 342.90 in a healthcare database. Analyzed using a linear mixed-effects
    regression model including age and sex as covariates; The relationship was found
    to be independent of sex effects. Additional metadata has not been transcribed;
    review the pending-field flags before approval. PDF image reading (P9-S1-C6, two-model
    agreement, human verification pending): Results of database analysis

    A total of 1,967,038 stroke patients were found in the database (1,014,239 women,
    952,799 men) in the period from 2011 to 2014. Original text-layer quotation is
    preserved below. PDF image reading (P8-S2-C13, two-model agreement, human verification
    pending): . These data are all summery data for the participating states for a
    particular year (2011–2014) Original text-layer quotation is preserved below.'
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
    - not_transcribed:sample.n
    - proposed_concept:aphasia_rate
  citation: '@Wallentin2018'
  source_passages:
  - section: Original source P8-S2-C4
    page: 8
    quote: 'As a proxy for stroke severity, the number of hemiparesis/hemiple-

      gia diagnoses were included (using the ICD-9 code: “342.90 Unsp Hemiplga Unspf
      Side”,

      which is the most commonly used ICD-9 code for hemiplegia/paresis in the database
      and

      which does not bias towards the dominant or nondominant side).'
    supports: method
  - section: Original source P10-S1-C2
    page: 10
    quote: 'A significant effect of age, t(274.83) = 2.11, p(uncorrected)<0.05, and
      a signifi-

      cant effect of stroke severity, t(268.73) = 4.77, p<0.001 was observed.'
    supports: claim
  - section: Original source P11-S1-C7
    page: 11
    quote: 'I also found an independent effect of stroke severity on aphasia rates
      as measured by diag-

      noses of hemiplegia.'
    supports: claim
  - section: Original source P11-S1-C9
    page: 11
    quote: In this study I found that severity effects on aphasia are independent
      of the sex effects.
    supports: claim
  - section: Original source P9-S1-C6
    page: 9
    quote: 'Results of database analysis

      A total of 1,967,038 stroke patients were found in the database (1,014,239 women,
      952,799

      men) in the period from 2011 to 2014.'
    supports: sample
  - section: Original source P11-S1-C11
    page: 11
    quote: 'It has to be said, however,

      that this analysis used a somewhat crude proxy for stroke severity.'
    supports: limitation
  - section: Original source P8-S2-C13
    page: 8
    quote: 'These data are all summery data for the

      participating states for a particular year (2011–2014).'
    supports: limitation
predictor_type: clinical
short_definition: Measured as the number of hemiparesis/hemiplegia diagnoses using
  ICD-9 code 342.90 in a healthcare database.
assessment:
- ICD-9 code 342.90
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-26'
relationship_review:
  paper: Wallentin2018
  proposal_id: R008
  review_status_sha256: c6268637d4437a0074a1f6fa20c75806b0be62dd143ed40acc63160ce04c7eda
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 2c0b802069cc237e3ab36fcd34c6dc316671c92e44194a26f1b5cf1e6814ec96
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 2c0b802069cc237e3ab36fcd34c6dc316671c92e44194a26f1b5cf1e6814ec96
        A/passages.json: f36cbfac4ffaa2c073f1653df7ae407f05a496efd1cfaad38b90b4c89f5d7456
        A/raw.json: f3b4c8523acb05007c1976eb1423db7a47044d2a5b5d4a6fdf48e151bc6945a6
        A/source-units.json: c9520e9aeb3fcef13046fbb11c2d8959ab4fa2a7f83659b0c70e7012a99447ed
        A/full-source-units.json: 4ac5d6dac018324bc2635d2f849125e3651987f602b28d5adc057b6a43a578a9
        A/meta.json: c9b9e8e8dc9149db290fe55539e989c9ee9096a4f0ece0644cb456da042e2b05
        A/table-images/page-7.png: 034c5faf385066407237be980430d4b3a2fa414f1fe13cb16ddcc3e9c4e80fcb
        A/table-images/page-4.png: 35673eb9139a632f2785850295344f0bfb4cb519924786edc06319bf614fa0d9
        A/table-images/TABLE-1-page-4-1.png: 875f66e0f2453265eb8336f69b1ef873ade1c52eef05766d91d22f0a7e3de5eb
        A/table-images/manifest.json: 3b957694cb1837168c63361b7c89e3394c60a0eaaac6616556ff375c0f189498
        A/table-images/TABLE-2-page-7-1.png: 86d3cea39f6d3b16a39ec77ee0f27d4a5f51c6f0b28d281fbfaf662a8116de9c
        A/clauses/window-03/raw.json: aa7bd6ad1718a75f8655b1fc681e95c17eb01296ba0c0ad4bc492dbf412610f8
        A/clauses/window-03/prompt.txt: 93552bcb7c8afe0fa6882901309522d3aabdddd5621c1352b4fc64d7b2e50047
        A/clauses/window-03/meta.json: 627a4b153590e86a3369d56897f78e02f630ea7ddd63f1ef86795c13c068c8e3
        A/clauses/window-04/raw.json: 1b339cf10da1cdde8c4f932c7ae089af055f384d593c9fb4eed0b673bc9cdfb5
        A/clauses/window-04/prompt.txt: b28c99497989412741fd7c967cad909f329b4b201c58d5d09774c323cf8bf288
        A/clauses/window-04/meta.json: 6648ed00e2a7936847198e98828b7f2c48df96381ff96f40b70ac6727593f5d0
        A/clauses/window-05/raw.json: fdb62ffea6285e8ed3aff051813c143e74c39f560b7dea3a6a260ce667101cd6
        A/clauses/window-05/prompt.txt: 5eb57fb2f72398328e184372b1d7f43b79b199f47babd919f62edcb2b4c725c7
        A/clauses/window-05/meta.json: f412d8a3c790d16bcf8689d64e066e0878e0a07ce756bbd83808d715e743ae95
        A/clauses/window-02/raw.json: 2c889b0ad8d0315fd3890928bec635775fc913f5bb5f3988785c9ad3c4ff96ec
        A/clauses/window-02/prompt.txt: 4ef8bd5fa4417cab6d1ff4075db782baddf955b376e616f64a33096314196872
        A/clauses/window-02/meta.json: 476090687875d2937feb7603f10c39a290539ec3593d409a63740cd0b66d5468
        A/clauses/window-07/raw.json: 599ed19fbc96bb6df0bc61c6cbd2e3888cdf49ebdaabeac732a9c1913b75964c
        A/clauses/window-07/prompt.txt: 5c1f0ce8869494a94e654985e86d905a7cf63a295a0f6b0794d46c04ce3d97bf
        A/clauses/window-07/meta.json: 3bdd3336c6ffa48cc7f6e724c469e8b1b173cf3b0e5c3b1bee274475ce019ecb
        A/clauses/window-01/raw.json: dff028f96c033dec033605be3d8c2549badcac6d032a0c6369d5cc85e60424e1
        A/clauses/window-01/prompt.txt: 2786e9f823081fa00b64983dd1c1352593d16766446e6e8ef6251e4931d74e37
        A/clauses/window-01/meta.json: 10b215e97fd23d718797aeb924ce3cd983bf89909a950a5046631142640c7943
        A/clauses/window-06/raw.json: 7bbf3a7208c05861d545f6696b37eabd2fab8adb936d987f40848a5321616352
        A/clauses/window-06/prompt.txt: 71aff44d4448a61f5bd66d7ab92b0e812d1db540d5dc25f43c11009cd6592c09
        A/clauses/window-06/meta.json: fd5279218577e27e43ff5de7cc0fd3c9349fa4970f6f610c8cca7f71d7a766c0
        A/clauses/window-08/raw.json: 8a2aabab6222663814b1682420f0885f1d91a119ceaf7b1a2642191b40e0e76b
        A/clauses/window-08/prompt.txt: cd94d5693f3e459f6f058545b5292ff7658a33f90abec3a788be968de4462f7a
        A/clauses/window-08/meta.json: dfaac4cf0a57f42a3aaf921bf3941443b9434567044306f881f6c5ac3019c8d0
        A/tables/TABLE-2-page-7-2/raw.json: b0f3a3cca80b882b6556c345959b385c9ac4efcab1d32d3d4aaccefb21fb14e4
        A/tables/TABLE-2-page-7-2/prompt.txt: 411b00f65c6d6ecaf0ceaaf7b7371d4a2861aaf1d90762f4dd410b5b2a7390e8
        A/tables/TABLE-2-page-7-2/meta.json: 7ec4fb610ab393c7b13a6a9d6209d077d17ae42ebb0fa8e4a6a64cf9bd468afb
        A/tables/TABLE-1-page-4-1/raw.json: 6e9822ca726a9eab3481e8f3561fef10a29ce9760f0374f51d5a11816eaef7a2
        A/tables/TABLE-1-page-4-1/prompt.txt: 98b81269c5534230e1ebff20fe84c6cb7cd3a6077ecfabdb657ebe491339d954
        A/tables/TABLE-1-page-4-1/meta.json: 26a824b82b38e277e54c45652f0f01a588c33401ebbec1e70661f06250df9761
        B/passages.json: f36cbfac4ffaa2c073f1653df7ae407f05a496efd1cfaad38b90b4c89f5d7456
        B/raw.json: 29854ed8940c219c82a7fe5406013ee95b478009fd4ae6ba9170a427b3b72bca
        B/source-units.json: c9520e9aeb3fcef13046fbb11c2d8959ab4fa2a7f83659b0c70e7012a99447ed
        B/full-source-units.json: 4ac5d6dac018324bc2635d2f849125e3651987f602b28d5adc057b6a43a578a9
        B/meta.json: 7ec8e3fa7c5a3878d872fe19031627d03ea485e0333b290bea35dfb6bd317489
        B/table-images/page-7.png: 034c5faf385066407237be980430d4b3a2fa414f1fe13cb16ddcc3e9c4e80fcb
        B/table-images/page-4.png: 35673eb9139a632f2785850295344f0bfb4cb519924786edc06319bf614fa0d9
        B/table-images/TABLE-1-page-4-1.png: 875f66e0f2453265eb8336f69b1ef873ade1c52eef05766d91d22f0a7e3de5eb
        B/table-images/manifest.json: 23b24f141df5e3dba75a50a5986499848a6d1843730fff4e4b89c56887b7fad1
        B/table-images/TABLE-2-page-7-1.png: 86d3cea39f6d3b16a39ec77ee0f27d4a5f51c6f0b28d281fbfaf662a8116de9c
        B/clauses/window-03/raw.json: 5b626dd14402ac0b01879f3ba92381264b14e02f4f159ccef7df9730042da73b
        B/clauses/window-03/prompt.txt: 93552bcb7c8afe0fa6882901309522d3aabdddd5621c1352b4fc64d7b2e50047
        B/clauses/window-03/meta.json: 26ac8ccaed17977851c6724912b5a036a0971b7fe9edfe1554801e64c8b493a5
        B/clauses/window-04/raw.json: 8f2d5b13fcf3641f5d4ddb2f4b032a07f96f1603f9c7117e1bc4701edcd8cf08
        B/clauses/window-04/prompt.txt: b28c99497989412741fd7c967cad909f329b4b201c58d5d09774c323cf8bf288
        B/clauses/window-04/meta.json: 0e3ad0acb2a7cd656e49b7d991c31975df6c224d251a411c6328cb8bf2a4ccfb
        B/clauses/window-05/raw.json: f8312b6020a686bfd7dc56f741254dade27f4f1f4cd2cad982b197970c4fdff2
        B/clauses/window-05/prompt.txt: 5eb57fb2f72398328e184372b1d7f43b79b199f47babd919f62edcb2b4c725c7
        B/clauses/window-05/meta.json: 9ae12b99148b90e88e433f831f4afff9ee77fbc230c494616cc9c30820a1d47e
        B/clauses/window-02/raw.json: 8429b58eceee2b356db74e73b1eb1a72ae320a54be3486c9d7df2d815959e1bc
        B/clauses/window-02/prompt.txt: 4ef8bd5fa4417cab6d1ff4075db782baddf955b376e616f64a33096314196872
        B/clauses/window-02/meta.json: 5740ae7661ff758d9b2162522c23b7ab71d64aee85dce32ec042cbe94e19e4f6
        B/clauses/window-07/raw.json: a9d3dde75f9387d0f43d670f7740b9cc5b55122bf480ca6bf82c974a452aa455
        B/clauses/window-07/prompt.txt: 5c1f0ce8869494a94e654985e86d905a7cf63a295a0f6b0794d46c04ce3d97bf
        B/clauses/window-07/meta.json: ad3847cdc41f6b45ee72461643cf3edfad50caf35f2813465237cbfbd0a71739
        B/clauses/window-01/raw.json: d476beeff81e06c8c9203f49d8bcbe10225e4dc254ee73a7cde8009b7a3c4c55
        B/clauses/window-01/prompt.txt: 2786e9f823081fa00b64983dd1c1352593d16766446e6e8ef6251e4931d74e37
        B/clauses/window-01/meta.json: b4c4550fb19fe39151bd764f1176b478d010be375b621dc196ea6ea60194f7e7
        B/clauses/window-06/raw.json: 57df33b9f0a9b9ced39eb7528283715d1958be536411d4cbc18055dc8209a3dd
        B/clauses/window-06/prompt.txt: 71aff44d4448a61f5bd66d7ab92b0e812d1db540d5dc25f43c11009cd6592c09
        B/clauses/window-06/meta.json: b7e53427124c02e0afb622db10c4785149d95c298388fd106f2ba22de78da757
        B/clauses/window-08/raw.json: 46c0f6ac287ba9f7555e4cd257d5195ee2a0ca4e9c3c8bf84ec67613c94776fa
        B/clauses/window-08/prompt.txt: cd94d5693f3e459f6f058545b5292ff7658a33f90abec3a788be968de4462f7a
        B/clauses/window-08/meta.json: 6dcd8bfd6ac18bf015fd4a3aee0df611172158f2dc5e05227b944b8ba4ed9ba3
        B/tables/TABLE-2-page-7-2/raw.json: 88a52783d3560e723a540f2ed078fcd378fb09b1188efb5598f1829fa5471dea
        B/tables/TABLE-2-page-7-2/prompt.txt: 411b00f65c6d6ecaf0ceaaf7b7371d4a2861aaf1d90762f4dd410b5b2a7390e8
        B/tables/TABLE-2-page-7-2/meta.json: 31a0933a96909f25adf00585b68d319ef5366f33bac4725ad4879d35bc5b88cf
        B/tables/TABLE-1-page-4-1/raw.json: e02a466f7a26df1b6b600c46cb1d4aa7a8f0371c496d8137bc162871cb17e006
        B/tables/TABLE-1-page-4-1/prompt.txt: 98b81269c5534230e1ebff20fe84c6cb7cd3a6077ecfabdb657ebe491339d954
        B/tables/TABLE-1-page-4-1/meta.json: a961b80902eee1e65d1699ddd05341547def381cf683aabcf5e66f849fffc26f
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
      pdf_sha256: 2c0b802069cc237e3ab36fcd34c6dc316671c92e44194a26f1b5cf1e6814ec96
      source_review: _compare/relationships-2026-11-16/review-current/Wallentin2018
      source_status_sha256: 257b1e743ed728bc0e38fed09850db12a7e32274196c545146d8cf32837e53dd
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R008
    exposure:
      text: stroke severity (hemiplegia diagnoses)
    outcome:
      text: aphasia rate
    analysis_label: linear mixed-effects regression (database)
    relation: association
    evidence_ids:
    - P10-S1-C2
    - P11-S1-C7
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
      pdf_sha256: 2c0b802069cc237e3ab36fcd34c6dc316671c92e44194a26f1b5cf1e6814ec96
      source_review: _compare/relationships-2026-11-16/review-current/Wallentin2018
      source_status_sha256: 257b1e743ed728bc0e38fed09850db12a7e32274196c545146d8cf32837e53dd
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P1-S1-C14
      - Result passage disposed without unit P5-S1-C11
      - Result passage disposed without unit P5-S1-C7
      - Result passage disposed without unit P6-S1-C12
      - Result passage disposed without unit P6-S2-C6
      - Result passage disposed without unit P7-S1-C5
      - Result passage disposed without unit P7-S1-C7
      - Result passage disposed without unit P7-S1-C8
      - Result passage disposed without unit P7-S1-C10
      - Result passage disposed without unit P7-S1-C11
      - Result passage disposed without unit P7-S1-C17
      - Result passage disposed without unit P7-S2-C9
      - Result passage disposed without unit P10-S1-C1
      - 'window 8: invalid/duplicate disposition P10-S1-C3'
      - Result passage disposed without unit P10-S1-C3
      - Result passage disposed without unit P10-S1-C5
      - Result passage disposed without unit P9-S1-C14
      - 'window 8: invalid/duplicate disposition P9-S1-C15'
      - Result passage disposed without unit P9-S1-C15
      - Result passage disposed without unit P10-S1-C11
      - Result passage disposed without unit P10-S1-C13
      - Result passage disposed without unit P10-S1-C18
      - Result passage disposed without unit P10-S1-C6
      - Result passage disposed without unit P10-S1-C7
      - Result passage disposed without unit P10-S1-C8
      - Accounting without a linked unit P11-S1-C3
      - 'window 11: invalid/duplicate disposition P11-S2-C7'
      - 'window 11: invalid/duplicate disposition P11-S2-C8'
      - Result passage disposed without unit P12-S1-C10
      unattached_null_or_qualifier_ids:
      - P6-S2-C6
      - P7-S1-C7
      - P7-S1-C10
      - P7-S2-C9
      - P10-S1-C5
      suppressed_nonrepresented_units: 3
      default_disposition_count_requires_completeness_check: 167
      unselected_timing_passages:
      - P8-S1-C4
      - P8-S1-C7
      personal_effect_slots_without_result_classification: []
      held_frame_selections: []
      empty_frame_slots_require_confirmation:
      - imaging_provenance
      - imaging_timing
      - validation
      - personal_factors
      - explicitly_not_adjusted
      unclassified_extraction_ids:
      - P2-S3-C3
      table_review_required:
      - TABLE-1-page-4-1
      - TABLE-2-page-7-2
      unlinked_tables:
      - TABLE-2-page-7-2
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P3-S1
        - P4-S1
        - P5-S1
        - P6-S1
        - P6-S2
        - P9-S1
        - P10-S1
        - P10-S2
        - P11-S1
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 2c0b802069cc237e3ab36fcd34c6dc316671c92e44194a26f1b5cf1e6814ec96
      source_review: _compare/relationships-2026-11-16/review-current/Wallentin2018
      source_status_sha256: 257b1e743ed728bc0e38fed09850db12a7e32274196c545146d8cf32837e53dd
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C12
      disposition: represented
      result_indexes:
      - 0
      reason: Reports significantly larger aphasia rates in women than men.
    - source_id: P1-S1-C14
      disposition: represented
      result_indexes:
      - 5
      reason: States sex failed to explain aphasia rate difference when age and severity
        were covariates.
    - source_id: P5-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Provides total patient counts.
    - source_id: P5-S1-C7
      disposition: represented
      result_indexes:
      - 0
      reason: Provides specific aphasia rates for females (29.6%) and males (26%).
    - source_id: P5-S1-C8
      disposition: represented
      result_indexes:
      - 0
      reason: Reports statistically significant difference in aphasia rates between
        women and men.
    - source_id: P5-S1-C9
      disposition: represented
      result_indexes:
      - 0
      reason: Reports overall sex aphasia rate ratio of 1.14.
    - source_id: P5-S1-C11
      disposition: represented
      result_indexes:
      - 0
      reason: States women are more likely to get aphasia from stroke.
    - source_id: P6-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports heterogeneity (I2) and funnel plot bias.
    - source_id: P6-S1-C3
      disposition: represented
      result_indexes:
      - 1
      reason: States publication year as covariate did not alter result and was not
        a significant predictor.
    - source_id: P6-S1-C4
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of higher aphasia rate for women.
    - source_id: P6-S1-C5
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of average aphasia rates.
    - source_id: P6-S1-C6
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of effect size.
    - source_id: P6-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison to prior meta-analysis.
    - source_id: P6-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of isolated aphasia study impact.
    - source_id: P6-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of isolated aphasia ratio.
    - source_id: P6-S1-C10
      disposition: represented
      result_indexes:
      - 1
      reason: States study year did not explain variance in sex differences.
    - source_id: P6-S1-C12
      disposition: repeated
      result_indexes:
      - 1
      reason: Restatement that no trend over time was visible.
    - source_id: P6-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Funnel plot bias result.
    - source_id: P7-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes lack of age reports in cohort.
    - source_id: P7-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation of interaction in Bersano et al. data.
    - source_id: P7-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive trend of sex difference growing with age in Bersano et al.
    - source_id: P7-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes number of studies with age info.
    - source_id: P7-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes age distribution of female vs male groups.
    - source_id: P7-S1-C12
      disposition: represented
      result_indexes:
      - 3
      - 4
      reason: Reports significant sex effect (t=5.1) and non-significant effect after
        adding age covariate (t=0.8).
    - source_id: P7-S1-C17
      disposition: background_or_descriptive
      result_indexes: []
      reason: States severity info is not reported in meta-analysis papers.
    - source_id: P7-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Funnel plot bias inspection.
    - source_id: P9-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Provides total aphasia counts for database.
    - source_id: P9-S1-C8
      disposition: represented
      result_indexes:
      - 5
      reason: Provides specific aphasia rates for females (33.2%) and males (30.2%).
    - source_id: P9-S1-C9
      disposition: represented
      result_indexes:
      - 5
      reason: Reports overall female/male aphasia rate ratio of 1.100.
    - source_id: P9-S1-C10
      disposition: represented
      result_indexes:
      - 5
      reason: Paired t-test supports existence of sex difference.
    - source_id: P9-S1-C11
      disposition: represented
      result_indexes:
      - 5
      reason: States no significant effect of sex over and above age and severity.
    - source_id: P9-S1-C14
      disposition: represented
      result_indexes:
      - 5
      reason: Replicates higher aphasia rate among women.
    - source_id: P9-S1-C15
      disposition: repeated
      result_indexes:
      - 5
      reason: Restatement that effect is explained by age.
    - source_id: P10-S1-C1
      disposition: represented
      result_indexes:
      - 5
      reason: Reports p=0.1 for sex effect in regression.
    - source_id: P10-S1-C2
      disposition: represented
      result_indexes:
      - 6
      - 7
      reason: Reports significant effect of age (p<0.05) and stroke severity (p<0.001).
    - source_id: P10-S1-C3
      disposition: repeated
      result_indexes:
      - 5
      reason: Restatement that sex is confounded by age.
    - source_id: P10-S1-C4
      disposition: represented
      result_indexes:
      - 8
      reason: Reports significant interaction between age and stroke severity.
    - source_id: P10-S1-C5
      disposition: represented
      result_indexes:
      - 9
      reason: States no other interactions (including sex/age) were significant.
    - source_id: P10-S1-C6
      disposition: repeated
      result_indexes:
      - 5
      reason: Restatement of replication of meta-analysis findings.
    - source_id: P10-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison of aphasia rates between studies.
    - source_id: P10-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports specific aphasia rates (27.7% vs 31.7%).
    - source_id: P10-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison to prior meta-analysis.
    - source_id: P10-S1-C10
      disposition: repeated
      result_indexes:
      - 5
      reason: Restatement that women are more likely to get aphasia.
    - source_id: P10-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison of rate ratios (1.10 vs 1.14).
    - source_id: P10-S1-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison of Cohen's d (0.63 vs 0.37).
    - source_id: P10-S1-C18
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes age difference between men and women.
    - source_id: P10-S1-C19
      disposition: represented
      result_indexes:
      - 6
      reason: Reports positive correlation between average age and aphasia rate.
    - source_id: P10-S2-C6
      disposition: represented
      result_indexes:
      - 5
      reason: States sex effects are no longer significant when age relationship is
        taken into account.
    - source_id: P11-S1-C1
      disposition: repeated
      result_indexes:
      - 4
      reason: Restatement that age explains away sex effect.
    - source_id: P11-S1-C2
      disposition: represented
      result_indexes:
      - 5
      reason: States no evidence of sex difference over and above age.
    - source_id: P11-S1-C5
      disposition: repeated
      result_indexes:
      - 5
      reason: Restatement of regression line for age.
    - source_id: P11-S1-C6
      disposition: repeated
      result_indexes:
      - 5
      reason: Restatement of no offset for sex.
    - source_id: P11-S1-C7
      disposition: represented
      result_indexes:
      - 7
      reason: Reports independent effect of stroke severity on aphasia rates.
    - source_id: P11-S1-C9
      disposition: represented
      result_indexes:
      - 7
      reason: States severity effects are independent of sex effects.
    - source_id: P11-S1-C14
      disposition: represented
      result_indexes:
      - 9
      reason: States database analysis showed no indication of interaction between
        sex and age.
    - source_id: P11-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Questioning interaction between age and sex.
    - source_id: P11-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Correlation between population age differences and Bersano et al. results.
    - source_id: P12-S1-C8
      disposition: repeated
      result_indexes:
      - 0
      reason: Conclusion restatement that women diagnosed more often.
    - source_id: P12-S1-C10
      disposition: repeated
      result_indexes:
      - 5
      reason: Conclusion restatement that sex difference caused by age.
    unresolved_coverage:
    - source_id: P11-S1-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P5-S1-C6
    - P5-S1-C7
    - P6-S1-C2
    - P6-S1-C4
    - P6-S1-C5
    - P6-S1-C6
    - P6-S1-C7
    - P6-S1-C8
    - P6-S1-C9
    - P6-S1-C12
    - P6-S2-C6
    - P7-S1-C5
    - P7-S1-C7
    - P7-S1-C8
    - P7-S1-C10
    - P7-S1-C11
    - P7-S1-C17
    - P7-S2-C9
    - P9-S1-C7
    - P9-S1-C8
    - P9-S1-C15
    - P10-S1-C3
    - P10-S1-C6
    - P10-S1-C7
    - P10-S1-C8
    - P10-S1-C9
    - P10-S1-C10
    - P10-S1-C11
    - P10-S1-C13
    - P10-S1-C18
    - P11-S1-C1
    - P11-S1-C5
    - P11-S1-C6
    - P11-S1-C9
    - P11-S1-C10
    - P11-S2-C3
    - P11-S2-C9
    - P12-S1-C8
    - P12-S1-C10
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-4-1
    - TABLE-2-page-7-2
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P4-S1-C1
      - P5-S1-C6
      - P9-S1-C6
      recruited_sample:
      - P1-S1-C10
      - P1-S1-C11
      - P8-S1-C3
      - P8-S1-C4
      - P8-S1-C6
      eligibility:
      - P3-S1-C10
      imaging_provenance: []
      imaging_timing: []
      outcome_timing:
      - P3-S1-C1
      outcome_definition:
      - P3-S1-C1
      - P8-S2-C3
      validation: []
      analysis_restrictions:
      - P3-S1-C8
      dependent_variable_statement:
      - P3-S1-C1
      - P8-S3-C3
      - P9-S1-C1
      limitations:
      - P7-S2-C3
      - P7-S2-C4
      - P7-S2-C10
      - P7-S2-C12
      - P11-S3-C2
      personal_factors: []
      tested_personal_effects:
      - P1-S1-C14
      - P7-S1-C12
      - P9-S1-C11
      - P10-S1-C1
      - P11-S1-C1
      adjustment_roles:
      - P1-S1-C14
      - P5-S1-C5
      - P7-S1-C12
      - P8-S1-C9
      - P9-S1-C2
      - P9-S1-C4
      - P10-S1-C2
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P7-S1-C2
      - P7-S1-C11
      - P8-S1-C8
      - P9-S1-C6
    outcome_type: status_at_assessment
    imaging_vs_outcome: not_stated
    validation_type: none_described
    held_selections: []
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
      pdf_sha256: 2c0b802069cc237e3ab36fcd34c6dc316671c92e44194a26f1b5cf1e6814ec96
      review_sha256: c6268637d4437a0074a1f6fa20c75806b0be62dd143ed40acc63160ce04c7eda
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
      - P10-S1-C2
      - P11-S1-C7
      source_result: In a linear mixed-effects regression analysis of US healthcare
        database data (2011-2014), a significant effect of stroke severity (proxied
        by hemiplegia diagnoses) on aphasia rates was observed (t=4.77, p<0.001).
        This effect was found to be independent of sex effects, which were not significant
        after adjusting for age and severity.
      result_status: detected
      patient_measurement: non_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis corresponds to the database analysis described
            in the source, specifically the linear mixed-effects regression using
            HCUP data. The source explicitly identifies this model and its components
            (P8-S2-C15, P9-S1-C1 to C5).
          source_ids:
          - P8-S2-C15
          - P9-S1-C1
          - P9-S1-C2
        direction:
          answer: fits
          reason: The source reports a significant effect of stroke severity on aphasia
            rates (P10-S1-C2). The proposed claim states a 'significant effect...
            was observed', which aligns with the detected association. The direction
            is not explicitly 'positive' or 'negative' in the claim text, but 'significant
            effect' is faithful to the source's report of significance without specifying
            direction in the summary claim, though the source implies a positive correlation
            (P10-S1-C19 mentions positive correlation between age and aphasia, and
            severity is a covariate). The claim does not contradict the source.
          source_ids:
          - P10-S1-C2
          - P11-S1-C7
        construct:
          answer: fits
          reason: The exposure is correctly identified as stroke severity proxied
            by hemiplegia diagnoses (ICD-9 342.90) as per P8-S2-C4. The outcome is
            aphasia rate (ICD-9 784.3) as per P8-S2-C3. The method is correctly identified
            as linear mixed-effects regression on database data. The patient measurement
            is non-imaging (administrative/ICD codes), not diffusion or functional
            imaging.
          source_ids:
          - P8-S2-C4
          - P8-S2-C3
          - P8-S2-C15
        qualifications:
          answer: fits
          reason: The proposed qualifications include the use of a linear mixed-effects
            model with age and sex as covariates, and the finding that the effect
            is independent of sex. This matches the source text in P11-S1-C9 ('severity
            effects on aphasia are independent of the sex effects') and P10-S1-C2
            (significant effect of severity observed in the model including sex and
            age). The limitation regarding the 'crude proxy' is also included.
          source_ids:
          - P11-S1-C9
          - P10-S1-C2
          - P11-S1-C11
        missing_material_caveat:
          answer: fits
          reason: The draft includes the key limitation that hemiplegia is a 'somewhat
            crude proxy' for stroke severity (P11-S1-C11) and that the data are summary
            data (P8-S2-C13). No other material caveats that would change the interpretation
            of the severity-aphasia association appear to be missing from the provided
            source window. The fact that sex was not significant is a result of the
            model, not a caveat on the severity finding itself, but the independence
            is correctly stated.
          source_ids:
          - P11-S1-C11
          - P8-S2-C13
      optional_pending:
      - Specific p-value and t-statistic for the severity effect are not transcribed
        in the claim text, though present in source P10-S1-C2.
      - Exact sample size breakdown by state/year is not transcribed, only total N.
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Sample size requires source confirmation; it has not been transcribed.
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Specific p-value and t-statistic for the severity effect are not transcribed
      in the claim text, though present in source P10-S1-C2.
    - Exact sample size breakdown by state/year is not transcribed, only total N.
    normalizations:
    - field: sample.n
      original: 1967038
      action: not_transcribed
      reason: Not supported by selected quotations
    analysis_identity:
      id: R008
      exposure:
        text: stroke severity (hemiplegia diagnoses)
      outcome:
        text: aphasia rate
      analysis_label: linear mixed-effects regression (database)
      relation: association
      evidence_ids:
      - P10-S1-C2
      - P11-S1-C7
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
        pdf_sha256: 2c0b802069cc237e3ab36fcd34c6dc316671c92e44194a26f1b5cf1e6814ec96
        source_review: _compare/relationships-2026-11-16/review-current/Wallentin2018
        source_status_sha256: 257b1e743ed728bc0e38fed09850db12a7e32274196c545146d8cf32837e53dd
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P9-S1-C6:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 2c0b802069cc237e3ab36fcd34c6dc316671c92e44194a26f1b5cf1e6814ec96
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 0932b5c5cfb24d50ef886e7de3fb6d05f0c0543ae8bfb705ffc998096eabcdcf
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P9-S1-C6
          page: 9
          text_layer_sha256: 0932b5c5cfb24d50ef886e7de3fb6d05f0c0543ae8bfb705ffc998096eabcdcf
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Results of database analysis

          A total of 1,967,038 stroke patients were found in the database (1,014,239
          women, 952,799

          men) in the period from 2011 to 2014.'
        anchor_text: 'Results of database analysis

          A total of 1,967,038 stroke patients were found in the database (1,014,239
          women, 952,799

          men) in the period from 2011 to 2014.'
        excluded_fragments: []
        image_sha256: 51c70540bff0e0797ff7ed0a924b45349322e7e8a8c7f27bd89af2c145df8c43
        transcription: 'Results of database analysis

          A total of 1,967,038 stroke patients were found in the database (1,014,239
          women, 952,799 men) in the period from 2011 to 2014.'
      P8-S2-C13:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 2c0b802069cc237e3ab36fcd34c6dc316671c92e44194a26f1b5cf1e6814ec96
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 31a768fea43ab12380ec4151ab036fb6b1eb57a9b51b579e16e0f6442c0ac4ca
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P8-S2-C13
          page: 8
          text_layer_sha256: 31a768fea43ab12380ec4151ab036fb6b1eb57a9b51b579e16e0f6442c0ac4ca
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'These data are all summery data for the

          participating states for a particular year (2011–2014).'
        anchor_text: 'These data are all summery data for the

          participating states for a particular year (2011–2014).'
        excluded_fragments: []
        image_sha256: cffb8ff299651e854496cc5187f987a910584fb07c47450ab69ba1800c5ecbea
        transcription: . These data are all summery data for the participating states
          for a particular year (2011–2014)
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 8
  quote: 'As a proxy for stroke severity, the number of hemiparesis/hemiple-

    gia diagnoses were included (using the ICD-9 code: “342.90 Unsp Hemiplga Unspf
    Side”,

    which is the most commonly used ICD-9 code for hemiplegia/paresis in the database
    and

    which does not bias towards the dominant or nondominant side).'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-26'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
