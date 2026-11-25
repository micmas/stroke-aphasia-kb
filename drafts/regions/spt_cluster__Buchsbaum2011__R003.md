---
id: spt_cluster
name: Spt cluster
kind: network
findings:
- id: f1
  target_audit:
    status: behaviour_label_present
    category: behaviour_or_language_construct
    original_target: phonological_working_memory
    reason: Label names a behaviour or language construct; its exact operational definition and measurement
      still need source review.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  outcome_measurement:
    status: needs_source_review
    instruments: []
    note: Outcome instrument/task is not yet verified for this finding. Do not infer it from the predictor
      or a paper-wide test list.
  target: phonological_working_memory
  target_kind: impairment
  claim: A cluster of activity in the left planum temporale (area Spt) was reliably
    active during both the encoding and delay phases of a phonological working memory
    task.
  direction: likely
  relationship: correlational
  method: fMRI_activation
  sample:
    n: 105
    population: healthy adults (age range 8-42)
    phase: not_reported
    time_post_onset: concurrent
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Peak overlap in Spt was 33% due to neuroanatomical variability of the posterior
    planum temporale, although visual inspection of single subjects showed clusters
    of activity in this region
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Brain activation during both the encoding (auditory-verbal
    stimulus presentation) and delay (covert rehearsal) phases of a phonological working
    memory task, as measured by a conjunction analysis of aggregate fMRI contrast
    maps. The finding is based on an aggregate analysis of five studies; The conjunction
    analysis was used to distinguish regions active in both phases from those active
    exclusively in one phase. Additional metadata has not been transcribed; review
    the pending-field flags before approval. PDF image reading (P2-S4-C8, two-model
    agreement, human verification pending): . The studies were selected because each

    involved auditory presentation of verbal material followed by a de-

    lay period involving verbal rehearsal, and because relevant con-

    trasts for these “encoding” and “delay” phases of the task were

    available (in non-normalized “native” image space) for each of

    the 105 individual subjects (age range: 8–42) that took part in the

    studies Original text-layer quotation is preserved below.'
  imaging_details:
    reference_space: not_reported
    atlases_used: []
  lesion_mapping: {}
  provenance:
    extracted_by: model:gemma4:31b
    extracted_on: '2026-11-23'
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
    - proposed_concept:phonological_working_memory
  citation: '@Buchsbaum2011'
  source_passages:
  - section: Original source P5-S1-C6
    page: 5
    quote: "As can be seen in Fig. 3, a number of regions were active during\nboth\
      \ task phases, including dorsal and ventral portions of the pre-\nfrontal cortex\
      \ the intraparietal sulcus, STS bilaterally, and area Spt\nin the left planum\
      \ temporale (see Table 3 for MNI coordinates of\nactivated clusters; maximum\
      \ coordinate: \x0251, \x0243, 20)."
    supports: claim
  - section: Original source P2-S4-C2
    page: 2
    quote: 'In the present study, we have gathered 105 single subject fMRI

      scans on a phonological working memory paradigm, collected

      across ﬁve studies and three laboratories, and performed an aggre-

      gate analysis on the entire set of statistical activation maps (see

      Yarkoni, Barch, Gray, Conturo, & Braver, 2009).'
    supports: sample
  - section: Original source P2-S4-C8
    page: 2
    quote: 'The studies were selected because each

      involved auditory presentation of verbal material followed by a de-

      lay period involving verbal rehearsal, and because relevant con-

      trasts for these ‘‘encoding’’ and ‘‘delay’’ phases of the task were

      available (in non-normalized ‘‘native’’ image space) for each of

      the 105 individual subjects (age range: 8–42) that took part in

      the studies.'
    supports: sample
  - section: Original source P5-S1-C2
    page: 5
    quote: 'Conjunction of encoding and delay contrasts

      To examine regions that were active both during stimulus

      encoding and verbal memory maintenance, we performed a con-

      junction analysis between the delay and encoding meta-contrasts.'
    supports: method
  - section: Original source P6-S1-C2
    page: 6
    quote: 'The peak percentage of overlap in Spt was what might appear to

      be a relatively modest value of 33% (35 out of 105 subjects).'
    supports: limitation
  - section: Original source P6-S1-C3
    page: 6
    quote: 'This

      number, however, reﬂects to some extent the neuroanatomical var-

      iability of the posterior portion of the planum temporale, which is

      difﬁcult to align across subjects due to individual differences in

      the trajectory of the Sylvian ﬁssure (Westbury, Zatorre, & Evans,

      1999).'
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-23'
relationship_review:
  paper: Buchsbaum2011
  proposal_id: R003
  review_status_sha256: 49a3b204de196752fe98ed72f01273582e2de467be6d7db6fcd6123b74a59e4d
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 4d8f454c8af2f92a90919680da4e4ad04f89a6b2bb7ede1a540f8c485b5efd86
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 4d8f454c8af2f92a90919680da4e4ad04f89a6b2bb7ede1a540f8c485b5efd86
        A/passages.json: 8d11ee109b68772c29469064df4b4fe7d9193cda4ced0c9b6442d6ef5738a730
        A/raw.json: 966e94603687bfca80a711df65329ffc80201ab0890f43a9590234b767f808d9
        A/source-units.json: 454d551402ed8f4c43518ca9b86722e8ba3dbdd10080b935146af2e79041e975
        A/full-source-units.json: c0c3415c8753161c7d1a292f1b1977cf791615b5aa7d0d46cc99e60675054cb1
        A/meta.json: e09c9a41c52bcfbcb482e40b41529245460e81a52cd42103adee197ca2e39da8
        A/table-images/TABLE-1-page-3-1.png: c0d23c7faabeac7ac7a0c8317e8d81e2a61248c3b1f8cefafead564cf538d1ae
        A/table-images/page-3.png: 958853aa4d1f7b914b22340d3729bac11568125227e6d12cc9434c7b26ec3aaf
        A/table-images/page-5.png: 9fd699a9a4fd4a9752e87815b6b68cc47fe0bb82926e3beb670a513d9fea2798
        A/table-images/page-4.png: dede2f21828007443f0d7907499c20005953e583b5a50223f6136cd1d4287d10
        A/table-images/manifest.json: a8640881e5010323709810d4d5e70091880e4c0026319c03a8d72a87018fa307
        A/table-images/TABLE-2-page-4-1.png: 0c44acc36eb1a9f77cdefa39a96de7e4f2135060b1d5bd6fd47b4dfc587b5592
        A/table-images/TABLE-3-page-5-1.png: 3fb76a8e0d0f78127db7c1807c9debbaf92d35c06773c959de792f896168a104
        A/clauses/window-03/raw.json: 74e42942666cd0278ebed6d4a879b7281393a8d3e3a0e1d154ac58a2d2c4179e
        A/clauses/window-03/prompt.txt: 7b6163bed6d3469b3095e277c56935b19c044713432be874c99b80ea4ab5c807
        A/clauses/window-03/meta.json: 141f746d9cdd5d914ef7460700971b5c41001ec9f7fd7948dbd644f7e886602d
        A/clauses/window-04/raw.json: b44f5940348daa219ac2fb41da75354744c7d58c965b93d223d51789f947963e
        A/clauses/window-04/prompt.txt: 4b0aac60087ee67ea411642e2367bc1f0b2f5d65a8370a090b45b710e01b63c9
        A/clauses/window-04/meta.json: 26712f3a2d1f7209d1b819bdfaa128e896faf49353025a102abe48dac8b1b098
        A/clauses/window-05/raw.json: 618bcda72669b0a8210bcaea8fe96c13da3f306a66c453f846d9b9a454186544
        A/clauses/window-05/prompt.txt: 92e5ab427617d2b4bfd37017d8a960cb5028fafcde5166add395587d24371b67
        A/clauses/window-05/meta.json: 9a35add5f38ecd6bfff8c665eea8f9845cc3adedcb9bb9ea5fe7b3471da8a446
        A/clauses/window-02/raw.json: 9a3b4ec205e824d39225666194fb99b8aef2729b26f51b77185a87072c6bd485
        A/clauses/window-02/prompt.txt: 7dd863f014960cfcd137759f09a4d662c4042f995faf173e0fb03a737d0fac0f
        A/clauses/window-02/meta.json: 44cac523fe2ca4b6b326fecb5b0d089aebccb7d007f88ad91a03e221db36b3fb
        A/clauses/window-09/raw.json: 73ccad6624f581a15cbc7c6db496539535517728b01c91fb263dbff23b4cbbd2
        A/clauses/window-09/prompt.txt: 7e043d8e3459e8de9f049116caab4a4cc7b84304728013966377d0036b9367e5
        A/clauses/window-09/meta.json: bcb9b29bfcf0c6a59f4c67bc86a10a1137b7da8684c4c2b538a0002f14082768
        A/clauses/window-07/raw.json: e5003918a3c65e6dbb7cf9a0c836a2c894937874db575b5d2c4730a6f86cc8f2
        A/clauses/window-07/prompt.txt: 88317a79527dea704d55b827d11afd3c037946b9f8e5f3a8d99e6feb4cbd3e40
        A/clauses/window-07/meta.json: fc5bdb807fe46ee71208a4ce6d2082e955f46e4672db280c35118495b543c873
        A/clauses/window-01/raw.json: 612d204dc556b557181d75d32b20c24f77f990189ea5dcd705ee931c38f934b6
        A/clauses/window-01/prompt.txt: 94b1e9e92f102bb3a22fb987428c05661aaba3fc47349afba965390be1425b4f
        A/clauses/window-01/meta.json: 2f451bd9859d888bd8fb47c6d9afbe8edae611bfc57d51c35dd18c43cd490ee2
        A/clauses/window-06/raw.json: 0612c3f516469e69806ca1f061018e0f2e960a585e8c30e2f325e9f18bbc655c
        A/clauses/window-06/prompt.txt: 7ed766b8e1943dfcd8e82a282d72bf32223d2eec2ad2478d418c0a10ba35dfc3
        A/clauses/window-06/meta.json: 0a66227fcfee6e3b8830672f4000ee0f92b1571a49eaf3729acbc9d8ceb68f0b
        A/clauses/window-08/raw.json: 167f084292b58774cfb8bd29f7fc7c33bb6117d742e675109084c59918b6605d
        A/clauses/window-08/prompt.txt: 380440f70c30839cc07e8051102acf00c2327b2ff55926ff983ad7a619090d83
        A/clauses/window-08/meta.json: 855f9e82cdd41d936066cb9d2d48879ec6f97806f336d5cafcb54f666e26d7e1
        A/tables/TABLE-3-page-5-3/raw.json: 5d158a802cbb6b333f6f5804ab768e26a8d67c2f16148f436ed0511faddbfede
        A/tables/TABLE-3-page-5-3/prompt.txt: b4b88e098ce854b346421ed5138c4aa41d2d6c7da0f301c96bccb333b854f351
        A/tables/TABLE-3-page-5-3/meta.json: 93c4f11602e39d999acd1475b2c2ca31804ffde22781469712409dc23f95fb8a
        A/tables/TABLE-1-page-3-1/raw.json: f6007fcd3f0f5b5cacd090e0342e3ac62629f085e7d85ebdcf33adab6422ce78
        A/tables/TABLE-1-page-3-1/prompt.txt: c43f612ee0c777af39016a1fa9dc02770bbdbe357069993060936af1694129b7
        A/tables/TABLE-1-page-3-1/meta.json: 177d25e1db819945bb6e32a11c0c7c4a78952601540428b7524e07f7255fa637
        A/tables/TABLE-2-page-4-2/raw.json: 625c545929db41a51254e8868d802ad27819c7f40b473d796aab00a4f153a537
        A/tables/TABLE-2-page-4-2/prompt.txt: 85ae65b84c0c102ba24123b335c75607e14d2d49135d87c195cd2aa908011a9c
        A/tables/TABLE-2-page-4-2/meta.json: 22d5b70b879011c3784d270f816a88262a0ff54218bbbd63af36bc93b52de79d
        B/passages.json: 8d11ee109b68772c29469064df4b4fe7d9193cda4ced0c9b6442d6ef5738a730
        B/raw.json: b399f011a7c3327462ef26a0c355636cf0702a950fa9dc2caa3af3fe0aa37c1f
        B/source-units.json: 454d551402ed8f4c43518ca9b86722e8ba3dbdd10080b935146af2e79041e975
        B/full-source-units.json: c0c3415c8753161c7d1a292f1b1977cf791615b5aa7d0d46cc99e60675054cb1
        B/meta.json: 9d42eb2772ce813d28b7282875206a4092af05f1e861b603b76060e7f70fc026
        B/table-images/TABLE-1-page-3-1.png: c0d23c7faabeac7ac7a0c8317e8d81e2a61248c3b1f8cefafead564cf538d1ae
        B/table-images/page-3.png: 958853aa4d1f7b914b22340d3729bac11568125227e6d12cc9434c7b26ec3aaf
        B/table-images/page-5.png: 9fd699a9a4fd4a9752e87815b6b68cc47fe0bb82926e3beb670a513d9fea2798
        B/table-images/page-4.png: dede2f21828007443f0d7907499c20005953e583b5a50223f6136cd1d4287d10
        B/table-images/manifest.json: b498b18bef3193b96487aa7df85a515140e4ea9a3b2ce31dac66b79d739ff6eb
        B/table-images/TABLE-2-page-4-1.png: 0c44acc36eb1a9f77cdefa39a96de7e4f2135060b1d5bd6fd47b4dfc587b5592
        B/table-images/TABLE-3-page-5-1.png: 3fb76a8e0d0f78127db7c1807c9debbaf92d35c06773c959de792f896168a104
        B/clauses/window-03/raw.json: de00c361066373e9a978fe49b2cf821d80652e4fc539ec511d7308f2ea434c71
        B/clauses/window-03/prompt.txt: 7b6163bed6d3469b3095e277c56935b19c044713432be874c99b80ea4ab5c807
        B/clauses/window-03/meta.json: 8575473d60b9c3ac6aeb1e7b2f66b416d863dc7bc74f63e923efda8f7b7c5ee3
        B/clauses/window-04/raw.json: e4ed8ffb198f80bc7b187404720e695f960260ceb8dd5720b28092678f535bfd
        B/clauses/window-04/prompt.txt: 4b0aac60087ee67ea411642e2367bc1f0b2f5d65a8370a090b45b710e01b63c9
        B/clauses/window-04/meta.json: 331f064947c6101f808300ef9ce2e086803db04b09bfbf65023441dbe2f5db74
        B/clauses/window-05/raw.json: cdd6a1efe1d102c5278e970c42ed6f65e41bfbf9d61937a3914551c418be005f
        B/clauses/window-05/prompt.txt: 92e5ab427617d2b4bfd37017d8a960cb5028fafcde5166add395587d24371b67
        B/clauses/window-05/meta.json: bf728cf83346b5cd368c04f23715af8a15b98d663fb5713cc154bc93f5f21489
        B/clauses/window-02/raw.json: 879d8c9a499b503ff90682bdc018386bf3aec5c468bd158db6b5978699229020
        B/clauses/window-02/prompt.txt: 7dd863f014960cfcd137759f09a4d662c4042f995faf173e0fb03a737d0fac0f
        B/clauses/window-02/meta.json: d31542c62a837cb7bf0a0c99921cb935a3c0a00224b1e94383be5e90c76640ce
        B/clauses/window-09/raw.json: a56ca1c89b7adef9d606c73b914b696061b6a0b880737113ca2c684b3d7e3685
        B/clauses/window-09/prompt.txt: 7e043d8e3459e8de9f049116caab4a4cc7b84304728013966377d0036b9367e5
        B/clauses/window-09/meta.json: 9655cd8eb121c4e8cafe3bddbca90974212dce3995af6be83a6b189fac0742a3
        B/clauses/window-07/raw.json: 3b88b7d1e7d489346fa36c6782bf1cc35006c27f3bfe5b47f8bc6dd219286836
        B/clauses/window-07/prompt.txt: 88317a79527dea704d55b827d11afd3c037946b9f8e5f3a8d99e6feb4cbd3e40
        B/clauses/window-07/meta.json: 7d148b904b30930d9ce83ec6277a34a9fb675992cbba90ccf0e754e61c3104e6
        B/clauses/window-01/raw.json: 38fb4f83cb36267302e4be631757d4d292e7904525e1e0dacf44ac709b3bce32
        B/clauses/window-01/prompt.txt: 94b1e9e92f102bb3a22fb987428c05661aaba3fc47349afba965390be1425b4f
        B/clauses/window-01/meta.json: 99aa71531e713e01145d333f4d5309f9b6f088f85ccf90380294ce3047d9fd1f
        B/clauses/window-06/raw.json: fda7221561f64bb42d1e04511fc404c05ca991082f8c57f31cf2a9238174b299
        B/clauses/window-06/prompt.txt: 7ed766b8e1943dfcd8e82a282d72bf32223d2eec2ad2478d418c0a10ba35dfc3
        B/clauses/window-06/meta.json: ce9b07d6cfa6136dc92a61b11ffbb9cb9b4dc4ba57745e189878666d0d11b7ee
        B/clauses/window-08/raw.json: 1ab7b3a97cb9e355006dfd7f49dc41f24d78935367d93a33157843e8d9fe76b8
        B/clauses/window-08/prompt.txt: 380440f70c30839cc07e8051102acf00c2327b2ff55926ff983ad7a619090d83
        B/clauses/window-08/meta.json: 881c5482e04211b20e6689425ef67a34ec695df84159b828f900aabb4387d739
        B/tables/TABLE-3-page-5-3/raw.json: a11cb94127e92de9aaf3b7bede852a1332bf9ad70e063895a3e225626f6904ff
        B/tables/TABLE-3-page-5-3/prompt.txt: b4b88e098ce854b346421ed5138c4aa41d2d6c7da0f301c96bccb333b854f351
        B/tables/TABLE-3-page-5-3/meta.json: 2852df886eb5c49762cf5198662c19de90af8ea63abc2414a0433e66b826dc48
        B/tables/TABLE-1-page-3-1/raw.json: 18ae701e7dae5c64ad0f0e24240d3b7d9d53fc979e279ebe9ca00ccffe8c0a45
        B/tables/TABLE-1-page-3-1/prompt.txt: c43f612ee0c777af39016a1fa9dc02770bbdbe357069993060936af1694129b7
        B/tables/TABLE-1-page-3-1/meta.json: dc5984bd19dcc93216c9b5127007e72f7e225254afb927cac24d36893506b4c3
        B/tables/TABLE-2-page-4-2/raw.json: 1128da8c17185e97ec990b67e769e224d4d932ecee29f96f09d03ca1e3d219c7
        B/tables/TABLE-2-page-4-2/prompt.txt: 85ae65b84c0c102ba24123b335c75607e14d2d49135d87c195cd2aa908011a9c
        B/tables/TABLE-2-page-4-2/meta.json: 460aabc87919ec0228e0c86bc1aaef6d1242ae86fdedd57f1fac3e93b73851bc
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
      pdf_sha256: 4d8f454c8af2f92a90919680da4e4ad04f89a6b2bb7ede1a540f8c485b5efd86
      source_review: _compare/relationships-2026-11-16/review-current/Buchsbaum2011
      source_status_sha256: 3c6955255ec66d70fe7ec098094cccce60bd971a2a5cfe7f660a023385c04a7e
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R003
    exposure:
      text: phonological working memory (encoding and delay phases)
    outcome:
      text: brain activation
    analysis_label: Conjunction of encoding and delay contrasts
    relation: association
    evidence_ids:
    - P5-S1-C6
    qualifier_ids:
    - P5-S1-C16
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 4d8f454c8af2f92a90919680da4e4ad04f89a6b2bb7ede1a540f8c485b5efd86
      source_review: _compare/relationships-2026-11-16/review-current/Buchsbaum2011
      source_status_sha256: 3c6955255ec66d70fe7ec098094cccce60bd971a2a5cfe7f660a023385c04a7e
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P3-S3-C6
      - Result passage disposed without unit P4-S1-C2
      - Result passage disposed without unit P4-S1-C8
      - Result passage disposed without unit P4-S1-C9
      - Accounting without a linked unit P4-S2-C14
      - Accounting without a linked unit P4-S2-C15
      - Accounting without a linked unit P4-S2-C16
      - Accounting without a linked unit P4-S3-C2
      - Unaccounted source passage P4-S2-C15
      - Unaccounted source passage P4-S2-C14
      - Unaccounted source passage P4-S3-C2
      - Unaccounted source passage P4-S2-C16
      - Accounting without a linked unit P4-S3-C4
      - Accounting without a linked unit P5-S1-C12
      - Accounting without a linked unit P5-S1-C6
      - Accounting without a linked unit P5-S1-C7
      - Accounting without a linked unit P5-S1-C8
      - Accounting without a linked unit P6-S1-C1
      - Accounting without a linked unit P6-S1-C2
      - Unaccounted source passage P5-S1-C7
      - Unaccounted source passage P5-S1-C12
      - Unaccounted source passage P5-S1-C6
      - Unaccounted source passage P5-S1-C8
      - Unaccounted source passage P4-S3-C4
      - Unaccounted source passage P6-S1-C1
      - Unaccounted source passage P6-S1-C2
      - Result passage disposed without unit P6-S1-C4
      - Result passage disposed without unit P6-S1-C7
      - Result passage disposed without unit P8-S2-C3
      - Accounting without a linked unit P8-S2-C8
      - Unaccounted source passage P8-S2-C8
      unattached_null_or_qualifier_ids:
      - P4-S2-C16
      - P6-S1-C1
      - P6-S1-C7
      suppressed_nonrepresented_units: 13
      default_disposition_count_requires_completeness_check: 230
      unselected_timing_passages:
      - P4-S1-C5
      - P4-S1-C6
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P4-S2-C14
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S2-C16
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S2-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P2-S4-C3
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: analysed_sample
        source_ids:
        - P2-S4-C2
        - P2-S4-C3
        - P4-S1-C5
        - P4-S1-C6
        - P4-S1-C7
        - P4-S1-C10
        - P4-S1-C12
        - P4-S2-C2
        - P4-S2-C3
        - P4-S2-C4
        - P4-S2-C5
        - P4-S2-C6
        - P4-S2-C7
        - P4-S2-C8
        - P4-S2-C9
        - P4-S2-C12
        - P4-S2-C13
        - P4-S3-C10
        - P6-S1-C10
        - P6-S1-C11
        - P6-S2-C2
        - P8-S2-C3
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - analysed_sample
      - validation
      - personal_factors
      - tested_personal_effects
      - adjustment_roles
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-3-1
      - TABLE-2-page-4-2
      - TABLE-3-page-5-3
      unlinked_tables:
      - TABLE-1-page-3-1
      - TABLE-2-page-4-2
      - TABLE-3-page-5-3
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P3-S1
        - P3-S3
        - P4-S2
        - P4-S3
        - P5-S1
        - P5-S2
        - P6-S1
        - P6-S2
        - P6-S3
        - P7-S4
        - P8-S1
        - P8-S3
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 4d8f454c8af2f92a90919680da4e4ad04f89a6b2bb7ede1a540f8c485b5efd86
      source_review: _compare/relationships-2026-11-16/review-current/Buchsbaum2011
      source_status_sha256: 3c6955255ec66d70fe7ec098094cccce60bd971a2a5cfe7f660a023385c04a7e
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C6
      disposition: represented
      result_indexes:
      - 3
      reason: States that maximal lesion overlap in conduction aphasia circumscribes
        area Spt as defined by fMRI.
    - source_id: P2-S4-C4
      disposition: represented
      result_indexes:
      - 3
      reason: Predicts and confirms that maximum lesion probability in conduction
        aphasia contains area Spt.
    - source_id: P3-S3-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the statistical threshold values for encoding and delay maps.
    - source_id: P4-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the null hypothesis distribution threshold for the conjunction
        analysis.
    - source_id: P4-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the nature of naming errors in the patient sample.
    - source_id: P4-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports overall language scores of the patient sample.
    - source_id: P4-S2-C14
      disposition: represented
      result_indexes:
      - 0
      - 1
      reason: Reports prominent activation in frontal, lateral temporal, and parietal
        cortices during encoding and delay.
    - source_id: P4-S2-C15
      disposition: represented
      result_indexes:
      - 0
      reason: Reports activation of bilateral superior temporal lobe auditory and
        multisensory cortex during encoding.
    - source_id: P4-S2-C16
      disposition: represented
      result_indexes:
      - 1
      reason: Reports rehearsal activity confined to left posterior planum temporale
        (Spt), pSTS, and mSTS.
    - source_id: P4-S3-C2
      disposition: represented
      result_indexes:
      - 1
      reason: Reports robust frontal cortex activation during encoding and delay.
    - source_id: P4-S3-C3
      disposition: represented
      result_indexes:
      - 1
      reason: Reports reliable rehearsal activity in supplementary motor area and
        superior parietal cortex.
    - source_id: P4-S3-C4
      disposition: represented
      result_indexes:
      - 1
      reason: Reports the most consistent rehearsal-related activity in the dorsal
        precentral gyrus.
    - source_id: P5-S1-C6
      disposition: represented
      result_indexes:
      - 2
      reason: Reports regions active during both task phases, including area Spt in
        the left planum temporale.
    - source_id: P5-S1-C7
      disposition: represented
      result_indexes:
      - 1
      reason: Reports that auditory cortex was not reliably activated during rehearsal.
    - source_id: P5-S1-C8
      disposition: represented
      result_indexes:
      - 2
      reason: Reports that area Spt and posterior STS were active only in the left
        hemisphere in conjunction analysis.
    - source_id: P5-S1-C12
      disposition: represented
      result_indexes:
      - 0
      - 1
      reason: Provides the whole-brain thresholds for encoding (37%) and delay (28%).
    - source_id: P6-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the general region compromised in conduction aphasia patients.
    - source_id: P6-S1-C2
      disposition: represented
      result_indexes:
      - 2
      reason: Reports the peak percentage of overlap in Spt for the conjunction analysis.
    - source_id: P6-S1-C4
      disposition: represented
      result_indexes:
      - 2
      reason: Reports visual inspection of single subject activation in the posterior
        planum temporale.
    - source_id: P6-S1-C7
      disposition: represented
      result_indexes:
      - 2
      reason: Reports that 100% of subjects in a specific group showed activation
        in the posterior planum temporale.
    - source_id: P6-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the location of lesions in conduction aphasia patients.
    - source_id: P6-S2-C2
      disposition: represented
      result_indexes:
      - 3
      reason: Reports that the peak area of cross-study overlap between lesion and
        fMRI maps is in area Spt.
    - source_id: P6-S2-C3
      disposition: represented
      result_indexes:
      - 3
      reason: Restates that maximum overlap between conduction aphasia lesions and
        fMRI working memory activation was in area Spt.
    - source_id: P8-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the patient sample's lack of 'repetition conduction aphasics'.
    - source_id: P8-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the involvement of posterior lateral STG and STS in conduction
        aphasia lesions.
    unresolved_coverage: []
    pending_source_ids:
    - P1-S1-C6
    - P2-S4-C4
    - P3-S3-C6
    - P4-S1-C2
    - P4-S1-C8
    - P4-S1-C9
    - P4-S3-C2
    - P5-S1-C7
    - P5-S1-C8
    - P5-S1-C12
    - P6-S1-C1
    - P6-S1-C2
    - P6-S1-C4
    - P6-S1-C7
    - P6-S1-C11
    - P6-S2-C3
    - P8-S2-C3
    - P8-S2-C8
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-3-1
    - TABLE-2-page-4-2
    - TABLE-3-page-5-3
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample: []
      recruited_sample:
      - P4-S1-C5
      - P4-S1-C6
      - P4-S1-C7
      - P4-S1-C10
      - P4-S1-C12
      eligibility:
      - P4-S1-C6
      - P4-S1-C7
      imaging_provenance:
      - P4-S2-C2
      - P4-S2-C3
      - P4-S2-C7
      imaging_timing:
      - P4-S2-C2
      outcome_timing:
      - P4-S1-C10
      outcome_definition:
      - P4-S1-C7
      - P4-S1-C9
      validation: []
      analysis_restrictions:
      - P3-S1-C10
      - P3-S2-C10
      - P3-S3-C6
      - P4-S1-C3
      - P5-S1-C12
      - P5-S1-C16
      - P6-S1-C2
      dependent_variable_statement:
      - P2-S4-C3
      - P3-S1-C8
      - P3-S1-C9
      limitations:
      - P6-S1-C3
      - P6-S1-C8
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles: []
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P4-S1-C10
      - P4-S1-C12
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: internal_cross_validation
    held_selections:
    - slot: dependent_variable_statement
      source_id: P4-S2-C14
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S2-C16
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S2-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P2-S4-C3
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: analysed_sample
      source_ids:
      - P2-S4-C2
      - P2-S4-C3
      - P4-S1-C5
      - P4-S1-C6
      - P4-S1-C7
      - P4-S1-C10
      - P4-S1-C12
      - P4-S2-C2
      - P4-S2-C3
      - P4-S2-C4
      - P4-S2-C5
      - P4-S2-C6
      - P4-S2-C7
      - P4-S2-C8
      - P4-S2-C9
      - P4-S2-C12
      - P4-S2-C13
      - P4-S3-C10
      - P6-S1-C10
      - P6-S1-C11
      - P6-S2-C2
      - P8-S2-C3
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
      pdf_sha256: 4d8f454c8af2f92a90919680da4e4ad04f89a6b2bb7ede1a540f8c485b5efd86
      review_sha256: 49a3b204de196752fe98ed72f01273582e2de467be6d7db6fcd6123b74a59e4d
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
      - P5-S1-C6
      source_result: The source describes a conjunction analysis of aggregate fMRI
        data from 105 healthy subjects (age 8-42) to identify brain regions active
        during both the encoding and delay phases of a phonological working memory
        task. The result identifies a cluster of activity in the left planum temporale
        (area Spt) and other regions (prefrontal, intraparietal, STS). The source
        notes that while the peak overlap in Spt was 33% in the group map due to anatomical
        variability, visual inspection of single subjects confirmed activity in this
        region.
      result_status: detected
      patient_measurement: functional_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis is the conjunction of encoding and delay contrasts
            from the aggregate fMRI study (105 subjects). The source (P5-S1-C2, P5-S1-C6)
            confirms this specific analysis was performed to find regions active in
            both phases.
          source_ids:
          - P5-S1-C2
          - P5-S1-C6
        direction:
          answer: fits
          reason: The source reports that area Spt was active in the conjunction analysis
            (P5-S1-C6). The draft claims a cluster was 'reliably active', which aligns
            with the source's finding of activation, despite the noted variability
            in peak overlap percentages.
          source_ids:
          - P5-S1-C6
          - P6-S1-C2
        construct:
          answer: fits
          reason: The exposure is phonological working memory (encoding/delay), the
            outcome is brain activation, and the method is fMRI. The source confirms
            the use of fMRI aggregate analysis for these phases (P2-S4-C2, P3-S1-C4).
            The patient measurement is correctly identified as functional imaging
            (fMRI activation), not lesion overlap or diffusion, as the 105-subject
            analysis is distinct from the 14-patient lesion overlay analysis.
          source_ids:
          - P2-S4-C2
          - P3-S1-C4
          - P5-S1-C6
        qualifications:
          answer: fits
          reason: The draft includes the qualification that the finding is based on
            an aggregate analysis of five studies and mentions the limitation regarding
            neuroanatomical variability affecting the peak overlap percentage. These
            are present in the source (P2-S4-C2, P6-S1-C2, P6-S1-C3).
          source_ids:
          - P2-S4-C2
          - P6-S1-C2
          - P6-S1-C3
        missing_material_caveat:
          answer: fits
          reason: The draft captures the main caveat regarding the 33% peak overlap
            and anatomical variability. No other material caveats that change the
            interpretation of the conjunction result are omitted from the provided
            source window.
          source_ids:
          - P6-S1-C2
          - P6-S1-C3
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
      id: R003
      exposure:
        text: phonological working memory (encoding and delay phases)
      outcome:
        text: brain activation
      analysis_label: Conjunction of encoding and delay contrasts
      relation: association
      evidence_ids:
      - P5-S1-C6
      qualifier_ids:
      - P5-S1-C16
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 4d8f454c8af2f92a90919680da4e4ad04f89a6b2bb7ede1a540f8c485b5efd86
        source_review: _compare/relationships-2026-11-16/review-current/Buchsbaum2011
        source_status_sha256: 3c6955255ec66d70fe7ec098094cccce60bd971a2a5cfe7f660a023385c04a7e
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P5-S1-C6:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 4d8f454c8af2f92a90919680da4e4ad04f89a6b2bb7ede1a540f8c485b5efd86
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 38f5c6f771f0b6a929632e62928e1b61a2907b4c649e73daabd5a7f2c3042d33
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P5-S1-C6
          page: 5
          text_layer_sha256: 38f5c6f771f0b6a929632e62928e1b61a2907b4c649e73daabd5a7f2c3042d33
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: "As can be seen in Fig. 3, a number of regions were active\
          \ during\nboth task phases, including dorsal and ventral portions of the\
          \ pre-\nfrontal cortex the intraparietal sulcus, STS bilaterally, and area\
          \ Spt\nin the left planum temporale (see Table 3 for MNI coordinates of\n\
          activated clusters; maximum coordinate: \x0251, \x0243, 20)."
        anchor_text: "As can be seen in Fig. 3, a number of regions were active during\n\
          both task phases, including dorsal and ventral portions of the pre-\nfrontal\
          \ cortex the intraparietal sulcus, STS bilaterally, and area Spt\nin the\
          \ left planum temporale (see Table 3 for MNI coordinates of\nactivated clusters;\
          \ maximum coordinate: \x0251, \x0243, 20)."
        excluded_fragments: []
      P2-S4-C8:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 4d8f454c8af2f92a90919680da4e4ad04f89a6b2bb7ede1a540f8c485b5efd86
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 0e209ee97e827929780a15db83a1925ee801af060c7a5ae2cf021d59e6fc2bdb
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S4-C8
          page: 2
          text_layer_sha256: 0e209ee97e827929780a15db83a1925ee801af060c7a5ae2cf021d59e6fc2bdb
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'The studies were selected because each

          involved auditory presentation of verbal material followed by a de-

          lay period involving verbal rehearsal, and because relevant con-

          trasts for these ‘‘encoding’’ and ‘‘delay’’ phases of the task were

          available (in non-normalized ‘‘native’’ image space) for each of

          the 105 individual subjects (age range: 8–42) that took part in

          the studies.'
        anchor_text: 'The studies were selected because each

          involved auditory presentation of verbal material followed by a de-

          lay period involving verbal rehearsal, and because relevant con-

          trasts for these ‘‘encoding’’ and ‘‘delay’’ phases of the task were

          available (in non-normalized ‘‘native’’ image space) for each of

          the 105 individual subjects (age range: 8–42) that took part in

          the studies.'
        excluded_fragments: []
        image_sha256: 4c6697f246c66853c67d5a5655efd67ffddbf5cd560d3f50338cdc165cd54209
        transcription: '. The studies were selected because each

          involved auditory presentation of verbal material followed by a de-

          lay period involving verbal rehearsal, and because relevant con-

          trasts for these “encoding” and “delay” phases of the task were

          available (in non-normalized “native” image space) for each of

          the 105 individual subjects (age range: 8–42) that took part in the

          studies'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 5
  quote: "As can be seen in Fig. 3, a number of regions were active during\nboth task\
    \ phases, including dorsal and ventral portions of the pre-\nfrontal cortex the\
    \ intraparietal sulcus, STS bilaterally, and area Spt\nin the left planum temporale\
    \ (see Table 3 for MNI coordinates of\nactivated clusters; maximum coordinate:\
    \ \x0251, \x0243, 20)."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-23'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
