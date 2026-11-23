---
id: adjunctive_a_tdcs_speech_therapy
name: adjunctive anodal tDCS during speech therapy
kind: therapy
findings:
- id: f1
  target: correct_naming_of_common_objects
  target_kind: impairment
  claim: adjunctive anodal tDCS during speech therapy did not demonstrate a lack of
    superiority over sham tDCS in improving the correct naming of common objects,
    indicating that further study of the intervention is not futile
  direction: no_effect
  relationship: treatment_response
  method: clinical_RCT
  sample:
    n: 74
    population: individuals with long-term (>6 months) aphasia due to a single previous
      left hemisphere ischemic stroke
    phase: not_reported
    time_post_onset: 1 week posttreatment
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - study was not powered for superiority analyses to compare A-tDCS with S-tDCS
  - cannot assume treatment effect generalizes to functional communication abilities
    or quality of life
  evidence_quality: RCT
  strength: weak
  notes: 'Exposure measurement: 1mA anodal tDCS applied to the left temporal lobe
    region with the highest naming-related activation on fMRI, administered during
    the first 20 minutes of 15 speech therapy sessions (45 minutes each) over 3 weeks,
    compared to sham tDCS. intent-to-treat analysis adjusted for enrolling site and
    baseline aphasia severity (WAB-R AQ); futility design where the null hypothesis
    assumed a benefit of A-tDCS over sham tDCS. Additional metadata has not been transcribed;
    review the pending-field flags before approval. PDF image reading (P1-S1-C10,
    two-model agreement, human verification pending): . Patients with long-term (>6
    months) aphasia due to 1 previous left hemisphere stroke were enrolled Original
    text-layer quotation is preserved below. PDF image reading (P1-S1-C14, two-model
    agreement, human verification pending): RESULTS A total of 74 patients were enrolled
    Original text-layer quotation is preserved below.'
  imaging_details:
    reference_space: not_reported
    atlases_used: []
  lesion_mapping: {}
  provenance:
    extracted_by: model:gemma4:31b
    extracted_on: '2026-11-23'
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
    - proposed_concept:correct_naming_of_common_objects
  therapy:
    id: adjunctive_a_tdcs_speech_therapy
    name: adjunctive anodal tDCS during speech therapy
  citation: '@Fridriksson2018JAMA'
  source_passages:
  - section: Original source P1-S2-C4
    page: 1
    quote: 'The adjusted mean (SE) change from pretreatment baseline in correct naming
      was 13.9 (2.4)

      words (95% CI, 9.0-18.7) for A-tDCS and 8.2 (2.2) words (95% CI, 3.8-12.6) for
      sham tDCS,

      with mean (SE) A-tDCS difference of 5.7 (3.3) words (95% CI, −0.9 to 12.3),
      indicating a

      relative 70% increase in correct naming for A-tDCS relative to sham.'
    supports: claim
  - section: Original source P1-S2-C5
    page: 1
    quote: 'The futility hypothesis

      P value was .90, indicating failure to reject the null hypothesis and, therefore,
      providing no

      evidence that further study of A-tDCS is futile.'
    supports: claim
  - section: Original source P1-S1-C10
    page: 1
    quote: 'Patients with long-term

      (>6 months) aphasia due to 1 previous left hemisphere stroke were enrolled.'
    supports: sample
  - section: Original source P1-S1-C14
    page: 1
    quote: RESULTS A total of 74 patients were enrolled.
    supports: sample
  - section: Original source P1-S1-C12
    page: 1
    quote: 'INTERVENTIONS Outpatient speech therapy for 3 weeks (15 sessions, 45 minutes
      each)

      combined with either A-tDCS vs sham tDCS applied to preserved left temporal
      lobe regions.'
    supports: method
  - section: Original source P2-S3-C4
    page: 2
    quote: 'As our goal was to stimulate

      survivingeloquenttissue,theanodalelectrodewasplacedover

      the temporal lobe region with the highest naming related ac-

      tivation on the fMRI (for more details on the fMRI setup, see

      the study by Fridriksson5).'
    supports: method
  - section: Original source P3-S2-C9
    page: 3
    quote: 'Outcomes

      The primary end point was the change in the number of cor-

      rectly named common objects at 1 week posttreatment, mea-

      sured using a portion (Naming 80) of the trained items from

      the treatment plus the PNT.'
    supports: claim
  - section: Original source P4-S1-C1
    page: 4
    quote: '

      required sample size was inflated from 33 to 37 per group to

      account for the effect of the dropouts in the intent-to-treat

      analysis using an inflation factor.25

      The primary analysis was an intent-to-treat analysis and

      was adjusted for enrolling site and baseline aphasia severity

      measured as the AQ from the WAB-R.'
    supports: method
  - section: Original source P6-S2-C12
    page: 6
    quote: 'Therefore, we cannot conclude

      that A-tDCS is effective for boosting the effect of aphasia even

      though the magnitude of naming improvement was numeri-

      callygreaterwithA-tDCScomparedwithS-tDCS.Itisalsoalimi-

      tation that we cannot definitively determine that the naming

      '
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-23'
relationship_review:
  paper: Fridriksson2018JAMA
  proposal_id: R001
  review_status_sha256: 10fc94cadeea7045fee6f27116a0b664fc4660e62b1b0168a9d7e13c01528c77
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 6ae87a3b3c2f72929b0c8266e0d862caab741b6fb5c43b19a22b8581f06fcdb1
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 6ae87a3b3c2f72929b0c8266e0d862caab741b6fb5c43b19a22b8581f06fcdb1
        A/passages.json: c058c12d716a073b6f6a2b2d1690460d5adb60dc2348352e58bef1503559790a
        A/raw.json: 9c67b4a1190aac3ee6e8adfcd24373c2e790f075876038e4a1b03855f04af891
        A/source-units.json: cae54612c6d76b72e7bfb89fa9cc9c2a263e49c1afc12dcf73314d23ed34123c
        A/full-source-units.json: e2ee9283ae56002a9a0ff0f49efc6f32a09b089c63e1801ec72918ee7e71642a
        A/meta.json: ddb029469214cec60c98bc8a42539e1e65d4dcfba8b0f94d8156a0b9bfab5cac
        A/table-images/page-6.png: 97c7a627ee22d5031178c0db238a5274b005cb5c74f6fe7601eaa74e16ceecd2
        A/table-images/page-5.png: 5036562f4e14911f22df72d181c90f452ce448f07537803d8b853213a1e7c5fb
        A/table-images/page-4.png: e5b7b9f99bc8f381183e5efb02bd3bc4c766963f76a81b6ce5d9aee1e0cbcdb8
        A/table-images/TABLE-1-page-4-1.png: ff63becd8a34160ae49638f7d7510ef3ce32a0da0cf68d91aa5525c0193a91c4
        A/table-images/TABLE-3-page-6-1.png: c796a164ef219333d9df9a153a45c6785d88c7529b1d5830999a247a34149562
        A/table-images/manifest.json: 138413838a9620bea2af1423de5baabacc1c4979e4dc4a53cea50a80ea56dac3
        A/table-images/TABLE-2-page-5-1.png: d66c6d70d3015b3f1f31cdd15185ff0295460b934add8f7b447d3053bc5a8500
        A/clauses/window-03/raw.json: c1d313c777a724550738883fe6eafeefe87f0f8591593c90ed11450f15157d26
        A/clauses/window-03/prompt.txt: ec0cb0514f679c217bc0dc372d67339aa16386132f962a3d65a3515fbb7cd09a
        A/clauses/window-03/meta.json: a931c2a273b31858923b03800397764b01a8fde02eb30c4c16e6b42ff2186f0f
        A/clauses/window-04/raw.json: 0592d51c8b34c25ca891dba09f1ff01f6fd1e2117849bd239609535347bce31c
        A/clauses/window-04/prompt.txt: 0944a77c12f7daea6cf8aba94ec4ac18b46aa04abf6eb870e7b32c34ee6429ab
        A/clauses/window-04/meta.json: ba7296bd5dc22edcbe35704d6dcdb3159ec4fe3f399bdaacc5cabadde82ec7c2
        A/clauses/window-05/raw.json: b1deb58eb8baa76bd0a2a7a66b4a05ae1a3331841d8c1d226bdf55749fb28c37
        A/clauses/window-05/prompt.txt: 9e07f54596166328f64d753c97c42d68ebcb8c080f6c5f77d3e89126a6b30423
        A/clauses/window-05/meta.json: 227e48d4b677010b6c7e308635f896c344a88c8d4b68eff5f7ae77ec4c674b35
        A/clauses/window-02/raw.json: c094846aec05792cae3248bb2953a46cffbd7c0001550d014f335f2b5ab706e9
        A/clauses/window-02/prompt.txt: 34731c47847ed3ec08ad80351e3f5e50420c7d04a44ebd25697b0f138326dce0
        A/clauses/window-02/meta.json: c84588bee169e5b1a28655751d20afd9800092212a9a904d7166aeb844eb3914
        A/clauses/window-01/raw.json: d84c171ebf5215e25ec0c220fae4b35604225061591396ff1cebbcf85c22457a
        A/clauses/window-01/prompt.txt: a820e26ee47106c62252c97a1f3442b4f6acf8835848bbc4372faf4cd2d68927
        A/clauses/window-01/meta.json: 8f14e43bffdd4856a5e9b2c189fb8ec53fcab5567bcf7fb63bfef28cacd5a9a3
        A/clauses/window-06/raw.json: c3372c411396ef8dd41bee2d9a57c35e4abfe45a3393a2f001e5b37410de57b1
        A/clauses/window-06/prompt.txt: 3ba1eed61e095d2bdad94d2fbf268f92b83f1f86b693a780bf7257d357fcd906
        A/clauses/window-06/meta.json: b31c7b0c747aea7672a8886608966fcd919d0141f59abfd6e8fb92302a36c965
        A/tables/TABLE-2-page-5-2/raw.json: f3dbb7906bc976ea7f4c718bbdc546b54eccc0349f1af8b6b96e79096094a6ee
        A/tables/TABLE-2-page-5-2/prompt.txt: 1879c5960adbb3fe5eb36210c8449d9a9dc7a2e65e7c51f4b3b4cd741422cee9
        A/tables/TABLE-2-page-5-2/meta.json: a6bde65e550d46046180ee9027a2046a1028292a7bedfbd6c17a647e9a463d43
        A/tables/TABLE-3-page-6-3/raw.json: 995e239c786589faf9e2cb4b4ac565e66637db0678a1ef66d01f6bc93aa10ef7
        A/tables/TABLE-3-page-6-3/prompt.txt: c6f12b107243b6c1564d3d1346f0e0bb2e189dbdb43104062d0aaef768821ee2
        A/tables/TABLE-3-page-6-3/meta.json: ebaa881f08f68856f718ceabbb811b38c413c426e07c0f63e8341c1cb6a3f516
        A/tables/TABLE-1-page-4-1/raw.json: a0dc64c6d251585f1f6a65c0919474eb9a8f241d70a4eafe9ecaa8354a51073b
        A/tables/TABLE-1-page-4-1/prompt.txt: 706401376477bc555f7a33a8a51bf9632901d758485a7176cc4eb3eee7a16d31
        A/tables/TABLE-1-page-4-1/meta.json: 02b2c9814c3972e939deffa3b7ee61851a8eb87777ac3d323d3992d115d679b6
        B/passages.json: c058c12d716a073b6f6a2b2d1690460d5adb60dc2348352e58bef1503559790a
        B/raw.json: 7a7dc534a73aaa345410c0a7be11fa3db6da7473491d2dba9e90dcb5ee0a1890
        B/source-units.json: cae54612c6d76b72e7bfb89fa9cc9c2a263e49c1afc12dcf73314d23ed34123c
        B/full-source-units.json: e2ee9283ae56002a9a0ff0f49efc6f32a09b089c63e1801ec72918ee7e71642a
        B/meta.json: 27e394d73d8c4a9482e8c3d29ba52b5d3776176647a559a795d025962c7a873a
        B/table-images/page-6.png: 97c7a627ee22d5031178c0db238a5274b005cb5c74f6fe7601eaa74e16ceecd2
        B/table-images/page-5.png: 5036562f4e14911f22df72d181c90f452ce448f07537803d8b853213a1e7c5fb
        B/table-images/page-4.png: e5b7b9f99bc8f381183e5efb02bd3bc4c766963f76a81b6ce5d9aee1e0cbcdb8
        B/table-images/TABLE-1-page-4-1.png: ff63becd8a34160ae49638f7d7510ef3ce32a0da0cf68d91aa5525c0193a91c4
        B/table-images/TABLE-3-page-6-1.png: c796a164ef219333d9df9a153a45c6785d88c7529b1d5830999a247a34149562
        B/table-images/manifest.json: 6c55ba91bc6a01c19e66e42dac4391561092d713aa99fed0bacaa2f4bed7888b
        B/table-images/TABLE-2-page-5-1.png: d66c6d70d3015b3f1f31cdd15185ff0295460b934add8f7b447d3053bc5a8500
        B/clauses/window-03/raw.json: 5b4ee68238f85d980b13449560661113c906ab31cae6d2c80f35401130bcc4ba
        B/clauses/window-03/prompt.txt: ec0cb0514f679c217bc0dc372d67339aa16386132f962a3d65a3515fbb7cd09a
        B/clauses/window-03/meta.json: d69865e3f8560c2c7865e94edb0a8757ac234c107f8300eb0fc7151c3bc85c39
        B/clauses/window-04/raw.json: d4b68091f8031f1ed47e0c2b91c85131cae30d5a2d1c84e5d324e6be0b3e11f8
        B/clauses/window-04/prompt.txt: 0944a77c12f7daea6cf8aba94ec4ac18b46aa04abf6eb870e7b32c34ee6429ab
        B/clauses/window-04/meta.json: b4ecfebd750b08bf698d5d43285c7b704a3a55d40babba6f94e56a27131b0f23
        B/clauses/window-05/raw.json: da789a18fcd1cafa115a59ced6e41dd92e8c31ea567ea8c3afd13cc26094b007
        B/clauses/window-05/prompt.txt: 9e07f54596166328f64d753c97c42d68ebcb8c080f6c5f77d3e89126a6b30423
        B/clauses/window-05/meta.json: 49c55e90bbc7b29310f2495784f5b97d94e23c2afa757a0cb1daca1bf3efc339
        B/clauses/window-02/raw.json: e4e5314ca4e301f9a75bfcd83565b7d0aeb35d3b1ec99d7530ed114e7fdd1b40
        B/clauses/window-02/prompt.txt: 34731c47847ed3ec08ad80351e3f5e50420c7d04a44ebd25697b0f138326dce0
        B/clauses/window-02/meta.json: 1ed03f6b21acf01b40c40186ce8e84d4b9b19bc8ad9438989384c42894f3d8fe
        B/clauses/window-01/raw.json: c093ca8004cd4e65e37eb380594b1f826a5e6e7c3fca900ab21b1ecc437f534e
        B/clauses/window-01/prompt.txt: a820e26ee47106c62252c97a1f3442b4f6acf8835848bbc4372faf4cd2d68927
        B/clauses/window-01/meta.json: 9e198d9b9922560981bbfd5977ebe0761ea6699bf1624d2296f9a429aa81551f
        B/clauses/window-06/raw.json: 036a51b8f53f4d66e33b44fdfd1cf1c07594bdb4a762fb4da938d49b47905291
        B/clauses/window-06/prompt.txt: 3ba1eed61e095d2bdad94d2fbf268f92b83f1f86b693a780bf7257d357fcd906
        B/clauses/window-06/meta.json: da9367256ea56653fb0836ad09c09325e252c3dd3b8da47d680cd304139aed53
        B/tables/TABLE-2-page-5-2/raw.json: 6958663d2caa639486bddd0489ecd8ff097711f8dabc5e0052327b3ce0a6d016
        B/tables/TABLE-2-page-5-2/prompt.txt: 1879c5960adbb3fe5eb36210c8449d9a9dc7a2e65e7c51f4b3b4cd741422cee9
        B/tables/TABLE-2-page-5-2/meta.json: bfaa3d382b029b5aaff09e672189bfaaea62e5b3616a749a3258cf1100e68c31
        B/tables/TABLE-3-page-6-3/raw.json: 86376bed3fb03f075689db38a8cf72c7e0501d370fe4188ec947803a1ee6c835
        B/tables/TABLE-3-page-6-3/prompt.txt: c6f12b107243b6c1564d3d1346f0e0bb2e189dbdb43104062d0aaef768821ee2
        B/tables/TABLE-3-page-6-3/meta.json: fef185bcfb9b8566b9694a253b5f8e226a94ff4415cb4fce2513beb68d589b12
        B/tables/TABLE-1-page-4-1/raw.json: e470e0ad941c9a44854378f389179b557c156357f6f4b647f3ab6e112fc8e12e
        B/tables/TABLE-1-page-4-1/prompt.txt: 706401376477bc555f7a33a8a51bf9632901d758485a7176cc4eb3eee7a16d31
        B/tables/TABLE-1-page-4-1/meta.json: fb4d286ef841a3f4097f79c96e9b7d7c6bc62f355d0509347f2d803ffa76452f
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
      pdf_sha256: 6ae87a3b3c2f72929b0c8266e0d862caab741b6fb5c43b19a22b8581f06fcdb1
      source_review: _compare/relationships-2026-11-16/review-current/Fridriksson2018JAMA
      source_status_sha256: 058ed9ce6ec4e809e7515789fc35399618e1371cf8f9073cf491075909e3ab03
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R001
    exposure:
      text: anodal transcranial direct current stimulation (A-tDCS) vs sham tDCS (S-tDCS)
    outcome:
      text: correct naming of common objects
    analysis_label: Primary futility analysis (1-week posttreatment)
    relation: treatment_effect
    evidence_ids:
    - P1-S2-C4
    - P5-S1-C4
    qualifier_ids:
    - P4-S1-C1
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 6ae87a3b3c2f72929b0c8266e0d862caab741b6fb5c43b19a22b8581f06fcdb1
      source_review: _compare/relationships-2026-11-16/review-current/Fridriksson2018JAMA
      source_status_sha256: 058ed9ce6ec4e809e7515789fc35399618e1371cf8f9073cf491075909e3ab03
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P4-S1-C13
      - Result passage disposed without unit P4-S1-C9
      - Result passage disposed without unit P4-S2-C2
      - Result passage disposed without unit P4-S2-C4
      - Result passage disposed without unit P4-S2-C5
      - Result passage disposed without unit P5-S1-C1
      - Result passage disposed without unit P5-S1-C9
      - Result passage disposed without unit P5-S2-C3
      - Result passage disposed without unit P6-S1-C3
      - Result passage disposed without unit P6-S1-C4
      - Result passage disposed without unit P6-S1-C5
      - Accounting without a linked unit P6-S1-C9
      - Unaccounted source passage P6-S1-C9
      - Result passage disposed without unit P6-S2-C12
      - Result passage disposed without unit P6-S3-C1
      unattached_null_or_qualifier_ids:
      - P4-S1-C7
      - P5-S2-C3
      - P6-S1-C5
      suppressed_nonrepresented_units: 13
      default_disposition_count_requires_completeness_check: 113
      unselected_timing_passages:
      - P1-S1-C7
      - P1-S1-C10
      - P1-S1-C15
      - P2-S1-C7
      - P2-S2-C3
      - P2-S3-C8
      - P3-S2-C6
      - P4-S1-C5
      - P4-S1-C6
      - P4-S1-C10
      - P4-S2-C6
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P1-S2-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P4-S1-C13
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      empty_frame_slots_require_confirmation:
      - validation
      - analysis_restrictions
      - dependent_variable_statement
      - personal_factors
      - tested_personal_effects
      - explicitly_not_adjusted
      unclassified_extraction_ids:
      - P2-S2-C10
      table_review_required:
      - TABLE-1-page-4-1
      - TABLE-2-page-5-2
      - TABLE-3-page-6-3
      unlinked_tables:
      - TABLE-1-page-4-1
      - TABLE-2-page-5-2
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P4-S1
        - P4-S2
        - P5-S1
        - P5-S2
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 6ae87a3b3c2f72929b0c8266e0d862caab741b6fb5c43b19a22b8581f06fcdb1
      source_review: _compare/relationships-2026-11-16/review-current/Fridriksson2018JAMA
      source_status_sha256: 058ed9ce6ec4e809e7515789fc35399618e1371cf8f9073cf491075909e3ab03
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S2-C4
      disposition: represented
      result_indexes:
      - 0
      reason: Reports adjusted mean change in naming for A-tDCS and sham.
    - source_id: P1-S2-C5
      disposition: represented
      result_indexes:
      - 1
      reason: Reports futility hypothesis P value.
    - source_id: P1-S2-C6
      disposition: represented
      result_indexes:
      - 8
      reason: Reports absence of serious adverse events.
    - source_id: P2-S2-C2
      disposition: represented
      result_indexes:
      - 11
      reason: Reports correlation between screening task and AQ.
    - source_id: P2-S3-C9
      disposition: repeated
      result_indexes:
      - 1
      reason: Restatement of futility result in Key Points.
    - source_id: P4-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes missing data for primary outcome.
    - source_id: P4-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes baseline similarity between arms.
    - source_id: P4-S1-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes numerical baseline differences.
    - source_id: P4-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Compares trial cohort to AphasiaBank.
    - source_id: P4-S2-C4
      disposition: represented
      result_indexes:
      - 10
      reason: Reports guessing accuracy for blinding.
    - source_id: P4-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes general improvement on treatment task.
    - source_id: P5-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes task compliance/participation.
    - source_id: P5-S1-C3
      disposition: represented
      result_indexes:
      - 1
      - 4
      reason: Reports futility P value and AQ correlation.
    - source_id: P5-S1-C4
      disposition: represented
      result_indexes:
      - 0
      reason: Reports adjusted mean change in naming at 1 week.
    - source_id: P5-S1-C5
      disposition: represented
      result_indexes:
      - 5
      reason: Reports results of completers-only analysis.
    - source_id: P5-S1-C6
      disposition: represented
      result_indexes:
      - 6
      reason: Reports results of baseline-adjusted sensitivity analysis.
    - source_id: P5-S1-C7
      disposition: represented
      result_indexes:
      - 2
      reason: Reports adjusted mean change at 4 weeks.
    - source_id: P5-S1-C8
      disposition: represented
      result_indexes:
      - 3
      reason: Reports adjusted mean change at 24 weeks.
    - source_id: P5-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes dropout counts.
    - source_id: P5-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes specific dropout event.
    - source_id: P5-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes seizure event.
    - source_id: P5-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Specifies seizure occurred in sham group.
    - source_id: P5-S2-C7
      disposition: represented
      result_indexes:
      - 9
      reason: Reports number of mild adverse events.
    - source_id: P5-S2-C8
      disposition: represented
      result_indexes:
      - 9
      reason: Reports erythema incidence.
    - source_id: P5-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports pain ratings (descriptive).
    - source_id: P5-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports highest pain rating.
    - source_id: P5-S2-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports vital signs similarity.
    - source_id: P5-S2-C12
      disposition: repeated
      result_indexes:
      - 1
      reason: Discussion restatement of futility result.
    - source_id: P6-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes comparability of stroke severity.
    - source_id: P6-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes numerical baseline differences.
    - source_id: P6-S1-C5
      disposition: repeated
      result_indexes:
      - 6
      reason: Discussion restatement of sensitivity analysis.
    - source_id: P6-S1-C9
      disposition: repeated
      result_indexes:
      - 0
      - 2
      - 3
      reason: Discussion summary of magnitude of effect across timepoints.
    - source_id: P6-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement on low rate of adverse events.
    - source_id: P6-S2-C9
      disposition: represented
      result_indexes:
      - 9
      reason: Reports erythema resolution.
    - source_id: P6-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: General safety conclusion.
    - source_id: P6-S2-C12
      disposition: repeated
      result_indexes:
      - 0
      reason: Discussion restatement of numerical naming improvement.
    - source_id: P6-S3-C1
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of numerical improvement.
    - source_id: P6-S3-C15
      disposition: represented
      result_indexes:
      - 9
      reason: Table of adverse events.
    unresolved_coverage:
    - source_id: P5-S1-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P2-S3-C9
    - P4-S1-C7
    - P4-S1-C9
    - P4-S1-C13
    - P4-S2-C2
    - P4-S2-C5
    - P5-S1-C1
    - P5-S1-C9
    - P5-S2-C3
    - P5-S2-C4
    - P5-S2-C5
    - P5-S2-C6
    - P5-S2-C9
    - P5-S2-C10
    - P5-S2-C11
    - P5-S2-C12
    - P6-S1-C3
    - P6-S1-C4
    - P6-S1-C5
    - P6-S1-C9
    - P6-S2-C8
    - P6-S2-C10
    - P6-S2-C12
    - P6-S3-C1
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-4-1
    - TABLE-2-page-5-2
    - TABLE-3-page-6-3
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P4-S1-C3
      - P5-S1-C2
      recruited_sample:
      - P1-S1-C9
      - P4-S1-C3
      eligibility:
      - P1-S1-C10
      - P2-S1-C7
      - P2-S2-C3
      imaging_provenance:
      - P2-S3-C4
      - P2-S3-C5
      imaging_timing:
      - P2-S3-C3
      outcome_timing:
      - P3-S2-C9
      - P3-S3-C5
      - P5-S1-C4
      - P5-S1-C7
      - P5-S1-C8
      outcome_definition:
      - P1-S1-C13
      - P3-S2-C9
      - P3-S3-C5
      validation: []
      analysis_restrictions: []
      dependent_variable_statement: []
      limitations:
      - P6-S2-C11
      - P6-S2-C12
      - P6-S3-C1
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P1-S1-C11
      - P4-S1-C1
      - P5-S1-C6
      - P5-S1-C7
      - P5-S1-C8
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P1-S1-C15
      - P1-S1-C16
      - P1-S1-C17
      - P1-S1-C18
      - P4-S1-C10
      - P4-S1-C11
      - P4-S2-C8
    outcome_type: change_from_baseline
    imaging_vs_outcome: precedes_outcome
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P1-S2-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P4-S1-C13
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
      pdf_sha256: 6ae87a3b3c2f72929b0c8266e0d862caab741b6fb5c43b19a22b8581f06fcdb1
      review_sha256: 10fc94cadeea7045fee6f27116a0b664fc4660e62b1b0168a9d7e13c01528c77
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
      - P1-S2-C4
      - P5-S1-C4
      source_result: The primary futility analysis (1-week posttreatment) failed to
        reject the null hypothesis that A-tDCS is superior to sham tDCS (P = .90).
        The adjusted mean difference in correct naming was 5.7 words (95% CI, -0.9
        to 12.3), indicating no evidence of futility, but the study was not powered
        for superiority.
      result_status: not_detected
      patient_measurement: non_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis corresponds to the primary futility analysis
            at 1-week posttreatment as described in P1-S2-C4 and P5-S1-C4. The model
            is an intent-to-treat analysis adjusted for site and baseline aphasia
            severity.
          source_ids:
          - P1-S2-C4
          - P5-S1-C4
          - P4-S1-C1
        direction:
          answer: fits
          reason: The source states that the null hypothesis (futility) was not rejected,
            meaning the treatment was not proven futile. The proposed core correctly
            interprets this as 'did not demonstrate a lack of superiority' rather
            than claiming a significant positive effect or a definitive null effect
            on efficacy. The direction 'no_effect' in the proposed core is interpreted
            as 'no detected futility' which aligns with the futility design outcome.
          source_ids:
          - P1-S2-C5
          - P5-S1-C3
          - P6-S2-C12
        construct:
          answer: fits
          reason: Exposure is A-tDCS vs sham. Outcome is correct naming of common
            objects. Measurement is behavioral (PNT/Naming 80), classified as non_imaging.
            The fMRI was used for electrode placement, not as the outcome measure.
          source_ids:
          - P1-S1-C12
          - P3-S2-C9
          - P2-S3-C4
        qualifications:
          answer: fits
          reason: The proposed core includes the futility design context and the specific
            adjustments (site, baseline severity). It also includes the limitation
            that the study was not powered for superiority, which is a material caveat
            from P6-S2-C11/C12.
          source_ids:
          - P4-S1-C1
          - P6-S2-C11
          - P6-S2-C12
        missing_material_caveat:
          answer: fits
          reason: The core includes the key limitation that the study was not powered
            for superiority and that generalizability to functional communication
            is uncertain. No other material caveats are omitted that would change
            the interpretation of the futility result.
          source_ids:
          - P6-S2-C11
          - P6-S2-C12
          - P6-S3-C1
      optional_pending:
      - Specific P-value for the unadjusted completers-only analysis (P5-S1-C5 mentions
        t=1.35, P=.91, but table readings are unverified)
      - Exact sample sizes for completers-only analysis (Table 2 readings suggest
        n=33/38, but unverified)
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Specific P-value for the unadjusted completers-only analysis (P5-S1-C5 mentions
      t=1.35, P=.91, but table readings are unverified)
    - Exact sample sizes for completers-only analysis (Table 2 readings suggest n=33/38,
      but unverified)
    normalizations: []
    analysis_identity:
      id: R001
      exposure:
        text: anodal transcranial direct current stimulation (A-tDCS) vs sham tDCS
          (S-tDCS)
      outcome:
        text: correct naming of common objects
      analysis_label: Primary futility analysis (1-week posttreatment)
      relation: treatment_effect
      evidence_ids:
      - P1-S2-C4
      - P5-S1-C4
      qualifier_ids:
      - P4-S1-C1
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 6ae87a3b3c2f72929b0c8266e0d862caab741b6fb5c43b19a22b8581f06fcdb1
        source_review: _compare/relationships-2026-11-16/review-current/Fridriksson2018JAMA
        source_status_sha256: 058ed9ce6ec4e809e7515789fc35399618e1371cf8f9073cf491075909e3ab03
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P1-S1-C10:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 6ae87a3b3c2f72929b0c8266e0d862caab741b6fb5c43b19a22b8581f06fcdb1
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 0a597e1b48197ee3edbb13cf93caf92229c781ca318d70eb0b5d8f2bab702007
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P1-S1-C10
          page: 1
          text_layer_sha256: 0a597e1b48197ee3edbb13cf93caf92229c781ca318d70eb0b5d8f2bab702007
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Patients with long-term

          (>6 months) aphasia due to 1 previous left hemisphere stroke were enrolled.'
        anchor_text: 'Patients with long-term

          (>6 months) aphasia due to 1 previous left hemisphere stroke were enrolled.'
        excluded_fragments: []
        image_sha256: 6ac6b89422ca69d6721658fc3e77b46502dd2806c06af4c15b9b5b1b3e396c7b
        transcription: . Patients with long-term (>6 months) aphasia due to 1 previous
          left hemisphere stroke were enrolled
      P1-S1-C14:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 6ae87a3b3c2f72929b0c8266e0d862caab741b6fb5c43b19a22b8581f06fcdb1
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 28db35ba4cad547f3a3f8dad5718f14ebcc3135bb188fde32082ee98ffe12cc8
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P1-S1-C14
          page: 1
          text_layer_sha256: 28db35ba4cad547f3a3f8dad5718f14ebcc3135bb188fde32082ee98ffe12cc8
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: RESULTS A total of 74 patients were enrolled.
        anchor_text: RESULTS A total of 74 patients were enrolled.
        excluded_fragments: []
        image_sha256: 51866a7c78cd1d4e9881098e9a1e7bfb184f7a1a2b3c6846c8cd6eabc4b91ab0
        transcription: RESULTS A total of 74 patients were enrolled
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 1
  quote: 'The adjusted mean (SE) change from pretreatment baseline in correct naming
    was 13.9 (2.4)

    words (95% CI, 9.0-18.7) for A-tDCS and 8.2 (2.2) words (95% CI, 3.8-12.6) for
    sham tDCS,

    with mean (SE) A-tDCS difference of 5.7 (3.3) words (95% CI, −0.9 to 12.3), indicating
    a

    relative 70% increase in correct naming for A-tDCS relative to sham.'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-23'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
