---
id: left_supramarginal_gyrus_phonematic_cluster
name: left supramarginal gyrus cluster
kind: network
findings:
- id: f1
  target_audit:
    status: behaviour_label_present
    category: behaviour_or_language_construct
    original_target: phonematic_structure_impairment
    reason: Label names a behaviour or language construct; its exact operational definition and measurement
      still need source review.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  outcome_measurement:
    status: needs_source_review
    instruments: []
    note: Outcome instrument/task is not yet verified for this finding. Do not infer it from the predictor
      or a paper-wide test list.
  target: phonematic_structure_impairment
  target_kind: impairment
  claim: Damage to the left supramarginal gyrus is significantly associated with impairment
    of phonematic structure in spontaneous speech, such that patients with damage
    to this area present significantly more phonematic errors than patients with an
    intact left supramarginal gyrus.
  direction: likely
  relationship: correlational
  method: VLSM
  sample:
    n: not_reported
    population: First-ever left-hemispheric ischaemic stroke patients with chronic
      aphasia
    phase: not_reported
    time_post_onset: Chronic phase (mean time post-stroke 12.6 months)
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Voxel-based lesion-symptom mapping may favour larger lesions to contribute to
    overall results
  - Chronic aphasia timing may sharpen the distinction between large lesion areas
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Patient lesion overlap with a voxel-wise map of the
    left supramarginal gyrus. Analysis based on semi-standardized rating of spontaneous
    speech within the Aachen Aphasia Test. Additional metadata has not been transcribed;
    review the pending-field flags before approval. PDF image reading (P3-S1-C9, two-model
    agreement, human verification pending): . Mean age of these participants was 52
    years [standard devi-

    ation (SD) = 12 years] and mean time post-stroke was 12.6 months

    (SD = 20.0 months; see Supplementary Table 1 for more details on the

    patient cohort) Original text-layer quotation is preserved below.'
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
    - not_transcribed:sample.n
    - proposed_concept:phonematic_structure_impairment
  citation: '@Henseler2014'
  source_passages:
  - section: Original source P5-S2-C4
    page: 5
    quote: 'For the level ‘phonematic structure’, there

      was a signiﬁcant association between behavioural impairment and

      damage to the left supramarginal gyrus (Fig. 4), i.e. patients with

      damage to this area presented signiﬁcantly more phonematic

      errors

      in

      spontaneous

      speech

      than

      patients

      with

      intact

      Figure 2 Aphasia syndromes.'
    supports: claim
  - section: Original source P10-S2-C3
    page: 10
    quote: 'Another dimension of spontaneous speech rating, ‘phonematic

      structure’, yielded circumscribed VLSM results in the left supra-

      marginal gyrus (Fig. 4).'
    supports: claim
  - section: Original source P3-S1-C7
    page: 3
    quote: 'The initial search yielded 1167

      patients who had undergone extensive language testing; 1093 were

      excluded, because they did not fulﬁl our inclusion criteria, which were:

      (i) single left-hemispheric ischaemic stroke in the middle cerebral artery

      territory; (ii) right handedness; (iii) native speakers of German; (iv)

      normal language development; (v) no concomitant severe microangio-

      pathy; (v) no dementia or other neurodegenerative disease; (vii) no

      pre-stroke history of psychiatric or neurological disease; and (viii) high

      resolution MRI available.'
    supports: sample
  - section: Original source P3-S1-C9
    page: 3
    quote: 'Mean age of these participants was 52 years [standard devi-

      ation (SD) = 12 years] and mean time post-stroke was 12.6 months

      (SD = 20.0 months; see Supplementary Table 1 for more details on the

      patient cohort).'
    supports: sample
  - section: Original source P4-S2-C8
    page: 4
    quote: 'Performance scores

      are statistically compared between groups by T-statistics as has been

      recently recommended by Medina et al. (2010).'
    supports: method
  - section: Original source P3-S3-C2
    page: 3
    quote: 'In detail spontaneous

      speech is scored for (i) communicative abilities; (ii) articulation and

      prosody; (iii) phonematic structure; (iv) semantic structure; (v) syntac-

      tic structure; and (vi) speech automatisms.'
    supports: method
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-24'
relationship_review:
  paper: Henseler2014
  proposal_id: R006
  review_status_sha256: ce9f7d622eb6325d8e241907f052309c0d89a28f2ac8bcdabd6732886e4a5bcd
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 2ab275d0f2cac9a302deb7e4615b84e288bff989d5a46b17468f75286daac4b9
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 2ab275d0f2cac9a302deb7e4615b84e288bff989d5a46b17468f75286daac4b9
        A/passages.json: 09b26048c8facaecdc7f2242f81f3d4f8d7b896f30975ed9bad8f1d4084cf00e
        A/raw.json: 26f1a47a061fcf6403787c6f1c35fa66d3bd28794b8a37779c96702a143c0264
        A/source-units.json: 6664e4cbd67d59e6c71be410b4557b6f8323deae012774a474efd2ae5f960613
        A/full-source-units.json: 950f39333a11dfd63157f898024978a8bcd713848e87e886024d1f72f53eddd0
        A/meta.json: d20b2cbd8c3324b18797ade905c953bd4d1083561f4ef5abff1d77ac231ef317
        A/table-images/page-4.png: 106a23aa9f2b0fcdda1d46ef0609b9795a05cd89e0089648aa40882fa18f7632
        A/table-images/TABLE-1-page-4-1.png: 724d3e46680eabfad5fcabc4ae3824b5195b8090949a986556b73f01d41eda98
        A/table-images/manifest.json: 956ba1df00b3905aef9f4f2858b0c6b24218081ec89ed4494de8a27b9658687d
        A/clauses/window-11/raw.json: 1fdf14e0da1983bdccc111f65dd024ba8e056b38d5ce82c901ed0bfc3040456e
        A/clauses/window-11/prompt.txt: aada5b4f0def3c4f859be5b2f0c3c8576f67fae79d51dcaee0d358de1e06aeda
        A/clauses/window-11/meta.json: 8968340058261e5a46f5619f9804dfea99ad1998ec62c0a9194b33d34b1d6873
        A/clauses/window-10/raw.json: 6ab32cbe8a52ff7cee779762a576bc24e5a51d423ed3d1ef4fde43f128eaf78b
        A/clauses/window-10/prompt.txt: 83ff980c90bff0e2dce9396a53601f1aa9cab7f95a5fd3adbae33afeec08579b
        A/clauses/window-10/meta.json: f95dc01f24dd724974de87dea1a6b6e81d717e50d07010860ff9cd22f741ff65
        A/clauses/window-03/raw.json: e50c8c0fff93fb0d791dd3a121e96e43f67c1f15fa0c89795510ef99c4debe8d
        A/clauses/window-03/prompt.txt: 9c8f9468f839841179b169414cc43b019c5e14ea218eac14fbfd194784dc3bd4
        A/clauses/window-03/meta.json: 03df28bd48c08fb62dbb03e6efec0b48a93f760457d0c6e6346bb88f7f870575
        A/clauses/window-04/raw.json: 0eb439f2d3bf589d2f42a765c795b642078caf1e9437f084d550fc8fa5506c87
        A/clauses/window-04/prompt.txt: 77bc0ea688ce9d9d84a2c5a4a001d71b4169fe7d5c9cc69fc917a18af202d3bf
        A/clauses/window-04/meta.json: d638dfe5501fb48e80b50f4498332d2837a269b261ad852cba4537d7ec34f627
        A/clauses/window-05/raw.json: 0252fe26ae4fb188c17041cd166b680b80a1ea4324b1f1a145bd9e8758ef7bbe
        A/clauses/window-05/prompt.txt: 2dd982f5435d7594cb4cb346246a1ddd95f89f02c5d5a8a0990f7b2099cbfb68
        A/clauses/window-05/meta.json: 4780a29c0afd84268a227a6017060e9341a55e50849a85ad2e903d3b81902559
        A/clauses/window-02/raw.json: c45bab7464b0e8288dfa4a33267a907618db3bdffdfc3acaf903f545ae2b2333
        A/clauses/window-02/prompt.txt: f2a7b3840bd8468a6e24246f6975da7827358fc9fd6cc49eaa45c26cf655a3b5
        A/clauses/window-02/meta.json: abe12f4890f25107f4dc18061f84564d9e8da49627b8e29c154237b06ea870b3
        A/clauses/window-09/raw.json: ec10848f168adabc3a4f26ff37b8bf495fbf00f2793901437b2600323a4172dc
        A/clauses/window-09/prompt.txt: 6969771fe00fa88c1f3f09f25422dd02442314fe8ffdf482c9eb1fdb0a23c5d2
        A/clauses/window-09/meta.json: 739edbd4bdb9151dc2a922bae97af511faba779df95f830bfc8a0042c0cd6d15
        A/clauses/window-07/raw.json: 3ad25f86b1965fab4d328bdc66f4f460ea90cfbc028ea89d1fb57296aa83f0e3
        A/clauses/window-07/prompt.txt: d901b7791e8f55f6f359240fbf91d58760f4266628b1f407f93dd528f0304a06
        A/clauses/window-07/meta.json: 0ca29f3ded2208e0d930b0ab4c80fac577c4298a7d493ab51e23ee9f15b4411c
        A/clauses/window-01/raw.json: a65a64674e64d03df42dbc82548be18938e7a3ce432f2281fb03d1ca21412827
        A/clauses/window-01/prompt.txt: 209e91acc12493559ff7bb2126e41251b9daaa54e0349f4f6ff9654bc738a2cf
        A/clauses/window-01/meta.json: f585aebb93b1beca46b32bf76c97ea5816e1afc25ec6979d79c684a175324304
        A/clauses/window-06/raw.json: 679b24c8dd20b654c132efbf1cd51a7c16fa3750ba4979ede9a0d1ff56c0f112
        A/clauses/window-06/prompt.txt: dc52f63515718a95d3e49e3602c4a1fcf5ebe031c5f9fe997b9ab959306b48f7
        A/clauses/window-06/meta.json: d493294fca6c56b7db78dc6b794a6073c911e300b6ebaf31a78e42241e0f8737
        A/clauses/window-08/raw.json: 4eb379ac061eeb114ce99a09667b507b0b78e090645c5bd0fa182bc83432ae7d
        A/clauses/window-08/prompt.txt: c19e379a9e1b44fbb68fbac006f3d49e0df5257c2fa7a2fdfce3f76ca65fad6c
        A/clauses/window-08/meta.json: 0ea6a6ac6cda468f91b3a387f0ff596b0ed489fe753bd500b95ac55ea91c91b1
        A/tables/TABLE-1-page-4-1/raw.json: 50fc92b7c5c98a7a41fc59c9e76085356f687d8010d328d4052b2dcd8c71f9eb
        A/tables/TABLE-1-page-4-1/prompt.txt: af1f2b881fcb63a0f304b10c5df295636ec027ee1411395fcfc1ac187528d090
        A/tables/TABLE-1-page-4-1/meta.json: 24b66f0cf0aa6b69ce7a8b2d2e10d2808984dcc04e11a23b60d462cd170d2251
        B/passages.json: 09b26048c8facaecdc7f2242f81f3d4f8d7b896f30975ed9bad8f1d4084cf00e
        B/raw.json: 32912c533e1a0f5c89c149c6301a3c876d45e89a487c3004adeb127b0f702dfe
        B/source-units.json: 6664e4cbd67d59e6c71be410b4557b6f8323deae012774a474efd2ae5f960613
        B/full-source-units.json: 950f39333a11dfd63157f898024978a8bcd713848e87e886024d1f72f53eddd0
        B/meta.json: 04ddd7a36327eb9bde077eae319b04b07b08dcc4bda5cce79a64688fb20b6ed4
        B/table-images/page-4.png: 106a23aa9f2b0fcdda1d46ef0609b9795a05cd89e0089648aa40882fa18f7632
        B/table-images/TABLE-1-page-4-1.png: 724d3e46680eabfad5fcabc4ae3824b5195b8090949a986556b73f01d41eda98
        B/table-images/manifest.json: c103f4460382c7f15341938fdfe8f4260d34bba856ca146f190b26be8fec83b7
        B/clauses/window-11/raw.json: 1fdf14e0da1983bdccc111f65dd024ba8e056b38d5ce82c901ed0bfc3040456e
        B/clauses/window-11/prompt.txt: aada5b4f0def3c4f859be5b2f0c3c8576f67fae79d51dcaee0d358de1e06aeda
        B/clauses/window-11/meta.json: b87bb6006b863b28ee5fe63addfd26f70d11ebd5b4d984b91264da5f7670e4f6
        B/clauses/window-10/raw.json: b16b38c6083d31427a215a97dafbb07911a2fa1766d6b99db0452637ce40b3a1
        B/clauses/window-10/prompt.txt: 83ff980c90bff0e2dce9396a53601f1aa9cab7f95a5fd3adbae33afeec08579b
        B/clauses/window-10/meta.json: 38c091ca58c723bbf7741440c362c57cc06522d015ff51b97a3adbefcf0e6ac3
        B/clauses/window-03/raw.json: e7dbe572e72c1b4126184a92fe47c11012b8b3c7fcf3d3c3ac0dab47b5e9024d
        B/clauses/window-03/prompt.txt: 9c8f9468f839841179b169414cc43b019c5e14ea218eac14fbfd194784dc3bd4
        B/clauses/window-03/meta.json: edaf7032ecad8be03d5c63772c0f61d1922284cdff487c6ad5268680e540e646
        B/clauses/window-04/raw.json: 2ffcf9d5da43c076dacead13aa6de2453c3e5718c431f7cb61eb68c2f92f656a
        B/clauses/window-04/prompt.txt: 77bc0ea688ce9d9d84a2c5a4a001d71b4169fe7d5c9cc69fc917a18af202d3bf
        B/clauses/window-04/meta.json: 42ea04cce1a3b84ec4a24bc8028d5e81226dc509d814c0753677bb51686bae24
        B/clauses/window-05/raw.json: e46fe797ef471ed8661eb1e2383ad0d92f7f26adf24ac8b0eee4beca4d9ba867
        B/clauses/window-05/prompt.txt: 2dd982f5435d7594cb4cb346246a1ddd95f89f02c5d5a8a0990f7b2099cbfb68
        B/clauses/window-05/meta.json: 6abaf871406379268e727c085948d8a056135a52d506caada943463cb0b87519
        B/clauses/window-02/raw.json: 151375f7da511619af6f5fa6a6bd24cb214afb70282da88ffa1fef49890bc514
        B/clauses/window-02/prompt.txt: f2a7b3840bd8468a6e24246f6975da7827358fc9fd6cc49eaa45c26cf655a3b5
        B/clauses/window-02/meta.json: ff2e6716656bc8661d740bafe2dc6fd2724a71c57ecf479336334c14471fc43f
        B/clauses/window-09/raw.json: 49a49e4e589357fb28e0a394797f38f1bd297240637a4970c41a36c12c748867
        B/clauses/window-09/prompt.txt: 6969771fe00fa88c1f3f09f25422dd02442314fe8ffdf482c9eb1fdb0a23c5d2
        B/clauses/window-09/meta.json: bc6351e50450debdbc2923b37c18fcf7c1af0f10154bfe3e4b4bf85dbdd8b344
        B/clauses/window-07/raw.json: 16a4a74718a9775303c0c97c9bbcdeeb086904b679668afe45559d7d12e338f8
        B/clauses/window-07/prompt.txt: d901b7791e8f55f6f359240fbf91d58760f4266628b1f407f93dd528f0304a06
        B/clauses/window-07/meta.json: 14f24a04c02477642bec63b6fa968f195f0d5a3990ea645a60d6eb49d1848f10
        B/clauses/window-01/raw.json: aae3aa42710fe0f67bf725aeaebc55ef952e0ddd147ea7954c84fd29307ff175
        B/clauses/window-01/prompt.txt: 209e91acc12493559ff7bb2126e41251b9daaa54e0349f4f6ff9654bc738a2cf
        B/clauses/window-01/meta.json: 239cb519bccc1e22e11810805c5014d0074a19558fa990c43a4a8e4ef42b44b4
        B/clauses/window-06/raw.json: cd866913be2ac448af5e93523c18f541fd6a55c9edb391eb9936ed9fe4cb99ba
        B/clauses/window-06/prompt.txt: dc52f63515718a95d3e49e3602c4a1fcf5ebe031c5f9fe997b9ab959306b48f7
        B/clauses/window-06/meta.json: 006561bbcfea8cbd9e83de0caac90fcfb22a474bc0947324c0485dc48312b0ac
        B/clauses/window-08/raw.json: 9590534d01ae3ac0ebee946192bf2eec6c83a42187c23cb1f60e88bff39f78b5
        B/clauses/window-08/prompt.txt: c19e379a9e1b44fbb68fbac006f3d49e0df5257c2fa7a2fdfce3f76ca65fad6c
        B/clauses/window-08/meta.json: 65716e118c549d3ec2490a29492bb5b9788877a2347a97e4edef01a9aaaf1510
        B/tables/TABLE-1-page-4-1/raw.json: 5789cd3331b587076b4a5bffefeacc94772750e8bcaf14c99ee0f357d7bf0007
        B/tables/TABLE-1-page-4-1/prompt.txt: af1f2b881fcb63a0f304b10c5df295636ec027ee1411395fcfc1ac187528d090
        B/tables/TABLE-1-page-4-1/meta.json: 823a576cab22fac70f06a04946d331381e7921955e0710e1fe846e33b86e7928
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
      pdf_sha256: 2ab275d0f2cac9a302deb7e4615b84e288bff989d5a46b17468f75286daac4b9
      source_review: _compare/relationships-2026-11-16/review-current/Henseler2014
      source_status_sha256: f7d11cc041dd647fc0d4191212ab8e276734e8027b57f397a18a95e69e39fad3
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R006
    exposure:
      text: phonematic structure impairment
    outcome:
      text: brain lesion location
    analysis_label: Spontaneous Speech VLSM
    relation: association
    evidence_ids:
    - P5-S2-C4
    - P10-S2-C3
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
      pdf_sha256: 2ab275d0f2cac9a302deb7e4615b84e288bff989d5a46b17468f75286daac4b9
      source_review: _compare/relationships-2026-11-16/review-current/Henseler2014
      source_status_sha256: f7d11cc041dd647fc0d4191212ab8e276734e8027b57f397a18a95e69e39fad3
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P3-S2-C11
      - Result passage disposed without unit P3-S2-C5
      - Result passage disposed without unit P3-S2-C7
      - Result passage disposed without unit P3-S2-C8
      - Result passage disposed without unit P5-S1-C6
      - Result passage disposed without unit P6-S1-C8
      - Result passage disposed without unit P6-S3-C5
      - Result passage disposed without unit P8-S1-C1
      - Result passage disposed without unit P8-S1-C2
      - Result passage disposed without unit P8-S1-C4
      - Result passage disposed without unit P8-S1-C5
      - Result passage disposed without unit P8-S1-C6
      - Accounting without a linked unit P9-S3-C4
      - Accounting without a linked unit P9-S3-C5
      - Accounting without a linked unit P9-S3-C6
      - Accounting without a linked unit P9-S3-C7
      - Accounting without a linked unit P9-S3-C8
      - Accounting without a linked unit P9-S3-C9
      - Unaccounted source passage P9-S3-C7
      - Unaccounted source passage P9-S3-C9
      - Unaccounted source passage P9-S3-C5
      - Unaccounted source passage P9-S3-C6
      - Unaccounted source passage P9-S3-C8
      - Unaccounted source passage P9-S3-C4
      - Result passage disposed without unit P10-S1-C4
      - Result passage disposed without unit P10-S1-C7
      - Accounting without a linked unit P10-S1-C8
      - Accounting without a linked unit P10-S2-C3
      - Result passage disposed without unit P10-S2-C7
      - Unaccounted source passage P10-S1-C8
      - Unaccounted source passage P10-S2-C3
      - Result passage disposed without unit P11-S3-C10
      - Result passage disposed without unit P11-S3-C11
      - Result passage disposed without unit P11-S3-C3
      - Accounting without a linked unit P11-S4-C4
      - Accounting without a linked unit P12-S1-C1
      - Unaccounted source passage P11-S4-C4
      - Unaccounted source passage P12-S1-C1
      unattached_null_or_qualifier_ids:
      - P3-S2-C7
      - P8-S1-C1
      - P8-S1-C4
      suppressed_nonrepresented_units: 15
      default_disposition_count_requires_completeness_check: 203
      unselected_timing_passages:
      - P1-S1-C7
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P5-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C13
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S2-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S2-C3
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
        source_id: P6-S2-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S2-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S2-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S2-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S2-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S2-C12
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S3-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S3-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S3-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S3-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S3-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S3-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S3-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C12
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C13
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C14
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C15
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C16
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S1-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S1-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S1-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S1-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S1-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S1-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S1-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S1-C12
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S2-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S2-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S2-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S2-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S2-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S2-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S2-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S2-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S2-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S2-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S2-C12
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S2-C13
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S3-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S3-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S3-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S3-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S3-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S3-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S3-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S3-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S3-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P3-S2-C11
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: outcome_definition
        source_ids:
        - P1-S2-C2
        - P1-S2-C3
        - P3-S3-C3
        - P3-S3-C4
        - P3-S3-C5
        - P3-S3-C6
        - P4-S3-C1
        - P4-S3-C2
        - P4-S3-C3
        - P4-S3-C4
        - P4-S3-C5
        - P5-S1-C1
        - P5-S1-C5
        - P5-S1-C13
        - P6-S1-C6
        - P6-S1-C7
        - P6-S1-C8
        - P6-S1-C9
        - P6-S1-C10
        - P6-S2-C2
        - P6-S2-C3
        - P6-S2-C4
        - P6-S2-C5
        - P6-S2-C6
        - P6-S2-C7
        - P6-S2-C8
        - P6-S2-C9
        - P6-S2-C10
        - P6-S2-C11
        - P6-S2-C12
        - P6-S3-C3
        - P6-S3-C4
        - P6-S3-C5
        - P6-S3-C6
        - P6-S3-C7
        - P6-S3-C8
        - P6-S3-C9
        - P7-S1-C1
        - P7-S1-C12
        - P7-S1-C13
        - P7-S1-C14
        - P7-S1-C15
        - P7-S1-C16
        - P8-S1-C4
        - P8-S1-C5
        - P8-S1-C6
        - P9-S1-C3
        - P9-S1-C4
        - P9-S1-C5
        - P10-S1-C1
        - P10-S1-C3
        - P10-S1-C4
        - P10-S1-C5
        - P10-S1-C7
        - P10-S1-C8
        - P10-S1-C9
        - P10-S1-C10
        - P10-S1-C11
        - P10-S1-C12
        - P10-S2-C1
        - P10-S2-C2
        - P10-S2-C3
        - P10-S2-C4
        - P10-S2-C5
        - P10-S2-C7
        - P10-S2-C8
        - P10-S2-C9
        - P10-S2-C10
        - P10-S2-C11
        - P10-S2-C12
        - P10-S2-C13
        - P10-S3-C2
        - P10-S3-C3
        - P10-S3-C4
        - P10-S3-C5
        - P10-S3-C6
        - P10-S3-C7
        - P10-S3-C8
        - P10-S3-C9
        - P10-S3-C10
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: limitations
        source_ids:
        - P11-S3-C6
        - P11-S3-C7
        - P11-S3-C8
        - P11-S3-C9
        - P11-S3-C10
        - P11-S3-C11
        - P12-S1-C1
        - P12-S1-C2
        - P12-S1-C3
        - P12-S1-C4
        - P12-S1-C5
        - P12-S1-C6
        - P12-S1-C7
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - outcome_definition
      - validation
      - limitations
      - personal_factors
      - tested_personal_effects
      - explicitly_not_adjusted
      unclassified_extraction_ids:
      - P2-S2-C11
      table_review_required:
      - TABLE-1-page-4-1
      unlinked_tables: []
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P3-S2
        - P3-S3
        - P5-S1
        - P5-S2
        - P6-S1
        - P6-S2
        - P6-S3
        - P7-S1
        - P7-S2
        - P8-S2
        - P9-S3
        - P10-S2
        - P10-S3
        - P11-S1
        - P11-S2
        - P11-S3
        - P12-S1
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 2ab275d0f2cac9a302deb7e4615b84e288bff989d5a46b17468f75286daac4b9
      source_review: _compare/relationships-2026-11-16/review-current/Henseler2014
      source_status_sha256: f7d11cc041dd647fc0d4191212ab8e276734e8027b57f397a18a95e69e39fad3
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S2-C4
      disposition: represented
      result_indexes:
      - 0
      - 1
      - 4
      - 5
      - 6
      - 7
      - 8
      - 9
      - 10
      - 11
      - 12
      - 13
      - 14
      - 15
      - 16
      - 17
      - 18
      - 19
      - 20
      - 21
      - 22
      - 23
      reason: Abstract summary of findings
    - source_id: P1-S2-C5
      disposition: represented
      result_indexes:
      - 0
      - 1
      - 2
      - 3
      reason: Abstract summary of syndrome results
    - source_id: P3-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient classification counts
    - source_id: P3-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient classification counts
    - source_id: P3-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient classification counts
    - source_id: P3-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient severity counts
    - source_id: P3-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient severity counts
    - source_id: P3-S2-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Cohort comparison
    - source_id: P5-S1-C5
      disposition: represented
      result_indexes:
      - 0
      - 1
      reason: Syndrome VLSM results
    - source_id: P5-S1-C6
      disposition: represented
      result_indexes:
      - 0
      - 1
      reason: Syndrome VLSM overlap
    - source_id: P5-S1-C7
      disposition: represented
      result_indexes:
      - 0
      reason: Broca's lesion site
    - source_id: P5-S1-C8
      disposition: represented
      result_indexes:
      - 1
      reason: Wernicke's lesion site
    - source_id: P5-S1-C10
      disposition: represented
      result_indexes:
      - 2
      reason: Global aphasia lesion site
    - source_id: P5-S1-C11
      disposition: represented
      result_indexes:
      - 2
      reason: Global aphasia lesion site
    - source_id: P5-S1-C12
      disposition: represented
      result_indexes:
      - 3
      reason: Amnestic aphasia null result
    - source_id: P5-S1-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Introductory statement to spontaneous speech results
    - source_id: P5-S2-C2
      disposition: represented
      result_indexes:
      - 4
      reason: Articulation lesion site
    - source_id: P5-S2-C3
      disposition: represented
      result_indexes:
      - 4
      reason: Articulation lesion site
    - source_id: P5-S2-C4
      disposition: represented
      result_indexes:
      - 5
      reason: Phonematic structure lesion site
    - source_id: P6-S1-C1
      disposition: repeated
      result_indexes:
      - 5
      reason: Restatement of phonematic structure result
    - source_id: P6-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: General observation on lesion specificity
    - source_id: P6-S1-C3
      disposition: represented
      result_indexes:
      - 6
      - 7
      reason: Semantic and syntactic structure lesion sites
    - source_id: P6-S1-C4
      disposition: represented
      result_indexes:
      - 8
      reason: Communication/automatisms lesion sites
    - source_id: P6-S1-C5
      disposition: represented
      result_indexes:
      - 9
      reason: Token test lesion site
    - source_id: P6-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Introductory statement to subtests
    - source_id: P6-S1-C7
      disposition: represented
      result_indexes:
      - 10
      reason: Speech repetition lesion site
    - source_id: P6-S1-C8
      disposition: represented
      result_indexes:
      - 11
      reason: Repetition complexity lesion sites
    - source_id: P6-S1-C9
      disposition: represented
      result_indexes:
      - 11
      reason: Repetition complexity lesion sites
    - source_id: P6-S1-C10
      disposition: represented
      result_indexes:
      - 12
      reason: Language comprehension lesion site
    - source_id: P6-S2-C1
      disposition: repeated
      result_indexes:
      - 12
      reason: Restatement of comprehension result
    - source_id: P6-S2-C2
      disposition: represented
      result_indexes:
      - 12
      reason: Language comprehension lesion site
    - source_id: P6-S2-C3
      disposition: represented
      result_indexes:
      - 13
      - 14
      reason: Written language and picture naming results
    - source_id: P6-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Introductory statement to additional tests
    - source_id: P6-S2-C5
      disposition: represented
      result_indexes:
      - 15
      reason: General picture naming lesion site
    - source_id: P6-S2-C6
      disposition: represented
      result_indexes:
      - 16
      reason: Living vs non-living naming lesion site
    - source_id: P6-S2-C7
      disposition: represented
      result_indexes:
      - 16
      reason: Living vs non-living naming lesion site
    - source_id: P6-S2-C8
      disposition: represented
      result_indexes:
      - 17
      reason: Compound vs single noun naming lesion site
    - source_id: P6-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Introductory statement to speeded naming
    - source_id: P6-S2-C10
      disposition: represented
      result_indexes:
      - 18
      reason: Speeded naming lesion site
    - source_id: P6-S2-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Introductory statement to lexico-semantics
    - source_id: P6-S2-C12
      disposition: represented
      result_indexes:
      - 19
      reason: Synonym judgment lesion site
    - source_id: P6-S2-C13
      disposition: represented
      result_indexes:
      - 20
      reason: Semantic differentiation lesion site
    - source_id: P6-S3-C3
      disposition: represented
      result_indexes:
      - 20
      reason: Semantic differentiation lesion site
    - source_id: P6-S3-C4
      disposition: represented
      result_indexes:
      - 20
      reason: Semantic differentiation lesion site
    - source_id: P6-S3-C5
      disposition: represented
      result_indexes:
      - 21
      reason: Word fluency lesion site
    - source_id: P7-S1-C1
      disposition: represented
      result_indexes:
      - 21
      reason: Word fluency network
    - source_id: P7-S1-C4
      disposition: represented
      result_indexes:
      - 22
      reason: Speech repetition sensitivity result
    - source_id: P7-S1-C5
      disposition: represented
      result_indexes:
      - 23
      reason: Written language sensitivity result
    - source_id: P8-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: General subtest intercorrelations
    - source_id: P8-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: General syndrome-subtest correlations
    - source_id: P8-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: General AAT construction validation
    - source_id: P8-S1-C4
      disposition: represented
      result_indexes:
      - 24
      reason: Regular vs time-constraint naming correlation
    - source_id: P8-S1-C5
      disposition: represented
      result_indexes:
      - 24
      reason: Regular vs time-constraint naming correlation
    - source_id: P8-S1-C6
      disposition: represented
      result_indexes:
      - 25
      reason: Time-constraint naming vs executive function correlation
    - source_id: P9-S1-C3
      disposition: represented
      result_indexes:
      - 0
      reason: Broca's lesion site
    - source_id: P9-S1-C4
      disposition: represented
      result_indexes:
      - 1
      reason: Wernicke's lesion site
    - source_id: P9-S3-C4
      disposition: represented
      result_indexes:
      - 2
      reason: Global aphasia lesion site
    - source_id: P9-S3-C7
      disposition: represented
      result_indexes:
      - 3
      reason: Amnestic aphasia null result
    - source_id: P10-S1-C8
      disposition: represented
      result_indexes:
      - 4
      reason: Articulation lesion site
    - source_id: P10-S2-C3
      disposition: represented
      result_indexes:
      - 5
      reason: Phonematic structure lesion site
    - source_id: P10-S2-C9
      disposition: represented
      result_indexes:
      - 10
      reason: Speech repetition lesion site
    - source_id: P10-S3-C5
      disposition: represented
      result_indexes:
      - 22
      reason: Speech repetition sensitivity result
    - source_id: P10-S3-C8
      disposition: represented
      result_indexes:
      - 12
      reason: Language comprehension lesion site
    - source_id: P10-S3-C10
      disposition: represented
      result_indexes:
      - 7
      reason: Syntactic structure lesion site
    - source_id: P11-S1-C6
      disposition: represented
      result_indexes:
      - 19
      - 20
      reason: Lexico-semantic processing lesion site
    - source_id: P11-S1-C8
      disposition: represented
      result_indexes:
      - 21
      reason: Semantic fluency lesion site
    - source_id: P11-S1-C9
      disposition: represented
      result_indexes:
      - 15
      reason: General picture naming lesion site
    - source_id: P11-S2-C5
      disposition: represented
      result_indexes:
      - 16
      reason: Living vs non-living naming lesion site
    - source_id: P11-S2-C7
      disposition: represented
      result_indexes:
      - 18
      reason: Speeded naming lesion site
    - source_id: P11-S2-C11
      disposition: represented
      result_indexes:
      - 24
      - 25
      reason: Naming correlations
    - source_id: P11-S3-C3
      disposition: repeated
      result_indexes:
      - 24
      - 25
      reason: Restatement of naming correlations
    unresolved_coverage:
    - source_id: P6-S2-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P6-S2-C4
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P6-S2-C11
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P6-S2-C13
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P11-S2-C11
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P9-S1-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S2-C1
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S2-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S3-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S3-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S3-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S3-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S1-C1
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S1-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S1-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S1-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S1-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S2-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S2-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S2-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S2-C12
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S2-C13
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C1
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S2-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S3-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S3-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S4-C1
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S4-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S1-C1
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S2-C4
    - P1-S2-C5
    - P3-S2-C4
    - P3-S2-C5
    - P3-S2-C7
    - P3-S2-C8
    - P3-S2-C9
    - P3-S2-C11
    - P5-S1-C6
    - P5-S1-C11
    - P5-S1-C13
    - P5-S2-C3
    - P6-S1-C1
    - P6-S1-C2
    - P6-S1-C6
    - P6-S2-C7
    - P6-S2-C9
    - P7-S1-C1
    - P8-S1-C1
    - P8-S1-C2
    - P8-S1-C3
    - P8-S1-C5
    - P9-S1-C5
    - P9-S2-C1
    - P9-S2-C9
    - P9-S3-C5
    - P9-S3-C6
    - P9-S3-C8
    - P9-S3-C9
    - P10-S1-C1
    - P10-S1-C3
    - P10-S1-C4
    - P10-S1-C5
    - P10-S1-C7
    - P10-S2-C7
    - P10-S2-C10
    - P10-S2-C11
    - P10-S2-C12
    - P11-S1-C1
    - P11-S1-C7
    - P11-S2-C6
    - P11-S3-C3
    - P11-S3-C10
    - P11-S3-C11
    - P11-S4-C1
    - P11-S4-C4
    - P12-S1-C1
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-4-1
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P3-S1-C8
      recruited_sample:
      - P1-S1-C7
      eligibility:
      - P3-S1-C7
      imaging_provenance:
      - P4-S1-C7
      imaging_timing:
      - P3-S1-C9
      outcome_timing:
      - P3-S1-C9
      outcome_definition: []
      validation: []
      analysis_restrictions:
      - P4-S2-C9
      - P4-S2-C10
      - P4-S2-C11
      dependent_variable_statement:
      - P2-S1-C5
      - P4-S2-C5
      - P4-S2-C6
      - P6-S2-C4
      limitations: []
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P4-S1-C6
      - P7-S1-C3
      - P7-S1-C4
      - P7-S1-C5
      - P10-S3-C4
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P3-S1-C9
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P5-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C13
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S2-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S2-C3
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
      source_id: P6-S2-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S2-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S2-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S2-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S2-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S2-C12
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S3-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S3-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S3-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S3-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S3-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S3-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S3-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C12
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C13
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C14
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C15
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C16
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S1-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S1-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S1-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S1-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S1-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S1-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S1-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S1-C12
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S2-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S2-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S2-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S2-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S2-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S2-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S2-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S2-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S2-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S2-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S2-C12
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S2-C13
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S3-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S3-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S3-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S3-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S3-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S3-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S3-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S3-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S3-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P3-S2-C11
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: outcome_definition
      source_ids:
      - P1-S2-C2
      - P1-S2-C3
      - P3-S3-C3
      - P3-S3-C4
      - P3-S3-C5
      - P3-S3-C6
      - P4-S3-C1
      - P4-S3-C2
      - P4-S3-C3
      - P4-S3-C4
      - P4-S3-C5
      - P5-S1-C1
      - P5-S1-C5
      - P5-S1-C13
      - P6-S1-C6
      - P6-S1-C7
      - P6-S1-C8
      - P6-S1-C9
      - P6-S1-C10
      - P6-S2-C2
      - P6-S2-C3
      - P6-S2-C4
      - P6-S2-C5
      - P6-S2-C6
      - P6-S2-C7
      - P6-S2-C8
      - P6-S2-C9
      - P6-S2-C10
      - P6-S2-C11
      - P6-S2-C12
      - P6-S3-C3
      - P6-S3-C4
      - P6-S3-C5
      - P6-S3-C6
      - P6-S3-C7
      - P6-S3-C8
      - P6-S3-C9
      - P7-S1-C1
      - P7-S1-C12
      - P7-S1-C13
      - P7-S1-C14
      - P7-S1-C15
      - P7-S1-C16
      - P8-S1-C4
      - P8-S1-C5
      - P8-S1-C6
      - P9-S1-C3
      - P9-S1-C4
      - P9-S1-C5
      - P10-S1-C1
      - P10-S1-C3
      - P10-S1-C4
      - P10-S1-C5
      - P10-S1-C7
      - P10-S1-C8
      - P10-S1-C9
      - P10-S1-C10
      - P10-S1-C11
      - P10-S1-C12
      - P10-S2-C1
      - P10-S2-C2
      - P10-S2-C3
      - P10-S2-C4
      - P10-S2-C5
      - P10-S2-C7
      - P10-S2-C8
      - P10-S2-C9
      - P10-S2-C10
      - P10-S2-C11
      - P10-S2-C12
      - P10-S2-C13
      - P10-S3-C2
      - P10-S3-C3
      - P10-S3-C4
      - P10-S3-C5
      - P10-S3-C6
      - P10-S3-C7
      - P10-S3-C8
      - P10-S3-C9
      - P10-S3-C10
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: limitations
      source_ids:
      - P11-S3-C6
      - P11-S3-C7
      - P11-S3-C8
      - P11-S3-C9
      - P11-S3-C10
      - P11-S3-C11
      - P12-S1-C1
      - P12-S1-C2
      - P12-S1-C3
      - P12-S1-C4
      - P12-S1-C5
      - P12-S1-C6
      - P12-S1-C7
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
      pdf_sha256: 2ab275d0f2cac9a302deb7e4615b84e288bff989d5a46b17468f75286daac4b9
      review_sha256: ce9f7d622eb6325d8e241907f052309c0d89a28f2ac8bcdabd6732886e4a5bcd
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
      - P5-S2-C4
      - P10-S2-C3
      source_result: VLSM analysis revealed a significant association between impairment
        in the 'phonematic structure' dimension of spontaneous speech and damage to
        the left supramarginal gyrus. Patients with lesions in this area presented
        significantly more phonematic errors than those with intact supramarginal
        gyrus.
      result_status: detected
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis corresponds to the VLSM analysis of the 'phonematic
            structure' dimension of spontaneous speech from the Aachen Aphasia Test,
            as described in P5-S2-C4 and P10-S2-C3. The proposed core correctly identifies
            this specific linguistic level and the associated brain region.
          source_ids:
          - P5-S2-C4
          - P10-S2-C3
        direction:
          answer: fits
          reason: The source explicitly states that damage to the left supramarginal
            gyrus yielded significantly higher scores for phonematic impairment (more
            errors). The proposed core correctly captures this direction of association
            (damage -> impairment).
          source_ids:
          - P5-S2-C4
          - P10-S2-C3
        construct:
          answer: fits
          reason: The exposure is correctly identified as phonematic structure impairment
            (a linguistic symptom), and the outcome is brain lesion location (specifically
            left supramarginal gyrus). The method is VLSM, which uses patient lesion
            maps overlaid on a standard template (MNI space) to find voxels where
            lesion presence predicts symptom severity. This matches the 'template_lesion_overlap'
            measurement type.
          source_ids:
          - P5-S2-C4
          - P10-S2-C3
          - P4-S2-C5
        qualifications:
          answer: fits
          reason: The proposed core includes the qualification that the analysis is
            based on the semi-standardized rating of spontaneous speech within the
            AAT. This is supported by P10-S2-C2 and P3-S3-C2, which describe the nature
            of the spontaneous speech scoring. The population and timing qualifications
            are also correctly stated.
          source_ids:
          - P10-S2-C2
          - P3-S3-C2
          - P3-S1-C7
          - P3-S1-C9
        missing_material_caveat:
          answer: fits
          reason: The proposed core includes limitations regarding the VLSM method
            potentially favoring larger lesions and the chronic timing. No material
            caveats that would change the interpretation of this specific association
            are omitted. The unresolved OCR warnings in P3-S1-C7 and P4-S2-C10/C11
            do not affect the core finding of the phonematic structure association,
            which is clearly stated in P5-S2-C4 and P10-S2-C3.
          source_ids:
          - P9-S3-C1
          - P9-S2-C10
      optional_pending:
      - Sample size for this specific VLSM analysis is not explicitly transcribed
        in the provided source window, though the main cohort is n=102.
      - Specific statistical thresholds (FDR corrected P < 0.01) are mentioned in
        P4-S2-C10 but not transcribed into the core fields.
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Sample size requires source confirmation; it has not been transcribed.
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Sample size for this specific VLSM analysis is not explicitly transcribed in
      the provided source window, though the main cohort is n=102.
    - Specific statistical thresholds (FDR corrected P < 0.01) are mentioned in P4-S2-C10
      but not transcribed into the core fields.
    normalizations:
    - field: sample.n
      original: 102
      action: not_transcribed
      reason: Not supported by selected quotations
    analysis_identity:
      id: R006
      exposure:
        text: phonematic structure impairment
      outcome:
        text: brain lesion location
      analysis_label: Spontaneous Speech VLSM
      relation: association
      evidence_ids:
      - P5-S2-C4
      - P10-S2-C3
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
        pdf_sha256: 2ab275d0f2cac9a302deb7e4615b84e288bff989d5a46b17468f75286daac4b9
        source_review: _compare/relationships-2026-11-16/review-current/Henseler2014
        source_status_sha256: f7d11cc041dd647fc0d4191212ab8e276734e8027b57f397a18a95e69e39fad3
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P3-S1-C7:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 2ab275d0f2cac9a302deb7e4615b84e288bff989d5a46b17468f75286daac4b9
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: a600bb126ea349cfb97f2d26bdf479bd54cf06e3f0be735bffa67da288f65962
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S1-C7
          page: 3
          text_layer_sha256: a600bb126ea349cfb97f2d26bdf479bd54cf06e3f0be735bffa67da288f65962
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: 'The initial search yielded 1167

          patients who had undergone extensive language testing; 1093 were

          excluded, because they did not fulﬁl our inclusion criteria, which were:

          (i) single left-hemispheric ischaemic stroke in the middle cerebral artery

          territory; (ii) right handedness; (iii) native speakers of German; (iv)

          normal language development; (v) no concomitant severe microangio-

          pathy; (v) no dementia or other neurodegenerative disease; (vii) no

          pre-stroke history of psychiatric or neurological disease; and (viii) high

          resolution MRI available.'
        anchor_text: 'The initial search yielded 1167

          patients who had undergone extensive language testing; 1093 were

          excluded, because they did not fulﬁl our inclusion criteria, which were:

          (i) single left-hemispheric ischaemic stroke in the middle cerebral artery

          territory; (ii) right handedness; (iii) native speakers of German; (iv)

          normal language development; (v) no concomitant severe microangio-

          pathy; (v) no dementia or other neurodegenerative disease; (vii) no

          pre-stroke history of psychiatric or neurological disease; and (viii) high

          resolution MRI available.'
        excluded_fragments: []
        image_sha256: ac3f18573ab0c39ce8d5719964fc39f5d2aee0b8867dd076eeb6964d2a05d1ae
      P3-S1-C9:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 2ab275d0f2cac9a302deb7e4615b84e288bff989d5a46b17468f75286daac4b9
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 78326cfe6dc6d69a52b23079d2dca9d9ef0cfbe87bd4bdf6e80251a96f2477a0
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S1-C9
          page: 3
          text_layer_sha256: 78326cfe6dc6d69a52b23079d2dca9d9ef0cfbe87bd4bdf6e80251a96f2477a0
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Mean age of these participants was 52 years [standard devi-

          ation (SD) = 12 years] and mean time post-stroke was 12.6 months

          (SD = 20.0 months; see Supplementary Table 1 for more details on the

          patient cohort).'
        anchor_text: 'Mean age of these participants was 52 years [standard devi-

          ation (SD) = 12 years] and mean time post-stroke was 12.6 months

          (SD = 20.0 months; see Supplementary Table 1 for more details on the

          patient cohort).'
        excluded_fragments: []
        image_sha256: a592c2d122a1d14766cbac00bab10d0153278383588c001d1d2f022350b65b27
        transcription: '. Mean age of these participants was 52 years [standard devi-

          ation (SD) = 12 years] and mean time post-stroke was 12.6 months

          (SD = 20.0 months; see Supplementary Table 1 for more details on the

          patient cohort)'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 5
  quote: 'For the level ‘phonematic structure’, there

    was a signiﬁcant association between behavioural impairment and

    damage to the left supramarginal gyrus (Fig. 4), i.e. patients with

    damage to this area presented signiﬁcantly more phonematic

    errors

    in

    spontaneous

    speech

    than

    patients

    with

    intact

    Figure 2 Aphasia syndromes.'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-24'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
