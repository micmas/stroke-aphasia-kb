---
id: wernickes_area_perfusion_delay
name: Wernicke's area perfusion delay
kind: predictor
findings:
- id: f1
  target_audit:
    status: behaviour_label_present
    category: behaviour_or_language_construct
    original_target: word_comprehension_error_rate
    reason: Label names a behaviour or language construct; its exact operational definition and measurement
      still need source review.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  outcome_measurement:
    status: needs_source_review
    instruments: []
    note: Outcome instrument/task is not yet verified for this finding. Do not infer it from the predictor
      or a paper-wide test list.
  target: word_comprehension_error_rate
  target_kind: impairment
  claim: In acute stroke patients without infarct in Wernicke's area, the mean number
    of seconds of delay in time-to-peak concentration of contrast in Wernicke's area
    (relative to the right) is strongly correlated with the rate of errors on a word
    comprehension test.
  direction: likely
  relationship: correlational
  method: LSM
  sample:
    n: 50
    population: Right-handed adults with acute left hemispheric ischemic stroke and
      premorbid English proficiency, specifically those without DWI abnormalities
      in Brodmann's area 22.
    phase: not_reported
    time_post_onset: Within 24 hours of symptom onset or progression; measured concurrently
      with language testing.
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - PWI is susceptible to motion artifacts.
  - PWI is less widely available in acute stroke settings.
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Mean number of seconds of delay in time-to-peak (TTP)
    concentration of contrast in left Brodmann''s area 22 relative to the homologous
    region on the right, measured using perfusion-weighted imaging (PWI) and identified
    via published BA templates. Analysis was restricted to patients without DWI abnormalities
    in BA 22 to avoid luxury perfusion effects. Additional metadata has not been transcribed;
    review the pending-field flags before approval. PDF image reading (P2-S2-C9, two-model
    agreement, human verification pending): . Thus, 50 subjects were

    included in the analysis of lexical–semantic impairment ver-

    sus delay on PWI Original text-layer quotation is preserved below. PDF image reading
    (P2-S2-C5, two-model agreement, human verification pending): . Time after onset
    or worsening of symptoms

    was 0.5 to 24 hours (mean, 10.3 hours; SD, 8.4) Original text-layer quotation
    is preserved below.'
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
    - proposed_concept:word_comprehension_error_rate
  citation: '@Hillis2001'
  source_passages:
  - section: Original source P1-S1-C9
    page: 1
    quote: 'For 50 patients without infarct in Wernicke’s area, we

      found a strong Pearson correlation between the rate of errors on a word comprehension
      test and the mean number of

      seconds of delay in time-to-peak concentration of contrast in Wernicke’s area,
      relative to the homologous region on the

      right.'
    supports: claim
  - section: Original source P3-S2-C2
    page: 3
    quote: 'Results

      A very high correlation (r 5 0.84; p , 0.00001) was

      found between the mean number of seconds delay in

      left BA 22 and the error rate in spoken word/picture

      verification, as illustrated in Figure 1.'
    supports: claim
  - section: Original source P3-S1-C11
    page: 3
    quote: 'To measure relative hypoperfusion in BA 22,

      this region was outlined in each hemisphere, and the Scion

      Image program30 was used to compute mean delay (in sec-

      onds) in TTP in left relative to right BA 22.'
    supports: method
  - section: Original source P3-S1-C13
    page: 3
    quote: 'Data Analysis

      For each of the 50 subjects without DWI abnormality in BA

      22, we determined the Pearson correlation between (1) mean

      delay in left BA 22 relative to right BA 22; and (2) the error

      rate in spoken word/picture verification (a measure of word

      comprehension and severity of lexical–semantic deficit).

      '
    supports: method
  - section: Original source P2-S2-C9
    page: 2
    quote: 'Thus, 50 subjects were

      included in the analysis of lexical–semantic impairment ver-

      sus delay on PWI.'
    supports: sample
  - section: Original source P2-S1-C6
    page: 2
    quote: 'Patients and Methods

      Patients

      A total of 80 patients met inclusion criteria of (1) clinical

      diagnosis of acute left hemispheric ischemic stroke within 24

      hours of symptom onset or symptom progression and (2)

      right-handed and premorbid proficiency in English; as well

      '
    supports: sample
  - section: Original source P2-S2-C5
    page: 2
    quote: 'Time after onset or worsening of symptoms

      was 0.5 to 24 hours (mean, 10.3 hours; SD, 8.4).'
    supports: sample
  - section: Original source P5-S1-C9
    page: 5
    quote: 'However, this imaging technique

      is less widely available in acute stroke and is very sus-

      ceptible to motion artifacts.'
    supports: limitation
predictor_type: imaging_metric
short_definition: Mean number of seconds of delay in time-to-peak (TTP) concentration
  of contrast in left Brodmann's area 22 relative to the homologous region on the
  right, measured using perfusion-weighted imaging (PWI) and identified via published
  BA templates.
assessment:
- spoken word/picture verification
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-24'
relationship_review:
  paper: Hillis2001
  proposal_id: R001
  review_status_sha256: 566005d990178333234da81aebee04fc5a886f86e3d7e70aa240b72cc4babb63
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: bc2033e2721e82705caeee57f4dee18735f8761cd5784e32ff3ff31c1273f0d0
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: bc2033e2721e82705caeee57f4dee18735f8761cd5784e32ff3ff31c1273f0d0
        A/passages.json: e44568a5662b8c9b6b1d9b9029f93b9082098d2b86ec0be6fd8efcd2535eea95
        A/raw.json: 811967ff94b2ee346e2c1378b8075a280c920cd38a47f4ef68214b7b99c753a0
        A/source-units.json: 8b74a073e531382dd234591e96fc924e1e9f5b114b352c69a4f5d93c5f678920
        A/full-source-units.json: bac6e07bb81d4fab72a53937fe3809962628051faf54a3201bb25c79b98487ee
        A/meta.json: 048416988c8a46ed9aa60054b708b5af03df1aa288d295ab5cc2f6e70ea427cc
        A/table-images/manifest.json: d731b783d0583d8c97623789c597b4a4949b5a68a592aa1fc4ade28435874efe
        A/clauses/window-03/raw.json: 0a64652f7384205b9b0bb622a1e68c3337796116e8f166dad6c455ccda39596b
        A/clauses/window-03/prompt.txt: 8351c2f0ca07226d1795e1b2c558eac9b09121559193440026a1c8cdcb1db430
        A/clauses/window-03/meta.json: 1711e44b7bb9fc50c028b8763fda9b7a119baca2dee13374f4653827a2105714
        A/clauses/window-02/raw.json: 826739166ef20b3666202104f4b665ab3ad917e71b360de67cf7ff9537b99268
        A/clauses/window-02/prompt.txt: c68c0dcd3d7bcbc6c6a6a92155d62f48bc08e65ad4659019a619fae50ecf4e34
        A/clauses/window-02/meta.json: d35eb95a26fe650633ef68145af633e1d7494f47204489b6e78955b7067d00f6
        A/clauses/window-01/raw.json: 17d6b46f84601766ad1cc6cb90ad9d64ae386f7263530237bd085cc8afd90469
        A/clauses/window-01/prompt.txt: 4a415175dd24ed61584f130908c44905f1cb3cd227f05692609518f69c12c485
        A/clauses/window-01/meta.json: 6c37423e7e389db9f0e0a728755dcd5cec6e0c265cd82a51476a5586e917692d
        B/passages.json: e44568a5662b8c9b6b1d9b9029f93b9082098d2b86ec0be6fd8efcd2535eea95
        B/raw.json: 93a4379a0ab205d917d39742f33eb5d39385900018d777ceb7f6141bc49af8c1
        B/source-units.json: 8b74a073e531382dd234591e96fc924e1e9f5b114b352c69a4f5d93c5f678920
        B/full-source-units.json: bac6e07bb81d4fab72a53937fe3809962628051faf54a3201bb25c79b98487ee
        B/meta.json: f4aa27da72cddd624e36f1540d4c246c431a588a4bf7c8305606e220aad24ba4
        B/table-images/manifest.json: d731b783d0583d8c97623789c597b4a4949b5a68a592aa1fc4ade28435874efe
        B/clauses/window-03/raw.json: 0214785a44f982c97d76a491faab2e1fdda504aa19b38cbf24f263cc809186b8
        B/clauses/window-03/prompt.txt: 8351c2f0ca07226d1795e1b2c558eac9b09121559193440026a1c8cdcb1db430
        B/clauses/window-03/meta.json: bbd292c64d61eca2b42ca97311170ff2276a5c268d608e2db3e632fedb3a1107
        B/clauses/window-02/raw.json: fd86090244dff96cd1999c58d7b44db415c0d088c0d133a770f94e925220f04e
        B/clauses/window-02/prompt.txt: c68c0dcd3d7bcbc6c6a6a92155d62f48bc08e65ad4659019a619fae50ecf4e34
        B/clauses/window-02/meta.json: 7927184b3cdccbf469ed8549feb23bfc1c3189c1e2d45bea17119b9b60cfa0de
        B/clauses/window-01/raw.json: 2be8bda2d281f5167230467245c7d1d605021fa479b3c2b8a9d0dbff4916bfac
        B/clauses/window-01/prompt.txt: 4a415175dd24ed61584f130908c44905f1cb3cd227f05692609518f69c12c485
        B/clauses/window-01/meta.json: b7fbe30ca78d771469dde2564b13355a8610eb0319ae0cf3d5eb3382d83247d1
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
      pdf_sha256: bc2033e2721e82705caeee57f4dee18735f8761cd5784e32ff3ff31c1273f0d0
      source_review: _compare/relationships-2026-11-16/review-current/Hillis2001
      source_status_sha256: 233e909ce4a7848de3016aef11d385cff047fe75db0c2c16f53c329703b14938
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R001
    exposure:
      text: mean number of seconds of delay in time-to-peak concentration of contrast
        in Wernicke’s area (relative to the right)
    outcome:
      text: rate of errors on a word comprehension test (spoken word/picture verification)
    analysis_label: Correlation of perfusion delay and word comprehension
    relation: association
    evidence_ids:
    - P1-S1-C9
    - P3-S2-C2
    qualifier_ids:
    - P2-S2-C9
    - P3-S1-C13
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: bc2033e2721e82705caeee57f4dee18735f8761cd5784e32ff3ff31c1273f0d0
      source_review: _compare/relationships-2026-11-16/review-current/Hillis2001
      source_status_sha256: 233e909ce4a7848de3016aef11d385cff047fe75db0c2c16f53c329703b14938
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P5-S1-C10
      - Result passage disposed without unit P5-S2-C4
      unattached_null_or_qualifier_ids: []
      suppressed_nonrepresented_units: 3
      default_disposition_count_requires_completeness_check: 76
      unselected_timing_passages:
      - P2-S1-C6
      - P2-S2-C1
      - P2-S2-C4
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P3-S2-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P2-S3-C2
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      empty_frame_slots_require_confirmation:
      - validation
      - analysis_restrictions
      - personal_factors
      - tested_personal_effects
      - adjustment_roles
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
        - P3-S2
        - P3-S3
        - P4-S1
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: bc2033e2721e82705caeee57f4dee18735f8761cd5784e32ff3ff31c1273f0d0
      source_review: _compare/relationships-2026-11-16/review-current/Hillis2001
      source_status_sha256: 233e909ce4a7848de3016aef11d385cff047fe75db0c2c16f53c329703b14938
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C9
      disposition: represented
      result_indexes:
      - 0
      reason: States the strong Pearson correlation between TTP delay in Wernicke's
        area and word comprehension error rate.
    - source_id: P3-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Provides mean scores for subtests in a control group.
    - source_id: P3-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports interjudge reliability for scoring.
    - source_id: P3-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports interjudge agreement for TTP delay calculations.
    - source_id: P3-S2-C2
      disposition: represented
      result_indexes:
      - 0
      reason: Provides the specific correlation coefficient (r=0.84) and p-value for
        the relationship.
    - source_id: P3-S2-C4
      disposition: represented
      result_indexes:
      - 1
      reason: Identifies the 2.5-second delay threshold associated with minimal impairment.
    - source_id: P3-S2-C5
      disposition: represented
      result_indexes:
      - 1
      reason: Qualifies the 2.5-second threshold by discussing patients with minimal
        impairment despite mean delays < 2.5s.
    - source_id: P3-S2-C6
      disposition: represented
      result_indexes:
      - 0
      reason: Provides individual patient examples illustrating the correlation between
        delay and error rate.
    - source_id: P3-S2-C7
      disposition: represented
      result_indexes:
      - 2
      reason: Reports that improved perfusion of BA 22 by day 3 was associated with
        improved spoken word/picture verification.
    - source_id: P4-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discusses previous PET studies and the general role of BA 22.
    - source_id: P5-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discusses clinical implications of diffusion-perfusion mismatch.
    - source_id: P5-S1-C4
      disposition: repeated
      result_indexes:
      - 1
      reason: Restates the 2.5-second threshold finding in the discussion.
    - source_id: P5-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion about contrast PWI as a measure of blood flow reduction.
    - source_id: P5-S2-C2
      disposition: repeated
      result_indexes:
      - 0
      reason: Summary statement restating the correlation between regional delay and
        functional impairment.
    - source_id: P5-S2-C4
      disposition: repeated
      result_indexes:
      - 0
      reason: Summary statement confirming the role of Wernicke's area in spoken word
        comprehension.
    unresolved_coverage: []
    pending_source_ids:
    - P3-S1-C1
    - P3-S1-C3
    - P3-S1-C12
    - P3-S2-C5
    - P3-S2-C6
    - P4-S1-C4
    - P5-S1-C3
    - P5-S1-C4
    - P5-S1-C10
    - P5-S2-C2
    - P5-S2-C4
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
      - P1-S1-C8
      eligibility:
      - P2-S2-C1
      - P2-S2-C6
      - P2-S2-C8
      imaging_provenance:
      - P3-S1-C10
      - P3-S1-C11
      imaging_timing:
      - P1-S1-C8
      - P2-S2-C5
      outcome_timing:
      - P3-S2-C7
      outcome_definition:
      - P2-S1-C5
      - P3-S1-C4
      - P3-S2-C2
      validation: []
      analysis_restrictions: []
      dependent_variable_statement:
      - P2-S1-C5
      - P3-S1-C13
      limitations:
      - P5-S1-C6
      - P5-S1-C7
      - P5-S1-C8
      - P5-S1-C9
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles: []
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P2-S2-C4
      - P2-S2-C5
    outcome_type: both_reported
    imaging_vs_outcome: mixed
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P3-S2-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P2-S3-C2
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
      pdf_sha256: bc2033e2721e82705caeee57f4dee18735f8761cd5784e32ff3ff31c1273f0d0
      review_sha256: 566005d990178333234da81aebee04fc5a886f86e3d7e70aa240b72cc4babb63
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
      - P1-S1-C9
      - P3-S2-C2
      source_result: A strong positive Pearson correlation (r = 0.84, p < 0.00001)
        was found between the mean number of seconds of delay in time-to-peak concentration
        of contrast in left Brodmann's area 22 (Wernicke's area) relative to the right,
        and the error rate on a spoken word/picture verification test in 50 acute
        stroke patients without infarct in that region.
      result_status: detected
      patient_measurement: non_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis is the correlation between perfusion delay
            in Wernicke's area and word comprehension error rates in the 50-patient
            subset without DWI abnormalities, as described in P1-S1-C9 and P3-S2-C2.
          source_ids:
          - P1-S1-C9
          - P3-S2-C2
          - P3-S1-C13
        direction:
          answer: fits
          reason: The source reports a 'very high correlation' (r=0.84) indicating
            that greater perfusion delay is associated with higher error rates (more
            severe impairment). The draft's direction 'likely' (implying a positive
            association/prediction) is consistent with this detected association.
          source_ids:
          - P3-S2-C2
          - P3-S2-C3
        construct:
          answer: fits
          reason: The exposure is correctly identified as the mean delay in TTP in
            Wernicke's area (BA 22) relative to the right. The outcome is the error
            rate on spoken word/picture verification. The patient measurement is non-imaging
            (behavioral language test), distinct from the imaging metric used for
            the exposure.
          source_ids:
          - P1-S1-C9
          - P3-S1-C13
          - P2-S3-C1
        qualifications:
          answer: fits
          reason: The draft correctly includes the critical qualification that the
            analysis was restricted to patients without DWI abnormalities in BA 22
            (to exclude luxury perfusion/infarct), which is explicitly stated in P2-S2-C6
            and P3-S1-C13.
          source_ids:
          - P2-S2-C6
          - P3-S1-C13
          - P2-S2-C9
        missing_material_caveat:
          answer: fits
          reason: The draft includes the key selection restriction (no DWI abnormality).
            While P5-S1-C7 mentions potential underestimation due to right hemisphere
            hypoperfusion, this is a general limitation of the relative TTP measure
            rather than a specific caveat that invalidates the core correlation finding
            in the context of the selected analysis. The primary material caveat regarding
            the exclusion of infarcted tissue is present.
          source_ids:
          - P2-S2-C6
          - P5-S1-C7
      optional_pending:
      - Specific correlation coefficient value (r=0.84) and p-value not transcribed
        in draft fields
      - Details on interjudge reliability of TTP measurement (P3-S1-C12)
      - Specific exclusion criteria for visual/auditory agnosia (P2-S2-C8)
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Specific correlation coefficient value (r=0.84) and p-value not transcribed
      in draft fields
    - Details on interjudge reliability of TTP measurement (P3-S1-C12)
    - Specific exclusion criteria for visual/auditory agnosia (P2-S2-C8)
    normalizations: []
    analysis_identity:
      id: R001
      exposure:
        text: mean number of seconds of delay in time-to-peak concentration of contrast
          in Wernicke’s area (relative to the right)
      outcome:
        text: rate of errors on a word comprehension test (spoken word/picture verification)
      analysis_label: Correlation of perfusion delay and word comprehension
      relation: association
      evidence_ids:
      - P1-S1-C9
      - P3-S2-C2
      qualifier_ids:
      - P2-S2-C9
      - P3-S1-C13
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: bc2033e2721e82705caeee57f4dee18735f8761cd5784e32ff3ff31c1273f0d0
        source_review: _compare/relationships-2026-11-16/review-current/Hillis2001
        source_status_sha256: 233e909ce4a7848de3016aef11d385cff047fe75db0c2c16f53c329703b14938
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P2-S2-C9:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: bc2033e2721e82705caeee57f4dee18735f8761cd5784e32ff3ff31c1273f0d0
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: e1563557f8fdf8c24a97c4009fa26d9d47c618a633ff6ae403bfdafe22400916
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S2-C9
          page: 2
          text_layer_sha256: e1563557f8fdf8c24a97c4009fa26d9d47c618a633ff6ae403bfdafe22400916
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Thus, 50 subjects were

          included in the analysis of lexical–semantic impairment ver-

          sus delay on PWI.'
        anchor_text: 'Thus, 50 subjects were

          included in the analysis of lexical–semantic impairment ver-

          sus delay on PWI.'
        excluded_fragments: []
        image_sha256: 67074a1746ffa0381e4b5323a4fce290200ebf76fba2f5cf301ac30a0ad7df4d
        transcription: '. Thus, 50 subjects were

          included in the analysis of lexical–semantic impairment ver-

          sus delay on PWI'
      P2-S1-C6:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: bc2033e2721e82705caeee57f4dee18735f8761cd5784e32ff3ff31c1273f0d0
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 732a3d904ccec80d7915383d6d9d7be8645191ffd7bbcc4fea781ef90ec741ed
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S1-C6
          page: 2
          text_layer_sha256: 95a812105fc35bef61c475bed55da417b49e6b0a4a523bd73b92b478fe3286fa
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: 'Patients and Methods

          Patients

          A total of 80 patients met inclusion criteria of (1) clinical

          diagnosis of acute left hemispheric ischemic stroke within 24

          hours of symptom onset or symptom progression and (2)

          right-handed and premorbid proficiency in English; as well

          '
        anchor_text: 'Patients and Methods

          Patients

          A total of 80 patients met inclusion criteria of (1) clinical

          diagnosis of acute left hemispheric ischemic stroke within 24

          hours of symptom onset or symptom progression and (2)

          right-handed and premorbid proficiency in English; as well'
        excluded_fragments: []
        image_sha256: 072d3e04911c8044861c1e517ad12af4e4c16abd9694bd58b1423632715c905e
      P2-S2-C5:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: bc2033e2721e82705caeee57f4dee18735f8761cd5784e32ff3ff31c1273f0d0
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: b66bf1158b63a1d9cbe511fe355706218f332ae239de5dbd7ef6649f81e37704
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S2-C5
          page: 2
          text_layer_sha256: b66bf1158b63a1d9cbe511fe355706218f332ae239de5dbd7ef6649f81e37704
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Time after onset or worsening of symptoms

          was 0.5 to 24 hours (mean, 10.3 hours; SD, 8.4).'
        anchor_text: 'Time after onset or worsening of symptoms

          was 0.5 to 24 hours (mean, 10.3 hours; SD, 8.4).'
        excluded_fragments: []
        image_sha256: 1f359694ca4b78dee97ec4cd71b13317dcc4529738a40188cf88dc048608ff8a
        transcription: '. Time after onset or worsening of symptoms

          was 0.5 to 24 hours (mean, 10.3 hours; SD, 8.4)'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 1
  quote: 'For 50 patients without infarct in Wernicke’s area, we

    found a strong Pearson correlation between the rate of errors on a word comprehension
    test and the mean number of

    seconds of delay in time-to-peak concentration of contrast in Wernicke’s area,
    relative to the homologous region on the

    right.'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-24'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
