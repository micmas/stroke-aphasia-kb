---
id: overall_emotion_identification_model
name: Overall emotion identification model
kind: predictor
findings:
- id: f1
  target: overall_emotional_prosody_identification_accuracy
  target_kind: impairment
  claim: The multivariable model for overall emotion identification was significant,
    with older age and greater damage to the right posterior STG acting as individual
    predictors of impairment.
  direction: likely
  relationship: correlational
  method: LSM
  sample:
    n: 23
    population: patients with acute unilateral right hemisphere ischemic stroke
    phase: not_reported
    time_post_onset: tested within 5 days of stroke
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Small sample size
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: A multivariable linear regression model including
    percent damage to proposed right hemisphere ventral stream structures (posterior
    STG, STG, temporal pole, IFG pars orbitalis, lateral OFC, amygdala, and sagittal
    stratum), age, education, and total lesion volume, where percent damage was measured
    as patient lesion overlap with the Johns Hopkins University atlas. The model accounted
    for approximately 52% of the variance (adjusted r2 = 0.52). Additional metadata
    has not been transcribed; review the pending-field flags before approval. PDF
    image reading (P2-S1-C6, two-model agreement, human verification pending): . We
    evaluated this

    hypothesis by examining relationships between damage to

    these structures and performance on an emotional prosody

    recognition task in a group of 23 patients with acute stroke Original text-layer
    quotation is preserved below. PDF image reading (P2-S2-C7, two-model agreement,
    human verification pending): . At the acute time

    point, 23 patients were tested within 5 days of stroke Original text-layer quotation
    is preserved below.'
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
    - proposed_concept:overall_emotional_prosody_identification_accuracy
  citation: '@Sheppard2020'
  source_passages:
  - section: Original source P1-S1-C12
    page: 1
    quote: 'Results

      The overall emotion identiﬁcation model was signiﬁcant (adjusted r2 = 0.52;
      p = 0.043); greater

      damage to right posterior STG (p = 0.038) and older age (p = 0.009) were individual
      predictors

      of impairment.'
    supports: claim
  - section: Original source P2-S1-C6
    page: 2
    quote: 'We evaluated this

      hypothesis by examining relationships between damage to

      these structures and performance on an emotional prosody

      recognition task in a group of 23 patients with acute stroke.'
    supports: sample
  - section: Original source P2-S2-C7
    page: 2
    quote: 'At the acute time

      point, 23 patients were tested within 5 days of stroke.'
    supports: method
  - section: Original source P3-S2-C2
    page: 3
    quote: 'The following independent variables were

      entered into the initial model: percent damage to each of 7

      regions of interest (posterior STG, STG, temporal pole, IFG

      pars orbitalis, lateral OFC, amygdala, sagittal stratum), overall

      lesion volume, age, and education.'
    supports: method
  - section: Original source P4-S1-C2
    page: 4
    quote: 'The model for overall emotion identiﬁcation was sig-

      niﬁcant, F10,10 = 3.15, p = 0.043, and accounted for

      approximately 52% of the variance (r2 = 0.76, adjusted r2 =

      0.52) (table 1).'
    supports: claim
  - section: Original source P4-S1-C3
    page: 4
    quote: 'Individual predictors of overall emotion

      identiﬁcation impairment were older age (p = 0.009) and

      greater damage to posterior STG (p = 0.038) (ﬁgure 2A).'
    supports: claim
predictor_type: imaging_metric
short_definition: A multivariable linear regression model including percent damage
  to proposed right hemisphere ventral stream structures (posterior STG, STG, temporal
  pole, IFG pars orbitalis, lateral OFC, amygdala, and sagittal stratum), age, education,
  and total lesion volume, where percent damage was measured as patient lesion overlap
  with the Johns Hopkins University atlas.
assessment:
- emotional prosody recognition task
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-25'
relationship_review:
  paper: Sheppard2020
  proposal_id: R006
  review_status_sha256: c758ade517f738742f073a8a84eb4bb4eb1626f6d31222cd998fce604a015ceb
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: b56add7cf1ba46bb2681949ae5c13dd2a0e77a66ecc9b28bbe363da2abb83924
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: b56add7cf1ba46bb2681949ae5c13dd2a0e77a66ecc9b28bbe363da2abb83924
        A/passages.json: 4fc5624af8fb02bceea86ec395237724552cfe87183af50b98330bd80bb8e82b
        A/raw.json: f5b7f0047623b8dc17b219cd276f330ccad56a2b1d8a54075de05a2f4ff27f72
        A/source-units.json: 9eb772aa6190a7eed5d8024a39fef75893c6b59e528ab861028e7c4fdd753a63
        A/full-source-units.json: b6c4bd62d67a011b338f754b6f1e0c40ea0871076d009e6782683d1e8b844d41
        A/meta.json: 29fd8428df6af006f24aa4ae000b64e9024e0fb824a5288500e60efe2e470f39
        A/table-images/page-5.png: 9ea32e6237ced40b4459615832b5d5778db43cac3a63660e8216dcb8b43db9c0
        A/table-images/page-4.png: 8d8d9677f2df26b7b7a03f9d02a07175a79d891bfa341e99a88167b1dd272b0a
        A/table-images/TABLE-1-page-4-1.png: 6460229f17b82870f5a64c539a5bd05dc2fab0e96516701aecc7642f5f29019e
        A/table-images/manifest.json: c0cd5917dfc8115f28bf6ffab4ec948bedfac1b44f82eb8c04de8430f0b97291
        A/table-images/TABLE-2-page-5-1.png: 4b776ceac8f79128691746d8a6f3c9fe914151b855eb5554b464e0a5a9f9faac
        A/clauses/window-03/raw.json: a786afdc0097a757b7aaf5f45ea6f7951d2a9707fdc041ad716338e6dfcccc4f
        A/clauses/window-03/prompt.txt: 6a10f2fad4c14ef3d1cdfe89f83b221f7c616b1740e742ba7ee4babdd96c7303
        A/clauses/window-03/meta.json: 9698184546ca3948cd7e9414eeeab49d2d017778512cbee442bc02d17a0c7bbf
        A/clauses/window-04/raw.json: 45f1bd6b85c67eee20aaefb8762f40348a511323d23b76feac963b0bcb52f0ed
        A/clauses/window-04/prompt.txt: 6f518df7283699881584a40d95cb5cd726c9ddaf34fe334b6d968058107cd5f6
        A/clauses/window-04/meta.json: b37a17680ef4e8e531c2b45b316d396ac89fa82814ce2103da0fd1b1b794efe2
        A/clauses/window-05/raw.json: a4d641c038c697a7b58ce8093fbc8afd0dca086e23a6ca8c500a9234d7ee49c0
        A/clauses/window-05/prompt.txt: aae21d7b8e5ad6a0e9e60ffb21252dd4b8898f4837ecf5636c1d95b9d744a00e
        A/clauses/window-05/meta.json: 98592cd9c9212dcf994906be488afce6af8889e1323da2abc800e19b2449692f
        A/clauses/window-02/raw.json: 8d350beaef9b0734a4985a57b030a4a5194ca0867195adf47a50c177e5737b3e
        A/clauses/window-02/prompt.txt: 2136235a68a3dd37096a697f26c01c1d480222108f66e847caa35c62e5fd45d6
        A/clauses/window-02/meta.json: d35799023ecc05a176dc167467f5e4e5c1244969abf48b726287d386779004d1
        A/clauses/window-07/raw.json: f213cdf31f190e6887e870c474a6e24024b344f0d5a963449fe8d36bb2a3e2c7
        A/clauses/window-07/prompt.txt: 535d83e9ce11610e883acd27017931ed31c6e3e547f63cb448b8487dbcf45c4c
        A/clauses/window-07/meta.json: 8149fff4681e06a9d2986c39d977b4a4a49f56641cf2760cf4ebf63d8ea7c651
        A/clauses/window-01/raw.json: d34f6e8f75955c77c75456e0f4dc1d4a417ba1d457d51ff1c3d5cc9ffcb73952
        A/clauses/window-01/prompt.txt: 1d4728e3ec4331ed2bd30f59b57cc8d32f6c260f50a196590f8f1ad6ef93a9ea
        A/clauses/window-01/meta.json: a61236a9f37e2543ae1268b71e8af500396b4a2cad54947d6a9879560e1a2043
        A/clauses/window-06/raw.json: 340240db1c4ac440357fd643c4565e387d58134eab5ec29af0df08715574b490
        A/clauses/window-06/prompt.txt: 2575bc11d1447c592475b8276d97269c98369cf93040a0af174661f4bec1bb0f
        A/clauses/window-06/meta.json: a6664fc7447728e773e4dc146dbef7fb01c261521a28ef679f0e28b842da05f4
        A/clauses/window-08/raw.json: fcbea05b6ec87c39548a2ec6928715b99f2bd53ea3487e3579a05930a8320e96
        A/clauses/window-08/prompt.txt: b3b247472c5e71d424884bb7e0c1ab7a712a605bfcd3c3200cc8983f83dc45e5
        A/clauses/window-08/meta.json: d50cdefdd0f0165067f54fddd1a708c88bd183ff3eea96e43671d2998bfc4f18
        A/tables/TABLE-2-page-5-2/raw.json: 47ab38fe2e5ddcb9455c6798286682fb37839a28f75e6cf07b08b3e95ec176a2
        A/tables/TABLE-2-page-5-2/prompt.txt: 2044ca24f1a13d7a7cd6c4474b62c849411a955f227b2492c3787ef797584ac7
        A/tables/TABLE-2-page-5-2/meta.json: d80d02b9d6f4111de9188d6e4e0cd1c2d85beb78face45b6c8c6340931c09a72
        A/tables/TABLE-1-page-4-1/raw.json: a05eb3631fffb618b2a84d937dc21ebc379fc66f3f7b55890c38dfccb89151cb
        A/tables/TABLE-1-page-4-1/prompt.txt: c8899e0817f304fa05c5edf0486e4cf87f44e38620544cced8c06b8660e49b6f
        A/tables/TABLE-1-page-4-1/meta.json: 1d1f9f6d8e003937969e3eaf4bf60102f5442080510e0c50bb41a3d2fa073f4e
        B/passages.json: 4fc5624af8fb02bceea86ec395237724552cfe87183af50b98330bd80bb8e82b
        B/raw.json: fde411db8ab0fcb077d2e5366d63948caa1280cacd7af5dbd197905a2d677619
        B/source-units.json: 9eb772aa6190a7eed5d8024a39fef75893c6b59e528ab861028e7c4fdd753a63
        B/full-source-units.json: b6c4bd62d67a011b338f754b6f1e0c40ea0871076d009e6782683d1e8b844d41
        B/meta.json: fba5c2d70d477e18404a9b665b8c54a8aa1ae95e9bb575efe06afd09e0e114d3
        B/table-images/page-5.png: 9ea32e6237ced40b4459615832b5d5778db43cac3a63660e8216dcb8b43db9c0
        B/table-images/page-4.png: 8d8d9677f2df26b7b7a03f9d02a07175a79d891bfa341e99a88167b1dd272b0a
        B/table-images/TABLE-1-page-4-1.png: 6460229f17b82870f5a64c539a5bd05dc2fab0e96516701aecc7642f5f29019e
        B/table-images/manifest.json: 5f4e9eb296b513f933eb511f2ffa8cf0e2c44ffa84097d0bbabad298450127de
        B/table-images/TABLE-2-page-5-1.png: 4b776ceac8f79128691746d8a6f3c9fe914151b855eb5554b464e0a5a9f9faac
        B/clauses/window-03/raw.json: 660deebeb11200aba8e27a514e868823f1b31e47ff8fadee7660c6e7e85da8f7
        B/clauses/window-03/prompt.txt: 6a10f2fad4c14ef3d1cdfe89f83b221f7c616b1740e742ba7ee4babdd96c7303
        B/clauses/window-03/meta.json: 1920b364bdaf73c5a376759b9fd26391a17102bd0177bf6ee441508226c98cbf
        B/clauses/window-04/raw.json: b87b2d46e76133f580c5b7d8272a2616b40c4819f32dad78dcf12b85239c56f1
        B/clauses/window-04/prompt.txt: 6f518df7283699881584a40d95cb5cd726c9ddaf34fe334b6d968058107cd5f6
        B/clauses/window-04/meta.json: 5a461de00f8ef7721d9217b987d0bf5409e24bdc883a84810076ceac3adcf91d
        B/clauses/window-05/raw.json: ff82fd3aa84ca4878994f17035beb68bea8d4ae23f9c4c4b18fc92a7eed9f295
        B/clauses/window-05/prompt.txt: aae21d7b8e5ad6a0e9e60ffb21252dd4b8898f4837ecf5636c1d95b9d744a00e
        B/clauses/window-05/meta.json: 43f51d37b29e64406208fe71dd24ba8a15cd88f3af7be1f5107259c077f18e68
        B/clauses/window-02/raw.json: 9a20b5268d9e8d8e52387231332cd1c304a45db45a5e7a0121b8aa6881790f38
        B/clauses/window-02/prompt.txt: 2136235a68a3dd37096a697f26c01c1d480222108f66e847caa35c62e5fd45d6
        B/clauses/window-02/meta.json: 0d2aebaf84b897a6f69bc0b68fb1c5f01ad273fe96eccec3b989ac22b120703f
        B/clauses/window-07/raw.json: 35893c48ab5f121891b3aa1a82fe31495164d4e6e7ea9d18725b4dca69c64478
        B/clauses/window-07/prompt.txt: 535d83e9ce11610e883acd27017931ed31c6e3e547f63cb448b8487dbcf45c4c
        B/clauses/window-07/meta.json: c3f4c6362a848e3fefe53f45d36a8cb7097ac93183fddebca041c258660f7f14
        B/clauses/window-01/raw.json: 2d38c346ac890aef99284ba59c03327fa38432ceae4c07b63f4f686cf7aade72
        B/clauses/window-01/prompt.txt: 1d4728e3ec4331ed2bd30f59b57cc8d32f6c260f50a196590f8f1ad6ef93a9ea
        B/clauses/window-01/meta.json: c326c11a2320a3884c870949283b89d1cdb07b4e0d57eb56efa057068f16ea35
        B/clauses/window-06/raw.json: de3a4f8d0f1ade9721a1772f38f99cacca53fa83f0ba0de41520266765c6cfdc
        B/clauses/window-06/prompt.txt: 2575bc11d1447c592475b8276d97269c98369cf93040a0af174661f4bec1bb0f
        B/clauses/window-06/meta.json: 7b33c3ed346c3964d6d92b479d0bbd4011191fb0bffd01586336650240fc638f
        B/clauses/window-08/raw.json: 5a575df476f06b9740d50b7cddb6b4b3146be51ec33c53bfb3140c3b20b6bd63
        B/clauses/window-08/prompt.txt: b3b247472c5e71d424884bb7e0c1ab7a712a605bfcd3c3200cc8983f83dc45e5
        B/clauses/window-08/meta.json: c668ec100586d7dd1be403e4bd15ec5a741a9b00519ac579b7b39ae525437309
        B/tables/TABLE-2-page-5-2/raw.json: be7fcbf99c962b111a904e6befc7abab16d4f0ecaf6ebe6a77110422a52d5ff7
        B/tables/TABLE-2-page-5-2/prompt.txt: 2044ca24f1a13d7a7cd6c4474b62c849411a955f227b2492c3787ef797584ac7
        B/tables/TABLE-2-page-5-2/meta.json: d86f3d2ea5bd6ec09f02540c2b228adbb6f650030f1f9af3378a5ab6d763aed2
        B/tables/TABLE-1-page-4-1/raw.json: b2bc7b63e413efb4f471ae42c415f9baccbf92876195052b8bbba70aa4be43df
        B/tables/TABLE-1-page-4-1/prompt.txt: c8899e0817f304fa05c5edf0486e4cf87f44e38620544cced8c06b8660e49b6f
        B/tables/TABLE-1-page-4-1/meta.json: 66bc50ff813f1e71e11de6770fdc2592315be9dde69795b1e904adbd06e6d669
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
      pdf_sha256: b56add7cf1ba46bb2681949ae5c13dd2a0e77a66ecc9b28bbe363da2abb83924
      source_review: _compare/relationships-2026-11-16/review-current/Sheppard2020
      source_status_sha256: 29effd7d06a484666440de71439b0fe70f4a816452843fd30d1d9c81e05cbd98
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R006
    exposure:
      text: RH ventral stream structures, age, education, and lesion volume
    outcome:
      text: overall emotional prosody identification accuracy
    analysis_label: Overall emotion identification model performance
    relation: performance
    evidence_ids:
    - P1-S1-C12
    - P4-S1-C2
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
      pdf_sha256: b56add7cf1ba46bb2681949ae5c13dd2a0e77a66ecc9b28bbe363da2abb83924
      source_review: _compare/relationships-2026-11-16/review-current/Sheppard2020
      source_status_sha256: 29effd7d06a484666440de71439b0fe70f4a816452843fd30d1d9c81e05cbd98
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P2-S2-C2
      - Result passage disposed without unit P2-S2-C3
      - Result passage disposed without unit P2-S2-C4
      - Result passage disposed without unit P2-S2-C5
      - Result passage disposed without unit P3-S2-C10
      - Result passage disposed without unit P3-S2-C8
      - Result passage disposed without unit P3-S2-C9
      - Result passage disposed without unit P3-S3-C1
      - Result passage disposed without unit P4-S1-C1
      - Result passage disposed without unit P4-S1-C2
      - Result passage disposed without unit P4-S2-C5
      - Result passage disposed without unit P4-S2-C6
      - Result passage disposed without unit P4-S2-C7
      - Result passage disposed without unit P4-S2-C8
      - Result passage disposed without unit P4-S2-C9
      - Result passage disposed without unit P4-S2-C10
      - Result passage disposed without unit P5-S1-C1
      - Result passage disposed without unit P5-S1-C5
      - Result passage disposed without unit P6-S1-C3
      - Result passage disposed without unit P6-S1-C4
      - Result passage disposed without unit P6-S1-C6
      - Result passage disposed without unit P6-S1-C11
      unattached_null_or_qualifier_ids:
      - P4-S2-C8
      - P4-S2-C9
      - P4-S2-C10
      - P5-S1-C5
      - P6-S1-C6
      - P6-S1-C11
      suppressed_nonrepresented_units: 7
      default_disposition_count_requires_completeness_check: 131
      unselected_timing_passages:
      - P2-S1-C6
      - P2-S1-C8
      - P2-S2-C7
      - P2-S2-C9
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P4-S1-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P2-S2-C9
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      empty_frame_slots_require_confirmation:
      - validation
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
        - P3-S3
        - P6-S2
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: b56add7cf1ba46bb2681949ae5c13dd2a0e77a66ecc9b28bbe363da2abb83924
      source_review: _compare/relationships-2026-11-16/review-current/Sheppard2020
      source_status_sha256: 29effd7d06a484666440de71439b0fe70f4a816452843fd30d1d9c81e05cbd98
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C12
      disposition: represented
      result_indexes:
      - 0
      - 6
      reason: Reports overall model significance and individual predictors (posterior
        STG, age).
    - source_id: P1-S1-C13
      disposition: represented
      result_indexes:
      - 1
      - 7
      reason: Reports fear model significance and individual predictors (amygdala,
        age, education).
    - source_id: P1-S1-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive statement about residual impairments in chronic stroke.
    - source_id: P2-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Demographic/clinical description of stroke territories.
    - source_id: P2-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Demographic description of stroke etiology.
    - source_id: P2-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Clinical description of visual neglect and other deficits.
    - source_id: P2-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Demographic description of medical history.
    - source_id: P3-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive mean accuracy for healthy controls.
    - source_id: P3-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive accuracy for individual emotions in controls.
    - source_id: P3-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive summary of control performance patterns.
    - source_id: P3-S2-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive statement on impairment prevalence in patients.
    - source_id: P3-S3-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Restatement of impairment prevalence.
    - source_id: P4-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive mean accuracy comparison.
    - source_id: P4-S1-C2
      disposition: represented
      result_indexes:
      - 0
      - 6
      reason: Provides F-statistic and variance for the overall model.
    - source_id: P4-S1-C3
      disposition: represented
      result_indexes:
      - 0
      reason: Identifies individual predictors for overall emotion identification.
    - source_id: P4-S1-C5
      disposition: represented
      result_indexes:
      - 2
      reason: Reports t-tests for posterior STG lesions and specific emotions.
    - source_id: P4-S1-C6
      disposition: represented
      result_indexes:
      - 3
      reason: Reports non-significance of the dorsal stream model for overall identification.
    - source_id: P4-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive mean accuracy for individual emotions in patients.
    - source_id: P4-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive pattern of accuracy.
    - source_id: P4-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive comparison to controls.
    - source_id: P4-S1-C10
      disposition: represented
      result_indexes:
      - 1
      - 7
      reason: Reports significance of the fear identification model.
    - source_id: P4-S1-C11
      disposition: represented
      result_indexes:
      - 1
      - 7
      reason: Reports variance for the fear identification model.
    - source_id: P4-S1-C12
      disposition: represented
      result_indexes:
      - 1
      reason: Identifies individual predictors for fear identification.
    - source_id: P4-S1-C13
      disposition: represented
      result_indexes:
      - 1
      reason: Explicit null finding for other predictors in the fear model.
    - source_id: P4-S1-C14
      disposition: represented
      result_indexes:
      - 4
      reason: Reports non-significance of dorsal stream models for individual emotions.
    - source_id: P4-S2-C3
      disposition: repeated
      result_indexes:
      - 4
      reason: Restatement of dorsal stream model non-significance.
    - source_id: P4-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive count of impaired patients.
    - source_id: P4-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive count of recovered patients.
    - source_id: P4-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive case of decline.
    - source_id: P4-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Imaging confirmation for a single case.
    - source_id: P4-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive count of recovery.
    - source_id: P4-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive count of improvement.
    - source_id: P5-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion statement.
    - source_id: P5-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to prior studies.
    - source_id: P5-S1-C3
      disposition: repeated
      result_indexes:
      - 0
      - 6
      reason: Restatement of overall model prediction.
    - source_id: P5-S1-C4
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of individual predictors for overall identification.
    - source_id: P5-S1-C5
      disposition: repeated
      result_indexes:
      - 1
      - 7
      reason: Restatement of fear model significance.
    - source_id: P5-S1-C6
      disposition: repeated
      result_indexes:
      - 1
      reason: Restatement of individual predictors for fear identification.
    - source_id: P5-S2-C5
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of posterior STG damage as an independent predictor.
    - source_id: P5-S2-C6
      disposition: repeated
      result_indexes:
      - 1
      reason: Restatement of amygdala role in fear recognition.
    - source_id: P5-S3-C2
      disposition: represented
      result_indexes:
      - 2
      reason: Table 2 data for posterior STG lesions and specific emotions.
    - source_id: P6-S1-C3
      disposition: repeated
      result_indexes:
      - 1
      reason: Restatement of education as a predictor for fear.
    - source_id: P6-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive observation of difficulty with fearful speech.
    - source_id: P6-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive counts of chronic stage recovery.
    - source_id: P6-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Study limitation regarding sample size.
    - source_id: P6-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive count of lesions in chronic group.
    - source_id: P6-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement of inability to determine chronic effect.
    unresolved_coverage:
    - source_id: P1-S1-C13
      disposition: unresolved
      reason: Unknown result index; not accepted as coverage
    - source_id: P4-S1-C10
      disposition: unresolved
      reason: Unknown result index; not accepted as coverage
    - source_id: P4-S1-C11
      disposition: unresolved
      reason: Unknown result index; not accepted as coverage
    - source_id: P4-S1-C14
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P5-S1-C5
      disposition: unresolved
      reason: Unknown result index; not accepted as coverage
    - source_id: P5-S2-C6
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P5-S3-C2
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    pending_source_ids:
    - P1-S1-C14
    - P2-S2-C2
    - P2-S2-C3
    - P2-S2-C4
    - P2-S2-C5
    - P3-S2-C8
    - P3-S2-C9
    - P3-S2-C10
    - P3-S2-C11
    - P3-S3-C1
    - P4-S1-C1
    - P4-S1-C7
    - P4-S1-C8
    - P4-S1-C9
    - P4-S1-C13
    - P4-S2-C3
    - P4-S2-C5
    - P4-S2-C6
    - P4-S2-C7
    - P4-S2-C8
    - P4-S2-C9
    - P4-S2-C10
    - P5-S1-C1
    - P5-S1-C2
    - P5-S1-C3
    - P5-S1-C4
    - P5-S1-C5
    - P5-S1-C6
    - P5-S2-C5
    - P6-S1-C3
    - P6-S1-C4
    - P6-S1-C6
    - P6-S1-C10
    - P6-S1-C11
    - P6-S1-C12
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
      - P2-S1-C6
      - P2-S2-C8
      - P3-S1-C11
      - P4-S2-C4
      recruited_sample:
      - P2-S1-C8
      - P2-S2-C7
      eligibility:
      - P2-S2-C6
      imaging_provenance:
      - P2-S3-C6
      imaging_timing:
      - P2-S3-C3
      outcome_timing:
      - P2-S1-C7
      - P2-S2-C8
      - P3-S1-C11
      - P4-S2-C4
      - P6-S1-C6
      outcome_definition:
      - P3-S1-C12
      validation: []
      analysis_restrictions:
      - P3-S2-C3
      dependent_variable_statement:
      - P3-S1-C12
      - P3-S2-C2
      - P3-S2-C5
      limitations:
      - P6-S1-C10
      - P6-S1-C11
      personal_factors:
      - P2-S2-C5
      tested_personal_effects:
      - P4-S1-C12
      - P5-S1-C6
      adjustment_roles:
      - P3-S2-C2
      - P3-S2-C5
      - P3-S2-C6
      - P4-S1-C4
      - P4-S1-C6
      - P5-S1-C3
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P2-S1-C8
      - P2-S2-C5
    outcome_type: both_reported
    imaging_vs_outcome: mixed
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P4-S1-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P2-S2-C9
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
      pdf_sha256: b56add7cf1ba46bb2681949ae5c13dd2a0e77a66ecc9b28bbe363da2abb83924
      review_sha256: c758ade517f738742f073a8a84eb4bb4eb1626f6d31222cd998fce604a015ceb
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
      - P1-S1-C12
      - P4-S1-C2
      source_result: The multivariable linear regression model for overall emotional
        prosody identification accuracy in acute right hemisphere stroke patients
        was significant (adjusted r2 = 0.52, p = 0.043). Greater damage to the right
        posterior superior temporal gyrus (p = 0.038) and older age (p = 0.009) were
        identified as individual predictors of impairment. The model included percent
        damage to ventral stream structures, age, education, and lesion volume.
      result_status: detected
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The proposed core correctly identifies the specific analysis as
            the multivariable linear regression model for 'overall emotion identification'
            (not individual emotions like fear). The source passages P1-S1-C12 and
            P4-S1-C2 confirm this is the model with adjusted r2 = 0.52 and p = 0.043,
            distinct from the fear model (P4-S1-C10/C11).
          source_ids:
          - P1-S1-C12
          - P4-S1-C2
          - P3-S1-C12
        direction:
          answer: fits
          reason: The claim states that older age and greater posterior STG damage
            are predictors of impairment. This aligns with the source text in P1-S1-C12
            ('greater damage... and older age... were individual predictors of impairment')
            and P4-S1-C3. The direction of association (damage/age -> lower accuracy/impairment)
            is preserved.
          source_ids:
          - P1-S1-C12
          - P4-S1-C3
        construct:
          answer: fits
          reason: The exposure is correctly defined as percent damage to RH ventral
            stream structures (specifically posterior STG), age, education, and lesion
            volume. The outcome is overall emotional prosody identification accuracy.
            The patient measurement is correctly identified as template_lesion_overlap,
            as the source (P2-S3-C6, P3-S1-C1) describes tracing lesions and calculating
            percent damage using the Johns Hopkins University atlas, rather than patient-specific
            diffusion tractography or functional imaging.
          source_ids:
          - P3-S2-C2
          - P2-S3-C6
          - P3-S1-C1
        qualifications:
          answer: fits
          reason: The proposed core includes the qualification that the model accounted
            for approximately 52% of variance (adjusted r2 = 0.52), which matches
            P4-S1-C2. It also notes the small sample size limitation, which is supported
            by P6-S1-C10. No material qualifiers are lost or misapplied.
          source_ids:
          - P4-S1-C2
          - P6-S1-C10
        missing_material_caveat:
          answer: fits
          reason: The core correctly restricts the finding to the acute time point
            (tested within 5 days, P2-S2-C7) and the specific population (acute RH
            ischemic stroke, P2-S1-C8). It does not incorrectly generalize to chronic
            patients or other emotions. The distinction between the overall model
            and the fear-specific model is maintained.
          source_ids:
          - P2-S2-C7
          - P2-S1-C8
          - P4-S1-C10
      optional_pending:
      - Specific p-values for non-significant predictors (e.g., education, lesion
        volume) in the overall model are not transcribed in the core but are available
        in Table 1 readings.
      - Exact F-statistic degrees of freedom (F10,10) are not explicitly in the core
        text but are in P4-S1-C2.
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Specific p-values for non-significant predictors (e.g., education, lesion volume)
      in the overall model are not transcribed in the core but are available in Table
      1 readings.
    - Exact F-statistic degrees of freedom (F10,10) are not explicitly in the core
      text but are in P4-S1-C2.
    normalizations: []
    analysis_identity:
      id: R006
      exposure:
        text: RH ventral stream structures, age, education, and lesion volume
      outcome:
        text: overall emotional prosody identification accuracy
      analysis_label: Overall emotion identification model performance
      relation: performance
      evidence_ids:
      - P1-S1-C12
      - P4-S1-C2
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
        pdf_sha256: b56add7cf1ba46bb2681949ae5c13dd2a0e77a66ecc9b28bbe363da2abb83924
        source_review: _compare/relationships-2026-11-16/review-current/Sheppard2020
        source_status_sha256: 29effd7d06a484666440de71439b0fe70f4a816452843fd30d1d9c81e05cbd98
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P2-S1-C6:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: b56add7cf1ba46bb2681949ae5c13dd2a0e77a66ecc9b28bbe363da2abb83924
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 4ac310e7ce9737c7d3b6c688f77189709b30515fdabd1763be3da794667f58f4
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S1-C6
          page: 2
          text_layer_sha256: 4ac310e7ce9737c7d3b6c688f77189709b30515fdabd1763be3da794667f58f4
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'We evaluated this

          hypothesis by examining relationships between damage to

          these structures and performance on an emotional prosody

          recognition task in a group of 23 patients with acute stroke.'
        anchor_text: 'We evaluated this

          hypothesis by examining relationships between damage to

          these structures and performance on an emotional prosody

          recognition task in a group of 23 patients with acute stroke.'
        excluded_fragments: []
        image_sha256: 96a15bfbf23e26b8e6df0a51be238650d600c0ea29e57fca7d34e0597ada2a3c
        transcription: '. We evaluated this

          hypothesis by examining relationships between damage to

          these structures and performance on an emotional prosody

          recognition task in a group of 23 patients with acute stroke'
      P2-S2-C7:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: b56add7cf1ba46bb2681949ae5c13dd2a0e77a66ecc9b28bbe363da2abb83924
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 6ec305b9d40b7c20c09f1737901419a472d1109b3dba860b29e2504f4631fd5b
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S2-C7
          page: 2
          text_layer_sha256: 6ec305b9d40b7c20c09f1737901419a472d1109b3dba860b29e2504f4631fd5b
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'At the acute time

          point, 23 patients were tested within 5 days of stroke.'
        anchor_text: 'At the acute time

          point, 23 patients were tested within 5 days of stroke.'
        excluded_fragments: []
        image_sha256: 5454f1d7c967d4809f737ad70a990794d32a0a13f39eb5df0f6eb624a19c156c
        transcription: '. At the acute time

          point, 23 patients were tested within 5 days of stroke'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 1
  quote: 'Results

    The overall emotion identiﬁcation model was signiﬁcant (adjusted r2 = 0.52; p
    = 0.043); greater

    damage to right posterior STG (p = 0.038) and older age (p = 0.009) were individual
    predictors

    of impairment.'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-25'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
