---
id: executive_dysfunction_cluster_svr_dsm
name: executive dysfunction cluster
kind: network
findings:
- id: f1
  target_audit:
    status: behaviour_label_present
    category: behaviour_or_language_construct
    original_target: executive_dysfunction
    reason: Label names a behaviour or language construct; its exact operational definition and measurement
      still need source review.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  outcome_measurement:
    status: needs_source_review
    instruments: []
    note: Outcome instrument/task is not yet verified for this finding. Do not infer it from the predictor
      or a paper-wide test list.
  target: executive_dysfunction
  target_kind: impairment
  claim: A cluster of disconnected white matter tracts, including the left frontal
    parahippocampal segment of the cingulum, anterior cortico-striatal tract, anterior
    thalamic radiations, and bilateral corpus callosum, was associated with more severe
    initial executive dysfunction.
  direction: likely
  relationship: correlational
  method: disconnectome
  sample:
    n: not_reported
    population: individuals with aphasia following a left-hemispheric stroke
    phase: not_reported
    time_post_onset: initial assessment (within 60 days post-stroke)
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - executive function was assessed using an ad-hoc executive score combining several
    skills rather than raw scores
  - relatively small sample size
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Patient lesion overlap with a population reference
    tract template to infer structural disconnections (SVR-DSM), specifically identifying
    a cluster including the left frontal parahippocampal segment of the cingulum (CFPH),
    anterior cortico-striatal tract, anterior thalamic radiations (ATR), and bilateral
    corpus callosum (CC). results are interpreted as statistical neural correlates
    rather than predictions; analysis regressed out age, stroke subtype, and lesion
    volume from the executive function score and lesion maps. Additional metadata
    has not been transcribed; review the pending-field flags before approval. PDF
    image reading (P2-S4-C9, two-model agreement, human verification pending): Participants


    The inclusion criteria were: age above 18 years, a left-hemispheric stroke confirmed
    by MRI, a diagnosis of aphasia confirmed by speech and language assessment, and
    a speech and language assessment performed at FA within 60 days post-stroke Original
    text-layer quotation is preserved below.'
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
    - not_transcribed:sample.n
    - proposed_concept:executive_dysfunction
  citation: '@Haldin2026'
  source_passages:
  - section: Original source P6-S1-C1
    page: 6
    quote: "\nFinally concerning EF, we identified a cluster encompassing 5,869 \n\
      voxels associated with more severe executive dysfunction initially (see \nFig.\
      \ 4D and Table 2)."
    supports: claim
  - section: Original source P6-S1-C3
    page: 6
    quote: "It included voxels in the left \nfrontal parahippocampal segment of the\
      \ cingulum (CFPH, 822 voxels), \nanterior cortico-striatal tract (176 voxels),\
      \ anterior thalamic radiations \n(ATR, 117 voxels), and the CC bilaterally (3,404\
      \ voxels).\n4."
    supports: claim
  - section: Original source P6-S1-C2
    page: 6
    quote: "This cluster survived cluster-wise thresholding, \nwith z-values ranging\
      \ from 0 to −3.5."
    supports: method
  - section: Original source P6-S2-C2
    page: 6
    quote: "Consequently, our results \nare interpreted as statistical neural correlates,\
      \ i.e., associations between \ndisconnected WM tracts and behavioral scores,\
      \ rather than as pre­\ndictions of these scores."
    supports: claim
  - section: Original source P4-S2-C2
    page: 4
    quote: "This disconnection probability is the voxel-wise probability of tracking\
      \ a \nWM fiber of healthy participants entering the lesioned area when \noverlayed\
      \ with the patient's lesion map."
    supports: method
  - section: Original source P4-S3-C4
    page: 4
    quote: "Based on the results of these \nadditional statistical analyses (see Supplementary\
      \ Material, Table C) \nand considering the relationship between lesion volume\
      \ and local lesion \nstatus, the following covariate regressions were applied:\
      \ (i) regression of \nlesion volume out of both the ASRS score at FA and the\
      \ lesion maps; (ii) \nregression of lesion volume out of both the naming score\
      \ and the lesion \nmaps, and regression of age out of the naming score; (iii)\
      \ regression of \nage and stroke subtype out of the EF score, and regression\
      \ of lesion \nvolume out of the lesion maps; and (iv) regression of the ASRS\
      \ score at \nFA out of aphasia severity at discharge, and regression of lesion\
      \ volume \nout of the lesion maps."
    supports: claim
  - section: Original source P2-S4-C9
    page: 2
    quote: "Participants\nThe inclusion criteria were: age above 18 years, a left-hemispheric\
      \ \nstroke confirmed by MRI, a diagnosis of aphasia confirmed by speech \nand\
      \ language assessment, and a speech and language assessment per­\nformed at\
      \ FA within 60 days post-stroke."
    supports: sample
  - section: Original source P8-S1-C11
    page: 8
    quote: "Second, EF was \nassessed using an ad-hoc executive score that combines\
      \ several execu­\ntive skills."
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-24'
relationship_review:
  paper: Haldin2026
  proposal_id: R006
  review_status_sha256: de1562d452fb07deddc08900e679558686d435ef472d67b5a1be8411edd536c8
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 77414d4917e881ee587f41482c1112aa8c5aac03626fda7c2b378763f6784c9d
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 77414d4917e881ee587f41482c1112aa8c5aac03626fda7c2b378763f6784c9d
        A/passages.json: 6ceb92a91d257c59cae828353a1a97f59705c81e2986c43b1a79b500dcbffad5
        A/raw.json: 0d7889ca2ce642938d5afa31b49099372c8f8308d05fe0a5f538eec0512a30ac
        A/source-units.json: 79d1c2e63d044bedf3063cb798e3ff219b76d3bf8a08f3316408b55549c1a1fb
        A/full-source-units.json: ec7810797d14e32ba3d84039ed89dae238414043df813065b731d0bc641cbbcd
        A/meta.json: 960efbb80484daf1a82992adcbfe80847302ff8396fb008f7c6ae25576495abb
        A/table-images/TABLE-2-page-9-1.png: bde602284353dfda5ed9eaf5bd77104a05f28f3ba142f1d69796eaa5fcd32cc0
        A/table-images/TABLE-1-page-7-1.png: 5608f821f866b03bcbd77411a7d433d95064472a1f191ac5d79a2a4dbab32033
        A/table-images/page-7.png: 3c625f3b30b9fae6c8e64641992a5ebbd4020b0b64a6eb23114adc8d6f510d04
        A/table-images/page-9.png: d6b45d24e32e8e03e3bf6f111527573f8ea7940f22b18122d132b62e96e4e750
        A/table-images/manifest.json: 3386b7b94fc176c0758a5b46aacb7dabfe57a87e5a2a357df9acc2e9c506fc0b
        A/clauses/window-10/raw.json: c906725b12d73eeb6357968433bdd7263a1c84232db1d424ee38c618eec25837
        A/clauses/window-10/prompt.txt: fb921da937e136a4201410a13ab17894184412fe8fe427b912a50a2542244797
        A/clauses/window-10/meta.json: a419a47e2cd8645772d8f6cadd44a80236f4b4229e4b1fbaa7d3d4dc210be0bb
        A/clauses/window-03/raw.json: 5a1523896e7c75549078e2b91b81c9222302dcfc58eeb2e8e14a97a53cca08a5
        A/clauses/window-03/prompt.txt: 4df98b3194ca268d267c7020ef77aaba2c1c9cafbced532fa1c1bfce2e6864ef
        A/clauses/window-03/meta.json: 09bad3dfeb2ddf554390609e52db97eceeb1c8e8d24231fce5406f90cbc37ce0
        A/clauses/window-04/raw.json: 684710668315420c88c70757473e53d49db4bfd5efe66e5662d136547baba703
        A/clauses/window-04/prompt.txt: 059759f815371e06c5db44aad61fb6fe0e24b881c7fc041c6f1b6b3211707d45
        A/clauses/window-04/meta.json: 3aa359f1b9cf889a8c5df53e09f6ce4e91fb88c31ff4fdeab5a7944a9db9cac5
        A/clauses/window-05/raw.json: 15772d4bafbd25743d2e3a18297a7067dcfdf52baa030da8f62de5ab6890d70f
        A/clauses/window-05/prompt.txt: 613e14a0834a7b42a635a2fd61ee4730ab731b49b8b9339daea847b7454ef854
        A/clauses/window-05/meta.json: 095a3fcc68cd0c9aaa5e4077bee847b2b60c0d1c5e320a3656408ee1a2d80568
        A/clauses/window-02/raw.json: f82a076e933046e86e22170bdd3d45e3bcae23d996027060280494d3ed3caa54
        A/clauses/window-02/prompt.txt: ca369179fa3233537e35b6b07d8d3a7d3138dca7c6225e325af182f794348f76
        A/clauses/window-02/meta.json: 874089091b67ade89f15f2ee25b728bdbdef9d2816a6738bc57fce1f1287349c
        A/clauses/window-09/raw.json: 0a7b3e8d7f512a8042b52a1e673b502917088ef0702983478fe7f06a2f278002
        A/clauses/window-09/prompt.txt: 9d8ce66402c4f085b6fa17d01c4efbc5f369fb9265e68af9b0938369a2b09348
        A/clauses/window-09/meta.json: 0c0411fb62c84854b67176f21f275f85f36cb651a86ea968b96cd979f9df6127
        A/clauses/window-07/raw.json: a5de159fc10b5923898eb8632befe0b8b977268e4f7bb3dc416f0944946fd72d
        A/clauses/window-07/prompt.txt: 22267cd73f2c98c0deaaa410a79ecc1c8ab670894cd6057fe07f1f83365da0bc
        A/clauses/window-07/meta.json: 1d0a2e30ff6fca9a36f174116f77f16cbfb13b2c6f424db92cdb1e6ef716f63b
        A/clauses/window-01/raw.json: e90b0b579e603f97c970e374f43059e30a67c9c9f28398a70ce73b82da0a1c10
        A/clauses/window-01/prompt.txt: 7fa6ce7de507d9be59d10edd9dbf7fdd85581cd65c4429274b6c9203001cabeb
        A/clauses/window-01/meta.json: a1a99605921f51ecce8249b7a95d8c667c9d4c6b020d3ad2bc19170be4619512
        A/clauses/window-06/raw.json: 6bff4aefc27fcb4a7cf05aa227455962e3f4f3729a1a9ce83c64c6680a5dc576
        A/clauses/window-06/prompt.txt: ce4ac18b2dca4bfa8b36e6bb8882ef9ff205c274ce40d9dab297a3e803dc2f52
        A/clauses/window-06/meta.json: 83e5ce10cb2032b0c975c6fa8f58d21b037acf2437497c3bb368c59e6652ec3c
        A/clauses/window-08/raw.json: 7feeb1b94ea881f7b137ae26d6befd01b3fa7577d5f088bda8dc892e1d08c5e6
        A/clauses/window-08/prompt.txt: 8c4330d00579d718c7d24f7e2d51cac2556f198de215afa8ba95d4329edce662
        A/clauses/window-08/meta.json: 3a4cf9a31378baa50c023a88785f2d88057404a1294bc8465c1571059690221d
        A/tables/TABLE-1-page-7-1/raw.json: cebdb1badef9bd554d7b55dc3628656a12ca03de42e40f3f3f21675fda3f96a4
        A/tables/TABLE-1-page-7-1/prompt.txt: a6fbfa772a98372e8f4192a3359d5b466b48a8cec1b153caee590165eb232c38
        A/tables/TABLE-1-page-7-1/meta.json: f2a2872af6d3697818162243ed6a6e20271e8f6a361b5802b8d60d0a0d03acad
        A/tables/TABLE-2-page-9-2/raw.json: d8ba65c268a4ad2f1a6e454ae4381cd2d05a056af8c9f6448fa3f5f969255250
        A/tables/TABLE-2-page-9-2/prompt.txt: ea852748b599fa0a486c79bce482c6d2b1e09d6b3f507aac8705572406151e69
        A/tables/TABLE-2-page-9-2/meta.json: 10796d8e73441308b08483eefec5319c774574d308bf8df59a35ec8bffdf85a3
        B/passages.json: 6ceb92a91d257c59cae828353a1a97f59705c81e2986c43b1a79b500dcbffad5
        B/raw.json: 07be0ffff081b5f0eba50c4416c43e308b3ed8f0eece828afd0c0a3f45990b63
        B/source-units.json: 79d1c2e63d044bedf3063cb798e3ff219b76d3bf8a08f3316408b55549c1a1fb
        B/full-source-units.json: ec7810797d14e32ba3d84039ed89dae238414043df813065b731d0bc641cbbcd
        B/meta.json: e2bd5581ee95f745b8fe82cdb2852e854e552ff06e965148a2ca913709a53503
        B/table-images/TABLE-2-page-9-1.png: bde602284353dfda5ed9eaf5bd77104a05f28f3ba142f1d69796eaa5fcd32cc0
        B/table-images/TABLE-1-page-7-1.png: 5608f821f866b03bcbd77411a7d433d95064472a1f191ac5d79a2a4dbab32033
        B/table-images/page-7.png: 3c625f3b30b9fae6c8e64641992a5ebbd4020b0b64a6eb23114adc8d6f510d04
        B/table-images/page-9.png: d6b45d24e32e8e03e3bf6f111527573f8ea7940f22b18122d132b62e96e4e750
        B/table-images/manifest.json: a257f90f11e8826457002988635f371a4dff0ae3d3424c228b25ab8c071c9d7b
        B/clauses/window-10/raw.json: 0c8d588499aad2347b85b4f5db335b480c3ec39ffd7e96c9b237b76f5d60debc
        B/clauses/window-10/prompt.txt: fb921da937e136a4201410a13ab17894184412fe8fe427b912a50a2542244797
        B/clauses/window-10/meta.json: dd5628dc0de01d9b40d47206a0808bb992d658918fb1b5a6d8e6a604ae90a77c
        B/clauses/window-03/raw.json: 785177704b3bdd8941da7aa11252c23d527f7751aba276d2be0269bfbf993c08
        B/clauses/window-03/prompt.txt: 4df98b3194ca268d267c7020ef77aaba2c1c9cafbced532fa1c1bfce2e6864ef
        B/clauses/window-03/meta.json: c0f5b1ba57a054b1f0a04ee677bb0dc7853391c71ad91884035d29e9f7663b03
        B/clauses/window-04/raw.json: 53ac72b85d2a062e12787b4710335bd88b212fda4deddfecc4aae3c5214ef1e6
        B/clauses/window-04/prompt.txt: 059759f815371e06c5db44aad61fb6fe0e24b881c7fc041c6f1b6b3211707d45
        B/clauses/window-04/meta.json: 395063254d053cfb5fb41e061b248274988c24fb5c32f601f1b02ab428f9c7f9
        B/clauses/window-05/raw.json: bf89aecd385a16a08781c5b3cd92d1c3814837877f61f35742f0eb78de360dc5
        B/clauses/window-05/prompt.txt: 613e14a0834a7b42a635a2fd61ee4730ab731b49b8b9339daea847b7454ef854
        B/clauses/window-05/meta.json: faa9a9f8c4b1b8d4f07a195f84b5a039cb99bc80fd13934ba29f1aa9edc1e764
        B/clauses/window-02/raw.json: 11e7bfd2878f0f6d9b6c2a4dacec7c2ccb1ea0a0f8461f319f82d546860fd6a8
        B/clauses/window-02/prompt.txt: ca369179fa3233537e35b6b07d8d3a7d3138dca7c6225e325af182f794348f76
        B/clauses/window-02/meta.json: 2e34b8ef853cb692fd4377bba5d7f0bb1b11cce0e447e19f928556af1869a2b5
        B/clauses/window-09/raw.json: 62e18a1df47dac90e9890c290b8e6a99f1040c8d5f153c594b38123551e3b398
        B/clauses/window-09/prompt.txt: 9d8ce66402c4f085b6fa17d01c4efbc5f369fb9265e68af9b0938369a2b09348
        B/clauses/window-09/meta.json: ec25a8de890d9d598cc508653d549c18ae133f9f8b6fdf45b5c9ff74d0886267
        B/clauses/window-07/raw.json: 94226ae29cf4d37abf226130b41914af09d199ddfc6552a3041b9f6326c00f50
        B/clauses/window-07/prompt.txt: 22267cd73f2c98c0deaaa410a79ecc1c8ab670894cd6057fe07f1f83365da0bc
        B/clauses/window-07/meta.json: 81bdbf33854adac9ca5544ef29a3c512fee2e2f0a20f472e1d85ab7f12b426eb
        B/clauses/window-01/raw.json: 360d32db605658912a7a26001b6d0b9c29191747d5390d7be2850f49bb73bdb7
        B/clauses/window-01/prompt.txt: 7fa6ce7de507d9be59d10edd9dbf7fdd85581cd65c4429274b6c9203001cabeb
        B/clauses/window-01/meta.json: faad5623e1a68167d68c9115af8cce1c96941c4a84c8e4aae835b6d264cf791f
        B/clauses/window-06/raw.json: ce3f95963e49477de0e808657400d0c7c791b8e5f71860058c6f82f90269d4fb
        B/clauses/window-06/prompt.txt: ce4ac18b2dca4bfa8b36e6bb8882ef9ff205c274ce40d9dab297a3e803dc2f52
        B/clauses/window-06/meta.json: b8df2d60da43a4531dbd72185c6430f57767cd5ec1b38a69de643198d14b5901
        B/clauses/window-08/raw.json: 1de8a866450ca8b57c785d4a8e42732b424d3c21fde847d5b5a1745e583c1311
        B/clauses/window-08/prompt.txt: 8c4330d00579d718c7d24f7e2d51cac2556f198de215afa8ba95d4329edce662
        B/clauses/window-08/meta.json: 13b36d55f203b34340f0f13b400c7c68b5f11e4274d2d2fe7b55bd3834bbed80
        B/tables/TABLE-1-page-7-1/raw.json: 78623686317d877d71d5ef886e5b225d278b8ac46205423b784f27cc85dc10a9
        B/tables/TABLE-1-page-7-1/prompt.txt: a6fbfa772a98372e8f4192a3359d5b466b48a8cec1b153caee590165eb232c38
        B/tables/TABLE-1-page-7-1/meta.json: fd97ca75552053eefcfd7d9c8146312016b2744005ca733e027a6643734bcee8
        B/tables/TABLE-2-page-9-2/raw.json: 7252217d1bf11a3bf1c3882ef3e9ee757902503a73ebacbfb6c17188a32c1767
        B/tables/TABLE-2-page-9-2/prompt.txt: ea852748b599fa0a486c79bce482c6d2b1e09d6b3f507aac8705572406151e69
        B/tables/TABLE-2-page-9-2/meta.json: 33123d0b5f93f9bf61fdcce09b0a5dd58ab4a39ad035c08b750fcb2ee65ac8b7
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
      pdf_sha256: 77414d4917e881ee587f41482c1112aa8c5aac03626fda7c2b378763f6784c9d
      source_review: _compare/relationships-2026-11-16/review-current/Haldin2026
      source_status_sha256: 41aae1204d04ece3669f873b26e2f87501477050139b52698f0116740e1355e3
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R006
    exposure:
      text: disconnections in left CFPH, anterior cortico-striatal tract, ATR, and
        CC bilaterally
    outcome:
      text: executive dysfunction (initial)
    analysis_label: SVR-DSM
    relation: association
    evidence_ids:
    - P6-S1-C1
    - P6-S1-C3
    qualifier_ids:
    - P6-S1-C2
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 77414d4917e881ee587f41482c1112aa8c5aac03626fda7c2b378763f6784c9d
      source_review: _compare/relationships-2026-11-16/review-current/Haldin2026
      source_status_sha256: 41aae1204d04ece3669f873b26e2f87501477050139b52698f0116740e1355e3
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P4-S5-C4
      - Result passage disposed without unit P5-S1-C2
      - Result passage disposed without unit P5-S1-C10
      - Result passage disposed without unit P5-S1-C8
      - Result passage disposed without unit P5-S1-C9
      - Result passage disposed without unit P5-S2-C3
      - Result passage disposed without unit P5-S2-C4
      - Result passage disposed without unit P5-S2-C5
      - Result passage disposed without unit P5-S2-C6
      - 'window 5: invalid/duplicate disposition P5-S2-C8'
      - Result passage disposed without unit P5-S3-C4
      - Result passage disposed without unit P6-S1-C10
      - Result passage disposed without unit P6-S2-C4
      - Accounting without a linked unit P7-S1-C4
      - Unaccounted source passage P7-S1-C4
      - Accounting without a linked unit P7-S2-C2
      - Accounting without a linked unit P7-S2-C5
      - Accounting without a linked unit P7-S3-C2
      - Accounting without a linked unit P7-S3-C5
      - Accounting without a linked unit P7-S3-C6
      - Unaccounted source passage P7-S3-C6
      - Unaccounted source passage P7-S2-C5
      - Unaccounted source passage P7-S3-C2
      - Unaccounted source passage P7-S2-C2
      - Unaccounted source passage P7-S3-C5
      - Result passage disposed without unit P7-S4-C5
      - Result passage disposed without unit P9-S2-C2
      - Result passage disposed without unit P9-S2-C4
      - Result passage disposed without unit P9-S2-C6
      unattached_null_or_qualifier_ids:
      - P5-S1-C8
      - P7-S4-C5
      - P9-S3-C4
      suppressed_nonrepresented_units: 16
      default_disposition_count_requires_completeness_check: 199
      unselected_timing_passages:
      - P1-S1-C3
      - P2-S4-C9
      - P2-S4-C10
      - P4-S4-C13
      - P4-S5-C3
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P5-S2-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S2-C14
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S3-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S3-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S3-C13
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      empty_frame_slots_require_confirmation:
      - tested_personal_effects
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-7-1
      - TABLE-2-page-9-2
      unlinked_tables:
      - TABLE-1-page-7-1
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P2-S4
        - P3-S2
        - P3-S3
        - P4-S4
        - P5-S1
        - P5-S2
        - P5-S3
        - P6-S1
        - P6-S2
        - P8-S1
        - P8-S2
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 77414d4917e881ee587f41482c1112aa8c5aac03626fda7c2b378763f6784c9d
      source_review: _compare/relationships-2026-11-16/review-current/Haldin2026
      source_status_sha256: 41aae1204d04ece3669f873b26e2f87501477050139b52698f0116740e1355e3
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C6
      disposition: repeated
      result_indexes:
      - 2
      - 3
      - 5
      reason: Abstract summary of findings
    - source_id: P3-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes missing data for naming scores
    - source_id: P4-S4-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Demographic data (age)
    - source_id: P4-S4-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Demographic data (sex, handedness)
    - source_id: P4-S4-C15
      disposition: background_or_descriptive
      result_indexes: []
      reason: Clinical data (stroke type, lesion size)
    - source_id: P4-S4-C16
      disposition: background_or_descriptive
      result_indexes: []
      reason: Baseline clinical scores
    - source_id: P4-S4-C17
      disposition: background_or_descriptive
      result_indexes: []
      reason: Baseline clinical scores
    - source_id: P4-S5-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of lesion overlay map
    - source_id: P5-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of lesion overlay map
    - source_id: P5-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of disconnectome overlay map
    - source_id: P5-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Clinical data for outcome cohort
    - source_id: P5-S1-C8
      disposition: represented
      result_indexes:
      - 6
      reason: Null finding for SVR-LSM and initial severity/naming
    - source_id: P5-S1-C9
      disposition: represented
      result_indexes:
      - 0
      reason: Identifies EF deficit clusters
    - source_id: P5-S1-C10
      disposition: represented
      result_indexes:
      - 0
      reason: Voxel-wise thresholding qualification
    - source_id: P5-S2-C3
      disposition: represented
      result_indexes:
      - 0
      reason: Identifies left caudate in EF cluster
    - source_id: P5-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Exclusion of small cluster
    - source_id: P5-S2-C5
      disposition: represented
      result_indexes:
      - 1
      reason: Identifies aphasia outcome cluster
    - source_id: P5-S2-C6
      disposition: represented
      result_indexes:
      - 1
      reason: Identifies left IFG-op in outcome cluster
    - source_id: P5-S2-C10
      disposition: represented
      result_indexes:
      - 2
      reason: Identifies initial severity clusters
    - source_id: P5-S2-C11
      disposition: represented
      result_indexes:
      - 2
      reason: Identifies AF and CC in severity cluster
    - source_id: P5-S2-C12
      disposition: represented
      result_indexes:
      - 2
      reason: Identifies SLF-I, ILF, SLF-III, UF, STR in severity cluster
    - source_id: P5-S2-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Exclusion of small clusters
    - source_id: P5-S2-C14
      disposition: represented
      result_indexes:
      - 3
      reason: Identifies naming ability clusters
    - source_id: P5-S2-C15
      disposition: represented
      result_indexes:
      - 3
      reason: Identifies CC and MdLF in naming cluster
    - source_id: P5-S3-C3
      disposition: represented
      result_indexes:
      - 3
      reason: Identifies ILF, SLF-III, acoustic radiation in naming cluster
    - source_id: P5-S3-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Exclusion of small clusters
    - source_id: P5-S3-C5
      disposition: represented
      result_indexes:
      - 4
      reason: Identifies aphasia outcome cluster
    - source_id: P5-S3-C6
      disposition: represented
      result_indexes:
      - 4
      reason: Voxel-wise thresholding qualification
    - source_id: P5-S3-C7
      disposition: represented
      result_indexes:
      - 4
      reason: Identifies SLF-III in outcome cluster
    - source_id: P6-S1-C1
      disposition: represented
      result_indexes:
      - 5
      reason: Identifies EF dysfunction cluster
    - source_id: P6-S1-C2
      disposition: represented
      result_indexes:
      - 5
      reason: Cluster-wise thresholding qualification
    - source_id: P6-S1-C3
      disposition: represented
      result_indexes:
      - 5
      reason: Identifies CFPH, CST, ATR, CC in EF cluster
    - source_id: P6-S1-C10
      disposition: represented
      result_indexes:
      - 7
      reason: Reports poor predictive performance
    - source_id: P7-S1-C4
      disposition: repeated
      result_indexes:
      - 2
      reason: Discussion restatement of severity findings
    - source_id: P7-S2-C5
      disposition: repeated
      result_indexes:
      - 5
      reason: Discussion restatement of EF findings
    - source_id: P7-S3-C2
      disposition: repeated
      result_indexes:
      - 3
      reason: Discussion restatement of naming findings
    - source_id: P7-S3-C5
      disposition: repeated
      result_indexes:
      - 3
      reason: Discussion restatement of naming findings
    - source_id: P7-S3-C6
      disposition: repeated
      result_indexes:
      - 3
      reason: Discussion restatement of naming findings
    - source_id: P7-S3-C13
      disposition: repeated
      result_indexes:
      - 4
      reason: Discussion restatement of outcome findings
    - source_id: P7-S4-C5
      disposition: repeated
      result_indexes:
      - 4
      reason: Discussion restatement of outcome findings
    - source_id: P7-S4-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to Table 1
    - source_id: P7-S4-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of Table 1
    - source_id: P8-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: General summary of study goals
    - source_id: P8-S1-C2
      disposition: repeated
      result_indexes:
      - 2
      - 3
      - 5
      reason: Conclusion summary of findings
    - source_id: P9-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of computational demands
    - source_id: P9-S1-C12
      disposition: repeated
      result_indexes:
      - 0
      - 1
      - 2
      - 3
      - 4
      - 5
      reason: Conclusion summary of findings
    - source_id: P9-S2-C2
      disposition: repeated
      result_indexes:
      - 0
      - 1
      - 2
      - 3
      - 4
      - 5
      reason: Conclusion summary of findings
    - source_id: P9-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion about language streams
    - source_id: P9-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion about distributed networks
    - source_id: P9-S2-C6
      disposition: repeated
      result_indexes:
      - 7
      reason: Conclusion restatement of poor prediction performance
    - source_id: P9-S3-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of Table 2
    unresolved_coverage:
    - source_id: P6-S1-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P6-S1-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P6-S1-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P6-S1-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P6-S2-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P6-S2-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S1-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S1-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S1-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C6
    - P3-S1-C8
    - P4-S4-C13
    - P4-S4-C14
    - P4-S4-C15
    - P4-S4-C16
    - P4-S4-C17
    - P4-S5-C4
    - P5-S1-C1
    - P5-S1-C2
    - P5-S1-C4
    - P5-S1-C10
    - P5-S2-C4
    - P5-S2-C13
    - P5-S3-C4
    - P6-S1-C2
    - P6-S1-C5
    - P6-S1-C6
    - P6-S1-C7
    - P6-S1-C8
    - P6-S2-C3
    - P6-S2-C4
    - P7-S1-C4
    - P7-S2-C5
    - P7-S3-C2
    - P7-S3-C5
    - P7-S3-C6
    - P7-S3-C13
    - P7-S4-C5
    - P7-S4-C8
    - P7-S4-C10
    - P8-S1-C1
    - P8-S1-C2
    - P8-S1-C3
    - P8-S1-C4
    - P8-S1-C6
    - P9-S1-C7
    - P9-S1-C12
    - P9-S2-C2
    - P9-S2-C3
    - P9-S2-C4
    - P9-S2-C6
    - P9-S3-C4
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-7-1
    - TABLE-2-page-9-2
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P4-S3-C11
      - P4-S4-C4
      - P4-S4-C5
      - P5-S1-C3
      recruited_sample:
      - P1-S1-C3
      - P2-S4-C11
      - P2-S4-C12
      - P4-S4-C11
      eligibility:
      - P2-S4-C9
      - P2-S4-C10
      imaging_provenance:
      - P4-S1-C8
      - P4-S1-C9
      imaging_timing:
      - P3-S2-C9
      outcome_timing:
      - P3-S2-C5
      - P3-S2-C7
      - P5-S1-C4
      outcome_definition:
      - P3-S2-C5
      - P3-S2-C6
      validation:
      - P4-S3-C6
      analysis_restrictions:
      - P4-S2-C11
      - P4-S4-C3
      dependent_variable_statement:
      - P4-S2-C12
      - P5-S1-C5
      - P5-S2-C7
      limitations:
      - P6-S2-C5
      - P8-S1-C8
      - P8-S1-C9
      - P8-S1-C11
      - P9-S1-C4
      - P9-S1-C6
      - P9-S1-C7
      - P9-S1-C8
      personal_factors:
      - P4-S3-C2
      - P4-S3-C4
      - P9-S1-C9
      tested_personal_effects: []
      adjustment_roles:
      - P4-S3-C4
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P4-S4-C13
      - P4-S4-C14
      - P4-S4-C15
      - P4-S4-C16
      - P4-S4-C17
      - P5-S1-C4
    outcome_type: both_reported
    imaging_vs_outcome: mixed
    validation_type: internal_cross_validation
    held_selections:
    - slot: dependent_variable_statement
      source_id: P5-S2-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S2-C14
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S3-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S3-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S3-C13
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
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
      pdf_sha256: 77414d4917e881ee587f41482c1112aa8c5aac03626fda7c2b378763f6784c9d
      review_sha256: de1562d452fb07deddc08900e679558686d435ef472d67b5a1be8411edd536c8
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
      - P6-S1-C1
      - P6-S1-C3
      source_result: SVR-DSM analysis identified a significant cluster (5,869 voxels)
        associated with more severe initial executive dysfunction. This cluster included
        the left frontal parahippocampal segment of the cingulum (CFPH), anterior
        cortico-striatal tract, anterior thalamic radiations (ATR), and the corpus
        callosum bilaterally. The result survived cluster-wise thresholding (p < 0.05,
        5,000 permutations).
      result_status: detected
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis corresponds to the SVR-DSM model for initial
            executive dysfunction. The source explicitly links the identified tracts
            (CFPH, anterior cortico-striatal, ATR, CC) to this specific outcome in
            P6-S1-C1 and P6-S1-C3. The method is correctly identified as SVR-DSM (disconnectome-symptom
            mapping).
          source_ids:
          - P6-S1-C1
          - P6-S1-C3
          - P4-S2-C12
        direction:
          answer: fits
          reason: The source states the cluster was associated with 'more severe executive
            dysfunction initially' (P6-S1-C1). The proposed claim states the tracts
            were associated with 'more severe initial executive dysfunction'. The
            direction of the association (disconnection -> severity) is preserved.
          source_ids:
          - P6-S1-C1
          - P6-S1-C6
        construct:
          answer: fits
          reason: The exposure is correctly described as disconnections in specific
            WM tracts (CFPH, anterior cortico-striatal, ATR, CC). The outcome is initial
            executive dysfunction. The patient measurement is correctly identified
            as template_lesion_overlap (disconnectome mapping uses patient lesions
            overlaid on healthy tractograms to estimate disconnection probability,
            not patient diffusion data). The method is SVR-DSM.
          source_ids:
          - P6-S1-C3
          - P4-S1-C6
          - P4-S1-C8
        qualifications:
          answer: fits
          reason: 'The draft includes the qualification that results are interpreted
            as statistical neural correlates rather than predictions (P6-S2-C2). It
            also correctly notes the covariates regressed out for this specific analysis:
            age, stroke subtype, and lesion volume (P4-S3-C4). The limitation regarding
            the ad-hoc executive score (P8-S1-C11) is also included.'
          source_ids:
          - P6-S2-C2
          - P4-S3-C4
          - P8-S1-C11
        missing_material_caveat:
          answer: fits
          reason: No material caveats are missing. The draft correctly captures the
            interpretation as correlational, the specific covariates used, and the
            nature of the executive function measure. The thresholding details (cluster-wise
            for EF) are consistent with the source (P5-S2-C8, P8-S1-C14).
          source_ids:
          - P6-S2-C2
          - P4-S3-C4
          - P8-S1-C11
      optional_pending:
      - Sample size for this specific analysis (70 participants for EF in SVR-LSM,
        likely similar or 72 for SVR-DSM as no exclusions mentioned for EF in DSM,
        but exact N not explicitly transcribed in the selected window for DSM EF specifically,
        though P4-S4-C5 implies no exclusions for EF in DSM).
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Sample size requires source confirmation; it has not been transcribed.
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Sample size for this specific analysis (70 participants for EF in SVR-LSM, likely
      similar or 72 for SVR-DSM as no exclusions mentioned for EF in DSM, but exact
      N not explicitly transcribed in the selected window for DSM EF specifically,
      though P4-S4-C5 implies no exclusions for EF in DSM).
    normalizations:
    - field: sample.n
      original: 72
      action: not_transcribed
      reason: Not supported by selected quotations
    analysis_identity:
      id: R006
      exposure:
        text: disconnections in left CFPH, anterior cortico-striatal tract, ATR, and
          CC bilaterally
      outcome:
        text: executive dysfunction (initial)
      analysis_label: SVR-DSM
      relation: association
      evidence_ids:
      - P6-S1-C1
      - P6-S1-C3
      qualifier_ids:
      - P6-S1-C2
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 77414d4917e881ee587f41482c1112aa8c5aac03626fda7c2b378763f6784c9d
        source_review: _compare/relationships-2026-11-16/review-current/Haldin2026
        source_status_sha256: 41aae1204d04ece3669f873b26e2f87501477050139b52698f0116740e1355e3
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P2-S4-C9:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 77414d4917e881ee587f41482c1112aa8c5aac03626fda7c2b378763f6784c9d
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 4f77ef62bcc38b2df76a17876f536fee612cc94d019e960d8abf4784a6333876
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S4-C9
          page: 2
          text_layer_sha256: 4f77ef62bcc38b2df76a17876f536fee612cc94d019e960d8abf4784a6333876
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "Participants\nThe inclusion criteria were: age above 18 years,\
          \ a left-hemispheric \nstroke confirmed by MRI, a diagnosis of aphasia confirmed\
          \ by speech \nand language assessment, and a speech and language assessment\
          \ per­\nformed at FA within 60 days post-stroke."
        anchor_text: "Participants\nThe inclusion criteria were: age above 18 years,\
          \ a left-hemispheric \nstroke confirmed by MRI, a diagnosis of aphasia confirmed\
          \ by speech \nand language assessment, and a speech and language assessment\
          \ per­\nformed at FA within 60 days post-stroke."
        excluded_fragments: []
        image_sha256: 21d394bd8c074d50c7c1b2da8b1d35f678e1478234aba01a473590e99e763d92
        transcription: 'Participants


          The inclusion criteria were: age above 18 years, a left-hemispheric stroke
          confirmed by MRI, a diagnosis of aphasia confirmed by speech and language
          assessment, and a speech and language assessment performed at FA within
          60 days post-stroke'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 6
  quote: "\nFinally concerning EF, we identified a cluster encompassing 5,869 \nvoxels\
    \ associated with more severe executive dysfunction initially (see \nFig. 4D and\
    \ Table 2)."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-24'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
