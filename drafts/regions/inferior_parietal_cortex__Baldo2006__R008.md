---
id: inferior_parietal_cortex
name: inferior parietal cortex cluster
kind: network
findings:
- id: f1
  target_audit:
    status: behaviour_label_present
    category: behaviour_or_language_construct
    original_target: verbal_fluency
    reason: Label names a behaviour or language construct; its exact operational definition and measurement
      still need source review.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  outcome_measurement:
    status: identified
    instruments:
    - name: Study verbal fluency tasks
      subtest: Letter and category fluency
    metric: Correct non-repeated items; 90 seconds per cue
    definition_source:
      citation: '@Baldo2006'
      page: 2
      quote: In the letter fluency task, patients were first asked to name words that began with the letter
        F. The examiner recorded the patients’ responses for 90 s. (The 90-s procedure was chosen rather
        than a 60-s procedure to be comparable to another study by our group.) Patients were subsequently
        asked to generate words beginning with the letters A and then S. Following letter fluency, patients
        were given 90 s to generate items belonging to the semantic cat- egories fruits, animals, and supermarket
        items, in that order. The order of the fluency conditions was fixed and was con- sistent across
        all patients. In both letter and category flu- ency conditions, patients were told to avoid repetitions.
        Performance for both fluency tasks was computed as the number of correct items generated in response
        to all three cues. Items were scored as correct if they belonged to the category and were not repetitions.
      basis: Main paper methods checked directly
      source_pdf: C0001_Baldo2006.pdf
      source_pdf_sha256: 924b0b7f66aba42402f55f1c4c2a48266c4a82e3358b0247380131ac1ebc7bed
    note: Measurement metadata identified from source evidence; finding remains unapproved.
  target: verbal_fluency
  target_kind: impairment
  claim: lesions in the inferior parietal cortex were associated with deficits in
    both letter and category fluency tasks
  direction: likely
  relationship: correlational
  method: VLSM
  sample:
    n: 48
    population: native English speaking, premorbidly right-handed patients with a
      single left-hemisphere cerebrovascular accident
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
  - restricted to patients with left-hemisphere lesions
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: patient lesion overlap with a voxel-based lesion symptom
    mapping (VLSM) analysis. letter fluency measured by generating words starting
    with F, A, and S; category fluency measured by generating items in fruits, animals,
    and supermarket items categories; performance computed as the total number of
    correct items generated across all three cues for each task. Additional metadata
    has not been transcribed; review the pending-field flags before approval. PDF
    image reading (P2-S2-C5, two-model agreement, human verification pending): METHODS


    Participants


    A total of 48 patients (14 women and 34 men) who had suffered a single, left-hemisphere
    cerebrovascular accident (CVA) were tested in the current study Original text-layer
    quotation is preserved below. PDF image reading (P2-S2-C6, two-model agreement,
    human verification pending): . Patients were all

    native English speakers and were premorbidly right-handed,

    according to the Edinburgh Handedness Inventory (Old-

    field, 1971) Original text-layer quotation is preserved below. Reconcile this
    new analysis with earlier drafts and source-review decisions for the paper; new
    candidate IDs do not carry earlier decisions forward.'
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
    - proposed_concept:verbal_fluency
  citation: '@Baldo2006'
  source_passages:
  - section: Original source P4-S1-C11
    page: 4
    quote: 'For

      example, both letter and category fluency tasks were also

      affected by lesions in inferior parietal cortex, a region often

      associated with verbal working memory (e.g., Jonides et al.,

      1998).'
    supports: claim
  - section: Original source P2-S2-C5
    page: 2
    quote: 'METHODS

      Participants

      A total of 48 patients (14 women and 34 men) who had

      suffered a single, left-hemisphere cerebrovascular accident

      (CVA) were tested in the current study.'
    supports: sample
  - section: Original source P2-S2-C7
    page: 2
    quote: 'All patients were tested in the chronic phase of

      their CVA, at least 9 months post-onset (M 5 62.8 months;

      SD 5 59.7; range, 9–273 months).'
    supports: sample
  - section: Original source P2-S2-C6
    page: 2
    quote: 'Patients were all

      native English speakers and were premorbidly right-handed,

      according to the Edinburgh Handedness Inventory (Old-

      field, 1971).'
    supports: sample
  - section: Original source P3-S1-C2
    page: 3
    quote: 'The VLSM analyses conducted t tests at every voxel

      to compare performance in patients with and without a lesion

      in that voxel.'
    supports: method
  - section: Original source P2-S3-C11
    page: 2
    quote: 'Performance for both fluency tasks was computed as the

      number of correct items generated in response to all three

      cues.'
    supports: method
  - section: Original source P4-S2-C8
    page: 4
    quote: 'Because the present study was restricted

      to patients with left-hemisphere lesions, our findings do not

      speak to the relative contribution of the right hemisphere to

      verbal fluency.'
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-20'
relationship_review:
  paper: Baldo2006
  proposal_id: R008
  review_status_sha256: d610aee7474eff499098bc5184549c6cbb3ceda71b2666c5f9dc75657dfa38f4
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 924b0b7f66aba42402f55f1c4c2a48266c4a82e3358b0247380131ac1ebc7bed
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 924b0b7f66aba42402f55f1c4c2a48266c4a82e3358b0247380131ac1ebc7bed
        A/passages.json: 7c086a1ef9c366c669035e4d45e7e7823e3af81232832fba5d70cef87ccc0c7c
        A/raw.json: c16e1efbd12f20f59e13a50099f715861a5fa09a7d424420e9ffdd30918918e2
        A/source-units.json: e70b06b797b9a2c79085cf095682e3825ae4c84f4c09bd8dd8bb022ebd5f002d
        A/full-source-units.json: 6d92a558b6df9152899e937ed3acc8cc60c25cd8a1a4bbcc072e64ac61f04a99
        A/meta.json: 1ccfa677a18777d0f574d7ba5ee28dd3328c07a4c47190378e64e2b26fdaf524
        A/table-images/manifest.json: ab0e6c88e498cce35655df548a5daa8abf73f24c0ea7d54548cc7777ae968c87
        A/clauses/window-03/raw.json: 05ed3ee18098138374d6ff4d1930078bf108d3946845ddb578f54906ab0afb1b
        A/clauses/window-03/prompt.txt: 3c91712ffdd5674a04f8af349bc27b220f4a7351f8e42b3250f50b533b3f0717
        A/clauses/window-03/meta.json: d23fbde0e9955d2edf0030d238223386145b0fbbbddf958d01f4d29fe27a4aa1
        A/clauses/window-04/raw.json: a5ace14936f3e94c1dfde934af1c1864eeca364b8f28b69f0abc3f2078d36c56
        A/clauses/window-04/prompt.txt: 6cdf3cd7aef5c40a123765225828466e487faed73d8390c4011929df83602f27
        A/clauses/window-04/meta.json: bdd5b4db244154cd14163558e5f206b88df8ad09c75fff561d78b720734e07a6
        A/clauses/window-02/raw.json: 5f77e7f810bb102b5af9efff422e52b0952df4b66b3e9a22183bc5f957b4d202
        A/clauses/window-02/prompt.txt: 8eb582588e035ff9d7e08722521878400b01038d7a6a18e3a485ab33e2f01b37
        A/clauses/window-02/meta.json: 2e3a79ecd1c8551427a31a81ac826e19165bcd59fa38ac4f15f2321747a43296
        A/clauses/window-01/raw.json: afbf4e6b2b4d0cd7037ca86ce1f8f247de670263bd4553476b66fa8cb523394f
        A/clauses/window-01/prompt.txt: 57d6fb9b0112b6e285d52b1bbc20c3429366062d0a7c178217ca2c27ae08accf
        A/clauses/window-01/meta.json: e4d08bb2a6acc61aebc1dcf7e1544484c0a1f0322f15208005f76cc2685876aa
        B/passages.json: 7c086a1ef9c366c669035e4d45e7e7823e3af81232832fba5d70cef87ccc0c7c
        B/raw.json: 379dcbc6db6c8efc95a940e6fa102a58566a39f09fa45c7ea7f59d2737268fe1
        B/source-units.json: e70b06b797b9a2c79085cf095682e3825ae4c84f4c09bd8dd8bb022ebd5f002d
        B/full-source-units.json: 6d92a558b6df9152899e937ed3acc8cc60c25cd8a1a4bbcc072e64ac61f04a99
        B/meta.json: bedfda47ee9fa80507ae8991094a1c4e33e566b6a7162f82ed5a952f5c6dd638
        B/table-images/manifest.json: ab0e6c88e498cce35655df548a5daa8abf73f24c0ea7d54548cc7777ae968c87
        B/clauses/window-03/raw.json: c75988d7fe905284f4ec42adbcf5de58a1e41269db2380a0fc1bf86628ff7249
        B/clauses/window-03/prompt.txt: 3c91712ffdd5674a04f8af349bc27b220f4a7351f8e42b3250f50b533b3f0717
        B/clauses/window-03/meta.json: 3145c95c82efea6b354e7f862e11820a514d5b6f22a33d5faf017c5c05c088e0
        B/clauses/window-04/raw.json: 58f6bdb91f9e5751c2f2f018f6a6785ce069a70bbe13486a6717e3f4ed07cb1c
        B/clauses/window-04/prompt.txt: 6cdf3cd7aef5c40a123765225828466e487faed73d8390c4011929df83602f27
        B/clauses/window-04/meta.json: 79abea50130cceb985062b3f5baf4c066946e1a57309543afe35a753e346efba
        B/clauses/window-02/raw.json: 62984aba5577997ba35daaca5e4642b445ec588c6b4f60becfc61d5a74a770a4
        B/clauses/window-02/prompt.txt: 8eb582588e035ff9d7e08722521878400b01038d7a6a18e3a485ab33e2f01b37
        B/clauses/window-02/meta.json: 9bf791e3902301753ba113dc1f7e555896db786ad174291944469901086e4c07
        B/clauses/window-01/raw.json: 02b976dd99ad8e13ce3d675ec2ddaece0588a52fa5453b653ada75090a195ec1
        B/clauses/window-01/prompt.txt: 57d6fb9b0112b6e285d52b1bbc20c3429366062d0a7c178217ca2c27ae08accf
        B/clauses/window-01/meta.json: f1beb09770f02b4d41ef5c4be63ce0879efbd432ff5c42e6f69b9358e1a1a85d
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
      pdf_sha256: 924b0b7f66aba42402f55f1c4c2a48266c4a82e3358b0247380131ac1ebc7bed
      source_review: _compare/relationships-2026-11-16/review-current/Baldo2006
      source_status_sha256: 05abdd0d5b195ff1a8712e7f5698fec2d705f82523c42cb62d93dd369f87d8cf
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R008
    exposure:
      text: lesions in inferior parietal cortex
    outcome:
      text: letter and category fluency
    analysis_label: VLSM (General)
    relation: association
    evidence_ids:
    - P4-S1-C11
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
      pdf_sha256: 924b0b7f66aba42402f55f1c4c2a48266c4a82e3358b0247380131ac1ebc7bed
      source_review: _compare/relationships-2026-11-16/review-current/Baldo2006
      source_status_sha256: 05abdd0d5b195ff1a8712e7f5698fec2d705f82523c42cb62d93dd369f87d8cf
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P3-S1-C5
      - Result passage disposed without unit P3-S2-C2
      - Result passage disposed without unit P3-S2-C4
      - Result passage disposed without unit P4-S1-C10
      - Result passage disposed without unit P4-S1-C11
      - Result passage disposed without unit P4-S1-C14
      - Result passage disposed without unit P4-S1-C7
      - Result passage disposed without unit P4-S1-C8
      unattached_null_or_qualifier_ids: []
      suppressed_nonrepresented_units: 6
      default_disposition_count_requires_completeness_check: 99
      unselected_timing_passages:
      - P2-S2-C8
      - P2-S2-C9
      - P2-S2-C11
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P3-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P3-S1-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S1-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      empty_frame_slots_require_confirmation:
      - validation
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
        - P3-S1
        - P3-S2
        - P4-S2
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 924b0b7f66aba42402f55f1c4c2a48266c4a82e3358b0247380131ac1ebc7bed
      source_review: _compare/relationships-2026-11-16/review-current/Baldo2006
      source_status_sha256: 05abdd0d5b195ff1a8712e7f5698fec2d705f82523c42cb62d93dd369f87d8cf
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C7
      disposition: repeated
      result_indexes:
      - 0
      - 1
      reason: Abstract restatement of results.
    - source_id: P1-S1-C8
      disposition: repeated
      result_indexes:
      - 0
      - 1
      - 8
      reason: Abstract restatement of results.
    - source_id: P2-S2-C4
      disposition: repeated
      result_indexes:
      - 0
      - 1
      reason: General summary of findings.
    - source_id: P3-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive mean performance scores.
    - source_id: P3-S1-C6
      disposition: represented
      result_indexes:
      - 0
      reason: Direct result of letter fluency VLSM.
    - source_id: P3-S1-C7
      disposition: represented
      result_indexes:
      - 0
      reason: Direct result of letter fluency VLSM.
    - source_id: P3-S1-C8
      disposition: represented
      result_indexes:
      - 1
      reason: Direct result of category fluency VLSM.
    - source_id: P3-S1-C9
      disposition: represented
      result_indexes:
      - 1
      reason: Direct result of category fluency VLSM.
    - source_id: P3-S1-C11
      disposition: represented
      result_indexes:
      - 2
      reason: Direct result of subtraction map analysis.
    - source_id: P3-S1-C12
      disposition: represented
      result_indexes:
      - 3
      reason: Direct result of subtraction map analysis.
    - source_id: P3-S2-C2
      disposition: represented
      result_indexes:
      - 4
      reason: Direct result of sensitivity analysis comparing 60s and 90s.
    - source_id: P3-S2-C4
      disposition: repeated
      result_indexes:
      - 0
      - 1
      reason: Discussion restatement of results.
    - source_id: P4-S1-C7
      disposition: represented
      result_indexes:
      - 5
      reason: Direct result of category-specific VLSM.
    - source_id: P4-S1-C8
      disposition: represented
      result_indexes:
      - 6
      reason: Direct result of category-specific VLSM.
    - source_id: P4-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Introductory statement to subsequent results.
    - source_id: P4-S1-C11
      disposition: represented
      result_indexes:
      - 7
      reason: Direct result regarding parietal cortex.
    - source_id: P4-S1-C14
      disposition: represented
      result_indexes:
      - 8
      reason: Direct result regarding insula and putamen.
    - source_id: P4-S2-C11
      disposition: repeated
      result_indexes:
      - 0
      - 1
      reason: Conclusion restatement of results.
    unresolved_coverage: []
    pending_source_ids:
    - P1-S1-C7
    - P1-S1-C8
    - P2-S2-C4
    - P3-S1-C5
    - P3-S2-C4
    - P4-S1-C10
    - P4-S2-C11
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
      - P2-S2-C11
      recruited_sample:
      - P2-S2-C5
      - P2-S2-C11
      eligibility:
      - P2-S2-C6
      - P2-S2-C10
      - P2-S2-C11
      - P2-S2-C13
      imaging_provenance:
      - P2-S3-C14
      imaging_timing:
      - P2-S3-C14
      outcome_timing:
      - P2-S2-C7
      outcome_definition:
      - P2-S3-C11
      validation: []
      analysis_restrictions:
      - P3-S1-C3
      dependent_variable_statement:
      - P4-S1-C6
      limitations:
      - P4-S2-C8
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles: []
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P2-S2-C5
      - P2-S2-C6
      - P2-S2-C7
      - P2-S2-C8
      - P2-S2-C9
      - P2-S2-C12
    outcome_type: status_at_assessment
    imaging_vs_outcome: precedes_outcome
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P3-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P3-S1-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S1-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
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
      pdf_sha256: 924b0b7f66aba42402f55f1c4c2a48266c4a82e3358b0247380131ac1ebc7bed
      review_sha256: d610aee7474eff499098bc5184549c6cbb3ceda71b2666c5f9dc75657dfa38f4
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
      - P4-S1-C11
      source_result: VLSM analyses revealed that both letter and category fluency
        tasks were affected by lesions in inferior parietal cortex, a region often
        associated with verbal working memory.
      result_status: detected
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis corresponds to the VLSM results for inferior
            parietal cortex affecting both letter and category fluency, as described
            in P4-S1-C11 and supported by the general VLSM methodology in P3-S1-C2.
          source_ids:
          - P4-S1-C11
          - P3-S1-C2
        direction:
          answer: fits
          reason: The source states that fluency tasks were 'affected by lesions'
            in the inferior parietal cortex, which aligns with the draft's claim of
            an association with deficits. The direction is consistent with the detected
            association.
          source_ids:
          - P4-S1-C11
        construct:
          answer: fits
          reason: The exposure (lesions in inferior parietal cortex) and outcome (letter
            and category fluency) are correctly identified. The patient measurement
            is correctly identified as template_lesion_overlap, as VLSM overlays patient
            lesions on standardized brain templates (P2-S3-C15) rather than using
            patient-specific diffusion tractography.
          source_ids:
          - P4-S1-C11
          - P2-S3-C15
        qualifications:
          answer: fits
          reason: The draft includes relevant qualifications regarding the specific
            fluency tasks (F, A, S for letter; fruits, animals, supermarket for category)
            and the limitation to left-hemisphere lesions, which are supported by
            the source passages.
          source_ids:
          - P2-S3-C5
          - P2-S3-C8
          - P4-S2-C8
        missing_material_caveat:
          answer: fits
          reason: No material caveats are missing. The draft correctly notes the restriction
            to left-hemisphere lesions and the specific nature of the fluency tasks.
            The unresolved image-reading disagreements in P2-S2-C7 through P2-S2-C12
            relate to demographic statistics (age, education, etc.) and do not alter
            the core relationship between inferior parietal lesions and fluency performance.
          source_ids:
          - P4-S2-C8
          - P2-S3-C5
          - P2-S3-C8
      optional_pending:
      - sample.time_post_onset
      - demographic_statistics
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
    - demographic_statistics
    normalizations:
    - field: sample.time_post_onset
      original: chronic phase, at least 9 months post-onset
      action: not_transcribed
      reason: 'Numbers not grounded in usable selected source readings: 9'
    analysis_identity:
      id: R008
      exposure:
        text: lesions in inferior parietal cortex
      outcome:
        text: letter and category fluency
      analysis_label: VLSM (General)
      relation: association
      evidence_ids:
      - P4-S1-C11
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
        pdf_sha256: 924b0b7f66aba42402f55f1c4c2a48266c4a82e3358b0247380131ac1ebc7bed
        source_review: _compare/relationships-2026-11-16/review-current/Baldo2006
        source_status_sha256: 05abdd0d5b195ff1a8712e7f5698fec2d705f82523c42cb62d93dd369f87d8cf
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P2-S2-C5:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 924b0b7f66aba42402f55f1c4c2a48266c4a82e3358b0247380131ac1ebc7bed
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 0b80e8826676958e5425aee2cae036b57e34489a4d02fd62ce986239d968bb3c
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S2-C5
          page: 2
          text_layer_sha256: 0b80e8826676958e5425aee2cae036b57e34489a4d02fd62ce986239d968bb3c
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'METHODS

          Participants

          A total of 48 patients (14 women and 34 men) who had

          suffered a single, left-hemisphere cerebrovascular accident

          (CVA) were tested in the current study.'
        anchor_text: 'METHODS

          Participants

          A total of 48 patients (14 women and 34 men) who had

          suffered a single, left-hemisphere cerebrovascular accident

          (CVA) were tested in the current study.'
        excluded_fragments: []
        image_sha256: 3ad9854a568b9d5082e0f8d9589028fab61905b2155d8be4782371539933f679
        transcription: 'METHODS


          Participants


          A total of 48 patients (14 women and 34 men) who had suffered a single,
          left-hemisphere cerebrovascular accident (CVA) were tested in the current
          study'
      P2-S2-C7:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 924b0b7f66aba42402f55f1c4c2a48266c4a82e3358b0247380131ac1ebc7bed
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: b0d4b4f4b4337d9f32be2d9cfed957f039a26539265cdb2b9819903c744dcbca
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S2-C7
          page: 2
          text_layer_sha256: b0d4b4f4b4337d9f32be2d9cfed957f039a26539265cdb2b9819903c744dcbca
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: 'All patients were tested in the chronic phase of

          their CVA, at least 9 months post-onset (M 5 62.8 months;

          SD 5 59.7; range, 9–273 months).'
        anchor_text: 'All patients were tested in the chronic phase of

          their CVA, at least 9 months post-onset (M 5 62.8 months;

          SD 5 59.7; range, 9–273 months).'
        excluded_fragments: []
      P2-S2-C6:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 924b0b7f66aba42402f55f1c4c2a48266c4a82e3358b0247380131ac1ebc7bed
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 2c53e8cbcb08d426794257a780209c1131d37b212c8cffb78b5b4b1e8db4bfe0
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S2-C6
          page: 2
          text_layer_sha256: 2c53e8cbcb08d426794257a780209c1131d37b212c8cffb78b5b4b1e8db4bfe0
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Patients were all

          native English speakers and were premorbidly right-handed,

          according to the Edinburgh Handedness Inventory (Old-

          field, 1971).'
        anchor_text: 'Patients were all

          native English speakers and were premorbidly right-handed,

          according to the Edinburgh Handedness Inventory (Old-

          field, 1971).'
        excluded_fragments: []
        image_sha256: 0518a827f844f42c15687eb8f72c9408d7ed4427b52067e473305796cb2ea979
        transcription: '. Patients were all

          native English speakers and were premorbidly right-handed,

          according to the Edinburgh Handedness Inventory (Old-

          field, 1971)'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 4
  quote: 'For

    example, both letter and category fluency tasks were also

    affected by lesions in inferior parietal cortex, a region often

    associated with verbal working memory (e.g., Jonides et al.,

    1998).'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-20'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
