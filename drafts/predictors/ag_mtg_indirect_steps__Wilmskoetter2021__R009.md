---
id: ag_mtg_indirect_steps
name: AG-MTG indirect connection steps
kind: predictor
findings:
- id: f1
  target: naming_recovery
  target_kind: prognosis
  claim: Among participants with indirect connections, fewer steps along the indirect connection between the AG and MTG significantly predicted an increase in correct naming responses after treatment.
  direction: likely
  relationship: correlational
  method: tractography
  sample:
    n: 32
    population: Thirty-two participants with an indirect AG-MTG connection from the 69-person chronic left-hemisphere ischaemic stroke aphasia cohort.
    phase: not_reported
    time_post_onset: measured at baseline and 24 weeks posttreatment
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - indirect connections were mapped based on structural connectomics, so functional use cannot be claimed
  - lesion maps were binarized
  - findings may not generalize to other aspects of language recovery beyond naming accuracy
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: The minimal number of steps (crossed gray matter nodes) along the shortest path between the angular gyrus (AG) and middle temporal gyrus (MTG), calculated using probabilistic tractography and network modeling on the whole-brain connectome. analysis performed only on participants with indirect connections; controlled for age, years of formal education, baseline WAB-AQ, and treatment type (A-tDCS vs S-tDCS); no such association was found for indirect connections between the IFGop and AG or the IFGop and MTG. Additional metadata has not been transcribed; review the pending-field flags before approval. PDF image reading (P3-S1-C1, two-model agreement, human verification pending): clinical trial evaluating the use of tDCS for aphasia treatment conducted at the University of South Carolina and the Medical University of South Carolina.²⁵ We included 69 of 74 participants from the clinical trial (excluding participants with hemorrhagic stroke [N = 2], no diffusion
    tensor imaging [N = 2], no posttreatment follow-up [N = 1]) Original text-layer quotation is preserved below. Publication correction (human verification pending): Analysis restricted to participants with an indirect AG-MTG connection, not the full cohort.'
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
    - proposed_concept:naming_recovery
    - publication_correction_pending_human_verification
  therapy:
    id: computerized_language_treatment
    name: computerized language treatment focusing on lexical-semantic processing
  citation: '@Wilmskoetter2021'
  source_passages:
  - section: Original source P6-S1-C11
    page: 6
    quote: "Fewer Steps Along Indirect Connections Predict \nBetter Treated Naming Recovery\nFor those participants with indirect connections, fewer \nsteps along the indirect connection between the AG and \nMTG significantly predicted an increase in correct naming \nresponses after treatment (standardized beta = −0.517, \nP = .012)."
    supports: claim
  - section: Original source P8-S1-C4
    page: 8
    quote: "Fewer Steps Along Indirect Connections Predict \nBetter Treated Naming Recovery\nIn line with our hypothesis we found a significant associa-\ntion between the number of steps along indirect connections \nbetween the AG and MTG and treated anomia recovery."
    supports: claim
  - section: Original source P8-S1-C5
    page: 8
    quote: "Fewer steps along indirect connections between the AG and \nMTG was predictive of more correct responses at follow-up \ncompared to baseline."
    supports: claim
  - section: Original source P8-S1-C6
    page: 8
    quote: "However, we did not find this asso-\nciation for indirect connections between the IFGop and AG \nor the IFGop and MTG."
    supports: claim
  - section: Original source P5-S2-C7
    page: 5
    quote: "To test Hypothesis 2, we performed multivariable linear \nregression modeling on participants with indirect connec-\ntions to test whether the number of steps along indirect con-\nnections was predictive of change in naming from baseline \nto follow-up."
    supports: method
  - section: Original source P5-S2-C8
    page: 5
    quote: We controlled for the same variables as before.
    supports: method
  - section: Original source P4-S1-C6
    page: 4
    quote: "We calculated indi-\nrect pairwise connections by computing the shortest path \nlength (ie, the minimal number of steps) between each pair \nof gray matter regions."
    supports: method
  - section: Original source P4-S1-C8
    page: 4
    quote: "Based on previously developed \nmethods,23,24 validated in participants with stroke,33 we \ncalculated propagation steps as follows: (1) 1 gray matter \nROI was seeded as the start region, (2) all neighboring \nregions directly connected to the start region were seeded, \nand (3) all neighboring regions reached from the seeded \nregions (indirectly connected to the start-region) are seeded."
    supports: method
  - section: Original source P3-S1-C7
    page: 3
    quote: "Outcome Measures for Anomia\nNaming accuracy was measured twice before and twice at \n24 weeks posttreatment with the Philadelphia Naming \nTest (PNT).28 Given variability in day-to-day aphasic per-\nformance, the number of correct items at each baseline \nand at each follow-up PNT administration was averaged."
    supports: method
  - section: Original source P3-S1-C1
    page: 3
    quote: "\n348\t\nNeurorehabilitation and Neural Repair 35(4)\nclinical trial evaluating the use of tDCS for aphasia treat-\nment conducted at the University of South Carolina and the \nMedical University of South Carolina.25 We included 69 of \n74 participants from the clinical trial (excluding partici-\npants with hemorrhagic stroke [N = 2], no diffusion tensor \nimaging [N = 2], no posttreatment follow-up [N = 1])."
    supports: sample
  - section: Original source P8-S3-C3
    page: 8
    quote: 'Limitations

      We mapped indirect connections based on structural con-

      nectomics; thus, we cannot claim that these indirect path-

      ways are indeed functionally used.'
    supports: limitation
  - section: Original source P8-S3-C5
    page: 8
    quote: "Furthermore, we binarized lesion maps into either \nlesioned or not lesioned tissue."
    supports: limitation
  - section: Original source P8-S3-C8
    page: 8
    quote: "Last, because we focused on treated naming recovery, \nfindings of this study might not generalize to improvements \nin other aspects of language with aphasia treatment."
    supports: limitation
predictor_type: imaging_metric
short_definition: The minimal number of steps (crossed gray matter nodes) along the shortest path between the angular gyrus (AG) and middle temporal gyrus (MTG), calculated using probabilistic tractography and network modeling on the whole-brain connectome.
assessment:
- Philadelphia Naming Test
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-26'
relationship_review:
  paper: Wilmskoetter2021
  proposal_id: R009
  review_status_sha256: 2e72ce2da0fd23b5fb9c83abb043c54f924a9e4fcc9de0368d7e042afd215acd
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 0b1cc78748f5f745c2e71127f56abbd32d3406925ae47b768f87f28ab874378a
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 0b1cc78748f5f745c2e71127f56abbd32d3406925ae47b768f87f28ab874378a
        A/passages.json: 62dc6d7d1e56e4f6c8864d804af73a1539d90b1aef1d7e5c7c908ee3fc4d7e87
        A/raw.json: 8c2d5de2d02630e12f57a3daec7788df8342884c7b701840798f6d79c8f57769
        A/source-units.json: 3e888bdc1bc8588737e1dcf8de509490f6b475499ce93fb70ec3b640142b4942
        A/full-source-units.json: b1962377ffa7f68093a3efad5dcd2d1601da2abc10effa93e1b2db3893140aa5
        A/meta.json: 09bc86ac43725a52770bae79df70936b47cbd33d94be79a511f496a4a8f34d65
        A/table-images/TABLE-1-page-3-1.png: 49a6bc871ff346ae60272980dc02640bfe24eb5bb62b3f445695bf30775edb39
        A/table-images/page-3.png: 8342325bab650aca4a975d58b9b7ec3e0b257d40c34dc2344f31086f1cf443f0
        A/table-images/page-5.png: c54a8afec389654142a2e0b0ccda291a55d867f7f74a482a47b78d3ada286ce6
        A/table-images/page-4.png: fda3708de82022ef8c8b4aad946933a4891f56dc79a971c136428c5c765781c1
        A/table-images/manifest.json: b5bf1fd2c18807f99333682e539788b88b181044891477ac10fe06a2de4fba06
        A/table-images/TABLE-2-page-4-1.png: 1e7464c076d832ff573a4674a07b7d839e17f2964b1098938ee3a1cd0dd586a2
        A/table-images/TABLE-3-page-5-1.png: 28b3dce6210046016cb95f3394d11b746a2402bbf54e8ed987f6714e8b55f10a
        A/clauses/window-03/raw.json: 30137bcc8dfdf3d0cc7c3f7f59b629bb388c2603898387c5ca99046a2d3a46ce
        A/clauses/window-03/prompt.txt: 42e32cb3afd694194630d06dd323384865fd0705cb771f1126bc9dba973a1040
        A/clauses/window-03/meta.json: d3b594f951c92ce548fbd856ab760a13b229b76a9699b823a0a53c08a6ec4fcb
        A/clauses/window-04/raw.json: 6509e0a1ea0f3b6fe1603535d806ac8bb53187f4bae0a4064b1c90465636f126
        A/clauses/window-04/prompt.txt: a33f74cf6d22d1a2e4dfa8b8cf22670f08df5f2f36639b8fa63ff7ea30486fa9
        A/clauses/window-04/meta.json: 33a3647ca94f154c038f7e6768270ec0d4f5e2d783f8972b6b772977ed26d22e
        A/clauses/window-05/raw.json: da42c4c2018a6b5c5428f96f495d7808f3b87856b5c690db0ca7a76b5af09113
        A/clauses/window-05/prompt.txt: e6fc1b7effa10906acffb3d00ee77db5cb1a04fb77804e6b3ea6caaf62bebab8
        A/clauses/window-05/meta.json: 8d35620b33a0db4a8cae8bc9cd0bd8144f6f6c030d78023d96bf163adb642929
        A/clauses/window-02/raw.json: 5d552a280b2ffe70d6a03881788e0a9f15a2be3223d03e35bca6c9d8f69b1c1c
        A/clauses/window-02/prompt.txt: 22367a866810d2491fe4079c16abbc22794d987b63dfa17ba0d422b989eb0255
        A/clauses/window-02/meta.json: 224e0476554e2ebe2cc679637506d2feacc1f3a65ae2473c8510f743c91181e5
        A/clauses/window-07/raw.json: 2baf7910b9fe4614ca083fe07f9a25eedd224c92b46c15602bea9c89a5b3feeb
        A/clauses/window-07/prompt.txt: eeff17572b320d197920bd201df9a52b902b2d6ae557b7a1948c24fc6846bb62
        A/clauses/window-07/meta.json: a343c96ebc23a149685945c2aaebaeca205e3607e900524ea71965d8c02eba2c
        A/clauses/window-01/raw.json: feddb8827cd6d26e8598c125f24785576527daeb0c6218d399f16a10a5631e2f
        A/clauses/window-01/prompt.txt: 1a42a91b27a4b49651c220000cabc61b02749080bb74d9739370236ed7fde270
        A/clauses/window-01/meta.json: b57e5a1ef17f96faa9b0ebed62c11e9b084bb68572fafd67710b9d504a96063c
        A/clauses/window-06/raw.json: bcc3af19f3a64ad9137c37c66350c5b062a7ed189535c24dbef945d6ec48460d
        A/clauses/window-06/prompt.txt: 11d727388f3d5273f5db536286c4f83359ee364ff298fb5d5b8279b86fbef0f0
        A/clauses/window-06/meta.json: e06c9f40afaebcc3f47e5cf89721192571d640a996dcc5f19095b0b66fbe3e99
        A/tables/TABLE-3-page-5-3/raw.json: a05ce2c090363de3e76fd1917a5a7d021b930fc9927e63a4cd4bb449cd61ebaf
        A/tables/TABLE-3-page-5-3/prompt.txt: af824c94e2eea00b4adcc835f186788d89de5592fc9bdbf1956830b678204c97
        A/tables/TABLE-3-page-5-3/meta.json: dac3641996a5834ac78a7510534271d552ee9becbe6bf6b154012f5f74c98813
        A/tables/TABLE-1-page-3-1/raw.json: f6ae655fcadf1fd9b1f527300bb9ce570f31e52085d729e012d531c2a04d3011
        A/tables/TABLE-1-page-3-1/prompt.txt: bac684a8cb1687802cb188dd09c534c5e04677238ccecb9b8cb48a0698700664
        A/tables/TABLE-1-page-3-1/meta.json: 864baadd33f3c374f3096ddf05f44a8558441b7aab99527fe2154aca102d5492
        A/tables/TABLE-2-page-4-2/raw.json: acde9539cf94e749fc52392b44145f2328676a30b469ab5481d1c9e6e5b4bdbb
        A/tables/TABLE-2-page-4-2/prompt.txt: dc4275769a7f9cb77b7bf0e4feb421f1610eb15288d73c115c62d435582482e8
        A/tables/TABLE-2-page-4-2/meta.json: 16a338181d49015421d36a472bd61495952a0df38308d57bca3942e35e49b489
        B/passages.json: 62dc6d7d1e56e4f6c8864d804af73a1539d90b1aef1d7e5c7c908ee3fc4d7e87
        B/raw.json: 49dd7c46df2533fd445e3ebac7419545388625bb37c9123ee7f51fb6ac5f770f
        B/source-units.json: 3e888bdc1bc8588737e1dcf8de509490f6b475499ce93fb70ec3b640142b4942
        B/full-source-units.json: b1962377ffa7f68093a3efad5dcd2d1601da2abc10effa93e1b2db3893140aa5
        B/meta.json: 41ea0311e4c1ddcb827b87085f64d63de1c894fabd1dc33a9a0dcfd10bcca75f
        B/table-images/TABLE-1-page-3-1.png: 49a6bc871ff346ae60272980dc02640bfe24eb5bb62b3f445695bf30775edb39
        B/table-images/page-3.png: 8342325bab650aca4a975d58b9b7ec3e0b257d40c34dc2344f31086f1cf443f0
        B/table-images/page-5.png: c54a8afec389654142a2e0b0ccda291a55d867f7f74a482a47b78d3ada286ce6
        B/table-images/page-4.png: fda3708de82022ef8c8b4aad946933a4891f56dc79a971c136428c5c765781c1
        B/table-images/manifest.json: fcfbe0d67fe6aa7a23e8d9b40c733a649e196ac9d6cd7ae65782324723198476
        B/table-images/TABLE-2-page-4-1.png: 1e7464c076d832ff573a4674a07b7d839e17f2964b1098938ee3a1cd0dd586a2
        B/table-images/TABLE-3-page-5-1.png: 28b3dce6210046016cb95f3394d11b746a2402bbf54e8ed987f6714e8b55f10a
        B/clauses/window-03/raw.json: 03c0a30f7a11431159db86e6074e64270c48d8bf3f0174ac9683c17af1e134ae
        B/clauses/window-03/prompt.txt: 42e32cb3afd694194630d06dd323384865fd0705cb771f1126bc9dba973a1040
        B/clauses/window-03/meta.json: 8c426e2ebdc34279e2b2cae7791d6dbb87755140e50bf81566072c9266c1b419
        B/clauses/window-04/raw.json: 4e071570efc813acaa47d108fcdf1cdb84eb1a91ab52e2d009a15f4d83cf6026
        B/clauses/window-04/prompt.txt: a33f74cf6d22d1a2e4dfa8b8cf22670f08df5f2f36639b8fa63ff7ea30486fa9
        B/clauses/window-04/meta.json: f76197549cdd17f1de72703e90f9d35b16a0d3ea92f0e58b10cfa50bbbe1cdce
        B/clauses/window-05/raw.json: 6ae2bce0a1bf1b524e74b2634ee07f6bc97d448863fe44611231fe04b9133611
        B/clauses/window-05/prompt.txt: e6fc1b7effa10906acffb3d00ee77db5cb1a04fb77804e6b3ea6caaf62bebab8
        B/clauses/window-05/meta.json: 3595892919023811ab964672d183b81a157c29024ae90418ed82d5fdee659324
        B/clauses/window-02/raw.json: 0aadc3651394060425351a2348f7feae2ff09acba7f5fa2fd5edd4e7cf3d508e
        B/clauses/window-02/prompt.txt: 22367a866810d2491fe4079c16abbc22794d987b63dfa17ba0d422b989eb0255
        B/clauses/window-02/meta.json: eaf5cb3f16f3dd45086823fc263774ec5f65abbc8ca5fb13510ea5e1e702603d
        B/clauses/window-07/raw.json: 7c7e926f73173168a8599b7774c6e2f3a8738b26fa32a7ee0cb3ac29db43b515
        B/clauses/window-07/prompt.txt: eeff17572b320d197920bd201df9a52b902b2d6ae557b7a1948c24fc6846bb62
        B/clauses/window-07/meta.json: f321abcedbd80f38460e5ad9301ea1c4fd6f5651aedc4aa49012dfeb9bb30068
        B/clauses/window-01/raw.json: 1d77d169991499ad59cb4e07875d17fa7720eed6aea17a1dbf51277ca0a955ce
        B/clauses/window-01/prompt.txt: 1a42a91b27a4b49651c220000cabc61b02749080bb74d9739370236ed7fde270
        B/clauses/window-01/meta.json: f3b619fc9736f261b9c2160925d94929b3b03f185f6990318460d3e6b65c30a2
        B/clauses/window-06/raw.json: 0655b707c9a5d60895c61cacf66f88d165c473a6b6c2bc1adf1285e60248c90c
        B/clauses/window-06/prompt.txt: 11d727388f3d5273f5db536286c4f83359ee364ff298fb5d5b8279b86fbef0f0
        B/clauses/window-06/meta.json: 70d00bc48faa316d2e36460648d5ac3876ed72ad5b564392e754c49316278296
        B/tables/TABLE-3-page-5-3/raw.json: 65dbe11da6d89fb82f2aaef69c697465a1639330a5460a635ebbaee2b1499858
        B/tables/TABLE-3-page-5-3/prompt.txt: af824c94e2eea00b4adcc835f186788d89de5592fc9bdbf1956830b678204c97
        B/tables/TABLE-3-page-5-3/meta.json: aff0d95edcbbbac81e7d086fc4a18d5d95c0ee19156dbfc5d80621f505e5ad20
        B/tables/TABLE-1-page-3-1/raw.json: ee5ebc08efad034e9688ba5ea7de97cbfb3b2c8ccca43906d7598570ec40e222
        B/tables/TABLE-1-page-3-1/prompt.txt: bac684a8cb1687802cb188dd09c534c5e04677238ccecb9b8cb48a0698700664
        B/tables/TABLE-1-page-3-1/meta.json: 2476f0066c4781fd57a41bd0526a38123eb8fc0eeb559222c06b25a7f50979db
        B/tables/TABLE-2-page-4-2/raw.json: fc17a49cf19082c9327ed5ba66fe5c15ebe9eec2f99cacef4423659e391f80b3
        B/tables/TABLE-2-page-4-2/prompt.txt: dc4275769a7f9cb77b7bf0e4feb421f1610eb15288d73c115c62d435582482e8
        B/tables/TABLE-2-page-4-2/meta.json: a70748b291062d93fa38ddc6c5e123697f3f38d0c9b4254da0fa1e9fdfaae615
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
      pdf_sha256: 0b1cc78748f5f745c2e71127f56abbd32d3406925ae47b768f87f28ab874378a
      source_review: _compare/relationships-2026-11-16/review-current/Wilmskoetter2021
      source_status_sha256: 474169038155498e684cbbc4c1909e73579028119daa99f6b4196ab829b881db
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R009
    exposure:
      text: number of steps along indirect connections between AG and MTG
    outcome:
      text: increase in correct naming responses after treatment
    analysis_label: Multivariable linear regression for AG-MTG indirect connections
    relation: association
    evidence_ids:
    - P6-S1-C11
    - P8-S1-C4
    - P8-S1-C5
    qualifier_ids:
    - P5-S2-C7
    - P5-S2-C8
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 0b1cc78748f5f745c2e71127f56abbd32d3406925ae47b768f87f28ab874378a
      source_review: _compare/relationships-2026-11-16/review-current/Wilmskoetter2021
      source_status_sha256: 474169038155498e684cbbc4c1909e73579028119daa99f6b4196ab829b881db
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Accounting without a linked unit P5-S1-C4
      - Accounting without a linked unit P5-S1-C5
      - Accounting without a linked unit P5-S1-C9
      - Result passage disposed without unit P5-S2-C6
      - Unaccounted source passage P5-S1-C4
      - Unaccounted source passage P5-S1-C9
      - Unaccounted source passage P5-S1-C5
      - Result passage disposed without unit P5-S3-C1
      - Result passage disposed without unit P6-S1-C10
      - Accounting without a linked unit P6-S1-C4
      - Accounting without a linked unit P6-S1-C5
      - Accounting without a linked unit P6-S1-C6
      - Accounting without a linked unit P6-S1-C7
      - Accounting without a linked unit P6-S1-C8
      - Accounting without a linked unit P6-S1-C9
      - Unaccounted source passage P6-S1-C8
      - Unaccounted source passage P6-S1-C9
      - Unaccounted source passage P6-S1-C4
      - Unaccounted source passage P6-S1-C7
      - Unaccounted source passage P6-S1-C5
      - Unaccounted source passage P6-S1-C6
      - Result passage disposed without unit P6-S1-C13
      - Result passage disposed without unit P6-S2-C2
      - Result passage disposed without unit P7-S1-C1
      - Result passage disposed without unit P7-S2-C6
      - Result passage disposed without unit P7-S2-C9
      - Result passage disposed without unit P7-S2-C11
      - Result passage disposed without unit P8-S1-C11
      - Result passage disposed without unit P8-S1-C12
      - Result passage disposed without unit P8-S1-C14
      - Result passage disposed without unit P8-S1-C4
      - Accounting without a linked unit P8-S1-C5
      - Accounting without a linked unit P8-S1-C6
      - Unaccounted source passage P8-S1-C5
      - Unaccounted source passage P8-S1-C6
      - Result passage disposed without unit P8-S1-C15
      - Unresolved source passage P8-S2-C10
      - Result passage disposed without unit P8-S2-C5
      - Result passage disposed without unit P8-S3-C9
      - Result passage disposed without unit P9-S1-C1
      unattached_null_or_qualifier_ids:
      - P5-S1-C9
      - P6-S1-C4
      - P6-S1-C10
      - P7-S2-C6
      - P7-S2-C9
      - P8-S1-C6
      suppressed_nonrepresented_units: 11
      default_disposition_count_requires_completeness_check: 141
      unselected_timing_passages:
      - P1-S2-C8
      - P2-S3-C8
      - P3-S1-C1
      personal_effect_slots_without_result_classification: []
      held_frame_selections: []
      empty_frame_slots_require_confirmation:
      - personal_factors
      - tested_personal_effects
      unclassified_extraction_ids:
      - P3-S1-C11
      table_review_required:
      - TABLE-1-page-3-1
      - TABLE-2-page-4-2
      - TABLE-3-page-5-3
      unlinked_tables:
      - TABLE-1-page-3-1
      - TABLE-2-page-4-2
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness. Figures are not automatically interpreted.
        caption_candidate_units:
        - P3-S1
        - P3-S2
        - P4-S2
        - P4-S3
        - P6-S1
        - P6-S2
        - P7-S2
      approval: Not performed. Structural checks and model selections do not establish semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 0b1cc78748f5f745c2e71127f56abbd32d3406925ae47b768f87f28ab874378a
      source_review: _compare/relationships-2026-11-16/review-current/Wilmskoetter2021
      source_status_sha256: 474169038155498e684cbbc4c1909e73579028119daa99f6b4196ab829b881db
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S2-C11
      disposition: repeated
      result_indexes:
      - 0
      reason: Abstract restatement of IFGop-AG connection results.
    - source_id: P1-S2-C12
      disposition: repeated
      result_indexes:
      - 4
      - 5
      reason: Abstract restatement of IFGop-MTG interaction results.
    - source_id: P1-S2-C14
      disposition: repeated
      result_indexes:
      - 0
      reason: Abstract conclusion regarding indirect connections and naming improvement.
    - source_id: P5-S1-C4
      disposition: represented
      result_indexes:
      - 10
      reason: Establishes association between lesion volume and connection type.
    - source_id: P5-S1-C5
      disposition: represented
      result_indexes:
      - 10
      reason: Details the direction of the lesion volume and connection type relationship.
    - source_id: P5-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes multicollinearity and covariate selection process.
    - source_id: P5-S2-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes correlation coefficients for multicollinearity check.
    - source_id: P5-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports Levene's test for equality of variance.
    - source_id: P5-S2-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Introduces the results section for naming recovery.
    - source_id: P5-S3-C1
      disposition: represented
      result_indexes:
      - 0
      - 2
      reason: Specifies the adjustment for control variables in the ANCOVA.
    - source_id: P5-S3-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports non-significant interaction and control variables for IFGop-AG.
    - source_id: P5-S3-C3
      disposition: represented
      result_indexes:
      - 0
      reason: Reports significant differences between direct/indirect and no connections for IFGop-AG.
    - source_id: P5-S3-C4
      disposition: represented
      result_indexes:
      - 0
      reason: Provides mean difference in correct responses for IFGop-AG.
    - source_id: P6-S1-C1
      disposition: represented
      result_indexes:
      - 0
      reason: Provides mean difference for indirect connections in IFGop-AG.
    - source_id: P6-S1-C2
      disposition: represented
      result_indexes:
      - 1
      reason: Reports null difference between direct and indirect connections for IFGop-AG.
    - source_id: P6-S1-C3
      disposition: represented
      result_indexes:
      - 2
      reason: Reports A-tDCS effect size and significance.
    - source_id: P6-S1-C4
      disposition: represented
      result_indexes:
      - 3
      reason: Reports significant interaction for IFGop-MTG.
    - source_id: P6-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: States other independent variables were not significant.
    - source_id: P6-S1-C6
      disposition: represented
      result_indexes:
      - 4
      - 5
      reason: Identifies the two groups showing significant improvement for IFGop-MTG.
    - source_id: P6-S1-C7
      disposition: represented
      result_indexes:
      - 4
      reason: Reports improvement for direct connections + S-tDCS (IFGop-MTG).
    - source_id: P6-S1-C8
      disposition: represented
      result_indexes:
      - 5
      reason: Reports improvement for indirect connections + A-tDCS (IFGop-MTG).
    - source_id: P6-S1-C9
      disposition: represented
      result_indexes:
      - 6
      reason: Reports null results for other IFGop-MTG group combinations.
    - source_id: P6-S1-C10
      disposition: represented
      result_indexes:
      - 7
      reason: Reports null main effects/interactions for AG-MTG.
    - source_id: P6-S1-C11
      disposition: represented
      result_indexes:
      - 8
      reason: Reports predictive value of fewer steps for AG-MTG.
    - source_id: P6-S1-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the anatomical path of indirect connections.
    - source_id: P6-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the anatomical path of indirect connections.
    - source_id: P7-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about relationships between naming and indirect connections.
    - source_id: P7-S1-C2
      disposition: represented
      result_indexes:
      - 0
      reason: Restates improvement for indirect connections (IFGop-AG).
    - source_id: P7-S1-C3
      disposition: represented
      result_indexes:
      - 0
      reason: Restates improvement for direct connections (IFGop-AG).
    - source_id: P7-S1-C6
      disposition: represented
      result_indexes:
      - 1
      reason: Restates no difference between direct and indirect connections (IFGop-AG).
    - source_id: P7-S2-C4
      disposition: represented
      result_indexes:
      - 2
      reason: Restates treatment type as independently predictive.
    - source_id: P7-S2-C5
      disposition: represented
      result_indexes:
      - 2
      reason: Restates A-tDCS superiority over S-tDCS.
    - source_id: P7-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discusses the conditions under which the treatment effect was observed.
    - source_id: P7-S2-C9
      disposition: represented
      result_indexes:
      - 3
      reason: Restates the significant interaction for IFGop-MTG.
    - source_id: P7-S2-C10
      disposition: represented
      result_indexes:
      - 4
      reason: Restates best gains for S-tDCS with direct connections (IFGop-MTG).
    - source_id: P7-S2-C11
      disposition: represented
      result_indexes:
      - 5
      reason: Restates best gains for A-tDCS with indirect connections (IFGop-MTG).
    - source_id: P8-S1-C4
      disposition: represented
      result_indexes:
      - 8
      reason: Restates association between AG-MTG steps and recovery.
    - source_id: P8-S1-C5
      disposition: represented
      result_indexes:
      - 8
      reason: Specifies that fewer steps predict more correct responses (AG-MTG).
    - source_id: P8-S1-C6
      disposition: represented
      result_indexes:
      - 9
      reason: Reports null association for IFGop-AG and IFGop-MTG steps.
    - source_id: P9-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion statement.
    unresolved_coverage:
    - source_id: P7-S3-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S1-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S1-C12
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S1-C14
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S1-C15
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S2-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S3-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S2-C11
    - P1-S2-C12
    - P1-S2-C14
    - P5-S1-C9
    - P5-S2-C1
    - P5-S2-C6
    - P5-S2-C12
    - P5-S3-C2
    - P5-S3-C4
    - P6-S1-C5
    - P6-S1-C6
    - P6-S1-C13
    - P6-S2-C2
    - P7-S1-C1
    - P7-S2-C6
    - P7-S3-C3
    - P8-S1-C11
    - P8-S1-C12
    - P8-S1-C14
    - P8-S1-C15
    - P8-S2-C5
    - P8-S3-C9
    - P9-S1-C1
    pending_policy: Every result passage without direct candidate evidence remains pending, including model-labelled background and restatements; those labels never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-3-1
    - TABLE-2-page-4-2
    - TABLE-3-page-5-3
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P3-S1-C1
      recruited_sample:
      - P3-S1-C1
      eligibility:
      - P3-S1-C1
      imaging_provenance:
      - P4-S1-C1
      imaging_timing:
      - P3-S1-C10
      outcome_timing:
      - P3-S1-C7
      outcome_definition:
      - P3-S1-C8
      validation:
      - P4-S1-C8
      analysis_restrictions:
      - P4-S1-C4
      dependent_variable_statement:
      - P5-S1-C8
      - P5-S2-C7
      limitations:
      - P8-S3-C3
      - P8-S3-C5
      - P8-S3-C6
      - P8-S3-C7
      - P8-S3-C8
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P5-S1-C8
      - P5-S1-C9
      - P5-S2-C8
      explicitly_not_adjusted:
      - P5-S1-C9
      descriptive_personal_factors:
      - P3-S2-C6
      - P3-S1-C5
    outcome_type: change_from_baseline
    imaging_vs_outcome: precedes_outcome
    validation_type: none_described
    held_selections: []
    policy: All slots and enums remain unverified. Held selections are not evidence of absence. Original response is preserved in frame/raw.json.
  approved: false
  source_check:
    profile: agent-repair
    scope: Agent corrected this draft against the original paper. The original automated attempt is retained as historical provenance and does not verify this revised version. Human PDF review and approval remain required. Analysis restricted to participants with an indirect AG-MTG connection, not the full cohort.
    binding:
      source_pdf_sha256: 0b1cc78748f5f745c2e71127f56abbd32d3406925ae47b768f87f28ab874378a
      original_source_sha256: b171ad7d8835a8f50718a6d90383ba273982810d5161b66a810e05574949e5b9
      repair_audit: logs/publication/draft-repairs-2026-11-26.json
      agent_repair_approved: false
    approved: false
    pending_details:
    - Detailed statistics, atlas/reference-space and structured confounder metadata not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Specific confidence intervals for the regression coefficient
    - Exact sample size of the subgroup with indirect AG-MTG connections
    normalizations: []
    analysis_identity:
      id: R009
      exposure:
        text: number of steps along indirect connections between AG and MTG
      outcome:
        text: increase in correct naming responses after treatment
      analysis_label: Multivariable linear regression for AG-MTG indirect connections
      relation: association
      evidence_ids:
      - P6-S1-C11
      - P8-S1-C4
      - P8-S1-C5
      qualifier_ids:
      - P5-S2-C7
      - P5-S2-C8
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 0b1cc78748f5f745c2e71127f56abbd32d3406925ae47b768f87f28ab874378a
        source_review: _compare/relationships-2026-11-16/review-current/Wilmskoetter2021
        source_status_sha256: 474169038155498e684cbbc4c1909e73579028119daa99f6b4196ab829b881db
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P3-S1-C1:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 0b1cc78748f5f745c2e71127f56abbd32d3406925ae47b768f87f28ab874378a
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: a3086828ae60dad221df3f3c78264cf0762aa9226d5695634352a9ea02133fa4
          exclusions_sha256: 669552c39077462d53e9771cf5cb47525028239382ada3a3977adfd7717d21a5
          source_id: P3-S1-C1
          page: 3
          text_layer_sha256: 7e979916a23eefda7ab07cc650c1998b4b6d324981fac0102900ad410b1e666f
          models: &id001
          - gemma4:31b
          - qwen3.8:27b
          model_digests: &id002
          - 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
          - 47951e4a666180bc2aedfc93c169472f2de783696fe196efbf063f5730ecf163
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "\n348\t\nNeurorehabilitation and Neural Repair 35(4)\nclinical trial evaluating the use of tDCS for aphasia treat-\nment conducted at the University of South Carolina and the \nMedical University of South Carolina.25 We included 69 of \n74 participants from the clinical trial (excluding partici-\npants with hemorrhagic stroke [N = 2], no diffusion tensor \nimaging [N = 2], no posttreatment follow-up [N = 1])."
        anchor_text: "clinical trial evaluating the use of tDCS for aphasia treat-\nment conducted at the University of South Carolina and the \nMedical University of South Carolina.25 We included 69 of \n74 participants from the clinical trial (excluding partici-\npants with hemorrhagic stroke [N = 2], no diffusion tensor \nimaging [N = 2], no posttreatment follow-up [N = 1])."
        excluded_fragments:
        - where: leading
          text: "348\t"
          furniture_line: "348\t"
          bbox:
          - 48.0
          - 39.5
          - 65.8
          - 51.2
          rule: repeated margin line
        - where: leading
          text: Neurorehabilitation and Neural Repair 35(4)
          furniture_line: Neurorehabilitation and Neural Repair 35(4)
          bbox:
          - 371.0
          - 39.5
          - 540.0
          - 51.1
          rule: repeated margin line
        image_sha256: ec0985e099e10af21fc5f359f80a9c2640ededf22ea540b2473ebf98831f91f7
        transcription: clinical trial evaluating the use of tDCS for aphasia treatment conducted at the University of South Carolina and the Medical University of South Carolina.²⁵ We included 69 of 74 participants from the clinical trial (excluding participants with hemorrhagic stroke [N = 2], no diffusion tensor imaging [N = 2], no posttreatment follow-up [N = 1])
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
    publication_correction:
      date: '2026-11-26T00:24:06.569756+00:00'
      by: agent:source-repair
      approved: false
      human_verification_required: true
      original_source_sha256: b171ad7d8835a8f50718a6d90383ba273982810d5161b66a810e05574949e5b9
      source_pdf_sha256: 0b1cc78748f5f745c2e71127f56abbd32d3406925ae47b768f87f28ab874378a
      pdf_pages:
      - 4
      - 5
      - 6
      note: Analysis restricted to participants with an indirect AG-MTG connection, not the full cohort.
      audit: logs/publication/draft-repairs-2026-11-26.json
    checked_by: agent:source-repair (human approval pending)
    date: '2026-11-26'
    corrections:
    - Analysis restricted to participants with an indirect AG-MTG connection, not the full cohort.
    original_scope: Independent model text review of core meaning; not human approval or complete PDF verification
    original_core_review:
      own_result_source_ids:
      - P6-S1-C11
      - P8-S1-C4
      - P8-S1-C5
      source_result: Among participants with indirect connections, fewer steps along the indirect connection between the AG and MTG significantly predicted an increase in correct naming responses after treatment (standardized beta = -0.517, P = .012). This association was not found for IFGop-AG or IFGop-MTG pairs.
      result_status: detected
      patient_measurement: patient_diffusion
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis corresponds to Hypothesis 2, a multivariable linear regression on participants with indirect connections testing the number of steps between AG and MTG against naming change. The source explicitly identifies this analysis and its result.
          source_ids:
          - P5-S2-C7
          - P6-S1-C11
          - P8-S1-C4
        direction:
          answer: fits
          reason: The source states that 'fewer steps... significantly predicted an increase in correct naming responses' (P6-S1-C11, P8-S1-C5). The proposed claim preserves this direction (fewer steps -> better outcome).
          source_ids:
          - P6-S1-C11
          - P8-S1-C5
        construct:
          answer: fits
          reason: The exposure is correctly identified as the number of steps along indirect connections between AG and MTG. The outcome is the change in correct naming responses (Philadelphia Naming Test). The method is correctly described as using probabilistic tractography to calculate propagation steps on the whole-brain connectome. The patient measurement is patient_diffusion because the connectome and propagation steps are derived from individual DTI data, not just template overlap.
          source_ids:
          - P4-S1-C3
          - P4-S1-C6
          - P4-S1-C8
          - P3-S1-C7
          - P6-S1-C11
        qualifications:
          answer: fits
          reason: The draft correctly includes the restriction to participants with indirect connections (P5-S2-C7), the control variables (P5-S2-C8), and the lack of association for other ROI pairs (P8-S1-C6). It also includes relevant limitations regarding structural vs functional connectivity and generalizability.
          source_ids:
          - P5-S2-C7
          - P5-S2-C8
          - P8-S1-C6
          - P8-S3-C3
          - P8-S3-C8
        missing_material_caveat:
          answer: fits
          reason: 'The draft includes the key limitations mentioned in the source: structural connectomics does not prove functional use (P8-S3-C3), binarization of lesions (P8-S3-C5), and limited generalizability to other language aspects (P8-S3-C8). No material caveats are omitted that would change the interpretation of the specific AG-MTG finding.'
          source_ids:
          - P8-S3-C3
          - P8-S3-C5
          - P8-S3-C8
      optional_pending:
      - Specific confidence intervals for the regression coefficient
      - Exact sample size of the subgroup with indirect AG-MTG connections
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    original_profile: core
    original_binding:
      profile: core
      version: core-source-check-v3
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      checker_model: qwen3.8:27b
      checker_digest: 47951e4a666180bc2aedfc93c169472f2de783696fe196efbf063f5730ecf163
      host: http://localhost:11434
      pdf_sha256: 0b1cc78748f5f745c2e71127f56abbd32d3406925ae47b768f87f28ab874378a
      review_sha256: 2e72ce2da0fd23b5fb9c83abb043c54f924a9e4fcc9de0368d7e042afd215acd
      code_sha256: c4650d24fa3e36e6f317cb65cc7626277a28936a7cdf5d07248d4b1e5bfa09aa
      source_helpers_sha256: e0e0f295e5efa1fdb4e9e8c84ca491d062df3aefe8ca8b4d9ca85fcb6d4c9082
      converter_sha256: 048f1e35905528676837a00b1b2406b1c97cb1eb47c48d63f121a5c00cc0afeb
      table_helpers_sha256: 78e562e9725fc484d6a12279ea710856dfd1d9aa13ee178d0358e9c0acdd2c8c
      mapper_budget: 2500
      reviewer_budget: 1600
      approved: false
      visual:
        models: *id001
        digests: *id002
        code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
        layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
reviewer_marks:
- id: relationship-source-check
  page: 6
  quote: "Fewer Steps Along Indirect Connections Predict \nBetter Treated Naming Recovery\nFor those participants with indirect connections, fewer \nsteps along the indirect connection between the AG and \nMTG significantly predicted an increase in correct naming \nresponses after treatment (standardized beta = −0.517, \nP = .012)."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-26'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor roles, all qualifiers, source audit issues and main-PDF tables/figures; check missing results. This model proposal is not verified.'
- id: publication-source-repair-2026-11-26
  status: pending
  by: agent:source-repair
  date: '2026-11-26'
  note: Analysis restricted to participants with an indirect AG-MTG connection, not the full cohort. Original automated review applies to the original version; verify the corrected finding against the cited pages before approval.
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
