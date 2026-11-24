---
id: stroke_location_moca_predictor
name: stroke location (MoCA predictor)
kind: predictor
findings:
- id: f1
  target: moca_score
  target_kind: prognosis
  claim: Stroke location is an independent predictor of cognitive outcome (MoCA) at
    3 months post stroke; including stroke location in a predictive model with age,
    initial NIHSS, and stroke volume significantly improves the prediction of cognitive
    outcome compared to using those variables alone.
  direction: likely
  relationship: correlational
  method: VLSM
  sample:
    n: not_reported
    population: Consecutive patients with suspected supratentorial ischemic stroke
      (NIHSS 1-25), excluding those with prestroke dementia or severe cognitive impairment.
    phase: not_reported
    time_post_onset: Imaging and NIHSS assessed 24 to 72 hours post stroke; cognitive
      outcome measured at 3 months.
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - The cohort contained primarily mild ischemic stroke patients, as severe patients
    were less tolerant of the MRI procedure.
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Patient lesion overlap with a population-based voxel-based
    lesion-symptom mapping (VLSM) map of cognitive eloquent regions, quantified as
    the number of eloquent voxels contained in the lesion. The improvement in prediction
    was validated in both a development sample (n=215) and an independent replication
    sample (n=74); A subanalysis using a short MoCA (sMoCA) without naming and language
    items produced similar results, suggesting the effect is not driven by aphasia
    alone. Additional metadata has not been transcribed; review the pending-field
    flags before approval. PDF image reading (P2-S2-C5, two-model agreement, human
    verification pending): .

    Primary inclusion criteria were men and women, older than 18

    years old, with a clinical diagnosis of minor-to-severe supratentorial

    cerebral infarct (NIHSS between 1 and 25) between 24 and 72 hours

    after the onset Original text-layer quotation is preserved below.'
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
    - proposed_concept:moca_score
  citation: '@Munsch2016'
  source_passages:
  - section: Original source P1-S2-C6
    page: 1
    quote: "In multivariable analyses, stroke location remained the \nstrongest independent\
      \ predictor of MoCA and significantly improved the prediction compared with\
      \ using only age, \ninitial National Institutes of Health Stroke Scale, and\
      \ stroke volume (area under the curve increased from 0.697–0.771; \ndifference=0.073;\
      \ 95% confidence interval, 0.008–0.155)."
    supports: claim
  - section: Original source P1-S2-C9
    page: 1
    quote: Conclusions—Stroke location is an independent predictor of cognitive outcome
      (MoCA) at 3 months post stroke.
    supports: claim
  - section: Original source P2-S2-C5
    page: 2
    quote: "Primary inclusion criteria were men and women, older than 18 \nyears old,\
      \ with a clinical diagnosis of minor-to-severe supratentorial \ncerebral infarct\
      \ (NIHSS between 1 and 25) between 24 and 72 hours \nafter the onset."
    supports: sample
  - section: Original source P2-S2-C6
    page: 2
    quote: "Exclusion criteria were history of symptomatic cere-\nbral infarct with\
      \ functional deficit (prestroke modified Rankin Scale \n[mRS] score ≥1), infratentorial\
      \ stroke, history of severe cognitive im-\npairment (dementia), or psychiatric\
      \ troubles matching to axis 1 of the \nDiagnostic and Statistical Manual of\
      \ Mental Disorders, Fourth edi-\ntion (DSM-IV) criteria except for major depression,\
      \ coma, pregnant \nor breast-feeding women, and contraindications to MRI."
    supports: sample
  - section: Original source P3-S1-C5
    page: 3
    quote: "This quantitative variable contains the information of location \nand\
      \ will be referred to as stroke location in the following sections."
    supports: method
  - section: Original source P4-S2-C3
    page: 4
    quote: "In multivariate analysis, the association between stroke \nlocation and\
      \ MoCA persisted (β=−0.293; 95% CI, −0.421 \nto −0.165) and was the variable\
      \ with the highest significance \nfollowed by baseline NIHSS (β=−0.158; 95%\
      \ CI, −0.264 \nto −0.051) and age (β=−0.048; 95% CI, −0.074 to −0.021; \nTable 3)."
    supports: claim
  - section: Original source P4-S2-C4
    page: 4
    quote: "This was illustrated by the significantly higher AUC \nof model 2 (AUC=0.771)\
      \ compared with that of model 1 \n(AUC=0.697) after the internal validation\
      \ step (Table 4; dif-\nference=0.073; 95% CI, 0.008–0.155; Figure 3B)."
    supports: claim
  - section: Original source P4-S2-C9
    page: 4
    quote: "In contrast, stroke location was significantly different between \npatients\
      \ with good and poor cognitive outcomes (median of \n25 eloquent voxels for\
      \ MoCA >25 versus 138 eloquent voxels \nfor MoCA ≤25; P=0.001; Table 2) and\
      \ significantly improved \nthe logistic regression model of cognitive outcome\
      \ (Table 4; \ndifference=0.119; 95% CI, 0.035–0.203; P=0.005; Figure \n3D)."
    supports: claim
  - section: Original source P6-S1-C10
    page: 6
    quote: "Our cohort contained \nmild ischemic stroke patients."
    supports: limitation
predictor_type: imaging_metric
short_definition: Patient lesion overlap with a population-based voxel-based lesion-symptom
  mapping (VLSM) map of cognitive eloquent regions, quantified as the number of eloquent
  voxels contained in the lesion.
assessment:
- Montreal Cognitive Assessment (MoCA)
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-25'
relationship_review:
  paper: Munsch2016
  proposal_id: R010
  review_status_sha256: dc30dc5b842a16b6252193a391aea9d04a0246fd48fb95369bcb09f69352f17d
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 0d28d32fcc74e177de672709f2e3a5ccd13ba1fb22ef4fb5a5c5748144366ff8
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 0d28d32fcc74e177de672709f2e3a5ccd13ba1fb22ef4fb5a5c5748144366ff8
        A/passages.json: cee335f2d01a2dfb2cbd0cf35d4fbccdaa81716d0b79a78bafaffa0abdd3ad39
        A/raw.json: 024a10224b08e199aa168c5f9d2a5dd837dcd3662f436a1a2116a7caccbb62e1
        A/source-units.json: a716b694f1a291ce9d91de24a100bfff38b72afa802ee99a1476525b57c4106e
        A/full-source-units.json: 342ed81cc5151a168d1ff66e69a9b85879e6e8fd84588901a6fb7c865c7231f9
        A/meta.json: c2023be3f6e915085215be5126308115fc5f5496869062753596529aff2a2395
        A/table-images/page-6.png: dc0160277df586fe752158f624b1e6e01907e73d3119de826eb1edfe7af63b9e
        A/table-images/page-5.png: 4b86fbea939ccb09766da6f8a38c7d0e998200767b20362dc16952d169782abb
        A/table-images/page-4.png: bd8edf4705abbee924c248cd4dcf3557c23b417bece9122cc6ce5d3445ab174d
        A/table-images/TABLE-1-page-4-1.png: 46f5b40cef3564f7f7446f6ea20b91b84916e537ff4d4b2bd317ec11f3cba8dd
        A/table-images/TABLE-4-page-6-1.png: 46948b4998d27eaaf7948de107d98895177c5ed444f8e8c44f1dbc05fc91a738
        A/table-images/TABLE-3-page-6-2.png: 173d81acc80864d4bb7805697018658b6ede18626d78ee17c118276cece73df1
        A/table-images/manifest.json: 7b83693198734d5eb043e170fa0212ce2dd5d880f6c46285c20fb740ac66d6b9
        A/table-images/TABLE-2-page-5-1.png: dbede997ead5fc682be266fd80cc6a6c0ed0249d286dfa5e7ba3f15080220aa9
        A/clauses/window-03/raw.json: 39b1f79de5193180b1e8ce63f1c9b5831b10d94def6bce3ed32f9e00dfdbf489
        A/clauses/window-03/prompt.txt: 9ea71eb0340b6d061398256e4268139746f1bb2be2554ced3da714dfd9104c5d
        A/clauses/window-03/meta.json: 91d1350147de1dcb03c8a07e5d19067af18c65f7155d1c9445e0b74856027e0c
        A/clauses/window-04/raw.json: 52c2f3fe2b5003d4a024f1ce3ceb313757962313db960a7d797fb976511a18b0
        A/clauses/window-04/prompt.txt: b6965ad8c07f1bf10deda1c9ff846e7f796746d86da9b0d37e541dea83fe7c72
        A/clauses/window-04/meta.json: e1d30d2bcdb501f9b69b3276fc73636c73506bb3e1897a6b89f75694ab75cc05
        A/clauses/window-05/raw.json: b6dc2c53879b5505a980c38c0eddc6ba80f3280227e136060e246473528bda03
        A/clauses/window-05/prompt.txt: 2ce1770ff951810cef92e80700a236bfe743b05d962b23a02b7a9e6d227f0a46
        A/clauses/window-05/meta.json: f2be574b9c77b1b01413954bf03b185691ad1ccc82148b7f5b6d6b75ebcec8e2
        A/clauses/window-02/raw.json: beab8aae3a747115a17fa775f7f855db88b12ff2678f42b642b40c8c2fdbc0b7
        A/clauses/window-02/prompt.txt: 15e7da9211dc58ada4051c32283c11adb6d12c02a4ac1897d425562c08101080
        A/clauses/window-02/meta.json: 83e64ed9130099d842080bc3bb9a03d8959f3fe42c57428ee64627c311af8018
        A/clauses/window-01/raw.json: c72afd42d979bb3d8113c0d10a99efe83086d72377bfc3becf5e94072f9b403a
        A/clauses/window-01/prompt.txt: bce24db64b3dbb701cc602f49b224dcd176de1717f4a21ae555d1650ab3b5a15
        A/clauses/window-01/meta.json: 9b62de46ab0846e5f7171de8738565ae2f09ccd60f3ef05f9cbdd7475047a5d0
        A/tables/TABLE-4-page-6-3/raw.json: af791ab8b4055431e2cb5cbd683164c87f543a2908905e2b1347b3324c8caf31
        A/tables/TABLE-4-page-6-3/prompt.txt: 279027dfa442e8b11c3dad17a3b5cb92ff99b70d27f66dd3586b222e4bf5eb1d
        A/tables/TABLE-4-page-6-3/meta.json: e478f7fbd8ac2d202672049dd7bfeb1cdca5962ed4e7c07b957a2e397009bd00
        A/tables/TABLE-2-page-5-2/raw.json: ae4748153f82bb97a424a14dd0b98cf56e5a8504c35061a10a1a215c51dc26a0
        A/tables/TABLE-2-page-5-2/prompt.txt: ed349b604c8064bafa0ab3129bc81a84ca93a2548cda8ae01ae9a7ecf46d06a9
        A/tables/TABLE-2-page-5-2/meta.json: 4f10350ebfee0a3e65de4c66c37e425f2df248d81f653dd83d017ff0da7f8878
        A/tables/TABLE-3-page-6-4/raw.json: 93271c101aa1af7ff6ed817fe62481de74b91fab98d448d6ecfcb25d27f12388
        A/tables/TABLE-3-page-6-4/prompt.txt: 22f1d63a0865227d002fc580d066e5d8802b4b03fc6c1684657c5648ec3cd050
        A/tables/TABLE-3-page-6-4/meta.json: f1ee5f909daefc3a7fa41bef214b537f5d2d6eaa9a1841bfa2360ae44af5e9dc
        A/tables/TABLE-1-page-4-1/raw.json: 558891d1bcce401c43aba21a6db26228c8a60002234e745f5b759712f8645cfb
        A/tables/TABLE-1-page-4-1/prompt.txt: cd963af133c1e8284e6247095b6d398b1d45ab56451a927c179fc1f7533011b2
        A/tables/TABLE-1-page-4-1/meta.json: 5d70faab732175b278d26d509e27926f821306c4c0bc680c75bd10bdb0b8057a
        B/passages.json: cee335f2d01a2dfb2cbd0cf35d4fbccdaa81716d0b79a78bafaffa0abdd3ad39
        B/raw.json: 24ae1111f7ae3093674db9dbc491868a81da62243759299d541a106d7f6c2d44
        B/source-units.json: a716b694f1a291ce9d91de24a100bfff38b72afa802ee99a1476525b57c4106e
        B/full-source-units.json: 342ed81cc5151a168d1ff66e69a9b85879e6e8fd84588901a6fb7c865c7231f9
        B/meta.json: 44b6c5a501bc0246feb0b7b256cb8414e0283f80b9b6922e9296e1a0d38542d9
        B/table-images/page-6.png: dc0160277df586fe752158f624b1e6e01907e73d3119de826eb1edfe7af63b9e
        B/table-images/page-5.png: 4b86fbea939ccb09766da6f8a38c7d0e998200767b20362dc16952d169782abb
        B/table-images/page-4.png: bd8edf4705abbee924c248cd4dcf3557c23b417bece9122cc6ce5d3445ab174d
        B/table-images/TABLE-1-page-4-1.png: 46f5b40cef3564f7f7446f6ea20b91b84916e537ff4d4b2bd317ec11f3cba8dd
        B/table-images/TABLE-4-page-6-1.png: 46948b4998d27eaaf7948de107d98895177c5ed444f8e8c44f1dbc05fc91a738
        B/table-images/TABLE-3-page-6-2.png: 173d81acc80864d4bb7805697018658b6ede18626d78ee17c118276cece73df1
        B/table-images/manifest.json: 2a5c34f38fad300830ebf78aa39bc057fbbfb7def29840eac07243b2bcf07f3b
        B/table-images/TABLE-2-page-5-1.png: dbede997ead5fc682be266fd80cc6a6c0ed0249d286dfa5e7ba3f15080220aa9
        B/clauses/window-03/raw.json: aaa77402ba3ce4e451a5ab237cfaeffa379864349ad5d204ea1dceb10cd18fd8
        B/clauses/window-03/prompt.txt: 9ea71eb0340b6d061398256e4268139746f1bb2be2554ced3da714dfd9104c5d
        B/clauses/window-03/meta.json: 0a4b591d6313d40aefd378eb8bc90b8eed17874fea8d69bb2c361b159469af30
        B/clauses/window-04/raw.json: d23eb7ae7b7b00da4eb562fe290b7d5ba4e7ce443d0636fca889e8435c5cb9ca
        B/clauses/window-04/prompt.txt: b6965ad8c07f1bf10deda1c9ff846e7f796746d86da9b0d37e541dea83fe7c72
        B/clauses/window-04/meta.json: e9613ffb7b63c18552c4f69ace486c545ba1bce40c842812478adaf23f4f69cc
        B/clauses/window-05/raw.json: 5d0e1b24bbaa195095b99e99734f6b7b3a9db21512425e2f99a3e86e38263d2f
        B/clauses/window-05/prompt.txt: 2ce1770ff951810cef92e80700a236bfe743b05d962b23a02b7a9e6d227f0a46
        B/clauses/window-05/meta.json: 6617b03fd187e65becb7776ad1ac9e3f203e7937bf61484222ea52c2a6ac68d7
        B/clauses/window-02/raw.json: 7de2b4f5a17a8486190feb8d309776a6084b313ae5dca3301a220d6dd771dce5
        B/clauses/window-02/prompt.txt: 15e7da9211dc58ada4051c32283c11adb6d12c02a4ac1897d425562c08101080
        B/clauses/window-02/meta.json: 65b85dcefbf33a34e4a70cb7060ff6c984d9de9b31ef6d29804c6caf4b13a088
        B/clauses/window-01/raw.json: 457260f2e4daad9176641b66ebfebadde3bdae133c3d331751e5ac158913d6d3
        B/clauses/window-01/prompt.txt: bce24db64b3dbb701cc602f49b224dcd176de1717f4a21ae555d1650ab3b5a15
        B/clauses/window-01/meta.json: 9246e9077676fcec4ea2ad3bdfd93acdde4c09c6c15cbaf4ae6df535a82c5642
        B/tables/TABLE-4-page-6-3/raw.json: 071f99e51e89384ffa92e4b2c0a9dd069738b7c418ad638aae66f27f7bce6fae
        B/tables/TABLE-4-page-6-3/prompt.txt: 279027dfa442e8b11c3dad17a3b5cb92ff99b70d27f66dd3586b222e4bf5eb1d
        B/tables/TABLE-4-page-6-3/meta.json: 32ecea808e343aa555e4999c08c233c009ee200f0f5f278addf79c4fa3106e28
        B/tables/TABLE-2-page-5-2/raw.json: 85916d25a4984742f294543c12c840b4186baf04d0355517c1df2a6489706901
        B/tables/TABLE-2-page-5-2/prompt.txt: ed349b604c8064bafa0ab3129bc81a84ca93a2548cda8ae01ae9a7ecf46d06a9
        B/tables/TABLE-2-page-5-2/meta.json: 02d2e62f8bc6082328f0df5f0f6d019e70b5153dad6e09fe32b5c3100101f3a3
        B/tables/TABLE-3-page-6-4/raw.json: 49457e08766156fd24c985d173b34d7875768c4cb2eefe3d4b2c9dae051f0e5b
        B/tables/TABLE-3-page-6-4/prompt.txt: 22f1d63a0865227d002fc580d066e5d8802b4b03fc6c1684657c5648ec3cd050
        B/tables/TABLE-3-page-6-4/meta.json: 1fde95e67d97ef4336cc960c253001f3ac451a069c517b3503695e59abec0777
        B/tables/TABLE-1-page-4-1/raw.json: 3cf81cdc3a2c02729686f6f80deef1fe960ec0fddd5d646e4cbc43c12678d8a3
        B/tables/TABLE-1-page-4-1/prompt.txt: cd963af133c1e8284e6247095b6d398b1d45ab56451a927c179fc1f7533011b2
        B/tables/TABLE-1-page-4-1/meta.json: 85152bd25b4d76f3390a233f8148faa175d9e41ee5bdaf2f4c6c4a0ef59bee31
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
      pdf_sha256: 0d28d32fcc74e177de672709f2e3a5ccd13ba1fb22ef4fb5a5c5748144366ff8
      source_review: _compare/relationships-2026-11-16/review-current/Munsch2016
      source_status_sha256: e6cce494dc77bc5b787b653ba82df446295ec792508349196fe7d52f1fa13a34
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R010
    exposure:
      text: stroke location (Model 2 vs Model 1)
    outcome:
      text: MoCA
    analysis_label: Model comparison (Internal Validation)
    relation: performance
    evidence_ids:
    - P1-S2-C6
    - P4-S2-C4
    qualifier_ids:
    - P4-S2-C4
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 0d28d32fcc74e177de672709f2e3a5ccd13ba1fb22ef4fb5a5c5748144366ff8
      source_review: _compare/relationships-2026-11-16/review-current/Munsch2016
      source_status_sha256: e6cce494dc77bc5b787b653ba82df446295ec792508349196fe7d52f1fa13a34
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Accounting without a linked unit P1-S2-C5
      - Accounting without a linked unit P1-S2-C6
      - Accounting without a linked unit P1-S2-C7
      - Accounting without a linked unit P1-S2-C8
      - Accounting without a linked unit P1-S2-C9
      - Unaccounted source passage P1-S2-C5
      - Unaccounted source passage P1-S2-C6
      - Unaccounted source passage P1-S2-C7
      - Unaccounted source passage P1-S2-C8
      - Unaccounted source passage P1-S2-C9
      - Accounting without a linked unit P4-S1-C2
      - Accounting without a linked unit P4-S1-C3
      - Accounting without a linked unit P4-S1-C4
      - Unaccounted source passage P4-S1-C2
      - Unaccounted source passage P4-S1-C3
      - Unaccounted source passage P4-S1-C4
      - Result passage disposed without unit P4-S1-C10
      - Result passage disposed without unit P4-S1-C11
      - Result passage disposed without unit P4-S1-C8
      - Result passage disposed without unit P4-S1-C9
      - Result passage disposed without unit P4-S2-C1
      - Result passage disposed without unit P4-S2-C2
      - Result passage disposed without unit P4-S2-C3
      - Result passage disposed without unit P4-S2-C7
      - Result passage disposed without unit P5-S1-C5
      - Result passage disposed without unit P5-S1-C8
      - Result passage disposed without unit P5-S2-C1
      - Result passage disposed without unit P6-S1-C1
      - Accounting without a linked unit P6-S1-C2
      - Result passage disposed without unit P6-S2-C4
      - Result passage disposed without unit P6-S2-C5
      - Accounting without a linked unit P6-S2-C8
      - Unaccounted source passage P6-S2-C8
      - Unaccounted source passage P6-S1-C2
      unattached_null_or_qualifier_ids:
      - P1-S2-C6
      - P1-S2-C7
      - P4-S1-C4
      - P4-S1-C8
      - P4-S1-C10
      - P4-S2-C1
      - P5-S1-C6
      - P5-S1-C8
      - P5-S2-C1
      - P6-S1-C1
      - P6-S2-C5
      suppressed_nonrepresented_units: 10
      default_disposition_count_requires_completeness_check: 100
      unselected_timing_passages:
      - P1-S1-C6
      - P2-S1-C6
      - P2-S2-C5
      - P2-S2-C9
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P4-S1-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S2-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S2-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S3-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P3-S2-C3
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P3-S2-C4
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P4-S2-C7
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P4-S2-C8
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P4-S2-C9
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P6-S2-C3
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: tested_personal_effects
        source_id: P2-S2-C8
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: outcome_timing
        source_ids:
        - P2-S2-C9
        - P2-S3-C2
        - P2-S4-C3
        - P3-S1-C1
        - P3-S2-C10
        - P4-S1-C8
        - P4-S2-C1
        - P5-S2-C10
        - P5-S2-C11
        - P5-S3-C5
        - P5-S3-C6
        - P6-S1-C2
        - P6-S2-C8
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: outcome_definition
        source_ids:
        - P2-S2-C9
        - P2-S2-C10
        - P2-S3-C1
        - P3-S1-C7
        - P3-S1-C8
        - P3-S1-C9
        - P4-S1-C8
        - P4-S2-C1
        - P4-S2-C5
        - P5-S2-C5
        - P6-S1-C2
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - outcome_timing
      - outcome_definition
      - tested_personal_effects
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-4-1
      - TABLE-2-page-5-2
      - TABLE-3-page-6-4
      - TABLE-4-page-6-3
      unlinked_tables:
      - TABLE-1-page-4-1
      - TABLE-3-page-6-4
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P2-S3
        - P3-S2
        - P4-S1
        - P4-S2
        - P4-S3
        - P5-S2
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 0d28d32fcc74e177de672709f2e3a5ccd13ba1fb22ef4fb5a5c5748144366ff8
      source_review: _compare/relationships-2026-11-16/review-current/Munsch2016
      source_status_sha256: e6cce494dc77bc5b787b653ba82df446295ec792508349196fe7d52f1fa13a34
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S2-C5
      disposition: represented
      result_indexes:
      - 0
      - 1
      - 2
      - 3
      reason: Reports univariate predictive value of location, age, NIHSS, and volume
        for mRS and MoCA.
    - source_id: P1-S2-C6
      disposition: represented
      result_indexes:
      - 4
      - 10
      reason: Reports stroke location as independent predictor of MoCA and AUC improvement.
    - source_id: P1-S2-C7
      disposition: represented
      result_indexes:
      - 8
      - 11
      reason: Reports stroke location not persisting as independent predictor for
        mRS and AUC change.
    - source_id: P1-S2-C8
      disposition: represented
      result_indexes:
      - 13
      - 14
      reason: Confirms similar results in replication sample.
    - source_id: P1-S2-C9
      disposition: repeated
      result_indexes:
      - 4
      reason: Conclusion restating stroke location as independent predictor of MoCA.
    - source_id: P3-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient demographics for development sample.
    - source_id: P3-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient demographics for replication sample.
    - source_id: P3-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Prestroke cognitive state (IQCODE) for replication sample.
    - source_id: P3-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of VLSM maps in Figure 2.
    - source_id: P4-S1-C2
      disposition: represented
      result_indexes:
      - 18
      reason: VLSM analysis showing left hemisphere association with worse functional
        outcome.
    - source_id: P4-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Anatomical description of motor pathway regions.
    - source_id: P4-S1-C4
      disposition: represented
      result_indexes:
      - 17
      reason: VLSM analysis showing left lateralization for MoCA.
    - source_id: P4-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Univariate difference in eloquent voxels for mRS groups.
    - source_id: P4-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Univariate discrimination of mRS groups by NIHSS, age, and volume.
    - source_id: P4-S1-C10
      disposition: represented
      result_indexes:
      - 8
      reason: Multivariate analysis showing NIHSS as only independent predictor for
        mRS.
    - source_id: P4-S1-C11
      disposition: represented
      result_indexes:
      - 11
      reason: Internal validation AUC difference for mRS models.
    - source_id: P4-S2-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Univariate difference in eloquent voxels for MoCA groups.
    - source_id: P4-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Univariate discrimination of MoCA groups by NIHSS, age, and volume.
    - source_id: P4-S2-C3
      disposition: represented
      result_indexes:
      - 4
      - 5
      - 6
      reason: Multivariate analysis for MoCA showing location, NIHSS, and age as predictors.
    - source_id: P4-S2-C4
      disposition: represented
      result_indexes:
      - 10
      reason: Internal validation AUC comparison for MoCA models.
    - source_id: P4-S2-C6
      disposition: represented
      result_indexes:
      - 12
      reason: sMoCA subanalysis AUC results.
    - source_id: P4-S2-C7
      disposition: repeated
      result_indexes:
      - 13
      - 14
      reason: General statement confirming main findings in replication sample.
    - source_id: P4-S2-C8
      disposition: represented
      result_indexes:
      - 15
      reason: Replication sample AUC difference for mRS models.
    - source_id: P4-S2-C9
      disposition: represented
      result_indexes:
      - 13
      - 14
      reason: Replication sample results for MoCA association and model performance.
    - source_id: P4-S2-C10
      disposition: represented
      result_indexes:
      - 16
      reason: Replication sample sMoCA model performance.
    - source_id: P5-S1-C1
      disposition: represented
      result_indexes:
      - 12
      - 16
      reason: AUC results for sMoCA in development and replication samples.
    - source_id: P5-S1-C3
      disposition: repeated
      result_indexes:
      - 4
      reason: Discussion restatement of location as independent predictor of MoCA.
    - source_id: P5-S1-C4
      disposition: repeated
      result_indexes:
      - 10
      reason: Discussion restatement of AUC improvement for MoCA.
    - source_id: P5-S1-C5
      disposition: repeated
      result_indexes:
      - 11
      reason: Discussion restatement of mRS prediction being driven by NIHSS.
    - source_id: P5-S2-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Anatomical description of eloquent areas in MoCA map.
    - source_id: P5-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Anatomical description of thalamus in MoCA map.
    - source_id: P5-S2-C3
      disposition: represented
      result_indexes:
      - 17
      reason: Discussion of left hemisphere association with cognitive impairment.
    - source_id: P5-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to Table 2.
    - source_id: P5-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: 'Table 2: Characteristics of patients according to cognitive outcome.'
    - source_id: P5-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Table 2 legend.
    - source_id: P5-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to Figure 2.
    - source_id: P5-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Figure 2 caption.
    - source_id: P5-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Figure 2 color range description.
    - source_id: P5-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Figure 2A/B description.
    - source_id: P5-S2-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Figure 2A/B color interpretation.
    - source_id: P5-S2-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Figure 2C/D description.
    - source_id: P5-S3-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Figure 2C/D description.
    - source_id: P5-S3-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Figure 2C/D color interpretation.
    - source_id: P6-S1-C1
      disposition: repeated
      result_indexes:
      - 12
      - 16
      reason: Discussion restatement of sMoCA results.
    - source_id: P6-S1-C2
      disposition: repeated
      result_indexes:
      - 8
      reason: Discussion restatement of location not being an independent predictor
        for mRS.
    - source_id: P6-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of sample differences and generalization.
    - source_id: P6-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of VLSM map voxel counts.
    - source_id: P6-S2-C8
      disposition: repeated
      result_indexes:
      - 10
      reason: Conclusion restating MoCA prediction improvement.
    - source_id: P6-S3-C1
      disposition: represented
      result_indexes:
      - 11
      reason: 'Table 4: AUC for mRS development sample internal validation.'
    - source_id: P6-S3-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Table 4 model definitions.
    - source_id: P6-S3-C5
      disposition: represented
      result_indexes:
      - 4
      - 5
      - 6
      - 8
      reason: 'Table 3: Regression coefficients for mRS and MoCA.'
    unresolved_coverage:
    - source_id: P4-S1-C2
      disposition: unresolved
      reason: Unknown result index; not accepted as coverage
    - source_id: P4-S2-C10
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P5-S2-C4
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P5-S2-C5
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P5-S2-C6
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P5-S2-C7
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P5-S2-C8
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P5-S2-C9
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P5-S2-C10
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P5-S2-C11
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P5-S2-C12
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P5-S3-C5
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P5-S3-C6
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P6-S3-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P6-S3-C2
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P6-S3-C5
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P5-S1-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P5-S1-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S2-C9
    - P3-S2-C6
    - P3-S2-C7
    - P3-S2-C8
    - P3-S2-C10
    - P4-S1-C3
    - P4-S1-C8
    - P4-S1-C9
    - P4-S2-C1
    - P4-S2-C2
    - P4-S2-C7
    - P5-S1-C3
    - P5-S1-C4
    - P5-S1-C5
    - P5-S1-C6
    - P5-S1-C8
    - P5-S2-C1
    - P5-S2-C2
    - P6-S1-C1
    - P6-S1-C2
    - P6-S2-C4
    - P6-S2-C5
    - P6-S2-C8
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-4-1
    - TABLE-2-page-5-2
    - TABLE-3-page-6-4
    - TABLE-4-page-6-3
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P2-S3-C6
      - P3-S2-C2
      recruited_sample:
      - P2-S2-C3
      eligibility:
      - P2-S2-C5
      - P2-S2-C6
      imaging_provenance:
      - P2-S3-C2
      - P2-S3-C3
      - P2-S3-C8
      - P5-S2-C8
      imaging_timing:
      - P2-S3-C2
      - P6-S1-C7
      outcome_timing: []
      outcome_definition: []
      validation:
      - P3-S1-C15
      - P3-S1-C16
      - P3-S2-C2
      - P4-S1-C11
      analysis_restrictions:
      - P2-S4-C5
      dependent_variable_statement:
      - P1-S2-C3
      - P3-S1-C7
      - P4-S1-C6
      limitations:
      - P6-S1-C9
      - P6-S1-C10
      - P6-S1-C11
      - P6-S2-C5
      personal_factors:
      - P2-S2-C8
      tested_personal_effects: []
      adjustment_roles:
      - P1-S2-C3
      - P3-S1-C12
      - P3-S1-C13
      - P4-S1-C6
      - P4-S1-C10
      - P4-S2-C3
      - P6-S3-C2
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P2-S2-C8
      - P3-S2-C5
      - P3-S2-C6
      - P5-S2-C5
    outcome_type: status_at_assessment
    imaging_vs_outcome: precedes_outcome
    validation_type: mixed
    held_selections:
    - slot: dependent_variable_statement
      source_id: P4-S1-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S2-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S2-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S3-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P3-S2-C3
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P3-S2-C4
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P4-S2-C7
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P4-S2-C8
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P4-S2-C9
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P6-S2-C3
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: tested_personal_effects
      source_id: P2-S2-C8
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: outcome_timing
      source_ids:
      - P2-S2-C9
      - P2-S3-C2
      - P2-S4-C3
      - P3-S1-C1
      - P3-S2-C10
      - P4-S1-C8
      - P4-S2-C1
      - P5-S2-C10
      - P5-S2-C11
      - P5-S3-C5
      - P5-S3-C6
      - P6-S1-C2
      - P6-S2-C8
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: outcome_definition
      source_ids:
      - P2-S2-C9
      - P2-S2-C10
      - P2-S3-C1
      - P3-S1-C7
      - P3-S1-C8
      - P3-S1-C9
      - P4-S1-C8
      - P4-S2-C1
      - P4-S2-C5
      - P5-S2-C5
      - P6-S1-C2
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
      pdf_sha256: 0d28d32fcc74e177de672709f2e3a5ccd13ba1fb22ef4fb5a5c5748144366ff8
      review_sha256: dc30dc5b842a16b6252193a391aea9d04a0246fd48fb95369bcb09f69352f17d
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
      - P1-S2-C6
      - P4-S2-C4
      source_result: In the development sample, adding stroke location (number of
        eloquent voxels) to a model containing age, NIHSS, and stroke volume significantly
        improved the prediction of MoCA outcome (AUC increased from 0.697 to 0.771;
        difference=0.073; 95% CI 0.008–0.155) after internal validation. This finding
        was confirmed in the replication sample.
      result_status: detected
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis corresponds to the model comparison (Model
            2 vs Model 1) for MoCA outcome in the development sample, as described
            in P1-S2-C6 and P4-S2-C4. The exposure is stroke location, and the outcome
            is MoCA.
          source_ids:
          - P1-S2-C6
          - P4-S2-C4
          - P3-S1-C12
          - P3-S1-C13
        direction:
          answer: fits
          reason: The source states that stroke location significantly improved prediction
            (AUC increase), which aligns with the 'detected' status and the claim
            that it is an independent predictor. The direction of the effect (improvement
            in prediction) is consistent across the development and replication samples.
          source_ids:
          - P1-S2-C6
          - P4-S2-C4
          - P4-S2-C9
        construct:
          answer: fits
          reason: The exposure is correctly identified as stroke location, measured
            as the number of eloquent voxels from VLSM maps (template_lesion_overlap).
            The outcome is MoCA. The method is VLSM. The population is ischemic stroke
            patients. The timing is 24-72h imaging and 3-month outcome.
          source_ids:
          - P1-S1-C6
          - P3-S1-C5
          - P3-S1-C7
          - P4-S2-C1
        qualifications:
          answer: fits
          reason: 'The draft includes the key qualifications: validation in both development
            and replication samples, and the subanalysis with sMoCA. The limitation
            regarding mild stroke patients is also included. These are faithful to
            the source.'
          source_ids:
          - P1-S2-C8
          - P4-S2-C5
          - P4-S2-C6
          - P6-S1-C10
        missing_material_caveat:
          answer: fits
          reason: No material caveats are missing. The draft correctly notes the internal
            validation and replication. The unresolved image-reading disagreements
            in P2-S2-C6 and P2-S2-C9 do not affect the core result of the model comparison
            for MoCA, which is clearly stated in the prose of P1-S2-C6 and P4-S2-C4.
          source_ids:
          - P1-S2-C6
          - P4-S2-C4
          - P6-S1-C10
      optional_pending:
      - Sample size requires source confirmation; it has not been transcribed.
      - Specific AUC values and confidence intervals are not transcribed in the draft,
        but the qualitative result (significant improvement) is present.
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Sample size requires source confirmation; it has not been transcribed.
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Sample size requires source confirmation; it has not been transcribed.
    - Specific AUC values and confidence intervals are not transcribed in the draft,
      but the qualitative result (significant improvement) is present.
    normalizations:
    - field: sample.n
      original: 289
      action: not_transcribed
      reason: Not supported by selected quotations
    analysis_identity:
      id: R010
      exposure:
        text: stroke location (Model 2 vs Model 1)
      outcome:
        text: MoCA
      analysis_label: Model comparison (Internal Validation)
      relation: performance
      evidence_ids:
      - P1-S2-C6
      - P4-S2-C4
      qualifier_ids:
      - P4-S2-C4
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 0d28d32fcc74e177de672709f2e3a5ccd13ba1fb22ef4fb5a5c5748144366ff8
        source_review: _compare/relationships-2026-11-16/review-current/Munsch2016
        source_status_sha256: e6cce494dc77bc5b787b653ba82df446295ec792508349196fe7d52f1fa13a34
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P2-S2-C5:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 0d28d32fcc74e177de672709f2e3a5ccd13ba1fb22ef4fb5a5c5748144366ff8
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 7ba5f1a414af341981603c0f8e2891eadb4abc557c7a0459b7d7822e2ddf785e
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S2-C5
          page: 2
          text_layer_sha256: 7ba5f1a414af341981603c0f8e2891eadb4abc557c7a0459b7d7822e2ddf785e
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "Primary inclusion criteria were men and women, older than\
          \ 18 \nyears old, with a clinical diagnosis of minor-to-severe supratentorial\
          \ \ncerebral infarct (NIHSS between 1 and 25) between 24 and 72 hours \n\
          after the onset."
        anchor_text: "Primary inclusion criteria were men and women, older than 18\
          \ \nyears old, with a clinical diagnosis of minor-to-severe supratentorial\
          \ \ncerebral infarct (NIHSS between 1 and 25) between 24 and 72 hours \n\
          after the onset."
        excluded_fragments: []
        image_sha256: 803d9fd950b0c7d3614f9f92bd6ebdced497915f17a270a278b642efe86364fe
        transcription: '.

          Primary inclusion criteria were men and women, older than 18

          years old, with a clinical diagnosis of minor-to-severe supratentorial

          cerebral infarct (NIHSS between 1 and 25) between 24 and 72 hours

          after the onset'
      P2-S2-C6:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 0d28d32fcc74e177de672709f2e3a5ccd13ba1fb22ef4fb5a5c5748144366ff8
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 3d96654770e190171cab133e839d4ceb7d8884b7f8a6fc3f0a32b649f093aab5
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S2-C6
          page: 2
          text_layer_sha256: 3d96654770e190171cab133e839d4ceb7d8884b7f8a6fc3f0a32b649f093aab5
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: "Exclusion criteria were history of symptomatic cere-\nbral\
          \ infarct with functional deficit (prestroke modified Rankin Scale \n[mRS]\
          \ score ≥1), infratentorial stroke, history of severe cognitive im-\npairment\
          \ (dementia), or psychiatric troubles matching to axis 1 of the \nDiagnostic\
          \ and Statistical Manual of Mental Disorders, Fourth edi-\ntion (DSM-IV)\
          \ criteria except for major depression, coma, pregnant \nor breast-feeding\
          \ women, and contraindications to MRI."
        anchor_text: "Exclusion criteria were history of symptomatic cere-\nbral infarct\
          \ with functional deficit (prestroke modified Rankin Scale \n[mRS] score\
          \ ≥1), infratentorial stroke, history of severe cognitive im-\npairment\
          \ (dementia), or psychiatric troubles matching to axis 1 of the \nDiagnostic\
          \ and Statistical Manual of Mental Disorders, Fourth edi-\ntion (DSM-IV)\
          \ criteria except for major depression, coma, pregnant \nor breast-feeding\
          \ women, and contraindications to MRI."
        excluded_fragments: []
        image_sha256: c4a982579e44b9f08c601d4dcb656db81225d9a44e28b2a1f615fc122c9548ce
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 1
  quote: "In multivariable analyses, stroke location remained the \nstrongest independent\
    \ predictor of MoCA and significantly improved the prediction compared with using\
    \ only age, \ninitial National Institutes of Health Stroke Scale, and stroke volume\
    \ (area under the curve increased from 0.697–0.771; \ndifference=0.073; 95% confidence\
    \ interval, 0.008–0.155)."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-25'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
