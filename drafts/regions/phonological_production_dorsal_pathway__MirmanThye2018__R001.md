---
id: phonological_production_dorsal_pathway
name: phonological-production dorsal pathway cluster
kind: network
findings:
- id: f1
  target_audit:
    status: behaviour_label_present
    category: behaviour_or_language_construct
    original_target: phonological_production_deficit
    reason: Label names a behaviour or language construct; its exact operational definition and measurement
      still need source review.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  outcome_measurement:
    status: needs_source_review
    instruments: []
    note: Outcome instrument/task is not yet verified for this finding. Do not infer it from the predictor
      or a paper-wide test list.
  target: phonological_production_deficit
  target_kind: impairment
  claim: Deficits in the phonological-production subsystem are associated with damage
    in a dorsal pathway primarily involving inferior parietal and frontal regions.
  direction: likely
  relationship: synthesis
  method: LSM
  sample:
    n: not_reported
    population: individuals with aphasia
    phase: not_reported
    time_post_onset: not_transcribed
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - structural MRI limitations for white-matter labels
  evidence_quality: narrative-review
  strength: weak
  notes: 'Exposure measurement: patient lesion overlap with a dorsal pathway primarily
    involving inferior parietal and frontal regions, as identified via data-driven
    lesion-symptom mapping. finding is a synthesis of results from four independent
    research groups using a data-driven approach to identify latent cognitive factors.
    Additional metadata has not been transcribed; review the pending-field flags before
    approval.'
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
    - proposed_concept:phonological_production_deficit
  citation: '@MirmanThye2018'
  source_passages:
  - section: Original source P3-S1-C4
    page: 3
    quote: "Deficits in the phonological-production subsystem \nare associated with\
      \ damage in a dorsal pathway primar-\nily involving inferior parietal and frontal\
      \ regions (Fig. \n2a, darker green)."
    supports: claim
  - section: Original source P1-S1-C4
    page: 1
    quote: "The modern version of the lesion method is called \nlesion-symptom mapping\
      \ (Bates et al., 2003; Rorden & \nKarnath, 2004) and uses brain scans (MRI or\
      \ computed \ntomography) to localize brain damage (lesions) for each \nindividual\
      \ in a group of participants with varying \ndegrees of deficit."
    supports: method
  - section: Original source P2-S1-C3
    page: 2
    quote: "Recent studies from four independent research \ngroups1 using the data-driven\
      \ approach have identified \nfour cognitive systems of language processing and\
      \ their \nassociated brain regions: phonology, semantics, fluency, \nand executive\
      \ functions."
    supports: sample
  - section: Original source P2-S1-C9
    page: 2
    quote: "The sub-\nstantial convergence across different laboratories, each \n\
      using a somewhat different battery of tests and testing \ndifferent groups of\
      \ individuals with aphasia, reveals \nthat this organization of language processing\
      \ is quite \nrobust."
    supports: sample
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-25'
relationship_review:
  paper: MirmanThye2018
  proposal_id: R001
  review_status_sha256: b06066d2600487f24589f3cda5312d3cfcf3764f0baf720eae279368773f95a8
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 7cb83fb698c86998f64457686ec810430c9012dffb91fbe19caac8c85064a92e
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 7cb83fb698c86998f64457686ec810430c9012dffb91fbe19caac8c85064a92e
        A/passages.json: bf28d38ee9815462ddc32bd52c02b5b0ce6cd5df650f175a8df56b41aea01120
        A/raw.json: 6010470873f946974ecf4f9e5e7fdffef3f65a2ce0dfa5c651fa7d46732923bf
        A/source-units.json: d91b1b7430ffca6cedf1ed2bd1c8248d1c7a7cff685f21958ebb3e4c5c7fbc20
        A/full-source-units.json: ee6fdcf129c72005d504fcc00412b4bfcc2227088971cc79c25155e3808bb823
        A/meta.json: 7f5f116383419c4a28c3be145552c6f98868b7246b26b906e688424019e14fdb
        A/table-images/manifest.json: 79186ac4b110ac6c4709192b82e0e8d9e8651e3b19b9a2f1a608645236f22bdb
        A/clauses/window-03/raw.json: 64bdacd02532e5100346aa4d1b50a2822bace28857c9c1a2591c7f4d73caf496
        A/clauses/window-03/prompt.txt: 63fdffd70c593f5a2bdddfc30bb50e4ab13858c8b870ed25a746b2153615caa7
        A/clauses/window-03/meta.json: 9c2dfaef352b2fd4298e6e616f7149b19fcc6549012f7b94a28003151a4e66b0
        A/clauses/window-04/raw.json: 510fa279ea9e48339e3ad014cf73451d3fe4ba5c8a39719bf2e65b6326ea364c
        A/clauses/window-04/prompt.txt: 8e8d8b13418b0c3ef33755f7b8be4bbb266a7f70b1b6d7bfb1616d46f524cfde
        A/clauses/window-04/meta.json: c8c394e0c924cb589b42640cd262654101939351b4bad0e507e67254a0e988f4
        A/clauses/window-05/raw.json: 7369b13df2d37fd7b36283f920837a7b48510dc2dcf0f0949e4d76e88c6274e7
        A/clauses/window-05/prompt.txt: b95893c989c6a706bf843d999767b0b30dc215333812d1500f54c1c39f43236a
        A/clauses/window-05/meta.json: 9928847343fa1ccb51d0550dca446e39a9cb9a68691e86eebfdab9e116e3d26d
        A/clauses/window-02/raw.json: d78e0cf55fad35624d450e5d4b6b6768681a38d4d15c41dac8862df3394c450e
        A/clauses/window-02/prompt.txt: 46cb176ab38e6b7cafff508140a4a89151e45a04eff14776887e5aee88f93fa4
        A/clauses/window-02/meta.json: 2cea0ecec9e70d7130ddb07e913a118836bd29a83f7803fc38e252ccb99c9933
        A/clauses/window-01/raw.json: bd70bb3f4f61fd5db7d505353b0e7d2322b43cebaa64e5b4f4cec65058cb3066
        A/clauses/window-01/prompt.txt: b4a24ac80b5c6df9047f5c86b6f6dcaf08f60fbd85269df131c9c63a20e3bcd3
        A/clauses/window-01/meta.json: 26836bcccbf87ab62724f3938bcb4f5aefc5374365dfa4104bc8da47ce17c51b
        B/passages.json: bf28d38ee9815462ddc32bd52c02b5b0ce6cd5df650f175a8df56b41aea01120
        B/raw.json: 7a6526d26b2276fcac3e434f003f4a3d461b7027f19ed347df08be42e7b2cd09
        B/source-units.json: d91b1b7430ffca6cedf1ed2bd1c8248d1c7a7cff685f21958ebb3e4c5c7fbc20
        B/full-source-units.json: ee6fdcf129c72005d504fcc00412b4bfcc2227088971cc79c25155e3808bb823
        B/meta.json: ab5d712bac33664c2770277182564994cc31546bf6a9190c35a0f9832d8fa5a4
        B/table-images/manifest.json: 79186ac4b110ac6c4709192b82e0e8d9e8651e3b19b9a2f1a608645236f22bdb
        B/clauses/window-03/raw.json: 13ed3a6415e90fdb749b19d89627bfb370899e3548b961e83c7bf4a3abd3fb42
        B/clauses/window-03/prompt.txt: 63fdffd70c593f5a2bdddfc30bb50e4ab13858c8b870ed25a746b2153615caa7
        B/clauses/window-03/meta.json: 27fe89c2875df6bd82fd3b21f7abda83a72457479e031d372fd362fc7e8486e7
        B/clauses/window-04/raw.json: 6a5c3e7894e7706b1a24a0d1371ddac215ae1fc335f388054ae255a43e819d79
        B/clauses/window-04/prompt.txt: 8e8d8b13418b0c3ef33755f7b8be4bbb266a7f70b1b6d7bfb1616d46f524cfde
        B/clauses/window-04/meta.json: 23a5af4716b2c5b1cb3938f59285cc17be7c3af0be2b95d9b5e2434d87f37ca4
        B/clauses/window-05/raw.json: aeb468f790b4c1ef3c2f8255380ccb83f820bc10ca215b93db6923966ff22349
        B/clauses/window-05/prompt.txt: b95893c989c6a706bf843d999767b0b30dc215333812d1500f54c1c39f43236a
        B/clauses/window-05/meta.json: 650c3d9d9c6dae245fd4559fb7368e538e213f4ef9bac204b52626a4831f6b6e
        B/clauses/window-02/raw.json: db02af5f526be14a9fdc8ea01a0cdaaf4af2afbc0a8cadb38a5bd3c89b9134d7
        B/clauses/window-02/prompt.txt: 46cb176ab38e6b7cafff508140a4a89151e45a04eff14776887e5aee88f93fa4
        B/clauses/window-02/meta.json: 07b8be0fda215d02e2e53ea1ce97bbc996d5767911a37e107c8c6799a3e67d9b
        B/clauses/window-01/raw.json: 0124061394e9578fa06db08ca6166c59366cbaa5b95608098214a94ff0032256
        B/clauses/window-01/prompt.txt: b4a24ac80b5c6df9047f5c86b6f6dcaf08f60fbd85269df131c9c63a20e3bcd3
        B/clauses/window-01/meta.json: c84efd87ca973b357d0298d05c199b97d73bebe06b5d8a008d6fc8fa4384e874
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
      pdf_sha256: 7cb83fb698c86998f64457686ec810430c9012dffb91fbe19caac8c85064a92e
      source_review: _compare/relationships-2026-11-16/review-current/MirmanThye2018
      source_status_sha256: d3ac1ad6ff5f5a1d3cf67f099386147ed2da468f86834f4ffa3597c0b5b6691a
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R001
    exposure:
      text: damage in a dorsal pathway primarily involving inferior parietal and frontal
        regions
    outcome:
      text: phonological-production subsystem deficits
    analysis_label: lesion-symptom mapping
    relation: association
    evidence_ids:
    - P3-S1-C4
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
      pdf_sha256: 7cb83fb698c86998f64457686ec810430c9012dffb91fbe19caac8c85064a92e
      source_review: _compare/relationships-2026-11-16/review-current/MirmanThye2018
      source_status_sha256: d3ac1ad6ff5f5a1d3cf67f099386147ed2da468f86834f4ffa3597c0b5b6691a
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P3-S1-C4
      - Result passage disposed without unit P3-S1-C5
      - Result passage disposed without unit P3-S1-C8
      - Result passage disposed without unit P3-S2-C3
      - Result passage disposed without unit P4-S1-C3
      - Result passage disposed without unit P4-S1-C8
      - Accounting without a linked unit P5-S1-C11
      - Result passage disposed without unit P5-S1-C3
      - Result passage disposed without unit P5-S1-C4
      - Accounting without a linked unit P5-S1-C9
      unattached_null_or_qualifier_ids: []
      suppressed_nonrepresented_units: 6
      default_disposition_count_requires_completeness_check: 68
      unselected_timing_passages: []
      personal_effect_slots_without_result_classification: []
      held_frame_selections: []
      empty_frame_slots_require_confirmation:
      - eligibility
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
        - P2-S1
        - P2-S2
        - P3-S1
        - P3-S2
        - P4-S1
        - P4-S2
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 7cb83fb698c86998f64457686ec810430c9012dffb91fbe19caac8c85064a92e
      source_review: _compare/relationships-2026-11-16/review-current/MirmanThye2018
      source_status_sha256: d3ac1ad6ff5f5a1d3cf67f099386147ed2da468f86834f4ffa3597c0b5b6691a
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: General summary of identified systems without specific lesion-outcome
        associations.
    - source_id: P1-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: General summary of neural basis for systems.
    - source_id: P1-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about inconsistency of executive function localization.
    - source_id: P2-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement that four systems were identified.
    - source_id: P2-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive statement about tasks drawing on multiple systems.
    - source_id: P2-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement about convergence across laboratories.
    - source_id: P3-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive statement about differentiation between articulation and
        recognition.
    - source_id: P3-S1-C4
      disposition: represented
      result_indexes:
      - 0
      reason: Directly establishes association between dorsal pathway damage and phonological-production
        deficits.
    - source_id: P3-S1-C5
      disposition: represented
      result_indexes:
      - 1
      reason: Directly establishes association between ventral pathway damage and
        phonological-recognition deficits.
    - source_id: P3-S1-C8
      disposition: represented
      result_indexes:
      - 2
      reason: Directly establishes association between superior temporal sulcus damage
        and general phonological factor.
    - source_id: P3-S2-C3
      disposition: represented
      result_indexes:
      - 3
      reason: Directly establishes association between anterior temporal lobe damage
        and semantic system deficits.
    - source_id: P4-S1-C3
      disposition: represented
      result_indexes:
      - 4
      reason: Directly establishes association between white-matter pathway damage
        and semantic deficits.
    - source_id: P4-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about white-matter bottlenecks.
    - source_id: P4-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Definition of the fluency system.
    - source_id: P4-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of the fluency system's function.
    - source_id: P4-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of symptoms of sentence-level planning deficits.
    - source_id: P4-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of symptoms of sentence-level planning deficits.
    - source_id: P4-S2-C4
      disposition: represented
      result_indexes:
      - 7
      reason: Establishes null/weak association between sentence-level planning system
        and sentence-comprehension deficits.
    - source_id: P4-S2-C5
      disposition: represented
      result_indexes:
      - 5
      reason: Directly establishes association between insula/frontal/precentral damage
        and fluency deficits.
    - source_id: P5-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion about core systems.
    - source_id: P5-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: General summary of phonological system.
    - source_id: P5-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: General summary of semantic system.
    - source_id: P5-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: General summary of fluency deficits.
    - source_id: P5-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement about constructs that did not emerge.
    - source_id: P5-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement about the lexicon.
    - source_id: P5-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement about syntax.
    unresolved_coverage: []
    pending_source_ids:
    - P1-S2-C4
    - P1-S2-C5
    - P1-S2-C6
    - P2-S1-C3
    - P2-S1-C5
    - P2-S1-C9
    - P3-S1-C2
    - P4-S1-C4
    - P4-S1-C6
    - P4-S1-C8
    - P4-S2-C2
    - P4-S2-C3
    - P5-S1-C2
    - P5-S1-C3
    - P5-S1-C4
    - P5-S1-C5
    - P5-S1-C8
    - P5-S1-C9
    - P5-S1-C11
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
      - P2-S1-C9
      recruited_sample:
      - P2-S1-C9
      eligibility: []
      imaging_provenance:
      - P1-S1-C4
      imaging_timing:
      - P1-S1-C4
      outcome_timing:
      - P1-S1-C4
      outcome_definition:
      - P1-S1-C5
      - P2-S1-C8
      validation: []
      analysis_restrictions: []
      dependent_variable_statement:
      - P1-S1-C5
      - P2-S1-C8
      limitations:
      - P5-S2-C4
      - P5-S2-C5
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles: []
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P2-S1-C9
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: not_stated
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
      pdf_sha256: 7cb83fb698c86998f64457686ec810430c9012dffb91fbe19caac8c85064a92e
      review_sha256: b06066d2600487f24589f3cda5312d3cfcf3764f0baf720eae279368773f95a8
      code_sha256: c4650d24fa3e36e6f317cb65cc7626277a28936a7cdf5d07248d4b1e5bfa09aa
      source_helpers_sha256: e0e0f295e5efa1fdb4e9e8c84ca491d062df3aefe8ca8b4d9ca85fcb6d4c9082
      converter_sha256: 048f1e35905528676837a00b1b2406b1c97cb1eb47c48d63f121a5c00cc0afeb
      table_helpers_sha256: 78e562e9725fc484d6a12279ea710856dfd1d9aa13ee178d0358e9c0acdd2c8c
      mapper_budget: 2500
      reviewer_budget: 1600
      approved: false
      visual:
        models:
        - gemma4:31b
        - qwen3.8:27b
        digests:
        - 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        - 47951e4a666180bc2aedfc93c169472f2de783696fe196efbf063f5730ecf163
        code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
        layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
    approved: false
    core_review:
      own_result_source_ids:
      - P3-S1-C4
      source_result: The source states that deficits in the phonological-production
        subsystem are associated with damage in a dorsal pathway primarily involving
        inferior parietal and frontal regions. This is presented as a finding from
        data-driven lesion-symptom mapping studies involving individuals with aphasia.
      result_status: detected
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis corresponds to the specific association described
            in P3-S1-C4 regarding the phonological-production subsystem and the dorsal
            pathway. The method is identified as lesion-symptom mapping (LSM), which
            is consistent with the source description of using brain scans to localize
            damage relative to deficits.
          source_ids:
          - P3-S1-C4
          - P1-S1-C4
        direction:
          answer: fits
          reason: The source explicitly states an association between deficits in
            the phonological-production subsystem and damage in the dorsal pathway.
            The draft preserves this directionality (association/detected effect)
            without inverting it or claiming a null result.
          source_ids:
          - P3-S1-C4
        construct:
          answer: fits
          reason: The exposure (damage in dorsal pathway involving inferior parietal
            and frontal regions) and outcome (phonological-production subsystem deficits)
            are accurately transcribed from P3-S1-C4. The patient measurement is correctly
            identified as template_lesion_overlap, as the source describes lesion-symptom
            mapping where individual lesions are overlaid on reference maps to test
            for associations with deficits, rather than patient-specific diffusion
            tractography.
          source_ids:
          - P3-S1-C4
          - P1-S1-C5
        qualifications:
          answer: fits
          reason: The draft includes the qualification that the finding is a synthesis
            of results from four independent research groups using a data-driven approach.
            This aligns with P2-S1-C3 and P2-S1-C9, which describe the convergence
            of these studies. The draft does not incorrectly attribute the finding
            to a single study or omit the context of the data-driven synthesis.
          source_ids:
          - P2-S1-C3
          - P2-S1-C9
          - P3-S1-C4
        missing_material_caveat:
          answer: fits
          reason: The draft captures the essential context of the finding as a synthesis.
            While specific statistical thresholds or sample sizes are not transcribed
            (marked as not_transcribed), this is acceptable for a qualitative draft.
            No material caveat that would change the interpretation of the association
            (e.g., a contradictory null result or a specific limitation that negates
            the finding) is omitted from the provided source window.
          source_ids:
          - P3-S1-C4
          - P5-S2-C5
      optional_pending:
      - Specific statistical thresholds or p-values for the association
      - Exact sample sizes for the four research groups
      - Specific MRI resolution or atlas used for the lesion overlap
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Specific statistical thresholds or p-values for the association
    - Exact sample sizes for the four research groups
    - Specific MRI resolution or atlas used for the lesion overlap
    normalizations: []
    analysis_identity:
      id: R001
      exposure:
        text: damage in a dorsal pathway primarily involving inferior parietal and
          frontal regions
      outcome:
        text: phonological-production subsystem deficits
      analysis_label: lesion-symptom mapping
      relation: association
      evidence_ids:
      - P3-S1-C4
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
        pdf_sha256: 7cb83fb698c86998f64457686ec810430c9012dffb91fbe19caac8c85064a92e
        source_review: _compare/relationships-2026-11-16/review-current/MirmanThye2018
        source_status_sha256: d3ac1ad6ff5f5a1d3cf67f099386147ed2da468f86834f4ffa3597c0b5b6691a
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings: {}
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 3
  quote: "Deficits in the phonological-production subsystem \nare associated with\
    \ damage in a dorsal pathway primar-\nily involving inferior parietal and frontal\
    \ regions (Fig. \n2a, darker green)."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-25'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
