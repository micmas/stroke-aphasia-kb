---
id: treatment_intensity
name: treatment intensity
kind: ingredient
findings:
- id: f1
  target: mit_repetition_trained_items
  target_kind: impairment
  claim: Treatment intensity predicted outcome on the repetition of trained items
    on the MIT task.
  direction: likely
  relationship: correlational
  method: behavioral_only
  sample:
    n: 27
    population: patients with severe nonfluent aphasia after left hemisphere stroke
    phase: not_reported
    time_post_onset: subacute phase (2 to 3 months poststroke)
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Study is underpowered
  - Lesion characteristics were not documented in detail
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Treatment intensity was measured as the total time
    spent in therapy, including face-to-face sessions (minimum 3 h/wk) and homework
    assignments, recorded by therapists and patients/relatives. Analysis included
    all patients who received MIT (both early and delayed groups); Measured using
    univariable linear regression. Additional metadata has not been transcribed; review
    the pending-field flags before approval. PDF image reading (P3-S1-C8, two-model
    agreement, human verification pending): . Inclusion crite-

    ria were: aphasic after left hemisphere stroke, time

    poststroke 2 to 3 months, premorbidly right-handed, age 18

    to 80 years, native language Dutch, and MIT candidate Original text-layer quotation
    is preserved below. PDF image reading (P1-S2-C20, two-model agreement, human verification
    pending): . A total of 27 participants were included: n = 16 in the experimental
    group

    and n = 11 in the control group Original text-layer quotation is preserved below.'
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
    - proposed_concept:mit_repetition_trained_items
  therapy:
    id: mit
    name: Melodic Intonation Therapy
  citation: '@vanderMeulen2014'
  source_passages:
  - section: Original source P5-S2-C2
    page: 5
    quote: 'Treatment intensity predicted outcome on the repeti-

      tion of trained items, MIT task (β = .04, p = .02).'
    supports: claim
  - section: Original source P4-S1-C11
    page: 4
    quote: "Potential determinants, that is, \nage, gender, severity of the aphasia\
      \ (score AAT Token Test), \ntreatment intensity, time poststroke at start of\
      \ MIT, patients’ \nlinguistic profile at the start of MIT: preMIT scores on\
      \ AAT \nlanguage repetition, AAT auditory comprehension, and the \nnonverbal\
      \ SAT were examined for all outcome measures by \nmeans \nof \nunivariable \n\
      linear \nregression \nanalyses."
    supports: method
  - section: Original source P3-S1-C8
    page: 3
    quote: "Inclusion crite-\nria were: aphasic after left hemisphere stroke, time\
      \ \npoststroke 2 to 3 months, premorbidly right-handed, age 18 \nto 80 years,\
      \ native language Dutch, and MIT candidate."
    supports: sample
  - section: Original source P3-S2-C12
    page: 3
    quote: "Therapists recorded therapy time per session, and patients \nor a close\
      \ relative recorded homework time per session."
    supports: method
  - section: Original source P1-S2-C20
    page: 1
    quote: "A total of 27 participants were included: n = 16 in the experimental group\
      \ \nand n = 11 in the control group."
    supports: sample
  - section: Original source P6-S1-C2
    page: 6
    quote: "The study is too underpowered to obtain significant \neffects on most\
      \ of the outcome measures, which is a clear \nlimitation of the study."
    supports: limitation
  - section: Original source P7-S3-C8
    page: 7
    quote: "Earlier studies reported age \nand initial aphasia severity to be important\
      \ predictors for \nlanguage recovery; however, these results are inconsistent\
      \ \nand the relation between these factors and the type of inter-\nvention is\
      \ not clear.3,5,11,41 Neurological variables, such as \nsize and location of\
      \ the lesion, may play an important \nrole.3,5,41,42 A limitation of the present\
      \ study is that lesion \ncharacteristics were not documented in detail."
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-26'
relationship_review:
  paper: vanderMeulen2014
  proposal_id: R010
  review_status_sha256: cac789243492b5b56fdf713988fc073da19ae1a45fa69f1ea43e8d9b37a574f1
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 04872e832b3dd08071e0e1417d6153c0af85d54dc3008dd0b49cc86d09e623fb
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 04872e832b3dd08071e0e1417d6153c0af85d54dc3008dd0b49cc86d09e623fb
        A/passages.json: c6691f5408bde59bf1136ffe102c06660a6dc18b036c179fb483bfe3623a1225
        A/raw.json: 2c1e699ae3e50bef8defcf2b3b62f84e5a198722e89823cb0868e17438c3c6f9
        A/source-units.json: f0045de2b05a928b6073444865b1aa5ef3673ee6a5f02172e0ab340c6b608941
        A/full-source-units.json: de0a44591e532101c27e436ddba495cf0f78a037ce9ecdf57c35d9f25c3bb2b4
        A/meta.json: 14aa2207e1ec9967df951b3fd85e24421643b626b8f606e83b9cd1a10f4a6f27
        A/table-images/page-5.png: 9a2b44407bed1b8a3679fa33d5267c61f1d78b3afebc3e7fb2802f935aea1be4
        A/table-images/page-4.png: 292fee8863d94134c4ccd65e4b68f746a85799f2a4519e5b71e6f7ccbaf5f9d1
        A/table-images/TABLE-1-page-4-1.png: 0b856630edb37a72dce9f8e6a74bece1eb451a298f8155a50e9baec3fdca6080
        A/table-images/manifest.json: dcdfef7fbda5e167095d3d7f894a8ecf12a0fd3a4b65fb4d8f27721ecabc6afe
        A/table-images/TABLE-2-page-5-1.png: 1ad11133422d18465591c17ddf120507a74e974a4fa62c5fa4ae3bca0fca42b3
        A/clauses/window-03/raw.json: 2fe03dd51eeaaa656e9e057ab340aef00ac296559d19eef9994dea7e77b41d77
        A/clauses/window-03/prompt.txt: 3f2091f4e0ae46f45cc45990c43b924f9b8411ca8b35b7fa09771c62ed2d4436
        A/clauses/window-03/meta.json: 226bdf7533a4f3d96df0ba65fd6b63a89c594f2d2f1ec7dd9a3e7e7caba6124d
        A/clauses/window-04/raw.json: bf7d5700dcea79491f81a5fb699f7db98fb1b64928427c7c6814123bbcd3bfd0
        A/clauses/window-04/prompt.txt: 434ead31ce475a435a6b1da166ede281ed441ccd74352ff31ff8c63c02257272
        A/clauses/window-04/meta.json: f219b7062be4a029c8bb0cd64d006841474ae85b18d3bd1f36e6e32d5f0cd03c
        A/clauses/window-05/raw.json: ccfaaa3d31c46810b819d045bab5ba0748b17e799bc2fc847a720741ee69407b
        A/clauses/window-05/prompt.txt: 84ae40dd92492d3788144a1cea00ddce67479f078ce09306c373b4316dc4f4ff
        A/clauses/window-05/meta.json: daf40c7520a8b79e52905777e7cfc531702e7a06fae0081f744348f0fc18b12f
        A/clauses/window-02/raw.json: 8829b0a14af210a05e7554a97050c246f7d79ed6cbd82652cacb39a292eb6eed
        A/clauses/window-02/prompt.txt: 669f60bf007af498652bd98d594c5a8a10a2cc819584447b03287e053c489775
        A/clauses/window-02/meta.json: 7c31b8c572500c6bf8e0fda91acf1a779846afb702a314f0e993ab927458ebeb
        A/clauses/window-07/raw.json: 8f7ec69bcbc4bec154ecf2eb79abb27e7f8df91c3c1248a35f10f7eb7482af2b
        A/clauses/window-07/prompt.txt: 58a2c6339f02b147f3a918a639f91a98ed31b4d748451d8c49b07b7b07d250b1
        A/clauses/window-07/meta.json: 1758c7fc79af7a14d4d5d48c67c3db51e451174f8b27c06481b1527ef909a6c9
        A/clauses/window-01/raw.json: dbcf62f4230c2b1cfcd0b361e97f32557109a87d16064dbabfbdcbaf577acbea
        A/clauses/window-01/prompt.txt: 0c7cfe327642fca1effb6673223d3c089e809d85b3b60a94338eecd2129760cc
        A/clauses/window-01/meta.json: 774329b54d45c3edd584676502fc7973e0e2d0038d73b22f469281dd31dd558b
        A/clauses/window-06/raw.json: 941600a8801182ff38fa173383959b7f22fb7431222ab6bbe9843e502db4f9cc
        A/clauses/window-06/prompt.txt: 0d4f982e798316c4fa7da4053bd670d5ac6e231205e72b085f4a3565a1e5f5f2
        A/clauses/window-06/meta.json: fdc0fe498f3e944e6141cb4b4af459eb8fba59b54e1af5f12713fa4f59ec528a
        A/tables/TABLE-2-page-5-2/raw.json: 59031c48756a696311ab5c7660931064d36c4b6f0a46444c03c33274c2575f86
        A/tables/TABLE-2-page-5-2/prompt.txt: 943ddc69a9609171c653692e5264eaaf7a23a3c7a610fede4698cb8bc9e4b15d
        A/tables/TABLE-2-page-5-2/meta.json: 236214331784dde51b684114b224261f02e67330767f8255bdfc782ddbc98326
        A/tables/TABLE-1-page-4-1/raw.json: 415066b6c007f689f2da78c20f08bd0c3f028fd1a56ae76c6f613576f80e9d51
        A/tables/TABLE-1-page-4-1/prompt.txt: ffc2898d9896458282ff3171f05bc3d36524a99cfaf23bf01faf81ce4bac103d
        A/tables/TABLE-1-page-4-1/meta.json: cfbddf3929cb7ad35b9a812c199c275e4188e7f4627bd3d332cec185ae256c25
        B/passages.json: c6691f5408bde59bf1136ffe102c06660a6dc18b036c179fb483bfe3623a1225
        B/raw.json: 945d935fd83cbb806c13a65885cfacf48ccbb031a74c144b1b74754759079444
        B/source-units.json: f0045de2b05a928b6073444865b1aa5ef3673ee6a5f02172e0ab340c6b608941
        B/full-source-units.json: de0a44591e532101c27e436ddba495cf0f78a037ce9ecdf57c35d9f25c3bb2b4
        B/meta.json: 2cef8aeede7b1b54171882e7f41cf8482357cb61ae5f1e433f8796dacac379db
        B/table-images/page-5.png: 9a2b44407bed1b8a3679fa33d5267c61f1d78b3afebc3e7fb2802f935aea1be4
        B/table-images/page-4.png: 292fee8863d94134c4ccd65e4b68f746a85799f2a4519e5b71e6f7ccbaf5f9d1
        B/table-images/TABLE-1-page-4-1.png: 0b856630edb37a72dce9f8e6a74bece1eb451a298f8155a50e9baec3fdca6080
        B/table-images/manifest.json: ea356df2842a3404ca4928a763df82bb439a16ee25d8531e93b04c4a24167468
        B/table-images/TABLE-2-page-5-1.png: 1ad11133422d18465591c17ddf120507a74e974a4fa62c5fa4ae3bca0fca42b3
        B/clauses/window-03/raw.json: 6c6fee2877b34eb7ac18a53c7ca5d23990eadc620373a9722fd8797d632fd02b
        B/clauses/window-03/prompt.txt: 3f2091f4e0ae46f45cc45990c43b924f9b8411ca8b35b7fa09771c62ed2d4436
        B/clauses/window-03/meta.json: d762f419c92f74932fc6e7e7385b4b0a92464f7dac5e332afca07c152e140221
        B/clauses/window-04/raw.json: 0cc6e24a0e31c9c409080563aeba045448888644d2a07bf881d90946d77c76b3
        B/clauses/window-04/prompt.txt: 434ead31ce475a435a6b1da166ede281ed441ccd74352ff31ff8c63c02257272
        B/clauses/window-04/meta.json: 0aa93507b55992822ba7aa5b73c9f9949828a4633f7b27dcdb5832d6b55607a7
        B/clauses/window-05/raw.json: fdc38b7e92c95da480f0e569d771e27bba86b1e79d1f5f3cbc12f9e9c8565a4f
        B/clauses/window-05/prompt.txt: 84ae40dd92492d3788144a1cea00ddce67479f078ce09306c373b4316dc4f4ff
        B/clauses/window-05/meta.json: a13444e8781096d11c0a73c42186bd5ac79fd91637540e427850b99649d28ddf
        B/clauses/window-02/raw.json: ea800565953a6e60ac3e6f37c5e2bb1ccd9c8465e568f40c66dd6b5b3a3cf155
        B/clauses/window-02/prompt.txt: 669f60bf007af498652bd98d594c5a8a10a2cc819584447b03287e053c489775
        B/clauses/window-02/meta.json: bcf39cb70758c7b1425c4fe82cbabc9d3721811d4c495a4cb1c33b5a7cfad056
        B/clauses/window-07/raw.json: 8f7ec69bcbc4bec154ecf2eb79abb27e7f8df91c3c1248a35f10f7eb7482af2b
        B/clauses/window-07/prompt.txt: 58a2c6339f02b147f3a918a639f91a98ed31b4d748451d8c49b07b7b07d250b1
        B/clauses/window-07/meta.json: 7f43084a085b99d7176dae2a8048f2c3119ca342fcd79972a9590d67e86e4bb0
        B/clauses/window-01/raw.json: b2b5395b4b0f4dabc505e28e178ec7693f2c5840ce8b7c80581b068453a75831
        B/clauses/window-01/prompt.txt: 0c7cfe327642fca1effb6673223d3c089e809d85b3b60a94338eecd2129760cc
        B/clauses/window-01/meta.json: 89b3aa18543a6094c83c2c0f7567071466e232490131d09afb30b501bc6f25f1
        B/clauses/window-06/raw.json: 40e998a0406988605e5a9417c67fb5261e80eb664deabf88146dbefabfaf74b8
        B/clauses/window-06/prompt.txt: 0d4f982e798316c4fa7da4053bd670d5ac6e231205e72b085f4a3565a1e5f5f2
        B/clauses/window-06/meta.json: ad39b8b21360e951467a23112ba711fc40fb364932e8e26733aa2f7ac59a3cfc
        B/tables/TABLE-2-page-5-2/raw.json: 185c5e85ee0e448b540420364088d36276ab10a06e2dfb31348b848059e3b8b3
        B/tables/TABLE-2-page-5-2/prompt.txt: 943ddc69a9609171c653692e5264eaaf7a23a3c7a610fede4698cb8bc9e4b15d
        B/tables/TABLE-2-page-5-2/meta.json: 4416bec881e390876ee545a3e39a396b0d3a9c6a590188d3a31321882e270085
        B/tables/TABLE-1-page-4-1/raw.json: 26c2aa6a32fa16b9dcd83dc9e1d714dc11ad9f6b599bda4e406545ca9a4287ca
        B/tables/TABLE-1-page-4-1/prompt.txt: ffc2898d9896458282ff3171f05bc3d36524a99cfaf23bf01faf81ce4bac103d
        B/tables/TABLE-1-page-4-1/meta.json: 3cdc1c69c9b1084006579619811b49289e56f9c0c3ba25b4d4ac0444aba0fc21
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
      pdf_sha256: 04872e832b3dd08071e0e1417d6153c0af85d54dc3008dd0b49cc86d09e623fb
      source_review: _compare/relationships-2026-11-16/review-current/vanderMeulen2014
      source_status_sha256: 4b417f874a602ac9739cc3dfbe99d123f209431f428507e5f67e26c4b6772a98
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R010
    exposure:
      text: treatment intensity
    outcome:
      text: repetition of trained items (MIT task)
    analysis_label: Determinants for Therapy Outcome
    relation: association
    evidence_ids:
    - P5-S2-C2
    qualifier_ids:
    - P4-S1-C11
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 04872e832b3dd08071e0e1417d6153c0af85d54dc3008dd0b49cc86d09e623fb
      source_review: _compare/relationships-2026-11-16/review-current/vanderMeulen2014
      source_status_sha256: 4b417f874a602ac9739cc3dfbe99d123f209431f428507e5f67e26c4b6772a98
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Accounting without a linked unit P1-S2-C10
      - Unaccounted source passage P1-S2-C10
      - Accounting without a linked unit P1-S2-C18
      - Accounting without a linked unit P1-S2-C21
      - Accounting without a linked unit P1-S2-C22
      - Accounting without a linked unit P1-S2-C23
      - Accounting without a linked unit P1-S3-C5
      - Unaccounted source passage P1-S3-C5
      - Unaccounted source passage P1-S2-C18
      - Unaccounted source passage P1-S2-C22
      - Unaccounted source passage P1-S2-C23
      - Unaccounted source passage P1-S2-C21
      - Result passage disposed without unit P3-S2-C3
      - Result passage disposed without unit P5-S1-C2
      - Result passage disposed without unit P5-S1-C10
      - Result passage disposed without unit P5-S1-C11
      - Accounting without a linked unit P5-S1-C6
      - Accounting without a linked unit P5-S1-C7
      - Accounting without a linked unit P5-S1-C8
      - Accounting without a linked unit P5-S1-C9
      - Unaccounted source passage P5-S1-C6
      - Unaccounted source passage P5-S1-C7
      - Unaccounted source passage P5-S1-C8
      - Unaccounted source passage P5-S1-C9
      - Result passage disposed without unit P5-S1-C13
      - Result passage disposed without unit P5-S2-C1
      - Result passage disposed without unit P5-S2-C4
      - Result passage disposed without unit P5-S2-C6
      - Result passage disposed without unit P5-S2-C7
      - Result passage disposed without unit P5-S2-C10
      - Unresolved source passage P5-S2-C10
      - Result passage disposed without unit P6-S1-C3
      - Result passage disposed without unit P7-S1-C11
      - Accounting without a linked unit P7-S1-C12
      - Accounting without a linked unit P7-S1-C5
      - Accounting without a linked unit P7-S2-C2
      - Accounting without a linked unit P7-S2-C3
      - Unaccounted source passage P7-S1-C12
      - Unaccounted source passage P7-S2-C2
      - Unaccounted source passage P7-S2-C3
      - Unaccounted source passage P7-S1-C5
      - Result passage disposed without unit P7-S2-C9
      - Result passage disposed without unit P7-S3-C5
      - Result passage disposed without unit P8-S1-C1
      unattached_null_or_qualifier_ids:
      - P5-S1-C2
      - P5-S1-C7
      - P5-S1-C8
      - P5-S1-C9
      - P5-S1-C11
      - P5-S1-C13
      - P5-S2-C1
      - P5-S2-C7
      - P6-S1-C3
      suppressed_nonrepresented_units: 18
      default_disposition_count_requires_completeness_check: 122
      unselected_timing_passages:
      - P1-S1-C2
      - P1-S2-C13
      - P3-S1-C8
      - P4-S2-C8
      personal_effect_slots_without_result_classification: []
      held_frame_selections: []
      empty_frame_slots_require_confirmation:
      - imaging_provenance
      - imaging_timing
      - validation
      - analysis_restrictions
      - personal_factors
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
        - P2-S1
        - P2-S2
        - P3-S2
        - P3-S3
        - P4-S2
        - P5-S1
        - P6-S1
        - P7-S2
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 04872e832b3dd08071e0e1417d6153c0af85d54dc3008dd0b49cc86d09e623fb
      source_review: _compare/relationships-2026-11-16/review-current/vanderMeulen2014
      source_status_sha256: 4b417f874a602ac9739cc3dfbe99d123f209431f428507e5f67e26c4b6772a98
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S2-C21
      disposition: represented
      result_indexes:
      - 0
      - 3
      reason: Reports significant effect on trained items and mixed results for untrained
        items.
    - source_id: P1-S2-C22
      disposition: represented
      result_indexes:
      - 2
      reason: Reports significant improvement in verbal communication after MIT.
    - source_id: P1-S2-C23
      disposition: represented
      result_indexes:
      - 4
      reason: Reports delaying MIT related to less improvement in trained material.
    - source_id: P1-S3-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion statement.
    - source_id: P3-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of therapy protocol.
    - source_id: P3-S2-C15
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement about treatment intensity recording.
    - source_id: P4-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement about sample size.
    - source_id: P4-S2-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Baseline gender difference.
    - source_id: P4-S2-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Treatment intensity comparison.
    - source_id: P4-S2-C15
      disposition: background_or_descriptive
      result_indexes: []
      reason: General improvement statement for MIT group.
    - source_id: P4-S2-C16
      disposition: background_or_descriptive
      result_indexes: []
      reason: General improvement statement for control group.
    - source_id: P4-S2-C17
      disposition: represented
      result_indexes:
      - 0
      - 1
      reason: Reports significant difference between groups for MIT repetition (trained)
        and AAT repetition.
    - source_id: P4-S2-C18
      disposition: represented
      result_indexes:
      - 2
      reason: Reports trend for ANELT.
    - source_id: P4-S2-C19
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to Table 1.
    - source_id: P5-S1-C2
      disposition: represented
      result_indexes:
      - 12
      reason: States that controlling for gender and severity did not alter results.
    - source_id: P5-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of mean improvement vs clinical relevance.
    - source_id: P5-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Proportion of participants with improvement >7 on ANELT.
    - source_id: P5-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Non-significant difference in ANELT improvement proportions.
    - source_id: P5-S1-C6
      disposition: represented
      result_indexes:
      - 5
      reason: Main effect of time on all outcome measures.
    - source_id: P5-S1-C7
      disposition: represented
      result_indexes:
      - 6
      - 7
      reason: Time effect present for both groups on repetition, but only experimental
        on functional tasks.
    - source_id: P5-S1-C8
      disposition: represented
      result_indexes:
      - 6
      - 7
      reason: Summary of time effect by group.
    - source_id: P5-S1-C9
      disposition: represented
      result_indexes:
      - 8
      reason: Interaction between time and group for trained items.
    - source_id: P5-S1-C10
      disposition: represented
      result_indexes:
      - 8
      reason: Experimental group improved more on trained items over time.
    - source_id: P5-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Visual inspection of Figure 2.
    - source_id: P5-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement about study power.
    - source_id: P5-S1-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Introductory statement for determinants.
    - source_id: P5-S2-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Introductory statement for determinants.
    - source_id: P5-S2-C2
      disposition: represented
      result_indexes:
      - 9
      reason: Treatment intensity predicted outcome on trained items.
    - source_id: P5-S2-C3
      disposition: represented
      result_indexes:
      - 10
      reason: Time poststroke predicted outcome on untrained items, AAT repetition,
        and ANELT.
    - source_id: P5-S2-C4
      disposition: represented
      result_indexes:
      - 10
      reason: Earlier start of MIT related to greater improvement.
    - source_id: P5-S2-C5
      disposition: represented
      result_indexes:
      - 13
      reason: No significant differences between responders and nonresponders.
    - source_id: P5-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion statement.
    - source_id: P5-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: General improvement statement.
    - source_id: P5-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: General improvement statement.
    - source_id: P5-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: General improvement statement.
    - source_id: P5-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to Table 2.
    - source_id: P5-S2-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Table 2 title.
    - source_id: P5-S2-C12
      disposition: represented
      result_indexes:
      - 0
      - 1
      reason: Table 2 data showing significant group differences for MIT repetition
        (trained) and AAT repetition.
    - source_id: P6-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of ANELT results.
    - source_id: P6-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement about study power.
    - source_id: P6-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: General observation of differences.
    - source_id: P7-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion statement.
    - source_id: P7-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison of Sabadel and ANELT.
    - source_id: P7-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Sabadel failed to show improvement.
    - source_id: P7-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of Sabadel task suitability.
    - source_id: P7-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of ANELT performance.
    - source_id: P7-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Anecdotal reports from partners.
    - source_id: P7-S2-C10
      disposition: represented
      result_indexes:
      - 4
      reason: Delay of 6 weeks related to less improvement.
    - source_id: P7-S2-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of timing effect.
    - source_id: P7-S3-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement about individual differences in success.
    - source_id: P7-S3-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Unable to detect determinants in pre-MIT profile.
    - source_id: P8-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion statement.
    unresolved_coverage:
    - source_id: P4-S2-C19
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P5-S2-C5
      disposition: unresolved
      reason: Unknown result index; not accepted as coverage
    - source_id: P5-S2-C11
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P5-S2-C12
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    pending_source_ids:
    - P1-S3-C5
    - P3-S2-C3
    - P3-S2-C15
    - P4-S2-C9
    - P4-S2-C12
    - P4-S2-C13
    - P4-S2-C15
    - P4-S2-C16
    - P5-S1-C3
    - P5-S1-C4
    - P5-S1-C5
    - P5-S1-C11
    - P5-S1-C12
    - P5-S1-C13
    - P5-S2-C1
    - P5-S2-C6
    - P5-S2-C7
    - P5-S2-C8
    - P5-S2-C9
    - P5-S2-C10
    - P6-S1-C1
    - P6-S1-C2
    - P6-S1-C3
    - P7-S1-C5
    - P7-S1-C11
    - P7-S1-C12
    - P7-S2-C2
    - P7-S2-C3
    - P7-S2-C9
    - P7-S2-C11
    - P7-S3-C5
    - P7-S3-C7
    - P8-S1-C1
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
      - P1-S2-C20
      recruited_sample:
      - P3-S1-C7
      eligibility:
      - P3-S1-C8
      - P3-S1-C9
      - P3-S1-C10
      imaging_provenance: []
      imaging_timing: []
      outcome_timing:
      - P1-S2-C16
      - P3-S2-C17
      outcome_definition:
      - P3-S3-C3
      validation: []
      analysis_restrictions: []
      dependent_variable_statement:
      - P4-S1-C7
      - P4-S1-C9
      - P4-S1-C11
      limitations:
      - P6-S1-C2
      - P7-S3-C8
      - P7-S3-C9
      - P7-S3-C10
      - P7-S3-C11
      personal_factors: []
      tested_personal_effects:
      - P5-S2-C2
      - P5-S2-C3
      adjustment_roles:
      - P4-S1-C7
      - P5-S1-C1
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P4-S3-C5
    outcome_type: change_from_baseline
    imaging_vs_outcome: not_stated
    validation_type: none_described
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
      pdf_sha256: 04872e832b3dd08071e0e1417d6153c0af85d54dc3008dd0b49cc86d09e623fb
      review_sha256: cac789243492b5b56fdf713988fc073da19ae1a45fa69f1ea43e8d9b37a574f1
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
      - P5-S2-C2
      source_result: Treatment intensity predicted outcome on the repetition of trained
        items, MIT task (β = .04, p = .02).
      result_status: detected
      patient_measurement: non_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The source P5-S2-C2 explicitly states that treatment intensity predicted
            outcome on the repetition of trained items in the MIT task. The proposed
            core correctly identifies this specific analysis and outcome.
          source_ids:
          - P5-S2-C2
          - P4-S1-C11
        direction:
          answer: fits
          reason: The source reports a significant association (p = .02). The proposed
            core uses 'likely' to indicate a detected association without overclaiming
            causality or specifying a direction not explicitly detailed in the immediate
            result sentence (though beta is positive, 'likely' is a safe qualitative
            descriptor for a detected predictor).
          source_ids:
          - P5-S2-C2
        construct:
          answer: fits
          reason: Exposure is treatment intensity. Outcome is repetition of trained
            items on the MIT task. The method is univariable linear regression (P4-S1-C11).
            The patient measurement is behavioral (non-imaging), as the MIT task is
            a language production test, not an imaging metric. The definition of treatment
            intensity in the core aligns with P3-S2-C12 (recorded therapy time).
          source_ids:
          - P5-S2-C2
          - P4-S1-C11
          - P3-S2-C12
          - P3-S3-C4
        qualifications:
          answer: fits
          reason: The core includes the qualification that the analysis included all
            patients who received MIT (early and delayed groups), which is supported
            by P4-S1-C10 ('data on all patients pre- and post-MIT were taken into
            account'). It also notes the univariable regression method. The limitations
            regarding underpowering and lesion documentation are correctly included.
          source_ids:
          - P4-S1-C10
          - P4-S1-C11
          - P6-S1-C2
          - P7-S3-C8
        missing_material_caveat:
          answer: fits
          reason: The core captures the key methodological context (univariable regression,
            all patients) and limitations (underpowered, no lesion data). No material
            caveat that changes the interpretation of the specific finding (treatment
            intensity predicting trained item repetition) is omitted.
          source_ids:
          - P4-S1-C11
          - P6-S1-C2
          - P7-S3-C8
      optional_pending: []
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    normalizations:
    - field: bucket
      original: predictors
      action: route_from_kind
      value: ingredients
    analysis_identity:
      id: R010
      exposure:
        text: treatment intensity
      outcome:
        text: repetition of trained items (MIT task)
      analysis_label: Determinants for Therapy Outcome
      relation: association
      evidence_ids:
      - P5-S2-C2
      qualifier_ids:
      - P4-S1-C11
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 04872e832b3dd08071e0e1417d6153c0af85d54dc3008dd0b49cc86d09e623fb
        source_review: _compare/relationships-2026-11-16/review-current/vanderMeulen2014
        source_status_sha256: 4b417f874a602ac9739cc3dfbe99d123f209431f428507e5f67e26c4b6772a98
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P3-S1-C8:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 04872e832b3dd08071e0e1417d6153c0af85d54dc3008dd0b49cc86d09e623fb
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: ae6028f66bb2568eee4cefc1e87ddfbfe5e6fb655e87cacc2b2252b1efd281c4
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S1-C8
          page: 3
          text_layer_sha256: ae6028f66bb2568eee4cefc1e87ddfbfe5e6fb655e87cacc2b2252b1efd281c4
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "Inclusion crite-\nria were: aphasic after left hemisphere\
          \ stroke, time \npoststroke 2 to 3 months, premorbidly right-handed, age\
          \ 18 \nto 80 years, native language Dutch, and MIT candidate."
        anchor_text: "Inclusion crite-\nria were: aphasic after left hemisphere stroke,\
          \ time \npoststroke 2 to 3 months, premorbidly right-handed, age 18 \nto\
          \ 80 years, native language Dutch, and MIT candidate."
        excluded_fragments: []
        image_sha256: a2b0d9a12a4bb3cea4480e445ef0e56fc5d2635f753f58d6082db69122e9091d
        transcription: '. Inclusion crite-

          ria were: aphasic after left hemisphere stroke, time

          poststroke 2 to 3 months, premorbidly right-handed, age 18

          to 80 years, native language Dutch, and MIT candidate'
      P1-S2-C20:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 04872e832b3dd08071e0e1417d6153c0af85d54dc3008dd0b49cc86d09e623fb
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 5a873e970abd28a3c1a38ab69e35d4cc30fcbc27bc2ecb479eb25f5c32e03ab1
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P1-S2-C20
          page: 1
          text_layer_sha256: 5a873e970abd28a3c1a38ab69e35d4cc30fcbc27bc2ecb479eb25f5c32e03ab1
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "A total of 27 participants were included: n = 16 in the experimental\
          \ group \nand n = 11 in the control group."
        anchor_text: "A total of 27 participants were included: n = 16 in the experimental\
          \ group \nand n = 11 in the control group."
        excluded_fragments: []
        image_sha256: 2c6b9da9d9177c5486e7ce8cb6614d29a5d3e49a040e2c621e2270fbc891c72d
        transcription: '. A total of 27 participants were included: n = 16 in the
          experimental group

          and n = 11 in the control group'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 5
  quote: 'Treatment intensity predicted outcome on the repeti-

    tion of trained items, MIT task (β = .04, p = .02).'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-26'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
