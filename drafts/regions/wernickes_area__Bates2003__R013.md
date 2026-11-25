---
id: wernickes_area
name: Wernicke's area cluster
kind: network
findings:
- id: f1
  target_audit:
    status: behaviour_label_present
    category: behaviour_or_language_construct
    original_target: auditory_comprehension
    reason: Label names a behaviour or language construct; its exact operational definition and measurement
      still need source review.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  outcome_measurement:
    status: needs_source_review
    instruments: []
    note: Outcome instrument/task is not yet verified for this finding. Do not infer it from the predictor
      or a paper-wide test list.
  target: auditory_comprehension
  target_kind: impairment
  claim: The contribution of Wernicke's area to auditory comprehension was no longer
    apparent after the middle temporal gyrus was factored out.
  direction: no_effect
  relationship: correlational
  method: VLSM
  sample:
    n: 101
    population: left-hemisphere-injured stroke patients with some degree of speech
      or language impairment
    phase: not_reported
    time_post_onset: at least one year after stroke
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Structural MRI limitations for white-matter labels
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Patient lesion overlap with a predefined ROI for Wernicke''s
    area. Analysis performed using ANCOVA to factor out the effect of the middle temporal
    gyrus. Additional metadata has not been transcribed; review the pending-field
    flags before approval. PDF image reading (P2-S1-C11, two-model agreement, human
    verification pending): We analyzed data on speech fluency and language comprehension
    for 101 left-hemisphere-injured stroke patients who showed some degree of speech
    or language impairment Original text-layer quotation is preserved below.'
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
    - proposed_concept:auditory_comprehension
  citation: '@Bates2003'
  source_passages:
  - section: Original source P3-S1-C7
    page: 3
    quote: 'The MTG remained a significant factor

      in auditory comprehension after Wernicke’s area was factored out

      (Fig. 2c), but after the MTG was factored out, the contribution

      of Wernicke’s area was no longer apparent (Fig. 2d).'
    supports: claim
  - section: Original source P3-S1-C5
    page: 3
    quote: 'We constructed four maps factoring out

      the effects of these voxels by carrying out analyses of covariance

      (ANCOVAs) at all other voxels using the state (intact or lesioned)

      of each voxel of interest as the covariates (Fig. 2).'
    supports: method
  - section: Original source P3-S1-C4
    page: 3
    quote: 'Based

      on anatomical criteria, we identified central voxels in four a priori

      ROIs: Broca’s area, the anterior insula, Wernicke’s area and the

      middle temporal gyrus.'
    supports: method
  - section: Original source P2-S1-C11
    page: 2
    quote: 'We analyzed data on speech fluency and language comprehen-

      sion for 101 left-hemisphere-injured stroke patients who showed

      some degree of speech or language impairment.'
    supports: sample
  - section: Original source P2-S2-C6
    page: 2
    quote: 'Patients were tested

      at least one year after stroke.'
    supports: sample
  - section: Original source P2-S1-C13
    page: 2
    quote: 'For this reason, we focused on

      the fluency and auditory comprehension subtests of a standard

      assessment tool, the Western Aphasia Battery (WAB)6.'
    supports: method
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-20'
relationship_review:
  paper: Bates2003
  proposal_id: R013
  review_status_sha256: 122eb2239d758cf4fd30a7b0161cd5230c041b310b08b626103af44fcc986ef7
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: ad741c4c3a6e952e4b8f7e42179c0d026428ac91e5f90ef9b8a348743ec7a8ef
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: ad741c4c3a6e952e4b8f7e42179c0d026428ac91e5f90ef9b8a348743ec7a8ef
        A/passages.json: 6b2ece4606b66019fabff662dd0d4bc85eba2c4d0cd0f0b23dc8c492d7b8c9fb
        A/raw.json: 8b4489d11f7fb5ebc4086e7260948584998d3a708359f6075d45a39b6fb69995
        A/source-units.json: 0879b514d61e95db610558f3a024e5ba63483e7246ac96b1649fd2cb3e2f1ed1
        A/full-source-units.json: 0879b514d61e95db610558f3a024e5ba63483e7246ac96b1649fd2cb3e2f1ed1
        A/meta.json: 7b94e1397a416dee7c0d59b3be88fd1294a7b604feb9a9f0f465052392a6429d
        A/table-images/manifest.json: 88c757d75eae33ca07a70cf3b3ea2c3c2c6a0e573c13f02b65b53e8e8771aaf0
        A/clauses/window-03/raw.json: 3fccdb792e56eb920d5672c98879ad0bb40b703d1ddfa7d0caa298bd78d97192
        A/clauses/window-03/prompt.txt: e507cd87a46dd4c8b7971062d6dce38face286acdabb67a38ecd06f35227f021
        A/clauses/window-03/meta.json: 650e91532191d84d889f1949eb901dbc2b7e2dff5664f95ccffb0b095a80ba8c
        A/clauses/window-04/raw.json: ff7c49bd0efeb773fd7f80398a4a400828e385de0153ec4173c0b24a564f57d5
        A/clauses/window-04/prompt.txt: 03fb49b08d4040036fd796a82d320085f969d2c9c2f212cb23647d03fbfdad5f
        A/clauses/window-04/meta.json: 3d1918981de39aa0547a9f26d068edc1a83af564ece6cd4ef247233c84a852e5
        A/clauses/window-05/raw.json: 1f5e99ee2eafc38d064061468744a15c38d7bb73259e70497c274f4f32ab0f74
        A/clauses/window-05/prompt.txt: 835373ce643f35fa068f1356d2bf6c0b8a7a8b35e7a97ca89124a7dd577820c9
        A/clauses/window-05/meta.json: 3e1e499080930bb214981f58000d58bccf5b69657e6ba116b9f040ff1483e0f0
        A/clauses/window-02/raw.json: 1bf2456c80e236c5263ce1a3b1bb36a5f8a9fc2255440f82ad13b1a1f38ca7fa
        A/clauses/window-02/prompt.txt: 8b9b6206cd406aa41d42cd3fcbac253cc57a897c0a058ab44acf4d8ea8590c75
        A/clauses/window-02/meta.json: 284fad56143a196bf3adc03fd0c1e36ddbbc61b56a383a1b5a364c4e9133afa1
        A/clauses/window-01/raw.json: 1b1880b6e1da2e90cf5cd9bad62aa6dec51e0e50901703b970c11416f9d08c81
        A/clauses/window-01/prompt.txt: 274a6d3b200b7cdca25519620014b14891b8872767fd6f03d5791b73e5c968b5
        A/clauses/window-01/meta.json: fdf05caf4b26f9b378a1582ccb0da117f0c64b2cffdf50ea565eea21b09bc338
        A/clauses/window-06/raw.json: 1a87546c3f20eb7483b21a9e30583b25807800031d1770df68b1082924fe474b
        A/clauses/window-06/prompt.txt: f612f2015ba3223be9c688eca98aca618b841774a288a5239670613a9ee7d296
        A/clauses/window-06/meta.json: 57e16995dea1837f0837bf9f142f9bc3f867d79e0abab1263f5bb5d572d3108c
        B/passages.json: 6b2ece4606b66019fabff662dd0d4bc85eba2c4d0cd0f0b23dc8c492d7b8c9fb
        B/raw.json: ffd5046d6ffca150bf78afdd83eebb68787d32db036d2016a6abc484f7b4cba0
        B/source-units.json: 0879b514d61e95db610558f3a024e5ba63483e7246ac96b1649fd2cb3e2f1ed1
        B/full-source-units.json: 0879b514d61e95db610558f3a024e5ba63483e7246ac96b1649fd2cb3e2f1ed1
        B/meta.json: 2776f470266f4ac63133670f228f9230284c13764c8c864615c415e6a079611c
        B/table-images/manifest.json: 88c757d75eae33ca07a70cf3b3ea2c3c2c6a0e573c13f02b65b53e8e8771aaf0
        B/clauses/window-03/raw.json: 6446088155ad765895caf2d48151538b123f325634bd4514bf507d4c1bd6ec4c
        B/clauses/window-03/prompt.txt: e507cd87a46dd4c8b7971062d6dce38face286acdabb67a38ecd06f35227f021
        B/clauses/window-03/meta.json: 162a4f4847e52d8eefdc039365ef5f6664a3aa8700956e32ac5063919cbc221b
        B/clauses/window-04/raw.json: 627e9c81f2697ad2a04f9f4c236fb9667c94e48348a6762c398205bb7e3507a3
        B/clauses/window-04/prompt.txt: 03fb49b08d4040036fd796a82d320085f969d2c9c2f212cb23647d03fbfdad5f
        B/clauses/window-04/meta.json: 07927e407a434fc67efeafb96888f3a2135df18814366e88ee5372553b56bf1d
        B/clauses/window-05/raw.json: c29d8b2c90c5803365643d6495d10695e85968ea15cd357c3ca127b8a7846b11
        B/clauses/window-05/prompt.txt: 835373ce643f35fa068f1356d2bf6c0b8a7a8b35e7a97ca89124a7dd577820c9
        B/clauses/window-05/meta.json: 8324cb45f17aa6614e9db2bfc3ba2ed22543c33e11c798c57c928fa5f8aff8d6
        B/clauses/window-02/raw.json: 9a1609a32c78f7e6b819bea3196bdc3bd627f301207f2952c5d1c9779d9b0399
        B/clauses/window-02/prompt.txt: 8b9b6206cd406aa41d42cd3fcbac253cc57a897c0a058ab44acf4d8ea8590c75
        B/clauses/window-02/meta.json: 8511c73379e739892de7855ab981c76582cf9e87d58a2a25a03b339ed78d1e21
        B/clauses/window-01/raw.json: fb559069b0a2c3036df18eec5269eab15d91b9bc4c69692bac3e123512046a7c
        B/clauses/window-01/prompt.txt: 274a6d3b200b7cdca25519620014b14891b8872767fd6f03d5791b73e5c968b5
        B/clauses/window-01/meta.json: 73eceba577170da6059d4a412ee93da78ef00cc78cc2759f3ac2ce52cb445d84
        B/clauses/window-06/raw.json: 162d049db2adcd3f5eca7e2313b9a4e3dca641862538897b738a6002920ebdcf
        B/clauses/window-06/prompt.txt: f612f2015ba3223be9c688eca98aca618b841774a288a5239670613a9ee7d296
        B/clauses/window-06/meta.json: 97abbdac13ef3ff0d0ef4bb900c02be7115e3bfba45ce7603d3e2171fc826edc
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
      pdf_sha256: ad741c4c3a6e952e4b8f7e42179c0d026428ac91e5f90ef9b8a348743ec7a8ef
      source_review: _compare/relationships-2026-11-16/review-current/Bates2003
      source_status_sha256: f8eb707439102f6f3860d9e5ef9775333b899952c7645dc3259e9b9c7399557a
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R013
    exposure:
      text: lesions in Wernicke's area
    outcome:
      text: auditory comprehension
    analysis_label: ANCOVA for auditory comprehension (factoring out MTG)
    relation: sensitivity
    evidence_ids:
    - P3-S1-C7
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
      pdf_sha256: ad741c4c3a6e952e4b8f7e42179c0d026428ac91e5f90ef9b8a348743ec7a8ef
      source_review: _compare/relationships-2026-11-16/review-current/Bates2003
      source_status_sha256: f8eb707439102f6f3860d9e5ef9775333b899952c7645dc3259e9b9c7399557a
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P1-S1-C1
      - Result passage disposed without unit P1-S1-C10
      - Result passage disposed without unit P1-S1-C6
      - Result passage disposed without unit P1-S1-C7
      - Accounting without a linked unit P1-S1-C8
      - Accounting without a linked unit P1-S1-C9
      - Unaccounted source passage P1-S1-C8
      - Unaccounted source passage P1-S1-C9
      - Result passage disposed without unit P1-S1-C13
      - Result passage disposed without unit P1-S1-C14
      - Result passage disposed without unit P1-S1-C16
      - Accounting without a linked unit P2-S2-C10
      - Accounting without a linked unit P2-S2-C11
      - Result passage disposed without unit P2-S2-C12
      - Result passage disposed without unit P2-S2-C14
      - Accounting without a linked unit P2-S3-C2
      - Unaccounted source passage P2-S3-C2
      - Unaccounted source passage P2-S2-C10
      - Unaccounted source passage P2-S2-C11
      - Result passage disposed without unit P2-S3-C3
      - Accounting without a linked unit P3-S1-C6
      - Accounting without a linked unit P3-S1-C7
      - Unaccounted source passage P3-S1-C7
      - Unaccounted source passage P3-S1-C6
      - Result passage disposed without unit P3-S1-C11
      unattached_null_or_qualifier_ids:
      - P1-S2-C2
      - P3-S1-C7
      suppressed_nonrepresented_units: 6
      default_disposition_count_requires_completeness_check: 82
      unselected_timing_passages: []
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P2-S2-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P2-S2-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P3-S1-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P2-S2-C5
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      empty_frame_slots_require_confirmation:
      - validation
      - limitations
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
        - P1-S2
        - P2-S2
        - P2-S3
        - P3-S1
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: ad741c4c3a6e952e4b8f7e42179c0d026428ac91e5f90ef9b8a348743ec7a8ef
      source_review: _compare/relationships-2026-11-16/review-current/Bates2003
      source_status_sha256: f8eb707439102f6f3860d9e5ef9775333b899952c7645dc3259e9b9c7399557a
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes general feature of experiments.
    - source_id: P1-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Interpretive implication of OHC deformation.
    - source_id: P1-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Null finding regarding structural changes (not a specific clinical outcome
        relationship).
    - source_id: P1-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Null finding regarding microphonics.
    - source_id: P1-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about sensitivity to manipulations.
    - source_id: P1-S1-C8
      disposition: represented
      result_indexes:
      - 1
      reason: Establishes effect of overstimulation on reticular lamina.
    - source_id: P1-S1-C9
      disposition: represented
      result_indexes:
      - 2
      reason: Establishes effect of overstimulation on basilar membrane.
    - source_id: P1-S1-C10
      disposition: represented
      result_indexes:
      - 3
      reason: Establishes effect of overstimulation on OHCs.
    - source_id: P1-S1-C13
      disposition: represented
      result_indexes:
      - 4
      reason: Establishes effect of drug on OHC deformation.
    - source_id: P1-S1-C14
      disposition: represented
      result_indexes:
      - 5
      - 6
      reason: Establishes effect of drug on reticular lamina and basilar membrane.
    - source_id: P1-S1-C16
      disposition: represented
      result_indexes:
      - 0
      reason: Summary finding of sound stimulation causing OHC deformation.
    - source_id: P1-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of dynamic model confirmation.
    - source_id: P2-S2-C10
      disposition: represented
      result_indexes:
      - 7
      reason: Identifies brain regions associated with fluency deficits.
    - source_id: P2-S2-C11
      disposition: represented
      result_indexes:
      - 8
      reason: Identifies brain regions associated with comprehension deficits.
    - source_id: P2-S2-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of effect size maps.
    - source_id: P2-S2-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison with traditional Broca/Wernicke areas.
    - source_id: P2-S3-C2
      disposition: repeated
      result_indexes:
      - 7
      - 8
      reason: Restatement of high t-score regions.
    - source_id: P2-S3-C3
      disposition: repeated
      result_indexes:
      - 7
      reason: Restatement of white matter role in fluency.
    - source_id: P2-S3-C11
      disposition: represented
      result_indexes:
      - 7
      - 8
      reason: Restatement of most impactful lesions for fluency and comprehension.
    - source_id: P3-S1-C6
      disposition: represented
      result_indexes:
      - 9
      - 10
      reason: Results of ANCOVAs for fluency.
    - source_id: P3-S1-C7
      disposition: represented
      result_indexes:
      - 11
      - 12
      reason: Results of ANCOVAs for comprehension.
    - source_id: P3-S1-C9
      disposition: represented
      result_indexes:
      - 13
      reason: Correlation between fluency and comprehension maps.
    - source_id: P3-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: General observation about peri-Sylvian lesions.
    - source_id: P3-S3-C26
      disposition: background_or_descriptive
      result_indexes: []
      reason: Finding from a different study (Mayr et al.) on conflict-adaptation.
    unresolved_coverage:
    - source_id: P1-S3-C21
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C1
    - P1-S1-C2
    - P1-S1-C4
    - P1-S1-C6
    - P1-S1-C7
    - P1-S2-C2
    - P1-S3-C21
    - P2-S2-C12
    - P2-S2-C14
    - P2-S3-C2
    - P2-S3-C3
    - P3-S1-C11
    - P3-S3-C26
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
      - P2-S1-C11
      recruited_sample:
      - P2-S1-C11
      eligibility:
      - P2-S2-C6
      - P2-S2-C7
      imaging_provenance:
      - P2-S1-C3
      - P2-S1-C4
      - P2-S2-C4
      - P2-S2-C5
      imaging_timing:
      - P2-S2-C6
      outcome_timing:
      - P2-S2-C6
      outcome_definition:
      - P2-S1-C13
      - P2-S2-C3
      - P2-S2-C13
      validation: []
      analysis_restrictions:
      - P2-S3-C13
      - P2-S3-C15
      - P2-S3-C16
      - P2-S3-C4
      - P2-S3-C5
      - P2-S3-C6
      - P3-S1-C5
      dependent_variable_statement:
      - P2-S1-C13
      - P2-S2-C9
      limitations: []
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P2-S3-C13
      - P2-S3-C15
      - P2-S3-C16
      - P3-S1-C5
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P2-S2-C7
    outcome_type: status_at_assessment
    imaging_vs_outcome: precedes_outcome
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P2-S2-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P2-S2-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P3-S1-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P2-S2-C5
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
      pdf_sha256: ad741c4c3a6e952e4b8f7e42179c0d026428ac91e5f90ef9b8a348743ec7a8ef
      review_sha256: 122eb2239d758cf4fd30a7b0161cd5230c041b310b08b626103af44fcc986ef7
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
      - P3-S1-C7
      source_result: In an ANCOVA analysis factoring out the middle temporal gyrus
        (MTG), the contribution of Wernicke's area to auditory comprehension was no
        longer apparent, whereas the MTG remained a significant factor when Wernicke's
        area was factored out.
      result_status: lost_after_adjustment
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis corresponds to the ANCOVA described in P3-S1-C7,
            which specifically tests the contribution of Wernicke's area after factoring
            out the MTG. This is distinct from the unadjusted VLSM or the reverse
            ANCOVA (factoring out Wernicke's area).
          source_ids:
          - P3-S1-C7
          - P3-S1-C5
        direction:
          answer: fits
          reason: The source states that 'the contribution of Wernicke's area was
            no longer apparent' after the MTG was factored out. This represents a
            loss of significance (adjusted null) for Wernicke's area in this specific
            model, which aligns with the 'no_effect' direction in the draft (interpreted
            as no detected association in the adjusted model).
          source_ids:
          - P3-S1-C7
        construct:
          answer: fits
          reason: The exposure is lesions in Wernicke's area (defined as a priori
            ROI in P3-S1-C4), the outcome is auditory comprehension (measured by WAB
            in P2-S1-C13), and the method is VLSM/ANCOVA. The patient measurement
            is correctly identified as template_lesion_overlap (lesions reconstructed
            onto templates in P2-S2-C4 and analyzed voxel-by-voxel in P1-S3-C20).
          source_ids:
          - P3-S1-C4
          - P2-S1-C13
          - P2-S2-C4
          - P1-S3-C20
        qualifications:
          answer: fits
          reason: The draft correctly includes the qualification that the analysis
            factored out the MTG. It correctly identifies this as a sensitivity analysis
            within the VLSM framework. The limitation regarding white-matter labels
            is a general limitation of the VLSM method mentioned in the paper (P2-S3-C3),
            though the specific result here concerns cortical ROIs.
          source_ids:
          - P3-S1-C7
          - P3-S1-C5
        missing_material_caveat:
          answer: fits
          reason: The draft captures the essential caveat that the null result is
            conditional on the MTG being factored out. It does not omit the fact that
            this is an adjusted result. The source P3-S1-C7 explicitly contrasts this
            with the MTG remaining significant, which supports the interpretation
            that the Wernicke's area effect is not independent of the MTG.
          source_ids:
          - P3-S1-C7
      optional_pending:
      - Specific statistical values (t-scores, p-values) for the ANCOVA results are
        not transcribed in the provided source window.
      - Exact anatomical coordinates or volume of the Wernicke's area ROI are not
        transcribed.
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Specific statistical values (t-scores, p-values) for the ANCOVA results are
      not transcribed in the provided source window.
    - Exact anatomical coordinates or volume of the Wernicke's area ROI are not transcribed.
    normalizations: []
    analysis_identity:
      id: R013
      exposure:
        text: lesions in Wernicke's area
      outcome:
        text: auditory comprehension
      analysis_label: ANCOVA for auditory comprehension (factoring out MTG)
      relation: sensitivity
      evidence_ids:
      - P3-S1-C7
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
        pdf_sha256: ad741c4c3a6e952e4b8f7e42179c0d026428ac91e5f90ef9b8a348743ec7a8ef
        source_review: _compare/relationships-2026-11-16/review-current/Bates2003
        source_status_sha256: f8eb707439102f6f3860d9e5ef9775333b899952c7645dc3259e9b9c7399557a
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P2-S1-C11:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: ad741c4c3a6e952e4b8f7e42179c0d026428ac91e5f90ef9b8a348743ec7a8ef
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: ca8d26393c134b7cfe3652914629c70e87de72c3a14f51e08d20a53c1b6bb508
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S1-C11
          page: 2
          text_layer_sha256: ca8d26393c134b7cfe3652914629c70e87de72c3a14f51e08d20a53c1b6bb508
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'We analyzed data on speech fluency and language comprehen-

          sion for 101 left-hemisphere-injured stroke patients who showed

          some degree of speech or language impairment.'
        anchor_text: 'We analyzed data on speech fluency and language comprehen-

          sion for 101 left-hemisphere-injured stroke patients who showed

          some degree of speech or language impairment.'
        excluded_fragments: []
        image_sha256: 2ea8fd07b1e41e932da5e75ee3a458051ec5fce1fc6fc6f2776d9a1e6427032d
        transcription: We analyzed data on speech fluency and language comprehension
          for 101 left-hemisphere-injured stroke patients who showed some degree of
          speech or language impairment
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 3
  quote: 'The MTG remained a significant factor

    in auditory comprehension after Wernicke’s area was factored out

    (Fig. 2c), but after the MTG was factored out, the contribution

    of Wernicke’s area was no longer apparent (Fig. 2d).'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-20'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
