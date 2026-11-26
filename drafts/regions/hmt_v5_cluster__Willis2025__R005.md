---
id: hmt_v5_cluster
name: hMT+/V5 cluster
kind: network
findings:
- id: f1
  target: residual_vision
  target_kind: impairment
  claim: Participants with any damage to hMT+/V5 performed at chance on motion and face/place detection tasks.
  direction: unlikely
  relationship: correlational
  method: LSM
  sample:
    n: not_reported
    population: The subgroup of eight patients with any hMT+/V5 damage within the 39-person V1-damage cohort; chance-level motion and face/place results refer to the available tests in this subgroup.
    phase: not_reported
    time_post_onset: Average 40 months (range 6-297 months) after pathology onset
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - hMT+/V5 atlas-defined region exhibits high interindividual variability
  - Manual delineation using T1 scans may underestimate lesion involvement
  - hMT+/V5 likely encompasses both MT and MST subregions
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Patient lesion overlap with a probabilistic hMT+/V5 reference template from the Jülich atlas, thresholded at 10%. The finding specifically concerns the motion and face/place detection tasks; Some participants without damage to hMT+/V5 also performed at chance. Additional metadata has not been transcribed; review the pending-field flags before approval. PDF image reading (P2-S4-C6, two-model agreement, human verification pending): . Average time after pathology onset was 40 months

    (range, 6–297 months) Original text-layer quotation is preserved below. PDF image reading (P2-S3-C3, two-model agreement, human verification pending): Materials and Methods

    Participants

    Thirty-nine participants with damage to V1 resulting in homonymous

    visual field deficits were included in this analysis Original text-layer quotation is preserved below. Publication correction (human verification pending): Restricted the finding to the eight participants with any hMT+/V5 damage, preserving task availability and avoiding inference about all 39 patients. Exact per-task subgroup denominators are not established; eight is the anatomical subgroup size.'
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
    - proposed_concept:residual_vision
    - publication_correction_pending_human_verification
  citation: '@Willis2025'
  source_passages:
  - section: Original source P6-S2-C3
    page: 6
    quote: 'Indeed,

      participants with “any” damage to hMT+/V5 (n = 8; average

      damage, 39%; range, 2–100%) performed at chance on motion

      and face/place detection tasks.'
    supports: claim
  - section: Original source P8-S1-C2
    page: 8
    quote: 'While the

      number of patients in the current study with damage to

      hMT+/V5 was relatively small (8/39), none showed residual

      vision for either the motion stimulus or for face/place stimuli.'
    supports: claim
  - section: Original source P3-S3-C14
    page: 3
    quote: 'Visual areas V1 and V4 and hMT+/V5 were

      extracted from the Jülich atlas, which provides histologically deﬁned

      regions, and the occipital cortex mask was extracted from the MNI struc-

      tural atlas, both implemented in FSL (fmrib.ox.ac.uk/fsl).'
    supports: method
  - section: Original source P4-S1-C7
    page: 4
    quote: 'Based on prior

      experience,

      neuroanatomy

      and

      compatibility

      with

      other

      atlases

      (Glasser et al., 2016) thresholds of 10% (hMT+/V5), 30% (V4), and

      50% (V1) were used.'
    supports: method
  - section: Original source P2-S4-C6
    page: 2
    quote: 'Average time after pathology onset was 40 months

      (range, 6–297 months).'
    supports: sample
  - section: Original source P2-S3-C3
    page: 2
    quote: 'Materials and Methods

      Participants

      Thirty-nine participants with damage to V1 resulting in homonymous

      visual ﬁeld deﬁcits were included in this analysis.'
    supports: sample
  - section: Original source P8-S1-C4
    page: 8
    quote: 'As this atlas-

      deﬁned region exhibits relatively high interindividual variability,

      there is a chance that smaller lesions could fall outside its true

      location.'
    supports: limitation
  - section: Original source P8-S1-C6
    page: 8
    quote: 'One possible explanation for the profound impact

      of lesions in many cases is that they were deﬁned manually using

      T1 scans, which may underestimate lesion involvement, e.g.,

      compared with quantitative MRI (Seiler et al., 2021).'
    supports: limitation
  - section: Original source P8-S1-C5
    page: 8
    quote: 'Also, hMT+/V5 here likely encompasses MT and

      MST, implying that either subregion would be critical to detect

      moving dots.'
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-26'
relationship_review:
  paper: Willis2025
  proposal_id: R005
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
    id: R005
    exposure:
      text: damage to hMT+/V5
    outcome:
      text: residual vision (motion and face/place detection tasks)
    analysis_label: Impact of hMT+/V5 damage on residual vision
    relation: association
    evidence_ids:
    - P6-S2-C3
    - P8-S1-C2
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
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: validation
        source_id: P4-S1-C10
        reason: No validation-design cue; inspect the source rather than inferring a design
      - slot: validation
        source_id: P6-S2-C13
        reason: No validation-design cue; inspect the source rather than inferring a design
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
        note: Automatic crops and matching transcriptions do not certify visual completeness. Figures are not automatically interpreted.
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
      approval: Not performed. Structural checks and model selections do not establish semantic correctness.
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
      reason: States V1 damage showed no relationship with residual vision and V4/hMT+ correlated with contrast detection.
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
      reason: Specifies threshold of 20% occipital damage for loss of residual vision in motion/face tasks.
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
      reason: States any damage to hMT+/V5 led to chance performance on motion and face/place tasks.
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
      reason: Identifies cluster of voxels associated with reduced residual function in contrast task.
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
      reason: Confirms significant correlation between occipital damage and all three tasks.
    - source_id: P8-S1-C2
      disposition: represented
      result_indexes:
      - 4
      reason: States none of the patients with hMT+/V5 damage showed residual vision for motion or face/place.
    - source_id: P8-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discusses specific participants with small hMT+/V5 damage.
    - source_id: P8-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports no difference in performance between left and right hemisphere hMT+/V5 damage.
    - source_id: P8-S2-C3
      disposition: represented
      result_indexes:
      - 5
      reason: Links optic radiation and lateral visual pathway damage to poor residual vision.
    - source_id: P8-S2-C5
      disposition: represented
      result_indexes:
      - 2
      reason: States V4 damage did not significantly correlate with face/place detection.
    - source_id: P8-S2-C8
      disposition: represented
      result_indexes:
      - 2
      reason: States significant correlation between contrast stimulus detection and V4 damage.
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
      reason: Concludes preservation of lateral optic radiation is most highly associated with residual vision.
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
    pending_policy: Every result passage without direct candidate evidence remains pending, including model-labelled background and restatements; those labels never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-3-1
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions are model suggestions. No original outputs changed.
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
      reason: Requires a Methods outcome definition; model selection retained for inspection only
    - slot: validation
      source_id: P4-S1-C10
      reason: No validation-design cue; inspect the source rather than inferring a design
    - slot: validation
      source_id: P6-S2-C13
      reason: No validation-design cue; inspect the source rather than inferring a design
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
    policy: All slots and enums remain unverified. Held selections are not evidence of absence. Original response is preserved in frame/raw.json.
  approved: false
  source_check:
    profile: agent-repair
    scope: Agent corrected this draft against the original paper. The original automated attempt is retained as historical provenance and does not verify this revised version. Human PDF review and approval remain required. Restricted the finding to the eight participants with any hMT+/V5 damage, preserving task availability and avoiding inference about all 39 patients. Exact per-task subgroup denominators are not established; eight is the anatomical subgroup size.
    binding:
      source_pdf_sha256: db3cb557db05560d6d0e1d137a713d95cfd0d640ed0694702e891099389d6835
      original_source_sha256: 20a6aff6ad4c24be5c4ddb8eb6c444125103e431d03975536e9d3e052d84eb1e
      repair_audit: logs/publication/draft-repairs-2026-11-26.json
      agent_repair_approved: false
    approved: false
    pending_details:
    - Detailed statistics, atlas/reference-space and structured confounder metadata not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    normalizations: []
    analysis_identity:
      id: R005
      exposure:
        text: damage to hMT+/V5
      outcome:
        text: residual vision (motion and face/place detection tasks)
      analysis_label: Impact of hMT+/V5 damage on residual vision
      relation: association
      evidence_ids:
      - P6-S2-C3
      - P8-S1-C2
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
          models: &id001
          - gemma4:31b
          - qwen3.8:27b
          model_digests: &id002
          - 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
          - 47951e4a666180bc2aedfc93c169472f2de783696fe196efbf063f5730ecf163
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
      P2-S3-C3:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: db3cb557db05560d6d0e1d137a713d95cfd0d640ed0694702e891099389d6835
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 86af853cac9c9aa179a27d8fe4b0961597ec128444840bf0b44c3740db937e01
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S3-C3
          page: 2
          text_layer_sha256: 86af853cac9c9aa179a27d8fe4b0961597ec128444840bf0b44c3740db937e01
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Materials and Methods

          Participants

          Thirty-nine participants with damage to V1 resulting in homonymous

          visual ﬁeld deﬁcits were included in this analysis.'
        anchor_text: 'Materials and Methods

          Participants

          Thirty-nine participants with damage to V1 resulting in homonymous

          visual ﬁeld deﬁcits were included in this analysis.'
        excluded_fragments: []
        image_sha256: ede3a2756e8f25beb00601170016bd903b8d756d50d41428a72c660b562f15e5
        transcription: 'Materials and Methods

          Participants

          Thirty-nine participants with damage to V1 resulting in homonymous

          visual field deficits were included in this analysis'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
    publication_correction:
      date: '2026-11-26T00:24:06.569756+00:00'
      by: agent:source-repair
      approved: false
      human_verification_required: true
      original_source_sha256: 20a6aff6ad4c24be5c4ddb8eb6c444125103e431d03975536e9d3e052d84eb1e
      source_pdf_sha256: db3cb557db05560d6d0e1d137a713d95cfd0d640ed0694702e891099389d6835
      pdf_pages:
      - 6
      - 7
      note: Restricted the finding to the eight participants with any hMT+/V5 damage, preserving task availability and avoiding inference about all 39 patients. Exact per-task subgroup denominators are not established; eight is the anatomical subgroup size.
      audit: logs/publication/draft-repairs-2026-11-26.json
    checked_by: agent:source-repair (human approval pending)
    date: '2026-11-26'
    corrections:
    - Restricted the finding to the eight participants with any hMT+/V5 damage, preserving task availability and avoiding inference about all 39 patients. Exact per-task subgroup denominators are not established; eight is the anatomical subgroup size.
    original_scope: Independent model text review of core meaning; not human approval or complete PDF verification
    original_core_review:
      own_result_source_ids:
      - P6-S2-C3
      - P8-S1-C2
      source_result: Participants with any damage to hMT+/V5 (n=8) performed at chance on motion and face/place detection tasks, indicating a significant impact on residual vision, though some participants without damage also performed at chance.
      result_status: detected
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis correctly identifies the specific finding regarding hMT+/V5 damage and its association with performance on motion and face/place tasks, distinct from the VLSM analysis or V4 findings.
          source_ids:
          - P6-S2-C3
          - P8-S1-C2
        direction:
          answer: fits
          reason: The claim that participants with damage performed at chance aligns with the source stating 'performed at chance on motion and face/place detection tasks' and 'none showed residual vision'.
          source_ids:
          - P6-S2-C3
          - P8-S1-C2
        construct:
          answer: fits
          reason: The exposure is correctly identified as damage to hMT+/V5 (measured via template overlap) and the outcome as residual vision in specific tasks. The method is correctly identified as correlational/LSM based on the source description of correlations and lesion mapping.
          source_ids:
          - P6-S2-C3
          - P8-S1-C2
          - P3-S3-C14
          - P4-S1-C7
        qualifications:
          answer: fits
          reason: The draft includes the necessary qualification that the finding is specific to motion and face/place tasks and acknowledges that some participants without damage also performed at chance, which is a material caveat from the source.
          source_ids:
          - P6-S2-C3
          - P8-S1-C2
          - P8-S1-C12
        missing_material_caveat:
          answer: fits
          reason: The draft includes limitations regarding interindividual variability and manual delineation. No material caveats that change the interpretation of the core relationship are missing.
          source_ids:
          - P8-S1-C4
          - P8-S1-C6
      optional_pending: []
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
        models: *id001
        digests: *id002
        code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
        layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
reviewer_marks:
- id: relationship-source-check
  page: 6
  quote: 'Indeed,

    participants with “any” damage to hMT+/V5 (n = 8; average

    damage, 39%; range, 2–100%) performed at chance on motion

    and face/place detection tasks.'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-26'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor roles, all qualifiers, source audit issues and main-PDF tables/figures; check missing results. This model proposal is not verified.'
- id: publication-source-repair-2026-11-26
  status: pending
  by: agent:source-repair
  date: '2026-11-26'
  note: Restricted the finding to the eight participants with any hMT+/V5 damage, preserving task availability and avoiding inference about all 39 patients. Exact per-task subgroup denominators are not established; eight is the anatomical subgroup size. Original automated review applies to the original version; verify the corrected finding against the cited pages before approval.
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
