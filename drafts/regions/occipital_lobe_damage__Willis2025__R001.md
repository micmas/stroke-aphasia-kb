---
id: occipital_lobe_damage
name: occipital lobe damage cluster
kind: network
findings:
- id: f1
  target: residual_vision
  target_kind: impairment
  claim: The percentage of damage to the affected occipital lobe was significantly
    correlated with residual visual performance across all three psychophysical detection
    tasks.
  direction: likely
  relationship: correlational
  method: LSM
  sample:
    n: not_reported
    population: patients with damage to V1 resulting in homonymous visual field deficits
      (including hemianopia, quadrantanopia, and scotoma)
    phase: not_reported
    time_post_onset: average 40 months after pathology onset (range 6-297 months)
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - lesions were defined manually using T1 scans, which may underestimate involvement
  - behavioral testing considered only a single visual location within the blind field
  - awareness measures were not systematically taken across all participants
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: The proportion of the affected occipital lobe that
    overlapped with the consensus lesion mask, calculated using the MNI structural
    atlas mask and fslmaths tool. Bonferroni corrected for three tasks (p < 0.0167);
    psychophysical results <50% were assigned 50% to prevent artifactual correlations;
    residual vision defined as above-chance responses to visual stimuli presented
    within the affected hemifield. Additional metadata has not been transcribed; review
    the pending-field flags before approval. PDF image reading (P2-S4-C6, two-model
    agreement, human verification pending): . Average time after pathology onset was
    40 months

    (range, 6–297 months) Original text-layer quotation is preserved below. PDF image
    reading (P2-S3-C5, two-model agreement, human verification pending): In each case,
    participants

    were aged 18–80 and had suffered damage to the brain resulting in hom-

    onymous visual field deficits (including, hemianopia, quadrantanopia,

    and scotoma) Original text-layer quotation is preserved below.'
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
    - not_transcribed:sample.n
    - proposed_concept:residual_vision
  citation: '@Willis2025'
  source_passages:
  - section: Original source P6-S1-C4
    page: 6
    quote: 'To determine the eﬀect of overall damage to the occipital cor-

      tex on visual performance, the initial analysis was a basic corre-

      lation of the percentage of occipital damage and psychophysical

      performance on the three tasks.'
    supports: method
  - section: Original source P6-S1-C6
    page: 6
    quote: 'Figure 5 shows the correlations

      for each task, all of which reach signiﬁcance (p < 0.0167;

      Bonferroni corrected for three tasks).'
    supports: claim
  - section: Original source P7-S1-C6
    page: 7
    quote: 'The signiﬁcance level was set at p < 0.0167

      to account for the multiple tasks and performance on all was signiﬁcantly correlated
      with the amount of damage.'
    supports: claim
  - section: Original source P2-S4-C6
    page: 2
    quote: 'Average time after pathology onset was 40 months

      (range, 6–297 months).'
    supports: sample
  - section: Original source P4-S1-C4
    page: 4
    quote: 'The proportion of the occipital cortex and each visual

      area that overlapped with the consensus lesion mask was then calculated

      as a measure of the extent of damage using the fslmaths tool.'
    supports: method
  - section: Original source P2-S3-C5
    page: 2
    quote: 'In each case, participants

      were aged 18–80 and had suﬀered damage to the brain resulting in hom-

      onymous visual ﬁeld deﬁcits (including, hemianopia, quadrantanopia,

      and scotoma).'
    supports: sample
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-26'
relationship_review:
  paper: Willis2025
  proposal_id: R001
  review_status_sha256: 710d9803984ea7be9383dae640b5de86ff04d5d3244744e16c633d69a13740eb
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: db3cb557db05560d6d0e1d137a713d95cfd0d640ed0694702e891099389d6835
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: db3cb557db05560d6d0e1d137a713d95cfd0d640ed0694702e891099389d6835
        A/passages.json: e14d9ede8b9e56ac528965331ec3b3a927234272aa024977afa04a5b967feb46
        A/raw.json: 8435ac4b1731e2e0b3be8649d4bcd783dfb8751e91b83d74457c056a1b2e826b
        A/source-units.json: 3044af84f52a421083d2055db9a173fab1a28086aa467f626d42db21d4ec739b
        A/full-source-units.json: 3f0daf8f8ed5724e64a625812de63ce613ad86210efd5cf91bb94aad2276dbac
        A/meta.json: 8b274578e0984d83643a6255cb88417b9b1d60bd2665ff1b76c04730b93039bc
        A/table-images/TABLE-1-page-3-1.png: e1f217591aa28b99595749edcfec18a8d3f7a1cf293148eca47b617cafb9f5a6
        A/table-images/page-3.png: fd58ccf10fa5e5e6ec22838b1b9b17a4fe002afe8403d9edeb3983294ad1f162
        A/table-images/manifest.json: b53fad97026d5aff1dc3beef588740cf9fcc943cbdd99e1473d49fdd7615cc04
        A/clauses/window-10/raw.json: 1e5b6441f57b2a08613a0b89d20a9e43cf1477ed8b19f7cb197d2169f4761b3c
        A/clauses/window-10/prompt.txt: 9caf221ab0ca0eafeb16f5b822651900276716840e1ce0e6ff0b15678913b8a6
        A/clauses/window-10/meta.json: 5b7f9a5748851b0035df483c1835a3739acab4c33b6d73efb8a0819597e9732e
        A/clauses/window-03/raw.json: 8c71675fc1410fffda449414b2952db7f0978480fece801d04383b073735988e
        A/clauses/window-03/prompt.txt: a7d707a0a94c4e07550f47be621713bcf32a96687593d768f795dd6cf6815d20
        A/clauses/window-03/meta.json: 0ed664bedfbb58025e201049e0b2587696fcc4d50ab7b415f6feab014b1a33a6
        A/clauses/window-04/raw.json: cf09375475f52bc305ca8e361641917bb37f49d0f5e7f87d40a6b83b3bcc327b
        A/clauses/window-04/prompt.txt: 92308eeb794414cb269b9e27fcfa056f26278072d9070d55701cdbf2839dc594
        A/clauses/window-04/meta.json: dda11cd34abe09aef23fd6acef44a562774e40143b1afd6d68c44ccc794bc66c
        A/clauses/window-05/raw.json: bfa08cab1e3dc31f598610527575ce7ff5f1008b146f9dd89fe283b9737a2984
        A/clauses/window-05/prompt.txt: e61df0ca8a3c9de3968cdefb3ee8cf7579d60d2b480f546df0f23bc763f4d464
        A/clauses/window-05/meta.json: f0fbcf912158fe2561d0653f2357114af9c66de87620ecfb31d2d6dcaf0ac69f
        A/clauses/window-02/raw.json: de7bb1e9943ba1a175d444840db71d8af37dd605e9cd77bf50e5af530fd5975a
        A/clauses/window-02/prompt.txt: d7e7146b31eb8f0b81f8de36dd64c9d15e4a12fefb08064a10d4c902739601bf
        A/clauses/window-02/meta.json: 6d3a8b48a6b843b1abe238a0204fadb058eafbeb71cfd7bb976000dda0500ed9
        A/clauses/window-09/raw.json: 84d3aab0fa78bf7efa0ea7eade8165b883eaea16913034fc2ecd6a8beca7c181
        A/clauses/window-09/prompt.txt: 7eff6199d3816ed8f8dcef518667c5561202abfe2f10be3820520a38ad91ae33
        A/clauses/window-09/meta.json: ca0e0149fd51742cf05bb6722f6d5e507d3d475d4336d5dec32442c1243911f1
        A/clauses/window-07/raw.json: d829536121d544c13c2a1e1bb0c578d1449419a0a1d1d599d39e836a77416c0d
        A/clauses/window-07/prompt.txt: f6561fe71e0c024fb3e43ead8ed35fee2f5979792efe42de4744f02a3985b113
        A/clauses/window-07/meta.json: 484eb8c94ccd3d00778349455ce08e096089872d102e67ab7555896ac17644ee
        A/clauses/window-01/raw.json: 8f3cb05984c84b62825fa16ac0b57a362977494ddee89328036f8f71a2decea1
        A/clauses/window-01/prompt.txt: 5a6f8cfb59121783f177d087bc54fe270fea7e4425a7af4bd6022bfb333cc2a0
        A/clauses/window-01/meta.json: b2767b4ccb6e52fab38ca239890ba0f0cb9e55da2fc495182a9b1b0ad77ea5d8
        A/clauses/window-06/raw.json: 8fcb0c815e7860f802d57286357e3dcdb1556d40f0cfd9b92c799c5b137aff98
        A/clauses/window-06/prompt.txt: 99232e69b27ca15657617dba3f535f446ad2095ae6e4aaa343da456c419312cf
        A/clauses/window-06/meta.json: efa7ef0a86d4e60ec88f46c3b7e749041fb1303ce37ea52f30457c3869fc3b82
        A/clauses/window-08/raw.json: 57b2a9a247b595ebbce5eeddedb224848471cbb6906db4691130c847529cd34d
        A/clauses/window-08/prompt.txt: 41fd1e69819db7acef444da008c543196f374de7027640df5ad7f1e387245d15
        A/clauses/window-08/meta.json: 7a3227c6bf70910d40e3a9d64a97abf1587911db832e3edd42f47550fce60e52
        A/tables/TABLE-1-page-3-1/raw.json: 2c14bad2d31e9593f38c50efd8c313e0fc184af4f84d96ee2678a6aa77ca8b33
        A/tables/TABLE-1-page-3-1/prompt.txt: c0a49416dcc056d9648e3dcc26c9660ee6292be506dc73df60eff02989f3b2eb
        A/tables/TABLE-1-page-3-1/meta.json: 61f4d3f8fcb4ac99efea068e053c8d4a3984240cab7bd294d627bf7b7b507e45
        B/passages.json: e14d9ede8b9e56ac528965331ec3b3a927234272aa024977afa04a5b967feb46
        B/raw.json: 1700ffce41fd78a4c3c33da0d7fa46abf02fd88f926dc9e3ac5e367d02b4ad96
        B/source-units.json: 3044af84f52a421083d2055db9a173fab1a28086aa467f626d42db21d4ec739b
        B/full-source-units.json: 3f0daf8f8ed5724e64a625812de63ce613ad86210efd5cf91bb94aad2276dbac
        B/meta.json: 7862a0e97df03b958048dbd08a6ae275b57b2a00f40d0b849f72deb37368fe4d
        B/table-images/TABLE-1-page-3-1.png: e1f217591aa28b99595749edcfec18a8d3f7a1cf293148eca47b617cafb9f5a6
        B/table-images/page-3.png: fd58ccf10fa5e5e6ec22838b1b9b17a4fe002afe8403d9edeb3983294ad1f162
        B/table-images/manifest.json: c275ed9e1496b6b4a26e7c00350f370e1f27ff61e1b8db94dfa2e807e873caeb
        B/clauses/window-10/raw.json: 4144d00811b55c717d4ec68ba2b339b7ad545b580372008be23957b7b3292473
        B/clauses/window-10/prompt.txt: 9caf221ab0ca0eafeb16f5b822651900276716840e1ce0e6ff0b15678913b8a6
        B/clauses/window-10/meta.json: ee49445cbf586bee072ece080601489ec05ae7b14424179faf46691dcc38ae5c
        B/clauses/window-03/raw.json: 82b932ef29e8647eea432ad4d143c8cf38327886755c6269f4dc13588ddb2bb5
        B/clauses/window-03/prompt.txt: a7d707a0a94c4e07550f47be621713bcf32a96687593d768f795dd6cf6815d20
        B/clauses/window-03/meta.json: c48d0680d9c21d3e01965d78dd3e33fa6067e5298a7a66dd0a6c5614787a44f2
        B/clauses/window-04/raw.json: 06034c1ae86333632f26a8ec97fd3cf00d32e88f3e45b25e1ed4b3868ed0214a
        B/clauses/window-04/prompt.txt: 92308eeb794414cb269b9e27fcfa056f26278072d9070d55701cdbf2839dc594
        B/clauses/window-04/meta.json: 91e8dc779f165e2190d3b12630f680faf317854ef74cc1986a526f9363dae22e
        B/clauses/window-05/raw.json: 205e5a265db5a4610ff95e3fd9ace075413d5530d28ae0a73e389d087a5b546b
        B/clauses/window-05/prompt.txt: e61df0ca8a3c9de3968cdefb3ee8cf7579d60d2b480f546df0f23bc763f4d464
        B/clauses/window-05/meta.json: d6b92792a1f3bd5dc98f3d4152c8cce60b7ef176ee4d606130d2e97b8650beda
        B/clauses/window-02/raw.json: 77e6810b747e7488a10eb6f610218ab7689b73e5a7f9a394e5676193ea509065
        B/clauses/window-02/prompt.txt: d7e7146b31eb8f0b81f8de36dd64c9d15e4a12fefb08064a10d4c902739601bf
        B/clauses/window-02/meta.json: 6a9c282e7428a18d6c8f1b232a2874977eb1a299d0db7dc73322dbf09c6db052
        B/clauses/window-09/raw.json: c9924ccfdea1dbf68b7b9bb5ac8486dea7ad67b0e2f803f0d3520b3dd2a40ae6
        B/clauses/window-09/prompt.txt: 7eff6199d3816ed8f8dcef518667c5561202abfe2f10be3820520a38ad91ae33
        B/clauses/window-09/meta.json: 4b7c0045c78e77a87a324b471b1cb918e0d5c0a800765c622b213eae03f9f635
        B/clauses/window-07/raw.json: bbdf120e81ceb3657bf0e1f89ccb03f6bd0bb5df1c302cb9dd5c28638cae7f7c
        B/clauses/window-07/prompt.txt: f6561fe71e0c024fb3e43ead8ed35fee2f5979792efe42de4744f02a3985b113
        B/clauses/window-07/meta.json: ff7e5308571b2862ec8b4107acb175416dd203d5c6a7b6942e1f255a3cc188e5
        B/clauses/window-01/raw.json: aca01c7083ae4bc043271bfeaa8b785856bbd67b5ce7a8f6dd4743039a2ccbcd
        B/clauses/window-01/prompt.txt: 5a6f8cfb59121783f177d087bc54fe270fea7e4425a7af4bd6022bfb333cc2a0
        B/clauses/window-01/meta.json: 23d69ac185183b142959dfec5d203454738108cf3ad819d6823f36c56a521575
        B/clauses/window-06/raw.json: 4fce5b7d723cc8162c1295022aedde3bb6c220849e3bb6f763e097e6b1b8d263
        B/clauses/window-06/prompt.txt: 99232e69b27ca15657617dba3f535f446ad2095ae6e4aaa343da456c419312cf
        B/clauses/window-06/meta.json: 8a421019225ac62644cfcf3e10f40ad6fa1ad97aabcc9e09022e41e6d56e932c
        B/clauses/window-08/raw.json: 734b300a682c4fe70be4b7778196f9b6bd38be1f5d9e4fd6531d0276ab9c8745
        B/clauses/window-08/prompt.txt: 41fd1e69819db7acef444da008c543196f374de7027640df5ad7f1e387245d15
        B/clauses/window-08/meta.json: d17e500677a9230fdf9fe9d3955d6496dcf1c2ee15951b1e3d2762e4a33f4c42
        B/tables/TABLE-1-page-3-1/raw.json: e377056a99d3ed2febdca6168b27124c1cbd67a488f34213cb41442d7aacaafb
        B/tables/TABLE-1-page-3-1/prompt.txt: c0a49416dcc056d9648e3dcc26c9660ee6292be506dc73df60eff02989f3b2eb
        B/tables/TABLE-1-page-3-1/meta.json: 4c8f9a8083cf1004caa34e61f9f6ebfea5182a4ab9094bccf053763520fcb312
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
      pdf_sha256: db3cb557db05560d6d0e1d137a713d95cfd0d640ed0694702e891099389d6835
      source_review: _compare/relationships-2026-11-16/review-current/Willis2025
      source_status_sha256: 5cba363249a89f2cc1ae5437982589d5b7cf93ce8998ecb9f71d5cddf54fd709
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R001
    exposure:
      text: percentage of occipital damage
    outcome:
      text: residual vision (contrast, motion, and face/place tasks)
    analysis_label: Correlation of occipital damage and psychophysical performance
    relation: association
    evidence_ids:
    - P6-S1-C6
    - P7-S1-C6
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
      pdf_sha256: db3cb557db05560d6d0e1d137a713d95cfd0d640ed0694702e891099389d6835
      source_review: _compare/relationships-2026-11-16/review-current/Willis2025
      source_status_sha256: 5cba363249a89f2cc1ae5437982589d5b7cf93ce8998ecb9f71d5cddf54fd709
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P3-S1-C10
      - Result passage disposed without unit P3-S2-C12
      - Result passage disposed without unit P3-S2-C13
      - Result passage disposed without unit P5-S1-C12
      - Result passage disposed without unit P5-S1-C14
      - Result passage disposed without unit P5-S2-C6
      - Result passage disposed without unit P5-S2-C10
      - Result passage disposed without unit P5-S2-C7
      - Result passage disposed without unit P6-S1-C2
      - Result passage disposed without unit P6-S1-C5
      - Result passage disposed without unit P6-S1-C6
      - Result passage disposed without unit P6-S2-C10
      - Result passage disposed without unit P6-S2-C11
      - Result passage disposed without unit P6-S2-C13
      - Result passage disposed without unit P6-S2-C16
      - Result passage disposed without unit P6-S2-C7
      - Result passage disposed without unit P6-S3-C4
      - Result passage disposed without unit P7-S1-C2
      - Result passage disposed without unit P7-S1-C6
      - Result passage disposed without unit P8-S1-C2
      - Result passage disposed without unit P8-S1-C10
      - Result passage disposed without unit P8-S1-C12
      - Result passage disposed without unit P8-S2-C3
      - Accounting without a linked unit P8-S2-C5
      - Accounting without a linked unit P8-S2-C8
      - Unaccounted source passage P8-S2-C5
      - Unaccounted source passage P8-S2-C8
      - Accounting without a linked unit P9-S1-C13
      - Unaccounted source passage P9-S1-C13
      - Accounting without a linked unit P9-S3-C11
      - Unaccounted source passage P9-S3-C11
      - Result passage disposed without unit P9-S4-C5
      unattached_null_or_qualifier_ids:
      - P7-S1-C2
      - P8-S1-C10
      - P8-S1-C12
      - P8-S2-C5
      suppressed_nonrepresented_units: 11
      default_disposition_count_requires_completeness_check: 223
      unselected_timing_passages:
      - P2-S2-C8
      - P2-S4-C5
      - P2-S4-C6
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P6-S2-C12
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P4-S1-C10
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P6-S2-C13
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: analysed_sample
        source_ids:
        - P2-S3-C3
        - P2-S3-C4
        - P2-S3-C5
        - P2-S3-C8
        - P2-S3-C10
        - P2-S3-C11
        - P2-S3-C12
        - P2-S3-C14
        - P2-S3-C15
        - P2-S4-C3
        - P2-S4-C5
        - P2-S4-C6
        - P2-S4-C7
        - P3-S2-C14
        - P3-S2-C15
        - P3-S3-C4
        - P4-S2-C4
        - P4-S2-C6
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: imaging_provenance
        source_ids:
        - P3-S3-C14
        - P3-S3-C15
        - P3-S3-C4
        - P4-S1-C1
        - P4-S1-C2
        - P4-S1-C3
        - P4-S1-C4
        - P4-S1-C5
        - P4-S1-C6
        - P4-S1-C7
        - P4-S1-C8
        - P4-S1-C9
        - P4-S1-C10
        - P4-S1-C11
        - P4-S1-C12
        - P4-S1-C13
        - P4-S2-C3
        - P4-S2-C5
        - P4-S2-C6
        - P4-S2-C7
        - P4-S2-C8
        - P4-S2-C9
        - P4-S2-C10
        - P4-S2-C11
        - P4-S2-C12
        - P4-S2-C13
        - P4-S2-C14
        - P4-S2-C15
        - P4-S2-C16
        - P4-S2-C17
        - P4-S2-C18
        - P5-S1-C1
        - P5-S1-C2
        - P5-S1-C3
        - P5-S1-C4
        - P5-S1-C5
        - P5-S1-C6
        - P5-S1-C7
        - P5-S1-C8
        - P5-S1-C9
        - P5-S1-C10
        - P5-S1-C11
        - P5-S1-C12
        - P5-S1-C13
        - P5-S1-C14
        - P5-S1-C15
        - P5-S1-C16
        - P5-S1-C17
        - P5-S2-C4
        - P5-S2-C5
        - P5-S2-C6
        - P5-S2-C7
        - P5-S2-C8
        - P5-S2-C9
        - P5-S2-C10
        - P5-S2-C12
        - P6-S1-C10
        - P6-S1-C11
        - P6-S1-C12
        - P6-S1-C13
        - P6-S1-C14
        - P6-S2-C8
        - P6-S2-C9
        - P6-S2-C10
        - P6-S2-C11
        - P6-S2-C12
        - P6-S2-C13
        - P6-S2-C14
        - P6-S2-C15
        - P6-S2-C16
        - P7-S1-C8
        - P7-S1-C9
        - P7-S1-C10
        - P7-S1-C11
        - P8-S1-C1
        - P8-S1-C2
        - P8-S1-C3
        - P8-S1-C4
        - P8-S1-C5
        - P8-S1-C6
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: outcome_definition
        source_ids:
        - P2-S4-C9
        - P2-S4-C10
        - P2-S4-C11
        - P2-S4-C12
        - P2-S4-C13
        - P2-S4-C14
        - P2-S4-C15
        - P2-S4-C16
        - P3-S1-C4
        - P3-S1-C5
        - P3-S1-C6
        - P3-S1-C7
        - P3-S1-C8
        - P3-S1-C9
        - P3-S1-C10
        - P3-S1-C11
        - P3-S1-C12
        - P3-S1-C13
        - P3-S1-C14
        - P3-S1-C15
        - P3-S2-C3
        - P3-S2-C4
        - P3-S2-C5
        - P3-S2-C6
        - P3-S2-C7
        - P3-S2-C8
        - P3-S2-C9
        - P3-S2-C10
        - P3-S2-C11
        - P3-S2-C12
        - P3-S2-C13
        - P3-S3-C6
        - P3-S3-C7
        - P3-S3-C8
        - P3-S3-C9
        - P3-S3-C10
        - P3-S3-C11
        - P3-S3-C12
        - P3-S3-C13
        - P3-S3-C14
        - P3-S3-C15
        - P3-S3-C16
        - P3-S4-C1
        - P3-S4-C2
        - P3-S4-C3
        - P4-S1-C1
        - P4-S1-C2
        - P4-S1-C3
        - P4-S1-C4
        - P4-S1-C5
        - P4-S1-C6
        - P4-S1-C7
        - P4-S1-C8
        - P4-S1-C9
        - P4-S1-C10
        - P4-S1-C11
        - P4-S1-C12
        - P4-S1-C13
        - P4-S2-C3
        - P4-S2-C4
        - P4-S2-C5
        - P4-S2-C6
        - P4-S2-C7
        - P4-S2-C8
        - P4-S2-C9
        - P4-S2-C10
        - P4-S2-C11
        - P4-S2-C12
        - P4-S2-C13
        - P4-S2-C14
        - P4-S2-C15
        - P4-S2-C16
        - P4-S2-C17
        - P4-S2-C18
        - P5-S1-C1
        - P5-S1-C2
        - P5-S1-C3
        - P5-S1-C4
        - P5-S1-C5
        - P5-S1-C6
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: limitations
        source_ids:
        - P9-S2-C6
        - P9-S2-C7
        - P9-S2-C8
        - P9-S2-C9
        - P9-S2-C10
        - P9-S2-C11
        - P9-S2-C12
        - P9-S2-C13
        - P9-S2-C14
        - P9-S2-C15
        - P9-S3-C4
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - analysed_sample
      - imaging_provenance
      - outcome_definition
      - validation
      - limitations
      - personal_factors
      - tested_personal_effects
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-3-1
      unlinked_tables:
      - TABLE-1-page-3-1
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P3-S1
        - P3-S3
        - P4-S1
        - P4-S2
        - P5-S1
        - P5-S2
        - P6-S1
        - P6-S2
        - P6-S3
        - P7-S1
        - P8-S2
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: db3cb557db05560d6d0e1d137a713d95cfd0d640ed0694702e891099389d6835
      source_review: _compare/relationships-2026-11-16/review-current/Willis2025
      source_status_sha256: 5cba363249a89f2cc1ae5437982589d5b7cf93ce8998ecb9f71d5cddf54fd709
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C7
      disposition: represented
      result_indexes:
      - 3
      reason: States V1 damage showed no relationship with residual vision and V4/hMT+
        correlated with contrast detection.
    - source_id: P1-S1-C8
      disposition: represented
      result_indexes:
      - 4
      reason: States hMT+/V5 damage impacted performance across all tasks.
    - source_id: P1-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discusses sufficiency of hMT+/V5 for residual vision.
    - source_id: P1-S2-C4
      disposition: represented
      result_indexes:
      - 5
      reason: Links lateral optic radiation damage to poor residual vision via VLSM.
    - source_id: P1-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about extrastriate cortex importance.
    - source_id: P1-S2-C10
      disposition: represented
      result_indexes:
      - 5
      reason: Identifies optic radiation as most highly associated with residual vision.
    - source_id: P3-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes data cleaning for chance performance.
    - source_id: P3-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes stimulus area measurements.
    - source_id: P3-S2-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes combining scrambled images.
    - source_id: P3-S2-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes collapsing face and place categories.
    - source_id: P4-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes mapping of V1 and V4.
    - source_id: P4-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes mapping of hMT+/V5.
    - source_id: P4-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes thresholding sensitivity analysis.
    - source_id: P4-S2-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes example of visual field deficit location.
    - source_id: P5-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes range of participant performance.
    - source_id: P5-S1-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports median performance values.
    - source_id: P5-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes visual area mask size.
    - source_id: P5-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes relationship between volume and threshold.
    - source_id: P5-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes consistency of V1 vs hMT+/V5.
    - source_id: P5-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes variability across thresholds.
    - source_id: P6-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports Friedman test across tasks.
    - source_id: P6-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes range of occipital damage.
    - source_id: P6-S1-C6
      disposition: represented
      result_indexes:
      - 0
      reason: States all three tasks significantly correlated with amount of damage.
    - source_id: P6-S1-C7
      disposition: represented
      result_indexes:
      - 0
      reason: Specifies threshold of 20% occipital damage for loss of residual vision
        in motion/face tasks.
    - source_id: P6-S1-C8
      disposition: represented
      result_indexes:
      - 0
      reason: Specifies contrast task performance persists up to 30-40% damage.
    - source_id: P6-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discusses lesion size as a non-exclusive factor.
    - source_id: P6-S1-C11
      disposition: represented
      result_indexes:
      - 1
      reason: States no relationship between V1 damage and performance for any task.
    - source_id: P6-S1-C13
      disposition: represented
      result_indexes:
      - 2
      reason: States only contrast detection correlated with V4 damage.
    - source_id: P6-S1-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes participants with V4 damage who still performed well.
    - source_id: P6-S2-C2
      disposition: represented
      result_indexes:
      - 3
      reason: States hMT+/V5 damage significantly correlated with contrast task performance.
    - source_id: P6-S2-C3
      disposition: represented
      result_indexes:
      - 4
      reason: States any damage to hMT+/V5 led to chance performance on motion and
        face/place tasks.
    - source_id: P6-S2-C4
      disposition: represented
      result_indexes:
      - 4
      reason: Concludes hMT+/V5 damage significantly impacts residual visual ability.
    - source_id: P6-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discusses participants without hMT+/V5 damage performing at chance.
    - source_id: P6-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes overlap of lesions in participants without hMT+/V5 damage.
    - source_id: P6-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes volume of damaged voxels included in VLSM.
    - source_id: P6-S2-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes maximum overlap in V1.
    - source_id: P6-S2-C12
      disposition: represented
      result_indexes:
      - 5
      reason: Identifies cluster of voxels associated with reduced residual function
        in contrast task.
    - source_id: P6-S2-C13
      disposition: represented
      result_indexes:
      - 5
      reason: Locates VLSM cluster in white matter of optic radiation.
    - source_id: P6-S2-C14
      disposition: represented
      result_indexes:
      - 5
      reason: Identifies tracts within the VLSM volume.
    - source_id: P6-S2-C16
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discusses overlap with independently derived tract.
    - source_id: P7-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discusses effect of sample size on significance.
    - source_id: P7-S1-C6
      disposition: represented
      result_indexes:
      - 0
      reason: Confirms significant correlation between occipital damage and all three
        tasks.
    - source_id: P8-S1-C2
      disposition: represented
      result_indexes:
      - 4
      reason: States none of the patients with hMT+/V5 damage showed residual vision
        for motion or face/place.
    - source_id: P8-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discusses specific participants with small hMT+/V5 damage.
    - source_id: P8-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports no difference in performance between left and right hemisphere
        hMT+/V5 damage.
    - source_id: P8-S2-C3
      disposition: represented
      result_indexes:
      - 5
      reason: Links optic radiation and lateral visual pathway damage to poor residual
        vision.
    - source_id: P8-S2-C5
      disposition: represented
      result_indexes:
      - 2
      reason: States V4 damage did not significantly correlate with face/place detection.
    - source_id: P8-S2-C8
      disposition: represented
      result_indexes:
      - 2
      reason: States significant correlation between contrast stimulus detection and
        V4 damage.
    - source_id: P8-S2-C15
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes lesion size in participants without hMT+/V5 damage.
    - source_id: P8-S2-C18
      disposition: represented
      result_indexes:
      - 5
      reason: Describes the significant voxel cluster in the optic radiation.
    - source_id: P9-S1-C13
      disposition: represented
      result_indexes:
      - 5
      reason: States white matter adjacent to V5/hMT+ was necessary for residual vision.
    - source_id: P9-S4-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion about VLSM application.
    - source_id: P9-S4-C5
      disposition: represented
      result_indexes:
      - 5
      reason: Concludes preservation of lateral optic radiation is most highly associated
        with residual vision.
    unresolved_coverage:
    - source_id: P6-S2-C12
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P6-S3-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S1-C12
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S2-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S3-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S3-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C7
    - P1-S1-C8
    - P1-S2-C3
    - P1-S2-C9
    - P3-S1-C10
    - P3-S2-C9
    - P3-S2-C12
    - P3-S2-C13
    - P4-S1-C1
    - P4-S1-C2
    - P4-S1-C10
    - P4-S2-C14
    - P5-S1-C12
    - P5-S1-C14
    - P5-S2-C4
    - P5-S2-C6
    - P5-S2-C7
    - P5-S2-C10
    - P6-S1-C2
    - P6-S1-C5
    - P6-S1-C7
    - P6-S1-C8
    - P6-S1-C9
    - P6-S1-C14
    - P6-S2-C4
    - P6-S2-C5
    - P6-S2-C7
    - P6-S2-C10
    - P6-S2-C11
    - P6-S2-C14
    - P6-S2-C16
    - P6-S3-C4
    - P7-S1-C2
    - P8-S1-C3
    - P8-S1-C10
    - P8-S1-C12
    - P8-S2-C9
    - P8-S2-C15
    - P8-S2-C18
    - P8-S3-C7
    - P9-S1-C13
    - P9-S3-C11
    - P9-S4-C4
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-3-1
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample: []
      recruited_sample:
      - P2-S3-C4
      - P2-S3-C8
      - P2-S3-C10
      - P2-S3-C11
      - P2-S3-C12
      - P2-S3-C14
      eligibility:
      - P2-S3-C5
      - P2-S3-C6
      imaging_provenance: []
      imaging_timing:
      - P2-S4-C3
      outcome_timing:
      - P2-S4-C3
      outcome_definition: []
      validation: []
      analysis_restrictions:
      - P5-S1-C3
      dependent_variable_statement:
      - P4-S2-C7
      - P5-S1-C4
      - P6-S1-C10
      limitations: []
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P5-S1-C3
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P2-S4-C5
      - P2-S4-C6
      - P3-S4-C1
      - P3-S4-C2
      - P3-S4-C3
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P6-S2-C12
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P4-S1-C10
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P6-S2-C13
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: analysed_sample
      source_ids:
      - P2-S3-C3
      - P2-S3-C4
      - P2-S3-C5
      - P2-S3-C8
      - P2-S3-C10
      - P2-S3-C11
      - P2-S3-C12
      - P2-S3-C14
      - P2-S3-C15
      - P2-S4-C3
      - P2-S4-C5
      - P2-S4-C6
      - P2-S4-C7
      - P3-S2-C14
      - P3-S2-C15
      - P3-S3-C4
      - P4-S2-C4
      - P4-S2-C6
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: imaging_provenance
      source_ids:
      - P3-S3-C14
      - P3-S3-C15
      - P3-S3-C4
      - P4-S1-C1
      - P4-S1-C2
      - P4-S1-C3
      - P4-S1-C4
      - P4-S1-C5
      - P4-S1-C6
      - P4-S1-C7
      - P4-S1-C8
      - P4-S1-C9
      - P4-S1-C10
      - P4-S1-C11
      - P4-S1-C12
      - P4-S1-C13
      - P4-S2-C3
      - P4-S2-C5
      - P4-S2-C6
      - P4-S2-C7
      - P4-S2-C8
      - P4-S2-C9
      - P4-S2-C10
      - P4-S2-C11
      - P4-S2-C12
      - P4-S2-C13
      - P4-S2-C14
      - P4-S2-C15
      - P4-S2-C16
      - P4-S2-C17
      - P4-S2-C18
      - P5-S1-C1
      - P5-S1-C2
      - P5-S1-C3
      - P5-S1-C4
      - P5-S1-C5
      - P5-S1-C6
      - P5-S1-C7
      - P5-S1-C8
      - P5-S1-C9
      - P5-S1-C10
      - P5-S1-C11
      - P5-S1-C12
      - P5-S1-C13
      - P5-S1-C14
      - P5-S1-C15
      - P5-S1-C16
      - P5-S1-C17
      - P5-S2-C4
      - P5-S2-C5
      - P5-S2-C6
      - P5-S2-C7
      - P5-S2-C8
      - P5-S2-C9
      - P5-S2-C10
      - P5-S2-C12
      - P6-S1-C10
      - P6-S1-C11
      - P6-S1-C12
      - P6-S1-C13
      - P6-S1-C14
      - P6-S2-C8
      - P6-S2-C9
      - P6-S2-C10
      - P6-S2-C11
      - P6-S2-C12
      - P6-S2-C13
      - P6-S2-C14
      - P6-S2-C15
      - P6-S2-C16
      - P7-S1-C8
      - P7-S1-C9
      - P7-S1-C10
      - P7-S1-C11
      - P8-S1-C1
      - P8-S1-C2
      - P8-S1-C3
      - P8-S1-C4
      - P8-S1-C5
      - P8-S1-C6
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: outcome_definition
      source_ids:
      - P2-S4-C9
      - P2-S4-C10
      - P2-S4-C11
      - P2-S4-C12
      - P2-S4-C13
      - P2-S4-C14
      - P2-S4-C15
      - P2-S4-C16
      - P3-S1-C4
      - P3-S1-C5
      - P3-S1-C6
      - P3-S1-C7
      - P3-S1-C8
      - P3-S1-C9
      - P3-S1-C10
      - P3-S1-C11
      - P3-S1-C12
      - P3-S1-C13
      - P3-S1-C14
      - P3-S1-C15
      - P3-S2-C3
      - P3-S2-C4
      - P3-S2-C5
      - P3-S2-C6
      - P3-S2-C7
      - P3-S2-C8
      - P3-S2-C9
      - P3-S2-C10
      - P3-S2-C11
      - P3-S2-C12
      - P3-S2-C13
      - P3-S3-C6
      - P3-S3-C7
      - P3-S3-C8
      - P3-S3-C9
      - P3-S3-C10
      - P3-S3-C11
      - P3-S3-C12
      - P3-S3-C13
      - P3-S3-C14
      - P3-S3-C15
      - P3-S3-C16
      - P3-S4-C1
      - P3-S4-C2
      - P3-S4-C3
      - P4-S1-C1
      - P4-S1-C2
      - P4-S1-C3
      - P4-S1-C4
      - P4-S1-C5
      - P4-S1-C6
      - P4-S1-C7
      - P4-S1-C8
      - P4-S1-C9
      - P4-S1-C10
      - P4-S1-C11
      - P4-S1-C12
      - P4-S1-C13
      - P4-S2-C3
      - P4-S2-C4
      - P4-S2-C5
      - P4-S2-C6
      - P4-S2-C7
      - P4-S2-C8
      - P4-S2-C9
      - P4-S2-C10
      - P4-S2-C11
      - P4-S2-C12
      - P4-S2-C13
      - P4-S2-C14
      - P4-S2-C15
      - P4-S2-C16
      - P4-S2-C17
      - P4-S2-C18
      - P5-S1-C1
      - P5-S1-C2
      - P5-S1-C3
      - P5-S1-C4
      - P5-S1-C5
      - P5-S1-C6
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: limitations
      source_ids:
      - P9-S2-C6
      - P9-S2-C7
      - P9-S2-C8
      - P9-S2-C9
      - P9-S2-C10
      - P9-S2-C11
      - P9-S2-C12
      - P9-S2-C13
      - P9-S2-C14
      - P9-S2-C15
      - P9-S3-C4
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
      pdf_sha256: db3cb557db05560d6d0e1d137a713d95cfd0d640ed0694702e891099389d6835
      review_sha256: 710d9803984ea7be9383dae640b5de86ff04d5d3244744e16c633d69a13740eb
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
      - P6-S1-C6
      - P7-S1-C6
      source_result: The study reports a significant correlation between the percentage
        of damage to the affected occipital lobe and residual visual performance across
        three psychophysical tasks (drifting contrast, moving dots, and face/place
        detection). The correlations reached significance at p < 0.0167 (Bonferroni
        corrected for three tasks). The analysis used Spearman rank correlations between
        the proportion of occipital cortex overlapping with the consensus lesion mask
        and the percentage correct on the behavioral tasks.
      result_status: detected
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis corresponds to the correlation of overall
            occipital damage percentage with psychophysical performance, as described
            in P6-S1-C4 and P6-S1-C6. This is distinct from the VLSM analysis or individual
            visual area correlations (V1, V4, hMT+/V5) described elsewhere in the
            source.
          source_ids:
          - P6-S1-C4
          - P6-S1-C6
          - P7-S1-C6
        direction:
          answer: fits
          reason: The source states that the correlations 'reach significance' (P6-S1-C6)
            and 'performance on all was significantly correlated with the amount of
            damage' (P7-S1-C6). The proposed draft correctly identifies this as a
            detected association. The direction is implied to be negative (more damage,
            less performance) based on the context of 'impaired performance' in P5-S1-C1
            and the general logic of lesion-symptom mapping, though the specific sign
            is not explicitly stated in the cited snippets, the 'association' is confirmed.
          source_ids:
          - P6-S1-C6
          - P7-S1-C6
        construct:
          answer: fits
          reason: The exposure is correctly identified as the percentage of occipital
            damage (P6-S1-C4, P4-S1-C4). The outcome is residual vision measured by
            the three psychophysical tasks (P6-S1-C4, P2-S4-C10). The patient measurement
            is template_lesion_overlap, as the damage percentage is calculated by
            overlapping the consensus lesion mask with the MNI structural atlas occipital
            cortex mask (P4-S1-C4). This is not patient_diffusion, as diffusion was
            not used to construct the occipital mask for this specific correlation.
          source_ids:
          - P6-S1-C4
          - P4-S1-C4
          - P2-S4-C10
        qualifications:
          answer: fits
          reason: The draft includes the Bonferroni correction (p < 0.0167) and the
            floor effect handling (assigning 50% to values <50%), which are material
            qualifiers found in P6-S1-C6, P7-S1-C6, and P6-S1-C3. The definition of
            residual vision is also correctly cited.
          source_ids:
          - P6-S1-C6
          - P7-S1-C6
          - P6-S1-C3
          - P2-S1-C6
        missing_material_caveat:
          answer: fits
          reason: The draft includes limitations regarding manual lesion definition
            and single visual location testing. It does not omit any material caveat
            that would change the interpretation of the correlation result. The distinction
            between this correlation and the VLSM or specific area correlations is
            maintained by the analysis identity check.
          source_ids:
          - P8-S1-C6
          - P9-S2-C10
          - P9-S3-C4
      optional_pending:
      - Sample size for this specific correlation (n=39 for contrast, subsets for
        others) is not explicitly transcribed in the draft fields but is available
        in source P3-S1-C4, P3-S1-C13, P3-S2-C3.
      - Specific correlation coefficients (r values) are not transcribed.
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Sample size requires source confirmation; it has not been transcribed.
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Sample size for this specific correlation (n=39 for contrast, subsets for others)
      is not explicitly transcribed in the draft fields but is available in source
      P3-S1-C4, P3-S1-C13, P3-S2-C3.
    - Specific correlation coefficients (r values) are not transcribed.
    normalizations:
    - field: sample.n
      original: 39
      action: not_transcribed
      reason: Not supported by selected quotations
    analysis_identity:
      id: R001
      exposure:
        text: percentage of occipital damage
      outcome:
        text: residual vision (contrast, motion, and face/place tasks)
      analysis_label: Correlation of occipital damage and psychophysical performance
      relation: association
      evidence_ids:
      - P6-S1-C6
      - P7-S1-C6
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
        pdf_sha256: db3cb557db05560d6d0e1d137a713d95cfd0d640ed0694702e891099389d6835
        source_review: _compare/relationships-2026-11-16/review-current/Willis2025
        source_status_sha256: 5cba363249a89f2cc1ae5437982589d5b7cf93ce8998ecb9f71d5cddf54fd709
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P2-S4-C6:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: db3cb557db05560d6d0e1d137a713d95cfd0d640ed0694702e891099389d6835
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 200882f315d07c46e89d153b9138316ebf6f560a3781d820bbf66c9b8efa650a
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S4-C6
          page: 2
          text_layer_sha256: 200882f315d07c46e89d153b9138316ebf6f560a3781d820bbf66c9b8efa650a
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Average time after pathology onset was 40 months

          (range, 6–297 months).'
        anchor_text: 'Average time after pathology onset was 40 months

          (range, 6–297 months).'
        excluded_fragments: []
        image_sha256: 1a1c0afe9979e5f640bfd0f06325b1253662da81c915f5604d9557f8956eee47
        transcription: '. Average time after pathology onset was 40 months

          (range, 6–297 months)'
      P2-S3-C5:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: db3cb557db05560d6d0e1d137a713d95cfd0d640ed0694702e891099389d6835
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 910cee6592680a24da99edb9706c091f9f8e69e4d39a3ee198b89210fc1f14fa
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S3-C5
          page: 2
          text_layer_sha256: 910cee6592680a24da99edb9706c091f9f8e69e4d39a3ee198b89210fc1f14fa
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'In each case, participants

          were aged 18–80 and had suﬀered damage to the brain resulting in hom-

          onymous visual ﬁeld deﬁcits (including, hemianopia, quadrantanopia,

          and scotoma).'
        anchor_text: 'In each case, participants

          were aged 18–80 and had suﬀered damage to the brain resulting in hom-

          onymous visual ﬁeld deﬁcits (including, hemianopia, quadrantanopia,

          and scotoma).'
        excluded_fragments: []
        image_sha256: efa4c0202dcf7110a3fb79ccd3fe0c0f70de93da99b2eda22fe4c84b551c1ccb
        transcription: 'In each case, participants

          were aged 18–80 and had suffered damage to the brain resulting in hom-

          onymous visual field deficits (including, hemianopia, quadrantanopia,

          and scotoma)'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 6
  quote: 'To determine the eﬀect of overall damage to the occipital cor-

    tex on visual performance, the initial analysis was a basic corre-

    lation of the percentage of occipital damage and psychophysical

    performance on the three tasks.'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-26'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
