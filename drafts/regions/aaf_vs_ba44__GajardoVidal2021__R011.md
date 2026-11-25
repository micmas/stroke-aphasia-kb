---
id: aaf_vs_ba44
name: aAF versus BA44 cluster
kind: network
findings:
- id: f1
  target_audit:
    status: behaviour_label_present
    category: behaviour_or_language_construct
    original_target: speech_production_ability
    reason: Label names a behaviour or language construct; its exact operational definition and measurement
      still need source review.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  outcome_measurement:
    status: identified
    instruments:
    - name: Comprehensive Aphasia Test
      subtest: Spoken picture description
    metric: Spoken picture description score; subcomponent contrasts and covariates retained in claim
    definition_source:
      citation: '@GajardoVidal2021'
      page: 1
      quote: 'Spoken picture description scores from the Comprehensive

        Aphasia Test were used as the outcome measure.'
      basis: Published source passage
    note: Measurement metadata identified from source evidence; finding remains unapproved.
  target: speech_production_ability
  target_kind: impairment
  claim: Patients with damage to the anterior arcuate fasciculus (aAF) performed significantly
    worse on the spoken picture description task than patients with damage to Brodmann
    area 44 (BA44), with poorer performance reflected in appropriate information carrying
    words, syntactic variety, grammatical well-formedness, and speed of speech production.
  direction: likely
  relationship: correlational
  method: LSM
  sample:
    n: not_reported
    population: Stroke survivors with unilateral left frontal lobe lesions sparing
      posterior speech production areas
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
  - Small sample size for post hoc group comparisons
  - Pairwise comparisons used Fisher's LSD method which does not control the family-wise
    error rate
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Patient lesion overlap with population-based atlas
    templates for the anterior segment of the arcuate fasciculus (aAF) and Brodmann
    area 44 (BA44), with groups matched for total lesion volume. Analysis used matched
    groups: 7 patients in the BA44 group and 7 patients in the aAF group; Groups were
    matched for total lesion volume (range and mean); Results remained significant
    after covarying out lesion load in the superior central insula and putamen. Additional
    metadata has not been transcribed; review the pending-field flags before approval.
    PDF image reading (P7-S4-C4, two-model agreement, human verification pending):
    . In total, there were

    seven, seven and eight patients who were matched for total le-

    sion volume (range and mean) in the BA44, aAF, and

    BA44+aAF groups, respectively Original text-layer quotation is preserved below.
    PDF image reading (P4-S2-C2, two-model agreement, human verification pending):
    . Inclusion criteria were:

    (i) aged over 18 years; (ii) no history of neurological or psychi-

    atric illness (other than stroke); (iii) native speaker of English;

    (iv) right handed pre-morbidly; (v) at least 3 months post-stroke

    (to allow enough time for spontaneous functional reorganization

    to occur); and (vi) <10 years since stroke onset (to control for

    longer term changes related to cognitive decline) Original text-layer quotation
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
    - not_transcribed:sample.time_post_onset
    - proposed_concept:speech_production_ability
  citation: '@GajardoVidal2021'
  source_passages:
  - section: Original source P9-S1-C9
    page: 9
    quote: 'A

      Fisher’s LSD post hoc test showed that this occurred because

      the aAF group performed significantly worse than the BA44

      group on the spoken picture description task [mean ± stand-

      ard

      deviation

      (SD)

      =

      55.4 ± 5.7

      versus

      62.9 ± 4.1;

      P = 0.013], with no significant differences between the aAF

      group, and the BA44 + aAF group (mean ± SD = 55.4 ± 5.7

      versus 55.5 ± 5.3; P = 0.979).'
    supports: claim
  - section: Original source P9-S2-C1
    page: 9
    quote: 'aggregated speech production scores, we observed that the

      speech output for the aAF group was poorer both in terms

      of quality and quantity than that for the BA44 group as

      reflected in their appropriate information carrying words

      [mean = 19.0 versus 28.0, t(12) = 1.97, P = 0.036 one-

      tailed], syntactic variety (mean = 3.4 versus 5.3, U = 6.5,

      P = 0.009 one-tailed), grammatical well-formedness (mean =

      3.6 versus 5.1, U = 11.5, P = 0.049 one-tailed), and speed of

      speech

      production

      (mean

      =

      1.6

      versus

      2.4,

      U = 8.0,

      P = 0.019 one-tailed) ratings.'
    supports: claim
  - section: Original source P7-S4-C4
    page: 7
    quote: 'In total, there were

      seven, seven and eight patients who were matched for total le-

      sion volume (range and mean) in the BA44, aAF, and

      BA44 + aAF groups, respectively.'
    supports: sample
  - section: Original source P4-S2-C2
    page: 4
    quote: 'Inclusion criteria were:

      (i) aged over 18 years; (ii) no history of neurological or psychi-

      atric illness (other than stroke); (iii) native speaker of English;

      (iv) right handed pre-morbidly; (v) at least 3 months post-stroke

      (to allow enough time for spontaneous functional reorganization

      to occur); and (vi) 510 years since stroke onset (to control for

      longer term changes related to cognitive decline).'
    supports: method
  - section: Original source P9-S1-C10
    page: 9
    quote: 'Critically, these results did not

      change after covarying out inter-patient differences in lesion

      load in the superior central insula and putamen, which were

      concurrently damaged in some of the patients from the aAF

      group (Fig. 3 and Table 5).'
    supports: confounders
  - section: Original source P8-S1-C5
    page: 8
    quote: 'Given the small number of patients in each group, pairwise

      comparisons were conducted using Fisher’s least significant dif-

      ference (LSD) method, which does not control the family-wise

      error rate.'
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-24'
relationship_review:
  paper: GajardoVidal2021
  proposal_id: R011
  review_status_sha256: 4b76f5c50cba7fc43c14744d0739463d1a4f2b445692ef436a9758b2615d6603
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: bc4a512d9f277c1330ee6db4299bd3190253a191e5b40dcf142ad2fdbe12a5f8
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: bc4a512d9f277c1330ee6db4299bd3190253a191e5b40dcf142ad2fdbe12a5f8
        A/passages.json: 1b455d099b94dfbf7c6a2fbf56055ca88cdaadd9dc567cf275a3752d1fb493b0
        A/raw.json: f2a0698f683f1d84a4ca79cd900df5baa5093ffd18b21fbcd69dbef1b699aac6
        A/source-units.json: 1e0c291b434e573dea9045db3c1bab87adcb5423a8983faf43942c6c4a9bc73a
        A/full-source-units.json: 71ebc5888b5ff41194af70d4046ddbe856dbdcfda7d8d91f0814f4af394ee3f4
        A/meta.json: c560efc97eeee52e791e7d4923fa83f4a4c0d9fffa75e764abb32caf467be2ef
        A/table-images/TABLE-4-page-9-1.png: 9689dd53c4ffe110991bbcbe23fe07d6c4e658e97ba58443c86baf98d7392a56
        A/table-images/page-10.png: c26507fe488b437055f8922f61a699ae595414c7f77052cc5bebc2bd67deb36f
        A/table-images/TABLE-3-page-8-1.png: 6447a9abecd0cb4e10bd160fd06313702b3a8216c83441b60efc398a08312618
        A/table-images/page-5.png: cf9f8af1a79c063e87ab4dade63efd3dade6fb0ad553007cab969484ac19adf2
        A/table-images/page-4.png: ac3ab2dfb5816ae065b02588b27c89c2f5b35f8fd5709713feb55cc53c41c980
        A/table-images/TABLE-1-page-4-1.png: c5a5d9afb580f860c52e478c57a62ff20fd0395a32465ee77e536ad9024afead
        A/table-images/page-9.png: 3b8255111985ada63f1bd8c1e442682c4aa2ad605f50109f7ea2eea6d3b30470
        A/table-images/page-8.png: 6cb50deb7e728354ef099e4c80c283d18d9c5ef4ec15d1b227ce30fdc460cdf7
        A/table-images/manifest.json: d1f77843e537c59a2819e53b48e6af974cfc0b40a714e668acfc01f56401d1b9
        A/table-images/TABLE-5-page-10-1.png: d18e2ac403f04c5c41a33587f34711c71358899030c1eda1bf40cc4cee9b0af6
        A/table-images/TABLE-2-page-5-1.png: c37bc1a3e5164d3a890438dae07122a572a9d835a1199254f3732d7ef18dac11
        A/clauses/window-10/raw.json: d7a91f72f8dde16244f7729348c947a0cb84a54330fefac0fc0e6584ab3174c1
        A/clauses/window-10/prompt.txt: 4e1c37464d73d45d7fd7d5b65c2941d374a57fcb50ee4dd58a02592c7a2d18be
        A/clauses/window-10/meta.json: ebba937e8d27e9698a2409a13b2713ab99e86d804831e393962344d96b8ca930
        A/clauses/window-03/raw.json: 3dedb02c4a4280f9e6a08143171fa343d0c1e469009832887711eb7946fe7c37
        A/clauses/window-03/prompt.txt: 307044463f852e440308cf086dd46971fbc6d8662a2ed4334690e252460cedb4
        A/clauses/window-03/meta.json: 02df1031c3cb5e82c8485311684f6fca2b518815f847e10c103048f596533280
        A/clauses/window-04/raw.json: 9a66577b1508c55b95bed5822a45f984923295a55c69eb9ad7f4eb78ac19e5d3
        A/clauses/window-04/prompt.txt: b1fb2c90dc1afea278b415d1d08ff1d263033cbf991acb2b916d77ea2fbdd3cc
        A/clauses/window-04/meta.json: e08021a64ae47843fac84bbecbd9513ba5b43405761ba6db350f0ae239dfec99
        A/clauses/window-05/raw.json: 9115c860d865cbcb0ca774d351508d721ffee71badbdc7ece31dc290e6570adb
        A/clauses/window-05/prompt.txt: a4e9d502410c5a1b4cb845a02face721e20c3bc01c920c62419bacecc96e3b9a
        A/clauses/window-05/meta.json: 11d0fdbff499fba76697f5ca12c21c3ed88246fee90b515c18cb97d0c2f76e7f
        A/clauses/window-02/raw.json: 30f3ba6dca13e87eab7c6a261ee5f843a353027b280ac0cc4be56c581764d867
        A/clauses/window-02/prompt.txt: 4b2506a815d77da4c45673b8b50e2b8677e1c86a46c12f36576f3a225d59f4e7
        A/clauses/window-02/meta.json: 8028b291fe96d4d0eab402b89e1c45170627e6ff7c7b2be3490befa9e64ee01c
        A/clauses/window-09/raw.json: dbf51863956dd901dda51ec8627025acc02f2cc80d4fe24cdf998e15a75c3b1e
        A/clauses/window-09/prompt.txt: bae263d828af3c8479f7c6b736084b3c39edccd4d36f85a044ec4e8a34917a40
        A/clauses/window-09/meta.json: 1aec33d355073672922584ca0ec28587a2bf45bfed4e80e713505b3423f02731
        A/clauses/window-07/raw.json: cb09a4654521178e8bc990b15813e610604e4503e4a50a39eb09c475afca6196
        A/clauses/window-07/prompt.txt: add6466ff551fd09c03d62b24a3ffd597cccd6eb9756f4f6c2b93eba8a512ab2
        A/clauses/window-07/meta.json: 481a8d651e3fafa4105772000d5b82bc7d6fc40cc16d2a6f3a558e339a219d5e
        A/clauses/window-01/raw.json: 4511b35391e76a50a7eb42345c9bf4f85d22eab990112659741263e06c3d3a0d
        A/clauses/window-01/prompt.txt: 243aa04f124197bfb55a27767fdc31db3310a56592da7e0b944bcd119f118729
        A/clauses/window-01/meta.json: e82ea9d93bb2fcd87fa39a34e99a818988af466c2fe1f0b74914aa70a4062d9e
        A/clauses/window-06/raw.json: 30d37e06b79bcd30ea2d4d53771b9ceca186c9ed23721133cb4f30a5ec917451
        A/clauses/window-06/prompt.txt: 84699ccdc3c0e73ef6baa9146adfab2736ff76ef1fdfe8e75b69ce4d954b751d
        A/clauses/window-06/meta.json: 313d2d9b1cabd79422a763bbea69773884b88ddda5d74b784917f784f86e1882
        A/clauses/window-08/raw.json: f0aa925b2be86eb4c3684527fb518048bd45b5b5c6f8efa858a2b7efe956c229
        A/clauses/window-08/prompt.txt: b60e37bc995274528d8f06a28ccfa705fb9a5be64912ad7073bb5c289c6345f8
        A/clauses/window-08/meta.json: 2d613d3870976e875a5ec9df027e2e2b75bd6035a6a727781cb7f3f4562ac192
        A/tables/TABLE-2-page-5-2/raw.json: 1365142847634f843a7cba1b083e2568790414dd77d653cff137c6efdb3f6347
        A/tables/TABLE-2-page-5-2/prompt.txt: 4247c5c2f499e096ee0d02c862f45be6026d651a3c66ed56a5b9bfaf6b397f7b
        A/tables/TABLE-2-page-5-2/meta.json: 924b25dbd92e24cee6b7d1a01660b481a5fd57d17908e4aa107b3b80a1822d80
        A/tables/TABLE-3-page-8-3/raw.json: cf61237903d3587d0e21aa9ad9cc03d802bd27db53d9c88bc929c64be2265ef5
        A/tables/TABLE-3-page-8-3/prompt.txt: e52613d8ef5a0ce49609c567f2ec46f9d2ecef323b136653a3f57a0b57d2d52d
        A/tables/TABLE-3-page-8-3/meta.json: 2df6db0bf67fed8ba84271aac3fbc2fe05f125c94852d4c8f3b303b4e28682e4
        A/tables/TABLE-5-page-10-5/raw.json: f7c6affd2f002ae34c338c6db269c6d992116e604306420569830bf3751c1ad8
        A/tables/TABLE-5-page-10-5/prompt.txt: 95d2988e6a8d1baba6a70bb314c5f80d3a495d6272263003f6a9ff5a8e1fc05e
        A/tables/TABLE-5-page-10-5/meta.json: cebe5d71758be64b28b0a3367ca79b0a1a8ed6e4b9f1c85de59ef34eaf317147
        A/tables/TABLE-1-page-4-1/raw.json: 9896abddf5b6616d3bc40f76e21192764299c259199639c01f8c1776b9a7e513
        A/tables/TABLE-1-page-4-1/prompt.txt: 96f0046520a7e5d68c3c01713136d9638589a0c5eb8a9eb10c71b5bb794c220c
        A/tables/TABLE-1-page-4-1/meta.json: e08a58be858e6090e4a3d4256262c60d72b8914a20aa53bf88eef8e177ea5e09
        A/tables/TABLE-4-page-9-4/raw.json: bcf8007aa0dfbedb022cc251b858594bd98475f558a8737c7b582dc78868c2f2
        A/tables/TABLE-4-page-9-4/prompt.txt: d0119fff13ed0ea4730ff958dce6b920adb1f07e715bdbefdee1731cb8ae1453
        A/tables/TABLE-4-page-9-4/meta.json: 76b35e63d6fc22feaefa22fb324909cf919829aece41d7f54ab6c892a6464730
        B/passages.json: 1b455d099b94dfbf7c6a2fbf56055ca88cdaadd9dc567cf275a3752d1fb493b0
        B/raw.json: b22eef0fb448139566a8a74d7fe2a573ffc9e03358d96529d8d4e9cb7a943c02
        B/source-units.json: 1e0c291b434e573dea9045db3c1bab87adcb5423a8983faf43942c6c4a9bc73a
        B/full-source-units.json: 71ebc5888b5ff41194af70d4046ddbe856dbdcfda7d8d91f0814f4af394ee3f4
        B/meta.json: faf5f90b4f340f0c75418674e22e86814dae5ec287b072170c5fd3af71512f15
        B/table-images/TABLE-4-page-9-1.png: 9689dd53c4ffe110991bbcbe23fe07d6c4e658e97ba58443c86baf98d7392a56
        B/table-images/page-10.png: c26507fe488b437055f8922f61a699ae595414c7f77052cc5bebc2bd67deb36f
        B/table-images/TABLE-3-page-8-1.png: 6447a9abecd0cb4e10bd160fd06313702b3a8216c83441b60efc398a08312618
        B/table-images/page-5.png: cf9f8af1a79c063e87ab4dade63efd3dade6fb0ad553007cab969484ac19adf2
        B/table-images/page-4.png: ac3ab2dfb5816ae065b02588b27c89c2f5b35f8fd5709713feb55cc53c41c980
        B/table-images/TABLE-1-page-4-1.png: c5a5d9afb580f860c52e478c57a62ff20fd0395a32465ee77e536ad9024afead
        B/table-images/page-9.png: 3b8255111985ada63f1bd8c1e442682c4aa2ad605f50109f7ea2eea6d3b30470
        B/table-images/page-8.png: 6cb50deb7e728354ef099e4c80c283d18d9c5ef4ec15d1b227ce30fdc460cdf7
        B/table-images/manifest.json: 65824a756fce9fab6c58adf8e24a234bdd7db22f72d998974de6dbfa0907ef56
        B/table-images/TABLE-5-page-10-1.png: d18e2ac403f04c5c41a33587f34711c71358899030c1eda1bf40cc4cee9b0af6
        B/table-images/TABLE-2-page-5-1.png: c37bc1a3e5164d3a890438dae07122a572a9d835a1199254f3732d7ef18dac11
        B/clauses/window-10/raw.json: ab9ed9f74a118227ecfae678ce4aded866cf5366d1f759c72cc2b547a6d34966
        B/clauses/window-10/prompt.txt: 4e1c37464d73d45d7fd7d5b65c2941d374a57fcb50ee4dd58a02592c7a2d18be
        B/clauses/window-10/meta.json: 20d6493a197738caf5985301860bc9fe34d7bf689ee1d294ed7a0e1f930dce31
        B/clauses/window-03/raw.json: b602902da09a8568f32cbc90a5140ca2309b93d4e023e57c89013da0c943f705
        B/clauses/window-03/prompt.txt: 307044463f852e440308cf086dd46971fbc6d8662a2ed4334690e252460cedb4
        B/clauses/window-03/meta.json: 64ceda4859eaccd6cbe4d0a1b488272d3486326581d6378668227da3bed0f3eb
        B/clauses/window-04/raw.json: 0647d6947d562214eb110673874ef0ad4f18b00c624e14607637f76a0d764966
        B/clauses/window-04/prompt.txt: b1fb2c90dc1afea278b415d1d08ff1d263033cbf991acb2b916d77ea2fbdd3cc
        B/clauses/window-04/meta.json: af11092caef571025d722c7b024abbc0e813164f2eca62cb8d44d3f03a797397
        B/clauses/window-05/raw.json: 56be093ec2bb8ce2fefcec29f0d95333f4c773b8edb25ed70bc2e62476a9b9d2
        B/clauses/window-05/prompt.txt: a4e9d502410c5a1b4cb845a02face721e20c3bc01c920c62419bacecc96e3b9a
        B/clauses/window-05/meta.json: e20a8f77911624feb2f33a6a6d7af3dcf538cc442a1c6bb76f190bab7d011c73
        B/clauses/window-02/raw.json: 79daa6b35d3965e5d9f14689fda138f12bc09a75fb1567e07992bed88ab466ab
        B/clauses/window-02/prompt.txt: 4b2506a815d77da4c45673b8b50e2b8677e1c86a46c12f36576f3a225d59f4e7
        B/clauses/window-02/meta.json: 25d20ff0104702bf2dd86207820e969fd253c02c920f4026c86f7d8197c6496e
        B/clauses/window-09/raw.json: 88149e7d538808aa10c3c64b8df91218416c656b4d9b4c727c27c40e9a6e1f4e
        B/clauses/window-09/prompt.txt: bae263d828af3c8479f7c6b736084b3c39edccd4d36f85a044ec4e8a34917a40
        B/clauses/window-09/meta.json: 10f82d4c2c86223ea969a14e7a48f6d5fb2fa7643aba12c925839b5f87da72eb
        B/clauses/window-07/raw.json: 64902754a4863bf00350f9f3ccc2a2c5705f5fb4bf7d5ed4bfeec44585c2ba06
        B/clauses/window-07/prompt.txt: add6466ff551fd09c03d62b24a3ffd597cccd6eb9756f4f6c2b93eba8a512ab2
        B/clauses/window-07/meta.json: 304bd5b76bf2137c6228cadaf332cc9b8d45b8f1270228e9e5619c77581c3790
        B/clauses/window-01/raw.json: 2a7d5680c12dd071e1cf4cb1a95e98f93f766dfb50c17513e90119c84647646f
        B/clauses/window-01/prompt.txt: 243aa04f124197bfb55a27767fdc31db3310a56592da7e0b944bcd119f118729
        B/clauses/window-01/meta.json: 2ac41a5a38c87517baa396cf60906304942bbbbfe3da66831a903cc13d249b02
        B/clauses/window-06/raw.json: 55f120e865beccae485651eb1151911ed308901ca6fa72ea42dcc66b01b177b3
        B/clauses/window-06/prompt.txt: 84699ccdc3c0e73ef6baa9146adfab2736ff76ef1fdfe8e75b69ce4d954b751d
        B/clauses/window-06/meta.json: 3d0508c3e9b820db1d86663e17094b80cba4ce117c5f60117bd88fdaefcdb472
        B/clauses/window-08/raw.json: 0da9aee25bc608bc8cf53291c56425674774e8d6f5e7f03b272aad06ac675324
        B/clauses/window-08/prompt.txt: b60e37bc995274528d8f06a28ccfa705fb9a5be64912ad7073bb5c289c6345f8
        B/clauses/window-08/meta.json: 61d6f97008fa7d3f5ab7fba1801efe01a6c191f03d8355951b19b0525890f3bb
        B/tables/TABLE-2-page-5-2/raw.json: 52bffd2a0a95dcb4b05ff2dc6caa8e995f013ba574a64749bfd409daf82d6037
        B/tables/TABLE-2-page-5-2/prompt.txt: 4247c5c2f499e096ee0d02c862f45be6026d651a3c66ed56a5b9bfaf6b397f7b
        B/tables/TABLE-2-page-5-2/meta.json: 4a79217c1d43366ad86331470282d8961d3656885df7501f694061cf80c1189c
        B/tables/TABLE-3-page-8-3/raw.json: 9cbe7047d1c30cfbc407c7c6ab491650de2c010542fdc1082e8a302f94cfdbd2
        B/tables/TABLE-3-page-8-3/prompt.txt: e52613d8ef5a0ce49609c567f2ec46f9d2ecef323b136653a3f57a0b57d2d52d
        B/tables/TABLE-3-page-8-3/meta.json: 67c6880966026ddbd4ac90783cac0c00a2152748a9f1a2319271142c4e1f4c7f
        B/tables/TABLE-5-page-10-5/raw.json: 1d48d27fb7d097e1d30fa097d5d3174003a39be8fca7e540abb62169a9e5e85c
        B/tables/TABLE-5-page-10-5/prompt.txt: 95d2988e6a8d1baba6a70bb314c5f80d3a495d6272263003f6a9ff5a8e1fc05e
        B/tables/TABLE-5-page-10-5/meta.json: d943b417d07dc60027a6188404baf679a8f173c21f8c4096f80008f0de580707
        B/tables/TABLE-1-page-4-1/raw.json: b2c27f8a6895d422a0fc9df2bb3b8af81f55b2879c89ba4a91124e7a82e96b2e
        B/tables/TABLE-1-page-4-1/prompt.txt: 96f0046520a7e5d68c3c01713136d9638589a0c5eb8a9eb10c71b5bb794c220c
        B/tables/TABLE-1-page-4-1/meta.json: 8434d2a504d817c6c30038e09c4771ad91841df894401cc66a2849ca57c738f1
        B/tables/TABLE-4-page-9-4/raw.json: eb1f149fe5a0b19acaf01145d8a7fae8a462ba4cbebe9341fbea89fc4bb2665a
        B/tables/TABLE-4-page-9-4/prompt.txt: d0119fff13ed0ea4730ff958dce6b920adb1f07e715bdbefdee1731cb8ae1453
        B/tables/TABLE-4-page-9-4/meta.json: cdc361e496960772e98224a3da057e85f5a6563d31266b65776e2fcb89637f44
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
      pdf_sha256: bc4a512d9f277c1330ee6db4299bd3190253a191e5b40dcf142ad2fdbe12a5f8
      source_review: _compare/relationships-2026-11-16/review-current/GajardoVidal2021
      source_status_sha256: aad5cb00fc763ef7b06523b9b87f374df532f1c37b5d3b24ac91e2e2badc97ce
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R011
    exposure:
      text: damage to aAF versus BA44
    outcome:
      text: appropriate information carrying words, syntactic variety, grammatical
        well-formedness, and speed of speech production
    analysis_label: Post hoc subscore analysis
    relation: association
    evidence_ids:
    - P9-S1-C11
    - P9-S2-C1
    qualifier_ids:
    - P9-S1-C11
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: bc4a512d9f277c1330ee6db4299bd3190253a191e5b40dcf142ad2fdbe12a5f8
      source_review: _compare/relationships-2026-11-16/review-current/GajardoVidal2021
      source_status_sha256: aad5cb00fc763ef7b06523b9b87f374df532f1c37b5d3b24ac91e2e2badc97ce
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P3-S2-C3
      - Result passage disposed without unit P6-S2-C2
      - Accounting without a linked unit P7-S1-C7
      - Accounting without a linked unit P7-S1-C8
      - Unaccounted source passage P7-S1-C7
      - Unaccounted source passage P7-S1-C8
      - Result passage disposed without unit P9-S1-C1
      - Result passage disposed without unit P9-S1-C10
      - Result passage disposed without unit P9-S1-C11
      - Result passage disposed without unit P9-S1-C3
      - Result passage disposed without unit P9-S1-C8
      - Result passage disposed without unit P9-S1-C9
      - Result passage disposed without unit P10-S1-C3
      - Result passage disposed without unit P11-S1-C6
      - Result passage disposed without unit P11-S2-C8
      - Result passage disposed without unit P11-S2-C9
      - Result passage disposed without unit P11-S3-C1
      - Result passage disposed without unit P13-S1-C2
      - Result passage disposed without unit P13-S1-C6
      unattached_null_or_qualifier_ids:
      - P6-S2-C2
      - P7-S1-C8
      - P9-S1-C10
      - P13-S1-C2
      suppressed_nonrepresented_units: 31
      default_disposition_count_requires_completeness_check: 224
      unselected_timing_passages:
      - P4-S2-C2
      - P4-S2-C3
      - P9-S1-C7
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P1-S1-C16
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S2-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S2-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S2-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S2-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C9
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
        source_id: P8-S1-C14
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C15
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C16
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S2-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S2-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S2-C5
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
        source_id: P9-S1-C1
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
        source_id: P9-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S3-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S3-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S3-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S3-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S3-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S1-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S1-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S1-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S1-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S1-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P4-S1-C4
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: imaging_provenance
        source_ids:
        - P3-S3-C3
        - P3-S3-C4
        - P3-S3-C5
        - P3-S3-C10
        - P3-S4-C2
        - P4-S1-C2
        - P5-S1-C11
        - P5-S1-C12
        - P5-S1-C13
        - P6-S1-C1
        - P6-S1-C2
        - P6-S1-C3
        - P6-S1-C4
        - P6-S1-C5
        - P6-S1-C6
        - P6-S1-C7
        - P6-S1-C8
        - P6-S1-C9
        - P12-S3-C1
        - P12-S3-C2
        - P12-S3-C3
        - P12-S3-C5
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: analysis_restrictions
        source_ids:
        - P3-S2-C2
        - P3-S2-C4
        - P3-S2-C5
        - P6-S2-C2
        - P6-S2-C7
        - P7-S1-C1
        - P7-S2-C15
        - P7-S3-C3
        - P7-S3-C4
        - P7-S3-C6
        - P8-S1-C5
        - P8-S1-C13
        - P8-S1-C14
        - P8-S1-C15
        - P8-S1-C16
        - P9-S1-C1
        - P9-S1-C2
        - P9-S1-C3
        - P9-S1-C4
        - P12-S1-C12
        - P12-S2-C1
        - P12-S2-C2
        - P12-S2-C3
        - P12-S2-C4
        - P12-S2-C5
        - P12-S2-C6
        - P12-S2-C7
        - P12-S2-C8
        - P12-S2-C9
        - P12-S2-C10
        - P12-S2-C11
        - P12-S2-C12
        - P12-S3-C1
        - P12-S3-C10
        - P12-S3-C1
        - P12-S3-C2
        - P12-S3-C3
        - P12-S3-C4
        - P12-S3-C5
        - P12-S3-C6
        - P12-S3-C7
        - P12-S3-C8
        - P12-S3-C9
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: limitations
        source_ids:
        - P12-S1-C11
        - P12-S1-C12
        - P12-S2-C1
        - P12-S2-C2
        - P12-S2-C3
        - P12-S2-C4
        - P12-S2-C5
        - P12-S2-C6
        - P12-S2-C7
        - P12-S2-C8
        - P12-S2-C9
        - P12-S2-C10
        - P12-S2-C11
        - P12-S2-C12
        - P12-S3-C1
        - P12-S3-C10
        - P12-S3-C2
        - P12-S3-C3
        - P12-S3-C4
        - P12-S3-C5
        - P12-S3-C6
        - P12-S3-C7
        - P12-S3-C8
        - P12-S3-C9
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: adjustment_roles
        source_ids:
        - P1-S1-C15
        - P5-S1-C9
        - P6-S1-C10
        - P7-S1-C1
        - P7-S2-C1
        - P7-S2-C10
        - P7-S2-C11
        - P7-S2-C14
        - P7-S2-C15
        - P7-S3-C11
        - P7-S4-C3
        - P7-S4-C5
        - P8-S1-C16
        - P8-S2-C3
        - P8-S2-C4
        - P8-S2-C5
        - P8-S2-C6
        - P8-S2-C7
        - P8-S3-C2
        - P8-S3-C3
        - P9-S1-C1
        - P9-S1-C2
        - P9-S1-C3
        - P9-S1-C4
        - P9-S3-C2
        - P9-S3-C3
        - P9-S3-C4
        - P9-S3-C5
        - P9-S3-C6
        - P10-S1-C7
        - P10-S1-C8
        - P11-S1-C3
        - P11-S1-C4
        - P11-S1-C6
        - P11-S1-C7
        - P11-S1-C8
        - P11-S1-C9
        - P12-S1-C3
        - P12-S1-C5
        - P12-S1-C6
        - P12-S1-C7
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - imaging_provenance
      - validation
      - analysis_restrictions
      - limitations
      - personal_factors
      - tested_personal_effects
      - adjustment_roles
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-4-1
      - TABLE-2-page-5-2
      - TABLE-3-page-8-3
      - TABLE-4-page-9-4
      - TABLE-5-page-10-5
      unlinked_tables:
      - TABLE-1-page-4-1
      - TABLE-2-page-5-2
      - TABLE-5-page-10-5
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P4-S1
        - P4-S2
        - P5-S1
        - P6-S2
        - P7-S1
        - P7-S2
        - P9-S1
        - P9-S2
        - P11-S1
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: bc4a512d9f277c1330ee6db4299bd3190253a191e5b40dcf142ad2fdbe12a5f8
      source_review: _compare/relationships-2026-11-16/review-current/GajardoVidal2021
      source_status_sha256: aad5cb00fc763ef7b06523b9b87f374df532f1c37b5d3b24ac91e2e2badc97ce
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C16
      disposition: represented
      result_indexes:
      - 1
      reason: States long-term speech production impairments were solely predicted
        by white matter damage near aAF with no contribution from Broca's area.
    - source_id: P1-S2-C2
      disposition: represented
      result_indexes:
      - 6
      reason: Establishes that aAF damage effects cannot be explained by Broca's area
        disconnection.
    - source_id: P1-S2-C3
      disposition: repeated
      result_indexes:
      - 1
      - 6
      reason: Restatement of main conclusions in the abstract.
    - source_id: P3-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes correlation between aAF and long segment of arcuate fasciculus.
    - source_id: P4-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Mentions replication of Model 2 in supplementary material.
    - source_id: P4-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Defines 'long-term' and 'persistent' based on patient phase.
    - source_id: P6-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discusses regression diagnostic statistics and multicollinearity.
    - source_id: P6-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes lesion overlap map figure.
    - source_id: P7-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Explains why BA45 was excluded from Model 2.
    - source_id: P7-S1-C8
      disposition: represented
      result_indexes:
      - 3
      reason: Defines Model 3 regressors.
    - source_id: P7-S3-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes patient numbers for post hoc thresholds.
    - source_id: P7-S4-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes performance of excluded patients during matching.
    - source_id: P7-S4-C5
      disposition: represented
      result_indexes:
      - 9
      reason: Confirms groups did not differ in age or time post-stroke.
    - source_id: P8-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes stroke type in post hoc groups.
    - source_id: P8-S1-C8
      disposition: represented
      result_indexes:
      - 0
      reason: 'Reports Model 1 results: BA44 predicted scores, BA45 did not.'
    - source_id: P8-S1-C9
      disposition: represented
      result_indexes:
      - 0
      reason: Reports R2 for Model 1.
    - source_id: P8-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Explains exclusion of BA45 from Model 2.
    - source_id: P8-S1-C11
      disposition: represented
      result_indexes:
      - 1
      reason: Reports that BA44 no longer explained scores in Model 2.
    - source_id: P8-S1-C12
      disposition: represented
      result_indexes:
      - 1
      reason: Reports that only aAF was significant in Model 2.
    - source_id: P8-S1-C13
      disposition: represented
      result_indexes:
      - 2
      reason: Reports no non-linear relationship in Model 3a.
    - source_id: P8-S1-C14
      disposition: represented
      result_indexes:
      - 3
      reason: Reports no moderation effect in Model 3b.
    - source_id: P8-S1-C15
      disposition: represented
      result_indexes:
      - 4
      reason: Reports results did not change after segregating BA44.
    - source_id: P8-S2-C3
      disposition: represented
      result_indexes:
      - 5
      reason: Reports total effects of cortical regions in Model 4.
    - source_id: P8-S2-C4
      disposition: represented
      result_indexes:
      - 5
      reason: Reports direct effects of cortical regions in Model 4.
    - source_id: P8-S2-C5
      disposition: represented
      result_indexes:
      - 5
      reason: Reports mediation percentage by aAF.
    - source_id: P8-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports correlation between aAF and BA44/BA45.
    - source_id: P9-S1-C1
      disposition: represented
      result_indexes:
      - 6
      reason: Reports BF for BA44 null hypothesis.
    - source_id: P9-S1-C3
      disposition: represented
      result_indexes:
      - 7
      reason: Reports BF for aAF alternative hypothesis.
    - source_id: P9-S1-C7
      disposition: represented
      result_indexes:
      - 9
      reason: Confirms matching of post hoc groups.
    - source_id: P9-S1-C8
      disposition: represented
      result_indexes:
      - 9
      reason: Reports significant effect of group on speech production.
    - source_id: P9-S1-C9
      disposition: represented
      result_indexes:
      - 9
      reason: Reports aAF group performed worse than BA44 group.
    - source_id: P9-S1-C10
      disposition: represented
      result_indexes:
      - 10
      reason: Reports results did not change after covarying insula and putamen.
    - source_id: P9-S1-C11
      disposition: represented
      result_indexes:
      - 11
      reason: Reports poorer quality and quantity of speech for aAF group.
    - source_id: P9-S2-C1
      disposition: represented
      result_indexes:
      - 11
      reason: Details specific subscore differences (words, variety, grammar, speed).
    - source_id: P9-S3-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Explains mediation effect calculation.
    - source_id: P9-S3-C4
      disposition: represented
      result_indexes:
      - 5
      reason: Confirms significance of total and indirect effects.
    - source_id: P9-S3-C5
      disposition: represented
      result_indexes:
      - 5
      reason: Confirms non-significance of direct effects.
    - source_id: P10-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation that no patient completely preserved neighbouring regions.
    - source_id: P10-S3-C5
      disposition: represented
      result_indexes:
      - 10
      reason: Table 5 results for ANCOVA.
    - source_id: P11-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Cites prior evidence of white matter damage effects.
    - source_id: P11-S2-C8
      disposition: represented
      result_indexes:
      - 6
      reason: States aAF effect cannot be explained by Broca's area disconnection.
    - source_id: P11-S3-C1
      disposition: represented
      result_indexes:
      - 6
      reason: Explains why BA44 damage with spared aAF had better outcomes than aAF
        damage with spared BA44.
    - source_id: P11-S3-C2
      disposition: repeated
      result_indexes:
      - 6
      - 7
      reason: Restatement of Bayesian results.
    - source_id: P11-S4-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Cites prior conclusions on aAF importance.
    - source_id: P12-S1-C3
      disposition: repeated
      result_indexes:
      - 11
      reason: Restatement of subscore results.
    - source_id: P12-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Mentions significant association when regions are considered in isolation.
    - source_id: P12-S1-C6
      disposition: repeated
      result_indexes:
      - 1
      reason: Restatement of Model 2 result.
    - source_id: P12-S1-C7
      disposition: repeated
      result_indexes:
      - 1
      reason: Restatement of Model 2 result.
    - source_id: P12-S3-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Mentions use of normative atlases.
    - source_id: P13-S1-C6
      disposition: repeated
      result_indexes:
      - 1
      - 6
      reason: Conclusion restating that BA44/45 do not contribute to long-term outcome.
    unresolved_coverage:
    - source_id: P9-S1-C11
      disposition: unresolved
      reason: Unknown result index; not accepted as coverage
    - source_id: P9-S2-C1
      disposition: unresolved
      reason: Unknown result index; not accepted as coverage
    - source_id: P10-S3-C5
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P11-S4-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P12-S1-C3
      disposition: unresolved
      reason: Unknown result index; not accepted as coverage
    - source_id: P12-S3-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P9-S2-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S2-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S2-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S3-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S2-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S3-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S1-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C16
    - P1-S2-C2
    - P1-S2-C3
    - P3-S2-C3
    - P4-S1-C4
    - P4-S2-C5
    - P6-S2-C2
    - P6-S2-C10
    - P7-S1-C7
    - P7-S1-C8
    - P7-S3-C10
    - P7-S4-C2
    - P7-S4-C5
    - P8-S1-C1
    - P8-S1-C9
    - P8-S1-C10
    - P8-S2-C6
    - P9-S1-C7
    - P9-S2-C3
    - P9-S2-C5
    - P9-S3-C3
    - P9-S3-C4
    - P9-S3-C5
    - P10-S1-C3
    - P11-S1-C6
    - P11-S2-C8
    - P11-S2-C9
    - P11-S3-C1
    - P11-S3-C2
    - P11-S3-C8
    - P12-S1-C3
    - P12-S1-C5
    - P12-S1-C6
    - P12-S1-C7
    - P12-S2-C9
    - P12-S3-C6
    - P13-S1-C2
    - P13-S1-C6
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-4-1
    - TABLE-2-page-5-2
    - TABLE-3-page-8-3
    - TABLE-4-page-9-4
    - TABLE-5-page-10-5
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P4-S2-C3
      recruited_sample:
      - P4-S1-C10
      eligibility:
      - P4-S1-C10
      - P4-S1-C12
      - P4-S2-C2
      - P4-S2-C3
      imaging_provenance: []
      imaging_timing:
      - P3-S2-C9
      - P3-S3-C1
      - P4-S2-C5
      - P5-S2-C4
      - P6-S1-C10
      - P11-S1-C5
      outcome_timing:
      - P1-S1-C16
      - P3-S2-C8
      - P3-S2-C9
      - P3-S3-C1
      - P4-S2-C5
      - P5-S2-C4
      - P11-S1-C1
      - P11-S1-C5
      outcome_definition:
      - P1-S1-C14
      - P4-S2-C10
      - P5-S1-C3
      - P5-S1-C4
      - P5-S1-C5
      validation: []
      analysis_restrictions: []
      dependent_variable_statement:
      - P1-S1-C14
      - P1-S1-C15
      - P2-S3-C3
      - P6-S1-C10
      limitations: []
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles: []
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P4-S2-C3
      - P4-S2-C4
      - P5-S2-C4
    outcome_type: both_reported
    imaging_vs_outcome: mixed
    validation_type: internal_cross_validation
    held_selections:
    - slot: dependent_variable_statement
      source_id: P1-S1-C16
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S2-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S2-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S2-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S2-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C9
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
      source_id: P8-S1-C14
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C15
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C16
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S2-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S2-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S2-C5
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
      source_id: P9-S1-C1
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
      source_id: P9-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S3-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S3-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S3-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S3-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S3-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S1-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S1-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S1-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S1-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S1-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P4-S1-C4
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: imaging_provenance
      source_ids:
      - P3-S3-C3
      - P3-S3-C4
      - P3-S3-C5
      - P3-S3-C10
      - P3-S4-C2
      - P4-S1-C2
      - P5-S1-C11
      - P5-S1-C12
      - P5-S1-C13
      - P6-S1-C1
      - P6-S1-C2
      - P6-S1-C3
      - P6-S1-C4
      - P6-S1-C5
      - P6-S1-C6
      - P6-S1-C7
      - P6-S1-C8
      - P6-S1-C9
      - P12-S3-C1
      - P12-S3-C2
      - P12-S3-C3
      - P12-S3-C5
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: analysis_restrictions
      source_ids:
      - P3-S2-C2
      - P3-S2-C4
      - P3-S2-C5
      - P6-S2-C2
      - P6-S2-C7
      - P7-S1-C1
      - P7-S2-C15
      - P7-S3-C3
      - P7-S3-C4
      - P7-S3-C6
      - P8-S1-C5
      - P8-S1-C13
      - P8-S1-C14
      - P8-S1-C15
      - P8-S1-C16
      - P9-S1-C1
      - P9-S1-C2
      - P9-S1-C3
      - P9-S1-C4
      - P12-S1-C12
      - P12-S2-C1
      - P12-S2-C2
      - P12-S2-C3
      - P12-S2-C4
      - P12-S2-C5
      - P12-S2-C6
      - P12-S2-C7
      - P12-S2-C8
      - P12-S2-C9
      - P12-S2-C10
      - P12-S2-C11
      - P12-S2-C12
      - P12-S3-C1
      - P12-S3-C10
      - P12-S3-C1
      - P12-S3-C2
      - P12-S3-C3
      - P12-S3-C4
      - P12-S3-C5
      - P12-S3-C6
      - P12-S3-C7
      - P12-S3-C8
      - P12-S3-C9
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: limitations
      source_ids:
      - P12-S1-C11
      - P12-S1-C12
      - P12-S2-C1
      - P12-S2-C2
      - P12-S2-C3
      - P12-S2-C4
      - P12-S2-C5
      - P12-S2-C6
      - P12-S2-C7
      - P12-S2-C8
      - P12-S2-C9
      - P12-S2-C10
      - P12-S2-C11
      - P12-S2-C12
      - P12-S3-C1
      - P12-S3-C10
      - P12-S3-C2
      - P12-S3-C3
      - P12-S3-C4
      - P12-S3-C5
      - P12-S3-C6
      - P12-S3-C7
      - P12-S3-C8
      - P12-S3-C9
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: adjustment_roles
      source_ids:
      - P1-S1-C15
      - P5-S1-C9
      - P6-S1-C10
      - P7-S1-C1
      - P7-S2-C1
      - P7-S2-C10
      - P7-S2-C11
      - P7-S2-C14
      - P7-S2-C15
      - P7-S3-C11
      - P7-S4-C3
      - P7-S4-C5
      - P8-S1-C16
      - P8-S2-C3
      - P8-S2-C4
      - P8-S2-C5
      - P8-S2-C6
      - P8-S2-C7
      - P8-S3-C2
      - P8-S3-C3
      - P9-S1-C1
      - P9-S1-C2
      - P9-S1-C3
      - P9-S1-C4
      - P9-S3-C2
      - P9-S3-C3
      - P9-S3-C4
      - P9-S3-C5
      - P9-S3-C6
      - P10-S1-C7
      - P10-S1-C8
      - P11-S1-C3
      - P11-S1-C4
      - P11-S1-C6
      - P11-S1-C7
      - P11-S1-C8
      - P11-S1-C9
      - P12-S1-C3
      - P12-S1-C5
      - P12-S1-C6
      - P12-S1-C7
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
      pdf_sha256: bc4a512d9f277c1330ee6db4299bd3190253a191e5b40dcf142ad2fdbe12a5f8
      review_sha256: 4b76f5c50cba7fc43c14744d0739463d1a4f2b445692ef436a9758b2615d6603
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
      - P9-S1-C11
      - P9-S2-C1
      source_result: 'In a post hoc subscore analysis of matched groups (BA44 vs aAF),
        patients with damage to the anterior arcuate fasciculus (aAF) showed significantly
        poorer performance than those with damage to Brodmann area 44 (BA44) on specific
        subscores of the spoken picture description task: appropriate information
        carrying words, syntactic variety, grammatical well-formedness, and speed
        of speech production. This finding is consistent with the primary group comparison
        and remained significant after adjusting for lesion load in the superior central
        insula and putamen.'
      result_status: detected
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis is the post hoc subscore comparison between
            the aAF and BA44 groups, as described in P9-S1-C11 and P9-S2-C1. The proposed
            core correctly identifies this as a post hoc analysis comparing these
            specific groups on specific subscores, distinct from the primary regression
            models or the overall ANOVA.
          source_ids:
          - P9-S1-C11
          - P9-S2-C1
          - P7-S3-C7
        direction:
          answer: fits
          reason: The source explicitly states that the aAF group performed worse
            than the BA44 group on the specified subscores (P9-S2-C1). The proposed
            core correctly captures this direction of effect (aAF damage associated
            with worse outcomes compared to BA44 damage).
          source_ids:
          - P9-S2-C1
          - P9-S1-C9
        construct:
          answer: fits
          reason: The exposure is correctly identified as damage to aAF versus BA44.
            The outcome is correctly identified as the specific subscores of the CAT
            spoken picture description task (appropriate information carrying words,
            syntactic variety, grammatical well-formedness, speed). The patient measurement
            is correctly identified as template_lesion_overlap, as the groups were
            defined by lesion load in atlas-based regions (P7-S3-C7, P3-S3-C3), not
            by patient-specific diffusion tractography.
          source_ids:
          - P9-S2-C1
          - P3-S3-C3
          - P7-S3-C7
        qualifications:
          answer: fits
          reason: 'The proposed core includes the critical qualifications: the analysis
            is post hoc, involves small matched groups (7 vs 7), and the result was
            robust to covarying for insula and putamen damage (P9-S1-C10). It also
            notes the limitation regarding Fisher''s LSD (P8-S1-C5). These qualifiers
            are present and accurate.'
          source_ids:
          - P9-S1-C10
          - P7-S4-C4
          - P8-S1-C5
        missing_material_caveat:
          answer: fits
          reason: No material caveats are missing. The core correctly flags the small
            sample size and the lack of family-wise error control as limitations.
            The robustness to insula/putamen covariates is included as a qualification.
            The distinction between this post hoc subscore analysis and the primary
            regression findings is maintained.
          source_ids:
          - P8-S1-C5
          - P9-S1-C10
          - P7-S4-C4
      optional_pending:
      - Exact sample sizes for the subscore analysis (implied as 7 vs 7 from P7-S4-C4,
        but not explicitly stated in the subscore text P9-S2-C1)
      - Specific statistical values (t, U, P-values) for each subscore are not transcribed
        in the core, as per the qualitative draft instruction
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Sample size requires source confirmation; it has not been transcribed.
    - 'sample.time_post_onset: source confirmation required; original proposed wording
      remains in the audit.'
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Exact sample sizes for the subscore analysis (implied as 7 vs 7 from P7-S4-C4,
      but not explicitly stated in the subscore text P9-S2-C1)
    - Specific statistical values (t, U, P-values) for each subscore are not transcribed
      in the core, as per the qualitative draft instruction
    normalizations:
    - field: sample.n
      original: 22
      action: not_transcribed
      reason: Not supported by selected quotations
    - field: sample.time_post_onset
      original: At least 3 months post-stroke; 92% of the total cohort were in the
        chronic phase (>6 months post-stroke)
      action: not_transcribed
      reason: 'Numbers not grounded in usable selected source readings: 6, 92'
    analysis_identity:
      id: R011
      exposure:
        text: damage to aAF versus BA44
      outcome:
        text: appropriate information carrying words, syntactic variety, grammatical
          well-formedness, and speed of speech production
      analysis_label: Post hoc subscore analysis
      relation: association
      evidence_ids:
      - P9-S1-C11
      - P9-S2-C1
      qualifier_ids:
      - P9-S1-C11
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: bc4a512d9f277c1330ee6db4299bd3190253a191e5b40dcf142ad2fdbe12a5f8
        source_review: _compare/relationships-2026-11-16/review-current/GajardoVidal2021
        source_status_sha256: aad5cb00fc763ef7b06523b9b87f374df532f1c37b5d3b24ac91e2e2badc97ce
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P7-S4-C4:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: bc4a512d9f277c1330ee6db4299bd3190253a191e5b40dcf142ad2fdbe12a5f8
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 65462d8b7393c316182de0c5e7a9cd3568f44ff34159523cb6839d0026242312
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P7-S4-C4
          page: 7
          text_layer_sha256: 65462d8b7393c316182de0c5e7a9cd3568f44ff34159523cb6839d0026242312
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'In total, there were

          seven, seven and eight patients who were matched for total le-

          sion volume (range and mean) in the BA44, aAF, and

          BA44 + aAF groups, respectively.'
        anchor_text: 'In total, there were

          seven, seven and eight patients who were matched for total le-

          sion volume (range and mean) in the BA44, aAF, and

          BA44 + aAF groups, respectively.'
        excluded_fragments: []
        image_sha256: d65e718f1090a7c10118bb5222850e0f5c6316c8aff998ab0a390d15a9439163
        transcription: '. In total, there were

          seven, seven and eight patients who were matched for total le-

          sion volume (range and mean) in the BA44, aAF, and

          BA44+aAF groups, respectively'
      P4-S2-C2:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: bc4a512d9f277c1330ee6db4299bd3190253a191e5b40dcf142ad2fdbe12a5f8
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 57c74a5e5190ab388501609f8357a08616cb906cf43139e399f9ef823da1285e
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P4-S2-C2
          page: 4
          text_layer_sha256: 57c74a5e5190ab388501609f8357a08616cb906cf43139e399f9ef823da1285e
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Inclusion criteria were:

          (i) aged over 18 years; (ii) no history of neurological or psychi-

          atric illness (other than stroke); (iii) native speaker of English;

          (iv) right handed pre-morbidly; (v) at least 3 months post-stroke

          (to allow enough time for spontaneous functional reorganization

          to occur); and (vi) 510 years since stroke onset (to control for

          longer term changes related to cognitive decline).'
        anchor_text: 'Inclusion criteria were:

          (i) aged over 18 years; (ii) no history of neurological or psychi-

          atric illness (other than stroke); (iii) native speaker of English;

          (iv) right handed pre-morbidly; (v) at least 3 months post-stroke

          (to allow enough time for spontaneous functional reorganization

          to occur); and (vi) 510 years since stroke onset (to control for

          longer term changes related to cognitive decline).'
        excluded_fragments: []
        image_sha256: 80cf80fb8e89f9d7873a4011f6a3e43553382f502b0e959df10fa864bf27fa26
        transcription: '. Inclusion criteria were:

          (i) aged over 18 years; (ii) no history of neurological or psychi-

          atric illness (other than stroke); (iii) native speaker of English;

          (iv) right handed pre-morbidly; (v) at least 3 months post-stroke

          (to allow enough time for spontaneous functional reorganization

          to occur); and (vi) <10 years since stroke onset (to control for

          longer term changes related to cognitive decline)'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 9
  quote: 'A

    Fisher’s LSD post hoc test showed that this occurred because

    the aAF group performed significantly worse than the BA44

    group on the spoken picture description task [mean ± stand-

    ard

    deviation

    (SD)

    =

    55.4 ± 5.7

    versus

    62.9 ± 4.1;

    P = 0.013], with no significant differences between the aAF

    group, and the BA44 + aAF group (mean ± SD = 55.4 ± 5.7

    versus 55.5 ± 5.3; P = 0.979).'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-24'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
