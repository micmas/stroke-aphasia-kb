---
id: age_hearing_lesion_volume
name: age, peripheral hearing, and lesion volume
kind: predictor
findings:
- id: f1
  target: comprehension_score_9mpo
  target_kind: prognosis
  claim: There was no significant correlation between language comprehension scores
    at 9 MPO and age, average bilateral peripheral hearing thresholds, or lesion volume.
  direction: no_effect
  relationship: correlational
  method: behavioral_only
  sample:
    n: 12
    population: participants with Wernicke's aphasia (WA) and superior temporal lobe
      lesions
    phase: not_reported
    time_post_onset: measured at 9 months post-stroke onset (MPO)
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - small sample size
  - potential recruitment bias toward more capable and medically well individuals
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Age (years), average bilateral peripheral air conduction
    hearing thresholds at 0.5, 1, 2, and 4 kHz, and lesion volume measured in voxels.
    comprehension score at 2.5 MPO was found to be significantly correlated with the
    9 MPO score. Additional metadata has not been transcribed; review the pending-field
    flags before approval. PDF image reading (P2-S3-C4, two-model agreement, human
    verification pending): . A total of 24 participants were

    referred to the study of whom 17 were contactable and 12

    fulfilled the inclusion and exclusion criteria and consented

    to participate Original text-layer quotation is preserved below.'
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
    - proposed_concept:comprehension_score_9mpo
  citation: '@Robson2019'
  source_passages:
  - section: Original source P6-S1-C6
    page: 6
    quote: "Correlation With Additional Variables\nOnset severity and age have been\
      \ shown to influence \nrecovery from stroke.43 Pearson correlations explored\
      \ the \nrelationship between comprehension scores at 9 MPO and \nadditional\
      \ variables: comprehension score at 2.5 MPO, \nage, average bilateral peripheral\
      \ hearing threshold, and \nlesion volume in voxels."
    supports: method
  - section: Original source P6-S1-C7
    page: 6
    quote: "A significant correlation was \nfound between 2.5 and 9 MPO comprehension\
      \ scores \n(r = 0.73; n = 11; P = .011) but not age, hearing, or lesion \nvolume."
    supports: claim
  - section: Original source P11-S1-C6
    page: 11
    quote: "However, we found no systematic relationship \nbetween age and comprehension\
      \ outcome or degree of \ncomprehension recovery, and general age-related limita-\n\
      tions on recovery would not explain the differences in \nrecovery over tasks."
    supports: claim
  - section: Original source P2-S3-C4
    page: 2
    quote: "A total of 24 participants were \nreferred to the study of whom 17 were\
      \ contactable and 12 \nfulfilled the inclusion and exclusion criteria and consented\
      \ \nto participate."
    supports: sample
  - section: Original source P5-S2-C3
    page: 5
    quote: "Additional Variable: Peripheral Hearing\nAlongside age and time postonset,\
      \ bilateral pure tone \nperipheral air conduction hearing thresholds at 0.5,\
      \ 1, 2, and \n4 kHz were measured and averaged."
    supports: method
  - section: Original source P5-S2-C4
    page: 5
    quote: 'Bias

      Potential bias in the study may have arisen through recruit-

      ment procedures: for example, only more capable and med-

      ically well individuals being referred to the research.'
    supports: limitation
  - section: Original source P10-S3-C5
    page: 10
    quote: "This sample size reflected an a priori power cal-\nculation; however,\
      \ this calculation was conducted on \nchronic WA data, and the sample remains\
      \ small."
    supports: limitation
predictor_type: imaging_metric
short_definition: Age (years), average bilateral peripheral air conduction hearing
  thresholds at 0.5, 1, 2, and 4 kHz, and lesion volume measured in voxels.
assessment:
- pure tone peripheral air conduction hearing thresholds
- MRI
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-25'
relationship_review:
  paper: Robson2019
  proposal_id: R012
  review_status_sha256: 247c2b79bca5ff0a9804e6890d49e4426eaf820e8d361ec054aebaefb27f6580
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: f0d9fd6c287f4f6db14223ea7d376a5f77971f8c0a4a46440d328c1905892fce
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: f0d9fd6c287f4f6db14223ea7d376a5f77971f8c0a4a46440d328c1905892fce
        A/passages.json: 64a24340ebe49bb996ed60b009ae466e80944869a95ba2586191e28f7770df46
        A/raw.json: f4a4a70c14b24955952d6e60e08aa48094ca969d9711a26db726b2b71d046011
        A/source-units.json: 49abd21d57e042f319a369cd5a62560388ab09e404cc717a62de6affe29ee1f8
        A/full-source-units.json: 3db4746fb7639bc4a34957dadfe47c338f85879f1c4b2cae5ab4e1dd5a9c5856
        A/meta.json: 3f766d28c5af4ba4ab5a2c9f46e55b22783f97e1e9b506a536177212d691ebf0
        A/table-images/TABLE-1-page-3-1.png: 2d8ba35f1dc552ccc2fc766958726139a1f12b7f5a21f34e21a399567a55f759
        A/table-images/TABLE-4-page-9-2.png: f16f9944224fc3fa4f8499063630c30889f4fb33d50cc96a0f2957b2f4a78158
        A/table-images/TABLE-3-page-9-1.png: f16f9944224fc3fa4f8499063630c30889f4fb33d50cc96a0f2957b2f4a78158
        A/table-images/TABLE-2-page-8-1.png: 5cd3f5a15dbce974f535f3e7cddb4b37d7967e0749605a18f8ef8d184fe6c137
        A/table-images/page-3.png: 6d762f30786fa7a784e7e8f8d7cf7e1ce736a10e1e0b0d64a9f8a354fc47881f
        A/table-images/page-9.png: fede3b992082cb35fc36d0841e74d5ce07457b6470b9125e0a33d45181e354c7
        A/table-images/page-8.png: 9dfcb6ac49b21d703b51bd532ab6c0c8719b481ac4fb0d09f9fd718dbb32708a
        A/table-images/manifest.json: fdd7e92dad6327ea9ddd75c32756d764fff5b8f53aa8983d05e99d64d1dc9158
        A/clauses/window-03/raw.json: 3e7c959cfab72023d4c6357b025aa0b42828b64dfed20a71433b5cfcd943b6b3
        A/clauses/window-03/prompt.txt: cc29dcbc30a5404a6fa90fb33b2e35001e303c382fef42024df16dc5a2f3d2fb
        A/clauses/window-03/meta.json: da36cb81869694ffdafcf3b043b827e7bcc112354ec9ece0120fee7a8c95e9be
        A/clauses/window-04/raw.json: 3c21d78288654b231b71dc7dd34bf78c40e1575e5db13479c7f096b186807b17
        A/clauses/window-04/prompt.txt: 496320ce0863454c0f547041204993c6f95a8b48062a7ddb343dffa815777bae
        A/clauses/window-04/meta.json: 292e3162a29e95192eda51a9cc1ce8bb67bd75f048a7b5dac23a79499c4e278d
        A/clauses/window-05/raw.json: 453898ac4646e0eca0231056a72a05d560b02a35e28970de1676107f799c1875
        A/clauses/window-05/prompt.txt: 6a64bdb52346130b8a072792d3a9f3983d62a5a926cf2c7a5cfe2b6387ddfb3f
        A/clauses/window-05/meta.json: 507d4de759aa09ebdd8408d8080484d7200bb8ea8da3fd2461fac1a8d9d2438b
        A/clauses/window-02/raw.json: 0cb91a348cd73b848b18e06c5a338fa3832c078d3eaf9570cdbaa925a0866b64
        A/clauses/window-02/prompt.txt: 8aff9eecfb3f9891bf50d5391f506d0cbba95fa78ce2adc371a7b565555b2935
        A/clauses/window-02/meta.json: 6320f670ea04fb8514c6fa3f2a39ebd4b8864a80a96310cca68d04383f70affb
        A/clauses/window-07/raw.json: 10b5276e09e85773151c5749fb8a64be3b4b7884d5166d5869f03efa214d4988
        A/clauses/window-07/prompt.txt: 0bc91ccab8ef50c32fb09462b8104cbcfdf02364b53285c485d60c3597d69945
        A/clauses/window-07/meta.json: 71569660634e20ba9eb756ee7d3befc1b68a6504d5d8b4ff08e6622de7234a88
        A/clauses/window-01/raw.json: d68c7ee5b9f21d4ee99555cdbfbe2bade0ab9e0f376f6b8976191b259deed27b
        A/clauses/window-01/prompt.txt: d5ebc9ba4503507222ae4921a287e7681f2222d207b50da01c73025e812babe1
        A/clauses/window-01/meta.json: 88238b73d2c5e5d08691a965bb89758fe1420bed92ebd14e9478075319df91a4
        A/clauses/window-06/raw.json: 0cb691021c9e6df3d2909cb2a65278903c9dd1f54e2b12abd8aa59fd383928f3
        A/clauses/window-06/prompt.txt: 8321a9b2f40d1827d395b2357f15c84100fb5e2bc9f71817e5a0184c5b41cf9e
        A/clauses/window-06/meta.json: 138af2ba079b0d5769a7fb8a00b6da581919849811fe0d3860884a2ff62c6ce0
        A/tables/TABLE-2-page-8-2/raw.json: b1daab80592c95079b2324ad4888be5638d0fe0a1f392e205f8d4225bd231a98
        A/tables/TABLE-2-page-8-2/prompt.txt: 4649511cda4fe22af44915da0dad735549b1d7736c0318ba07572a9bbb6208ea
        A/tables/TABLE-2-page-8-2/meta.json: 7ea24c51c9c40281334aee0911f14dda56033859225fb246694bd5ffed211ef5
        A/tables/TABLE-1-page-3-1/raw.json: 20737923793ff83e93d019c5ad6531876474b516544054372a5b951000a4b5d3
        A/tables/TABLE-1-page-3-1/prompt.txt: 2c765515f063dc7429587dd850d5fc42f9d3265524cbf7cba675396b299032ef
        A/tables/TABLE-1-page-3-1/meta.json: da08ce9e171bddeb53980605191af6b2c9f0a9e59e695e1c4c769030113097fd
        A/tables/TABLE-3-page-9-3/raw.json: b9a2e7b4061bcd03318b9b6db817be83a9217db942cd4b84d83102185302c447
        A/tables/TABLE-3-page-9-3/prompt.txt: 77fac605990c1a56e16b95d6695fe04e13c7bbe45be934d084c58b1157366ed8
        A/tables/TABLE-3-page-9-3/meta.json: f0ca8a58009dcbbab87a91d34c2ad53de42dc8b78603e46fe0b2bb03b0c8dc62
        A/tables/TABLE-4-page-9-4/raw.json: 1e86ab9e0482e9d8bf6896302121d096d3bb388b37cd2b167ad4809a3b06c311
        A/tables/TABLE-4-page-9-4/prompt.txt: 91c0f1dd26e72d9ecc0f8a2b72aa0ebdaff9d67badc194ffb7553350f88c26c3
        A/tables/TABLE-4-page-9-4/meta.json: 26c81784f87195d5de8b0209ee7e15151a104af0fdb20af1c4b7fa5fdf6e4f31
        B/passages.json: 64a24340ebe49bb996ed60b009ae466e80944869a95ba2586191e28f7770df46
        B/raw.json: bf0e603277156ebe8c63966294ca16580550fea760360d87702056720b9df4c0
        B/source-units.json: 49abd21d57e042f319a369cd5a62560388ab09e404cc717a62de6affe29ee1f8
        B/full-source-units.json: 3db4746fb7639bc4a34957dadfe47c338f85879f1c4b2cae5ab4e1dd5a9c5856
        B/meta.json: b0ca80488aea2bd89a8eb3c69df53e74bfc76d1ed4d08aaa0728d75242abdb2f
        B/table-images/TABLE-1-page-3-1.png: 2d8ba35f1dc552ccc2fc766958726139a1f12b7f5a21f34e21a399567a55f759
        B/table-images/TABLE-4-page-9-2.png: f16f9944224fc3fa4f8499063630c30889f4fb33d50cc96a0f2957b2f4a78158
        B/table-images/TABLE-3-page-9-1.png: f16f9944224fc3fa4f8499063630c30889f4fb33d50cc96a0f2957b2f4a78158
        B/table-images/TABLE-2-page-8-1.png: 5cd3f5a15dbce974f535f3e7cddb4b37d7967e0749605a18f8ef8d184fe6c137
        B/table-images/page-3.png: 6d762f30786fa7a784e7e8f8d7cf7e1ce736a10e1e0b0d64a9f8a354fc47881f
        B/table-images/page-9.png: fede3b992082cb35fc36d0841e74d5ce07457b6470b9125e0a33d45181e354c7
        B/table-images/page-8.png: 9dfcb6ac49b21d703b51bd532ab6c0c8719b481ac4fb0d09f9fd718dbb32708a
        B/table-images/manifest.json: 700805ab4ec6e1b8d73f800439adb93d24d70c504800f5bdbd344c998b3e4130
        B/clauses/window-03/raw.json: bc1cb7a86cc8f565612e4088fc1e3907d6e40dbfc917bead9c00e0286a7d0e40
        B/clauses/window-03/prompt.txt: cc29dcbc30a5404a6fa90fb33b2e35001e303c382fef42024df16dc5a2f3d2fb
        B/clauses/window-03/meta.json: 546d3f33463ad81d42437254dc3c6857a0faae4543905a68fbca6432e701bd54
        B/clauses/window-04/raw.json: 5dcac30a75fd1afce4705a62519f5174187af886152c78fa62ed60b43ea41dc5
        B/clauses/window-04/prompt.txt: 496320ce0863454c0f547041204993c6f95a8b48062a7ddb343dffa815777bae
        B/clauses/window-04/meta.json: 905a24ed49bd59f28939d1e6432333280a5a79eb2bb26c93d525f3e5f5365f61
        B/clauses/window-05/raw.json: b031490abbcbc1bb670e8e6d8ca518e1d0fd969097b295e96aa10b32d1a40c48
        B/clauses/window-05/prompt.txt: 6a64bdb52346130b8a072792d3a9f3983d62a5a926cf2c7a5cfe2b6387ddfb3f
        B/clauses/window-05/meta.json: 771fa07fa0c14f405412ae3db6101dbb04af32d653eaeb346e13e5181ab1eec6
        B/clauses/window-02/raw.json: deeb02e582e94122847e2d7a0a23a469fdcc8c5a6ba286e1b8ff32ccafbafd10
        B/clauses/window-02/prompt.txt: 8aff9eecfb3f9891bf50d5391f506d0cbba95fa78ce2adc371a7b565555b2935
        B/clauses/window-02/meta.json: 0b9145bebf1c7b7e0fabc11ce93731562a4e319fa824ed8bef8acbf5358df337
        B/clauses/window-07/raw.json: 706590768814dbab3ee2a1bc68708268d807c539f9672f52950d38c7aeeb312a
        B/clauses/window-07/prompt.txt: 0bc91ccab8ef50c32fb09462b8104cbcfdf02364b53285c485d60c3597d69945
        B/clauses/window-07/meta.json: 9a02e3d534db05ebc7371ba7aa66cb6093ea648c5eb0340c6a3bd028bc893bbb
        B/clauses/window-01/raw.json: 9708d648f1472d9c2a013f76e5c128256b23051fe10f7cdf99b857290af66686
        B/clauses/window-01/prompt.txt: d5ebc9ba4503507222ae4921a287e7681f2222d207b50da01c73025e812babe1
        B/clauses/window-01/meta.json: 37750c528e85af3d2e0e8987f531d72290c19b116e8093921ef26d37dbc82b3b
        B/clauses/window-06/raw.json: 020173608002f3008b950901a3ba61083f094d3d16fb4e9a3c2bf20cd8774626
        B/clauses/window-06/prompt.txt: 8321a9b2f40d1827d395b2357f15c84100fb5e2bc9f71817e5a0184c5b41cf9e
        B/clauses/window-06/meta.json: a42287a8494b41fc1b2424a8bb26abff74d7bed8bcaffe3c9f14e92710b1a1cb
        B/tables/TABLE-2-page-8-2/raw.json: b1daab80592c95079b2324ad4888be5638d0fe0a1f392e205f8d4225bd231a98
        B/tables/TABLE-2-page-8-2/prompt.txt: 4649511cda4fe22af44915da0dad735549b1d7736c0318ba07572a9bbb6208ea
        B/tables/TABLE-2-page-8-2/meta.json: 5fa57cd2c382323c5758943800189bb234225e2958c1300d04a5640951767367
        B/tables/TABLE-1-page-3-1/raw.json: 399197de787764448088fbe6fd8b9e285e1897fd2754770acdaf28e7c7fa9dad
        B/tables/TABLE-1-page-3-1/prompt.txt: 2c765515f063dc7429587dd850d5fc42f9d3265524cbf7cba675396b299032ef
        B/tables/TABLE-1-page-3-1/meta.json: b49d30ce7fa7a36844ee9aef1dcf6980787130292808ae8113f5155a88401143
        B/tables/TABLE-3-page-9-3/raw.json: b9a2e7b4061bcd03318b9b6db817be83a9217db942cd4b84d83102185302c447
        B/tables/TABLE-3-page-9-3/prompt.txt: 77fac605990c1a56e16b95d6695fe04e13c7bbe45be934d084c58b1157366ed8
        B/tables/TABLE-3-page-9-3/meta.json: 9d37513c3debaeeb0cb1651af1885d57da5a36425ea8aee5f233b5e3a4625c90
        B/tables/TABLE-4-page-9-4/raw.json: 0503b8ed514fe65b19eb5ad2d92006d98653e0e4fa7dcdb05f7faea1634e1985
        B/tables/TABLE-4-page-9-4/prompt.txt: 91c0f1dd26e72d9ecc0f8a2b72aa0ebdaff9d67badc194ffb7553350f88c26c3
        B/tables/TABLE-4-page-9-4/meta.json: 0a36557412036468bdf2bab4360a55e8b3e0e379b3f90ddc982e869f35078417
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
      pdf_sha256: f0d9fd6c287f4f6db14223ea7d376a5f77971f8c0a4a46440d328c1905892fce
      source_review: _compare/relationships-2026-11-16/review-current/Robson2019
      source_status_sha256: 3dfb83dbd5ea75789981df520079e7c9862e7af3fa4dccc34cbab70be87748cd
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R012
    exposure:
      text: age, average bilateral peripheral hearing threshold, or lesion volume
    outcome:
      text: comprehension score at 9 MPO
    analysis_label: Additional variable correlation
    relation: association
    evidence_ids:
    - P6-S1-C7
    - P11-S1-C6
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
      pdf_sha256: f0d9fd6c287f4f6db14223ea7d376a5f77971f8c0a4a46440d328c1905892fce
      source_review: _compare/relationships-2026-11-16/review-current/Robson2019
      source_status_sha256: 3dfb83dbd5ea75789981df520079e7c9862e7af3fa4dccc34cbab70be87748cd
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P3-S1-C6
      - Result passage disposed without unit P3-S2-C13
      - Result passage disposed without unit P3-S2-C14
      - Result passage disposed without unit P4-S1-C3
      - Result passage disposed without unit P5-S3-C2
      - Accounting without a linked unit P5-S3-C3
      - Result passage disposed without unit P5-S3-C4
      - Result passage disposed without unit P5-S3-C5
      - Accounting without a linked unit P6-S1-C3
      - Accounting without a linked unit P6-S1-C4
      - Accounting without a linked unit P6-S1-C5
      - Accounting without a linked unit P6-S1-C7
      - Unaccounted source passage P6-S1-C3
      - Unaccounted source passage P6-S1-C7
      - Unaccounted source passage P6-S1-C4
      - Unaccounted source passage P6-S1-C5
      - Unaccounted source passage P5-S3-C3
      - Accounting without a linked unit P6-S1-C11
      - Accounting without a linked unit P6-S2-C1
      - Accounting without a linked unit P8-S1-C1
      - Accounting without a linked unit P8-S1-C11
      - Accounting without a linked unit P8-S1-C2
      - Accounting without a linked unit P8-S1-C4
      - Accounting without a linked unit P8-S1-C8
      - Unaccounted source passage P8-S1-C8
      - Unaccounted source passage P6-S1-C11
      - Unaccounted source passage P8-S1-C2
      - Unaccounted source passage P8-S1-C4
      - Unaccounted source passage P8-S1-C11
      - Unaccounted source passage P8-S1-C1
      - Unaccounted source passage P6-S2-C1
      - Result passage disposed without unit P10-S1-C2
      - Result passage disposed without unit P10-S1-C3
      - Result passage disposed without unit P10-S1-C7
      - Result passage disposed without unit P10-S1-C8
      - Result passage disposed without unit P10-S2-C1
      - Result passage disposed without unit P10-S2-C4
      - Accounting without a linked unit P10-S2-C5
      - Accounting without a linked unit P10-S2-C6
      - Accounting without a linked unit P10-S2-C7
      - Unaccounted source passage P10-S2-C5
      - Unaccounted source passage P10-S2-C7
      - Unaccounted source passage P10-S2-C6
      - 'window 8: invalid/duplicate disposition P10-S3-C7'
      - 'window 8: invalid/duplicate disposition P10-S3-C9'
      - Result passage disposed without unit P10-S3-C9
      - Result passage disposed without unit P11-S1-C10
      - Result passage disposed without unit P11-S1-C7
      unattached_null_or_qualifier_ids:
      - P3-S2-C8
      - P5-S3-C3
      - P5-S3-C5
      - P6-S1-C5
      suppressed_nonrepresented_units: 12
      default_disposition_count_requires_completeness_check: 156
      unselected_timing_passages:
      - P1-S2-C9
      - P2-S2-C6
      - P2-S2-C13
      - P4-S1-C1
      - P10-S3-C5
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P5-S2-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S2-C12
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S2-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C2
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
      - slot: validation
        source_id: P5-S2-C6
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: tested_personal_effects
        source_id: P6-S1-C6
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: outcome_timing
        source_ids:
        - P1-S2-C10
        - P2-S2-C7
        - P5-S2-C7
        - P6-S1-C1
        - P6-S1-C5
        - P6-S1-C6
        - P6-S1-C9
        - P8-S1-C1
        - P8-S1-C2
        - P10-S1-C2
        - P10-S1-C3
        - P10-S1-C4
        - P10-S1-C5
        - P10-S1-C7
        - P10-S1-C8
        - P10-S2-C5
        - P10-S2-C6
        - P10-S2-C7
        - P11-S1-C10
        - P11-S1-C11
        - P11-S1-C12
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: limitations
        source_ids:
        - P5-S2-C4
        - P10-S3-C5
        - P10-S3-C7
        - P10-S3-C8
        - P10-S3-C9
        - P10-S3-C10
        - P11-S1-C2
        - P11-S1-C4
        - P11-S1-C5
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - outcome_timing
      - validation
      - limitations
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-3-1
      - TABLE-2-page-8-2
      - TABLE-3-page-9-3
      - TABLE-4-page-9-4
      unlinked_tables:
      - TABLE-1-page-3-1
      - TABLE-2-page-8-2
      - TABLE-3-page-9-3
      - TABLE-4-page-9-4
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P3-S2
        - P4-S2
        - P5-S2
        - P6-S2
        - P7-S1
        - P10-S1
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: f0d9fd6c287f4f6db14223ea7d376a5f77971f8c0a4a46440d328c1905892fce
      source_review: _compare/relationships-2026-11-16/review-current/Robson2019
      source_status_sha256: 3dfb83dbd5ea75789981df520079e7c9862e7af3fa4dccc34cbab70be87748cd
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S2-C12
      disposition: represented
      result_indexes:
      - 0
      reason: Reports strong and consistent recovery of language comprehension.
    - source_id: P1-S2-C13
      disposition: represented
      result_indexes:
      - 1
      - 2
      - 3
      - 4
      reason: Reports improvements in slow auditory temporal, phonological short-term
        memory, and semantic processing, and lack of improvement in others.
    - source_id: P1-S2-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Abstract summary of predictive findings already detailed in results.
    - source_id: P3-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes participant profiles (classical vs nonclassical WA).
    - source_id: P3-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes imaging exclusion criteria.
    - source_id: P3-S2-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes lesion distribution.
    - source_id: P3-S2-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes lesion overlap areas.
    - source_id: P4-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Explains rationale for composite measure.
    - source_id: P4-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes PCA method for composite score.
    - source_id: P5-S2-C8
      disposition: represented
      result_indexes:
      - 0
      reason: Provides ANOVA results for comprehension improvement.
    - source_id: P5-S2-C9
      disposition: repeated
      result_indexes:
      - 0
      reason: Restates comprehension improvement across case series.
    - source_id: P5-S2-C10
      disposition: represented
      result_indexes:
      - 0
      reason: Provides t-test results for pairwise comprehension improvements.
    - source_id: P5-S2-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the creation of the composite measure.
    - source_id: P5-S2-C12
      disposition: represented
      result_indexes:
      - 1
      - 2
      - 3
      reason: Reports significant improvements in slow auditory temporal, phonological
        short-term memory, and semantic association.
    - source_id: P5-S3-C1
      disposition: repeated
      result_indexes:
      - 1
      reason: Restates ANOVA for slow auditory temporal processing.
    - source_id: P5-S3-C2
      disposition: represented
      result_indexes:
      - 4
      reason: Notes lack of improvement in remaining neuropsychological tasks.
    - source_id: P5-S3-C3
      disposition: represented
      result_indexes:
      - 1
      - 2
      - 3
      reason: Provides t-test details for specific neuropsychological improvements.
    - source_id: P5-S3-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes baseline normal limits.
    - source_id: P5-S3-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes sensitivity check for normal limits.
    - source_id: P6-S1-C3
      disposition: represented
      result_indexes:
      - 9
      reason: Reports null relationship between comprehension and profile at 2.5 MPO.
    - source_id: P6-S1-C4
      disposition: represented
      result_indexes:
      - 5
      - 6
      - 7
      reason: Reports correlations at 5 MPO for phonological processing, rapid auditory
        processing, and nonverbal reasoning.
    - source_id: P6-S1-C5
      disposition: represented
      result_indexes:
      - 8
      reason: Reports correlation at 9 MPO for rapid auditory temporal processing.
    - source_id: P6-S1-C7
      disposition: represented
      result_indexes:
      - 10
      - 11
      reason: Reports correlations between 9 MPO comprehension and baseline comprehension,
        age, hearing, and lesion volume.
    - source_id: P6-S1-C10
      disposition: represented
      result_indexes:
      - 17
      reason: Reports null relationship between 2.5 MPO scores and 5 MPO comprehension.
    - source_id: P6-S1-C11
      disposition: represented
      result_indexes:
      - 12
      - 13
      reason: Reports associations between 2.5 MPO rapid auditory/phonological memory
        and 9 MPO comprehension.
    - source_id: P6-S2-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Figure 2 caption.
    - source_id: P8-S1-C1
      disposition: repeated
      result_indexes:
      - 12
      reason: Restates association of 2.5 MPO rapid auditory processing with 9 MPO
        comprehension.
    - source_id: P8-S1-C2
      disposition: represented
      result_indexes:
      - 14
      - 15
      reason: Reports associations between 5 MPO word/nonword phonological processing
        and 9 MPO comprehension.
    - source_id: P8-S1-C8
      disposition: repeated
      result_indexes:
      - 9
      reason: Restates null relationship at 2.5 MPO.
    - source_id: P8-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion summary of emerging relationships.
    - source_id: P8-S1-C12
      disposition: repeated
      result_indexes:
      - 5
      - 6
      - 8
      reason: Discussion restatement of 5 MPO and 9 MPO associations.
    - source_id: P8-S2-C1
      disposition: repeated
      result_indexes:
      - 5
      - 6
      - 8
      reason: Discussion restatement of 5 MPO and 9 MPO associations.
    - source_id: P10-S1-C2
      disposition: repeated
      result_indexes:
      - 0
      reason: Restates comprehension improvement.
    - source_id: P10-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes recovery curve similarity.
    - source_id: P10-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about recovery of associated functions.
    - source_id: P10-S1-C8
      disposition: repeated
      result_indexes:
      - 1
      - 2
      - 3
      reason: Restates group-level improvements in specific neuropsychological assessments.
    - source_id: P10-S2-C1
      disposition: repeated
      result_indexes:
      - 1
      - 2
      - 3
      reason: Restates group-level improvements in specific neuropsychological assessments.
    - source_id: P10-S2-C2
      disposition: represented
      result_indexes:
      - 4
      reason: Reports lack of consistent recovery in phonological and rapid auditory
        processing.
    - source_id: P10-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: General discussion of findings.
    - source_id: P10-S2-C5
      disposition: represented
      result_indexes:
      - 18
      reason: Reports independence of comprehension recovery from slow auditory and
        semantic processing.
    - source_id: P10-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: General discussion of rapid auditory/phonological influence.
    - source_id: P10-S2-C7
      disposition: represented
      result_indexes:
      - 12
      - 14
      reason: Restates cross-lagged associations for rapid auditory (2.5 MPO) and
        word phonological (5 MPO) processing.
    - source_id: P10-S3-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes therapy content.
    - source_id: P10-S3-C10
      disposition: represented
      result_indexes:
      - 19
      reason: Reports no correlation between therapy amount and comprehension outcomes.
    - source_id: P11-S1-C1
      disposition: repeated
      result_indexes:
      - 19
      reason: Restates null effect of therapy involvement.
    - source_id: P11-S1-C6
      disposition: repeated
      result_indexes:
      - 11
      reason: Restates null relationship between age and comprehension.
    - source_id: P11-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion summary of long-term outcomes.
    - source_id: P11-S2-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion summary of constraints on recovery.
    - source_id: P11-S2-C2
      disposition: repeated
      result_indexes:
      - 12
      reason: Restates association of subacute rapid auditory processing with chronic
        outcome.
    unresolved_coverage:
    - source_id: P10-S3-C10
      disposition: unresolved
      reason: Unknown result index; not accepted as coverage
    - source_id: P11-S1-C1
      disposition: unresolved
      reason: Unknown result index; not accepted as coverage
    - source_id: P11-S2-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P8-S1-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S2-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C12
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S2-C14
    - P3-S1-C6
    - P3-S2-C8
    - P3-S2-C13
    - P3-S2-C14
    - P4-S1-C3
    - P4-S1-C4
    - P5-S2-C9
    - P5-S2-C11
    - P5-S3-C1
    - P5-S3-C4
    - P5-S3-C5
    - P6-S2-C1
    - P8-S1-C1
    - P8-S1-C4
    - P8-S1-C11
    - P8-S1-C12
    - P8-S2-C1
    - P10-S1-C2
    - P10-S1-C3
    - P10-S1-C7
    - P10-S1-C8
    - P10-S2-C1
    - P10-S2-C3
    - P10-S2-C4
    - P10-S2-C6
    - P10-S3-C9
    - P11-S1-C7
    - P11-S1-C10
    - P11-S1-C11
    - P11-S1-C12
    - P11-S2-C2
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-3-1
    - TABLE-2-page-8-2
    - TABLE-3-page-9-3
    - TABLE-4-page-9-4
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P2-S3-C4
      - P2-S3-C6
      - P3-S1-C6
      recruited_sample:
      - P2-S3-C4
      - P2-S3-C6
      eligibility:
      - P2-S3-C1
      - P2-S3-C6
      - P3-S1-C5
      imaging_provenance:
      - P3-S2-C4
      - P3-S2-C7
      - P3-S2-C9
      - P4-S2-C7
      imaging_timing:
      - P3-S1-C4
      outcome_timing: []
      outcome_definition:
      - P3-S2-C16
      - P3-S2-C17
      - P4-S1-C3
      - P5-S2-C11
      validation: []
      analysis_restrictions:
      - P4-S1-C4
      - P6-S1-C9
      dependent_variable_statement:
      - P6-S1-C9
      limitations: []
      personal_factors:
      - P5-S2-C3
      tested_personal_effects:
      - P6-S1-C7
      - P10-S3-C10
      - P11-S1-C6
      adjustment_roles:
      - P6-S1-C8
      - P6-S1-C9
      explicitly_not_adjusted:
      - P10-S3-C11
      descriptive_personal_factors:
      - P3-S1-C2
      - P3-S2-C3
      - P5-S2-C3
    outcome_type: both_reported
    imaging_vs_outcome: mixed
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P5-S2-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S2-C12
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S2-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C2
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
    - slot: validation
      source_id: P5-S2-C6
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: tested_personal_effects
      source_id: P6-S1-C6
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: outcome_timing
      source_ids:
      - P1-S2-C10
      - P2-S2-C7
      - P5-S2-C7
      - P6-S1-C1
      - P6-S1-C5
      - P6-S1-C6
      - P6-S1-C9
      - P8-S1-C1
      - P8-S1-C2
      - P10-S1-C2
      - P10-S1-C3
      - P10-S1-C4
      - P10-S1-C5
      - P10-S1-C7
      - P10-S1-C8
      - P10-S2-C5
      - P10-S2-C6
      - P10-S2-C7
      - P11-S1-C10
      - P11-S1-C11
      - P11-S1-C12
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: limitations
      source_ids:
      - P5-S2-C4
      - P10-S3-C5
      - P10-S3-C7
      - P10-S3-C8
      - P10-S3-C9
      - P10-S3-C10
      - P11-S1-C2
      - P11-S1-C4
      - P11-S1-C5
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
      pdf_sha256: f0d9fd6c287f4f6db14223ea7d376a5f77971f8c0a4a46440d328c1905892fce
      review_sha256: 247c2b79bca5ff0a9804e6890d49e4426eaf820e8d361ec054aebaefb27f6580
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
      - P6-S1-C7
      - P11-S1-C6
      source_result: Pearson correlations between comprehension scores at 9 MPO and
        additional variables (age, average bilateral peripheral hearing threshold,
        and lesion volume in voxels) found no significant relationship for any of
        these variables. A significant correlation was found between comprehension
        scores at 2.5 MPO and 9 MPO.
      result_status: not_detected
      patient_measurement: non_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis corresponds to the 'Correlation With Additional
            Variables' section (P6-S1-C6), which explicitly tests the association
            between 9 MPO comprehension and age, hearing, and lesion volume. The source
            confirms these specific variables were tested in this context.
          source_ids:
          - P6-S1-C6
          - P6-S1-C7
        direction:
          answer: fits
          reason: The source states 'not age, hearing, or lesion volume' were significantly
            correlated (P6-S1-C7), and P11-S1-C6 confirms 'no systematic relationship
            between age and comprehension outcome'. The draft's 'no_effect' direction
            accurately reflects the lack of detected association.
          source_ids:
          - P6-S1-C7
          - P11-S1-C6
        construct:
          answer: fits
          reason: The exposure variables (age, hearing, lesion volume) and outcome
            (comprehension at 9 MPO) are correctly identified. The patient measurement
            is non_imaging (behavioral/clinical metrics), not diffusion or template
            overlap, as the analysis uses Pearson correlations on these specific variables
            rather than voxel-wise imaging analysis.
          source_ids:
          - P6-S1-C6
          - P5-S2-C3
        qualifications:
          answer: fits
          reason: The draft includes the qualification that comprehension at 2.5 MPO
            was significantly correlated with 9 MPO, which is a key context from P6-S1-C7
            and P6-S1-C8. This qualification is material as it explains why 2.5 MPO
            was later used as a covariate, but the null result for the other variables
            stands in this specific correlation analysis.
          source_ids:
          - P6-S1-C7
          - P6-S1-C8
        missing_material_caveat:
          answer: fits
          reason: The draft includes limitations regarding sample size and recruitment
            bias. No material caveats regarding the specific null findings for age/hearing/lesion
            volume are omitted that would change the interpretation of the null result
            itself.
          source_ids:
          - P10-S3-C5
          - P5-S2-C4
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
        text: age, average bilateral peripheral hearing threshold, or lesion volume
      outcome:
        text: comprehension score at 9 MPO
      analysis_label: Additional variable correlation
      relation: association
      evidence_ids:
      - P6-S1-C7
      - P11-S1-C6
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
        pdf_sha256: f0d9fd6c287f4f6db14223ea7d376a5f77971f8c0a4a46440d328c1905892fce
        source_review: _compare/relationships-2026-11-16/review-current/Robson2019
        source_status_sha256: 3dfb83dbd5ea75789981df520079e7c9862e7af3fa4dccc34cbab70be87748cd
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P2-S3-C4:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: f0d9fd6c287f4f6db14223ea7d376a5f77971f8c0a4a46440d328c1905892fce
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 5c87e3a6260db818b81e8712a03e96e21f92c0606e55b7f801e0a664c3075f9d
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S3-C4
          page: 2
          text_layer_sha256: 5c87e3a6260db818b81e8712a03e96e21f92c0606e55b7f801e0a664c3075f9d
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "A total of 24 participants were \nreferred to the study of\
          \ whom 17 were contactable and 12 \nfulfilled the inclusion and exclusion\
          \ criteria and consented \nto participate."
        anchor_text: "A total of 24 participants were \nreferred to the study of whom\
          \ 17 were contactable and 12 \nfulfilled the inclusion and exclusion criteria\
          \ and consented \nto participate."
        excluded_fragments: []
        image_sha256: 03fd965fa280c98b7a4a8f6036ac89b81e89bbc79cf066cdaa486ab86d2a4c93
        transcription: '. A total of 24 participants were

          referred to the study of whom 17 were contactable and 12

          fulfilled the inclusion and exclusion criteria and consented

          to participate'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 6
  quote: "Correlation With Additional Variables\nOnset severity and age have been\
    \ shown to influence \nrecovery from stroke.43 Pearson correlations explored the\
    \ \nrelationship between comprehension scores at 9 MPO and \nadditional variables:\
    \ comprehension score at 2.5 MPO, \nage, average bilateral peripheral hearing\
    \ threshold, and \nlesion volume in voxels."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-25'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
