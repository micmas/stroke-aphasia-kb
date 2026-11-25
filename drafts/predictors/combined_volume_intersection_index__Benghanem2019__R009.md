---
id: combined_volume_intersection_index
name: combined volume and intersection index
kind: predictor
findings:
- id: f1
  target_audit:
    status: needs_source_review
    category: ambiguous_or_composite
    original_target: good_outcome_3m
    reason: A score, generic outcome or composite label does not uniquely identify a behaviour. Check the
      task, subtests and analysis before retargeting.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  outcome_measurement:
    status: needs_source_review
    instruments: []
    note: Outcome instrument/task is not yet verified for this finding. Do not infer it from the predictor
      or a paper-wide test list.
  target: good_outcome_3m
  target_kind: prognosis
  claim: In the subgroup of patients with an Aphasia Rapid Test score at day 7 (ART
    D7) < 11, the combined variable of lesion volume ≥ 50 ml or intersection index
    ≥ 20% had no significant effect on the likelihood of a good outcome at 3 months.
  direction: no_effect
  relationship: correlational
  method: LSM
  sample:
    n: 36
    population: Patients with post-stroke aphasia and ischemic stroke in the left
      middle cerebral artery territory
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
  - Single center study
  - Retrospective database
  - Amount of speech and language therapy was not controlled or reliably monitored
  - Stroke volume in MNI normalized images may have been underestimated due to lack
    of lesion masking during normalization
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Presence of either a lesion volume ≥ 50 ml or a lesion
    overlap with a left temporo-parietal white matter (TPWM) region-of-interest ≥
    20%, measured via DWI at 24-48 hours post-stroke. Analysis performed specifically
    for the subgroup with ART D7 < 11. Additional metadata has not been transcribed;
    review the pending-field flags before approval. PDF image reading (P2-S1-C7, two-model
    agreement, human verification pending): Materials and methods


    Patients


    We enrolled 73 patients admitted to the stroke unit of the Pitié-Salpêtrière Hospital
    who consecutively met the following criteria: (1) ischemic stroke in the left
    middle cerebral artery (MCA) territory, (2) persistent aphasia at day 1 post stroke
    (≥ 1 point in the language items of the NIHSS), (3) age ≥ 18 years, (4) MRI performed
    at 1–2 days post stroke and suitable for spatial normalization, (5) no severe
    white matter lesions (Fazekas score < 3), (6) an available ART score at day 7
    post-stroke and Aphasia Handicap Score (AHS) at 3 months post-stroke Original
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
    - not_transcribed:sample.time_post_onset
    - prior_paper_decisions_reconciliation_pending
    - proposed_concept:good_outcome_3m
  citation: '@Benghanem2019'
  source_passages:
  - section: Original source P4-S1-C13
    page: 4
    quote: "In the \nsubgroup of 36 patients with ART D7 < 11, the combined \nvariable\
      \ (volume ≥ 50 ml or intersection index ≥ 20%) had \nno significant effect on\
      \ outcome (p = 0.19)."
    supports: claim
  - section: Original source P4-S2-C1
    page: 4
    quote: no significant effect on outcome (p = 0.19).
    supports: claim
  - section: Original source P2-S1-C7
    page: 2
    quote: "Materials and methods\nPatients\nWe enrolled 73 patients admitted to the\
      \ stroke unit of the \nPitié-Salpêtrière Hospital who consecutively met the\
      \ follow-\ning criteria: (1) ischemic stroke in the left middle cerebral \n\
      artery (MCA) territory, (2) persistent aphasia at day 1 post \nstroke (≥ 1 point\
      \ in the language items of the NIHSS), (3) \nage ≥ 18 years, (4) MRI performed\
      \ at 1–2 days post stroke \nand suitable for spatial normalization, (5) no severe\
      \ white \nmatter lesions (Fazekas score < 3), (6) an available ART \nscore at\
      \ day 7 post-stroke and Aphasia Handicap Score \n(AHS) at 3 months post-stroke."
    supports: sample
  - section: Original source P3-S1-C4
    page: 3
    quote: "The next step consisted in calculating the percent overlap \nof each subject’s\
      \ lesion with a TPWM region-of-interest as \ndefined in Ref. [18]."
    supports: method
  - section: Original source P3-S1-C8
    page: 3
    quote: "We then \ncomputed the intersection index given as the proportion of \n\
      the TPWM critical area damaged by the infarct (Fig. 1)."
    supports: method
  - section: Original source P4-S1-C2
    page: 4
    quote: "We further tested the univariate predictive value of a \ncombined variable,\
      \ which represents the presence of either \na large volume or either the damage\
      \ to a critical area: vol-\nume ≥ 50 ml or intersection index ≥ 20%."
    supports: method
  - section: Original source P1-S1-C4
    page: 1
    quote: Good outcome at 3-months was defined by an Aphasia Handicap Score of 0–2.
    supports: method
  - section: Original source P6-S1-C7
    page: 6
    quote: "Limitations\nFirst, this is a single center study based on data acquired\
      \ \nduring routine care."
    supports: limitation
  - section: Original source P6-S1-C12
    page: 6
    quote: "We did not control (nor reliably monitor) the \namount of Speech and Language\
      \ Therapy, which, neverthe-\nless, is systematically given to our patients at\
      \ least twice a \nweek."
    supports: limitation
  - section: Original source P6-S2-C5
    page: 6
    quote: "Finally, we may have underestimated the \nstroke volume in the MNI normalised\
      \ images since we did \nnot use lesion masking in the process."
    supports: limitation
predictor_type: imaging_metric
short_definition: Presence of either a lesion volume ≥ 50 ml or a lesion overlap with
  a left temporo-parietal white matter (TPWM) region-of-interest ≥ 20%, measured via
  DWI at 24-48 hours post-stroke.
assessment:
- DWI
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-20'
relationship_review:
  paper: Benghanem2019
  proposal_id: R009
  review_status_sha256: e353159479a583847af15f961106a03996c3f71665773b600efeca23cd9501f2
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: de74f7cd268421bddcb9fb6c0342ce9097101bb93fa6984b50ad91bc1fcc285b
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: de74f7cd268421bddcb9fb6c0342ce9097101bb93fa6984b50ad91bc1fcc285b
        A/passages.json: b71245a24c9f1c02e0c9feb799f00ef3082fffc17e57ea392299b7c90a508fcb
        A/raw.json: cf235ab5c745f708aed9f66fd5c96c3cb303c8b78eabecaa3c9b607dc6555f80
        A/source-units.json: 1967709bd71511fd265895a5c40d37dcf8ffd0bc2ac779fa75845640e72dd8a6
        A/full-source-units.json: d917e12bb9b105fb0b2f541ca464919cdba9654d9f9af35a04dbfec931aa2e8c
        A/meta.json: 454e5609a7de6d88f930eef35703f52d56cad9804bc30e4a6921e7bac1414acb
        A/table-images/TABLE-1-page-3-1.png: 8a1b0de4f0e20df10b12b6456daf3f182d97bea48eda576b3df131e7eb01278f
        A/table-images/page-3.png: 824a4dd1feee4b7b0ac4829a865f7168416cedf1cb6614829003d18d8c40cfbd
        A/table-images/page-4.png: 0ed9d3ea55332b45d090a0445a1b255b1aa532989561d39f797ddf967433afc4
        A/table-images/manifest.json: e60244d1b14fcec7be06d0ede31f6acb3057dd00bac14b837a879524c46aa053
        A/table-images/TABLE-2-page-4-1.png: 2175e472614749a47306dafb79b2136ec656b32c799d6d00b288154ee4357ef7
        A/clauses/window-03/raw.json: 05dcf1cc780c186ce67660af0e8d4131f8c862744480d543c18525477b840d52
        A/clauses/window-03/prompt.txt: 941bd2f0e25d68766196b1a4fc732b3c1a92d3a230dc4ee21a639cab0a2260c8
        A/clauses/window-03/meta.json: 00a4bb5397101b9945906a6ceb7209a5ce4e0ba5ca9e2b82907bc672edb4b3df
        A/clauses/window-04/raw.json: 4b4460eb1086ba56187df4c8654e36c3499c1be078d21a1fe4f901e2f9a58581
        A/clauses/window-04/prompt.txt: e9b772a18405ceb86c152a57c6b8db50b4028f60d13571b0a1c2b3e402c54fad
        A/clauses/window-04/meta.json: ea1691265535c48399d08d7bac569d7b420bad395fa543840ec5efa44314a403
        A/clauses/window-05/raw.json: 42c1d93c3e9355cdc097a2a8d63d718db6acd99f01972c7ec2f0866ecebff370
        A/clauses/window-05/prompt.txt: 808d554ab19695e89d25b3f5bb54b5e838da18985e455ceadaefe02e1348e8b3
        A/clauses/window-05/meta.json: 9b2107458f017343889f23257ffe882ec8cb5ba959fb174eba42d5a36e72302b
        A/clauses/window-02/raw.json: 0840e652a06fe2208b2dea93c22afd65a41119db2adcb574e6168fc7cd1126e9
        A/clauses/window-02/prompt.txt: c2cd1cd07ab1fd0f3ded1603b7a6258f8fabab2d84366b162578b44693577e15
        A/clauses/window-02/meta.json: 4bd698f4b8dfb1563da04473bba1f4979c5ce1f150f0eeae41cb22e9ba0f5052
        A/clauses/window-01/raw.json: 2d41ca25b6e824f2481d2cfce9b7a4d54a752da578ece32dfd56a8763d7712b4
        A/clauses/window-01/prompt.txt: 177f91f1bed076049c4286446d33c7334533849459f2897ec6d46b2e1ce711c4
        A/clauses/window-01/meta.json: a4a2e50a2802ad5837b8a21da08ea53e8808957cfe3b58573476e3b48261fce6
        A/tables/TABLE-1-page-3-1/raw.json: 8f8d545593daa44290d14d061e2cc498afdbf8ab59017977e37ec9dc2740d47d
        A/tables/TABLE-1-page-3-1/prompt.txt: 6aac8535143d6184519bbbbb3cbf123d722909fe5a1a89f7d6b3992516dfc8af
        A/tables/TABLE-1-page-3-1/meta.json: 29e394fe7ba73d18fb2210864811f9db49f59b5acd03a3ca203ff248783ad40f
        A/tables/TABLE-2-page-4-2/raw.json: ae549870db42a818fc5d596e8b546f04e1b81a67a56ddf9b1da7f4674eec9f83
        A/tables/TABLE-2-page-4-2/prompt.txt: ddc640f48c414c645a43bc35ad1c69a9845c5fa8b3ba51717fcf8ddec1b3ed69
        A/tables/TABLE-2-page-4-2/meta.json: b340dcb6293267994e0a3e5a5bd2b7ace5021f12ce5233191b9259aa77f302f0
        B/passages.json: b71245a24c9f1c02e0c9feb799f00ef3082fffc17e57ea392299b7c90a508fcb
        B/raw.json: eef94861e234b4cf95f0ebaec55626990680bb898911067c3aa804fa58a67ae7
        B/source-units.json: 1967709bd71511fd265895a5c40d37dcf8ffd0bc2ac779fa75845640e72dd8a6
        B/full-source-units.json: d917e12bb9b105fb0b2f541ca464919cdba9654d9f9af35a04dbfec931aa2e8c
        B/meta.json: dcca5afb19406ffc895ab5d0c3b1a67ff8c4ef3a2326a7c69846b00850b6fcf2
        B/table-images/TABLE-1-page-3-1.png: 8a1b0de4f0e20df10b12b6456daf3f182d97bea48eda576b3df131e7eb01278f
        B/table-images/page-3.png: 824a4dd1feee4b7b0ac4829a865f7168416cedf1cb6614829003d18d8c40cfbd
        B/table-images/page-4.png: 0ed9d3ea55332b45d090a0445a1b255b1aa532989561d39f797ddf967433afc4
        B/table-images/manifest.json: bc6b7d9fa87ec0c236da026cb52104803909f782ef28c15312965c3ee32a97bf
        B/table-images/TABLE-2-page-4-1.png: 2175e472614749a47306dafb79b2136ec656b32c799d6d00b288154ee4357ef7
        B/clauses/window-03/raw.json: 91d31416ccebc6f631904b83104172c243e8fda68aea64e0aad1f6218e2de03f
        B/clauses/window-03/prompt.txt: 941bd2f0e25d68766196b1a4fc732b3c1a92d3a230dc4ee21a639cab0a2260c8
        B/clauses/window-03/meta.json: 323675e9d9fe8485fd2bedbfd3650fa3e274fa3f4826e326d19357d2ae74cd02
        B/clauses/window-04/raw.json: 500e22c5badc9eab9e1221ac48524545894c40298a24a021a195ad1c8fad80a6
        B/clauses/window-04/prompt.txt: e9b772a18405ceb86c152a57c6b8db50b4028f60d13571b0a1c2b3e402c54fad
        B/clauses/window-04/meta.json: 6606d45250259fd5036ddc1b141330a6917096d8caa057f8672874f1f15a9d41
        B/clauses/window-05/raw.json: 826d1540ad5c971e805246e53fefbd3d02fe0dab960e74a9651a75f05064cd60
        B/clauses/window-05/prompt.txt: 808d554ab19695e89d25b3f5bb54b5e838da18985e455ceadaefe02e1348e8b3
        B/clauses/window-05/meta.json: 35ca4977dc98c989b92afc2ba2763ce43316b95a6e090c838d4def93d2e20be4
        B/clauses/window-02/raw.json: 1c5e195e54a75c4b8e97ea205de42cd8afefd3e93082768e943eddde7b42e42c
        B/clauses/window-02/prompt.txt: c2cd1cd07ab1fd0f3ded1603b7a6258f8fabab2d84366b162578b44693577e15
        B/clauses/window-02/meta.json: 1061c8feb6d35c0e13d38983da0b4af5e58265e7992e3d12d8ac53a27bb6882a
        B/clauses/window-01/raw.json: 1268be5e6c07ab1c5655fbac3b3bef33ef06d35dfb8fb1e096fb551917458a87
        B/clauses/window-01/prompt.txt: 177f91f1bed076049c4286446d33c7334533849459f2897ec6d46b2e1ce711c4
        B/clauses/window-01/meta.json: ab04f9663c84ac16f70fb15fd023f6020a76f82fd91972cc8fa50e8df18573fb
        B/tables/TABLE-1-page-3-1/raw.json: 448e1448819f2b9be22b31a8e2bc1ac1117a0c6b9cad36a73ff8b20e6d6f4a68
        B/tables/TABLE-1-page-3-1/prompt.txt: 6aac8535143d6184519bbbbb3cbf123d722909fe5a1a89f7d6b3992516dfc8af
        B/tables/TABLE-1-page-3-1/meta.json: 8cfebd61cd6ce7d849e55d8a25dabace13ea57988e836f5d3bba24a7b9c9e60f
        B/tables/TABLE-2-page-4-2/raw.json: 68653dd819da1d925c11ab7b1de8ef00ee400b07044ffaa26b9ccc08dac61655
        B/tables/TABLE-2-page-4-2/prompt.txt: ddc640f48c414c645a43bc35ad1c69a9845c5fa8b3ba51717fcf8ddec1b3ed69
        B/tables/TABLE-2-page-4-2/meta.json: 4eccc4ccdda99c571a2d7dad59a4fff3ab76cdcf74cb8e9d56c69e4fb74cdddb
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
      pdf_sha256: de74f7cd268421bddcb9fb6c0342ce9097101bb93fa6984b50ad91bc1fcc285b
      source_review: _compare/relationships-2026-11-16/review-current/Benghanem2019
      source_status_sha256: b09957a54eac66744165c396d3325c8498f3082893551c878aad8fdac6227d32
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R009
    exposure:
      text: combined variable (volume ≥ 50 ml or intersection index ≥ 20%)
    outcome:
      text: good outcome at 3 months (AHS 0–2)
    analysis_label: Subgroup analysis (ART D7 < 11)
    relation: sensitivity
    evidence_ids:
    - P4-S1-C13
    - P4-S2-C1
    qualifier_ids:
    - P4-S2-C1
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: de74f7cd268421bddcb9fb6c0342ce9097101bb93fa6984b50ad91bc1fcc285b
      source_review: _compare/relationships-2026-11-16/review-current/Benghanem2019
      source_status_sha256: b09957a54eac66744165c396d3325c8498f3082893551c878aad8fdac6227d32
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P1-S1-C10
      - Result passage disposed without unit P3-S2-C6
      - Result passage disposed without unit P3-S2-C7
      - Result passage disposed without unit P3-S2-C8
      - Result passage disposed without unit P4-S1-C11
      - Result passage disposed without unit P4-S1-C3
      - Result passage disposed without unit P5-S1-C15
      - Result passage disposed without unit P5-S1-C4
      unattached_null_or_qualifier_ids:
      - P1-S1-C10
      suppressed_nonrepresented_units: 9
      default_disposition_count_requires_completeness_check: 100
      unselected_timing_passages:
      - P1-S1-C3
      - P2-S1-C8
      - P2-S1-C9
      - P6-S1-C8
      - P6-S2-C4
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P1-S1-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S1-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S2-C12
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: tested_personal_effects
        source_id: P3-S1-C10
        reason: No current-result classification; a covariate description is not an
          individual test
      empty_frame_slots_require_confirmation:
      - tested_personal_effects
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-3-1
      - TABLE-2-page-4-2
      unlinked_tables:
      - TABLE-2-page-4-2
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P1-S2
        - P3-S1
        - P3-S2
        - P4-S1
        - P4-S2
        - P5-S2
        - P5-S3
        - P6-S1
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: de74f7cd268421bddcb9fb6c0342ce9097101bb93fa6984b50ad91bc1fcc285b
      source_review: _compare/relationships-2026-11-16/review-current/Benghanem2019
      source_status_sha256: b09957a54eac66744165c396d3325c8498f3082893551c878aad8fdac6227d32
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C8
      disposition: represented
      result_indexes:
      - 0
      - 1
      - 2
      reason: States ART D7, infarct volume, and intersection index as univariate
        predictors.
    - source_id: P1-S1-C9
      disposition: represented
      result_indexes:
      - 6
      reason: Provides classification accuracy for the multivariate model.
    - source_id: P1-S1-C10
      disposition: represented
      result_indexes:
      - 8
      reason: States significance of the interaction term.
    - source_id: P1-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Conclusion restating findings.
    - source_id: P3-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive of infarct location map.
    - source_id: P3-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive of affected brain areas.
    - source_id: P3-S2-C8
      disposition: represented
      result_indexes:
      - 0
      - 1
      - 2
      reason: Confirms univariate predictors.
    - source_id: P3-S2-C9
      disposition: represented
      result_indexes:
      - 3
      reason: States non-significance of gender, age, and thrombolysis.
    - source_id: P3-S2-C10
      disposition: represented
      result_indexes:
      - 0
      reason: Provides variance and accuracy for ART D7.
    - source_id: P3-S2-C11
      disposition: represented
      result_indexes:
      - 1
      reason: Provides variance and accuracy for infarct volume.
    - source_id: P3-S2-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Table 1 baseline characteristics.
    - source_id: P4-S1-C1
      disposition: represented
      result_indexes:
      - 2
      reason: Provides variance and accuracy for intersection index.
    - source_id: P4-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient count for combined variable profile.
    - source_id: P4-S1-C4
      disposition: represented
      result_indexes:
      - 4
      reason: Provides accuracy for combined variable.
    - source_id: P4-S1-C5
      disposition: represented
      result_indexes:
      - 4
      reason: Provides OR for combined variable.
    - source_id: P4-S1-C7
      disposition: represented
      result_indexes:
      - 7
      reason: Provides ORs for multivariate predictors.
    - source_id: P4-S1-C8
      disposition: represented
      result_indexes:
      - 6
      reason: Provides accuracy and variance for multivariate model.
    - source_id: P4-S1-C10
      disposition: represented
      result_indexes:
      - 8
      reason: Provides OR and p-value for interaction term.
    - source_id: P4-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of Figure 3.
    - source_id: P4-S1-C13
      disposition: represented
      result_indexes:
      - 9
      reason: Identifies subgroup for ART D7 < 11.
    - source_id: P4-S2-C2
      disposition: represented
      result_indexes:
      - 10
      reason: Provides p-value and outcome percentages for ART D7 >= 11 subgroup.
    - source_id: P5-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement about supplementary analysis results.
    - source_id: P5-S1-C8
      disposition: represented
      result_indexes:
      - 0
      reason: Restates ART D7 variance and accuracy.
    - source_id: P5-S1-C13
      disposition: represented
      result_indexes:
      - 1
      - 2
      reason: Confirms volume and intersection index as univariate predictors.
    - source_id: P5-S1-C15
      disposition: background_or_descriptive
      result_indexes: []
      reason: Cut-off value for volume.
    - source_id: P5-S2-C9
      disposition: represented
      result_indexes:
      - 2
      reason: Confirms intersection index as univariate predictor with cut-off.
    - source_id: P5-S2-C10
      disposition: represented
      result_indexes:
      - 1
      - 2
      reason: Compares variance explained by volume and intersection index.
    - source_id: P5-S2-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Variance explained by combined variable.
    - source_id: P5-S2-C12
      disposition: represented
      result_indexes:
      - 6
      reason: Restates multivariate model accuracy.
    - source_id: P6-S1-C2
      disposition: represented
      result_indexes:
      - 8
      reason: Restates significance of interaction.
    - source_id: P6-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Conclusion restating ART as predictor.
    - source_id: P6-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Conclusion restating imaging impact.
    - source_id: P6-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement on unexplained variance.
    unresolved_coverage:
    - source_id: P4-S2-C2
      disposition: unresolved
      reason: Unknown result index; not accepted as coverage
    - source_id: P6-S1-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P6-S1-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C11
    - P3-S2-C6
    - P3-S2-C7
    - P3-S2-C12
    - P4-S1-C3
    - P4-S1-C11
    - P5-S1-C4
    - P5-S1-C15
    - P5-S2-C10
    - P5-S2-C11
    - P6-S1-C3
    - P6-S1-C4
    - P6-S2-C6
    - P6-S2-C7
    - P6-S2-C9
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-3-1
    - TABLE-2-page-4-2
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P2-S1-C7
      recruited_sample:
      - P2-S1-C7
      - P2-S1-C8
      eligibility:
      - P2-S1-C7
      imaging_provenance:
      - P3-S1-C4
      - P3-S1-C5
      imaging_timing:
      - P2-S1-C7
      - P3-S1-C5
      - P5-S1-C13
      outcome_timing:
      - P1-S1-C2
      - P2-S1-C6
      - P2-S1-C7
      - P2-S2-C13
      - P3-S1-C10
      - P3-S1-C12
      - P5-S1-C7
      - P5-S1-C13
      outcome_definition:
      - P1-S1-C4
      - P2-S3-C3
      - P5-S1-C1
      validation:
      - P5-S1-C8
      - P6-S2-C3
      analysis_restrictions:
      - P6-S2-C3
      dependent_variable_statement:
      - P1-S1-C7
      - P3-S1-C10
      - P3-S1-C12
      - P4-S1-C6
      limitations:
      - P6-S1-C7
      - P6-S1-C8
      - P6-S1-C10
      - P6-S1-C12
      - P6-S1-C13
      - P6-S2-C2
      - P6-S2-C3
      - P6-S2-C5
      personal_factors:
      - P3-S1-C10
      tested_personal_effects: []
      adjustment_roles:
      - P3-S1-C10
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P3-S1-C10
    outcome_type: status_at_assessment
    imaging_vs_outcome: precedes_outcome
    validation_type: internal_cross_validation
    held_selections:
    - slot: dependent_variable_statement
      source_id: P1-S1-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S1-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S2-C12
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: tested_personal_effects
      source_id: P3-S1-C10
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
      pdf_sha256: de74f7cd268421bddcb9fb6c0342ce9097101bb93fa6984b50ad91bc1fcc285b
      review_sha256: e353159479a583847af15f961106a03996c3f71665773b600efeca23cd9501f2
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
      - P4-S1-C13
      - P4-S2-C1
      source_result: In the subgroup of 36 patients with ART D7 < 11, the combined
        variable (volume ≥ 50 ml or intersection index ≥ 20%) had no significant effect
        on outcome (p = 0.19).
      result_status: not_detected
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis is the subgroup analysis for patients with
            ART D7 < 11, testing the combined variable against good outcome. This
            matches the source passages P4-S1-C13 and P4-S2-C1.
          source_ids:
          - P4-S1-C13
          - P4-S2-C1
        direction:
          answer: fits
          reason: The source explicitly states 'no significant effect' with p=0.19.
            The draft correctly identifies this as a null result (no_effect) for this
            specific subgroup, distinguishing it from the significant effect found
            in the ART D7 >= 11 subgroup.
          source_ids:
          - P4-S1-C13
          - P4-S2-C1
        construct:
          answer: fits
          reason: The exposure is correctly defined as the combined variable (volume
            >= 50 ml OR intersection index >= 20%). The outcome is good outcome at
            3 months (AHS 0-2). The patient measurement is template_lesion_overlap,
            as the intersection index is derived from overlaying patient lesions on
            a reference TPWM ROI, not from patient-specific diffusion tractography.
          source_ids:
          - P4-S1-C2
          - P3-S1-C4
          - P3-S1-C8
          - P1-S1-C4
        qualifications:
          answer: fits
          reason: The draft correctly includes the qualification that this result
            applies specifically to the subgroup with ART D7 < 11. It does not incorrectly
            generalize this null finding to the whole cohort or the other subgroup.
          source_ids:
          - P4-S1-C13
          - P4-S2-C1
        missing_material_caveat:
          answer: fits
          reason: The draft includes relevant limitations such as single-center design,
            retrospective nature, and lack of control for speech therapy. No material
            caveats that would change the interpretation of this specific null result
            are omitted.
          source_ids:
          - P6-S1-C7
          - P6-S1-C12
          - P6-S2-C5
      optional_pending:
      - sample.time_post_onset
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
    normalizations:
    - field: sample.time_post_onset
      original: Imaging at 24-48 hours post-stroke; initial severity at day 7; outcome
        at 3 months post-stroke
      action: not_transcribed
      reason: 'Numbers not grounded in usable selected source readings: 24, 48'
    analysis_identity:
      id: R009
      exposure:
        text: combined variable (volume ≥ 50 ml or intersection index ≥ 20%)
      outcome:
        text: good outcome at 3 months (AHS 0–2)
      analysis_label: Subgroup analysis (ART D7 < 11)
      relation: sensitivity
      evidence_ids:
      - P4-S1-C13
      - P4-S2-C1
      qualifier_ids:
      - P4-S2-C1
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: de74f7cd268421bddcb9fb6c0342ce9097101bb93fa6984b50ad91bc1fcc285b
        source_review: _compare/relationships-2026-11-16/review-current/Benghanem2019
        source_status_sha256: b09957a54eac66744165c396d3325c8498f3082893551c878aad8fdac6227d32
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P2-S1-C7:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: de74f7cd268421bddcb9fb6c0342ce9097101bb93fa6984b50ad91bc1fcc285b
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 5584a12a7c5eb1b277755471410d9cf65ea8326eaf281d593a7425c9eb4e2264
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S1-C7
          page: 2
          text_layer_sha256: 5584a12a7c5eb1b277755471410d9cf65ea8326eaf281d593a7425c9eb4e2264
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "Materials and methods\nPatients\nWe enrolled 73 patients admitted\
          \ to the stroke unit of the \nPitié-Salpêtrière Hospital who consecutively\
          \ met the follow-\ning criteria: (1) ischemic stroke in the left middle\
          \ cerebral \nartery (MCA) territory, (2) persistent aphasia at day 1 post\
          \ \nstroke (≥ 1 point in the language items of the NIHSS), (3) \nage ≥ 18\
          \ years, (4) MRI performed at 1–2 days post stroke \nand suitable for spatial\
          \ normalization, (5) no severe white \nmatter lesions (Fazekas score < 3),\
          \ (6) an available ART \nscore at day 7 post-stroke and Aphasia Handicap\
          \ Score \n(AHS) at 3 months post-stroke."
        anchor_text: "Materials and methods\nPatients\nWe enrolled 73 patients admitted\
          \ to the stroke unit of the \nPitié-Salpêtrière Hospital who consecutively\
          \ met the follow-\ning criteria: (1) ischemic stroke in the left middle\
          \ cerebral \nartery (MCA) territory, (2) persistent aphasia at day 1 post\
          \ \nstroke (≥ 1 point in the language items of the NIHSS), (3) \nage ≥ 18\
          \ years, (4) MRI performed at 1–2 days post stroke \nand suitable for spatial\
          \ normalization, (5) no severe white \nmatter lesions (Fazekas score < 3),\
          \ (6) an available ART \nscore at day 7 post-stroke and Aphasia Handicap\
          \ Score \n(AHS) at 3 months post-stroke."
        excluded_fragments: []
        image_sha256: c7278536d339286750fcf08224e25cb0c5d38f407cf51b3cb05cd9f7348e8b36
        transcription: 'Materials and methods


          Patients


          We enrolled 73 patients admitted to the stroke unit of the Pitié-Salpêtrière
          Hospital who consecutively met the following criteria: (1) ischemic stroke
          in the left middle cerebral artery (MCA) territory, (2) persistent aphasia
          at day 1 post stroke (≥ 1 point in the language items of the NIHSS), (3)
          age ≥ 18 years, (4) MRI performed at 1–2 days post stroke and suitable for
          spatial normalization, (5) no severe white matter lesions (Fazekas score
          < 3), (6) an available ART score at day 7 post-stroke and Aphasia Handicap
          Score (AHS) at 3 months post-stroke'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 4
  quote: "In the \nsubgroup of 36 patients with ART D7 < 11, the combined \nvariable\
    \ (volume ≥ 50 ml or intersection index ≥ 20%) had \nno significant effect on\
    \ outcome (p = 0.19)."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-20'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
