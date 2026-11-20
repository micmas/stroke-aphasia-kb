---
id: therapy_intensity
name: therapy intensity
kind: ingredient
findings:
- id: f1
  target: aphasia_recovery
  target_kind: impairment
  claim: Higher intensity of aphasia therapy (more hours per week and higher total
    hours) is significantly correlated with greater improvement in aphasia recovery
    scores.
  direction: likely
  relationship: correlational
  method: meta-analysis
  sample:
    n: 864
    population: stroke survivors suffering from aphasia
    phase: not_reported
    time_post_onset: concurrent association between therapy intensity and outcome
      across 10 reviewed studies
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Findings are constrained by the limitations of the original included studies
  evidence_quality: meta-analysis
  strength: weak
  notes: 'Exposure measurement: Intensity of aphasia therapy measured as hours of
    therapy provided per week and total hours of therapy provided across the treatment
    period. Positive studies provided a mean of 8.8 hours per week over 11.2 weeks
    (total 98.4 hours), while negative studies provided a mean of 2.0 hours per week
    over 22.9 weeks (total 43.6 hours). Additional metadata has not been transcribed;
    review the pending-field flags before approval. PDF image reading (P2-S2-C18,
    two-model agreement, human verification pending): These 10


    studies represented 864 individual patients Original text-layer quotation is preserved
    below.'
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
    - proposed_concept:aphasia_recovery
  therapy:
    id: speech_and_language_therapy
    name: speech and language therapy
  citation: '@Bhogal2003'
  source_passages:
  - section: Original source P1-S1-C6
    page: 1
    quote: 'Intensity of therapy was recorded in terms of length of therapy,

      hours of therapy provided per week, and total hours of therapy provided.'
    supports: method
  - section: Original source P1-S1-C12
    page: 1
    quote: "The number of hours of therapy provided in a week was\nsignificantly correlated\
      \ to greater improvement on the PICA (P\x020.001) and the Token Test (P\x02\
      0.027)."
    supports: claim
  - section: Original source P1-S1-C13
    page: 1
    quote: "Total number\nof hours of therapy was significantly correlated with greater\
      \ improvement on the PICA (P\x030.001) and the Token Test\n(P\x030.001)."
    supports: claim
  - section: Original source P2-S2-C18
    page: 2
    quote: 'These 10

      studies represented 864 individual patients.'
    supports: sample
  - section: Original source P4-S1-C11
    page: 4
    quote: 'In the positive studies, significantly more hours

      of therapy per week and significantly more total therapy

      hours in a significantly shorter period of time were provided,

      as compared with the negative studies.'
    supports: claim
  - section: Original source P4-S1-C9
    page: 4
    quote: 'Four studies

      yielded positive results,5,6,13,15 and 4 yielded negative

      outcomes.10,11,14,16

      Of the 4 positive trials analyzed,5,6,13,15 intensive practice

      (mean, 8.8 hours a week) was provided over a short amount

      of time (mean, 11.2 weeks), thereby accumulating an average

      of 98.4 hours of total therapy time.'
    supports: confounders
  - section: Original source P4-S1-C10
    page: 4
    quote: 'In the 4 negative studies

      analyzed,10,11,14,16 less intense practice (mean, 2.0 hours a

      week) was provided for a longer duration (mean, 22.9 weeks),

      accumulating an average of 43.6 hours of total therapy time

      (see Table 3).'
    supports: confounders
  - section: Original source P5-S2-C13
    page: 5
    quote: 'Most of the limitations of the present

      review stem, in part, from the limitations of the original

      studies.'
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-20'
relationship_review:
  paper: Bhogal2003
  proposal_id: R001
  review_status_sha256: 4c13e32663886bf90e8897e86fbd3b93ab19c6aec7fc0a79c4721a4d0028d20b
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 7ba839ea300a49d73c99777071b06e8af4a76eb1984b9c6c842fd875b70b1033
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 7ba839ea300a49d73c99777071b06e8af4a76eb1984b9c6c842fd875b70b1033
        A/passages.json: 337704a58d87499f71f72fc7ecdfb7fc320e6689c3b91d4c957a244513827790
        A/raw.json: e2cfe588d21c93fc1fe7d3a972112442280a7f175995a217e46148f20437c951
        A/source-units.json: 9bc6f93cd621d1ef8c0644f658646e5fa8d9341ed15edfda4dcc9a17bb8ce810
        A/full-source-units.json: 1606f602918f13c895466c0e1daee2b58b5d7c757c7f7fd1fce02073e6912d95
        A/meta.json: d4b3981c17d0ad64914fb59ec36ac0bc8c6ac88f00083ca72c5577603f8e600b
        A/table-images/TABLE-1-page-3-1.png: ddc39ad4471e8d324a32d7641639b50930b664a2d94ab2334c45bd7e5a025b1c
        A/table-images/page-3.png: 8bda1c7fa1972db7ebab67852f706545d60f5f2fa2f4b370ec20e3d0121facca
        A/table-images/page-5.png: a1e1b57377b8aa0bab4c70ff8f4b8bc0e8d53ce67d5013ebefd35bffaa201277
        A/table-images/page-4.png: 3246caba69f76833a02a1f07ecef40690be68e24e6bd0abb46ec7b1b331e1d65
        A/table-images/TABLE-3-page-4-2.png: ae16abb4c1621b1cf9950068456f3ae962e995a39a0e7e118fad6df6224a32d7
        A/table-images/manifest.json: 76e0cc64e8beaa00340ccfed86f0addbf21a77ac624ac2424ca3e0b1ba113d01
        A/table-images/TABLE-2-page-4-1.png: ae16abb4c1621b1cf9950068456f3ae962e995a39a0e7e118fad6df6224a32d7
        A/table-images/TABLE-4-page-5-1.png: 1e29f5b5f01bd01d1a79a2419a4c7d543f14d42396169ac3bcb893ce4e16d76d
        A/clauses/window-03/raw.json: 4dd6e6297f0e6d083558db42c9eea234ebd347a32c6f194672380b0b60088c4c
        A/clauses/window-03/prompt.txt: 8fc279b628b0f12eb20ef03f219f8a42c86618fe1211072f64c8d02feb211613
        A/clauses/window-03/meta.json: 246905de0166328c0fb65633711d822fe35407386c070c35298495416ebbfbeb
        A/clauses/window-04/raw.json: caa668d105fd4764ba0dda0746ebce1180341a2931f248ce562efe37b74bef1f
        A/clauses/window-04/prompt.txt: a389a107daa565329a02cf8733848a9b2537f1e05abd82ddbef58019ec379080
        A/clauses/window-04/meta.json: 33a47273d149a39c99c2b69c8fbb1c513451b29cb9204b7e33998e25675a6d4d
        A/clauses/window-05/raw.json: daf6ef64c82379f297394f436c5d18d9783fae9a65ebd13f3ea1a15d967175ea
        A/clauses/window-05/prompt.txt: d8ff97663ac4feeb5377b51e45ebfb05af646f61b68b2107b4de1799e802b5c1
        A/clauses/window-05/meta.json: 87d7f5a9ae03bc990d91ceb8d4a9d031c1003164aafef4442868ee29f5c5c83c
        A/clauses/window-02/raw.json: ea148481b83be9f3dd4f4ffc79dc68f7caf10f96d0225af0a6e6e408b364f17d
        A/clauses/window-02/prompt.txt: bc03bd8655bba99b333b0ac52daee66dbaa67d42b28eedd5f011daa0e46da063
        A/clauses/window-02/meta.json: ed2c6a3d535425d255b0df505fe0915b98f8916b70d6b6743686611d62c00e4b
        A/clauses/window-01/raw.json: ac7665556a85e20f764e1ef7d227a0dc72aabd8bf8e5e4bfa3a8d2536aa5f792
        A/clauses/window-01/prompt.txt: c17128b0996394b64614b49d074e9b3e14934b6a4f9256f0357a1bd886081dc6
        A/clauses/window-01/meta.json: 0f716ebbb7419e93a88853d8967820551687ec5d975138ea1dfe56573c7a5e7b
        A/clauses/window-06/raw.json: 53dcf8a41f3da6d063f129602ec84e4f3c05df322a06e25deb2d1b02eefcb8b9
        A/clauses/window-06/prompt.txt: c29c5615e7e76d0e5e7952119d29b8d860fedac4f17179753d22bcba846f3d09
        A/clauses/window-06/meta.json: bc402f1d081c9f2c8d23612bc16403f8f3dbedafb391ae27bccf4cd10ec60162
        A/tables/TABLE-4-page-5-4/raw.json: 031ef574dc4d358c9d6ccba3836d9b6708b6e4b3bb48bf92d7fe9d5f25db9c58
        A/tables/TABLE-4-page-5-4/prompt.txt: 00899641404641299ee8ba87ca105420021a23f65497e97bcc71b8957485009c
        A/tables/TABLE-4-page-5-4/meta.json: 55d8e5d6d76fd07cfc7b0039e915851e1bd092ccb88d385d061e9c0e4146c3dd
        A/tables/TABLE-1-page-3-1/raw.json: 13e5692113efad502cad9c30d054153ec8289c2c8782d228479fcad6384b3704
        A/tables/TABLE-1-page-3-1/prompt.txt: 71abbb255e7c7a330e7ca66b8a1838c2b26824b66974be293e0022dc7455ac74
        A/tables/TABLE-1-page-3-1/meta.json: b9923cddea37dd23add7b96e9b3ee9de1bd0b560ef5a72e211cb73e4641fd32e
        A/tables/TABLE-3-page-4-3/raw.json: e4b3eefa2d21c9e65e34986928209658596ca033a738476eaa0c7344ff0e2cfa
        A/tables/TABLE-3-page-4-3/prompt.txt: 52c9297a5a2857cf202c06b6d3c71ab48c5ee4b84f3262404e23d2bdbcefec6c
        A/tables/TABLE-3-page-4-3/meta.json: 0d92db129154f0a1b5d35b6a54528a2d1b2388db20fbe61f210d5a83b002649f
        A/tables/TABLE-2-page-4-2/raw.json: 21a2779bb9f31fda1a7b70dde03872f71ccc7df3bcce641144775e2401d618e0
        A/tables/TABLE-2-page-4-2/prompt.txt: 22a1e6eede9a849a27b6fbfd930bb6f82a4b68a6966edf065b5bfa325e5a1b64
        A/tables/TABLE-2-page-4-2/meta.json: 1a0d000516b13431736ba8e1a9c319bbf67c83d5a0ad7341f18102bf4a3cf937
        B/passages.json: 337704a58d87499f71f72fc7ecdfb7fc320e6689c3b91d4c957a244513827790
        B/raw.json: 9cdaf5d0a9950b4c90e92d3da6ef9b7f5077215a3e997453aeed1bfb307f80bc
        B/source-units.json: 9bc6f93cd621d1ef8c0644f658646e5fa8d9341ed15edfda4dcc9a17bb8ce810
        B/full-source-units.json: 1606f602918f13c895466c0e1daee2b58b5d7c757c7f7fd1fce02073e6912d95
        B/meta.json: 834bb502688af11e0c700ad6ad7f7fb085c5cca482453b8f91b272417c80c500
        B/table-images/TABLE-1-page-3-1.png: ddc39ad4471e8d324a32d7641639b50930b664a2d94ab2334c45bd7e5a025b1c
        B/table-images/page-3.png: 8bda1c7fa1972db7ebab67852f706545d60f5f2fa2f4b370ec20e3d0121facca
        B/table-images/page-5.png: a1e1b57377b8aa0bab4c70ff8f4b8bc0e8d53ce67d5013ebefd35bffaa201277
        B/table-images/page-4.png: 3246caba69f76833a02a1f07ecef40690be68e24e6bd0abb46ec7b1b331e1d65
        B/table-images/TABLE-3-page-4-2.png: ae16abb4c1621b1cf9950068456f3ae962e995a39a0e7e118fad6df6224a32d7
        B/table-images/manifest.json: 02cc41fa9ddc0c5ee8679159decc3cd42fdb419ecf48727d095a9f5099118cd0
        B/table-images/TABLE-2-page-4-1.png: ae16abb4c1621b1cf9950068456f3ae962e995a39a0e7e118fad6df6224a32d7
        B/table-images/TABLE-4-page-5-1.png: 1e29f5b5f01bd01d1a79a2419a4c7d543f14d42396169ac3bcb893ce4e16d76d
        B/clauses/window-03/raw.json: 2714706e3d2efcbaeaee5785faa89e868d5cf113c2703dd63979f6da49160efa
        B/clauses/window-03/prompt.txt: 8fc279b628b0f12eb20ef03f219f8a42c86618fe1211072f64c8d02feb211613
        B/clauses/window-03/meta.json: 44c787a562e0abd0d78b4ea3847277813363c6d0e6b5f83fc7daaecdcbd8ae7d
        B/clauses/window-04/raw.json: e878fe17695cec90034a3815382e578b47c5a5e20c38d3d52386fadb82db58b4
        B/clauses/window-04/prompt.txt: a389a107daa565329a02cf8733848a9b2537f1e05abd82ddbef58019ec379080
        B/clauses/window-04/meta.json: 54403da84b9b9e77bc468ac4c63eedb86611594742e6fdb70ce18f2bb3a55caa
        B/clauses/window-05/raw.json: 5dfdc8bb4667cc7a941e50824b07440d3bf853adb6513959d3524191c54c8042
        B/clauses/window-05/prompt.txt: d8ff97663ac4feeb5377b51e45ebfb05af646f61b68b2107b4de1799e802b5c1
        B/clauses/window-05/meta.json: 07ed4c747314a273be9d0e0a8264eda6ec0df08b51573c08a1d1f74156a5241f
        B/clauses/window-02/raw.json: ea443960ffdaa834952fd3a96c9b18c42bfc63807fa812321a6e3c7f7ceded26
        B/clauses/window-02/prompt.txt: bc03bd8655bba99b333b0ac52daee66dbaa67d42b28eedd5f011daa0e46da063
        B/clauses/window-02/meta.json: 845f8f3c3fb6d5dd6656d7ac9ce1cb3397714ae24187a4c8b1c1e1400a3e00b6
        B/clauses/window-01/raw.json: 9204809627fe281a97d38c64f716f731e47a908bf7581c9d16e57ec5ac8dc96f
        B/clauses/window-01/prompt.txt: c17128b0996394b64614b49d074e9b3e14934b6a4f9256f0357a1bd886081dc6
        B/clauses/window-01/meta.json: b1cb718df95cb9affb52d29892bbf31ca5d2f7287eb8032b4c18d7fae1203d1f
        B/clauses/window-06/raw.json: b5dc467279298d35cd0f578bcf1f5da075f2aa2fa32568d2220fd98d907a30d3
        B/clauses/window-06/prompt.txt: c29c5615e7e76d0e5e7952119d29b8d860fedac4f17179753d22bcba846f3d09
        B/clauses/window-06/meta.json: 8bd00958b8cc8af7b5be5aea1e962d1e7a0eb9690c92f7cb82a9c65203ba1a0f
        B/tables/TABLE-4-page-5-4/raw.json: 5d1bd10c3b209c5f4163f3a5da70650da8d75ac2200796e600c5976353770fa7
        B/tables/TABLE-4-page-5-4/prompt.txt: 00899641404641299ee8ba87ca105420021a23f65497e97bcc71b8957485009c
        B/tables/TABLE-4-page-5-4/meta.json: f83b9c92c7b512d0a45ec867c14699274f27b157ffb609749b698c6d949a74b2
        B/tables/TABLE-1-page-3-1/raw.json: 6147a748c8627ac59a3f8cec4258d1e9a33315f7257c4d917a128032844d552a
        B/tables/TABLE-1-page-3-1/prompt.txt: 71abbb255e7c7a330e7ca66b8a1838c2b26824b66974be293e0022dc7455ac74
        B/tables/TABLE-1-page-3-1/meta.json: d0e6df63831b35fc726b9b658d63a0ee14ad4213bbafcde3e485efe8a1e9adb6
        B/tables/TABLE-3-page-4-3/raw.json: 8df958766b62efdbab54cb971ebcbf15c5e2be0d50a32776582fa5907fb2e214
        B/tables/TABLE-3-page-4-3/prompt.txt: 52c9297a5a2857cf202c06b6d3c71ab48c5ee4b84f3262404e23d2bdbcefec6c
        B/tables/TABLE-3-page-4-3/meta.json: 9c26051ccc7a8a68c35a3bf98422f67f44e72c0f741d94098e308094321dc970
        B/tables/TABLE-2-page-4-2/raw.json: 4091228de513d1dfb22db9b1c9800853dd1c01e788a779abf787f18eb1bde377
        B/tables/TABLE-2-page-4-2/prompt.txt: 22a1e6eede9a849a27b6fbfd930bb6f82a4b68a6966edf065b5bfa325e5a1b64
        B/tables/TABLE-2-page-4-2/meta.json: 71e8878710a02e21a31ab8591515d904b4e2b4267883134bf01a650addb1dc80
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
      pdf_sha256: 7ba839ea300a49d73c99777071b06e8af4a76eb1984b9c6c842fd875b70b1033
      source_review: _compare/relationships-2026-11-16/review-current/Bhogal2003
      source_status_sha256: d56835807d123a0a5d0f41da4d0876dce51d7d242ba0083082c06aa8b590fb45
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R001
    exposure:
      text: intensity of therapy
    outcome:
      text: treatment effect
    analysis_label: Comparison of positive vs negative studies
    relation: association
    evidence_ids:
    - P1-S1-C8
    - P1-S1-C9
    - P3-S3-C5
    - P4-S1-C9
    - P4-S1-C10
    - P4-S1-C11
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
      pdf_sha256: 7ba839ea300a49d73c99777071b06e8af4a76eb1984b9c6c842fd875b70b1033
      source_review: _compare/relationships-2026-11-16/review-current/Bhogal2003
      source_status_sha256: d56835807d123a0a5d0f41da4d0876dce51d7d242ba0083082c06aa8b590fb45
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P1-S1-C8
      - Result passage disposed without unit P1-S1-C9
      - Accounting without a linked unit P2-S4-C6
      - Accounting without a linked unit P2-S4-C8
      - Accounting without a linked unit P3-S1-C10
      - Accounting without a linked unit P3-S1-C11
      - Accounting without a linked unit P3-S1-C2
      - Accounting without a linked unit P3-S1-C7
      - Accounting without a linked unit P3-S2-C7
      - Unaccounted source passage P3-S1-C7
      - Unaccounted source passage P3-S1-C2
      - Unaccounted source passage P2-S4-C6
      - Unaccounted source passage P3-S1-C11
      - Unaccounted source passage P3-S2-C7
      - Unaccounted source passage P3-S1-C10
      - Unaccounted source passage P2-S4-C8
      - Result passage disposed without unit P3-S3-C4
      - Result passage disposed without unit P3-S3-C5
      - Result passage disposed without unit P3-S3-C6
      - Result passage disposed without unit P4-S1-C1
      - Result passage disposed without unit P4-S1-C9
      - Result passage disposed without unit P4-S1-C10
      - Result passage disposed without unit P4-S1-C11
      - Accounting without a linked unit P4-S2-C2
      - Result passage disposed without unit P4-S2-C3
      - Result passage disposed without unit P4-S2-C4
      - Result passage disposed without unit P4-S2-C5
      - Result passage disposed without unit P4-S2-C6
      - Unaccounted source passage P4-S2-C2
      - Result passage disposed without unit P5-S1-C10
      - Result passage disposed without unit P5-S1-C12
      - Result passage disposed without unit P5-S1-C13
      - Result passage disposed without unit P5-S1-C7
      - 'window 8: invalid/duplicate disposition P5-S2-C13'
      - Accounting without a linked unit P5-S2-C3
      - Accounting without a linked unit P5-S2-C4
      - Accounting without a linked unit P5-S2-C5
      - Unaccounted source passage P5-S2-C3
      - Unaccounted source passage P5-S2-C4
      - Unaccounted source passage P5-S2-C5
      - Accounting without a linked unit P5-S3-C10
      - Result passage disposed without unit P5-S3-C2
      - Result passage disposed without unit P5-S3-C3
      - Accounting without a linked unit P5-S3-C9
      - Unaccounted source passage P5-S3-C10
      - Unaccounted source passage P5-S3-C9
      unattached_null_or_qualifier_ids:
      - P1-S1-C8
      - P3-S3-C5
      - P4-S1-C1
      - P5-S1-C13
      - P5-S2-C4
      - P5-S3-C4
      suppressed_nonrepresented_units: 9
      default_disposition_count_requires_completeness_check: 120
      unselected_timing_passages: []
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P5-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      empty_frame_slots_require_confirmation:
      - imaging_provenance
      - imaging_timing
      - outcome_timing
      - outcome_definition
      - validation
      - personal_factors
      - tested_personal_effects
      - adjustment_roles
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-3-1
      - TABLE-2-page-4-2
      - TABLE-3-page-4-3
      - TABLE-4-page-5-4
      unlinked_tables:
      - TABLE-1-page-3-1
      - TABLE-2-page-4-2
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units: []
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 7ba839ea300a49d73c99777071b06e8af4a76eb1984b9c6c842fd875b70b1033
      source_review: _compare/relationships-2026-11-16/review-current/Bhogal2003
      source_status_sha256: d56835807d123a0a5d0f41da4d0876dce51d7d242ba0083082c06aa8b590fb45
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C8
      disposition: represented
      result_indexes:
      - 0
      reason: Describes therapy hours/weeks for positive vs negative studies.
    - source_id: P1-S1-C9
      disposition: represented
      result_indexes:
      - 0
      reason: Describes total hours for positive vs negative studies.
    - source_id: P1-S1-C10
      disposition: represented
      result_indexes:
      - 1
      reason: Reports inverse correlation between length of therapy and weekly/total
        hours.
    - source_id: P1-S1-C11
      disposition: represented
      result_indexes:
      - 2
      reason: Reports inverse correlation between length of therapy and PICA scores.
    - source_id: P1-S1-C12
      disposition: represented
      result_indexes:
      - 3
      reason: Reports correlation between weekly hours and PICA/Token Test improvement.
    - source_id: P1-S1-C13
      disposition: represented
      result_indexes:
      - 4
      reason: Reports correlation between total hours and PICA/Token Test improvement.
    - source_id: P3-S3-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Summary count of positive and negative studies.
    - source_id: P3-S3-C5
      disposition: represented
      result_indexes:
      - 0
      reason: Provides average hours/weeks for positive vs negative studies.
    - source_id: P3-S3-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Introductory phrase to total hours data.
    - source_id: P4-S1-C1
      disposition: represented
      result_indexes:
      - 0
      reason: Provides total hours for positive vs negative trials.
    - source_id: P4-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes number of studies using specific scales.
    - source_id: P4-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: States number of studies providing appropriate data.
    - source_id: P4-S1-C9
      disposition: represented
      result_indexes:
      - 0
      reason: Details intensity metrics for positive trials.
    - source_id: P4-S1-C10
      disposition: represented
      result_indexes:
      - 0
      reason: Details intensity metrics for negative trials.
    - source_id: P4-S1-C11
      disposition: represented
      result_indexes:
      - 0
      reason: States significant differences in intensity between positive and negative
        studies.
    - source_id: P4-S1-C12
      disposition: represented
      result_indexes:
      - 1
      reason: Reports inverse correlation between length of therapy and weekly hours.
    - source_id: P4-S2-C2
      disposition: represented
      result_indexes:
      - 8
      reason: Reports correlation between weekly hours and total hours.
    - source_id: P4-S2-C3
      disposition: repeated
      result_indexes:
      - 1
      reason: Restatement of inverse correlation between length and weekly hours.
    - source_id: P4-S2-C4
      disposition: repeated
      result_indexes:
      - 8
      reason: Restatement of correlation between weekly and total hours.
    - source_id: P4-S2-C5
      disposition: repeated
      result_indexes:
      - 1
      reason: Restatement of inverse correlation between length and intensity.
    - source_id: P4-S2-C6
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of intensity difference between positive and negative studies.
    - source_id: P4-S2-C7
      disposition: represented
      result_indexes:
      - 6
      reason: Provides mean improvement for positive studies on PICA and Token Test.
    - source_id: P4-S2-C8
      disposition: represented
      result_indexes:
      - 6
      reason: Provides mean improvement for negative studies on PICA and Token Test.
    - source_id: P4-S2-C9
      disposition: represented
      result_indexes:
      - 6
      reason: States significant difference in PICA and Token Test improvement between
        groups.
    - source_id: P5-S1-C3
      disposition: represented
      result_indexes:
      - 7
      reason: Provides mean ratio of improvement in FCP for negative and positive
        trials.
    - source_id: P5-S1-C4
      disposition: represented
      result_indexes:
      - 7
      reason: States non-significant difference in FCP scores between groups.
    - source_id: P5-S1-C5
      disposition: repeated
      result_indexes:
      - 7
      reason: Restatement of non-significant FCP results.
    - source_id: P5-S1-C6
      disposition: represented
      result_indexes:
      - 2
      reason: Reports inverse correlation between length of therapy and PICA scores.
    - source_id: P5-S1-C7
      disposition: repeated
      result_indexes:
      - 2
      reason: Restatement of inverse correlation between length and PICA.
    - source_id: P5-S1-C8
      disposition: represented
      result_indexes:
      - 5
      reason: Reports non-significant trend between length of therapy and Token Test
        scores.
    - source_id: P5-S1-C9
      disposition: represented
      result_indexes:
      - 3
      reason: Reports correlation between weekly hours and PICA/Token Test improvement.
    - source_id: P5-S1-C10
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of total hours difference between positive and negative
        studies.
    - source_id: P5-S1-C11
      disposition: represented
      result_indexes:
      - 4
      reason: Reports correlation between total hours and PICA/Token Test scores.
    - source_id: P5-S1-C12
      disposition: repeated
      result_indexes:
      - 4
      reason: Restatement of total hours correlation with improvement.
    - source_id: P5-S1-C13
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of intensity metrics for positive vs negative studies.
    - source_id: P5-S2-C2
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement that intensive therapy resulted in improved outcomes.
    - source_id: P5-S2-C3
      disposition: repeated
      result_indexes:
      - 3
      reason: Restatement of association between intense therapy and PICA/Token Test
        scores.
    - source_id: P5-S2-C4
      disposition: repeated
      result_indexes:
      - 7
      reason: Restatement that FCP did not yield a similar pattern.
    - source_id: P5-S2-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes quality ratings of studies.
    - source_id: P5-S3-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes limitations regarding nonstandardized measures.
    - source_id: P5-S3-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes study power and sample size limitations.
    - source_id: P5-S3-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Details on specific trial (Lincoln et al) completion rates.
    - source_id: P5-S3-C9
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement that lower-intensity therapy does not result in significant
        change.
    - source_id: P5-S3-C10
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement that intensive SLT results in significant improvement.
    unresolved_coverage:
    - source_id: P5-S2-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P3-S3-C4
    - P3-S3-C6
    - P4-S1-C1
    - P4-S1-C4
    - P4-S1-C8
    - P4-S2-C3
    - P4-S2-C4
    - P4-S2-C5
    - P4-S2-C6
    - P5-S1-C5
    - P5-S1-C7
    - P5-S1-C10
    - P5-S1-C12
    - P5-S1-C13
    - P5-S2-C2
    - P5-S2-C3
    - P5-S2-C4
    - P5-S2-C5
    - P5-S2-C14
    - P5-S3-C2
    - P5-S3-C3
    - P5-S3-C4
    - P5-S3-C9
    - P5-S3-C10
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-3-1
    - TABLE-2-page-4-2
    - TABLE-3-page-4-3
    - TABLE-4-page-5-4
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P4-S1-C8
      - P4-S1-C9
      - P4-S1-C10
      recruited_sample:
      - P2-S1-C11
      eligibility:
      - P2-S1-C2
      - P2-S1-C4
      - P2-S1-C5
      - P2-S1-C6
      - P2-S1-C7
      imaging_provenance: []
      imaging_timing: []
      outcome_timing: []
      outcome_definition: []
      validation: []
      analysis_restrictions:
      - P4-S1-C5
      - P4-S1-C6
      dependent_variable_statement:
      - P1-S1-C7
      - P2-S2-C13
      - P4-S1-C2
      - P4-S1-C3
      limitations:
      - P5-S2-C13
      - P5-S2-C14
      - P5-S3-C2
      - P5-S3-C3
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles: []
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P2-S2-C18
    outcome_type: change_from_baseline
    imaging_vs_outcome: not_stated
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P5-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C11
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
      pdf_sha256: 7ba839ea300a49d73c99777071b06e8af4a76eb1984b9c6c842fd875b70b1033
      review_sha256: 4c13e32663886bf90e8897e86fbd3b93ab19c6aec7fc0a79c4721a4d0028d20b
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
      - P1-S1-C8
      - P1-S1-C9
      - P3-S3-C5
      - P4-S1-C9
      - P4-S1-C10
      - P4-S1-C11
      source_result: The study is a meta-analysis of 10 clinical trials (8 used for
        correlation analysis) investigating the relationship between the intensity
        of speech and language therapy (SLT) and aphasia recovery in stroke patients.
        The analysis compared studies that reported a significant treatment effect
        (positive) with those that did not (negative). It found that positive studies
        provided significantly higher therapy intensity (mean 8.8 hours/week for 11.2
        weeks, totaling 98.4 hours) compared to negative studies (mean 2.0 hours/week
        for 22.9 weeks, totaling 43.6 hours). Pearson correlations confirmed that
        higher hours per week and total hours were associated with greater improvement
        in PICA and Token Test scores, while total therapy duration was inversely
        correlated with intensity.
      result_status: detected
      patient_measurement: non_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis correctly identifies the core comparison as
            the relationship between therapy intensity and treatment outcome (positive
            vs negative studies) using Pearson correlations and t-tests on the aggregated
            study data. The source confirms this is the primary analysis described
            in the Results section.
          source_ids:
          - P1-S1-C7
          - P2-S2-C12
          - P2-S2-C13
          - P4-S1-C2
        direction:
          answer: fits
          reason: The draft correctly states that higher intensity is correlated with
            greater improvement. The source explicitly states that positive studies
            (higher intensity) had greater mean improvements on PICA and Token Test
            scores compared to negative studies, and that hours per week/total hours
            were significantly correlated with greater improvement.
          source_ids:
          - P1-S1-C12
          - P1-S1-C13
          - P4-S1-C11
          - P4-S2-C7
          - P4-S2-C8
        construct:
          answer: fits
          reason: The exposure (therapy intensity) and outcome (aphasia recovery via
            PICA/Token Test) are correctly identified. The patient measurement is
            non-imaging (clinical scales), which is accurate as the study uses behavioral
            scores, not imaging data. The draft correctly identifies the population
            as stroke survivors with aphasia.
          source_ids:
          - P1-S1-C3
          - P1-S1-C6
          - P4-S1-C3
          - P2-S1-C6
        qualifications:
          answer: fits
          reason: The draft includes the specific intensity values for positive vs
            negative studies (8.8 vs 2.0 hours/week; 98.4 vs 43.6 total hours) which
            matches the source data in P4-S1-C9 and P4-S1-C10. The limitation regarding
            original study constraints is also correctly included.
          source_ids:
          - P4-S1-C9
          - P4-S1-C10
          - P5-S2-C13
        missing_material_caveat:
          answer: fits
          reason: The draft captures the main limitation mentioned in the source (P5-S2-C13).
            While the source notes that some studies were excluded from the correlation
            analysis due to missing data (P4-S1-C5, P4-S1-C6), the draft's focus on
            the 8 studies used for the correlation is consistent with the 'core relationship'
            being reviewed. No material caveat that changes the interpretation of
            the positive correlation is omitted.
          source_ids:
          - P5-S2-C13
          - P4-S1-C8
      optional_pending:
      - Specific P-values for the correlation between intensity and PICA/Token Test
        scores are not transcribed in the draft, but the direction and significance
        are captured.
      - The exact number of studies included in the correlation analysis (8 vs 10)
        is not explicitly stated in the draft's main claim, though the sample size
        864 refers to the total patients in the 10 studies.
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Specific P-values for the correlation between intensity and PICA/Token Test
      scores are not transcribed in the draft, but the direction and significance
      are captured.
    - The exact number of studies included in the correlation analysis (8 vs 10) is
      not explicitly stated in the draft's main claim, though the sample size 864
      refers to the total patients in the 10 studies.
    normalizations:
    - field: bucket
      original: predictors
      action: route_from_kind
      value: ingredients
    analysis_identity:
      id: R001
      exposure:
        text: intensity of therapy
      outcome:
        text: treatment effect
      analysis_label: Comparison of positive vs negative studies
      relation: association
      evidence_ids:
      - P1-S1-C8
      - P1-S1-C9
      - P3-S3-C5
      - P4-S1-C9
      - P4-S1-C10
      - P4-S1-C11
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
        pdf_sha256: 7ba839ea300a49d73c99777071b06e8af4a76eb1984b9c6c842fd875b70b1033
        source_review: _compare/relationships-2026-11-16/review-current/Bhogal2003
        source_status_sha256: d56835807d123a0a5d0f41da4d0876dce51d7d242ba0083082c06aa8b590fb45
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P1-S1-C12:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 7ba839ea300a49d73c99777071b06e8af4a76eb1984b9c6c842fd875b70b1033
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 7814d70d2427bed878535eff14cdb38a461461f319bcf16681883786edbe15f7
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P1-S1-C12
          page: 1
          text_layer_sha256: 7814d70d2427bed878535eff14cdb38a461461f319bcf16681883786edbe15f7
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: "The number of hours of therapy provided in a week was\nsignificantly\
          \ correlated to greater improvement on the PICA (P\x020.001) and the Token\
          \ Test (P\x020.027)."
        anchor_text: "The number of hours of therapy provided in a week was\nsignificantly\
          \ correlated to greater improvement on the PICA (P\x020.001) and the Token\
          \ Test (P\x020.027)."
        excluded_fragments: []
      P1-S1-C13:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 7ba839ea300a49d73c99777071b06e8af4a76eb1984b9c6c842fd875b70b1033
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 4f79e92868afe9aa42f0be7d7031a888b1081b64f8124a476325edcd8a646ca3
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P1-S1-C13
          page: 1
          text_layer_sha256: 4f79e92868afe9aa42f0be7d7031a888b1081b64f8124a476325edcd8a646ca3
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: "Total number\nof hours of therapy was significantly correlated\
          \ with greater improvement on the PICA (P\x030.001) and the Token Test\n\
          (P\x030.001)."
        anchor_text: "Total number\nof hours of therapy was significantly correlated\
          \ with greater improvement on the PICA (P\x030.001) and the Token Test\n\
          (P\x030.001)."
        excluded_fragments: []
      P2-S2-C18:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 7ba839ea300a49d73c99777071b06e8af4a76eb1984b9c6c842fd875b70b1033
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: e9f865c29dc3f0c083a5b694ec4df33f1debd27cc1e56d4499a2796f0a2e1961
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S2-C18
          page: 2
          text_layer_sha256: e9f865c29dc3f0c083a5b694ec4df33f1debd27cc1e56d4499a2796f0a2e1961
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'These 10

          studies represented 864 individual patients.'
        anchor_text: 'These 10

          studies represented 864 individual patients.'
        excluded_fragments: []
        image_sha256: 0e9796d35d2afd4905cb06876b711233e2db0f3b91a9467b4887805f91a29a6a
        transcription: 'These 10


          studies represented 864 individual patients'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 1
  quote: 'Intensity of therapy was recorded in terms of length of therapy,

    hours of therapy provided per week, and total hours of therapy provided.'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-20'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
