---
id: infarct_volume
name: infarct volume
kind: predictor
findings:
- id: f1
  outcome_measurement:
    status: identified
    instruments:
    - name: Aphasia Rapid Test
    metric: Aphasia severity score; scale-specific analyses remain in the claim and source passages
    note: Rosso2015 identifies ART and an additional BDAE global-severity analysis. Final interpretation
      and scoring still require review.
  target_audit:
    status: construct_separated
    category: behaviour_or_language_construct
    original_target: art_score
    reason: Separated aphasia severity from the Aphasia Rapid Test score using the cited paper. Metadata
      correction only.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  target: overall_aphasia_severity
  target_kind: impairment
  claim: The association between infarct volume and aphasia severity was no longer
    significant when the contribution of fractional anisotropy values in the severity-related
    white matter cluster was taken into account.
  direction: no_effect
  relationship: correlational
  method: LSM
  sample:
    n: not_reported
    population: Right-handed chronic poststroke aphasic patients with first-ever stroke
      in the left middle cerebral territory
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
  - Relatively low sample size
  - Heterogeneous timing of assessments since stroke
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Total infarct volumes delineated on FLAIR images by
    manual outlining by a stroke clinician and calculated in MNI space. Measured via
    partial correlation removing the effects of FA values in a specific white matter
    cluster (including posterior arm of internal capsule, posterior portion of external
    capsule, and temporoparietal junction). Additional metadata has not been transcribed;
    review the pending-field flags before approval. PDF image reading (P8-S2-C2, two-model
    agreement, human verification pending): . Also timing of

    assessments/measurements since stroke is heterogeneous in

    this study (ranging from 3 to >40 months), the interquartile

    ranges (25th and 75th percentiles) were between 5 and 20

    months (median = 8 months) Original text-layer quotation is preserved below.'
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
    - not_transcribed:sample.n
    - not_transcribed:sample.time_post_onset
    - proposed_concept:art_score
  citation: '@Rosso2015'
  source_passages:
  - section: Original source P5-S2-C6
    page: 5
    quote: "Conversely, once the possible contribu-\ntion of the FA values on the\
      \ relationship between the infarct \nvolumes and the ART scores was taken into\
      \ account, the \npartial correlation coefficient for infarct volumes was no\
      \ \nlonger significant (partial correlation coefficient = −0.194, \nP = .38),\
      \ These results suggested that infarct volume contri-\nbution was likely a reflection\
      \ of damage to this particular \narea."
    supports: claim
  - section: Original source P2-S2-C5
    page: 2
    quote: "Population\nTwenty-three right-handed patients (14 males, mean ± stan-\n\
      dard deviation [SD] age = 57 ± 19 years, mean ± SD time \npoststroke = 16 ±\
      \ 21 months) participated in the study."
    supports: sample
  - section: Original source P2-S2-C6
    page: 2
    quote: "Patients were recruited retrospectively according to the fol-\nlowing\
      \ criteria: (a) presence of their first ever stroke in the \nleft middle cerebral\
      \ territory, (b) age >18 and < 85 years, \n(c) French native speaker, (d) aphasia\
      \ persistent at day 1 \npoststroke (≥1 point in the language items of the Aphasia\
      \ \nRapid Test [ART]16), (e) no contraindications for MRI, \n(f) no severe white\
      \ matter lesions (Fazekas score <3), and \n(g) right-handedness."
    supports: sample
  - section: Original source P3-S2-C2
    page: 3
    quote: "Anatomical Images Processing\nInfarct lesions were delineated on the FLAIR\
      \ images of \neach patient in the native space by interactive manual out-\n\
      lining using the MRICron software (http://www.cabiatl.\ncom/mricro/mricron).21\
      \ This segmentation was performed \nby an experienced stroke clinician."
    supports: method
  - section: Original source P2-S2-C7
    page: 2
    quote: "Language Evaluation\nThe language evaluation was performed the same day\
      \ as the \nmultimodal MRI."
    supports: method
  - section: Original source P8-S2-C2
    page: 8
    quote: "Also timing of \nassessments/measurements since stroke is heterogeneous\
      \ in \nthis study (ranging from 3 to >40 months), the interquartile \nranges\
      \ (25th and 75th percentiles) were between 5 and 20 \nmonths (median = 8 months)."
    supports: sample
predictor_type: imaging_metric
short_definition: Total infarct volumes delineated on FLAIR images by manual outlining
  by a stroke clinician and calculated in MNI space.
assessment:
- Aphasia Rapid Test
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-25'
relationship_review:
  paper: Rosso2015
  proposal_id: R007
  review_status_sha256: 6266a4ac471f6083bef61bb805a1097f325bb7eb7751d988162c4b242fbef284
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 62f8b17cfd2acfea8d0a9998c0f3e7fbdad6da4927b6313b04debe55c36a3c16
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 62f8b17cfd2acfea8d0a9998c0f3e7fbdad6da4927b6313b04debe55c36a3c16
        A/passages.json: c5526f61ff1f21ef59d0e37a315605da4a5e74de8c77c2930f9c0e66d293b61a
        A/raw.json: a404fc5d41addd4d312d2298aa0fc567e510d817b1ea65f5c30053fe55b97430
        A/source-units.json: 1555b6a1cf96d8250c69e76d8cb84d872b5cb43ae86a3842d4dac9ce94f6e8b8
        A/full-source-units.json: 9ffdb6b75a58f69f1ecd576f75cc73252082ecd163f11269be5586742e886886
        A/meta.json: cedff90f25e8b829aa5a59f37b5c82bb9d0cac460aac406122f2ed5705fcd300
        A/table-images/page-5.png: 3de427d8c496c1ab2a78a441399ba49076b4a0aac2a508d1ea2aadf7c5e7aad8
        A/table-images/page-4.png: 170b61619506a361bbddab0312be17003256489a64c9e366eb0400862d710424
        A/table-images/TABLE-1-page-4-1.png: d8666ac3cc87cdead81e955b78478c07f1cd878733e31988bf18405f78d6c4f1
        A/table-images/manifest.json: 56e19b285d66dab77f268088e8f0b5a35a7675e3e82912a50bcb6a13635e207c
        A/table-images/TABLE-2-page-5-1.png: 14b778644a831f3a60d15c4194da6e15fbb6417ab4b4032f094b4f59b838eba7
        A/clauses/window-03/raw.json: c2259ca951513c4a6a986bfd45f16b30c7de713119ddd5dca037ec413906c9c1
        A/clauses/window-03/prompt.txt: 611e1409b589fae48aa76c80e76d5124100de90b59169986eec7f56bc1e01f7e
        A/clauses/window-03/meta.json: 36d703efbfd0df947ce8acc18c423732ad1e47fa03828ee9c099589bc7d3e86e
        A/clauses/window-04/raw.json: 55291cc998c9d6aea99080b75d31b94b3d9c12a7e559b265c40fa3045edfcf3b
        A/clauses/window-04/prompt.txt: 674d0cc260586407b55bbe827f0639d69e4aefb0572fe5692c782ed5c199e78c
        A/clauses/window-04/meta.json: 0ec93cbf132dbb2fe067de64c8da847def52cbcf724f1b360398188a1cf7d89e
        A/clauses/window-05/raw.json: 8d5647eb9102e43ebf4f6000821724d634ac62705234bf492de1bda57706aad0
        A/clauses/window-05/prompt.txt: 9336733274ee9790fc8e13cf531aa74a41282279eebf7f08a2f8dd0a80a2b11c
        A/clauses/window-05/meta.json: cb2bf4f24935d0aeb6938d0f6e0270e7b2fc70647351df3c52834dbe91726a57
        A/clauses/window-02/raw.json: c370e275e8075cad13ea0e3cf1592eda47ccbd7d8db345a436a2c4fde6dbca04
        A/clauses/window-02/prompt.txt: 7372fa896634957b9e83dea0e8fb126978fdee75e519394ca010be3412be3595
        A/clauses/window-02/meta.json: cfbdb5460ceb16d09c34eed66d891dd1c16204ae7e620c6a099a86fa3545e883
        A/clauses/window-01/raw.json: dbdb2b7d4a574540728044e02979d1f26ffd0e6ba8f9636bb04f6715d621f65e
        A/clauses/window-01/prompt.txt: 297a69cb5a0579ad04649202a4b22b337ae9a7dcc813419cc98e1f73a6beb377
        A/clauses/window-01/meta.json: 818a52955704d9750b79ea039bf0a8938fc1bbc7424d82ca7c5997e2d944e88a
        A/tables/TABLE-2-page-5-2/raw.json: 537db5ca558ec2a49734237c1ecba19ecd151a937b12e8ec8d1235545799facb
        A/tables/TABLE-2-page-5-2/prompt.txt: d6e0eb9addcdb1f4df968c7a1a3d83b84020176b7a28abf2203357912c07f3c6
        A/tables/TABLE-2-page-5-2/meta.json: 748a0cfe6fe5533f621f530f2f01a4e36beb22c9472a666bf766efb25ce83e93
        A/tables/TABLE-1-page-4-1/raw.json: 32dfd6364b5567a1ff63fea22298efde553887442e94fcb055e4d43d4167618e
        A/tables/TABLE-1-page-4-1/prompt.txt: 7d4d939190e15d8e0402c9def3286c7fc7d05b565d3fc0102932f9e7be5a9c3c
        A/tables/TABLE-1-page-4-1/meta.json: bb107a7851e2950593706bf2698e0ccbec102008f1b2493c4b01f3091cf28088
        B/passages.json: c5526f61ff1f21ef59d0e37a315605da4a5e74de8c77c2930f9c0e66d293b61a
        B/raw.json: 5b7f2cd6b8bbfa676553f3d901a7844c80814ec7aca143f4f8f1bc068f2af6d0
        B/source-units.json: 1555b6a1cf96d8250c69e76d8cb84d872b5cb43ae86a3842d4dac9ce94f6e8b8
        B/full-source-units.json: 9ffdb6b75a58f69f1ecd576f75cc73252082ecd163f11269be5586742e886886
        B/meta.json: 4bdaf2153f7144f7d71555e7c2894a1f358473245e763977db2ba96166e08822
        B/table-images/page-5.png: 3de427d8c496c1ab2a78a441399ba49076b4a0aac2a508d1ea2aadf7c5e7aad8
        B/table-images/page-4.png: 170b61619506a361bbddab0312be17003256489a64c9e366eb0400862d710424
        B/table-images/TABLE-1-page-4-1.png: d8666ac3cc87cdead81e955b78478c07f1cd878733e31988bf18405f78d6c4f1
        B/table-images/manifest.json: 6fb38f409da91aa0d8524841abd5b7ebfe1c319362ab4d470c7f7deeb92573e9
        B/table-images/TABLE-2-page-5-1.png: 14b778644a831f3a60d15c4194da6e15fbb6417ab4b4032f094b4f59b838eba7
        B/clauses/window-03/raw.json: 32eb6ea837a03e776fb5d64d1bbfabb00e2c5f2d932a4c7102e5fcfde4752035
        B/clauses/window-03/prompt.txt: 611e1409b589fae48aa76c80e76d5124100de90b59169986eec7f56bc1e01f7e
        B/clauses/window-03/meta.json: 8c84eff757c507e831469c52df8a44c3f373a8d0504c301704cac6821dbf71d0
        B/clauses/window-04/raw.json: ebafff3ad7f2e2478a9706b1ef82f2fb43fa7b7a19e81ba1f6201a10d9bd04bb
        B/clauses/window-04/prompt.txt: 674d0cc260586407b55bbe827f0639d69e4aefb0572fe5692c782ed5c199e78c
        B/clauses/window-04/meta.json: 778df1129b0403c84dea54723cd562cfd9791f891151fcccbd9b75ccaf96c071
        B/clauses/window-05/raw.json: f7a1d99654297e7717c5a3b9375fc5b07a31f8463b5b27c2010abb2d2102814d
        B/clauses/window-05/prompt.txt: 9336733274ee9790fc8e13cf531aa74a41282279eebf7f08a2f8dd0a80a2b11c
        B/clauses/window-05/meta.json: f4d0a91c84a21ce26895b721c3b288016dd3a46d5e7bd859c33b4df6b2a7848d
        B/clauses/window-02/raw.json: cb579649aa9aee680c1974cd445e6f71e820f7e79561b828c5a68fcbc6d5fe35
        B/clauses/window-02/prompt.txt: 7372fa896634957b9e83dea0e8fb126978fdee75e519394ca010be3412be3595
        B/clauses/window-02/meta.json: d6385db60197993d80a59891b5435ada12bfadec1a5c00a76eed1237df079b1a
        B/clauses/window-01/raw.json: 33867cf46f869d2d9964899be395c82a2fa97e7336ff49201bf3fd947e923ed5
        B/clauses/window-01/prompt.txt: 297a69cb5a0579ad04649202a4b22b337ae9a7dcc813419cc98e1f73a6beb377
        B/clauses/window-01/meta.json: 719635927d92394a2b438b657ec79850ebb50ade4633a3319b0935ae5995e7d5
        B/tables/TABLE-2-page-5-2/raw.json: 408be154e1f4e0e217a7a3c2e762fc6cd36831405a3fc789ec260e135ffe067e
        B/tables/TABLE-2-page-5-2/prompt.txt: d6e0eb9addcdb1f4df968c7a1a3d83b84020176b7a28abf2203357912c07f3c6
        B/tables/TABLE-2-page-5-2/meta.json: 01c9403f17a7adb61aa7b1d6962ce7057424e50a09369aefd7cb84b111960d3d
        B/tables/TABLE-1-page-4-1/raw.json: 32dfd6364b5567a1ff63fea22298efde553887442e94fcb055e4d43d4167618e
        B/tables/TABLE-1-page-4-1/prompt.txt: 7d4d939190e15d8e0402c9def3286c7fc7d05b565d3fc0102932f9e7be5a9c3c
        B/tables/TABLE-1-page-4-1/meta.json: 98700eb291688052041b4772ffb5beef49daf6365df5bbea85dee9d9cb6f3055
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
      pdf_sha256: 62f8b17cfd2acfea8d0a9998c0f3e7fbdad6da4927b6313b04debe55c36a3c16
      source_review: _compare/relationships-2026-11-16/review-current/Rosso2015
      source_status_sha256: 1fc035d679e1128045aeb741ee69934eb2628f64a37b6c58d6eb3fde8bd5a270
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R007
    exposure:
      text: infarct volumes
    outcome:
      text: ART scores
    analysis_label: partial correlation
    relation: sensitivity
    evidence_ids:
    - P5-S2-C6
    qualifier_ids:
    - P5-S2-C6
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 62f8b17cfd2acfea8d0a9998c0f3e7fbdad6da4927b6313b04debe55c36a3c16
      source_review: _compare/relationships-2026-11-16/review-current/Rosso2015
      source_status_sha256: 1fc035d679e1128045aeb741ee69934eb2628f64a37b6c58d6eb3fde8bd5a270
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P1-S2-C11
      - Accounting without a linked unit P1-S2-C12
      - Accounting without a linked unit P1-S2-C13
      - Accounting without a linked unit P1-S2-C14
      - Unaccounted source passage P1-S2-C14
      - Unaccounted source passage P1-S2-C12
      - Unaccounted source passage P1-S2-C13
      - Result passage disposed without unit P5-S1-C1
      - Result passage disposed without unit P5-S1-C2
      - Result passage disposed without unit P5-S1-C3
      - Result passage disposed without unit P5-S1-C5
      - Result passage disposed without unit P5-S1-C6
      - Result passage disposed without unit P6-S1-C2
      - Result passage disposed without unit P6-S1-C5
      - Result passage disposed without unit P7-S1-C1
      - Result passage disposed without unit P7-S2-C6
      - Accounting without a linked unit P8-S1-C2
      - Result passage disposed without unit P8-S1-C9
      - Unaccounted source passage P8-S1-C2
      unattached_null_or_qualifier_ids:
      - P3-S2-C5
      - P5-S1-C2
      - P6-S1-C5
      - P8-S1-C2
      suppressed_nonrepresented_units: 5
      default_disposition_count_requires_completeness_check: 109
      unselected_timing_passages:
      - P1-S2-C7
      - P2-S2-C5
      - P2-S2-C6
      - P8-S2-C2
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P5-S1-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S2-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S2-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P3-S1-C9
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      empty_frame_slots_require_confirmation:
      - validation
      - analysis_restrictions
      - personal_factors
      - tested_personal_effects
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-4-1
      - TABLE-2-page-5-2
      unlinked_tables:
      - TABLE-1-page-4-1
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P3-S1
        - P3-S2
        - P5-S1
        - P5-S2
        - P6-S1
        - P7-S2
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 62f8b17cfd2acfea8d0a9998c0f3e7fbdad6da4927b6313b04debe55c36a3c16
      source_review: _compare/relationships-2026-11-16/review-current/Rosso2015
      source_status_sha256: 1fc035d679e1128045aeb741ee69934eb2628f64a37b6c58d6eb3fde8bd5a270
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S2-C11
      disposition: repeated
      result_indexes:
      - 0
      reason: Abstract restatement of voxel-based regression results.
    - source_id: P1-S2-C12
      disposition: repeated
      result_indexes:
      - 2
      reason: Abstract restatement of FA/ART correlation.
    - source_id: P1-S2-C13
      disposition: repeated
      result_indexes:
      - 4
      reason: Abstract restatement of variance comparison.
    - source_id: P1-S2-C14
      disposition: repeated
      result_indexes:
      - 6
      reason: Abstract restatement of partial correlation for infarct volume.
    - source_id: P3-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes healthy subject probability maps used for overlap analysis.
    - source_id: P3-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes a single case of lesion differentiation.
    - source_id: P4-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Section header for results.
    - source_id: P4-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient baseline ART score at day 1.
    - source_id: P4-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient baseline ART score at time of study.
    - source_id: P5-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient distribution of ART scores.
    - source_id: P5-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient aphasia profile distribution.
    - source_id: P5-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of infarct localization probability map.
    - source_id: P5-S1-C4
      disposition: represented
      result_indexes:
      - 0
      reason: Primary result of voxel-based regression for ART.
    - source_id: P5-S1-C5
      disposition: represented
      result_indexes:
      - 0
      reason: Qualifies the critical area as overlapping AF and IFOF.
    - source_id: P5-S1-C6
      disposition: represented
      result_indexes:
      - 0
      reason: Qualifies that the area spared the uncinate fasciculus.
    - source_id: P5-S1-C7
      disposition: represented
      result_indexes:
      - 1
      reason: Result of voxel-based regression for BDAE SS.
    - source_id: P5-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Correlation between the two outcome measures (ART and BDAE SS).
    - source_id: P5-S1-C9
      disposition: repeated
      result_indexes:
      - 2
      reason: Restatement of FA/ART correlation.
    - source_id: P5-S2-C1
      disposition: represented
      result_indexes:
      - 2
      reason: Detailed FA/ART correlation statistics.
    - source_id: P5-S2-C2
      disposition: represented
      result_indexes:
      - 3
      reason: Detailed infarct volume/ART correlation statistics.
    - source_id: P5-S2-C3
      disposition: represented
      result_indexes:
      - 4
      reason: Comparison of variance explained by FA vs infarct volume.
    - source_id: P5-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of partial correlation methodology.
    - source_id: P5-S2-C5
      disposition: represented
      result_indexes:
      - 5
      reason: Partial correlation of FA/ART adjusted for infarct volume.
    - source_id: P5-S2-C6
      disposition: represented
      result_indexes:
      - 6
      reason: Partial correlation of infarct volume/ART adjusted for FA.
    - source_id: P5-S2-C7
      disposition: represented
      result_indexes:
      - 7
      reason: Correlation of Pintersection with ART scores.
    - source_id: P5-S2-C2
      disposition: represented
      result_indexes:
      - 3
      reason: Detailed infarct volume/ART correlation statistics.
    - source_id: P6-S1-C2
      disposition: repeated
      result_indexes:
      - 0
      - 2
      reason: Discussion summary of critical area and its correlation with severity.
    - source_id: P6-S1-C4
      disposition: repeated
      result_indexes:
      - 2
      reason: Discussion restatement of variance explained by FA.
    - source_id: P6-S1-C5
      disposition: repeated
      result_indexes:
      - 5
      reason: Discussion restatement of FA significance after adjusting for volume.
    - source_id: P7-S1-C1
      disposition: repeated
      result_indexes:
      - 5
      - 6
      reason: Discussion restatement of partial correlation results.
    - source_id: P7-S1-C4
      disposition: repeated
      result_indexes:
      - 0
      reason: Discussion restatement of white matter structure association.
    - source_id: P7-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to prior study (Marchina et al) regarding uncinate/extreme
        capsule.
    - source_id: P7-S2-C5
      disposition: represented
      result_indexes:
      - 0
      reason: Finding that uncinate was not a critical location in this cohort.
    - source_id: P7-S2-C6
      disposition: represented
      result_indexes:
      - 0
      reason: Finding that critical area extended into white matter of supramarginalis
        and superior temporal gyri.
    - source_id: P7-S2-C7
      disposition: repeated
      result_indexes:
      - 3
      reason: Discussion restatement of infarct size correlation.
    - source_id: P8-S1-C2
      disposition: repeated
      result_indexes:
      - 6
      reason: Discussion restatement of infarct size non-significance after adjustment.
    - source_id: P8-S1-C9
      disposition: repeated
      result_indexes:
      - 6
      - 7
      reason: Discussion summary of evidence for ischemic damage hypothesis.
    - source_id: P8-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison of infarct probability maps to other studies.
    - source_id: P8-S2-C4
      disposition: repeated
      result_indexes:
      - 2
      reason: Discussion restatement of variance explained.
    - source_id: P8-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation that medial subcallosal pathway was preserved in patients.
    - source_id: P8-S2-C7
      disposition: repeated
      result_indexes:
      - 0
      reason: Conclusion restatement of white matter crossroad association.
    - source_id: P8-S2-C8
      disposition: repeated
      result_indexes:
      - 5
      reason: Conclusion restatement of FA independence from infarct size.
    unresolved_coverage:
    - source_id: P5-S2-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P5-S2-C4
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P5-S2-C2
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    pending_source_ids:
    - P1-S2-C11
    - P1-S2-C12
    - P1-S2-C13
    - P1-S2-C14
    - P3-S1-C9
    - P3-S2-C5
    - P4-S1-C9
    - P4-S2-C2
    - P4-S2-C3
    - P5-S1-C1
    - P5-S1-C2
    - P5-S1-C3
    - P5-S1-C5
    - P5-S1-C6
    - P5-S1-C8
    - P5-S1-C9
    - P6-S1-C2
    - P6-S1-C4
    - P6-S1-C5
    - P7-S1-C1
    - P7-S1-C4
    - P7-S2-C2
    - P7-S2-C5
    - P7-S2-C6
    - P7-S2-C7
    - P8-S1-C2
    - P8-S1-C9
    - P8-S1-C12
    - P8-S2-C4
    - P8-S2-C6
    - P8-S2-C7
    - P8-S2-C8
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-4-1
    - TABLE-2-page-5-2
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P2-S2-C5
      recruited_sample:
      - P2-S2-C6
      eligibility:
      - P2-S2-C6
      imaging_provenance:
      - P3-S1-C9
      imaging_timing:
      - P2-S2-C2
      outcome_timing:
      - P2-S2-C2
      - P4-S2-C3
      outcome_definition:
      - P2-S2-C9
      - P2-S2-C10
      - P2-S3-C2
      - P3-S1-C11
      - P5-S1-C4
      - P5-S1-C9
      - P6-S1-C4
      validation: []
      analysis_restrictions: []
      dependent_variable_statement:
      - P3-S1-C6
      - P4-S1-C2
      - P4-S1-C3
      - P5-S2-C4
      limitations:
      - P8-S1-C6
      - P8-S1-C8
      - P8-S1-C11
      - P8-S2-C2
      - P8-S2-C4
      - P8-S2-C5
      - P8-S2-C6
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P3-S1-C6
      - P4-S1-C2
      - P4-S1-C3
      - P5-S2-C5
      - P5-S2-C6
      - P7-S1-C1
      - P8-S1-C9
      - P8-S2-C3
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P2-S2-C5
      - P4-S2-C6
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P5-S1-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S2-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S2-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P3-S1-C9
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
      pdf_sha256: 62f8b17cfd2acfea8d0a9998c0f3e7fbdad6da4927b6313b04debe55c36a3c16
      review_sha256: 6266a4ac471f6083bef61bb805a1097f325bb7eb7751d988162c4b242fbef284
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
      - P5-S2-C6
      source_result: The partial correlation between infarct volumes and ART scores,
        after removing the effects of FA values in the severity-related white matter
        cluster, was not statistically significant (r = -0.194, P = .38). This indicates
        that the association between infarct volume and aphasia severity was no longer
        significant when the contribution of FA values was taken into account.
      result_status: lost_after_adjustment
      patient_measurement: regional_lesion_load
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis is the partial correlation of infarct volumes
            with ART scores, controlling for FA values. This matches the source description
            in P5-S2-C6 and P4-S1-C3.
          source_ids:
          - P5-S2-C6
          - P4-S1-C3
        direction:
          answer: fits
          reason: The source states the partial correlation coefficient was -0.194
            with P = .38, which is not significant. The draft correctly identifies
            this as a 'no_effect' (no statistically detected association) in the context
            of the adjusted model, consistent with the 'lost_after_adjustment' status.
          source_ids:
          - P5-S2-C6
        construct:
          answer: fits
          reason: The exposure is infarct volume (measured via FLAIR outlining, P3-S2-C2),
            the outcome is ART scores (P2-S2-C9), and the method is partial correlation
            removing FA effects (P5-S2-C6). The patient measurement is regional lesion
            load (infarct volume), not template overlap or patient diffusion.
          source_ids:
          - P3-S2-C2
          - P2-S2-C9
          - P5-S2-C6
        qualifications:
          answer: fits
          reason: The draft includes the critical qualification that the null result
            is conditional on controlling for FA values in the specific white matter
            cluster. It also notes the population and limitations (sample size, timing).
          source_ids:
          - P5-S2-C6
          - P8-S1-C6
          - P8-S2-C2
        missing_material_caveat:
          answer: fits
          reason: The draft captures the main caveats regarding sample size and timing
            heterogeneity. The specific interpretation that infarct volume contribution
            is likely a reflection of damage to the specific area (P5-S2-C6) is implicitly
            supported by the null result in the context of the paper's argument, but
            the core statistical finding is faithfully represented.
          source_ids:
          - P5-S2-C6
          - P8-S1-C6
      optional_pending:
      - Sample size requires source confirmation; it has not been transcribed.
      - 'sample.time_post_onset: source confirmation required; original proposed wording
        remains in the audit.'
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
    - Sample size requires source confirmation; it has not been transcribed.
    - 'sample.time_post_onset: source confirmation required; original proposed wording
      remains in the audit.'
    normalizations:
    - field: sample.n
      original: 23
      action: not_transcribed
      reason: Not supported by selected quotations
    - field: sample.time_post_onset
      original: Chronic stage (mean 16 months poststroke; range 3 to >40 months);
        imaging and language evaluation performed on the same day
      action: not_transcribed
      reason: 'Numbers not grounded in usable selected source readings: 16'
    analysis_identity:
      id: R007
      exposure:
        text: infarct volumes
      outcome:
        text: ART scores
      analysis_label: partial correlation
      relation: sensitivity
      evidence_ids:
      - P5-S2-C6
      qualifier_ids:
      - P5-S2-C6
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 62f8b17cfd2acfea8d0a9998c0f3e7fbdad6da4927b6313b04debe55c36a3c16
        source_review: _compare/relationships-2026-11-16/review-current/Rosso2015
        source_status_sha256: 1fc035d679e1128045aeb741ee69934eb2628f64a37b6c58d6eb3fde8bd5a270
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P2-S2-C5:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 62f8b17cfd2acfea8d0a9998c0f3e7fbdad6da4927b6313b04debe55c36a3c16
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 1860fe58ef6fd4329515f33a3f9669359fcef73a6603a4363bada810730e0556
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S2-C5
          page: 2
          text_layer_sha256: 1860fe58ef6fd4329515f33a3f9669359fcef73a6603a4363bada810730e0556
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: "Population\nTwenty-three right-handed patients (14 males,\
          \ mean ± stan-\ndard deviation [SD] age = 57 ± 19 years, mean ± SD time\
          \ \npoststroke = 16 ± 21 months) participated in the study."
        anchor_text: "Population\nTwenty-three right-handed patients (14 males, mean\
          \ ± stan-\ndard deviation [SD] age = 57 ± 19 years, mean ± SD time \npoststroke\
          \ = 16 ± 21 months) participated in the study."
        excluded_fragments: []
        image_sha256: 21ee018dc4563f73436115f01fa0d6f8944f48b78fd29c73d824293e51fae69e
      P2-S2-C6:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 62f8b17cfd2acfea8d0a9998c0f3e7fbdad6da4927b6313b04debe55c36a3c16
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 7b3afa1eae7e737d3671ced001d4c835c705c8c231a8faa860223aff6a08fb7e
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S2-C6
          page: 2
          text_layer_sha256: 7b3afa1eae7e737d3671ced001d4c835c705c8c231a8faa860223aff6a08fb7e
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: "Patients were recruited retrospectively according to the fol-\n\
          lowing criteria: (a) presence of their first ever stroke in the \nleft middle\
          \ cerebral territory, (b) age >18 and < 85 years, \n(c) French native speaker,\
          \ (d) aphasia persistent at day 1 \npoststroke (≥1 point in the language\
          \ items of the Aphasia \nRapid Test [ART]16), (e) no contraindications for\
          \ MRI, \n(f) no severe white matter lesions (Fazekas score <3), and \n(g)\
          \ right-handedness."
        anchor_text: "Patients were recruited retrospectively according to the fol-\n\
          lowing criteria: (a) presence of their first ever stroke in the \nleft middle\
          \ cerebral territory, (b) age >18 and < 85 years, \n(c) French native speaker,\
          \ (d) aphasia persistent at day 1 \npoststroke (≥1 point in the language\
          \ items of the Aphasia \nRapid Test [ART]16), (e) no contraindications for\
          \ MRI, \n(f) no severe white matter lesions (Fazekas score <3), and \n(g)\
          \ right-handedness."
        excluded_fragments: []
      P8-S2-C2:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 62f8b17cfd2acfea8d0a9998c0f3e7fbdad6da4927b6313b04debe55c36a3c16
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: f967d2d3e39440145fa641ddf5ffc7bf7e696c979345d5192530488d31869bdc
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P8-S2-C2
          page: 8
          text_layer_sha256: f967d2d3e39440145fa641ddf5ffc7bf7e696c979345d5192530488d31869bdc
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "Also timing of \nassessments/measurements since stroke is\
          \ heterogeneous in \nthis study (ranging from 3 to >40 months), the interquartile\
          \ \nranges (25th and 75th percentiles) were between 5 and 20 \nmonths (median\
          \ = 8 months)."
        anchor_text: "Also timing of \nassessments/measurements since stroke is heterogeneous\
          \ in \nthis study (ranging from 3 to >40 months), the interquartile \nranges\
          \ (25th and 75th percentiles) were between 5 and 20 \nmonths (median = 8\
          \ months)."
        excluded_fragments: []
        image_sha256: f1dd5371a2dce6be083816df5e3db5766e7da3941660577026d862f7af3ddb35
        transcription: '. Also timing of

          assessments/measurements since stroke is heterogeneous in

          this study (ranging from 3 to >40 months), the interquartile

          ranges (25th and 75th percentiles) were between 5 and 20

          months (median = 8 months)'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 5
  quote: "Conversely, once the possible contribu-\ntion of the FA values on the relationship\
    \ between the infarct \nvolumes and the ART scores was taken into account, the\
    \ \npartial correlation coefficient for infarct volumes was no \nlonger significant\
    \ (partial correlation coefficient = −0.194, \nP = .38), These results suggested\
    \ that infarct volume contri-\nbution was likely a reflection of damage to this\
    \ particular \narea."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-25'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
