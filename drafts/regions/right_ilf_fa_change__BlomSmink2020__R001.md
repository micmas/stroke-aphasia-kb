---
id: right_ilf_fa_change
name: right ILF FA change
kind: tract
findings:
- id: f1
  target: naming_recovery
  target_kind: impairment
  claim: A strong positive correlation was found between FA change in the right ILF
    and change in BNT score, where an increase in FA was associated with considerable
    improvement in naming accuracy, and a decrease in FA was related to limited improvement
    or slight deterioration.
  direction: likely
  relationship: correlational
  method: DTI
  sample:
    n: 10
    population: participants with aphasia after first-ever left-hemisphere stroke
    phase: not_reported
    time_post_onset: subacute stage, with two assessments and scans performed within
      3 months post onset and a 1-month interval between sessions
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Small sample size
  - Predominantly male sample
  - Variability in timing of assessments and scans across individuals
  - DTI provides only indirect measures of white matter tissue properties
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Change in mean fractional anisotropy (FA) of the right
    inferior longitudinal fasciculus (ILF) reconstructed via deterministic tractography
    using manual ROI placement based on a priori anatomical knowledge. The relationship
    was concurrent between the change in FA and the change in BNT score over the 1-month
    interval. Additional metadata has not been transcribed; review the pending-field
    flags before approval. PDF image reading (P1-S2-C9, two-model agreement, human
    verification pending): . Ten participants with aphasia after left-hemisphere stroke
    underwent language testing and diffusion tensor imaging twice within 3 months
    post onset, with a 1-month interval between sessions Original text-layer quotation
    is preserved below. PDF image reading (P2-S2-C4, two-model agreement, human verification
    pending): Methods


    Participants


    Ten participants (7 men; mean age: 61.8 ± 7.8 years) with aphasia due to first-ever
    left-hemisphere stroke completed the study Original text-layer quotation is preserved
    below. PDF image reading (P3-S1-C3, two-model agreement, human verification pending):
    . The first assessment was performed at a mean of

    39.4 ± 14.1 days post onset (range: 17-62 days post onset)

    and the second assessment at a mean of 72.8 ± 14.8 days

    post onset (range: 50-96 days post onset) Original text-layer quotation is preserved
    below. PDF image reading (P9-S2-C8, two-model agreement, human verification pending):
    . Another limitation is that the participants were predominantly male (7 men,
    3 women) Original text-layer quotation is preserved below. Reconcile this new
    analysis with earlier drafts and source-review decisions for the paper; new candidate
    IDs do not carry earlier decisions forward.'
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
    - prior_paper_decisions_reconciliation_pending
    - proposed_concept:naming_recovery
  citation: '@BlomSmink2020'
  source_passages:
  - section: Original source P1-S2-C15
    page: 1
    quote: "A strong positive correlation was found between FA change in the right\
      \ ILF within \nthe ventral stream and change on the BNT (r = 0.91, P < .001)."
    supports: claim
  - section: Original source P6-S1-C11
    page: 6
    quote: "A strong positive correlation was found between FA change \nin the ILF\
      \ and change in BNT score (r = 0.91, P < .001; \nFigure 5); an increase in FA\
      \ was associated with a consider-\nable improvement on the BNT (range BNT change\
      \ score: \n12 to 14), a decrease in FA was related to a limited improve-\n"
    supports: claim
  - section: Original source P1-S2-C9
    page: 1
    quote: "Ten participants with aphasia after left-hemisphere stroke underwent language\
      \ testing and diffusion \ntensor imaging twice within 3 months post onset, with\
      \ a 1-month interval between sessions."
    supports: sample
  - section: Original source P2-S2-C4
    page: 2
    quote: "Methods\nParticipants\nTen participants (7 men; mean age: 61.8 ± 7.8 years)\
      \ with \naphasia due to first-ever left-hemisphere stroke completed \nthe study."
    supports: sample
  - section: Original source P3-S1-C3
    page: 3
    quote: "The first assessment was performed at a mean of \n39.4 ± 14.1 days post\
      \ onset (range: 17-62 days post onset) \nand the second assessment at a mean\
      \ of 72.8 ± 14.8 days \npost onset (range: 50-96 days post onset)."
    supports: method
  - section: Original source P3-S2-C2
    page: 3
    quote: 'Deterministic tractography was used to reconstruct the dor-

      sal and ventral tracts for both hemispheres in native space.'
    supports: method
  - section: Original source P3-S2-C3
    page: 3
    quote: "Using the FA color-coded maps, regions of interest (ROIs) \nwere drawn\
      \ manually on the coronal and axial slices based \non a priori anatomical knowledge."
    supports: method
  - section: Original source P9-S2-C6
    page: 9
    quote: "A first limitation is the \nsmall sample size."
    supports: limitation
  - section: Original source P9-S2-C8
    page: 9
    quote: "Another \nlimitation is that the participants were predominantly male\
      \ \n(7 men, 3 women)."
    supports: limitation
  - section: Original source P9-S2-C12
    page: 9
    quote: "A third limitation is that the time post onset at \nwhich the behavioral\
      \ and tractography data were obtained \nvaried across individuals and between\
      \ measurements."
    supports: limitation
  - section: Original source P9-S3-C5
    page: 9
    quote: "Last, \nDTI tractography provides only indirect measures of white \nmatter\
      \ tissue properties, and, hence, uncertainty exists about \nthe correspondence\
      \ between DTI measures and underlying \nneuroanatomical factors.44\nIn conclusion,\
      \ the present findings provide preliminary \nevidence of a relationship between\
      \ change in white matter \nintegrity in the right ventral stream and naming\
      \ recovery in \nsubacute aphasia."
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-20'
relationship_review:
  paper: BlomSmink2020
  proposal_id: R001
  review_status_sha256: 6cdbabaec32a9cf5079ac05478fbc10dd882e06a972719cae8cfd411d98c657b
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: eced2b5115c01465a6bcf6c63cd51aa6557fe1951db56dbb4a245ddd49aef701
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: eced2b5115c01465a6bcf6c63cd51aa6557fe1951db56dbb4a245ddd49aef701
        A/passages.json: ff4b1c8ed29b3987eae705ee5e6761b8c8f12ffb38bbc70434eebf882719fe2a
        A/raw.json: ced54a95f31911d7f40f4db457e3294a5349395765b250217abc08aded732cac
        A/source-units.json: 7835f71cd5814c23fc9874d12fdd9d58b9cc526532c46e2f0990839c1d1b248f
        A/full-source-units.json: 6d6dc2a753f2ab8ab2acbe0db0b4d9327332aeea4ba726ee5e87f0f46499eaea
        A/meta.json: 2a642ed022a132eca02c7d2234a34eec6fd69e8dfd32a9da9d0948bd051983f5
        A/table-images/TABLE-1-page-3-1.png: 5c9971b3404b4ff7aa7273da0eacf93acfcdcb50427453517b375f1dff205a4a
        A/table-images/page-3.png: f6213235fc137bc6adecdcd6463071e169be07c3e38e2e9413cd2470cb45d18d
        A/table-images/page-6.png: 30255dfc820398fd611fd4d9f05956b62a12609abc668a9d6374a0bed92f810f
        A/table-images/TABLE-3-page-8-1.png: a284ae152a819ffc5a079a6b44217112ede12bfd728a103edae298f289f96c0d
        A/table-images/page-8.png: 373828001e352dc31eaeb9c6baf770e7b428dbfa42accd81462d499edb54e4df
        A/table-images/TABLE-2-page-6-1.png: 139311f4499bdb0434a1a9e444ff1628e72ed9d086a43675d591ed15e91cd8e0
        A/table-images/manifest.json: f74a3ca614deec942b6c0115bc0952b5dc69aea4d99d07290afb4c59b61fb56a
        A/clauses/window-03/raw.json: 4690fb45c37b4b799cb7b3754e9a646e53ea83e3dc9b7b358bbaa2d49b6ccf38
        A/clauses/window-03/prompt.txt: edec749e7f77fa8ebf5b82d00ebb4e9f876806460585ebd220e5920889c57191
        A/clauses/window-03/meta.json: f7e4b2d78ae64b0ba873f67370e27732eafc64c26d08e5fb677c89c434582bd2
        A/clauses/window-04/raw.json: c52834e773f1bc81b55b07daf05d4b3414b400e0c612fc767418852391f2910b
        A/clauses/window-04/prompt.txt: 99d1b16c3b2f5e56c28d7cc05d93dd85260d62362835f1cd6f883dde9df8a0b3
        A/clauses/window-04/meta.json: d47ddac2f52b08d51d0e04e373716144387c26bb47cd065f74094005c38dcb4e
        A/clauses/window-05/raw.json: 8d769cbea1aa29a899f1e7cc1e89afd212d71e57bc99ea843be62cf6c94f1e61
        A/clauses/window-05/prompt.txt: ba2690b5877c2f9548f8efe5ae0e7fbf357b82bc9948e53ee3bfacc962e44c20
        A/clauses/window-05/meta.json: b684fbda9946776c192a7b52567770f32ad87879c8c632255cbd0fa0e2ec21ea
        A/clauses/window-02/raw.json: 7e51600fc6f5b4340c4c2b6a16f71c75bf385c022bf8d243d8d93579b375cecb
        A/clauses/window-02/prompt.txt: 272f64ab805a304d3ff14d4ba5a8b48a1add2f9c1a160d4dbfbc33ba173f7356
        A/clauses/window-02/meta.json: 6815ede29ca10bac7f431e267c0f08d95ac30c866e7cc474a40fb868df518130
        A/clauses/window-01/raw.json: 9eb9555960ec595ca13edcbe8433f94a7cd5dfe44a5e389ce0c38b41b541968f
        A/clauses/window-01/prompt.txt: 1284b56b72ff8cd6eb7ea7ab41306ddbbd30d687d9d025bfeb2b336c9d2d98cc
        A/clauses/window-01/meta.json: 530cb56d351bb18512e298ee6566de00333c254d0d80bca4f2236096f4be8970
        A/clauses/window-06/raw.json: 8de0b2a3c16e3d1a0288a35d98d9658399f701fb39b5e430632d7572f3290ad1
        A/clauses/window-06/prompt.txt: 2cad4a8e00fd665bfb231196c6621cdad8a6608e30a49250eafc3a27dc2aa1cd
        A/clauses/window-06/meta.json: 9a68e46da520e2d162b07b489baa4e89ed936352cf07d1c6260752ed62e45f85
        A/tables/TABLE-3-page-8-3/raw.json: d083050cec82230e91c5ff283d7d31c62059e120279c864ec0e757b570c20c48
        A/tables/TABLE-3-page-8-3/prompt.txt: 397a53b25ea76be54bd32210610265229da4c7bfeee3abf370cf1e851cfba2ac
        A/tables/TABLE-3-page-8-3/meta.json: d2bdabafbc048b4819afaa396505318207fa73c3effa6729329e65e512077199
        A/tables/TABLE-2-page-6-2/raw.json: 83033a295ffe92225dabbb2ea19939b61a2ac06a3f524389f83cece5f987a1f2
        A/tables/TABLE-2-page-6-2/prompt.txt: b9b4c52d02ab309a653ded4edb8ede36b50d3dcf8376d59243f7b646f323821c
        A/tables/TABLE-2-page-6-2/meta.json: 1fa20e9222eb35a43bbc82c2976da2a21294d0359d8ab1f95e1b22872cb89d85
        A/tables/TABLE-1-page-3-1/raw.json: 6875bc166f430d73e1fdd8e07474626b3a00f19b69747a404c96c15b72dc14ba
        A/tables/TABLE-1-page-3-1/prompt.txt: 597aebf9bbc5d02962a8bb758a1bdb9e78da59fc5599a491ff50cfd967044ede
        A/tables/TABLE-1-page-3-1/meta.json: 63ffe73ea10d4ded20a671b8c349154431ca059a7c1b2da9f4a510e06c7fe94c
        B/passages.json: ff4b1c8ed29b3987eae705ee5e6761b8c8f12ffb38bbc70434eebf882719fe2a
        B/raw.json: a6d126bc3f4c460ab01099509dc0ff25af3f5729fb107807c57933103fdbff5e
        B/source-units.json: 7835f71cd5814c23fc9874d12fdd9d58b9cc526532c46e2f0990839c1d1b248f
        B/full-source-units.json: 6d6dc2a753f2ab8ab2acbe0db0b4d9327332aeea4ba726ee5e87f0f46499eaea
        B/meta.json: d67474ab710925e4f2455cb76ce4d6f04ad96b1193153b243dce6ef645162e7c
        B/table-images/TABLE-1-page-3-1.png: 5c9971b3404b4ff7aa7273da0eacf93acfcdcb50427453517b375f1dff205a4a
        B/table-images/page-3.png: f6213235fc137bc6adecdcd6463071e169be07c3e38e2e9413cd2470cb45d18d
        B/table-images/page-6.png: 30255dfc820398fd611fd4d9f05956b62a12609abc668a9d6374a0bed92f810f
        B/table-images/TABLE-3-page-8-1.png: a284ae152a819ffc5a079a6b44217112ede12bfd728a103edae298f289f96c0d
        B/table-images/page-8.png: 373828001e352dc31eaeb9c6baf770e7b428dbfa42accd81462d499edb54e4df
        B/table-images/TABLE-2-page-6-1.png: 139311f4499bdb0434a1a9e444ff1628e72ed9d086a43675d591ed15e91cd8e0
        B/table-images/manifest.json: 7329462efbeb59ad2d6298d10e93c9265b9e3d31d91a672429ee7b1d9441913b
        B/clauses/window-03/raw.json: 64eb64d11a5c0825bf8cec8a5403f3f52deacada99c8287c7f260e345fd2265d
        B/clauses/window-03/prompt.txt: edec749e7f77fa8ebf5b82d00ebb4e9f876806460585ebd220e5920889c57191
        B/clauses/window-03/meta.json: 50c3ad730b3b93676e85f3b5cc113bc557643a2d2cbab69c00d07d169b44aa1b
        B/clauses/window-04/raw.json: 7565769d6243bf67eb5a076c6fcf9c5a5b4b3f6aafa61844505d88eae6685fc4
        B/clauses/window-04/prompt.txt: 99d1b16c3b2f5e56c28d7cc05d93dd85260d62362835f1cd6f883dde9df8a0b3
        B/clauses/window-04/meta.json: 52dd17a6270785e26750232c303225b65a664ee43cb127efbc4cbea947ed8e01
        B/clauses/window-05/raw.json: f5c879eb5cf94040e306ae337b5b281a2592823cb231bd4fafd0fad2ee7f17a9
        B/clauses/window-05/prompt.txt: ba2690b5877c2f9548f8efe5ae0e7fbf357b82bc9948e53ee3bfacc962e44c20
        B/clauses/window-05/meta.json: 11e68f56d908be1b618416c0459212c88578b254fbd9979b9c82b87eedb67c2c
        B/clauses/window-02/raw.json: 60d7363288ec7f10a7906227de6f0fa437730937a8a42fe4e68fa956f23f728e
        B/clauses/window-02/prompt.txt: 272f64ab805a304d3ff14d4ba5a8b48a1add2f9c1a160d4dbfbc33ba173f7356
        B/clauses/window-02/meta.json: bdd8def04a480a08d754c97d72c30610568fe28c27658e268ddddd70e6b8ec5e
        B/clauses/window-01/raw.json: 6a9e98a240a51db298ca84774c0d84af6882db93d7e42a1d0098d416029f1e4c
        B/clauses/window-01/prompt.txt: 1284b56b72ff8cd6eb7ea7ab41306ddbbd30d687d9d025bfeb2b336c9d2d98cc
        B/clauses/window-01/meta.json: 781c542d03a008855260688cab4342db37d5b96832853f34370ca48e72417faf
        B/clauses/window-06/raw.json: c14c9df4b4e6d349dc20204e61fe4ab1213d18e3226f87ab8d577fa0b89b6ae0
        B/clauses/window-06/prompt.txt: 2cad4a8e00fd665bfb231196c6621cdad8a6608e30a49250eafc3a27dc2aa1cd
        B/clauses/window-06/meta.json: 0e5aea106d959af5a01f239ae3827e6381335bbdbf54af5eca9313adc97af216
        B/tables/TABLE-3-page-8-3/raw.json: 219462a6c3aabd0eb918f8330b6765a0c4e22a63c492454a8c0a55f413f40390
        B/tables/TABLE-3-page-8-3/prompt.txt: 397a53b25ea76be54bd32210610265229da4c7bfeee3abf370cf1e851cfba2ac
        B/tables/TABLE-3-page-8-3/meta.json: 6a0c9c2dd3df2089eed6389c836d7cbb222a77f2d28ce339b1146eadde72a3eb
        B/tables/TABLE-2-page-6-2/raw.json: 96a103cd41e7d924b884f19929106f3e14062ca2f92e6a9b72c6e5e8ed27d4bc
        B/tables/TABLE-2-page-6-2/prompt.txt: b9b4c52d02ab309a653ded4edb8ede36b50d3dcf8376d59243f7b646f323821c
        B/tables/TABLE-2-page-6-2/meta.json: b79c050f4b4c9c777192ecbb56024f33c9dc2cc333d626940c9e5825a906daa4
        B/tables/TABLE-1-page-3-1/raw.json: 0911d7edd03a457614408a9668c6a472c5ca03be31e2fc8145d34903795ac586
        B/tables/TABLE-1-page-3-1/prompt.txt: 597aebf9bbc5d02962a8bb758a1bdb9e78da59fc5599a491ff50cfd967044ede
        B/tables/TABLE-1-page-3-1/meta.json: faec968f3ebec9f6481960bca52696a6960ef70e77982a09772532fedd9f3b4e
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
      pdf_sha256: eced2b5115c01465a6bcf6c63cd51aa6557fe1951db56dbb4a245ddd49aef701
      source_review: _compare/relationships-2026-11-16/review-current/BlomSmink2020
      source_status_sha256: b7df07adba3a8cfe0cae0aa9bcda7dedd479dd60d5b253dbf60ee61134fc5e91
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R001
    exposure:
      text: fractional anisotropy (FA) change in the right inferior longitudinal fasciculus
        (ILF)
    outcome:
      text: change in Boston Naming Test (BNT) score
    analysis_label: Correlational analysis of FA change and naming recovery
    relation: association
    evidence_ids:
    - P1-S2-C15
    - P6-S1-C11
    qualifier_ids:
    - P1-S2-C16
    - P6-S1-C11
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: eced2b5115c01465a6bcf6c63cd51aa6557fe1951db56dbb4a245ddd49aef701
      source_review: _compare/relationships-2026-11-16/review-current/BlomSmink2020
      source_status_sha256: b7df07adba3a8cfe0cae0aa9bcda7dedd479dd60d5b253dbf60ee61134fc5e91
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P5-S1-C6
      - Result passage disposed without unit P5-S1-C7
      - Result passage disposed without unit P6-S1-C1
      - Result passage disposed without unit P6-S1-C2
      - Result passage disposed without unit P6-S1-C3
      - Result passage disposed without unit P6-S1-C4
      - Result passage disposed without unit P6-S1-C10
      - Accounting without a linked unit P6-S1-C11
      - Result passage disposed without unit P6-S2-C1
      - Accounting without a linked unit P6-S2-C5
      - Unaccounted source passage P6-S1-C11
      - Unaccounted source passage P6-S2-C5
      - Result passage disposed without unit P9-S1-C1
      - Result passage disposed without unit P9-S1-C2
      - Unresolved source passage P9-S1-C3
      - Result passage disposed without unit P9-S1-C4
      - Accounting without a linked unit P9-S3-C3
      - Accounting without a linked unit P9-S3-C4
      - Unaccounted source passage P9-S3-C4
      - Unaccounted source passage P9-S3-C3
      unattached_null_or_qualifier_ids:
      - P5-S1-C6
      - P6-S1-C10
      - P6-S3-C3
      suppressed_nonrepresented_units: 15
      default_disposition_count_requires_completeness_check: 123
      unselected_timing_passages:
      - P1-S2-C9
      - P2-S2-C3
      - P2-S2-C4
      - P2-S2-C7
      - P2-S2-C10
      - P8-S1-C3
      - P9-S2-C12
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P6-S1-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P2-S3-C3
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: limitations
        source_ids:
        - P9-S2-C6
        - P9-S2-C7
        - P9-S2-C8
        - P9-S2-C9
        - P9-S2-C10
        - P9-S2-C11
        - P9-S2-C12
        - P9-S2-C13
        - P9-S3-C5
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - validation
      - limitations
      - personal_factors
      - tested_personal_effects
      - adjustment_roles
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-3-1
      - TABLE-2-page-6-2
      - TABLE-3-page-8-3
      unlinked_tables:
      - TABLE-3-page-8-3
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P2-S3
        - P3-S2
        - P4-S1
        - P5-S1
        - P5-S2
        - P6-S1
        - P6-S2
        - P7-S1
        - P8-S1
        - P9-S3
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: eced2b5115c01465a6bcf6c63cd51aa6557fe1951db56dbb4a245ddd49aef701
      source_review: _compare/relationships-2026-11-16/review-current/BlomSmink2020
      source_status_sha256: b7df07adba3a8cfe0cae0aa9bcda7dedd479dd60d5b253dbf60ee61134fc5e91
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S2-C15
      disposition: represented
      result_indexes:
      - 0
      reason: Reports strong positive correlation between right ILF FA change and
        BNT change.
    - source_id: P1-S2-C16
      disposition: represented
      result_indexes:
      - 0
      reason: Qualifies the right ILF FA change association with specific BNT improvement
        ranges.
    - source_id: P1-S2-C17
      disposition: represented
      result_indexes:
      - 1
      reason: Reports null correlations for other tracts.
    - source_id: P1-S2-C19
      disposition: repeated
      result_indexes:
      - 0
      reason: Abstract conclusion restating the right ILF association.
    - source_id: P2-S3-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Justifies collapsing tDCS/sham data based on prior RCT results and supplementary
        data.
    - source_id: P5-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes tractography success rates and exclusions.
    - source_id: P5-S1-C7
      disposition: represented
      result_indexes:
      - 3
      reason: Reports no significant group-level FA changes.
    - source_id: P5-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes individual FA changes for left SLF.
    - source_id: P5-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes individual FA changes for right SLF.
    - source_id: P5-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes individual FA changes for left IFOF.
    - source_id: P5-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes individual FA changes for right IFOF.
    - source_id: P5-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes individual FA changes for left ILF.
    - source_id: P5-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes individual FA changes for right ILF.
    - source_id: P6-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes individual FA changes for left MdLF.
    - source_id: P6-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes individual FA changes for right MdLF.
    - source_id: P6-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes individual FA changes for left UF.
    - source_id: P6-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes individual FA changes for right UF.
    - source_id: P6-S1-C5
      disposition: represented
      result_indexes:
      - 4
      reason: Reports significant group-level BNT score improvement.
    - source_id: P6-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes individual BNT change distributions.
    - source_id: P6-S1-C8
      disposition: represented
      result_indexes:
      - 1
      reason: Reports null correlations for left hemisphere tracts.
    - source_id: P6-S1-C9
      disposition: represented
      result_indexes:
      - 2
      reason: Reports moderate negative correlation for right SLF.
    - source_id: P6-S1-C10
      disposition: represented
      result_indexes:
      - 2
      reason: Qualifies right SLF correlation as not surviving multiple testing correction.
    - source_id: P6-S1-C11
      disposition: represented
      result_indexes:
      - 0
      reason: Reports strong positive correlation for right ILF and associated BNT
        improvement ranges.
    - source_id: P6-S2-C1
      disposition: repeated
      result_indexes:
      - 0
      reason: Reference to Figure 5 for right ILF correlation.
    - source_id: P6-S2-C5
      disposition: repeated
      result_indexes:
      - 0
      - 1
      reason: Discussion summary of right ILF association and left hemisphere nulls.
    - source_id: P6-S3-C3
      disposition: repeated
      result_indexes:
      - 2
      reason: Discussion restatement of right SLF finding.
    - source_id: P6-S3-C6
      disposition: represented
      result_indexes:
      - 3
      reason: Table 2 providing data for group-level FA changes.
    - source_id: P9-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discusses lesion volume in relation to right ILF changes.
    - source_id: P9-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discusses specific participant (P2) lesion volume and FA decrease.
    - source_id: P9-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discusses uncertainty regarding lesion site.
    - source_id: P9-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discusses bidirectional changes in right ILF.
    - source_id: P9-S1-C5
      disposition: repeated
      result_indexes:
      - 0
      reason: Discussion restatement of right ILF FA change and BNT relationship.
    - source_id: P9-S2-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Theorizes neural mechanisms (degeneration vs plasticity) for right ILF
        changes.
    - source_id: P9-S2-C3
      disposition: repeated
      result_indexes:
      - 1
      reason: Discussion restatement that other ventral tracts (UF) played no role.
    - source_id: P9-S3-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Restates lack of tDCS effect on naming recovery or tract integrity.
    - source_id: P9-S3-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discusses lack of tDCS confounding in scatterplots.
    - source_id: P9-S3-C6
      disposition: repeated
      result_indexes:
      - 0
      reason: Conclusion restating right ILF association.
    unresolved_coverage:
    - source_id: P6-S3-C6
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P9-S2-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P9-S2-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S2-C16
    - P1-S2-C19
    - P2-S3-C3
    - P5-S1-C6
    - P5-S1-C9
    - P5-S1-C10
    - P5-S2-C2
    - P5-S2-C3
    - P5-S2-C4
    - P5-S2-C5
    - P6-S1-C1
    - P6-S1-C2
    - P6-S1-C3
    - P6-S1-C4
    - P6-S1-C7
    - P6-S1-C10
    - P6-S2-C1
    - P6-S2-C5
    - P6-S3-C3
    - P9-S1-C1
    - P9-S1-C2
    - P9-S1-C3
    - P9-S1-C4
    - P9-S1-C5
    - P9-S2-C3
    - P9-S2-C11
    - P9-S3-C3
    - P9-S3-C4
    - P9-S3-C6
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-3-1
    - TABLE-2-page-6-2
    - TABLE-3-page-8-3
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P2-S2-C4
      recruited_sample:
      - P2-S2-C10
      eligibility:
      - P2-S2-C7
      - P2-S2-C8
      imaging_provenance:
      - P3-S1-C5
      imaging_timing:
      - P3-S1-C4
      outcome_timing:
      - P3-S1-C3
      outcome_definition:
      - P3-S1-C2
      validation: []
      analysis_restrictions:
      - P5-S1-C5
      dependent_variable_statement:
      - P5-S1-C3
      - P5-S1-C4
      limitations: []
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles: []
      explicitly_not_adjusted:
      - P9-S3-C3
      - P9-S3-C4
      descriptive_personal_factors:
      - P2-S2-C4
      - P3-S2-C12
    outcome_type: change_from_baseline
    imaging_vs_outcome: mixed
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P6-S1-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P2-S3-C3
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: limitations
      source_ids:
      - P9-S2-C6
      - P9-S2-C7
      - P9-S2-C8
      - P9-S2-C9
      - P9-S2-C10
      - P9-S2-C11
      - P9-S2-C12
      - P9-S2-C13
      - P9-S3-C5
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
      pdf_sha256: eced2b5115c01465a6bcf6c63cd51aa6557fe1951db56dbb4a245ddd49aef701
      review_sha256: 6cdbabaec32a9cf5079ac05478fbc10dd882e06a972719cae8cfd411d98c657b
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
      - P1-S2-C15
      - P6-S1-C11
      source_result: A strong positive correlation (r = 0.91, P < .001) was found
        between the change in fractional anisotropy (FA) in the right inferior longitudinal
        fasciculus (ILF) and the change in Boston Naming Test (BNT) scores in subacute
        poststroke aphasia patients. An increase in FA was associated with considerable
        improvement in naming accuracy, while a decrease was associated with limited
        improvement or slight deterioration.
      result_status: detected
      patient_measurement: patient_diffusion
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis correctly identifies the correlational analysis
            between right ILF FA change and BNT change as the primary significant
            finding, distinct from the non-significant correlations for other tracts
            or the uncorrected SLF correlation.
          source_ids:
          - P1-S2-C13
          - P1-S2-C15
          - P6-S1-C11
        direction:
          answer: fits
          reason: The draft correctly describes the direction as a positive correlation
            where increased FA change is associated with improved BNT scores, matching
            the source text 'strong positive correlation' and 'increase in FA was
            associated with considerable improvement'.
          source_ids:
          - P1-S2-C15
          - P6-S1-C11
        construct:
          answer: fits
          reason: The exposure is correctly identified as FA change in the right ILF
            measured via deterministic tractography (patient_diffusion), and the outcome
            is BNT change. The draft does not confuse this with template overlap or
            other tracts.
          source_ids:
          - P1-S2-C10
          - P1-S2-C11
          - P3-S2-C2
          - P4-S1-C8
        qualifications:
          answer: fits
          reason: The draft includes relevant limitations such as small sample size,
            predominantly male sample, and the indirect nature of DTI measures. It
            correctly notes the subacute timing. The qualifier regarding the concurrent
            nature of the change is appropriate.
          source_ids:
          - P9-S2-C6
          - P9-S2-C8
          - P9-S3-C5
          - P1-S2-C9
        missing_material_caveat:
          answer: fits
          reason: No material caveats are missing that would change the interpretation
            of the core relationship. The draft acknowledges the observational nature
            and limitations. The unresolved image reading disagreements in P2-S2-C8,
            P3-S1-C4, and P8-S1-C3 do not affect the core statistical result of the
            right ILF correlation, which is clearly stated in the text and abstract.
          source_ids:
          - P9-S2-C5
          - P9-S3-C5
      optional_pending:
      - Specific coordinates or atlas metadata for the ILF ROI definition
      - Detailed statistics for the non-significant tracts
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Specific coordinates or atlas metadata for the ILF ROI definition
    - Detailed statistics for the non-significant tracts
    normalizations:
    - field: bucket
      original: predictors
      action: route_from_kind
      value: regions
    analysis_identity:
      id: R001
      exposure:
        text: fractional anisotropy (FA) change in the right inferior longitudinal
          fasciculus (ILF)
      outcome:
        text: change in Boston Naming Test (BNT) score
      analysis_label: Correlational analysis of FA change and naming recovery
      relation: association
      evidence_ids:
      - P1-S2-C15
      - P6-S1-C11
      qualifier_ids:
      - P1-S2-C16
      - P6-S1-C11
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: eced2b5115c01465a6bcf6c63cd51aa6557fe1951db56dbb4a245ddd49aef701
        source_review: _compare/relationships-2026-11-16/review-current/BlomSmink2020
        source_status_sha256: b7df07adba3a8cfe0cae0aa9bcda7dedd479dd60d5b253dbf60ee61134fc5e91
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P1-S2-C9:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: eced2b5115c01465a6bcf6c63cd51aa6557fe1951db56dbb4a245ddd49aef701
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: c119828c098388b0bffa5e9752a4d17a18a0847968119e83c4e8b3854187a49c
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P1-S2-C9
          page: 1
          text_layer_sha256: c119828c098388b0bffa5e9752a4d17a18a0847968119e83c4e8b3854187a49c
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "Ten participants with aphasia after left-hemisphere stroke\
          \ underwent language testing and diffusion \ntensor imaging twice within\
          \ 3 months post onset, with a 1-month interval between sessions."
        anchor_text: "Ten participants with aphasia after left-hemisphere stroke underwent\
          \ language testing and diffusion \ntensor imaging twice within 3 months\
          \ post onset, with a 1-month interval between sessions."
        excluded_fragments: []
        image_sha256: 783b1cb46023cfed8b8f88d29aff1cffbcbf44c30bfc95f986e6c48e84be7bf5
        transcription: . Ten participants with aphasia after left-hemisphere stroke
          underwent language testing and diffusion tensor imaging twice within 3 months
          post onset, with a 1-month interval between sessions
      P2-S2-C4:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: eced2b5115c01465a6bcf6c63cd51aa6557fe1951db56dbb4a245ddd49aef701
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: d9113aaa21d0d5d586cfdef003981f03c849b60880b84424e3d0ddbd8570fe02
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S2-C4
          page: 2
          text_layer_sha256: d9113aaa21d0d5d586cfdef003981f03c849b60880b84424e3d0ddbd8570fe02
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "Methods\nParticipants\nTen participants (7 men; mean age:\
          \ 61.8 ± 7.8 years) with \naphasia due to first-ever left-hemisphere stroke\
          \ completed \nthe study."
        anchor_text: "Methods\nParticipants\nTen participants (7 men; mean age: 61.8\
          \ ± 7.8 years) with \naphasia due to first-ever left-hemisphere stroke completed\
          \ \nthe study."
        excluded_fragments: []
        image_sha256: b8d7cc520fd32609e48ba92f487e37ac38bf152fcc26ccfe38532d6cb0916052
        transcription: 'Methods


          Participants


          Ten participants (7 men; mean age: 61.8 ± 7.8 years) with aphasia due to
          first-ever left-hemisphere stroke completed the study'
      P3-S1-C3:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: eced2b5115c01465a6bcf6c63cd51aa6557fe1951db56dbb4a245ddd49aef701
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 803bcb267cffbe7e63a1c9d7f90369f80cba076a0089e819c103635cefb5c2d9
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S1-C3
          page: 3
          text_layer_sha256: 803bcb267cffbe7e63a1c9d7f90369f80cba076a0089e819c103635cefb5c2d9
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "The first assessment was performed at a mean of \n39.4 ± 14.1\
          \ days post onset (range: 17-62 days post onset) \nand the second assessment\
          \ at a mean of 72.8 ± 14.8 days \npost onset (range: 50-96 days post onset)."
        anchor_text: "The first assessment was performed at a mean of \n39.4 ± 14.1\
          \ days post onset (range: 17-62 days post onset) \nand the second assessment\
          \ at a mean of 72.8 ± 14.8 days \npost onset (range: 50-96 days post onset)."
        excluded_fragments: []
        image_sha256: 7e0519d8ec755357c23b5d3c421523703cdf64e150c41198ef6a59ed1d2f3f68
        transcription: '. The first assessment was performed at a mean of

          39.4 ± 14.1 days post onset (range: 17-62 days post onset)

          and the second assessment at a mean of 72.8 ± 14.8 days

          post onset (range: 50-96 days post onset)'
      P9-S2-C8:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: eced2b5115c01465a6bcf6c63cd51aa6557fe1951db56dbb4a245ddd49aef701
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 48164f7a84d1b4d22f61e810c54928a22956309ef2048b61e13525f5a7b8baef
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P9-S2-C8
          page: 9
          text_layer_sha256: 48164f7a84d1b4d22f61e810c54928a22956309ef2048b61e13525f5a7b8baef
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "Another \nlimitation is that the participants were predominantly\
          \ male \n(7 men, 3 women)."
        anchor_text: "Another \nlimitation is that the participants were predominantly\
          \ male \n(7 men, 3 women)."
        excluded_fragments: []
        image_sha256: 0886c13823defdd4b1269af426ea619311b3f9326b2d2b6c2e9b8a56b436f6b0
        transcription: . Another limitation is that the participants were predominantly
          male (7 men, 3 women)
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 1
  quote: "A strong positive correlation was found between FA change in the right ILF\
    \ within \nthe ventral stream and change on the BNT (r = 0.91, P < .001)."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-20'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
