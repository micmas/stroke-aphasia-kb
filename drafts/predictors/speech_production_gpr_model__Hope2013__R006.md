---
id: speech_production_gpr_model
name: speech production GPR predictor
kind: predictor
findings:
- id: f1
  target: speech_production_score
  target_kind: prognosis
  claim: A combination of time post-stroke and lesion damage can accurately predict
    later assessment scores for speech production in stroke patients.
  direction: likely
  relationship: correlational
  method: MVPA
  sample:
    n: 270
    population: stroke patients with focal brain damage, aged 20 to 90 years, excluding
      those less than 1 month post-stroke at assessment
    phase: not_reported
    time_post_onset: longitudinal prediction of future scores based on initial assessment
      and imaging; data includes patients from less than one month to more than 30
      years post-stroke
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - The model systematically underestimates the severity of impairments for the most
    impaired patients
  - The dataset pools scans from very different recovery phases (acute to chronic),
    which may introduce noise
  - Potential for over-fitting in the feature selection process
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: A Gaussian Process Regression model using a combination
    of time post-stroke, lesion volume, and encroachment into 35 specific brain regions
    (derived from T1-weighted MRI scans and atlas-based coding). The model was validated
    using a longitudinal configuration on 38 patients who were assessed more than
    once; The preferred predictor configuration includes time post-stroke as the most
    significant single predictor. Additional metadata has not been transcribed; review
    the pending-field flags before approval. PDF image reading (P5-S1-C5, two-model
    agreement, human verification pending): . The best subset included

    37 relevant predictors (R² = 0.59, F = 38.38, p < 0.001), including

    time post-stroke (the most significant, single predictor), lesion

    volume, and encroachment into 35 regions of the brain (listed in

    Table 1) Original text-layer quotation is preserved below. PDF image reading (P2-S2-C4,
    two-model agreement, human verification pending): . We only excluded patients
    if they:


    a) were very young (<20 years) or very old (>90 years)

    b) were less than 1 month post-stroke at assessment

    c) had evidence of other significant neurological conditions (e.g. dementia, multiple
    sclerosis)

    d) did not speak English as a first language

    e) showed no visible damage anywhere in the brain, as assessed by a neurologist
    (APL), using the patients'' raw T1-weighted scans

    f) had suffered dispersed rather than focal damage Original text-layer quotation
    is preserved below. PDF image reading (P2-S3-C3, two-model agreement, human verification
    pending): . This selection process left us with

    data from 270 patients, but with repeated assessments for some patients

    at different times post-stroke, our dataset included a total of 315 speech

    production scores.


    2.3. Original text-layer quotation is preserved below. PDF image reading (P8-S1-C11,
    two-model agreement, human verification pending): Limitations of the current study


    One criticism of the system described here is that it pools scans taken both soon
    after stroke (within the first month), and many years later (30 years or more)
    Original text-layer quotation is preserved below.'
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
    - proposed_concept:speech_production_score
  citation: '@Hope2013'
  source_passages:
  - section: Original source P5-S2-C4
    page: 5
    quote: 'After learning from just

      the patient data used for the cross-sectional conﬁguration, our learner

      can predict the later assessment scores very accurately (R2 = 0.84,

      F = 225.00, p b 0.001; see Fig. 5).

      3.8.'
    supports: claim
  - section: Original source P5-S1-C5
    page: 5
    quote: 'The best subset included

      37 relevant predictors (R2 = 0.59, F = 38.38, p b 0.001), including

      time post-stroke (the most signiﬁcant, single predictor), lesion

      volume, and encroachment into 35 regions of the brain (listed in

      Table 1).'
    supports: method
  - section: Original source P5-S1-C10
    page: 5
    quote: 'Predicting longitudinal data

      As determined by ARD, our preferred predictor conﬁguration for

      speech production skills is a combination of time post-stroke and lesion

      damage.'
    supports: claim
  - section: Original source P2-S2-C4
    page: 2
    quote: 'We only excluded patients if they:

      a) were very young (b20 years) or very old (>90 years)

      b) were less than 1 month post-stroke at assessment

      c) had evidence of other signiﬁcant neurological conditions (e.g. de-

      mentia, multiple sclerosis)

      d) did not speak English as a ﬁrst language

      e) showed no visible damage anywhere in the brain, as assessed by a

      neurologist (APL), using the patients'' raw T1-weighted scans

      f) had suffered dispersed rather than focal damage.'
    supports: sample
  - section: Original source P2-S3-C3
    page: 2
    quote: 'This selection process left us with

      data from 270 patients, but with repeated assessments for some patients

      at different times post-stroke, our dataset included a total of 315 speech

      production scores.

      2.3.'
    supports: sample
  - section: Original source P8-S2-C5
    page: 8
    quote: 'Another more immediate criticism is that our preferred predictor

      conﬁguration systematically under-estimates the severity of the impair-

      ments suffered by the most impaired patients in our dataset (i.e. by

      predicting speech production scores consistently above those actually

      assigned on assessment; see Fig. 4).'
    supports: limitation
  - section: Original source P8-S1-C11
    page: 8
    quote: 'Limitations of the current study

      One criticism of the system described here is that it pools scans taken

      both soon after stroke (within the ﬁrst month), and many years later

      (30 years or more).'
    supports: limitation
  - section: Original source P8-S3-C6
    page: 8
    quote: 'In this work, we have selected a preferred

      conﬁguration on the basis of its performance within and across the data

      we have, which raises the spectre of over-ﬁtting in the feature selection

      process, and consequent questions concerning its generalisation to in-

      dependent data.'
    supports: limitation
predictor_type: imaging_metric
short_definition: A Gaussian Process Regression model using a combination of time
  post-stroke, lesion volume, and encroachment into 35 specific brain regions (derived
  from T1-weighted MRI scans and atlas-based coding).
assessment:
- Comprehensive Aphasia Test
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-24'
relationship_review:
  paper: Hope2013
  proposal_id: R006
  review_status_sha256: 1a02cea8e83bdb908a2496b7f14ecf8ab679535b2204ce474d97fa2a487a2997
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: a48c35b7451ad08b6d510255208ab948deb5a6a6d76ad93eea27445b207a4a31
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: a48c35b7451ad08b6d510255208ab948deb5a6a6d76ad93eea27445b207a4a31
        A/passages.json: d0342f4ec30482de08693515e39bc7480da4f397e76ce8ff737bf663f55d0865
        A/raw.json: 88343cc527b142ac77ad9d1bf608018a569cebbd89f1784bea789211f75f7e4c
        A/source-units.json: d768726d391c53abcb5e56a17e61ed0782d925807b4a65b3fef45da0905cfd86
        A/full-source-units.json: ad68f2c8bf1953b90ab23000b4acd048aa3b30cd4b589fdd3f9080c53ff1fb0c
        A/meta.json: 2d97cb9ec908b8f9d968ad22f9f32292c362431843ea06fa36063043ba526308
        A/table-images/TABLE-1-page-6-1.png: 516dd041a4a8593a1490c342df34699856f27fea66601a6afdec37166d9e9f06
        A/table-images/page-6.png: 85411e2d1a76c89dfc6a81c6e63e0664f6cbf192bc1a9e9e70d9d6fc53544f62
        A/table-images/TABLE-3-page-6-3.png: 3dee2e2a19f6913a3a9d70506b19427e672b70da9bde2f6129897a1f4955f62b
        A/table-images/manifest.json: edebef6fc7fce5c383578a66e40d883bf42539ea92938744c786de151f65b5f1
        A/table-images/TABLE-2-page-6-2.png: 0fbcaaaaddeffe1386cab6053bd49751ff87774a39e14e730cf7989fc73e5466
        A/clauses/window-03/raw.json: 9207b702f835380a270aa446205f2817d5f04c32fe0c074fdb9d1b19cb16e4a6
        A/clauses/window-03/prompt.txt: 843eb3847e0ba077ce8cd3f85f8f2a632d39091836ea22937f30af8799c63172
        A/clauses/window-03/meta.json: 0a6cee076a5893edd8ca917e4a49bf338ee177ae7ac44b4c11ceb6bb8a6de4ef
        A/clauses/window-04/raw.json: 1d9fc24335b6761c2c354828360be5f2d30cb9927aa1302d48701eb467787526
        A/clauses/window-04/prompt.txt: fc3332e20c0e4bd7792d813b64bbb5a0422d0af2cd37770a06a3acaf5ae538cd
        A/clauses/window-04/meta.json: 9eb9d2d7016f5f68cbf17daff43b2f4f0ad28c374e1beef2dc8ae020faea489a
        A/clauses/window-05/raw.json: 87df72c45f23b7baeaac8fc450d04803b09919f13cb6473675f6255ec5259a32
        A/clauses/window-05/prompt.txt: 1a70b887311c4eaf9eb5a4f0a041a7ac380e3febff36d0476adbeeb0a30650b3
        A/clauses/window-05/meta.json: 8e88e7d0ad40b5b7ede48b0cee0464e2fbddbd03e63afa368e5481492fc1c2de
        A/clauses/window-02/raw.json: 94fe12c6673fa16fd4e603aec572abe17cedff3cb9c58012e9139beee732405e
        A/clauses/window-02/prompt.txt: d391efe8402379571e1c0d16ddbc4ca296859cf26778fb1341f6bb28e806644e
        A/clauses/window-02/meta.json: b7b3e44653fbe17e5f5a6b8cf35469997c1b5f09a23bf4e091a19e77d9b15efe
        A/clauses/window-09/raw.json: 52c2444dbee099c96f8c3a3eaeec25b0423eb28ad14022e345ecb589a386a5ca
        A/clauses/window-09/prompt.txt: ce2f900cebc8af03b46e7c3d2c4f8d3730bd21dc8657c7d51b27543e6aa43991
        A/clauses/window-09/meta.json: 4543d55ba8933a52890da08925ccd97ee07f31ab6fe078a0c605844184ad6d1f
        A/clauses/window-07/raw.json: 4ed3f0d95d346a923f08dea9de7debd62f0f0f619a3ac6d72b03c2bc2e71bfac
        A/clauses/window-07/prompt.txt: 2570855b56198d35a9ece1d892762b27f6f43e1d647d71c99e06ac94217f802d
        A/clauses/window-07/meta.json: a4b1acd794dd1d101183b917ebba943d9d468afd7bbd20c31fccbe13becdff11
        A/clauses/window-01/raw.json: 578825e54c4307770df98a8ac0a9165398ae57d57eb5c0e37d438bd352eb1305
        A/clauses/window-01/prompt.txt: a8fe4061417d4a5bef41ac80eb60667ac0080a8c0b48708431a4cfb41300b938
        A/clauses/window-01/meta.json: 18e5c0fdfbec463f06d28d520fc7daf7d5a136af679e1a358c11ad8b5191eacc
        A/clauses/window-06/raw.json: e88e3d7c3a8eeba2b0a30ccdac3a968c15643e1e3177a64d9cebaa5352edfac6
        A/clauses/window-06/prompt.txt: b639f82960c164f41416a5a67e5ac99187f638e8a409832ce25e38392bc66a69
        A/clauses/window-06/meta.json: df2aeda991051c1dd525d33daa7edd85cffe7cd98653bdbbab3de6ca808a6331
        A/clauses/window-08/raw.json: 599345ffa12db43b5b4700d29ae1fa4d35535bb46edbce588ace0870468c325b
        A/clauses/window-08/prompt.txt: 7cf44f4d4f82e4bf3acdb6188518faf1c752ae17f92ad7276819eadfc8cd28b7
        A/clauses/window-08/meta.json: 5277f5a05a883e14068beeb7f5f38ad4323cf9415392ce955301a02dcca561d5
        A/tables/TABLE-1-page-6-1/raw.json: 3f589b4d74a34d72bc2b456c68d172a3155badf02f9ccc4dab5b7d71d829af52
        A/tables/TABLE-1-page-6-1/prompt.txt: 44137a7d3690d7478ead9ec116f0f083e9f82e3dff3a9750c351bee1811f903d
        A/tables/TABLE-1-page-6-1/meta.json: 794434a3ddd7b4cb93f9011880742e8e7dad5daa4638ad7a85808d10064a69dd
        A/tables/TABLE-3-page-6-3/raw.json: 3eef3e8a8474d1942b38d057fbe2fc80abef3a41f8a99d95abe1036c8d840770
        A/tables/TABLE-3-page-6-3/prompt.txt: d270f0a8220c09c1de9bb4c9a6283afadce0e73eb4bd1a78f2e6e3c9589544ab
        A/tables/TABLE-3-page-6-3/meta.json: d5058e4134cd28796f45a16294423278163cf107bac3623b3f7237b80bffb5ef
        A/tables/TABLE-2-page-6-2/raw.json: cba3f3f3dc1397122f8c2c759692ea1ba30cd0a9263b204ebbc94a154ce796ee
        A/tables/TABLE-2-page-6-2/prompt.txt: dd251a98290bb5182830c38715eeb8d262f7d6c1fa5601fb6d680a936b762d2e
        A/tables/TABLE-2-page-6-2/meta.json: e2f29e97c0241e97b3e10633d2599224ef6cb38846979d9c6f482b828b282e5e
        B/passages.json: d0342f4ec30482de08693515e39bc7480da4f397e76ce8ff737bf663f55d0865
        B/raw.json: feac5c8cff70e2d1ee97eadce7d82e0094d03c9289892755db1987794a5c46ee
        B/source-units.json: d768726d391c53abcb5e56a17e61ed0782d925807b4a65b3fef45da0905cfd86
        B/full-source-units.json: ad68f2c8bf1953b90ab23000b4acd048aa3b30cd4b589fdd3f9080c53ff1fb0c
        B/meta.json: 8cbde3a7a773e8543bce500557d1cd5121f89936efb51ae37f8a262301a50e19
        B/table-images/TABLE-1-page-6-1.png: 516dd041a4a8593a1490c342df34699856f27fea66601a6afdec37166d9e9f06
        B/table-images/page-6.png: 85411e2d1a76c89dfc6a81c6e63e0664f6cbf192bc1a9e9e70d9d6fc53544f62
        B/table-images/TABLE-3-page-6-3.png: 3dee2e2a19f6913a3a9d70506b19427e672b70da9bde2f6129897a1f4955f62b
        B/table-images/manifest.json: 7ac8a7c3875f6116b8cf37a6a443b4fa4589746619a0c242cc5ee9ac669926ea
        B/table-images/TABLE-2-page-6-2.png: 0fbcaaaaddeffe1386cab6053bd49751ff87774a39e14e730cf7989fc73e5466
        B/clauses/window-03/raw.json: 15f7e373546da54ac764484635f5b9a346d3b1956dd5abbfb3383adb0f089e98
        B/clauses/window-03/prompt.txt: 843eb3847e0ba077ce8cd3f85f8f2a632d39091836ea22937f30af8799c63172
        B/clauses/window-03/meta.json: 17b89fab1ffa568caa1d62dbacf304ca44477e8facd4a4d47f3157182111d369
        B/clauses/window-04/raw.json: 019139e2d68555eb923b689081e05889b75a403a7459b9f1372afe021d53c959
        B/clauses/window-04/prompt.txt: fc3332e20c0e4bd7792d813b64bbb5a0422d0af2cd37770a06a3acaf5ae538cd
        B/clauses/window-04/meta.json: 7eb013c963b3c6b8e7e36637678cea31bf63905eee4112bad4b1b35878371c32
        B/clauses/window-05/raw.json: 57b90b173fd6252ac8a4aeb636c634ae42e2567295422e4720b8c76e25037b6e
        B/clauses/window-05/prompt.txt: 1a70b887311c4eaf9eb5a4f0a041a7ac380e3febff36d0476adbeeb0a30650b3
        B/clauses/window-05/meta.json: 55efb22c11979e802492c63d3fa83391890dd30fa52940173d70498de54dc28e
        B/clauses/window-02/raw.json: 4c6af90a26e4f46ff5cb519664282c36f4a07ab230be4b0743aefba45fc9ac98
        B/clauses/window-02/prompt.txt: d391efe8402379571e1c0d16ddbc4ca296859cf26778fb1341f6bb28e806644e
        B/clauses/window-02/meta.json: b24b7ac9e3081d07476147b3a436f00c32cb66fe13ed0fbc84ed4ff4bcad5bc0
        B/clauses/window-09/raw.json: 6a6249d23e70bf316cb47d73251a304dc139f5ea3dd873af54c5e30d8785749c
        B/clauses/window-09/prompt.txt: ce2f900cebc8af03b46e7c3d2c4f8d3730bd21dc8657c7d51b27543e6aa43991
        B/clauses/window-09/meta.json: 466307692d61b4046ca6621e3514f5c768ea0c892aaaaf6e079f51dd6a1c6d37
        B/clauses/window-07/raw.json: ee1e133ccb73c25c55d08bbff31c2cefc7cc94da66b4cfa521209dcfa82dfaa1
        B/clauses/window-07/prompt.txt: 2570855b56198d35a9ece1d892762b27f6f43e1d647d71c99e06ac94217f802d
        B/clauses/window-07/meta.json: 5ed85f7c861c6b36e3f017c1b5f132bb79a2731e0beac89ec6c1846d0e7993a9
        B/clauses/window-01/raw.json: 0f60a730a2b16606aec9b972a8dcbf4836936a4f3decf77a2d66e5bd48599501
        B/clauses/window-01/prompt.txt: a8fe4061417d4a5bef41ac80eb60667ac0080a8c0b48708431a4cfb41300b938
        B/clauses/window-01/meta.json: 345e4effd36939d802b1da509495fec900018a9e98602d9555d587df9ceec045
        B/clauses/window-06/raw.json: 45d609f7db9bb32e41d899c70b45d429bb3199fb80a8f7d9de0229a6c331dc56
        B/clauses/window-06/prompt.txt: b639f82960c164f41416a5a67e5ac99187f638e8a409832ce25e38392bc66a69
        B/clauses/window-06/meta.json: faf5a32144bb0502b38cd7bbb9fc8cdd7325e8398d16c228f547418c284755a5
        B/clauses/window-08/raw.json: 672bd77323b8a9b5213df9284734f570f6558e94aacf09912f0b71e314e9f8f1
        B/clauses/window-08/prompt.txt: 7cf44f4d4f82e4bf3acdb6188518faf1c752ae17f92ad7276819eadfc8cd28b7
        B/clauses/window-08/meta.json: 179cff5e5787f7e8f9ef1ae5feea230a9f11c5ded3f1900672460743ea5731a8
        B/tables/TABLE-1-page-6-1/raw.json: 7bb523c20ac64f7d38ab408da15d67fdf27f16b6761a8d5016b7ed414839e2da
        B/tables/TABLE-1-page-6-1/prompt.txt: 44137a7d3690d7478ead9ec116f0f083e9f82e3dff3a9750c351bee1811f903d
        B/tables/TABLE-1-page-6-1/meta.json: 30166b7a65a55e315ab4479c5f42528603e9f008648162d3b03cbab62eb63503
        B/tables/TABLE-3-page-6-3/raw.json: 1e78f7090ef7461cb2818fb011feaa1a42837b9f21a2928c3c98570b87a7958e
        B/tables/TABLE-3-page-6-3/prompt.txt: d270f0a8220c09c1de9bb4c9a6283afadce0e73eb4bd1a78f2e6e3c9589544ab
        B/tables/TABLE-3-page-6-3/meta.json: 2748154009ce2163c0dd180c86ba6454446ffd646bf3474b115902539553d642
        B/tables/TABLE-2-page-6-2/raw.json: 83a87b335e81e1bc7972bc444496ea7d32a1fe1982bb1e1bf6e6e1acbc9cb2b6
        B/tables/TABLE-2-page-6-2/prompt.txt: dd251a98290bb5182830c38715eeb8d262f7d6c1fa5601fb6d680a936b762d2e
        B/tables/TABLE-2-page-6-2/meta.json: e1e58e8ab20c6120c82c8b3d2b7e9c1ea168b5accb73387aaf1b2a6be0a34281
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
      pdf_sha256: a48c35b7451ad08b6d510255208ab948deb5a6a6d76ad93eea27445b207a4a31
      source_review: _compare/relationships-2026-11-16/review-current/Hope2013
      source_status_sha256: 2dad0ec35b3ff43b44735b94ddc98425c92c525778a7d5426c760e069dcacd88
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R006
    exposure:
      text: preferred predictor configuration (time post-stroke and lesion damage)
    outcome:
      text: speech production score
    analysis_label: Predicting longitudinal data
    relation: association
    evidence_ids:
    - P5-S2-C4
    qualifier_ids:
    - P5-S1-C10
    - P5-S2-C1
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: a48c35b7451ad08b6d510255208ab948deb5a6a6d76ad93eea27445b207a4a31
      source_review: _compare/relationships-2026-11-16/review-current/Hope2013
      source_status_sha256: 2dad0ec35b3ff43b44735b94ddc98425c92c525778a7d5426c760e069dcacd88
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Unresolved source passage P1-S2-C12
      - Accounting without a linked unit P2-S1-C7
      - Result passage disposed without unit P2-S2-C7
      - Unaccounted source passage P2-S1-C7
      - Result passage disposed without unit P4-S2-C6
      - Result passage disposed without unit P5-S2-C16
      - Result passage disposed without unit P5-S3-C2
      - Result passage disposed without unit P6-S1-C3
      - Result passage disposed without unit P6-S1-C4
      - Result passage disposed without unit P6-S2-C2
      - Accounting without a linked unit P6-S2-C7
      - Unaccounted source passage P6-S2-C7
      - Result passage disposed without unit P8-S2-C5
      - Result passage disposed without unit P8-S3-C3
      - Result passage disposed without unit P8-S3-C10
      - Result passage disposed without unit P9-S1-C4
      - Accounting without a linked unit P9-S1-C9
      - Unaccounted source passage P9-S1-C9
      - Result passage disposed without unit P9-S2-C3
      unattached_null_or_qualifier_ids:
      - P8-S3-C3
      - P9-S1-C4
      suppressed_nonrepresented_units: 19
      default_disposition_count_requires_completeness_check: 197
      unselected_timing_passages:
      - P2-S1-C7
      - P2-S2-C4
      - P2-S2-C6
      - P2-S3-C3
      - P4-S1-C7
      - P8-S1-C11
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P5-S2-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P3-S4-C10
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P3-S4-C11
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: tested_personal_effects
        source_id: P4-S1-C11
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: limitations
        source_ids:
        - P8-S1-C11
        - P8-S1-C12
        - P8-S2-C2
        - P8-S2-C5
        - P8-S2-C8
        - P8-S2-C9
        - P8-S3-C6
        - P8-S3-C7
        - P8-S3-C10
        - P8-S3-C11
        - P9-S1-C4
        - P9-S1-C5
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - limitations
      - explicitly_not_adjusted
      unclassified_extraction_ids:
      - P8-S1-C12
      table_review_required:
      - TABLE-1-page-6-1
      - TABLE-2-page-6-2
      - TABLE-3-page-6-3
      unlinked_tables:
      - TABLE-2-page-6-2
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P3-S2
        - P4-S1
        - P4-S3
        - P5-S1
        - P5-S2
        - P6-S3
        - P7-S2
        - P7-S3
        - P8-S1
        - P8-S2
        - P8-S3
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: a48c35b7451ad08b6d510255208ab948deb5a6a6d76ad93eea27445b207a4a31
      source_review: _compare/relationships-2026-11-16/review-current/Hope2013
      source_status_sha256: 2dad0ec35b3ff43b44735b94ddc98425c92c525778a7d5426c760e069dcacd88
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Abstract statement of general validation results.
    - source_id: P1-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Abstract statement of general capability.
    - source_id: P2-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive of patient self-assessment.
    - source_id: P4-S2-C2
      disposition: represented
      result_indexes:
      - 0
      reason: Reports non-significant R2 for demographics-only model.
    - source_id: P4-S2-C6
      disposition: represented
      result_indexes:
      - 1
      reason: Reports improved R2 and reduced error for lesion volume model.
    - source_id: P4-S2-C9
      disposition: represented
      result_indexes:
      - 2
      reason: Reports increased R2 and reduced error for lateralised volume model.
    - source_id: P4-S3-C6
      disposition: represented
      result_indexes:
      - 3
      reason: Reports R2 for atlas-based coding model.
    - source_id: P4-S3-C6
      disposition: represented
      result_indexes:
      - 3
      reason: Reports R2 for atlas-based coding model.
    - source_id: P5-S1-C5
      disposition: represented
      result_indexes:
      - 4
      reason: Reports R2 for best ARD feature subset.
    - source_id: P5-S1-C6
      disposition: represented
      result_indexes:
      - 4
      reason: Reports significant reduction in prediction error for best ARD subset.
    - source_id: P5-S1-C8
      disposition: represented
      result_indexes:
      - 8
      reason: States composite measure performance is better than individual tests.
    - source_id: P5-S1-C9
      disposition: represented
      result_indexes:
      - 8
      reason: States best feature subset for composite score has less error than components.
    - source_id: P5-S1-C10
      disposition: represented
      result_indexes:
      - 5
      reason: Defines preferred predictor configuration.
    - source_id: P5-S2-C4
      disposition: represented
      result_indexes:
      - 5
      reason: Reports R2 for longitudinal predictions.
    - source_id: P5-S2-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive of longitudinal validation process.
    - source_id: P5-S2-C16
      disposition: background_or_descriptive
      result_indexes: []
      reason: General observation about subset size and performance.
    - source_id: P6-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: General summary of results in discussion.
    - source_id: P6-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: General observation about recovery over time.
    - source_id: P6-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: General discussion on outcome variable sensitivity.
    - source_id: P6-S2-C7
      disposition: represented
      result_indexes:
      - 6
      - 7
      reason: Reports AUC for cross-sectional and longitudinal configurations.
    - source_id: P6-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: General comparison to past work.
    - source_id: P7-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison of error standard deviations with Tilling et al.
    - source_id: P7-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison to Stonnington et al.
    - source_id: P7-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison of R2 values to Stonnington et al.
    - source_id: P7-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Restatement of preferred predictor configuration.
    - source_id: P7-S3-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive example of a specific patient prognosis.
    - source_id: P7-S3-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive example of a specific patient prognosis.
    - source_id: P8-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation about predictive power and number of predictors.
    - source_id: P8-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive of right-hemisphere sample skew.
    - source_id: P8-S2-C4
      disposition: represented
      result_indexes: []
      reason: 'Null finding: no evidence that restricting dataset to acute/chronic
        phase improves predictions.'
    - source_id: P8-S2-C5
      disposition: represented
      result_indexes: []
      reason: Finding that preferred configuration underestimates severity for most
        impaired patients.
    - source_id: P8-S3-C3
      disposition: represented
      result_indexes: []
      reason: Finding that preferred configuration makes coarse distinctions for right-hemisphere
        damage.
    - source_id: P8-S3-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of over-fitting mitigation.
    - source_id: P8-S5-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of DTI consistency.
    - source_id: P9-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion on the difficulty of interpreting region predictors.
    - source_id: P9-S1-C9
      disposition: repeated
      result_indexes:
      - 8
      reason: Restatement that composite score was more predictable than components.
    - source_id: P9-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion summary.
    unresolved_coverage:
    - source_id: P4-S3-C6
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P8-S2-C4
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P8-S2-C5
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P8-S3-C3
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P5-S3-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S3-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C7
    - P1-S1-C9
    - P2-S2-C7
    - P5-S1-C6
    - P5-S1-C10
    - P5-S2-C11
    - P5-S2-C16
    - P5-S3-C2
    - P6-S1-C3
    - P6-S1-C4
    - P6-S2-C2
    - P6-S2-C9
    - P7-S1-C6
    - P7-S1-C8
    - P7-S2-C3
    - P7-S2-C7
    - P7-S3-C9
    - P7-S3-C10
    - P8-S1-C5
    - P8-S1-C9
    - P8-S2-C4
    - P8-S2-C5
    - P8-S3-C3
    - P8-S3-C8
    - P8-S3-C10
    - P8-S5-C2
    - P9-S1-C4
    - P9-S1-C9
    - P9-S2-C3
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-6-1
    - TABLE-2-page-6-2
    - TABLE-3-page-6-3
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P2-S3-C3
      recruited_sample:
      - P2-S1-C7
      eligibility:
      - P2-S2-C4
      - P2-S2-C5
      - P2-S2-C6
      imaging_provenance:
      - P2-S1-C7
      - P3-S2-C5
      - P4-S3-C3
      imaging_timing:
      - P3-S1-C5
      outcome_timing:
      - P5-S2-C2
      - P6-S1-C2
      - P7-S3-C6
      outcome_definition:
      - P2-S3-C10
      - P2-S4-C2
      - P3-S1-C3
      validation:
      - P3-S4-C3
      - P5-S2-C3
      analysis_restrictions:
      - P2-S2-C8
      dependent_variable_statement:
      - P4-S1-C5
      limitations: []
      personal_factors:
      - P2-S1-C7
      - P4-S1-C7
      - P4-S1-C8
      - P4-S1-C11
      tested_personal_effects:
      - P4-S2-C6
      - P4-S2-C9
      adjustment_roles:
      - P4-S1-C11
      - P4-S2-C6
      - P4-S2-C9
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P4-S1-C7
      - P4-S1-C8
    outcome_type: both_reported
    imaging_vs_outcome: concurrent
    validation_type: internal_cross_validation
    held_selections:
    - slot: dependent_variable_statement
      source_id: P5-S2-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P3-S4-C10
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P3-S4-C11
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: tested_personal_effects
      source_id: P4-S1-C11
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: limitations
      source_ids:
      - P8-S1-C11
      - P8-S1-C12
      - P8-S2-C2
      - P8-S2-C5
      - P8-S2-C8
      - P8-S2-C9
      - P8-S3-C6
      - P8-S3-C7
      - P8-S3-C10
      - P8-S3-C11
      - P9-S1-C4
      - P9-S1-C5
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
      pdf_sha256: a48c35b7451ad08b6d510255208ab948deb5a6a6d76ad93eea27445b207a4a31
      review_sha256: 1a02cea8e83bdb908a2496b7f14ecf8ab679535b2204ce474d97fa2a487a2997
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
      source_result: The study reports that a Gaussian Process Regression model, using
        a preferred predictor configuration of time post-stroke and lesion damage
        (specifically volume and encroachment into 35 regions), was able to predict
        later speech production assessment scores for 38 patients with high accuracy
        (R2 = 0.84, p < 0.001). This is a performance result demonstrating the predictive
        utility of the model in a longitudinal configuration.
      result_status: performance_only
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis (R006) correctly identifies the longitudinal
            prediction task described in P5-S2-C4, where the model trained on cross-sectional
            data predicts future scores for patients with repeat assessments. The
            exposure (time + lesion) and outcome (speech production) match the source.
          source_ids:
          - P5-S2-C4
          - P5-S2-C2
          - P5-S2-C3
        direction:
          answer: fits
          reason: The source explicitly states the model predicts scores 'very accurately'
            with a high R2 value. The proposed draft's direction 'likely' (implying
            a positive predictive association) is consistent with the reported performance.
            It does not claim a causal direction, but a predictive one, which aligns
            with the GPR framework.
          source_ids:
          - P5-S2-C4
          - P5-S1-C5
        construct:
          answer: fits
          reason: The exposure is correctly identified as the combination of time
            post-stroke and lesion damage (P5-S1-C10). The outcome is the speech production
            score (P1-S2-C8). The patient measurement is correctly classified as template_lesion_overlap,
            as the lesion data is derived by overlaying patient lesions on atlas-based
            regions of interest (P4-S3-C2, P4-S3-C3), not by patient-specific diffusion
            tractography.
          source_ids:
          - P5-S1-C10
          - P4-S3-C2
          - P4-S3-C3
          - P1-S2-C8
        qualifications:
          answer: fits
          reason: The draft includes the key qualification that the longitudinal validation
            was performed on a subset of 38 patients (P5-S2-C2). It also notes the
            preferred configuration includes time as the most significant predictor
            (P5-S1-C5). The limitations regarding underestimation of severe impairment
            and potential overfitting are also captured.
          source_ids:
          - P5-S2-C2
          - P5-S1-C5
          - P8-S2-C5
          - P8-S3-C6
        missing_material_caveat:
          answer: fits
          reason: The draft captures the material caveats regarding the model's systematic
            underestimation of severe impairment (P8-S2-C5) and the potential for
            overfitting due to feature selection (P8-S3-C6). The unresolved OCR warning
            in P5-S2-C4 is noted in the source but does not change the core meaning
            of the high accuracy claim (R2=0.84 is clear in text). No material caveat
            is omitted that would change the interpretation of the predictive performance.
          source_ids:
          - P8-S2-C5
          - P8-S3-C6
          - P5-S2-C4
      optional_pending:
      - 'not_transcribed: Specific R2 and p-values for the longitudinal prediction
        are present in source P5-S2-C4 but not required for the qualitative draft'
      - 'not_transcribed: Detailed list of the 35 brain regions in Table 1'
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - 'not_transcribed: R2 and p-values for longitudinal prediction'
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - 'not_transcribed: Specific R2 and p-values for the longitudinal prediction are
      present in source P5-S2-C4 but not required for the qualitative draft'
    - 'not_transcribed: Detailed list of the 35 brain regions in Table 1'
    normalizations: []
    analysis_identity:
      id: R006
      exposure:
        text: preferred predictor configuration (time post-stroke and lesion damage)
      outcome:
        text: speech production score
      analysis_label: Predicting longitudinal data
      relation: association
      evidence_ids:
      - P5-S2-C4
      qualifier_ids:
      - P5-S1-C10
      - P5-S2-C1
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: a48c35b7451ad08b6d510255208ab948deb5a6a6d76ad93eea27445b207a4a31
        source_review: _compare/relationships-2026-11-16/review-current/Hope2013
        source_status_sha256: 2dad0ec35b3ff43b44735b94ddc98425c92c525778a7d5426c760e069dcacd88
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P5-S2-C4:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: a48c35b7451ad08b6d510255208ab948deb5a6a6d76ad93eea27445b207a4a31
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: d36ad9be4e955318379be47534376f1cec9e7d8dd69ad19195f949f7dd5dcdd7
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P5-S2-C4
          page: 5
          text_layer_sha256: d36ad9be4e955318379be47534376f1cec9e7d8dd69ad19195f949f7dd5dcdd7
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: 'After learning from just

          the patient data used for the cross-sectional conﬁguration, our learner

          can predict the later assessment scores very accurately (R2 = 0.84,

          F = 225.00, p b 0.001; see Fig. 5).

          3.8.'
        anchor_text: 'After learning from just

          the patient data used for the cross-sectional conﬁguration, our learner

          can predict the later assessment scores very accurately (R2 = 0.84,

          F = 225.00, p b 0.001; see Fig. 5).

          3.8.'
        excluded_fragments: []
        image_sha256: e4fae66c6730d9b4b2f894c226fb308d67c9614d21a3b1e4f3f78e09d16c000b
      P5-S1-C5:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: a48c35b7451ad08b6d510255208ab948deb5a6a6d76ad93eea27445b207a4a31
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 55ef0c514c312aa69d30e61cda5a12dbcb22fb07c1ed354f3ae8fde7b590514f
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P5-S1-C5
          page: 5
          text_layer_sha256: 55ef0c514c312aa69d30e61cda5a12dbcb22fb07c1ed354f3ae8fde7b590514f
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'The best subset included

          37 relevant predictors (R2 = 0.59, F = 38.38, p b 0.001), including

          time post-stroke (the most signiﬁcant, single predictor), lesion

          volume, and encroachment into 35 regions of the brain (listed in

          Table 1).'
        anchor_text: 'The best subset included

          37 relevant predictors (R2 = 0.59, F = 38.38, p b 0.001), including

          time post-stroke (the most signiﬁcant, single predictor), lesion

          volume, and encroachment into 35 regions of the brain (listed in

          Table 1).'
        excluded_fragments: []
        image_sha256: d10cd1e06a9cd612dc3cf1909f416fa757efb294bd83b0ed623f7a749f572a55
        transcription: '. The best subset included

          37 relevant predictors (R² = 0.59, F = 38.38, p < 0.001), including

          time post-stroke (the most significant, single predictor), lesion

          volume, and encroachment into 35 regions of the brain (listed in

          Table 1)'
      P2-S2-C4:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: a48c35b7451ad08b6d510255208ab948deb5a6a6d76ad93eea27445b207a4a31
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 63dc3311d5338d3410ef7fa4390855534d10eda56a8d22011a6304b8c12f0e89
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S2-C4
          page: 2
          text_layer_sha256: 63dc3311d5338d3410ef7fa4390855534d10eda56a8d22011a6304b8c12f0e89
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'We only excluded patients if they:

          a) were very young (b20 years) or very old (>90 years)

          b) were less than 1 month post-stroke at assessment

          c) had evidence of other signiﬁcant neurological conditions (e.g. de-

          mentia, multiple sclerosis)

          d) did not speak English as a ﬁrst language

          e) showed no visible damage anywhere in the brain, as assessed by a

          neurologist (APL), using the patients'' raw T1-weighted scans

          f) had suffered dispersed rather than focal damage.'
        anchor_text: 'We only excluded patients if they:

          a) were very young (b20 years) or very old (>90 years)

          b) were less than 1 month post-stroke at assessment

          c) had evidence of other signiﬁcant neurological conditions (e.g. de-

          mentia, multiple sclerosis)

          d) did not speak English as a ﬁrst language

          e) showed no visible damage anywhere in the brain, as assessed by a

          neurologist (APL), using the patients'' raw T1-weighted scans

          f) had suffered dispersed rather than focal damage.'
        excluded_fragments: []
        image_sha256: 7d2ac667822bf9d3282a6b7f127937c76ef6b5914f7c2e4ec2dea1d1c280e6fd
        transcription: '. We only excluded patients if they:


          a) were very young (<20 years) or very old (>90 years)

          b) were less than 1 month post-stroke at assessment

          c) had evidence of other significant neurological conditions (e.g. dementia,
          multiple sclerosis)

          d) did not speak English as a first language

          e) showed no visible damage anywhere in the brain, as assessed by a neurologist
          (APL), using the patients'' raw T1-weighted scans

          f) had suffered dispersed rather than focal damage'
      P2-S3-C3:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: a48c35b7451ad08b6d510255208ab948deb5a6a6d76ad93eea27445b207a4a31
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 44c35ee2b4d20251f8d8d9eece6d14fee6f3869800c7b22e3ea1c44bbd32963b
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S3-C3
          page: 2
          text_layer_sha256: 44c35ee2b4d20251f8d8d9eece6d14fee6f3869800c7b22e3ea1c44bbd32963b
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'This selection process left us with

          data from 270 patients, but with repeated assessments for some patients

          at different times post-stroke, our dataset included a total of 315 speech

          production scores.

          2.3.'
        anchor_text: 'This selection process left us with

          data from 270 patients, but with repeated assessments for some patients

          at different times post-stroke, our dataset included a total of 315 speech

          production scores.

          2.3.'
        excluded_fragments: []
        image_sha256: e71e7f2e7dd3ffd71c813aa523b328994bbee401f6ba1b18eb715978d4fcb43c
        transcription: '. This selection process left us with

          data from 270 patients, but with repeated assessments for some patients

          at different times post-stroke, our dataset included a total of 315 speech

          production scores.


          2.3.'
      P8-S1-C11:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: a48c35b7451ad08b6d510255208ab948deb5a6a6d76ad93eea27445b207a4a31
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: a41e12af448e63614ab5bdc0c8b4cdb936320056ab6a1f21978818a62962f1cc
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P8-S1-C11
          page: 8
          text_layer_sha256: a41e12af448e63614ab5bdc0c8b4cdb936320056ab6a1f21978818a62962f1cc
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Limitations of the current study

          One criticism of the system described here is that it pools scans taken

          both soon after stroke (within the ﬁrst month), and many years later

          (30 years or more).'
        anchor_text: 'Limitations of the current study

          One criticism of the system described here is that it pools scans taken

          both soon after stroke (within the ﬁrst month), and many years later

          (30 years or more).'
        excluded_fragments: []
        image_sha256: 255d1745676be0d3c6b3dbc578f4e2278484257401a0351652d32ae76eba2584
        transcription: 'Limitations of the current study


          One criticism of the system described here is that it pools scans taken
          both soon after stroke (within the first month), and many years later (30
          years or more)'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 5
  quote: 'After learning from just

    the patient data used for the cross-sectional conﬁguration, our learner

    can predict the later assessment scores very accurately (R2 = 0.84,

    F = 225.00, p b 0.001; see Fig. 5).

    3.8.'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-24'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
