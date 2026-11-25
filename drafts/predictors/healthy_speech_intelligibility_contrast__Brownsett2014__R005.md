---
id: healthy_speech_intelligibility_contrast
name: Healthy participant intelligibility contrast
kind: predictor
findings:
- id: f1
  target_audit:
    status: behaviour_label_present
    category: behaviour_or_language_construct
    original_target: repetition_performance
    reason: Label names a behaviour or language construct; its exact operational definition and measurement
      still need source review.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  outcome_measurement:
    status: needs_source_review
    instruments: []
    note: Outcome instrument/task is not yet verified for this finding. Do not infer it from the predictor
      or a paper-wide test list.
  target: repetition_performance
  target_kind: impairment
  claim: Healthy participants performed significantly better at repeating sentences
    after listening to normal speech than after listening to noise-vocoded speech,
    both before and after training.
  direction: likely
  relationship: correlational
  method: behavioral_only
  sample:
    n: 17
    population: healthy right-handed participants with no history of neurological
      illness or developmental language impairment
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
  author_limitations: []
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Comparison of repetition performance after listening
    to normal clear speech (ListNorm) versus 3-channel noise-vocoded speech (ListVoc).
    performance on normal speech trials was at ceiling at both time-points. Additional
    metadata has not been transcribed; review the pending-field flags before approval.
    PDF image reading (P6-S1-C2, two-model agreement, human verification pending):
    . Before training, using the com-

    bined semantic and articulation score as the measure: $t(15) = 13$;

    two-tailed; $P < 0.001$; 95% confidence interval (CI) = 42.6–59.4. Original text-layer
    quotation is preserved below. PDF image reading (P3-S2-C12, two-model agreement,
    human verification pending): . Seventeen participants completed the study (11
    females; mean

    age 60 years; range, 25–82 years) with a mean duration of formal

    education of 15 years (range 10–20 years) Original text-layer quotation is preserved
    below.'
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
    - not_transcribed:author_limitations
    - not_transcribed:sample.time_post_onset
    - proposed_concept:repetition_performance
  citation: '@Brownsett2014'
  source_passages:
  - section: Original source P6-S1-C1
    page: 6
    quote: '

      Healthy participants

      Predictably, the healthy participants were better at repeating after

      listening to normal speech trials (ListNorm) than listening to

      vocoded speech trials (ListVoc).'
    supports: claim
  - section: Original source P6-S1-C2
    page: 6
    quote: 'Before training, using the com-

      bined semantic and articulation score as the measure: t(15) = 13;

      two-tailed; P 5 0.001; 95% conﬁdence interval (CI) = 42.6–59.4.'
    supports: claim
  - section: Original source P6-S1-C3
    page: 6
    quote: 'After

      training:

      t(16) = 11.6,

      two-tailed;

      P 5 0.001;

      95%

      CI = 28.2–40.7.'
    supports: claim
  - section: Original source P3-S2-C12
    page: 3
    quote: 'Seventeen participants completed the study (11 females; mean

      age 60 years; range, 25–82 years) with a mean duration of formal

      education of 15 years (range 10–20 years).'
    supports: sample
  - section: Original source P3-S2-C11
    page: 3
    quote: 'Healthy participants (control subjects) had no history of neurological

      illness,

      no

      sinistrality,

      no

      history

      of

      developmental

      language

      impairment, no contraindications to MRI and English as the ﬁrst lan-

      guage.'
    supports: sample
  - section: Original source P3-S1-C5
    page: 3
    quote: 'In parallel, the healthy participants received training on

      discriminating noise-vocoded speech.'
    supports: method
  - section: Original source P6-S1-C7
    page: 6
    quote: "Performance was at ceiling at both time-\npoints: t(15) = 1.5, P 4 0.1,\
      \ two-tailed; 95% CI = \x040.4–2.5."
    supports: claim
predictor_type: behavioural
short_definition: Comparison of repetition performance after listening to normal clear
  speech (ListNorm) versus 3-channel noise-vocoded speech (ListVoc).
assessment:
- combined semantic and articulation score
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-23'
relationship_review:
  paper: Brownsett2014
  proposal_id: R005
  review_status_sha256: 516f4bdba234f7b90802a5ca706b5074ba75ac6f5ec61775889a14e0ff9efcf9
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 5afbac2f573d594d73c1c2f5910be59fc3db6650fed5f2600634a5146b722423
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 5afbac2f573d594d73c1c2f5910be59fc3db6650fed5f2600634a5146b722423
        A/passages.json: bd4f39541d46207911a9352de3eacbc063b5093f05fafae797e7fff7159bb428
        A/raw.json: 286c2c4d5b3305bdaa8006eb70799d0e457b202cf10920a9f481a3fe1f9711cc
        A/source-units.json: ac0dd659701e7b8f3a0499eea6ef1c09b067619371d34caee28aafc51f3cce28
        A/full-source-units.json: 8cb4e664732df432860e78bdd502c834ec09ddcbc1aea4825bc1950d686bf8c5
        A/meta.json: 89153c4e9f316a22eafd18c3b577c306bdc58c28be4b0c1a3e27f3be25c84466
        A/table-images/page-9.png: c16e1a2cef6741e3dc6ef28fd87b78aac02309b94316a6c018183d1ea6692ad6
        A/table-images/manifest.json: 7288cc0b7f2978cf42973240f6fe9c884f6e093f90a003d46e730ff4ba48229d
        A/table-images/TABLE-1-page-9-1.png: 9ec0fc8c7bbee69430744f3889fa925b2c9506a2e91eae81adf43a2c60ec192e
        A/clauses/window-10/raw.json: 4cd57f39561b7fb379dd23f57ab245096d3139eec4ebfd4bc01f1727f24dee06
        A/clauses/window-10/prompt.txt: f753e492e14796cfa5de929aaa6002d96a36442891a6470a774e475622916de0
        A/clauses/window-10/meta.json: 000c7cb8c2c798306a409c6d862dc877b273937d113e5826a1bf4daa40e0c2b3
        A/clauses/window-03/raw.json: 06572e48e45f47982ba51466bb996b22e4c7055086bd6f77189b7de5f2ce726d
        A/clauses/window-03/prompt.txt: 4716a73079ab1ef2af3bf03b9e4a4bb492445607d5cb0828c1017866da89ce53
        A/clauses/window-03/meta.json: 2d719bcb228683b29c2e4bbd874bf51d4d1f5819416d38a91a55371b7a28b05d
        A/clauses/window-04/raw.json: 3ecae97b9f211f281a2f9d7efdaa8af7afcdd366c817cef8371d033881dca811
        A/clauses/window-04/prompt.txt: a54639fdc5d3ad5910778be933dc45d772e5a78c6877f663e85461aa77b02627
        A/clauses/window-04/meta.json: 14f34cc450bc636d48dc439a21948a26b6cb064f036f4630a162579b9b67e1c3
        A/clauses/window-05/raw.json: 3c68bf7112cc43232cfb1e982755ad790fa0fe8c29e2b3df42f424b11d8792e0
        A/clauses/window-05/prompt.txt: a321d8c48b466a6390bf84b9672ca837dbd56db0c5ae81c1705754d2cc8bef71
        A/clauses/window-05/meta.json: 268c8a04e0fd4bc2f019bd1198a3447a4f97c2cc7306f4b0b2292575d9039426
        A/clauses/window-02/raw.json: 8742c561db020c1b5607c58ced2d134a230da046c60c89d9a39239e4d4fe5047
        A/clauses/window-02/prompt.txt: 1f353a391ef7e3de7259af46d648ecad2177b1cfdeee3a468d94a066a029d367
        A/clauses/window-02/meta.json: 1bef3988a8f2df9e94f4c5fd774e059292cde8ead527ad99832c920bdfdda630
        A/clauses/window-09/raw.json: 7461dd84066eaee3453595b8467cb3b8ce18296458ee5186929dfc9da6bcc5e9
        A/clauses/window-09/prompt.txt: 16df01915d7a733d910aa8680892bad9f1a928c71993004bf1ed89989c9b96f7
        A/clauses/window-09/meta.json: ab25d4a206bde761259715e4342247ca0276161e536445e5fe662b6b64ba22ab
        A/clauses/window-07/raw.json: dc230c000106a99e669d454f7d1b57943356268a6abff473cfebac817930a998
        A/clauses/window-07/prompt.txt: 56478af12537d5cb07b19f68495a6f5a6eb82cd17bf1cbff31f9fbeba0e90fd4
        A/clauses/window-07/meta.json: 1bec47f1550a46ce61c3aeac6a01152bec2d80f054ddf5736fc817f19296b5cf
        A/clauses/window-01/raw.json: 31fd784aa844ac2998150c921b776ceb22f9cae4233a50867b908b148cd9e93d
        A/clauses/window-01/prompt.txt: 96ab4efb27d267a4a72895e4b0f34387a8c1e3e4f6b6412a259eca2b9b107318
        A/clauses/window-01/meta.json: 38baac291d437670fa31dc6e6b4ee9f8401c040b7ac454888367529a7e41c57d
        A/clauses/window-06/raw.json: 4f01c797968fece479ebb833891c7a10014dda9774fafd1072089e68ec4c6d74
        A/clauses/window-06/prompt.txt: 4af9bd263f1cbfdb5e30e8b3e68a824e13d8418c7d2c4cb09ac3efcbd78bf301
        A/clauses/window-06/meta.json: caaafb2182cb4816cab4f4bbbd0f3b8b37772af37a746eb7203b425df32c8b07
        A/clauses/window-08/raw.json: 5a98daf98e860374b2d1c5f0303b12110c6fb3fc545abeecce4b0dba3290fa09
        A/clauses/window-08/prompt.txt: 4a344756fd1c47de470e9644d796b9f59efb2b438557f408969b08d3434ea680
        A/clauses/window-08/meta.json: c835933f51628a80e62ac6be6650eb7cbf9e4f01c271a64175e2bf184ea64836
        A/tables/TABLE-1-page-9-1/raw.json: 614aa912b1f3caa1571cc142d26662f23b4a6b2cf2d8d62134e2c86fdd1c5495
        A/tables/TABLE-1-page-9-1/prompt.txt: d1871618d4f7f38b995094cdf26355c801307a05c797a0eed5676da1f44c2a82
        A/tables/TABLE-1-page-9-1/meta.json: d4a44938488617d5f70715e9425c2c728aa58b7951ff676e861070c48d78e88e
        B/passages.json: bd4f39541d46207911a9352de3eacbc063b5093f05fafae797e7fff7159bb428
        B/raw.json: 955550c99bed5de2a538561a523365b3ee3f259b3b5fd531f6438223fba9e169
        B/source-units.json: ac0dd659701e7b8f3a0499eea6ef1c09b067619371d34caee28aafc51f3cce28
        B/full-source-units.json: 8cb4e664732df432860e78bdd502c834ec09ddcbc1aea4825bc1950d686bf8c5
        B/meta.json: 6a927d43028261490670680fe18d0bf745058bd82c0b995338dca390956486bc
        B/table-images/page-9.png: c16e1a2cef6741e3dc6ef28fd87b78aac02309b94316a6c018183d1ea6692ad6
        B/table-images/manifest.json: 2a893f8c4fa2f92dcc98cefa5988aafbfe74347d0a79742e8fd5411e0512958f
        B/table-images/TABLE-1-page-9-1.png: 9ec0fc8c7bbee69430744f3889fa925b2c9506a2e91eae81adf43a2c60ec192e
        B/clauses/window-10/raw.json: 9113d0702a9e4b432d87dc363c940a135660ec5b9e6b4c75bf9da79932e0d753
        B/clauses/window-10/prompt.txt: f753e492e14796cfa5de929aaa6002d96a36442891a6470a774e475622916de0
        B/clauses/window-10/meta.json: f10da16ba020962654ef5001d32aeb295e7bb6fbd00d8812e94362e7aa49fe81
        B/clauses/window-03/raw.json: 20c1a948cd1cae3afae65185226faec07eaa559445b8e4d69572ac60e436711a
        B/clauses/window-03/prompt.txt: 4716a73079ab1ef2af3bf03b9e4a4bb492445607d5cb0828c1017866da89ce53
        B/clauses/window-03/meta.json: c6de8916757b5ea99885786107ebe399d7ca7b382d22c765083577705f795f8c
        B/clauses/window-04/raw.json: 545b186ced99c6007071c9a028098704246f2372ecfcc242364325d4f9d7371f
        B/clauses/window-04/prompt.txt: a54639fdc5d3ad5910778be933dc45d772e5a78c6877f663e85461aa77b02627
        B/clauses/window-04/meta.json: b9987aa584af23ab1d7a9f6483c87038d53fe4553702cb42e7dbbbea30e9dc06
        B/clauses/window-05/raw.json: 7dc483fe69cda2c10bfed15b9ca62868084a4ebcee204d3170e0eb7d60ae864c
        B/clauses/window-05/prompt.txt: a321d8c48b466a6390bf84b9672ca837dbd56db0c5ae81c1705754d2cc8bef71
        B/clauses/window-05/meta.json: 75024cc0521866f26619c7a75a370988ef2e9a499f634673fce8c5cfb0e5ad99
        B/clauses/window-02/raw.json: 949c8a70f7b907bccbd8bc3971a78f06b959b4eb2759ff1aace4db17770e6b0a
        B/clauses/window-02/prompt.txt: 1f353a391ef7e3de7259af46d648ecad2177b1cfdeee3a468d94a066a029d367
        B/clauses/window-02/meta.json: 5fc1f6125d845d7c181267df31385ea737f4433e394c2bf281a7d83a719d0549
        B/clauses/window-09/raw.json: fdacb8a9a4e60a3a25f344bb67cd873216195ae517e710f84f56f8ea59140bc0
        B/clauses/window-09/prompt.txt: 16df01915d7a733d910aa8680892bad9f1a928c71993004bf1ed89989c9b96f7
        B/clauses/window-09/meta.json: 051a8f6917bd039f82e76c38e70bd4bf18a16e9dde14124d9e43acdb8be8897f
        B/clauses/window-07/raw.json: b391c6b760b26d7ac3b9479e682e0922ad034ca45b4d53cd3ca2514ad97464c9
        B/clauses/window-07/prompt.txt: 56478af12537d5cb07b19f68495a6f5a6eb82cd17bf1cbff31f9fbeba0e90fd4
        B/clauses/window-07/meta.json: fcf92643a825f5461fa8f9721a9ace0b9d4df49122c702f9e0c9ef5dba2f72c3
        B/clauses/window-01/raw.json: 8117c4308ae4ab6c4dc6b2ffc857fef4a5f730025e2cf05067ec67df6ab36ebb
        B/clauses/window-01/prompt.txt: 96ab4efb27d267a4a72895e4b0f34387a8c1e3e4f6b6412a259eca2b9b107318
        B/clauses/window-01/meta.json: 2eb58f8e87f5094bdd35ef50d9dda9b6eb37c84e750fc89d24b9f545cfc28731
        B/clauses/window-06/raw.json: b990c7cc6d1fa995845dae511ddfb7d128a7552751718f304760c0d483dab1ef
        B/clauses/window-06/prompt.txt: 4af9bd263f1cbfdb5e30e8b3e68a824e13d8418c7d2c4cb09ac3efcbd78bf301
        B/clauses/window-06/meta.json: 090eb6a761a872865d5a2000b32186c32ae1ed237fdeddd9e564b92760ee79e2
        B/clauses/window-08/raw.json: a461d1dd473fcc28265be3827a2551180e1aaa694ecd2418055c74fe7c0f8fe7
        B/clauses/window-08/prompt.txt: 4a344756fd1c47de470e9644d796b9f59efb2b438557f408969b08d3434ea680
        B/clauses/window-08/meta.json: 0d27a32469fbebf666dc1abdeadd2d68553006da75869d4a0991cb15e26c7888
        B/tables/TABLE-1-page-9-1/raw.json: b0c77121051cb3ebfcf599289778cd3f13d4170b4286aa88743b59d1efbaab47
        B/tables/TABLE-1-page-9-1/prompt.txt: d1871618d4f7f38b995094cdf26355c801307a05c797a0eed5676da1f44c2a82
        B/tables/TABLE-1-page-9-1/meta.json: 95eedac7f71ab1ba6e730b0d1b986e643e644ea63bb619412bde786011edb3d9
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
      pdf_sha256: 5afbac2f573d594d73c1c2f5910be59fc3db6650fed5f2600634a5146b722423
      source_review: _compare/relationships-2026-11-16/review-current/Brownsett2014
      source_status_sha256: db78cf6ae75b54719848df57c39ab827ef7ccc5035f72e21bef70fdc9031377c
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R005
    exposure:
      text: listening to normal speech (ListNorm) vs vocoded speech (ListVoc)
    outcome:
      text: repetition performance (combined semantic and articulation score)
    analysis_label: Healthy participant intelligibility contrast
    relation: association
    evidence_ids:
    - P6-S1-C1
    - P6-S1-C2
    - P6-S1-C3
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
      pdf_sha256: 5afbac2f573d594d73c1c2f5910be59fc3db6650fed5f2600634a5146b722423
      source_review: _compare/relationships-2026-11-16/review-current/Brownsett2014
      source_status_sha256: db78cf6ae75b54719848df57c39ab827ef7ccc5035f72e21bef70fdc9031377c
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P1-S2-C3
      - Result passage disposed without unit P1-S2-C4
      - 'window 2: invalid/duplicate disposition P3-S1-C7'
      - 'window 3: invalid/duplicate disposition P5-S3-C10'
      - 'window 3: invalid/duplicate disposition P5-S3-C15'
      - Result passage disposed without unit P5-S3-C15
      - Result passage disposed without unit P6-S1-C2
      - Result passage disposed without unit P6-S1-C3
      - Result passage disposed without unit P6-S1-C4
      - Result passage disposed without unit P6-S1-C5
      - Result passage disposed without unit P6-S1-C6
      - Result passage disposed without unit P6-S1-C7
      - Result passage disposed without unit P6-S1-C8
      - Result passage disposed without unit P6-S2-C2
      - Result passage disposed without unit P6-S2-C4
      - Result passage disposed without unit P6-S2-C5
      - Result passage disposed without unit P7-S1-C1
      - Result passage disposed without unit P7-S1-C2
      - Result passage disposed without unit P7-S1-C3
      - Result passage disposed without unit P7-S1-C4
      - Result passage disposed without unit P7-S1-C10
      - Result passage disposed without unit P7-S1-C7
      - Result passage disposed without unit P7-S1-C8
      - Accounting without a linked unit P7-S2-C2
      - Accounting without a linked unit P7-S2-C3
      - Unaccounted source passage P7-S2-C2
      - Unaccounted source passage P7-S2-C3
      - Result passage disposed without unit P8-S1-C1
      - Accounting without a linked unit P8-S1-C11
      - Result passage disposed without unit P8-S1-C12
      - Accounting without a linked unit P8-S1-C2
      - Accounting without a linked unit P8-S1-C3
      - Accounting without a linked unit P8-S1-C7
      - Accounting without a linked unit P8-S1-C8
      - Accounting without a linked unit P8-S1-C9
      - Unaccounted source passage P8-S1-C11
      - Unaccounted source passage P8-S1-C8
      - Unaccounted source passage P8-S1-C2
      - Unaccounted source passage P8-S1-C7
      - Unaccounted source passage P8-S1-C9
      - Unaccounted source passage P8-S1-C3
      - Result passage disposed without unit P8-S2-C1
      - Result passage disposed without unit P8-S2-C2
      - Result passage disposed without unit P8-S2-C3
      - Result passage disposed without unit P8-S2-C4
      - Result passage disposed without unit P10-S1-C4
      - Result passage disposed without unit P10-S1-C5
      - Result passage disposed without unit P10-S1-C6
      - Result passage disposed without unit P10-S1-C7
      - Result passage disposed without unit P10-S1-C9
      - Result passage disposed without unit P10-S2-C12
      - Result passage disposed without unit P11-S1-C1
      - Result passage disposed without unit P11-S1-C2
      - Result passage disposed without unit P11-S1-C5
      - Result passage disposed without unit P11-S2-C7
      - 'window 12: invalid/duplicate disposition P11-S2-C10'
      - Result passage disposed without unit P11-S2-C10
      unattached_null_or_qualifier_ids:
      - P6-S2-C4
      - P7-S1-C2
      - P7-S1-C4
      - P7-S1-C10
      - P8-S1-C3
      suppressed_nonrepresented_units: 11
      default_disposition_count_requires_completeness_check: 215
      unselected_timing_passages:
      - P1-S1-C11
      - P2-S2-C7
      - P3-S1-C9
      - P3-S1-C10
      - P3-S2-C3
      - P3-S2-C4
      - P3-S2-C12
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P9-S1-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P5-S1-C10
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: tested_personal_effects
        source_id: P5-S2-C4
        reason: No current-result classification; a covariate description is not an
          individual test
      empty_frame_slots_require_confirmation:
      - validation
      - analysis_restrictions
      - personal_factors
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-9-1
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
        - P4-S2
        - P4-S3
        - P6-S1
        - P6-S2
        - P7-S1
        - P7-S2
        - P8-S2
        - P9-S1
        - P9-S2
        - P10-S1
        - P10-S2
        - P10-S3
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 5afbac2f573d594d73c1c2f5910be59fc3db6650fed5f2600634a5146b722423
      source_review: _compare/relationships-2026-11-16/review-current/Brownsett2014
      source_status_sha256: db78cf6ae75b54719848df57c39ab827ef7ccc5035f72e21bef70fdc9031377c
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S2-C3
      disposition: represented
      result_indexes:
      - 0
      reason: Directly states increased activity in midline frontal cortex for noise-vocoded
        vs clear speech in healthy participants.
    - source_id: P1-S2-C4
      disposition: represented
      result_indexes:
      - 1
      reason: Directly states the same region was activated in aphasic patients listening
        to standard sentences.
    - source_id: P1-S2-C6
      disposition: represented
      result_indexes:
      - 2
      reason: Directly states activity correlated significantly with patients' communicative
        abilities.
    - source_id: P1-S2-C7
      disposition: represented
      result_indexes:
      - 2
      reason: Qualifies the correlation as not influenced by lesion size or age.
    - source_id: P3-S1-C6
      disposition: represented
      result_indexes:
      - 26
      reason: States changes were not mirrored by functional imaging data before and
        after training.
    - source_id: P3-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Mentions null results are not included in the paper for brevity.
    - source_id: P4-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes preliminary behavioural testing to justify the use of 3-channel
        vocoding.
    - source_id: P5-S3-C15
      disposition: background_or_descriptive
      result_indexes: []
      reason: Section header for behavioural results.
    - source_id: P5-S4-C1
      disposition: represented
      result_indexes:
      - 3
      reason: States repetition performance correlated significantly between sessions.
    - source_id: P5-S4-C2
      disposition: represented
      result_indexes:
      - 3
      reason: States no significant differences between sessions using any of the
        three measures.
    - source_id: P6-S1-C1
      disposition: represented
      result_indexes:
      - 4
      reason: States healthy participants were better at repeating normal speech than
        vocoded speech.
    - source_id: P6-S1-C2
      disposition: represented
      result_indexes:
      - 4
      reason: Provides statistical support for the difference before training.
    - source_id: P6-S1-C3
      disposition: represented
      result_indexes:
      - 4
      reason: Provides statistical support for the difference after training.
    - source_id: P6-S1-C4
      disposition: represented
      result_indexes:
      - 5
      reason: States significant difference between pre- and post-training repeat
        vocoded trials.
    - source_id: P6-S1-C5
      disposition: represented
      result_indexes:
      - 5
      reason: Provides mean percentage improvement and statistical significance for
        vocoded stimuli.
    - source_id: P6-S1-C6
      disposition: represented
      result_indexes:
      - 6
      reason: States no difference on repeat normal spoken sentence trials as a result
        of training.
    - source_id: P6-S1-C7
      disposition: represented
      result_indexes:
      - 6
      reason: Provides statistical support for the null effect on normal speech.
    - source_id: P6-S1-C8
      disposition: represented
      result_indexes:
      - 7
      reason: States no difference between patients (normal speech) and healthy participants
        (vocoded speech).
    - source_id: P6-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Conclusion that the aim of comparable difficulty was achieved.
    - source_id: P6-S2-C2
      disposition: represented
      result_indexes:
      - 8
      reason: States no greater activity in grey matter regions in response to ListNorm
        across sessions.
    - source_id: P6-S2-C4
      disposition: represented
      result_indexes:
      - 9
      reason: Qualifies the main effect of task by stating there was no Task x Session
        interaction.
    - source_id: P6-S2-C5
      disposition: represented
      result_indexes:
      - 9
      reason: Lists the extensive activation found in the main effect of Task.
    - source_id: P7-S1-C1
      disposition: represented
      result_indexes:
      - 9
      reason: Continues the list of activated regions for the main effect of Task.
    - source_id: P7-S1-C2
      disposition: represented
      result_indexes:
      - 9
      reason: Identifies additional activated areas in patients with intact tissue.
    - source_id: P7-S1-C3
      disposition: represented
      result_indexes:
      - 9
      reason: Lists subcortical regions activated in the main effect of Task.
    - source_id: P7-S1-C4
      disposition: represented
      result_indexes:
      - 10
      reason: Describes the contrast between ListNorm and repeat trials.
    - source_id: P7-S1-C7
      disposition: represented
      result_indexes:
      - 11
      reason: States a main effect of session revealed activation in the precuneus.
    - source_id: P7-S1-C8
      disposition: represented
      result_indexes:
      - 12
      reason: States no differences between sessions for either task relative to ListWhite.
    - source_id: P7-S1-C10
      disposition: represented
      result_indexes:
      - 13
      reason: Identifies the Task x Intelligibility interaction in specific brain
        regions.
    - source_id: P7-S2-C1
      disposition: represented
      result_indexes:
      - 13
      reason: References Figure 6 for the interaction.
    - source_id: P7-S2-C2
      disposition: represented
      result_indexes:
      - 14
      reason: States dACC/SFG was activated by ListVoc relative to other conditions.
    - source_id: P7-S2-C3
      disposition: represented
      result_indexes:
      - 15
      reason: States ListVoc vs ListNorm contrast showed activity in salience and
        central executive networks.
    - source_id: P8-S1-C1
      disposition: represented
      result_indexes:
      - 16
      reason: States the reverse contrast (easier vs difficult) demonstrated the default
        mode network.
    - source_id: P8-S1-C3
      disposition: represented
      result_indexes:
      - 17
      reason: States no voxels survived threshold for session interactions.
    - source_id: P8-S1-C4
      disposition: represented
      result_indexes:
      - 17
      reason: Concludes training effects on brain activity were not apparent in univariate
        ANOVA.
    - source_id: P8-S1-C7
      disposition: represented
      result_indexes:
      - 18
      reason: States healthy participants had greater activity in the default mode
        network (precuneus, etc.).
    - source_id: P8-S1-C8
      disposition: represented
      result_indexes:
      - 18
      reason: Identifies additional greater activity in left ventral prefrontal cortex
        and right medial planum temporale.
    - source_id: P8-S1-C9
      disposition: represented
      result_indexes:
      - 19
      reason: States patients had greater activity in the salience network.
    - source_id: P8-S1-C11
      disposition: represented
      result_indexes:
      - 20
      reason: States no differences in the comparison of patients (ListNorm) vs healthy
        (ListVoc).
    - source_id: P9-S1-C4
      disposition: represented
      result_indexes:
      - 21
      reason: States picture description score was not significantly different between
        sessions.
    - source_id: P9-S1-C5
      disposition: represented
      result_indexes:
      - 22
      reason: States no difference between sessions for dACC/SFG activation effect
        size.
    - source_id: P9-S1-C7
      disposition: represented
      result_indexes:
      - 23
      reason: States significant positive correlation between dACC/SFG activation
        and picture description scores.
    - source_id: P9-S1-C9
      disposition: represented
      result_indexes:
      - 24
      reason: States the regression model was statistically significant and accounted
        for 50% of variance.
    - source_id: P9-S1-C10
      disposition: represented
      result_indexes:
      - 25
      reason: States dACC/SFG activation predicted score, but age and lesion volume
        did not.
    - source_id: P11-S4-C3
      disposition: represented
      result_indexes:
      - 26
      reason: States no evident functional imaging correlate for training in either
        group.
    - source_id: P11-S3-C11
      disposition: represented
      result_indexes:
      - 27
      reason: States ability to repeat did not improve after therapy.
    - source_id: P11-S3-C12
      disposition: represented
      result_indexes:
      - 27
      reason: States online repetition during scanning did not improve.
    unresolved_coverage:
    - source_id: P6-S1-C9
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P7-S2-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P8-S1-C4
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P7-S1-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P7-S2-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S1-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S1-C12
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S2-C1
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S2-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S2-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S2-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S1-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S1-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S1-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S1-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S1-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S1-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S1-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S1-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S2-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S2-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S2-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S2-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S2-C12
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C1
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S2-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S2-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S2-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S3-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S3-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S3-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S2-C7
    - P3-S1-C7
    - P4-S1-C7
    - P5-S3-C15
    - P6-S2-C4
    - P7-S1-C6
    - P7-S2-C4
    - P8-S1-C2
    - P8-S1-C12
    - P8-S2-C1
    - P8-S2-C2
    - P8-S2-C3
    - P8-S2-C4
    - P10-S1-C4
    - P10-S1-C5
    - P10-S1-C6
    - P10-S1-C7
    - P10-S1-C8
    - P10-S1-C9
    - P10-S1-C10
    - P10-S1-C11
    - P10-S2-C2
    - P10-S2-C3
    - P10-S2-C5
    - P10-S2-C6
    - P10-S2-C12
    - P11-S1-C1
    - P11-S1-C2
    - P11-S1-C3
    - P11-S1-C5
    - P11-S2-C7
    - P11-S2-C9
    - P11-S2-C10
    - P11-S3-C4
    - P11-S3-C8
    - P11-S3-C9
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-9-1
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P3-S1-C10
      - P3-S2-C12
      recruited_sample:
      - P3-S1-C9
      - P3-S1-C10
      eligibility:
      - P3-S1-C10
      - P3-S2-C10
      - P3-S2-C11
      - P11-S4-C7
      imaging_provenance:
      - P5-S1-C10
      imaging_timing:
      - P3-S2-C14
      - P3-S2-C15
      - P3-S2-C16
      - P6-S1-C11
      outcome_timing:
      - P3-S2-C16
      - P5-S3-C7
      - P5-S3-C10
      - P6-S1-C11
      outcome_definition:
      - P5-S2-C5
      - P5-S2-C6
      - P5-S2-C7
      - P5-S2-C8
      - P5-S3-C11
      - P5-S3-C12
      - P5-S3-C13
      - P5-S3-C14
      validation: []
      analysis_restrictions: []
      dependent_variable_statement:
      - P5-S2-C4
      - P8-S2-C9
      - P9-S1-C8
      limitations:
      - P11-S4-C4
      - P11-S4-C5
      - P11-S4-C6
      - P11-S4-C7
      personal_factors: []
      tested_personal_effects:
      - P9-S1-C10
      - P11-S2-C10
      adjustment_roles:
      - P5-S2-C4
      - P9-S1-C8
      - P9-S1-C10
      - P11-S2-C10
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P3-S1-C10
      - P3-S2-C3
      - P3-S2-C4
      - P3-S2-C5
      - P3-S2-C6
      - P3-S2-C11
      - P3-S2-C12
    outcome_type: both_reported
    imaging_vs_outcome: mixed
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P9-S1-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P5-S1-C10
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: tested_personal_effects
      source_id: P5-S2-C4
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
      pdf_sha256: 5afbac2f573d594d73c1c2f5910be59fc3db6650fed5f2600634a5146b722423
      review_sha256: 516f4bdba234f7b90802a5ca706b5074ba75ac6f5ec61775889a14e0ff9efcf9
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
      - P6-S1-C1
      - P6-S1-C2
      - P6-S1-C3
      source_result: Healthy participants performed significantly better at repeating
        sentences after listening to normal speech (ListNorm) than after listening
        to noise-vocoded speech (ListVoc), as measured by the combined semantic and
        articulation score. This difference was significant both before training (t(15)=13,
        P<0.001) and after training (t(16)=11.6, P<0.001).
      result_status: detected
      patient_measurement: non_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis corresponds to the behavioral comparison in
            healthy participants between ListNorm and ListVoc conditions, using the
            combined semantic and articulation score, as described in P6-S1-C1 through
            P6-S1-C3.
          source_ids:
          - P6-S1-C1
          - P6-S1-C2
          - P6-S1-C3
        direction:
          answer: fits
          reason: The source explicitly states that healthy participants were 'better
            at repeating after listening to normal speech trials (ListNorm) than listening
            to vocoded speech trials (ListVoc)' (P6-S1-C1), and the proposed claim
            preserves this direction of association.
          source_ids:
          - P6-S1-C1
        construct:
          answer: fits
          reason: The exposure (ListNorm vs ListVoc) and outcome (repetition performance
            via combined semantic and articulation score) are correctly identified.
            The measurement is behavioral (non-imaging) in the healthy group, distinct
            from the patient imaging analysis.
          source_ids:
          - P6-S1-C1
          - P6-S1-C2
          - P5-S2-C5
        qualifications:
          answer: fits
          reason: The proposed draft includes the qualification that performance on
            normal speech trials was at ceiling, which is supported by P6-S1-C7. The
            timing (before/after training) is correctly reflected in the claim.
          source_ids:
          - P6-S1-C7
          - P6-S1-C2
          - P6-S1-C3
        missing_material_caveat:
          answer: fits
          reason: No material caveats are missing. The draft correctly notes the ceiling
            effect on normal speech and the specific training context. The distinction
            between healthy and patient groups is maintained.
          source_ids:
          - P6-S1-C7
          - P6-S1-C4
      optional_pending:
      - sample.time_post_onset
      - exact_statistical_values
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
    - exact_statistical_values
    normalizations:
    - field: sample.time_post_onset
      original: measured before and after a 2-week training programme on discriminating
        noise-vocoded speech
      action: not_transcribed
      reason: 'Numbers not grounded in usable selected source readings: 2'
    analysis_identity:
      id: R005
      exposure:
        text: listening to normal speech (ListNorm) vs vocoded speech (ListVoc)
      outcome:
        text: repetition performance (combined semantic and articulation score)
      analysis_label: Healthy participant intelligibility contrast
      relation: association
      evidence_ids:
      - P6-S1-C1
      - P6-S1-C2
      - P6-S1-C3
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
        pdf_sha256: 5afbac2f573d594d73c1c2f5910be59fc3db6650fed5f2600634a5146b722423
        source_review: _compare/relationships-2026-11-16/review-current/Brownsett2014
        source_status_sha256: db78cf6ae75b54719848df57c39ab827ef7ccc5035f72e21bef70fdc9031377c
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P6-S1-C2:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 5afbac2f573d594d73c1c2f5910be59fc3db6650fed5f2600634a5146b722423
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 57a2b797804d49cd63a6e69fd63062e614d05c7e13864238d4474f551654de1c
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P6-S1-C2
          page: 6
          text_layer_sha256: 57a2b797804d49cd63a6e69fd63062e614d05c7e13864238d4474f551654de1c
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Before training, using the com-

          bined semantic and articulation score as the measure: t(15) = 13;

          two-tailed; P 5 0.001; 95% conﬁdence interval (CI) = 42.6–59.4.'
        anchor_text: 'Before training, using the com-

          bined semantic and articulation score as the measure: t(15) = 13;

          two-tailed; P 5 0.001; 95% conﬁdence interval (CI) = 42.6–59.4.'
        excluded_fragments: []
        image_sha256: 70cf08564a9bc920a6d42d5438d592ccf41b1a7ef45d64c29b3c7a13da5c2c8f
        transcription: '. Before training, using the com-

          bined semantic and articulation score as the measure: $t(15) = 13$;

          two-tailed; $P < 0.001$; 95% confidence interval (CI) = 42.6–59.4.'
      P6-S1-C3:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 5afbac2f573d594d73c1c2f5910be59fc3db6650fed5f2600634a5146b722423
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: ed5fbf283473cf026b78f2a80901abafa2d2e4984989d787298b0e7329216735
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P6-S1-C3
          page: 6
          text_layer_sha256: ed5fbf283473cf026b78f2a80901abafa2d2e4984989d787298b0e7329216735
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: 'After

          training:

          t(16) = 11.6,

          two-tailed;

          P 5 0.001;

          95%

          CI = 28.2–40.7.'
        anchor_text: 'After

          training:

          t(16) = 11.6,

          two-tailed;

          P 5 0.001;

          95%

          CI = 28.2–40.7.'
        excluded_fragments: []
        image_sha256: 9bb4ab156d0c3932c9f00fac3e7f92024fec38c89aa7a48cdf9b65e0490b3aec
      P3-S2-C12:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 5afbac2f573d594d73c1c2f5910be59fc3db6650fed5f2600634a5146b722423
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: a29506b42782abfde5effbc2d3ee44d7ea0f0c0f53931fa41320e6e1ba325c8d
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S2-C12
          page: 3
          text_layer_sha256: a29506b42782abfde5effbc2d3ee44d7ea0f0c0f53931fa41320e6e1ba325c8d
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Seventeen participants completed the study (11 females; mean

          age 60 years; range, 25–82 years) with a mean duration of formal

          education of 15 years (range 10–20 years).'
        anchor_text: 'Seventeen participants completed the study (11 females; mean

          age 60 years; range, 25–82 years) with a mean duration of formal

          education of 15 years (range 10–20 years).'
        excluded_fragments: []
        image_sha256: e6c0b400dc8f99788166f352fdb48b27ba7eeb3e9ef98e3788d388af14f36c35
        transcription: '. Seventeen participants completed the study (11 females;
          mean

          age 60 years; range, 25–82 years) with a mean duration of formal

          education of 15 years (range 10–20 years)'
      P6-S1-C7:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 5afbac2f573d594d73c1c2f5910be59fc3db6650fed5f2600634a5146b722423
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: ecb73b0663d487681c6a4802b84a21e90c13604a0e9202fbe8021748a487ea44
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P6-S1-C7
          page: 6
          text_layer_sha256: ecb73b0663d487681c6a4802b84a21e90c13604a0e9202fbe8021748a487ea44
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: "Performance was at ceiling at both time-\npoints: t(15) =\
          \ 1.5, P 4 0.1, two-tailed; 95% CI = \x040.4–2.5."
        anchor_text: "Performance was at ceiling at both time-\npoints: t(15) = 1.5,\
          \ P 4 0.1, two-tailed; 95% CI = \x040.4–2.5."
        excluded_fragments: []
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 6
  quote: '

    Healthy participants

    Predictably, the healthy participants were better at repeating after

    listening to normal speech trials (ListNorm) than listening to

    vocoded speech trials (ListVoc).'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-23'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
