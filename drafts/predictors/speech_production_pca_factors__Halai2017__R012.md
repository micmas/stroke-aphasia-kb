---
id: speech_production_pca_factors
name: speech production PCA factors
kind: predictor
findings:
- id: f1
  target_audit:
    status: needs_source_review
    category: non_behaviour_or_methodological
    original_target: lesion_distribution
    reason: This endpoint is not a behaviour. Review its scope and target kind; do not relabel it as a behavioural
      deficit.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  outcome_measurement:
    status: needs_source_review
    instruments: []
    note: Outcome instrument/task is not yet verified for this finding. Do not infer it from the predictor
      or a paper-wide test list.
  target: lesion_distribution
  target_kind: region
  claim: After accounting for lesion volume, there were no significant voxel-based
    correlational clusters for either the speech quanta (F1) or semantic variety (F2)
    factors.
  direction: no_effect
  relationship: correlational
  method: VBCM
  sample:
    n: 31
    population: chronic stroke patients with impairment in producing and/or understanding
      spoken language
    phase: not_reported
    time_post_onset: at least 12 months post-stroke at the time of scanning and assessment
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - automated lesion identification detects areas of unexpected tissue class, including
    missing grey/white matter and augmented CSF space
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Patient scores on two principal components (F1: speech
    quanta, F2: semantic variety) derived from a rotated PCA of speech production
    measures (number of words, types, TTR, morphemes, MLU, and WPM) extracted from
    ''Cookie theft'' picture descriptions. analysis adjusted for lesion volume. Additional
    metadata has not been transcribed; review the pending-field flags before approval.
    PDF image reading (P4-S2-C3, two-model agreement, human verification pending):
    Participants


    Thirty one chronic stroke patients (either ischaemic or hae-

    morrhagic) were recruited (the same patients as reported by

    Butler et al., 2014), who had impairment in producing and/or

    understanding spoken language and their aphasia was clas-

    sified using the Boston Diagnostic Aphasia Examination

    (BDAE) Original text-layer quotation is preserved below. PDF image reading (P4-S2-C5,
    two-model agreement, human verification pending): . All patients

    were at least 12 months post-stroke at the time of scanning and

    assessment, were native English speakers with normal or

    corrected-to-normal hearing and vision (see Table 1 for a

    summary of demographic details) Original text-layer quotation is preserved below.
    Reconcile this new analysis with earlier drafts and source-review decisions for
    the paper; new candidate IDs do not carry earlier decisions forward.'
  imaging_details:
    reference_space: not_reported
    atlases_used: []
  lesion_mapping: {}
  provenance:
    extracted_by: model:gemma4:31b
    extracted_on: '2026-11-24'
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
    - proposed_concept:lesion_distribution
  citation: '@Halai2017'
  source_passages:
  - section: Original source P8-S3-C4
    page: 8
    quote: 'After adding a co-

      variate for lesion volume, no signiﬁcant clusters remained for

      F1 or F2.

      3.5.'
    supports: claim
  - section: Original source P4-S2-C3
    page: 4
    quote: 'Participants

      Thirty one chronic stroke patients (either ischaemic or hae-

      morrhagic) were recruited (the same patients as reported by

      Butler et al., 2014), who had impairment in producing and/or

      understanding spoken language and their aphasia was clas-

      siﬁed using the Boston Diagnostic Aphasia Examination

      (BDAE).'
    supports: sample
  - section: Original source P4-S2-C5
    page: 4
    quote: 'All patients

      were at least 12 months post-stroke at the time of scanning

      and assessment, were native English speakers with normal or

      corrected-to-normal hearing and vision (see Table 1 for a

      summary of demographic details).'
    supports: sample
  - section: Original source P6-S2-C1
    page: 6
    quote: 'We used the T1-weighted images with continuous signal

      intensity values across the whole brain and correlated these

      with individual measures or PCA factor scores using a voxel-

      based correlational methodology (VBCM: Tyler, Marslen-

      Wilson, & Stamatakis, 2005), a variant of voxel-lesion symp-

      tom mapping (VSLM: Bates et al., 2003).'
    supports: method
  - section: Original source P6-S1-C11
    page: 6
    quote: 'We

      should

      note

      here,

      explicitly,

      that

      although

      commonly referred to as an automated ‘lesion’ segmentation

      method, the technique detects areas of unexpected tissue

      class e and, thus, identiﬁes missing grey and white matter

      but also areas of augmented cerebral spinal ﬂuid (CSF) space.'
    supports: limitation
  - section: Original source P8-S2-C9
    page: 8
    quote: 'The measures that tapped

      into overall quantity of speech (e.g., number of words and

      WPM) loaded heavily on factor 1; hence we refer to this factor

      as ‘speech quanta’.'
    supports: claim
  - section: Original source P8-S2-C10
    page: 8
    quote: 'Factor 2 was interpreted as ‘semantic va-

      riety’, as the TTR measurement loaded heavily on it (e.g.,

      proportion of unique words spoken).'
    supports: claim
predictor_type: imaging_metric
short_definition: 'Patient scores on two principal components (F1: speech quanta,
  F2: semantic variety) derived from a rotated PCA of speech production measures (number
  of words, types, TTR, morphemes, MLU, and WPM) extracted from ''Cookie theft'' picture
  descriptions.'
assessment:
- Boston Diagnostic Aphasia Examination (Cookie theft picture description)
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-24'
relationship_review:
  paper: Halai2017
  proposal_id: R012
  review_status_sha256: 2d709ade5f5e26d25ded5f0d9175b09862fc572ccc664532983b4fadac69c43b
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 8734accf0936fda0c0b3612e1ecaed66ef0b23f19bce849e602298fd90306020
    original_review_binding:
      version: relationship-review-v5
      input_hashes:
        pdf: 8734accf0936fda0c0b3612e1ecaed66ef0b23f19bce849e602298fd90306020
        A/passages.json: 7ef41597dd0d4303863aa0ae8701d02d8ad3e140ebc2fd0033e5892336355c4b
        A/raw.json: 8d5848b5e61c4458346098ade72d7574dfecde66d4558ec28498ce054997249c
        A/source-units.json: 6b19cb82736498292cab9a96bc55b37eccc3011b98b6695d37cb7995c6c70102
        A/full-source-units.json: 6b19cb82736498292cab9a96bc55b37eccc3011b98b6695d37cb7995c6c70102
        A/meta.json: 1b3b5e6a88a370f80a261ff9e3a3d68c69f2e7d060804d8b3cbfd8e0f4153d84
        A/table-images/manifest.json: 56e4ebdef47c740d7d1059d76c4e9e15cdc4b4202dde744da6e2cfb59774a816
        A/clauses/window-11/raw.json: b9cca10f39eaaf31fada5d9546c5c8693d3de87ec95a3c8923df81724f4d1d6e
        A/clauses/window-11/prompt.txt: 8cc48b1bb7fced5c2bec846230c562db680ec8ac26b453f78a77466e29460a4e
        A/clauses/window-11/meta.json: e665b0fe842bf7c9a846e8a7e3135a01f891bb4df11082abeee623ead3f803b2
        A/clauses/window-16/raw.json: b79b3657b242b0825dbefa62e4d4721159fee789567c56774d6c58d8f6dd142e
        A/clauses/window-16/prompt.txt: abde187450fcc5b2cd88309099610ca208c91db1ee78c9826fbee2bcc6e2df8e
        A/clauses/window-16/meta.json: f50ae8afc220494f9b6a76aa90c9f353eb55bdc6b4094fefbd2279dc6769315a
        A/clauses/window-18/raw.json: 9b81787c3001eb0b26e6cc4715d7161b8e7e7323b824dc6d53ce8a4407d267bc
        A/clauses/window-18/prompt.txt: d615fa6bf2eb952e61143c661e0de5995fbb7b7389803b668c89fc189cfaaa16
        A/clauses/window-18/meta.json: d0482392cdd87bac00244592acc587371e3a753d4a3bb008168a25096921ca7e
        A/clauses/window-17/raw.json: 5e8e158f6f3836151f1322714ce8e8d67e4260eb14454e7589702ebf20adfd21
        A/clauses/window-17/prompt.txt: 4b74aab44e3c158cf0b6ab42838f168ab3ddb821b74bf91a81f3c440f9259518
        A/clauses/window-17/meta.json: df7487cdef25815295249eeed7708db25a523f25e428461eea6d907385a6362c
        A/clauses/window-10/raw.json: 32da41b63071bf7c79e805c38b222d1ef6c6a300f6d2d40f7beda4e72989bb24
        A/clauses/window-10/prompt.txt: 02dc88b4b9e02d5bb49e9fdc9d00ba3cf4d80c037f4d9c83045e57d2dd48bc88
        A/clauses/window-10/meta.json: 63304fabe752f4e9ec8d3fd791a63b541dcdbb68833668b4f9ec64f0f99719de
        A/clauses/window-03/raw.json: e68225c910345b1e198b3f9f29172417c962b02e084bf9eb9f11e458195ba41d
        A/clauses/window-03/prompt.txt: 178940dca7c549a14aecbb499f062674fea529984f234a189d6c193822179007
        A/clauses/window-03/meta.json: 7d1adef02a61f4d490c157cde9281a345050bdaa548aa4342c5ab478b4c83528
        A/clauses/window-04/raw.json: 8fecce958caa4786a0416705095d7ad4e15946d9c0bbecb5546dfd4c0df496cd
        A/clauses/window-04/prompt.txt: 6c6b64dc14f6fec7dde5406c226970da391513fa8a99e9a726fbf3cde9d9cf2a
        A/clauses/window-04/meta.json: df090a767235022784848fe3a6fb065358c6d75c82276dfd26251800992c7414
        A/clauses/window-05/raw.json: 9eeb673c52488491c3d8ce88d0d0647af74fc3602500c94f652aa873e7137615
        A/clauses/window-05/prompt.txt: 415d6be7e7c0f978603a0afa81b086bb689fc8d653c81fecbe3293bb9598967a
        A/clauses/window-05/meta.json: 12c9439e2d2a840d6d980074272935265713d9e3d0e49c043b57dfcade1582a1
        A/clauses/window-02/raw.json: 671f418db67883d11d7ccd1e5f5de0f9368ecf3b6c644bec3e16259a1a7780a9
        A/clauses/window-02/prompt.txt: 007283a0268e2a99d3d1b4272320adee622eb5bba10216113bb3b32470cb4ecf
        A/clauses/window-02/meta.json: 3dd35d8a7c09979cfb9b63e384b1d2a2156bf746e83536ff18d7aa6da53f5e59
        A/clauses/window-15/raw.json: 993d995522dbfb107b9f4c622a9ac01dcbdc39eb960aaf0ec0ac1083e8548add
        A/clauses/window-15/prompt.txt: eb5078909ab0e9ccc9f354190c8d4f6623cbc5a0cd5a5a65f1d5cc4ff3ab59bb
        A/clauses/window-15/meta.json: cfe4d8a8c4deaaf5d17ff4b47fc7be165f4b86275228d87efacc4c3dd9cac7ae
        A/clauses/window-12/raw.json: 7e884b0f76c57353acb8ebf4fe3c37691440e1a68d92d03957c4715cfff07f54
        A/clauses/window-12/prompt.txt: db6d6dc0f9c4e66bfc3d15341e873a87d333915d5ce1c611c2169ebbed54d00f
        A/clauses/window-12/meta.json: 03891698d73da776b0f9676e281f202cfef446866a6916bad90250f6ea3ae5c5
        A/clauses/window-13/raw.json: e026984d4eb6f9ff98ed1503f4ab3bca4e8ad126c14d9ce4734eb45a4fc62b4c
        A/clauses/window-13/prompt.txt: a3b2ee2efb0aed0cacb9bf453350b48ada9c112176fdbfa64704e59721fa8c45
        A/clauses/window-13/meta.json: 5ba7d9a6667b73c95b390c69cc0cf201a3773fea5f4590ee6b608fada1813387
        A/clauses/window-14/raw.json: 0bd452bc218bb4062b5aa76c807905f28a5a5875f8336c335bce1f2727dea7dd
        A/clauses/window-14/prompt.txt: 9fda25b34678ca50ce009d4a55b827f99d7dca27de215a01a2bf75d1450ed067
        A/clauses/window-14/meta.json: 906ca9b3cd45823049c0607aed3a082125eeda796ba4d8fb52d5bc4ad95af47f
        A/clauses/window-09/raw.json: 33a0153a412926b0f578b4913466bfe6201b2a9b1ff826af217a82abe02a1bf7
        A/clauses/window-09/prompt.txt: 63fc2bcc9cee97886bdd0f1ab41293c55c307291f7c4c75c1dbd0fe81d4bceaa
        A/clauses/window-09/meta.json: 2eca1081b70191a9876636b3aae98e56493d8f1838785891891d489cbf55c981
        A/clauses/window-07/raw.json: 3deeb7a4acadb25d6479ec0ab1ec5a3a93236e94f65709f12209ac53a7526592
        A/clauses/window-07/prompt.txt: dbbdbe8e6fa7d86e0a9f99a52d195044393a979f9fef63a7c0520a0325e7a5aa
        A/clauses/window-07/meta.json: e26b09df1cff8917e6d1a7c8dec2c85235962a38492cf9dcba2aec031c9fa9c6
        A/clauses/window-01/raw.json: 5cae9438b354309bd41dcf66589a6fdff3060cb8b7bf1762f71961020fb3b45b
        A/clauses/window-01/prompt.txt: 296f7a0265bbd95e8873cfb1b58bb43ddcdf89291dac70da02d3d1f8616b4e0a
        A/clauses/window-01/meta.json: 19dfc0a2bbbeea77dde1f0f8a4cef1230c859ca37fcf954228a558a8e20e85e9
        A/clauses/window-06/raw.json: a98fc90d58b8809e531dc30aa110ab4628b6b684d2ade45b6cda96971430a4f5
        A/clauses/window-06/prompt.txt: 1f01a51e19120506835225db50b69450535413ecbde4de0631aafe892a3af00a
        A/clauses/window-06/meta.json: ed5427eb83f91bd0ab164912a554537b607030bbc0a27331751fcfa351926709
        A/clauses/window-08/raw.json: 51e127ca229217e44f734618f1715807def81954b045b982e6435ab65012ed6f
        A/clauses/window-08/prompt.txt: e20245b8fd3aa952612865298db22bc74ab50214a83990e6c7c69468599eb2a0
        A/clauses/window-08/meta.json: 175d6503bedc61f5012f0d7f4ccaa5990ae39773c80ed17df6642036811a32ca
        B/passages.json: 7ef41597dd0d4303863aa0ae8701d02d8ad3e140ebc2fd0033e5892336355c4b
        B/raw.json: d989a01a3fa00d22d925046d3836419b6fd2964b6381ff0f27a92475937bed2b
        B/source-units.json: 6b19cb82736498292cab9a96bc55b37eccc3011b98b6695d37cb7995c6c70102
        B/full-source-units.json: 6b19cb82736498292cab9a96bc55b37eccc3011b98b6695d37cb7995c6c70102
        B/meta.json: f6f18da286dbe45dee0072337a74cebcddf1410d13497a5554de72f4d2c8648d
        B/table-images/manifest.json: 56e4ebdef47c740d7d1059d76c4e9e15cdc4b4202dde744da6e2cfb59774a816
        B/clauses/window-11/raw.json: 6efd173da2fe27a0d0662c8466e3631d41293eb7431c5ab629eab36411126be0
        B/clauses/window-11/prompt.txt: 8cc48b1bb7fced5c2bec846230c562db680ec8ac26b453f78a77466e29460a4e
        B/clauses/window-11/meta.json: 35beda64db26a4e0a479173c8c2fbb1e87b09e05f2c8d22b6fa5f233e6da414c
        B/clauses/window-16/raw.json: 109d7c121db2bd91d99d2023e69d46de706cc7cf48685475ebbad2f6e8571cb4
        B/clauses/window-16/prompt.txt: abde187450fcc5b2cd88309099610ca208c91db1ee78c9826fbee2bcc6e2df8e
        B/clauses/window-16/meta.json: 1bf33361911f951071a619e90937acc3c05e4bcc6470e43adb101014b3eeb329
        B/clauses/window-18/raw.json: 4827f3b020e6b939cf3ed153eadc25b802ade152a94e17b57fce9ea34df6355b
        B/clauses/window-18/prompt.txt: d615fa6bf2eb952e61143c661e0de5995fbb7b7389803b668c89fc189cfaaa16
        B/clauses/window-18/meta.json: 399681647463a5f7907437c3c1e759670b15a7fb3188c0149fe576a25e563f1e
        B/clauses/window-17/raw.json: 5343c9f50e2b8fa6376502e09bce7101faf0cc87e4c34f0cfd33dd0f048761e7
        B/clauses/window-17/prompt.txt: 4b74aab44e3c158cf0b6ab42838f168ab3ddb821b74bf91a81f3c440f9259518
        B/clauses/window-17/meta.json: 4c6b5e3edbe7bee7c3851a16d6bbce146345e2c9cf59f37d3708ddfb137ba920
        B/clauses/window-10/raw.json: e6e105f50728c97cadd013977014add447fb29a300287f8a1edb828b998a86e9
        B/clauses/window-10/prompt.txt: 02dc88b4b9e02d5bb49e9fdc9d00ba3cf4d80c037f4d9c83045e57d2dd48bc88
        B/clauses/window-10/meta.json: e6e44ed3b380a5dae262f6856e691a3cb70de4e47a6a48358ebee3ae4274d9dd
        B/clauses/window-03/raw.json: 18a97dfd872d720683e93cd034649f42366c2ba3179fcec8981ae932b8dc6371
        B/clauses/window-03/prompt.txt: 178940dca7c549a14aecbb499f062674fea529984f234a189d6c193822179007
        B/clauses/window-03/meta.json: 54100d96d170017e6b236159613b913c4202e1779a0328d3ad02103b583d4c0a
        B/clauses/window-04/raw.json: ca8e49f0374e9017da273cf64d0e2bc435ad3e9bf88027641349a484b3eaa669
        B/clauses/window-04/prompt.txt: 6c6b64dc14f6fec7dde5406c226970da391513fa8a99e9a726fbf3cde9d9cf2a
        B/clauses/window-04/meta.json: f6190e1b5d2bd04a038ad57139c2aaafa5103520b9928ffee2c3e25ec27fd456
        B/clauses/window-05/raw.json: 456ee1c63083d50f4eed5132e2df38ea29adecb6a8bcb3c5f33b4dacac8158e5
        B/clauses/window-05/prompt.txt: 415d6be7e7c0f978603a0afa81b086bb689fc8d653c81fecbe3293bb9598967a
        B/clauses/window-05/meta.json: 930445d779526752517e583f2989d361563ffa66674dfb60e1a1a43684eb08fe
        B/clauses/window-02/raw.json: f880f1d9694d5cb3d95e322529b9ace95028943fc6d51b2ae280b47175d0ee04
        B/clauses/window-02/prompt.txt: 007283a0268e2a99d3d1b4272320adee622eb5bba10216113bb3b32470cb4ecf
        B/clauses/window-02/meta.json: 3fd27ec2a3516c78dbccfa0ae0d78b4c6a4ce36bcb7112238c2f2225ac580c55
        B/clauses/window-15/raw.json: c19cd514b752fefdda125dc7abfbd2fc66228812a035b0f16db62ccf720f435e
        B/clauses/window-15/prompt.txt: eb5078909ab0e9ccc9f354190c8d4f6623cbc5a0cd5a5a65f1d5cc4ff3ab59bb
        B/clauses/window-15/meta.json: 79bd5fa452f68b7cc6a918633f53379208a5108addc723385eae3a181fa33cb6
        B/clauses/window-12/raw.json: 32ee714fbaa3e8563649cde498d68b9a38335336bd040a39149cae3028e987dd
        B/clauses/window-12/prompt.txt: db6d6dc0f9c4e66bfc3d15341e873a87d333915d5ce1c611c2169ebbed54d00f
        B/clauses/window-12/meta.json: 46404199fe451069bc2c7549f0e40843a19630090161b7501c9c0109b69ca1a9
        B/clauses/window-13/raw.json: 7e0ba9cbf8367ba43f98439bb6b30bbcfa75b3721b8c256ca2913b803de18ebf
        B/clauses/window-13/prompt.txt: a3b2ee2efb0aed0cacb9bf453350b48ada9c112176fdbfa64704e59721fa8c45
        B/clauses/window-13/meta.json: bc304492fd5b960325ed863e8e08a656d4f73f4bc1a0fb99e6852f47f32a761b
        B/clauses/window-14/raw.json: 25f16bc0ddf289bdfad42f3c42f23dba821f4bee6cf1f8b6f389f8a814f99fc6
        B/clauses/window-14/prompt.txt: 9fda25b34678ca50ce009d4a55b827f99d7dca27de215a01a2bf75d1450ed067
        B/clauses/window-14/meta.json: 3b1825a67bee519d04e057265da95a061a621f45a17d36795e1abba0e7124fe8
        B/clauses/window-09/raw.json: f5e6046712e394f52c5914715674a02e4c3e1516ecf2dede590c9113aa9af66b
        B/clauses/window-09/prompt.txt: 63fc2bcc9cee97886bdd0f1ab41293c55c307291f7c4c75c1dbd0fe81d4bceaa
        B/clauses/window-09/meta.json: df6af6e437d3166f9670febf095e4058fda81d807ea2b5d2ae78f23cdc1ebdc5
        B/clauses/window-07/raw.json: 1e9c192ed871823d2cbe78c69b2ee4198abeb17907584b28573be964096ccb5a
        B/clauses/window-07/prompt.txt: dbbdbe8e6fa7d86e0a9f99a52d195044393a979f9fef63a7c0520a0325e7a5aa
        B/clauses/window-07/meta.json: 0e3b07d41668d0751976799bcadc044901c0cf4d8bec63a3afb0da682be08c2a
        B/clauses/window-01/raw.json: 209cf15ef73577c92cd9cf4afeecd89b5d72bdb2480d2d320b7465a6ccd72cf0
        B/clauses/window-01/prompt.txt: 296f7a0265bbd95e8873cfb1b58bb43ddcdf89291dac70da02d3d1f8616b4e0a
        B/clauses/window-01/meta.json: 479867da7da6f3361224867a1cb89c0939433834682dd467e3df363eeb4d2515
        B/clauses/window-06/raw.json: 3963416927a6dd8c07f28aed19d9d7705b8f4e61e7468b635d5d70b2530ba367
        B/clauses/window-06/prompt.txt: 1f01a51e19120506835225db50b69450535413ecbde4de0631aafe892a3af00a
        B/clauses/window-06/meta.json: 741a75fd1bd56b37b33c0d10f41084a2e5a4c897ad51a0efa374abec50cfbf5b
        B/clauses/window-08/raw.json: 40082bcbe3f0a00d66e1259bfcaa3cbecc39cda4822a5d7239679b3409872400
        B/clauses/window-08/prompt.txt: e20245b8fd3aa952612865298db22bc74ab50214a83990e6c7c69468599eb2a0
        B/clauses/window-08/meta.json: 3ab60426248db1a4460aaf14094847e9716867a7eb5e03f9c05d480a62908d5b
      code:
        relationship_review.py: 6d0359072ca11a7569362fe49703755a98b4207ba814fcd311161c48936053ed
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
      pdf_sha256: 8734accf0936fda0c0b3612e1ecaed66ef0b23f19bce849e602298fd90306020
      source_review: _compare/relationships-2026-11-16/review-current/Halai2017
      source_status_sha256: 4c858c453c8a88982ee9594748f589d82a470d7b08409a46efd71e87200aea91
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R012
    exposure:
      text: speech quanta (F1) and semantic variety (F2) factors
    outcome:
      text: lesion clusters
    analysis_label: VBCM of speech production PCA factors (adjusted for lesion volume)
    relation: sensitivity
    evidence_ids:
    - P8-S3-C4
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
      pdf_sha256: 8734accf0936fda0c0b3612e1ecaed66ef0b23f19bce849e602298fd90306020
      source_review: _compare/relationships-2026-11-16/review-current/Halai2017
      source_status_sha256: 4c858c453c8a88982ee9594748f589d82a470d7b08409a46efd71e87200aea91
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Accounting without a linked unit P1-S2-C3
      - Unaccounted source passage P1-S2-C3
      - Result passage disposed without unit P2-S1-C1
      - Result passage disposed without unit P5-S1-C10
      - Result passage disposed without unit P6-S2-C3
      - Result passage disposed without unit P6-S2-C12
      - Result passage disposed without unit P6-S2-C13
      - Result passage disposed without unit P8-S1-C2
      - Result passage disposed without unit P8-S1-C5
      - Result passage disposed without unit P8-S1-C14
      - Result passage disposed without unit P8-S1-C15
      - Result passage disposed without unit P8-S2-C3
      - Result passage disposed without unit P8-S2-C4
      - Result passage disposed without unit P8-S2-C11
      - Result passage disposed without unit P8-S2-C13
      - Result passage disposed without unit P8-S3-C10
      - Result passage disposed without unit P8-S3-C11
      - Result passage disposed without unit P9-S1-C1
      - Result passage disposed without unit P11-S1-C1
      - Result passage disposed without unit P11-S1-C10
      - Result passage disposed without unit P11-S1-C11
      - Result passage disposed without unit P12-S1-C1
      - Accounting without a linked unit P12-S1-C6
      - Accounting without a linked unit P12-S1-C7
      - Unaccounted source passage P12-S1-C6
      - Unaccounted source passage P12-S1-C7
      - Result passage disposed without unit P12-S1-C11
      - Accounting without a linked unit P12-S2-C2
      - Unaccounted source passage P12-S2-C2
      - Result passage disposed without unit P12-S3-C10
      - Result passage disposed without unit P12-S3-C7
      - Result passage disposed without unit P12-S4-C2
      unattached_null_or_qualifier_ids:
      - P12-S3-C5
      suppressed_nonrepresented_units: 32
      default_disposition_count_requires_completeness_check: 197
      unselected_timing_passages:
      - P4-S2-C3
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P1-S2-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P3-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S2-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S2-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S2-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C12
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C13
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C14
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C15
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S2-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S2-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S2-C13
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S1-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S1-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S2-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S2-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S2-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S2-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S2-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S2-C25
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P4-S1-C11
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P6-S1-C7
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P6-S1-C10
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P11-S1-C6
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P11-S1-C12
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: analysed_sample
        source_ids:
        - P1-S1-C9
        - P1-S2-C2
        - P4-S2-C3
        - P6-S1-C1
        - P6-S2-C12
        - P6-S2-C14
        - P10-S2-C3
        - P11-S1-C4
        - P13-S1-C7
        - P14-S4-C6
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: recruited_sample
        source_ids:
        - P1-S1-C9
        - P1-S2-C2
        - P2-S3-C3
        - P3-S1-C2
        - P4-S2-C3
        - P5-S2-C4
        - P6-S2-C12
        - P6-S2-C14
        - P14-S2-C34
        - P14-S4-C6
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: imaging_provenance
        source_ids:
        - P4-S2-C8
        - P5-S1-C14
        - P6-S2-C9
        - P8-S2-C2
        - P9-S1-C2
        - P10-S1-C5
        - P11-S1-C1
        - P12-S2-C2
        - P12-S2-C7
        - P12-S2-C8
        - P12-S2-C9
        - P12-S2-C10
        - P13-S2-C5
        - P13-S3-C3
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: adjustment_roles
        source_ids:
        - P1-S2-C3
        - P4-S1-C4
        - P5-S1-C11
        - P6-S2-C7
        - P6-S2-C8
        - P8-S2-C1
        - P8-S2-C4
        - P8-S2-C5
        - P8-S2-C6
        - P8-S3-C4
        - P9-S1-C3
        - P9-S1-C11
        - P11-S2-C1
        - P11-S2-C6
        - P12-S1-C8
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: descriptive_personal_factors
        source_ids:
        - P1-S1-C9
        - P1-S2-C2
        - P2-S3-C6
        - P3-S2-C9
        - P4-S2-C3
        - P4-S2-C5
        - P4-S2-C6
        - P4-S3-C6
        - P5-S2-C6
        - P7-S1-C1
        - P7-S1-C2
        - P11-S1-C10
        - P11-S1-C11
        - P11-S2-C4
        - P11-S2-C5
        - P13-S1-C4
        - P14-S4-C6
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - analysed_sample
      - recruited_sample
      - imaging_provenance
      - validation
      - personal_factors
      - tested_personal_effects
      - adjustment_roles
      - explicitly_not_adjusted
      - descriptive_personal_factors
      unclassified_extraction_ids: []
      table_review_required: []
      unlinked_tables: []
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P6-S1
        - P6-S2
        - P6-S3
        - P8-S1
        - P8-S2
        - P9-S1
        - P10-S1
        - P11-S1
        - P11-S2
        - P12-S3
        - P13-S2
        - P13-S3
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 8734accf0936fda0c0b3612e1ecaed66ef0b23f19bce849e602298fd90306020
      source_review: _compare/relationships-2026-11-16/review-current/Halai2017
      source_status_sha256: 4c858c453c8a88982ee9594748f589d82a470d7b08409a46efd71e87200aea91
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the general result of the PCA process (number of components)
        rather than a specific relationship.
    - source_id: P1-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the general result of the PCA process (number of components)
        rather than a specific relationship.
    - source_id: P1-S2-C3
      disposition: repeated
      result_indexes:
      - 16
      reason: Abstract restatement of the omnibus PCA results for speech quanta.
    - source_id: P2-S1-C1
      disposition: repeated
      result_indexes:
      - 14
      - 15
      reason: Abstract restatement of phonological and semantic neural correlates.
    - source_id: P3-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discusses previous work by the authors on PCA factors and lesion distributions.
    - source_id: P3-S3-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports findings from a previous study (Borovsky et al., 2007).
    - source_id: P3-S4-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports findings from a previous study (Borovsky et al., 2007).
    - source_id: P5-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the PCA methodology (orthogonal rotation).
    - source_id: P6-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the analysis plan (three VBCM analyses).
    - source_id: P6-S2-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the lesion overlap map (Fig 1A).
    - source_id: P6-S2-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports the maximum number of participants in a single voxel (descriptive).
    - source_id: P8-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: States that a high degree of inter-correlation was found without specifying
        the pairs.
    - source_id: P8-S1-C3
      disposition: represented
      result_indexes:
      - 0
      reason: Provides specific correlation between token measure, MLU, and WPM.
    - source_id: P8-S1-C4
      disposition: represented
      result_indexes:
      - 0
      reason: Provides specific correlation between MLU, TTR, and WPM.
    - source_id: P8-S1-C5
      disposition: represented
      result_indexes:
      - 1
      reason: Reports null findings for other correlations.
    - source_id: P8-S1-C10
      disposition: represented
      result_indexes:
      - 2
      reason: Reports neural correlates for token measure (T).
    - source_id: P8-S1-C11
      disposition: represented
      result_indexes:
      - 2
      reason: Reports white matter correlation for token measure (T).
    - source_id: P8-S1-C12
      disposition: represented
      result_indexes:
      - 3
      reason: Reports neural correlates for MLU.
    - source_id: P8-S1-C13
      disposition: represented
      result_indexes:
      - 4
      reason: Reports neural correlates for TTR.
    - source_id: P8-S1-C14
      disposition: represented
      result_indexes:
      - 4
      reason: Reports peak voxels for TTR.
    - source_id: P8-S1-C15
      disposition: represented
      result_indexes:
      - 5
      reason: Reports null findings for WPM.
    - source_id: P8-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the correlation between lesion volume and MCA territory integrity.
    - source_id: P8-S2-C4
      disposition: represented
      result_indexes:
      - 6
      - 7
      - 8
      reason: States that including lesion size reduced significance across all measures.
    - source_id: P8-S2-C5
      disposition: represented
      result_indexes:
      - 6
      - 7
      reason: Reports null results for TTR and T after adjustment.
    - source_id: P8-S2-C6
      disposition: represented
      result_indexes:
      - 8
      reason: Reports significant results for MLU after adjustment.
    - source_id: P8-S2-C13
      disposition: represented
      result_indexes:
      - 9
      reason: Reports neural correlates for speech quanta factor (F1).
    - source_id: P8-S2-C14
      disposition: represented
      result_indexes:
      - 10
      reason: Reports neural correlates for semantic variety factor (F2).
    - source_id: P8-S3-C2
      disposition: represented
      result_indexes:
      - 10
      reason: Reports neural correlates for semantic variety factor (F2).
    - source_id: P8-S3-C3
      disposition: represented
      result_indexes:
      - 10
      reason: Reports weaker correlation for semantic variety factor (F2).
    - source_id: P8-S3-C4
      disposition: represented
      result_indexes:
      - 11
      reason: Reports null results for F1 and F2 after lesion volume adjustment.
    - source_id: P8-S3-C6
      disposition: represented
      result_indexes:
      - 12
      reason: Reports correlation between speech quanta and phonology factors.
    - source_id: P8-S3-C7
      disposition: represented
      result_indexes:
      - 13
      reason: Reports correlation between semantic variety and semantics factors.
    - source_id: P8-S3-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the four-factor solution of the omnibus PCA.
    - source_id: P8-S3-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the loading of tasks on the third factor.
    - source_id: P8-S3-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the loading of tasks on the third factor.
    - source_id: P8-S4-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the composition of the omnibus PCA factors.
    - source_id: P9-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the variance of the fourth factor in the omnibus PCA.
    - source_id: P9-S1-C3
      disposition: represented
      result_indexes:
      - 14
      - 15
      - 16
      - 17
      reason: Specifies that results are adjusted for lesion volume.
    - source_id: P9-S1-C11
      disposition: repeated
      result_indexes:
      - 11
      reason: Restatement of null results for factors after lesion volume correction.
    - source_id: P10-S1-C1
      disposition: represented
      result_indexes:
      - 14
      reason: Reports neural correlates for the phonological factor.
    - source_id: P10-S1-C2
      disposition: represented
      result_indexes:
      - 14
      reason: Reports white matter correlates for the phonological factor.
    - source_id: P10-S1-C3
      disposition: represented
      result_indexes:
      - 15
      reason: Reports neural correlates for the semantic factor.
    - source_id: P10-S1-C4
      disposition: represented
      result_indexes:
      - 15
      reason: Reports specific regions for the semantic factor.
    - source_id: P10-S1-C5
      disposition: represented
      result_indexes:
      - 15
      reason: Reports white matter correlates for the semantic factor.
    - source_id: P10-S1-C6
      disposition: represented
      result_indexes:
      - 16
      reason: Reports neural correlates for the speech quanta factor.
    - source_id: P11-S1-C1
      disposition: represented
      result_indexes:
      - 16
      reason: Reports white matter correlates for the speech quanta factor.
    - source_id: P11-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discusses the effect of lesion size on the speech quanta factor.
    - source_id: P11-S1-C3
      disposition: represented
      result_indexes:
      - 17
      reason: Reports null results for the executive factor.
    - source_id: P11-S1-C4
      disposition: represented
      result_indexes:
      - 18
      reason: Reports correlation between lesion volume and executive ability.
    - source_id: P12-S1-C6
      disposition: repeated
      result_indexes:
      - 2
      - 3
      reason: Discussion restatement of individual fluency measure results.
    - source_id: P12-S1-C7
      disposition: repeated
      result_indexes:
      - 4
      reason: Discussion restatement of TTR results.
    - source_id: P12-S2-C2
      disposition: repeated
      result_indexes:
      - 9
      reason: Discussion restatement of speech quanta factor results.
    - source_id: P12-S2-C3
      disposition: repeated
      result_indexes:
      - 10
      reason: Discussion restatement of speech variety factor results.
    - source_id: P12-S2-C7
      disposition: repeated
      result_indexes:
      - 14
      reason: Discussion restatement of phonological factor results.
    - source_id: P12-S2-C8
      disposition: repeated
      result_indexes:
      - 15
      reason: Discussion restatement of semantic factor results.
    - source_id: P12-S2-C9
      disposition: repeated
      result_indexes:
      - 16
      reason: Discussion restatement of speech quanta factor results.
    - source_id: P12-S2-C10
      disposition: repeated
      result_indexes:
      - 16
      reason: Discussion restatement of speech quanta white matter results.
    - source_id: P12-S2-C11
      disposition: repeated
      result_indexes:
      - 17
      reason: Discussion restatement of executive factor null results.
    unresolved_coverage:
    - source_id: P8-S2-C14
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P9-S1-C3
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P8-S2-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S2-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S2-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S2-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S1-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C12
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S2-C1
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S1-C1
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S1-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S1-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S2-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S2-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S3-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S3-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S3-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S3-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S4-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C9
    - P1-S2-C2
    - P1-S2-C3
    - P2-S1-C1
    - P3-S1-C7
    - P3-S3-C9
    - P3-S4-C1
    - P5-S1-C10
    - P6-S2-C3
    - P6-S2-C12
    - P6-S2-C13
    - P8-S1-C2
    - P8-S2-C3
    - P8-S2-C4
    - P8-S2-C7
    - P8-S2-C9
    - P8-S2-C10
    - P8-S2-C11
    - P8-S3-C9
    - P8-S3-C10
    - P8-S3-C11
    - P8-S4-C1
    - P9-S1-C1
    - P9-S1-C11
    - P10-S1-C7
    - P11-S1-C2
    - P11-S1-C10
    - P11-S1-C11
    - P11-S1-C12
    - P11-S2-C1
    - P12-S1-C1
    - P12-S1-C6
    - P12-S1-C7
    - P12-S1-C8
    - P12-S1-C11
    - P12-S2-C2
    - P12-S2-C3
    - P12-S2-C4
    - P12-S2-C6
    - P12-S2-C7
    - P12-S2-C8
    - P12-S2-C9
    - P12-S2-C10
    - P12-S2-C11
    - P12-S3-C3
    - P12-S3-C5
    - P12-S3-C7
    - P12-S3-C10
    - P12-S4-C2
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
      analysed_sample: []
      recruited_sample: []
      eligibility:
      - P4-S2-C3
      - P4-S2-C4
      - P4-S2-C5
      - P4-S2-C6
      - P14-S2-C34
      imaging_provenance: []
      imaging_timing:
      - P4-S2-C5
      outcome_timing:
      - P4-S2-C5
      - P14-S4-C6
      outcome_definition:
      - P4-S2-C1
      - P4-S2-C9
      - P4-S3-C1
      - P9-S1-C5
      - P13-S2-C25
      validation: []
      analysis_restrictions:
      - P4-S2-C4
      - P4-S3-C12
      dependent_variable_statement:
      - P2-S3-C3
      - P4-S2-C1
      - P4-S2-C9
      - P4-S3-C1
      limitations:
      - P2-S2-C6
      - P2-S2-C7
      - P3-S2-C5
      - P12-S1-C8
      - P12-S2-C4
      - P13-S1-C5
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles: []
      explicitly_not_adjusted: []
      descriptive_personal_factors: []
    outcome_type: both_reported
    imaging_vs_outcome: concurrent
    validation_type: mixed
    window_merge: Union of selected IDs; differing window enums retained conservatively
      as both/mixed. Not verified study-level facts.
    held_selections:
    - slot: dependent_variable_statement
      source_id: P1-S2-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P3-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S2-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S2-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S2-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C12
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C13
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C14
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C15
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S2-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S2-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S2-C13
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S1-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S1-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S2-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S2-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S2-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S2-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S2-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S2-C25
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P4-S1-C11
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P6-S1-C7
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P6-S1-C10
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P11-S1-C6
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P11-S1-C12
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: analysed_sample
      source_ids:
      - P1-S1-C9
      - P1-S2-C2
      - P4-S2-C3
      - P6-S1-C1
      - P6-S2-C12
      - P6-S2-C14
      - P10-S2-C3
      - P11-S1-C4
      - P13-S1-C7
      - P14-S4-C6
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: recruited_sample
      source_ids:
      - P1-S1-C9
      - P1-S2-C2
      - P2-S3-C3
      - P3-S1-C2
      - P4-S2-C3
      - P5-S2-C4
      - P6-S2-C12
      - P6-S2-C14
      - P14-S2-C34
      - P14-S4-C6
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: imaging_provenance
      source_ids:
      - P4-S2-C8
      - P5-S1-C14
      - P6-S2-C9
      - P8-S2-C2
      - P9-S1-C2
      - P10-S1-C5
      - P11-S1-C1
      - P12-S2-C2
      - P12-S2-C7
      - P12-S2-C8
      - P12-S2-C9
      - P12-S2-C10
      - P13-S2-C5
      - P13-S3-C3
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: adjustment_roles
      source_ids:
      - P1-S2-C3
      - P4-S1-C4
      - P5-S1-C11
      - P6-S2-C7
      - P6-S2-C8
      - P8-S2-C1
      - P8-S2-C4
      - P8-S2-C5
      - P8-S2-C6
      - P8-S3-C4
      - P9-S1-C3
      - P9-S1-C11
      - P11-S2-C1
      - P11-S2-C6
      - P12-S1-C8
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: descriptive_personal_factors
      source_ids:
      - P1-S1-C9
      - P1-S2-C2
      - P2-S3-C6
      - P3-S2-C9
      - P4-S2-C3
      - P4-S2-C5
      - P4-S2-C6
      - P4-S3-C6
      - P5-S2-C6
      - P7-S1-C1
      - P7-S1-C2
      - P11-S1-C10
      - P11-S1-C11
      - P11-S2-C4
      - P11-S2-C5
      - P13-S1-C4
      - P14-S4-C6
      reason: Runaway selection (>8 passages); entire slot requires source review
    policy: All slots and enums remain unverified. Held selections are not evidence
      of absence. Original responses are preserved in frame/chunk-*/attempt-*/raw.json.
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
      pdf_sha256: 8734accf0936fda0c0b3612e1ecaed66ef0b23f19bce849e602298fd90306020
      review_sha256: 2d709ade5f5e26d25ded5f0d9175b09862fc572ccc664532983b4fadac69c43b
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
      - P8-S3-C4
      source_result: The source states that after adding a covariate for lesion volume,
        no significant clusters remained for the speech quanta (F1) or semantic variety
        (F2) factors in the VBCM analysis.
      result_status: lost_after_adjustment
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis R012 corresponds to the VBCM analysis of speech
            production PCA factors (F1 and F2) adjusted for lesion volume, as described
            in P8-S3-C4 and P6-S2-C5.
          source_ids:
          - P8-S3-C4
          - P6-S2-C5
        direction:
          answer: fits
          reason: The draft correctly identifies the result as a loss of significance
            after adjustment (no_effect in the adjusted model), consistent with P8-S3-C4
            stating 'no significant clusters remained'.
          source_ids:
          - P8-S3-C4
        construct:
          answer: fits
          reason: The exposure (speech quanta and semantic variety factors) and outcome
            (lesion distribution via VBCM) are correctly identified. The patient measurement
            is template_lesion_overlap (VBCM using T1 images and lesion maps), not
            patient_diffusion.
          source_ids:
          - P8-S2-C9
          - P8-S2-C10
          - P6-S2-C1
        qualifications:
          answer: fits
          reason: The draft includes the critical qualification that the analysis
            was adjusted for lesion volume, which is the condition under which the
            null result was observed.
          source_ids:
          - P8-S3-C4
          - P6-S2-C7
        missing_material_caveat:
          answer: fits
          reason: The draft includes the limitation regarding automated lesion identification
            detecting unexpected tissue classes (P6-S1-C11). No other material caveats
            are omitted that would change the interpretation of the null result.
          source_ids:
          - P6-S1-C11
      optional_pending: []
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    normalizations: []
    analysis_identity:
      id: R012
      exposure:
        text: speech quanta (F1) and semantic variety (F2) factors
      outcome:
        text: lesion clusters
      analysis_label: VBCM of speech production PCA factors (adjusted for lesion volume)
      relation: sensitivity
      evidence_ids:
      - P8-S3-C4
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
        pdf_sha256: 8734accf0936fda0c0b3612e1ecaed66ef0b23f19bce849e602298fd90306020
        source_review: _compare/relationships-2026-11-16/review-current/Halai2017
        source_status_sha256: 4c858c453c8a88982ee9594748f589d82a470d7b08409a46efd71e87200aea91
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P4-S2-C3:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 8734accf0936fda0c0b3612e1ecaed66ef0b23f19bce849e602298fd90306020
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: f170e953262ba5004e731b4c38f349d767cd4f3686b9c171aee9898a52cff4ce
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P4-S2-C3
          page: 4
          text_layer_sha256: f170e953262ba5004e731b4c38f349d767cd4f3686b9c171aee9898a52cff4ce
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Participants

          Thirty one chronic stroke patients (either ischaemic or hae-

          morrhagic) were recruited (the same patients as reported by

          Butler et al., 2014), who had impairment in producing and/or

          understanding spoken language and their aphasia was clas-

          siﬁed using the Boston Diagnostic Aphasia Examination

          (BDAE).'
        anchor_text: 'Participants

          Thirty one chronic stroke patients (either ischaemic or hae-

          morrhagic) were recruited (the same patients as reported by

          Butler et al., 2014), who had impairment in producing and/or

          understanding spoken language and their aphasia was clas-

          siﬁed using the Boston Diagnostic Aphasia Examination

          (BDAE).'
        excluded_fragments: []
        image_sha256: 4e2461e2b72867b48b6b6ab04be48cd286e7740d9c311a122642830c7eefeaf9
        transcription: 'Participants


          Thirty one chronic stroke patients (either ischaemic or hae-

          morrhagic) were recruited (the same patients as reported by

          Butler et al., 2014), who had impairment in producing and/or

          understanding spoken language and their aphasia was clas-

          sified using the Boston Diagnostic Aphasia Examination

          (BDAE)'
      P4-S2-C5:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 8734accf0936fda0c0b3612e1ecaed66ef0b23f19bce849e602298fd90306020
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 48e09e3a6941d5a0d6d7c64a2943e61995cdd2644249b175cdabba0ec32de5df
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P4-S2-C5
          page: 4
          text_layer_sha256: 48e09e3a6941d5a0d6d7c64a2943e61995cdd2644249b175cdabba0ec32de5df
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'All patients

          were at least 12 months post-stroke at the time of scanning

          and assessment, were native English speakers with normal or

          corrected-to-normal hearing and vision (see Table 1 for a

          summary of demographic details).'
        anchor_text: 'All patients

          were at least 12 months post-stroke at the time of scanning

          and assessment, were native English speakers with normal or

          corrected-to-normal hearing and vision (see Table 1 for a

          summary of demographic details).'
        excluded_fragments: []
        image_sha256: 1b69f7dfc197ee93fc7b2ec46231815d7f9df0a4798416f5c831490b941b9ac5
        transcription: '. All patients

          were at least 12 months post-stroke at the time of scanning and

          assessment, were native English speakers with normal or

          corrected-to-normal hearing and vision (see Table 1 for a

          summary of demographic details)'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 8
  quote: 'After adding a co-

    variate for lesion volume, no signiﬁcant clusters remained for

    F1 or F2.

    3.5.'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-24'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
