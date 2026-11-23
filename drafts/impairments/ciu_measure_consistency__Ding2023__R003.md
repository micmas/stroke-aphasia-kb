---
id: ciu_measure_consistency
name: CIU measure consistency
kind: impairment
findings:
- id: f1
  target: ciu_measure_consistency
  target_kind: impairment
  claim: 'CIU measures (#CIUs, CIUs/min, and %CIUs) are highly consistent across elicitation
    genres, with #CIUs and CIUs/min being strongly correlated and both moderately
    correlated with %CIUs.'
  direction: likely
  relationship: correlational
  method: behavioral_only
  sample:
    n: 80
    population: native English speakers with post-stroke aphasia following left hemisphere
      stroke
    phase: not_reported
    time_post_onset: concurrent
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations: []
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Consistency between three measures of informativeness
    in spoken discourse: total number of correct information units (#CIUs), rate of
    production (CIUs/min), and percentage of output (%CIUs), measured across 10 discourse
    samples in three genres. measures were averaged across all tasks; different CIU
    measures were described as only weakly dissociable. Additional metadata has not
    been transcribed; review the pending-field flags before approval. PDF image reading
    (P3-S1-C5, two-model agreement, human verification pending): Materials and methods


    Participants


    The data set consisted of behavioural data from 80 participants who had suffered
    a left hemisphere stroke that produced some degree of language impairment Original
    text-layer quotation is preserved below.'
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
    - not_transcribed:author_limitations
    - proposed_concept:ciu_measure_consistency
  citation: '@Ding2023'
  source_passages:
  - section: Original source P6-S1-C1
    page: 6
    quote: "\nResults\nBehavioural results\nCIU measures had high consistency across\
      \ all prompts and \ngenres (r > 0.38, P < 0.0009; Fig. 1)."
    supports: claim
  - section: Original source P6-S1-C3
    page: 6
    quote: "These results indicate that CIU measures are high­\nly consistent across\
      \ elicitation genres.\n#CIUs and CIUs/min were strongly correlated (r = 0.73,\
      \ P  \n< 0.0001), and they were moderately correlated with %CIUs \n(r > 0.44,\
      \ P < 0.0001; see Fig. 2), which suggests different \nCIU measures were only\
      \ weakly dissociable in post-stroke \naphasia."
    supports: claim
  - section: Original source P3-S1-C5
    page: 3
    quote: "Materials and methods\nParticipants\nThe data set consisted of behavioural\
      \ data from 80 partici­\npants who had suffered a left hemisphere stroke that\
      \ pro­\nduced \nsome \ndegree \nof \nlanguage \nimpairment."
    supports: sample
  - section: Original source P4-S2-C12
    page: 4
    quote: "Three standard CIU measures were calculated: #CIUs, \nCIUs/min and CIUs\
      \ per cent (#CIUs/number of intelligible \nwords) (Table 2)."
    supports: method
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-23'
relationship_review:
  paper: Ding2023
  proposal_id: R003
  review_status_sha256: 0ea22cd8f27287119a68c98dcb74a841ea1a723a4b3159cc06014f09df67c176
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 77c974f72189c570ff88f3bf0a70c8500180ea52e07d41fd2ca8dcfe591b4454
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 77c974f72189c570ff88f3bf0a70c8500180ea52e07d41fd2ca8dcfe591b4454
        A/passages.json: f3860b57316fcd569aada54cbc92956dff891f5dc59d2d441fb3603834ddd6db
        A/raw.json: 5d7095d97748539a0cda8eb6caba104be2fe6a2e71ea4e1b27b3ff4fa3abfc5f
        A/source-units.json: a4cd94967bb9fda33bf59af2982f7f42b6d64311ed378746932d2e9e211e4169
        A/full-source-units.json: eedb1461b2c13537bc9dba5401dfef2082daa975027a763e34c5d792951bcde7
        A/meta.json: f6a6a551bbcd751af960eaeedb198bab8d55f5eeb963f5a38c5ecd4b85280a0f
        A/table-images/TABLE-1-page-3-1.png: 3d85e76ea61e0d8609a6425193e4111038188be0aec88530bdac71ab2e0fc798
        A/table-images/TABLE-4-page-9-1.png: cb0b890de071ecb9cd4e2f1fb32f476eb400b7954810af6aa541f06ebff4b877
        A/table-images/page-3.png: 38fa1b26565cf0b15a9c1afb2606156b32a1f9b8e77f3cc2805decce3a5d8635
        A/table-images/page-7.png: b8eda8efe11b8c6346d65b073c4fbfe9d87b36e80db6cdd5c65f15c4f298d712
        A/table-images/page-4.png: 626b42271ab6ba2b9e7c05ee478df3a1654f2a8944a472eb81e6e1be8a6d4501
        A/table-images/page-9.png: e06d4ced29e0965d8b59a4534d6de402b8ae15c362d4927f0ea1e116e62d0b8d
        A/table-images/manifest.json: f3e1548d8fd169ba8e7e241c36615eca636c122ca032f6e708dffe658203ff08
        A/table-images/TABLE-2-page-4-1.png: cf3dc4d21b72892e602c9693007dd7fe4c1439954939db95f457a903fdfbb06d
        A/table-images/TABLE-3-page-7-1.png: bde38aab6ffa29e83241abc9ab41f635adfed56acb2088199ade51673e518ca3
        A/clauses/window-03/raw.json: 9cb813e3a1aa5e10d8b5ce11331a8e3f76f731a1ec67bc01795b72748afe640d
        A/clauses/window-03/prompt.txt: c4805683e45b061355e4c36e421af65462479b854f90b71799a8096e82b992fc
        A/clauses/window-03/meta.json: d54258c40fc6fcdc160f5016c0334db6f11bab5dee968abba5fa1232a540b065
        A/clauses/window-04/raw.json: 9409771115d20c7e16ad90e97d3ffb6f1017815d3589e7483300c847c5776075
        A/clauses/window-04/prompt.txt: 0952c7dae111a990202411636af80359f6579cdf0ac5ed485a78d9f5665e55c5
        A/clauses/window-04/meta.json: 22aa8640e1ffc882ecd838fcda1f498534f715d65665abcdba6d5656a303fdac
        A/clauses/window-05/raw.json: e8d32df5efef8885b1c890ca20b1f1c6659c3c84230105d51b01e7a033b9321e
        A/clauses/window-05/prompt.txt: 9d80b0dd60e841097270c805dad45ce84418a062cb76e492d64f4c855e41f44b
        A/clauses/window-05/meta.json: 48c01c4ecb2d35c1591fa8fd86781955868c9eb6f30bf389c80882b0df459e1e
        A/clauses/window-02/raw.json: 8a4d5bcbf6048678fbb6a25c756229d9faedc2ff4adecaa6c66fae119b362292
        A/clauses/window-02/prompt.txt: f95dcc0acd5a613315b5f833b18d1b49ea17db05fe4bf76afbebfc5259db8193
        A/clauses/window-02/meta.json: 1941d737833ed7f2f7e1f807cf383fb3b7ccc39aced6b3f65803baa1623945d0
        A/clauses/window-07/raw.json: af599bbd9a8f0dde4c3a050a45301ae124bb37a3f559f635146a3c435da3a128
        A/clauses/window-07/prompt.txt: 31aa53082e81ad9b52a62bfceca3524e260807e6a8c61e75b6499d1ced99718e
        A/clauses/window-07/meta.json: 303e55a8f37a92017b46c3bf015143804d2c8d1e53cd707a632258edc0721d00
        A/clauses/window-01/raw.json: 1b318da6e3d8eb5c963c75e7938759895031ca7ae412ad89404ad811cf64e0b3
        A/clauses/window-01/prompt.txt: a254022807f300e311ec0ce7820e9a1183c6c58037f5a26778b7ae54a9dc68e2
        A/clauses/window-01/meta.json: 7dd76dcee80c9ae3cc9788b4861f4a1185dc96f8a4330833ec123b9cdd44797e
        A/clauses/window-06/raw.json: 14d7cd83e8e47a68781d6a7747bf3aa62247e2ecc2dd3bfdfb1522bfce88f967
        A/clauses/window-06/prompt.txt: a6900a769aae93da8c44a41a1334feedafdb2972e2764afea7ab834ad913eff7
        A/clauses/window-06/meta.json: fb13e5ad04307db1b0d8b93832e0beb46192cfa4aafe7209a83f791139b1aa3f
        A/clauses/window-08/raw.json: 303c3e735890b3c42de44a53dcb78bcfc248206d2bc77b2f81f8f5f08c2c81dc
        A/clauses/window-08/prompt.txt: d7579e0f31f307036008482512da863b7def720dc010d02feb4ed7bc54bfb196
        A/clauses/window-08/meta.json: 82057a811dfe43e19265dbb1da3ff626a6c292650df05f943fd5d297533a3bdb
        A/tables/TABLE-1-page-3-1/raw.json: 11c92d2622b81ceee791ff80d35b3cc9e8c94d480c11e4c41a613057e0e53eb8
        A/tables/TABLE-1-page-3-1/prompt.txt: 2d549d9d561de7ac8197a95da996ac4c8263eb0bca2aa6a6f0deff542ebcaccd
        A/tables/TABLE-1-page-3-1/meta.json: ec84b79cd1daaecc025d0104e434d5cb75a7f1d9014570495d02f5604f807106
        A/tables/TABLE-3-page-7-3/raw.json: faf9e51dd2296b13fab88105c65b19c8fda0e932bfa3df11d3e5c19477aec0b7
        A/tables/TABLE-3-page-7-3/prompt.txt: 306fd0c23d414ff5706a7f50256afddf5aa10938976b1a7313e080146c034f9b
        A/tables/TABLE-3-page-7-3/meta.json: 6bb185eb876b8c43887477e63d4eea351750d9d76b9dadcd500bedb7bc6c7a93
        A/tables/TABLE-4-page-9-4/raw.json: 9b6ba01aa83386b0361e43392c8178f77a85a58fe418f4935cd7e56a92484bf6
        A/tables/TABLE-4-page-9-4/prompt.txt: dfc286be7fc313449813fb4f986428a3af3fb521350f004280c766b3e7f998a8
        A/tables/TABLE-4-page-9-4/meta.json: 3a3cfe88057a5de5607a7f12777f036e56c52a1b6d1a447008f06a879f56b8d6
        A/tables/TABLE-2-page-4-2/raw.json: f1f0cd3bd2efe767852a4582ea7206d9156a9ed5bdde938dfa1dd92fa9d9eccd
        A/tables/TABLE-2-page-4-2/prompt.txt: 5757a6423f613301b2c33c01a312bf9c2df7de9377ba3388639e8929ebeba434
        A/tables/TABLE-2-page-4-2/meta.json: 6bd392895facdd3c221b11f2dcf73a8a623583bbd03888771ab24f627f963d01
        B/passages.json: f3860b57316fcd569aada54cbc92956dff891f5dc59d2d441fb3603834ddd6db
        B/raw.json: a720d1f7f84107f03685cb6d870addb92b7b6d27c0bb7c8c67a3c17326417cf5
        B/source-units.json: a4cd94967bb9fda33bf59af2982f7f42b6d64311ed378746932d2e9e211e4169
        B/full-source-units.json: eedb1461b2c13537bc9dba5401dfef2082daa975027a763e34c5d792951bcde7
        B/meta.json: 691a38ee63db5ba6b4856bf9d4f664926801c6a0ecfa8b7f2b3817441974faea
        B/table-images/TABLE-1-page-3-1.png: 3d85e76ea61e0d8609a6425193e4111038188be0aec88530bdac71ab2e0fc798
        B/table-images/TABLE-4-page-9-1.png: cb0b890de071ecb9cd4e2f1fb32f476eb400b7954810af6aa541f06ebff4b877
        B/table-images/page-3.png: 38fa1b26565cf0b15a9c1afb2606156b32a1f9b8e77f3cc2805decce3a5d8635
        B/table-images/page-7.png: b8eda8efe11b8c6346d65b073c4fbfe9d87b36e80db6cdd5c65f15c4f298d712
        B/table-images/page-4.png: 626b42271ab6ba2b9e7c05ee478df3a1654f2a8944a472eb81e6e1be8a6d4501
        B/table-images/page-9.png: e06d4ced29e0965d8b59a4534d6de402b8ae15c362d4927f0ea1e116e62d0b8d
        B/table-images/manifest.json: 271da6cb012a5654070f0f0f5a799161cb0e267b89bfa89a8035b2996591e8e4
        B/table-images/TABLE-2-page-4-1.png: cf3dc4d21b72892e602c9693007dd7fe4c1439954939db95f457a903fdfbb06d
        B/table-images/TABLE-3-page-7-1.png: bde38aab6ffa29e83241abc9ab41f635adfed56acb2088199ade51673e518ca3
        B/clauses/window-03/raw.json: ade837e1a326772f2cadcd9da243c55c18ececf9497c9711d2e357fccee94cad
        B/clauses/window-03/prompt.txt: c4805683e45b061355e4c36e421af65462479b854f90b71799a8096e82b992fc
        B/clauses/window-03/meta.json: 472c2cd4cc3359e6fe052ba24415ff878168dfff533a9fdf8d4399a961125350
        B/clauses/window-04/raw.json: 9fac8ca6316526f55b8a27b3524340bcb1cada0fbd5d1915dafaffea8225cee5
        B/clauses/window-04/prompt.txt: 0952c7dae111a990202411636af80359f6579cdf0ac5ed485a78d9f5665e55c5
        B/clauses/window-04/meta.json: 47d8e2b3483edf76ff197887b6d29f21701083783519a3f8e944c3f2ddcabf85
        B/clauses/window-05/raw.json: 9a23efc1e08c18be9950c09793e5ae07dea4bb17b9965d27c6cf22ed6e5a135e
        B/clauses/window-05/prompt.txt: 9d80b0dd60e841097270c805dad45ce84418a062cb76e492d64f4c855e41f44b
        B/clauses/window-05/meta.json: 340e3b3c3abbb4c27a383dc6d6850f40dd01ccc8461101d99b021edc81e9f765
        B/clauses/window-02/raw.json: f2e353415a79d31a3fd6002ae547d49657d493c9f363d167624197941243b97f
        B/clauses/window-02/prompt.txt: f95dcc0acd5a613315b5f833b18d1b49ea17db05fe4bf76afbebfc5259db8193
        B/clauses/window-02/meta.json: ba185b2fd9e7f06c355f8de8b344ae9b669d51a0562c1c36bdf1b83701aa2e4f
        B/clauses/window-07/raw.json: 97c0e35cbf12e5a2358c07ff20bd98ecd360b6691d0e77894f1dbcd101ebaf69
        B/clauses/window-07/prompt.txt: 31aa53082e81ad9b52a62bfceca3524e260807e6a8c61e75b6499d1ced99718e
        B/clauses/window-07/meta.json: e83e7aaaeaf17311aa90f27aa0b24ba578bbc99f191a4de38eae2a7df633e3e7
        B/clauses/window-01/raw.json: b652822d116940b0b03aa2c08a0e113a7eea351ba03b98544a5504b0cad82910
        B/clauses/window-01/prompt.txt: a254022807f300e311ec0ce7820e9a1183c6c58037f5a26778b7ae54a9dc68e2
        B/clauses/window-01/meta.json: 62e433650929d877ba08ef8661a71b484c8920050cb42a43d46bac394a47ca34
        B/clauses/window-06/raw.json: b9fcccd159669d2318f39d45a3c3c452f7ac1f9b070b9003a7df071a9d7ef688
        B/clauses/window-06/prompt.txt: a6900a769aae93da8c44a41a1334feedafdb2972e2764afea7ab834ad913eff7
        B/clauses/window-06/meta.json: fdf3d9f39bcc340f97e39ca495183cdba68080341aba13fd26e6dae471f4b4a2
        B/clauses/window-08/raw.json: f3a404f843efaad5cf719cb1be5f5bc2993d38e197d6f3ae05dce071f8c7913c
        B/clauses/window-08/prompt.txt: d7579e0f31f307036008482512da863b7def720dc010d02feb4ed7bc54bfb196
        B/clauses/window-08/meta.json: 38d238c95ac2ed9053f6157813979951c36f12c15a2bdf18e06ecb635c42e0cb
        B/tables/TABLE-1-page-3-1/raw.json: 11c92d2622b81ceee791ff80d35b3cc9e8c94d480c11e4c41a613057e0e53eb8
        B/tables/TABLE-1-page-3-1/prompt.txt: 2d549d9d561de7ac8197a95da996ac4c8263eb0bca2aa6a6f0deff542ebcaccd
        B/tables/TABLE-1-page-3-1/meta.json: 7ec11b3717f538795bb4a99f440b8a30bc7d2763501ba5d0e8166ec623b8ded7
        B/tables/TABLE-3-page-7-3/raw.json: eb64542bfd0295fab38273c3fcfc84ab7489ec7a2d11031f44c07ba5a3a1193f
        B/tables/TABLE-3-page-7-3/prompt.txt: 306fd0c23d414ff5706a7f50256afddf5aa10938976b1a7313e080146c034f9b
        B/tables/TABLE-3-page-7-3/meta.json: 5a93fb10b6898407cc184b8cfc69b0f2152d3ec4f022e343484ff49150d628af
        B/tables/TABLE-4-page-9-4/raw.json: 3490b1728d05ad5c90ad4dd197bdee5928a4de70cb62baf5db3032aa772debef
        B/tables/TABLE-4-page-9-4/prompt.txt: dfc286be7fc313449813fb4f986428a3af3fb521350f004280c766b3e7f998a8
        B/tables/TABLE-4-page-9-4/meta.json: 36b921717a684f3318558285ee647768ff09c3079fdd5ac47507788c40eed0da
        B/tables/TABLE-2-page-4-2/raw.json: adc14d244807e849f674912e97a000e85140e198250f69ce6f8ba031fbbba54f
        B/tables/TABLE-2-page-4-2/prompt.txt: 5757a6423f613301b2c33c01a312bf9c2df7de9377ba3388639e8929ebeba434
        B/tables/TABLE-2-page-4-2/meta.json: 4d46689c0fed15b113154db29b82144e778226bd2f3b9680eaada0030656bf92
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
      pdf_sha256: 77c974f72189c570ff88f3bf0a70c8500180ea52e07d41fd2ca8dcfe591b4454
      source_review: _compare/relationships-2026-11-16/review-current/Ding2023
      source_status_sha256: 543fad80ede5b259e6db5d74e8d6f329ae6a5e5a1192bc31a29ce9f18965fdfe
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R003
    exposure:
      text: CIU measures (#CIUs, CIUs/min, %CIUs)
    outcome:
      text: CIU measures
    analysis_label: CIU Measure Correlation
    relation: association
    evidence_ids:
    - P6-S1-C3
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
      pdf_sha256: 77c974f72189c570ff88f3bf0a70c8500180ea52e07d41fd2ca8dcfe591b4454
      source_review: _compare/relationships-2026-11-16/review-current/Ding2023
      source_status_sha256: 543fad80ede5b259e6db5d74e8d6f329ae6a5e5a1192bc31a29ce9f18965fdfe
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P1-S1-C8
      - Accounting without a linked unit P4-S2-C10
      - Accounting without a linked unit P4-S2-C11
      - Accounting without a linked unit P4-S2-C6
      - Accounting without a linked unit P4-S2-C7
      - Unaccounted source passage P4-S2-C7
      - Unaccounted source passage P4-S2-C10
      - Unaccounted source passage P4-S2-C11
      - Unaccounted source passage P4-S2-C6
      - Result passage disposed without unit P6-S1-C1
      - Result passage disposed without unit P6-S1-C10
      - Result passage disposed without unit P8-S1-C1
      - Result passage disposed without unit P8-S1-C15
      - Result passage disposed without unit P8-S1-C3
      - Result passage disposed without unit P10-S1-C10
      - Result passage disposed without unit P10-S1-C11
      - Result passage disposed without unit P10-S2-C8
      - Result passage disposed without unit P10-S2-C12
      - Unresolved source passage P10-S4-C2
      - Result passage disposed without unit P11-S2-C8
      - Accounting without a linked unit P11-S4-C3
      - Accounting without a linked unit P12-S1-C1
      - Unaccounted source passage P11-S4-C3
      - Unaccounted source passage P12-S1-C1
      unattached_null_or_qualifier_ids:
      - P8-S1-C15
      - P10-S1-C11
      - P11-S2-C8
      suppressed_nonrepresented_units: 9
      default_disposition_count_requires_completeness_check: 146
      unselected_timing_passages:
      - P3-S1-C2
      - P3-S1-C7
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P6-S1-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P5-S2-C10
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P5-S2-C11
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P5-S3-C2
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P5-S3-C4
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P5-S3-C5
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P5-S3-C6
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P5-S3-C7
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P5-S3-C9
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P10-S1-C2
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P10-S1-C4
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P10-S1-C5
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P10-S1-C9
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P10-S1-C10
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P10-S1-C13
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P10-S1-C14
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P10-S1-C15
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P10-S2-C3
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P10-S2-C10
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P11-S2-C9
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: tested_personal_effects
        source_id: P5-S3-C2
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P5-S3-C4
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P5-S3-C5
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P10-S1-C4
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: imaging_provenance
        source_ids:
        - P4-S2-C13
        - P4-S2-C14
        - P4-S2-C15
        - P4-S2-C16
        - P5-S2-C7
        - P5-S3-C7
        - P5-S3-C8
        - P8-S1-C10
        - P10-S1-C14
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - imaging_provenance
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-3-1
      - TABLE-2-page-4-2
      - TABLE-3-page-7-3
      - TABLE-4-page-9-4
      unlinked_tables:
      - TABLE-1-page-3-1
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P6-S1
        - P6-S2
        - P7-S1
        - P8-S1
        - P9-S1
        - P9-S2
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 77c974f72189c570ff88f3bf0a70c8500180ea52e07d41fd2ca8dcfe591b4454
      source_review: _compare/relationships-2026-11-16/review-current/Ding2023
      source_status_sha256: 543fad80ede5b259e6db5d74e8d6f329ae6a5e5a1192bc31a29ce9f18965fdfe
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Title of the paper
    - source_id: P1-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Abstract statement of results, repeated in results section
    - source_id: P1-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Abstract statement of results, repeated in results section
    - source_id: P3-S3-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Demographic information regarding ethnicity
    - source_id: P4-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of data collection requirements
    - source_id: P4-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Inter-rater reliability statistics
    - source_id: P4-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Inter-rater reliability statistics by genre
    - source_id: P4-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Intra-rater reliability statistics
    - source_id: P4-S2-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Intra-rater reliability statistics by genre
    - source_id: P6-S1-C1
      disposition: represented
      result_indexes:
      - 0
      reason: Establishes high consistency of CIU measures across prompts and genres
    - source_id: P6-S1-C2
      disposition: represented
      result_indexes:
      - 1
      reason: Establishes no significant difference in consistency between and within
        genres
    - source_id: P6-S1-C3
      disposition: represented
      result_indexes:
      - 2
      reason: Establishes correlations between different CIU measures
    - source_id: P6-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: PCA component extraction description
    - source_id: P6-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: PCA variance explanation
    - source_id: P6-S1-C7
      disposition: represented
      result_indexes:
      - 3
      reason: Establishes relationship between CIU measures and PCA components
    - source_id: P6-S1-C8
      disposition: represented
      result_indexes:
      - 3
      reason: Establishes unique role of semantic ability in %CIUs
    - source_id: P6-S1-C9
      disposition: represented
      result_indexes:
      - 4
      reason: Establishes correlation between CIU measures and total lesion size
    - source_id: P6-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of lesion overlay map
    - source_id: P6-S1-C11
      disposition: represented
      result_indexes:
      - 5
      - 6
      - 7
      reason: 'Reports significance of lesion LSM for #CIUs, CIUs/min, and %CIUs'
    - source_id: P6-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to figures
    - source_id: P6-S2-C3
      disposition: represented
      result_indexes:
      - 5
      - 6
      reason: Identifies location of voxels in dorsal stream white matter tracts
    - source_id: P6-S2-C4
      disposition: represented
      result_indexes:
      - 5
      reason: 'Specifies regions for #CIUs in lesion LSM'
    - source_id: P6-S2-C5
      disposition: represented
      result_indexes:
      - 6
      reason: Specifies regions for CIUs/min in lesion LSM
    - source_id: P6-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Interpretive statement about white matter damage
    - source_id: P6-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Introduction to disconnection LSM
    - source_id: P6-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of Figure 1
    - source_id: P6-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of Figure 1
    - source_id: P6-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of Figure 1
    - source_id: P6-S2-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of Figure 1
    - source_id: P6-S2-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of Figure 1
    - source_id: P6-S2-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statistical result for Figure 1 comparisons
    - source_id: P7-S1-C1
      disposition: represented
      result_indexes:
      - 8
      - 9
      reason: 'Reports significance of disconnection LSM for #CIUs and CIUs/min'
    - source_id: P7-S1-C2
      disposition: represented
      result_indexes:
      - 10
      reason: Reports non-significance of disconnection LSM for %CIUs
    - source_id: P7-S1-C4
      disposition: represented
      result_indexes:
      - 8
      - 9
      reason: Identifies solution-relevant voxels in dorsal white matter pathways
    - source_id: P7-S1-C5
      disposition: represented
      result_indexes:
      - 8
      reason: 'Specifies critical tracts and regions for #CIUs in disconnection LSM'
    - source_id: P7-S1-C6
      disposition: represented
      result_indexes:
      - 9
      reason: Specifies critical tracts and regions for CIUs/min in disconnection
        LSM
    - source_id: P7-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Summary statement of overlap
    - source_id: P7-S1-C9
      disposition: represented
      result_indexes:
      - 11
      - 12
      reason: Reports tract-wise LSM correlations for dorsal and ventral pathways
    - source_id: P8-S1-C1
      disposition: represented
      result_indexes:
      - 12
      reason: Specifies lack of correlation with ventral pathways
    - source_id: P8-S1-C2
      disposition: represented
      result_indexes:
      - 13
      reason: Reports no significant tract correlations for %CIUs
    - source_id: P8-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Summary statement of convergence
    - source_id: P8-S1-C15
      disposition: repeated
      result_indexes:
      - 13
      reason: Restatement of non-significant %CIUs LSM
    - source_id: P9-S1-C2
      disposition: represented
      result_indexes:
      - 14
      reason: Reports interaction between aphasia subtypes and CIU measures
    - source_id: P9-S1-C3
      disposition: represented
      result_indexes:
      - 14
      reason: 'Reports higher consistency for #CIUs in anomic/fluent groups'
    - source_id: P9-S1-C4
      disposition: represented
      result_indexes:
      - 14
      reason: Reports higher consistency for %CIUs and CIUs/min in anomic group
    - source_id: P9-S1-C5
      disposition: represented
      result_indexes:
      - 11
      reason: Provides partial correlation coefficients for tract-wise LSM
    - source_id: P10-S1-C2
      disposition: represented
      result_indexes:
      - 15
      reason: Reports %CIUs correlation with AF damage after excluding severe impairment
    - source_id: P10-S1-C3
      disposition: represented
      result_indexes:
      - 16
      reason: Reports non-significant lesion LSM for restricted sample
    - source_id: P10-S1-C5
      disposition: represented
      result_indexes:
      - 17
      reason: Reports persistence of dorsal white matter effects when controlling
        for repetition
    - source_id: P10-S1-C6
      disposition: represented
      result_indexes:
      - 18
      reason: Reports %CIUs correlation with posterior grey matter when controlling
        for repetition
    - source_id: P10-S1-C7
      disposition: represented
      result_indexes:
      - 19
      reason: 'Reports non-significant lesion LSM for #CIUs and CIUs/min when controlling
        for repetition'
    - source_id: P10-S1-C8
      disposition: represented
      result_indexes:
      - 20
      reason: Reports effect of apraxia covariate on LSM results
    - source_id: P10-S1-C10
      disposition: represented
      result_indexes:
      - 21
      reason: Reports consistency of dorsal white matter pathways across genres
    - source_id: P10-S1-C11
      disposition: represented
      result_indexes:
      - 22
      reason: 'Reports non-significant lesion LSM for #CIUs in specific genres'
    - source_id: P10-S1-C12
      disposition: represented
      result_indexes:
      - 23
      reason: 'Reports correlation of inferior frontal gyrus with #CIUs in picture
        sequence genre'
    - source_id: P10-S1-C13
      disposition: represented
      result_indexes:
      - 24
      reason: Reports correlation of AF with %CIUs in tract LSM for specific genre
    - source_id: P10-S1-C15
      disposition: represented
      result_indexes:
      - 25
      reason: Reports persistence of dorsal white matter pathways in lesion/tract
        LSM with MIITRA template
    - source_id: P10-S2-C1
      disposition: represented
      result_indexes:
      - 26
      reason: Reports loss of effect in disconnection LSM with MIITRA template
    - source_id: P10-S1-C16
      disposition: represented
      result_indexes:
      - 27
      reason: Reports correlation between %CIUs and AF in tract LSM with MIITRA template
    - source_id: P10-S2-C4
      disposition: represented
      result_indexes:
      - 28
      reason: Reports lesion correlates of WAB fluency
    unresolved_coverage:
    - source_id: P6-S1-C12
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P6-S2-C6
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P6-S2-C7
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P6-S2-C8
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P6-S2-C9
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P6-S2-C10
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P6-S2-C11
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P6-S2-C12
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P9-S1-C5
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P10-S2-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P10-S2-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S2-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S2-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S2-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S2-C12
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S3-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S3-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S3-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S3-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S2-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S2-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S2-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S2-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S2-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S2-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S2-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S3-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S3-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S3-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S3-C12
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S4-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S4-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S1-C1
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C1
    - P1-S1-C8
    - P1-S1-C9
    - P3-S3-C2
    - P4-S1-C9
    - P4-S2-C6
    - P4-S2-C7
    - P4-S2-C10
    - P4-S2-C11
    - P6-S1-C5
    - P6-S1-C6
    - P6-S1-C10
    - P6-S2-C3
    - P6-S2-C13
    - P7-S1-C4
    - P7-S1-C7
    - P8-S1-C3
    - P8-S1-C15
    - P10-S2-C8
    - P10-S2-C9
    - P10-S2-C10
    - P10-S2-C11
    - P10-S2-C12
    - P10-S3-C3
    - P10-S3-C5
    - P10-S3-C8
    - P10-S3-C9
    - P11-S1-C2
    - P11-S1-C5
    - P11-S1-C9
    - P11-S2-C2
    - P11-S2-C3
    - P11-S2-C5
    - P11-S2-C7
    - P11-S2-C8
    - P11-S2-C9
    - P11-S2-C10
    - P11-S3-C4
    - P11-S3-C7
    - P11-S3-C10
    - P11-S3-C12
    - P11-S4-C2
    - P11-S4-C3
    - P12-S1-C1
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-3-1
    - TABLE-2-page-4-2
    - TABLE-3-page-7-3
    - TABLE-4-page-9-4
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P1-S1-C5
      recruited_sample:
      - P3-S1-C5
      - P3-S1-C7
      eligibility:
      - P3-S1-C6
      imaging_provenance: []
      imaging_timing:
      - P4-S2-C13
      outcome_timing:
      - P11-S3-C7
      outcome_definition:
      - P2-S1-C5
      - P4-S2-C12
      - P5-S1-C8
      validation:
      - P5-S2-C9
      - P10-S2-C5
      analysis_restrictions:
      - P5-S1-C10
      - P5-S2-C3
      - P5-S3-C4
      - P10-S1-C1
      dependent_variable_statement:
      - P5-S1-C8
      - P5-S1-C9
      - P5-S2-C3
      - P8-S1-C11
      limitations:
      - P11-S3-C6
      - P11-S3-C7
      - P11-S3-C8
      - P11-S3-C10
      - P11-S3-C11
      personal_factors:
      - P3-S1-C6
      - P3-S1-C8
      - P3-S2-C1
      - P3-S2-C2
      - P3-S2-C3
      - P6-S1-C4
      - P10-S1-C4
      tested_personal_effects:
      - P11-S2-C5
      adjustment_roles:
      - P5-S1-C9
      - P5-S2-C3
      - P5-S2-C8
      - P5-S3-C5
      - P8-S1-C11
      - P9-S1-C10
      - P10-S1-C4
      - P10-S1-C5
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P3-S1-C6
      - P3-S1-C8
      - P3-S2-C1
      - P3-S2-C2
      - P3-S2-C3
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: internal_cross_validation
    held_selections:
    - slot: dependent_variable_statement
      source_id: P6-S1-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P5-S2-C10
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P5-S2-C11
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P5-S3-C2
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P5-S3-C4
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P5-S3-C5
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P5-S3-C6
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P5-S3-C7
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P5-S3-C9
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P10-S1-C2
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P10-S1-C4
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P10-S1-C5
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P10-S1-C9
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P10-S1-C10
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P10-S1-C13
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P10-S1-C14
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P10-S1-C15
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P10-S2-C3
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P10-S2-C10
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P11-S2-C9
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: tested_personal_effects
      source_id: P5-S3-C2
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P5-S3-C4
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P5-S3-C5
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P10-S1-C4
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: imaging_provenance
      source_ids:
      - P4-S2-C13
      - P4-S2-C14
      - P4-S2-C15
      - P4-S2-C16
      - P5-S2-C7
      - P5-S3-C7
      - P5-S3-C8
      - P8-S1-C10
      - P10-S1-C14
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
      pdf_sha256: 77c974f72189c570ff88f3bf0a70c8500180ea52e07d41fd2ca8dcfe591b4454
      review_sha256: 0ea22cd8f27287119a68c98dcb74a841ea1a723a4b3159cc06014f09df67c176
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
      - P6-S1-C3
      source_result: 'The source reports that #CIUs and CIUs/min were strongly correlated
        (r = 0.73, P < 0.0001) and moderately correlated with %CIUs (r > 0.44, P <
        0.0001), indicating that the CIU measures are highly consistent and only weakly
        dissociable in post-stroke aphasia.'
      result_status: detected
      patient_measurement: non_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis corresponds to the correlation of CIU measures
            described in P6-S1-C3, which matches the proposed core's focus on CIU
            measure consistency.
          source_ids:
          - P6-S1-C3
          - P3-S1-C3
        direction:
          answer: fits
          reason: The source explicitly states strong and moderate positive correlations,
            supporting the 'likely' direction of consistency in the draft.
          source_ids:
          - P6-S1-C3
        construct:
          answer: fits
          reason: The exposure and outcome are both CIU measures (#CIUs, CIUs/min,
            %CIUs), and the measurement is behavioral (CIU scoring), not imaging-based.
            The draft correctly identifies this as a behavioral correlation.
          source_ids:
          - P6-S1-C3
          - P4-S2-C12
        qualifications:
          answer: fits
          reason: The draft includes the qualification that measures were averaged
            across tasks and are weakly dissociable, which aligns with the source's
            conclusion in P6-S1-C3.
          source_ids:
          - P6-S1-C3
          - P3-S3-C3
        missing_material_caveat:
          answer: fits
          reason: No material caveats regarding the specific correlation analysis
            are omitted. The source notes high consistency, and the draft reflects
            this without introducing conflicting or missing critical limitations for
            this specific result.
          source_ids:
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
        text: CIU measures (#CIUs, CIUs/min, %CIUs)
      outcome:
        text: CIU measures
      analysis_label: CIU Measure Correlation
      relation: association
      evidence_ids:
      - P6-S1-C3
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
        pdf_sha256: 77c974f72189c570ff88f3bf0a70c8500180ea52e07d41fd2ca8dcfe591b4454
        source_review: _compare/relationships-2026-11-16/review-current/Ding2023
        source_status_sha256: 543fad80ede5b259e6db5d74e8d6f329ae6a5e5a1192bc31a29ce9f18965fdfe
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P3-S1-C5:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 77c974f72189c570ff88f3bf0a70c8500180ea52e07d41fd2ca8dcfe591b4454
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 66a22f526a58b468558103fa4bf13db0e699839d4ee9fb3347221221002b0cf7
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S1-C5
          page: 3
          text_layer_sha256: 66a22f526a58b468558103fa4bf13db0e699839d4ee9fb3347221221002b0cf7
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "Materials and methods\nParticipants\nThe data set consisted\
          \ of behavioural data from 80 partici­\npants who had suffered a left hemisphere\
          \ stroke that pro­\nduced \nsome \ndegree \nof \nlanguage \nimpairment."
        anchor_text: "Materials and methods\nParticipants\nThe data set consisted\
          \ of behavioural data from 80 partici­\npants who had suffered a left hemisphere\
          \ stroke that pro­\nduced \nsome \ndegree \nof \nlanguage \nimpairment."
        excluded_fragments: []
        image_sha256: ceff5e1b81471cf89ec3abc8bc384091e18ab2725114edf17a263ff201d26b18
        transcription: 'Materials and methods


          Participants


          The data set consisted of behavioural data from 80 participants who had
          suffered a left hemisphere stroke that produced some degree of language
          impairment'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 6
  quote: "\nResults\nBehavioural results\nCIU measures had high consistency across\
    \ all prompts and \ngenres (r > 0.38, P < 0.0009; Fig. 1)."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-23'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
