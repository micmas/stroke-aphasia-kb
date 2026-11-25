---
id: left_fronto_temporo_parietal_cluster
name: left fronto-temporo-parietal cluster
kind: network
findings:
- id: f1
  outcome_measurement:
    status: needs_source_review
    instruments: []
    note: Outcome instrument/task is not yet verified for this finding. Do not infer it from the predictor
      or a paper-wide test list.
  target_audit:
    status: behaviour_label_present
    category: behaviour_or_language_construct
    original_target: aphasia
    reason: Label names a behaviour or language construct; its exact operational definition and measurement
      still need source review.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  target: aphasia
  target_kind: impairment
  claim: Regions associated with aphasia, assessed with the NIHSS subscale, were predominantly
    left-lateralized and located in the fronto-temporo-parietal regions.
  direction: likely
  relationship: correlational
  method: LSM
  sample:
    n: 522
    population: patients aged 18–49 years with first-ever ischemic stroke
    phase: not_reported
    time_post_onset: aphasia assessed at discharge; cognitive assessments performed
      at a median of 83 days post-stroke
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Underrepresentation of patients with severe language impairment may have attenuated
    associations with language-related brain regions
  - Sensitivity analysis adjusting for lesion volume resulted in no significant clusters
    for language
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Patient lesion overlap with a data-driven cluster
    in the left fronto-temporo-parietal regions, identified via multivariate lesion-symptom
    mapping (SCCAN). The association was identified using multivariate lesion-symptom
    mapping (SCCAN) with a cluster-size threshold of 150 voxels. Additional metadata
    has not been transcribed; review the pending-field flags before approval. PDF
    image reading (P3-S4-C14, two-model agreement, human verification pending): Results


    Of the 1,322 patients included in the ODYSSEY study with an ischemic stroke, 522
    ischemic stroke patients were included in this analysis, see Fig. 1 for a flowchart
    of the study population Original text-layer quotation is preserved below. PDF
    image reading (P1-S2-C4, two-model agreement, human verification pending): .

    Methods: We conducted a multicenter prospective cohort study between 2013 and
    2021, enrolling patients aged

    18–49 years with first-ever ischemic stroke and a visible stroke lesion on MRI
    Original text-layer quotation is preserved below. PDF image reading (P4-S1-C4,
    two-model agreement, human verification pending): . Median time from index event
    to cognitive assessment was

    83 days (IQR 56–119) Original text-layer quotation is preserved below.'
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
    - proposed_concept:aphasia
  citation: '@Schellekens2026'
  source_passages:
  - section: Original source P5-S1-C10
    page: 5
    quote: "Finally, regions associated with aphasia, \nassessed with the NIHSS subscale,\
      \ were predominantly left-lateralized \n(r = 0.626, p < 0.001, optimal sparseness\
      \ = -0.456), and located in \nthe fronto-temporo-parietal regions.\n5."
    supports: claim
  - section: Original source P3-S2-C9
    page: 3
    quote: "Multivariate lesion-symptom mapping\nWe performed multivariate LSM using\
      \ the spare canonical correla­\ntion analysis (SCCAN) as implemented in the\
      \ LESYMAP package \n(version: 0.0.0.9222) in R (Team RC)."
    supports: method
  - section: Original source P3-S3-C12
    page: 3
    quote: "We performed separate multi­\nvariate LSMs for the presence of a major\
      \ VCD, Z-score of each cognitive \ndomain, and aphasia assessed by the NIHSS\
      \ language subscale at \ndischarge."
    supports: method
  - section: Original source P3-S4-C14
    page: 3
    quote: "Results\nOf the 1,322 patients included in the ODYSSEY study with an \n\
      ischemic stroke, 522 ischemic stroke patients were included in this \nanalysis,\
      \ see Fig. 1 for a flowchart of the study population."
    supports: sample
  - section: Original source P1-S2-C4
    page: 1
    quote: "Methods: We conducted a multicenter prospective cohort study between 2013\
      \ and 2021, enrolling patients aged \n18–49 years with first-ever ischemic stroke\
      \ and a visible stroke lesion on MRI."
    supports: sample
  - section: Original source P4-S1-C4
    page: 4
    quote: "Median time from index event to cognitive assessment was \n83 days (IQR\
      \ 56–119)."
    supports: sample
  - section: Original source P5-S2-C2
    page: 5
    quote: "After adjusting the cognitive outcomes for \nlesion volume, no significant\
      \ clusters were observed for VCD, visual \nneglect, or language, while the results\
      \ for other cognitive domains \nremained essentially similar."
    supports: limitation
  - section: Original source P8-S3-C12
    page: 8
    quote: "The underrepresentation of patients \nwith a severe language impairment\
      \ may have attenuated associations \nwith language-related brain regions, potentially\
      \ underestimating find­\nings related to language deficits."
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-25'
relationship_review:
  paper: Schellekens2026
  proposal_id: R009
  review_status_sha256: b9501e4d35b53856ff40b6854492e1cad263cc3b5a3d1f52b3a6bb9cb427e3e6
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 7570f761aaaf1c9cc476c7a77340fe8a212c1c335b17f076cdec383184722fb9
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 7570f761aaaf1c9cc476c7a77340fe8a212c1c335b17f076cdec383184722fb9
        A/passages.json: e9cef16f0a2fc79962f750c6d3d171420284fb5022210e0d7d6ab46bb89187ca
        A/raw.json: 573f86e21d8f9603aa2aa06f3d663811155f0d958aec901190b7f6527b554fd1
        A/source-units.json: 9192e9f2f0058ccea09330a78358f9f76343013667882613456d2fd5b3fadf57
        A/full-source-units.json: 9724cbde4a178a1f6691bd4a83585b121c3412ed73e3d32687c9177a01d50f01
        A/meta.json: 1fa494c013231dd7180370e6969bbf23aa3bc440e414ef7430acfd8fb254302e
        A/table-images/TABLE-1-page-5-1.png: 316b4b0ef5fadf3ff9bf0e1ccc807960735d38449abbe5d3f7a4aaa2847a447d
        A/table-images/page-5.png: 7c03a7a0c3238e0f288a45655fbb5faa6b07bc47b9e625300ad4a0b6cd30752b
        A/table-images/manifest.json: ca59055ca9f30ac6bc058fc63af13fb15a661ce3cbacd2f75c69fbd60c4c2b07
        A/table-images/TABLE-2-page-5-2.png: 87794b6e7d9dca7f69ebd54629c88e9eb7f0a2000c4578be8c50d4c6a899ad45
        A/clauses/window-11/raw.json: 433ff56d97414b4af151ca6d96e8eb42f8d3067058381a4336b95171d5f17ab5
        A/clauses/window-11/prompt.txt: bfddc7b0e5cac2fc64a618a313e7eb07d956ff6fde407175049abedcba0cb876
        A/clauses/window-11/meta.json: 888bb5681ac08ce7fa68970bc77756fbb0eeea8111078833c6d9e93c9e9e8eec
        A/clauses/window-10/raw.json: fa51296d7d2b094a629bc8c555c3c2c6933be94ed830cf86ba713b402f3c4619
        A/clauses/window-10/prompt.txt: 8e82ffcb889360af9fe6335b6240a75bfe93f86a99b1f777c0426967f657bbfb
        A/clauses/window-10/meta.json: b318a6a4d42d8da36cfb77451fd0b3873d84735ff9411b2b4d8094c64ccaa4b7
        A/clauses/window-03/raw.json: e8e31548cef70e9a6a35efcf2902ea98640f690f5bd2b7ad3640a346c2de5e30
        A/clauses/window-03/prompt.txt: 421172dfb2677038a4717c64c8bfcd95800bcb004dae366fefd785ee3f00d423
        A/clauses/window-03/meta.json: 6de0ac301f21150d37f9e85601d4b532de08b8f14bcdcf0f3e890cb787a5524e
        A/clauses/window-04/raw.json: 980b9919e26cb36ad2ab065053c5c79976c05b60f59ecc7c214bfc53a1abebcf
        A/clauses/window-04/prompt.txt: 53fa79fb88e500c0b01a067832beef2e3fa39dfe7b49b8adca9c85e8dbe2196c
        A/clauses/window-04/meta.json: ccf13a5ec76d3c234d2a59c1dabb9b7e77018f9629ede93a991fe90e405c9a9c
        A/clauses/window-05/raw.json: 5b7da416c72d24964452fbde7c4dc9406050ff3f1fb3ad1c04d588a3edb8976d
        A/clauses/window-05/prompt.txt: df70256608314478d3f190d804936ce274eef5d6a707785d6dfffb3e487fc4ac
        A/clauses/window-05/meta.json: 3506693a18c872ec7ac7bdd0b31ff78528d4433b7e7fc76fbe5f8c72708c96e6
        A/clauses/window-02/raw.json: 882ccc4c414d83dfd21ba15e55ca78d93b74b54737f41891ac66314ffc0e7c76
        A/clauses/window-02/prompt.txt: c354e642b88d72b7a6c20d0068de324fbbff38cc3c92f8768fb467fcdb0686fe
        A/clauses/window-02/meta.json: 9cda4e6c04fc2fd67317a6cf613a9803d35c325c38ac85bb0adb0c1fa9752bb2
        A/clauses/window-09/raw.json: cabffc051c1a5d08b97a10a39846d97a827563fc33f79a1f9757dd53624756f4
        A/clauses/window-09/prompt.txt: e3c1ac4ef83cae7ee2b5d564c07475869d811f07c223e5fb340eeced531f7908
        A/clauses/window-09/meta.json: 31c187a5dd9641d132944ba6672c37e21b4f1d126e299f73987a2b043d51d96a
        A/clauses/window-07/raw.json: 97d39e964e7ace6abf050085a4a6ccb8a19271cd208c502348fd3998ee2a19a7
        A/clauses/window-07/prompt.txt: cdb0995ec64d5e423bcbf196adece601969f7bf0f362b4f9b99bf9cedece4ffe
        A/clauses/window-07/meta.json: 95382e76f8eef85e42780b3773c7c2e2a256b082ce46e6166e5011f67415cdc2
        A/clauses/window-01/raw.json: a2fcf55684083f531892fd1db1d7e61bb64b59ed5f6e1a3e66f513079a64a6c6
        A/clauses/window-01/prompt.txt: cde7c3135d76a81f0bc2211f615f2725dc60c282ac67e3a105df5b954d661d45
        A/clauses/window-01/meta.json: 39b1be659e56b64630690ea7b39bff05c8bcbcc32379cb5232747b9300943851
        A/clauses/window-06/raw.json: 0961df7ccc3d26662a5e29bff7983a3b0f9042cc1dbf233379d9feb91ce66b8a
        A/clauses/window-06/prompt.txt: 9a8df08de78a33b2e6da1cae57df82f0ef6519427364af05d33f2700fc9cbd73
        A/clauses/window-06/meta.json: 831b969ce98219961d07247b41e74d42f04420bee85381685fbfab1f95334a80
        A/clauses/window-08/raw.json: 93b220820936d1a41fed5a6a151e712d98974f7e7098940ad38afc5788e25845
        A/clauses/window-08/prompt.txt: 6b7a39ec55a213370827890e688ff0a8764f14062a3533edaa738a815ea519b7
        A/clauses/window-08/meta.json: 0042d39d4463f517a09c9f4fa6cca296d79982d67210ce32711f718efc62b2f1
        A/tables/TABLE-1-page-5-1/raw.json: 6fd8092159e92294a111ef50461fc6266bb58bda6d169ca8ea0f2f942a685c0c
        A/tables/TABLE-1-page-5-1/prompt.txt: e8e4b5d6155837c48a30eaa43da339656a8df08a09da7a9c0c17e9c84ac86091
        A/tables/TABLE-1-page-5-1/meta.json: e2f0da8861e2ddc2f64419a0118581b0bc4bf12c173a43af1c5e7eece1162a0d
        A/tables/TABLE-2-page-5-2/raw.json: 2b18a73f857556bf2ed490d78c8d0eacd59841c6863a61cb17f1fdff5c3d26e1
        A/tables/TABLE-2-page-5-2/prompt.txt: cf17295399aad93036970cdad5e22054046d16f3332cb4afb549d8d3a4d35c5c
        A/tables/TABLE-2-page-5-2/meta.json: 2332b287a55415f10ca30b105f8fae6d884b8062c26e781dedd4c5a9c652d698
        B/passages.json: e9cef16f0a2fc79962f750c6d3d171420284fb5022210e0d7d6ab46bb89187ca
        B/raw.json: b85a61ed905adbd61f9ce095cab9d894945a02f454ab57f1d3f5104a32d4b001
        B/source-units.json: 9192e9f2f0058ccea09330a78358f9f76343013667882613456d2fd5b3fadf57
        B/full-source-units.json: 9724cbde4a178a1f6691bd4a83585b121c3412ed73e3d32687c9177a01d50f01
        B/meta.json: 7c55f675dffbf836fbd0b3cead84bf6ef081e68c4dadc20b97bf6c407ee8b6eb
        B/table-images/TABLE-1-page-5-1.png: 316b4b0ef5fadf3ff9bf0e1ccc807960735d38449abbe5d3f7a4aaa2847a447d
        B/table-images/page-5.png: 7c03a7a0c3238e0f288a45655fbb5faa6b07bc47b9e625300ad4a0b6cd30752b
        B/table-images/manifest.json: e4456afd13fefa5c0e6ffa092d2dc13b51651f69211610e2e6bb8a92edacd367
        B/table-images/TABLE-2-page-5-2.png: 87794b6e7d9dca7f69ebd54629c88e9eb7f0a2000c4578be8c50d4c6a899ad45
        B/clauses/window-11/raw.json: 433ff56d97414b4af151ca6d96e8eb42f8d3067058381a4336b95171d5f17ab5
        B/clauses/window-11/prompt.txt: bfddc7b0e5cac2fc64a618a313e7eb07d956ff6fde407175049abedcba0cb876
        B/clauses/window-11/meta.json: e5085cd74f1cbeddd9573f26376eed2b3b86e103db209a048ad9388e06d974f1
        B/clauses/window-10/raw.json: 165789951765543d0ad874a803b5445a14de9b645ebe495cb6f4638132862f7c
        B/clauses/window-10/prompt.txt: 8e82ffcb889360af9fe6335b6240a75bfe93f86a99b1f777c0426967f657bbfb
        B/clauses/window-10/meta.json: 468fc9fb79c7dcdd43f4445aec4c6222ee58991965dd69c4848df44c23c86291
        B/clauses/window-03/raw.json: 44b9d88a57ad70a9fe9110661e72c0e688826629f6313f116a8ab4f99a870f2c
        B/clauses/window-03/prompt.txt: 421172dfb2677038a4717c64c8bfcd95800bcb004dae366fefd785ee3f00d423
        B/clauses/window-03/meta.json: 24349afb169296f6185d3837a32bcd64a21732aa5eb993fb0b1a0559400390b5
        B/clauses/window-04/raw.json: 2010a860973fd717614cf60014fc92f446f5a68ed55cf3957fbbd911e232994a
        B/clauses/window-04/prompt.txt: 53fa79fb88e500c0b01a067832beef2e3fa39dfe7b49b8adca9c85e8dbe2196c
        B/clauses/window-04/meta.json: 6af28e2528f0918f14b577577f1d5645f0a529354f8487e9ebcbd73b9f424c37
        B/clauses/window-05/raw.json: e2a65284c8bf5df90cd6e603384baa3f426cef6b5d992944673b6db1fc65c2fe
        B/clauses/window-05/prompt.txt: df70256608314478d3f190d804936ce274eef5d6a707785d6dfffb3e487fc4ac
        B/clauses/window-05/meta.json: c4744c71a5a19bd77d72ab89e7786b0c68976426d546e73f2a57296c33ed2e0f
        B/clauses/window-02/raw.json: 3af9e9b11e0f93c5bbf17b3d5865fa78f3c8d608238e56707561955b1cd5f477
        B/clauses/window-02/prompt.txt: c354e642b88d72b7a6c20d0068de324fbbff38cc3c92f8768fb467fcdb0686fe
        B/clauses/window-02/meta.json: 2a5de84470a5d81a3dedfd8aaea2668230fadecfc182b9381fcf5a1a56f7725f
        B/clauses/window-09/raw.json: 2c91790f61bea3a7ea5996714b7b6bbd92dee51731a84171d97dc7161c5379c3
        B/clauses/window-09/prompt.txt: e3c1ac4ef83cae7ee2b5d564c07475869d811f07c223e5fb340eeced531f7908
        B/clauses/window-09/meta.json: 19a0a5d776edd8930fae37b481e198fe1e596cd099563fb6d4426723078668d0
        B/clauses/window-07/raw.json: 5a85cd7cf54cb9905ac9712b3985fd2e2ae95f599168d39bef65fa3e6e4e9df4
        B/clauses/window-07/prompt.txt: cdb0995ec64d5e423bcbf196adece601969f7bf0f362b4f9b99bf9cedece4ffe
        B/clauses/window-07/meta.json: 22f821c53d908a7cad19bbfa2fd6eee8a102759867266be04e91cda68da02199
        B/clauses/window-01/raw.json: a40b3afcc1cd4382a0d10dacde78f64b22b857ab96dc006ccebc65212b553197
        B/clauses/window-01/prompt.txt: cde7c3135d76a81f0bc2211f615f2725dc60c282ac67e3a105df5b954d661d45
        B/clauses/window-01/meta.json: 809be1962ad2578bd4e8a41276747c18cd7ac456b57b992166325dd841080f4c
        B/clauses/window-06/raw.json: bb4e922ef9a53a01b1d6b7854f05c8390b03655d160bd18b01e5d3e9a595d09d
        B/clauses/window-06/prompt.txt: 9a8df08de78a33b2e6da1cae57df82f0ef6519427364af05d33f2700fc9cbd73
        B/clauses/window-06/meta.json: 30a9a1c8dcc5d609dc2afc0bbe358d660c2c33005f1567b633dfe8cb58b5c950
        B/clauses/window-08/raw.json: 911d18b2f7a42933b8a97a98a76f9d5cd025f399da6c6c2e7d6e7bf287d6464c
        B/clauses/window-08/prompt.txt: 6b7a39ec55a213370827890e688ff0a8764f14062a3533edaa738a815ea519b7
        B/clauses/window-08/meta.json: a0312ba043724b55045d362d02aab7ae958b54c37563ae13b400d20c22d85f9b
        B/tables/TABLE-1-page-5-1/raw.json: b27399c7e30670e2922ede33ca3becaba12bb7f9b58c5c496543f69f21feac3b
        B/tables/TABLE-1-page-5-1/prompt.txt: e8e4b5d6155837c48a30eaa43da339656a8df08a09da7a9c0c17e9c84ac86091
        B/tables/TABLE-1-page-5-1/meta.json: 8babf171080ee08dbe1f4ccbac0ec4767517586efd13999e6e575552dd20f79d
        B/tables/TABLE-2-page-5-2/raw.json: 781b59883cf72fdd732b4d87adbd0aa9cce2c7373488d6746c6caff6d5857b05
        B/tables/TABLE-2-page-5-2/prompt.txt: cf17295399aad93036970cdad5e22054046d16f3332cb4afb549d8d3a4d35c5c
        B/tables/TABLE-2-page-5-2/meta.json: c5b27c735b7d33585fca06f956346500c4e1f5afb74f097660fce46c284f0732
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
      pdf_sha256: 7570f761aaaf1c9cc476c7a77340fe8a212c1c335b17f076cdec383184722fb9
      source_review: _compare/relationships-2026-11-16/review-current/Schellekens2026
      source_status_sha256: a02aa33529147baa143dcab2d11ed945316e591e7af44c75c7b414d5c70f4315
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R009
    exposure:
      text: left fronto-temporo-parietal regions
    outcome:
      text: aphasia (NIHSS subscale)
    analysis_label: Multivariate lesion-symptom mapping
    relation: association
    evidence_ids:
    - P5-S1-C10
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
      pdf_sha256: 7570f761aaaf1c9cc476c7a77340fe8a212c1c335b17f076cdec383184722fb9
      source_review: _compare/relationships-2026-11-16/review-current/Schellekens2026
      source_status_sha256: a02aa33529147baa143dcab2d11ed945316e591e7af44c75c7b414d5c70f4315
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P1-S2-C9
      - Accounting without a linked unit P2-S1-C1
      - Accounting without a linked unit P2-S1-C2
      - Unaccounted source passage P2-S1-C1
      - Unaccounted source passage P2-S1-C2
      - Accounting without a linked unit P3-S4-C12
      - Result passage disposed without unit P4-S1-C10
      - Result passage disposed without unit P4-S1-C11
      - Accounting without a linked unit P4-S1-C6
      - Unaccounted source passage P3-S4-C12
      - Unaccounted source passage P4-S1-C6
      - Result passage disposed without unit P4-S1-C12
      - Accounting without a linked unit P4-S1-C14
      - Accounting without a linked unit P4-S1-C15
      - Accounting without a linked unit P5-S1-C1
      - Accounting without a linked unit P5-S1-C2
      - Accounting without a linked unit P5-S1-C3
      - Accounting without a linked unit P5-S1-C4
      - Accounting without a linked unit P5-S1-C5
      - Unaccounted source passage P5-S1-C4
      - Unaccounted source passage P5-S1-C1
      - Unaccounted source passage P4-S1-C14
      - Unaccounted source passage P5-S1-C3
      - Unaccounted source passage P4-S1-C15
      - Unaccounted source passage P5-S1-C5
      - Unaccounted source passage P5-S1-C2
      - Result passage disposed without unit P5-S2-C4
      - Result passage disposed without unit P5-S2-C5
      - Result passage disposed without unit P5-S2-C7
      - Result passage disposed without unit P6-S1-C1
      - Result passage disposed without unit P8-S1-C11
      - Result passage disposed without unit P8-S1-C13
      - Result passage disposed without unit P8-S2-C5
      - Result passage disposed without unit P8-S2-C13
      - Accounting without a linked unit P8-S3-C2
      - Unaccounted source passage P8-S3-C2
      - 'window 10: invalid/duplicate disposition P8-S4-C6'
      unattached_null_or_qualifier_ids:
      - P5-S2-C5
      - P8-S2-C5
      suppressed_nonrepresented_units: 27
      default_disposition_count_requires_completeness_check: 253
      unselected_timing_passages:
      - P1-S2-C4
      - P1-S2-C5
      - P2-S2-C10
      - P4-S1-C2
      - P8-S2-C6
      - P8-S4-C14
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P4-S1-C12
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
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
      - slot: validation
        source_id: P3-S3-C13
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: tested_personal_effects
        source_id: P3-S4-C9
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: limitations
        source_ids:
        - P7-S1-C5
        - P7-S1-C6
        - P8-S3-C11
        - P8-S3-C12
        - P8-S3-C13
        - P8-S3-C14
        - P8-S3-C15
        - P8-S3-C16
        - P8-S4-C2
        - P8-S4-C4
        - P8-S4-C5
        - P8-S4-C11
        - P8-S4-C12
        - P8-S4-C13
        - P8-S4-C14
        - P8-S5-C2
        - P8-S5-C3
        - P8-S5-C4
        - P8-S5-C5
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - validation
      - limitations
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-5-1
      - TABLE-2-page-5-2
      unlinked_tables:
      - TABLE-2-page-5-2
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P3-S4
        - P3-S5
        - P4-S1
        - P4-S2
        - P6-S1
        - P7-S1
        - P7-S2
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 7570f761aaaf1c9cc476c7a77340fe8a212c1c335b17f076cdec383184722fb9
      source_review: _compare/relationships-2026-11-16/review-current/Schellekens2026
      source_status_sha256: a02aa33529147baa143dcab2d11ed945316e591e7af44c75c7b414d5c70f4315
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes study population demographics and VCD prevalence.
    - source_id: P1-S2-C10
      disposition: represented
      result_indexes:
      - 0
      reason: States association between bilateral/cerebellar lesions and major VCD.
    - source_id: P2-S1-C1
      disposition: repeated
      result_indexes:
      - 1
      - 2
      - 4
      - 6
      - 7
      reason: Abstract restatement of domain-specific lesion associations.
    - source_id: P2-S1-C2
      disposition: repeated
      result_indexes:
      - 0
      - 8
      reason: Abstract restatement of aphasia and VCD associations.
    - source_id: P2-S1-C3
      disposition: repeated
      result_indexes:
      - 0
      - 1
      - 2
      - 4
      - 6
      - 7
      reason: Abstract restatement of widespread lesion distribution.
    - source_id: P3-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes patient exclusion due to registration failure.
    - source_id: P3-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes common rare causes of stroke.
    - source_id: P3-S4-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the statistical plan for separate LSMs.
    - source_id: P4-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes baseline characteristics differences between VCD groups.
    - source_id: P4-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes most frequent lesion territory (right MCA).
    - source_id: P4-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes regions with insufficient coverage for LSM.
    - source_id: P4-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement that LSM identified brain regions.
    - source_id: P4-S1-C14
      disposition: represented
      result_indexes:
      - 0
      reason: Identifies bilateral regions and left angular gyrus for major VCD.
    - source_id: P4-S1-C15
      disposition: represented
      result_indexes:
      - 0
      reason: Identifies right cerebellum cluster for major VCD.
    - source_id: P5-S1-C1
      disposition: represented
      result_indexes:
      - 1
      reason: Identifies regions for episodic memory.
    - source_id: P5-S1-C2
      disposition: represented
      result_indexes:
      - 2
      reason: Identifies regions for processing speed.
    - source_id: P5-S1-C3
      disposition: represented
      result_indexes:
      - 3
      reason: Identifies regions for visuoconstruction.
    - source_id: P5-S1-C4
      disposition: represented
      result_indexes:
      - 4
      reason: Identifies regions for executive functioning.
    - source_id: P5-S1-C5
      disposition: represented
      result_indexes:
      - 5
      reason: Identifies right-lateralized regions for visual neglect.
    - source_id: P5-S1-C6
      disposition: represented
      result_indexes:
      - 5
      reason: Identifies cerebellar regions for visual neglect.
    - source_id: P5-S1-C7
      disposition: represented
      result_indexes:
      - 6
      reason: Identifies regions for attention and working memory.
    - source_id: P5-S1-C8
      disposition: represented
      result_indexes:
      - 7
      reason: Identifies left hemisphere regions for language.
    - source_id: P5-S1-C9
      disposition: represented
      result_indexes:
      - 7
      reason: Identifies right cerebellum cluster for language.
    - source_id: P5-S1-C10
      disposition: represented
      result_indexes:
      - 8
      reason: Identifies left fronto-temporo-parietal regions for aphasia.
    - source_id: P5-S1-C11
      disposition: represented
      result_indexes:
      - 13
      reason: Reports reversed effects after internal LESYMAP volume correction.
    - source_id: P5-S1-C12
      disposition: represented
      result_indexes:
      - 10
      reason: Reports loss of significance for VCD, neglect, and language after volume
        adjustment.
    - source_id: P5-S2-C2
      disposition: represented
      result_indexes:
      - 10
      - 11
      reason: Reports null results for some domains and similar results for others
        after volume adjustment.
    - source_id: P5-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: States that adjustment for time and depression did not change results.
    - source_id: P5-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes modest reduction in cluster focality for early assessments.
    - source_id: P5-S2-C5
      disposition: represented
      result_indexes:
      - 12
      reason: Reports no significant clusters for visuoconstruction or neglect in
        early assessments.
    - source_id: P5-S2-C7
      disposition: repeated
      result_indexes:
      - 0
      - 1
      - 2
      - 4
      - 6
      - 7
      reason: Discussion restatement of cerebellar involvement in cognition.
    - source_id: P6-S1-C1
      disposition: repeated
      result_indexes:
      - 0
      - 1
      - 2
      - 4
      - 6
      - 7
      reason: Discussion restatement of widespread distribution.
    - source_id: P6-S1-C3
      disposition: repeated
      result_indexes:
      - 0
      - 1
      - 2
      - 4
      - 6
      - 7
      reason: Discussion restatement of bilateral associations.
    - source_id: P6-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: States that results correspond with established literature.
    - source_id: P7-S1-C1
      disposition: repeated
      result_indexes:
      - 1
      - 2
      - 4
      - 6
      - 7
      reason: Discussion restatement of domain-specific findings.
    - source_id: P7-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Speculates on the robustness of acute phase imaging.
    - source_id: P7-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Compares findings to voxel-based methods.
    - source_id: P7-S1-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Compares cluster size to voxel-based methods.
    - source_id: P8-S1-C6
      disposition: repeated
      result_indexes:
      - 6
      - 1
      reason: Discussion restatement of attention and memory associations.
    - source_id: P8-S1-C9
      disposition: repeated
      result_indexes:
      - 5
      reason: Discussion restatement of neglect associations.
    - source_id: P8-S1-C11
      disposition: repeated
      result_indexes:
      - 8
      reason: Discussion restatement of strong aphasia relationship.
    - source_id: P8-S1-C12
      disposition: repeated
      result_indexes:
      - 8
      reason: Discussion restatement of aphasia location.
    - source_id: P8-S1-C13
      disposition: repeated
      result_indexes:
      - 7
      reason: Discussion restatement of weak language relationship and cerebellar
        clusters.
    - source_id: P8-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discusses missing data in the language domain.
    - source_id: P8-S2-C9
      disposition: repeated
      result_indexes:
      - 0
      - 1
      - 2
      - 4
      - 6
      - 7
      reason: Discussion restatement of infratentorial/cerebellar associations.
    - source_id: P8-S2-C13
      disposition: repeated
      result_indexes:
      - 7
      reason: Discussion restatement of right cerebellum and language.
    - source_id: P8-S4-C7
      disposition: represented
      result_indexes:
      - 13
      reason: Reports reversed effects after internal LESYMAP volume correction.
    - source_id: P8-S4-C9
      disposition: represented
      result_indexes:
      - 10
      reason: Reports loss of significance for VCD, neglect, and language after volume
        adjustment.
    - source_id: P8-S4-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports r values (effect sizes) for brain-behavior relationships.
    - source_id: P9-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about focal regions associated with performance.
    - source_id: P9-S1-C10
      disposition: repeated
      result_indexes:
      - 0
      - 1
      - 2
      - 4
      - 6
      - 7
      reason: Conclusion restatement of widespread distribution.
    unresolved_coverage:
    - source_id: P5-S1-C11
      disposition: unresolved
      reason: Unknown result index; not accepted as coverage
    - source_id: P5-S1-C12
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P8-S4-C7
      disposition: unresolved
      reason: Unknown result index; not accepted as coverage
    - source_id: P8-S3-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S2-C9
    - P2-S1-C1
    - P2-S1-C2
    - P2-S1-C3
    - P3-S1-C6
    - P3-S2-C4
    - P3-S4-C12
    - P4-S1-C6
    - P4-S1-C10
    - P4-S1-C11
    - P4-S1-C12
    - P5-S2-C3
    - P5-S2-C4
    - P5-S2-C7
    - P6-S1-C1
    - P6-S1-C3
    - P6-S1-C4
    - P7-S1-C1
    - P7-S1-C7
    - P7-S1-C12
    - P7-S1-C13
    - P8-S1-C6
    - P8-S1-C9
    - P8-S1-C11
    - P8-S1-C12
    - P8-S1-C13
    - P8-S2-C5
    - P8-S2-C9
    - P8-S2-C13
    - P8-S3-C2
    - P8-S4-C11
    - P9-S1-C7
    - P9-S1-C10
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-5-1
    - TABLE-2-page-5-2
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P3-S4-C14
      recruited_sample:
      - P2-S2-C8
      - P2-S2-C10
      - P2-S2-C11
      eligibility:
      - P2-S2-C10
      - P2-S2-C12
      imaging_provenance:
      - P2-S3-C14
      - P3-S1-C1
      - P3-S3-C15
      - P3-S3-C16
      imaging_timing:
      - P2-S4-C4
      - P4-S1-C3
      - P8-S5-C1
      outcome_timing:
      - P2-S3-C5
      - P4-S1-C4
      - P8-S5-C1
      - P9-S1-C2
      outcome_definition:
      - P2-S3-C10
      - P2-S3-C12
      - P3-S3-C12
      validation: []
      analysis_restrictions:
      - P3-S3-C11
      - P3-S3-C12
      - P3-S4-C7
      - P3-S4-C11
      - P5-S2-C2
      - P5-S2-C4
      - P8-S4-C7
      - P8-S4-C9
      dependent_variable_statement:
      - P3-S3-C12
      limitations: []
      personal_factors:
      - P2-S3-C8
      - P3-S1-C8
      - P3-S1-C9
      - P3-S1-C10
      - P3-S2-C2
      - P4-S1-C6
      - P5-S3-C3
      tested_personal_effects:
      - P5-S2-C2
      - P5-S2-C3
      adjustment_roles:
      - P2-S3-C8
      - P3-S4-C7
      - P3-S4-C9
      - P5-S2-C2
      - P5-S2-C3
      - P8-S4-C7
      - P8-S4-C8
      - P8-S4-C9
      explicitly_not_adjusted:
      - P3-S4-C13
      - P5-S3-C3
      descriptive_personal_factors:
      - P4-S1-C2
      - P4-S1-C6
      - P5-S3-C5
    outcome_type: status_at_assessment
    imaging_vs_outcome: precedes_outcome
    validation_type: internal_cross_validation
    held_selections:
    - slot: dependent_variable_statement
      source_id: P4-S1-C12
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
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
    - slot: validation
      source_id: P3-S3-C13
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: tested_personal_effects
      source_id: P3-S4-C9
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: limitations
      source_ids:
      - P7-S1-C5
      - P7-S1-C6
      - P8-S3-C11
      - P8-S3-C12
      - P8-S3-C13
      - P8-S3-C14
      - P8-S3-C15
      - P8-S3-C16
      - P8-S4-C2
      - P8-S4-C4
      - P8-S4-C5
      - P8-S4-C11
      - P8-S4-C12
      - P8-S4-C13
      - P8-S4-C14
      - P8-S5-C2
      - P8-S5-C3
      - P8-S5-C4
      - P8-S5-C5
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
      pdf_sha256: 7570f761aaaf1c9cc476c7a77340fe8a212c1c335b17f076cdec383184722fb9
      review_sha256: b9501e4d35b53856ff40b6854492e1cad263cc3b5a3d1f52b3a6bb9cb427e3e6
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
      - P5-S1-C10
      source_result: Multivariate lesion-symptom mapping identified a significant
        association between aphasia (assessed by NIHSS language subscale) and left-lateralized
        lesions in the fronto-temporo-parietal regions (r = 0.626, p < 0.001).
      result_status: detected
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis corresponds to the multivariate lesion-symptom
            mapping (SCCAN) for aphasia as described in P5-S1-C10 and P3-S3-C12. The
            method, outcome (NIHSS language subscale), and population match the source.
          source_ids:
          - P5-S1-C10
          - P3-S3-C12
          - P3-S2-C9
        direction:
          answer: fits
          reason: The source states that regions associated with aphasia were 'predominantly
            left-lateralized' and located in 'fronto-temporo-parietal regions' (P5-S1-C10).
            The proposed core correctly identifies this as a detected association
            with left fronto-temporo-parietal regions.
          source_ids:
          - P5-S1-C10
        construct:
          answer: fits
          reason: The exposure is correctly identified as lesion location (left fronto-temporo-parietal)
            and the outcome as aphasia (NIHSS subscale). The patient measurement is
            template_lesion_overlap, as lesions were segmented and registered to MNI
            space (P3-S1-C1, P3-S3-C15) and mapped using SCCAN. The source explicitly
            states 'regions associated with aphasia... were predominantly left-lateralized'
            (P5-S1-C10), supporting the construct.
          source_ids:
          - P5-S1-C10
          - P3-S1-C1
          - P3-S3-C15
          - P1-S2-C7
        qualifications:
          answer: fits
          reason: The proposed core includes the method (SCCAN) and the cluster-size
            threshold (150 voxels, P3-S3-C10). It also correctly includes the limitation
            regarding underrepresentation of severe language impairment (P8-S3-C12)
            and the sensitivity analysis result (P5-S2-C2). These are material qualifiers
            present in the source.
          source_ids:
          - P3-S3-C10
          - P8-S3-C12
          - P5-S2-C2
        missing_material_caveat:
          answer: fits
          reason: 'The core includes the key limitations: the potential attenuation
            of findings due to exclusion of patients with severe aphasia (P8-S3-C12)
            and the loss of significance for language clusters after adjusting for
            lesion volume (P5-S2-C2). No other material caveats that change the interpretation
            of this specific association appear to be missing from the provided source
            window.'
          source_ids:
          - P8-S3-C12
          - P5-S2-C2
      optional_pending:
      - Specific coordinates of the peak cluster
      - Exact sparseness value interpretation details
      - Detailed sensitivity analysis statistics for other domains
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Specific coordinates of the peak cluster
    - Exact sparseness value interpretation details
    - Detailed sensitivity analysis statistics for other domains
    normalizations: []
    analysis_identity:
      id: R009
      exposure:
        text: left fronto-temporo-parietal regions
      outcome:
        text: aphasia (NIHSS subscale)
      analysis_label: Multivariate lesion-symptom mapping
      relation: association
      evidence_ids:
      - P5-S1-C10
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
        pdf_sha256: 7570f761aaaf1c9cc476c7a77340fe8a212c1c335b17f076cdec383184722fb9
        source_review: _compare/relationships-2026-11-16/review-current/Schellekens2026
        source_status_sha256: a02aa33529147baa143dcab2d11ed945316e591e7af44c75c7b414d5c70f4315
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P3-S4-C14:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 7570f761aaaf1c9cc476c7a77340fe8a212c1c335b17f076cdec383184722fb9
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 2b3baa4cff512c5a69f5ba5d90e39938b9c17364e1e4b86192d3f3c40e97d6e4
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S4-C14
          page: 3
          text_layer_sha256: 2b3baa4cff512c5a69f5ba5d90e39938b9c17364e1e4b86192d3f3c40e97d6e4
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "Results\nOf the 1,322 patients included in the ODYSSEY study\
          \ with an \nischemic stroke, 522 ischemic stroke patients were included\
          \ in this \nanalysis, see Fig. 1 for a flowchart of the study population."
        anchor_text: "Results\nOf the 1,322 patients included in the ODYSSEY study\
          \ with an \nischemic stroke, 522 ischemic stroke patients were included\
          \ in this \nanalysis, see Fig. 1 for a flowchart of the study population."
        excluded_fragments: []
        image_sha256: ca2856e3eaf392b90732ef02844804ec2f7967e7e7001a5834d1cb8d14906ab8
        transcription: 'Results


          Of the 1,322 patients included in the ODYSSEY study with an ischemic stroke,
          522 ischemic stroke patients were included in this analysis, see Fig. 1
          for a flowchart of the study population'
      P1-S2-C4:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 7570f761aaaf1c9cc476c7a77340fe8a212c1c335b17f076cdec383184722fb9
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: ccac1737b76e78a712ec3e580ae88a89219285b17bb28212d6e223b65e580725
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P1-S2-C4
          page: 1
          text_layer_sha256: ccac1737b76e78a712ec3e580ae88a89219285b17bb28212d6e223b65e580725
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "Methods: We conducted a multicenter prospective cohort study\
          \ between 2013 and 2021, enrolling patients aged \n18–49 years with first-ever\
          \ ischemic stroke and a visible stroke lesion on MRI."
        anchor_text: "Methods: We conducted a multicenter prospective cohort study\
          \ between 2013 and 2021, enrolling patients aged \n18–49 years with first-ever\
          \ ischemic stroke and a visible stroke lesion on MRI."
        excluded_fragments: []
        image_sha256: 6f7d794750146069ca61747b5fe618ee9bbef1e07ed0607718bf003b90e24578
        transcription: '.

          Methods: We conducted a multicenter prospective cohort study between 2013
          and 2021, enrolling patients aged

          18–49 years with first-ever ischemic stroke and a visible stroke lesion
          on MRI'
      P4-S1-C4:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 7570f761aaaf1c9cc476c7a77340fe8a212c1c335b17f076cdec383184722fb9
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 0b696da821f91a34ab32b8da9f872688ec8675e812e79019a370d326e100a2dd
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P4-S1-C4
          page: 4
          text_layer_sha256: 0b696da821f91a34ab32b8da9f872688ec8675e812e79019a370d326e100a2dd
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "Median time from index event to cognitive assessment was \n\
          83 days (IQR 56–119)."
        anchor_text: "Median time from index event to cognitive assessment was \n\
          83 days (IQR 56–119)."
        excluded_fragments: []
        image_sha256: a8f0f678c92772cbba9988b2e022578c41d10af18358c096115b7bac5633e515
        transcription: '. Median time from index event to cognitive assessment was

          83 days (IQR 56–119)'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 5
  quote: "Finally, regions associated with aphasia, \nassessed with the NIHSS subscale,\
    \ were predominantly left-lateralized \n(r = 0.626, p < 0.001, optimal sparseness\
    \ = -0.456), and located in \nthe fronto-temporo-parietal regions.\n5."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-25'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
