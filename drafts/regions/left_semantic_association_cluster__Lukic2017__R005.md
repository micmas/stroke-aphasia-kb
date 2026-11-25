---
id: left_semantic_association_cluster
name: left semantic association cluster
kind: network
findings:
- id: f1
  target_audit:
    status: behaviour_label_present
    category: behaviour_or_language_construct
    original_target: word_semantic_association
    reason: Label names a behaviour or language construct; its exact operational definition and measurement
      still need source review.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  outcome_measurement:
    status: needs_source_review
    instruments: []
    note: Outcome instrument/task is not yet verified for this finding. Do not infer it from the predictor
      or a paper-wide test list.
  target: word_semantic_association
  target_kind: impairment
  claim: word semantic association performance was negatively associated with lesions
    in the left IFG, STG, and putamen, as well as in two unlabeled clusters spatially
    contiguous to the insula and caudate
  direction: likely
  relationship: correlational
  method: VLSM
  sample:
    n: 40
    population: individuals with aphasia resulting from a single-left hemisphere stroke
    phase: not_reported
    time_post_onset: at least eight months post onset of stroke
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - not_transcribed
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: patient lesion overlap with a cluster comprising the
    left inferior frontal gyrus, superior temporal gyrus, putamen, and two unlabeled
    clusters spatially contiguous to the insula and caudate. results were only marginally
    significant after applying a correction for multiple comparisons. Additional metadata
    has not been transcribed; review the pending-field flags before approval. PDF
    image reading (P3-S2-C4, two-model agreement, human verification pending): Aphasic
    participants were at least eight months post onset of stroke (57.2 ± 52.3 months)
    and presented with aphasia based on administration of the Western Aphasia Battery-Revised
    (WAB-R; [57]) and a uniform set of cross-site language measures Original text-layer
    quotation is preserved below. PDF image reading (P3-S1-C7, two-model agreement,
    human verification pending): . Forty participants with aphasia (14 female) resulting
    from a single-left hemisphere stroke and 40 cognitively healthy age-matched (AM)
    controls (18 female) were recruited for the study from three research sites: Northwestern
    (NU), Boston (BU and MGH), and Johns Hopkins (JHU) Universities Original text-layer
    quotation is preserved below.'
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
    - proposed_concept:word_semantic_association
  citation: '@Lukic2017'
  source_passages:
  - section: Original source P6-S2-C2
    page: 6
    quote: 'Similarly, word semantic

      association performance was negatively associated with

      lesions in the left IFG, STG, and putamen, as well as in two

      unlabeled clusters spatially contiguous to the insula and cau-

      date (p = 0 068).'
    supports: claim
  - section: Original source P3-S2-C4
    page: 3
    quote: 'Aphasic participants were at least eight months post

      onset of stroke (57.2 ±52.3 months) and presented with

      aphasia based on administration of the Western Aphasia Bat-

      tery-Revised (WAB-R; [57]) and a uniform set of cross-site

      language measures.'
    supports: sample
  - section: Original source P3-S1-C7
    page: 3
    quote: 'Forty participants with aphasia (14 female)

      resulting from a single-left hemisphere stroke and 40 cogni-

      tively healthy age-matched (AM) controls (18 female) were

      recruited for the study from three research sites: Northwest-

      ern (NU), Boston (BU and MGH), and Johns Hopkins (JHU)

      Universities.'
    supports: sample
  - section: Original source P4-S2-C11
    page: 4
    quote: 'A voxel-based lesion symptom mapping

      (VLSM) approach was used to analyze the relationship

      between lesions in the left hemisphere and language perfor-

      mance [55], using the VLSM toolbox (http://www.crl.ucsd

      .edu/vlsm) running under Matlab R2014a.'
    supports: method
  - section: Original source P3-S2-C10
    page: 3
    quote: 'From the

      PALPA, subtests 35, 40, and 51 were selected to evaluate oral

      reading of words with regular and irregular orthography

      (PALPA35), spelling-to-dictation of words with high and

      low

      frequency

      (PALPA40),

      and

      semantic

      association

      between written words (PALPA51), respectively.'
    supports: method
  - section: Original source P10-S1-C4
    page: 10
    quote: 'However, given that VLSM analyses yielded results

      that were only marginally signiﬁcant after applying a cor-

      rection for multiple comparisons, the discussion will focus

      primarily on the results of the VBM analyses, and VLSM

      results will be discussed within the context of the explana-

      tion of the VBM results.'
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-24'
relationship_review:
  paper: Lukic2017
  proposal_id: R005
  review_status_sha256: 34571233832f782b51e56a171cff24eb543b1e5d46e592c8d4c3326c3076ea7e
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: de35ad93bd93a1ae6fe470952a0b96689bee4f7dc632d682f5b2fafc18631b4c
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: de35ad93bd93a1ae6fe470952a0b96689bee4f7dc632d682f5b2fafc18631b4c
        A/passages.json: 0d8c4b4e560e062e61df83292627ef82dcdd067498a196c2a69139203f28d302
        A/raw.json: 6c6ec0dbf55aa9d08ac9c045223f8dbafca2210e046b65bfccdd8ca0720befee
        A/source-units.json: 42681602471e4c98d931170296396465ff446fa36a45f7ba54750b2281b57ec8
        A/full-source-units.json: a943f3c90fb2ccc3b40b29db0c1f92ade2ce6c8b706b08feaef7bf84dca3e012
        A/meta.json: 86856afee8fab370bd141d24bee3e2cc2b2c4802c46fd116c7fe6b66784c9c52
        A/table-images/TABLE-1-page-3-1.png: aaf259f4c057c44ca3f64914821dcd158aa13a946abfa6cb7c9c4cb8aa722a36
        A/table-images/TABLE-4-page-9-1.png: 21685a7ec5a9fd31f9b222b305434c40c1f2139735d23c3b94e69a1c77dc9046
        A/table-images/page-3.png: 40d54c4ae96a8055dc898405c1467344cc24367454ed3d9553663f8d9c4374f6
        A/table-images/page-6.png: 4249266d1d5d518914fefc8ba595ff1094c5ae816e0bd72c5189add3a3d39642
        A/table-images/page-5.png: e53821421240747d34e38a6902fae58edaa4e14cc4faf8a65b4ae3ea6fea9e45
        A/table-images/page-9.png: 891c4e6ae56323e98f2790dccc4e9b9ad0e19799f31e5ebe92e50e4cf74a54d3
        A/table-images/TABLE-3-page-6-1.png: c53a3b17081feca61ed0aae798cb6cef91e14e7b818eb61a7ffdac86c13a91f9
        A/table-images/manifest.json: cd5c2437df0b841dd3f0a17842fb1d2043d61b8e56a952abc16eb1f5e4e97001
        A/table-images/TABLE-2-page-5-1.png: 7f2c043ee0bdfaf80105a0b0d3e9ee5d39acff20b0db6a9dfca9bbd0261f1de2
        A/clauses/window-03/raw.json: 4268d07f8bbfed4591abb3fbb4c0ec670c4fe1634fbd02e1f97a14adc348a7c7
        A/clauses/window-03/prompt.txt: e71f275d8d079c495ee19f4df6eb8ca7fe515d61a54dc555b7779d7cb8838998
        A/clauses/window-03/meta.json: 5ed049fe9016126f938f832929a65b7941e456b372ec83c66c03743304ef7348
        A/clauses/window-04/raw.json: 52cc371201cadcca9ec42547a3b4fcb0ee6b928b69fbdaa699d6f63ccec82441
        A/clauses/window-04/prompt.txt: 23b8013034719e5bd907fe757a8f4c1e16c10024b7f5316e3a73c2e972b8314b
        A/clauses/window-04/meta.json: a29ab6d93ba04768e6c61d6535ac825d64c6a9ac3ee917628cd5e48115ebc254
        A/clauses/window-05/raw.json: 928108b23081e08fbe5ff8bd042e4efb738d01bfbc60fefd3da863c534cf53f9
        A/clauses/window-05/prompt.txt: aa27ab2ac33e15e84580c1ccf145b4311c8fc009bee7fce5a795a5b6ed46a3c6
        A/clauses/window-05/meta.json: df48f1a2850164385b9d8331cc6a902fde3d4e22ff492904a91e5e76816155fc
        A/clauses/window-02/raw.json: 27fcfa31ce942408f178444140c59e8062ff12c1eee0b2a01c35fca783bc4b67
        A/clauses/window-02/prompt.txt: dbdfbbe2c4b3b02f043c7da4beac76bdab8de93048eeaff1b19190b6084b38d0
        A/clauses/window-02/meta.json: d2399df4fc5ed0d1a24bf9ee240aab40cde3bb547792ef03996b7f3c85b64a70
        A/clauses/window-07/raw.json: b5f1ba0b9ce9dd5ff9f731a42f5f0b790ced37f1ef95fb5a450d049d0e5c43f9
        A/clauses/window-07/prompt.txt: 0639cf30016efb8cd4fdcf34b74b53b1a3ec0b168b712f9dd774eab197b2cfa1
        A/clauses/window-07/meta.json: d98662a9e5fdf0471f6e786d412e8f7aa4bdca655f5d3f0d4dfedfe1a6bb3882
        A/clauses/window-01/raw.json: 08370785ceec7772a0eb3afa5b88f435fd084996008a021d4b75ffcb45cd8d7b
        A/clauses/window-01/prompt.txt: b213e765dadd10513a80bae384b0e73cc25f16bf4fe55b02e5af4cd6b656cb1b
        A/clauses/window-01/meta.json: 007115c8827893716ff481c26f5b94fea517c2e57513ea6e29d3bb56e48baac0
        A/clauses/window-06/raw.json: 38ae35a924b4d37ead80a92aec15af2a20660a2a4f05edb8b4ebcc841b48d465
        A/clauses/window-06/prompt.txt: 5119a28c5a5293eceb27b8ee6802504154e79fee7f82d0988a1c70104c5b1abe
        A/clauses/window-06/meta.json: caa1db041415be8f0dcad50f3f8e7d4056574b161d1bb30a624837b773d5cd3f
        A/clauses/window-08/raw.json: a7ff9eb0b44002664832dd76560c3d321fbf45cbcda2043ee565970183e2d4e7
        A/clauses/window-08/prompt.txt: e1f4006e1194fda5cc3c554e2be802748fef706b1eb573f71f589de2cbde8a2e
        A/clauses/window-08/meta.json: 47d08ce4bc784c3e0dde061bac090507b7a8580896a2fb165688191c1374e9ab
        A/tables/TABLE-2-page-5-2/raw.json: b926c2e3682326671bb2f75c7331a375f5e114715600f105eda1deaeb4eb2901
        A/tables/TABLE-2-page-5-2/prompt.txt: 4cf898de3fa24f80045d864dd9e7322c4ca5fedc6f1f2477e80d6aa3c7c119a0
        A/tables/TABLE-2-page-5-2/meta.json: 2a6f2007e7b5e6b30c83a964fa9162c46d1c6f0ceffebc8e1b690ed24f37d841
        A/tables/TABLE-3-page-6-3/raw.json: 900266752475e46d5751c533c0530d4eb366806c6f60608e0fb95e7cd058d4c8
        A/tables/TABLE-3-page-6-3/prompt.txt: 07bc93b1fdd74e0f67bdebb2f2d4812a168bde7bb03bb58eba7a8fc3493f2c8f
        A/tables/TABLE-3-page-6-3/meta.json: 0fa71184c9e5386f1a134055543b701bc56fe16bf17c0a9f9c08e8e10e6394cd
        A/tables/TABLE-1-page-3-1/raw.json: 4ef2003e4d3eb9f20e047924f95a50b200ae80db5b93fd17c8e2c9c2007be547
        A/tables/TABLE-1-page-3-1/prompt.txt: 073ac4b54113df5c2bce95ca573fab9003b1c4799b9ef6b83c156e9ccbadde43
        A/tables/TABLE-1-page-3-1/meta.json: 131f45b32a5e2e28352fb9ed9ac5567ed7a64719a84c993e0386bb99b4901e86
        A/tables/TABLE-4-page-9-4/raw.json: 866528d7e8b424344c9ac73c73c411e56cb569178b05b1f73096a719c31f1d67
        A/tables/TABLE-4-page-9-4/prompt.txt: 22436d03f641dd988c8119507ac7553a7f5425f101e90ee9b2260be1a14f1e9c
        A/tables/TABLE-4-page-9-4/meta.json: db3458a815a3b5503818150f606d099330c8a2bd04574c9cdbdcbea829f60bb3
        B/passages.json: 0d8c4b4e560e062e61df83292627ef82dcdd067498a196c2a69139203f28d302
        B/raw.json: d306fb9e5fdd29c39c59ad9b77216a18b3570e860dc1e3ddc62830e7036e0dd9
        B/source-units.json: 42681602471e4c98d931170296396465ff446fa36a45f7ba54750b2281b57ec8
        B/full-source-units.json: a943f3c90fb2ccc3b40b29db0c1f92ade2ce6c8b706b08feaef7bf84dca3e012
        B/meta.json: 2cd99a1dc610866e9bc86ac3e2202236cec413e46d18f9c306dfd8be90e60c34
        B/table-images/TABLE-1-page-3-1.png: aaf259f4c057c44ca3f64914821dcd158aa13a946abfa6cb7c9c4cb8aa722a36
        B/table-images/TABLE-4-page-9-1.png: 21685a7ec5a9fd31f9b222b305434c40c1f2139735d23c3b94e69a1c77dc9046
        B/table-images/page-3.png: 40d54c4ae96a8055dc898405c1467344cc24367454ed3d9553663f8d9c4374f6
        B/table-images/page-6.png: 4249266d1d5d518914fefc8ba595ff1094c5ae816e0bd72c5189add3a3d39642
        B/table-images/page-5.png: e53821421240747d34e38a6902fae58edaa4e14cc4faf8a65b4ae3ea6fea9e45
        B/table-images/page-9.png: 891c4e6ae56323e98f2790dccc4e9b9ad0e19799f31e5ebe92e50e4cf74a54d3
        B/table-images/TABLE-3-page-6-1.png: c53a3b17081feca61ed0aae798cb6cef91e14e7b818eb61a7ffdac86c13a91f9
        B/table-images/manifest.json: 13ad2bb9b4047217edf80b22dfdee56514412cc7e73f889a39e06ed82f64aca7
        B/table-images/TABLE-2-page-5-1.png: 7f2c043ee0bdfaf80105a0b0d3e9ee5d39acff20b0db6a9dfca9bbd0261f1de2
        B/clauses/window-03/raw.json: b4f45e071c5353172731fa02344c9f598d26f5dd78b6a52f85cdc960e2cc8c8e
        B/clauses/window-03/prompt.txt: e71f275d8d079c495ee19f4df6eb8ca7fe515d61a54dc555b7779d7cb8838998
        B/clauses/window-03/meta.json: 84478094ee8db3580f21c46e46a347fc6e285a5b4ea74aea61e30d5c3d82ef2e
        B/clauses/window-04/raw.json: fbd1d2c97208e07bf5c30226137ebd05e4781707cc504838de6fcb70b6c79428
        B/clauses/window-04/prompt.txt: 23b8013034719e5bd907fe757a8f4c1e16c10024b7f5316e3a73c2e972b8314b
        B/clauses/window-04/meta.json: d234ef234960e272c84fb87479fed870d8d57bfc7cee3a73eb9bdd11a9ee97f0
        B/clauses/window-05/raw.json: af54d3003d543744cd55f5d467de24ab01b2fade0e29031ef94154ae04ceba7e
        B/clauses/window-05/prompt.txt: aa27ab2ac33e15e84580c1ccf145b4311c8fc009bee7fce5a795a5b6ed46a3c6
        B/clauses/window-05/meta.json: fbc842d2792c4391381d2deb53305c003438214218db48358d1d82ef0cfa99c3
        B/clauses/window-02/raw.json: e6ecdc9b62682d8cea553046a373b643e0085e435d2e857074d0264437837917
        B/clauses/window-02/prompt.txt: dbdfbbe2c4b3b02f043c7da4beac76bdab8de93048eeaff1b19190b6084b38d0
        B/clauses/window-02/meta.json: 0ccccf967db698880969e18a55fc6270c69be1605e2231175885bcbbf46bcd49
        B/clauses/window-07/raw.json: 8d5a11d22b7be19a7b3efc6c9bdab2921c5ed649c0f0acb1aaefe360e6a957a6
        B/clauses/window-07/prompt.txt: 0639cf30016efb8cd4fdcf34b74b53b1a3ec0b168b712f9dd774eab197b2cfa1
        B/clauses/window-07/meta.json: 37db4eea2781f3d671edd10f4d9c44e9a500ed58abb14fb8f33001bf51c2e234
        B/clauses/window-01/raw.json: 225560af3a951c8c4428ece46693e2234ed701ce285176e889215c74538c5774
        B/clauses/window-01/prompt.txt: b213e765dadd10513a80bae384b0e73cc25f16bf4fe55b02e5af4cd6b656cb1b
        B/clauses/window-01/meta.json: 7d98ff01e4d7e27dfa38bb9842d7b42631b8834fdf8d35eccf4fec1339d2f098
        B/clauses/window-06/raw.json: a30ec99b88e6c0640f321bfae229c43a480a4609b91242fc86aa7e87abb4216b
        B/clauses/window-06/prompt.txt: 5119a28c5a5293eceb27b8ee6802504154e79fee7f82d0988a1c70104c5b1abe
        B/clauses/window-06/meta.json: 19acc8f2f90e3b7d786465dc07f2d477dcbc5a919a45d8b0d80aedf483505e0d
        B/clauses/window-08/raw.json: 75958d510e44246b6f914df7f3bb0f7ac47d827bd712af06ccbfc383103d6f69
        B/clauses/window-08/prompt.txt: e1f4006e1194fda5cc3c554e2be802748fef706b1eb573f71f589de2cbde8a2e
        B/clauses/window-08/meta.json: a9c7d93fb1dfdc36582474a656355179ef371860b7bd14710f66d86dc46e9421
        B/tables/TABLE-2-page-5-2/raw.json: 3540f7d013bdac856ba7757fb41f46d35dbe937527a0cdf6ff21059e866fd83a
        B/tables/TABLE-2-page-5-2/prompt.txt: 4cf898de3fa24f80045d864dd9e7322c4ca5fedc6f1f2477e80d6aa3c7c119a0
        B/tables/TABLE-2-page-5-2/meta.json: 81958e832657303cbe3895582fbfe2215e532013454f82747ac5fc085c43d946
        B/tables/TABLE-3-page-6-3/raw.json: 1d393e0c05192ee7fe1ebe45f160afbf1a37eaed17a44237622f8828df3e94b5
        B/tables/TABLE-3-page-6-3/prompt.txt: 07bc93b1fdd74e0f67bdebb2f2d4812a168bde7bb03bb58eba7a8fc3493f2c8f
        B/tables/TABLE-3-page-6-3/meta.json: e54bb482459ce23c5d5756e9ab628b759c6a06e0747a5171802574e423f8e5e3
        B/tables/TABLE-1-page-3-1/raw.json: 6994cb5fda1b55a2927209496114225e81c6c9cfe25460334e8a248d89c7f46b
        B/tables/TABLE-1-page-3-1/prompt.txt: 073ac4b54113df5c2bce95ca573fab9003b1c4799b9ef6b83c156e9ccbadde43
        B/tables/TABLE-1-page-3-1/meta.json: 96fa7231a0c153d6ad2c054bcfcfb5bb0387f89eb0007fd7f259484252fc9811
        B/tables/TABLE-4-page-9-4/raw.json: 6e3dcc81b63cc4b503e5e970a896c7af2907cbe0acb0d534ed020381892da17a
        B/tables/TABLE-4-page-9-4/prompt.txt: 22436d03f641dd988c8119507ac7553a7f5425f101e90ee9b2260be1a14f1e9c
        B/tables/TABLE-4-page-9-4/meta.json: ee8818e86c38bfbf33c7e4b9f406eb0984a1966e80876774f451881709f2977a
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
      pdf_sha256: de35ad93bd93a1ae6fe470952a0b96689bee4f7dc632d682f5b2fafc18631b4c
      source_review: _compare/relationships-2026-11-16/review-current/Lukic2017
      source_status_sha256: 73903ece552889759d5beee340b7cd1aac671b8190dc59110993afcffb36fd1f
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R005
    exposure:
      text: left IFG, STG, putamen, and clusters contiguous to insula and caudate
        lesions
    outcome:
      text: word semantic association
    analysis_label: VLSM Analysis
    relation: association
    evidence_ids:
    - P6-S2-C2
    - P10-S1-C3
    qualifier_ids:
    - P6-S1-C14
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: de35ad93bd93a1ae6fe470952a0b96689bee4f7dc632d682f5b2fafc18631b4c
      source_review: _compare/relationships-2026-11-16/review-current/Lukic2017
      source_status_sha256: 73903ece552889759d5beee340b7cd1aac671b8190dc59110993afcffb36fd1f
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P6-S1-C1
      - Result passage disposed without unit P6-S1-C2
      - Accounting without a linked unit P6-S1-C4
      - Accounting without a linked unit P6-S1-C5
      - Accounting without a linked unit P6-S1-C8
      - Unaccounted source passage P6-S1-C5
      - Unaccounted source passage P6-S1-C4
      - Unaccounted source passage P6-S1-C8
      - Accounting without a linked unit P6-S1-C13
      - Accounting without a linked unit P6-S2-C2
      - Accounting without a linked unit P6-S2-C3
      - Accounting without a linked unit P6-S2-C4
      - Accounting without a linked unit P6-S2-C9
      - Unaccounted source passage P6-S2-C9
      - Unaccounted source passage P6-S2-C2
      - Unaccounted source passage P6-S2-C3
      - Unaccounted source passage P6-S2-C4
      - Unaccounted source passage P6-S1-C13
      - Accounting without a linked unit P6-S2-C11
      - Accounting without a linked unit P7-S1-C1
      - Accounting without a linked unit P7-S1-C2
      - Accounting without a linked unit P7-S1-C4
      - Unaccounted source passage P7-S1-C4
      - Unaccounted source passage P6-S2-C11
      - Unaccounted source passage P7-S1-C1
      - Unaccounted source passage P7-S1-C2
      - Accounting without a linked unit P7-S1-C7
      - Accounting without a linked unit P9-S1-C1
      - Unaccounted source passage P7-S1-C7
      - Unaccounted source passage P9-S1-C1
      - Result passage disposed without unit P11-S1-C1
      - Result passage disposed without unit P11-S1-C7
      - Result passage disposed without unit P11-S1-C8
      - Result passage disposed without unit P11-S2-C10
      - Result passage disposed without unit P11-S2-C8
      unattached_null_or_qualifier_ids:
      - P11-S2-C10
      suppressed_nonrepresented_units: 6
      default_disposition_count_requires_completeness_check: 176
      unselected_timing_passages:
      - P3-S1-C11
      - P3-S1-C12
      - P3-S2-C1
      - P7-S1-C3
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P6-S2-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S2-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S2-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S3-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S3-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S4-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P4-S2-C8
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P4-S3-C4
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P5-S2-C4
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: imaging_provenance
        source_ids:
        - P3-S3-C3
        - P4-S1-C4
        - P4-S1-C5
        - P4-S1-C6
        - P4-S1-C8
        - P4-S1-C9
        - P4-S1-C10
        - P4-S1-C11
        - P4-S1-C12
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: outcome_definition
        source_ids:
        - P3-S2-C6
        - P3-S2-C8
        - P3-S2-C10
        - P3-S2-C11
        - P5-S1-C5
        - P6-S1-C2
        - P6-S2-C13
        - P9-S1-C2
        - P9-S1-C3
        - P9-S1-C5
        - P9-S1-C6
        - P10-S1-C2
        - P10-S1-C3
        - P10-S2-C9
        - P10-S3-C4
        - P10-S3-C5
        - P10-S3-C7
        - P10-S3-C8
        - P10-S4-C3
        - P11-S1-C11
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - imaging_provenance
      - outcome_definition
      - validation
      - personal_factors
      - tested_personal_effects
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-3-1
      - TABLE-2-page-5-2
      - TABLE-3-page-6-3
      - TABLE-4-page-9-4
      unlinked_tables:
      - TABLE-1-page-3-1
      - TABLE-3-page-6-3
      - TABLE-4-page-9-4
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P4-S1
        - P4-S2
        - P4-S3
        - P5-S3
        - P6-S1
        - P6-S2
        - P7-S1
        - P8-S1
        - P9-S1
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: de35ad93bd93a1ae6fe470952a0b96689bee4f7dc632d682f5b2fafc18631b4c
      source_review: _compare/relationships-2026-11-16/review-current/Lukic2017
      source_status_sha256: 73903ece552889759d5beee340b7cd1aac671b8190dc59110993afcffb36fd1f
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S2-C3
      disposition: represented
      result_indexes:
      - 0
      reason: Reports reduced GM volume in RH SMA for aphasic group.
    - source_id: P1-S2-C4
      disposition: repeated
      result_indexes:
      - 8
      - 9
      reason: Abstract restatement of VBM results.
    - source_id: P3-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Demographic matching information.
    - source_id: P3-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Demographic matching information.
    - source_id: P3-S2-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Demographic matching information.
    - source_id: P3-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive WAB-AQ scores.
    - source_id: P4-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Definition of ROIs.
    - source_id: P5-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to Table 2 for descriptive scores.
    - source_id: P5-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive performance on comprehension tasks.
    - source_id: P6-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive performance on comprehension tasks.
    - source_id: P6-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive performance on production tasks.
    - source_id: P6-S1-C4
      disposition: represented
      result_indexes: []
      reason: Null result for entire RH GM volume difference.
    - source_id: P6-S1-C5
      disposition: represented
      result_indexes:
      - 0
      reason: Reports reduced GM volume in right SMA for patients.
    - source_id: P6-S1-C8
      disposition: represented
      result_indexes:
      - 1
      - 2
      reason: Reports difference in SMA GM volume for poor performers vs controls
        and no difference for good performers.
    - source_id: P6-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to Table 3.
    - source_id: P6-S1-C13
      disposition: represented
      result_indexes:
      - 3
      reason: Reports trend for spoken word comprehension lesions.
    - source_id: P6-S2-C2
      disposition: represented
      result_indexes:
      - 4
      reason: Reports association between word semantic association and LH lesions.
    - source_id: P6-S2-C3
      disposition: represented
      result_indexes:
      - 5
      reason: Reports trend for sentence comprehension lesions.
    - source_id: P6-S2-C4
      disposition: represented
      result_indexes:
      - 6
      reason: Reports null results for production measures in VLSM.
    - source_id: P6-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to Table 4.
    - source_id: P6-S2-C9
      disposition: represented
      result_indexes:
      - 7
      reason: Reports positive relationship between spoken word comprehension and
        RH MTG/insula GM volume.
    - source_id: P6-S2-C10
      disposition: represented
      result_indexes:
      - 12
      reason: Reports null results for word semantic association and sentence comprehension
        in VBM.
    - source_id: P6-S2-C11
      disposition: represented
      result_indexes:
      - 8
      reason: Reports positive relationship between word production and RH SMA/insula
        GM volume.
    - source_id: P6-S3-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Summary of Table 3.
    - source_id: P6-S3-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of statistical correction.
    - source_id: P7-S1-C1
      disposition: represented
      result_indexes:
      - 9
      - 11
      reason: Reports positive relations for oral reading and sentence production
        with RH SMA/pallidum/hippocampus.
    - source_id: P7-S1-C2
      disposition: represented
      result_indexes:
      - 10
      reason: Reports positive relation for spelling-to-dictation with RH hippocampus/postcentral.
    - source_id: P7-S1-C4
      disposition: repeated
      result_indexes:
      - 0
      reason: Discussion restatement of SMA GM volume reduction.
    - source_id: P7-S1-C5
      disposition: repeated
      result_indexes:
      - 1
      reason: Discussion restatement of SMA GM volume difference in poor performers.
    - source_id: P9-S1-C1
      disposition: repeated
      result_indexes:
      - 7
      - 8
      - 11
      reason: Discussion restatement of VBM results.
    - source_id: P9-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Summary of Table 4.
    - source_id: P10-S1-C2
      disposition: represented
      result_indexes:
      - 7
      - 12
      reason: Reports positive association for spoken word comprehension and null
        for others.
    - source_id: P10-S1-C3
      disposition: repeated
      result_indexes:
      - 3
      - 4
      - 5
      reason: Discussion restatement of VLSM results.
    - source_id: P10-S2-C2
      disposition: repeated
      result_indexes:
      - 7
      reason: Discussion restatement of insula association with word comprehension.
    - source_id: P10-S2-C5
      disposition: repeated
      result_indexes:
      - 12
      reason: Discussion restatement of null sentence comprehension effect.
    - source_id: P10-S2-C8
      disposition: repeated
      result_indexes:
      - 5
      reason: Discussion restatement of sentence comprehension lesions.
    - source_id: P10-S3-C4
      disposition: repeated
      result_indexes:
      - 8
      - 9
      - 11
      reason: Discussion restatement of production associations with RH SMA.
    - source_id: P10-S3-C8
      disposition: repeated
      result_indexes:
      - 8
      reason: Discussion restatement of insula association with word production.
    - source_id: P10-S4-C3
      disposition: repeated
      result_indexes:
      - 10
      reason: Discussion restatement of spelling-to-dictation association.
    - source_id: P11-S1-C1
      disposition: repeated
      result_indexes:
      - 10
      reason: Discussion restatement of spelling-to-dictation results.
    - source_id: P11-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison to prior study (Xing et al.).
    - source_id: P11-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison to prior study (Xing et al.).
    - source_id: P11-S1-C9
      disposition: repeated
      result_indexes:
      - 7
      - 8
      - 11
      reason: Discussion summary of VBM results.
    - source_id: P11-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Theoretical discussion of homology.
    - source_id: P11-S2-C9
      disposition: repeated
      result_indexes:
      - 7
      - 12
      reason: Discussion of results in context of homology.
    - source_id: P11-S2-C10
      disposition: repeated
      result_indexes:
      - 8
      - 9
      - 11
      reason: Discussion of results in context of homology.
    - source_id: P11-S3-C8
      disposition: repeated
      result_indexes:
      - 7
      - 8
      - 9
      - 10
      - 11
      reason: Conclusion restatement of recruitment patterns.
    unresolved_coverage:
    - source_id: P6-S1-C4
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P6-S3-C4
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P7-S1-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S2-C4
    - P3-S1-C11
    - P3-S1-C12
    - P3-S2-C1
    - P3-S2-C5
    - P4-S2-C4
    - P5-S2-C8
    - P5-S2-C9
    - P6-S1-C1
    - P6-S1-C2
    - P6-S1-C4
    - P6-S1-C11
    - P6-S1-C13
    - P6-S2-C8
    - P6-S3-C2
    - P7-S1-C7
    - P9-S1-C1
    - P9-S2-C2
    - P11-S1-C1
    - P11-S1-C7
    - P11-S1-C8
    - P11-S1-C9
    - P11-S2-C8
    - P11-S2-C9
    - P11-S2-C10
    - P11-S3-C8
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-3-1
    - TABLE-2-page-5-2
    - TABLE-3-page-6-3
    - TABLE-4-page-9-4
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P3-S1-C7
      recruited_sample:
      - P3-S1-C7
      eligibility:
      - P3-S1-C7
      - P3-S1-C8
      - P3-S1-C9
      - P3-S1-C10
      - P3-S2-C4
      imaging_provenance: []
      imaging_timing:
      - P3-S2-C4
      outcome_timing:
      - P3-S2-C4
      outcome_definition: []
      validation: []
      analysis_restrictions:
      - P4-S1-C4
      - P4-S1-C6
      - P4-S2-C5
      - P5-S2-C3
      - P5-S2-C4
      - P6-S2-C13
      - P9-S1-C9
      - P9-S2-C3
      dependent_variable_statement:
      - P4-S2-C6
      - P4-S2-C13
      - P5-S1-C5
      - P9-S1-C5
      limitations:
      - P11-S1-C3
      - P11-S1-C12
      - P11-S2-C12
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P4-S2-C7
      - P5-S1-C7
      - P5-S1-C8
      - P5-S1-C9
      - P6-S1-C7
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P3-S1-C7
      - P3-S1-C11
      - P3-S2-C5
      - P3-S3-C5
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P6-S2-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S2-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S2-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S3-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S3-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S4-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P4-S2-C8
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P4-S3-C4
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P5-S2-C4
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: imaging_provenance
      source_ids:
      - P3-S3-C3
      - P4-S1-C4
      - P4-S1-C5
      - P4-S1-C6
      - P4-S1-C8
      - P4-S1-C9
      - P4-S1-C10
      - P4-S1-C11
      - P4-S1-C12
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: outcome_definition
      source_ids:
      - P3-S2-C6
      - P3-S2-C8
      - P3-S2-C10
      - P3-S2-C11
      - P5-S1-C5
      - P6-S1-C2
      - P6-S2-C13
      - P9-S1-C2
      - P9-S1-C3
      - P9-S1-C5
      - P9-S1-C6
      - P10-S1-C2
      - P10-S1-C3
      - P10-S2-C9
      - P10-S3-C4
      - P10-S3-C5
      - P10-S3-C7
      - P10-S3-C8
      - P10-S4-C3
      - P11-S1-C11
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
      pdf_sha256: de35ad93bd93a1ae6fe470952a0b96689bee4f7dc632d682f5b2fafc18631b4c
      review_sha256: 34571233832f782b51e56a171cff24eb543b1e5d46e592c8d4c3326c3076ea7e
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
      - P6-S2-C2
      - P10-S1-C3
      source_result: VLSM analysis revealed a negative association between lesions
        in the left IFG, STG, putamen, and clusters contiguous to insula/caudate and
        word semantic association performance (PALPA51). The result was marginally
        significant (p=0.068) after permutation correction, and the authors note that
        VLSM results were only marginally significant after multiple comparison correction,
        focusing discussion primarily on VBM results.
      result_status: detected_only_at_relaxed_threshold
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis correctly identifies the VLSM analysis for
            word semantic association (PALPA51) in the aphasia cohort, matching the
            source description in P6-S2-C2 and P10-S1-C3.
          source_ids:
          - P6-S2-C2
          - P10-S1-C3
        direction:
          answer: fits
          reason: The source explicitly states a 'negative association' between lesions
            and performance (P6-S2-C2), which aligns with the proposed claim of negative
            association. The direction is preserved.
          source_ids:
          - P6-S2-C2
          - P10-S1-C3
        construct:
          answer: fits
          reason: The exposure (left IFG, STG, putamen, contiguous clusters) and outcome
            (word semantic association/PALPA51) are correctly identified. The patient
            measurement is template_lesion_overlap, as VLSM overlays patient lesions
            on reference maps, not patient_diffusion.
          source_ids:
          - P6-S2-C2
          - P4-S2-C11
        qualifications:
          answer: fits
          reason: The proposed draft includes the qualification that results were
            'only marginally significant after applying a correction for multiple
            comparisons' (P10-S1-C4), which is a material caveat present in the source.
            The p-value of 0.068 in P6-S2-C2 supports this marginal significance.
          source_ids:
          - P10-S1-C4
          - P6-S2-C2
        missing_material_caveat:
          answer: fits
          reason: The draft includes the key limitation regarding marginal significance.
            No other material caveats (such as population restrictions or timing)
            are omitted that would change the interpretation of this specific VLSM
            result.
          source_ids:
          - P10-S1-C4
      optional_pending:
      - Exact p-value transcription (0.068 vs table readings)
      - Specific coordinates of the unlabeled clusters
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Exact p-value transcription (0.068 vs table readings)
    - Specific coordinates of the unlabeled clusters
    normalizations: []
    analysis_identity:
      id: R005
      exposure:
        text: left IFG, STG, putamen, and clusters contiguous to insula and caudate
          lesions
      outcome:
        text: word semantic association
      analysis_label: VLSM Analysis
      relation: association
      evidence_ids:
      - P6-S2-C2
      - P10-S1-C3
      qualifier_ids:
      - P6-S1-C14
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: de35ad93bd93a1ae6fe470952a0b96689bee4f7dc632d682f5b2fafc18631b4c
        source_review: _compare/relationships-2026-11-16/review-current/Lukic2017
        source_status_sha256: 73903ece552889759d5beee340b7cd1aac671b8190dc59110993afcffb36fd1f
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P3-S2-C4:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: de35ad93bd93a1ae6fe470952a0b96689bee4f7dc632d682f5b2fafc18631b4c
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: fcf20fa2db34e28f034f1fb3557336ab42b2c01ca8bd5ebde9143c60055dbef0
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S2-C4
          page: 3
          text_layer_sha256: fcf20fa2db34e28f034f1fb3557336ab42b2c01ca8bd5ebde9143c60055dbef0
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Aphasic participants were at least eight months post

          onset of stroke (57.2 ±52.3 months) and presented with

          aphasia based on administration of the Western Aphasia Bat-

          tery-Revised (WAB-R; [57]) and a uniform set of cross-site

          language measures.'
        anchor_text: 'Aphasic participants were at least eight months post

          onset of stroke (57.2 ±52.3 months) and presented with

          aphasia based on administration of the Western Aphasia Bat-

          tery-Revised (WAB-R; [57]) and a uniform set of cross-site

          language measures.'
        excluded_fragments: []
        image_sha256: 072e48793fe54a5275384ceec75dc4495d1f2162308b81c25fe6388daf712b07
        transcription: Aphasic participants were at least eight months post onset
          of stroke (57.2 ± 52.3 months) and presented with aphasia based on administration
          of the Western Aphasia Battery-Revised (WAB-R; [57]) and a uniform set of
          cross-site language measures
      P3-S1-C7:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: de35ad93bd93a1ae6fe470952a0b96689bee4f7dc632d682f5b2fafc18631b4c
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: a0a6c767455ca0a148155178a517523384b0b2dd1ac2929f7969dc3c911a3731
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S1-C7
          page: 3
          text_layer_sha256: a0a6c767455ca0a148155178a517523384b0b2dd1ac2929f7969dc3c911a3731
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Forty participants with aphasia (14 female)

          resulting from a single-left hemisphere stroke and 40 cogni-

          tively healthy age-matched (AM) controls (18 female) were

          recruited for the study from three research sites: Northwest-

          ern (NU), Boston (BU and MGH), and Johns Hopkins (JHU)

          Universities.'
        anchor_text: 'Forty participants with aphasia (14 female)

          resulting from a single-left hemisphere stroke and 40 cogni-

          tively healthy age-matched (AM) controls (18 female) were

          recruited for the study from three research sites: Northwest-

          ern (NU), Boston (BU and MGH), and Johns Hopkins (JHU)

          Universities.'
        excluded_fragments: []
        image_sha256: 86cc2e1978cc59cc3f5e76d8d8e680dd782a358dd4c5c2edd1a996fb6f8cd415
        transcription: '. Forty participants with aphasia (14 female) resulting from
          a single-left hemisphere stroke and 40 cognitively healthy age-matched (AM)
          controls (18 female) were recruited for the study from three research sites:
          Northwestern (NU), Boston (BU and MGH), and Johns Hopkins (JHU) Universities'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 6
  quote: 'Similarly, word semantic

    association performance was negatively associated with

    lesions in the left IFG, STG, and putamen, as well as in two

    unlabeled clusters spatially contiguous to the insula and cau-

    date (p = 0 068).'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-24'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
