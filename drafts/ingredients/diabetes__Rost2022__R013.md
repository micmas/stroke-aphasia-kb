---
id: diabetes
name: diabetes
kind: ingredient
findings:
- id: f1
  target: brain_infarcts
  target_kind: impairment
  claim: Rost2022 reports, based on the autopsy study cited as reference 68, that diabetes increased the odds of brain infarcts, particularly lacunes, but not Alzheimer disease pathology
  direction: likely
  relationship: synthesis
  method: narrative_review
  sample:
    n: not_reported
    population: 'Participants in the studies summarized by Rost2022; this record is a secondary review report, not a newly recruited cohort. Primary source: the autopsy study cited as reference 68.'
    phase: not_reported
    time_post_onset: Varies across reviewed studies; see cited primary study and source passages.
  statistics:
    threshold: not_applicable_review_synthesis
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - finding based on neuropathological analysis of autopsied patients
  evidence_quality: narrative-review
  strength: weak
  notes: 'Reclassified as a secondary review report, explicitly attributing the result to the autopsy study cited as reference 68. This is not a new primary sample or independent replication; quantitative estimates and study-level attribution require human verification against the primary publication. Source repair (unapproved): Reclassified as a secondary review report, explicitly attributing the result to the autopsy study cited as reference 68. This is not a new primary sample or independent replication; quantitative estimates and study-level attribution require human verification against the primary publication.'
  imaging_details:
    reference_space: not_applicable
    atlases_used: []
  lesion_mapping: {}
  provenance:
    extracted_by: agent:source-repair
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
    - not_transcribed:sample.n
    - proposed_concept:brain_infarcts
    - agent_source_repair_pending_human_review
  citation: '@Rost2022'
  source_passages:
  - section: Original source P5-S3-C3
    page: 5
    quote: "For instance, a neuropatho-\nlogical analysis of more than 1.300 autopsied patients \nwith diabetes found that diabetes increased the odds \nof brain infarcts, particularly lacunes, but not Alzheimer \ndisease (AD) pathology.68 As detailed below, the burden \n\n"
    supports: claim
  - section: Original source P5-S3-C3
    page: 5
    quote: "For instance, a neuropatho-\nlogical analysis of more than 1.300 autopsied patients \nwith diabetes found that diabetes increased the odds \nof brain infarcts, particularly lacunes, but not Alzheimer \ndisease (AD) pathology.68 As detailed below, the burden \n\n"
    supports: sample
  - section: Original source P5-S3-C3
    page: 5
    quote: "For instance, a neuropatho-\nlogical analysis of more than 1.300 autopsied patients \nwith diabetes found that diabetes increased the odds \nof brain infarcts, particularly lacunes, but not Alzheimer \ndisease (AD) pathology.68 As detailed below, the burden \n\n"
    supports: method
  design: narrative-review
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-25'
relationship_review:
  paper: Rost2022
  proposal_id: R013
  approved: false
  original_core_review:
    paper: Rost2022
    proposal_id: R013
    review_status_sha256: 21b4b527693cef6f9f990166a0152d64c2a417f65c0623da8a7ddf6181f62e7b
    review_binding:
      version: candidate-inventory-v1
      input_hashes:
        pdf: 3f10b8323077805b1b142ba70865bc674ad2c3377da82ca8ab9439a559cb1672
      original_review_binding:
        version: relationship-review-v4
        input_hashes:
          pdf: 3f10b8323077805b1b142ba70865bc674ad2c3377da82ca8ab9439a559cb1672
          A/passages.json: 146968a218ac779f968b33bee6f2d2d60a2e0598c8a9fae23c4fbf324237d975
          A/raw.json: ff3e067d0eb830d74dcba7e252d112891865c8fe7c020570532f2ed88594da3d
          A/source-units.json: 924df3501e60f90a791eb3fa9b3d0fcc1e43dd488b6b62a7f940ac4e47b15e56
          A/full-source-units.json: f9960516c14dad2ec119d4e3417afaa848ebff83be4adbfb0ed7f25d9c8efe1d
          A/meta.json: ecae46ae95dbabf6183d11dccb4f38c7cd88a4e598e6fadc5a68bb746381ac12
          A/table-images/TABLE-1-page-3-1.png: 493983cd0c93b87394647e7da633fb28abbcbe22bb22becc144116b83908c043
          A/table-images/TABLE-3-page-10-1.png: 664d66d2b8ebbe147c7acf2b58f6ccf12fb40addb3fb9f34deade7d4526ac366
          A/table-images/page-10.png: 43b425b45a0c5ce37efe53981601c213b12cde68a77fa9c19fb1ac9846e533b5
          A/table-images/page-11.png: 7fee21107c91a8e07a8c9bb7d6750c3fd16317130a6e882e92132dc2cc6bdc58
          A/table-images/TABLE-2-page-8-1.png: a74a9ff22ddc8d1612b52bd591b6293bfc10d7edd5b8ab30aff785f1cbf55b20
          A/table-images/page-3.png: 1ce2f13ccc70f15d8ce64ffb12e1310b1bcb5d08009da2049812e88fb83fe422
          A/table-images/TABLE-4-page-11-1.png: bd53aeba54091b6bfcf3298403e68834ca03e6b3fa872cb3dd6150565a0de7d2
          A/table-images/page-8.png: 3abb7b67733575626e8a4b6c90b16ac78abfe19d159b98b7fa0c4927722a5e3f
          A/table-images/manifest.json: cebd0074423388d34a11ed664632334a602fdc62c083cd373aa6893532bb2a3b
          A/clauses/window-03/raw.json: 8f08bf5bc441ac00197a257abc555328714356ce9acd3f4d1f40793df95f850e
          A/clauses/window-03/prompt.txt: 0f6f1657e4d34cffb05a0311d4bc942f45a83428638d8286375cc5bd3824f416
          A/clauses/window-03/meta.json: 65cbf852829d4901f2207341f34d5126c1e593b9acdbbb31c9505ef6aee9555c
          A/clauses/window-04/raw.json: ad6da6cff35b0e7771345d1a6f14ae2e33896f8ad4dd13bb9ea83a5770bffdf8
          A/clauses/window-04/prompt.txt: fab3e3cd054a52c0ba68417ae3412963c2e5d7138e96a5caacf313523b519839
          A/clauses/window-04/meta.json: 35d933950f728ade0fe5d92395a4cd42ff01eface743d17ba31460a85fb5cf3e
          A/clauses/window-05/raw.json: 29efcd9120daa8da42b65ff5c7b142c632d404062e33a400a7c8089fa7a8696d
          A/clauses/window-05/prompt.txt: aa64f8dc30dbee387ae04b815590724b7613df20cddde885e83fd79c9cd2f085
          A/clauses/window-05/meta.json: 1ab84f0fa8a122ed858b551893d3f0fe2afe0fe684ba349670e772852f120ae5
          A/clauses/window-02/raw.json: dd7b9cb699f2536d0eab9a9623ec15fbd9b81bd3b05e4f16e8f85d383d1bc936
          A/clauses/window-02/prompt.txt: 18a427fa4b8bfeb761f00ff82ccb37de74d53778e56623b4a5fbe0d7d5f9e1c0
          A/clauses/window-02/meta.json: 0e9e492750f8323cb7a10918e95d617bfdd554d6330f5e6badfe5fedd7059c8f
          A/clauses/window-09/raw.json: ec7d91edd153628200ea997fd41a3165f941f5ea329d2160d9b1564138f24c9c
          A/clauses/window-09/prompt.txt: 9010d9a7400d1178038209b04187575026974acb749755c7991d4910db3c1806
          A/clauses/window-09/meta.json: 75c409967db11a72667484ea27a3b026e6a8787ddd31481383e24861dcd86eff
          A/clauses/window-07/raw.json: 722bf6eb3a6e80e9f3c04ccc9a60bdf36fc7fe09d12639b9cd59deed6c319ab5
          A/clauses/window-07/prompt.txt: 4009e422b0844097737669b3fcc9b4cdd4ec6de721948355bba1a7929c9bcc94
          A/clauses/window-07/meta.json: 2af5bd77730cd55951f9cd6f048f5cc9d05013ac3532ab13fd1e55f6854589f1
          A/clauses/window-01/raw.json: ef67fa6fe9663edf7c878a8dc794e9c971835fcbc0913f79a4f45a4197e53846
          A/clauses/window-01/prompt.txt: da1a092248e5783328cf6d80b5ed778b928eb83f105e5c3543788fdf28e3d0e3
          A/clauses/window-01/meta.json: 372c6beb493f58a468e3469682c8de5b1f313bd65b33e50647070a18b9938648
          A/clauses/window-06/raw.json: c2d2872827839c5903ab026742330e0d43663f79af70aa0504bf13392c4878c3
          A/clauses/window-06/prompt.txt: 8de15e1a50d28c7bcfc5bb5ea0b0dd90080e2aff2c71e08a47536a78a2950fcd
          A/clauses/window-06/meta.json: d4a2216a6cb612ca7ed49bf9437dba6124c1229f06569e6b167f76138aacb8f1
          A/clauses/window-08/raw.json: 245d9b9c2ae776f00bf56def36152bf2b1dddd8f57b7894b7f8d5a8bda4dcace
          A/clauses/window-08/prompt.txt: 33918747b8744713912dc222a4d3192c553c2005298ee681f972144205c374bb
          A/clauses/window-08/meta.json: b10a2e0a3744e7c366a039eeb59719f0a8144d6bc11c1f618dd82d9c9f05e81a
          A/tables/TABLE-4-page-11-4/raw.json: c416c8ac25bebe71d5b92dd70cf60db25dffa9811f17601b93dcc308de5691cb
          A/tables/TABLE-4-page-11-4/prompt.txt: 75e33dec845cd6194c337c1ffb32f323c8cd8140b31b16e7aa5585a035954a95
          A/tables/TABLE-4-page-11-4/meta.json: 9af225ff1d1aacf8e8ebe17727135089a3c52af8dff6f8b58e3b34e96ad41f4b
          A/tables/TABLE-2-page-8-2/raw.json: bcefc5c6f7d16c5a792d45b300b1b8fef6472cfb7b697e926635ba5e0f127be7
          A/tables/TABLE-2-page-8-2/prompt.txt: 471f23dfe56b757f01480b1396085f647d139763c3e89f7316c0f32630f665d4
          A/tables/TABLE-2-page-8-2/meta.json: 2275694ac96cf2048ba5da4684d85fa64b0fd93574f5bc3d15876507f0917077
          A/tables/TABLE-3-page-10-3/raw.json: dbeee60dd070252f91d1bd4ee9ab0baa0ea13cb8f43e8bdb5f0fc5c62b826479
          A/tables/TABLE-3-page-10-3/prompt.txt: 2f0b3b63e408f1ee3f1520275ad2e15f3f2a205fb85df05f0ae1482fe00010c5
          A/tables/TABLE-3-page-10-3/meta.json: 17eec2f5e3a0ea125a671139d8255c70f72da6c881092e3326164b8d75d5c37d
          A/tables/TABLE-1-page-3-1/raw.json: 5efce61cfb5a04440e240181d72edcac759c569b05a61a2214f29cb47fe0196f
          A/tables/TABLE-1-page-3-1/prompt.txt: 7dbb68ba3c82d143200926f372928db37cfa4a95eafa3ea8c46e70da7f236a7e
          A/tables/TABLE-1-page-3-1/meta.json: 0c2d1dbab6792f349d46830e20aa23b8aba2d0dd73bd81b268faec4b2750c9d3
          B/passages.json: 146968a218ac779f968b33bee6f2d2d60a2e0598c8a9fae23c4fbf324237d975
          B/raw.json: 0e43e2f0032526471635e6a8d3f0a96ab422e509e8669631aa58e44d87f1c0b7
          B/source-units.json: 924df3501e60f90a791eb3fa9b3d0fcc1e43dd488b6b62a7f940ac4e47b15e56
          B/full-source-units.json: f9960516c14dad2ec119d4e3417afaa848ebff83be4adbfb0ed7f25d9c8efe1d
          B/meta.json: 03c7f4748f89710094fd91ee3435400c7a3a402fe0dbaa43b7d67b4a00d61ac5
          B/table-images/TABLE-1-page-3-1.png: 493983cd0c93b87394647e7da633fb28abbcbe22bb22becc144116b83908c043
          B/table-images/TABLE-3-page-10-1.png: 664d66d2b8ebbe147c7acf2b58f6ccf12fb40addb3fb9f34deade7d4526ac366
          B/table-images/page-10.png: 43b425b45a0c5ce37efe53981601c213b12cde68a77fa9c19fb1ac9846e533b5
          B/table-images/page-11.png: 7fee21107c91a8e07a8c9bb7d6750c3fd16317130a6e882e92132dc2cc6bdc58
          B/table-images/TABLE-2-page-8-1.png: a74a9ff22ddc8d1612b52bd591b6293bfc10d7edd5b8ab30aff785f1cbf55b20
          B/table-images/page-3.png: 1ce2f13ccc70f15d8ce64ffb12e1310b1bcb5d08009da2049812e88fb83fe422
          B/table-images/TABLE-4-page-11-1.png: bd53aeba54091b6bfcf3298403e68834ca03e6b3fa872cb3dd6150565a0de7d2
          B/table-images/page-8.png: 3abb7b67733575626e8a4b6c90b16ac78abfe19d159b98b7fa0c4927722a5e3f
          B/table-images/manifest.json: 9460b074f5eee05d8aa2fc3a5999d9fbd42a9893105a34793a761753309c859d
          B/clauses/window-03/raw.json: bc799b33c90a602f97011d423e962b2a43032bcec6af794d7aeeb9dac02b29fb
          B/clauses/window-03/prompt.txt: 0f6f1657e4d34cffb05a0311d4bc942f45a83428638d8286375cc5bd3824f416
          B/clauses/window-03/meta.json: 2fdffa1ecf91e725f1cd8afa5bef35ad3a84193740616e5c00c0aab3921a478d
          B/clauses/window-04/raw.json: b75a5749fa3cbad7ffccabd493212bee170373a14cc2aae1d3a32e2af0429e4d
          B/clauses/window-04/prompt.txt: fab3e3cd054a52c0ba68417ae3412963c2e5d7138e96a5caacf313523b519839
          B/clauses/window-04/meta.json: 39a360da3a1f5fab56a6b33397ac18e0e352ed9b34e2d326fe86785a4baf5da1
          B/clauses/window-05/raw.json: d1941e3d3fed9f4a8f0ee96e54c3e7b5f84ed3482653229e3dc5847ead617999
          B/clauses/window-05/prompt.txt: aa64f8dc30dbee387ae04b815590724b7613df20cddde885e83fd79c9cd2f085
          B/clauses/window-05/meta.json: 1be8595ba6705b2af05fabe545be27a6c5df3b91e9b76b95ff7c40c6a938a468
          B/clauses/window-02/raw.json: 9ff915f38084d7fd65c153251ed07b0452c2f265a2eac8d5ffda0cf34c5ce232
          B/clauses/window-02/prompt.txt: 18a427fa4b8bfeb761f00ff82ccb37de74d53778e56623b4a5fbe0d7d5f9e1c0
          B/clauses/window-02/meta.json: 4174042b25cfd907b2788cec7c4affc5a81180ee7562f7a42a92023de95d6157
          B/clauses/window-09/raw.json: 3f5bc69281b7679e4ba1a25083b46f60d9166396f336af026ed42789ec82df2d
          B/clauses/window-09/prompt.txt: 9010d9a7400d1178038209b04187575026974acb749755c7991d4910db3c1806
          B/clauses/window-09/meta.json: 822e192f1ee7c635c2e9bb784a65df2e50dc9d5557bfb2fc7ebb6dd35eaf6818
          B/clauses/window-07/raw.json: 5c8fa37aaa3416fef8c1957df2292184b444c14a6f69e4a0aa4b4d274a4a5d92
          B/clauses/window-07/prompt.txt: 4009e422b0844097737669b3fcc9b4cdd4ec6de721948355bba1a7929c9bcc94
          B/clauses/window-07/meta.json: 79ab61fefc64f92ee940c898df70cb73684b6100186ee06d67bc5f658f87495b
          B/clauses/window-01/raw.json: 37c365b52ec4e7d97f3ff721841f1bfa388c0e9b2e9b35e062f4a5f9ef5998c6
          B/clauses/window-01/prompt.txt: da1a092248e5783328cf6d80b5ed778b928eb83f105e5c3543788fdf28e3d0e3
          B/clauses/window-01/meta.json: 9f0d16f74d894c3c6b24692501157098990e5bcbbf545b7f3b145a99cc44c8bf
          B/clauses/window-06/raw.json: 50fcf7a7ab40885fc289910cddabfb4d39d8a27ecbe88b860789a59bbbb47936
          B/clauses/window-06/prompt.txt: 8de15e1a50d28c7bcfc5bb5ea0b0dd90080e2aff2c71e08a47536a78a2950fcd
          B/clauses/window-06/meta.json: da736a99acaf995b243a77fcd3a64012ea1abab81f46ce0e07e7afe6f335c008
          B/clauses/window-08/raw.json: 3c713fdb45ac6940430d4bd44c8a6ae97ee3bfb6e1e3fe9402b0110d755787d9
          B/clauses/window-08/prompt.txt: 33918747b8744713912dc222a4d3192c553c2005298ee681f972144205c374bb
          B/clauses/window-08/meta.json: f06475d09f81f1fac767e633c533262d594be11e8101a989f15042e5353c3c77
          B/tables/TABLE-4-page-11-4/raw.json: b05e6193b6d0962142d7d564b702ca2af560a0225cc03c5249720eb82bf64afd
          B/tables/TABLE-4-page-11-4/prompt.txt: 75e33dec845cd6194c337c1ffb32f323c8cd8140b31b16e7aa5585a035954a95
          B/tables/TABLE-4-page-11-4/meta.json: 6f1e55367ade26e566726def0c9b50b8178c4a2e4df8c493179423804da0bb70
          B/tables/TABLE-2-page-8-2/raw.json: e99688856aa2c607e5b4bfead69ef29d37cf1af0c508466c1bd9222d8e14c3a2
          B/tables/TABLE-2-page-8-2/prompt.txt: 471f23dfe56b757f01480b1396085f647d139763c3e89f7316c0f32630f665d4
          B/tables/TABLE-2-page-8-2/meta.json: 7ecdada0d296e3734eae670449c427461871ccaa9feea4979cd64a0623ff5b6f
          B/tables/TABLE-3-page-10-3/raw.json: 2f1599b88c2d05145cedbdfb97003fce8543dc4b0312b76720388133ab8fc20b
          B/tables/TABLE-3-page-10-3/prompt.txt: 2f0b3b63e408f1ee3f1520275ad2e15f3f2a205fb85df05f0ae1482fe00010c5
          B/tables/TABLE-3-page-10-3/meta.json: adc5d18c41a3871469becc5e46715a88119c36639164a7686b3661c3135f8572
          B/tables/TABLE-1-page-3-1/raw.json: 777bc4244e94dbe1228ccfd2469b31ed7ce7fe45cb80d64c229307ee1a6f19b6
          B/tables/TABLE-1-page-3-1/prompt.txt: 7dbb68ba3c82d143200926f372928db37cfa4a95eafa3ea8c46e70da7f236a7e
          B/tables/TABLE-1-page-3-1/meta.json: c119f8a359a10bbf29eafd5618b105391d8c9ad89370575b79e16e95e302b7fc
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
        pdf_sha256: 3f10b8323077805b1b142ba70865bc674ad2c3377da82ca8ab9439a559cb1672
        source_review: _compare/relationships-2026-11-16/review-current/Rost2022
        source_status_sha256: 526d3f07ec746cc7184d2a9429c4133fb7fa6cef70af0778c6d37baab8c94b4e
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
      packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
    proposal:
      id: R013
      exposure:
        text: diabetes
      outcome:
        text: odds of brain infarcts (particularly lacunes)
      analysis_label: Neuropathological analysis
      relation: association
      evidence_ids:
      - P5-S3-C3
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
        pdf_sha256: 3f10b8323077805b1b142ba70865bc674ad2c3377da82ca8ab9439a559cb1672
        source_review: _compare/relationships-2026-11-16/review-current/Rost2022
        source_status_sha256: 526d3f07ec746cc7184d2a9429c4133fb7fa6cef70af0778c6d37baab8c94b4e
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    audit:
      original_audit:
        coverage_issues: []
        unattached_null_or_qualifier_ids: []
        suppressed_nonrepresented_units: 1
        default_disposition_count_requires_completeness_check: 180
        unselected_timing_passages:
        - P13-S2-C2
        - P14-S1-C3
        - P14-S1-C4
        personal_effect_slots_without_result_classification: []
        held_frame_selections:
        - slot: dependent_variable_statement
          source_id: P7-S1-C3
          reason: Requires a Methods outcome definition; model selection retained for inspection only
        - slot: dependent_variable_statement
          source_id: P7-S1-C4
          reason: Requires a Methods outcome definition; model selection retained for inspection only
        - slot: dependent_variable_statement
          source_id: P11-S1-C7
          reason: Requires a Methods outcome definition; model selection retained for inspection only
        - slot: dependent_variable_statement
          source_id: P11-S1-C8
          reason: Requires a Methods outcome definition; model selection retained for inspection only
        - slot: dependent_variable_statement
          source_id: P12-S1-C3
          reason: Requires a Methods outcome definition; model selection retained for inspection only
        - slot: dependent_variable_statement
          source_id: P12-S1-C4
          reason: Requires a Methods outcome definition; model selection retained for inspection only
        - slot: dependent_variable_statement
          source_id: P13-S2-C5
          reason: Requires a Methods outcome definition; model selection retained for inspection only
        - slot: validation
          source_id: P13-S2-C2
          reason: No validation-design cue; inspect the source rather than inferring a design
        - slot: tested_personal_effects
          source_id: P5-S2-C11
          reason: No current-result classification; a covariate description is not an individual test
        - slot: tested_personal_effects
          source_id: P5-S3-C1
          reason: No current-result classification; a covariate description is not an individual test
        - slot: tested_personal_effects
          source_id: P5-S3-C2
          reason: No current-result classification; a covariate description is not an individual test
        - slot: tested_personal_effects
          source_id: P5-S3-C3
          reason: No current-result classification; a covariate description is not an individual test
        - slot: tested_personal_effects
          source_id: P6-S1-C4
          reason: No current-result classification; a covariate description is not an individual test
        - slot: tested_personal_effects
          source_id: P6-S2-C2
          reason: No current-result classification; a covariate description is not an individual test
        - slot: tested_personal_effects
          source_id: P6-S2-C3
          reason: No current-result classification; a covariate description is not an individual test
        - slot: tested_personal_effects
          source_id: P6-S2-C5
          reason: No current-result classification; a covariate description is not an individual test
        - slot: tested_personal_effects
          source_id: P7-S2-C1
          reason: No current-result classification; a covariate description is not an individual test
        - slot: tested_personal_effects
          source_id: P7-S2-C3
          reason: No current-result classification; a covariate description is not an individual test
        - slot: tested_personal_effects
          source_id: P7-S2-C5
          reason: No current-result classification; a covariate description is not an individual test
        - slot: tested_personal_effects
          source_id: P7-S2-C6
          reason: No current-result classification; a covariate description is not an individual test
        - slot: tested_personal_effects
          source_id: P9-S1-C3
          reason: No current-result classification; a covariate description is not an individual test
        - slot: tested_personal_effects
          source_id: P11-S1-C7
          reason: No current-result classification; a covariate description is not an individual test
        - slot: tested_personal_effects
          source_id: P11-S1-C8
          reason: No current-result classification; a covariate description is not an individual test
        - slot: tested_personal_effects
          source_id: P12-S1-C3
          reason: No current-result classification; a covariate description is not an individual test
        - slot: tested_personal_effects
          source_id: P12-S1-C4
          reason: No current-result classification; a covariate description is not an individual test
        - slot: tested_personal_effects
          source_id: P13-S2-C2
          reason: No current-result classification; a covariate description is not an individual test
        - slot: personal_factors
          source_ids:
          - P1-S1-C12
          - P5-S2-C9
          - P5-S2-C10
          - P5-S2-C11
          - P5-S3-C1
          - P5-S3-C2
          - P5-S3-C3
          - P6-S1-C4
          - P6-S2-C2
          - P6-S2-C3
          - P6-S2-C5
          - P7-S2-C1
          - P7-S2-C3
          - P7-S2-C5
          - P7-S2-C6
          - P9-S1-C3
          - P13-S1-C4
          - P13-S1-C5
          - P13-S1-C6
          reason: Runaway selection (>8 passages); entire slot requires source review
        - slot: descriptive_personal_factors
          source_ids:
          - P1-S1-C12
          - P5-S2-C9
          - P5-S2-C10
          - P5-S2-C11
          - P5-S3-C1
          - P5-S3-C2
          - P5-S3-C3
          - P6-S1-C4
          - P6-S2-C2
          - P6-S2-C3
          - P6-S2-C5
          - P7-S2-C1
          - P7-S2-C3
          - P7-S2-C5
          - P7-S2-C6
          - P9-S1-C3
          - P13-S1-C4
          - P13-S1-C5
          - P13-S1-C6
          reason: Runaway selection (>8 passages); entire slot requires source review
        empty_frame_slots_require_confirmation:
        - validation
        - analysis_restrictions
        - personal_factors
        - tested_personal_effects
        - explicitly_not_adjusted
        - descriptive_personal_factors
        unclassified_extraction_ids: []
        table_review_required:
        - TABLE-1-page-3-1
        - TABLE-2-page-8-2
        - TABLE-3-page-10-3
        - TABLE-4-page-11-4
        unlinked_tables:
        - TABLE-1-page-3-1
        - TABLE-2-page-8-2
        - TABLE-3-page-10-3
        - TABLE-4-page-11-4
        source_anomalies: []
        visual_review_required:
          scope: All main-paper figures and table crops
          note: Automatic crops and matching transcriptions do not certify visual completeness. Figures are not automatically interpreted.
          caption_candidate_units:
          - P1-S2
          - P1-S3
          - P4-S1
          - P7-S3
          - P8-S2
          - P9-S1
          - P10-S2
          - P10-S3
          - P12-S2
          - P14-S3
        approval: Not performed. Structural checks and model selections do not establish semantic correctness.
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 3f10b8323077805b1b142ba70865bc674ad2c3377da82ca8ab9439a559cb1672
        source_review: _compare/relationships-2026-11-16/review-current/Rost2022
        source_status_sha256: 526d3f07ec746cc7184d2a9429c4133fb7fa6cef70af0778c6d37baab8c94b4e
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
      coverage:
      - source_id: P3-S1-C6
        disposition: background_or_descriptive
        result_indexes: []
        reason: Describes general cognitive profiles and domain-specific impairments without reporting a specific current-study measured relationship.
      - source_id: P3-S2-C1
        disposition: background_or_descriptive
        result_indexes: []
        reason: Describes general cognitive profiles and domain-specific impairments without reporting a specific current-study measured relationship.
      - source_id: P3-S2-C3
        disposition: background_or_descriptive
        result_indexes: []
        reason: Discusses the general impact of white matter dysfunction on brain networks.
      - source_id: P4-S2-C3
        disposition: background_or_descriptive
        result_indexes: []
        reason: General statement about cognitive decline before stroke.
      - source_id: P5-S1-C3
        disposition: background_or_descriptive
        result_indexes: []
        reason: General statement that lesion location alone does not predict outcome.
      - source_id: P10-S1-C4
        disposition: background_or_descriptive
        result_indexes: []
        reason: Discusses the sensitivity and specificity of the MoCA cutoff.
      unresolved_coverage: []
      pending_source_ids:
      - P3-S1-C6
      - P3-S2-C1
      - P3-S2-C3
      - P4-S2-C3
      - P5-S1-C3
      - P10-S1-C4
      pending_policy: Every result passage without direct candidate evidence remains pending, including model-labelled background and restatements; those labels never certify completeness.
      tables_requiring_review:
      - TABLE-1-page-3-1
      - TABLE-2-page-8-2
      - TABLE-3-page-10-3
      - TABLE-4-page-11-4
      paper_complete: false
      approved: false
      policy: New candidates require independent source checks; coverage dispositions are model suggestions. No original outputs changed.
    study_frame:
      slots:
        analysed_sample:
        - P3-S3-C1
        - P7-S1-C4
        - P14-S1-C3
        recruited_sample:
        - P14-S1-C3
        eligibility:
        - P14-S1-C3
        imaging_provenance:
        - P10-S2-C4
        - P11-S1-C5
        - P11-S1-C6
        - P12-S2-C4
        imaging_timing:
        - P10-S2-C4
        - P11-S1-C6
        outcome_timing:
        - P2-S1-C4
        - P3-S1-C2
        - P5-S2-C4
        - P5-S2-C8
        - P10-S3-C6
        outcome_definition:
        - P2-S1-C4
        - P3-S1-C2
        - P10-S1-C4
        validation: []
        analysis_restrictions: []
        dependent_variable_statement:
        - P5-S1-C4
        - P6-S2-C7
        - P6-S2-C8
        - P6-S3-C3
        limitations:
        - P4-S1-C3
        - P5-S2-C2
        - P13-S1-C6
        personal_factors: []
        tested_personal_effects: []
        adjustment_roles:
        - P7-S1-C3
        explicitly_not_adjusted: []
        descriptive_personal_factors: []
      outcome_type: both_reported
      imaging_vs_outcome: mixed
      validation_type: none_described
      held_selections:
      - slot: dependent_variable_statement
        source_id: P7-S1-C3
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: dependent_variable_statement
        source_id: P11-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: dependent_variable_statement
        source_id: P11-S1-C8
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: dependent_variable_statement
        source_id: P12-S1-C3
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: dependent_variable_statement
        source_id: P12-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: dependent_variable_statement
        source_id: P13-S2-C5
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: validation
        source_id: P13-S2-C2
        reason: No validation-design cue; inspect the source rather than inferring a design
      - slot: tested_personal_effects
        source_id: P5-S2-C11
        reason: No current-result classification; a covariate description is not an individual test
      - slot: tested_personal_effects
        source_id: P5-S3-C1
        reason: No current-result classification; a covariate description is not an individual test
      - slot: tested_personal_effects
        source_id: P5-S3-C2
        reason: No current-result classification; a covariate description is not an individual test
      - slot: tested_personal_effects
        source_id: P5-S3-C3
        reason: No current-result classification; a covariate description is not an individual test
      - slot: tested_personal_effects
        source_id: P6-S1-C4
        reason: No current-result classification; a covariate description is not an individual test
      - slot: tested_personal_effects
        source_id: P6-S2-C2
        reason: No current-result classification; a covariate description is not an individual test
      - slot: tested_personal_effects
        source_id: P6-S2-C3
        reason: No current-result classification; a covariate description is not an individual test
      - slot: tested_personal_effects
        source_id: P6-S2-C5
        reason: No current-result classification; a covariate description is not an individual test
      - slot: tested_personal_effects
        source_id: P7-S2-C1
        reason: No current-result classification; a covariate description is not an individual test
      - slot: tested_personal_effects
        source_id: P7-S2-C3
        reason: No current-result classification; a covariate description is not an individual test
      - slot: tested_personal_effects
        source_id: P7-S2-C5
        reason: No current-result classification; a covariate description is not an individual test
      - slot: tested_personal_effects
        source_id: P7-S2-C6
        reason: No current-result classification; a covariate description is not an individual test
      - slot: tested_personal_effects
        source_id: P9-S1-C3
        reason: No current-result classification; a covariate description is not an individual test
      - slot: tested_personal_effects
        source_id: P11-S1-C7
        reason: No current-result classification; a covariate description is not an individual test
      - slot: tested_personal_effects
        source_id: P11-S1-C8
        reason: No current-result classification; a covariate description is not an individual test
      - slot: tested_personal_effects
        source_id: P12-S1-C3
        reason: No current-result classification; a covariate description is not an individual test
      - slot: tested_personal_effects
        source_id: P12-S1-C4
        reason: No current-result classification; a covariate description is not an individual test
      - slot: tested_personal_effects
        source_id: P13-S2-C2
        reason: No current-result classification; a covariate description is not an individual test
      - slot: personal_factors
        source_ids:
        - P1-S1-C12
        - P5-S2-C9
        - P5-S2-C10
        - P5-S2-C11
        - P5-S3-C1
        - P5-S3-C2
        - P5-S3-C3
        - P6-S1-C4
        - P6-S2-C2
        - P6-S2-C3
        - P6-S2-C5
        - P7-S2-C1
        - P7-S2-C3
        - P7-S2-C5
        - P7-S2-C6
        - P9-S1-C3
        - P13-S1-C4
        - P13-S1-C5
        - P13-S1-C6
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: descriptive_personal_factors
        source_ids:
        - P1-S1-C12
        - P5-S2-C9
        - P5-S2-C10
        - P5-S2-C11
        - P5-S3-C1
        - P5-S3-C2
        - P5-S3-C3
        - P6-S1-C4
        - P6-S2-C2
        - P6-S2-C3
        - P6-S2-C5
        - P7-S2-C1
        - P7-S2-C3
        - P7-S2-C5
        - P7-S2-C6
        - P9-S1-C3
        - P13-S1-C4
        - P13-S1-C5
        - P13-S1-C6
        reason: Runaway selection (>8 passages); entire slot requires source review
      policy: All slots and enums remain unverified. Held selections are not evidence of absence. Original response is preserved in frame/raw.json.
    approved: false
    source_check:
      profile: core
      scope: Independent model text review of core meaning; not human approval or complete PDF verification
      binding:
        profile: core
        version: core-source-check-v3
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        checker_model: qwen3.8:27b
        checker_digest: 47951e4a666180bc2aedfc93c169472f2de783696fe196efbf063f5730ecf163
        host: http://localhost:11434
        pdf_sha256: 3f10b8323077805b1b142ba70865bc674ad2c3377da82ca8ab9439a559cb1672
        review_sha256: 21b4b527693cef6f9f990166a0152d64c2a417f65c0623da8a7ddf6181f62e7b
        code_sha256: c4650d24fa3e36e6f317cb65cc7626277a28936a7cdf5d07248d4b1e5bfa09aa
        source_helpers_sha256: e0e0f295e5efa1fdb4e9e8c84ca491d062df3aefe8ca8b4d9ca85fcb6d4c9082
        converter_sha256: 048f1e35905528676837a00b1b2406b1c97cb1eb47c48d63f121a5c00cc0afeb
        table_helpers_sha256: 78e562e9725fc484d6a12279ea710856dfd1d9aa13ee178d0358e9c0acdd2c8c
        mapper_budget: 2500
        reviewer_budget: 1600
        approved: false
        visual:
          models:
          - gemma4:31b
          - qwen3.8:27b
          digests:
          - 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
          - 47951e4a666180bc2aedfc93c169472f2de783696fe196efbf063f5730ecf163
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
      approved: false
      core_review:
        own_result_source_ids:
        - P5-S3-C3
        source_result: A neuropathological analysis of >1,300 autopsied patients found that diabetes increased the odds of brain infarcts, particularly lacunes, but not Alzheimer disease pathology.
        result_status: detected
        patient_measurement: non_imaging
        checks:
          analysis_identity:
            answer: fits
            reason: The source P5-S3-C3 explicitly describes a 'neuropathological analysis' of autopsied patients, which matches the proposed analysis label and the nature of the evidence (post-mortem pathology rather than in-vivo imaging).
            source_ids:
            - P5-S3-C3
          direction:
            answer: fits
            reason: The source states diabetes 'increased the odds' of infarcts/lacunes, which aligns with the proposed direction of 'likely' (positive association). The source also notes a lack of association with AD pathology, which is captured in the claim text.
            source_ids:
            - P5-S3-C3
          construct:
            answer: fits
            reason: Exposure is diabetes, outcome is brain infarcts (specifically lacunes). The measurement is neuropathological (autopsy), which is correctly classified as non_imaging. The proposed draft correctly identifies the population as autopsied patients.
            source_ids:
            - P5-S3-C3
          qualifications:
            answer: fits
            reason: The qualification 'specifically associated with lacunes' is supported by the source text 'particularly lacunes'. The limitation regarding the neuropathological/autopsy nature is also correctly included.
            source_ids:
            - P5-S3-C3
          missing_material_caveat:
            answer: fits
            reason: The source explicitly states the finding was 'not' associated with Alzheimer disease pathology. The proposed claim includes this negative finding ('but not Alzheimer disease pathology'), so no material caveat is missing. The sample size (>1300) is mentioned in the source but marked as pending in the draft, which is acceptable for a qualitative draft.
            source_ids:
            - P5-S3-C3
        optional_pending:
        - Sample size (>1300) is mentioned in source but not transcribed to numeric field
        - Specific odds ratios or confidence intervals not transcribed
        verdict: draft
        reason: All five core checks fit the source.
        material_issues: []
      pending_details:
      - Sample size requires source confirmation; it has not been transcribed.
      - Detailed statistics, atlas/reference-space and structured confounder metadata not transcribed.
      - Recovery phase is not classified; use the reported timing words.
      - Evidence-strength rating is a conservative draft placeholder pending human review.
      - Sample size (>1300) is mentioned in source but not transcribed to numeric field
      - Specific odds ratios or confidence intervals not transcribed
      normalizations:
      - field: bucket
        original: predictors
        action: route_from_kind
        value: ingredients
      - field: sample.n
        original: 1300
        action: not_transcribed
        reason: Not supported by selected quotations
      analysis_identity:
        id: R013
        exposure:
          text: diabetes
        outcome:
          text: odds of brain infarcts (particularly lacunes)
        analysis_label: Neuropathological analysis
        relation: association
        evidence_ids:
        - P5-S3-C3
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
          pdf_sha256: 3f10b8323077805b1b142ba70865bc674ad2c3377da82ca8ab9439a559cb1672
          source_review: _compare/relationships-2026-11-16/review-current/Rost2022
          source_status_sha256: 526d3f07ec746cc7184d2a9429c4133fb7fa6cef70af0778c6d37baab8c94b4e
          code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
          version: candidate-inventory-v1
      paper_complete: false
      visual_prose_readings: {}
      remaining:
      - Human PDF review and approval
      - Pending metadata enrichment
      - Main Results, figures and tables completeness check
  original_publication_entry:
    id: diabetes
    name: diabetes
    kind: ingredient
    findings:
    - id: f1
      target: brain_infarcts
      target_kind: impairment
      claim: diabetes increased the odds of brain infarcts, particularly lacunes, but not Alzheimer disease pathology
      direction: likely
      relationship: correlational
      method: behavioral_only
      sample:
        n: not_reported
        population: autopsied patients
        phase: not_reported
        time_post_onset: post-mortem
      statistics:
        threshold: not_transcribed
      confounders_controlled: []
      confounders_not_controlled: []
      region_definition:
        kind: not_reported
        description: Not transcribed; see source passages and claim.
      author_limitations:
      - finding based on neuropathological analysis of autopsied patients
      evidence_quality: cohort
      strength: weak
      notes: 'Exposure measurement: presence of diabetes measured via neuropathological analysis of autopsied patients. specifically associated with lacunes. Additional metadata has not been transcribed; review the pending-field flags before approval.'
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
        - not_transcribed:sample.n
        - proposed_concept:brain_infarcts
      citation: '@Rost2022'
      source_passages:
      - section: Original source P5-S3-C3
        page: 5
        quote: "For instance, a neuropatho-\nlogical analysis of more than 1.300 autopsied patients \nwith diabetes found that diabetes increased the odds \nof brain infarcts, particularly lacunes, but not Alzheimer \ndisease (AD) pathology.68 As detailed below, the burden \n\n"
        supports: claim
      - section: Original source P5-S3-C3
        page: 5
        quote: "For instance, a neuropatho-\nlogical analysis of more than 1.300 autopsied patients \nwith diabetes found that diabetes increased the odds \nof brain infarcts, particularly lacunes, but not Alzheimer \ndisease (AD) pathology.68 As detailed below, the burden \n\n"
        supports: sample
      - section: Original source P5-S3-C3
        page: 5
        quote: "For instance, a neuropatho-\nlogical analysis of more than 1.300 autopsied patients \nwith diabetes found that diabetes increased the odds \nof brain infarcts, particularly lacunes, but not Alzheimer \ndisease (AD) pathology.68 As detailed below, the burden \n\n"
        supports: method
    schema_version: '2.8'
    status: draft
    created_by: agent:relationship-converter
    created_on: '2026-11-25'
    relationship_review:
      paper: Rost2022
      proposal_id: R013
      review_status_sha256: 21b4b527693cef6f9f990166a0152d64c2a417f65c0623da8a7ddf6181f62e7b
      review_binding:
        version: candidate-inventory-v1
        input_hashes:
          pdf: 3f10b8323077805b1b142ba70865bc674ad2c3377da82ca8ab9439a559cb1672
        original_review_binding:
          version: relationship-review-v4
          input_hashes:
            pdf: 3f10b8323077805b1b142ba70865bc674ad2c3377da82ca8ab9439a559cb1672
            A/passages.json: 146968a218ac779f968b33bee6f2d2d60a2e0598c8a9fae23c4fbf324237d975
            A/raw.json: ff3e067d0eb830d74dcba7e252d112891865c8fe7c020570532f2ed88594da3d
            A/source-units.json: 924df3501e60f90a791eb3fa9b3d0fcc1e43dd488b6b62a7f940ac4e47b15e56
            A/full-source-units.json: f9960516c14dad2ec119d4e3417afaa848ebff83be4adbfb0ed7f25d9c8efe1d
            A/meta.json: ecae46ae95dbabf6183d11dccb4f38c7cd88a4e598e6fadc5a68bb746381ac12
            A/table-images/TABLE-1-page-3-1.png: 493983cd0c93b87394647e7da633fb28abbcbe22bb22becc144116b83908c043
            A/table-images/TABLE-3-page-10-1.png: 664d66d2b8ebbe147c7acf2b58f6ccf12fb40addb3fb9f34deade7d4526ac366
            A/table-images/page-10.png: 43b425b45a0c5ce37efe53981601c213b12cde68a77fa9c19fb1ac9846e533b5
            A/table-images/page-11.png: 7fee21107c91a8e07a8c9bb7d6750c3fd16317130a6e882e92132dc2cc6bdc58
            A/table-images/TABLE-2-page-8-1.png: a74a9ff22ddc8d1612b52bd591b6293bfc10d7edd5b8ab30aff785f1cbf55b20
            A/table-images/page-3.png: 1ce2f13ccc70f15d8ce64ffb12e1310b1bcb5d08009da2049812e88fb83fe422
            A/table-images/TABLE-4-page-11-1.png: bd53aeba54091b6bfcf3298403e68834ca03e6b3fa872cb3dd6150565a0de7d2
            A/table-images/page-8.png: 3abb7b67733575626e8a4b6c90b16ac78abfe19d159b98b7fa0c4927722a5e3f
            A/table-images/manifest.json: cebd0074423388d34a11ed664632334a602fdc62c083cd373aa6893532bb2a3b
            A/clauses/window-03/raw.json: 8f08bf5bc441ac00197a257abc555328714356ce9acd3f4d1f40793df95f850e
            A/clauses/window-03/prompt.txt: 0f6f1657e4d34cffb05a0311d4bc942f45a83428638d8286375cc5bd3824f416
            A/clauses/window-03/meta.json: 65cbf852829d4901f2207341f34d5126c1e593b9acdbbb31c9505ef6aee9555c
            A/clauses/window-04/raw.json: ad6da6cff35b0e7771345d1a6f14ae2e33896f8ad4dd13bb9ea83a5770bffdf8
            A/clauses/window-04/prompt.txt: fab3e3cd054a52c0ba68417ae3412963c2e5d7138e96a5caacf313523b519839
            A/clauses/window-04/meta.json: 35d933950f728ade0fe5d92395a4cd42ff01eface743d17ba31460a85fb5cf3e
            A/clauses/window-05/raw.json: 29efcd9120daa8da42b65ff5c7b142c632d404062e33a400a7c8089fa7a8696d
            A/clauses/window-05/prompt.txt: aa64f8dc30dbee387ae04b815590724b7613df20cddde885e83fd79c9cd2f085
            A/clauses/window-05/meta.json: 1ab84f0fa8a122ed858b551893d3f0fe2afe0fe684ba349670e772852f120ae5
            A/clauses/window-02/raw.json: dd7b9cb699f2536d0eab9a9623ec15fbd9b81bd3b05e4f16e8f85d383d1bc936
            A/clauses/window-02/prompt.txt: 18a427fa4b8bfeb761f00ff82ccb37de74d53778e56623b4a5fbe0d7d5f9e1c0
            A/clauses/window-02/meta.json: 0e9e492750f8323cb7a10918e95d617bfdd554d6330f5e6badfe5fedd7059c8f
            A/clauses/window-09/raw.json: ec7d91edd153628200ea997fd41a3165f941f5ea329d2160d9b1564138f24c9c
            A/clauses/window-09/prompt.txt: 9010d9a7400d1178038209b04187575026974acb749755c7991d4910db3c1806
            A/clauses/window-09/meta.json: 75c409967db11a72667484ea27a3b026e6a8787ddd31481383e24861dcd86eff
            A/clauses/window-07/raw.json: 722bf6eb3a6e80e9f3c04ccc9a60bdf36fc7fe09d12639b9cd59deed6c319ab5
            A/clauses/window-07/prompt.txt: 4009e422b0844097737669b3fcc9b4cdd4ec6de721948355bba1a7929c9bcc94
            A/clauses/window-07/meta.json: 2af5bd77730cd55951f9cd6f048f5cc9d05013ac3532ab13fd1e55f6854589f1
            A/clauses/window-01/raw.json: ef67fa6fe9663edf7c878a8dc794e9c971835fcbc0913f79a4f45a4197e53846
            A/clauses/window-01/prompt.txt: da1a092248e5783328cf6d80b5ed778b928eb83f105e5c3543788fdf28e3d0e3
            A/clauses/window-01/meta.json: 372c6beb493f58a468e3469682c8de5b1f313bd65b33e50647070a18b9938648
            A/clauses/window-06/raw.json: c2d2872827839c5903ab026742330e0d43663f79af70aa0504bf13392c4878c3
            A/clauses/window-06/prompt.txt: 8de15e1a50d28c7bcfc5bb5ea0b0dd90080e2aff2c71e08a47536a78a2950fcd
            A/clauses/window-06/meta.json: d4a2216a6cb612ca7ed49bf9437dba6124c1229f06569e6b167f76138aacb8f1
            A/clauses/window-08/raw.json: 245d9b9c2ae776f00bf56def36152bf2b1dddd8f57b7894b7f8d5a8bda4dcace
            A/clauses/window-08/prompt.txt: 33918747b8744713912dc222a4d3192c553c2005298ee681f972144205c374bb
            A/clauses/window-08/meta.json: b10a2e0a3744e7c366a039eeb59719f0a8144d6bc11c1f618dd82d9c9f05e81a
            A/tables/TABLE-4-page-11-4/raw.json: c416c8ac25bebe71d5b92dd70cf60db25dffa9811f17601b93dcc308de5691cb
            A/tables/TABLE-4-page-11-4/prompt.txt: 75e33dec845cd6194c337c1ffb32f323c8cd8140b31b16e7aa5585a035954a95
            A/tables/TABLE-4-page-11-4/meta.json: 9af225ff1d1aacf8e8ebe17727135089a3c52af8dff6f8b58e3b34e96ad41f4b
            A/tables/TABLE-2-page-8-2/raw.json: bcefc5c6f7d16c5a792d45b300b1b8fef6472cfb7b697e926635ba5e0f127be7
            A/tables/TABLE-2-page-8-2/prompt.txt: 471f23dfe56b757f01480b1396085f647d139763c3e89f7316c0f32630f665d4
            A/tables/TABLE-2-page-8-2/meta.json: 2275694ac96cf2048ba5da4684d85fa64b0fd93574f5bc3d15876507f0917077
            A/tables/TABLE-3-page-10-3/raw.json: dbeee60dd070252f91d1bd4ee9ab0baa0ea13cb8f43e8bdb5f0fc5c62b826479
            A/tables/TABLE-3-page-10-3/prompt.txt: 2f0b3b63e408f1ee3f1520275ad2e15f3f2a205fb85df05f0ae1482fe00010c5
            A/tables/TABLE-3-page-10-3/meta.json: 17eec2f5e3a0ea125a671139d8255c70f72da6c881092e3326164b8d75d5c37d
            A/tables/TABLE-1-page-3-1/raw.json: 5efce61cfb5a04440e240181d72edcac759c569b05a61a2214f29cb47fe0196f
            A/tables/TABLE-1-page-3-1/prompt.txt: 7dbb68ba3c82d143200926f372928db37cfa4a95eafa3ea8c46e70da7f236a7e
            A/tables/TABLE-1-page-3-1/meta.json: 0c2d1dbab6792f349d46830e20aa23b8aba2d0dd73bd81b268faec4b2750c9d3
            B/passages.json: 146968a218ac779f968b33bee6f2d2d60a2e0598c8a9fae23c4fbf324237d975
            B/raw.json: 0e43e2f0032526471635e6a8d3f0a96ab422e509e8669631aa58e44d87f1c0b7
            B/source-units.json: 924df3501e60f90a791eb3fa9b3d0fcc1e43dd488b6b62a7f940ac4e47b15e56
            B/full-source-units.json: f9960516c14dad2ec119d4e3417afaa848ebff83be4adbfb0ed7f25d9c8efe1d
            B/meta.json: 03c7f4748f89710094fd91ee3435400c7a3a402fe0dbaa43b7d67b4a00d61ac5
            B/table-images/TABLE-1-page-3-1.png: 493983cd0c93b87394647e7da633fb28abbcbe22bb22becc144116b83908c043
            B/table-images/TABLE-3-page-10-1.png: 664d66d2b8ebbe147c7acf2b58f6ccf12fb40addb3fb9f34deade7d4526ac366
            B/table-images/page-10.png: 43b425b45a0c5ce37efe53981601c213b12cde68a77fa9c19fb1ac9846e533b5
            B/table-images/page-11.png: 7fee21107c91a8e07a8c9bb7d6750c3fd16317130a6e882e92132dc2cc6bdc58
            B/table-images/TABLE-2-page-8-1.png: a74a9ff22ddc8d1612b52bd591b6293bfc10d7edd5b8ab30aff785f1cbf55b20
            B/table-images/page-3.png: 1ce2f13ccc70f15d8ce64ffb12e1310b1bcb5d08009da2049812e88fb83fe422
            B/table-images/TABLE-4-page-11-1.png: bd53aeba54091b6bfcf3298403e68834ca03e6b3fa872cb3dd6150565a0de7d2
            B/table-images/page-8.png: 3abb7b67733575626e8a4b6c90b16ac78abfe19d159b98b7fa0c4927722a5e3f
            B/table-images/manifest.json: 9460b074f5eee05d8aa2fc3a5999d9fbd42a9893105a34793a761753309c859d
            B/clauses/window-03/raw.json: bc799b33c90a602f97011d423e962b2a43032bcec6af794d7aeeb9dac02b29fb
            B/clauses/window-03/prompt.txt: 0f6f1657e4d34cffb05a0311d4bc942f45a83428638d8286375cc5bd3824f416
            B/clauses/window-03/meta.json: 2fdffa1ecf91e725f1cd8afa5bef35ad3a84193740616e5c00c0aab3921a478d
            B/clauses/window-04/raw.json: b75a5749fa3cbad7ffccabd493212bee170373a14cc2aae1d3a32e2af0429e4d
            B/clauses/window-04/prompt.txt: fab3e3cd054a52c0ba68417ae3412963c2e5d7138e96a5caacf313523b519839
            B/clauses/window-04/meta.json: 39a360da3a1f5fab56a6b33397ac18e0e352ed9b34e2d326fe86785a4baf5da1
            B/clauses/window-05/raw.json: d1941e3d3fed9f4a8f0ee96e54c3e7b5f84ed3482653229e3dc5847ead617999
            B/clauses/window-05/prompt.txt: aa64f8dc30dbee387ae04b815590724b7613df20cddde885e83fd79c9cd2f085
            B/clauses/window-05/meta.json: 1be8595ba6705b2af05fabe545be27a6c5df3b91e9b76b95ff7c40c6a938a468
            B/clauses/window-02/raw.json: 9ff915f38084d7fd65c153251ed07b0452c2f265a2eac8d5ffda0cf34c5ce232
            B/clauses/window-02/prompt.txt: 18a427fa4b8bfeb761f00ff82ccb37de74d53778e56623b4a5fbe0d7d5f9e1c0
            B/clauses/window-02/meta.json: 4174042b25cfd907b2788cec7c4affc5a81180ee7562f7a42a92023de95d6157
            B/clauses/window-09/raw.json: 3f5bc69281b7679e4ba1a25083b46f60d9166396f336af026ed42789ec82df2d
            B/clauses/window-09/prompt.txt: 9010d9a7400d1178038209b04187575026974acb749755c7991d4910db3c1806
            B/clauses/window-09/meta.json: 822e192f1ee7c635c2e9bb784a65df2e50dc9d5557bfb2fc7ebb6dd35eaf6818
            B/clauses/window-07/raw.json: 5c8fa37aaa3416fef8c1957df2292184b444c14a6f69e4a0aa4b4d274a4a5d92
            B/clauses/window-07/prompt.txt: 4009e422b0844097737669b3fcc9b4cdd4ec6de721948355bba1a7929c9bcc94
            B/clauses/window-07/meta.json: 79ab61fefc64f92ee940c898df70cb73684b6100186ee06d67bc5f658f87495b
            B/clauses/window-01/raw.json: 37c365b52ec4e7d97f3ff721841f1bfa388c0e9b2e9b35e062f4a5f9ef5998c6
            B/clauses/window-01/prompt.txt: da1a092248e5783328cf6d80b5ed778b928eb83f105e5c3543788fdf28e3d0e3
            B/clauses/window-01/meta.json: 9f0d16f74d894c3c6b24692501157098990e5bcbbf545b7f3b145a99cc44c8bf
            B/clauses/window-06/raw.json: 50fcf7a7ab40885fc289910cddabfb4d39d8a27ecbe88b860789a59bbbb47936
            B/clauses/window-06/prompt.txt: 8de15e1a50d28c7bcfc5bb5ea0b0dd90080e2aff2c71e08a47536a78a2950fcd
            B/clauses/window-06/meta.json: da736a99acaf995b243a77fcd3a64012ea1abab81f46ce0e07e7afe6f335c008
            B/clauses/window-08/raw.json: 3c713fdb45ac6940430d4bd44c8a6ae97ee3bfb6e1e3fe9402b0110d755787d9
            B/clauses/window-08/prompt.txt: 33918747b8744713912dc222a4d3192c553c2005298ee681f972144205c374bb
            B/clauses/window-08/meta.json: f06475d09f81f1fac767e633c533262d594be11e8101a989f15042e5353c3c77
            B/tables/TABLE-4-page-11-4/raw.json: b05e6193b6d0962142d7d564b702ca2af560a0225cc03c5249720eb82bf64afd
            B/tables/TABLE-4-page-11-4/prompt.txt: 75e33dec845cd6194c337c1ffb32f323c8cd8140b31b16e7aa5585a035954a95
            B/tables/TABLE-4-page-11-4/meta.json: 6f1e55367ade26e566726def0c9b50b8178c4a2e4df8c493179423804da0bb70
            B/tables/TABLE-2-page-8-2/raw.json: e99688856aa2c607e5b4bfead69ef29d37cf1af0c508466c1bd9222d8e14c3a2
            B/tables/TABLE-2-page-8-2/prompt.txt: 471f23dfe56b757f01480b1396085f647d139763c3e89f7316c0f32630f665d4
            B/tables/TABLE-2-page-8-2/meta.json: 7ecdada0d296e3734eae670449c427461871ccaa9feea4979cd64a0623ff5b6f
            B/tables/TABLE-3-page-10-3/raw.json: 2f1599b88c2d05145cedbdfb97003fce8543dc4b0312b76720388133ab8fc20b
            B/tables/TABLE-3-page-10-3/prompt.txt: 2f0b3b63e408f1ee3f1520275ad2e15f3f2a205fb85df05f0ae1482fe00010c5
            B/tables/TABLE-3-page-10-3/meta.json: adc5d18c41a3871469becc5e46715a88119c36639164a7686b3661c3135f8572
            B/tables/TABLE-1-page-3-1/raw.json: 777bc4244e94dbe1228ccfd2469b31ed7ce7fe45cb80d64c229307ee1a6f19b6
            B/tables/TABLE-1-page-3-1/prompt.txt: 7dbb68ba3c82d143200926f372928db37cfa4a95eafa3ea8c46e70da7f236a7e
            B/tables/TABLE-1-page-3-1/meta.json: c119f8a359a10bbf29eafd5618b105391d8c9ad89370575b79e16e95e302b7fc
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
          pdf_sha256: 3f10b8323077805b1b142ba70865bc674ad2c3377da82ca8ab9439a559cb1672
          source_review: _compare/relationships-2026-11-16/review-current/Rost2022
          source_status_sha256: 526d3f07ec746cc7184d2a9429c4133fb7fa6cef70af0778c6d37baab8c94b4e
          code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
          version: candidate-inventory-v1
        packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      proposal:
        id: R013
        exposure:
          text: diabetes
        outcome:
          text: odds of brain infarcts (particularly lacunes)
        analysis_label: Neuropathological analysis
        relation: association
        evidence_ids:
        - P5-S3-C3
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
          pdf_sha256: 3f10b8323077805b1b142ba70865bc674ad2c3377da82ca8ab9439a559cb1672
          source_review: _compare/relationships-2026-11-16/review-current/Rost2022
          source_status_sha256: 526d3f07ec746cc7184d2a9429c4133fb7fa6cef70af0778c6d37baab8c94b4e
          code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
          version: candidate-inventory-v1
      audit:
        original_audit:
          coverage_issues: []
          unattached_null_or_qualifier_ids: []
          suppressed_nonrepresented_units: 1
          default_disposition_count_requires_completeness_check: 180
          unselected_timing_passages:
          - P13-S2-C2
          - P14-S1-C3
          - P14-S1-C4
          personal_effect_slots_without_result_classification: []
          held_frame_selections:
          - slot: dependent_variable_statement
            source_id: P7-S1-C3
            reason: Requires a Methods outcome definition; model selection retained for inspection only
          - slot: dependent_variable_statement
            source_id: P7-S1-C4
            reason: Requires a Methods outcome definition; model selection retained for inspection only
          - slot: dependent_variable_statement
            source_id: P11-S1-C7
            reason: Requires a Methods outcome definition; model selection retained for inspection only
          - slot: dependent_variable_statement
            source_id: P11-S1-C8
            reason: Requires a Methods outcome definition; model selection retained for inspection only
          - slot: dependent_variable_statement
            source_id: P12-S1-C3
            reason: Requires a Methods outcome definition; model selection retained for inspection only
          - slot: dependent_variable_statement
            source_id: P12-S1-C4
            reason: Requires a Methods outcome definition; model selection retained for inspection only
          - slot: dependent_variable_statement
            source_id: P13-S2-C5
            reason: Requires a Methods outcome definition; model selection retained for inspection only
          - slot: validation
            source_id: P13-S2-C2
            reason: No validation-design cue; inspect the source rather than inferring a design
          - slot: tested_personal_effects
            source_id: P5-S2-C11
            reason: No current-result classification; a covariate description is not an individual test
          - slot: tested_personal_effects
            source_id: P5-S3-C1
            reason: No current-result classification; a covariate description is not an individual test
          - slot: tested_personal_effects
            source_id: P5-S3-C2
            reason: No current-result classification; a covariate description is not an individual test
          - slot: tested_personal_effects
            source_id: P5-S3-C3
            reason: No current-result classification; a covariate description is not an individual test
          - slot: tested_personal_effects
            source_id: P6-S1-C4
            reason: No current-result classification; a covariate description is not an individual test
          - slot: tested_personal_effects
            source_id: P6-S2-C2
            reason: No current-result classification; a covariate description is not an individual test
          - slot: tested_personal_effects
            source_id: P6-S2-C3
            reason: No current-result classification; a covariate description is not an individual test
          - slot: tested_personal_effects
            source_id: P6-S2-C5
            reason: No current-result classification; a covariate description is not an individual test
          - slot: tested_personal_effects
            source_id: P7-S2-C1
            reason: No current-result classification; a covariate description is not an individual test
          - slot: tested_personal_effects
            source_id: P7-S2-C3
            reason: No current-result classification; a covariate description is not an individual test
          - slot: tested_personal_effects
            source_id: P7-S2-C5
            reason: No current-result classification; a covariate description is not an individual test
          - slot: tested_personal_effects
            source_id: P7-S2-C6
            reason: No current-result classification; a covariate description is not an individual test
          - slot: tested_personal_effects
            source_id: P9-S1-C3
            reason: No current-result classification; a covariate description is not an individual test
          - slot: tested_personal_effects
            source_id: P11-S1-C7
            reason: No current-result classification; a covariate description is not an individual test
          - slot: tested_personal_effects
            source_id: P11-S1-C8
            reason: No current-result classification; a covariate description is not an individual test
          - slot: tested_personal_effects
            source_id: P12-S1-C3
            reason: No current-result classification; a covariate description is not an individual test
          - slot: tested_personal_effects
            source_id: P12-S1-C4
            reason: No current-result classification; a covariate description is not an individual test
          - slot: tested_personal_effects
            source_id: P13-S2-C2
            reason: No current-result classification; a covariate description is not an individual test
          - slot: personal_factors
            source_ids:
            - P1-S1-C12
            - P5-S2-C9
            - P5-S2-C10
            - P5-S2-C11
            - P5-S3-C1
            - P5-S3-C2
            - P5-S3-C3
            - P6-S1-C4
            - P6-S2-C2
            - P6-S2-C3
            - P6-S2-C5
            - P7-S2-C1
            - P7-S2-C3
            - P7-S2-C5
            - P7-S2-C6
            - P9-S1-C3
            - P13-S1-C4
            - P13-S1-C5
            - P13-S1-C6
            reason: Runaway selection (>8 passages); entire slot requires source review
          - slot: descriptive_personal_factors
            source_ids:
            - P1-S1-C12
            - P5-S2-C9
            - P5-S2-C10
            - P5-S2-C11
            - P5-S3-C1
            - P5-S3-C2
            - P5-S3-C3
            - P6-S1-C4
            - P6-S2-C2
            - P6-S2-C3
            - P6-S2-C5
            - P7-S2-C1
            - P7-S2-C3
            - P7-S2-C5
            - P7-S2-C6
            - P9-S1-C3
            - P13-S1-C4
            - P13-S1-C5
            - P13-S1-C6
            reason: Runaway selection (>8 passages); entire slot requires source review
          empty_frame_slots_require_confirmation:
          - validation
          - analysis_restrictions
          - personal_factors
          - tested_personal_effects
          - explicitly_not_adjusted
          - descriptive_personal_factors
          unclassified_extraction_ids: []
          table_review_required:
          - TABLE-1-page-3-1
          - TABLE-2-page-8-2
          - TABLE-3-page-10-3
          - TABLE-4-page-11-4
          unlinked_tables:
          - TABLE-1-page-3-1
          - TABLE-2-page-8-2
          - TABLE-3-page-10-3
          - TABLE-4-page-11-4
          source_anomalies: []
          visual_review_required:
            scope: All main-paper figures and table crops
            note: Automatic crops and matching transcriptions do not certify visual completeness. Figures are not automatically interpreted.
            caption_candidate_units:
            - P1-S2
            - P1-S3
            - P4-S1
            - P7-S3
            - P8-S2
            - P9-S1
            - P10-S2
            - P10-S3
            - P12-S2
            - P14-S3
          approval: Not performed. Structural checks and model selections do not establish semantic correctness.
        candidate_discovery:
          model: gemma4:31b
          model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
          pdf_sha256: 3f10b8323077805b1b142ba70865bc674ad2c3377da82ca8ab9439a559cb1672
          source_review: _compare/relationships-2026-11-16/review-current/Rost2022
          source_status_sha256: 526d3f07ec746cc7184d2a9429c4133fb7fa6cef70af0778c6d37baab8c94b4e
          code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
          version: candidate-inventory-v1
        coverage:
        - source_id: P3-S1-C6
          disposition: background_or_descriptive
          result_indexes: []
          reason: Describes general cognitive profiles and domain-specific impairments without reporting a specific current-study measured relationship.
        - source_id: P3-S2-C1
          disposition: background_or_descriptive
          result_indexes: []
          reason: Describes general cognitive profiles and domain-specific impairments without reporting a specific current-study measured relationship.
        - source_id: P3-S2-C3
          disposition: background_or_descriptive
          result_indexes: []
          reason: Discusses the general impact of white matter dysfunction on brain networks.
        - source_id: P4-S2-C3
          disposition: background_or_descriptive
          result_indexes: []
          reason: General statement about cognitive decline before stroke.
        - source_id: P5-S1-C3
          disposition: background_or_descriptive
          result_indexes: []
          reason: General statement that lesion location alone does not predict outcome.
        - source_id: P10-S1-C4
          disposition: background_or_descriptive
          result_indexes: []
          reason: Discusses the sensitivity and specificity of the MoCA cutoff.
        unresolved_coverage: []
        pending_source_ids:
        - P3-S1-C6
        - P3-S2-C1
        - P3-S2-C3
        - P4-S2-C3
        - P5-S1-C3
        - P10-S1-C4
        pending_policy: Every result passage without direct candidate evidence remains pending, including model-labelled background and restatements; those labels never certify completeness.
        tables_requiring_review:
        - TABLE-1-page-3-1
        - TABLE-2-page-8-2
        - TABLE-3-page-10-3
        - TABLE-4-page-11-4
        paper_complete: false
        approved: false
        policy: New candidates require independent source checks; coverage dispositions are model suggestions. No original outputs changed.
      study_frame:
        slots:
          analysed_sample:
          - P3-S3-C1
          - P7-S1-C4
          - P14-S1-C3
          recruited_sample:
          - P14-S1-C3
          eligibility:
          - P14-S1-C3
          imaging_provenance:
          - P10-S2-C4
          - P11-S1-C5
          - P11-S1-C6
          - P12-S2-C4
          imaging_timing:
          - P10-S2-C4
          - P11-S1-C6
          outcome_timing:
          - P2-S1-C4
          - P3-S1-C2
          - P5-S2-C4
          - P5-S2-C8
          - P10-S3-C6
          outcome_definition:
          - P2-S1-C4
          - P3-S1-C2
          - P10-S1-C4
          validation: []
          analysis_restrictions: []
          dependent_variable_statement:
          - P5-S1-C4
          - P6-S2-C7
          - P6-S2-C8
          - P6-S3-C3
          limitations:
          - P4-S1-C3
          - P5-S2-C2
          - P13-S1-C6
          personal_factors: []
          tested_personal_effects: []
          adjustment_roles:
          - P7-S1-C3
          explicitly_not_adjusted: []
          descriptive_personal_factors: []
        outcome_type: both_reported
        imaging_vs_outcome: mixed
        validation_type: none_described
        held_selections:
        - slot: dependent_variable_statement
          source_id: P7-S1-C3
          reason: Requires a Methods outcome definition; model selection retained for inspection only
        - slot: dependent_variable_statement
          source_id: P7-S1-C4
          reason: Requires a Methods outcome definition; model selection retained for inspection only
        - slot: dependent_variable_statement
          source_id: P11-S1-C7
          reason: Requires a Methods outcome definition; model selection retained for inspection only
        - slot: dependent_variable_statement
          source_id: P11-S1-C8
          reason: Requires a Methods outcome definition; model selection retained for inspection only
        - slot: dependent_variable_statement
          source_id: P12-S1-C3
          reason: Requires a Methods outcome definition; model selection retained for inspection only
        - slot: dependent_variable_statement
          source_id: P12-S1-C4
          reason: Requires a Methods outcome definition; model selection retained for inspection only
        - slot: dependent_variable_statement
          source_id: P13-S2-C5
          reason: Requires a Methods outcome definition; model selection retained for inspection only
        - slot: validation
          source_id: P13-S2-C2
          reason: No validation-design cue; inspect the source rather than inferring a design
        - slot: tested_personal_effects
          source_id: P5-S2-C11
          reason: No current-result classification; a covariate description is not an individual test
        - slot: tested_personal_effects
          source_id: P5-S3-C1
          reason: No current-result classification; a covariate description is not an individual test
        - slot: tested_personal_effects
          source_id: P5-S3-C2
          reason: No current-result classification; a covariate description is not an individual test
        - slot: tested_personal_effects
          source_id: P5-S3-C3
          reason: No current-result classification; a covariate description is not an individual test
        - slot: tested_personal_effects
          source_id: P6-S1-C4
          reason: No current-result classification; a covariate description is not an individual test
        - slot: tested_personal_effects
          source_id: P6-S2-C2
          reason: No current-result classification; a covariate description is not an individual test
        - slot: tested_personal_effects
          source_id: P6-S2-C3
          reason: No current-result classification; a covariate description is not an individual test
        - slot: tested_personal_effects
          source_id: P6-S2-C5
          reason: No current-result classification; a covariate description is not an individual test
        - slot: tested_personal_effects
          source_id: P7-S2-C1
          reason: No current-result classification; a covariate description is not an individual test
        - slot: tested_personal_effects
          source_id: P7-S2-C3
          reason: No current-result classification; a covariate description is not an individual test
        - slot: tested_personal_effects
          source_id: P7-S2-C5
          reason: No current-result classification; a covariate description is not an individual test
        - slot: tested_personal_effects
          source_id: P7-S2-C6
          reason: No current-result classification; a covariate description is not an individual test
        - slot: tested_personal_effects
          source_id: P9-S1-C3
          reason: No current-result classification; a covariate description is not an individual test
        - slot: tested_personal_effects
          source_id: P11-S1-C7
          reason: No current-result classification; a covariate description is not an individual test
        - slot: tested_personal_effects
          source_id: P11-S1-C8
          reason: No current-result classification; a covariate description is not an individual test
        - slot: tested_personal_effects
          source_id: P12-S1-C3
          reason: No current-result classification; a covariate description is not an individual test
        - slot: tested_personal_effects
          source_id: P12-S1-C4
          reason: No current-result classification; a covariate description is not an individual test
        - slot: tested_personal_effects
          source_id: P13-S2-C2
          reason: No current-result classification; a covariate description is not an individual test
        - slot: personal_factors
          source_ids:
          - P1-S1-C12
          - P5-S2-C9
          - P5-S2-C10
          - P5-S2-C11
          - P5-S3-C1
          - P5-S3-C2
          - P5-S3-C3
          - P6-S1-C4
          - P6-S2-C2
          - P6-S2-C3
          - P6-S2-C5
          - P7-S2-C1
          - P7-S2-C3
          - P7-S2-C5
          - P7-S2-C6
          - P9-S1-C3
          - P13-S1-C4
          - P13-S1-C5
          - P13-S1-C6
          reason: Runaway selection (>8 passages); entire slot requires source review
        - slot: descriptive_personal_factors
          source_ids:
          - P1-S1-C12
          - P5-S2-C9
          - P5-S2-C10
          - P5-S2-C11
          - P5-S3-C1
          - P5-S3-C2
          - P5-S3-C3
          - P6-S1-C4
          - P6-S2-C2
          - P6-S2-C3
          - P6-S2-C5
          - P7-S2-C1
          - P7-S2-C3
          - P7-S2-C5
          - P7-S2-C6
          - P9-S1-C3
          - P13-S1-C4
          - P13-S1-C5
          - P13-S1-C6
          reason: Runaway selection (>8 passages); entire slot requires source review
        policy: All slots and enums remain unverified. Held selections are not evidence of absence. Original response is preserved in frame/raw.json.
      approved: false
      source_check:
        profile: core
        scope: Independent model text review of core meaning; not human approval or complete PDF verification
        binding:
          profile: core
          version: core-source-check-v3
          model: gemma4:31b
          model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
          checker_model: qwen3.8:27b
          checker_digest: 47951e4a666180bc2aedfc93c169472f2de783696fe196efbf063f5730ecf163
          host: http://localhost:11434
          pdf_sha256: 3f10b8323077805b1b142ba70865bc674ad2c3377da82ca8ab9439a559cb1672
          review_sha256: 21b4b527693cef6f9f990166a0152d64c2a417f65c0623da8a7ddf6181f62e7b
          code_sha256: c4650d24fa3e36e6f317cb65cc7626277a28936a7cdf5d07248d4b1e5bfa09aa
          source_helpers_sha256: e0e0f295e5efa1fdb4e9e8c84ca491d062df3aefe8ca8b4d9ca85fcb6d4c9082
          converter_sha256: 048f1e35905528676837a00b1b2406b1c97cb1eb47c48d63f121a5c00cc0afeb
          table_helpers_sha256: 78e562e9725fc484d6a12279ea710856dfd1d9aa13ee178d0358e9c0acdd2c8c
          mapper_budget: 2500
          reviewer_budget: 1600
          approved: false
          visual:
            models:
            - gemma4:31b
            - qwen3.8:27b
            digests:
            - 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
            - 47951e4a666180bc2aedfc93c169472f2de783696fe196efbf063f5730ecf163
            code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
            layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
        approved: false
        core_review:
          own_result_source_ids:
          - P5-S3-C3
          source_result: A neuropathological analysis of >1,300 autopsied patients found that diabetes increased the odds of brain infarcts, particularly lacunes, but not Alzheimer disease pathology.
          result_status: detected
          patient_measurement: non_imaging
          checks:
            analysis_identity:
              answer: fits
              reason: The source P5-S3-C3 explicitly describes a 'neuropathological analysis' of autopsied patients, which matches the proposed analysis label and the nature of the evidence (post-mortem pathology rather than in-vivo imaging).
              source_ids:
              - P5-S3-C3
            direction:
              answer: fits
              reason: The source states diabetes 'increased the odds' of infarcts/lacunes, which aligns with the proposed direction of 'likely' (positive association). The source also notes a lack of association with AD pathology, which is captured in the claim text.
              source_ids:
              - P5-S3-C3
            construct:
              answer: fits
              reason: Exposure is diabetes, outcome is brain infarcts (specifically lacunes). The measurement is neuropathological (autopsy), which is correctly classified as non_imaging. The proposed draft correctly identifies the population as autopsied patients.
              source_ids:
              - P5-S3-C3
            qualifications:
              answer: fits
              reason: The qualification 'specifically associated with lacunes' is supported by the source text 'particularly lacunes'. The limitation regarding the neuropathological/autopsy nature is also correctly included.
              source_ids:
              - P5-S3-C3
            missing_material_caveat:
              answer: fits
              reason: The source explicitly states the finding was 'not' associated with Alzheimer disease pathology. The proposed claim includes this negative finding ('but not Alzheimer disease pathology'), so no material caveat is missing. The sample size (>1300) is mentioned in the source but marked as pending in the draft, which is acceptable for a qualitative draft.
              source_ids:
              - P5-S3-C3
          optional_pending:
          - Sample size (>1300) is mentioned in source but not transcribed to numeric field
          - Specific odds ratios or confidence intervals not transcribed
          verdict: draft
          reason: All five core checks fit the source.
          material_issues: []
        pending_details:
        - Sample size requires source confirmation; it has not been transcribed.
        - Detailed statistics, atlas/reference-space and structured confounder metadata not transcribed.
        - Recovery phase is not classified; use the reported timing words.
        - Evidence-strength rating is a conservative draft placeholder pending human review.
        - Sample size (>1300) is mentioned in source but not transcribed to numeric field
        - Specific odds ratios or confidence intervals not transcribed
        normalizations:
        - field: bucket
          original: predictors
          action: route_from_kind
          value: ingredients
        - field: sample.n
          original: 1300
          action: not_transcribed
          reason: Not supported by selected quotations
        analysis_identity:
          id: R013
          exposure:
            text: diabetes
          outcome:
            text: odds of brain infarcts (particularly lacunes)
          analysis_label: Neuropathological analysis
          relation: association
          evidence_ids:
          - P5-S3-C3
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
            pdf_sha256: 3f10b8323077805b1b142ba70865bc674ad2c3377da82ca8ab9439a559cb1672
            source_review: _compare/relationships-2026-11-16/review-current/Rost2022
            source_status_sha256: 526d3f07ec746cc7184d2a9429c4133fb7fa6cef70af0778c6d37baab8c94b4e
            code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
            version: candidate-inventory-v1
        paper_complete: false
        visual_prose_readings: {}
        remaining:
        - Human PDF review and approval
        - Pending metadata enrichment
        - Main Results, figures and tables completeness check
    reviewer_marks:
    - id: relationship-source-check
      page: 5
      quote: "For instance, a neuropatho-\nlogical analysis of more than 1.300 autopsied patients \nwith diabetes found that diabetes increased the odds \nof brain infarcts, particularly lacunes, but not Alzheimer \ndisease (AD) pathology.68 As detailed below, the burden \n\n"
      status: pending
      by: agent:relationship-converter
      date: '2026-11-25'
      note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor roles, all qualifiers, source audit issues and main-PDF tables/figures; check missing results. This model proposal is not verified.'
  original_mapping:
    decision: draft
    reason: The source provides a specific finding from a neuropathological analysis of autopsied patients regarding the association between diabetes and the odds of brain infarcts (specifically lacunes).
    bucket: predictors
    entity_id: diabetes
    name: diabetes
    kind: ingredient
    predictor_type: clinical
    definition: presence of diabetes measured via neuropathological analysis of autopsied patients
    assessment: []
    target: brain_infarcts
    target_kind: impairment
    claim: diabetes increased the odds of brain infarcts, particularly lacunes, but not Alzheimer disease pathology
    direction: likely
    method: behavioral_only
    relationship: correlational
    therapy: null
    sample_n: 1300
    population: autopsied patients
    timing: post-mortem
    qualifications:
    - specifically associated with lacunes
    limitations:
    - finding based on neuropathological analysis of autopsied patients
    optional_pending: []
    evidence_quality: cohort
    passages:
    - source_id: P5-S3-C3
      supports: claim
    - source_id: P5-S3-C3
      supports: sample
    - source_id: P5-S3-C3
      supports: method
  original_attempt:
    binding:
      profile: core
      version: core-source-check-v3
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      checker_model: qwen3.8:27b
      checker_digest: 47951e4a666180bc2aedfc93c169472f2de783696fe196efbf063f5730ecf163
      host: http://localhost:11434
      pdf_sha256: 3f10b8323077805b1b142ba70865bc674ad2c3377da82ca8ab9439a559cb1672
      review_sha256: 21b4b527693cef6f9f990166a0152d64c2a417f65c0623da8a7ddf6181f62e7b
      code_sha256: c4650d24fa3e36e6f317cb65cc7626277a28936a7cdf5d07248d4b1e5bfa09aa
      source_helpers_sha256: e0e0f295e5efa1fdb4e9e8c84ca491d062df3aefe8ca8b4d9ca85fcb6d4c9082
      converter_sha256: 048f1e35905528676837a00b1b2406b1c97cb1eb47c48d63f121a5c00cc0afeb
      table_helpers_sha256: 78e562e9725fc484d6a12279ea710856dfd1d9aa13ee178d0358e9c0acdd2c8c
      mapper_budget: 2500
      reviewer_budget: 1600
      approved: false
      visual:
        models:
        - gemma4:31b
        - qwen3.8:27b
        digests:
        - 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        - 47951e4a666180bc2aedfc93c169472f2de783696fe196efbf063f5730ecf163
        code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
        layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
    proposal: R013
    status: draft
    reason: All five core checks fit the source.
    material_issues: []
    path: drafts/ingredients/diabetes__Rost2022__R013.md
    seconds_this_run: 64.11945687499247
  source_check:
    profile: agent-repair
    scope: Agent source reconstruction; original model reviews do not certify the changed record. No independent model pass or human approval.
    approved: false
    paper_complete: false
    binding:
      pdf_sha256: 3f10b8323077805b1b142ba70865bc674ad2c3377da82ca8ab9439a559cb1672
      original_mapping_sha256: a33ad67c103bb9fdf51c03810a5363c2a94b8fd9c141dedc4349376776089127
      original_status_sha256: bad1ec89aa2756e931028613a62b70f3d82ad9f3a2c8bfac60a63b2b912c8def
      evidence_sha256: 04b01d22d31311988530423b0dd362f69d64f554f589769e79d86bc83c17144d
    publication_correction:
      by: agent:source-repair
      date: '2026-11-26T02:05:16.806224+00:00'
      pdf_pages:
      - 1
      - 5
      - 12
      - 13
      - 18
      - 19
      - 20
      note: Reclassified as a secondary review report, explicitly attributing the result to the autopsy study cited as reference 68. This is not a new primary sample or independent replication; quantitative estimates and study-level attribution require human verification against the primary publication.
      approved: false
      audit: logs/publication/draft-repairs-2026-11-26-round2.json
    remaining:
    - Human source review and approval
    - Full paper completeness review
reviewer_marks:
- id: relationship-source-check
  page: 5
  quote: "For instance, a neuropatho-\nlogical analysis of more than 1.300 autopsied patients \nwith diabetes found that diabetes increased the odds \nof brain infarcts, particularly lacunes, but not Alzheimer \ndisease (AD) pathology.68 As detailed below, the burden \n\n"
  status: pending
  by: agent:relationship-converter
  date: '2026-11-25'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor roles, all qualifiers, source audit issues and main-PDF tables/figures; check missing results. This model proposal is not verified.'
- id: source-repair-round2
  status: pending
  by: agent:source-repair
  date: '2026-11-26'
  note: Reclassified as a secondary review report, explicitly attributing the result to the autopsy study cited as reference 68. This is not a new primary sample or independent replication; quantitative estimates and study-level attribution require human verification against the primary publication.
---

# Source review required

This repaired draft remains unapproved. Original outputs and review provenance are preserved.
