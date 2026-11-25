---
id: frontal_isthmus_periventricular_wm_cluster
name: frontal isthmus and anterior periventricular white matter cluster
kind: network
findings:
- id: f1
  target_audit:
    status: behaviour_label_present
    category: behaviour_or_language_construct
    original_target: non_fluent_verbal_output
    reason: Label names a behaviour or language construct; its exact operational definition and measurement
      still need source review.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  outcome_measurement:
    status: needs_source_review
    instruments: []
    note: Outcome instrument/task is not yet verified for this finding. Do not infer it from the predictor
      or a paper-wide test list.
  target: non_fluent_verbal_output
  target_kind: impairment
  claim: Lesions extending into the deep white matter of the frontal isthmus and anterior
    periventricular white matter resulted in more severe and prolonged non-fluent
    verbal output compared to shallow lesions of the frontal operculum.
  direction: likely
  relationship: correlational
  method: LSM
  sample:
    n: not_reported
    population: individuals with aphasia following stroke
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
  - finding is reported within a narrative review synthesis of prior work (Alexander
    et al.)
  evidence_quality: narrative-review
  strength: weak
  notes: 'Exposure measurement: Patient lesion overlap with the deep white matter
    of the frontal isthmus and anterior periventricular white matter. contrasted with
    shallow lesions of the frontal operculum which resulted in transient disorders.
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
    - proposed_concept:non_fluent_verbal_output
  citation: '@Plowman2012'
  source_passages:
  - section: Original source P4-S1-C11
    page: 4
    quote: 'While shallow lesions of the frontal oper-

      culum resulted in transient disorders of language output with

      normal articulation and repetition, lesions that extended into the

      deep white matter of the frontal isthmus and anterior periventricu-

      lar white matter resulted in more severe and prolonged non-ﬂuent

      '
    supports: claim
  - section: Original source P4-S2-C1
    page: 4
    quote: 'normal articulation and repetition, lesions that extended into the

      deep white matter of the frontal isthmus and anterior periventricu-

      lar white matter resulted in more severe and prolonged non-ﬂuent

      verbal output.'
    supports: claim
  - section: Original source P2-S1-C6
    page: 2
    quote: 'Research design and methods

      For this review, we considered all studies that recruited patients

      with a diagnosis of aphasia following stroke and reported stan-

      dardized measures designed to predict aphasia outcomes.'
    supports: sample
  - section: Original source P2-S2-C5
    page: 2
    quote: 'Instead, the presentation of results provides a qualitative assess-

      ment of the studies.'
    supports: method
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-25'
relationship_review:
  paper: Plowman2012
  proposal_id: R017
  review_status_sha256: c89504ffcf33add92b2797f423ef92b6b5661c51290ed24470391997daef7a1d
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: ef0aaf55a3919bf3928bc764f9271e407b8176b38f51ed6574cbb892431360d2
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: ef0aaf55a3919bf3928bc764f9271e407b8176b38f51ed6574cbb892431360d2
        A/passages.json: c9039af878d326f615adec2b8cb2c4c296d5aa544151a577a7da0454b0f71d9a
        A/raw.json: e7b74149863117bb66b0e644db9c107b1fffef114ae30ad8a77f687a509dbac0
        A/source-units.json: 418f68b878b82357924fb15211e7d0f69400f6c6d62d25b0b48c7add2fe06d29
        A/full-source-units.json: 8ec24a7a33018d850da07345998e72579a2dbeeec5754b209a9c59e66c4478e0
        A/meta.json: b0971e9c251c149ac0ce1ccac2a5e3257fcb686088d7588a299348f9892212dc
        A/table-images/page-4.png: 406f6ab9ba756ae1318d4e5049d0fe96b942f9b4e01645a2d0e1afc50a875133
        A/table-images/TABLE-1-page-4-1.png: db266073443156cb16228f19d44e974d8a7ecf42c1311faffd2e9915f97d5485
        A/table-images/manifest.json: ef58da6cfe204cee9fda3ad236f2d6a611538ebf3d1c49b842884751b973e66e
        A/clauses/window-03/raw.json: 881984ba35163b3e85a4a40adb6e50277f26398119dbacd957ddf534097654c9
        A/clauses/window-03/prompt.txt: 5146951c266f08b1a92751edc7ac828d976d88173e30f01d6153194cb9fb71e6
        A/clauses/window-03/meta.json: 68d611444c2b2b26d110a4fe3854f784862de8d13e0f9644a61d747a81bfeb41
        A/clauses/window-04/raw.json: 2eb18e112a2bba8cd3fd2abece5616338035605d5523803c5f0bae3b38afeb42
        A/clauses/window-04/prompt.txt: 4cd7c741a0e62106f0ecfca9695d6fddacb9737ac635879f2dd0832504a5e003
        A/clauses/window-04/meta.json: 381929025b17f982c67bd61e577aa745222272c1624706dadd1402cba5b6adef
        A/clauses/window-05/raw.json: 9fb132083e45436ecba711857901e7252a95af52d167b018a09610e7ee567b60
        A/clauses/window-05/prompt.txt: f3885f098cdce514f183070df178af030997066089172b549af3f33eed0e157f
        A/clauses/window-05/meta.json: 8670c7fc21cd0c76f9d5016c4974520eab6a01131f181f860ca106abf5f5678f
        A/clauses/window-02/raw.json: f9baacb824ad3ba1b8428d3f19c238c62e3163a8b2bcafdf97519f93de29c9c7
        A/clauses/window-02/prompt.txt: 8844919f33ac7c8bdf3452b30e5d93223cc46ad7560a2a4731553f73497ef975
        A/clauses/window-02/meta.json: c5e92d8dad22896acd4ee388649aba98ea8586235c5a5a41c5afebaecf7c5f97
        A/clauses/window-01/raw.json: cbdc2990982cdd6a2288293f72c8faa686a702d6763af5d2c7930f08921b7df3
        A/clauses/window-01/prompt.txt: c278e31d37dc858665f40242ed822e2145115549d7008094647dff98564ef78d
        A/clauses/window-01/meta.json: 6af568a14fc6b185fa7aee2556470947f89aa8e84c81af0cdf66ebbeee70fdda
        A/tables/TABLE-1-page-4-1/raw.json: 484e84c64e0e2d8e3df84ec0cfc49da8bbe9538f147c9930b16a11cea19d56bb
        A/tables/TABLE-1-page-4-1/prompt.txt: 282f06efaa2a3d49e438c68c8f8dcebb3ee8cb2ea334c782a10d299251872851
        A/tables/TABLE-1-page-4-1/meta.json: 6bd32d61ddd066298d217730873a7e667e1f23d5ea612ae0c07186c1e8896d91
        B/passages.json: c9039af878d326f615adec2b8cb2c4c296d5aa544151a577a7da0454b0f71d9a
        B/raw.json: c82b372d180dc036453d719b3ea097b446655426075981719a108b9236108949
        B/source-units.json: 418f68b878b82357924fb15211e7d0f69400f6c6d62d25b0b48c7add2fe06d29
        B/full-source-units.json: 8ec24a7a33018d850da07345998e72579a2dbeeec5754b209a9c59e66c4478e0
        B/meta.json: 7624094ce65817ecd0d68bafb7877e5ae94f41afff4f100f4874e57f9518fd84
        B/table-images/page-4.png: 406f6ab9ba756ae1318d4e5049d0fe96b942f9b4e01645a2d0e1afc50a875133
        B/table-images/TABLE-1-page-4-1.png: db266073443156cb16228f19d44e974d8a7ecf42c1311faffd2e9915f97d5485
        B/table-images/manifest.json: 9e47018b40c2f3d1711140cfd7b1c5519db21b6715b3f927b8df6edbaa3ecc54
        B/clauses/window-03/raw.json: b57e5794278301463f2060daddf10f2725699772219a38ff0a86ec7255db8ad5
        B/clauses/window-03/prompt.txt: 5146951c266f08b1a92751edc7ac828d976d88173e30f01d6153194cb9fb71e6
        B/clauses/window-03/meta.json: 4ad18c912b5714d459e453a253047bfd2f7426399ca63e9bd0c7066dbd811e2c
        B/clauses/window-04/raw.json: c697ec05cdbe1ba7feae2ac276e6d33854b4789d3bad64b58091bd32335df2d3
        B/clauses/window-04/prompt.txt: 4cd7c741a0e62106f0ecfca9695d6fddacb9737ac635879f2dd0832504a5e003
        B/clauses/window-04/meta.json: 6b5a5f50e98187e8bf9901330386c383c6add40f20a68e6b98909d46ac26d860
        B/clauses/window-05/raw.json: df3ecaa80e19a9a9bae855d8112da442e520b2c967cf6bf662800bfd9819d36e
        B/clauses/window-05/prompt.txt: f3885f098cdce514f183070df178af030997066089172b549af3f33eed0e157f
        B/clauses/window-05/meta.json: affcbcacf7102e1692e7a45205507e6cb325fc838f258fe7c9666e5b0df39ddc
        B/clauses/window-02/raw.json: a06d72ed398799049385037ebda7880879ce4a499b2e2f82124189a26529f6ab
        B/clauses/window-02/prompt.txt: 8844919f33ac7c8bdf3452b30e5d93223cc46ad7560a2a4731553f73497ef975
        B/clauses/window-02/meta.json: 4730e5f2721bfb7634a4e1ce3359203b45f4a97eddffb50ce936168d88c7aa64
        B/clauses/window-01/raw.json: 7e156c134daa915cb5a6fbc4db6cab7bfe1b27617dfdb23db4c6d16d15816699
        B/clauses/window-01/prompt.txt: c278e31d37dc858665f40242ed822e2145115549d7008094647dff98564ef78d
        B/clauses/window-01/meta.json: e959f4a36f0cef230e7fdcf17d64bc6fc7570ba0918e6e12873fff7b92ec36fe
        B/tables/TABLE-1-page-4-1/raw.json: d03e131256c4d4293e2ea3906f40c43596cd700f1797392506d209acc3d7b57a
        B/tables/TABLE-1-page-4-1/prompt.txt: 282f06efaa2a3d49e438c68c8f8dcebb3ee8cb2ea334c782a10d299251872851
        B/tables/TABLE-1-page-4-1/meta.json: e188a4fa253413acf15322143ace86ca3daba3b2f22f9bcd45c5fa926748162f
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
      pdf_sha256: ef0aaf55a3919bf3928bc764f9271e407b8176b38f51ed6574cbb892431360d2
      source_review: _compare/relationships-2026-11-16/review-current/Plowman2012
      source_status_sha256: caa094a78da1d0d1c5d79de24514910a7cacb76337980659b60aeed0fe6b2b1d
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R017
    exposure:
      text: lesions extending into deep white matter of frontal isthmus and anterior
        periventricular white matter
    outcome:
      text: non-fluent verbal output
    analysis_label: White matter depth and output
    relation: association
    evidence_ids:
    - P4-S1-C11
    - P4-S2-C1
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
      pdf_sha256: ef0aaf55a3919bf3928bc764f9271e407b8176b38f51ed6574cbb892431360d2
      source_review: _compare/relationships-2026-11-16/review-current/Plowman2012
      source_status_sha256: caa094a78da1d0d1c5d79de24514910a7cacb76337980659b60aeed0fe6b2b1d
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P4-S3-C7
      unattached_null_or_qualifier_ids: []
      suppressed_nonrepresented_units: 8
      default_disposition_count_requires_completeness_check: 114
      unselected_timing_passages: []
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: tested_personal_effects
        source_id: P2-S2-C14
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P2-S3-C7
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P3-S1-C2
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P3-S1-C5
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P3-S2-C10
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P3-S2-C12
        reason: No current-result classification; a covariate description is not an
          individual test
      empty_frame_slots_require_confirmation:
      - validation
      - analysis_restrictions
      - limitations
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-4-1
      unlinked_tables:
      - TABLE-1-page-4-1
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units: []
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: ef0aaf55a3919bf3928bc764f9271e407b8176b38f51ed6574cbb892431360d2
      source_review: _compare/relationships-2026-11-16/review-current/Plowman2012
      source_status_sha256: caa094a78da1d0d1c5d79de24514910a7cacb76337980659b60aeed0fe6b2b1d
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C6
      disposition: represented
      result_indexes:
      - 0
      reason: Identifies patient-related factors as potential influential factors.
    - source_id: P1-S1-C7
      disposition: represented
      result_indexes:
      - 2
      reason: States initial severity is most predictive.
    - source_id: P1-S1-C8
      disposition: represented
      result_indexes:
      - 1
      reason: Identifies lesion site and size as influential.
    - source_id: P4-S3-C7
      disposition: represented
      result_indexes:
      - 18
      reason: Links AF fiber change to conversational information unit improvement.
    - source_id: P5-S1-C3
      disposition: represented
      result_indexes:
      - 19
      reason: Summarizes that stroke-related variables influence recovery while patient-related
        ones do not.
    unresolved_coverage: []
    pending_source_ids: []
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-4-1
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P2-S1-C6
      recruited_sample:
      - P2-S1-C6
      eligibility:
      - P2-S1-C6
      imaging_provenance:
      - P4-S3-C5
      imaging_timing:
      - P4-S2-C7
      outcome_timing:
      - P3-S2-C2
      - P3-S3-C5
      - P3-S3-C6
      - P4-S1-C6
      outcome_definition:
      - P2-S1-C12
      - P3-S2-C10
      - P3-S3-C4
      - P4-S2-C5
      validation: []
      analysis_restrictions: []
      dependent_variable_statement:
      - P3-S2-C2
      - P3-S2-C10
      - P3-S3-C4
      - P4-S2-C5
      limitations: []
      personal_factors:
      - P1-S1-C6
      - P1-S3-C3
      - P2-S1-C9
      - P2-S1-C10
      - P3-S1-C5
      - P3-S1-C6
      - P3-S1-C8
      - P4-S4-C1
      tested_personal_effects:
      - P5-S1-C3
      adjustment_roles:
      - P3-S1-C7
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P1-S1-C6
      - P2-S1-C9
      - P2-S1-C10
      - P3-S1-C5
      - P3-S1-C6
      - P3-S1-C8
      - P4-S4-C1
    outcome_type: both_reported
    imaging_vs_outcome: mixed
    validation_type: none_described
    held_selections:
    - slot: tested_personal_effects
      source_id: P2-S2-C14
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P2-S3-C7
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P3-S1-C2
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P3-S1-C5
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P3-S2-C10
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P3-S2-C12
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
      pdf_sha256: ef0aaf55a3919bf3928bc764f9271e407b8176b38f51ed6574cbb892431360d2
      review_sha256: c89504ffcf33add92b2797f423ef92b6b5661c51290ed24470391997daef7a1d
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
      - P4-S1-C11
      - P4-S2-C1
      source_result: The source reports that lesions extending into the deep white
        matter of the frontal isthmus and anterior periventricular white matter resulted
        in more severe and prolonged non-fluent verbal output, in contrast to shallow
        lesions of the frontal operculum which resulted in transient disorders.
      result_status: detected
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis correctly identifies the specific comparison
            between deep white matter lesions (frontal isthmus/anterior periventricular)
            and shallow opercular lesions regarding non-fluent output, as described
            in the Alexander et al. findings cited in the review.
          source_ids:
          - P4-S1-C11
          - P4-S2-C1
        direction:
          answer: fits
          reason: 'The direction is preserved: deep white matter involvement is associated
            with more severe/prolonged non-fluency, while shallow lesions are associated
            with transient issues. The draft correctly captures this comparative direction.'
          source_ids:
          - P4-S1-C11
          - P4-S2-C1
        construct:
          answer: fits
          reason: The exposure (lesion depth/location) and outcome (non-fluent verbal
            output) are correctly identified. The patient measurement is classified
            as template_lesion_overlap because the source describes lesion location
            relative to anatomical structures (frontal isthmus, periventricular white
            matter) rather than patient-specific diffusion tractography or voxel-wise
            tissue analysis in the context of this review synthesis.
          source_ids:
          - P4-S1-C11
          - P4-S2-C1
        qualifications:
          answer: fits
          reason: The draft includes the necessary qualification that this finding
            is part of a narrative review synthesis of prior work (Alexander et al.)
            and contrasts with shallow lesions. It does not overstate the finding
            as a primary statistical result of the current paper but correctly frames
            it as reported evidence.
          source_ids:
          - P4-S1-C11
          - P4-S2-C1
          - P2-S2-C5
        missing_material_caveat:
          answer: fits
          reason: No material caveats are missing. The draft acknowledges the narrative
            nature of the source and the specific anatomical comparison. The lack
            of specific statistical thresholds or sample sizes is noted as pending/optional,
            which is appropriate for a qualitative draft.
          source_ids:
          - P4-S1-C11
          - P4-S2-C1
      optional_pending:
      - Specific statistical values or p-values for the Alexander et al. finding
      - Exact sample size of the Alexander et al. study
      - Specific imaging modality used in Alexander et al. (likely CT/MRI lesion mapping,
        but not explicitly detailed in this window)
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Specific statistical values or p-values for the Alexander et al. finding
    - Exact sample size of the Alexander et al. study
    - Specific imaging modality used in Alexander et al. (likely CT/MRI lesion mapping,
      but not explicitly detailed in this window)
    normalizations: []
    analysis_identity:
      id: R017
      exposure:
        text: lesions extending into deep white matter of frontal isthmus and anterior
          periventricular white matter
      outcome:
        text: non-fluent verbal output
      analysis_label: White matter depth and output
      relation: association
      evidence_ids:
      - P4-S1-C11
      - P4-S2-C1
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
        pdf_sha256: ef0aaf55a3919bf3928bc764f9271e407b8176b38f51ed6574cbb892431360d2
        source_review: _compare/relationships-2026-11-16/review-current/Plowman2012
        source_status_sha256: caa094a78da1d0d1c5d79de24514910a7cacb76337980659b60aeed0fe6b2b1d
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
  page: 4
  quote: 'While shallow lesions of the frontal oper-

    culum resulted in transient disorders of language output with

    normal articulation and repetition, lesions that extended into the

    deep white matter of the frontal isthmus and anterior periventricu-

    lar white matter resulted in more severe and prolonged non-ﬂuent

    '
  status: pending
  by: agent:relationship-converter
  date: '2026-11-25'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
