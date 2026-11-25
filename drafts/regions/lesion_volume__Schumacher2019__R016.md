---
id: lesion_volume
name: lesion volume
kind: classical
findings:
- id: f1
  target: pca_behavioral_components
  target_kind: impairment
  claim: Lesion volume correlated with the separate non-verbal shift-update component
    and with the semantic and speech quanta components of both PCAs.
  direction: likely
  relationship: correlational
  method: behavioral_only
  sample:
    n: not_reported
    population: individuals with chronic post-stroke aphasia (single left hemispheric
      stroke)
    phase: not_reported
    time_post_onset: at least 1 year before assessment and imaging
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - The study notes that future work will require replication based on larger group
    sizes.
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Lesion volume calculated from the lesion identified
    by the automated lesion identification method (Seghier et al., 2008). The target
    components (non-verbal shift-update, semantic, and speech quanta) were derived
    from principal component analyses (PCA) of non-verbal and language tests. Additional
    metadata has not been transcribed; review the pending-field flags before approval.
    PDF image reading (P3-S2-C2, two-model agreement, human verification pending):
    . All partici-

    pants had a single left hemispheric stroke (ischaemic or haem-

    orrhagic) at least 1 year before assessment and imaging (see

    Fig. 1 for lesion overlap map) and had no additional signifi-

    cant neurological conditions and no contraindications for

    MRI Original text-layer quotation is preserved below. PDF image reading (P12-S3-C5,
    two-model agreement, human verification pending): . In the current study we

    obtained 32 cases (similar to Lacey et al., 2017) and so

    future work will require replication based on larger

    groups sizes Original text-layer quotation is preserved below.'
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
    - proposed_concept:pca_behavioral_components
  citation: '@Schumacher2019'
  source_passages:
  - section: Original source P8-S1-C7
    page: 8
    quote: 'More speciﬁcally, lesion volume

      correlated

      with

      the

      separate

      non-verbal

      shift-update

      component and with the semantic and speech quanta com-

      ponents of both PCAs.'
    supports: claim
  - section: Original source P3-S1-C9
    page: 3
    quote: "Materials and methods\nParticipants\nThirty-eight participants were recruited\
      \ for the present study\n(11 female, 27 male; mean age 64 \x02 11.9 years, range\
      \ 45–88\nyears; see Supplementary Table 1 for more details)."
    supports: sample
  - section: Original source P3-S2-C2
    page: 3
    quote: 'All partici-

      pants had a single left hemispheric stroke (ischaemic or haem-

      orrhagic) at least 1 year before assessment and imaging (see

      Fig. 1 for lesion overlap map) and had no additional signiﬁ-

      cant neurological conditions and no contraindications for

      MRI.'
    supports: sample
  - section: Original source P4-S3-C11
    page: 4
    quote: 'In additional

      analyses, lesion volume (calculated from the lesion identiﬁed

      by the automated lesion identiﬁcation method; Seghier et al.,

      2008), age, education, and time post-stroke were entered as

      covariates.'
    supports: method
  - section: Original source P12-S3-C5
    page: 12
    quote: 'In the current study we

      obtained 32 cases (similar to Lacey et al., 2017) and so

      future

      work

      will

      require

      replication

      based

      on

      larger

      groups sizes.'
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-25'
relationship_review:
  paper: Schumacher2019
  proposal_id: R016
  review_status_sha256: db3f056c36189e65e48db2cc8c2281a2086319b22ae47531e47f8ded7176caaa
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 7ed3bf60e56cc5818811274e6368ab07625bc9cef5175a7bd217643f3d05ed25
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 7ed3bf60e56cc5818811274e6368ab07625bc9cef5175a7bd217643f3d05ed25
        A/passages.json: ae7af96aeeb853ae092eed8cc22be7a231bf3a32f625b5b27299bab506c8de8f
        A/raw.json: f7b31db356240217ee926d6a788d08206652142203a2800a824c1370c2cd9a7b
        A/source-units.json: 464741228ab595a98bf8105efb33ffe60e23aec5a7156fe0a7e67bde7d0c0dfa
        A/full-source-units.json: 2d242a3984af2b613a68b578c7bf95b44d16d4416114ea804d44f5bebe764449
        A/meta.json: 4417286ce3e0ffcafab0d66faa9f33c7e14f44305960b079459bad8244e4bdf6
        A/table-images/TABLE-2-page-9-1.png: f686ee58b4925bcc34449907d793d38d41381cc29521d1b645bd534e3a3bdeb0
        A/table-images/TABLE-1-page-8-1.png: b7fb05057f14bd2d729e9657006327d766b2fc5b85d63a98af02dd127fc12668
        A/table-images/page-9.png: 4511b1458f7535b429b4ffd6b2ca22621eca6e5ba380e27c42e7c6b69a9ff6a7
        A/table-images/page-8.png: 33aa6b5ff5ed647586f8beec197224b6138898de2add6ba3e0f8ba987c31494c
        A/table-images/manifest.json: 4e3a4a48bc644ba9314c4dce0562c84701f18938c43e5f119c738cf42c405b37
        A/clauses/window-03/raw.json: 10caae7c49b7860e6932ad9e715036ab4818dae615ce0b25560fd00cbf4e9aff
        A/clauses/window-03/prompt.txt: dfa923f91b5cf26a40a82648c2de97c458c246b1dce60e1972e6db2e21310918
        A/clauses/window-03/meta.json: 3298268859949599c062bfbb04ca747151bfb98958d5c350082e6c12ae8b642c
        A/clauses/window-04/raw.json: f7e203142f4cf66d502851ebb4880cc95eee6b3d09ec313ad631e975b124ba95
        A/clauses/window-04/prompt.txt: f1ddd0c9c8f85dfe177d8872a9093ff4f13e2037ad57faf48f710e74e70fe1e3
        A/clauses/window-04/meta.json: ab08d17d8b84d2e8b2cade06ad69ac3f0f4107f0eb5e107a6d02448605d81143
        A/clauses/window-05/raw.json: db1a3f31f631141b32626acfc40c49f188f37cc499e30ba21f25dd6797887140
        A/clauses/window-05/prompt.txt: 0a0b930ea445724ce6eb9493bbb235f1ef8bc35f6a48d46e8e1c5ee0909123b3
        A/clauses/window-05/meta.json: a18337100249e9e675424e1b89fe96ec7d53d2a5b1908037e5cc1b5eccb9cd8c
        A/clauses/window-02/raw.json: c8674f9c1543e0e5260d50a57ec3263c1e80202e9f16dbbfd38b44af131f4696
        A/clauses/window-02/prompt.txt: e9575728e2956c1d6f32b9a1a627bc7eaa2044c549151a60ede8c056efc3107c
        A/clauses/window-02/meta.json: 9efef01a1bc6e8a94eae1f4f4ed0deb98533e2e7d66d32ebde7a1cb3b1869277
        A/clauses/window-09/raw.json: e0a65f0503a2d2a34f0ea12d795d61ccbae75e6b880b1a0b8a3b1176e8971336
        A/clauses/window-09/prompt.txt: b72a90e4af8ec6dc742a1242a8d1ec236abef662af55686816502939334c092f
        A/clauses/window-09/meta.json: 7976ad4b9ba37cbe2b2abeecb21f27448fa37033ec7ce6c0724a527f7273827f
        A/clauses/window-07/raw.json: 2499df6690ccb00964676565c413b2bad2387f26ad7000cc4bf1b5a8c9bac1b7
        A/clauses/window-07/prompt.txt: c2f318f4e41d739d4c16c383a155f96bafecac885de098d50f31d03f4010348a
        A/clauses/window-07/meta.json: e8b43bdeb5a2a0914a2335ab5ffbd3d155a6f689a4fc8e886448a1d7c4d9b482
        A/clauses/window-01/raw.json: 1742c3a4e2714875c5c0750a905ac58ccdcf6600ad04db98f85eba37100fa60c
        A/clauses/window-01/prompt.txt: 448d16d16b7fdbb550a520d643d4696fa1dfc9a88c5780a890b49b0b162d577b
        A/clauses/window-01/meta.json: 971629096477941b16bcb32ea3f67f93d7bc0ea776a48fe5ee4074d016a4166e
        A/clauses/window-06/raw.json: 6fd4b24e2117452777aa5d492ead11c74d870d1be185c576ee7ee40c3c966a83
        A/clauses/window-06/prompt.txt: bc0a84d02fea4036719c22c56aedc5faaae9ad6b587f75eddddbfe68567dc79f
        A/clauses/window-06/meta.json: f2a5912309d65ef0058f2174e17a5efb104e37ef7985d3f11f455c452510d476
        A/clauses/window-08/raw.json: a9fcf204752cdfeb9d02f4d734b7a0ac9af40cc73a99946087bef0b0d5fafff0
        A/clauses/window-08/prompt.txt: bb8ac9ec7bfdfbfc8d09279ea9a80cf31c68fe901d7e21b5dae4e6700393f485
        A/clauses/window-08/meta.json: 41d68db015b681cb5e8db2d9586b8ebe0d876198c0a455c67b9e2e6023ac2a0d
        A/tables/TABLE-1-page-8-1/raw.json: 6d9abd80f2e2a24790cc20f7be46af26efeb5913f1602c5c3a383c0a672dea83
        A/tables/TABLE-1-page-8-1/prompt.txt: 6fd9f53f9bd438a261133ef5f80d8a22706b85c977cf41a8febafd55b8093de2
        A/tables/TABLE-1-page-8-1/meta.json: b5b06c1c14bc2f745f5777044507b6a6595bd714594ef1335b63d79d3e1808b0
        A/tables/TABLE-2-page-9-2/raw.json: 93f5755cfc30bbf6a497fe50626034eb80195b6e0b71d66d40f396946c77e476
        A/tables/TABLE-2-page-9-2/prompt.txt: 8a80c4cd4d9e7048c8221146825520ef9c49385ed9c9b3fcc03ba9c2f30b9b6f
        A/tables/TABLE-2-page-9-2/meta.json: 7cd159487f30696f42d4b2dbe1443e4c05a6177944dac70ed97dcd4dec279723
        B/passages.json: ae7af96aeeb853ae092eed8cc22be7a231bf3a32f625b5b27299bab506c8de8f
        B/raw.json: bb8bda80d937af461dc361882c8b1bd2088510d1b30957289f5e30c2a857bf19
        B/source-units.json: 464741228ab595a98bf8105efb33ffe60e23aec5a7156fe0a7e67bde7d0c0dfa
        B/full-source-units.json: 2d242a3984af2b613a68b578c7bf95b44d16d4416114ea804d44f5bebe764449
        B/meta.json: e11b25b442eeaf0bdf846fae17400427e12ed9821ecc07c6a4c38afa236a42f6
        B/table-images/TABLE-2-page-9-1.png: f686ee58b4925bcc34449907d793d38d41381cc29521d1b645bd534e3a3bdeb0
        B/table-images/TABLE-1-page-8-1.png: b7fb05057f14bd2d729e9657006327d766b2fc5b85d63a98af02dd127fc12668
        B/table-images/page-9.png: 4511b1458f7535b429b4ffd6b2ca22621eca6e5ba380e27c42e7c6b69a9ff6a7
        B/table-images/page-8.png: 33aa6b5ff5ed647586f8beec197224b6138898de2add6ba3e0f8ba987c31494c
        B/table-images/manifest.json: ae75e8d6590a43cb1ee8db51b25c494eb2d11a008242c5cf1978ca1c436d9afd
        B/clauses/window-03/raw.json: 0bcfe10a8301147754c426719cb2705fd31ddc7dfc14f4d1d7a97274d7dde6e6
        B/clauses/window-03/prompt.txt: dfa923f91b5cf26a40a82648c2de97c458c246b1dce60e1972e6db2e21310918
        B/clauses/window-03/meta.json: 32d54b58310c0045c1cde8a837970371ad5bc003ad9c669193ac15f79926db91
        B/clauses/window-04/raw.json: 9619262d34271eedb9aace3c84fa1fc46ae8a378bd23106325a31283127babf9
        B/clauses/window-04/prompt.txt: f1ddd0c9c8f85dfe177d8872a9093ff4f13e2037ad57faf48f710e74e70fe1e3
        B/clauses/window-04/meta.json: aae42ad5a2f9bbb8e7fc9e009b77fc7ebbb7b779b258447e5c9c8f7a13443673
        B/clauses/window-05/raw.json: 113efe426e24aa73234cb9f847bb59f91fb536353e461152db47f10866707eab
        B/clauses/window-05/prompt.txt: 0a0b930ea445724ce6eb9493bbb235f1ef8bc35f6a48d46e8e1c5ee0909123b3
        B/clauses/window-05/meta.json: b2163f5e4cdb2a0353bb639eeba1b8b03dd826fa8c02ea9c8f8f675202de0cfc
        B/clauses/window-02/raw.json: 06433409eef6eab15c3ae4ed69cb7dd80b606065c893afe82f942b55e9d01974
        B/clauses/window-02/prompt.txt: e9575728e2956c1d6f32b9a1a627bc7eaa2044c549151a60ede8c056efc3107c
        B/clauses/window-02/meta.json: afbda3ce6babe458ff425570dbc17f434ca5d0406bfd137890ce94758390df0e
        B/clauses/window-09/raw.json: 4573f570ee7eded2acd057c53f6d08b40f7dd9f40f2a1ce13ec10bfeb67856de
        B/clauses/window-09/prompt.txt: b72a90e4af8ec6dc742a1242a8d1ec236abef662af55686816502939334c092f
        B/clauses/window-09/meta.json: b8a0e24866e71adfdee7330a53c96a724032aa49adb44d16acab868d7a7fa8a5
        B/clauses/window-07/raw.json: a26b05ba972b7a0d9748f3a18003d55f7247ab61d21a78bfcddc0ff0cbaa642e
        B/clauses/window-07/prompt.txt: c2f318f4e41d739d4c16c383a155f96bafecac885de098d50f31d03f4010348a
        B/clauses/window-07/meta.json: 5fc9203d8b21fe91c790b1cc20684b34893c5dcb1e9262f08683be2df01af75c
        B/clauses/window-01/raw.json: f0d472ebc3a9d6859f6e9efb6075b6ceb5a7e61f5a17ec52b3d7337a3ceb0455
        B/clauses/window-01/prompt.txt: 448d16d16b7fdbb550a520d643d4696fa1dfc9a88c5780a890b49b0b162d577b
        B/clauses/window-01/meta.json: a7e709ec7d0f33aa032055ac4cd04fa6d3deeafe341e2fea741d4f68824608b4
        B/clauses/window-06/raw.json: b9414da69899b4e3401569b6134b76872f67597bc4f9034611902d26c3cde82f
        B/clauses/window-06/prompt.txt: bc0a84d02fea4036719c22c56aedc5faaae9ad6b587f75eddddbfe68567dc79f
        B/clauses/window-06/meta.json: 1b6b373cf6022e9842d772cf303180d7ea7fd2566f9f20f8ad8991cd1b115f5a
        B/clauses/window-08/raw.json: c72881cd62c65a53ff2ec9986c2fccf33fb2fc93b0b574af3fc6d6b09df3f3b3
        B/clauses/window-08/prompt.txt: bb8ac9ec7bfdfbfc8d09279ea9a80cf31c68fe901d7e21b5dae4e6700393f485
        B/clauses/window-08/meta.json: b884f1b597b4a39eb10a43e519bd157b93e5be1a8fcd49d419681ab62c981b13
        B/tables/TABLE-1-page-8-1/raw.json: 25a28feeed0d2350f6d702357cf37c4e62ef39245836c5a73122e0011084b9d4
        B/tables/TABLE-1-page-8-1/prompt.txt: 6fd9f53f9bd438a261133ef5f80d8a22706b85c977cf41a8febafd55b8093de2
        B/tables/TABLE-1-page-8-1/meta.json: 3a4afcd8fe036ad75836df3e931ebe6be019653ee704ec517ed806158f7940c6
        B/tables/TABLE-2-page-9-2/raw.json: 79621b095e14218a3ed7dfb431ea46bb3fd093c4dffb3c9dccc0cfe278472d48
        B/tables/TABLE-2-page-9-2/prompt.txt: 8a80c4cd4d9e7048c8221146825520ef9c49385ed9c9b3fcc03ba9c2f30b9b6f
        B/tables/TABLE-2-page-9-2/meta.json: 29f0f8b3a311af26f771b960a6ddb55bcb64c804ea14f2aacca94297105b1759
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
      pdf_sha256: 7ed3bf60e56cc5818811274e6368ab07625bc9cef5175a7bd217643f3d05ed25
      source_review: _compare/relationships-2026-11-16/review-current/Schumacher2019
      source_status_sha256: eafa41abca7c633ceb2966f0f946fa2c6c460715a16000aca63392f839e05cff
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R016
    exposure:
      text: lesion volume
    outcome:
      text: non-verbal shift-update, semantic, and speech quanta components
    analysis_label: Spearman Correlation
    relation: association
    evidence_ids:
    - P8-S1-C7
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
      pdf_sha256: 7ed3bf60e56cc5818811274e6368ab07625bc9cef5175a7bd217643f3d05ed25
      source_review: _compare/relationships-2026-11-16/review-current/Schumacher2019
      source_status_sha256: eafa41abca7c633ceb2966f0f946fa2c6c460715a16000aca63392f839e05cff
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P1-S1-C11
      - Result passage disposed without unit P1-S1-C7
      - Result passage disposed without unit P1-S1-C8
      - Unresolved source passage P4-S1-C15
      - Accounting without a linked unit P5-S3-C2
      - Accounting without a linked unit P5-S3-C4
      - Accounting without a linked unit P5-S3-C6
      - Accounting without a linked unit P6-S1-C2
      - Accounting without a linked unit P6-S1-C3
      - Unaccounted source passage P5-S3-C4
      - Unaccounted source passage P6-S1-C3
      - Unaccounted source passage P5-S3-C2
      - Unaccounted source passage P5-S3-C6
      - Unaccounted source passage P6-S1-C2
      - Result passage disposed without unit P6-S1-C11
      - Result passage disposed without unit P6-S1-C12
      - Result passage disposed without unit P6-S1-C6
      - Accounting without a linked unit P6-S1-C7
      - Accounting without a linked unit P6-S1-C8
      - Result passage disposed without unit P6-S2-C1
      - Accounting without a linked unit P6-S2-C2
      - Unaccounted source passage P6-S2-C2
      - Unaccounted source passage P6-S1-C7
      - Unaccounted source passage P6-S1-C8
      - Result passage disposed without unit P8-S1-C5
      - Result passage disposed without unit P10-S1-C10
      - Result passage disposed without unit P10-S1-C11
      - Accounting without a linked unit P11-S1-C1
      - Accounting without a linked unit P11-S1-C2
      - Result passage disposed without unit P11-S1-C3
      - Result passage disposed without unit P11-S1-C4
      - Result passage disposed without unit P11-S1-C5
      - Unaccounted source passage P11-S1-C2
      - Unaccounted source passage P11-S1-C1
      - Result passage disposed without unit P11-S1-C6
      - Result passage disposed without unit P11-S1-C7
      - Result passage disposed without unit P11-S1-C8
      - Result passage disposed without unit P11-S1-C9
      - Result passage disposed without unit P11-S2-C2
      - Result passage disposed without unit P11-S2-C3
      - Result passage disposed without unit P11-S2-C4
      - Result passage disposed without unit P11-S2-C6
      - Result passage disposed without unit P11-S2-C8
      - Result passage disposed without unit P11-S3-C3
      - Accounting without a linked unit P11-S3-C7
      - Accounting without a linked unit P12-S1-C1
      - Accounting without a linked unit P12-S1-C2
      - Accounting without a linked unit P12-S1-C3
      - Unaccounted source passage P12-S1-C3
      - Unaccounted source passage P12-S1-C2
      - Unaccounted source passage P12-S1-C1
      - Unaccounted source passage P11-S3-C7
      - Result passage disposed without unit P12-S2-C5
      - Result passage disposed without unit P12-S3-C6
      - Result passage disposed without unit P12-S4-C3
      - Result passage disposed without unit P13-S1-C1
      unattached_null_or_qualifier_ids:
      - P4-S1-C6
      - P5-S3-C4
      - P6-S1-C2
      - P6-S1-C12
      - P6-S2-C1
      - P11-S1-C2
      - P13-S1-C1
      suppressed_nonrepresented_units: 23
      default_disposition_count_requires_completeness_check: 166
      unselected_timing_passages:
      - P1-S1-C5
      - P3-S1-C9
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P5-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C6
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
      - slot: dependent_variable_statement
        source_id: P5-S1-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C10
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
        source_id: P10-S2-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S2-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S2-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S1-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S1-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S2-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S2-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S2-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S2-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S2-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S2-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S2-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S3-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S3-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S3-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S3-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S3-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S3-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S1-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S1-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S1-C5
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
        source_id: P12-S1-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S1-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S1-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S2-C1
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
        source_id: P12-S2-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S2-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S2-C6
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
        source_id: P12-S2-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S3-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S3-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S3-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S3-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S3-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S3-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S3-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S3-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S3-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S3-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S3-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S1-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S1-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P4-S2-C4
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P4-S2-C3
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P5-S1-C9
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P10-S2-C4
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P10-S2-C6
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P10-S2-C9
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P11-S1-C10
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P11-S1-C11
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P11-S2-C2
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P11-S2-C3
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P11-S2-C4
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P11-S2-C5
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P11-S2-C6
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P11-S2-C7
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P11-S2-C8
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P11-S3-C2
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P11-S3-C3
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P11-S3-C4
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P11-S3-C5
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P11-S3-C6
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P11-S3-C7
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P12-S1-C1
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P12-S1-C2
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P12-S1-C3
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P12-S1-C4
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P12-S1-C5
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P12-S1-C6
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P12-S1-C7
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P12-S1-C8
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P12-S1-C9
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P12-S1-C10
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P12-S2-C1
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P12-S2-C2
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P12-S2-C3
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P12-S2-C4
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P12-S2-C5
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P12-S2-C6
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P12-S2-C7
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P12-S2-C8
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P12-S2-C9
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P12-S2-C10
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P12-S3-C1
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P12-S3-C3
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P12-S3-C4
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P12-S3-C5
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P12-S3-C6
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P12-S3-C7
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P12-S3-C8
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P12-S3-C9
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P12-S3-C10
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P12-S3-C11
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P13-S1-C1
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P13-S1-C2
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P13-S1-C3
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: outcome_definition
        source_ids:
        - P4-S1-C3
        - P5-S2-C5
        - P5-S2-C6
        - P5-S2-C8
        - P5-S2-C9
        - P6-S1-C2
        - P6-S1-C7
        - P6-S1-C11
        - P8-S2-C3
        - P10-S1-C12
        - P10-S2-C3
        - P10-S2-C4
        - P10-S2-C6
        - P10-S2-C9
        - P11-S1-C1
        - P11-S1-C2
        - P11-S1-C4
        - P11-S1-C5
        - P11-S1-C6
        - P11-S1-C7
        - P11-S1-C9
        - P11-S2-C2
        - P11-S2-C3
        - P11-S2-C4
        - P11-S2-C5
        - P11-S2-C6
        - P11-S2-C7
        - P11-S2-C8
        - P11-S3-C2
        - P11-S3-C3
        - P11-S3-C4
        - P11-S3-C5
        - P11-S3-C6
        - P11-S3-C7
        - P12-S1-C1
        - P12-S1-C2
        - P12-S1-C3
        - P12-S1-C4
        - P12-S1-C5
        - P12-S1-C6
        - P12-S1-C7
        - P12-S1-C8
        - P12-S1-C9
        - P12-S1-C10
        - P12-S2-C1
        - P12-S2-C2
        - P12-S2-C3
        - P12-S2-C4
        - P12-S2-C5
        - P12-S2-C6
        - P12-S2-C7
        - P12-S2-C8
        - P12-S2-C9
        - P12-S2-C10
        - P12-S3-C1
        - P12-S3-C2
        - P12-S3-C3
        - P12-S3-C4
        - P12-S3-C5
        - P12-S3-C6
        - P12-S3-C7
        - P12-S3-C8
        - P12-S3-C9
        - P12-S3-C10
        - P12-S3-C11
        - P13-S1-C1
        - P13-S1-C2
        - P13-S1-C3
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - outcome_definition
      - personal_factors
      - tested_personal_effects
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-8-1
      - TABLE-2-page-9-2
      unlinked_tables:
      - TABLE-2-page-9-2
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P3-S2
        - P3-S3
        - P4-S3
        - P5-S2
        - P6-S1
        - P6-S2
        - P7-S1
        - P8-S1
        - P10-S1
        - P10-S2
        - P11-S1
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 7ed3bf60e56cc5818811274e6368ab07625bc9cef5175a7bd217643f3d05ed25
      source_review: _compare/relationships-2026-11-16/review-current/Schumacher2019
      source_status_sha256: eafa41abca7c633ceb2966f0f946fa2c6c460715a16000aca63392f839e05cff
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes PCA component interpretation, not a measured relationship.
    - source_id: P1-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes PCA component interpretation, not a measured relationship.
    - source_id: P1-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes methodology of VBCM analysis.
    - source_id: P1-S1-C10
      disposition: represented
      result_indexes:
      - 0
      - 1
      - 2
      reason: Summarizes VBCM results for non-verbal components.
    - source_id: P1-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about multivariate methods.
    - source_id: P4-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes PCA composition.
    - source_id: P4-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes PCA composition.
    - source_id: P4-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes PCA composition.
    - source_id: P4-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes correlation between excluded measures.
    - source_id: P5-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive prevalence of impairment.
    - source_id: P5-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive prevalence of impairment.
    - source_id: P5-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive prevalence of impairment.
    - source_id: P5-S2-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive prevalence of impairment.
    - source_id: P5-S3-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes norm comparison methodology.
    - source_id: P5-S3-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive group comparison of impairment.
    - source_id: P5-S3-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive group comparison of impairment.
    - source_id: P6-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: PCA variance/loadings alone.
    - source_id: P6-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: PCA variance/loadings alone.
    - source_id: P6-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: PCA variance/loadings alone.
    - source_id: P6-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: PCA variance/loadings alone.
    - source_id: P6-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: PCA variance/loadings alone.
    - source_id: P6-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: PCA variance/loadings alone.
    - source_id: P6-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: PCA variance/loadings alone.
    - source_id: P6-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement on PCA stability.
    - source_id: P6-S2-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement on PCA stability.
    - source_id: P6-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: PCA variance/loadings alone.
    - source_id: P6-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: PCA variance/loadings alone.
    - source_id: P6-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement on PCA stability.
    - source_id: P6-S2-C7
      disposition: represented
      result_indexes:
      - 13
      reason: Reports correlation between non-verbal and language impairment.
    - source_id: P7-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes PCA loading stability.
    - source_id: P7-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports PCA prediction accuracy (performance of the PCA itself).
    - source_id: P7-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: General observation on task loadings.
    - source_id: P8-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: General observation on task loadings.
    - source_id: P8-S1-C3
      disposition: represented
      result_indexes:
      - 13
      reason: Reports correlation between non-verbal and language impairment.
    - source_id: P8-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Qualitative observation about shift-update component.
    - source_id: P8-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: General observation on PCA orthogonality.
    - source_id: P8-S1-C6
      disposition: represented
      result_indexes:
      - 14
      reason: Reports correlation between lesion volume and severity.
    - source_id: P8-S1-C7
      disposition: represented
      result_indexes:
      - 15
      reason: Reports correlation between lesion volume and specific components.
    - source_id: P8-S1-C8
      disposition: represented
      result_indexes:
      - 16
      reason: Reports correlation between age and components.
    - source_id: P8-S1-C9
      disposition: represented
      result_indexes:
      - 17
      - 18
      reason: Reports correlations for education and time post-stroke.
    - source_id: P8-S1-C10
      disposition: represented
      result_indexes:
      - 19
      - 20
      reason: Reports partial correlations after adjustment.
    - source_id: P8-S2-C1
      disposition: repeated
      result_indexes:
      - 20
      reason: Restatement of phonology partial correlation.
    - source_id: P8-S2-C3
      disposition: represented
      result_indexes:
      - 0
      - 1
      - 2
      - 3
      - 4
      - 5
      reason: Establishes that VBCM yielded significant clusters for all components.
    - source_id: P8-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to figures/tables.
    - source_id: P10-S1-C1
      disposition: represented
      result_indexes:
      - 0
      reason: Specifies structural correlates for shift-update.
    - source_id: P10-S1-C2
      disposition: represented
      result_indexes:
      - 1
      reason: Specifies structural correlates for inhibit-generate.
    - source_id: P10-S1-C3
      disposition: represented
      result_indexes:
      - 2
      reason: Specifies structural correlates for speed.
    - source_id: P10-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison to prior studies.
    - source_id: P10-S1-C5
      disposition: represented
      result_indexes:
      - 3
      reason: Specifies structural correlates for phonology.
    - source_id: P10-S1-C6
      disposition: represented
      result_indexes:
      - 4
      reason: Specifies structural correlates for semantics.
    - source_id: P10-S1-C7
      disposition: represented
      result_indexes:
      - 5
      reason: Specifies structural correlates for speech quanta.
    - source_id: P10-S1-C8
      disposition: represented
      result_indexes:
      - 6
      reason: Reports significance after lesion volume adjustment.
    - source_id: P10-S1-C9
      disposition: represented
      result_indexes:
      - 7
      reason: Reports loss of significance for semantics/shift-update after adjustment.
    - source_id: P10-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to supplementary material.
    - source_id: P10-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement on multivariate results.
    - source_id: P10-S1-C12
      disposition: represented
      result_indexes:
      - 8
      reason: Reports SVR-LSM significant clusters.
    - source_id: P10-S2-C3
      disposition: represented
      result_indexes:
      - 10
      reason: Reports PRoNTo whole-brain model performance.
    - source_id: P10-S2-C4
      disposition: repeated
      result_indexes:
      - 11
      reason: States results were the same for restricted territory.
    - source_id: P11-S1-C1
      disposition: represented
      result_indexes:
      - 11
      reason: Reports PRoNTo restricted territory model performance.
    - source_id: P11-S1-C2
      disposition: represented
      result_indexes:
      - 9
      - 12
      reason: Reports sensitivity results for SVR-LSM and PRoNTo after lesion volume
        adjustment.
    - source_id: P11-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: General summary of study findings.
    - source_id: P11-S3-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: General observation on component independence.
    - source_id: P11-S3-C7
      disposition: repeated
      result_indexes:
      - 0
      - 1
      - 2
      - 3
      - 4
      - 5
      reason: Restatement of structural correlates.
    - source_id: P12-S1-C1
      disposition: repeated
      result_indexes:
      - 0
      - 1
      - 2
      - 3
      - 4
      - 5
      reason: Restatement of structural correlates.
    - source_id: P12-S3-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement about sample size.
    - source_id: P12-S4-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Hypothetical statement about future prediction models.
    - source_id: P12-S4-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Hypothetical statement about future prediction models.
    - source_id: P13-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion.
    unresolved_coverage:
    - source_id: P12-S4-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P12-S4-C2
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P11-S1-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S2-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S2-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S2-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S2-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S2-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S1-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S1-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S1-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S1-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S1-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S2-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S3-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S4-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C7
    - P1-S1-C8
    - P1-S1-C9
    - P1-S1-C10
    - P1-S1-C11
    - P4-S1-C5
    - P4-S1-C6
    - P4-S1-C7
    - P4-S1-C12
    - P5-S2-C6
    - P5-S2-C7
    - P5-S2-C8
    - P5-S2-C11
    - P5-S3-C2
    - P5-S3-C4
    - P5-S3-C6
    - P6-S1-C2
    - P6-S1-C3
    - P6-S1-C5
    - P6-S1-C6
    - P6-S1-C7
    - P6-S1-C8
    - P6-S1-C11
    - P6-S1-C12
    - P6-S2-C1
    - P6-S2-C2
    - P6-S2-C3
    - P6-S2-C4
    - P7-S1-C1
    - P7-S1-C2
    - P7-S1-C3
    - P8-S1-C1
    - P8-S1-C4
    - P8-S1-C5
    - P8-S2-C1
    - P8-S2-C4
    - P10-S1-C4
    - P10-S1-C10
    - P10-S1-C11
    - P10-S2-C4
    - P11-S1-C3
    - P11-S1-C4
    - P11-S1-C5
    - P11-S1-C6
    - P11-S1-C7
    - P11-S1-C8
    - P11-S1-C9
    - P11-S2-C2
    - P11-S2-C3
    - P11-S2-C4
    - P11-S2-C5
    - P11-S2-C6
    - P11-S2-C8
    - P11-S3-C3
    - P11-S3-C7
    - P12-S1-C1
    - P12-S1-C2
    - P12-S1-C3
    - P12-S1-C4
    - P12-S1-C5
    - P12-S1-C6
    - P12-S2-C5
    - P12-S3-C5
    - P12-S3-C6
    - P12-S4-C3
    - P13-S1-C1
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-8-1
    - TABLE-2-page-9-2
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P4-S1-C10
      recruited_sample:
      - P3-S1-C9
      eligibility:
      - P3-S2-C2
      - P3-S2-C4
      imaging_provenance:
      - P4-S2-C6
      imaging_timing:
      - P3-S2-C2
      outcome_timing:
      - P3-S2-C2
      outcome_definition: []
      validation:
      - P5-S1-C7
      - P5-S1-C8
      - P10-S2-C3
      - P12-S3-C2
      analysis_restrictions:
      - P4-S1-C11
      dependent_variable_statement:
      - P4-S2-C5
      - P4-S3-C7
      - P4-S3-C9
      - P4-S3-C10
      limitations:
      - P12-S3-C5
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P4-S3-C11
      - P5-S1-C2
      - P5-S1-C10
      - P8-S1-C10
      - P10-S1-C8
      - P11-S1-C2
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P3-S1-C9
      - P3-S2-C2
      - P3-S2-C3
      - P4-S2-C10
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: internal_cross_validation
    held_selections:
    - slot: dependent_variable_statement
      source_id: P5-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C6
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
    - slot: dependent_variable_statement
      source_id: P5-S1-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C10
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
      source_id: P10-S2-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S2-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S2-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S1-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S1-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S2-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S2-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S2-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S2-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S2-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S2-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S2-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S3-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S3-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S3-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S3-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S3-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S3-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S1-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S1-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S1-C5
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
      source_id: P12-S1-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S1-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S1-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S2-C1
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
      source_id: P12-S2-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S2-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S2-C6
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
      source_id: P12-S2-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S3-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S3-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S3-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S3-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S3-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S3-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S3-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S3-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S3-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S3-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S3-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S1-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S1-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P4-S2-C4
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P4-S2-C3
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P5-S1-C9
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P10-S2-C4
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P10-S2-C6
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P10-S2-C9
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P11-S1-C10
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P11-S1-C11
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P11-S2-C2
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P11-S2-C3
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P11-S2-C4
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P11-S2-C5
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P11-S2-C6
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P11-S2-C7
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P11-S2-C8
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P11-S3-C2
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P11-S3-C3
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P11-S3-C4
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P11-S3-C5
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P11-S3-C6
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P11-S3-C7
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P12-S1-C1
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P12-S1-C2
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P12-S1-C3
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P12-S1-C4
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P12-S1-C5
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P12-S1-C6
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P12-S1-C7
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P12-S1-C8
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P12-S1-C9
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P12-S1-C10
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P12-S2-C1
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P12-S2-C2
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P12-S2-C3
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P12-S2-C4
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P12-S2-C5
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P12-S2-C6
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P12-S2-C7
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P12-S2-C8
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P12-S2-C9
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P12-S2-C10
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P12-S3-C1
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P12-S3-C3
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P12-S3-C4
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P12-S3-C5
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P12-S3-C6
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P12-S3-C7
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P12-S3-C8
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P12-S3-C9
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P12-S3-C10
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P12-S3-C11
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P13-S1-C1
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P13-S1-C2
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P13-S1-C3
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: outcome_definition
      source_ids:
      - P4-S1-C3
      - P5-S2-C5
      - P5-S2-C6
      - P5-S2-C8
      - P5-S2-C9
      - P6-S1-C2
      - P6-S1-C7
      - P6-S1-C11
      - P8-S2-C3
      - P10-S1-C12
      - P10-S2-C3
      - P10-S2-C4
      - P10-S2-C6
      - P10-S2-C9
      - P11-S1-C1
      - P11-S1-C2
      - P11-S1-C4
      - P11-S1-C5
      - P11-S1-C6
      - P11-S1-C7
      - P11-S1-C9
      - P11-S2-C2
      - P11-S2-C3
      - P11-S2-C4
      - P11-S2-C5
      - P11-S2-C6
      - P11-S2-C7
      - P11-S2-C8
      - P11-S3-C2
      - P11-S3-C3
      - P11-S3-C4
      - P11-S3-C5
      - P11-S3-C6
      - P11-S3-C7
      - P12-S1-C1
      - P12-S1-C2
      - P12-S1-C3
      - P12-S1-C4
      - P12-S1-C5
      - P12-S1-C6
      - P12-S1-C7
      - P12-S1-C8
      - P12-S1-C9
      - P12-S1-C10
      - P12-S2-C1
      - P12-S2-C2
      - P12-S2-C3
      - P12-S2-C4
      - P12-S2-C5
      - P12-S2-C6
      - P12-S2-C7
      - P12-S2-C8
      - P12-S2-C9
      - P12-S2-C10
      - P12-S3-C1
      - P12-S3-C2
      - P12-S3-C3
      - P12-S3-C4
      - P12-S3-C5
      - P12-S3-C6
      - P12-S3-C7
      - P12-S3-C8
      - P12-S3-C9
      - P12-S3-C10
      - P12-S3-C11
      - P13-S1-C1
      - P13-S1-C2
      - P13-S1-C3
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
      pdf_sha256: 7ed3bf60e56cc5818811274e6368ab07625bc9cef5175a7bd217643f3d05ed25
      review_sha256: db3f056c36189e65e48db2cc8c2281a2086319b22ae47531e47f8ded7176caaa
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
      - P8-S1-C7
      source_result: Lesion volume correlated with the separate non-verbal shift-update
        component and with the semantic and speech quanta components of both PCAs.
      result_status: detected
      patient_measurement: non_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The source P8-S1-C7 explicitly states that lesion volume correlated
            with the specified components. The proposed core correctly identifies
            this as a correlation analysis involving lesion volume and PCA-derived
            behavioral components.
          source_ids:
          - P8-S1-C7
          - P4-S2-C5
        direction:
          answer: fits
          reason: The source reports a significant correlation. The proposed core
            uses 'likely' direction which is acceptable for a qualitative draft where
            specific sign (positive/negative) is not transcribed, but the existence
            of the association is correctly captured.
          source_ids:
          - P8-S1-C7
        construct:
          answer: fits
          reason: The exposure is lesion volume (calculated from automated lesion
            identification, P4-S3-C11). The outcome is the PCA components (shift-update,
            semantic, speech quanta). The patient measurement is non-imaging (behavioral
            scores from neuropsychological tests), not imaging-based. The proposed
            core correctly identifies the target as 'pca_behavioral_components' and
            the method as 'behavioral_only' (in terms of the outcome variable being
            behavioral, though the predictor is imaging-derived). The distinction
            that the outcome is behavioral is correct.
          source_ids:
          - P8-S1-C7
          - P4-S3-C11
          - P4-S1-C4
        qualifications:
          answer: fits
          reason: The proposed core includes the qualification that the targets were
            derived from PCA. It also notes the limitation regarding sample size.
            The source P8-S1-C7 specifies 'separate non-verbal shift-update' and 'semantic
            and speech quanta components of both PCAs'. The proposed claim text matches
            this specificity.
          source_ids:
          - P8-S1-C7
          - P12-S3-C5
        missing_material_caveat:
          answer: fits
          reason: No material caveats are missing. The core correctly reflects the
            specific components involved. The fact that this is a correlation (not
            causal) is implied by 'correlational' relationship. The sample size limitation
            is included.
          source_ids:
          - P8-S1-C7
          - P12-S3-C5
      optional_pending:
      - Specific correlation coefficients and p-values for these individual component
        correlations are not transcribed in the provided source window, only the general
        statement of significance.
      - The exact sign of the correlation (positive/negative) is not explicitly stated
        in P8-S1-C7, though P4-S3-C8 suggests a negative correlation between abnormality
        and performance, implying a negative correlation between lesion volume and
        component scores if higher scores indicate better performance.
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Sample size requires source confirmation; it has not been transcribed.
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Specific correlation coefficients and p-values for these individual component
      correlations are not transcribed in the provided source window, only the general
      statement of significance.
    - The exact sign of the correlation (positive/negative) is not explicitly stated
      in P8-S1-C7, though P4-S3-C8 suggests a negative correlation between abnormality
      and performance, implying a negative correlation between lesion volume and component
      scores if higher scores indicate better performance.
    normalizations:
    - field: bucket
      original: predictors
      action: route_from_kind
      value: regions
    - field: sample.n
      original: 38
      action: not_transcribed
      reason: Not supported by selected quotations
    analysis_identity:
      id: R016
      exposure:
        text: lesion volume
      outcome:
        text: non-verbal shift-update, semantic, and speech quanta components
      analysis_label: Spearman Correlation
      relation: association
      evidence_ids:
      - P8-S1-C7
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
        pdf_sha256: 7ed3bf60e56cc5818811274e6368ab07625bc9cef5175a7bd217643f3d05ed25
        source_review: _compare/relationships-2026-11-16/review-current/Schumacher2019
        source_status_sha256: eafa41abca7c633ceb2966f0f946fa2c6c460715a16000aca63392f839e05cff
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P3-S1-C9:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 7ed3bf60e56cc5818811274e6368ab07625bc9cef5175a7bd217643f3d05ed25
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 24f09a842141b4e1ea58e9dd107fdfeaa66e55f655b91e75f9dbdb6c1a2b3313
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S1-C9
          page: 3
          text_layer_sha256: 24f09a842141b4e1ea58e9dd107fdfeaa66e55f655b91e75f9dbdb6c1a2b3313
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: "Materials and methods\nParticipants\nThirty-eight participants\
          \ were recruited for the present study\n(11 female, 27 male; mean age 64\
          \ \x02 11.9 years, range 45–88\nyears; see Supplementary Table 1 for more\
          \ details)."
        anchor_text: "Materials and methods\nParticipants\nThirty-eight participants\
          \ were recruited for the present study\n(11 female, 27 male; mean age 64\
          \ \x02 11.9 years, range 45–88\nyears; see Supplementary Table 1 for more\
          \ details)."
        excluded_fragments: []
      P3-S2-C2:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 7ed3bf60e56cc5818811274e6368ab07625bc9cef5175a7bd217643f3d05ed25
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 3a331db8f841d449aa65ddece3f40004f034b677abb08780ab5061f2e7491df9
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S2-C2
          page: 3
          text_layer_sha256: 3a331db8f841d449aa65ddece3f40004f034b677abb08780ab5061f2e7491df9
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'All partici-

          pants had a single left hemispheric stroke (ischaemic or haem-

          orrhagic) at least 1 year before assessment and imaging (see

          Fig. 1 for lesion overlap map) and had no additional signiﬁ-

          cant neurological conditions and no contraindications for

          MRI.'
        anchor_text: 'All partici-

          pants had a single left hemispheric stroke (ischaemic or haem-

          orrhagic) at least 1 year before assessment and imaging (see

          Fig. 1 for lesion overlap map) and had no additional signiﬁ-

          cant neurological conditions and no contraindications for

          MRI.'
        excluded_fragments: []
        image_sha256: 8f4a91978b094e75acd9151714035e6525e90fea0d65dd9d8b60efae67784c57
        transcription: '. All partici-

          pants had a single left hemispheric stroke (ischaemic or haem-

          orrhagic) at least 1 year before assessment and imaging (see

          Fig. 1 for lesion overlap map) and had no additional signifi-

          cant neurological conditions and no contraindications for

          MRI'
      P12-S3-C5:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 7ed3bf60e56cc5818811274e6368ab07625bc9cef5175a7bd217643f3d05ed25
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: b15ca2137ba529ce9c64de2e1555595f21227efb7b6a6cf83b5d39e2c4c5575a
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P12-S3-C5
          page: 12
          text_layer_sha256: b15ca2137ba529ce9c64de2e1555595f21227efb7b6a6cf83b5d39e2c4c5575a
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'In the current study we

          obtained 32 cases (similar to Lacey et al., 2017) and so

          future

          work

          will

          require

          replication

          based

          on

          larger

          groups sizes.'
        anchor_text: 'In the current study we

          obtained 32 cases (similar to Lacey et al., 2017) and so

          future

          work

          will

          require

          replication

          based

          on

          larger

          groups sizes.'
        excluded_fragments: []
        image_sha256: c03bcde0cb547b42c032f137ea05830e95eafbafd0457e3c3b2a2a16eed01ff5
        transcription: '. In the current study we

          obtained 32 cases (similar to Lacey et al., 2017) and so

          future work will require replication based on larger

          groups sizes'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 8
  quote: 'More speciﬁcally, lesion volume

    correlated

    with

    the

    separate

    non-verbal

    shift-update

    component and with the semantic and speech quanta com-

    ponents of both PCAs.'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-25'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
