---
id: psci_strategic_regions
name: PSCI strategic regions cluster
kind: network
findings:
- id: f1
  target: psci
  target_kind: impairment
  claim: Infarcts in the left frontotemporal lobes, right parietal lobe, and left
    thalamus were significantly associated with post-stroke cognitive impairment.
  direction: likely
  relationship: correlational
  method: VLSM
  sample:
    n: 2950
    population: patients with acute ischemic stroke
    phase: not_reported
    time_post_onset: Imaging mostly performed in the first two weeks post-stroke;
      cognitive assessment generally performed 2-6 months post-stroke (median 105
      days).
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Patients with severe dysphasia were generally excluded from the original cohorts,
    potentially underrepresenting language-related brain regions
  - Generalizability to non-Caucasian and non-Asian ethnicities is undetermined
  - Pre-stroke cognitive status was unavailable for a substantial number of cohorts
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Patient lesion overlap with voxels in the left frontotemporal
    lobes, right parietal lobe, and left thalamus, as identified by voxel-based lesion-symptom
    mapping. Association remained significant after correction for multiple testing
    (FDR q<0.01); Over 80% of patients with infarcts in these regions had PSCI; Results
    were comparable in sensitivity analyses limited to patients with cognitive assessment
    >=2 weeks post-stroke and those with multidomain neuropsychological assessment.
    Additional metadata has not been transcribed; review the pending-field flags before
    approval. PDF image reading (P6-S1-C4, two-model agreement, human verification
    pending): . A pilot study showed successful harmonization of clinical and imaging

    data from six cohorts (N=878), achieving 46% brain coverage, indicating that two
    to three thousand patients

    would be required for complete coverage.12

    In this Meta-VCI-Map consortium study, we performed a large-scale multicenter
    lesion-symptom mapping

    study in 2950 patients with acute ischemic stroke from 12 cohorts, aiming to identify
    infarct locations most

    strongly predictive of PSCI and create a comprehensive brain map of strategic
    infarct locations Original text-layer quotation is preserved below. PDF image
    reading (P9-S2-C5, two-model agreement, human verification pending): . Cognitive
    assessment was generally performed 2-6 months post-stroke (median 105 days, IQR
    74-170) Original text-layer quotation is preserved below. PDF image reading (P10-S1-C2,
    two-model agreement, human verification pending): . Imaging was mostly performed
    in the first two weeks post-stroke (median 4 days, IQR 1-9) Original text-layer
    quotation is preserved below.'
  imaging_details:
    reference_space: not_reported
    atlases_used: []
  lesion_mapping: {}
  provenance:
    extracted_by: model:gemma4:31b
    extracted_on: '2026-11-26'
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
    - proposed_concept:psci
  citation: '@Weaver2021'
  source_passages:
  - section: Original source P10-S1-C12
    page: 10
    quote: "Particularly,infarcts in the left \nfrontotemporal lobes, right parietal\
      \ lobe, and left thalamus were significantly associated with PSCI after \ncorrection\
      \ for multiple testing (FDR q<0·01), with high voxel-wise ORs (>20)."
    supports: claim
  - section: Original source P10-S1-C13
    page: 10
    quote: "Over 80% of patients with \ninfarcts in these regions had PSCI (appendix,\
      \ p.8)."
    supports: claim
  - section: Original source P6-S1-C4
    page: 6
    quote: "A pilot study showed successful harmonization of clinical and imaging\
      \ \ndata from six cohorts (N=878), achieving 46% brain coverage, indicating\
      \ that two to three thousand patients \nwould be required for complete coverage.12\
      \  \nIn this Meta-VCI-Map consortium study, we performed a large-scale multicenter\
      \ lesion-symptom mapping \nstudy in 2950 patients with acute ischemic stroke\
      \ from 12 cohorts, aiming to identify infarct locations most \nstrongly predictive\
      \ of PSCI and create a comprehensive brain map of strategic infarct locations."
    supports: sample
  - section: Original source P8-S1-C5
    page: 8
    quote: "Voxel-based lesion-symptom mapping \nVoxel-based lesion-symptom mapping\
      \ (VLSM) was performed to relate infarct location to PSCI \noccurrence."
    supports: method
  - section: Original source P9-S2-C5
    page: 9
    quote: "Cognitive \nassessment was generally performed 2-6 months post-stroke\
      \ (median 105 days, IQR 74-170)."
    supports: claim
  - section: Original source P10-S1-C2
    page: 10
    quote: "Imaging was mostly \nperformed in the first two weeks post-stroke (median\
      \ 4 days, IQR 1-9)."
    supports: claim
  - section: Original source P10-S1-C15
    page: 10
    quote: "Sensitivity analyses limited to patients with cognitive assessment ≥2\
      \ weeks post-stroke \n(N=2554) and patients with multidomain neuropsychological\
      \ assessment (N=2343) showed comparable \nresults (appendix, p.9)."
    supports: claim
  - section: Original source P14-S1-C7
    page: 14
    quote: "For \nexample, to be eligible for cognitive testing, (severe) dysphasia\
      \ was generally an exclusion criterion."
    supports: limitation
  - section: Original source P14-S1-C12
    page: 14
    quote: "Finally, our \npooled sample only includes Caucasian and Asian patients,\
      \ thus generalizability to other ethnicities remains \nundetermined."
    supports: limitation
  - section: Original source P14-S1-C11
    page: 14
    quote: "Therefore variation in timing of assessment \nmight influence our results.5\
      \ Third, information on pre-stroke cognitive status was not available for a\
      \ \nsubstantial number of cohorts, therefore we could not take this into account\
      \ in our analyses."
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-26'
relationship_review:
  paper: Weaver2021
  proposal_id: R001
  review_status_sha256: 62079c9b6fe3bd141afe4142389bd01d52c52cd5ffe615aba9a910914ef86123
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 6f87e4b48eb6114330f6e209da5c17f72fd7dc5ad859f256944904caf77028c3
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 6f87e4b48eb6114330f6e209da5c17f72fd7dc5ad859f256944904caf77028c3
        A/passages.json: 8942f47ab5d1628f9c6f5ce6da8c9df5cc4df3cf2317ea39f19745d7f95565de
        A/raw.json: 4d99265d8d36be14b896d632ba2afffc73bf5e44da4b6d7a7aa98ee018fdaaae
        A/source-units.json: 60434444c0c2b5a75067241465769a9841f9f83fd75034bde3a53064e9275139
        A/full-source-units.json: df22044e0ccfd10a56c060003a8a0313f5db001cb365e319aedb31df44f3821d
        A/meta.json: fb9647ba060ffaa56d4ec65bd0bfe33f6f1b9001dcc474182b6212436bedcd9e
        A/table-images/TABLE-1-page-21-1.png: 4bd71b37ebdb32844a1cb42f711ced13af8e0f4f9d7b387d4a5f40cf28ec8c7c
        A/table-images/TABLE-2-page-22-1.png: 5c351ccc01d2acb3f171c431c4050778f49f076b070012283df4d03a31f29abc
        A/table-images/manifest.json: fd3b2c9868b8c7c6d9e727729e44c791e0e5856a6bf7ff45f2dbad228560a1c6
        A/table-images/page-21.png: 4a3228449039f1450677b16ef5b0044b16f8d3feded6eb7ebb3dfb546c74dc81
        A/table-images/page-22.png: 7ead7c06c64cf03953b9db03e3ed9c5615d804b56f78a11beb4bfe2cbce18a13
        A/clauses/window-03/raw.json: ba639a641b76c5321697cd88508d478225808d675b4dfa62ac0c45bd85d4d092
        A/clauses/window-03/prompt.txt: 2d03244a919a86ad1ab0f8d4833f9a433e8c5e685134d0570b2d7fdf55821f7d
        A/clauses/window-03/meta.json: 2ae875d72b610741e66db66cf45267c273325f3823a521a0c4504f6de3048901
        A/clauses/window-04/raw.json: f50d1bd0d258aa1a3c93d3ec8d2fe7096ed59ebf272403f1cd11de4f82de9832
        A/clauses/window-04/prompt.txt: 10e9c79adb63482467601c49089bd9ba05490853928117b3ba652f3b8bd77ffb
        A/clauses/window-04/meta.json: 5531408fd827778e92b75a60653f519ada271c9ef21396c16e938f6e822e98c6
        A/clauses/window-05/raw.json: 503466c532ef11fce342d7d29e8c41ffd6bea9e59b04b39fc2e64a4a6daf3371
        A/clauses/window-05/prompt.txt: 5301048d618a20963c839c6b1589e8590e73f7a6d6c8b10d464ffc8192cd4c60
        A/clauses/window-05/meta.json: 4e7b3f241936307e7777cdc5bd55c9e42d27d5e2efb7b44e78272989257e6281
        A/clauses/window-02/raw.json: e65142072e039827d85bc745b84b7b70c88c673c7c2907ee811b737962d12f4c
        A/clauses/window-02/prompt.txt: 317ab878e99314aab14ae680272369886fbc8864aafca7fa749bdaef668a90e3
        A/clauses/window-02/meta.json: 7f0a84c615c4526f747847f7882c2a09984aba3c4a1b5459d174e600fb63dc26
        A/clauses/window-09/raw.json: 9e5b663c85e940feed20fa71462ade749ecdf43df000eae7ac40aab16e57309a
        A/clauses/window-09/prompt.txt: 740e0d35db3c8ef067167b5bee95eb4771dcda97200a874d0dd55f81423c3217
        A/clauses/window-09/meta.json: c0eb7c2cde29a9bb358b3718ccc3c03026ec7122c56c062808f7a8d7ab7640fb
        A/clauses/window-07/raw.json: 964ea9c4be61b8f21f6b4b6cedfbc828051bd4ad0cc9eedf65133e2901d0b3ac
        A/clauses/window-07/prompt.txt: ad357bb681a16fa931c537e4fb982a8457a670ac34d49891221f54e10e90ae82
        A/clauses/window-07/meta.json: a0b5f700e45c2658a59212f7be2acd63a2214f093268f78019b7f418fb4392f3
        A/clauses/window-01/raw.json: 54fd78b36e3c29fadc4755ad7bf65431d0430ea15d7aa144f7882cca1b6ff606
        A/clauses/window-01/prompt.txt: 11cce4c2caa4ad822e24c93a4a9a2e9b5fc47ebbd32d311936fce2e8ad3f9487
        A/clauses/window-01/meta.json: 2b85a1a8a6ed16f145483b6084ca62da7469c250b9fc0ebd1e366911717abe30
        A/clauses/window-06/raw.json: 53b91eaf104822c3712158aaa3f3fd0c43ac97db46d108c76be55a8ad06aef37
        A/clauses/window-06/prompt.txt: 475ef24ce90e4f872282d472cb51ee0590f16feedcdc15c23bb79d312d04cdf1
        A/clauses/window-06/meta.json: 3523d460cb7fb63bd30a0facaad6e1164d9da9a0f17338a0e87c3dbfc7077cdf
        A/clauses/window-08/raw.json: fa6aa0746964152c979e72c59f0c252659c046588af73886272717228efe9e6c
        A/clauses/window-08/prompt.txt: fd36a61bb337606e9fd9f02be45decf82a588c8c6de845ead9568ad4e84b3f9e
        A/clauses/window-08/meta.json: 4b987650d172b8d4738368833442585f7fd983c1ea95a4f716c9d9ff3191ff9a
        A/tables/TABLE-1-page-21-1/raw.json: 8f656ce6214ac6d21bab77d539c68581d93f68422ddc8b86da1cfb28f331d211
        A/tables/TABLE-1-page-21-1/prompt.txt: 095d75d71aceaaefa621de0aa8fc2863c3ba7f04a424395d259e58d5a0bbc411
        A/tables/TABLE-1-page-21-1/meta.json: 11aa9e47db47ae03dedeb4cce2016de2f7c8cb01fc8bb529b1d0db9d3b79754e
        A/tables/TABLE-2-page-22-2/raw.json: cbd67dc5dc483658d886a44a4cf40a59144b388e47cdf4393ab66124eadd3e84
        A/tables/TABLE-2-page-22-2/prompt.txt: ca07260c1fd2ff87f69a7d83d362e1bc28ea0d79cb3670a02772cc624816e337
        A/tables/TABLE-2-page-22-2/meta.json: e4d9949f20aa9d3f2fece5fd26666cbc508dc4bd1735c90d82860afc5486adf5
        B/passages.json: 8942f47ab5d1628f9c6f5ce6da8c9df5cc4df3cf2317ea39f19745d7f95565de
        B/raw.json: 23619fec3b0fef4cc1a40510a5228ff39557de0edfcf93ee4298f28595d0fa36
        B/source-units.json: 60434444c0c2b5a75067241465769a9841f9f83fd75034bde3a53064e9275139
        B/full-source-units.json: df22044e0ccfd10a56c060003a8a0313f5db001cb365e319aedb31df44f3821d
        B/meta.json: 97c4ae988f1c9ab936c14fb455ffdcd515973feca4b450ac6b80d815f01a7b52
        B/table-images/TABLE-1-page-21-1.png: 4bd71b37ebdb32844a1cb42f711ced13af8e0f4f9d7b387d4a5f40cf28ec8c7c
        B/table-images/TABLE-2-page-22-1.png: 5c351ccc01d2acb3f171c431c4050778f49f076b070012283df4d03a31f29abc
        B/table-images/manifest.json: 63434129a22ee919f8ca2416551bbefdc371489951f541fd18c0eb8adc715829
        B/table-images/page-21.png: 4a3228449039f1450677b16ef5b0044b16f8d3feded6eb7ebb3dfb546c74dc81
        B/table-images/page-22.png: 7ead7c06c64cf03953b9db03e3ed9c5615d804b56f78a11beb4bfe2cbce18a13
        B/clauses/window-03/raw.json: c61514cb1606d399575cbe783414a7fc97b60d8cb7895657b21e66d7daeff2cf
        B/clauses/window-03/prompt.txt: 2d03244a919a86ad1ab0f8d4833f9a433e8c5e685134d0570b2d7fdf55821f7d
        B/clauses/window-03/meta.json: b035f14d643398fc4e500a4293b4c00e9338b410af2838518eaad8895fe55c8a
        B/clauses/window-04/raw.json: 4748b8336d19eb0c07376ac419fae67f9f31cfa0e716cf56225a1498083afc03
        B/clauses/window-04/prompt.txt: 10e9c79adb63482467601c49089bd9ba05490853928117b3ba652f3b8bd77ffb
        B/clauses/window-04/meta.json: e88a0c7598c40126580480fe53a58e9a00450f50ff12d8d6ff397d894521d038
        B/clauses/window-05/raw.json: f3e6073650f15c2f54195326c500ed93e57019454b75e72064113b83b75ff0d0
        B/clauses/window-05/prompt.txt: 5301048d618a20963c839c6b1589e8590e73f7a6d6c8b10d464ffc8192cd4c60
        B/clauses/window-05/meta.json: 34f0663d7e05ef1ab9e74aeff4ce1e9bed18e41e7d580ccf8d85dee388a09da0
        B/clauses/window-02/raw.json: 3fd04713cb7b641180c8746a07b821bfdd416405c03fd2dfde43bffb1f816893
        B/clauses/window-02/prompt.txt: 317ab878e99314aab14ae680272369886fbc8864aafca7fa749bdaef668a90e3
        B/clauses/window-02/meta.json: cbd9f2d883e7c6415d7bf1dcf72a25bb4e64e60d34afda8e9bad1b69aae4e62d
        B/clauses/window-09/raw.json: 9e5b663c85e940feed20fa71462ade749ecdf43df000eae7ac40aab16e57309a
        B/clauses/window-09/prompt.txt: 740e0d35db3c8ef067167b5bee95eb4771dcda97200a874d0dd55f81423c3217
        B/clauses/window-09/meta.json: 34e28ab8ad4a2e142d8768679d9aa491da62e79f926399257d76992f16d85506
        B/clauses/window-07/raw.json: f4946dd70aff2777af3ad8905e4d4b8610b119a0f1810b364d690068fa0c9859
        B/clauses/window-07/prompt.txt: ad357bb681a16fa931c537e4fb982a8457a670ac34d49891221f54e10e90ae82
        B/clauses/window-07/meta.json: a787e29b545ea951e09bfecc3468ce2f7e0d02a06c50ffea481364f3d187750b
        B/clauses/window-01/raw.json: 0cd46936277e61e11c263deccd1840ac05f5c9ed1cd06db1ceecc27e879aaea6
        B/clauses/window-01/prompt.txt: 11cce4c2caa4ad822e24c93a4a9a2e9b5fc47ebbd32d311936fce2e8ad3f9487
        B/clauses/window-01/meta.json: e35523eb70d37b36beca1bb7153a015c34e7b6180533ac7ae9083ac7bd67623e
        B/clauses/window-06/raw.json: 4a5d347b2f31638b18cd25869d9ecff2b5d17075f81222ebed803add5b07b36e
        B/clauses/window-06/prompt.txt: 475ef24ce90e4f872282d472cb51ee0590f16feedcdc15c23bb79d312d04cdf1
        B/clauses/window-06/meta.json: c9be23ed1d66d135375c04d2831832fc31c0c454c4a59ea982508d955c16fe3f
        B/clauses/window-08/raw.json: 17337f1f20ebb94a0d861b47ea917d3452d5360b99abbe010781b68c5aafc128
        B/clauses/window-08/prompt.txt: fd36a61bb337606e9fd9f02be45decf82a588c8c6de845ead9568ad4e84b3f9e
        B/clauses/window-08/meta.json: f132e0e498bd35fa6cfa2e3aa9fd921bfb8011d7db4b033d10890fb2eb570cef
        B/tables/TABLE-1-page-21-1/raw.json: ea3a0faa521c24e1b13949f078910685624814ec2db6a3e39a074dac8ba37573
        B/tables/TABLE-1-page-21-1/prompt.txt: 095d75d71aceaaefa621de0aa8fc2863c3ba7f04a424395d259e58d5a0bbc411
        B/tables/TABLE-1-page-21-1/meta.json: 028375c5e64cafdcca6cea22b43658686b6e23658d6fc55bab9a1e71ac0e772d
        B/tables/TABLE-2-page-22-2/raw.json: d4734018ce395a27c26c80f7f88474dad78d6a33afa3d82de7260087ac4f8205
        B/tables/TABLE-2-page-22-2/prompt.txt: ca07260c1fd2ff87f69a7d83d362e1bc28ea0d79cb3670a02772cc624816e337
        B/tables/TABLE-2-page-22-2/meta.json: 32c55c862cf4c6534d1c82a61d0e32dd674706634bd1ca5ded7f79ca32b68066
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
      pdf_sha256: 6f87e4b48eb6114330f6e209da5c17f72fd7dc5ad859f256944904caf77028c3
      source_review: _compare/relationships-2026-11-16/review-current/Weaver2021
      source_status_sha256: d24a6dda221caa7500999b18f3f8cb188e5d61a588cf5e0149f1d25bc5a812b5
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R001
    exposure:
      text: infarcts in the left frontotemporal lobes, right parietal lobe, and left
        thalamus
    outcome:
      text: post-stroke cognitive impairment (PSCI)
    analysis_label: Voxel-based lesion-symptom mapping (VLSM)
    relation: association
    evidence_ids:
    - P10-S1-C12
    qualifier_ids:
    - P10-S1-C12
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 6f87e4b48eb6114330f6e209da5c17f72fd7dc5ad859f256944904caf77028c3
      source_review: _compare/relationships-2026-11-16/review-current/Weaver2021
      source_status_sha256: d24a6dda221caa7500999b18f3f8cb188e5d61a588cf5e0149f1d25bc5a812b5
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P4-S1-C10
      - Result passage disposed without unit P4-S1-C11
      - Accounting without a linked unit P4-S1-C12
      - Accounting without a linked unit P4-S1-C14
      - Result passage disposed without unit P5-S1-C11
      - Result passage disposed without unit P5-S1-C9
      - Unaccounted source passage P4-S1-C12
      - Unaccounted source passage P4-S1-C14
      - Result passage disposed without unit P5-S1-C12
      - Result passage disposed without unit P5-S2-C3
      - Result passage disposed without unit P5-S2-C4
      - Result passage disposed without unit P9-S1-C12
      - Result passage disposed without unit P10-S1-C10
      - Accounting without a linked unit P10-S1-C14
      - Accounting without a linked unit P10-S1-C15
      - Accounting without a linked unit P10-S2-C3
      - Accounting without a linked unit P10-S2-C4
      - Accounting without a linked unit P10-S2-C5
      - Unresolved source passage P10-S2-C7
      - Accounting without a linked unit P11-S1-C1
      - Unaccounted source passage P10-S2-C3
      - Unaccounted source passage P10-S1-C14
      - Unaccounted source passage P11-S1-C1
      - Unaccounted source passage P10-S2-C4
      - Unaccounted source passage P10-S2-C5
      - Unaccounted source passage P10-S1-C15
      - Result passage disposed without unit P12-S1-C9
      - Accounting without a linked unit P12-S2-C5
      - Accounting without a linked unit P12-S2-C6
      - Accounting without a linked unit P13-S1-C2
      - Accounting without a linked unit P13-S1-C5
      - Unaccounted source passage P13-S1-C2
      - Unaccounted source passage P12-S2-C5
      - Unaccounted source passage P13-S1-C5
      - Unaccounted source passage P12-S2-C6
      - Result passage disposed without unit P13-S1-C10
      - Accounting without a linked unit P13-S2-C4
      - Accounting without a linked unit P13-S2-C6
      - Accounting without a linked unit P14-S1-C3
      - Accounting without a linked unit P14-S1-C4
      - Unaccounted source passage P13-S2-C4
      - Unaccounted source passage P14-S1-C4
      - Unaccounted source passage P14-S1-C3
      - Unaccounted source passage P13-S2-C6
      - Result passage disposed without unit P14-S1-C9
      unattached_null_or_qualifier_ids:
      - P4-S1-C14
      - P10-S1-C1
      - P13-S1-C2
      - P13-S1-C5
      - P13-S2-C4
      - P14-S1-C9
      suppressed_nonrepresented_units: 5
      default_disposition_count_requires_completeness_check: 216
      unselected_timing_passages:
      - P6-S1-C4
      - P9-S1-C13
      - P13-S2-C9
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P10-S1-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S1-C12
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: tested_personal_effects
        source_id: P8-S2-C2
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: limitations
        source_ids:
        - P13-S1-C4
        - P13-S1-C7
        - P14-S1-C4
        - P14-S1-C6
        - P14-S1-C7
        - P14-S1-C8
        - P14-S1-C10
        - P14-S1-C11
        - P14-S1-C12
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - limitations
      - tested_personal_effects
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-21-1
      - TABLE-2-page-22-2
      unlinked_tables:
      - TABLE-1-page-21-1
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P9-S1
        - P9-S2
        - P10-S1
        - P10-S2
        - P11-S1
        - P12-S2
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 6f87e4b48eb6114330f6e209da5c17f72fd7dc5ad859f256944904caf77028c3
      source_review: _compare/relationships-2026-11-16/review-current/Weaver2021
      source_status_sha256: d24a6dda221caa7500999b18f3f8cb188e5d61a588cf5e0149f1d25bc5a812b5
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P4-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes sample demographics and PSCI prevalence.
    - source_id: P4-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes brain lesion coverage percentage.
    - source_id: P4-S1-C12
      disposition: repeated
      result_indexes:
      - 0
      reason: Abstract restatement of VLSM results.
    - source_id: P4-S1-C14
      disposition: repeated
      result_indexes:
      - 8
      reason: Abstract restatement of location impact score correspondence.
    - source_id: P5-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes study value regarding brain coverage.
    - source_id: P5-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about domain-specific patterns.
    - source_id: P5-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about generalizability.
    - source_id: P5-S2-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Fragment of a sentence about cognitive domains.
    - source_id: P5-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about the basis of the prediction score.
    - source_id: P5-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion about predictive locations.
    - source_id: P9-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes heterogeneity of clinical characteristics.
    - source_id: P10-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes imaging modalities used.
    - source_id: P10-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes PSCI occurrence rates.
    - source_id: P10-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes PSCI occurrence in specific cohorts.
    - source_id: P10-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes frequency of cognitive domain affection.
    - source_id: P10-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes brain lesion coverage.
    - source_id: P10-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes excluded brain regions.
    - source_id: P10-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes cohort-specific infarct patterns.
    - source_id: P10-S1-C12
      disposition: represented
      result_indexes:
      - 0
      reason: Primary source for VLSM associations.
    - source_id: P10-S1-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes percentage of patients with PSCI in strategic regions.
    - source_id: P10-S1-C14
      disposition: represented
      result_indexes:
      - 1
      reason: Primary source for low-risk infarct locations.
    - source_id: P10-S1-C15
      disposition: represented
      result_indexes:
      - 12
      reason: Primary source for sensitivity analysis results.
    - source_id: P10-S2-C1
      disposition: represented
      result_indexes:
      - 12
      reason: Qualifies the sensitivity analysis sample size.
    - source_id: P10-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about cortical/large subcortical infarcts.
    - source_id: P10-S2-C4
      disposition: represented
      result_indexes:
      - 3
      reason: Primary source for small subcortical infarct associations.
    - source_id: P10-S2-C5
      disposition: represented
      result_indexes:
      - 4
      reason: Primary source for infratentorial infarct null result.
    - source_id: P10-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the decision to perform domain-specific analyses.
    - source_id: P11-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about domain-specific patterns.
    - source_id: P11-S1-C2
      disposition: represented
      result_indexes:
      - 6
      reason: Primary source for processing speed association.
    - source_id: P11-S1-C3
      disposition: represented
      result_indexes:
      - 5
      - 6
      reason: Primary source for language, memory, and visuospatial associations.
    - source_id: P11-S1-C4
      disposition: represented
      result_indexes:
      - 7
      - 8
      reason: Primary source for univariate and multivariate associations of the score.
    - source_id: P11-S1-C5
      disposition: represented
      result_indexes:
      - 9
      reason: Primary source for cross-validation performance.
    - source_id: P11-S1-C6
      disposition: represented
      result_indexes:
      - 9
      reason: Provides c-statistics for cross-validation.
    - source_id: P11-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes trends in smaller cohorts.
    - source_id: P11-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes poor performance in one specific cohort.
    - source_id: P11-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes cohorts excluded from validation.
    - source_id: P11-S1-C10
      disposition: represented
      result_indexes:
      - 10
      reason: Primary source for clinical predictor model performance.
    - source_id: P11-S1-C11
      disposition: represented
      result_indexes:
      - 10
      reason: Primary source for added value of location impact score.
    - source_id: P11-S1-C12
      disposition: represented
      result_indexes:
      - 11
      reason: Primary source for univariate model selection.
    - source_id: P11-S2-C1
      disposition: repeated
      result_indexes:
      - 10
      reason: Restatement of best correspondence.
    - source_id: P11-S2-C2
      disposition: represented
      result_indexes:
      - 11
      reason: Primary source for univariate model performance similarity.
    - source_id: P11-S2-C2
      disposition: represented
      result_indexes:
      - 11
      reason: Primary source for univariate model performance similarity.
    - source_id: P11-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes visual rating agreement (Kappa).
    - source_id: P11-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes inter/intra-rater agreement.
    - source_id: P11-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes time taken for visual rating.
    - source_id: P12-S1-C2
      disposition: repeated
      result_indexes:
      - 0
      reason: Discussion restatement of VLSM results.
    - source_id: P12-S2-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes brain coverage.
    - source_id: P12-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes previous study outcomes.
    - source_id: P12-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about strategic locations representing domains.
    - source_id: P13-S1-C2
      disposition: represented
      result_indexes:
      - 3
      reason: Discussion detail on left thalamus across subtypes.
    - source_id: P13-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes PSCI occurrence in low-risk groups.
    - source_id: P14-S1-C3
      disposition: repeated
      result_indexes:
      - 9
      reason: Discussion restatement of robust prediction.
    - source_id: P14-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes factors influencing model fit.
    - source_id: P14-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discusses impact of excluding dysphasia.
    - source_id: P14-S1-C14
      disposition: repeated
      result_indexes:
      - 9
      reason: Summary restatement of robust prediction.
    unresolved_coverage:
    - source_id: P10-S2-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P10-S2-C6
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P11-S1-C12
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P11-S2-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P11-S2-C2
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P12-S2-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P12-S2-C2
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P12-S1-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S1-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S2-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S1-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S1-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S2-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S2-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P4-S1-C10
    - P4-S1-C11
    - P4-S1-C12
    - P4-S1-C14
    - P5-S1-C9
    - P5-S1-C11
    - P5-S1-C12
    - P5-S2-C1
    - P5-S2-C3
    - P5-S2-C4
    - P9-S1-C12
    - P10-S1-C1
    - P10-S1-C4
    - P10-S1-C5
    - P10-S1-C6
    - P10-S1-C7
    - P10-S1-C8
    - P10-S1-C10
    - P10-S1-C13
    - P10-S2-C3
    - P11-S1-C1
    - P11-S1-C7
    - P11-S1-C8
    - P11-S1-C9
    - P11-S2-C4
    - P11-S2-C5
    - P11-S2-C6
    - P12-S1-C2
    - P12-S1-C3
    - P12-S1-C9
    - P12-S2-C5
    - P12-S2-C6
    - P13-S1-C2
    - P13-S1-C5
    - P13-S1-C10
    - P13-S2-C4
    - P13-S2-C6
    - P13-S2-C8
    - P14-S1-C3
    - P14-S1-C4
    - P14-S1-C9
    - P14-S1-C14
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-21-1
    - TABLE-2-page-22-2
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P4-S1-C10
      - P5-S1-C9
      - P6-S1-C4
      - P9-S1-C11
      - P10-S1-C4
      recruited_sample:
      - P4-S1-C4
      - P6-S1-C4
      - P9-S1-C11
      eligibility:
      - P4-S1-C5
      - P6-S2-C3
      - P7-S1-C2
      - P7-S1-C14
      imaging_provenance:
      - P7-S1-C12
      - P7-S1-C13
      - P7-S2-C3
      - P10-S1-C1
      imaging_timing:
      - P10-S1-C2
      outcome_timing:
      - P4-S1-C5
      - P6-S1-C1
      - P6-S2-C3
      - P8-S1-C11
      - P9-S2-C5
      - P10-S1-C2
      - P14-S1-C10
      outcome_definition:
      - P4-S1-C6
      - P6-S2-C3
      - P7-S1-C5
      - P7-S1-C11
      - P12-S2-C3
      validation:
      - P4-S1-C9
      - P5-S1-C12
      - P8-S2-C3
      - P11-S1-C5
      - P11-S1-C10
      - P14-S1-C3
      analysis_restrictions:
      - P8-S1-C6
      dependent_variable_statement:
      - P4-S1-C7
      - P8-S1-C5
      - P8-S1-C7
      limitations: []
      personal_factors:
      - P6-S1-C2
      - P8-S2-C2
      - P13-S1-C4
      tested_personal_effects: []
      adjustment_roles:
      - P4-S1-C14
      - P8-S2-C2
      - P11-S1-C5
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P4-S1-C10
      - P9-S1-C13
      - P9-S2-C4
      - P10-S1-C4
    outcome_type: status_at_assessment
    imaging_vs_outcome: precedes_outcome
    validation_type: mixed
    held_selections:
    - slot: dependent_variable_statement
      source_id: P10-S1-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S1-C12
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: tested_personal_effects
      source_id: P8-S2-C2
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: limitations
      source_ids:
      - P13-S1-C4
      - P13-S1-C7
      - P14-S1-C4
      - P14-S1-C6
      - P14-S1-C7
      - P14-S1-C8
      - P14-S1-C10
      - P14-S1-C11
      - P14-S1-C12
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
      pdf_sha256: 6f87e4b48eb6114330f6e209da5c17f72fd7dc5ad859f256944904caf77028c3
      review_sha256: 62079c9b6fe3bd141afe4142389bd01d52c52cd5ffe615aba9a910914ef86123
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
      - P10-S1-C12
      source_result: Infarcts in the left frontotemporal lobes, right parietal lobe,
        and left thalamus were significantly associated with PSCI after correction
        for multiple testing (FDR q<0.01), with high voxel-wise ORs (>20).
      result_status: detected
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis is the primary VLSM analysis on the total
            sample (N=2950) identifying strategic regions for PSCI, as described in
            P10-S1-C12 and P8-S1-C5.
          source_ids:
          - P10-S1-C12
          - P8-S1-C5
          - P6-S1-C4
        direction:
          answer: fits
          reason: The source explicitly states these regions were 'significantly associated'
            with PSCI with high ORs (>20), indicating a positive association (increased
            risk). The draft correctly reflects this detected association.
          source_ids:
          - P10-S1-C12
        construct:
          answer: fits
          reason: The exposure is correctly identified as infarcts in specific regions
            (left frontotemporal, right parietal, left thalamus). The outcome is PSCI.
            The method is VLSM. The patient measurement is correctly identified as
            template_lesion_overlap (lesions registered to MNI-152 template, P7-S2-C3),
            not patient_diffusion.
          source_ids:
          - P10-S1-C12
          - P8-S1-C5
          - P7-S2-C3
        qualifications:
          answer: fits
          reason: The draft includes the FDR correction (q<0.01) and the high ORs
            (>20) as stated in P10-S1-C12. It also includes the sensitivity analysis
            results (P10-S1-C15) and the >80% PSCI occurrence (P10-S1-C13) as qualifications/context.
            These are faithful to the source.
          source_ids:
          - P10-S1-C12
          - P10-S1-C13
          - P10-S1-C15
        missing_material_caveat:
          answer: fits
          reason: 'The draft includes key limitations: exclusion of severe dysphasia
            (P14-S1-C7), ethnicity generalizability (P14-S1-C12), and pre-stroke cognition
            (P14-S1-C11). No material caveat that changes the interpretation of the
            primary association is omitted.'
          source_ids:
          - P14-S1-C7
          - P14-S1-C12
          - P14-S1-C11
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
      id: R001
      exposure:
        text: infarcts in the left frontotemporal lobes, right parietal lobe, and
          left thalamus
      outcome:
        text: post-stroke cognitive impairment (PSCI)
      analysis_label: Voxel-based lesion-symptom mapping (VLSM)
      relation: association
      evidence_ids:
      - P10-S1-C12
      qualifier_ids:
      - P10-S1-C12
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 6f87e4b48eb6114330f6e209da5c17f72fd7dc5ad859f256944904caf77028c3
        source_review: _compare/relationships-2026-11-16/review-current/Weaver2021
        source_status_sha256: d24a6dda221caa7500999b18f3f8cb188e5d61a588cf5e0149f1d25bc5a812b5
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P6-S1-C4:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 6f87e4b48eb6114330f6e209da5c17f72fd7dc5ad859f256944904caf77028c3
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: d1cdfa2143bb07b5b0162df77f7ef27e9cdd66a12cbd490e50ffb788a5f7f0a8
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P6-S1-C4
          page: 6
          text_layer_sha256: d1cdfa2143bb07b5b0162df77f7ef27e9cdd66a12cbd490e50ffb788a5f7f0a8
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "A pilot study showed successful harmonization of clinical\
          \ and imaging \ndata from six cohorts (N=878), achieving 46% brain coverage,\
          \ indicating that two to three thousand patients \nwould be required for\
          \ complete coverage.12  \nIn this Meta-VCI-Map consortium study, we performed\
          \ a large-scale multicenter lesion-symptom mapping \nstudy in 2950 patients\
          \ with acute ischemic stroke from 12 cohorts, aiming to identify infarct\
          \ locations most \nstrongly predictive of PSCI and create a comprehensive\
          \ brain map of strategic infarct locations."
        anchor_text: "A pilot study showed successful harmonization of clinical and\
          \ imaging \ndata from six cohorts (N=878), achieving 46% brain coverage,\
          \ indicating that two to three thousand patients \nwould be required for\
          \ complete coverage.12  \nIn this Meta-VCI-Map consortium study, we performed\
          \ a large-scale multicenter lesion-symptom mapping \nstudy in 2950 patients\
          \ with acute ischemic stroke from 12 cohorts, aiming to identify infarct\
          \ locations most \nstrongly predictive of PSCI and create a comprehensive\
          \ brain map of strategic infarct locations."
        excluded_fragments: []
        image_sha256: 04f0ee97aeb4272178e05efc5271e3e406e49661f43f77d46f7b61bc06007f95
        transcription: '. A pilot study showed successful harmonization of clinical
          and imaging

          data from six cohorts (N=878), achieving 46% brain coverage, indicating
          that two to three thousand patients

          would be required for complete coverage.12

          In this Meta-VCI-Map consortium study, we performed a large-scale multicenter
          lesion-symptom mapping

          study in 2950 patients with acute ischemic stroke from 12 cohorts, aiming
          to identify infarct locations most

          strongly predictive of PSCI and create a comprehensive brain map of strategic
          infarct locations'
      P9-S2-C5:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 6f87e4b48eb6114330f6e209da5c17f72fd7dc5ad859f256944904caf77028c3
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: a84e9c91b745b1c8a675586d25ba071af58ca225dea2507e2a01a96f29837be5
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P9-S2-C5
          page: 9
          text_layer_sha256: a84e9c91b745b1c8a675586d25ba071af58ca225dea2507e2a01a96f29837be5
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "Cognitive \nassessment was generally performed 2-6 months\
          \ post-stroke (median 105 days, IQR 74-170)."
        anchor_text: "Cognitive \nassessment was generally performed 2-6 months post-stroke\
          \ (median 105 days, IQR 74-170)."
        excluded_fragments: []
        image_sha256: df8c6c7eb17051f331f954ef38ca44365cba1e5f6e93d4dfee349a764f02c976
        transcription: . Cognitive assessment was generally performed 2-6 months post-stroke
          (median 105 days, IQR 74-170)
      P10-S1-C2:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 6f87e4b48eb6114330f6e209da5c17f72fd7dc5ad859f256944904caf77028c3
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: dbf3e323d7eb634da673609e6dd1ddb57aa7d727021d5eee5328454b02e5f742
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P10-S1-C2
          page: 10
          text_layer_sha256: dbf3e323d7eb634da673609e6dd1ddb57aa7d727021d5eee5328454b02e5f742
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "Imaging was mostly \nperformed in the first two weeks post-stroke\
          \ (median 4 days, IQR 1-9)."
        anchor_text: "Imaging was mostly \nperformed in the first two weeks post-stroke\
          \ (median 4 days, IQR 1-9)."
        excluded_fragments: []
        image_sha256: 06827c08ed1687a2a20aeb382ae860ece034a4cbef3ffb6649787524c89b7c13
        transcription: . Imaging was mostly performed in the first two weeks post-stroke
          (median 4 days, IQR 1-9)
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 10
  quote: "Particularly,infarcts in the left \nfrontotemporal lobes, right parietal\
    \ lobe, and left thalamus were significantly associated with PSCI after \ncorrection\
    \ for multiple testing (FDR q<0·01), with high voxel-wise ORs (>20)."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-26'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
