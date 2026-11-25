---
id: left_af_fa
name: left arcuate fasciculus FA
kind: predictor
findings:
- id: f1
  target_audit:
    status: needs_source_review
    category: ambiguous_or_composite
    original_target: repetition_aq
    reason: A score, generic outcome or composite label does not uniquely identify a behaviour. Check the
      task, subtests and analysis before retargeting.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  outcome_measurement:
    status: needs_source_review
    instruments: []
    note: Outcome instrument/task is not yet verified for this finding. Do not infer it from the predictor
      or a paper-wide test list.
  target: repetition_aq
  target_kind: impairment
  claim: Poorer repetition is associated with greater damage (lower FA value) to the
    left arcuate fasciculus.
  direction: likely
  relationship: correlational
  method: DTI
  sample:
    n: not_reported
    population: Patients with a history of left hemisphere stroke (ischemic or hemorrhagic),
      premorbidly right-handed
    phase: not_reported
    time_post_onset: Imaging and language testing performed at least 1 month post-stroke
      (mean 22 months); imaging and assessment occurred within 2 weeks of each other.
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Damage was not limited to specific white matter tracts in any case
  - Post-stroke reorganization is a potential confound due to the wide range of time
    since stroke
  - DTI analysis was restricted to FA value measurement
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Fractional anisotropy (FA) measured in a 12-voxel
    region of interest (ROI) in the vertical segment of the left arcuate fasciculus
    where it arches around the insula, identified using color-coded directional diffusion
    maps and a standard white matter atlas. The association remained significant when
    using MR imaging ratings of damage to the left inferior frontal gyrus (Broca area)
    as a covariate; The association remained significant when using the presence of
    lacunar infarcts and/or periventricular white matter abnormalities as a covariate.
    Additional metadata has not been transcribed; review the pending-field flags before
    approval. PDF image reading (P2-S1-C3, two-model agreement, human verification
    pending): . For this reason, the presence or

    absence of WM abnormalities on MR imaging was used as covariates in

    the analyses presented below. All of the participants were at least 1 month

    poststroke onset (mean, 22 months; SD, 24 months; range, 1–72

    months). Mean age was 58 years (SD, 11 years; range, 38–77 years). All of

    the participants were given the Western Aphasia Battery (WAB),17 and

    the composite indices (aphasia quotient [AQ]) for repetition, compre-

    hension, and naming were extracted Original text-layer quotation is preserved
    below. PDF image reading (P2-S4-C4, two-model agreement, human verification pending):
    DTI, structural MR imaging, and language data were acquired within 2 weeks of
    each other Original text-layer quotation is preserved below.'
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
    - not_transcribed:sample.n
    - proposed_concept:repetition_aq
  citation: '@Breier2008'
  source_passages:
  - section: Original source P3-S1-C4
    page: 3
    quote: "The relationship be-\ntween the FA value for the AF and the repetition\
      \ AQ (F[1,18]\n\x01 10.64; P \x04 .004) was significant, whereas the relationship\n\
      with the comprehension AQ (F[1,18] \x01 6.74; P \x04 .018) was\nmarginally significant."
    supports: claim
  - section: Original source P3-S1-C10
    page: 3
    quote: 'Poorer repetition is associated with greater

      damage (lower FA value) to the AF.'
    supports: claim
  - section: Original source P3-S1-C7
    page: 3
    quote: 'The findings

      for the relations between the SLF and AF

      and repetition AQ remained significant.'
    supports: claim
  - section: Original source P2-S1-C1
    page: 2
    quote: '

      Methods

      Participants

      Twenty individuals (13 men) with a history of left hemisphere stroke, 16

      in the distribution of the left middle cerebral artery (15 ischemic and 1

      hemorrhagic) and 4 in subcortical regions (3 ischemic and 1 hemor-

      rhagic), participated in the study.'
    supports: sample
  - section: Original source P2-S1-C3
    page: 2
    quote: 'For this reason, the presence or

      absence of WM abnormalities on MR imaging was used as covariates in

      theanalysespresentedbelow.Alloftheparticipantswereatleast1month

      poststroke onset (mean, 22 months; SD, 24 months; range, 1–72

      months).Meanagewas58years(SD,11years;range,38–77years).Allof

      the participants were given the Western Aphasia Battery (WAB),17 and

      the composite indices (aphasia quotient [AQ]) for repetition, compre-

      hension, and naming were extracted.'
    supports: sample
  - section: Original source P2-S3-C3
    page: 2
    quote: 'DTI Analyses

      Fractional anisotropy (FA) indices for the left and right SLF, AF, and UF

      were determined in each hemisphere for each patient by 2 independent

      raters(J.I.B.andD.M.)whowereblindtothelanguagedata.Weobtained

      FA values for the AF in the portion that curves around the depth of the

      caudal portion of the Sylvian fissure, forming an arc.'
    supports: method
  - section: Original source P2-S3-C7
    page: 2
    quote: 'A rectangular 12-voxel region was then placed around this point

      in the sagittal plane and the box moved, if necessary, to produce the

      highest average FA value possible in that plane (Fig 1).'
    supports: method
  - section: Original source P2-S4-C4
    page: 2
    quote: 'DTI, structural MR imaging, and language data were acquired within

      2 weeks of each other.'
    supports: method
  - section: Original source P4-S1-C1
    page: 4
    quote: '

      thought of as a subdivision of the SLF, forming a large arc

      around the insula and projecting into the temporal lobe.27

      Within the left hemisphere, the fibers of the SLF and AF con-

      nect various aspects of the temporal and frontal cortex in-

      volved in receptive and expressive language,30 forming part of

      the distributed language network.31,32 We measured the FA

      values in the AF in its vertical segment at the point at which it

      arches around the insula, and we measured the FA values in

      the SLF where it runs anteroposterior deep to the Sylvian

      fissure.'
    supports: method
  - section: Original source P4-S3-C5
    page: 4
    quote: 'There was also a

      wide range of lesion size in the current study, and in no case

      was damage limited to specific WM tracts.'
    supports: limitation
  - section: Original source P4-S3-C2
    page: 4
    quote: 'Given the large range of time since stroke in the study sam-

      ple, poststroke reorganization is a potential confound in this

      study.'
    supports: limitation
  - section: Original source P4-S2-C9
    page: 4
    quote: 'In addition, the DTI

      analysis was restricted to FA value measurement.'
    supports: limitation
predictor_type: imaging_metric
short_definition: Fractional anisotropy (FA) measured in a 12-voxel region of interest
  (ROI) in the vertical segment of the left arcuate fasciculus where it arches around
  the insula, identified using color-coded directional diffusion maps and a standard
  white matter atlas.
assessment:
- Western Aphasia Battery (WAB)
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-20'
relationship_review:
  paper: Breier2008
  proposal_id: R004
  review_status_sha256: 60f9bf2b5e382c51bb89a9bbb423aab5a3298dcd94337a04678147f21c362051
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 84c02c74ca834f3db3c6bd5b55fffedd45e7e0f20963f011a232ebd5071ce337
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 84c02c74ca834f3db3c6bd5b55fffedd45e7e0f20963f011a232ebd5071ce337
        A/passages.json: 8f3e0861c9cf0a815bacbb6c105a5576884eb4e8f2e8ba7064c7edd95aa28539
        A/raw.json: ced5daeba81d16820192b56b90f6777008861d050582f48f57d6c23e59417103
        A/source-units.json: 1d96cdfd3dfa5f4edcbfa485db98545f8a767719a4fb4dfd6d7af062721c6b60
        A/full-source-units.json: fabd535fa5d417a3f6ac632ad8c3606d244ceeb40f9ffd620600dc476130ff26
        A/meta.json: f60754a5d8e96fcd953bb20e7359b870a7d77653faf710422cfeae246e88558f
        A/table-images/manifest.json: bcd390ab568c4b89dae6e8013c7885de1789860f5d884f0d9c09115d8fc46045
        A/clauses/window-03/raw.json: 4d658f1f50df3b2b7e33af321e4d64e2368fc049f2dd50d7ad1de591a0b0cafa
        A/clauses/window-03/prompt.txt: f65a5dd4d75dfba67bb833d911c8ad0f50e7c847940a6e14d2074a703251af86
        A/clauses/window-03/meta.json: 0e29ec738e66bb551562ae81b368a6cc3e9f05ea75747b688f27c84a633495eb
        A/clauses/window-04/raw.json: 4610b20686565bc2c452cd65bb5d4378525da6a61999c6c9e06d9a18b130f9d6
        A/clauses/window-04/prompt.txt: 589ac71f1417adcbcf7a7ef2c6f433cac0ea83b06427ed659704e323f0586053
        A/clauses/window-04/meta.json: 2cf768c34008dba9fe23a76e06bf3d94b4e800c74350eb30521882f3cc4856c9
        A/clauses/window-02/raw.json: 46b213f5252c4e2a200dd9c40f9a84bb00499bdeebf590f7b17eb49c368c81d4
        A/clauses/window-02/prompt.txt: c2b879fed3326c4016c19d14c2ca38198e573bf871f7b96ae818d62026e968db
        A/clauses/window-02/meta.json: 0df34e6ddeec66d7278cd6b85ba9c5cd4c3d484d4934f86ed89739be2c2cdd02
        A/clauses/window-01/raw.json: 0dab26115e2aa18f4efd562948b83604296fdfd6deddbafcea32679ec1627de9
        A/clauses/window-01/prompt.txt: d199eda9b880ed195e9ee0d10a5736a4787eb50994fd947323715ffc3ad806ca
        A/clauses/window-01/meta.json: afc1fa3423545b35628cb2f0ba68dbfc37fa06c4372e24e031d1770c59a04d94
        B/passages.json: 8f3e0861c9cf0a815bacbb6c105a5576884eb4e8f2e8ba7064c7edd95aa28539
        B/raw.json: cf26a73979ea6de3468485f8e128ee708f6f6e28cbb0f374d9908d64a92c7ffb
        B/source-units.json: 1d96cdfd3dfa5f4edcbfa485db98545f8a767719a4fb4dfd6d7af062721c6b60
        B/full-source-units.json: fabd535fa5d417a3f6ac632ad8c3606d244ceeb40f9ffd620600dc476130ff26
        B/meta.json: 72e206d1e3c8c6cab15231a4d03adea1b3d81d057586875d294a54c9cb2aac67
        B/table-images/manifest.json: bcd390ab568c4b89dae6e8013c7885de1789860f5d884f0d9c09115d8fc46045
        B/clauses/window-03/raw.json: bee7e32ad82e2f20a3fcb188fb8d1aa81066c556d2933f6f047b5ed39e9c8db2
        B/clauses/window-03/prompt.txt: f65a5dd4d75dfba67bb833d911c8ad0f50e7c847940a6e14d2074a703251af86
        B/clauses/window-03/meta.json: 93a5b91a5f46842b63af7f207df0e62e7cfae0a137507753ab19c7f91ebfd8cd
        B/clauses/window-04/raw.json: 16dbc8370fa6223beb63f3c8b1e6eb05a8646ea05f593295e62af5203b0f5597
        B/clauses/window-04/prompt.txt: 589ac71f1417adcbcf7a7ef2c6f433cac0ea83b06427ed659704e323f0586053
        B/clauses/window-04/meta.json: 2455c123d33efd7e19011668a318549888a340be08d2adf0c1bb646a7c5faf55
        B/clauses/window-02/raw.json: 15404887fe438bb26ad26d3606c04f7e7c4ebaaa6c9191b8b200ea51f6505423
        B/clauses/window-02/prompt.txt: c2b879fed3326c4016c19d14c2ca38198e573bf871f7b96ae818d62026e968db
        B/clauses/window-02/meta.json: 7d924677da5de102685c98dcd298e75e82f163610e1f8e205c65100acd419f74
        B/clauses/window-01/raw.json: 6a7b334250c4e17ac8edc1a5d8171329db96f3fcb9a0796163d34f4ada23f71c
        B/clauses/window-01/prompt.txt: d199eda9b880ed195e9ee0d10a5736a4787eb50994fd947323715ffc3ad806ca
        B/clauses/window-01/meta.json: 0249dc942a0d48c1fd30486c86f2ec08a39a79fdf212e8b835010a1f21bb4c62
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
      pdf_sha256: 84c02c74ca834f3db3c6bd5b55fffedd45e7e0f20963f011a232ebd5071ce337
      source_review: _compare/relationships-2026-11-16/review-current/Breier2008
      source_status_sha256: 2c15c65a6ac200a2209fc938832a613dc1cd0f77196daf6da15e65b843473adf
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R004
    exposure:
      text: left hemisphere arcuate fasciculus (AF) FA
    outcome:
      text: repetition AQ
    analysis_label: Follow-up analysis
    relation: association
    evidence_ids:
    - P3-S1-C4
    - P3-S1-C10
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
      pdf_sha256: 84c02c74ca834f3db3c6bd5b55fffedd45e7e0f20963f011a232ebd5071ce337
      source_review: _compare/relationships-2026-11-16/review-current/Breier2008
      source_status_sha256: 2c15c65a6ac200a2209fc938832a613dc1cd0f77196daf6da15e65b843473adf
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P2-S3-C10
      - Result passage disposed without unit P2-S4-C6
      - Result passage disposed without unit P3-S1-C1
      - Result passage disposed without unit P3-S1-C2
      - Result passage disposed without unit P3-S1-C4
      - Result passage disposed without unit P3-S1-C5
      - Result passage disposed without unit P3-S1-C13
      - Result passage disposed without unit P3-S1-C7
      - Result passage disposed without unit P3-S1-C8
      - Result passage disposed without unit P4-S3-C9
      unattached_null_or_qualifier_ids:
      - P2-S4-C6
      - P3-S1-C5
      - P3-S1-C7
      - P3-S1-C8
      - P4-S3-C9
      suppressed_nonrepresented_units: 6
      default_disposition_count_requires_completeness_check: 77
      unselected_timing_passages:
      - P1-S1-C8
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: validation
        source_id: P2-S3-C10
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: limitations
        source_ids:
        - P4-S2-C10
        - P4-S2-C11
        - P4-S2-C12
        - P4-S2-C7
        - P4-S2-C8
        - P4-S3-C2
        - P4-S3-C3
        - P4-S3-C5
        - P4-S3-C7
        reason: Runaway selection (>8 passages); entire slot requires source review
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
        - P2-S3
        - P2-S4
        - P3-S1
        - P3-S2
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 84c02c74ca834f3db3c6bd5b55fffedd45e7e0f20963f011a232ebd5071ce337
      source_review: _compare/relationships-2026-11-16/review-current/Breier2008
      source_status_sha256: 2c15c65a6ac200a2209fc938832a613dc1cd0f77196daf6da15e65b843473adf
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C10
      disposition: repeated
      result_indexes:
      - 3
      - 4
      reason: Restatement of results in abstract.
    - source_id: P1-S1-C11
      disposition: repeated
      result_indexes:
      - 4
      reason: Restatement of results in abstract.
    - source_id: P1-S1-C12
      disposition: repeated
      result_indexes:
      - 6
      reason: Restatement of results in abstract.
    - source_id: P1-S1-C13
      disposition: repeated
      result_indexes:
      - 8
      reason: Restatement of results in abstract.
    - source_id: P2-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes patient characteristics and WM disease presence.
    - source_id: P2-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes DTI acquisition and SNR.
    - source_id: P2-S3-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes ROI placement for large lesions.
    - source_id: P2-S3-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports inter-rater reliability correlation.
    - source_id: P2-S4-C6
      disposition: represented
      result_indexes:
      - 0
      reason: Establishes significant interaction for AF.
    - source_id: P3-S1-C1
      disposition: represented
      result_indexes:
      - 0
      - 1
      reason: Establishes significant interaction for AF and SLF.
    - source_id: P3-S1-C2
      disposition: represented
      result_indexes:
      - 2
      reason: Establishes null finding for UF.
    - source_id: P3-S1-C4
      disposition: represented
      result_indexes:
      - 3
      - 4
      reason: Establishes AF relationship with repetition and comprehension.
    - source_id: P3-S1-C5
      disposition: represented
      result_indexes:
      - 5
      reason: Establishes SLF relationship with repetition.
    - source_id: P3-S1-C7
      disposition: represented
      result_indexes:
      - 6
      reason: Establishes persistence of SLF/AF repetition effect after adjustment.
    - source_id: P3-S1-C8
      disposition: represented
      result_indexes:
      - 7
      reason: Establishes loss of AF comprehension effect after adjustment.
    - source_id: P3-S1-C10
      disposition: repeated
      result_indexes:
      - 3
      reason: Restatement of AF-repetition association.
    - source_id: P3-S1-C11
      disposition: repeated
      result_indexes:
      - 5
      reason: Restatement of SLF-repetition association.
    - source_id: P3-S1-C12
      disposition: represented
      result_indexes:
      - 8
      reason: Establishes null findings for right hemisphere and demographics.
    - source_id: P3-S1-C13
      disposition: represented
      result_indexes:
      - 9
      reason: Establishes no change in results when using demographics or WM disease
        as covariates.
    - source_id: P3-S2-C2
      disposition: represented
      result_indexes:
      - 10
      reason: Establishes non-significant difference between ROI FA values.
    - source_id: P3-S2-C3
      disposition: repeated
      result_indexes:
      - 3
      - 5
      reason: Discussion restatement of SLF/AF repetition findings.
    - source_id: P4-S1-C2
      disposition: repeated
      result_indexes:
      - 3
      - 4
      - 5
      reason: Discussion restatement of AF and SLF findings.
    - source_id: P4-S1-C3
      disposition: repeated
      result_indexes:
      - 6
      - 7
      reason: Discussion restatement of sensitivity results.
    - source_id: P4-S1-C6
      disposition: repeated
      result_indexes:
      - 2
      reason: Discussion restatement of UF null finding.
    - source_id: P4-S2-C6
      disposition: repeated
      result_indexes:
      - 6
      reason: Restatement of repetition deficits independent of cortical damage.
    - source_id: P4-S3-C4
      disposition: repeated
      result_indexes:
      - 9
      reason: Restatement that demographics did not affect findings.
    - source_id: P4-S3-C9
      disposition: repeated
      result_indexes:
      - 6
      - 7
      - 9
      reason: Synthesis of results regarding independent variance and WM abnormalities.
    unresolved_coverage: []
    pending_source_ids:
    - P1-S1-C10
    - P1-S1-C11
    - P1-S1-C12
    - P1-S1-C13
    - P2-S1-C2
    - P2-S2-C3
    - P2-S3-C8
    - P2-S3-C10
    - P3-S2-C3
    - P4-S1-C2
    - P4-S1-C3
    - P4-S1-C6
    - P4-S2-C6
    - P4-S3-C4
    - P4-S3-C9
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
      - P2-S1-C1
      recruited_sample:
      - P2-S1-C1
      eligibility:
      - P1-S1-C8
      - P1-S1-C9
      - P2-S1-C1
      - P2-S1-C3
      imaging_provenance:
      - P2-S3-C5
      imaging_timing:
      - P1-S1-C9
      - P2-S1-C3
      - P2-S4-C4
      outcome_timing:
      - P1-S1-C9
      - P2-S1-C3
      - P2-S4-C4
      outcome_definition:
      - P2-S1-C3
      validation: []
      analysis_restrictions:
      - P2-S3-C8
      - P4-S2-C9
      dependent_variable_statement:
      - P2-S4-C5
      limitations: []
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P2-S1-C3
      - P3-S1-C6
      - P3-S1-C13
      - P4-S3-C8
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P2-S1-C1
      - P2-S1-C3
      - P3-S1-C12
      - P4-S3-C3
      - P4-S3-C4
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: none_described
    held_selections:
    - slot: validation
      source_id: P2-S3-C10
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: limitations
      source_ids:
      - P4-S2-C10
      - P4-S2-C11
      - P4-S2-C12
      - P4-S2-C7
      - P4-S2-C8
      - P4-S3-C2
      - P4-S3-C3
      - P4-S3-C5
      - P4-S3-C7
      reason: Runaway selection (>8 passages); entire slot requires source review
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
      pdf_sha256: 84c02c74ca834f3db3c6bd5b55fffedd45e7e0f20963f011a232ebd5071ce337
      review_sha256: 60f9bf2b5e382c51bb89a9bbb423aab5a3298dcd94337a04678147f21c362051
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
      - P3-S1-C4
      - P3-S1-C10
      source_result: A significant association was detected between left arcuate fasciculus
        (AF) fractional anisotropy (FA) and repetition aphasia quotient (AQ) (F[1,18]
        = 10.64; P < .004). The direction of the association is such that poorer repetition
        performance is associated with greater damage (lower FA values) to the AF.
        This association remained significant after adjusting for cortical damage
        (inferior frontal gyrus) and white matter disease covariates.
      result_status: detected
      patient_measurement: patient_diffusion
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis corresponds to the follow-up univariate analysis
            of the relationship between left AF FA and repetition AQ, as described
            in P3-S1-C4 and summarized in P3-S1-C10. The model and comparison match
            the source.
          source_ids:
          - P3-S1-C4
          - P3-S1-C10
        direction:
          answer: fits
          reason: The source explicitly states in P3-S1-C10 that 'Poorer repetition
            is associated with greater damage (lower FA value) to the AF.' The proposed
            draft correctly captures this directionality.
          source_ids:
          - P3-S1-C10
        construct:
          answer: fits
          reason: The exposure is correctly identified as left AF FA. The outcome
            is repetition AQ. The measurement method is patient-specific diffusion
            tensor imaging (DTI) where FA is extracted from a 12-voxel ROI in the
            patient's own brain (P2-S3-C3, P2-S3-C7), not a template overlay. The
            draft correctly identifies this as patient_diffusion.
          source_ids:
          - P2-S3-C3
          - P2-S3-C7
          - P3-S1-C4
        qualifications:
          answer: fits
          reason: The draft includes the qualification that the association remained
            significant after adjusting for cortical damage (Broca area) and WM disease.
            This is supported by P3-S1-C7 ('findings... remained significant') and
            P3-S1-C13 (no changes when WM disease used as covariate). These are correctly
            framed as robustness qualifiers, not standalone null findings for the
            covariates.
          source_ids:
          - P3-S1-C7
          - P3-S1-C13
        missing_material_caveat:
          answer: fits
          reason: The draft includes relevant limitations regarding lesion heterogeneity
            (P4-S3-C5), post-stroke reorganization (P4-S3-C2), and the restriction
            to FA metrics (P4-S2-C9). No material caveats that would change the interpretation
            of the core association are omitted.
          source_ids:
          - P4-S3-C5
          - P4-S3-C2
          - P4-S2-C9
      optional_pending:
      - Sample size (N=20) is mentioned in source P2-S1-C1 but not transcribed into
        the draft's sample_n field; this is an optional omission.
      - Specific F-statistics and P-values are not transcribed into the draft, which
        is acceptable for a qualitative draft.
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Sample size requires source confirmation; it has not been transcribed.
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Sample size (N=20) is mentioned in source P2-S1-C1 but not transcribed into
      the draft's sample_n field; this is an optional omission.
    - Specific F-statistics and P-values are not transcribed into the draft, which
      is acceptable for a qualitative draft.
    normalizations:
    - field: sample.n
      original: 20
      action: not_transcribed
      reason: Not supported by selected quotations
    analysis_identity:
      id: R004
      exposure:
        text: left hemisphere arcuate fasciculus (AF) FA
      outcome:
        text: repetition AQ
      analysis_label: Follow-up analysis
      relation: association
      evidence_ids:
      - P3-S1-C4
      - P3-S1-C10
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
        pdf_sha256: 84c02c74ca834f3db3c6bd5b55fffedd45e7e0f20963f011a232ebd5071ce337
        source_review: _compare/relationships-2026-11-16/review-current/Breier2008
        source_status_sha256: 2c15c65a6ac200a2209fc938832a613dc1cd0f77196daf6da15e65b843473adf
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P3-S1-C4:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 84c02c74ca834f3db3c6bd5b55fffedd45e7e0f20963f011a232ebd5071ce337
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: ff85dbb2168e99887af5e7af55af431ac49c1be1340d94b5dffcc38b264e8cbc
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S1-C4
          page: 3
          text_layer_sha256: ff85dbb2168e99887af5e7af55af431ac49c1be1340d94b5dffcc38b264e8cbc
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: "The relationship be-\ntween the FA value for the AF and the\
          \ repetition AQ (F[1,18]\n\x01 10.64; P \x04 .004) was significant, whereas\
          \ the relationship\nwith the comprehension AQ (F[1,18] \x01 6.74; P \x04\
          \ .018) was\nmarginally significant."
        anchor_text: "The relationship be-\ntween the FA value for the AF and the\
          \ repetition AQ (F[1,18]\n\x01 10.64; P \x04 .004) was significant, whereas\
          \ the relationship\nwith the comprehension AQ (F[1,18] \x01 6.74; P \x04\
          \ .018) was\nmarginally significant."
        excluded_fragments: []
      P2-S1-C1:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 84c02c74ca834f3db3c6bd5b55fffedd45e7e0f20963f011a232ebd5071ce337
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 7c07dfeb13c9a95b3fa4469e2a9e6c254a70768b976794a9ddd6c5b3bf5109bd
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S1-C1
          page: 2
          text_layer_sha256: 371b04cbc804ff3af2863db04c4747f031c8590e486c41e53fb9149050b8d4ce
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: '

          Methods

          Participants

          Twenty individuals (13 men) with a history of left hemisphere stroke, 16

          in the distribution of the left middle cerebral artery (15 ischemic and
          1

          hemorrhagic) and 4 in subcortical regions (3 ischemic and 1 hemor-

          rhagic), participated in the study.'
        anchor_text: 'Methods

          Participants

          Twenty individuals (13 men) with a history of left hemisphere stroke, 16

          in the distribution of the left middle cerebral artery (15 ischemic and
          1

          hemorrhagic) and 4 in subcortical regions (3 ischemic and 1 hemor-

          rhagic), participated in the study.'
        excluded_fragments: []
        image_sha256: ba995a1462ac3bfb465161bc9fb45eef51d8f3c08eae9416a0b6ae69691a2bce
      P2-S1-C3:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 84c02c74ca834f3db3c6bd5b55fffedd45e7e0f20963f011a232ebd5071ce337
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: bed6c55ff6a17cd6893d2856d369636bfed28695aac90ff8e8a3225ff33ef3a4
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S1-C3
          page: 2
          text_layer_sha256: bed6c55ff6a17cd6893d2856d369636bfed28695aac90ff8e8a3225ff33ef3a4
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'For this reason, the presence or

          absence of WM abnormalities on MR imaging was used as covariates in

          theanalysespresentedbelow.Alloftheparticipantswereatleast1month

          poststroke onset (mean, 22 months; SD, 24 months; range, 1–72

          months).Meanagewas58years(SD,11years;range,38–77years).Allof

          the participants were given the Western Aphasia Battery (WAB),17 and

          the composite indices (aphasia quotient [AQ]) for repetition, compre-

          hension, and naming were extracted.'
        anchor_text: 'For this reason, the presence or

          absence of WM abnormalities on MR imaging was used as covariates in

          theanalysespresentedbelow.Alloftheparticipantswereatleast1month

          poststroke onset (mean, 22 months; SD, 24 months; range, 1–72

          months).Meanagewas58years(SD,11years;range,38–77years).Allof

          the participants were given the Western Aphasia Battery (WAB),17 and

          the composite indices (aphasia quotient [AQ]) for repetition, compre-

          hension, and naming were extracted.'
        excluded_fragments: []
        image_sha256: c5bddd82fbe503b7a3f50536c8f4d6017a72f275c26b8a9928a7df35631c7170
        transcription: '. For this reason, the presence or

          absence of WM abnormalities on MR imaging was used as covariates in

          the analyses presented below. All of the participants were at least 1 month

          poststroke onset (mean, 22 months; SD, 24 months; range, 1–72

          months). Mean age was 58 years (SD, 11 years; range, 38–77 years). All of

          the participants were given the Western Aphasia Battery (WAB),17 and

          the composite indices (aphasia quotient [AQ]) for repetition, compre-

          hension, and naming were extracted'
      P2-S4-C4:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 84c02c74ca834f3db3c6bd5b55fffedd45e7e0f20963f011a232ebd5071ce337
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 8cc1d1122a6f6ac39630f9ecf7e77e1b7638f9d2a1a509ee64cbba22bcb03a36
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S4-C4
          page: 2
          text_layer_sha256: 8cc1d1122a6f6ac39630f9ecf7e77e1b7638f9d2a1a509ee64cbba22bcb03a36
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'DTI, structural MR imaging, and language data were acquired
          within

          2 weeks of each other.'
        anchor_text: 'DTI, structural MR imaging, and language data were acquired
          within

          2 weeks of each other.'
        excluded_fragments: []
        image_sha256: fa9cf1c07cc51aea120b9e189212abea50588a92cc6d044ea38939c09b7c182b
        transcription: DTI, structural MR imaging, and language data were acquired
          within 2 weeks of each other
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 3
  quote: "The relationship be-\ntween the FA value for the AF and the repetition AQ\
    \ (F[1,18]\n\x01 10.64; P \x04 .004) was significant, whereas the relationship\n\
    with the comprehension AQ (F[1,18] \x01 6.74; P \x04 .018) was\nmarginally significant."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-20'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
