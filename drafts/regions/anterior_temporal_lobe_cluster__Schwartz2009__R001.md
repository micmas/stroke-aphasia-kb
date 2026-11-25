---
id: anterior_temporal_lobe_cluster
name: anterior temporal lobe cluster
kind: network
findings:
- id: f1
  target: semantic_error_rate
  target_kind: impairment
  claim: Lesion status in the anterior temporal lobe (specifically Brodmann areas
    21 and 38) was significantly associated with an increased rate of semantic naming
    errors.
  direction: likely
  relationship: correlational
  method: VLSM
  sample:
    n: 64
    population: individuals with post-stroke aphasia secondary to left hemisphere
      stroke
    phase: not_reported
    time_post_onset: Not transcribed; confirm from the original PDF population and
      timing passages.
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Vascular anatomy of the middle cerebral artery territory limited the exploration
    of mesial temporal lobe and occipital regions
  - The identified region likely underestimates the full extent of temporal lobe involvement
    due to weak coverage in certain areas
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Patient lesion status (presence or absence of lesion)
    at each voxel, analyzed via voxel-based lesion-symptom mapping. The highest concentration
    of significant voxels was found in the anterior half of the middle temporal gyrus
    and the temporal pole; The association remained prominent after regressing out
    total lesion volume; The association remained prominent after filtering out non-verbal
    semantic comprehension (NVcomp) and verbal comprehension (Vcomp) scores. Additional
    metadata has not been transcribed; review the pending-field flags before approval.
    PDF image reading (P4-S2-C10, two-model agreement, human verification pending):
    . The 64 who were included in the study (42%

    females; 48% African American) had a mean age of 58 (range 26–78),

    mean years of education of 14 (10–21) and mean months post-onset

    of 68 (1–381) Original text-layer quotation is preserved below.'
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
    - not_transcribed:sample.time_post_onset
    - proposed_concept:semantic_error_rate
  citation: '@Schwartz2009'
  source_passages:
  - section: Original source P7-S1-C12
    page: 7
    quote: 'Anatomic ﬁndings

      In the analysis performed to explore the anatomic basis of the

      variable SemErr, we found 35 466 voxels for which a signiﬁcant

      correlation between lesion status and impaired performance on

      the SemErr measure was identiﬁed.'
    supports: claim
  - section: Original source P7-S1-C14
    page: 7
    quote: 'The highest concentration of signiﬁcant voxels (19 411

      voxels) was in the anterior half of the middle temporal gyrus and

      the temporal pole, in Brodmann area regions 21 and 38, respec-

      tively.'
    supports: claim
  - section: Original source P4-S2-C10
    page: 4
    quote: 'The 64 who were included in the study (42%

      females; 48% African American) had a mean age of 58 (range 26–78),

      mean years of education of 14 (10–21) and mean months post-onset

      of 68 (1–381).'
    supports: sample
  - section: Original source P4-S3-C2
    page: 4
    quote: 'Language tests

      The 175-item Philadelphia Naming Test (Roach et al., 1996) was used

      to measure semantic error production in picture naming.'
    supports: method
  - section: Original source P5-S2-C8
    page: 5
    quote: 'A simple

      t-test comparing the scores between patients with and without lesions

      was performed at each voxel using the VoxBo brain imaging package

      (www.voxbo.org).'
    supports: method
  - section: Original source P8-S1-C4
    page: 8
    quote: 'Of the 6366 voxels exceeding threshold, the majority (4361) were

      in the anterior temporal lobe region described above.'
    supports: claim
  - section: Original source P12-S3-C6
    page: 12
    quote: 'It must be emphasized that the region within the left anterior

      temporal lobe that our analysis picked out almost certainly under-

      estimates the extent of the temporal lobe involvement.'
    supports: limitation
  - section: Original source P7-S1-C3
    page: 7
    quote: 'As aphasia is typically associated with strokes in the middle

      cerebral artery territory, we are unable to explore the contribution

      of brain regions typically supplied by the posterior or anterior

      cerebral arteries.'
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-25'
relationship_review:
  paper: Schwartz2009
  proposal_id: R001
  review_status_sha256: d5f30f53979a12ab859c2c061e8de47469ddd04ae873f510a9e507c8842b29ec
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 9cf2d54579089e10ec7294d1ba700958129654cf1f30bc1b95cffe15a4b12829
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 9cf2d54579089e10ec7294d1ba700958129654cf1f30bc1b95cffe15a4b12829
        A/passages.json: 9510c003d94f3d2a1ec8aa0dcd08e513c98b36b682daa3a5ab5d1ef0367f724e
        A/raw.json: a958f61947e5ecf7694171787f8e8d3c38fce1f54cf54a142d181d75e580815f
        A/source-units.json: aa3b7d5f2d07f212fc3de1fc15767b323498e2f5ac427cdf8422f39b7de4ab45
        A/full-source-units.json: 0221e1ae173b2b25e4a4b5b45e3a7bd4fc7addda069b246fe29f3c22c15c49a3
        A/meta.json: 4a1d3fe73fcfce0fe58892197dd8acc37c4a864bedba9ab8cc641ab85d253082
        A/table-images/TABLE-1-page-6-1.png: d690cf7a569d6926583f777797410a2971e6095f4c4007ad0f8d7fa783a3eafd
        A/table-images/page-6.png: fc4809e0218b1fd7dea0e780c8337099075260707d03d63bf537f3f953c0558a
        A/table-images/manifest.json: 3d5318042ad61035ff689f452982357f204474b22a3b8ebbec652a497d2b2ee3
        A/clauses/window-11/raw.json: ebff3aad6a3170b46fa72efb65bbdf468cf415ff9601231b8744333114dd1a50
        A/clauses/window-11/prompt.txt: 0943f5ff91f538b6573ae2566be515d77fd4a50a8d45b6e4d31fc372f7a2231a
        A/clauses/window-11/meta.json: 966bf85cd6f03aadd3f76d9a79a0f53957754aefc9a3182922d204430e7a117d
        A/clauses/window-10/raw.json: c31001e4b7c403fcfa4dc20ca550bee10b158c4b885ebcbe71f0943460dfa5bf
        A/clauses/window-10/prompt.txt: eb2481efd87a1d452e5a54fc7f6999f7801d60da321d745411c044821d0fdc84
        A/clauses/window-10/meta.json: 6c221c32410eb5e3e6cf71b5465f0da399f586304a7cd35c68b0ae0782704e03
        A/clauses/window-03/raw.json: 0450539d603e38c739123ac10a7ca414e41f26a47b14440c650753e6673e5c2e
        A/clauses/window-03/prompt.txt: 37c82e1087a2eefcced4991e59481b9de9921ad3d4e9efa75d52f862240d5003
        A/clauses/window-03/meta.json: def78a544e6a19325442d4af6ffe65f4f8e12176877294567f117f123bd91491
        A/clauses/window-04/raw.json: f125952c8e8749a741d5da970cf2d5f4fb4a193cf1af8e1b953b25fdbd2474da
        A/clauses/window-04/prompt.txt: 29f3bf861c626ed4c559a7c62e6a0b7bca46dc844258ba4cb89cf8c74602e223
        A/clauses/window-04/meta.json: 77e8a38a9248eff91551c5d0d7b590e2dd4dbd282eac2b98fca20a7ac3889e43
        A/clauses/window-05/raw.json: e3cbd08f82ee01967a4fe6be10b55f8916ebbc513628eecdca93d60cedf6a7ad
        A/clauses/window-05/prompt.txt: fdeeae3755d26c30a79cdc6ce4cb2de5e4470cbfccd7df801c061b018799a26b
        A/clauses/window-05/meta.json: 54c065fa23092bf4c7f9b9ba1582940e75b708c02e604c754a8f5de298ce1cee
        A/clauses/window-02/raw.json: b80265b1e16c9099182fa0192ac502b869aaf55c7bf116f5ee1f8327d12a9c13
        A/clauses/window-02/prompt.txt: d94de06a3e798e0ddd3b4bb6cd5d5a0f6e09ff6d01df9dbcaed95c8bb7ae877d
        A/clauses/window-02/meta.json: 863251d115a15e35575cd6f4f5c25d51630747947dd14baf416e4554a20864e5
        A/clauses/window-09/raw.json: 59a201fbc6e4c34e1e6d4f6af6845f6337e5991ea4bcc4b978faaf62f87d6fb9
        A/clauses/window-09/prompt.txt: 7a5f508cabb24a84c1f6a6ef4715e8b776766a3e55202075a4b04c8f271ea6d1
        A/clauses/window-09/meta.json: b21b5a7f520eae8924b617eea1a6fbe9e0bdd1a8c695e3f0edff63ed915913d6
        A/clauses/window-07/raw.json: 858382a3b84a0152886f2369cb9e7b58b8a2e50cca7038adfd4712b54789125a
        A/clauses/window-07/prompt.txt: 1d3b0c6fc0c77716aece971dea97909cd315993b9961377c8074101cfa9ad007
        A/clauses/window-07/meta.json: 1a5b2a0da00e5eab7e00a1c601bba887827bb22df9a56fc70f0e69bbafbfc37a
        A/clauses/window-01/raw.json: 8b6c04365f8d55ec23eb1827e4eaecc0666a8932bc0244f4afe2b13063d6586d
        A/clauses/window-01/prompt.txt: 3806dcabf07537e86d4571f0e6570bf14712e736e8c7ab888da43ddff8c54a6d
        A/clauses/window-01/meta.json: cc6b7cddc6a83827a0b6635752713b29b779754665fb78e9828c9ca447e0c0c5
        A/clauses/window-06/raw.json: 691de8db16e53961b863fa07381553b82977464f5f89a4d0d70ad5d276795850
        A/clauses/window-06/prompt.txt: 40919782e41993528305725c607147b796ce107a18847581b21bdd649f441e4f
        A/clauses/window-06/meta.json: f048a0da3bc7ae63fb7121d5f532fb9491d090bbae87c9902467c1c0fb5a6a50
        A/clauses/window-08/raw.json: ececa517cc9fa19fe943700e4ad452b0cb9b82d6ac4f11c1384b48b0e6eb6ad8
        A/clauses/window-08/prompt.txt: e74bcad7e2aea593748ae905503cabf2cc21603bb449442ce86793360f0c7db6
        A/clauses/window-08/meta.json: 2708ebc75a5deb1411b6097d9153fc6193991bbbe5c46a9e74a482bbd03f18ee
        A/tables/TABLE-1-page-6-1/raw.json: 1c8602d7dce8c4011e3c6236e645df83c801d559601d2cd6db0de01f7aa8e797
        A/tables/TABLE-1-page-6-1/prompt.txt: 8475611e916953d3c73c816bfdc8949e7522bf39af8b18f62823e6c2a18bfc3e
        A/tables/TABLE-1-page-6-1/meta.json: 96feb0a3d49fedd69ebecebe63cef14b60d5b5268bfa24f7e8cf89e21496b9ec
        B/passages.json: 9510c003d94f3d2a1ec8aa0dcd08e513c98b36b682daa3a5ab5d1ef0367f724e
        B/raw.json: 3d23b7b27f56470e76d837a21c41f4380bfdc273f994d8d758b51574c873c054
        B/source-units.json: aa3b7d5f2d07f212fc3de1fc15767b323498e2f5ac427cdf8422f39b7de4ab45
        B/full-source-units.json: 0221e1ae173b2b25e4a4b5b45e3a7bd4fc7addda069b246fe29f3c22c15c49a3
        B/meta.json: cf5a9f26938f1db725b056182110f5b6bcabe53c313fb2b0fb6384e9d6ff9afe
        B/table-images/TABLE-1-page-6-1.png: d690cf7a569d6926583f777797410a2971e6095f4c4007ad0f8d7fa783a3eafd
        B/table-images/page-6.png: fc4809e0218b1fd7dea0e780c8337099075260707d03d63bf537f3f953c0558a
        B/table-images/manifest.json: 006736910e705655d14e38428091475dcb452878e18bdbfd9370f28bc8f9ee26
        B/clauses/window-11/raw.json: 2a135afd1f0c8e5b17b93a6d487fa766346905a4cf75d6237fdc187e4a79f305
        B/clauses/window-11/prompt.txt: 0943f5ff91f538b6573ae2566be515d77fd4a50a8d45b6e4d31fc372f7a2231a
        B/clauses/window-11/meta.json: a7b704f3c9970df89ca50664aa675d0f3441dacd3c89ceee600900de4280c8f9
        B/clauses/window-10/raw.json: b73e78aa1563242ab9acc8fba69545d54a6d24bda042f10a34259a9abbd2e3d0
        B/clauses/window-10/prompt.txt: eb2481efd87a1d452e5a54fc7f6999f7801d60da321d745411c044821d0fdc84
        B/clauses/window-10/meta.json: 5149ca7a9f7819e6603f56526742693b1413657f3e8d3df1f7c16d4bfc057c1c
        B/clauses/window-03/raw.json: 0424ca806c4e642641fb3d2e886322c066772362c05dcde30a4581471858e9b7
        B/clauses/window-03/prompt.txt: 37c82e1087a2eefcced4991e59481b9de9921ad3d4e9efa75d52f862240d5003
        B/clauses/window-03/meta.json: 0d0b71b3fd25e564a4c95ee65f79a7a5f15b576a76243c9985b36be9acded343
        B/clauses/window-04/raw.json: c9791a1fdbd60b175fc20015dcfb3a6a5a59f1ae33493faa5a7f3b33e91902ad
        B/clauses/window-04/prompt.txt: 29f3bf861c626ed4c559a7c62e6a0b7bca46dc844258ba4cb89cf8c74602e223
        B/clauses/window-04/meta.json: 92bbf9214c81b926357953513540bc8f547b9b360232b66035b31fef6c27593f
        B/clauses/window-05/raw.json: ab39f11fdb5837e81d1deab6c7de01c9fa5ac8ab0ededa5bb5dafe5408e6ddbf
        B/clauses/window-05/prompt.txt: fdeeae3755d26c30a79cdc6ce4cb2de5e4470cbfccd7df801c061b018799a26b
        B/clauses/window-05/meta.json: a84a433e76bb07715731cf3d647a1864360f2f3e7d32c8f0aee7de59981fc178
        B/clauses/window-02/raw.json: 232a91c5fdbe771221a8686061c96e8afc86d38a0ee8309cdccc8a51f36b6050
        B/clauses/window-02/prompt.txt: d94de06a3e798e0ddd3b4bb6cd5d5a0f6e09ff6d01df9dbcaed95c8bb7ae877d
        B/clauses/window-02/meta.json: eb783b557023802cd55c4ce0f0885e421a9c6a90aa4512579787d8d30645cfbf
        B/clauses/window-09/raw.json: 6e47aa071701033d1a594ee57b4b28ff3f5e91e545ba3b30ec8ec7868c171ecb
        B/clauses/window-09/prompt.txt: 7a5f508cabb24a84c1f6a6ef4715e8b776766a3e55202075a4b04c8f271ea6d1
        B/clauses/window-09/meta.json: a7f45b7ad758c7cc49dd04eea1ab3d2fdba8fc06a0ad41d0c7793887bcf83ff0
        B/clauses/window-07/raw.json: 4122d79124021d0c1931387d0a220af064544235f9bf0663bbaca62fdffe9678
        B/clauses/window-07/prompt.txt: 1d3b0c6fc0c77716aece971dea97909cd315993b9961377c8074101cfa9ad007
        B/clauses/window-07/meta.json: df6fb9825256766aae55860c04ab556989af3ba3b9d79cbb88e3b91e6f7d819c
        B/clauses/window-01/raw.json: 7d8e5223790badb42f88234e2686ab5a9c4ae5c2732f1c1f450496ea85596066
        B/clauses/window-01/prompt.txt: 3806dcabf07537e86d4571f0e6570bf14712e736e8c7ab888da43ddff8c54a6d
        B/clauses/window-01/meta.json: d8fed178563ed85cabf94d7cacd48eb9d5d135679a545d1fa31cf0f9e7cc3ea2
        B/clauses/window-06/raw.json: 23dc2ed65a7991375f68886f1ad367dc825a562bedf4413ba43719dbfa060717
        B/clauses/window-06/prompt.txt: 40919782e41993528305725c607147b796ce107a18847581b21bdd649f441e4f
        B/clauses/window-06/meta.json: a929084af1ff4a9f5cdce99d58a9671116608529cbc92e104b6e3bc6ab0fdd42
        B/clauses/window-08/raw.json: 56d0e1032ec37f64b88254b3486902b5515eed204da28aa852aa4fa4e462db47
        B/clauses/window-08/prompt.txt: e74bcad7e2aea593748ae905503cabf2cc21603bb449442ce86793360f0c7db6
        B/clauses/window-08/meta.json: 3ada2141f5a3705074df16a6a4412e6172e47ceebcefea67db37a7e1f13ff592
        B/tables/TABLE-1-page-6-1/raw.json: 223a7fcf63b91b6de427105127d3ac7e29be99ec8f96bbe156ab4388314394ca
        B/tables/TABLE-1-page-6-1/prompt.txt: 8475611e916953d3c73c816bfdc8949e7522bf39af8b18f62823e6c2a18bfc3e
        B/tables/TABLE-1-page-6-1/meta.json: 8a521c55137fd612d054ab48b6b0043d94bd70b179ab20c596103ab688ffd074
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
      pdf_sha256: 9cf2d54579089e10ec7294d1ba700958129654cf1f30bc1b95cffe15a4b12829
      source_review: _compare/relationships-2026-11-16/review-current/Schwartz2009
      source_status_sha256: 4763f18f11ea91e8571a263278e854c7fb35384af21dd6bbbdf6fb6ab17ae969
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R001
    exposure:
      text: lesion status
    outcome:
      text: semantic error rate (SemErr)
    analysis_label: Voxel-based lesion-symptom mapping (unfiltered)
    relation: association
    evidence_ids:
    - P7-S1-C12
    - P7-S1-C13
    - P7-S1-C14
    - P7-S1-C15
    - P7-S2-C2
    - P7-S2-C3
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
      pdf_sha256: 9cf2d54579089e10ec7294d1ba700958129654cf1f30bc1b95cffe15a4b12829
      source_review: _compare/relationships-2026-11-16/review-current/Schwartz2009
      source_status_sha256: 4763f18f11ea91e8571a263278e854c7fb35384af21dd6bbbdf6fb6ab17ae969
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P5-S3-C2
      - Result passage disposed without unit P5-S3-C3
      - Result passage disposed without unit P5-S3-C5
      - Result passage disposed without unit P5-S3-C6
      - Result passage disposed without unit P5-S3-C9
      - Result passage disposed without unit P6-S1-C2
      - Result passage disposed without unit P6-S1-C3
      - Result passage disposed without unit P6-S1-C9
      - Result passage disposed without unit P7-S1-C5
      - Result passage disposed without unit P7-S1-C6
      - Result passage disposed without unit P7-S1-C7
      - Result passage disposed without unit P7-S1-C10
      - Result passage disposed without unit P7-S1-C11
      - Result passage disposed without unit P7-S1-C8
      - Result passage disposed without unit P8-S1-C10
      - Unresolved source passage P8-S1-C15
      - Result passage disposed without unit P8-S1-C6
      - Result passage disposed without unit P8-S1-C8
      - Result passage disposed without unit P8-S1-C9
      - Result passage disposed without unit P9-S1-C10
      - Result passage disposed without unit P9-S1-C5
      - Result passage disposed without unit P10-S2-C4
      - Result passage disposed without unit P12-S2-C7
      - Result passage disposed without unit P12-S3-C11
      - Accounting without a linked unit P12-S4-C2
      - Accounting without a linked unit P12-S4-C3
      - Accounting without a linked unit P12-S4-C4
      - Unaccounted source passage P12-S4-C2
      - Unaccounted source passage P12-S4-C4
      - Unaccounted source passage P12-S4-C3
      - Result passage disposed without unit P13-S1-C6
      - Accounting without a linked unit P13-S2-C3
      - Accounting without a linked unit P13-S2-C5
      - Accounting without a linked unit P13-S3-C4
      - Accounting without a linked unit P13-S3-C7
      - Result passage disposed without unit P13-S4-C3
      - Result passage disposed without unit P13-S4-C4
      - Unaccounted source passage P13-S2-C5
      - Unaccounted source passage P13-S2-C3
      - Unaccounted source passage P13-S3-C7
      - Unaccounted source passage P13-S3-C4
      - Result passage disposed without unit P14-S1-C1
      - Result passage disposed without unit P14-S1-C3
      - Result passage disposed without unit P14-S2-C4
      unattached_null_or_qualifier_ids:
      - P12-S3-C11
      - P13-S1-C6
      - P13-S2-C5
      - P13-S4-C3
      suppressed_nonrepresented_units: 33
      default_disposition_count_requires_completeness_check: 232
      unselected_timing_passages:
      - P4-S2-C10
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P7-S1-C12
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C13
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P5-S2-C6
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      empty_frame_slots_require_confirmation:
      - validation
      - personal_factors
      - tested_personal_effects
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-6-1
      unlinked_tables: []
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P2-S3
        - P3-S2
        - P4-S3
        - P6-S1
        - P7-S1
        - P7-S2
        - P8-S1
        - P8-S2
        - P9-S1
        - P10-S2
        - P10-S3
        - P11-S1
        - P12-S1
        - P12-S2
        - P12-S3
        - P14-S1
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 9cf2d54579089e10ec7294d1ba700958129654cf1f30bc1b95cffe15a4b12829
      source_review: _compare/relationships-2026-11-16/review-current/Schwartz2009
      source_status_sha256: 4763f18f11ea91e8571a263278e854c7fb35384af21dd6bbbdf6fb6ab17ae969
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C13
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of results in abstract.
    - source_id: P1-S1-C14
      disposition: repeated
      result_indexes:
      - 3
      reason: Restatement of results in abstract.
    - source_id: P4-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes study goal and recruitment strategy.
    - source_id: P5-S2-C15
      disposition: background_or_descriptive
      result_indexes: []
      reason: Introduction to language test results section.
    - source_id: P5-S3-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient classification demographics.
    - source_id: P5-S3-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient classification demographics.
    - source_id: P5-S3-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive statistics of naming test performance.
    - source_id: P5-S3-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive statistics of naming test performance.
    - source_id: P5-S3-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison to other samples.
    - source_id: P5-S3-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive statistics of naming test performance.
    - source_id: P5-S3-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive statistics of naming test performance.
    - source_id: P5-S3-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive statistics of comprehension tests.
    - source_id: P5-S3-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Correlation between test scores, not lesion-symptom mapping.
    - source_id: P5-S3-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Correlation between test scores, not lesion-symptom mapping.
    - source_id: P6-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive statistics of lesion patterns.
    - source_id: P6-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive statistics of lesion patterns.
    - source_id: P6-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive statistics of lesion patterns.
    - source_id: P6-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of lesion overlap map.
    - source_id: P7-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of coverage.
    - source_id: P7-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of coverage.
    - source_id: P7-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of coverage.
    - source_id: P7-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of coverage.
    - source_id: P7-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Analysis of lesion size vs location.
    - source_id: P7-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Analysis of lesion size vs location.
    - source_id: P7-S1-C12
      disposition: represented
      result_indexes:
      - 0
      reason: Establishes significant voxels for SemErr.
    - source_id: P7-S1-C13
      disposition: represented
      result_indexes:
      - 0
      reason: Identifies anterior temporal lobe as highest t-values.
    - source_id: P7-S1-C14
      disposition: represented
      result_indexes:
      - 0
      reason: Identifies Brodmann area 21 and 38 as significant.
    - source_id: P7-S1-C15
      disposition: represented
      result_indexes:
      - 0
      reason: Identifies posterior middle temporal gyrus as significant.
    - source_id: P7-S2-C2
      disposition: represented
      result_indexes:
      - 0
      reason: Identifies Brodmann area 37 as significant.
    - source_id: P7-S2-C3
      disposition: represented
      result_indexes:
      - 0
      reason: Identifies Brodmann areas 45 and 46 as significant.
    - source_id: P7-S2-C4
      disposition: represented
      result_indexes:
      - 0
      reason: Identifies deep white matter as significant.
    - source_id: P7-S2-C5
      disposition: represented
      result_indexes:
      - 1
      reason: Null finding for Wernicke's area.
    - source_id: P7-S2-C6
      disposition: represented
      result_indexes:
      - 2
      reason: Effect of Vcomp filtering on overall pattern.
    - source_id: P7-S2-C7
      disposition: represented
      result_indexes:
      - 2
      reason: Reduction of significant voxels in prefrontal cortex after Vcomp filtering.
    - source_id: P8-S1-C1
      disposition: represented
      result_indexes:
      - 2
      reason: Concentration of voxels in anterior temporal lobe after Vcomp filtering.
    - source_id: P8-S1-C2
      disposition: represented
      result_indexes:
      - 3
      reason: Impact of NVcomp filtering on results.
    - source_id: P8-S1-C3
      disposition: represented
      result_indexes:
      - 3
      reason: Null findings for Brodmann area 45/46 and 37 after NVcomp filtering.
    - source_id: P8-S1-C4
      disposition: represented
      result_indexes:
      - 3
      reason: Majority of significant voxels in anterior temporal lobe after NVcomp
        filtering.
    - source_id: P8-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of raw scan inspection.
    - source_id: P8-S1-C8
      disposition: represented
      result_indexes:
      - 4
      reason: Overlap differences in anterior temporal lobe and prefrontal areas.
    - source_id: P8-S1-C9
      disposition: represented
      result_indexes:
      - 4
      reason: Robustness of overlap differences in these regions.
    - source_id: P8-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation of sensory-motor cortex voxels in overlap map.
    - source_id: P8-S1-C14
      disposition: represented
      result_indexes:
      - 5
      reason: Anterior temporal lobe prominence after regressing total lesion volume.
    - source_id: P10-S1-C2
      disposition: represented
      result_indexes:
      - 6
      reason: Significant partial correlations for Brodmann area 21 and 38.
    - source_id: P10-S1-C6
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of unfiltered analysis results in discussion.
    - source_id: P10-S1-C8
      disposition: repeated
      result_indexes:
      - 2
      - 3
      reason: Restatement of filtering results in discussion.
    - source_id: P10-S1-C9
      disposition: repeated
      result_indexes:
      - 3
      reason: Conclusion regarding anterior temporal lobe.
    - source_id: P10-S1-C10
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of results for Brodmann areas 37 and 45/46.
    - source_id: P10-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of prevalence of ATL lesions.
    - source_id: P10-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of lesion size vs location.
    - source_id: P10-S2-C7
      disposition: repeated
      result_indexes:
      - 6
      reason: Restatement of partial correlation results.
    - source_id: P10-S2-C10
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of peak t-value location.
    - source_id: P12-S1-C7
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of mid-middle temporal gyrus as essential.
    - source_id: P12-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison to Damasio's findings.
    - source_id: P12-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Theoretical interpretation of results.
    - source_id: P12-S3-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of underestimation of temporal lobe involvement.
    - source_id: P12-S3-C11
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of areas outside ATL that correlated with SemErr.
    - source_id: P12-S4-C1
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of areas outside ATL that correlated with SemErr.
    - source_id: P12-S4-C2
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of Brodmann area 37 and 45/46 results.
    - source_id: P12-S4-C3
      disposition: repeated
      result_indexes:
      - 0
      - 2
      reason: Restatement of unfiltered and Vcomp filtered results.
    - source_id: P12-S4-C4
      disposition: repeated
      result_indexes:
      - 3
      reason: Restatement of NVcomp filtering results.
    - source_id: P13-S1-C6
      disposition: represented
      result_indexes: []
      reason: Null finding for Vcomp filtering pattern (no voxels fit this pattern).
    - source_id: P13-S2-C3
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of prefrontal cortex association.
    - source_id: P13-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to Cloutman et al. (2009) results.
    - source_id: P13-S3-C4
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of prefrontal voxel cluster location.
    - source_id: P13-S3-C7
      disposition: repeated
      result_indexes:
      - 3
      reason: Restatement of NVcomp filtering effect on middle frontal gyrus.
    - source_id: P13-S4-C3
      disposition: represented
      result_indexes:
      - 1
      reason: Null finding for posterior superior temporal gyrus.
    - source_id: P13-S4-C4
      disposition: repeated
      result_indexes:
      - 1
      reason: Restatement of null finding for posterior superior temporal gyrus.
    - source_id: P14-S1-C1
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of significant voxel locations.
    - source_id: P14-S1-C2
      disposition: repeated
      result_indexes:
      - 1
      reason: Restatement of null finding for Wernicke's area.
    - source_id: P14-S2-C4
      disposition: repeated
      result_indexes:
      - 0
      - 3
      reason: Conclusion restating causal relation between ATL and semantic errors.
    unresolved_coverage:
    - source_id: P7-S1-C15
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P13-S1-C6
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P8-S2-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S2-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S1-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S1-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P14-S1-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C13
    - P1-S1-C14
    - P4-S1-C6
    - P5-S2-C15
    - P5-S3-C2
    - P5-S3-C3
    - P5-S3-C5
    - P5-S3-C6
    - P5-S3-C7
    - P5-S3-C9
    - P5-S3-C10
    - P5-S3-C11
    - P5-S3-C12
    - P5-S3-C13
    - P6-S1-C1
    - P6-S1-C2
    - P6-S1-C3
    - P6-S1-C9
    - P7-S1-C5
    - P7-S1-C6
    - P7-S1-C7
    - P7-S1-C8
    - P7-S1-C10
    - P7-S1-C11
    - P7-S2-C4
    - P8-S1-C6
    - P8-S1-C10
    - P8-S2-C3
    - P8-S2-C7
    - P9-S1-C5
    - P9-S1-C10
    - P10-S1-C6
    - P10-S1-C8
    - P10-S1-C9
    - P10-S1-C10
    - P10-S2-C4
    - P10-S2-C6
    - P10-S2-C7
    - P10-S2-C10
    - P12-S1-C7
    - P12-S2-C4
    - P12-S2-C7
    - P12-S3-C7
    - P12-S3-C11
    - P12-S4-C1
    - P12-S4-C2
    - P12-S4-C3
    - P12-S4-C4
    - P13-S1-C6
    - P13-S2-C3
    - P13-S2-C5
    - P13-S3-C4
    - P13-S3-C7
    - P13-S4-C3
    - P13-S4-C4
    - P14-S1-C1
    - P14-S1-C2
    - P14-S1-C3
    - P14-S2-C4
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-6-1
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P1-S1-C11
      - P4-S2-C10
      recruited_sample:
      - P4-S2-C2
      - P4-S2-C3
      - P4-S2-C9
      eligibility:
      - P4-S2-C8
      - P4-S2-C9
      imaging_provenance:
      - P5-S1-C4
      - P5-S1-C6
      - P5-S1-C8
      - P5-S1-C9
      - P5-S2-C2
      imaging_timing:
      - P4-S2-C11
      - P5-S1-C11
      outcome_timing:
      - P1-S1-C11
      - P4-S2-C11
      outcome_definition:
      - P1-S2-C4
      - P4-S3-C9
      - P4-S3-C13
      - P4-S3-C16
      - P4-S4-C3
      validation: []
      analysis_restrictions:
      - P5-S2-C7
      - P6-S1-C10
      dependent_variable_statement:
      - P1-S1-C12
      - P4-S3-C9
      - P5-S2-C12
      - P5-S2-C13
      limitations:
      - P7-S1-C2
      - P7-S1-C3
      - P7-S1-C4
      - P7-S1-C9
      - P12-S3-C7
      - P12-S3-C9
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P1-S1-C14
      - P4-S3-C14
      - P4-S3-C14
      - P5-S2-C12
      - P5-S2-C13
      - P8-S1-C13
      - P10-S1-C7
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P4-S2-C10
      - P5-S3-C3
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P7-S1-C12
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C13
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P5-S2-C6
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
      pdf_sha256: 9cf2d54579089e10ec7294d1ba700958129654cf1f30bc1b95cffe15a4b12829
      review_sha256: d5f30f53979a12ab859c2c061e8de47469ddd04ae873f510a9e507c8842b29ec
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
      - P7-S1-C12
      - P7-S1-C13
      - P7-S1-C14
      - P7-S1-C15
      - P7-S2-C2
      - P7-S2-C3
      source_result: Voxel-based lesion-symptom mapping (unfiltered) identified 35,466
        significant voxels where lesion status predicted semantic error rate (SemErr).
        The highest concentration of significant voxels (19,411) was in the anterior
        half of the middle temporal gyrus and temporal pole (Brodmann areas 21 and
        38). A second cluster was in the posterior middle temporal gyrus (Brodmann
        area 37), and a smaller cluster in the lateral prefrontal cortex (Brodmann
        areas 45/46).
      result_status: detected
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis is the unfiltered VLSM of SemErr. The source
            (P7-S1-C12) explicitly describes the 'analysis performed to explore the
            anatomic basis of the variable SemErr' finding 35,466 voxels. This matches
            the proposed core's focus on the unfiltered association, distinct from
            the filtered analyses (NVcomp/Vcomp) described later in the text.
          source_ids:
          - P7-S1-C12
          - P5-S2-C8
          - P5-S2-C9
        direction:
          answer: fits
          reason: The source states that significant voxels were identified where
            'lesion status and impaired performance on the SemErr measure' were correlated
            (P7-S1-C12). The proposed core claims an association with 'increased rate
            of semantic naming errors', which aligns with the detection of impaired
            performance (higher error rates) in lesioned voxels.
          source_ids:
          - P7-S1-C12
          - P7-S1-C13
        construct:
          answer: fits
          reason: The exposure is lesion status (binary presence/absence at voxel
            level, P2-S2-C6, P5-S2-C3). The outcome is semantic error rate (SemErr),
            defined as semantic errors divided by trials (P4-S3-C9). The method is
            VLSM using t-tests at each voxel (P5-S2-C8). The patient measurement is
            template_lesion_overlap, as lesions were warped to MNI space and analyzed
            for overlap with symptom scores, not patient-specific diffusion tractography.
          source_ids:
          - P4-S3-C9
          - P5-S2-C3
          - P5-S2-C8
          - P2-S2-C6
        qualifications:
          answer: fits
          reason: 'The proposed core includes qualifications regarding the persistence
            of the effect after filtering out NVcomp and Vcomp, and lesion volume.
            The source supports this: P7-S2-C6 states filtering Vcomp ''changed the
            strength of effects slightly but not the overall pattern''; P8-S1-C2 notes
            NVcomp had a ''more substantial impact'' but P8-S1-C4 confirms the majority
            of voxels remained in the anterior temporal lobe; P8-S1-C14 confirms anterior
            temporal lobe involvement remained prominent after regressing out lesion
            volume. These are correctly framed as robustness/qualifications of the
            primary finding rather than standalone nulls.'
          source_ids:
          - P7-S2-C6
          - P8-S1-C2
          - P8-S1-C4
          - P8-S1-C14
        missing_material_caveat:
          answer: fits
          reason: The proposed core includes limitations regarding vascular anatomy
            and coverage (P7-S1-C3, P12-S3-C6, P12-S3-C9). It also notes the underestimation
            of temporal lobe extent. No material caveats that would change the interpretation
            of the unfiltered result are omitted. The distinction between the unfiltered
            result and the filtered results is maintained.
          source_ids:
          - P7-S1-C3
          - P12-S3-C6
          - P12-S3-C9
      optional_pending:
      - sample.time_post_onset
      - exact_voxel_counts_for_filtered_analyses
      - specific_brodmann_area_boundaries_for_clusters
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - 'sample.time_post_onset: source confirmation required; original proposed wording
      remains in the audit.'
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - sample.time_post_onset
    - exact_voxel_counts_for_filtered_analyses
    - specific_brodmann_area_boundaries_for_clusters
    normalizations:
    - field: sample.time_post_onset
      original: mean 68 months post-onset (range 1-381 months); 92% at least 6 months
        post-onset
      action: not_transcribed
      reason: 'Numbers not grounded in usable selected source readings: 6, 92'
    analysis_identity:
      id: R001
      exposure:
        text: lesion status
      outcome:
        text: semantic error rate (SemErr)
      analysis_label: Voxel-based lesion-symptom mapping (unfiltered)
      relation: association
      evidence_ids:
      - P7-S1-C12
      - P7-S1-C13
      - P7-S1-C14
      - P7-S1-C15
      - P7-S2-C2
      - P7-S2-C3
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
        pdf_sha256: 9cf2d54579089e10ec7294d1ba700958129654cf1f30bc1b95cffe15a4b12829
        source_review: _compare/relationships-2026-11-16/review-current/Schwartz2009
        source_status_sha256: 4763f18f11ea91e8571a263278e854c7fb35384af21dd6bbbdf6fb6ab17ae969
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P4-S2-C10:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 9cf2d54579089e10ec7294d1ba700958129654cf1f30bc1b95cffe15a4b12829
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 90f1651ce1922d73d72d512787915bab595752b913c8d357b45298fc3285dd80
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P4-S2-C10
          page: 4
          text_layer_sha256: 90f1651ce1922d73d72d512787915bab595752b913c8d357b45298fc3285dd80
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'The 64 who were included in the study (42%

          females; 48% African American) had a mean age of 58 (range 26–78),

          mean years of education of 14 (10–21) and mean months post-onset

          of 68 (1–381).'
        anchor_text: 'The 64 who were included in the study (42%

          females; 48% African American) had a mean age of 58 (range 26–78),

          mean years of education of 14 (10–21) and mean months post-onset

          of 68 (1–381).'
        excluded_fragments: []
        image_sha256: 482be50362c80d9bfed122daa6ce9839b058ce25f172c5d91c0116d8346a5cae
        transcription: '. The 64 who were included in the study (42%

          females; 48% African American) had a mean age of 58 (range 26–78),

          mean years of education of 14 (10–21) and mean months post-onset

          of 68 (1–381)'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 7
  quote: 'Anatomic ﬁndings

    In the analysis performed to explore the anatomic basis of the

    variable SemErr, we found 35 466 voxels for which a signiﬁcant

    correlation between lesion status and impaired performance on

    the SemErr measure was identiﬁed.'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-25'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
