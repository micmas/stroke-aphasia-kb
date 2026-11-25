---
id: posterior_bottleneck_cluster
name: posterior bottleneck cluster
kind: network
findings:
- id: f1
  target_audit:
    status: behaviour_label_present
    category: behaviour_or_language_construct
    original_target: naming_and_auditory_semantic_processing
    reason: Label names a behaviour or language construct; its exact operational definition and measurement
      still need source review.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  outcome_measurement:
    status: needs_source_review
    instruments: []
    note: Outcome instrument/task is not yet verified for this finding. Do not infer it from the predictor
      or a paper-wide test list.
  target: naming_and_auditory_semantic_processing
  target_kind: impairment
  claim: Damage to the posterior bottleneck region is associated with impairments
    in picture naming and auditory semantic decision-making, providing unique predictive
    information beyond that attributable to concomitant cortical damage or lesion
    loads on the traversing tracts.
  direction: likely
  relationship: correlational
  method: LSM
  sample:
    n: 43
    population: chronic left hemispheric stroke patients
    phase: not_reported
    time_post_onset: at least 1 year post-stroke
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Bottleneck ROIs were defined using thresholded tract probability maps
  - Only 4 patients had damage exclusively to the posterior bottleneck ROI
  - Auditory semantic decision data were missing for 4 patients due to hardware issues
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Patient lesion overlap with a posterior bottleneck
    ROI defined by the intersection of left ILF, IFOF, and SLF/AF tract labels from
    the ICBM-DTI atlas at a 20% probability threshold. The association for naming
    and auditory semantic decisions remained significant after controlling for lesion
    volume and concomitant cortical and tract lesion loads in a hierarchical regression
    model; Findings were corroborated by SVR-LSM with direct total lesion volume control
    (DTLVC). Additional metadata has not been transcribed; review the pending-field
    flags before approval. PDF image reading (P2-S2-C3, two-model agreement, human
    verification pending): Data were collected from 43 patients with chronic left
    hemispheric

    stroke participating in different studies by our laboratory Original text-layer
    quotation is preserved below. PDF image reading (P2-S2-C5, two-model agreement,
    human verification pending): . All patients had a single left hemispheric stroke

    and received a clinical diagnosis of aphasia following the initial in-

    sult, which occurred at least 1 year prior to data collection Original text-layer
    quotation is preserved below. PDF image reading (P12-S3-C3, two-model agreement,
    human verification pending): . In addition, only 4 patients had damage to only
    the

    posterior bottleneck ROI, and so future studies that incorporate more

    patients with damage to this region are necessary to fully characterize

    its relationship to post-stroke language function Original text-layer quotation
    is preserved below.'
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
    - proposed_concept:naming_and_auditory_semantic_processing
  citation: '@Griffis2017'
  source_passages:
  - section: Original source P3-S4-C11
    page: 3
    quote: 'Next, we deﬁned a posteri-

      or bottleneck ROI according to the same procedure, but using labels for

      three of the language-relevant tracts previously identiﬁed in the poste-

      rior temporal WM: the left ILF, IFOF, and SLF/AF (Turken and Dronkers,

      2011).'
    supports: method
  - section: Original source P8-S1-C8
    page: 8
    quote: 'The full model explained signiﬁcantly more variance than

      the lesion load control model (R2 = 0.72, ΔR2 = 0.23, F1,33 = 28.03,

      p b 0.001, corrected), indicating that posterior ROI lesion status provid-

      ed unique information about naming scores even after accounting for

      concomitant cortical and tract damage.'
    supports: claim
  - section: Original source P8-S2-C4
    page: 8
    quote: 'The full model explained signiﬁcantly more variance

      than the lesion load control model (R2 = 0.50, ΔR2 = 0.16, F1,29 =

      9.28, p = 0.005, corrected), indicating that ROI lesion status provid-

      ed unique information about auditory semantic decision scores even

      after accounting for concomitant cortical and tract damage.'
    supports: claim
  - section: Original source P10-S2-C2
    page: 10
    quote: 'Naming, verbal ﬂuency, and auditory semantic decision scores were

      signiﬁcantly impaired by damage to the posterior bottleneck region

      (Figs. 3 and 4).'
    supports: claim
  - section: Original source P10-S2-C7
    page: 10
    quote: 'Our SVR-

      LSM + DTLVC analyses also found that damage to the WM in this region

      is a strong predictor of deﬁcits in all three language outcomes (Fig. 4;

      Table 1).'
    supports: claim
  - section: Original source P2-S2-C3
    page: 2
    quote: 'Data were collected from 43 patients with chronic left hemispheric

      stroke participating in different studies by our laboratory.'
    supports: sample
  - section: Original source P2-S2-C5
    page: 2
    quote: 'All patients had a single left hemispheric stroke

      and received a clinical diagnosis of aphasia following the initial in-

      sult, which occurred at least 1 year prior to data collection.'
    supports: sample
  - section: Original source P12-S2-C6
    page: 12
    quote: 'Limitations and conclusions

      A limitation of the current study is that the bottleneck ROIs were de-

      ﬁned using thresholded tract probability maps.'
    supports: limitation
  - section: Original source P12-S3-C3
    page: 12
    quote: 'In addition, only 4 patients had damage to only the

      posterior bottleneck ROI, and so future studies that incorporate more

      patients with damage to this region are necessary to fully characterize

      its relationship to post-stroke language function.'
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-24'
relationship_review:
  paper: Griffis2017
  proposal_id: R011
  review_status_sha256: 43958cb95a3b54e4f7b928dffb84af4cd8201ab009564e6c1c6243c6a956588a
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 87da389bf64f94e3d1077845f1cf612ccaada3eedeb0afb2c7ba8ca7e9aab136
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 87da389bf64f94e3d1077845f1cf612ccaada3eedeb0afb2c7ba8ca7e9aab136
        A/passages.json: a74d10e19ade4e1ec4afb95b34e36f30fd512e91493bca17fb844c703677352f
        A/raw.json: 3c7872f686e5b8e55f84d7b2f49ae87eca6fa81d43167f663b48f920d99b2b79
        A/source-units.json: 1c307f280deffe9d3b5348bf655e8fa23dda02c408213ec71199307c3a38b02d
        A/full-source-units.json: 821351c338ccab3bf2492d96c90e63b773b9e08c815d0b52028d889343d3a331
        A/meta.json: 30a27effe1eba442878f9ab35347fb142e81429f62cf45d63f7e430e9e38d0e3
        A/table-images/page-10.png: 8fd3046da41f40e08e5b5a2d625b7aedb7ac6b8b09cb129f7ad54f5464545042
        A/table-images/manifest.json: 68808f7b2542e9c9a47936606ba080120cdce375641c7761dfc06a222bc97d5a
        A/table-images/TABLE-1-page-10-1.png: 6faef615d1a9bdeed59ad447fe9fc42b2aa491d9f468f6efcd9e2195d6c117e4
        A/clauses/window-11/raw.json: ce2eb0670b54b291120633fb0f0eff5b1f6457d5eeb4d102d7e8ac77ae773057
        A/clauses/window-11/prompt.txt: 822a3d5ccc911cd036d339efb6f13577afc290758d9b9149d1d2deed0d45b423
        A/clauses/window-11/meta.json: d03568043a664af9c6fc1a4875d3e19c7322d76b136b5a9a2a558beb194525ac
        A/clauses/window-10/raw.json: 93788d8f45d651bc235cd9ee1ed7224e7405a339689ae511267c4c10c5636f56
        A/clauses/window-10/prompt.txt: f95a7486c39194419ce3675fc9cbbe7528b755a8bff8bdc0287c232280f1ce2f
        A/clauses/window-10/meta.json: 22d42d7c27822fe632a58ce33df9bc390788970720ed7f36ec2c3198fc3b8638
        A/clauses/window-03/raw.json: d0d2bb218ae5fc8ea2bc81d4b692557098baa976be6805690bdca7012fa6a280
        A/clauses/window-03/prompt.txt: f6213a29a9f0d4a442075f98a80ba26787ffc7a2c1595020843f011366d83453
        A/clauses/window-03/meta.json: 614ef7df3746fbbdee8fcd2f0ea960428cd66f9cac8dbb2822a022f9c88a975b
        A/clauses/window-04/raw.json: c3d6fb829119048d9c5d8b538f3306b11b35cb96ef7394f8e8551c5cc162338b
        A/clauses/window-04/prompt.txt: fa2fe66802cc27f3c9ea259c48134a5a96434713da4c15c9d8d9d136c58c858f
        A/clauses/window-04/meta.json: 4c2f15395c1816b1993eb721480ebf7c3e18b0fd61a2cfb94f2697839b73648d
        A/clauses/window-05/raw.json: 40109fb682d17d18d108e5f0f53bd285ff66ca32e930ab15e52fbe390d482c88
        A/clauses/window-05/prompt.txt: 455d04411f6d4a2a42e56e3b942a400589f2484f0e92dd942e01780f8c1947e5
        A/clauses/window-05/meta.json: e79d4abc9d5b85c77d7d05ac588e7e0e37cb323c1de4024861a4f5de1da38e89
        A/clauses/window-02/raw.json: 89890d732a97d80842f837dcf47b14a4798443ab45e93778c4a6e3f097d8e181
        A/clauses/window-02/prompt.txt: aea0e2f1c2f168abe4d3f0974afa27c4ac38bcc6a598ddfdd61ee80eacfab2d5
        A/clauses/window-02/meta.json: c0c11b0b57223c469d71e07574e454dca0788c1712fc3c25e04a2128c0cbd3bd
        A/clauses/window-12/raw.json: 9cdd3965c6fbed42edb0d773540beabe1c7b98d9a0f2ee1d3c7cf3c5f15b5a44
        A/clauses/window-12/prompt.txt: 492233d7e83f416ebf4450fbd633d3df5c6a23ddb0536e3ea21ead83dbfe691a
        A/clauses/window-12/meta.json: 6dfbd16e564bcaec4bd287ad6ba6dc292e12fc5360b8e2b6faf811cdb6a5cfae
        A/clauses/window-09/raw.json: d9c397a273b7e16f888f157f75b5d71187cbe8464284c9b79b2f0914e1972948
        A/clauses/window-09/prompt.txt: 4d6fb0b44226711c47eeced51117da6ddbd1602018a1f9e6d13d556140f5fe60
        A/clauses/window-09/meta.json: 38e7b22e2e647189ad386b7b49d4d6b4ea1c765c1a01312f613fc1b5a443cc13
        A/clauses/window-07/raw.json: 5ec6d82e9773132369f720a2d234ba7c2ef7df9cadf246732c1e98fabc449ebf
        A/clauses/window-07/prompt.txt: ac49c424a3ca213c2fe3c3a04c77c73ae51ab47fbde7192f67fc50fb947599cc
        A/clauses/window-07/meta.json: 5954f20f0a344469072dbdbc1cf8f1d9b56e494ebadd3ea4d3bd05978de2adcb
        A/clauses/window-01/raw.json: 4be963b582bd75a70fd0a31b39bc8bf4bb3c5f780e9d6914a336790387524f01
        A/clauses/window-01/prompt.txt: 4f890e6818566160dd7d902caf1ee7fcd2911bb104d392ec851df64a2a27cb85
        A/clauses/window-01/meta.json: d7f87bc28f27e438489437bfcdbf5b3882a63bbf58e4dc7def2fe7dcd1e1be6c
        A/clauses/window-06/raw.json: 276d08682a550aa932ac485313f7c65e2a8156a0f22877c642fe61ecee5dd940
        A/clauses/window-06/prompt.txt: 0477994774860247ed6862beb675260650a44c66fdc0b1cd287af0dcaaf806d1
        A/clauses/window-06/meta.json: 49d9cf22c5fca5f55bc94707f8a0d3e3887d555925153fa0506d0a8efd812c2c
        A/clauses/window-08/raw.json: a8e2507cc11a8996e9501d9612dd810e6d398c4256eac65642ff2e866c38589a
        A/clauses/window-08/prompt.txt: b93a49a6de8b13cf09e8657a4d9eb942fd1de352d26413db3b55b58f77ac7b8f
        A/clauses/window-08/meta.json: 161629618faf73448a9ded4454cfec4330485cb51f874ee6359fe17582a11464
        A/tables/TABLE-1-page-10-1/raw.json: 83ebe1acde88714e2c4826ef354c545cde0fd919410279e9bead72fd7a25933f
        A/tables/TABLE-1-page-10-1/prompt.txt: 70323986a31777e5f237e571d4661cdd27fab1ddb13145828da564ea1cdd7cbe
        A/tables/TABLE-1-page-10-1/meta.json: 991af5108901d27a09508c73575efb263830cad7dd1ceaac77a37b8be4450d53
        B/passages.json: a74d10e19ade4e1ec4afb95b34e36f30fd512e91493bca17fb844c703677352f
        B/raw.json: 0b6337487b35071c0e5a1c34cd6e7617a3c4e2c111be26286335c9bc4645e236
        B/source-units.json: 1c307f280deffe9d3b5348bf655e8fa23dda02c408213ec71199307c3a38b02d
        B/full-source-units.json: 821351c338ccab3bf2492d96c90e63b773b9e08c815d0b52028d889343d3a331
        B/meta.json: 6ea070d83cae3f718d771383bc3257e6d506c7a8e3961b903b64d1264258be7e
        B/table-images/page-10.png: 8fd3046da41f40e08e5b5a2d625b7aedb7ac6b8b09cb129f7ad54f5464545042
        B/table-images/manifest.json: cd0dde2550cc84f60573062ace6aa6ac56d1ff3793a317cc3beb44030a17654e
        B/table-images/TABLE-1-page-10-1.png: 6faef615d1a9bdeed59ad447fe9fc42b2aa491d9f468f6efcd9e2195d6c117e4
        B/clauses/window-11/raw.json: cbdb0b039bd7f9cfc21112e5c1b5b6a2751f91a7d0321e3375d49cce3434293b
        B/clauses/window-11/prompt.txt: 822a3d5ccc911cd036d339efb6f13577afc290758d9b9149d1d2deed0d45b423
        B/clauses/window-11/meta.json: 4be6fcdb32d086b9e6e2f13503d24b6f65076b857bf3f1f82f5c93fe5c53050b
        B/clauses/window-10/raw.json: f773a9dfbac5eca275dd747afd5a0b740b828d3ae0d543096f6e56c2490f8151
        B/clauses/window-10/prompt.txt: f95a7486c39194419ce3675fc9cbbe7528b755a8bff8bdc0287c232280f1ce2f
        B/clauses/window-10/meta.json: c1ed871adaf7bc5145f4ea1592083cf74454f9102d27d97cd3c9bfa64291807c
        B/clauses/window-03/raw.json: 5cfb7176563e62834883684ff9a1c9d9850ffabf56e20a8fcd8b5475cff5416c
        B/clauses/window-03/prompt.txt: f6213a29a9f0d4a442075f98a80ba26787ffc7a2c1595020843f011366d83453
        B/clauses/window-03/meta.json: 35b3796e17ed0c6d7f12c7f702ef5c071c2998b65c7d70f791d223559e75f1c7
        B/clauses/window-04/raw.json: 5427c0b3d4a94d400405eb0c0a07f21e6d23823313cd1ace6d6d183412ad4096
        B/clauses/window-04/prompt.txt: fa2fe66802cc27f3c9ea259c48134a5a96434713da4c15c9d8d9d136c58c858f
        B/clauses/window-04/meta.json: b7c9c381d08b068062aa794b86bdbf63ccab20160ea48f1c102cc6669789e56d
        B/clauses/window-05/raw.json: 9f97a7160507f41a11bfe2f4371b31dcb0593a08e5379d38f9b7483049a5bbce
        B/clauses/window-05/prompt.txt: 455d04411f6d4a2a42e56e3b942a400589f2484f0e92dd942e01780f8c1947e5
        B/clauses/window-05/meta.json: 8daf1e1564f8398335b42deaa209529dc84abe9da4f6fa506456770d30c0a2ca
        B/clauses/window-02/raw.json: 4a597c168147d1816cb25e4920e3344eba7b4e2cc26febf12717a6a5027c00f0
        B/clauses/window-02/prompt.txt: aea0e2f1c2f168abe4d3f0974afa27c4ac38bcc6a598ddfdd61ee80eacfab2d5
        B/clauses/window-02/meta.json: f5e4e4301b0ec37023aad3d213627e516d5f7f9f64ac0f1d816079236e14cc18
        B/clauses/window-12/raw.json: ed782cd7fef3669ba9d1ff057d6b5e2197ad25fced67963c5a8fcadd18c1026e
        B/clauses/window-12/prompt.txt: 492233d7e83f416ebf4450fbd633d3df5c6a23ddb0536e3ea21ead83dbfe691a
        B/clauses/window-12/meta.json: 075e228bda4f17ec75c47896949a76764d1909251b0c3cb1b4c69abab8d01593
        B/clauses/window-09/raw.json: 47d2f64feafc32bf70c8c36e899cae6952a516b84140cd2ddb72abff569a04ee
        B/clauses/window-09/prompt.txt: 4d6fb0b44226711c47eeced51117da6ddbd1602018a1f9e6d13d556140f5fe60
        B/clauses/window-09/meta.json: 089b9c97cf66e9e993422d1bb2fd410a702600bb471e4b7ac2c35347bc1e2510
        B/clauses/window-07/raw.json: 6550847a094d4c52c444cbeeb5633477195c900b3fbae0610a4ad131d4b52aa2
        B/clauses/window-07/prompt.txt: ac49c424a3ca213c2fe3c3a04c77c73ae51ab47fbde7192f67fc50fb947599cc
        B/clauses/window-07/meta.json: 736e51966045d247e0d139c9614c7136ef71eb48d0ad84f1b4d24d1825e75dbd
        B/clauses/window-01/raw.json: 8d48014645284f6ad4ac3823185a6c7133396f451d92698eb625ce4e7d6afe49
        B/clauses/window-01/prompt.txt: 4f890e6818566160dd7d902caf1ee7fcd2911bb104d392ec851df64a2a27cb85
        B/clauses/window-01/meta.json: e5aa464abb089f7c9e8aaed1432e0861e1d11cd0988727cad0123b00b5912af3
        B/clauses/window-06/raw.json: 1f936952f6df774857ebcbf8973172dd83653c75fd52be987cb5c3a067ff663a
        B/clauses/window-06/prompt.txt: 0477994774860247ed6862beb675260650a44c66fdc0b1cd287af0dcaaf806d1
        B/clauses/window-06/meta.json: 8e48b6cf48aab3c404a55da125e705971f0dac6315986cd40fdf205410bdf5fa
        B/clauses/window-08/raw.json: 9a2a65222880a69d2d85791a805f67656ebee16c277f75bb20f2b74d3aefb9bd
        B/clauses/window-08/prompt.txt: b93a49a6de8b13cf09e8657a4d9eb942fd1de352d26413db3b55b58f77ac7b8f
        B/clauses/window-08/meta.json: e02c1bea21c86516db6893c86d79e35340f17ba61d2795ab9d82539d8d63125e
        B/tables/TABLE-1-page-10-1/raw.json: 25a0cece33ab84fabd54ea582b418b3b2cc296d4402299b963d9b11dff0187ac
        B/tables/TABLE-1-page-10-1/prompt.txt: 70323986a31777e5f237e571d4661cdd27fab1ddb13145828da564ea1cdd7cbe
        B/tables/TABLE-1-page-10-1/meta.json: 262a513270faace3ed0c0048bcfff1402d21d22a767e45a7a8e9c80d283a20e8
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
      pdf_sha256: 87da389bf64f94e3d1077845f1cf612ccaada3eedeb0afb2c7ba8ca7e9aab136
      source_review: _compare/relationships-2026-11-16/review-current/Griffis2017
      source_status_sha256: bbf3c0991b2fffcac805aeb03b5e92358b8e6df0e138e37268aa1caadfbe6c6f
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R011
    exposure:
      text: posterior bottleneck ROI damage
    outcome:
      text: verbal fluency, naming, and auditory semantic decision
    analysis_label: SVR-LSM + DTLVC
    relation: association
    evidence_ids:
    - P9-S1-C1
    - P10-S2-C7
    qualifier_ids:
    - P8-S2-C6
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 87da389bf64f94e3d1077845f1cf612ccaada3eedeb0afb2c7ba8ca7e9aab136
      source_review: _compare/relationships-2026-11-16/review-current/Griffis2017
      source_status_sha256: bbf3c0991b2fffcac805aeb03b5e92358b8e6df0e138e37268aa1caadfbe6c6f
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - 'window 1: invalid/duplicate disposition P1-S1-C10'
      - Result passage disposed without unit P1-S1-C10
      - Result passage disposed without unit P1-S1-C11
      - Result passage disposed without unit P1-S1-C12
      - Result passage disposed without unit P3-S2-C12
      - Result passage disposed without unit P5-S4-C9
      - Result passage disposed without unit P6-S3-C11
      - Result passage disposed without unit P6-S4-C2
      - Result passage disposed without unit P6-S4-C3
      - Result passage disposed without unit P8-S2-C6
      - Result passage disposed without unit P10-S1-C10
      - Result passage disposed without unit P10-S2-C8
      - Result passage disposed without unit P10-S4-C1
      - Result passage disposed without unit P11-S1-C5
      - Accounting without a linked unit P11-S2-C4
      - Result passage disposed without unit P11-S3-C3
      - Result passage disposed without unit P11-S3-C8
      - Result passage disposed without unit P11-S4-C3
      - Result passage disposed without unit P11-S4-C4
      - Unaccounted source passage P11-S2-C4
      - Result passage disposed without unit P11-S5-C2
      - Result passage disposed without unit P11-S5-C3
      - Result passage disposed without unit P12-S1-C2
      - Accounting without a linked unit P12-S1-C8
      - Result passage disposed without unit P12-S2-C8
      - Result passage disposed without unit P12-S2-C9
      - Unaccounted source passage P12-S1-C8
      unattached_null_or_qualifier_ids:
      - P5-S3-C9
      - P5-S4-C9
      suppressed_nonrepresented_units: 22
      default_disposition_count_requires_completeness_check: 262
      unselected_timing_passages:
      - P1-S1-C8
      - P2-S2-C3
      - P12-S2-C11
      - P12-S3-C3
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P5-S3-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S3-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S3-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S3-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S3-C12
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S4-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S4-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S4-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S4-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S4-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C12
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C13
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S2-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S2-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S2-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S2-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S2-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S2-C12
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S2-C14
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S2-C15
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S1-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S1-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S1-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S1-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S2-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S2-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S2-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P5-S4-C8
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: limitations
        source_ids:
        - P12-S2-C6
        - P12-S2-C7
        - P12-S2-C10
        - P12-S2-C11
        - P12-S2-C11
        - P12-S3-C2
        - P12-S3-C3
        - P12-S3-C4
        - P12-S3-C5
        - P12-S3-C6
        - P12-S3-C7
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: adjustment_roles
        source_ids:
        - P2-S1-C9
        - P2-S1-C10
        - P5-S2-C8
        - P5-S2-C9
        - P5-S3-C7
        - P5-S3-C8
        - P5-S3-C11
        - P5-S3-C12
        - P5-S4-C5
        - P5-S4-C6
        - P5-S4-C9
        - P6-S1-C4
        - P6-S1-C5
        - P6-S1-C7
        - P8-S1-C5
        - P8-S1-C6
        - P8-S1-C12
        - P8-S1-C13
        - P8-S2-C1
        - P8-S2-C4
        - P8-S2-C5
        - P8-S2-C11
        - P8-S2-C12
        - P8-S2-C14
        - P8-S2-C15
        - P10-S1-C9
        - P12-S1-C2
        - P12-S1-C4
        - P12-S1-C8
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - limitations
      - personal_factors
      - tested_personal_effects
      - adjustment_roles
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-10-1
      unlinked_tables: []
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P2-S2
        - P2-S3
        - P3-S1
        - P3-S4
        - P4-S1
        - P5-S2
        - P6-S4
        - P6-S5
        - P7-S1
        - P8-S1
        - P8-S2
        - P9-S1
        - P10-S1
        - P10-S2
        - P10-S3
        - P10-S4
        - P11-S1
        - P11-S2
        - P11-S4
        - P12-S1
        - P12-S2
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 87da389bf64f94e3d1077845f1cf612ccaada3eedeb0afb2c7ba8ca7e9aab136
      source_review: _compare/relationships-2026-11-16/review-current/Griffis2017
      source_status_sha256: bbf3c0991b2fffcac805aeb03b5e92358b8e6df0e138e37268aa1caadfbe6c6f
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Hypothesis regarding bottleneck vulnerability.
    - source_id: P1-S1-C9
      disposition: repeated
      result_indexes:
      - 0
      - 1
      - 2
      - 3
      - 4
      - 5
      - 6
      - 7
      - 8
      - 9
      - 10
      - 11
      - 12
      - 13
      reason: Abstract summary of results.
    - source_id: P1-S1-C10
      disposition: repeated
      result_indexes:
      - 3
      - 6
      - 9
      reason: Abstract summary of sensitivity results.
    - source_id: P1-S1-C11
      disposition: repeated
      result_indexes:
      - 10
      - 11
      - 12
      - 13
      reason: Abstract summary of SVR-LSM results.
    - source_id: P1-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Mention of post-hoc fiber tracking consistency.
    - source_id: P2-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient clinical status description.
    - source_id: P3-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Task confirmation procedure.
    - source_id: P3-S2-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Correlation between fluency tasks.
    - source_id: P3-S4-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Correlation between language test scores.
    - source_id: P3-S4-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Correlation between language test scores.
    - source_id: P3-S4-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to Figure 1B.
    - source_id: P4-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: ROI voxel counts.
    - source_id: P5-S3-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Lesion load calculation method.
    - source_id: P5-S4-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to supplementary control analyses.
    - source_id: P6-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: SVR-LSM ROI creation method.
    - source_id: P6-S3-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Data transformation for homoscedasticity.
    - source_id: P6-S4-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Data transformation for homoscedasticity.
    - source_id: P6-S4-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Correlation between transformed and untransformed scores.
    - source_id: P6-S4-C4
      disposition: represented
      result_indexes:
      - 0
      - 1
      - 2
      reason: Model significance for verbal fluency.
    - source_id: P6-S4-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Untransformed score model performance.
    - source_id: P6-S4-C6
      disposition: represented
      result_indexes:
      - 0
      - 1
      - 2
      reason: Unique predictors for verbal fluency.
    - source_id: P6-S4-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Lesion load control model performance.
    - source_id: P6-S4-C11
      disposition: represented
      result_indexes:
      - 3
      reason: Full model improvement for verbal fluency.
    - source_id: P8-S1-C2
      disposition: represented
      result_indexes:
      - 4
      - 5
      reason: Model significance for naming.
    - source_id: P8-S1-C3
      disposition: represented
      result_indexes:
      - 4
      - 5
      reason: Unique predictors for naming.
    - source_id: P8-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Lesion load control model performance for naming.
    - source_id: P8-S1-C8
      disposition: represented
      result_indexes:
      - 6
      reason: Full model improvement for naming.
    - source_id: P8-S1-C10
      disposition: represented
      result_indexes:
      - 7
      - 8
      reason: Model significance for auditory semantic decisions.
    - source_id: P8-S1-C11
      disposition: represented
      result_indexes:
      - 7
      - 8
      reason: Unique predictors for auditory semantic decisions.
    - source_id: P8-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Control model non-significance for auditory semantic decisions.
    - source_id: P8-S2-C4
      disposition: represented
      result_indexes:
      - 9
      reason: Full model improvement for auditory semantic decisions.
    - source_id: P8-S2-C6
      disposition: represented
      result_indexes:
      - 10
      - 11
      - 12
      - 13
      reason: SVR-LSM results reference.
    - source_id: P9-S1-C1
      disposition: represented
      result_indexes:
      - 10
      - 11
      - 12
      reason: SVR-LSM overlap with bottleneck ROIs.
    - source_id: P10-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of ROI analysis goals.
    - source_id: P10-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Consistency between SVR-LSM and ROI analyses.
    - source_id: P10-S2-C2
      disposition: repeated
      result_indexes:
      - 10
      - 11
      - 12
      reason: Discussion summary of posterior bottleneck effects.
    - source_id: P10-S2-C7
      disposition: represented
      result_indexes:
      - 10
      - 11
      - 12
      reason: SVR-LSM results for posterior bottleneck.
    - source_id: P10-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Post-hoc fiber tracking results.
    - source_id: P10-S3-C3
      disposition: represented
      result_indexes:
      - 11
      reason: Null result for anterior bottleneck on naming/auditory semantic processing.
    - source_id: P10-S3-C5
      disposition: represented
      result_indexes:
      - 11
      reason: Association between anterior bottleneck and verbal fluency.
    - source_id: P10-S3-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Near-significance of anterior bottleneck on auditory semantic decisions.
    - source_id: P10-S4-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Near-significance of anterior bottleneck on auditory semantic decisions.
    - source_id: P10-S4-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: SVR-LSM peak table.
    - source_id: P11-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to supplementary analyses.
    - source_id: P11-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: SVR-LSM peak overlap with anterior bottleneck.
    - source_id: P11-S2-C4
      disposition: represented
      result_indexes:
      - 13
      reason: SVR-LSM associations for cortical hubs.
    - source_id: P11-S4-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to previous studies on cortical hubs.
    - source_id: P11-S4-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of semantic vs letter fluency.
    - source_id: P11-S5-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to previous studies on anterior temporal lobe.
    - source_id: P11-S5-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of semantic network recruitment.
    - source_id: P12-S1-C2
      disposition: repeated
      result_indexes:
      - 3
      - 6
      - 9
      reason: Discussion summary of sensitivity results.
    - source_id: P12-S2-C1
      disposition: repeated
      result_indexes:
      - 3
      - 6
      - 9
      reason: Discussion summary of sensitivity results.
    - source_id: P12-S3-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of chronic patient limitation.
    - source_id: P12-S3-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Need for longitudinal studies.
    unresolved_coverage:
    - source_id: P10-S4-C3
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P11-S4-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P11-S4-C2
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P11-S5-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P12-S2-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P12-S3-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P12-S3-C2
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P9-S1-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S3-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S3-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S4-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S4-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S5-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S1-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S2-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S2-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S3-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S3-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C5
    - P1-S1-C9
    - P1-S1-C10
    - P1-S1-C11
    - P1-S1-C12
    - P2-S2-C6
    - P3-S2-C10
    - P3-S2-C12
    - P3-S4-C3
    - P3-S4-C4
    - P3-S4-C5
    - P4-S1-C4
    - P5-S3-C9
    - P5-S4-C9
    - P6-S2-C5
    - P6-S3-C11
    - P6-S4-C2
    - P6-S4-C3
    - P6-S4-C4
    - P6-S4-C5
    - P6-S4-C9
    - P8-S1-C2
    - P8-S1-C6
    - P8-S1-C10
    - P8-S2-C2
    - P8-S2-C6
    - P9-S1-C2
    - P10-S1-C9
    - P10-S1-C10
    - P10-S2-C2
    - P10-S2-C8
    - P10-S3-C8
    - P10-S4-C1
    - P11-S1-C1
    - P11-S1-C3
    - P11-S1-C5
    - P11-S3-C3
    - P11-S3-C8
    - P11-S4-C3
    - P11-S4-C4
    - P11-S5-C2
    - P11-S5-C3
    - P12-S1-C2
    - P12-S1-C8
    - P12-S2-C8
    - P12-S2-C9
    - P12-S3-C10
    - P12-S3-C11
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-10-1
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P2-S2-C3
      - P2-S2-C11
      recruited_sample:
      - P2-S2-C3
      eligibility:
      - P2-S2-C4
      - P2-S2-C5
      imaging_provenance:
      - P3-S1-C2
      - P3-S1-C4
      - P6-S3-C3
      imaging_timing:
      - P2-S2-C5
      outcome_timing:
      - P2-S2-C5
      outcome_definition:
      - P3-S1-C11
      - P3-S1-C12
      - P3-S1-C13
      - P3-S1-C14
      - P3-S1-C15
      - P3-S2-C5
      - P3-S2-C8
      validation:
      - P6-S2-C2
      analysis_restrictions:
      - P6-S1-C7
      - P6-S1-C8
      dependent_variable_statement:
      - P5-S2-C4
      - P5-S2-C5
      - P5-S2-C8
      - P5-S2-C9
      limitations: []
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles: []
      explicitly_not_adjusted:
      - P5-S5-C3
      descriptive_personal_factors:
      - P2-S2-C9
      - P2-S2-C12
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: internal_cross_validation
    held_selections:
    - slot: dependent_variable_statement
      source_id: P5-S3-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S3-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S3-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S3-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S3-C12
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S4-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S4-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S4-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S4-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S4-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C12
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C13
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S2-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S2-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S2-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S2-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S2-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S2-C12
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S2-C14
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S2-C15
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S1-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S1-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S1-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S1-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S2-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S2-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S2-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P5-S4-C8
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: limitations
      source_ids:
      - P12-S2-C6
      - P12-S2-C7
      - P12-S2-C10
      - P12-S2-C11
      - P12-S2-C11
      - P12-S3-C2
      - P12-S3-C3
      - P12-S3-C4
      - P12-S3-C5
      - P12-S3-C6
      - P12-S3-C7
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: adjustment_roles
      source_ids:
      - P2-S1-C9
      - P2-S1-C10
      - P5-S2-C8
      - P5-S2-C9
      - P5-S3-C7
      - P5-S3-C8
      - P5-S3-C11
      - P5-S3-C12
      - P5-S4-C5
      - P5-S4-C6
      - P5-S4-C9
      - P6-S1-C4
      - P6-S1-C5
      - P6-S1-C7
      - P8-S1-C5
      - P8-S1-C6
      - P8-S1-C12
      - P8-S1-C13
      - P8-S2-C1
      - P8-S2-C4
      - P8-S2-C5
      - P8-S2-C11
      - P8-S2-C12
      - P8-S2-C14
      - P8-S2-C15
      - P10-S1-C9
      - P12-S1-C2
      - P12-S1-C4
      - P12-S1-C8
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
      pdf_sha256: 87da389bf64f94e3d1077845f1cf612ccaada3eedeb0afb2c7ba8ca7e9aab136
      review_sha256: 43958cb95a3b54e4f7b928dffb84af4cd8201ab009564e6c1c6243c6a956588a
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
      - P10-S2-C7
      - P9-S1-C1
      source_result: The SVR-LSM + DTLVC analysis identified significant lesion predictors
        for deficits in verbal fluency, naming, and auditory semantic decisions. Specifically,
        the posterior bottleneck ROI overlapped with the significant maps for naming
        and auditory semantic decisions, corroborating the a priori findings that
        damage to this region is associated with impairments in these outcomes. The
        analysis controlled for total lesion volume using the DTLVC option.
      result_status: detected
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis R011 specifies 'SVR-LSM + DTLVC' and the source
            P10-S2-C7 explicitly discusses the results of 'SVR-LSM + DTLVC analyses'
            finding that damage to the posterior region is a strong predictor. P9-S1-C1
            confirms the overlap of the posterior ROI with the SVR-LSM maps for naming
            and auditory semantic decisions.
          source_ids:
          - P10-S2-C7
          - P9-S1-C1
        direction:
          answer: fits
          reason: The source states that damage to the posterior bottleneck region
            is associated with 'deficits' and 'impairments' in the language measures
            (P10-S2-C2, P10-S2-C7). The proposed core claims an association with 'impairments',
            which preserves the direction of the detected effect (damage -> worse
            performance).
          source_ids:
          - P10-S2-C2
          - P10-S2-C7
        construct:
          answer: fits
          reason: The exposure is correctly identified as damage to the posterior
            bottleneck ROI (defined by ILF, IFOF, SLF/AF intersection in P3-S4-C11).
            The outcomes are naming and auditory semantic decision (P1-S1-C8, P8-S1-C2,
            P8-S1-C10). The method is SVR-LSM + DTLVC (P6-S1-C2, P6-S1-C4). The patient
            measurement is template_lesion_overlap because the analysis uses patient
            lesion masks overlaid on the brain to find voxels/regions predicting behavior,
            not patient-specific diffusion tractography (which was exploratory and
            used a healthy template, P6-S3-C2).
          source_ids:
          - P3-S4-C11
          - P6-S1-C2
          - P6-S1-C4
          - P8-S1-C2
          - P8-S1-C10
        qualifications:
          answer: fits
          reason: The proposed core includes the qualification that findings were
            corroborated by SVR-LSM + DTLVC. It also mentions controlling for lesion
            volume (DTLVC). While the core focuses on the SVR-LSM result, the source
            P10-S2-C7 explicitly links the SVR-LSM findings to the a priori ROI results.
            The core does not falsely claim the SVR-LSM result was the *only* analysis,
            but rather that it corroborates the association. The limitation regarding
            the small number of patients with exclusive posterior damage (P12-S3-C3)
            is included.
          source_ids:
          - P10-S2-C7
          - P12-S3-C3
          - P6-S1-C4
        missing_material_caveat:
          answer: fits
          reason: The core includes the limitation that ROIs were defined using thresholded
            tract probability maps (P12-S2-C6) and the small sample size for exclusive
            posterior damage (P12-S3-C3). It also notes the missing data for auditory
            semantic decisions (P3-S2-C11). No material caveat that changes the interpretation
            of the association is omitted. The distinction between the a priori ROI
            analysis and the data-driven SVR-LSM analysis is maintained by the analysis
            label and the corroboration language.
          source_ids:
          - P12-S2-C6
          - P12-S3-C3
          - P3-S2-C11
      optional_pending:
      - Specific cluster coordinates or peak values from Table 1 are not transcribed.
      - Exact F-statistics or p-values for the SVR-LSM clusters are not transcribed.
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Specific cluster coordinates or peak values from Table 1 are not transcribed.
    - Exact F-statistics or p-values for the SVR-LSM clusters are not transcribed.
    normalizations: []
    analysis_identity:
      id: R011
      exposure:
        text: posterior bottleneck ROI damage
      outcome:
        text: verbal fluency, naming, and auditory semantic decision
      analysis_label: SVR-LSM + DTLVC
      relation: association
      evidence_ids:
      - P9-S1-C1
      - P10-S2-C7
      qualifier_ids:
      - P8-S2-C6
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 87da389bf64f94e3d1077845f1cf612ccaada3eedeb0afb2c7ba8ca7e9aab136
        source_review: _compare/relationships-2026-11-16/review-current/Griffis2017
        source_status_sha256: bbf3c0991b2fffcac805aeb03b5e92358b8e6df0e138e37268aa1caadfbe6c6f
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P8-S1-C8:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 87da389bf64f94e3d1077845f1cf612ccaada3eedeb0afb2c7ba8ca7e9aab136
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 08fe5873d28cb7212900544c11dd7f92fafb5150378c6832fef4dc8bfb4f8531
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P8-S1-C8
          page: 8
          text_layer_sha256: 08fe5873d28cb7212900544c11dd7f92fafb5150378c6832fef4dc8bfb4f8531
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: 'The full model explained signiﬁcantly more variance than

          the lesion load control model (R2 = 0.72, ΔR2 = 0.23, F1,33 = 28.03,

          p b 0.001, corrected), indicating that posterior ROI lesion status provid-

          ed unique information about naming scores even after accounting for

          concomitant cortical and tract damage.'
        anchor_text: 'The full model explained signiﬁcantly more variance than

          the lesion load control model (R2 = 0.72, ΔR2 = 0.23, F1,33 = 28.03,

          p b 0.001, corrected), indicating that posterior ROI lesion status provid-

          ed unique information about naming scores even after accounting for

          concomitant cortical and tract damage.'
        excluded_fragments: []
        image_sha256: e400fceee6589a77e18762d83cdc393a7fd55433f1598f0f3ca8e3d1be2563fb
      P2-S2-C3:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 87da389bf64f94e3d1077845f1cf612ccaada3eedeb0afb2c7ba8ca7e9aab136
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: d8b56d45fffb247c6fee04e54fbe5822f7d96e9a87af62ed90fbc3fbe3c69d70
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S2-C3
          page: 2
          text_layer_sha256: d8b56d45fffb247c6fee04e54fbe5822f7d96e9a87af62ed90fbc3fbe3c69d70
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Data were collected from 43 patients with chronic left hemispheric

          stroke participating in different studies by our laboratory.'
        anchor_text: 'Data were collected from 43 patients with chronic left hemispheric

          stroke participating in different studies by our laboratory.'
        excluded_fragments: []
        image_sha256: c6ec10690554323c3a520f770dc5c54da74b32b0af4ff89ea66b6cb578bdeada
        transcription: 'Data were collected from 43 patients with chronic left hemispheric

          stroke participating in different studies by our laboratory'
      P2-S2-C5:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 87da389bf64f94e3d1077845f1cf612ccaada3eedeb0afb2c7ba8ca7e9aab136
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 6db7ad17f7d4353d36e2ab7dd49dcbe79eee96bcc92782a9b1a4a3918b5eb463
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S2-C5
          page: 2
          text_layer_sha256: 6db7ad17f7d4353d36e2ab7dd49dcbe79eee96bcc92782a9b1a4a3918b5eb463
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'All patients had a single left hemispheric stroke

          and received a clinical diagnosis of aphasia following the initial in-

          sult, which occurred at least 1 year prior to data collection.'
        anchor_text: 'All patients had a single left hemispheric stroke

          and received a clinical diagnosis of aphasia following the initial in-

          sult, which occurred at least 1 year prior to data collection.'
        excluded_fragments: []
        image_sha256: 44b972e40c47eaf734599636fe863c5936cdf9423a08a3a51961b90ba0d624dd
        transcription: '. All patients had a single left hemispheric stroke

          and received a clinical diagnosis of aphasia following the initial in-

          sult, which occurred at least 1 year prior to data collection'
      P12-S3-C3:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 87da389bf64f94e3d1077845f1cf612ccaada3eedeb0afb2c7ba8ca7e9aab136
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 645ff7522c54e80225a9af1bdea903862fe49c66a252e6f75d675f05dcc69501
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P12-S3-C3
          page: 12
          text_layer_sha256: 645ff7522c54e80225a9af1bdea903862fe49c66a252e6f75d675f05dcc69501
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'In addition, only 4 patients had damage to only the

          posterior bottleneck ROI, and so future studies that incorporate more

          patients with damage to this region are necessary to fully characterize

          its relationship to post-stroke language function.'
        anchor_text: 'In addition, only 4 patients had damage to only the

          posterior bottleneck ROI, and so future studies that incorporate more

          patients with damage to this region are necessary to fully characterize

          its relationship to post-stroke language function.'
        excluded_fragments: []
        image_sha256: 8f4684b28dc5f99135bff52b63617f08b47e016f3ad0d270586d234b0a725170
        transcription: '. In addition, only 4 patients had damage to only the

          posterior bottleneck ROI, and so future studies that incorporate more

          patients with damage to this region are necessary to fully characterize

          its relationship to post-stroke language function'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 3
  quote: 'Next, we deﬁned a posteri-

    or bottleneck ROI according to the same procedure, but using labels for

    three of the language-relevant tracts previously identiﬁed in the poste-

    rior temporal WM: the left ILF, IFOF, and SLF/AF (Turken and Dronkers,

    2011).'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-24'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
