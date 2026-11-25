---
id: aalcts_atlas_prediction_model
name: AALCTS atlas prediction model
kind: predictor
findings:
- id: f1
  target: aphasia_type
  target_kind: impairment
  claim: The AALCTS atlas was the most successful for predicting aphasia type, resolving
    7 out of 10 binary contrasts and achieving the highest average performance, although
    differences in classification accuracy between the tested atlases were not significant.
  direction: likely
  relationship: correlational
  method: MVPA
  sample:
    n: 98
    population: right-handed patients with chronic left hemisphere stroke and aphasia
    phase: not_reported
    time_post_onset: at least 6 months post-stroke; imaging obtained within 2 days
      of behavioural assessment
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Unbalanced group sizes for different aphasia types
  - Small sample size for Wernicke's aphasia (n=7)
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: A multivariate classification model (SVM) using the
    proportion of damage to brain areas defined by the AALCTS atlas (a union of AAL
    and CTS atlases), where lesions were manually drawn on T2-weighted MRI and normalized
    using enantiomorphic normalization. The AALCTS atlas was the only one to successfully
    classify Broca''s versus Wernicke''s aphasia; Three contrasts (anomic vs Wernicke''s,
    Broca''s vs global, and conduction vs Wernicke''s) could not be resolved by any
    atlas; Differences in accuracy between atlases were not statistically significant
    (p = 0.355 for Friedman test). Additional metadata has not been transcribed; review
    the pending-field flags before approval. PDF image reading (P6-S1-C12, two-model
    agreement, human verification pending): . All patients were at least 6 months
    post-stroke, and the mean time since stroke onset was 40.1 months (SD= 49.6; range
    = 6–276) Original text-layer quotation is preserved below. PDF image reading (P1-S1-C5,
    two-model agreement, human verification pending): . Our sample consisted of 98
    patients with five types of aphasia (Broca’s, Wernicke’s, global, conduction,
    and anomic), classified based on scores on the Western Aphasia Battery Original
    text-layer quotation is preserved below.'
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
    - proposed_concept:aphasia_type
  citation: '@Yourganov2015Predicting'
  source_passages:
  - section: Original source P11-S1-C3
    page: 11
    quote: 'Overall, the AALCTS atlas was the most successful: it could resolve 7
      out of 10 contrasts.'
    supports: claim
  - section: Original source P11-S1-C5
    page: 11
    quote: "The \naverage performance of AALCTS was the highest, and the average performance\
      \ of the CTS \nwhite-matter atlas was the lowest; however, the differences in\
      \ classification accuracy \nbetween atlases were not significant (Friedman test\
      \ for column effects: p = 0.355; Wilcoxon \nsigned-rank test between CTS and\
      \ AALCTS atlases: p = 0.106)."
    supports: claim
  - section: Original source P11-S1-C6
    page: 11
    quote: "AALCTS was the only \natlas that could successfully classify Broca’s versus\
      \ Wernicke’s aphasia."
    supports: claim
  - section: Original source P11-S1-C7
    page: 11
    quote: "Three contrasts \ncould not be resolved using any atlas: anomic versus\
      \ Wernicke’s, Broca’s versus global, and \nconduction versus Wernicke’s aphasia."
    supports: claim
  - section: Original source P6-S1-C12
    page: 6
    quote: "All patients were at least 6 months post-stroke, and the mean time since\
      \ stroke onset \nwas 40.1 months (SD= 49.6; range = 6–276)."
    supports: sample
  - section: Original source P1-S1-C6
    page: 1
    quote: "Binary lesion maps were obtained from structural MRI scans (obtained at\
      \ least 6 \nmonths poststroke, and within 2 days of behavioural assessment);\
      \ after spatial normalization, the \nlesions were parcellated into a disjoint\
      \ set of brain areas."
    supports: method
  - section: Original source P5-S1-C10
    page: 5
    quote: "In our analysis, we used a brain atlas (e.g., the Brodmann atlas) to define\
      \ \nthe brain areas and to compute the amount of damage to each area; the left-hemisphere\
      \ areas \nare the features for our predictive algorithm."
    supports: method
  - section: Original source P7-S2-C3
    page: 7
    quote: A union of AAL and CTS atlases (AALCTS); 150 areas.
    supports: method
  - section: Original source P8-S1-C5
    page: 8
    quote: "For the remaining areas, we computed the percentage of damage as the ratio\
      \ of lesioned \nvoxels to the total number of voxels in the area.\n2.4 Classification\n\
      Support vector machines (SVMs) were used to predict the aphasia type from brain\
      \ damage."
    supports: method
  - section: Original source P1-S1-C5
    page: 1
    quote: "Our sample consisted of 98 patients with five types of aphasia \n(Broca’s,\
      \ Wernicke’s, global, conduction, and anomic), classified based on scores on\
      \ the Western \nAphasia Battery."
    supports: sample
predictor_type: imaging_metric
short_definition: A multivariate classification model (SVM) using the proportion of
  damage to brain areas defined by the AALCTS atlas (a union of AAL and CTS atlases),
  where lesions were manually drawn on T2-weighted MRI and normalized using enantiomorphic
  normalization.
assessment:
- Western Aphasia Battery
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-26'
relationship_review:
  paper: Yourganov2015Predicting
  proposal_id: R009
  review_status_sha256: 710fb84e0f929b47c9d891ce28b6f33301413a6eeeb1ccc09fed7f9fb0adf832
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 8cea32fbedcdb4af1a30ac7fecebcb769f1951e7eac742197a0fccd30494ee3a
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 8cea32fbedcdb4af1a30ac7fecebcb769f1951e7eac742197a0fccd30494ee3a
        A/passages.json: eda8a4ce4493769df5e53955f6634f88ebac0b2731e2514d8acca2db0dc70a6c
        A/raw.json: fbd83613acb86b637217e0211aaa5195ed9d1fab78329ed7326f7ddb62bf47e4
        A/source-units.json: 0e7faec18ed7218387577b83cf22832caa148ecd0ef217c077fe9653c004baf1
        A/full-source-units.json: 9a691aa0fd339625641dfb4a23f0d1b83253f30f2f50e0b0a5f1bfe93f44ef4d
        A/meta.json: a930a4d266f0bac6bafbd67c6d1312a8456c43a27167ea1c14bf7a4e4373269b
        A/table-images/TABLE-2-page-23-1.png: 249dbf7afd2ce8879f6984b615c745ca0a6bba065e3d92fa55f837ca6abebe54
        A/table-images/TABLE-1-page-22-1.png: edc4658dc6a750cba3a281214183e048b8aae6a5070e694267519e5629180988
        A/table-images/TABLE-3-page-24-1.png: d141b7d29b8ad2d3fbe1b55ec4f7c3545d87da0e049fdc79ad8d2b457d2a17fe
        A/table-images/manifest.json: 31d14e3bdb045e047a65b3597fb996116bae626b54d8e6a8e68bab67147edd89
        A/table-images/page-23.png: 8a6c56b32ffbee5e949ce6831104c42740a35d75f69b423a51131d050331d727
        A/table-images/page-22.png: 91301ae99c30079edc3758aabf1ab57dd7f6721542fcf6e69a90f21eb45865df
        A/table-images/page-24.png: 1bdcad7a1b64f1cf5a670e6ff5b844cbf1eeeb3c2808f73b32640d1b362eae5c
        A/clauses/window-03/raw.json: d832de4c8ca7bd570643835c661725f9c04743914a094a18941edaf7be5ccf86
        A/clauses/window-03/prompt.txt: 6a2ab34db14ea8319304ede7f9ece4d5deb1d1290cab551a25d52b9450e0dd56
        A/clauses/window-03/meta.json: 84aa7bf436316774bd300cdd4a725234e1598aa851e38eca99c5cf4a4358e474
        A/clauses/window-04/raw.json: f3f219ebc54aff8ac0defe3775deaedf617f9d4cb70cd66e5f9e404ffecf9206
        A/clauses/window-04/prompt.txt: 0126ae1a3c872cb776e3a0c347f0908019a06cf7260c0f85869e72717d9837e2
        A/clauses/window-04/meta.json: 62fd0e0760fdbf60c442276084ebe9c69db8e3726398aab8eb1dafbc29bb7725
        A/clauses/window-05/raw.json: 598815ccb139aecaf4cf3545ce7076caa36373f1045328a7d05d8aa4c4b252aa
        A/clauses/window-05/prompt.txt: 80442853c49cdee21f76c011b057469287f3be2fdaa22e025222c692ccea97c3
        A/clauses/window-05/meta.json: dc0779c8f4b3fab4c218ad58f3c63d9aa5a7cfb2437697983a21d0c6313d62a9
        A/clauses/window-02/raw.json: 08e78ffef5f94cb5750dedb3ef90b869464bca981d74d7f3c3ee9219cc25a796
        A/clauses/window-02/prompt.txt: 8292a1a5a01a5eea8e5edbe00b5a41fc31e7605bdf78cc06aa67496a164f43f7
        A/clauses/window-02/meta.json: d5a0cb2ad209f3d828c6c0cb8d1675ea381589d1a07366e764557cfb46527037
        A/clauses/window-09/raw.json: b1f4c0de1268f75a156b0794370886836cbee2e9af8e5dfc369c9c498efd5633
        A/clauses/window-09/prompt.txt: 60eb0d41e74627e85ef1f128476f84d3eba57e4ef93c87940ebe9896335dc90f
        A/clauses/window-09/meta.json: b93de1913d25f707fec3f9eb98c88ecfb0a00d96b9f610e3b25f694133e558ff
        A/clauses/window-07/raw.json: 2a90abd2e436d944ea3a590cb2a1374569b084b4a34143b0abcf2d8c05867f85
        A/clauses/window-07/prompt.txt: 6965ab81b2630047704978c926d9930d8fa8d2b31262ec636d2515e05bd1be8d
        A/clauses/window-07/meta.json: 09c8c9c2b4a5153de423f9e1c7e51b8120a09b0debab06c8b4e42cfcb0eae488
        A/clauses/window-01/raw.json: 63ad56e05b4fd04d7c5f97aea3367f952bdaae31e1d3ee44d3bd08e08f2edb82
        A/clauses/window-01/prompt.txt: 4e9046dfe4c82d44aaa1d510c22d78baef991182332c4977487e9376d11cd87d
        A/clauses/window-01/meta.json: c4d4c66077d8d853c2940ed770d229d6e7f1fab22ddef2a7130e3872e38adaa9
        A/clauses/window-06/raw.json: 1b504932ddbbf97e7705ffd120943cd9ea9db4f12539b1839c42c335e6a9c4e7
        A/clauses/window-06/prompt.txt: 1f9327320a0aca9cf29bb9ca31195cb8b559e48b7c8b5e1c7bf408ebc68eb7ef
        A/clauses/window-06/meta.json: ba084f618109a1dd77811c8c978bf572f37ab9608f537a363b147981a993d0e6
        A/clauses/window-08/raw.json: f981c05cca1de277a8a4ecfb9d7df300c8579976555f85a7408caa077a5f536f
        A/clauses/window-08/prompt.txt: 3d7de8b1de20504a4705b728ec2e97de04d69606c5c27713b9eab59c6a687d7e
        A/clauses/window-08/meta.json: 8e5f5f1e6d4f366bca76e25e1a63eee04fa9ae3fd4b904faad19d95e4dc934b1
        A/tables/TABLE-3-page-24-3/raw.json: 368319a4b56827139a10145412bc40640b616594cbd4f008000a962e7cd46f08
        A/tables/TABLE-3-page-24-3/prompt.txt: 95a5f24e943a31edd45e21486df2d8950534bcac3a26f61f55299d1ed1f9288f
        A/tables/TABLE-3-page-24-3/meta.json: 69990888418e007b7eb72d7ca868320f99f93b804ee12587d29110da3dca6b3f
        A/tables/TABLE-2-page-23-2/raw.json: 4ffbc8aee6aae53c7bdf04a67629d84cfbc7375e3d82fc8db2cbb8d9301e6248
        A/tables/TABLE-2-page-23-2/prompt.txt: d28d03b92c3d7a224d26a42bc7094fa3b326e420220e23eacd5f56e9f064696f
        A/tables/TABLE-2-page-23-2/meta.json: 170802aee2a2927fa011b8e4093ba0c69f7e30396746989916e9ca957716d73f
        A/tables/TABLE-1-page-22-1/raw.json: 9948ec1469b0bd343276a84984c4cc3115dc184ad3c13910e1763b6bd2b8d0d5
        A/tables/TABLE-1-page-22-1/prompt.txt: 16c4dc64a31c34b5af791a0b7b774589e5d250596214a12f622dbd93b43ad627
        A/tables/TABLE-1-page-22-1/meta.json: 915662e2ab8d836fd98b3eb4da5ded24cb73c64b519cb77b6608705f86f7c2ca
        B/passages.json: eda8a4ce4493769df5e53955f6634f88ebac0b2731e2514d8acca2db0dc70a6c
        B/raw.json: aaf9eafe954a9cb5af27609893ef61be4615437e4378f3af51c9e1d04a1ee7a5
        B/source-units.json: 0e7faec18ed7218387577b83cf22832caa148ecd0ef217c077fe9653c004baf1
        B/full-source-units.json: 9a691aa0fd339625641dfb4a23f0d1b83253f30f2f50e0b0a5f1bfe93f44ef4d
        B/meta.json: 601f93bf1e35d35ef483302224c5faa9f3edc4c817b64fb11c08efe78a93ec8f
        B/table-images/TABLE-2-page-23-1.png: 249dbf7afd2ce8879f6984b615c745ca0a6bba065e3d92fa55f837ca6abebe54
        B/table-images/TABLE-1-page-22-1.png: edc4658dc6a750cba3a281214183e048b8aae6a5070e694267519e5629180988
        B/table-images/TABLE-3-page-24-1.png: d141b7d29b8ad2d3fbe1b55ec4f7c3545d87da0e049fdc79ad8d2b457d2a17fe
        B/table-images/manifest.json: 83106e2c9c7477801ea46996d5acc65ee3e8c769013eb95b5fa4be5023058752
        B/table-images/page-23.png: 8a6c56b32ffbee5e949ce6831104c42740a35d75f69b423a51131d050331d727
        B/table-images/page-22.png: 91301ae99c30079edc3758aabf1ab57dd7f6721542fcf6e69a90f21eb45865df
        B/table-images/page-24.png: 1bdcad7a1b64f1cf5a670e6ff5b844cbf1eeeb3c2808f73b32640d1b362eae5c
        B/clauses/window-03/raw.json: a613ce61e17ad614a7290b940026dc35ddd174261df9a1c948e13cf0e5222ef9
        B/clauses/window-03/prompt.txt: 6a2ab34db14ea8319304ede7f9ece4d5deb1d1290cab551a25d52b9450e0dd56
        B/clauses/window-03/meta.json: 1e1ba7c8c83af5f331b1207e54175a4d8a801bfbdde3032cd5f0d7c828214a82
        B/clauses/window-04/raw.json: 9f9d47f34967d758b68a26098f2726746561cdff11a23fd50f5e62b1856e3897
        B/clauses/window-04/prompt.txt: 0126ae1a3c872cb776e3a0c347f0908019a06cf7260c0f85869e72717d9837e2
        B/clauses/window-04/meta.json: 8b166580bf87c7eb876c38de64749f27fa96e9c8250a0de82e9613054f39e58d
        B/clauses/window-05/raw.json: 450ada14e66144016e5bb6f5675af1794c075fb6c4c2f9db17995217630ff728
        B/clauses/window-05/prompt.txt: 80442853c49cdee21f76c011b057469287f3be2fdaa22e025222c692ccea97c3
        B/clauses/window-05/meta.json: a9530ddf70313e505a969ff5f4b897c51a484392a84f67d886caa2e6970e82f9
        B/clauses/window-02/raw.json: 01f79e46a168fbf43ba5fcae1d8af027acad84c728ea6054f46685895bbea6a7
        B/clauses/window-02/prompt.txt: 8292a1a5a01a5eea8e5edbe00b5a41fc31e7605bdf78cc06aa67496a164f43f7
        B/clauses/window-02/meta.json: 45c3e8aefb733b59fa0c8a6e6befb3f01175d8d7c13067df0e2455d5ac7814b4
        B/clauses/window-09/raw.json: d90351cb45b18031cab37da90929da38f18159e082507ef6745de0ac979483a4
        B/clauses/window-09/prompt.txt: 60eb0d41e74627e85ef1f128476f84d3eba57e4ef93c87940ebe9896335dc90f
        B/clauses/window-09/meta.json: 7f08a34142a0c4f12c5b6556ac3d37747b8c8597c2bec58d39f7b69571564d96
        B/clauses/window-07/raw.json: cf20c1e1740dc4d600d3453892749b896a0f028f0e6d96c2ac59d3ab4716ab86
        B/clauses/window-07/prompt.txt: 6965ab81b2630047704978c926d9930d8fa8d2b31262ec636d2515e05bd1be8d
        B/clauses/window-07/meta.json: 545512922c597d3c30a1432f3746d26d5d3d2de4b6964943491ae2d98b37289a
        B/clauses/window-01/raw.json: 4b023babbbc6470f60bc63b9aed3b99657580edd38a18eb0c8ad35541d55b88f
        B/clauses/window-01/prompt.txt: 4e9046dfe4c82d44aaa1d510c22d78baef991182332c4977487e9376d11cd87d
        B/clauses/window-01/meta.json: 07aa3098d2fa6303113a18f17021a6888ef9dc886966727e3cc21098d8ee4335
        B/clauses/window-06/raw.json: 898adcb18d180d3179553e4313cb2d1b033849edbeb548963cd2312ae055b480
        B/clauses/window-06/prompt.txt: 1f9327320a0aca9cf29bb9ca31195cb8b559e48b7c8b5e1c7bf408ebc68eb7ef
        B/clauses/window-06/meta.json: 36d3f41f7909656be849f1982d4b967f37d23cf4350d88381f0ce3bb855f42fe
        B/clauses/window-08/raw.json: 4e801645a76b17650cf600edd8d8a9614f4f12b5ddbec377d3d61876524c186b
        B/clauses/window-08/prompt.txt: 3d7de8b1de20504a4705b728ec2e97de04d69606c5c27713b9eab59c6a687d7e
        B/clauses/window-08/meta.json: 4bbe55c470d0434f1e10325ec269dfd15913bd6bf0a849019e6f16bdcf4bff70
        B/tables/TABLE-3-page-24-3/raw.json: 05174d49f1aea6d2be2355723372113683aa3402f7a08201e7e19f0e4f87339f
        B/tables/TABLE-3-page-24-3/prompt.txt: 95a5f24e943a31edd45e21486df2d8950534bcac3a26f61f55299d1ed1f9288f
        B/tables/TABLE-3-page-24-3/meta.json: f93f2f357add80b9ee6a98d2be2fcc07340bb53bd51aa89e2deefe509f902372
        B/tables/TABLE-2-page-23-2/raw.json: e5e39f6de3a24124923ad736b077e82f764e2d04f0182d6379fd22faf503ebba
        B/tables/TABLE-2-page-23-2/prompt.txt: d28d03b92c3d7a224d26a42bc7094fa3b326e420220e23eacd5f56e9f064696f
        B/tables/TABLE-2-page-23-2/meta.json: 82975eec533529914696f92fe90272b610c2bbda9202a3891cd3aed6fd9f9f6b
        B/tables/TABLE-1-page-22-1/raw.json: 9948ec1469b0bd343276a84984c4cc3115dc184ad3c13910e1763b6bd2b8d0d5
        B/tables/TABLE-1-page-22-1/prompt.txt: 16c4dc64a31c34b5af791a0b7b774589e5d250596214a12f622dbd93b43ad627
        B/tables/TABLE-1-page-22-1/meta.json: a6e18ae8ef4fa9a20f11f09526debf3476f150be23fb59b85b134ce30ea6d3da
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
      pdf_sha256: 8cea32fbedcdb4af1a30ac7fecebcb769f1951e7eac742197a0fccd30494ee3a
      source_review: _compare/relationships-2026-11-16/review-current/Yourganov2015Predicting
      source_status_sha256: 75b08f1ea060399c2e32c4e2367cea59d57eebad5ca437ab202fdee7e89d6f06
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R009
    exposure:
      text: brain atlas type
    outcome:
      text: classification accuracy
    analysis_label: Atlas performance comparison
    relation: model_comparison
    evidence_ids:
    - P11-S1-C5
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
      pdf_sha256: 8cea32fbedcdb4af1a30ac7fecebcb769f1951e7eac742197a0fccd30494ee3a
      source_review: _compare/relationships-2026-11-16/review-current/Yourganov2015Predicting
      source_status_sha256: 75b08f1ea060399c2e32c4e2367cea59d57eebad5ca437ab202fdee7e89d6f06
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P1-S1-C8
      - Result passage disposed without unit P10-S2-C2
      - Result passage disposed without unit P10-S2-C10
      - Result passage disposed without unit P11-S1-C1
      - Result passage disposed without unit P11-S1-C2
      - Result passage disposed without unit P11-S1-C3
      - Result passage disposed without unit P11-S1-C4
      - Result passage disposed without unit P11-S1-C5
      - Result passage disposed without unit P11-S1-C6
      - Result passage disposed without unit P11-S1-C7
      - Result passage disposed without unit P11-S2-C5
      - Result passage disposed without unit P11-S2-C6
      - Result passage disposed without unit P11-S2-C7
      - Result passage disposed without unit P12-S1-C1
      - Result passage disposed without unit P12-S1-C2
      - Result passage disposed without unit P12-S1-C3
      - Result passage disposed without unit P12-S1-C4
      - Result passage disposed without unit P12-S1-C5
      - Result passage disposed without unit P12-S1-C10
      - Result passage disposed without unit P12-S1-C11
      - Result passage disposed without unit P12-S1-C12
      - Result passage disposed without unit P12-S1-C13
      - Result passage disposed without unit P12-S1-C7
      - Result passage disposed without unit P12-S1-C8
      - Result passage disposed without unit P12-S1-C9
      - Result passage disposed without unit P12-S2-C3
      - Accounting without a linked unit P12-S2-C6
      - Accounting without a linked unit P12-S2-C8
      - Result passage disposed without unit P13-S1-C1
      - Accounting without a linked unit P13-S1-C2
      - Unaccounted source passage P13-S1-C2
      - Unaccounted source passage P12-S2-C8
      - Unaccounted source passage P12-S2-C6
      - Result passage disposed without unit P13-S1-C11
      - Result passage disposed without unit P13-S2-C8
      - Result passage disposed without unit P14-S1-C5
      unattached_null_or_qualifier_ids:
      - P10-S2-C10
      - P11-S1-C5
      - P11-S1-C6
      - P12-S1-C12
      suppressed_nonrepresented_units: 24
      default_disposition_count_requires_completeness_check: 201
      unselected_timing_passages:
      - P5-S2-C5
      - P6-S1-C2
      - P6-S1-C11
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P10-S2-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P5-S2-C4
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      empty_frame_slots_require_confirmation:
      - personal_factors
      - tested_personal_effects
      - adjustment_roles
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-22-1
      - TABLE-2-page-23-2
      - TABLE-3-page-24-3
      unlinked_tables:
      - TABLE-1-page-22-1
      - TABLE-2-page-23-2
      - TABLE-3-page-24-3
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P7-S1
        - P11-S1
        - P11-S2
        - P12-S1
        - P12-S2
        - P13-S1
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 8cea32fbedcdb4af1a30ac7fecebcb769f1951e7eac742197a0fccd30494ee3a
      source_review: _compare/relationships-2026-11-16/review-current/Yourganov2015Predicting
      source_status_sha256: 75b08f1ea060399c2e32c4e2367cea59d57eebad5ca437ab202fdee7e89d6f06
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C8
      disposition: represented
      result_indexes:
      - 0
      reason: States classifier could differentiate aphasia using any of five parcellations.
    - source_id: P1-S1-C9
      disposition: represented
      result_indexes:
      - 0
      reason: Identifies novel parcellation as providing best accuracy.
    - source_id: P1-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about consistency with prior reports.
    - source_id: P1-S1-C11
      disposition: represented
      result_indexes:
      - 0
      reason: Overall result that automated classification can distinguish aphasia
        types.
    - source_id: P5-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion about correspondence between damage and deficit.
    - source_id: P10-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Points to tables for accuracy results.
    - source_id: P10-S2-C4
      disposition: represented
      result_indexes:
      - 1
      reason: Defines Table 1 as ratio of correctly predicted patients for pairings.
    - source_id: P10-S2-C5
      disposition: represented
      result_indexes:
      - 1
      reason: Defines Table 2 as per-class prediction accuracy.
    - source_id: P10-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Explains why some high accuracies are not significant.
    - source_id: P11-S1-C1
      disposition: represented
      result_indexes:
      - 1
      reason: Null finding for anomic vs Wernicke's aphasia.
    - source_id: P11-S1-C2
      disposition: represented
      result_indexes:
      - 1
      reason: Specific accuracy for anomic vs Wernicke's (81.28%) and its relation
        to chance.
    - source_id: P11-S1-C3
      disposition: represented
      result_indexes:
      - 0
      reason: AALCTS atlas resolved 7/10 contrasts.
    - source_id: P11-S1-C4
      disposition: represented
      result_indexes:
      - 0
      reason: JHU atlas resolved 5 contrasts, others 6.
    - source_id: P11-S1-C5
      disposition: represented
      result_indexes:
      - 8
      reason: Comparison of average performance across atlases (not significant).
    - source_id: P11-S1-C6
      disposition: represented
      result_indexes:
      - 1
      reason: AALCTS only atlas to classify Broca's vs Wernicke's.
    - source_id: P11-S1-C7
      disposition: represented
      result_indexes:
      - 1
      reason: Lists three contrasts that could not be resolved by any atlas.
    - source_id: P11-S2-C5
      disposition: represented
      result_indexes:
      - 4
      reason: No brain areas strongly predictive of anomic aphasia.
    - source_id: P11-S2-C6
      disposition: represented
      result_indexes:
      - 4
      reason: No spatial pattern specific for anomic aphasia.
    - source_id: P11-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement that other types have stronger associations.
    - source_id: P12-S1-C1
      disposition: represented
      result_indexes:
      - 3
      reason: Broca's associated with pars opercularis (BA 44).
    - source_id: P12-S1-C2
      disposition: represented
      result_indexes:
      - 3
      reason: Broca's associated with rolandic operculum.
    - source_id: P12-S1-C3
      disposition: represented
      result_indexes:
      - 3
      reason: Broca's associated with arcuate fasciculus (long/anterior segments).
    - source_id: P12-S1-C4
      disposition: represented
      result_indexes:
      - 4
      reason: Conduction associated with posterior arcuate fasciculus, Heschl's gyrus,
        and optical tracts.
    - source_id: P12-S1-C5
      disposition: represented
      result_indexes:
      - 5
      reason: Global aphasia associated with extensive cortical damage.
    - source_id: P12-S1-C6
      disposition: represented
      result_indexes:
      - 5
      reason: Lists specific areas with high predictive relevance for global aphasia.
    - source_id: P12-S1-C7
      disposition: represented
      result_indexes:
      - 5
      reason: Lists white-matter tracts predictive of global aphasia.
    - source_id: P12-S1-C8
      disposition: represented
      result_indexes:
      - 6
      reason: Wernicke's predicted from angular, Heschl's, superior temporal gyri,
        temporal pole, and putamen.
    - source_id: P12-S1-C9
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of overall ability to distinguish aphasia types.
    - source_id: P12-S1-C10
      disposition: represented
      result_indexes:
      - 2
      reason: Fluent vs non-fluent types distinguished using AALCTS.
    - source_id: P12-S1-C11
      disposition: represented
      result_indexes:
      - 2
      reason: Accuracy for fluent vs non-fluent pairings was 87% or higher.
    - source_id: P12-S1-C12
      disposition: represented
      result_indexes:
      - 1
      reason: Only conduction vs anomic resolved among fluent pairings.
    - source_id: P12-S2-C1
      disposition: represented
      result_indexes:
      - 1
      reason: Global vs Broca's accuracy was at chance level.
    - source_id: P12-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of similarity between Broca's and global aphasia areas.
    - source_id: P12-S2-C6
      disposition: represented
      result_indexes:
      - 3
      reason: Broca's predicted from pars opercularis, white-matter tracts, and globus
        pallidus.
    - source_id: P12-S2-C8
      disposition: represented
      result_indexes:
      - 3
      reason: Supramarginal and Heschl's gyri predict Broca's aphasia.
    - source_id: P13-S1-C1
      disposition: represented
      result_indexes:
      - 6
      reason: Wernicke's associated with classical Wernicke's area and neighborhood.
    - source_id: P13-S1-C2
      disposition: represented
      result_indexes:
      - 6
      reason: Wernicke's associated with temporal poles and putamen.
    - source_id: P13-S1-C4
      disposition: represented
      result_indexes:
      - 4
      reason: Conduction associated with Heschl's gyrus, posterior arcuate fasciculus,
        and optic radiations.
    - source_id: P13-S1-C6
      disposition: represented
      result_indexes:
      - 5
      reason: Global associated with areas predictive for Broca's, Wernicke's, and
        insular regions.
    - source_id: P13-S1-C7
      disposition: represented
      result_indexes:
      - 4
      reason: 'Anomic aphasia: no brain areas strongly predictive.'
    - source_id: P13-S1-C8
      disposition: represented
      result_indexes:
      - 0
      reason: AALCTS achieved numerically best prediction accuracy.
    - source_id: P13-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about WAB providing consistent criteria.
    - source_id: P14-S1-C5
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of overall result.
    - source_id: P14-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion supporting historical accounts.
    unresolved_coverage:
    - source_id: P12-S2-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P12-S1-C13
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S2-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S1-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S1-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C10
    - P1-S1-C11
    - P5-S2-C10
    - P10-S2-C2
    - P10-S2-C4
    - P10-S2-C5
    - P10-S2-C10
    - P11-S1-C2
    - P11-S1-C6
    - P11-S2-C7
    - P12-S1-C9
    - P12-S1-C13
    - P12-S2-C3
    - P12-S2-C5
    - P13-S1-C9
    - P13-S1-C11
    - P13-S2-C8
    - P14-S1-C5
    - P14-S1-C6
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-22-1
    - TABLE-2-page-23-2
    - TABLE-3-page-24-3
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P6-S1-C8
      recruited_sample:
      - P6-S1-C2
      eligibility:
      - P6-S1-C6
      - P6-S1-C7
      imaging_provenance:
      - P6-S2-C2
      imaging_timing:
      - P6-S1-C12
      - P6-S2-C2
      outcome_timing:
      - P1-S1-C6
      outcome_definition:
      - P1-S1-C5
      - P6-S1-C9
      validation:
      - P8-S2-C3
      - P8-S2-C4
      - P8-S2-C9
      - P9-S1-C4
      - P9-S1-C6
      analysis_restrictions:
      - P8-S1-C3
      - P8-S1-C4
      dependent_variable_statement:
      - P1-S1-C7
      - P8-S1-C6
      limitations:
      - P5-S2-C2
      - P12-S2-C10
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles: []
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P6-S1-C11
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: internal_cross_validation
    held_selections:
    - slot: dependent_variable_statement
      source_id: P10-S2-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P5-S2-C4
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
      pdf_sha256: 8cea32fbedcdb4af1a30ac7fecebcb769f1951e7eac742197a0fccd30494ee3a
      review_sha256: 710fb84e0f929b47c9d891ce28b6f33301413a6eeeb1ccc09fed7f9fb0adf832
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
      - P11-S1-C5
      source_result: The AALCTS atlas achieved the highest average classification
        accuracy and resolved the most contrasts (7/10), but the differences in performance
        between the tested atlases were not statistically significant (Friedman test
        p=0.355).
      result_status: model_comparison
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The source explicitly compares the performance of different brain
            atlases (AALCTS, JHU, CTS, etc.) in predicting aphasia types. The proposed
            core correctly identifies this as a model comparison where the 'exposure'
            is the atlas type and the 'outcome' is classification accuracy.
          source_ids:
          - P11-S1-C5
          - P10-S2-C8
        direction:
          answer: fits
          reason: 'The source states AALCTS had the highest average performance but
            that differences were not significant. The draft correctly captures this
            nuance: it identifies AALCTS as the ''most successful'' (ranking) while
            explicitly noting the lack of statistical significance, avoiding a false
            claim of a significant superiority.'
          source_ids:
          - P11-S1-C5
        construct:
          answer: fits
          reason: The exposure is correctly identified as the brain atlas type. The
            outcome is classification accuracy. The patient measurement is correctly
            identified as template_lesion_overlap (proportion of damage to atlas-defined
            areas), not patient_diffusion or functional imaging. The method is SVM
            (MVPA).
          source_ids:
          - P5-S1-C10
          - P8-S1-C5
          - P7-S2-C3
        qualifications:
          answer: fits
          reason: The draft includes the critical qualification that the difference
            between atlases was not statistically significant (p=0.355). It also correctly
            notes the specific success of AALCTS in resolving Broca's vs Wernicke's
            and the failure of all atlases in three specific contrasts. These qualifiers
            are present and accurate.
          source_ids:
          - P11-S1-C5
          - P11-S1-C6
          - P11-S1-C7
        missing_material_caveat:
          answer: fits
          reason: The draft includes the necessary caveats regarding the non-significance
            of the atlas comparison and the specific unresolved contrasts. It also
            mentions the unbalanced group sizes and small sample size for Wernicke's
            aphasia, which are material limitations affecting the interpretation of
            the classification results.
          source_ids:
          - P11-S1-C5
          - P11-S1-C7
          - P12-S2-C9
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
      id: R009
      exposure:
        text: brain atlas type
      outcome:
        text: classification accuracy
      analysis_label: Atlas performance comparison
      relation: model_comparison
      evidence_ids:
      - P11-S1-C5
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
        pdf_sha256: 8cea32fbedcdb4af1a30ac7fecebcb769f1951e7eac742197a0fccd30494ee3a
        source_review: _compare/relationships-2026-11-16/review-current/Yourganov2015Predicting
        source_status_sha256: 75b08f1ea060399c2e32c4e2367cea59d57eebad5ca437ab202fdee7e89d6f06
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P6-S1-C12:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 8cea32fbedcdb4af1a30ac7fecebcb769f1951e7eac742197a0fccd30494ee3a
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: ca45967d1e7550ca9672dd7c90782a13d8c904759727c90b31608b9a97d4e411
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P6-S1-C12
          page: 6
          text_layer_sha256: ca45967d1e7550ca9672dd7c90782a13d8c904759727c90b31608b9a97d4e411
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "All patients were at least 6 months post-stroke, and the mean\
          \ time since stroke onset \nwas 40.1 months (SD= 49.6; range = 6–276)."
        anchor_text: "All patients were at least 6 months post-stroke, and the mean\
          \ time since stroke onset \nwas 40.1 months (SD= 49.6; range = 6–276)."
        excluded_fragments: []
        image_sha256: 9094456b87d82079ee979e5a1d10828a22c10b2302ba9f539e03cd6cd67525c9
        transcription: . All patients were at least 6 months post-stroke, and the
          mean time since stroke onset was 40.1 months (SD= 49.6; range = 6–276)
      P1-S1-C5:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 8cea32fbedcdb4af1a30ac7fecebcb769f1951e7eac742197a0fccd30494ee3a
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: c851dbb8211f03107dd4f6f21c792dfbab10c8cbe960cdcfa5bbd376b6662b8f
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P1-S1-C5
          page: 1
          text_layer_sha256: c851dbb8211f03107dd4f6f21c792dfbab10c8cbe960cdcfa5bbd376b6662b8f
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "Our sample consisted of 98 patients with five types of aphasia\
          \ \n(Broca’s, Wernicke’s, global, conduction, and anomic), classified based\
          \ on scores on the Western \nAphasia Battery."
        anchor_text: "Our sample consisted of 98 patients with five types of aphasia\
          \ \n(Broca’s, Wernicke’s, global, conduction, and anomic), classified based\
          \ on scores on the Western \nAphasia Battery."
        excluded_fragments: []
        image_sha256: be4f9b92e386f10e8d289104837762914d4df7ecf7b52d107c1ffe6cb95a1dde
        transcription: . Our sample consisted of 98 patients with five types of aphasia
          (Broca’s, Wernicke’s, global, conduction, and anomic), classified based
          on scores on the Western Aphasia Battery
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 11
  quote: 'Overall, the AALCTS atlas was the most successful: it could resolve 7 out
    of 10 contrasts.'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-26'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
