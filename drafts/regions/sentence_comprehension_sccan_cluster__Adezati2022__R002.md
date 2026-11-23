---
id: sentence_comprehension_sccan_cluster
name: sentence comprehension cluster
kind: network
findings:
- id: f1
  target: sentence_comprehension_deficit
  target_kind: impairment
  claim: lesions in the posterior superior temporal cortex, inferior frontal gyrus
    pars triangularis, and frontal white matter (superior and anterior corona radiata)
    were associated with sentence comprehension deficits
  direction: likely
  relationship: correlational
  method: LSM
  sample:
    n: 50
    population: participants with aphasia secondary to a single left hemisphere stroke
    phase: not_reported
    time_post_onset: post-stroke
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - small sample size compared to some prior LSM studies
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: patient lesion overlap with a sparse canonical correlation
    analysis (SCCAN) multivariate lesion-symptom mapping model identifying voxels
    in the posterior superior temporal cortex, inferior frontal gyrus pars triangularis,
    and frontal white matter (superior and anterior corona radiata). identified using
    multivariate SCCAN LSM with 4-fold cross-validation; analysis corrected for lesion
    size using direct total lesion volume control (dTLVC); only voxels lesioned in
    at least 10% of participants were included. Additional metadata has not been transcribed;
    review the pending-field flags before approval. PDF image reading (P2-S3-C5, two-model
    agreement, human verification pending): Almost all of the participants included
    in the current study

    were previously included in a lesion-symptom mapping study of se-

    mantic and phonological fluency (Thye et al., 2021).¹


    Prospectively collected Magnetic Resonance Imaging (MRI) and

    psycholinguistic data from 50 participants with aphasia secondary to

    a single left hemisphere stroke were analysed Original text-layer quotation is
    preserved below. PDF image reading (P4-S4-C5, two-model agreement, human verification
    pending): . Note that Lwi et al.

    had a much larger sample size (N = 168) than the present study (N =

    50) Original text-layer quotation is preserved below. Reconcile this new analysis
    with earlier drafts and source-review decisions for the paper; new candidate IDs
    do not carry earlier decisions forward.'
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
    - proposed_concept:sentence_comprehension_deficit
  citation: '@Adezati2022'
  source_passages:
  - section: Original source P4-S2-C12
    page: 4
    quote: "Multivariate SCCAN LSM also identified a relatively sparse \nsolution\
      \ (optimal sparseness = 0.173, CV correlation = 0.55, p <\n0.0001) with suprathreshold\
      \ voxels in posterior superior temporal \ncortex, IFG pars triangularis, and\
      \ frontal white matter (superior and \nanterior corona radiata)."
    supports: claim
  - section: Original source P4-S3-C6
    page: 4
    quote: "The key findings were that \nlesions in the posterior superior temporal\
      \ lobe and IFG pars triangularis \nwere associated with sentence comprehension\
      \ deficits, which was \nobserved in both mass univariate and multivariate LSM."
    supports: claim
  - section: Original source P2-S3-C5
    page: 2
    quote: "Almost all of the participants included in the current study \nwere previously\
      \ included in a lesion-symptom mapping study of se­\nmantic and phonological\
      \ fluency (Thye et al., 2021).1 \nProspectively collected Magnetic Resonance\
      \ Imaging (MRI) and \npsycholinguistic data from 50 participants with aphasia\
      \ secondary to a \nsingle left hemisphere stroke were analysed."
    supports: sample
  - section: Original source P4-S2-C3
    page: 4
    quote: "Multivariate LSM was conducted using SCCAN \nwith 4-fold cross-validation\
      \ to optimise sparseness (Pustina et al., 2018)."
    supports: method
  - section: Original source P4-S1-C14
    page: 4
    quote: "All analyses were also \ncorrected for lesion size using direct total\
      \ lesion volume control (dTLVC) \n(Mirman et al., 2015)."
    supports: confounders
  - section: Original source P4-S1-C13
    page: 4
    quote: "The analyses were corrected for suf­\nficient lesion involvement by only\
      \ including voxels that were lesioned in \nat least 10% of the participants\
      \ (minimum n = 5)."
    supports: method
  - section: Original source P4-S4-C5
    page: 4
    quote: "Note that Lwi et al. \nhad a much larger sample size (N = 168) than the\
      \ present study (N =\n50)."
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-20'
relationship_review:
  paper: Adezati2022
  proposal_id: R002
  review_status_sha256: a811e7d28f3da67aec2623d368ac07797e6704395c2892e521b2a60a57b53f62
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: c3b862039f6071dd869b806ed04e339c905c23d11d3d903d1cbe6fb4f89a977c
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: c3b862039f6071dd869b806ed04e339c905c23d11d3d903d1cbe6fb4f89a977c
        A/passages.json: 11886d409d20fec61ee25b3d2a3b217d6161dab2fb909d04b4725a8ce719fa2c
        A/raw.json: 875e02cdc21fa9faa82b14be2b740f0a5900c620baf707de4a551a1a9ce97ae4
        A/source-units.json: dc132f8035b4a438c6094f09d3d9faa7d2a541791629dc0841734785c424c34c
        A/full-source-units.json: 62f4829a973a56a478e615824577219549191ee62485f6993247fb91b4e5a134
        A/meta.json: 516a720ef4c4c49835892d23edb5467b6af34a06fdcbf4398054866367771742
        A/table-images/page-3.png: f440b5f57da726bd095636ab776dd0481910933423bf83c2dd313c6a108f4164
        A/table-images/TABLE-1-page-2-1.png: 6da7f6ef0293c8b503ac46cce4f0eeceb314eb3ae7767df2edc53ce733b849d6
        A/table-images/page-2.png: 879c362f5bcfd72563c228a3a1e9da352e6aa7183dc49e7b8da4ac0e5d6c4294
        A/table-images/page-5.png: 95d94cacf3c18db4995c8b978dd760e2fe0d2b62b7558aaed61d84db93df29c9
        A/table-images/manifest.json: 9b54abb50076bb307a14e0727c3fe4e3e15893b9bc176a9eff433ddff6d8277a
        A/table-images/TABLE-2-page-3-1.png: ab9e23386d490f88e8908b6ad68023dcff503ca7e9701de1b1bf43631b1f7f79
        A/table-images/TABLE-3-page-5-1.png: 10169c8e6feca22388ee6ef5104f002a9e6c1d31a39a0d204a9d2fc0274fdb8b
        A/clauses/window-03/raw.json: 86bb54f8c9d1594907a406440ef958041b7eec0347a32703c9f139ab85792780
        A/clauses/window-03/prompt.txt: 25c24d5474ea15f0fec4f28128f4ae3f5b49e9f13d106ec505cf3a19bc131f62
        A/clauses/window-03/meta.json: aba1b67ab3b80a23a4a53e4c825259fd06caecd49fb5d19af44e99935eae12d0
        A/clauses/window-04/raw.json: 645a88aa6567f07d83c57a124a160dbd11f3ed16d08cc68c73dd208f5535824d
        A/clauses/window-04/prompt.txt: 3b6af5e44f7926fe60fe8d8b0a0891a0975672650dec7661cf0db168c3a8e9c1
        A/clauses/window-04/meta.json: 281696fc3fc55e12d4ffda4feeabdb2b39180c78b80a3c699de493a346d22fb5
        A/clauses/window-05/raw.json: b3e1dc57f1c38dc4e820057033287759a796eaeb7dd938ce4cf5896f59ffc67a
        A/clauses/window-05/prompt.txt: 6606cf9a3602a7f7fa85e3a307d0851bf2cbc5ab8ed65eeabcf2ceb3c1951a5d
        A/clauses/window-05/meta.json: 48a7701617839b9208ce2ea712d6ac8d19d85cd66182de1340d25ed827514d9d
        A/clauses/window-02/raw.json: c3e2b2926b3c9a4ce9673b2d23962fc3b767bfce00607f89665606a1f4c616ae
        A/clauses/window-02/prompt.txt: af05a03f57469d17d3e0caa1ba734ea1e24634266b9b602378518193df8c586e
        A/clauses/window-02/meta.json: 8452721adf7449f7df60359a18026ff61d213c604705ddcc6a1aae24cf261e3b
        A/clauses/window-01/raw.json: ff34618267db999b6059a0f3baa09834c3f5d29114c98e62277a65a87a757650
        A/clauses/window-01/prompt.txt: 208cd2889926074f26b673d244d95d0ff90952b781ac34aff326fbc78ccd8495
        A/clauses/window-01/meta.json: 4ed94910bb7381534ba7f55d7a457ac19c7f744760a27df95d3472b6c093e36a
        A/tables/TABLE-3-page-5-3/raw.json: 8c68152a0b7759458a61bc174b1dd20190ed2b528753f5f2fecf1852e6b8e736
        A/tables/TABLE-3-page-5-3/prompt.txt: 6333dea07d7faee3d9fcb0c2aba20ba619545215d76a308d4b835d26d8f7e1c5
        A/tables/TABLE-3-page-5-3/meta.json: 552a747f9b044df1942861c2648354cfeb6e70b9efb2d21fb93c3037428c8636
        A/tables/TABLE-1-page-2-1/raw.json: e5bffed55cf67e23914cc9c4e01a2969de01311866a25e8d731875f603e8a5b5
        A/tables/TABLE-1-page-2-1/prompt.txt: b3f4828a5ba8053f0ad9c017491daaaf8074171e140c4adf01e5473a1d7f5c4a
        A/tables/TABLE-1-page-2-1/meta.json: a128cce801a25262fd28629fd8bd88c9ecce3f787dd0856c67d95cdb96b2e465
        A/tables/TABLE-2-page-3-2/raw.json: 1a423f72e175a065da8b9d4434a2336318874ac83558561af4273b58e93e1782
        A/tables/TABLE-2-page-3-2/prompt.txt: e30b0c9a30ecde0a3d7ad2a79690785571fc91f2639d85509700cd4f12a833d2
        A/tables/TABLE-2-page-3-2/meta.json: 2181e063543da1b09f82d0edcf9582425441ee821bf4dee2a5350c7badfe0ba9
        B/passages.json: 11886d409d20fec61ee25b3d2a3b217d6161dab2fb909d04b4725a8ce719fa2c
        B/raw.json: 1d79be72a44812962b7eaf6a621ca0b58489315b862a0ad7155f4310feeaab9a
        B/source-units.json: dc132f8035b4a438c6094f09d3d9faa7d2a541791629dc0841734785c424c34c
        B/full-source-units.json: 62f4829a973a56a478e615824577219549191ee62485f6993247fb91b4e5a134
        B/meta.json: 050839df919f2d0b9bc275adf0442ee1d15f6133f4634ccd38de0243065d494e
        B/table-images/page-3.png: f440b5f57da726bd095636ab776dd0481910933423bf83c2dd313c6a108f4164
        B/table-images/TABLE-1-page-2-1.png: 6da7f6ef0293c8b503ac46cce4f0eeceb314eb3ae7767df2edc53ce733b849d6
        B/table-images/page-2.png: 879c362f5bcfd72563c228a3a1e9da352e6aa7183dc49e7b8da4ac0e5d6c4294
        B/table-images/page-5.png: 95d94cacf3c18db4995c8b978dd760e2fe0d2b62b7558aaed61d84db93df29c9
        B/table-images/manifest.json: dd4fdf0899bcfe45df5699a97e39cd459d7c07049b05df77b065ccd9778b2c8e
        B/table-images/TABLE-2-page-3-1.png: ab9e23386d490f88e8908b6ad68023dcff503ca7e9701de1b1bf43631b1f7f79
        B/table-images/TABLE-3-page-5-1.png: 10169c8e6feca22388ee6ef5104f002a9e6c1d31a39a0d204a9d2fc0274fdb8b
        B/clauses/window-03/raw.json: e6aab6ab6990f763ca11e70d90977c8910efbaa16df0769d1770368781feebaa
        B/clauses/window-03/prompt.txt: 25c24d5474ea15f0fec4f28128f4ae3f5b49e9f13d106ec505cf3a19bc131f62
        B/clauses/window-03/meta.json: 3ccf684a2411d00eb8df052ac8d42f396c8b0a1026759ce7e53f040a2f1dae93
        B/clauses/window-04/raw.json: 3578bbd0ab7a43530cc60a505d666624cae34626104933cb84a85e338b69ff1a
        B/clauses/window-04/prompt.txt: 3b6af5e44f7926fe60fe8d8b0a0891a0975672650dec7661cf0db168c3a8e9c1
        B/clauses/window-04/meta.json: ed6d76ca3e8886c02f82e4e2fb50cacd3acbd11b36a936ff2e21cb4d7414074f
        B/clauses/window-05/raw.json: 46fc38a3ecae10df4314817de0a59728dd3819e25b77ca3f122504f6bed1a9d3
        B/clauses/window-05/prompt.txt: 6606cf9a3602a7f7fa85e3a307d0851bf2cbc5ab8ed65eeabcf2ceb3c1951a5d
        B/clauses/window-05/meta.json: 2417c1047dcefede7ca9ef583ec18b0589488d431a389fd23802d7aafa5b430d
        B/clauses/window-02/raw.json: 99e3ba3dc7c906143d60b00bb18424e6925ad4cb97557de423e9c140f4ce6c6c
        B/clauses/window-02/prompt.txt: af05a03f57469d17d3e0caa1ba734ea1e24634266b9b602378518193df8c586e
        B/clauses/window-02/meta.json: 5082635e5b8e7abd70f23248340a2b89390205c1ef0290fc6aa08fb409cf4fe1
        B/clauses/window-01/raw.json: e83852410738a262c4b2d19f8f49ed10cfe11bd5aee9d5071da59c74891d34e2
        B/clauses/window-01/prompt.txt: 208cd2889926074f26b673d244d95d0ff90952b781ac34aff326fbc78ccd8495
        B/clauses/window-01/meta.json: 42565868ee9cde8cc56f07ec77487f21f3619ceb7191521935216b41038937ff
        B/tables/TABLE-3-page-5-3/raw.json: 8c68152a0b7759458a61bc174b1dd20190ed2b528753f5f2fecf1852e6b8e736
        B/tables/TABLE-3-page-5-3/prompt.txt: 6333dea07d7faee3d9fcb0c2aba20ba619545215d76a308d4b835d26d8f7e1c5
        B/tables/TABLE-3-page-5-3/meta.json: f7eaff1435bfeeceba58be43c9162038a01e44404f13e4dc322772146bf1393e
        B/tables/TABLE-1-page-2-1/raw.json: 18048d806bc59d502ab708d79ca2d35e16dffd20e60b166fa10cbeede7c1ffad
        B/tables/TABLE-1-page-2-1/prompt.txt: b3f4828a5ba8053f0ad9c017491daaaf8074171e140c4adf01e5473a1d7f5c4a
        B/tables/TABLE-1-page-2-1/meta.json: 8eebc3495cd60f0ec4d237928633ff3bf216f7187ba92a66e7217065180eda0d
        B/tables/TABLE-2-page-3-2/raw.json: 98c83c68830388b1b5124a7da4a9cfe62c6ace5eef60d98fe24d4265b2bfd31c
        B/tables/TABLE-2-page-3-2/prompt.txt: e30b0c9a30ecde0a3d7ad2a79690785571fc91f2639d85509700cd4f12a833d2
        B/tables/TABLE-2-page-3-2/meta.json: 2f0f4b1d24581380c909c73379a4ff4abf8ca5b6e9a2874cca508ed7222220d8
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
      pdf_sha256: c3b862039f6071dd869b806ed04e339c905c23d11d3d903d1cbe6fb4f89a977c
      source_review: _compare/relationships-2026-11-16/review-current/Adezati2022
      source_status_sha256: 1c4071d2a004c4126d6c5926369e50d5c24aff88f81e7f416a4fa65d3fc71a81
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R002
    exposure:
      text: lesions in posterior superior temporal cortex, IFG pars triangularis,
        and frontal white matter (superior and anterior corona radiata)
    outcome:
      text: sentence comprehension deficits
    analysis_label: multivariate SCCAN LSM
    relation: association
    evidence_ids:
    - P1-S1-C8
    - P4-S2-C12
    - P4-S3-C6
    qualifier_ids:
    - P4-S2-C3
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: c3b862039f6071dd869b806ed04e339c905c23d11d3d903d1cbe6fb4f89a977c
      source_review: _compare/relationships-2026-11-16/review-current/Adezati2022
      source_status_sha256: 1c4071d2a004c4126d6c5926369e50d5c24aff88f81e7f416a4fa65d3fc71a81
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Accounting without a linked unit P4-S2-C11
      - Accounting without a linked unit P4-S2-C12
      - Unaccounted source passage P4-S2-C12
      - Unaccounted source passage P4-S2-C11
      - Result passage disposed without unit P4-S4-C11
      - Accounting without a linked unit P4-S4-C7
      - 'window 5: invalid/duplicate disposition P4-S4-C8'
      - Unaccounted source passage P4-S4-C7
      unattached_null_or_qualifier_ids:
      - P4-S3-C11
      suppressed_nonrepresented_units: 10
      default_disposition_count_requires_completeness_check: 108
      unselected_timing_passages: []
      personal_effect_slots_without_result_classification: []
      held_frame_selections: []
      empty_frame_slots_require_confirmation:
      - personal_factors
      - tested_personal_effects
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-2-1
      - TABLE-2-page-3-2
      - TABLE-3-page-5-3
      unlinked_tables:
      - TABLE-2-page-3-2
      - TABLE-3-page-5-3
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P3-S1
        - P3-S3
        - P3-S4
        - P4-S2
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: c3b862039f6071dd869b806ed04e339c905c23d11d3d903d1cbe6fb4f89a977c
      source_review: _compare/relationships-2026-11-16/review-current/Adezati2022
      source_status_sha256: 1c4071d2a004c4126d6c5926369e50d5c24aff88f81e7f416a4fa65d3fc71a81
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C8
      disposition: represented
      result_indexes:
      - 0
      - 1
      reason: States association of posterior superior temporal lobe and IFG pars
        triangularis with deficits in both mass univariate and multivariate LSM.
    - source_id: P1-S1-C9
      disposition: represented
      result_indexes:
      - 3
      reason: States graph theoretic measures were not significantly associated with
        deficits after accounting for lesion size.
    - source_id: P2-S4-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes lack of correlation between time since stroke and Token Test
        performance.
    - source_id: P4-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Introduces the LSM results section.
    - source_id: P4-S2-C11
      disposition: represented
      result_indexes:
      - 0
      reason: Identifies suprathreshold voxels in posterior superior temporal lobe
        and IFG pars triangularis via mass-univariate VLSM.
    - source_id: P4-S2-C12
      disposition: represented
      result_indexes:
      - 1
      reason: Identifies suprathreshold voxels in posterior superior temporal cortex,
        IFG pars triangularis, and frontal white matter via SCCAN LSM.
    - source_id: P4-S2-C13
      disposition: represented
      result_indexes:
      - 2
      reason: Reports overall lesion volume as a statistically significant effect
        in connectivity regressions.
    - source_id: P4-S3-C2
      disposition: represented
      result_indexes:
      - 2
      reason: Confirms overall lesion volume as the only significant effect in connectivity
        disruption regressions.
    - source_id: P4-S3-C3
      disposition: represented
      result_indexes:
      - 3
      reason: States graph theory metrics were not significant predictors of Token
        Test performance.
    - source_id: P4-S3-C6
      disposition: represented
      result_indexes:
      - 0
      - 1
      reason: Restates association of posterior superior temporal lobe and IFG pars
        triangularis with deficits in both LSM methods.
    - source_id: P4-S3-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discusses correlation between frontal and temporal damage.
    - source_id: P4-S3-C9
      disposition: represented
      result_indexes:
      - 3
      reason: Restates that graph theoretic measures were not significantly associated
        with deficits after accounting for lesion size.
    - source_id: P4-S3-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Compares results to Lwi et al. (2021).
    - source_id: P4-S4-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discusses lack of involvement of anterior temporal regions.
    - source_id: P4-S4-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discusses lack of involvement of inferior parietal regions.
    - source_id: P4-S4-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Interprets critical regions as associated with speech perception, WM,
        and semantic control.
    - source_id: P4-S4-C11
      disposition: repeated
      result_indexes:
      - 0
      - 1
      reason: Restates the critical role of posterior superior temporal and inferior
        frontal regions.
    - source_id: P4-S4-C12
      disposition: repeated
      result_indexes:
      - 3
      reason: Restates caution regarding use of connectome disruption measures.
    unresolved_coverage: []
    pending_source_ids:
    - P2-S4-C2
    - P4-S2-C10
    - P4-S2-C13
    - P4-S3-C7
    - P4-S3-C11
    - P4-S4-C6
    - P4-S4-C7
    - P4-S4-C8
    - P4-S4-C11
    - P4-S4-C12
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-2-1
    - TABLE-2-page-3-2
    - TABLE-3-page-5-3
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P2-S3-C5
      recruited_sample:
      - P2-S3-C5
      eligibility:
      - P2-S3-C5
      imaging_provenance:
      - P3-S1-C6
      imaging_timing:
      - P2-S3-C5
      outcome_timing:
      - P2-S3-C5
      outcome_definition:
      - P2-S3-C8
      validation:
      - P4-S2-C3
      analysis_restrictions:
      - P3-S3-C15
      - P4-S1-C13
      dependent_variable_statement:
      - P4-S2-C7
      - P4-S2-C9
      limitations:
      - P4-S4-C4
      - P4-S4-C6
      - P4-S4-C7
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P4-S1-C14
      - P4-S2-C9
      explicitly_not_adjusted:
      - P2-S4-C2
      descriptive_personal_factors:
      - P2-S4-C4
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: internal_cross_validation
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
      pdf_sha256: c3b862039f6071dd869b806ed04e339c905c23d11d3d903d1cbe6fb4f89a977c
      review_sha256: a811e7d28f3da67aec2623d368ac07797e6704395c2892e521b2a60a57b53f62
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
      - P1-S1-C8
      - P4-S2-C12
      - P4-S3-C6
      source_result: Multivariate SCCAN LSM identified a sparse solution (optimal
        sparseness = 0.173, CV correlation = 0.55, p < 0.0001) with suprathreshold
        voxels in posterior superior temporal cortex, IFG pars triangularis, and frontal
        white matter (superior and anterior corona radiata) associated with sentence
        comprehension deficits. This finding was observed in both mass univariate
        and multivariate LSM. The analysis was corrected for lesion size using direct
        total lesion volume control (dTLVC) and restricted to voxels lesioned in at
        least 10% of participants.
      result_status: detected
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis is the multivariate SCCAN LSM. The source
            (P4-S2-C12) explicitly describes this method and its results. The draft
            correctly identifies this as the core relationship, distinct from the
            mass-univariate VLSM or the connectivity regressions.
          source_ids:
          - P4-S2-C12
          - P4-S2-C3
        direction:
          answer: fits
          reason: The source states that lesions in these regions were 'associated
            with sentence comprehension deficits' (P1-S1-C8, P4-S3-C6). The draft
            claims an association with deficits, which aligns with the detected positive
            association between lesion presence and symptom severity (deficit).
          source_ids:
          - P1-S1-C8
          - P4-S3-C6
        construct:
          answer: fits
          reason: 'Exposure: Lesions in posterior superior temporal cortex, IFG pars
            triangularis, and frontal white matter (superior and anterior corona radiata).
            This matches P4-S2-C12 exactly. Outcome: Sentence comprehension deficits,
            measured by Token Test. This matches P2-S3-C8 and P1-S1-C8. Method: Multivariate
            SCCAN LSM. This matches P4-S2-C3. Patient measurement is template_lesion_overlap
            as the analysis uses lesion masks overlaid on a stereotaxic space (Colin27/MNI)
            to identify voxels, not patient-specific diffusion tractography for the
            primary LSM result.'
          source_ids:
          - P4-S2-C12
          - P2-S3-C8
          - P4-S2-C3
          - P3-S1-C3
        qualifications:
          answer: fits
          reason: 'The draft includes the key methodological qualifiers: multivariate
            SCCAN with 4-fold cross-validation (P4-S2-C3), correction for lesion size
            via dTLVC (P4-S1-C14), and the 10% lesion frequency threshold (P4-S1-C13).
            These are present in the source and correctly applied to the analysis.'
          source_ids:
          - P4-S2-C3
          - P4-S1-C14
          - P4-S1-C13
        missing_material_caveat:
          answer: fits
          reason: The draft notes the small sample size (N=50) as a limitation, which
            is explicitly mentioned in P4-S4-C5. No other material caveats that would
            change the interpretation of the association are omitted. The distinction
            between this result and the null connectivity result is maintained by
            focusing on the LSM finding.
          source_ids:
          - P4-S4-C5
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
      id: R002
      exposure:
        text: lesions in posterior superior temporal cortex, IFG pars triangularis,
          and frontal white matter (superior and anterior corona radiata)
      outcome:
        text: sentence comprehension deficits
      analysis_label: multivariate SCCAN LSM
      relation: association
      evidence_ids:
      - P1-S1-C8
      - P4-S2-C12
      - P4-S3-C6
      qualifier_ids:
      - P4-S2-C3
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: c3b862039f6071dd869b806ed04e339c905c23d11d3d903d1cbe6fb4f89a977c
        source_review: _compare/relationships-2026-11-16/review-current/Adezati2022
        source_status_sha256: 1c4071d2a004c4126d6c5926369e50d5c24aff88f81e7f416a4fa65d3fc71a81
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P2-S3-C5:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: c3b862039f6071dd869b806ed04e339c905c23d11d3d903d1cbe6fb4f89a977c
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: a5ae4df48ffd1f58a0630974e1380c7f46f3d86e1a3cffceabbc1f785e5a1b19
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S3-C5
          page: 2
          text_layer_sha256: a5ae4df48ffd1f58a0630974e1380c7f46f3d86e1a3cffceabbc1f785e5a1b19
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "Almost all of the participants included in the current study\
          \ \nwere previously included in a lesion-symptom mapping study of se­\n\
          mantic and phonological fluency (Thye et al., 2021).1 \nProspectively collected\
          \ Magnetic Resonance Imaging (MRI) and \npsycholinguistic data from 50 participants\
          \ with aphasia secondary to a \nsingle left hemisphere stroke were analysed."
        anchor_text: "Almost all of the participants included in the current study\
          \ \nwere previously included in a lesion-symptom mapping study of se­\n\
          mantic and phonological fluency (Thye et al., 2021).1 \nProspectively collected\
          \ Magnetic Resonance Imaging (MRI) and \npsycholinguistic data from 50 participants\
          \ with aphasia secondary to a \nsingle left hemisphere stroke were analysed."
        excluded_fragments: []
        image_sha256: af92d4075a8eff6e737ffc9639789910aab33f56da465de84483ec537e7d05b2
        transcription: 'Almost all of the participants included in the current study

          were previously included in a lesion-symptom mapping study of se-

          mantic and phonological fluency (Thye et al., 2021).¹


          Prospectively collected Magnetic Resonance Imaging (MRI) and

          psycholinguistic data from 50 participants with aphasia secondary to

          a single left hemisphere stroke were analysed'
      P4-S4-C5:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: c3b862039f6071dd869b806ed04e339c905c23d11d3d903d1cbe6fb4f89a977c
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 2e785d6c405246d8d375799a8ddac1fd9b78c91c788ff1161a73df5f2532e89b
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P4-S4-C5
          page: 4
          text_layer_sha256: 2e785d6c405246d8d375799a8ddac1fd9b78c91c788ff1161a73df5f2532e89b
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "Note that Lwi et al. \nhad a much larger sample size (N =\
          \ 168) than the present study (N =\n50)."
        anchor_text: "Note that Lwi et al. \nhad a much larger sample size (N = 168)\
          \ than the present study (N =\n50)."
        excluded_fragments: []
        image_sha256: 5801504b3ce9ade3bd2b97a6080aa9e975126cd2d59792ffdd93b5e91d492c71
        transcription: '. Note that Lwi et al.

          had a much larger sample size (N = 168) than the present study (N =

          50)'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 4
  quote: "Multivariate SCCAN LSM also identified a relatively sparse \nsolution (optimal\
    \ sparseness = 0.173, CV correlation = 0.55, p <\n0.0001) with suprathreshold\
    \ voxels in posterior superior temporal \ncortex, IFG pars triangularis, and frontal\
    \ white matter (superior and \nanterior corona radiata)."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-20'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
