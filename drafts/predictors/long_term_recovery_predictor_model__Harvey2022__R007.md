---
id: long_term_recovery_predictor_model
name: long-term aphasia recovery predictor model
kind: predictor
findings:
- id: f1
  target: wab_r_aq_proportion_change
  target_kind: prognosis
  claim: A model combining lesion volume, ALA aphasia domain scores, and ALA participation
    domain scores significantly predicts the proportion change in WAB-R AQ during
    the chronic phase of aphasia.
  direction: likely
  relationship: correlational
  method: behavioral_only
  sample:
    n: 18
    population: individuals with chronic aphasia due to left hemisphere stroke
    phase: not_reported
    time_post_onset: initial assessment at 5 or more months post-onset, with follow-up
      at least 1 year later
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Small sample size may impact generalizability
  - Psychosocial variables were only measured at follow-up, preventing analysis of
    stability across the chronic period
  - Sensitivity analysis excluding participants assessed at exactly 5 MPO showed that
    psychosocial factors were no longer significant predictors
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: A combined model using lesion volume (measured via
    manual segmentation of MRI/CT and computed via VoxBo), and self-reported psychosocial
    scores from the Assessment for Living with Aphasia (ALA) aphasia and participation
    domains. Smaller lesion volume and greater self-perceived aphasia severity (ALA
    aphasia domain) relate to better outcomes; Increased satisfaction with life participation
    (ALA participation domain) is associated with greater long-term language gains;
    The model fit was significantly improved by adding ALA scores to lesion volume.
    Additional metadata has not been transcribed; review the pending-field flags before
    approval. PDF image reading (P5-S1-C2, two-model agreement, human verification
    pending): Participants were included based on the following criteria: initial
    language assessment obtained at 5 or more MPO; native English speaker, pre-morbid
    right handedness, normal or corrected-to-normal vision and hearing; no other comorbid
    neurological or psychiatric disorders; at least 1 year time interval between initial
    and follow-up testing; and had undergone CT or MRI scanning at the time of the
    initial language assessment Original text-layer quotation is preserved below.
    PDF image reading (P5-S1-C4, two-model agreement, human verification pending):
    . The 18 individuals included in the study (12 male) had a mean age of 52.9 (standard
    deviation (SD) = ±12.7; range = 30–77), years of education of 15 (SD = ±3.2; range
    = 12–21), and MPO of 39.8 (SD = ±39.2; range = 5–133) at the initial assessment
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
    - proposed_concept:wab_r_aq_proportion_change
  citation: '@Harvey2022'
  source_passages:
  - section: Original source P10-S1-C1
    page: 10
    quote: "\n68.2% (unadjusted R2) of the variance, F(4, 13) = 6.96, p = .003, R2Adjusted\
      \ = .58, which \nretained three factors: lesion volume as well as ALA scores\
      \ on the aphasia and participation \ndomains."
    supports: claim
  - section: Original source P10-S1-C3
    page: 10
    quote: "Consistent \nwith the previous regression models, the negative regression\
      \ weights for lesion volume \nand ALA aphasia domain scores indicate that smaller\
      \ lesions and greater, self-perceived \naphasia severity relate to better outcomes."
    supports: claim
  - section: Original source P10-S1-C4
    page: 10
    quote: "By contrast, the positive regression weight for \nALA participation domain\
      \ suggests that increased satisfaction with life participation is \nassociated\
      \ with greater long-term language gains."
    supports: claim
  - section: Original source P5-S1-C2
    page: 5
    quote: "Participants were included based on the following criteria: initial language\
      \ assessment \nobtained at 5 or more MPO; native English speaker, pre-morbid\
      \ right handedness, normal \nor corrected-to-normal vision and hearing; no other\
      \ comorbid neurological or psychiatric \ndisorders; at least 1 year time interval\
      \ between initial and follow-up testing; and had \nundergone CT or MRI scanning\
      \ at the time of the initial language assessment."
    supports: sample
  - section: Original source P5-S1-C4
    page: 5
    quote: "The 18 individuals included in the \nstudy (12 male) had a mean age of\
      \ 52.9 (standard deviation (SD) = ±12.7; range = 30–77), \nyears of education\
      \ of 15 (SD = ±3.2; range = 12–21), and MPO of 39.8 (SD = ±39.2; range \n= 5–133)\
      \ at the initial assessment."
    supports: sample
  - section: Original source P6-S1-C12
    page: 6
    quote: 'In both regression models, aphasia recovery was defined as percent change
      in WAB-

      R AQ from initial to follow-up language assessment, calculated as ((AQFollow-up
      – AQinitial)/

      AQinitial) × 100.'
    supports: method
  - section: Original source P10-S1-C7
    page: 10
    quote: "The results were partially \nconsistent with those involving all participants,\
      \ as lesion volume remained a significant \npredictor of long-term language\
      \ gains, p < .05, but psychosocial and treatment-related \nfactors were not,\
      \ p’s > .27."
    supports: limitation
  - section: Original source P13-S1-C2
    page: 13
    quote: "Second, because we did not obtain these data at \ninitial assessment,\
      \ we cannot address whether the relationship between these psychosocial \nvariables\
      \ and aphasia recovery reflects attitudes that were stable across the chronic\
      \ period \nor specific to the follow-up assessment."
    supports: limitation
  - section: Original source P14-S1-C5
    page: 14
    quote: "It is also worth noting that although the lesion subtraction results reported\
      \ \nhere are largely consistent with previous literature (Hope et al., 2013;\
      \ Rosso et al., 2015) \nand are also in line with the uncorrected VLSM results,\
      \ the findings should be interpreted \nwith caution due to the small number\
      \ of participants included as a whole, which can impact \nthe generalizability\
      \ of either result."
    supports: limitation
predictor_type: imaging_metric
short_definition: A combined model using lesion volume (measured via manual segmentation
  of MRI/CT and computed via VoxBo), and self-reported psychosocial scores from the
  Assessment for Living with Aphasia (ALA) aphasia and participation domains.
assessment:
- Western Aphasia Battery-Revised (WAB-R) Aphasia Quotient (AQ)
- Assessment for Living with Aphasia (ALA)
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-24'
relationship_review:
  paper: Harvey2022
  proposal_id: R007
  review_status_sha256: a5065df6065420145974ca440f61948504542cb7b2e59b93c322d9838131452c
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 98e28182cbad7ccf9837885c0de069ab3bf010548b99eebca53d0bfdc50538ec
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 98e28182cbad7ccf9837885c0de069ab3bf010548b99eebca53d0bfdc50538ec
        A/passages.json: e971f85e75ab8df0eec131cfa298fd15103d6b2a78e7354301c49dc8a99176ba
        A/raw.json: 7e92cfd937f14415b36f0e5ab9720f1428cb4c25b99d2cdedf265c736e23ba87
        A/source-units.json: 725f99844edcb28116d1d6b17b83d9b9316f295bbe11147247afab8b2a35fcd9
        A/full-source-units.json: f151b8ae18af299e254085c8ada26a930cea3ccfb3e3f0ac0e087348347246a7
        A/meta.json: f36b4ed24931fdd947f833b6dbb068eb0a681f35baf752691d15ad77f0a217a9
        A/table-images/TABLE-1-page-21-1.png: dfd5654698a8ac746b4385e737dbd7fd57fe86161011da9e49ca198135917764
        A/table-images/TABLE-2-page-22-1.png: 37160f582f36dd7b2d02d9c17aed646e4f80fbfb4307ce5c0a924000401a6b03
        A/table-images/manifest.json: ae37148868201e1d2e6ad7e91118538a2d71f14cdcba3f9c4cf8b9a75625701f
        A/table-images/TABLE-4-page-24-1.png: 36b257789f808e186234048c147f1dbbb39791bba63d832a354a1f43611292a9
        A/table-images/page-21.png: 322eaf3c232e08122efe8674e774cc4ac073dcbb77208fdf3abce8b49f744fb0
        A/table-images/page-23.png: b933435ec9cd2f8134cc300174fd53eb029ff48505c0dafc222d2fe0b8c72077
        A/table-images/page-22.png: 61985389e38e3c235285b8371bd6875e6bd95e96151d1aad03d97ab013ff6eef
        A/table-images/TABLE-3-page-23-1.png: 37b647caa6e49d306bf4b8d3da18e6a28cf67950b2e892203b10254beed60f67
        A/table-images/page-24.png: e08c81fb6a47eac4ce5269cc8a64e0846114ecb16afb96306acf70d3eeb8b549
        A/clauses/window-03/raw.json: 78b4ce36712d2a4185ffa5794fe19b7af83fd18a5c807681b60514870e612bf6
        A/clauses/window-03/prompt.txt: 6c592ea98e5c713ff74d7d23d23b7e423ab3bac85a7123585400911d8033a157
        A/clauses/window-03/meta.json: 7c239671a2d636f690e3c58ad5651afe5b879328d00e1e50832f31e3f9fc9b84
        A/clauses/window-04/raw.json: 0525f38c3ece98e27bf7a8fc43ba81b51fe2cd5c2bd860b499be8688d64a329a
        A/clauses/window-04/prompt.txt: 92d9c47aa16ddadf34fbc222f5f31c35eeee911429e239f036e0215cea0116f8
        A/clauses/window-04/meta.json: cb0872b682d64850b9bfb19e74cdb69ac9913b192c36207ac3c11f81d24aeacf
        A/clauses/window-05/raw.json: 2b02bffb3141b98a3a9d02d2b75895d62339e170d3118c202afd04c0c9a42057
        A/clauses/window-05/prompt.txt: 24f8fdf5b112d120c3eae3ce78da38ca88f8c06d7dabb12e76aa087b649cfaa1
        A/clauses/window-05/meta.json: 7f47cb10f2320e4aaa365d30324f0fc32de20bc95b5831ec0d298cd29645129f
        A/clauses/window-02/raw.json: b80dc67a18c8456993f8ff86fde37fbbe6de112a6dab2b46e22f07fee4278968
        A/clauses/window-02/prompt.txt: 7e4bebd9ab89aba59a5f94230fb6b7f1b8107293bc33f789e13e166da5960dfa
        A/clauses/window-02/meta.json: 848368e1db11824faf5e7ef014402a0dc537571fb6fe6711b58af40eea55bf34
        A/clauses/window-07/raw.json: c12cf298f9797081d2471184f0ed017999be22b4b8709107b98876b9222a285e
        A/clauses/window-07/prompt.txt: 051cc38ad33ea25ff4119ee089957168ba62de083d4f312bd03e4797dec4ad51
        A/clauses/window-07/meta.json: 85842c7b9c34511de0f65e6b1fe34d7004cecf9a03020591df47da5fd93eb0b1
        A/clauses/window-01/raw.json: 63de869d0835c0d5eb08bab2b6658d34db3fdfb8f55316045d22daff160f84af
        A/clauses/window-01/prompt.txt: 83c75312e8e4e85b8b72db4951ca0eed269783a34301af81a765be0765422968
        A/clauses/window-01/meta.json: a0b92d7c188a8c645fc24ca978aa7117a673e41683ff787edcd39c1e5c9dea39
        A/clauses/window-06/raw.json: 6184b202e902927c8fddd7749f30e388852a57b5643ed2575719c98712b863ef
        A/clauses/window-06/prompt.txt: d66df46140c2cab1b9bf296e2b93e916afef71f7db0dd0619e0cfda85b34150d
        A/clauses/window-06/meta.json: cb9d766fcc95ad6f24fc09045013ca03cf8cfa9fe6caee97fe9527142ab8e8be
        A/clauses/window-08/raw.json: 9ba048f992f90118b1116c31879afff9a0a8695973ecac803ae91f060b3e9587
        A/clauses/window-08/prompt.txt: 041f84eaa6128d38ff24a5f76488dfb4044dd07f4c41412ddbb75ac8534c4e56
        A/clauses/window-08/meta.json: 0b459f2b48d713393164182a27229b0c5414ca68f8b9ce93b89b16e623b63b0c
        A/tables/TABLE-4-page-24-4/raw.json: aee9938f154cea2fb0b2d102f4811870748c5f7531a9ea5860df8ef81d83e04f
        A/tables/TABLE-4-page-24-4/prompt.txt: 48356a93ae25d6990019a2ccff3186b19b004cbbd84db68d8cb2083f02db3a30
        A/tables/TABLE-4-page-24-4/meta.json: 14fe40e614409eb7896df5d13f09af04dd202db84461e9e09728312f9cda5601
        A/tables/TABLE-3-page-23-3/raw.json: 31725875c403979bff8a1335fcb0d9f8ada73c798ce84aed265768e1f6d4a50c
        A/tables/TABLE-3-page-23-3/prompt.txt: dc3af511c15c3846b629e57c891d3a5f2496643da3fdff04ed27410ec8560cf7
        A/tables/TABLE-3-page-23-3/meta.json: 4ae62f54be9458b9b72b4c761d9cd27a3b1f0ce26e6fda81563fbb7f214904b2
        A/tables/TABLE-1-page-21-1/raw.json: 92ff10da1fc68b079e7b18ba9d0bfce2f4f2f59311d9c76cf92470ea9a85ff96
        A/tables/TABLE-1-page-21-1/prompt.txt: 2bd3691873e3dea4ab6845d3c704d2ac05e6c60db3511263a95af6ac83d30860
        A/tables/TABLE-1-page-21-1/meta.json: b92a35b9b59773c1b1f1418584521b442edfb18543bad4e05043230c591e267e
        A/tables/TABLE-2-page-22-2/raw.json: eae42695ec033e20068e2de7360c450bb58c8233e5c312d45b9908ceb878e499
        A/tables/TABLE-2-page-22-2/prompt.txt: a4da6989f0143140da047eb9f93c6f4052eef92268bfd8fe4ea273eae686cb07
        A/tables/TABLE-2-page-22-2/meta.json: 137d7b63ff2ea865dc9295595c295c614d1260de8450002e6d6b8c62d4cfb2c5
        B/passages.json: e971f85e75ab8df0eec131cfa298fd15103d6b2a78e7354301c49dc8a99176ba
        B/raw.json: 72fbf480612c9d6e018b03e814e121fb6c09700d28a8648ca557e2f8f031727f
        B/source-units.json: 725f99844edcb28116d1d6b17b83d9b9316f295bbe11147247afab8b2a35fcd9
        B/full-source-units.json: f151b8ae18af299e254085c8ada26a930cea3ccfb3e3f0ac0e087348347246a7
        B/meta.json: e3c5b6b1d66037b05c18201d26e5ffb96400c9c058ea7f57f8280ec56298e825
        B/table-images/TABLE-1-page-21-1.png: dfd5654698a8ac746b4385e737dbd7fd57fe86161011da9e49ca198135917764
        B/table-images/TABLE-2-page-22-1.png: 37160f582f36dd7b2d02d9c17aed646e4f80fbfb4307ce5c0a924000401a6b03
        B/table-images/manifest.json: ddad6fd225f2d16ad174377ccf6e0a2a90ede3e5728a56719548a1581ddc623d
        B/table-images/TABLE-4-page-24-1.png: 36b257789f808e186234048c147f1dbbb39791bba63d832a354a1f43611292a9
        B/table-images/page-21.png: 322eaf3c232e08122efe8674e774cc4ac073dcbb77208fdf3abce8b49f744fb0
        B/table-images/page-23.png: b933435ec9cd2f8134cc300174fd53eb029ff48505c0dafc222d2fe0b8c72077
        B/table-images/page-22.png: 61985389e38e3c235285b8371bd6875e6bd95e96151d1aad03d97ab013ff6eef
        B/table-images/TABLE-3-page-23-1.png: 37b647caa6e49d306bf4b8d3da18e6a28cf67950b2e892203b10254beed60f67
        B/table-images/page-24.png: e08c81fb6a47eac4ce5269cc8a64e0846114ecb16afb96306acf70d3eeb8b549
        B/clauses/window-03/raw.json: 49170a061f9ed361251396e9ae815f6e609876d9fd810f82f2814015a4bbd090
        B/clauses/window-03/prompt.txt: 6c592ea98e5c713ff74d7d23d23b7e423ab3bac85a7123585400911d8033a157
        B/clauses/window-03/meta.json: 0a5e6f9687f81701d666381616a4e6c175d1d3eea9b584731ad377b5927d4c39
        B/clauses/window-04/raw.json: a8d939f1a63a51c13ee69559b65137f9c9936838983c9f991fa3e633da6fc101
        B/clauses/window-04/prompt.txt: 92d9c47aa16ddadf34fbc222f5f31c35eeee911429e239f036e0215cea0116f8
        B/clauses/window-04/meta.json: b02f7a3342c947d9f2c95359e7d8c72277faa6c8e25dc8e04045a38ce8198729
        B/clauses/window-05/raw.json: 7e9095077c19b65697eb70818aa289988469ec616ee63e44776d97e3e6e05260
        B/clauses/window-05/prompt.txt: 24f8fdf5b112d120c3eae3ce78da38ca88f8c06d7dabb12e76aa087b649cfaa1
        B/clauses/window-05/meta.json: c0ddadca949c135e1dca78bfd81736ce2b7a9bcc40be0158a4700d4b7fb9a986
        B/clauses/window-02/raw.json: e3fabddedf2eadb155b392f3a636d18b99b1b3a48f1f8a2ceafb488adae9f92a
        B/clauses/window-02/prompt.txt: 7e4bebd9ab89aba59a5f94230fb6b7f1b8107293bc33f789e13e166da5960dfa
        B/clauses/window-02/meta.json: ffa6abfb37ef11560ce82befd92a94d5eb69109904bc892b18ba2936ee195281
        B/clauses/window-07/raw.json: bcd134c4f1ae0d631d09904d6a6f9db42dec458d329ee0ba78b9ded29cd999f9
        B/clauses/window-07/prompt.txt: 051cc38ad33ea25ff4119ee089957168ba62de083d4f312bd03e4797dec4ad51
        B/clauses/window-07/meta.json: ce965c06b678aa0fa6e9a311e541196e244080717693f40061f59ada910c4bfa
        B/clauses/window-01/raw.json: 0f9ae609c3fb7f79d996cb32e01e9807334fe6d2cf1ae378fb49d93ca5f8922f
        B/clauses/window-01/prompt.txt: 83c75312e8e4e85b8b72db4951ca0eed269783a34301af81a765be0765422968
        B/clauses/window-01/meta.json: b769ece90db573266e84817f7128a9be86b51eca02edaeda6dab3e5fdb0a78d9
        B/clauses/window-06/raw.json: a15655786e6461103bb8281b7aa937ef2fb96ad7c50b2fc6114a196de8bce1e5
        B/clauses/window-06/prompt.txt: d66df46140c2cab1b9bf296e2b93e916afef71f7db0dd0619e0cfda85b34150d
        B/clauses/window-06/meta.json: f6cd28bcae4c065940327b94de794d45002b382bd948dcd5e204b3011a48bf24
        B/clauses/window-08/raw.json: 710919ebff3c2548eeaea5a43d4311625f09c64a46db5a06b2f6211cfe368fda
        B/clauses/window-08/prompt.txt: 041f84eaa6128d38ff24a5f76488dfb4044dd07f4c41412ddbb75ac8534c4e56
        B/clauses/window-08/meta.json: 417e5003f536a1f95a7c2237d27d305749c45afeaea16d3ea590f3480f03e1ba
        B/tables/TABLE-4-page-24-4/raw.json: 010d51ea72d0f71e3f66b0dfb300b62ad87cef135ec57a2cdf4c987b648b755f
        B/tables/TABLE-4-page-24-4/prompt.txt: 48356a93ae25d6990019a2ccff3186b19b004cbbd84db68d8cb2083f02db3a30
        B/tables/TABLE-4-page-24-4/meta.json: 45cbf6f5904e36e8c2bca58974ba97a0d904967d83ff4ea93094b3c2aea68cd7
        B/tables/TABLE-3-page-23-3/raw.json: 1bd73af2cea36bc3cad346e18d5e85460b63b3b338803b80e704a1d456066302
        B/tables/TABLE-3-page-23-3/prompt.txt: dc3af511c15c3846b629e57c891d3a5f2496643da3fdff04ed27410ec8560cf7
        B/tables/TABLE-3-page-23-3/meta.json: 5215d12b8b0a47279985cbf5e851934cbca684cac79f872dc4d34e72d26a2b88
        B/tables/TABLE-1-page-21-1/raw.json: 77ed6d13ae70f262f81a16055fd0dbfdab96e86832864685870e90539be8c85a
        B/tables/TABLE-1-page-21-1/prompt.txt: 2bd3691873e3dea4ab6845d3c704d2ac05e6c60db3511263a95af6ac83d30860
        B/tables/TABLE-1-page-21-1/meta.json: 840586a30a6486c0bb16478d6438e753fd5f24c73ecb7e0c5e503702238f9a71
        B/tables/TABLE-2-page-22-2/raw.json: eae42695ec033e20068e2de7360c450bb58c8233e5c312d45b9908ceb878e499
        B/tables/TABLE-2-page-22-2/prompt.txt: a4da6989f0143140da047eb9f93c6f4052eef92268bfd8fe4ea273eae686cb07
        B/tables/TABLE-2-page-22-2/meta.json: 03f9d34bf63a009fc0aaa428949f2e1e1386d5feed1ed6fd058a21b8affe4c9c
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
      pdf_sha256: 98e28182cbad7ccf9837885c0de069ab3bf010548b99eebca53d0bfdc50538ec
      source_review: _compare/relationships-2026-11-16/review-current/Harvey2022
      source_status_sha256: 26fb808213296dce7e4b8ba70e3b60f7613a89221c52849b38a8e7ed65ac2ae0
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R007
    exposure:
      text: lesion volume, ALA aphasia domain score, and ALA participation domain
        score
    outcome:
      text: proportion change in WAB-R AQ
    analysis_label: Stepwise regression assessing added predictive value
    relation: association
    evidence_ids:
    - P10-S1-C3
    - P10-S1-C4
    qualifier_ids:
    - P10-S1-C1
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 98e28182cbad7ccf9837885c0de069ab3bf010548b99eebca53d0bfdc50538ec
      source_review: _compare/relationships-2026-11-16/review-current/Harvey2022
      source_status_sha256: 26fb808213296dce7e4b8ba70e3b60f7613a89221c52849b38a8e7ed65ac2ae0
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P1-S1-C10
      - Accounting without a linked unit P1-S1-C11
      - Accounting without a linked unit P1-S1-C12
      - Accounting without a linked unit P1-S1-C13
      - Accounting without a linked unit P1-S1-C14
      - Result passage disposed without unit P2-S1-C5
      - Unaccounted source passage P1-S1-C13
      - Unaccounted source passage P1-S1-C14
      - Unaccounted source passage P1-S1-C11
      - Unaccounted source passage P1-S1-C12
      - Result passage disposed without unit P4-S1-C7
      - Result passage disposed without unit P9-S1-C2
      - Result passage disposed without unit P9-S1-C3
      - Result passage disposed without unit P9-S1-C5
      - Accounting without a linked unit P9-S2-C7
      - Unaccounted source passage P9-S2-C7
      - Result passage disposed without unit P10-S1-C10
      - Result passage disposed without unit P10-S1-C9
      - Result passage disposed without unit P10-S2-C6
      - Result passage disposed without unit P11-S1-C5
      - Result passage disposed without unit P11-S1-C8
      - Accounting without a linked unit P13-S1-C2
      - Accounting without a linked unit P13-S1-C3
      - Accounting without a linked unit P13-S1-C5
      - Accounting without a linked unit P13-S1-C6
      - Accounting without a linked unit P13-S1-C8
      - Accounting without a linked unit P13-S1-C9
      - Accounting without a linked unit P13-S2-C3
      - Unaccounted source passage P13-S1-C2
      - Unaccounted source passage P13-S1-C8
      - Unaccounted source passage P13-S1-C3
      - Unaccounted source passage P13-S1-C5
      - Unaccounted source passage P13-S2-C3
      - Unaccounted source passage P13-S1-C6
      - Unaccounted source passage P13-S1-C9
      - Accounting without a linked unit P13-S2-C7
      - Accounting without a linked unit P14-S1-C9
      - Result passage disposed without unit P14-S2-C2
      - Unaccounted source passage P14-S1-C9
      - Unaccounted source passage P13-S2-C7
      unattached_null_or_qualifier_ids:
      - P1-S1-C10
      - P1-S1-C12
      - P9-S1-C3
      - P11-S1-C5
      - P13-S1-C3
      - P13-S1-C6
      - P13-S2-C7
      suppressed_nonrepresented_units: 6
      default_disposition_count_requires_completeness_check: 157
      unselected_timing_passages:
      - P1-S1-C7
      - P5-S1-C2
      - P5-S1-C4
      - P9-S1-C1
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P9-S1-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S1-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S1-C12
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S1-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P14-S1-C5
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: tested_personal_effects
        source_id: P13-S1-C4
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: personal_factors
        source_ids:
        - P4-S1-C10
        - P5-S1-C7
        - P5-S2-C2
        - P5-S2-C3
        - P5-S2-C5
        - P6-S1-C10
        - P7-S1-C1
        - P9-S1-C11
        - P9-S1-C12
        - P10-S1-C1
        - P10-S1-C4
        - P11-S1-C4
        - P12-S1-C8
        - P12-S2-C2
        - P12-S2-C4
        - P13-S1-C4
        - P13-S1-C6
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - validation
      - personal_factors
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-21-1
      - TABLE-2-page-22-2
      - TABLE-3-page-23-3
      - TABLE-4-page-24-4
      unlinked_tables:
      - TABLE-1-page-21-1
      - TABLE-4-page-24-4
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
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 98e28182cbad7ccf9837885c0de069ab3bf010548b99eebca53d0bfdc50538ec
      source_review: _compare/relationships-2026-11-16/review-current/Harvey2022
      source_status_sha256: 26fb808213296dce7e4b8ba70e3b60f7613a89221c52849b38a8e7ed65ac2ae0
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes participant group distribution (improved vs stable/declined).
    - source_id: P1-S1-C11
      disposition: repeated
      result_indexes:
      - 0
      reason: Abstract restatement of lesion volume prediction.
    - source_id: P1-S1-C12
      disposition: repeated
      result_indexes:
      - 11
      reason: Abstract restatement of lesion location findings.
    - source_id: P1-S1-C13
      disposition: repeated
      result_indexes:
      - 2
      - 3
      - 4
      reason: Abstract restatement of psychosocial and treatment factors.
    - source_id: P1-S1-C14
      disposition: repeated
      result_indexes:
      - 6
      reason: Abstract restatement of model fit improvement.
    - source_id: P2-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Introduction of previous findings/observations.
    - source_id: P4-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement of study goal.
    - source_id: P4-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation of incidental findings during retesting.
    - source_id: P9-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive range of AQ difference scores.
    - source_id: P9-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive count of participants improving.
    - source_id: P9-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of group subdivision for analysis.
    - source_id: P9-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Clinical significance of AQ increase.
    - source_id: P9-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of model variable removal (sex).
    - source_id: P9-S1-C7
      disposition: represented
      result_indexes:
      - 0
      - 1
      reason: Provides model fit statistics for the first regression.
    - source_id: P9-S1-C8
      disposition: represented
      result_indexes:
      - 0
      reason: Identifies lesion volume as significant predictor.
    - source_id: P9-S1-C9
      disposition: represented
      result_indexes:
      - 0
      reason: Specifies direction of lesion volume effect.
    - source_id: P9-S1-C10
      disposition: represented
      result_indexes:
      - 1
      reason: States other predictors were not significant.
    - source_id: P9-S1-C11
      disposition: represented
      result_indexes:
      - 2
      - 3
      - 4
      reason: Provides model fit and retained factors for psychosocial regression.
    - source_id: P9-S1-C12
      disposition: represented
      result_indexes:
      - 2
      - 3
      - 4
      reason: Identifies significant psychosocial factors and SLT trend.
    - source_id: P9-S2-C3
      disposition: represented
      result_indexes:
      - 2
      reason: Specifies positive relationship for participation domain.
    - source_id: P9-S2-C4
      disposition: represented
      result_indexes:
      - 4
      reason: Specifies positive benefit of SLT.
    - source_id: P9-S2-C5
      disposition: represented
      result_indexes:
      - 3
      reason: Specifies negative relationship for aphasia domain.
    - source_id: P9-S2-C6
      disposition: represented
      result_indexes:
      - 6
      reason: States psychosocial factors improved model fit.
    - source_id: P9-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Model variance statistics.
    - source_id: P10-S1-C1
      disposition: represented
      result_indexes:
      - 6
      - 7
      reason: Provides model fit and retained factors for combined regression.
    - source_id: P10-S1-C2
      disposition: represented
      result_indexes:
      - 8
      reason: States SLT was not significant in combined model.
    - source_id: P10-S1-C3
      disposition: represented
      result_indexes:
      - 7
      reason: Specifies weights for lesion volume and aphasia domain.
    - source_id: P10-S1-C4
      disposition: represented
      result_indexes:
      - 7
      reason: Specifies weight for participation domain.
    - source_id: P10-S1-C7
      disposition: represented
      result_indexes:
      - 9
      - 10
      reason: Results of sensitivity analysis excluding 5 MPO participants.
    - source_id: P10-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive observation of lesion overlap maps.
    - source_id: P10-S1-C10
      disposition: represented
      result_indexes:
      - 11
      reason: Introduces lesion subtraction results.
    - source_id: P10-S1-C11
      disposition: represented
      result_indexes:
      - 11
      reason: Identifies cortical regions associated with non-improvement.
    - source_id: P10-S2-C1
      disposition: repeated
      result_indexes:
      - 11
      reason: Repeats cortical region findings.
    - source_id: P10-S2-C2
      disposition: represented
      result_indexes:
      - 11
      reason: Details specific temporoparietal regions.
    - source_id: P10-S2-C3
      disposition: represented
      result_indexes:
      - 11
      reason: Details specific frontal regions.
    - source_id: P10-S2-C4
      disposition: represented
      result_indexes:
      - 11
      reason: Details specific white matter structures.
    - source_id: P10-S2-C5
      disposition: represented
      result_indexes:
      - 11
      reason: Details other white matter tracts.
    - source_id: P10-S2-C6
      disposition: represented
      result_indexes:
      - 12
      reason: States VLSM results are consistent with subtraction analysis.
    - source_id: P10-S2-C7
      disposition: represented
      result_indexes:
      - 12
      reason: Concludes regions impact recovery regardless of total volume.
    - source_id: P11-S1-C3
      disposition: repeated
      result_indexes:
      - 11
      reason: Discussion restatement of lesion location.
    - source_id: P11-S1-C4
      disposition: repeated
      result_indexes:
      - 2
      - 3
      reason: Discussion restatement of psychosocial factors.
    - source_id: P11-S1-C5
      disposition: repeated
      result_indexes:
      - 4
      reason: Discussion restatement of SLT effect.
    - source_id: P11-S1-C8
      disposition: repeated
      result_indexes:
      - 0
      reason: Discussion restatement of lesion volume.
    - source_id: P11-S2-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Citing prior literature (Plowman et al.).
    - source_id: P11-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparing current results to prior studies (Basilakos, Hope).
    - source_id: P12-S1-C1
      disposition: repeated
      result_indexes:
      - 11
      reason: Discussion restatement of lesion location.
    - source_id: P12-S1-C5
      disposition: repeated
      result_indexes:
      - 12
      reason: Discussion restatement of VLSM results.
    - source_id: P12-S1-C8
      disposition: repeated
      result_indexes:
      - 2
      - 3
      reason: Discussion restatement of psychosocial vs demographic variables.
    - source_id: P12-S2-C2
      disposition: repeated
      result_indexes:
      - 2
      - 3
      reason: Discussion restatement of ALA domain relationships.
    - source_id: P13-S1-C3
      disposition: repeated
      result_indexes:
      - 1
      reason: Discussion restatement of null demographic findings.
    - source_id: P13-S1-C5
      disposition: repeated
      result_indexes:
      - 4
      reason: Discussion restatement of SLT influence.
    - source_id: P13-S2-C3
      disposition: repeated
      result_indexes:
      - 6
      reason: Discussion restatement of model fit improvement.
    - source_id: P13-S2-C7
      disposition: repeated
      result_indexes:
      - 9
      - 10
      reason: Discussion restatement of sensitivity analysis.
    - source_id: P14-S1-C5
      disposition: repeated
      result_indexes:
      - 11
      - 12
      reason: Discussion restatement of lesion analysis consistency.
    - source_id: P14-S2-C1
      disposition: repeated
      result_indexes:
      - 0
      reason: Conclusion restatement of lesion size as predictor.
    unresolved_coverage:
    - source_id: P9-S2-C7
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P10-S2-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P10-S2-C6
      disposition: unresolved
      reason: Unknown result index; not accepted as coverage
    - source_id: P10-S2-C7
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P11-S2-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P11-S2-C2
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P12-S1-C5
      disposition: unresolved
      reason: Unknown result index; not accepted as coverage
    - source_id: P14-S1-C5
      disposition: unresolved
      reason: Unknown result index; not accepted as coverage
    - source_id: P14-S2-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P11-S2-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S2-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S2-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S1-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S1-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S1-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P14-S1-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P14-S2-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C10
    - P1-S1-C11
    - P1-S1-C12
    - P1-S1-C13
    - P1-S1-C14
    - P2-S1-C5
    - P4-S1-C5
    - P4-S1-C7
    - P9-S1-C2
    - P9-S1-C3
    - P9-S1-C4
    - P9-S1-C5
    - P9-S1-C6
    - P9-S1-C7
    - P9-S1-C11
    - P10-S1-C1
    - P10-S1-C9
    - P10-S1-C10
    - P11-S1-C3
    - P11-S1-C4
    - P11-S1-C5
    - P11-S1-C8
    - P11-S2-C8
    - P12-S1-C1
    - P12-S1-C5
    - P12-S1-C8
    - P12-S2-C2
    - P12-S2-C4
    - P12-S2-C5
    - P13-S1-C3
    - P13-S1-C5
    - P13-S1-C6
    - P13-S1-C8
    - P13-S1-C9
    - P13-S2-C3
    - P13-S2-C7
    - P14-S1-C5
    - P14-S1-C9
    - P14-S2-C2
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-21-1
    - TABLE-2-page-22-2
    - TABLE-3-page-23-3
    - TABLE-4-page-24-4
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P5-S1-C4
      recruited_sample:
      - P4-S1-C6
      eligibility:
      - P5-S1-C2
      imaging_provenance:
      - P6-S1-C4
      - P6-S1-C5
      - P8-S2-C4
      imaging_timing:
      - P6-S1-C3
      outcome_timing:
      - P4-S1-C9
      - P6-S1-C12
      outcome_definition:
      - P6-S1-C12
      validation: []
      analysis_restrictions:
      - P7-S1-C2
      - P7-S1-C3
      - P7-S1-C4
      - P10-S1-C6
      dependent_variable_statement:
      - P6-S1-C10
      - P6-S1-C12
      - P8-S1-C1
      limitations:
      - P8-S1-C2
      - P8-S1-C3
      - P8-S2-C7
      - P13-S1-C8
      - P13-S1-C9
      - P14-S1-C5
      - P14-S1-C6
      personal_factors: []
      tested_personal_effects:
      - P9-S1-C11
      - P9-S1-C12
      - P10-S1-C1
      - P10-S1-C4
      - P11-S1-C4
      - P12-S1-C8
      - P13-S1-C6
      adjustment_roles:
      - P6-S1-C10
      - P6-S2-C2
      - P6-S2-C3
      - P7-S2-C3
      - P7-S2-C9
      - P8-S1-C1
      - P8-S2-C5
      explicitly_not_adjusted:
      - P7-S1-C2
      - P7-S1-C3
      - P7-S1-C4
      descriptive_personal_factors:
      - P5-S1-C4
    outcome_type: change_from_baseline
    imaging_vs_outcome: precedes_outcome
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P9-S1-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S1-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S1-C12
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S1-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P14-S1-C5
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: tested_personal_effects
      source_id: P13-S1-C4
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: personal_factors
      source_ids:
      - P4-S1-C10
      - P5-S1-C7
      - P5-S2-C2
      - P5-S2-C3
      - P5-S2-C5
      - P6-S1-C10
      - P7-S1-C1
      - P9-S1-C11
      - P9-S1-C12
      - P10-S1-C1
      - P10-S1-C4
      - P11-S1-C4
      - P12-S1-C8
      - P12-S2-C2
      - P12-S2-C4
      - P13-S1-C4
      - P13-S1-C6
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
      pdf_sha256: 98e28182cbad7ccf9837885c0de069ab3bf010548b99eebca53d0bfdc50538ec
      review_sha256: a5065df6065420145974ca440f61948504542cb7b2e59b93c322d9838131452c
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
      - P10-S1-C3
      - P10-S1-C4
      source_result: In the stepwise regression model assessing added predictive value,
        the inclusion of ALA aphasia and participation domain scores alongside lesion
        volume significantly improved model fit (F(3, 13) = 3.66, p = .04). The final
        model retained lesion volume, ALA aphasia domain, and ALA participation domain
        as significant predictors of proportion change in WAB-R AQ. Specifically,
        smaller lesion volume and greater self-perceived aphasia severity (negative
        regression weight for ALA aphasia domain) were associated with better outcomes,
        while increased satisfaction with life participation (positive regression
        weight for ALA participation domain) was associated with greater long-term
        language gains. Amount of SLT was not a significant predictor in this final
        model.
      result_status: detected
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis R007 corresponds to the third regression model
            described in the source (P6-S1-C10, P7-S1-C6, P9-S2-C6), which evaluates
            the added predictive value of psychosocial factors (ALA domains) to the
            previously identified predictor (lesion volume). The outcome is proportion
            change in WAB-R AQ. The source confirms this specific model structure
            and result.
          source_ids:
          - P6-S1-C10
          - P7-S1-C6
          - P9-S2-C6
          - P10-S1-C1
        direction:
          answer: fits
          reason: 'The source explicitly states the direction of the associations:
            negative regression weights for lesion volume and ALA aphasia domain (indicating
            smaller lesions and greater perceived severity relate to better outcomes)
            and a positive regression weight for ALA participation domain (indicating
            increased satisfaction relates to greater gains). The proposed core correctly
            captures these directions.'
          source_ids:
          - P10-S1-C3
          - P10-S1-C4
        construct:
          answer: fits
          reason: The exposure variables (lesion volume, ALA aphasia/participation
            scores) and outcome (proportion change in WAB-R AQ) are correctly identified.
            The patient measurement for lesion volume is template_lesion_overlap (lesions
            warped to MNI template, volume computed via VoxBo), not patient_diffusion.
            The ALA scores are self-report psychosocial measures. The construct is
            faithful to the source.
          source_ids:
          - P6-S1-C8
          - P6-S1-C9
          - P5-S1-C7
          - P6-S1-C12
        qualifications:
          answer: fits
          reason: 'The proposed core includes the key qualifications: the specific
            directions of the predictors, the significant improvement in model fit,
            and the limitations regarding small sample size and the sensitivity analysis
            excluding participants at 5 MPO (where psychosocial factors lost significance).
            These are all present in the source (P10-S1-C6, P10-S1-C7, P14-S1-C5).'
          source_ids:
          - P10-S1-C6
          - P10-S1-C7
          - P14-S1-C5
        missing_material_caveat:
          answer: fits
          reason: The core includes the critical caveat that the association of psychosocial
            factors was not robust when excluding participants assessed at the cusp
            of the chronic phase (5 MPO), as noted in P10-S1-C7. It also notes the
            small sample size limitation. No material caveats are omitted that would
            change the interpretation of the detected association.
          source_ids:
          - P10-S1-C7
          - P14-S1-C5
      optional_pending:
      - Specific R-squared values and F-statistics for the final model
      - Exact p-values for individual predictors in the final model
      - Details of the 'add-on' questions excluded from the model
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Specific R-squared values and F-statistics for the final model
    - Exact p-values for individual predictors in the final model
    - Details of the 'add-on' questions excluded from the model
    normalizations: []
    analysis_identity:
      id: R007
      exposure:
        text: lesion volume, ALA aphasia domain score, and ALA participation domain
          score
      outcome:
        text: proportion change in WAB-R AQ
      analysis_label: Stepwise regression assessing added predictive value
      relation: association
      evidence_ids:
      - P10-S1-C3
      - P10-S1-C4
      qualifier_ids:
      - P10-S1-C1
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 98e28182cbad7ccf9837885c0de069ab3bf010548b99eebca53d0bfdc50538ec
        source_review: _compare/relationships-2026-11-16/review-current/Harvey2022
        source_status_sha256: 26fb808213296dce7e4b8ba70e3b60f7613a89221c52849b38a8e7ed65ac2ae0
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P5-S1-C2:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 98e28182cbad7ccf9837885c0de069ab3bf010548b99eebca53d0bfdc50538ec
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: c3b51ae070c7b3a64e0badaf3890f4766d9b700744443c6e0bd4dcc8201f3015
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P5-S1-C2
          page: 5
          text_layer_sha256: c3b51ae070c7b3a64e0badaf3890f4766d9b700744443c6e0bd4dcc8201f3015
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "Participants were included based on the following criteria:\
          \ initial language assessment \nobtained at 5 or more MPO; native English\
          \ speaker, pre-morbid right handedness, normal \nor corrected-to-normal\
          \ vision and hearing; no other comorbid neurological or psychiatric \ndisorders;\
          \ at least 1 year time interval between initial and follow-up testing; and\
          \ had \nundergone CT or MRI scanning at the time of the initial language\
          \ assessment."
        anchor_text: "Participants were included based on the following criteria:\
          \ initial language assessment \nobtained at 5 or more MPO; native English\
          \ speaker, pre-morbid right handedness, normal \nor corrected-to-normal\
          \ vision and hearing; no other comorbid neurological or psychiatric \ndisorders;\
          \ at least 1 year time interval between initial and follow-up testing; and\
          \ had \nundergone CT or MRI scanning at the time of the initial language\
          \ assessment."
        excluded_fragments: []
        image_sha256: e4e2e3aa22c3069d1304d50d7d2bbb9fb9584b4657a66ac9faf4f2b5e9891cf6
        transcription: 'Participants were included based on the following criteria:
          initial language assessment obtained at 5 or more MPO; native English speaker,
          pre-morbid right handedness, normal or corrected-to-normal vision and hearing;
          no other comorbid neurological or psychiatric disorders; at least 1 year
          time interval between initial and follow-up testing; and had undergone CT
          or MRI scanning at the time of the initial language assessment'
      P5-S1-C4:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 98e28182cbad7ccf9837885c0de069ab3bf010548b99eebca53d0bfdc50538ec
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 81fcccfce6750be51f0ddc7a1a59a7d2cb9b57e291837f0ebf670c70c629b0e7
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P5-S1-C4
          page: 5
          text_layer_sha256: 81fcccfce6750be51f0ddc7a1a59a7d2cb9b57e291837f0ebf670c70c629b0e7
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "The 18 individuals included in the \nstudy (12 male) had a\
          \ mean age of 52.9 (standard deviation (SD) = ±12.7; range = 30–77), \n\
          years of education of 15 (SD = ±3.2; range = 12–21), and MPO of 39.8 (SD\
          \ = ±39.2; range \n= 5–133) at the initial assessment."
        anchor_text: "The 18 individuals included in the \nstudy (12 male) had a mean\
          \ age of 52.9 (standard deviation (SD) = ±12.7; range = 30–77), \nyears\
          \ of education of 15 (SD = ±3.2; range = 12–21), and MPO of 39.8 (SD = ±39.2;\
          \ range \n= 5–133) at the initial assessment."
        excluded_fragments: []
        image_sha256: e9b069718f68f8eb78bc50276b90ee878ca4eef69ed21c7a6f8c3a48771a3ca8
        transcription: . The 18 individuals included in the study (12 male) had a
          mean age of 52.9 (standard deviation (SD) = ±12.7; range = 30–77), years
          of education of 15 (SD = ±3.2; range = 12–21), and MPO of 39.8 (SD = ±39.2;
          range = 5–133) at the initial assessment
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 10
  quote: "\n68.2% (unadjusted R2) of the variance, F(4, 13) = 6.96, p = .003, R2Adjusted\
    \ = .58, which \nretained three factors: lesion volume as well as ALA scores on\
    \ the aphasia and participation \ndomains."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-24'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
