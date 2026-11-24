---
id: post_stroke_aphasia_tapping
name: post-stroke aphasia tapping performance
kind: impairment
findings:
- id: f1
  target: tapping_performance
  target_kind: impairment
  claim: Individuals with chronic, post-stroke aphasia performed significantly below
    the level of neurotypical controls on rhythm production (tapping).
  direction: likely
  relationship: correlational
  method: behavioral_only
  sample:
    n: not_reported
    population: Not transcribed; confirm from the original PDF population and timing
      passages.
    phase: not_reported
    time_post_onset: Chronic stage of recovery (approximately 1 year or more post-stroke).
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - The aphasia cohort exhibited more variability in tapping performance compared
    to controls.
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Tapping performance measured via a composite score
    (averaging vector length and absolute vector angle) across isochronous and music-based
    tapping tasks. Tapping was performed with the left hand for all participants to
    maintain consistency due to common right-sided motor weakness in aphasia. Additional
    metadata has not been transcribed; review the pending-field flags before approval.
    PDF image reading (P3-S2-C6, two-model agreement, human verification pending):
    MATERIALS AND METHODS


    Participants


    Thirty-three individuals with chronic, post-stroke aphasia and 29 neurotypical
    controls, matched on age and education level, successfully completed the research
    protocol Original text-layer quotation is preserved below. PDF image reading (P3-S2-C8,
    two-model agreement, human verification pending): . We recruited indi-

    viduals with aphasia who had aphasia due to ischemic or hemorrhagic stroke confined
    mostly to

    left hemisphere supratentorial regions (Wilson et al., 2023) and were in the chronic
    stage of

    recovery (approximately 1 yr or more post-stroke) Original text-layer quotation
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
    - not_transcribed:sample.n
    - not_transcribed:sample.population
    - proposed_concept:tapping_performance
  citation: '@Kasdan2025'
  source_passages:
  - section: Original source P11-S1-C3
    page: 11
    quote: 'Individuals with aphasia performed below the level of controls on tapping
      (β = 19.98, p =

      0.0030, Δr2 = 12.7%, f 2 = 0.18) and demographic factors were not significantly
      associated with

      tapping (Table 3).'
    supports: claim
  - section: Original source P3-S2-C6
    page: 3
    quote: 'MATERIALS AND METHODS

      Participants

      Thirty-three individuals with chronic, post-stroke aphasia and 29 neurotypical
      controls, matched

      on age and education level, successfully completed the research protocol.'
    supports: sample
  - section: Original source P3-S2-C8
    page: 3
    quote: 'We recruited indi-

      viduals with aphasia who had aphasia due to ischemic or hemorrhagic stroke confined
      mostly to

      left hemisphere supratentorial regions (Wilson et al., 2023) and were in the
      chronic stage of

      recovery (approximately 1 yr or more post-stroke).'
    supports: sample
  - section: Original source P4-S1-C14
    page: 4
    quote: 'As many individuals with aphasia experience motor weakness on their right
      side, we

      instructed all participants to tap with their left hand for consistency.'
    supports: confounders
  - section: Original source P9-S1-C7
    page: 9
    quote: 'A tapping composite score for each partic-

      ipant was then computed, which was the average of vector length and vector angle
      across nine

      stimuli (3 isochronous, 6 music).'
    supports: method
  - section: Original source P11-S1-C5
    page: 11
    quote: 'In general, individuals with aphasia exhibited more variability in their
      tapping

      performance compared to controls (Figure 1 and Figures S1 and S2 for individual
      level data).'
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-24'
relationship_review:
  paper: Kasdan2025
  proposal_id: R001
  review_status_sha256: d7ffc5bd3ea54f538fa848f4f144fa0e4a72665d2948fba8700a261e2a7af1b1
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 153707f62f0c4a223cb76cd9205efb5ad7a3776b097854fdcdce6007ec0f9c98
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 153707f62f0c4a223cb76cd9205efb5ad7a3776b097854fdcdce6007ec0f9c98
        A/passages.json: efbf25d8e111bd95ef6316315ef0956f84e62dcea08cd7835ee87e9d14d065d1
        A/raw.json: ec1cac73eb4ce5162bd4cd8ae839f4d0aeb855d6ce9cc179881b64b3ee364d6d
        A/source-units.json: ed9c8906fe315341d0efe7abf45f4e42d1cc17ce74071735927b2212557e9d93
        A/full-source-units.json: cf0c551e91c11889d7f3071372bf95a07de883122b5ac634636917f804ae0388
        A/meta.json: 7d5716179e581d016871f408924e83c022302a02353e71019f7753bc2e27d6be
        A/table-images/TABLE-3-page-10-2.png: f4c18fb625c12d808a16532d4e871fd618f8c4c16340aa98cad20db81ba62832
        A/table-images/page-14.png: 91497ed01177a3c0eee45d48d8cad1a69684b4b598d9cdfe28be94e02d7d6a0e
        A/table-images/TABLE-4-page-14-1.png: 73bbaa4449ac525b59f412eb0f2132fcd79ea8fe9bd91450829880d4ae3015d1
        A/table-images/page-10.png: 081b11050eda596b5f8f236f985ae454f79da566957b3bbb6f732cf2848b56f4
        A/table-images/page-4.png: 99f71409c0f8debb68eaafbb7be4f4ce6721f6b8fd969ee4513f860739f8b6f5
        A/table-images/TABLE-1-page-4-1.png: 0865af9fff42ab1171a4c723f9f3cddcf53ba8e3ac342778bc66d9a6fd2919ad
        A/table-images/manifest.json: fbcf73b0b6d1f4d7624fdf7436c7c4f403f81ae2104185be364a9d2a5627a995
        A/table-images/TABLE-2-page-10-1.png: f4c18fb625c12d808a16532d4e871fd618f8c4c16340aa98cad20db81ba62832
        A/clauses/window-11/raw.json: 1de1a5286ba92b3f49cf13e2b1971c016ca3a79d1386d3f11f20c078ca8c1668
        A/clauses/window-11/prompt.txt: 8f36b6f0c2bc2e9f4ae90c8be7490e699a2081ce7db12e0cfd15454db4f17a1c
        A/clauses/window-11/meta.json: 860addbd60eae55fe0482e514ada2efc7881133c231305d69cfbda65cf91cb60
        A/clauses/window-10/raw.json: fd3d2070a435a761bcb0409808135cf18b30b892e57188d04319074afbb18d1b
        A/clauses/window-10/prompt.txt: 69b34e66f3d75548726b45528392f0d7b69744bf2b3c3113a51116d916fb6ee3
        A/clauses/window-10/meta.json: b7b9fa2be7ecc58e05a60ce65cc1c6ce94b1d6f3b3b24dc9747482f60fb116ec
        A/clauses/window-03/raw.json: c1170d08396f13c6916a51bcf364cacc3005a3b7eb3204189ddb7163ad92b4d9
        A/clauses/window-03/prompt.txt: 57fc2fe390776ecdcbff494226d3d2930dc965fd76f416a9b98ad71f1fae9559
        A/clauses/window-03/meta.json: 05ec45594ad745ffa75803d1a7f0e5a9c367ef4c9d9d40fbf3f5a444dacfa910
        A/clauses/window-04/raw.json: f2cee593dbd1b08c03af907b7265976659c0761988a13443980a100095bc7a89
        A/clauses/window-04/prompt.txt: 4f6b5f2355c60a678257459397dd1b4902a629950bb3e76dea7e9475bd530ac1
        A/clauses/window-04/meta.json: eceda17f913394951ca9857313d1a8764084415c2205eb4c05a0c0763161a1ec
        A/clauses/window-05/raw.json: 10d2ca044c139845c5fa7c0840b3029c895eb01e5f82eaf9f1aca797ce04e2a9
        A/clauses/window-05/prompt.txt: c9c6aeeb8feeee1b204c36ee26563028c67b75a966783ae7ad517e376ee0b102
        A/clauses/window-05/meta.json: c59045d20a41fb76daeef167bd80307e50c81a0a8a97c3d1bdfe31d5c12a40b1
        A/clauses/window-02/raw.json: 435a37067aaf9180057c9d4c03e25d3594af4366e9c54714012da7c30a678886
        A/clauses/window-02/prompt.txt: c1166790db75cb2c8e3f3b4b9f4c338669dd75d7e86b37e8528e350e47990607
        A/clauses/window-02/meta.json: 90ba004c0a63de21602b2236b86ca65290c1de946992e4b4f1c7797a7a5cc7b6
        A/clauses/window-12/raw.json: 2dc5dc2fa61c2d3733cf072120dd724301ee05f80d37920a1b0c4600890962b5
        A/clauses/window-12/prompt.txt: c3158450e2a9c05ddc5e82d3007bd3e2261c9ce3fc8398a1eb0b29e0fc3b939a
        A/clauses/window-12/meta.json: ab168c4322ab7655f1c609f5b00d03dbc2331f08bfee780d8c35bfc445d902b2
        A/clauses/window-13/raw.json: 7e6083fab2d9561390d71d61a35cc74db0ae2fd4d525372fc88908750b137df2
        A/clauses/window-13/prompt.txt: 59445d0d37b3bafe6337da1c8f7e08f2d0d4235d300e2384e32c0694fa8e5426
        A/clauses/window-13/meta.json: 0f7b76ccb4a699ed22b1ac586a03e08365e141e715028ac6c48801ab6ae7b823
        A/clauses/window-09/raw.json: 2ccc7d28aec2950b68a557ab7b941be8298d6e705402a6b60b80545089ff75ae
        A/clauses/window-09/prompt.txt: 980d1f2d270a1cb84b33f496c866fee6a057e50cf1f05b9f13e8f6366e46814f
        A/clauses/window-09/meta.json: dac080529c712db328a6db55a26ad86c4746e03c652d78f6be85ed5b4c796260
        A/clauses/window-07/raw.json: 29a9f937d7c2c8c56f750f75c18c8d23dc339c675c835078cf52923eb63fc355
        A/clauses/window-07/prompt.txt: df8702908c87083bf69e0ca43139b73df49b14bf3ce5345cefae29edd2ce077f
        A/clauses/window-07/meta.json: db178b62fee122a233ebbf0e495228009aac7b872d94c38236cab314f6b7be6b
        A/clauses/window-01/raw.json: b1eb698362b99fa2d09162c1e16a4d0cc331bce64eb66a17037d8c64307c8b15
        A/clauses/window-01/prompt.txt: 557d7a64aed68253d0989c3a826a06a8274b260527436a67a9ac73e7bf5f4bbc
        A/clauses/window-01/meta.json: 5dcc9a798653f93b9dd72af00e5254376971453603893ca8f516c5ce201da71f
        A/clauses/window-06/raw.json: 19d54ae575f6ecf25abb7e65cacf671b68c92505371d9fc390d3c94394fe7702
        A/clauses/window-06/prompt.txt: b1e6b93ca7a7dc07b3544ee6e30b36626dfb2a725b1d56cdc08ffa116e0ade55
        A/clauses/window-06/meta.json: 1626f8b273a79f2068187c0cb62d7e1cc5d1e9cccc1ebd15fc33c8d70ce2a672
        A/clauses/window-08/raw.json: 8767755d78dae80806dd79a7876c12f19aa7a068a8ce689dbfd3923493451525
        A/clauses/window-08/prompt.txt: 6059ebf0e4efc825be5ab2403975dfde9c9f903a7444d48afb551ef532650f87
        A/clauses/window-08/meta.json: c2070da778a5b7ad0241076d09c22ac7d363e9a081c1e36ddacee0802b585f7a
        A/tables/TABLE-3-page-10-3/raw.json: b693dabbf97b3839d3e1b434ee97e5a31476203f85c002fccab1c3c02963d497
        A/tables/TABLE-3-page-10-3/prompt.txt: f0247b3c52dbf8ba335e99958e03021af410d00259904dbfb519488958123ea4
        A/tables/TABLE-3-page-10-3/meta.json: e6ffad70401e202b0ff1561fc419477fa6505e857007da2878e3757c678717b6
        A/tables/TABLE-2-page-10-2/raw.json: bcc7f4d41ec9de0efdb64b024d211994dbc522994736783ab01c8343c0d72868
        A/tables/TABLE-2-page-10-2/prompt.txt: bfaeab1dfc482f8ec2055d65cfc122d6d99624f0b2ffa683e82c2b19a1804d08
        A/tables/TABLE-2-page-10-2/meta.json: 99f21b76ae4ec2e4d1ef69c55813dd2f661be1e5ef79f3452e01ca209052eb92
        A/tables/TABLE-1-page-4-1/raw.json: b15d35bb52b576c21a92b71af35da2c097b158eb759ec674df5b453ad91cd917
        A/tables/TABLE-1-page-4-1/prompt.txt: 5f5202d3f184f8749e4c3bcf525faaa6c4a01cbe0a59017a10bdaec54504e926
        A/tables/TABLE-1-page-4-1/meta.json: c0858cb30ff859bd5c3446722e6d911537a0b67ca2f804b34552626b5e3b1e6f
        A/tables/TABLE-4-page-14-4/raw.json: 2d4cfd15bff4593384de8ad5b85a8fad48684942ddd37f6f42640bdb16f1794f
        A/tables/TABLE-4-page-14-4/prompt.txt: 0068aad2b928f3b47cd2b27c0ca0fc37bbb54816e0e7775b553cc6effaa9f4fb
        A/tables/TABLE-4-page-14-4/meta.json: a223c085d42dcdc142f6c5482fd395361e70c64b7e664237d3eb7717943f2b82
        B/passages.json: efbf25d8e111bd95ef6316315ef0956f84e62dcea08cd7835ee87e9d14d065d1
        B/raw.json: 631b0800c1c05162fe614dbec3a54efa3f3123af0353fd5bce1a8846c958b767
        B/source-units.json: ed9c8906fe315341d0efe7abf45f4e42d1cc17ce74071735927b2212557e9d93
        B/full-source-units.json: cf0c551e91c11889d7f3071372bf95a07de883122b5ac634636917f804ae0388
        B/meta.json: 933043f95b184dd661b5f65f70d8e1e7200718931393d43ab49ff820fa1e2607
        B/table-images/TABLE-3-page-10-2.png: f4c18fb625c12d808a16532d4e871fd618f8c4c16340aa98cad20db81ba62832
        B/table-images/page-14.png: 91497ed01177a3c0eee45d48d8cad1a69684b4b598d9cdfe28be94e02d7d6a0e
        B/table-images/TABLE-4-page-14-1.png: 73bbaa4449ac525b59f412eb0f2132fcd79ea8fe9bd91450829880d4ae3015d1
        B/table-images/page-10.png: 081b11050eda596b5f8f236f985ae454f79da566957b3bbb6f732cf2848b56f4
        B/table-images/page-4.png: 99f71409c0f8debb68eaafbb7be4f4ce6721f6b8fd969ee4513f860739f8b6f5
        B/table-images/TABLE-1-page-4-1.png: 0865af9fff42ab1171a4c723f9f3cddcf53ba8e3ac342778bc66d9a6fd2919ad
        B/table-images/manifest.json: f61e690872794e972c7718c384c8bab462d18c1dd298a6529e13f562ff0556fd
        B/table-images/TABLE-2-page-10-1.png: f4c18fb625c12d808a16532d4e871fd618f8c4c16340aa98cad20db81ba62832
        B/clauses/window-11/raw.json: a34b4ab4cd3edb40ec42ef4abd05ad98ae05b8229ef5f0931abd8ed18c70c93e
        B/clauses/window-11/prompt.txt: 8f36b6f0c2bc2e9f4ae90c8be7490e699a2081ce7db12e0cfd15454db4f17a1c
        B/clauses/window-11/meta.json: 1d642e89077541609a33c5718d3a9a1a2785716e27c1e7eec90ee954f0067918
        B/clauses/window-10/raw.json: 6bd74f7b5e780c1a54816255be56b54394bab5c69b2c41927461dbc25e3be0ed
        B/clauses/window-10/prompt.txt: 69b34e66f3d75548726b45528392f0d7b69744bf2b3c3113a51116d916fb6ee3
        B/clauses/window-10/meta.json: 869da01efebfe12e5a5be67bb4b1b0ff4ba756c317e6853aa4a3affea9bacf78
        B/clauses/window-03/raw.json: d35e84a1a150545cd6c3857ad48cf29ada453f1df313af66a8ee581e6448d6b0
        B/clauses/window-03/prompt.txt: 57fc2fe390776ecdcbff494226d3d2930dc965fd76f416a9b98ad71f1fae9559
        B/clauses/window-03/meta.json: 6926f84abcb0cc7a75a67d233f29a2b71acaff5ab731ea3381a83574663bc276
        B/clauses/window-04/raw.json: 49e9b77c77f1683e671379d011f5409fc0204d2c06ab522c12f8fea086eddd82
        B/clauses/window-04/prompt.txt: 4f6b5f2355c60a678257459397dd1b4902a629950bb3e76dea7e9475bd530ac1
        B/clauses/window-04/meta.json: d1621a1bcca2fbf59507acc95cef69150115e81b63521afe132213ae44114669
        B/clauses/window-05/raw.json: 0b013a4d1122789f52289ecf8d1986784dca6ef6bb97003e4dbffe2bf1b2fa2d
        B/clauses/window-05/prompt.txt: c9c6aeeb8feeee1b204c36ee26563028c67b75a966783ae7ad517e376ee0b102
        B/clauses/window-05/meta.json: ce1f251fc77bb5374a4b506a3e7e7ae7d58e3ea991261c03f4f92d0de1bb851c
        B/clauses/window-02/raw.json: f62c7741930d3e0e7d6f6c17fa13aaf68a1c93622ebf14203a6ad3520362998c
        B/clauses/window-02/prompt.txt: c1166790db75cb2c8e3f3b4b9f4c338669dd75d7e86b37e8528e350e47990607
        B/clauses/window-02/meta.json: 1fbcb657a0e6ed19655974d808ea7a1688698b272d1c97f22fa127060326e9b5
        B/clauses/window-12/raw.json: f46f7b948b7b7a9e963d2adc09cbe91a68e4d86af802aa42fac516f9be7e302d
        B/clauses/window-12/prompt.txt: c3158450e2a9c05ddc5e82d3007bd3e2261c9ce3fc8398a1eb0b29e0fc3b939a
        B/clauses/window-12/meta.json: 0b9cde986ba40683dfec67eef48842c1b502a2b1517a23f3e835dfa20327d8e3
        B/clauses/window-13/raw.json: 7e6083fab2d9561390d71d61a35cc74db0ae2fd4d525372fc88908750b137df2
        B/clauses/window-13/prompt.txt: 59445d0d37b3bafe6337da1c8f7e08f2d0d4235d300e2384e32c0694fa8e5426
        B/clauses/window-13/meta.json: 180b9e844cd47424a4f63becb61e562768fe1ccd0a7bad6bd2955cb7eff384ec
        B/clauses/window-09/raw.json: 59c45a713f54c1172dc1f97d63382b44127460189a7a311866373e69929838b0
        B/clauses/window-09/prompt.txt: 980d1f2d270a1cb84b33f496c866fee6a057e50cf1f05b9f13e8f6366e46814f
        B/clauses/window-09/meta.json: 908fbe8feeeb0b0db0900598981b0cc074e34b305d6616e04548f80e431c96f2
        B/clauses/window-07/raw.json: 95581efa6d9de138b31e7aaf5843597be98f7a94fec0133ee7e3f8f63a755e7f
        B/clauses/window-07/prompt.txt: df8702908c87083bf69e0ca43139b73df49b14bf3ce5345cefae29edd2ce077f
        B/clauses/window-07/meta.json: 0957907172cb897a8e39705effcde525596e23abdb191e5761b95b781718bb5a
        B/clauses/window-01/raw.json: 3a7a011fea9223a26daff1571966eb036cc64001a2972f4f8cb7b28caf6653be
        B/clauses/window-01/prompt.txt: 557d7a64aed68253d0989c3a826a06a8274b260527436a67a9ac73e7bf5f4bbc
        B/clauses/window-01/meta.json: ee79414ecbad73cadaac6a2bfc90b56aa9926ad4bc677105279fcf01dd489c83
        B/clauses/window-06/raw.json: c2d5dd5b6e59240214f0deba2a550f851eeab53d5f17d13f8d751e20dd5ee2d7
        B/clauses/window-06/prompt.txt: b1e6b93ca7a7dc07b3544ee6e30b36626dfb2a725b1d56cdc08ffa116e0ade55
        B/clauses/window-06/meta.json: ec9b835aace29d78e901bf8b94e70aff5a7ffe3a03472ab18a529d1a69b7c992
        B/clauses/window-08/raw.json: 2d22883e307a36e1e8399a10b79f63dac5e4110f1cd05f09554048cb009db02b
        B/clauses/window-08/prompt.txt: 6059ebf0e4efc825be5ab2403975dfde9c9f903a7444d48afb551ef532650f87
        B/clauses/window-08/meta.json: 3114830d444861bebc548df6f058c9c440dc22c4831fdf5f72d9aabd074faa89
        B/tables/TABLE-3-page-10-3/raw.json: afe588b58a97f89678a0dc702467e8c92b09951faef85ac94f594d20eddfd204
        B/tables/TABLE-3-page-10-3/prompt.txt: f0247b3c52dbf8ba335e99958e03021af410d00259904dbfb519488958123ea4
        B/tables/TABLE-3-page-10-3/meta.json: 3ee9be0000cb1186e01a04fe514f00a4855abe6f5f8da4a63c87181367f1c89d
        B/tables/TABLE-2-page-10-2/raw.json: fcf8e99cae5b5d7ae3becde869a5d47e5ece418042a6f06d74e602cdfcb99d87
        B/tables/TABLE-2-page-10-2/prompt.txt: bfaeab1dfc482f8ec2055d65cfc122d6d99624f0b2ffa683e82c2b19a1804d08
        B/tables/TABLE-2-page-10-2/meta.json: 0bf842567af212be7504d0274806032ae316116df62c9a59ff5e4f40b94eb606
        B/tables/TABLE-1-page-4-1/raw.json: 918492b7f4738c1c825be8ecebdb05cfcff63874269dcb809efbb106031c1ca1
        B/tables/TABLE-1-page-4-1/prompt.txt: 5f5202d3f184f8749e4c3bcf525faaa6c4a01cbe0a59017a10bdaec54504e926
        B/tables/TABLE-1-page-4-1/meta.json: 16c642e0d4519aac7cf59c53ccafa268a020944abf1ea383f8ff55847a000ab8
        B/tables/TABLE-4-page-14-4/raw.json: 12b53289c86dee9bc1bf8f07304c7daf009802b8feda5ea8a73fa6a88541106f
        B/tables/TABLE-4-page-14-4/prompt.txt: 0068aad2b928f3b47cd2b27c0ca0fc37bbb54816e0e7775b553cc6effaa9f4fb
        B/tables/TABLE-4-page-14-4/meta.json: a3ead9c6dda617eab438562cff8174d64240e4b13e4948341a82f706a1c36061
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
      pdf_sha256: 153707f62f0c4a223cb76cd9205efb5ad7a3776b097854fdcdce6007ec0f9c98
      source_review: _compare/relationships-2026-11-16/review-current/Kasdan2025
      source_status_sha256: 001ade5867bbfd1a9b311dbd516916ce69b34b934d33222b0695959377b25d1d
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R001
    exposure:
      text: post-stroke aphasia
    outcome:
      text: tapping performance
    analysis_label: Group comparison of rhythm production
    relation: association
    evidence_ids:
    - P11-S1-C3
    qualifier_ids:
    - P10-S1-C13
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 153707f62f0c4a223cb76cd9205efb5ad7a3776b097854fdcdce6007ec0f9c98
      source_review: _compare/relationships-2026-11-16/review-current/Kasdan2025
      source_status_sha256: 001ade5867bbfd1a9b311dbd516916ce69b34b934d33222b0695959377b25d1d
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P1-S1-C11
      - Accounting without a linked unit P1-S1-C12
      - Result passage disposed without unit P1-S1-C13
      - Accounting without a linked unit P1-S1-C14
      - Unaccounted source passage P1-S1-C14
      - Unaccounted source passage P1-S1-C12
      - Accounting without a linked unit P6-S1-C16
      - Unaccounted source passage P6-S1-C16
      - Accounting without a linked unit P11-S1-C2
      - Unaccounted source passage P11-S1-C2
      - Result passage disposed without unit P12-S1-C10
      - Result passage disposed without unit P12-S1-C9
      - Result passage disposed without unit P14-S1-C3
      - Accounting without a linked unit P14-S1-C4
      - Accounting without a linked unit P14-S1-C7
      - Accounting without a linked unit P14-S1-C8
      - Accounting without a linked unit P15-S1-C1
      - Accounting without a linked unit P15-S1-C2
      - Unaccounted source passage P14-S1-C4
      - Unaccounted source passage P15-S1-C2
      - Unaccounted source passage P14-S1-C7
      - Unaccounted source passage P14-S1-C8
      - Unaccounted source passage P15-S1-C1
      - Result passage disposed without unit P15-S1-C14
      - Result passage disposed without unit P15-S1-C7
      - Result passage disposed without unit P15-S1-C9
      - Result passage disposed without unit P16-S1-C1
      - Result passage disposed without unit P16-S1-C10
      - Accounting without a linked unit P16-S1-C12
      - Accounting without a linked unit P16-S1-C2
      - Accounting without a linked unit P16-S1-C3
      - Result passage disposed without unit P16-S1-C7
      - Accounting without a linked unit P16-S1-C9
      - Unaccounted source passage P16-S1-C2
      - Unaccounted source passage P16-S1-C9
      - Unaccounted source passage P16-S1-C3
      - Unaccounted source passage P16-S1-C12
      - Result passage disposed without unit P16-S2-C3
      - Accounting without a linked unit P16-S2-C4
      - Result passage disposed without unit P17-S1-C5
      - Result passage disposed without unit P17-S1-C7
      - Accounting without a linked unit P17-S1-C8
      - Unaccounted source passage P17-S1-C8
      - Unaccounted source passage P16-S2-C4
      - Accounting without a linked unit P17-S2-C3
      - Accounting without a linked unit P18-S1-C1
      - Accounting without a linked unit P18-S1-C10
      - Accounting without a linked unit P18-S1-C11
      - Accounting without a linked unit P18-S1-C6
      - Unaccounted source passage P18-S1-C1
      - Unaccounted source passage P17-S2-C3
      - Unaccounted source passage P18-S1-C10
      - Unaccounted source passage P18-S1-C6
      - Unaccounted source passage P18-S1-C11
      - Accounting without a linked unit P18-S2-C5
      - Accounting without a linked unit P19-S1-C11
      - Accounting without a linked unit P19-S2-C3
      - Accounting without a linked unit P19-S2-C6
      - Unaccounted source passage P19-S1-C11
      - Unaccounted source passage P18-S2-C5
      - Unaccounted source passage P19-S2-C6
      - Unaccounted source passage P19-S2-C3
      unattached_null_or_qualifier_ids:
      - P9-S1-C5
      - P11-S1-C2
      - P14-S1-C3
      - P15-S1-C6
      - P17-S1-C7
      - P17-S1-C8
      - P18-S1-C11
      suppressed_nonrepresented_units: 22
      default_disposition_count_requires_completeness_check: 310
      unselected_timing_passages:
      - P1-S1-C10
      - P3-S2-C6
      - P3-S2-C7
      - P3-S2-C8
      - P8-S1-C1
      - P15-S1-C13
      - P16-S1-C4
      - P18-S2-C7
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P14-S1-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P14-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P14-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P15-S1-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P15-S1-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P17-S2-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P10-S1-C6
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: limitations
        source_ids:
        - P18-S2-C3
        - P18-S2-C4
        - P18-S2-C5
        - P18-S2-C7
        - P18-S2-C8
        - P18-S2-C9
        - P19-S1-C2
        - P19-S1-C3
        - P19-S1-C4
        - P19-S1-C5
        - P19-S1-C6
        - P19-S1-C7
        - P19-S1-C8
        - P19-S1-C9
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - validation
      - limitations
      unclassified_extraction_ids:
      - P2-S1-C11
      - P2-S3-C1
      - P2-S3-C2
      - P2-S3-C3
      - P2-S3-C4
      table_review_required:
      - TABLE-1-page-4-1
      - TABLE-2-page-10-2
      - TABLE-3-page-10-3
      - TABLE-4-page-14-4
      unlinked_tables:
      - TABLE-1-page-4-1
      - TABLE-2-page-10-2
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P11-S1
        - P12-S1
        - P12-S2
        - P13-S1
        - P14-S1
        - P15-S1
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 153707f62f0c4a223cb76cd9205efb5ad7a3776b097854fdcdce6007ec0f9c98
      source_review: _compare/relationships-2026-11-16/review-current/Kasdan2025
      source_status_sha256: 001ade5867bbfd1a9b311dbd516916ce69b34b934d33222b0695959377b25d1d
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C11
      disposition: represented
      result_indexes:
      - 0
      reason: Abstract statement of individual variability in tapping.
    - source_id: P1-S1-C12
      disposition: represented
      result_indexes:
      - 6
      reason: Abstract statement of LSM results for tapping.
    - source_id: P1-S1-C13
      disposition: repeated
      result_indexes:
      - 6
      reason: Restatement of LSM finding.
    - source_id: P1-S1-C14
      disposition: represented
      result_indexes:
      - 10
      reason: Abstract statement of tapping and language production association.
    - source_id: P5-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes a single control participant's tapping hand.
    - source_id: P6-S1-C16
      disposition: background_or_descriptive
      result_indexes: []
      reason: Validation of MES against GMSI in controls.
    - source_id: P8-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Rationale for using circular statistics.
    - source_id: P8-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of automatic onset detection.
    - source_id: P8-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of manual onset detection.
    - source_id: P8-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statistical test on manual modifications of data.
    - source_id: P9-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Correlation between repetitions of music clips.
    - source_id: P9-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Data averaging procedure.
    - source_id: P9-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: PCA variance/loadings result.
    - source_id: P10-S1-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Whole-model predictive performance (R2, F, p).
    - source_id: P11-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison of MES Total score between groups.
    - source_id: P11-S1-C3
      disposition: represented
      result_indexes:
      - 0
      reason: Direct result of tapping group difference.
    - source_id: P11-S1-C4
      disposition: represented
      result_indexes:
      - 2
      reason: Direct result of musical training on tapping.
    - source_id: P11-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation of variability.
    - source_id: P12-S1-C1
      disposition: represented
      result_indexes:
      - 1
      reason: Direct result of beat perception group difference.
    - source_id: P12-S1-C2
      disposition: represented
      result_indexes:
      - 3
      reason: Direct result of musical training on beat perception.
    - source_id: P12-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Null finding for demographics and beat perception.
    - source_id: P12-S1-C6
      disposition: represented
      result_indexes:
      - 4
      reason: Correlation between production and perception in full sample.
    - source_id: P12-S1-C7
      disposition: represented
      result_indexes:
      - 4
      reason: Correlation between production and perception in aphasia and controls.
    - source_id: P12-S1-C8
      disposition: represented
      result_indexes:
      - 4
      reason: Sensitivity result after removing outlier.
    - source_id: P12-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Count of impaired tappers.
    - source_id: P12-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Count of impaired perceivers.
    - source_id: P12-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of lesion distribution.
    - source_id: P14-S1-C1
      disposition: represented
      result_indexes:
      - 6
      reason: Direct result of VLSM for tapping.
    - source_id: P14-S1-C2
      disposition: represented
      result_indexes:
      - 7
      reason: Correlation between ROI damage and tapping.
    - source_id: P14-S1-C3
      disposition: repeated
      result_indexes:
      - 7
      reason: Qualification of the ROI correlation.
    - source_id: P14-S1-C4
      disposition: represented
      result_indexes:
      - 8
      - 9
      reason: Correlations of tapping and beat perception with aphasia severity.
    - source_id: P14-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to Table S3.
    - source_id: P14-S1-C7
      disposition: represented
      result_indexes:
      - 10
      reason: Correlations of tapping with language production.
    - source_id: P14-S1-C8
      disposition: represented
      result_indexes:
      - 10
      reason: Correlations of tapping with repetition, reading, and comprehension.
    - source_id: P15-S1-C1
      disposition: represented
      result_indexes:
      - 10
      reason: Null correlations of tapping with motor speech.
    - source_id: P15-S1-C2
      disposition: repeated
      result_indexes:
      - 10
      reason: Qualification of sentence comprehension correlation.
    - source_id: P15-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to BAT results in supplement.
    - source_id: P15-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Count of limb apraxia.
    - source_id: P15-S1-C8
      disposition: represented
      result_indexes:
      - 11
      - 12
      reason: Association of limb apraxia and motor strength with tapping.
    - source_id: P15-S1-C10
      disposition: represented
      result_indexes:
      - 13
      reason: Null effect of motor variables on beat perception.
    - source_id: P15-S1-C12
      disposition: represented
      result_indexes:
      - 14
      reason: Null effect of stroke covariates on rhythm.
    - source_id: P16-S1-C1
      disposition: repeated
      result_indexes:
      - 6
      reason: Discussion restatement of LSM.
    - source_id: P16-S1-C2
      disposition: repeated
      result_indexes:
      - 6
      reason: Discussion restatement of LSM.
    - source_id: P16-S1-C3
      disposition: repeated
      result_indexes:
      - 10
      reason: Discussion restatement of language production association.
    - source_id: P16-S2-C3
      disposition: repeated
      result_indexes:
      - 4
      reason: Discussion restatement of production/perception correlation.
    - source_id: P16-S2-C4
      disposition: repeated
      result_indexes:
      - 6
      reason: Discussion restatement of LSM.
    - source_id: P17-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of cluster location relative to comprehension regions.
    - source_id: P17-S1-C7
      disposition: repeated
      result_indexes:
      - 10
      reason: Discussion restatement of comprehension null result.
    - source_id: P17-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Null finding for basal ganglia damage.
    - source_id: P17-S2-C3
      disposition: repeated
      result_indexes:
      - 10
      reason: Discussion restatement of language production association.
    - source_id: P18-S1-C1
      disposition: repeated
      result_indexes:
      - 10
      reason: Discussion restatement of AOS null result.
    - source_id: P18-S1-C6
      disposition: repeated
      result_indexes:
      - 2
      - 3
      reason: Discussion restatement of musical training effects.
    - source_id: P18-S1-C10
      disposition: repeated
      result_indexes:
      - 11
      reason: Discussion restatement of limb apraxia association.
    - source_id: P19-S2-C3
      disposition: repeated
      result_indexes:
      - 6
      reason: Discussion restatement of posterior temporoparietal region.
    unresolved_coverage:
    - source_id: P15-S1-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P15-S1-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P15-S1-C14
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P16-S1-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P16-S1-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P16-S1-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P16-S1-C12
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P18-S1-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P18-S2-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P19-S1-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P19-S2-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C11
    - P1-S1-C12
    - P1-S1-C13
    - P1-S1-C14
    - P5-S1-C1
    - P6-S1-C16
    - P8-S1-C10
    - P8-S2-C5
    - P8-S2-C6
    - P8-S2-C8
    - P9-S1-C4
    - P9-S1-C5
    - P9-S1-C6
    - P10-S1-C14
    - P11-S1-C2
    - P11-S1-C5
    - P12-S1-C3
    - P12-S1-C8
    - P12-S1-C9
    - P12-S1-C10
    - P12-S2-C2
    - P14-S1-C3
    - P14-S1-C6
    - P15-S1-C2
    - P15-S1-C5
    - P15-S1-C6
    - P15-S1-C7
    - P15-S1-C9
    - P15-S1-C14
    - P16-S1-C1
    - P16-S1-C2
    - P16-S1-C3
    - P16-S1-C7
    - P16-S1-C9
    - P16-S1-C10
    - P16-S1-C12
    - P16-S2-C3
    - P16-S2-C4
    - P17-S1-C5
    - P17-S1-C7
    - P17-S1-C8
    - P17-S2-C3
    - P18-S1-C1
    - P18-S1-C6
    - P18-S1-C10
    - P18-S1-C11
    - P18-S2-C5
    - P19-S1-C11
    - P19-S2-C3
    - P19-S2-C6
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-4-1
    - TABLE-2-page-10-2
    - TABLE-3-page-10-3
    - TABLE-4-page-14-4
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P3-S2-C6
      - P4-S1-C16
      recruited_sample:
      - P3-S2-C6
      - P3-S2-C11
      - P4-S1-C3
      - P4-S1-C4
      eligibility:
      - P3-S2-C7
      - P3-S2-C8
      - P3-S2-C10
      imaging_provenance:
      - P7-S2-C8
      - P8-S1-C4
      imaging_timing:
      - P8-S1-C2
      outcome_timing:
      - P8-S1-C2
      outcome_definition:
      - P9-S2-C10
      - P10-S1-C10
      validation: []
      analysis_restrictions:
      - P14-S1-C5
      dependent_variable_statement:
      - P10-S1-C6
      limitations: []
      personal_factors:
      - P6-S1-C8
      - P6-S1-C11
      - P6-S1-C14
      - P10-S1-C13
      - P15-S1-C8
      - P18-S1-C6
      - P18-S1-C10
      tested_personal_effects:
      - P11-S1-C4
      - P12-S1-C2
      - P15-S1-C8
      - P18-S1-C6
      adjustment_roles:
      - P10-S1-C7
      explicitly_not_adjusted:
      - P14-S1-C5
      descriptive_personal_factors:
      - P4-S1-C16
      - P4-S2-C1
    outcome_type: status_at_assessment
    imaging_vs_outcome: mixed
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P14-S1-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P14-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P14-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P15-S1-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P15-S1-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P17-S2-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P10-S1-C6
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: limitations
      source_ids:
      - P18-S2-C3
      - P18-S2-C4
      - P18-S2-C5
      - P18-S2-C7
      - P18-S2-C8
      - P18-S2-C9
      - P19-S1-C2
      - P19-S1-C3
      - P19-S1-C4
      - P19-S1-C5
      - P19-S1-C6
      - P19-S1-C7
      - P19-S1-C8
      - P19-S1-C9
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
      pdf_sha256: 153707f62f0c4a223cb76cd9205efb5ad7a3776b097854fdcdce6007ec0f9c98
      review_sha256: d7ffc5bd3ea54f538fa848f4f144fa0e4a72665d2948fba8700a261e2a7af1b1
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
      - P11-S1-C3
      source_result: Individuals with chronic, post-stroke aphasia performed significantly
        below the level of neurotypical controls on tapping (β = 19.98, p = 0.0030,
        Δr2 = 12.7%, f2 = 0.18). Demographic factors were not significantly associated
        with tapping.
      result_status: detected
      patient_measurement: non_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis is a group comparison of tapping performance
            between individuals with aphasia and controls. The source P11-S1-C3 explicitly
            reports this comparison with a significant result. The proposed core correctly
            identifies this as the primary group comparison for the tapping outcome.
          source_ids:
          - P11-S1-C3
          - P10-S1-C2
        direction:
          answer: fits
          reason: The source states individuals with aphasia performed 'below the
            level of controls'. The proposed core claim states they 'performed significantly
            below the level of neurotypical controls'. The direction is preserved.
          source_ids:
          - P11-S1-C3
        construct:
          answer: fits
          reason: The exposure is post-stroke aphasia (group status) and the outcome
            is tapping performance. The source confirms the population is chronic
            post-stroke aphasia (P3-S2-C8) and the outcome is tapping (P11-S1-C3).
            The patient measurement is behavioral tapping (non_imaging), not diffusion
            or lesion overlap, which are used for other analyses (LSM) in the paper
            but not for this specific group comparison result.
          source_ids:
          - P11-S1-C3
          - P3-S2-C8
          - P9-S1-C7
        qualifications:
          answer: fits
          reason: The proposed core includes the qualification that tapping was performed
            with the left hand for consistency due to right-sided weakness (P4-S1-C14).
            This is a material methodological detail affecting the measurement. The
            core also notes the chronic timing (P3-S2-C8). No material qualifiers
            are lost.
          source_ids:
          - P4-S1-C14
          - P3-S2-C8
        missing_material_caveat:
          answer: fits
          reason: The core captures the main finding and relevant methodological constraints.
            The limitation regarding variability is included. No material caveats
            that change the interpretation of the group difference are omitted.
          source_ids:
          - P11-S1-C5
          - P11-S1-C3
      optional_pending:
      - Sample size (n=33 aphasia, n=29 controls) is available in P3-S2-C6 and P1-S1-C10
        but not transcribed in the core fields; confirm if required for final schema.
      - Specific statistical values (beta, p-value, effect size) are not transcribed
        in the core claim text, consistent with qualitative draft status.
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Sample size requires source confirmation; it has not been transcribed.
    - 'sample.population: source confirmation required; original proposed wording
      remains in the audit.'
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Sample size (n=33 aphasia, n=29 controls) is available in P3-S2-C6 and P1-S1-C10
      but not transcribed in the core fields; confirm if required for final schema.
    - Specific statistical values (beta, p-value, effect size) are not transcribed
      in the core claim text, consistent with qualitative draft status.
    normalizations:
    - field: sample.n
      original: 62
      action: not_transcribed
      reason: Not supported by selected quotations
    - field: sample.population
      original: Individuals with chronic, post-stroke aphasia (n=33) and matched neurotypical
        controls (n=29), aged 18-90 years, with strokes confined mostly to left hemisphere
        supratentorial regions.
      action: not_transcribed
      reason: 'Numbers not grounded in usable selected source readings: 18, 33, 9E+1'
    analysis_identity:
      id: R001
      exposure:
        text: post-stroke aphasia
      outcome:
        text: tapping performance
      analysis_label: Group comparison of rhythm production
      relation: association
      evidence_ids:
      - P11-S1-C3
      qualifier_ids:
      - P10-S1-C13
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 153707f62f0c4a223cb76cd9205efb5ad7a3776b097854fdcdce6007ec0f9c98
        source_review: _compare/relationships-2026-11-16/review-current/Kasdan2025
        source_status_sha256: 001ade5867bbfd1a9b311dbd516916ce69b34b934d33222b0695959377b25d1d
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P3-S2-C6:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 153707f62f0c4a223cb76cd9205efb5ad7a3776b097854fdcdce6007ec0f9c98
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: c0cfed9644ab4a8de28b90bb729856ed59a24187132e1c9e77f1603b606c7c29
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S2-C6
          page: 3
          text_layer_sha256: c0cfed9644ab4a8de28b90bb729856ed59a24187132e1c9e77f1603b606c7c29
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'MATERIALS AND METHODS

          Participants

          Thirty-three individuals with chronic, post-stroke aphasia and 29 neurotypical
          controls, matched

          on age and education level, successfully completed the research protocol.'
        anchor_text: 'MATERIALS AND METHODS

          Participants

          Thirty-three individuals with chronic, post-stroke aphasia and 29 neurotypical
          controls, matched

          on age and education level, successfully completed the research protocol.'
        excluded_fragments: []
        image_sha256: 2f8a6f9cc4b85656a090491bd7651ed64f04443c2106235939520a1567f19d4d
        transcription: 'MATERIALS AND METHODS


          Participants


          Thirty-three individuals with chronic, post-stroke aphasia and 29 neurotypical
          controls, matched on age and education level, successfully completed the
          research protocol'
      P3-S2-C8:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 153707f62f0c4a223cb76cd9205efb5ad7a3776b097854fdcdce6007ec0f9c98
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: a99e43ffa69d5ebe2bf8780a33125db4502333dfc33f447c5a287d1639be457a
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S2-C8
          page: 3
          text_layer_sha256: a99e43ffa69d5ebe2bf8780a33125db4502333dfc33f447c5a287d1639be457a
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'We recruited indi-

          viduals with aphasia who had aphasia due to ischemic or hemorrhagic stroke
          confined mostly to

          left hemisphere supratentorial regions (Wilson et al., 2023) and were in
          the chronic stage of

          recovery (approximately 1 yr or more post-stroke).'
        anchor_text: 'We recruited indi-

          viduals with aphasia who had aphasia due to ischemic or hemorrhagic stroke
          confined mostly to

          left hemisphere supratentorial regions (Wilson et al., 2023) and were in
          the chronic stage of

          recovery (approximately 1 yr or more post-stroke).'
        excluded_fragments: []
        image_sha256: 64f6f604634065b63ee207f7a33012c5cf12caaedfc8e14ac53eb590d5b4b173
        transcription: '. We recruited indi-

          viduals with aphasia who had aphasia due to ischemic or hemorrhagic stroke
          confined mostly to

          left hemisphere supratentorial regions (Wilson et al., 2023) and were in
          the chronic stage of

          recovery (approximately 1 yr or more post-stroke)'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 11
  quote: 'Individuals with aphasia performed below the level of controls on tapping
    (β = 19.98, p =

    0.0030, Δr2 = 12.7%, f 2 = 0.18) and demographic factors were not significantly
    associated with

    tapping (Table 3).'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-24'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
