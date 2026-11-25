---
id: left_temporal_complex_sentence_cluster
name: left temporal complex sentence cluster
kind: network
findings:
- id: f1
  target_audit:
    status: behaviour_label_present
    category: behaviour_or_language_construct
    original_target: complex_sentence_processing
    reason: Label names a behaviour or language construct; its exact operational definition and measurement
      still need source review.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  outcome_measurement:
    status: needs_source_review
    instruments: []
    note: Outcome instrument/task is not yet verified for this finding. Do not infer it from the predictor
      or a paper-wide test list.
  target: complex_sentence_processing
  target_kind: impairment
  claim: The processing of complex sentences (including passives, subject extraction,
    and object extraction) involved the mid-posterior left MTG and more superior portions
    of the temporal lobe such as the left STG, STS, and underlying white matter.
  direction: likely
  relationship: correlational
  method: LSM
  sample:
    n: 131
    population: right-handed left hemisphere stroke survivors with native-like English
      proficiency and more than 8 years of education
    phase: not_reported
    time_post_onset: at least 6 months post-stroke
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - CYCLE-R has a small number of test stimuli per subtest and a non-exhaustive set
    of sentence types
  - Sentence length was not controlled across sentence types
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Patient lesion overlap with a cluster comprising the
    mid-posterior left middle temporal gyrus (MTG), superior temporal gyrus (STG),
    superior temporal sulcus (STS), and underlying white matter (IFOF/ILF), measured
    via univariate lesion-symptom mapping. Analysis included covariates for age, years
    of education, months post-stroke, and lesion size; Findings were reinforced by
    multivariate LSM and an extra analysis controlling for lexical-semantic processing
    abilities. Additional metadata has not been transcribed; review the pending-field
    flags before approval. PDF image reading (P4-S3-C4, two-model agreement, human
    verification pending): Materials and methods

    Participants and measures

    Participants included 131 individuals (32 females and 99 males) who sustained
    a single left hemisphere stroke at least 6 months before being tested and scanned
    Original text-layer quotation is preserved below. Reconcile this new analysis
    with earlier drafts and source-review decisions for the paper; new candidate IDs
    do not carry earlier decisions forward.'
  imaging_details:
    reference_space: not_reported
    atlases_used: []
  lesion_mapping: {}
  provenance:
    extracted_by: model:gemma4:31b
    extracted_on: '2026-11-20'
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
    - prior_paper_decisions_reconciliation_pending
    - proposed_concept:complex_sentence_processing
  citation: '@Biondo2024'
  source_passages:
  - section: Original source P10-S1-C6
    page: 10
    quote: "Conversely, the processing of more complex sentences in­\nvolved the more\
      \ superior portions of the temporal lobe \nsuch as the left STG, STS, the mid-posterior\
      \ MTG and \nunderlying white matter (MaxLSM passives: [−38, −24, \n−6], IFOF/ILF;\
      \ subject extraction: [−34, −24, 0] IFOF \nand object extraction: [−46, −12,\
      \ −8] ILF)."
    supports: claim
  - section: Original source P4-S3-C4
    page: 4
    quote: "Materials and methods\nParticipants and measures\nParticipants included\
      \ 131 individuals (32 females and 99 \nmales) who sustained a single left hemisphere\
      \ stroke at least \n6 months before being tested and scanned."
    supports: sample
  - section: Original source P7-S1-C10
    page: 7
    quote: "Lesion–symptom mapping\nBoth univariate and multivariate LSM analyses\
      \ were con­\nducted to relate auditory comprehension performance on \nthe CYCLE-R\
      \ to underlying lesion data, using methods de­\nscribed in detail in the study\
      \ by Ivanova et al.51 Univariate \nLSM1 provides a statistical comparison of\
      \ behaviour across \npatients with and without a lesion on a voxel-by-voxel\
      \ basis."
    supports: method
  - section: Original source P7-S2-C5
    page: 7
    quote: "For the multi­\nvariate analysis, we used the support vector regression–based\
      \ \n(SVR) method with standard hyper-parameter values com­\nmonly used in the\
      \ field.70,71\nIn all LSM analyses, we included the following demo­\ngraphic\
      \ variables as covariates: age, years of education, \nmonths post-stroke and\
      \ lesion size.51,52 Analyses that \ndid not include lesion size as a covariate\
      \ are reported in \nSupplementary Table 2 and Fig. 2."
    supports: confounders
  - section: Original source P10-S1-C3
    page: 10
    quote: "The multivariate \nLSM analyses identified significant LSM clusters in\
      \ four of \nthe five sentence group analyses (see Supplementary Fig. 1 \nand\
      \ Table 1) with similar foci to the univariate analyses, pro­\nviding additional\
      \ confirmation of the findings.51\nThe results of the extra LSM analyses controlling\
      \ for \nlexical-semantic processing abilities showed smaller clusters \nbut\
      \ with similar foci, as shown in Fig. 4 (a full list of \nBrainnetome parcels\
      \ was provided in the Supplementary \nTable 3)."
    supports: claim
  - section: Original source P13-S3-C4
    page: 13
    quote: "The current study utilized the CYCLE-R, which was devel­\noped to test\
      \ comprehension on a wide range of syntactic \nstructures but has a small number\
      \ of test stimuli per subtest \nand a non-exhaustive set of sentence types."
    supports: limitation
  - section: Original source P13-S3-C5
    page: 13
    quote: "Also, although \nthe CYCLE-R controls for a number of linguistic variables\
      \ \nacross sentence types (e.g. word frequency), other variables \nare not controlled\
      \ (e.g. sentence length), thus limiting the \nability of creating controlled\
      \ minimal pairs.9 Another limita­\ntion is that our disconnection analyses relied\
      \ on indirect \nmeasures of structural disconnection, as diffusion tensor im­\n\
      aging data were only available for a subset of participants."
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-20'
relationship_review:
  paper: Biondo2024
  proposal_id: R006
  review_status_sha256: 5372ca4975f5838bd2522f0a006d61742c0d82a8c9593473410e7313d5be650a
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 95c7ba0fbcae47fa0a2b9e4464989b20bd28acf6336150aaa28d95ac1d563b83
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 95c7ba0fbcae47fa0a2b9e4464989b20bd28acf6336150aaa28d95ac1d563b83
        A/passages.json: 262c4ba9b53108c38d6640733ed04ceb6f5104d2d7c65fa8e12e97b7dbefd007
        A/raw.json: eb491f3436a0e15db8bdd003f965ce605b53039fdc0045a1dac123e3b3bf98cb
        A/source-units.json: 2fba2e07794e7504d172480c79cbf614e5bc06d888f19cdc9292b4856704e531
        A/full-source-units.json: 4cbd089c09affde0dda9dab26c28a06fdf21a3691642ea7f0dfca04d7fb68b3c
        A/meta.json: f3c809f1336121b0f4059265e80dbfb3f3e0ff7c7df5a66797b220fbffa9d66f
        A/table-images/TABLE-1-page-5-1.png: 3e68880e064d5921c67cddde8fe1265d37a15eed0c4efecd5333ce0294e1f113
        A/table-images/page-6.png: 8d441ebe1cb4c4aa85fa353290573cd66117d37f865686aa914a15ca16a2fba0
        A/table-images/TABLE-3-page-8-1.png: c5cf62004466dd410ab4f53bc37f73c7741fa540a7b59ea6a928ba323a56c8df
        A/table-images/page-5.png: aa6888983b1e82cb6534653f1a2e9e4cf7c4d98f454b82b1d1931be7d725b4ce
        A/table-images/TABLE-3-page-8-2.png: 5f425c526abe9d2315b29ce0e760809c2f885431deaad4682411c1b5dc67306a
        A/table-images/page-4.png: a603630634f3cdf88e47cc2ec2b26615ac678037b5ed09c00d731a8005f6de4c
        A/table-images/TABLE-1-page-4-1.png: aa3ba24383d863bee306f606ee3dad393b61b4952a36ca10da24bc47708d2bf2
        A/table-images/page-8.png: afc4a56ab85ae479a8fffe074af621660905ada17e35847fa1bb61273b80929a
        A/table-images/TABLE-2-page-6-1.png: d620534734b8b5471da9e1c12fd7862d7d4aa37c2663c39758cc4c6f74c495df
        A/table-images/manifest.json: 1a6d88631eea0e9318633109040a3b87c84e4097fe6d4cceb9051f8fdf8c2663
        A/clauses/window-03/raw.json: e96fcc808ebbc9de501bf2c153e7af49335520bdffb711625b4c30073ee5f700
        A/clauses/window-03/prompt.txt: 167fcab495f6f0b62af671e8d5427ba12c8b1a43b86b56ee1b6c8176fd798d9d
        A/clauses/window-03/meta.json: 0eaadbcae4ae799b0c96b771f8bc2d03cedeabece0dd0f3b3a7dbfe876496f81
        A/clauses/window-04/raw.json: 5c9fb186331f95d53eabe7ba256209088483861ec594e6eb6201debb7418e5ef
        A/clauses/window-04/prompt.txt: 128787287b1ae1f3863792491b61ec153372d6d1ad94a6ac511374469260a0db
        A/clauses/window-04/meta.json: c2f021bc359634d36b34064bcf39868cf9e86b463bc9c2d79064db939837d3be
        A/clauses/window-05/raw.json: 1dc261f316adbc3f062a9be27455021420f02d8878b8ab619d50a3511f72091f
        A/clauses/window-05/prompt.txt: becf109a27fb257d9d9c1f1df6ac0bd96281f1334e259826a3d5e6c3597d6f4a
        A/clauses/window-05/meta.json: 827fde99ee541a4dd3464e70bf6e64880e31a5ac64384ac87164b2de36398800
        A/clauses/window-02/raw.json: f1cc2300b588aa9edb25a6e82e4cce3c22c1a6ca4f4700bd349f6e030a60eec7
        A/clauses/window-02/prompt.txt: 20c995225eea25211524b0759f992df633483ccd9fb263ca21f1ead3e5468703
        A/clauses/window-02/meta.json: e643868789cb730de7d54e2ada374e5a60b450780bd96ee823e07790018ed32e
        A/clauses/window-07/raw.json: 38190d82bec9fd319209fa1e46e567b490ae4eaeaa20a68170e40ac00979f29d
        A/clauses/window-07/prompt.txt: 479054bb54409186e25f933b68f7f7eec2a75ecdea24f87b02969f245c58d45d
        A/clauses/window-07/meta.json: a4070df1631c900fa220029a66a587a703d47fef264c7748d0e34005fa91847e
        A/clauses/window-01/raw.json: 4e154dfa12ee58f72b04e89c535d4f86fc4d39d747142dc009ac27671b925fe2
        A/clauses/window-01/prompt.txt: 5909a22cd32ff02143cfebb849ce6fa456255988d703955fc8e0876c816c5ace
        A/clauses/window-01/meta.json: 6434023864406ad297e3e45387e8258afaa834c8b941365a8746d106c0c1aba7
        A/clauses/window-06/raw.json: e02cfdb7de29e5732e9df65c3a12240010de61bc587ee96e848fd7e0f051388c
        A/clauses/window-06/prompt.txt: e6ae0ee196c6fb607e306f071bf36847464bec98a7e6bca719942d20d51d07c5
        A/clauses/window-06/meta.json: f850a85ba971fb8678a997f8a69c23fb602541df4f1107c097a8bab1d240a8fb
        A/clauses/window-08/raw.json: 7b325f62c57f75abd9b9f2e7773ad3a20148e50ea586972c06634cba1b9101ce
        A/clauses/window-08/prompt.txt: 06a6bb2e8404a1b8669378be5313f0ed4ac5368244ff6fcc1fb65e0962d21762
        A/clauses/window-08/meta.json: 2f88003953ee752f922dc7ee029bfbb3312d3e029fded82a711ca5b308112216
        A/tables/TABLE-2-page-6-3/raw.json: 03278f36e1563811feb5a564f7298c001d4a662b163cea08399e5cf91ea3ee58
        A/tables/TABLE-2-page-6-3/prompt.txt: fcb1fd2fa34f027eeb18c39a631c7d38ad2b4cf9449ab16d7caf558e798ee5b8
        A/tables/TABLE-2-page-6-3/meta.json: 7e2a32202502cff6a3b5a8fecfb5963765477a02c34d56b8fcd193129cddc125
        A/tables/TABLE-3-page-8-4/raw.json: 298e2f5d30a2b72772324db8bb1f77770913ba574d477ab7c829cfde008d7190
        A/tables/TABLE-3-page-8-4/prompt.txt: 2f8a0a9bd48568b14f205db50fdef56369cd02ed6d4075f107e118602fd3d4ed
        A/tables/TABLE-3-page-8-4/meta.json: 532e465202bf1cac39afdeb4205d51ac0fe5aa2c9d227a833e362f44a38ed7cb
        A/tables/TABLE-1-page-5-2/raw.json: 7e6236cc63e4e959f5b92daacb2afa55657371ce1ceff8970344342eea2f0842
        A/tables/TABLE-1-page-5-2/prompt.txt: 04b8e3a5e0cd93f3ff3f0281e430da78acc6bf82b92e13275a940811a7be23ad
        A/tables/TABLE-1-page-5-2/meta.json: 73b7d78d7fa3314ecb6017eead37b21516f7a645c924d368e7bdc0e66aa5a892
        A/tables/TABLE-1-page-4-1/raw.json: fd48ad96d6233d8dcbca88131a03cdeb3e08ce503145b0f31e56db8e285500a4
        A/tables/TABLE-1-page-4-1/prompt.txt: ff81d5b439ccec3642d1c4cb6610133b916a19b81ee2983353063b2d1da53892
        A/tables/TABLE-1-page-4-1/meta.json: a94bda02efcb12b96521e75dee786c4ac8efb81f61a52bc69356570212badebc
        B/passages.json: 262c4ba9b53108c38d6640733ed04ceb6f5104d2d7c65fa8e12e97b7dbefd007
        B/raw.json: e16bedace8d6532183315cb435fe81b49ea586f2f2bea09c9c92e943f69aec7f
        B/source-units.json: 2fba2e07794e7504d172480c79cbf614e5bc06d888f19cdc9292b4856704e531
        B/full-source-units.json: 4cbd089c09affde0dda9dab26c28a06fdf21a3691642ea7f0dfca04d7fb68b3c
        B/meta.json: aa237166992a6cbc35a9054b2a78c7bedf6273e637ef01675f0853f7ed666b57
        B/table-images/TABLE-1-page-5-1.png: 3e68880e064d5921c67cddde8fe1265d37a15eed0c4efecd5333ce0294e1f113
        B/table-images/page-6.png: 8d441ebe1cb4c4aa85fa353290573cd66117d37f865686aa914a15ca16a2fba0
        B/table-images/TABLE-3-page-8-1.png: c5cf62004466dd410ab4f53bc37f73c7741fa540a7b59ea6a928ba323a56c8df
        B/table-images/page-5.png: aa6888983b1e82cb6534653f1a2e9e4cf7c4d98f454b82b1d1931be7d725b4ce
        B/table-images/TABLE-3-page-8-2.png: 5f425c526abe9d2315b29ce0e760809c2f885431deaad4682411c1b5dc67306a
        B/table-images/page-4.png: a603630634f3cdf88e47cc2ec2b26615ac678037b5ed09c00d731a8005f6de4c
        B/table-images/TABLE-1-page-4-1.png: aa3ba24383d863bee306f606ee3dad393b61b4952a36ca10da24bc47708d2bf2
        B/table-images/page-8.png: afc4a56ab85ae479a8fffe074af621660905ada17e35847fa1bb61273b80929a
        B/table-images/TABLE-2-page-6-1.png: d620534734b8b5471da9e1c12fd7862d7d4aa37c2663c39758cc4c6f74c495df
        B/table-images/manifest.json: 697ac90a0833f32198db5977df4b7e6416f3cfb9e51086514a07ab12ccd85bbb
        B/clauses/window-03/raw.json: adc84863ca28cc106244349956c528f83e9c37b9371cbd30a02dba0db0ca090e
        B/clauses/window-03/prompt.txt: 167fcab495f6f0b62af671e8d5427ba12c8b1a43b86b56ee1b6c8176fd798d9d
        B/clauses/window-03/meta.json: 5c7ef91236c7b99bb9a9561b03d8518af2f0ed6df34a5b89f49fb8eb69e258e9
        B/clauses/window-04/raw.json: dbfbfcbf8a9c229a3c83cce3466ff68b78c76652915c4aa911f626a98b54cfce
        B/clauses/window-04/prompt.txt: 128787287b1ae1f3863792491b61ec153372d6d1ad94a6ac511374469260a0db
        B/clauses/window-04/meta.json: cb2e4786a955109687d38bef4f1e537362b6199f59db0be0228fc1b12b78bd66
        B/clauses/window-05/raw.json: 00a81d54f6e27775e0d6ecc62f4f4c8857995c891d9dd5eaaabae6253f4cf948
        B/clauses/window-05/prompt.txt: becf109a27fb257d9d9c1f1df6ac0bd96281f1334e259826a3d5e6c3597d6f4a
        B/clauses/window-05/meta.json: 4367460cdceba451a0c629097d5f825d6fda3e391cf09587042237682feedb4d
        B/clauses/window-02/raw.json: a720182e673f6ae9475451adff1ed0eb608e2445fca7ac65b6bdf494388c334b
        B/clauses/window-02/prompt.txt: 20c995225eea25211524b0759f992df633483ccd9fb263ca21f1ead3e5468703
        B/clauses/window-02/meta.json: aed0280fec6ff0a39004169d968bcadfc380afae4dd55adf1646ada034e19842
        B/clauses/window-07/raw.json: b95d4907d7ad4d04317761cc022023e55ce14e7a4aadae7c0769de4bd8df75aa
        B/clauses/window-07/prompt.txt: 479054bb54409186e25f933b68f7f7eec2a75ecdea24f87b02969f245c58d45d
        B/clauses/window-07/meta.json: bd7e6dab7e6bc40c672de9ed59ea97f27853dc596649d178cef0cbb231584e36
        B/clauses/window-01/raw.json: 77f239056e36d9764b4056af51ab588b48293135140440224a0e795fcd4880af
        B/clauses/window-01/prompt.txt: 5909a22cd32ff02143cfebb849ce6fa456255988d703955fc8e0876c816c5ace
        B/clauses/window-01/meta.json: 42bfd33f98a81a58027009f205a917a19cdaf48d15f717b46e326a7fc9720c9b
        B/clauses/window-06/raw.json: be4025c1e35fc568742ea5024b3e380c83e7114949fd0d824bdf022997ea181b
        B/clauses/window-06/prompt.txt: e6ae0ee196c6fb607e306f071bf36847464bec98a7e6bca719942d20d51d07c5
        B/clauses/window-06/meta.json: 6cdc42a23ecc3bc94300f8dcaca65f01397abc958b3e8f9fba2de4eb8707d18b
        B/clauses/window-08/raw.json: ad86e543144d9ae0c0c3a0a4ffc6326d4bf5d54b5ebd461ed8518c6eae7db472
        B/clauses/window-08/prompt.txt: 06a6bb2e8404a1b8669378be5313f0ed4ac5368244ff6fcc1fb65e0962d21762
        B/clauses/window-08/meta.json: c465e9a39297b2f52c86edf93146af7828322ddc9bad61777841b23f56d522a4
        B/tables/TABLE-2-page-6-3/raw.json: e217bf3ca443349d0545e503bd7f9658b75f75882e4e94afd66eb08789caf26b
        B/tables/TABLE-2-page-6-3/prompt.txt: fcb1fd2fa34f027eeb18c39a631c7d38ad2b4cf9449ab16d7caf558e798ee5b8
        B/tables/TABLE-2-page-6-3/meta.json: 0e65230acde5d19358badaf48f7fda9b511593bc425008ba2e12d184f2b66835
        B/tables/TABLE-3-page-8-4/raw.json: 4fde0c0d7cfbcaf4f49c7a4a58b842637bf63990193e74b9b27192051dd094dc
        B/tables/TABLE-3-page-8-4/prompt.txt: 2f8a0a9bd48568b14f205db50fdef56369cd02ed6d4075f107e118602fd3d4ed
        B/tables/TABLE-3-page-8-4/meta.json: bd093c6572055233a91efb91d9e04fef1636bcf99e49f25c64d0314742256204
        B/tables/TABLE-1-page-5-2/raw.json: 529e17dc852f1c94b3d769703eed9ef488a1eaa19b5cabc82dfa0f94393fd264
        B/tables/TABLE-1-page-5-2/prompt.txt: 04b8e3a5e0cd93f3ff3f0281e430da78acc6bf82b92e13275a940811a7be23ad
        B/tables/TABLE-1-page-5-2/meta.json: abef333d4bfce55ec525228a8ee4d5c2dbe32efb7cb0e1e084d15927f11ce585
        B/tables/TABLE-1-page-4-1/raw.json: de70c5af62d6c624844196de8ddc8e0c578d9a738a4cfe4a684dd8cc38be0a06
        B/tables/TABLE-1-page-4-1/prompt.txt: ff81d5b439ccec3642d1c4cb6610133b916a19b81ee2983353063b2d1da53892
        B/tables/TABLE-1-page-4-1/meta.json: 24f6a2134d896440c9c228742025619109d37cd2e937a1ae0573a182579ced85
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
      pdf_sha256: 95c7ba0fbcae47fa0a2b9e4464989b20bd28acf6336150aaa28d95ac1d563b83
      source_review: _compare/relationships-2026-11-16/review-current/Biondo2024
      source_status_sha256: e791581881f60ab01930b1ad15dc18476192dadd37f574085197989397c29036
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R006
    exposure:
      text: 'mid-posterior left MTG, left STG, STS, and underlying white matter (passives:
        IFOF/ILF; subject extraction: IFOF; object extraction: anterior STS/ILF)'
    outcome:
      text: complex sentence processing
    analysis_label: Univariate LSM (Complex)
    relation: association
    evidence_ids:
    - P10-S1-C1
    - P10-S1-C6
    qualifier_ids:
    - P9-S1-C1
    - P9-S1-C2
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 95c7ba0fbcae47fa0a2b9e4464989b20bd28acf6336150aaa28d95ac1d563b83
      source_review: _compare/relationships-2026-11-16/review-current/Biondo2024
      source_status_sha256: e791581881f60ab01930b1ad15dc18476192dadd37f574085197989397c29036
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P7-S1-C2
      - Result passage disposed without unit P7-S1-C9
      - Accounting without a linked unit P8-S1-C2
      - Accounting without a linked unit P8-S1-C3
      - Accounting without a linked unit P8-S1-C4
      - Accounting without a linked unit P8-S1-C6
      - Accounting without a linked unit P8-S1-C7
      - Unaccounted source passage P8-S1-C2
      - Unaccounted source passage P8-S1-C4
      - Unaccounted source passage P8-S1-C7
      - Unaccounted source passage P8-S1-C6
      - Unaccounted source passage P8-S1-C3
      - Result passage disposed without unit P8-S1-C8
      - Accounting without a linked unit P8-S2-C2
      - Accounting without a linked unit P8-S2-C3
      - Unaccounted source passage P8-S2-C3
      - Unaccounted source passage P8-S2-C2
      - Accounting without a linked unit P10-S1-C3
      - Accounting without a linked unit P10-S1-C4
      - Accounting without a linked unit P10-S1-C5
      - Accounting without a linked unit P10-S1-C6
      - Accounting without a linked unit P10-S2-C2
      - Accounting without a linked unit P10-S2-C3
      - Accounting without a linked unit P10-S2-C4
      - Unaccounted source passage P10-S2-C4
      - Unaccounted source passage P10-S2-C3
      - Unaccounted source passage P10-S1-C6
      - Unaccounted source passage P10-S1-C5
      - Unaccounted source passage P10-S1-C3
      - Unaccounted source passage P10-S2-C2
      - Unaccounted source passage P10-S1-C4
      - Accounting without a linked unit P12-S1-C7
      - Accounting without a linked unit P12-S2-C2
      - Accounting without a linked unit P12-S2-C3
      - Accounting without a linked unit P12-S2-C4
      - Accounting without a linked unit P12-S2-C5
      - Unaccounted source passage P12-S1-C7
      - Unaccounted source passage P12-S2-C2
      - Unaccounted source passage P12-S2-C4
      - Unaccounted source passage P12-S2-C5
      - Unaccounted source passage P12-S2-C3
      - Accounting without a linked unit P13-S1-C8
      - Accounting without a linked unit P13-S1-C9
      - Accounting without a linked unit P13-S2-C4
      - Accounting without a linked unit P13-S2-C5
      - Unaccounted source passage P13-S2-C5
      - Unaccounted source passage P13-S2-C4
      - Unaccounted source passage P13-S1-C8
      - Unaccounted source passage P13-S1-C9
      unattached_null_or_qualifier_ids:
      - P7-S1-C9
      - P8-S1-C4
      - P10-S1-C3
      suppressed_nonrepresented_units: 9
      default_disposition_count_requires_completeness_check: 147
      unselected_timing_passages:
      - P4-S2-C8
      - P4-S3-C4
      - P4-S3-C5
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P10-S2-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P4-S3-C7
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      empty_frame_slots_require_confirmation:
      - validation
      - personal_factors
      - tested_personal_effects
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-4-1
      - TABLE-1-page-5-2
      - TABLE-2-page-6-3
      - TABLE-3-page-8-4
      unlinked_tables:
      - TABLE-1-page-4-1
      - TABLE-1-page-5-2
      - TABLE-2-page-6-3
      - TABLE-3-page-8-4
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P7-S1
        - P7-S2
        - P7-S3
        - P8-S1
        - P8-S2
        - P9-S1
        - P10-S1
        - P10-S2
        - P11-S1
        - P12-S2
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 95c7ba0fbcae47fa0a2b9e4464989b20bd28acf6336150aaa28d95ac1d563b83
      source_review: _compare/relationships-2026-11-16/review-current/Biondo2024
      source_status_sha256: e791581881f60ab01930b1ad15dc18476192dadd37f574085197989397c29036
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C11
      disposition: repeated
      result_indexes:
      - 3
      - 8
      reason: Abstract restatement of general sentence comprehension findings.
    - source_id: P1-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about white matter involvement.
    - source_id: P1-S2-C3
      disposition: repeated
      result_indexes:
      - 9
      - 10
      - 14
      reason: Abstract restatement of specific tract requirements for non-canonical
        sentences.
    - source_id: P5-S3-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Demographic table data.
    - source_id: P7-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of lesion overlay figure.
    - source_id: P7-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement about missing values not affecting results.
    - source_id: P8-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to Figure 2.
    - source_id: P8-S1-C2
      disposition: represented
      result_indexes:
      - 0
      reason: Direct behavioral comparison of simple vs complex sentences.
    - source_id: P8-S1-C3
      disposition: represented
      result_indexes:
      - 0
      reason: Direct behavioral comparison of complex sentence types.
    - source_id: P8-S1-C4
      disposition: represented
      result_indexes:
      - 0
      reason: Null result for subject extraction vs passives.
    - source_id: P8-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to Table 3.
    - source_id: P8-S1-C6
      disposition: represented
      result_indexes:
      - 1
      reason: Correlation between simple and non-canonical sentences.
    - source_id: P8-S1-C7
      disposition: represented
      result_indexes:
      - 1
      reason: Interpretation of simple sentence correlation.
    - source_id: P8-S1-C8
      disposition: represented
      result_indexes:
      - 2
      reason: Correlation between passives and other complex sentences.
    - source_id: P8-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to Figure 3.
    - source_id: P8-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to Supplementary Table 1.
    - source_id: P8-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Introductory sentence for LSM results.
    - source_id: P8-S2-C2
      disposition: represented
      result_indexes:
      - 3
      reason: Univariate LSM results for general comprehension.
    - source_id: P8-S2-C3
      disposition: represented
      result_indexes:
      - 4
      reason: Univariate LSM results for simple sentences.
    - source_id: P8-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to Figure 2.
    - source_id: P8-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of Figure 2.
    - source_id: P8-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of Figure 2.
    - source_id: P8-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to Table 3.
    - source_id: P10-S1-C1
      disposition: represented
      result_indexes:
      - 5
      reason: Univariate LSM results for complex sentences.
    - source_id: P10-S1-C2
      disposition: represented
      result_indexes:
      - 6
      reason: Univariate LSM result for passives (angular gyrus).
    - source_id: P10-S1-C3
      disposition: represented
      result_indexes:
      - 11
      reason: Results of extra LSM analysis controlling for lexical-semantic processing.
    - source_id: P10-S1-C4
      disposition: represented
      result_indexes:
      - 3
      reason: Univariate LSM results for all sentences.
    - source_id: P10-S1-C5
      disposition: represented
      result_indexes:
      - 4
      reason: Univariate LSM results for simple sentences.
    - source_id: P10-S1-C6
      disposition: represented
      result_indexes:
      - 5
      reason: Univariate LSM results for complex sentences.
    - source_id: P10-S1-C7
      disposition: represented
      result_indexes:
      - 11
      reason: Conclusion of extra LSM analysis.
    - source_id: P10-S2-C2
      disposition: represented
      result_indexes:
      - 7
      reason: Tract disconnection results for overall comprehension.
    - source_id: P10-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Introductory statement for nuanced tract results.
    - source_id: P10-S2-C4
      disposition: represented
      result_indexes:
      - 7
      reason: Tract disconnection results for canonical and non-canonical sentences.
    - source_id: P10-S2-C5
      disposition: represented
      result_indexes:
      - 8
      - 9
      reason: Tract disconnection results for subject and object extraction.
    - source_id: P10-S2-C6
      disposition: represented
      result_indexes:
      - 10
      reason: Null result for dorsal tracts and passives.
    - source_id: P10-S2-C7
      disposition: represented
      result_indexes:
      - 8
      - 9
      - 10
      reason: Tract disconnection results for CCMdPoeor.
    - source_id: P10-S3-C5
      disposition: repeated
      result_indexes:
      - 3
      reason: Discussion restatement of general temporal region involvement.
    - source_id: P10-S3-C8
      disposition: repeated
      result_indexes:
      - 7
      reason: Discussion restatement of general tract involvement.
    - source_id: P12-S1-C1
      disposition: repeated
      result_indexes:
      - 9
      reason: Discussion restatement of AF and object extraction.
    - source_id: P12-S1-C3
      disposition: repeated
      result_indexes:
      - 7
      reason: Discussion restatement of CCPoeor involvement.
    - source_id: P12-S1-C7
      disposition: represented
      result_indexes:
      - 15
      reason: Finding that left inferior frontal regions were not critical (standard
        analysis).
    - source_id: P12-S2-C2
      disposition: represented
      result_indexes:
      - 12
      reason: LSM result without lesion size covariate for pars orbitalis.
    - source_id: P12-S2-C3
      disposition: represented
      result_indexes:
      - 13
      reason: LSM result without lesion size covariate for pars triangularis (complex).
    - source_id: P12-S2-C4
      disposition: represented
      result_indexes:
      - 14
      reason: LSM result without lesion size covariate for pars triangularis (simple/passives).
    - source_id: P12-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Interpretation of IFG results.
    - source_id: P13-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about recruitment of different regions.
    - source_id: P13-S1-C8
      disposition: repeated
      result_indexes:
      - 4
      - 7
      reason: Discussion restatement of simple sentence correlates.
    - source_id: P13-S1-C9
      disposition: repeated
      result_indexes:
      - 8
      - 9
      reason: Discussion restatement of SLF and extraction sentences.
    - source_id: P13-S2-C4
      disposition: repeated
      result_indexes:
      - 10
      reason: Discussion restatement of passives and temporal regions.
    - source_id: P13-S2-C5
      disposition: repeated
      result_indexes:
      - 8
      - 9
      reason: Discussion restatement of frontal-temporal tracts and retrieval.
    - source_id: P13-S2-C6
      disposition: repeated
      result_indexes:
      - 9
      reason: Discussion restatement of AF and object extraction.
    - source_id: P14-S1-C10
      disposition: repeated
      result_indexes:
      - 3
      - 15
      reason: Conclusion restatement of temporal vs frontal roles.
    - source_id: P14-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: General concluding statement.
    unresolved_coverage:
    - source_id: P8-S2-C4
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P8-S2-C5
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P8-S2-C6
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P8-S2-C7
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P10-S1-C7
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P13-S1-C1
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C11
    - P1-S2-C2
    - P1-S2-C3
    - P5-S3-C1
    - P7-S1-C2
    - P7-S1-C9
    - P8-S1-C1
    - P8-S1-C5
    - P8-S1-C9
    - P8-S1-C11
    - P8-S1-C12
    - P10-S2-C3
    - P10-S3-C5
    - P10-S3-C8
    - P12-S1-C1
    - P12-S1-C3
    - P12-S2-C5
    - P13-S1-C1
    - P13-S1-C7
    - P13-S1-C8
    - P13-S1-C9
    - P13-S2-C4
    - P13-S2-C5
    - P13-S2-C6
    - P14-S1-C10
    - P14-S2-C2
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-4-1
    - TABLE-1-page-5-2
    - TABLE-2-page-6-3
    - TABLE-3-page-8-4
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P1-S1-C11
      - P4-S3-C4
      recruited_sample:
      - P4-S3-C4
      eligibility:
      - P4-S3-C5
      - P4-S3-C6
      imaging_provenance:
      - P3-S1-C1
      - P7-S1-C4
      imaging_timing:
      - P5-S1-C9
      outcome_timing:
      - P1-S1-C10
      outcome_definition:
      - P4-S3-C9
      - P5-S1-C1
      validation: []
      analysis_restrictions:
      - P7-S1-C11
      - P7-S2-C4
      - P7-S2-C5
      dependent_variable_statement:
      - P7-S1-C6
      - P7-S1-C10
      - P7-S2-C8
      limitations:
      - P13-S3-C4
      - P13-S3-C5
      - P13-S3-C6
      - P13-S3-C7
      - P14-S1-C4
      - P14-S1-C6
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P7-S2-C5
      - P7-S2-C7
      - P9-S1-C2
      - P10-S1-C3
      - P12-S2-C1
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P5-S3-C1
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P10-S2-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P4-S3-C7
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
      pdf_sha256: 95c7ba0fbcae47fa0a2b9e4464989b20bd28acf6336150aaa28d95ac1d563b83
      review_sha256: 5372ca4975f5838bd2522f0a006d61742c0d82a8c9593473410e7313d5be650a
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
      - P10-S1-C1
      - P10-S1-C6
      source_result: Univariate LSM analysis identified that the processing of complex
        sentences (passives, subject extraction, object extraction) involved the mid-posterior
        left MTG, left STG, STS, and underlying white matter (IFOF/ILF). This finding
        was robust to the inclusion of covariates (age, education, time post-stroke,
        lesion size) and confirmed by multivariate LSM and an extra analysis controlling
        for lexical-semantic processing.
      result_status: detected
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis corresponds to the univariate LSM results
            for complex sentence groups (passives, subject/object extraction) reported
            in P10-S1-C1 and P10-S1-C6. The proposed core correctly identifies this
            as a univariate LSM analysis.
          source_ids:
          - P10-S1-C1
          - P10-S1-C6
          - P7-S1-C10
        direction:
          answer: fits
          reason: The source states that complex sentence processing 'involved' the
            specified regions, implying a significant association (lesion-symptom
            mapping). The proposed core uses 'likely' and 'correlational' which is
            consistent with the observational nature of LSM, though 'detected' is
            the precise status. The direction of association (lesion in these areas
            -> impairment) is preserved.
          source_ids:
          - P10-S1-C1
          - P10-S1-C6
        construct:
          answer: fits
          reason: The exposure is correctly identified as lesion overlap in specific
            anatomical regions (MTG, STG, STS, WM). The outcome is complex sentence
            processing. The method is LSM. The patient measurement is template_lesion_overlap
            (lesions overlaid on MNI template), not patient_diffusion (diffusion was
            used for the separate disconnection mapping, not the LSM).
          source_ids:
          - P10-S1-C1
          - P10-S1-C6
          - P5-S1-C8
          - P7-S1-C3
        qualifications:
          answer: fits
          reason: 'The proposed core includes the key qualifications: covariates were
            included (P7-S2-C5), and the finding was reinforced by multivariate LSM
            and lexical-semantic control (P10-S1-C3). The limitations regarding CYCLE-R
            stimuli and sentence length are also included.'
          source_ids:
          - P7-S2-C5
          - P10-S1-C3
          - P13-S3-C4
          - P13-S3-C5
        missing_material_caveat:
          answer: fits
          reason: No material caveats are missing. The core correctly notes the covariates
            and the confirmation by other models. The limitation about indirect disconnection
            measures (P13-S3-C5) applies to the tract analysis, not the LSM, but is
            included as a general limitation which is acceptable. The distinction
            between univariate and multivariate is clear.
          source_ids:
          - P10-S1-C3
          - P13-S3-C5
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
      id: R006
      exposure:
        text: 'mid-posterior left MTG, left STG, STS, and underlying white matter
          (passives: IFOF/ILF; subject extraction: IFOF; object extraction: anterior
          STS/ILF)'
      outcome:
        text: complex sentence processing
      analysis_label: Univariate LSM (Complex)
      relation: association
      evidence_ids:
      - P10-S1-C1
      - P10-S1-C6
      qualifier_ids:
      - P9-S1-C1
      - P9-S1-C2
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 95c7ba0fbcae47fa0a2b9e4464989b20bd28acf6336150aaa28d95ac1d563b83
        source_review: _compare/relationships-2026-11-16/review-current/Biondo2024
        source_status_sha256: e791581881f60ab01930b1ad15dc18476192dadd37f574085197989397c29036
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P4-S3-C4:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 95c7ba0fbcae47fa0a2b9e4464989b20bd28acf6336150aaa28d95ac1d563b83
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: a371f8a1680b66e7417dac2454da825339f0bb06c661f9f19ec90d5b3735630c
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P4-S3-C4
          page: 4
          text_layer_sha256: a371f8a1680b66e7417dac2454da825339f0bb06c661f9f19ec90d5b3735630c
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "Materials and methods\nParticipants and measures\nParticipants\
          \ included 131 individuals (32 females and 99 \nmales) who sustained a single\
          \ left hemisphere stroke at least \n6 months before being tested and scanned."
        anchor_text: "Materials and methods\nParticipants and measures\nParticipants\
          \ included 131 individuals (32 females and 99 \nmales) who sustained a single\
          \ left hemisphere stroke at least \n6 months before being tested and scanned."
        excluded_fragments: []
        image_sha256: 73c8e8332325bb59b28a66a669fff885560df3e838e2ff2f446ec8ffffced052
        transcription: 'Materials and methods

          Participants and measures

          Participants included 131 individuals (32 females and 99 males) who sustained
          a single left hemisphere stroke at least 6 months before being tested and
          scanned'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 10
  quote: "Conversely, the processing of more complex sentences in­\nvolved the more\
    \ superior portions of the temporal lobe \nsuch as the left STG, STS, the mid-posterior\
    \ MTG and \nunderlying white matter (MaxLSM passives: [−38, −24, \n−6], IFOF/ILF;\
    \ subject extraction: [−34, −24, 0] IFOF \nand object extraction: [−46, −12, −8]\
    \ ILF)."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-20'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
