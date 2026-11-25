---
id: left_precentral_gyrus_posterior_wall
name: left precentral gyrus (posterior wall) cluster
kind: network
findings:
- id: f1
  target_audit:
    status: behaviour_label_present
    category: behaviour_or_language_construct
    original_target: apraxia_of_speech
    reason: Label names a behaviour or language construct; its exact operational definition and measurement
      still need source review.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  outcome_measurement:
    status: needs_source_review
    instruments: []
    note: Outcome instrument/task is not yet verified for this finding. Do not infer it from the predictor
      or a paper-wide test list.
  target: apraxia_of_speech
  target_kind: impairment
  claim: The posterior wall of the left precentral gyrus predicted the presence of
    apraxia of speech in the comparison between patients with pure AOS and those without
    AOS.
  direction: likely
  relationship: correlational
  method: VLSM
  sample:
    n: 136
    population: Right-handed patients with first-ever acute ischemic stroke and isolated
      nonlacunar infarcts in the left middle cerebral artery territory
    phase: not_reported
    time_post_onset: Median interval between stroke onset and neuropsychological evaluation
      was 7 days; MRI acquisition occurred 3 days from evaluation and 9 days from
      onset.
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Assessment of motor speech abilities was qualitative
  - Inter-rater reliability for speech assessment was not examined
  - Potential underestimation of dysfunctional area as T2WI/FLAIR were used instead
    of diffusion-weighted imaging for spatial extent
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Patient lesion overlap with the posterior wall of
    the left precentral gyrus, measured via T2-weighted or FLAIR MRI images. Finding
    specifically noted in the comparison between pure AOS (AOS without aphasia) and
    non-AOS groups. Additional metadata has not been transcribed; review the pending-field
    flags before approval. PDF image reading (P2-S1-C12, two-model agreement, human
    verification pending): . In total, 136 patients (70.5±12.9 years old,

    79 males) were included Original text-layer quotation is preserved below. PDF
    image reading (P2-S1-C9, two-model agreement, human verification pending): . The
    severity of neurological deficits

    was evaluated using the National Institutes of Health Stroke Scale

    (NIHSS) score on admission.24 The inclusion criteria for this study

    were as follows: (1) first-ever stroke onset, (2) isolated nonlacunar

    infarcts in the left middle cerebral artery territory verified on MRI, (3)

    right handed, (4) no previous history of dementia, and (5) neuropsy-

    chological evaluation by speech-language pathologists during his/her

    hospital stay Original text-layer quotation is preserved below. PDF image reading
    (P2-S3-C2, two-model agreement, human verification pending): . The median interval
    between stroke onset and neuropsycho-

    logical evaluation was 7 days (5–10) Original text-layer quotation is preserved
    below. PDF image reading (P2-S3-C4, two-model agreement, human verification pending):
    . The intervals between neuropsychological evaluation and

    MRI acquisition and between onset and MRI acquisition were 3 days

    (1–6.75) and 9 days (7–12.75), respectively Original text-layer quotation is preserved
    below.'
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
    - proposed_concept:apraxia_of_speech
  citation: '@Itabashi2015'
  source_passages:
  - section: Original source P4-S1-C1
    page: 4
    quote: "\n34    Stroke    January 2016\nSimilarly, the posterior wall of the left\
      \ precentral gyrus pre-\ndicted the presence of AOS in the comparison between\
      \ pure \nAOS and non-AOS (Z≥2.995, Figure  2B)."
    supports: claim
  - section: Original source P2-S1-C12
    page: 2
    quote: "In total, 136 patients (70.5±12.9 years old, \n79 males) were included."
    supports: sample
  - section: Original source P2-S1-C9
    page: 2
    quote: "The severity of neurological deficits \nwas evaluated using the National\
      \ Institutes of Health Stroke Scale \n(NIHSS) score on admission.24 The inclusion\
      \ criteria for this study \nwere as follows: (1) first-ever stroke onset, (2)\
      \ isolated nonlacunar \ninfarcts in the left middle cerebral artery territory\
      \ verified on MRI, (3) \nright handed, (4) no previous history of dementia,\
      \ and (5) neuropsy-\nchological evaluation by speech-language pathologists during\
      \ his/her \nhospital stay."
    supports: sample
  - section: Original source P2-S3-C2
    page: 2
    quote: 'The median interval between stroke onset and neuropsycho-

      logical evaluation was 7 days (5–10).'
    supports: sample
  - section: Original source P2-S3-C4
    page: 2
    quote: "The intervals between neuropsychological evaluation and \nMRI acquisition\
      \ and between onset and MRI acquisition were 3 days \n(1–6.75) and 9 days (7–12.75),\
      \ respectively."
    supports: sample
  - section: Original source P2-S4-C4
    page: 2
    quote: "Voxel-Based Lesion–Symptom Mapping\nVoxel-based lesion–symptom mapping\
      \ (VLSM) analyses were per-\nformed using nonparametric mapping (http://www.mccauslandcenter.\n\
      sc.edu/mricro/npm/) and MRIcron software.29 Intergroup compari-\nsons were made\
      \ between the following groups: all AOS (pure AOS \nplus AOS-aphasia) and non-AOS,\
      \ pure AOS and non-AOS, AOS-\naphasia and non-AOS, and pure AOS and AOS-aphasia."
    supports: method
  - section: Original source P2-S2-C6
    page: 2
    quote: "Patients who exhibited any speech abnormalities, word \nfinding difficulty,\
      \ or ≥1 errors on the repetition, naming, or buccofa-\ncial praxis underwent\
      \ further assessments with the standard language \ntest of aphasia to determine\
      \ the diagnosis of speech and language \ndisorders.25 The standard language\
      \ test of aphasia is a comprehensive \ntest of language functions for adult\
      \ Japanese speakers and comprises \nsubtests for auditory word and sentence\
      \ comprehension, object nam-\ning, word and sentence repetition, cartoon description,\
      \ verbal fluency, \nreading aloud and comprehension, writing, and calculation."
    supports: method
  - section: Original source P5-S2-C3
    page: 5
    quote: "Second, the assessment of motor speech abilities \nin this study was qualitative,\
      \ and its inter-rater reliability was \nnot examined."
    supports: limitation
  - section: Original source P5-S2-C4
    page: 5
    quote: "Standardized quantitative measures for motor \nspeech abilities should\
      \ be incorporated in future studies.7,23 \nThird, we may have underestimated\
      \ the spatial extent of dys-\nfunction because dysfunctional area often extends\
      \ beyond the \nregions of infarction observed on T2WI or FLAIR in patients \n\
      with acute stroke.18 Diffusion-weighted image would be supe-\nrior for detecting\
      \ such areas in acute phase."
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-24'
relationship_review:
  paper: Itabashi2015
  proposal_id: R002
  review_status_sha256: a2065e6574d89913d56348de75684048a64463388077cffeb93ee937a3497134
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: f85fa3b99e2f8551290e88cde33808f05df0917784491147108f6d599c058015
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: f85fa3b99e2f8551290e88cde33808f05df0917784491147108f6d599c058015
        A/passages.json: 69f2f38dc98bfecf0fdfeb56d44b304f0f9677321780b76107372d0854ec85a0
        A/raw.json: 96ebb2f2fa336f43cbdb2b540b0a0621223b9ad98e78857e319fa5dbf3d6b3ef
        A/source-units.json: e24a7967fd9226ba8b695e8cd2d968e4a191ed371faf91bac87594fb7c862a46
        A/full-source-units.json: 4197d632b6e6fb3447acce7f08a7d545ec03a09c4dcc4e51ce9004277c4d4b3a
        A/meta.json: ab497dcfcef71505e73220df6a15fbab9d4676d95388154d8f9a365a34f33b91
        A/table-images/manifest.json: 15950fc7df15fdadfa8092aeb2638adbe49767d83156fce70edb4588082e989a
        A/clauses/window-03/raw.json: 69b02cbfecf675fd072888f5f79211dd3a885e2a94afa8792dc4f64fb69a0fb2
        A/clauses/window-03/prompt.txt: d45d08537cf5c15a859b2ea4758653379bb16df7f795c64dca457104b3075bb8
        A/clauses/window-03/meta.json: a11f3272b0a70e0d5987e26f27ee76b84fe90c6547bf8416ad6d37caf237bf82
        A/clauses/window-04/raw.json: 79ed7ecc094eefa8b57f2e1aed7120cd8b593bea56414314bc8340cabe4314b5
        A/clauses/window-04/prompt.txt: fbf3b2c941170219ed7a2855ba9ff5d34ed290314f9dfebe2563664e3bdc50cc
        A/clauses/window-04/meta.json: 6ac60ce0f6531208a2eb6a220a7a653e8b88fe371608cb725775a4dc67bd5a9b
        A/clauses/window-02/raw.json: 1fac83128f2e15db9c4ee6df5861673abea74463b8ec89c143f0be36e5cc0f1f
        A/clauses/window-02/prompt.txt: 9449dfe077aa670f5684d373049e385523d164e30c3443e9b23d59fddb0d3260
        A/clauses/window-02/meta.json: d9ec99e0e365cf5626a378edddee8d9849879b6045c1cad9e2d776db8b73b024
        A/clauses/window-01/raw.json: 0db67174775931c4e778aa546b896ad985e6314547ad7d9a044c377aed59bda0
        A/clauses/window-01/prompt.txt: 9e9d2ca8259ed2530d56908d5b0d664c4e94e9ccd118be1f8d251e1367f01dd1
        A/clauses/window-01/meta.json: f10cad9f8524c39afc724597eeb63f5fca19628fecd170d589cd503e9edb6e0e
        B/passages.json: 69f2f38dc98bfecf0fdfeb56d44b304f0f9677321780b76107372d0854ec85a0
        B/raw.json: f6ca458bc2e6d27bdc067ca67395c20b617f14fa62994fa8dd1a019ca8993ecc
        B/source-units.json: e24a7967fd9226ba8b695e8cd2d968e4a191ed371faf91bac87594fb7c862a46
        B/full-source-units.json: 4197d632b6e6fb3447acce7f08a7d545ec03a09c4dcc4e51ce9004277c4d4b3a
        B/meta.json: 3756d8282d130c72224feba5a93e1c46106ae73b714af803cf23cdadbfc7aa03
        B/table-images/manifest.json: 15950fc7df15fdadfa8092aeb2638adbe49767d83156fce70edb4588082e989a
        B/clauses/window-03/raw.json: a73957ffd970c28e376b1e44be35ab6f575d6395b5a6e7d374f1872e9686ba94
        B/clauses/window-03/prompt.txt: d45d08537cf5c15a859b2ea4758653379bb16df7f795c64dca457104b3075bb8
        B/clauses/window-03/meta.json: 4c54d4df0f9fc5677c440adfa1f5af79c7ff2e9314e3c83ed43b5fba787dd6f7
        B/clauses/window-04/raw.json: f253121ec1b97ab0b741cd1d7a9e075428db510fcb5201a0b4260cbd2a7bb040
        B/clauses/window-04/prompt.txt: fbf3b2c941170219ed7a2855ba9ff5d34ed290314f9dfebe2563664e3bdc50cc
        B/clauses/window-04/meta.json: 7d6e1cf240b9bc2100fb54a6f9285e0d537e744968fc7a71eaa75d5b9e7c6894
        B/clauses/window-02/raw.json: bc10d7f9d5a6d8b917e2f6773cf47721c9f70123f7a7da6cc96142be53e21a5b
        B/clauses/window-02/prompt.txt: 9449dfe077aa670f5684d373049e385523d164e30c3443e9b23d59fddb0d3260
        B/clauses/window-02/meta.json: c983cd428652b3500beb72e6398c0eabf1495488cae281514a55a0dd0632d34f
        B/clauses/window-01/raw.json: 86c19f028193fc368dcdf4dfb0b720213c128e3327487cf77f7d2944ca747696
        B/clauses/window-01/prompt.txt: 9e9d2ca8259ed2530d56908d5b0d664c4e94e9ccd118be1f8d251e1367f01dd1
        B/clauses/window-01/meta.json: f9059251de253e47f21a166f3e9bb3dd00212baa485954137e5871e0fc6c7aab
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
      pdf_sha256: f85fa3b99e2f8551290e88cde33808f05df0917784491147108f6d599c058015
      source_review: _compare/relationships-2026-11-16/review-current/Itabashi2015
      source_status_sha256: d098d9c9b187c6f0425d7c3b93aaeecd5328a5158895f77655f33aa70a8f400a
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R002
    exposure:
      text: left precentral gyrus (posterior wall)
    outcome:
      text: apraxia of speech (AOS)
    analysis_label: VLSM (pure AOS vs non-AOS)
    relation: association
    evidence_ids:
    - P4-S1-C1
    qualifier_ids:
    - P4-S2-C14
    - P4-S2-C15
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: f85fa3b99e2f8551290e88cde33808f05df0917784491147108f6d599c058015
      source_review: _compare/relationships-2026-11-16/review-current/Itabashi2015
      source_status_sha256: d098d9c9b187c6f0425d7c3b93aaeecd5328a5158895f77655f33aa70a8f400a
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P1-S2-C9
      - Result passage disposed without unit P2-S4-C13
      - Accounting without a linked unit P3-S1-C4
      - Accounting without a linked unit P4-S1-C1
      - Accounting without a linked unit P4-S1-C2
      - Unaccounted source passage P4-S1-C1
      - Unaccounted source passage P3-S1-C4
      - Unaccounted source passage P4-S1-C2
      - Result passage disposed without unit P4-S2-C13
      - Result passage disposed without unit P4-S2-C15
      - Result passage disposed without unit P4-S2-C17
      - Result passage disposed without unit P5-S1-C1
      - Result passage disposed without unit P5-S2-C11
      - Accounting without a linked unit P5-S2-C6
      - Unaccounted source passage P5-S2-C6
      - Result passage disposed without unit P5-S2-C13
      unattached_null_or_qualifier_ids: []
      suppressed_nonrepresented_units: 14
      default_disposition_count_requires_completeness_check: 96
      unselected_timing_passages:
      - P1-S2-C5
      - P2-S1-C3
      - P2-S1-C4
      - P2-S1-C12
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P4-S1-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S1-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P2-S4-C5
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      empty_frame_slots_require_confirmation:
      - validation
      - personal_factors
      - tested_personal_effects
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
        - P3-S1
        - P4-S1
        - P4-S2
        - P5-S1
        - P5-S2
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: f85fa3b99e2f8551290e88cde33808f05df0917784491147108f6d599c058015
      source_review: _compare/relationships-2026-11-16/review-current/Itabashi2015
      source_status_sha256: d098d9c9b187c6f0425d7c3b93aaeecd5328a5158895f77655f33aa70a8f400a
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes patient counts for diagnosis groups.
    - source_id: P1-S2-C10
      disposition: repeated
      result_indexes:
      - 0
      reason: Abstract summary of the main VLSM result.
    - source_id: P2-S1-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports median NIHSS score of the population.
    - source_id: P2-S4-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports patient counts for diagnosis groups.
    - source_id: P3-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to Figure 1 (overlap maps).
    - source_id: P3-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to Figures 2 and 3 (VLSM results).
    - source_id: P3-S1-C4
      disposition: represented
      result_indexes:
      - 0
      reason: Establishes association for all AOS vs non-AOS.
    - source_id: P4-S1-C1
      disposition: represented
      result_indexes:
      - 1
      reason: Establishes association for pure AOS vs non-AOS.
    - source_id: P4-S1-C2
      disposition: represented
      result_indexes:
      - 2
      reason: Establishes association for AOS-aphasia vs non-AOS.
    - source_id: P4-S1-C3
      disposition: represented
      result_indexes:
      - 3
      reason: Establishes null finding for pure AOS vs AOS-aphasia.
    - source_id: P4-S1-C4
      disposition: represented
      result_indexes:
      - 4
      reason: Establishes association for AOS-aphasia vs pure AOS.
    - source_id: P4-S2-C8
      disposition: repeated
      result_indexes:
      - 1
      reason: Discussion restatement of pure AOS results.
    - source_id: P4-S2-C9
      disposition: repeated
      result_indexes:
      - 1
      reason: Discussion restatement of pure AOS results.
    - source_id: P4-S2-C13
      disposition: represented
      result_indexes:
      - 0
      reason: Provides Z-score threshold for all AOS vs non-AOS.
    - source_id: P4-S2-C15
      disposition: represented
      result_indexes:
      - 1
      reason: Provides Z-score threshold for pure AOS vs non-AOS.
    - source_id: P4-S2-C17
      disposition: represented
      result_indexes:
      - 2
      reason: Provides Z-score threshold for AOS-aphasia vs non-AOS.
    - source_id: P5-S1-C1
      disposition: repeated
      result_indexes:
      - 1
      - 2
      reason: Discussion restatement of pure AOS and AOS-aphasia results.
    - source_id: P5-S2-C6
      disposition: repeated
      result_indexes:
      - 0
      reason: Conclusion restatement of main finding.
    - source_id: P5-S2-C11
      disposition: represented
      result_indexes:
      - 3
      reason: Provides Z-score threshold for pure AOS vs AOS-aphasia.
    - source_id: P5-S2-C13
      disposition: represented
      result_indexes:
      - 4
      reason: Provides Z-score threshold for AOS-aphasia vs pure AOS.
    unresolved_coverage: []
    pending_source_ids:
    - P1-S2-C9
    - P1-S2-C10
    - P2-S1-C13
    - P2-S4-C13
    - P3-S1-C2
    - P3-S1-C3
    - P4-S2-C8
    - P4-S2-C9
    - P4-S2-C13
    - P4-S2-C15
    - P4-S2-C17
    - P5-S1-C1
    - P5-S2-C6
    - P5-S2-C11
    - P5-S2-C13
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
      - P2-S1-C12
      recruited_sample:
      - P2-S1-C3
      eligibility:
      - P2-S1-C9
      - P2-S1-C10
      - P2-S1-C11
      imaging_provenance:
      - P2-S3-C8
      - P2-S3-C9
      imaging_timing:
      - P2-S3-C4
      outcome_timing:
      - P2-S3-C2
      outcome_definition:
      - P2-S2-C9
      validation: []
      analysis_restrictions:
      - P2-S4-C5
      - P2-S4-C6
      dependent_variable_statement:
      - P2-S4-C5
      limitations:
      - P5-S2-C2
      - P5-S2-C3
      - P5-S2-C4
      - P5-S2-C5
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P2-S4-C9
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P2-S1-C12
      - P2-S1-C13
      - P3-S1-C6
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P4-S1-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S1-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P2-S4-C5
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
      pdf_sha256: f85fa3b99e2f8551290e88cde33808f05df0917784491147108f6d599c058015
      review_sha256: a2065e6574d89913d56348de75684048a64463388077cffeb93ee937a3497134
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
      - P4-S1-C1
      source_result: In the VLSM comparison between pure AOS and non-AOS, the posterior
        wall of the left precentral gyrus predicted the presence of AOS (Z≥2.995).
      result_status: detected
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The source P4-S1-C1 explicitly describes the VLSM analysis comparing
            pure AOS and non-AOS groups, identifying the posterior wall of the left
            precentral gyrus as the associated region. This matches the selected analysis
            label and evidence.
          source_ids:
          - P4-S1-C1
          - P2-S4-C4
        direction:
          answer: fits
          reason: The source states the region 'predicted the presence of AOS', indicating
            a positive association. The draft's direction 'likely' and claim 'predicted
            the presence' are consistent with this detected association.
          source_ids:
          - P4-S1-C1
        construct:
          answer: fits
          reason: The exposure is correctly identified as the left precentral gyrus
            (posterior wall). The outcome is AOS. The method is VLSM. The patient
            measurement is correctly identified as template_lesion_overlap, as the
            study overlays patient lesions on a standard template (P2-S3-C9) rather
            than using patient-derived diffusion tractography.
          source_ids:
          - P4-S1-C1
          - P2-S3-C9
          - P2-S4-C4
        qualifications:
          answer: fits
          reason: The draft includes the critical qualification that the finding is
            specific to the 'pure AOS vs non-AOS' comparison. This is supported by
            P4-S1-C1 and P4-S2-C9, which distinguish this result from the 'all AOS'
            or 'AOS-aphasia' comparisons.
          source_ids:
          - P4-S1-C1
          - P4-S2-C9
        missing_material_caveat:
          answer: fits
          reason: The draft includes relevant limitations regarding the qualitative
            nature of the assessment and the imaging modality (T2WI/FLAIR vs DWI).
            No material caveats that would change the interpretation of the specific
            VLSM result are omitted.
          source_ids:
          - P5-S2-C3
          - P5-S2-C4
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
        text: left precentral gyrus (posterior wall)
      outcome:
        text: apraxia of speech (AOS)
      analysis_label: VLSM (pure AOS vs non-AOS)
      relation: association
      evidence_ids:
      - P4-S1-C1
      qualifier_ids:
      - P4-S2-C14
      - P4-S2-C15
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: f85fa3b99e2f8551290e88cde33808f05df0917784491147108f6d599c058015
        source_review: _compare/relationships-2026-11-16/review-current/Itabashi2015
        source_status_sha256: d098d9c9b187c6f0425d7c3b93aaeecd5328a5158895f77655f33aa70a8f400a
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P2-S1-C12:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: f85fa3b99e2f8551290e88cde33808f05df0917784491147108f6d599c058015
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 2a7c3a4b1e3d1c6d74eb378ef102e16096464b8d294a990fb2576993ffafd025
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S1-C12
          page: 2
          text_layer_sha256: 2a7c3a4b1e3d1c6d74eb378ef102e16096464b8d294a990fb2576993ffafd025
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "In total, 136 patients (70.5±12.9 years old, \n79 males) were\
          \ included."
        anchor_text: "In total, 136 patients (70.5±12.9 years old, \n79 males) were\
          \ included."
        excluded_fragments: []
        image_sha256: ea0e2eb8fd942f2e4d0b36535ec6c3cdb90bfbf27b3ae0a1083508103a4af64b
        transcription: '. In total, 136 patients (70.5±12.9 years old,

          79 males) were included'
      P2-S1-C9:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: f85fa3b99e2f8551290e88cde33808f05df0917784491147108f6d599c058015
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: ac16055329408ce14bf51689056e57ec3bd17cc7e13527b672d3729276dd2bd6
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S1-C9
          page: 2
          text_layer_sha256: ac16055329408ce14bf51689056e57ec3bd17cc7e13527b672d3729276dd2bd6
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "The severity of neurological deficits \nwas evaluated using\
          \ the National Institutes of Health Stroke Scale \n(NIHSS) score on admission.24\
          \ The inclusion criteria for this study \nwere as follows: (1) first-ever\
          \ stroke onset, (2) isolated nonlacunar \ninfarcts in the left middle cerebral\
          \ artery territory verified on MRI, (3) \nright handed, (4) no previous\
          \ history of dementia, and (5) neuropsy-\nchological evaluation by speech-language\
          \ pathologists during his/her \nhospital stay."
        anchor_text: "The severity of neurological deficits \nwas evaluated using\
          \ the National Institutes of Health Stroke Scale \n(NIHSS) score on admission.24\
          \ The inclusion criteria for this study \nwere as follows: (1) first-ever\
          \ stroke onset, (2) isolated nonlacunar \ninfarcts in the left middle cerebral\
          \ artery territory verified on MRI, (3) \nright handed, (4) no previous\
          \ history of dementia, and (5) neuropsy-\nchological evaluation by speech-language\
          \ pathologists during his/her \nhospital stay."
        excluded_fragments: []
        image_sha256: 46f1815389b476335522f91bf14fe35163153e31d30bc53233563a31fe9f83c4
        transcription: '. The severity of neurological deficits

          was evaluated using the National Institutes of Health Stroke Scale

          (NIHSS) score on admission.24 The inclusion criteria for this study

          were as follows: (1) first-ever stroke onset, (2) isolated nonlacunar

          infarcts in the left middle cerebral artery territory verified on MRI, (3)

          right handed, (4) no previous history of dementia, and (5) neuropsy-

          chological evaluation by speech-language pathologists during his/her

          hospital stay'
      P2-S3-C2:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: f85fa3b99e2f8551290e88cde33808f05df0917784491147108f6d599c058015
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: e5bc880c27ac2c15e054aa9a2b95073459c58fcca7d5a97a510f64b7899306b4
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S3-C2
          page: 2
          text_layer_sha256: e5bc880c27ac2c15e054aa9a2b95073459c58fcca7d5a97a510f64b7899306b4
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'The median interval between stroke onset and neuropsycho-

          logical evaluation was 7 days (5–10).'
        anchor_text: 'The median interval between stroke onset and neuropsycho-

          logical evaluation was 7 days (5–10).'
        excluded_fragments: []
        image_sha256: 5e99b3a338bcbfe083fd46c7f51e54bc8bd28bf91c55a664138cb98bce1301d4
        transcription: '. The median interval between stroke onset and neuropsycho-

          logical evaluation was 7 days (5–10)'
      P2-S3-C4:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: f85fa3b99e2f8551290e88cde33808f05df0917784491147108f6d599c058015
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: b9e3afee2fa47833e954d2a6ba0db9a18e33647deccf0f42576417e33362c4b9
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S3-C4
          page: 2
          text_layer_sha256: b9e3afee2fa47833e954d2a6ba0db9a18e33647deccf0f42576417e33362c4b9
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "The intervals between neuropsychological evaluation and \n\
          MRI acquisition and between onset and MRI acquisition were 3 days \n(1–6.75)\
          \ and 9 days (7–12.75), respectively."
        anchor_text: "The intervals between neuropsychological evaluation and \nMRI\
          \ acquisition and between onset and MRI acquisition were 3 days \n(1–6.75)\
          \ and 9 days (7–12.75), respectively."
        excluded_fragments: []
        image_sha256: 87059b3d32d071a05fbf600a43b1c95a73adf683827bf161d45a15a89a6b06bf
        transcription: '. The intervals between neuropsychological evaluation and

          MRI acquisition and between onset and MRI acquisition were 3 days

          (1–6.75) and 9 days (7–12.75), respectively'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 4
  quote: "\n34    Stroke    January 2016\nSimilarly, the posterior wall of the left\
    \ precentral gyrus pre-\ndicted the presence of AOS in the comparison between\
    \ pure \nAOS and non-AOS (Z≥2.995, Figure  2B)."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-24'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
