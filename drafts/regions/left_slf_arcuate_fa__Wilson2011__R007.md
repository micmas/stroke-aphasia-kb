---
id: left_slf_arcuate_fa
name: left SLF/Arcuate FA
kind: tract
findings:
- id: f1
  target: syntactic_processing
  target_kind: impairment
  claim: Reduced FA in the left SLF/Arcuate is associated with deficits in both syntactic
    comprehension and production, and this relationship remains significant even when
    gray matter volumes in the left inferior frontal gyrus are included as a covariate.
  direction: likely
  relationship: correlational
  method: DTI
  sample:
    n: 27
    population: patients with primary progressive aphasia (nonfluent, semantic, and
      logopenic variants)
    phase: not_reported
    time_post_onset: mean years since onset of disease was 5.6
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - could not determine whether syntactic processing depends differentially on particular
    subcomponents of the SLF/Arcuate because they are often damaged in parallel
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Mean fractional anisotropy (FA) of the left SLF/Arcuate
    tract, mapped using probabilistic tractography with seed regions of interest placed
    at known bottlenecks on individual patients'' color-coded diffusion maps. analysis
    adjusted for gray matter volumes in the left inferior frontal gyrus; analysis
    also adjusted for PPA variant, overall severity (MMSE), executive function, and
    motor speech. Additional metadata has not been transcribed; review the pending-field
    flags before approval. PDF image reading (P5-S2-C7, two-model agreement, human
    verification pending): EXPERIMENTAL PROCEDURES


    Participants

    We studied 27 patients with PPA, recruited through the Memory and Aging Center
    at the University of California, San Francisco (UCSF) Original text-layer quotation
    is preserved below. PDF image reading (P5-S2-C9, two-model agreement, human verification
    pending): . Patients were classified into one of three

    PPA variants: nonfluent (n = 11), semantic (n = 10), and logopenic (n = 6) Original
    text-layer quotation is preserved below. PDF image reading (P5-S3-C4, two-model
    agreement, human verification pending): . The mean MMSE score

    was 24.0 (SD = 5.3, range = 8–30), and the mean years since onset of disease

    was 5.6 (SD = 2.9, range = 2–13) Original text-layer quotation is preserved below.'
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
  citation: '@Wilson2011'
  source_passages:
  - section: Original source P2-S2-C4
    page: 2
    quote: 'DTI Correlates of Syntactic Deﬁcits

      In the left SLF/Arcuate, reduced FA was strongly

      associated

      with

      deﬁcits

      in

      both

      syntactic

      comprehension (r = 0.61, F[1, 25] = 14.81, p =

      0.0007, Figure 2A) and production (r = 0.73, F[1, 25] = 28.00,

      p < 0.0001, Figure 2B).'
    supports: claim
  - section: Original source P3-S2-C5
    page: 3
    quote: 'When gray matter

      volumes in the IFG were included as a covariate, FA in the left

      SLF/Arcuate continued to predict both syntactic comprehension

      (partial r = 0.40, F[1, 24] = 4.61, p = 0.042) and production (partial

      r = 0.60, F[1, 24] = 13.34, p = 0.0013) scores.'
    supports: claim
  - section: Original source P3-S1-C13
    page: 3
    quote: 'In the full models with

      all potential mediating factors included, FA in the SLF/Arcuate

      continued to predict syntactic comprehension (partial r = 0.63,

      F[1, 17] = 10.29, p = 0.0052) and production (partial r = 0.54,

      F[1, 17] = 8.52, p = 0.0096) scores.'
    supports: claim
  - section: Original source P5-S2-C7
    page: 5
    quote: 'EXPERIMENTAL PROCEDURES

      Participants

      We studied 27 patients with PPA, recruited through the Memory and Aging

      Center at the University of California, San Francisco (UCSF).'
    supports: sample
  - section: Original source P5-S2-C9
    page: 5
    quote: 'Patients were classiﬁed into one of three

      PPA variants: nonﬂuent (n = 11), semantic (n = 10), and logopenic (n = 6).'
    supports: sample
  - section: Original source P5-S3-C4
    page: 5
    quote: 'The mean MMSE score

      was 24.0 (SD = 5.3, range = 8–30), and the mean years since onset of disease

      was 5.6 (SD = 2.9, range = 2–13).'
    supports: sample
  - section: Original source P5-S3-C8
    page: 5
    quote: 'Three tracts

      were mapped using probabilistic tractography implemented in FSL (Behrens

      et al., 2003, 2007): the SLF/Arcuate, ECFS, and UF.'
    supports: method
  - section: Original source P5-S3-C9
    page: 5
    quote: 'Each tract was seeded in known ‘‘bottlenecks’’ on individual subjects’
      color-

      coded images (Figures 1A–1C).'
    supports: method
  - section: Original source P5-S3-C14
    page: 5
    quote: 'We quantiﬁed white matter integrity in terms of mean FA (Basser et al.,
      1994)

      in each individual’s tracts.'
    supports: method
  - section: Original source P5-S4-C6
    page: 5
    quote: 'Behavioral Assessments

      Syntactic comprehension was assessed using a two-alternative forced choice

      auditory sentence-to-picture matching task (Wilson et al., 2010a).'
    supports: claim
  - section: Original source P6-S1-C1
    page: 6
    quote: '

      Syntactic production was rated on a seven point scale by two researchers

      (S.M.W. and K.R., the latter a licensed speech-language pathologist).'
    supports: claim
  - section: Original source P5-S1-C12
    page: 5
    quote: 'For this reason, we could not determine whether syntactic pro-

      cessing depends differentially on particular subcomponents of

      the SLF/Arcuate.'
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-26'
relationship_review:
  paper: Wilson2011
  proposal_id: R007
  review_status_sha256: 0a3762230cc0b271757dc962cf171f38e255399758a8c4a2d1495004a1fcca72
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: fde000e1fc86d9993dac4c418d93e4566c4c0521ed6bb3c80efba23a81a521ca
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: fde000e1fc86d9993dac4c418d93e4566c4c0521ed6bb3c80efba23a81a521ca
        A/passages.json: ee6e36f90218165bc3f956a55f80b6db89204a26f392d0eba3027f6ee54eff30
        A/raw.json: 6c31b2bcce33bfb7f0b9b9a771c3a8df5a5f9bcf212efe54773223d405bf9df8
        A/source-units.json: 2909a39aa998205eeffdc121f9d06e53e7183b7e64f72c137ccf938348beba99
        A/full-source-units.json: 2df3d8336abaa77f435ba7e4661f35e39ca528ba66a9eb46ac983ed5fd5f6f2d
        A/meta.json: ceb2812f755fd189f8e01ead4c09e60062615b45842cea5760a6af2c4b2eeac3
        A/table-images/manifest.json: 19a203963bd0dcc35463e1a5e59b9bfacc09c21581ae41292b3a44cc4d5172e0
        A/clauses/window-03/raw.json: 8f60530c8fcd09b0f90f2389aa1e701e74c83a127bfa0506c477e71ca56c1d52
        A/clauses/window-03/prompt.txt: fc59134aa886705210ca97026c006237afa71bede30d5c4eef14cea45ad16e11
        A/clauses/window-03/meta.json: cd8dbf5f7dca1409853c35c7d933fbbef7c2cde94dd201aaf44f7b818403eeab
        A/clauses/window-04/raw.json: 36ae1036286c35b1b815a9d462ce682523c3342cf4abe450cb4e4c164d3921c1
        A/clauses/window-04/prompt.txt: 8c93b7754ff6b67a78cc0e866ca6191869b619a03678605d7c10cec3723e35f1
        A/clauses/window-04/meta.json: 586e717cbec141f119106aa3ea5411aa07ebf32e6bf7e796bcfedf7bc4f0a4f8
        A/clauses/window-05/raw.json: 90878038a30d425637cfc0188f8e57844026c4c4b89f9f5b787ba27bab69bab1
        A/clauses/window-05/prompt.txt: ebd6fee1304d278c501adaa32d1d427073fdb543ca8fbb6c7cf6d130dfc5e0a1
        A/clauses/window-05/meta.json: 631ec8ce6eb317a065b301ab5587267b4148194df7013f2d56d13255ecebfee8
        A/clauses/window-02/raw.json: 08042f191b9eab2ab1bae3e3ca97050e9fb138210bae10547a085c660f35383c
        A/clauses/window-02/prompt.txt: 5a97a038bcd7b1fd332c79d61c4b2f3e30c7f4d1679a8db058061dae305e6428
        A/clauses/window-02/meta.json: 9a9f9a9e23e0fe687f1beff31bb94c3f4725c50ff514d2a053dc07257e349a59
        A/clauses/window-01/raw.json: 33666ef61253f66361a6ec62d2c157c9900ffc08894041581858ee2a26bd85ac
        A/clauses/window-01/prompt.txt: 517c4cce692bfe4a0b55c29c80813ffd2dd6e0ab791a51de79248924df72659a
        A/clauses/window-01/meta.json: f5461329c83ca397ed011b43b393f30b798286db352cf6c272c2abd5ab0991cd
        A/clauses/window-06/raw.json: d726c73aeefe467ecae05f7a51aef5ef56221de8d54ece693e01b73213978615
        A/clauses/window-06/prompt.txt: 3b7bd7cd6c12abbb8fa91f8c0258f8805b0a70581eb5e64025dbe0602e210ef0
        A/clauses/window-06/meta.json: 966c9163aaf6ac9cd76d4946369b9525c5e5d2c37b47976f0427e88ae3040705
        B/passages.json: ee6e36f90218165bc3f956a55f80b6db89204a26f392d0eba3027f6ee54eff30
        B/raw.json: 8b493a9f426cd95eb53a42e90d6bdc771d38face4af69f68944aa9fdeeb45b29
        B/source-units.json: 2909a39aa998205eeffdc121f9d06e53e7183b7e64f72c137ccf938348beba99
        B/full-source-units.json: 2df3d8336abaa77f435ba7e4661f35e39ca528ba66a9eb46ac983ed5fd5f6f2d
        B/meta.json: bbf77296d03bc4f1f5e73dc7f7ad45c724f278f3859ab952011dbbdc9795ff0f
        B/table-images/manifest.json: 19a203963bd0dcc35463e1a5e59b9bfacc09c21581ae41292b3a44cc4d5172e0
        B/clauses/window-03/raw.json: 8150f3e8fc1cf3a7216d04af065781f5d0b9036ea84eebbd2b54383cbc36e7ca
        B/clauses/window-03/prompt.txt: fc59134aa886705210ca97026c006237afa71bede30d5c4eef14cea45ad16e11
        B/clauses/window-03/meta.json: 793c1e9f427fd5efb0082f09bd6ea7a1f1ba1048ec4fc471453e40ae5fa4132d
        B/clauses/window-04/raw.json: 55dd0e862bab0394e493b17c21192cc0684d1933c940e63578932b38163e3352
        B/clauses/window-04/prompt.txt: 8c93b7754ff6b67a78cc0e866ca6191869b619a03678605d7c10cec3723e35f1
        B/clauses/window-04/meta.json: e8f2027e7218833e9adaf0b9748c60a7b37ed478a186a7c6ecfddda24acbf08f
        B/clauses/window-05/raw.json: 8a67fe60937cf1dfbc943b18174576e63ae764e5a299bf5844e5df565ebb1c69
        B/clauses/window-05/prompt.txt: ebd6fee1304d278c501adaa32d1d427073fdb543ca8fbb6c7cf6d130dfc5e0a1
        B/clauses/window-05/meta.json: 7805690decdf2d998086f876bf66dc29e07239f029550a27e096ac4905dc9eeb
        B/clauses/window-02/raw.json: 02434094b3405e6eebf2ddd636246519d1dc7f63f827d6b64cf326d5be339704
        B/clauses/window-02/prompt.txt: 5a97a038bcd7b1fd332c79d61c4b2f3e30c7f4d1679a8db058061dae305e6428
        B/clauses/window-02/meta.json: 962d1872eb363cb9faef46403e8c4080c791068e68ba7e0764559995ca03898d
        B/clauses/window-01/raw.json: 338cd510cd21334810ed99b45559f609dcc1662454104e8e05015a95dc4a3ca8
        B/clauses/window-01/prompt.txt: 517c4cce692bfe4a0b55c29c80813ffd2dd6e0ab791a51de79248924df72659a
        B/clauses/window-01/meta.json: b27e291597c06ab0665bef7080076ab88f6b1f23f555620f33733081dbea1f88
        B/clauses/window-06/raw.json: 1a78ed90b988dd401f77206f7785846bad99f7ddbe411c185175f890b98afd3b
        B/clauses/window-06/prompt.txt: 3b7bd7cd6c12abbb8fa91f8c0258f8805b0a70581eb5e64025dbe0602e210ef0
        B/clauses/window-06/meta.json: 8223df7883ec54417aea0e6a0bcdc36e912bb1a1433953dd17a7e3104d683b7f
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
      pdf_sha256: fde000e1fc86d9993dac4c418d93e4566c4c0521ed6bb3c80efba23a81a521ca
      source_review: _compare/relationships-2026-11-16/review-current/Wilson2011
      source_status_sha256: af4741f74b79725988cacfb1e13f3eb2025fd19d884fe2943b893facc850ae06
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R007
    exposure:
      text: left SLF/Arcuate FA
    outcome:
      text: syntactic comprehension and production
    analysis_label: Prediction adjusted for gray matter atrophy
    relation: sensitivity
    evidence_ids:
    - P3-S2-C5
    qualifier_ids:
    - P3-S2-C6
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: fde000e1fc86d9993dac4c418d93e4566c4c0521ed6bb3c80efba23a81a521ca
      source_review: _compare/relationships-2026-11-16/review-current/Wilson2011
      source_status_sha256: af4741f74b79725988cacfb1e13f3eb2025fd19d884fe2943b893facc850ae06
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P1-S1-C10
      - Result passage disposed without unit P2-S1-C11
      - Result passage disposed without unit P2-S1-C13
      - Result passage disposed without unit P2-S1-C14
      - Result passage disposed without unit P3-S1-C13
      - Result passage disposed without unit P4-S1-C1
      - Result passage disposed without unit P4-S1-C3
      - Result passage disposed without unit P4-S1-C4
      - Result passage disposed without unit P4-S1-C6
      - Result passage disposed without unit P4-S1-C7
      - Result passage disposed without unit P4-S1-C8
      - Result passage disposed without unit P4-S1-C9
      - 'window 5: invalid/duplicate disposition P4-S2-C11'
      - Result passage disposed without unit P5-S2-C4
      - Result passage disposed without unit P5-S2-C5
      - Result passage disposed without unit P6-S1-C5
      unattached_null_or_qualifier_ids:
      - P4-S1-C4
      - P5-S2-C5
      suppressed_nonrepresented_units: 33
      default_disposition_count_requires_completeness_check: 115
      unselected_timing_passages:
      - P5-S2-C11
      - P5-S3-C4
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P2-S2-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P2-S2-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P3-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P3-S1-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P3-S2-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P3-S2-C6
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
      - slot: dependent_variable_statement
        source_id: P4-S3-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P3-S2-C8
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P4-S2-C11
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P5-S2-C3
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: tested_personal_effects
        source_id: P3-S2-C2
        reason: No current-result classification; a covariate description is not an
          individual test
      empty_frame_slots_require_confirmation:
      - validation
      - dependent_variable_statement
      - explicitly_not_adjusted
      unclassified_extraction_ids:
      - P1-S1-C13
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
        - P3-S2
        - P3-S3
        - P4-S1
        - P4-S2
        - P4-S3
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: fde000e1fc86d9993dac4c418d93e4566c4c0521ed6bb3c80efba23a81a521ca
      source_review: _compare/relationships-2026-11-16/review-current/Wilson2011
      source_status_sha256: af4741f74b79725988cacfb1e13f3eb2025fd19d884fe2943b893facc850ae06
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C8
      disposition: represented
      result_indexes:
      - 0
      reason: Summary of SLF/Arcuate association with syntactic deficits.
    - source_id: P1-S1-C9
      disposition: represented
      result_indexes:
      - 4
      - 6
      reason: Summary of prediction after gray matter atrophy adjustment.
    - source_id: P1-S1-C10
      disposition: represented
      result_indexes:
      - 1
      - 2
      reason: Summary of null association for ventral tracts.
    - source_id: P2-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes tract identification in patients.
    - source_id: P2-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison to previous studies.
    - source_id: P2-S1-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes behavioral measure range.
    - source_id: P2-S1-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive statistics of scores.
    - source_id: P2-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Correlation between comprehension and production scores (not exposure-outcome).
    - source_id: P2-S2-C4
      disposition: represented
      result_indexes:
      - 0
      reason: Direct result for left SLF/Arcuate FA and syntax.
    - source_id: P2-S2-C5
      disposition: represented
      result_indexes:
      - 1
      - 2
      reason: Direct null results for ECFS and UF FA and syntax.
    - source_id: P2-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Correlation between left and right SLF/Arcuate FA.
    - source_id: P3-S1-C2
      disposition: represented
      result_indexes:
      - 3
      reason: Left SLF/Arcuate prediction in hemispheric model.
    - source_id: P3-S1-C3
      disposition: represented
      result_indexes:
      - 3
      reason: Right SLF/Arcuate null prediction in hemispheric model.
    - source_id: P3-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: General association of mediating factors with syntax.
    - source_id: P3-S1-C13
      disposition: represented
      result_indexes:
      - 4
      reason: Prediction of SLF/Arcuate in full model with mediating factors.
    - source_id: P3-S2-C4
      disposition: represented
      result_indexes:
      - 5
      reason: VBM correlation of left IFG and syntax.
    - source_id: P3-S2-C5
      disposition: represented
      result_indexes:
      - 6
      reason: SLF/Arcuate prediction adjusted for IFG volume.
    - source_id: P3-S2-C6
      disposition: represented
      result_indexes:
      - 6
      reason: IFG volume as a significant predictor in the same model.
    - source_id: P3-S2-C10
      disposition: represented
      result_indexes:
      - 7
      reason: Results for constrained tracts.
    - source_id: P3-S3-C1
      disposition: represented
      result_indexes:
      - 7
      reason: Specific values for constrained SLF/Arcuate and ECFS.
    - source_id: P3-S3-C2
      disposition: represented
      result_indexes:
      - 0
      reason: Figure 2 caption restating SLF/Arcuate association.
    - source_id: P3-S3-C3
      disposition: represented
      result_indexes:
      - 1
      - 2
      reason: Figure 2 caption restating null results for ECFS and UF.
    - source_id: P4-S1-C1
      disposition: represented
      result_indexes:
      - 7
      reason: Null result for constrained ECFS.
    - source_id: P4-S1-C3
      disposition: represented
      result_indexes:
      - 8
      reason: Null association between SLF/Arcuate and lexical measures.
    - source_id: P4-S1-C4
      disposition: represented
      result_indexes:
      - 9
      - 10
      reason: Ventral tract association with lexical measures and subsequent loss
        of effect after adjustment.
    - source_id: P4-S1-C6
      disposition: repeated
      result_indexes:
      - 0
      reason: Discussion restatement of SLF/Arcuate correlation.
    - source_id: P4-S1-C7
      disposition: repeated
      result_indexes:
      - 1
      - 2
      reason: Discussion restatement of ventral tract nulls.
    - source_id: P4-S1-C8
      disposition: repeated
      result_indexes:
      - 4
      reason: Discussion restatement of SLF/Arcuate effect with covariates.
    - source_id: P4-S1-C9
      disposition: repeated
      result_indexes:
      - 4
      - 6
      reason: Discussion restatement of SLF/Arcuate effect with specific covariates.
    - source_id: P4-S2-C10
      disposition: represented
      result_indexes:
      - 5
      - 6
      reason: Figure 3 caption restating IFG and SLF/Arcuate results.
    - source_id: P4-S3-C2
      disposition: represented
      result_indexes:
      - 7
      reason: Figure 3 caption restating constrained tract results.
    - source_id: P4-S3-C4
      disposition: represented
      result_indexes:
      - 8
      reason: Figure 4 caption restating SLF/Arcuate lexical nulls.
    - source_id: P5-S1-C4
      disposition: repeated
      result_indexes:
      - 1
      - 2
      reason: Discussion restatement of null role of ventral tracts in grammar.
    - source_id: P5-S1-C5
      disposition: repeated
      result_indexes:
      - 1
      - 2
      reason: Discussion restatement of null correlations for ventral tracts.
    - source_id: P5-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Mentions association with motor speech deficits (details in supplement).
    - source_id: P5-S2-C3
      disposition: repeated
      result_indexes:
      - 7
      reason: Discussion restatement of constrained ECFS null result.
    - source_id: P5-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion statement.
    - source_id: P5-S2-C5
      disposition: repeated
      result_indexes:
      - 0
      reason: General conclusion restating SLF/Arcuate role.
    - source_id: P6-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Inter-rater reliability for production scores.
    - source_id: P6-S1-C11
      disposition: represented
      result_indexes:
      - 5
      reason: Definition of the IFG ROI based on correlation with syntax.
    unresolved_coverage: []
    pending_source_ids:
    - P1-S1-C8
    - P1-S1-C9
    - P1-S1-C10
    - P2-S1-C11
    - P2-S1-C12
    - P2-S1-C13
    - P2-S1-C14
    - P2-S2-C2
    - P2-S2-C8
    - P3-S1-C11
    - P3-S2-C6
    - P3-S2-C10
    - P4-S1-C1
    - P4-S1-C6
    - P4-S1-C7
    - P4-S1-C8
    - P4-S1-C9
    - P5-S1-C4
    - P5-S1-C5
    - P5-S1-C9
    - P5-S2-C3
    - P5-S2-C4
    - P5-S2-C5
    - P6-S1-C5
    - P6-S1-C11
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
      - P5-S2-C9
      recruited_sample:
      - P5-S2-C7
      eligibility:
      - P5-S2-C10
      imaging_provenance:
      - P2-S1-C3
      - P5-S3-C8
      - P6-S2-C3
      imaging_timing:
      - P5-S3-C8
      outcome_timing:
      - P5-S3-C8
      outcome_definition:
      - P2-S1-C2
      - P5-S3-C14
      validation: []
      analysis_restrictions:
      - P3-S1-C5
      - P3-S2-C8
      - P4-S3-C2
      dependent_variable_statement: []
      limitations:
      - P5-S1-C10
      - P5-S1-C11
      - P5-S1-C12
      - P5-S2-C2
      personal_factors:
      - P3-S1-C7
      - P3-S1-C8
      - P3-S1-C9
      - P5-S2-C11
      - P5-S2-C12
      - P5-S3-C4
      tested_personal_effects:
      - P3-S1-C11
      - P3-S1-C13
      - P4-S1-C4
      - P5-S1-C9
      adjustment_roles:
      - P3-S1-C12
      - P3-S2-C5
      - P4-S1-C4
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P5-S2-C11
      - P5-S2-C12
      - P5-S3-C4
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: internal_cross_validation
    held_selections:
    - slot: dependent_variable_statement
      source_id: P2-S2-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P2-S2-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P3-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P3-S1-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P3-S2-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P3-S2-C6
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
    - slot: dependent_variable_statement
      source_id: P4-S3-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P3-S2-C8
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P4-S2-C11
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P5-S2-C3
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: tested_personal_effects
      source_id: P3-S2-C2
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
      pdf_sha256: fde000e1fc86d9993dac4c418d93e4566c4c0521ed6bb3c80efba23a81a521ca
      review_sha256: 0a3762230cc0b271757dc962cf171f38e255399758a8c4a2d1495004a1fcca72
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
      - P3-S2-C5
      source_result: In the analysis adjusting for gray matter volumes in the left
        inferior frontal gyrus (IFG), FA in the left SLF/Arcuate continued to predict
        syntactic comprehension (partial r = 0.40, p = 0.042) and production (partial
        r = 0.60, p = 0.0013). The source notes that gray matter volume was also a
        significant predictor in these models.
      result_status: detected
      patient_measurement: patient_diffusion
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis (R007) is identified by evidence P3-S2-C5,
            which describes the model including gray matter volumes in the IFG as
            a covariate. The proposed core correctly identifies this specific adjusted
            analysis, distinguishing it from the unadjusted correlations (P2-S2-C4)
            or the full mediating factors model (P3-S1-C13).
          source_ids:
          - P3-S2-C5
          - P3-S2-C3
        direction:
          answer: fits
          reason: The source states that 'FA in the left SLF/Arcuate continued to
            predict' deficits, with positive partial correlations (r=0.40, r=0.60)
            between FA and scores (where lower scores indicate deficits, implying
            reduced FA is associated with deficits). The proposed claim 'Reduced FA...
            is associated with deficits' preserves this directionality. The 'remains
            significant' clause is supported by the p-values in P3-S2-C5.
          source_ids:
          - P3-S2-C5
          - P3-S2-C7
        construct:
          answer: fits
          reason: The exposure is correctly identified as left SLF/Arcuate FA. The
            outcome is syntactic comprehension and production. The method is DTI.
            The patient measurement is patient_diffusion because the FA values are
            derived from individual patient tractography (seeded on individual color-coded
            maps, P5-S3-C9), not from a template overlay or population map. The proposed
            core correctly defines the exposure as mean FA of the left SLF/Arcuate.
          source_ids:
          - P2-S1-C2
          - P5-S3-C14
          - P5-S3-C9
        qualifications:
          answer: fits
          reason: The proposed core includes the qualification that the analysis is
            adjusted for gray matter volumes in the left IFG, which is the specific
            covariate in P3-S2-C5. It also lists other adjustments (PPA variant, severity,
            etc.) which are part of the broader robustness checks described in P3-S1-C12
            and P3-S1-C13, though P3-S2-C5 specifically isolates the gray matter adjustment.
            Including the broader context is acceptable as it does not misrepresent
            the specific result in P3-S2-C5, but the primary qualification for this
            specific evidence ID is the gray matter adjustment.
          source_ids:
          - P3-S2-C5
          - P3-S2-C6
          - P3-S1-C12
        missing_material_caveat:
          answer: fits
          reason: The source P3-S2-C6 notes that gray matter volume was also a significant
            predictor. The proposed core does not explicitly state that gray matter
            was a significant predictor, but it does not claim it was not. The core
            focuses on the SLF/Arcuate's predictive power. The limitation regarding
            subcomponents (P5-S1-C12) is included. No material caveat that changes
            the interpretation of the SLF/Arcuate result is omitted.
          source_ids:
          - P3-S2-C6
          - P5-S1-C12
      optional_pending:
      - Specific p-values and F-statistics for the gray matter adjusted model are
        not transcribed in the core fields, but are present in source P3-S2-C5.
      - The specific MNI coordinates for the IFG ROI are not transcribed, but are
        present in source P6-S1-C11.
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Specific p-values and F-statistics for the gray matter adjusted model are not
      transcribed in the core fields, but are present in source P3-S2-C5.
    - The specific MNI coordinates for the IFG ROI are not transcribed, but are present
      in source P6-S1-C11.
    normalizations:
    - field: bucket
      original: predictors
      action: route_from_kind
      value: regions
    analysis_identity:
      id: R007
      exposure:
        text: left SLF/Arcuate FA
      outcome:
        text: syntactic comprehension and production
      analysis_label: Prediction adjusted for gray matter atrophy
      relation: sensitivity
      evidence_ids:
      - P3-S2-C5
      qualifier_ids:
      - P3-S2-C6
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: fde000e1fc86d9993dac4c418d93e4566c4c0521ed6bb3c80efba23a81a521ca
        source_review: _compare/relationships-2026-11-16/review-current/Wilson2011
        source_status_sha256: af4741f74b79725988cacfb1e13f3eb2025fd19d884fe2943b893facc850ae06
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P5-S2-C7:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: fde000e1fc86d9993dac4c418d93e4566c4c0521ed6bb3c80efba23a81a521ca
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 4479edff2a45224f467e1b0795c6881828fc0601c3260bfbede93642e4778188
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P5-S2-C7
          page: 5
          text_layer_sha256: 4479edff2a45224f467e1b0795c6881828fc0601c3260bfbede93642e4778188
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'EXPERIMENTAL PROCEDURES

          Participants

          We studied 27 patients with PPA, recruited through the Memory and Aging

          Center at the University of California, San Francisco (UCSF).'
        anchor_text: 'EXPERIMENTAL PROCEDURES

          Participants

          We studied 27 patients with PPA, recruited through the Memory and Aging

          Center at the University of California, San Francisco (UCSF).'
        excluded_fragments: []
        image_sha256: 4d3a2aea437ee0a2fd4fddb2863889c8ad2eeabf35fbfec3150cb92063d5aab1
        transcription: 'EXPERIMENTAL PROCEDURES


          Participants

          We studied 27 patients with PPA, recruited through the Memory and Aging
          Center at the University of California, San Francisco (UCSF)'
      P5-S2-C9:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: fde000e1fc86d9993dac4c418d93e4566c4c0521ed6bb3c80efba23a81a521ca
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: f94528d2496be9320f04043fa10c2f588c563a01d0987c92b10718f7d7db12ac
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P5-S2-C9
          page: 5
          text_layer_sha256: f94528d2496be9320f04043fa10c2f588c563a01d0987c92b10718f7d7db12ac
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Patients were classiﬁed into one of three

          PPA variants: nonﬂuent (n = 11), semantic (n = 10), and logopenic (n = 6).'
        anchor_text: 'Patients were classiﬁed into one of three

          PPA variants: nonﬂuent (n = 11), semantic (n = 10), and logopenic (n = 6).'
        excluded_fragments: []
        image_sha256: 973126b1cc551c461d2a6082ec3c1d41b41307920b114ed0c29a41a0cd9ec709
        transcription: '. Patients were classified into one of three

          PPA variants: nonfluent (n = 11), semantic (n = 10), and logopenic (n =
          6)'
      P5-S3-C4:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: fde000e1fc86d9993dac4c418d93e4566c4c0521ed6bb3c80efba23a81a521ca
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 8fb51dd62ac94965662fa9e92cf400674bd5cff0b63d04807bd16afbb1b5f798
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P5-S3-C4
          page: 5
          text_layer_sha256: 8fb51dd62ac94965662fa9e92cf400674bd5cff0b63d04807bd16afbb1b5f798
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'The mean MMSE score

          was 24.0 (SD = 5.3, range = 8–30), and the mean years since onset of disease

          was 5.6 (SD = 2.9, range = 2–13).'
        anchor_text: 'The mean MMSE score

          was 24.0 (SD = 5.3, range = 8–30), and the mean years since onset of disease

          was 5.6 (SD = 2.9, range = 2–13).'
        excluded_fragments: []
        image_sha256: b33b4338c7a7efbe9391776ffd90b14ddb832431d32b417b9654bc682d07707e
        transcription: '. The mean MMSE score

          was 24.0 (SD = 5.3, range = 8–30), and the mean years since onset of disease

          was 5.6 (SD = 2.9, range = 2–13)'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 2
  quote: 'DTI Correlates of Syntactic Deﬁcits

    In the left SLF/Arcuate, reduced FA was strongly

    associated

    with

    deﬁcits

    in

    both

    syntactic

    comprehension (r = 0.61, F[1, 25] = 14.81, p =

    0.0007, Figure 2A) and production (r = 0.73, F[1, 25] = 28.00,

    p < 0.0001, Figure 2B).'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-26'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
