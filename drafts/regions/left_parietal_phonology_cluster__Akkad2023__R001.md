---
id: left_parietal_phonology_cluster
name: left parietal cluster
kind: network
findings:
- id: f1
  target: phonological_factor
  target_kind: impairment
  claim: Performance on the phonological factor was uniquely correlated with a cluster
    of voxels in the left parietal lobe, with peak voxels in the left superior parietal
    lobe and intraparietal sulcus, including voxels in the left inferior parietal
    lobule.
  direction: likely
  relationship: correlational
  method: VBCM
  sample:
    n: 36
    population: English speakers with chronic aphasia following a single left-hemisphere
      stroke and long-term speech production deficits (anomia), with relatively intact
      comprehension and no speech apraxia
    phase: not_reported
    time_post_onset: at least 12 months post-stroke; concurrent association between
      imaging and assessment
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Small sample size
  - Structural MRI scans were not optimised for the detection of white matter fibre
    bundles
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Patient lesion overlap with a voxel-based correlational
    morphology (VBCM) analysis of a latent phonological factor (derived via PCA of
    behavioral tests including word and non-word repetition). The phonological factor
    was one of four orthogonal PCA factors entered simultaneously as covariates; Analysis
    controlled for lesion volume. Additional metadata has not been transcribed; review
    the pending-field flags before approval. PDF image reading (P2-S4-C13, two-model
    agreement, human verification pending): Participants


    Thirty-six English speakers with chronic aphasia following a single left-hemisphere
    stroke participated in the study (see Fig. 1 for a lesion overlap map, Table 1
    for demographic and clinical data) Original text-layer quotation is preserved
    below. PDF image reading (P2-S5-C2, two-model agreement, human verification pending):
    . All were at

    least 12 months post-stroke and at the time of scanning and assessment,

    had normal hearing, normal or corrected-to-normal visual acuity and no

    previous history of significant neurological or psychiatric disease Original text-layer
    quotation is preserved below. PDF image reading (P3-S1-C1, two-model agreement,
    human verification pending): (Swinburn et al., 2004); (iii) relatively spared
    ability to repeat single

    monosyllabic words from the Psycholinguistic Assessments of Language

    Processing in Aphasia (Kay, 1992); (iv) absence of speech apraxia as

    determined by the Apraxia Battery for Adults (Dabul, 2000) Original text-layer
    quotation is preserved below. Reconcile this new analysis with earlier drafts
    and source-review decisions for the paper; new candidate IDs do not carry earlier
    decisions forward.'
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
    - proposed_concept:phonological_factor
  citation: '@Akkad2023'
  source_passages:
  - section: Original source P5-S2-C8
    page: 5
    quote: "Performance on the phonological factor was uniquely correlated \nwith\
      \ a cluster of voxels in the left parietal lobe, with peak voxels in the \n\
      left superior parietal lobe and intraparietal sulcus."
    supports: claim
  - section: Original source P5-S2-C9
    page: 5
    quote: "The cluster also \nincluded voxels in the left inferior parietal lobule."
    supports: claim
  - section: Original source P2-S4-C13
    page: 2
    quote: "Participants \nThirty-six English speakers with chronic aphasia following\
      \ a single \nleft-hemisphere stroke participated in the study (see Fig. 1 for\
      \ a lesion \noverlap map, Table 1 for demographic and clinical data)."
    supports: sample
  - section: Original source P2-S5-C2
    page: 2
    quote: "All were at \nleast 12 months post-stroke and at the time of scanning\
      \ and assessment, \nhad normal hearing, normal or corrected-to-normal visual\
      \ acuity and no \nprevious history of significant neurological or psychiatric\
      \ disease."
    supports: sample
  - section: Original source P2-S5-C3
    page: 2
    quote: "In­\nclusion criteria were: (i) anomia as determined by the naming subtest\
      \ of \nthe Comprehensive Aphasia Test (Swinburn et al., 2004); (ii) good single\
      \ \nword comprehension as indexed by an accuracy score>70% on the \nspoken word\
      \ comprehension subtest of the Comprehensive Aphasia Test \nH."
    supports: sample
  - section: Original source P3-S1-C1
    page: 3
    quote: "\nNeuroImage: Clinical 39 (2023) 103452\n3\n(Swinburn et al., 2004); (iii)\
      \ relatively spared ability to repeat single \nmonosyllabic words from the Psycholinguistic\
      \ Assessments of Language \nProcessing in Aphasia (Kay, 1992); (iv) absence\
      \ of speech apraxia as \ndetermined by the Apraxia Battery for Adults (Dabul,\
      \ 2000)."
    supports: sample
  - section: Original source P4-S1-C11
    page: 4
    quote: "Lesion-Symptom mapping \nFor lesion-symptom mapping, we used the fuzzy\
      \ lesion images as \ndescribed above and correlated these with PCA factor scores\
      \ using a \nvoxel-based correlational methodology (VBCM) (Tyler et al., 2005),\
      \ a \nvariant of voxel-lesion symptom mapping (VLSM) (Bates et al., 2003)."
    supports: method
  - section: Original source P5-S1-C5
    page: 5
    quote: "In order to ensure that the results were not merely attrib­\nutable to\
      \ lesion size, each participants’ lesion volume was calculated \nfrom the lesion\
      \ identified by the automated lesion identification method \n(Seghier et al.,\
      \ 2008) and this was entered as a covariate in the VBCM."
    supports: confounders
  - section: Original source P5-S1-C11
    page: 5
    quote: "Tasks that tapped into input and \noutput phonology (e.g. word and non-word\
      \ repetition) loaded heavily \non Factor 1, as such we refer to this factor\
      \ as ‘Phonology’."
    supports: claim
  - section: Original source P7-S4-C2
    page: 7
    quote: "It is important to note that our \nfindings are limited by a small sample\
      \ size and should be interpreted \nwith caution."
    supports: limitation
  - section: Original source P6-S3-C10
    page: 6
    quote: "We \nnote that VBM and structural MRI scans are not optimised for the\
      \ \ndetection of white matter fibre bundles and therefore, any interpretation\
      \ \nof white matter tracts in this study are limited."
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-20'
relationship_review:
  paper: Akkad2023
  proposal_id: R001
  review_status_sha256: c4a369558853c060aa4c2265d603cef97efe695659c60a271361fed977cacee2
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 84a00ab74d2b971ceb854a33aa548a335443cae5658f32e4cc3444237e344e40
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 84a00ab74d2b971ceb854a33aa548a335443cae5658f32e4cc3444237e344e40
        A/passages.json: 8c6cf2b3daafd546e3ce17ada8141a3d1e940ecc90f70c4625d1d88cbe44ebdb
        A/raw.json: 119f238116774559d4d8fe39b1850918f4253ab4df7c6504c2d76b06d5ea861a
        A/source-units.json: 0b6e7b4ecac4cc15b854d9d6244ad327fd2853c3e7e1f6283464dfac06b2fa50
        A/full-source-units.json: eb83db8d362899e54f24fb7a0b52bb14e3e491568ba7b1f5df858d76b95f2e2b
        A/meta.json: 0ad5e15295dfb6ac7a5f11e29cea643cc7567cc2c21e26bf2b31602d6814265f
        A/table-images/page-6.png: 08aacae3c967dee76d396065585a0a4cb4270bdc3fccdb697c1887f3bf33e7e6
        A/table-images/page-4.png: 178e254ac56b367b9ba1984ce7f44b02ec724749abe7e333a3e0a21cfd63e7b4
        A/table-images/TABLE-1-page-4-1.png: 0369966b0095e1349e7a393b27d1b9ce07be71431ff50833e3cd5efed11b7c85
        A/table-images/TABLE-3-page-6-1.png: 7b48e852629aa7042af308d192015c5c84814d7bd5e845132cdedbd095b3621f
        A/table-images/TABLE-2-page-4-2.png: 6c2623fe0939da6deb0706d37c6fa1ed2500e2d7cff3ba1566e3327ccd39fea2
        A/table-images/manifest.json: 57a893bf52bf6dc7c8e5703c711bedd1ec64f88bb4827f8be478a3cf11b4f4fc
        A/clauses/window-03/raw.json: fb2ebcdb9ca66fe581b1ce8b5cd6b9b587a499c5340beaf5f48b69b224fd9f91
        A/clauses/window-03/prompt.txt: 1bf39734a2bd21111625aed07717ce8671b3fbf7579b3f041af37459b3f1e668
        A/clauses/window-03/meta.json: 071fc8cb33ba16ddca064281c59bf3dc450c669fb6d6146c33eac4f9b1ac5d7a
        A/clauses/window-04/raw.json: 9f01ed7e33d92a08cba31baed75619958f7cd020eb295cfb39fba079c589e348
        A/clauses/window-04/prompt.txt: 718622945ab855d2ccfad5383921de5518fccbf55b564c21014bb94f792dd09d
        A/clauses/window-04/meta.json: ed01824402c0397d6f2233d3f72be0b04c9b0f2f64b938cd7652c8cb3c530375
        A/clauses/window-05/raw.json: a56a435ebaef11f3bb7dab955e16f5dbd74696b1f61f1edd1892cb3cf9e36e8a
        A/clauses/window-05/prompt.txt: e81462383fe5e8003f3ba4a03a01d3eb9f340ccf814c2b92058e46bf69acf55d
        A/clauses/window-05/meta.json: 6b5e8dcfad4039ae2b5d38f5e5f612192874987dc4988874aaf1ea5ecf1570b0
        A/clauses/window-02/raw.json: 002891ab1fb5aa84a74f5ff323cea390e4b2dbc01d1be72f39ff0847e6dd1178
        A/clauses/window-02/prompt.txt: 81ff665755e53068034c71c31ffe028ecd7f800ad0785135e41cf1679e439c37
        A/clauses/window-02/meta.json: 8ed446778c7adb6c94c3e878684639a4aae070a6746134cd136c5d80d80690fd
        A/clauses/window-07/raw.json: 9cc67a5dbf62d98722ebafad17748f93e9844d15a83aada85269d78a46830bd3
        A/clauses/window-07/prompt.txt: 73badb46c3f3b9d98cf2e3d544f9fdc64dbd355e72e4373fd237a2d0831c2c9c
        A/clauses/window-07/meta.json: d8b2f0fd542a218e8941c8ec06edd83b91cb36f68566c29fbb437274454480cd
        A/clauses/window-01/raw.json: 9bf3af3e315a3067ddeb9ee1369c0b478fe3e6b0fd2d6e0e5fbfcd8b2ef0ba6b
        A/clauses/window-01/prompt.txt: e92dab33369c07205dfd02e8f8a80970a43fad527ed50148bcc5c16a03696715
        A/clauses/window-01/meta.json: dd9ee73230908ad42b63e90b12047297bcccd3b4cc6faadfacbd49e9a3667afa
        A/clauses/window-06/raw.json: 3c880c2036c7e094a731362363db1e18f5f06268ec6b27f5e81413a42ef38cf2
        A/clauses/window-06/prompt.txt: 832b157d3b49798257b027ecef0b76c78c8257eac14ecba8ffeba13a7d39d5d8
        A/clauses/window-06/meta.json: 65da4b01ef78edad4c5b2ba0917063c1faabf77709fc859839efe4b50aa35ca2
        A/clauses/window-08/raw.json: e707c704e012eacdd64db5a61f5dc8abcc1da7a9e4ee6fb9a47ee1573ab1e735
        A/clauses/window-08/prompt.txt: 46d2406d97ab52ef747854bb3bc341bd2f5bb209ad725fefa002e62fc4b3be0c
        A/clauses/window-08/meta.json: e5b421ffc9c3ded168129ba4d1a84a2ef5a61b68a694d4b59ca9f305cca28477
        A/tables/TABLE-3-page-6-3/raw.json: 8dfa59c6b4b4122a8749b4f5dceef005cb9bdf6e4c862072f9839de2fde3d3c1
        A/tables/TABLE-3-page-6-3/prompt.txt: 2cd8a4a4819c10fb017a613bdd9705e923ac2fdcafbe70af588729a6e48f202c
        A/tables/TABLE-3-page-6-3/meta.json: 9c6a9a57400ca7624fbada59e995bc8e923e15fc0e84afdb3685636037d61516
        A/tables/TABLE-1-page-4-1/raw.json: 34523ca975d3b354491b914d971c6246667378ce236c3c20d95025e48af6f0c0
        A/tables/TABLE-1-page-4-1/prompt.txt: b6b2fca8175855253046f4aeb2617d0bb039d65f141cf8f8177d7bf2953370a9
        A/tables/TABLE-1-page-4-1/meta.json: e5a3ab7d07e5c5b966e0ca4e2d150acb4125b29b8c7a7bf4c0d67d41aaab00db
        A/tables/TABLE-2-page-4-2/raw.json: a39f884564040d659c853e278fe792dfea8b91f51dcec4fa82e20765405f0682
        A/tables/TABLE-2-page-4-2/prompt.txt: 6bbb6563b1313f08f526ba7c5e9fbb067b222dd871f1e66241ccf9cf1f558bdf
        A/tables/TABLE-2-page-4-2/meta.json: fba781e3c19dcab686d4739e5b32f5153a1db2f1fa4d0d5710f8e72a84f6fc3a
        B/passages.json: 8c6cf2b3daafd546e3ce17ada8141a3d1e940ecc90f70c4625d1d88cbe44ebdb
        B/raw.json: 0ee1339a4c929cdc048bc8dec86c79892270497168d5ad5ff3c37df2440ce034
        B/source-units.json: 0b6e7b4ecac4cc15b854d9d6244ad327fd2853c3e7e1f6283464dfac06b2fa50
        B/full-source-units.json: eb83db8d362899e54f24fb7a0b52bb14e3e491568ba7b1f5df858d76b95f2e2b
        B/meta.json: 975aa54b2bc582d8a6a938cad3fa2d0408a0e367889423fad37d219d2e6ef0a2
        B/table-images/page-6.png: 08aacae3c967dee76d396065585a0a4cb4270bdc3fccdb697c1887f3bf33e7e6
        B/table-images/page-4.png: 178e254ac56b367b9ba1984ce7f44b02ec724749abe7e333a3e0a21cfd63e7b4
        B/table-images/TABLE-1-page-4-1.png: 0369966b0095e1349e7a393b27d1b9ce07be71431ff50833e3cd5efed11b7c85
        B/table-images/TABLE-3-page-6-1.png: 7b48e852629aa7042af308d192015c5c84814d7bd5e845132cdedbd095b3621f
        B/table-images/TABLE-2-page-4-2.png: 6c2623fe0939da6deb0706d37c6fa1ed2500e2d7cff3ba1566e3327ccd39fea2
        B/table-images/manifest.json: 1a81202cffd0ee9272d22dacb5cd9a05ffa480b56dc5e4b77edad175b7e4393e
        B/clauses/window-03/raw.json: 34722af7028b0efafba52b9a2195addb0315da5620c26d2f528f845edd00cf54
        B/clauses/window-03/prompt.txt: 1bf39734a2bd21111625aed07717ce8671b3fbf7579b3f041af37459b3f1e668
        B/clauses/window-03/meta.json: bc7557d755d9a94f25457f70d8174b79163c4291c2ef127e9a43d007eca3d925
        B/clauses/window-04/raw.json: df8b0d3d15090a3e7179a0a85b2f46673fec9f442e667a1ff535964ec737386d
        B/clauses/window-04/prompt.txt: 718622945ab855d2ccfad5383921de5518fccbf55b564c21014bb94f792dd09d
        B/clauses/window-04/meta.json: fb2273e4622aa5c8dbff55f649b582be8abbcc5ee8cda6a4282ee014f0324039
        B/clauses/window-05/raw.json: 5030cd3227048f8f2896aa1ef56ced1ea6387f8f9341159aa3860ce2145f7617
        B/clauses/window-05/prompt.txt: e81462383fe5e8003f3ba4a03a01d3eb9f340ccf814c2b92058e46bf69acf55d
        B/clauses/window-05/meta.json: 82b962fa6580546ccb2b75c54baaaa9d9fbec97a47c3b0d1140771ce396f6b45
        B/clauses/window-02/raw.json: b44ab149ba470c2f29ab6e427a33c1c20300ee1005e81e9ac6c886debb3c2891
        B/clauses/window-02/prompt.txt: 81ff665755e53068034c71c31ffe028ecd7f800ad0785135e41cf1679e439c37
        B/clauses/window-02/meta.json: 3e72b72defbe6bdfde2077632d4c93599c11a584db99919ac9c99b605f4fad6f
        B/clauses/window-07/raw.json: 1644384374c5d61c4422bcf07753bba967dcb320f28c3eba842619f96d3447d3
        B/clauses/window-07/prompt.txt: 73badb46c3f3b9d98cf2e3d544f9fdc64dbd355e72e4373fd237a2d0831c2c9c
        B/clauses/window-07/meta.json: af267c402b4f8a22838734bb0c5381dbb70a5fe4c7aa06cd8ce81dfc25f697b2
        B/clauses/window-01/raw.json: 89b3af628f868c9d4a028c496c794a93f6670fb59306e7e374833bec74895f2e
        B/clauses/window-01/prompt.txt: e92dab33369c07205dfd02e8f8a80970a43fad527ed50148bcc5c16a03696715
        B/clauses/window-01/meta.json: cf37f029687fc6d6ff7aabb74480f109a7e5d2ebd079dfc0a6c231aaef7e52f5
        B/clauses/window-06/raw.json: c915bbf3e536ac7b03407509affe23ef95051decb68a34de150c38c870767413
        B/clauses/window-06/prompt.txt: 832b157d3b49798257b027ecef0b76c78c8257eac14ecba8ffeba13a7d39d5d8
        B/clauses/window-06/meta.json: 14e8b3ba1965cb3b81e8a5ace0d791780a3e3452ddc026db46198f0077689775
        B/clauses/window-08/raw.json: efde6d505f1030374f070a22f70d4d6be883f05ae5e5e4593a2a96e1af494721
        B/clauses/window-08/prompt.txt: 46d2406d97ab52ef747854bb3bc341bd2f5bb209ad725fefa002e62fc4b3be0c
        B/clauses/window-08/meta.json: 330f9e24d4966b25f0b77c2aa570d2b646cebde19976d41e73fba6483de17a35
        B/tables/TABLE-3-page-6-3/raw.json: 37ad8984785f499f2ad735d29d6639d51787638c4f8010117efea3f2c73d63e4
        B/tables/TABLE-3-page-6-3/prompt.txt: 2cd8a4a4819c10fb017a613bdd9705e923ac2fdcafbe70af588729a6e48f202c
        B/tables/TABLE-3-page-6-3/meta.json: 9f1d524fdc3a9383ff48e474ff0ca11fad2be10053cd5b7f2b8fee51e7393070
        B/tables/TABLE-1-page-4-1/raw.json: 85b9734dfc99b0ff782da20fc6c5085f460ef829f0d669e62999c63a15c21af8
        B/tables/TABLE-1-page-4-1/prompt.txt: b6b2fca8175855253046f4aeb2617d0bb039d65f141cf8f8177d7bf2953370a9
        B/tables/TABLE-1-page-4-1/meta.json: 0e6ef5198c68c5ce5e255389d446b79ff8d83a724fa5d09a1b2ca4f26860199d
        B/tables/TABLE-2-page-4-2/raw.json: a71377cfe0c1143133f7dd7086f6c9c6b11e37829456f43db1f7f5a88116064c
        B/tables/TABLE-2-page-4-2/prompt.txt: 6bbb6563b1313f08f526ba7c5e9fbb067b222dd871f1e66241ccf9cf1f558bdf
        B/tables/TABLE-2-page-4-2/meta.json: b6aad5097601df6ae03cc717fb180455a7a8636aa71a0e7bd990a5f330983703
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
      pdf_sha256: 84a00ab74d2b971ceb854a33aa548a335443cae5658f32e4cc3444237e344e40
      source_review: _compare/relationships-2026-11-16/review-current/Akkad2023
      source_status_sha256: 15ad6658b87971a6e568f6ae98cd0be730493d4704512aa6376c56a31606b3df
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R001
    exposure:
      text: phonological factor
    outcome:
      text: tissue damage in the left parietal lobe (peak in left superior parietal
        lobe and intraparietal sulcus, including left inferior parietal lobule)
    analysis_label: VBCM of PCA factors
    relation: association
    evidence_ids:
    - P5-S2-C8
    - P5-S2-C9
    qualifier_ids:
    - P5-S2-C7
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 84a00ab74d2b971ceb854a33aa548a335443cae5658f32e4cc3444237e344e40
      source_review: _compare/relationships-2026-11-16/review-current/Akkad2023
      source_status_sha256: 15ad6658b87971a6e568f6ae98cd0be730493d4704512aa6376c56a31606b3df
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Accounting without a linked unit P1-S2-C2
      - Accounting without a linked unit P1-S2-C3
      - Unaccounted source passage P1-S2-C3
      - Unaccounted source passage P1-S2-C2
      - Result passage disposed without unit P5-S1-C11
      - Result passage disposed without unit P5-S1-C12
      - Result passage disposed without unit P5-S2-C2
      - Result passage disposed without unit P5-S2-C3
      - Result passage disposed without unit P5-S2-C15
      - 'window 7: invalid/duplicate disposition P6-S3-C10'
      - Result passage disposed without unit P6-S4-C2
      - Accounting without a linked unit P7-S1-C11
      - Accounting without a linked unit P7-S1-C3
      - Accounting without a linked unit P7-S1-C7
      - Result passage disposed without unit P7-S2-C7
      - Unaccounted source passage P7-S1-C7
      - Unaccounted source passage P7-S1-C11
      - Unaccounted source passage P7-S1-C3
      - Result passage disposed without unit P7-S2-C8
      - Result passage disposed without unit P7-S2-C9
      unattached_null_or_qualifier_ids: []
      suppressed_nonrepresented_units: 17
      default_disposition_count_requires_completeness_check: 173
      unselected_timing_passages:
      - P1-S1-C11
      - P2-S3-C9
      - P2-S4-C13
      - P4-S2-C3
      - P6-S1-C3
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: validation
        source_id: P4-S1-C12
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      empty_frame_slots_require_confirmation:
      - validation
      - personal_factors
      - tested_personal_effects
      - explicitly_not_adjusted
      unclassified_extraction_ids:
      - P2-S2-C11
      table_review_required:
      - TABLE-1-page-4-1
      - TABLE-2-page-4-2
      - TABLE-3-page-6-3
      unlinked_tables:
      - TABLE-1-page-4-1
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P2-S4
        - P2-S5
        - P3-S1
        - P3-S3
        - P4-S1
        - P5-S1
        - P5-S2
        - P5-S3
        - P5-S4
        - P6-S1
        - P6-S2
        - P6-S3
        - P7-S1
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 84a00ab74d2b971ceb854a33aa548a335443cae5658f32e4cc3444237e344e40
      source_review: _compare/relationships-2026-11-16/review-current/Akkad2023
      source_status_sha256: 15ad6658b87971a6e568f6ae98cd0be730493d4704512aa6376c56a31606b3df
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S2-C2
      disposition: represented
      result_indexes: []
      reason: Abstract restatement of general findings
    - source_id: P1-S2-C3
      disposition: represented
      result_indexes: []
      reason: Abstract restatement of general findings
    - source_id: P3-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes missing data incidence
    - source_id: P5-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: PCA variance reporting
    - source_id: P5-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Factor interpretation
    - source_id: P5-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Factor interpretation
    - source_id: P5-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Factor interpretation
    - source_id: P5-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Factor interpretation
    - source_id: P5-S2-C8
      disposition: represented
      result_indexes:
      - 0
      reason: Direct result of VBCM for phonology
    - source_id: P5-S2-C9
      disposition: represented
      result_indexes:
      - 0
      reason: Direct result of VBCM for phonology
    - source_id: P5-S2-C10
      disposition: represented
      result_indexes:
      - 1
      reason: Direct result of VBCM for semantics
    - source_id: P5-S2-C11
      disposition: represented
      result_indexes:
      - 1
      reason: Direct result of VBCM for semantics
    - source_id: P5-S2-C12
      disposition: represented
      result_indexes:
      - 2
      reason: Direct result of VBCM for verbal working memory
    - source_id: P5-S2-C15
      disposition: represented
      result_indexes:
      - 2
      reason: Direct result of VBCM for verbal working memory
    - source_id: P5-S3-C2
      disposition: represented
      result_indexes:
      - 3
      reason: Direct result of VBCM for executive functions
    - source_id: P5-S3-C6
      disposition: represented
      result_indexes:
      - 4
      - 5
      reason: Direct result of ROI analysis for Broca's area
    - source_id: P5-S3-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Correlation between lesion volume and factors
    - source_id: P6-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Correlation between lesion volume and factors
    - source_id: P6-S1-C2
      disposition: represented
      result_indexes:
      - 7
      reason: Sensitivity result for age/time covariates
    - source_id: P6-S1-C4
      disposition: represented
      result_indexes:
      - 6
      reason: Sensitivity result for lesion volume covariate
    - source_id: P6-S1-C9
      disposition: repeated
      result_indexes:
      - 0
      - 1
      - 2
      - 3
      reason: Discussion restatement of VBCM results
    - source_id: P6-S2-C1
      disposition: repeated
      result_indexes:
      - 3
      reason: Discussion restatement of executive function result
    - source_id: P6-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Variance reporting
    - source_id: P6-S2-C4
      disposition: repeated
      result_indexes:
      - 0
      reason: Discussion restatement of phonology result
    - source_id: P6-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison to prior study
    - source_id: P6-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison to prior study
    - source_id: P6-S2-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Variance reporting
    - source_id: P6-S3-C3
      disposition: repeated
      result_indexes:
      - 1
      reason: Discussion restatement of semantic result
    - source_id: P6-S3-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: General behavioral claim
    - source_id: P6-S3-C9
      disposition: repeated
      result_indexes:
      - 2
      reason: Discussion restatement of verbal working memory result
    - source_id: P6-S4-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Table reference
    - source_id: P6-S4-C3
      disposition: represented
      result_indexes:
      - 0
      - 1
      - 2
      - 3
      reason: Table 3 provides coordinates for VBCM results
    - source_id: P7-S1-C3
      disposition: repeated
      result_indexes:
      - 3
      reason: Discussion restatement of executive function result
    - source_id: P7-S1-C7
      disposition: repeated
      result_indexes:
      - 3
      reason: Discussion restatement of executive function result
    - source_id: P7-S1-C11
      disposition: repeated
      result_indexes:
      - 3
      reason: Discussion restatement of executive function result
    - source_id: P7-S2-C1
      disposition: repeated
      result_indexes:
      - 3
      reason: Discussion restatement of executive function result
    - source_id: P7-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes factor loadings
    - source_id: P7-S2-C8
      disposition: repeated
      result_indexes:
      - 3
      reason: Discussion restatement of executive function result
    - source_id: P7-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison to prior study
    - source_id: P7-S3-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison to prior study
    - source_id: P7-S3-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison to prior study
    - source_id: P7-S3-C8
      disposition: repeated
      result_indexes: []
      reason: Conclusion restatement
    - source_id: P7-S3-C9
      disposition: repeated
      result_indexes:
      - 3
      reason: Conclusion restatement of executive function result
    unresolved_coverage:
    - source_id: P1-S2-C2
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P1-S2-C3
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P6-S2-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P6-S4-C3
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P7-S2-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P7-S3-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P7-S3-C2
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P7-S3-C8
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    pending_source_ids:
    - P1-S2-C2
    - P1-S2-C3
    - P3-S2-C8
    - P5-S1-C9
    - P5-S1-C11
    - P5-S1-C12
    - P5-S2-C2
    - P5-S2-C3
    - P5-S3-C9
    - P6-S1-C1
    - P6-S1-C9
    - P6-S2-C3
    - P6-S2-C4
    - P6-S2-C6
    - P6-S2-C8
    - P6-S2-C12
    - P6-S3-C3
    - P6-S3-C5
    - P6-S3-C9
    - P6-S4-C2
    - P7-S1-C3
    - P7-S1-C7
    - P7-S1-C11
    - P7-S2-C7
    - P7-S2-C8
    - P7-S2-C9
    - P7-S3-C8
    - P7-S3-C9
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-4-1
    - TABLE-2-page-4-2
    - TABLE-3-page-6-3
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P4-S2-C2
      recruited_sample:
      - P4-S2-C2
      eligibility:
      - P2-S5-C2
      - P2-S5-C3
      - P3-S1-C1
      - P3-S1-C2
      imaging_provenance:
      - P4-S1-C6
      imaging_timing:
      - P2-S5-C2
      outcome_timing:
      - P2-S5-C2
      outcome_definition:
      - P4-S1-C11
      validation: []
      analysis_restrictions:
      - P5-S1-C3
      - P5-S1-C5
      - P5-S1-C6
      dependent_variable_statement:
      - P4-S1-C11
      - P5-S1-C4
      limitations:
      - P6-S3-C10
      - P7-S4-C2
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P3-S2-C12
      - P5-S1-C3
      - P5-S1-C5
      - P5-S1-C6
      - P5-S3-C7
      - P6-S1-C2
      - P6-S1-C4
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P4-S2-C2
      - P4-S2-C3
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: none_described
    held_selections:
    - slot: validation
      source_id: P4-S1-C12
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
      pdf_sha256: 84a00ab74d2b971ceb854a33aa548a335443cae5658f32e4cc3444237e344e40
      review_sha256: c4a369558853c060aa4c2265d603cef97efe695659c60a271361fed977cacee2
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
      - P5-S2-C8
      - P5-S2-C9
      source_result: Performance on the phonological factor was uniquely correlated
        with a cluster of voxels in the left parietal lobe, with peak voxels in the
        left superior parietal lobe and intraparietal sulcus, including voxels in
        the left inferior parietal lobule. This association was identified using Voxel-Based
        Correlational Morphology (VBCM) correlating PCA factor scores with lesion
        maps, controlling for lesion volume.
      result_status: detected
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis corresponds to the VBCM analysis of the phonological
            PCA factor. The source explicitly states that performance on this factor
            was correlated with tissue damage in the left parietal lobe (P5-S2-C8,
            P5-S2-C9). The method (VBCM) and the specific factor (Phonology, derived
            from word/non-word repetition) match the proposed core.
          source_ids:
          - P5-S2-C8
          - P5-S2-C9
          - P5-S1-C11
          - P4-S1-C11
        direction:
          answer: fits
          reason: The source states a 'unique correlation' between the phonological
            factor and the left parietal cluster. The proposed core describes this
            as a 'likely' association/correlation, which is faithful to the statistical
            finding of a significant correlation without overclaiming causality or
            a specific direction of effect (e.g., damage causes impairment vs. impairment
            localizes to damage) beyond the correlational nature of VBCM.
          source_ids:
          - P5-S2-C8
          - P5-S2-C9
        construct:
          answer: fits
          reason: The exposure is the 'phonological factor' (PCA Factor 1), and the
            outcome is 'tissue damage' (lesion overlap) in the left parietal lobe.
            The patient measurement is correctly identified as template_lesion_overlap
            (VBCM uses lesion maps overlaid on standard space), not patient_diffusion.
            The anatomical locations (left superior parietal, intraparietal sulcus,
            left inferior parietal lobule) match the source text exactly.
          source_ids:
          - P5-S2-C8
          - P5-S2-C9
          - P5-S1-C11
          - P4-S1-C11
        qualifications:
          answer: fits
          reason: The proposed core includes the qualification that the factor was
            one of four orthogonal PCA factors entered simultaneously, which is supported
            by P5-S1-C3 and P5-S1-C4. It also notes control for lesion volume, supported
            by P5-S1-C5 and P5-S1-C6. The limitations regarding small sample size
            (P7-S4-C2) and white matter detection limits (P6-S3-C10) are also included.
          source_ids:
          - P5-S1-C3
          - P5-S1-C4
          - P5-S1-C5
          - P5-S1-C6
          - P7-S4-C2
          - P6-S3-C10
        missing_material_caveat:
          answer: fits
          reason: 'The core includes the key methodological caveats: the use of VBCM
            (which implies lesion overlap), the control for lesion volume, the small
            sample size, and the limitation regarding white matter interpretation.
            No material caveat that changes the interpretation of the left parietal
            phonology association appears to be omitted. The ''unique'' nature of
            the correlation (controlling for other factors) is captured in the qualifications.'
          source_ids:
          - P5-S1-C4
          - P5-S1-C5
          - P7-S4-C2
          - P6-S3-C10
      optional_pending:
      - Specific p-values or cluster sizes for the left parietal cluster are not transcribed
        in the provided source window, but the qualitative association is clear.
      - Exact MNI coordinates for the peak voxels are not transcribed.
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Specific p-values or cluster sizes for the left parietal cluster are not transcribed
      in the provided source window, but the qualitative association is clear.
    - Exact MNI coordinates for the peak voxels are not transcribed.
    normalizations: []
    analysis_identity:
      id: R001
      exposure:
        text: phonological factor
      outcome:
        text: tissue damage in the left parietal lobe (peak in left superior parietal
          lobe and intraparietal sulcus, including left inferior parietal lobule)
      analysis_label: VBCM of PCA factors
      relation: association
      evidence_ids:
      - P5-S2-C8
      - P5-S2-C9
      qualifier_ids:
      - P5-S2-C7
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 84a00ab74d2b971ceb854a33aa548a335443cae5658f32e4cc3444237e344e40
        source_review: _compare/relationships-2026-11-16/review-current/Akkad2023
        source_status_sha256: 15ad6658b87971a6e568f6ae98cd0be730493d4704512aa6376c56a31606b3df
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P2-S4-C13:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 84a00ab74d2b971ceb854a33aa548a335443cae5658f32e4cc3444237e344e40
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: b3894ed65716081e656ea53426688baf088bd8a15459f0767970950aa8621012
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S4-C13
          page: 2
          text_layer_sha256: b3894ed65716081e656ea53426688baf088bd8a15459f0767970950aa8621012
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "Participants \nThirty-six English speakers with chronic aphasia\
          \ following a single \nleft-hemisphere stroke participated in the study\
          \ (see Fig. 1 for a lesion \noverlap map, Table 1 for demographic and clinical\
          \ data)."
        anchor_text: "Participants \nThirty-six English speakers with chronic aphasia\
          \ following a single \nleft-hemisphere stroke participated in the study\
          \ (see Fig. 1 for a lesion \noverlap map, Table 1 for demographic and clinical\
          \ data)."
        excluded_fragments: []
        image_sha256: 389fece24d2b6ee70faf586994c29fcb753c6b172965700250110e1e574166a6
        transcription: 'Participants


          Thirty-six English speakers with chronic aphasia following a single left-hemisphere
          stroke participated in the study (see Fig. 1 for a lesion overlap map, Table
          1 for demographic and clinical data)'
      P2-S5-C2:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 84a00ab74d2b971ceb854a33aa548a335443cae5658f32e4cc3444237e344e40
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: c22156d87c55423ee8bec3fa25951a8c512de06836c10704e946943bf7bd61c7
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S5-C2
          page: 2
          text_layer_sha256: c22156d87c55423ee8bec3fa25951a8c512de06836c10704e946943bf7bd61c7
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "All were at \nleast 12 months post-stroke and at the time\
          \ of scanning and assessment, \nhad normal hearing, normal or corrected-to-normal\
          \ visual acuity and no \nprevious history of significant neurological or\
          \ psychiatric disease."
        anchor_text: "All were at \nleast 12 months post-stroke and at the time of\
          \ scanning and assessment, \nhad normal hearing, normal or corrected-to-normal\
          \ visual acuity and no \nprevious history of significant neurological or\
          \ psychiatric disease."
        excluded_fragments: []
        image_sha256: f86a78ad69cd11503fd200e3e8728974421f5c68a4897a3646b295bf9cf59d94
        transcription: '. All were at

          least 12 months post-stroke and at the time of scanning and assessment,

          had normal hearing, normal or corrected-to-normal visual acuity and no

          previous history of significant neurological or psychiatric disease'
      P2-S5-C3:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 84a00ab74d2b971ceb854a33aa548a335443cae5658f32e4cc3444237e344e40
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: a529458ff71c2cc1b813baa1e6b5a4b69a329131566b1d252408d0c72f28b22f
          exclusions_sha256: 5fe648bf798e45e35af50d85e76b46748988857989a18d036a56c20708c2d1ef
          source_id: P2-S5-C3
          page: 2
          text_layer_sha256: 892452e101b80214e5fd9d651e740427dfee3a21cd548c70e21e5327d8e79eef
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: "In­\nclusion criteria were: (i) anomia as determined by the\
          \ naming subtest of \nthe Comprehensive Aphasia Test (Swinburn et al., 2004);\
          \ (ii) good single \nword comprehension as indexed by an accuracy score>70%\
          \ on the \nspoken word comprehension subtest of the Comprehensive Aphasia\
          \ Test \nH."
        anchor_text: "In­\nclusion criteria were: (i) anomia as determined by the\
          \ naming subtest of \nthe Comprehensive Aphasia Test (Swinburn et al., 2004);\
          \ (ii) good single \nword comprehension as indexed by an accuracy score>70%\
          \ on the \nspoken word comprehension subtest of the Comprehensive Aphasia\
          \ Test "
        excluded_fragments:
        - where: trailing
          text: H.
          furniture_line: 'H. Akkad et al.                                                                                                                                                                                                                                  '
          bbox:
          - 37.6
          - 33.6
          - 501.5
          - 44.1
          rule: repeated margin line
        image_sha256: 01cf613a7d242ee1fd0b2eb95fa60b01417ad1c4ff028f28aec587f57aa2fca6
      P3-S1-C1:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 84a00ab74d2b971ceb854a33aa548a335443cae5658f32e4cc3444237e344e40
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 1b64965855f9819640e9f39fd0d921023bff207b91713484cf99a4fde5243c5b
          exclusions_sha256: 140bc5a6ab19f1e61766389624d50021ed0b006e7f983fe2327d91b5e930f7bc
          source_id: P3-S1-C1
          page: 3
          text_layer_sha256: 8c8de2c86bdd43196a84b5495548b67ed151550be063a6de4b49cdb61e4a4fbf
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "\nNeuroImage: Clinical 39 (2023) 103452\n3\n(Swinburn et al.,\
          \ 2004); (iii) relatively spared ability to repeat single \nmonosyllabic\
          \ words from the Psycholinguistic Assessments of Language \nProcessing in\
          \ Aphasia (Kay, 1992); (iv) absence of speech apraxia as \ndetermined by\
          \ the Apraxia Battery for Adults (Dabul, 2000)."
        anchor_text: "(Swinburn et al., 2004); (iii) relatively spared ability to\
          \ repeat single \nmonosyllabic words from the Psycholinguistic Assessments\
          \ of Language \nProcessing in Aphasia (Kay, 1992); (iv) absence of speech\
          \ apraxia as \ndetermined by the Apraxia Battery for Adults (Dabul, 2000)."
        excluded_fragments:
        - where: leading
          text: 'NeuroImage: Clinical 39 (2023) 103452'
          furniture_line: 'NeuroImage: Clinical 39 (2023) 103452'
          bbox:
          - 448.1
          - 33.7
          - 558.3
          - 44.1
          rule: repeated margin line
        - where: leading
          text: '3'
          furniture_line: '3'
          bbox:
          - 296.2
          - 754.5
          - 299.8
          - 764.9
          rule: repeated margin line
        image_sha256: e49a5749bc59ad14d4fc1c95895f115405034e3b31fa387db53f5f6912f353bc
        transcription: '(Swinburn et al., 2004); (iii) relatively spared ability to
          repeat single

          monosyllabic words from the Psycholinguistic Assessments of Language

          Processing in Aphasia (Kay, 1992); (iv) absence of speech apraxia as

          determined by the Apraxia Battery for Adults (Dabul, 2000)'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 5
  quote: "Performance on the phonological factor was uniquely correlated \nwith a\
    \ cluster of voxels in the left parietal lobe, with peak voxels in the \nleft\
    \ superior parietal lobe and intraparietal sulcus."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-20'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
