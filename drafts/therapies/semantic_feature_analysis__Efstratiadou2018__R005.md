---
id: semantic_feature_analysis
name: semantic feature analysis
kind: therapy
findings:
- id: f1
  target: naming_of_trained_items
  target_kind: impairment
  claim: Improvement in naming of trained items was observed in most participants
    with Broca's (85.71%), anomic (81.25%), Wernicke's (80%), conduction (100%), and
    transcortical motor aphasia (100%), while negative outcomes were found for participants
    with global and mixed aphasia.
  direction: likely
  relationship: treatment_response
  method: meta-analysis
  sample:
    n: 55
    population: Not transcribed; confirm from the original PDF population and timing
      passages.
    phase: not_reported
    time_post_onset: post-therapy gains assessed immediately after treatment ended
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Lack of standardized dosage and treatment duration across included studies
  - Variations in treatment protocols (e.g., modifications to feature categories or
    addition of homework)
  - All included studies were single case studies
  evidence_quality: meta-analysis
  strength: weak
  notes: 'Exposure measurement: A treatment protocol where individuals with word retrieval
    difficulties are shown a picture to name and encouraged to generate semantic features
    (e.g., group, action, use, location, properties, associations) by completing a
    feature analysis chart, using systematic cueing that is gradually faded. Improvement
    was specifically for trained items; Participants included both fluent (33) and
    nonfluent (21) types. Additional metadata has not been transcribed; review the
    pending-field flags before approval. PDF image reading (P6-S3-C4, two-model agreement,
    human verification pending): . A total of 55 participants have been treated in
    the included studies Original text-layer quotation is preserved below. PDF image
    reading (P10-S1-C12, two-model agreement, human verification pending): . Apha-

    sia was due to a stroke in 51 individuals and to traumatic

    brain injury in four individuals (neuropathology for three

    individuals was not reported) Original text-layer quotation is preserved below.
    PDF image reading (P4-S3-C6, two-model agreement, human verification pending):
    . All studies were single case

    studies (N = 21) Original text-layer quotation is preserved below.'
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
    - not_transcribed:sample.population
    - proposed_concept:naming_of_trained_items
  therapy:
    id: semantic_feature_analysis
    name: semantic feature analysis
  citation: '@Efstratiadou2018'
  source_passages:
  - section: Original source P10-S2-C7
    page: 10
    quote: 'Twelve of the 14 (85.71%) participants with Broca’s

      aphasia, 13 of the 16 anomic participants (81.25%), four

      of the five (80%) individuals with Wernicke’s aphasia, and

      all nine with conduction aphasia and three with transcor-

      tical motor aphasia (100%) showed improvement on nam-

      ing of trained items.'
    supports: claim
  - section: Original source P10-S2-C8
    page: 10
    quote: 'Negative outcomes were found for

      the two participants with global and mixed aphasia.'
    supports: claim
  - section: Original source P2-S3-C9
    page: 2
    quote: 'During SFA treatment, individuals

      with word retrieval difficulties are shown a picture to name,

      and they are encouraged to generate the semantic features

      of the target word by completing the feature analysis chart.'
    supports: method
  - section: Original source P6-S3-C4
    page: 6
    quote: 'A to-

      tal of 55 participants have been treated in the included

      studies.'
    supports: sample
  - section: Original source P10-S1-C12
    page: 10
    quote: 'Apha-

      sia was due to a stroke in 51 individuals and to traumatic

      brain injury in four individuals (neuropathology for three

      individuals was not reported).'
    supports: sample
  - section: Original source P12-S1-C3
    page: 12
    quote: 'All studies assessed posttherapy gains immediately

      after treatment ended.'
    supports: method
  - section: Original source P15-S1-C2
    page: 15
    quote: 'Therefore, another limiting factor is the lack

      of a standardized dosage and treatment duration across

      studies.'
    supports: limitation
  - section: Original source P14-S3-C12
    page: 14
    quote: 'Many studies changed the tra-

      ditional SFA protocol in various ways, such as modifica-

      tions to the semantic feature categories (Mehta & Isaki,

      2016; Wambaugh & Ferguson, 2007; Wambaugh et al.,

      2014), eliciting fewer features (Hashimoto & Frome, 2011;

      Mehta & Isaki, 2016), writing the features in addition

      to or instead of saying them (Hashimoto & Frome, 2011),

      following different treatment stages (L. A. Davis & Stanton,

      2005), and adding new factors, such as independent home-

      work (Falconer & Antonucci, 2012).'
    supports: limitation
  - section: Original source P4-S3-C6
    page: 4
    quote: 'All studies were single case

      studies (N = 21).'
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-23'
relationship_review:
  paper: Efstratiadou2018
  proposal_id: R005
  review_status_sha256: 71453e86d91903d06b2957c7e7f267f13b820fc57127950d0f32df0aeb2c5e77
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: c8562d7b60d51b5ec07c8d06adda9523b0af176ca21610d4d53af3f26f94ec8a
    original_review_binding:
      version: relationship-review-v5
      input_hashes:
        pdf: c8562d7b60d51b5ec07c8d06adda9523b0af176ca21610d4d53af3f26f94ec8a
        A/passages.json: 58b74711cafea0b183c1dd9de9c5ee40de6dccf4c8414bbb0d6951d45c5eccda
        A/raw.json: 486a332671a58f25b65c39b96123977d2b2a0aa6c83e5f93f3f343d73e0389ae
        A/source-units.json: fc090d70c633262bbdb9fb19da54dc0d097cb070b9f0f0b36f14f210aedd8942
        A/full-source-units.json: 216290e0c7e4ae816423030ab10b04a386b365ca05ded0f66b219ccdf84dcd5e
        A/meta.json: a315fcf7abf63a4c4d133df969dd317c8cda03dbc4ae2c2e179f0b82088982d1
        A/table-images/TABLE-3-page-10-1.png: fd8aa7fef241b0f4d6b7daf368cf0c4522abd824eda43bb568b5885dc4dca173
        A/table-images/page-13.png: 6875ada03d9aca889757887933114066f363147270f8541e4c8888657eb5a776
        A/table-images/page-12.png: b593d093399a6c4326713b9f5aad691da3eb454773fc3fa65ea6f15cfba07da2
        A/table-images/page-10.png: 14cd645ddf06831f62a5e767977b690af6b2d45f0e92159f847fee9266833b78
        A/table-images/TABLE-3-page-9-1.png: be95bf69b9bf1c5f2839890177980b8f7b5977d9b1d7b808c337f78f23c7c25a
        A/table-images/TABLE-1-page-7-1.png: 85b41857a713e18358c022b28b9d6b4c33bd84ebd747dbf82718986f35302fb4
        A/table-images/page-11.png: e087011565c733659f87535a8ef9fccc9b1215d405908734caa100f291ceb56b
        A/table-images/TABLE-2-page-8-1.png: e0228e6d7ea98c2566a5e3a486936e0004f63545015dde3cc4f1d7bd7832a067
        A/table-images/page-7.png: ae2b402a2e74fe06600665a915f05b5f0ed84048b6627a73fc8ed48e7a2bfc75
        A/table-images/TABLE-4-page-11-1.png: 53ccf3e0cf28ce6b40d3f83aa161bdebd443130f99c6245ca6db13bbe84c0072
        A/table-images/page-9.png: cae024a094da4cecfa7d1d582da4db1483bd09b7b21c79694a3a1968e3b16646
        A/table-images/page-8.png: 26668b9d21a3c29dba81116e35d85ad1b48518e06f5e8109d2d0b7e5f0d123fb
        A/table-images/manifest.json: ed4bf8b2c88e159d2a1c82ed737be0ea3334c08dc16e7b3be8f65a42fd77c284
        A/table-images/TABLE-6-page-13-1.png: c0b6f76c124d70fd184c9f28d2c6fe28aa625d2cc3bc8cd1e99d801439a2c91d
        A/table-images/TABLE-5-page-12-1.png: 5d26122cfca4c972664f8a89b41455ff1ec7a3cd694de8cbdf76f8a0ed2d3cdd
        A/clauses/window-11/raw.json: e20a3d3c6c36d25c288b49b85f51980be6407bb7f7a61500b3d7d6bd5ca11784
        A/clauses/window-11/prompt.txt: 90f6db8bd5580941e39b369119401ab772033dc3682f726a84c8f83591e20abc
        A/clauses/window-11/meta.json: a8f0efd5877d5006cdff1f4cab59d721fe2d2b5413e715cb6ab6c9712d31360f
        A/clauses/window-10/raw.json: f1afd87894287ab1ac6d51633d35601d203dcf16fc52fd6ea7bcecf28a9c6443
        A/clauses/window-10/prompt.txt: 08855200def221488adb1263577f84b36aa03f106b193a8f444c60239486ed76
        A/clauses/window-10/meta.json: 735171ab10d98af8e5e40d370213423d1e96bde053335b41a941bdeffe63ce66
        A/clauses/window-03/raw.json: f94754c3a391c94b752118724d831d79c621ff83f98512e482316211af14c7cc
        A/clauses/window-03/prompt.txt: 36af5a70af7044a51a9921b143e1ec5f89f3d03278f75f2546a9d6a5653f3e7a
        A/clauses/window-03/meta.json: a91ea9ce15cfda5bef0e1a19527834404c998d8622fe90321c836fd18816861d
        A/clauses/window-04/raw.json: af08a087775971bd360fc2234048230a7527d52edae26c1ac38097a29b903f88
        A/clauses/window-04/prompt.txt: 2a8e27e2d4cb19b62432675f111a4d88da5751c11a2ddedd43ec5c195066a099
        A/clauses/window-04/meta.json: d8003d3503d35cbc22023146e4db4e58c9c2b70e29cc837b7399c458c23e363a
        A/clauses/window-05/raw.json: 327286b469777b37ab86043eb435eeff8d48cc0d1c5cecb14b40c046f876e1b0
        A/clauses/window-05/prompt.txt: 3002458982c18ae4dfef19d0b879dd83b1564ca07ea81269cbd28a67b890d25e
        A/clauses/window-05/meta.json: 19cb91d199a2bafab56c40afdaa4105f0bad76f1a256f59f4e9ba531661de018
        A/clauses/window-02/raw.json: 9a2d86dbbcb0dec9d4b580f63fb14e241d4979076be89eebd1726670a68be443
        A/clauses/window-02/prompt.txt: e45f5793099bd1801cd67e191045e3e41a6a89dac73158af9d9b605c3fa46b28
        A/clauses/window-02/meta.json: af433079938e3eea4a49ec112ec0d52eb578130bc88d879d1170940e1c58bbb2
        A/clauses/window-12/raw.json: 5b6eafcb5946bbfe9ba8f70a981efefd018cec09d2cc5f2c0d29c28890d584b3
        A/clauses/window-12/prompt.txt: 18ae09b3085476ee52f7ecb198af87ff2f00460f34379c88cdc4131c0c08c813
        A/clauses/window-12/meta.json: 55154fa4bd8b547e707c1f9eb19a8cb664c3b344ce66ae3a62a0015567c56eb8
        A/clauses/window-13/raw.json: 366a7f4c2fda218e9f30695c4d87173298e973d11f23132cde7690903bd6660a
        A/clauses/window-13/prompt.txt: 049dea359c382bff351cc0df363bde772c6d9085e151e3e9286294855bca5f66
        A/clauses/window-13/meta.json: c2966433b236cbc1e68e2733b4297452fd966a2dc996d55b0b8a33d9ff7b1383
        A/clauses/window-14/raw.json: 214fc7ee2876aed430112e3172c899103be38270ea801ef3c989fb697ed27d25
        A/clauses/window-14/prompt.txt: a8aa3201a398c6ec66f8e8ea991f4c960f690d31a542df93f219bb73fd580963
        A/clauses/window-14/meta.json: 73d7a62a61269b4630de8bd0d9cf1876bdb51f0e3fbf7e95ce802951f7353871
        A/clauses/window-09/raw.json: 1334001311db8674a47ede79297ff25ce90a4ba86402082b446405bf00066d56
        A/clauses/window-09/prompt.txt: 106e431a1ae43b3f1c6df88b2d306368330bf8a7273684b3b87ffc7703a56497
        A/clauses/window-09/meta.json: 3cdc137d32bf44362acc7494268ae5a6f80e5a1970fe40931ce306f12f2fb322
        A/clauses/window-07/raw.json: 2ed8e5e2b0da4b663b54ef2ad7503a19359dcb0e61daaad5bff26c2d9f53518c
        A/clauses/window-07/prompt.txt: f8f29a9cae82184fd2e8a1f68e76e9cbb59e2c4df05bb0122c9578a6f722b3cf
        A/clauses/window-07/meta.json: 736829d8f838b5045be2dff9241620bfd59ffcf7a8d7bf70fa542a0b9eaec6b0
        A/clauses/window-01/raw.json: fe8304b2cfc58add905fcae0b1e2d4ad01cf9d971fcc446d4e31e83600597f94
        A/clauses/window-01/prompt.txt: 292ed45907c76d07c93fd676fc3f3e31f9771b7d14be3faf75a0ca143ad4cca6
        A/clauses/window-01/meta.json: 8afd65c122f15a3bc1ee74527b92830c295a2a7da88e29630680f937156aecd9
        A/clauses/window-06/raw.json: 0776be8a153aef65953950cd7437e0976d387f4453f7f2251d72038f92f1b36a
        A/clauses/window-06/prompt.txt: bcad3eb7bf47d9f8f55f15c2ee75a9f10f0ea6afd63e5f90e903cdf1cddf040a
        A/clauses/window-06/meta.json: e8cd29c5c2777e5eda7a6061d7c9f37882a54d581b5f949a729e5ca4f2a090f9
        A/clauses/window-08/raw.json: 1cc1963e54f98d1083ee2009106e672c38656fad5056aa791a2472c43d85b872
        A/clauses/window-08/prompt.txt: 6bb0da02bb62d4288a32fa651c4e0800a3d581926f3c01e46583fd7ed3dccf44
        A/clauses/window-08/meta.json: 8f47945a11ef776ab9e8809223e3c15485b8f124021935b3cedbcb94ae65ae2d
        A/tables/TABLE-4-page-11-5/raw.json: 1c2a76d8fdf6de30ff8f3c35e6d561baa676d0a7c2934bbb2665fe4621800626
        A/tables/TABLE-4-page-11-5/prompt.txt: 8a75668847caa213b28eae120a01f888aff8db45f19b137fff7d4aae45c2ae69
        A/tables/TABLE-4-page-11-5/meta.json: ede0e72ded1c3146f6ee4d8958d078ef08e73996ddb38fda97d4a9916caa08e4
        A/tables/TABLE-2-page-8-2/raw.json: c8929cd45ccc370ddaa5e060d44ba9b61f0245a2da069adc3e0ac538846c1ae0
        A/tables/TABLE-2-page-8-2/prompt.txt: 091356fc22ae9e0370cbd52686734d8dc0e32c03da87d3bdb0115fdccb8fdcd9
        A/tables/TABLE-2-page-8-2/meta.json: 0778db872865532d84cd73ac0eef4b3c75df94d5b7e213b5ddb2d50e40bce38f
        A/tables/TABLE-1-page-7-1/raw.json: bf24c86fbd75324ffbaf0c97dbcb34c7813903a3f0506e3f6d844e0122080537
        A/tables/TABLE-1-page-7-1/prompt.txt: 9f0e13c2a881dd3fcfada4c0bd4d799f2b207291ef410e549f95374131edb264
        A/tables/TABLE-1-page-7-1/meta.json: 74428f1de54426b3af3462c042c4384f87ad0ad777e5d5b00e701e3c08254bf1
        A/tables/TABLE-3-page-10-4/raw.json: 3b421ec141e06c3ed1543a4755f8d24786a4c3759ed1619e96078f585d10b49d
        A/tables/TABLE-3-page-10-4/prompt.txt: 01a3921c74398973d277da9f9135f8201bf1de9387d4c47fc65503ecdfc3e781
        A/tables/TABLE-3-page-10-4/meta.json: f153cc0f746ef80a1549cabfbc9f8428054a03b8fd61eb7f66b5eb176b3f4f09
        A/tables/TABLE-5-page-12-6/raw.json: f97d63c4a0b48498bbf3219d6c0cae38b1b77f28ffe81f0cb06202319015e5f2
        A/tables/TABLE-5-page-12-6/prompt.txt: bdaea8a58c102f7f127aaa132ac0fc686e758d8d9aaefb807680f8863368f88e
        A/tables/TABLE-5-page-12-6/meta.json: 3d25bf797186536dceae0962c364d071d6404c81ae185539a3b2b8b37f5ed5eb
        A/tables/TABLE-3-page-9-3/raw.json: 1003576b365b6087b2e215865d6c2e9e893622b266b6c1bcb94d7068cb0477b6
        A/tables/TABLE-3-page-9-3/prompt.txt: da39bd76d29180b79e92f9700cfdc4318cdb088f5b1269db0993db22391245c4
        A/tables/TABLE-3-page-9-3/meta.json: defacce7c16bcc6d86dbfbbfce3df1bf453c114e0e45fc7c4be0ea2aabf4a57b
        A/tables/TABLE-6-page-13-7/raw.json: d4105798d6e77838494ba721ab6b2961850f187b8aa82db4b22284b07e3c9daa
        A/tables/TABLE-6-page-13-7/prompt.txt: 12b4e490f255f0913be2a274040b007b4a3cabaf9b1c9ad6352bd35fb1711fe2
        A/tables/TABLE-6-page-13-7/meta.json: dc924ba380f91ad424d5205055f17741752793e9d78ac8e2e3f50ebc201d63b1
        B/passages.json: 58b74711cafea0b183c1dd9de9c5ee40de6dccf4c8414bbb0d6951d45c5eccda
        B/raw.json: f8c8d78b934b81ca3cf74378f3e16b20ec162f8215c7b681caa7174190ce405b
        B/source-units.json: fc090d70c633262bbdb9fb19da54dc0d097cb070b9f0f0b36f14f210aedd8942
        B/full-source-units.json: 216290e0c7e4ae816423030ab10b04a386b365ca05ded0f66b219ccdf84dcd5e
        B/meta.json: 7b45f26b8cef83dca3107028cd8bfa10d11a2396383b7ffe811de933d10921f8
        B/table-images/TABLE-3-page-10-1.png: fd8aa7fef241b0f4d6b7daf368cf0c4522abd824eda43bb568b5885dc4dca173
        B/table-images/page-13.png: 6875ada03d9aca889757887933114066f363147270f8541e4c8888657eb5a776
        B/table-images/page-12.png: b593d093399a6c4326713b9f5aad691da3eb454773fc3fa65ea6f15cfba07da2
        B/table-images/page-10.png: 14cd645ddf06831f62a5e767977b690af6b2d45f0e92159f847fee9266833b78
        B/table-images/TABLE-3-page-9-1.png: be95bf69b9bf1c5f2839890177980b8f7b5977d9b1d7b808c337f78f23c7c25a
        B/table-images/TABLE-1-page-7-1.png: 85b41857a713e18358c022b28b9d6b4c33bd84ebd747dbf82718986f35302fb4
        B/table-images/page-11.png: e087011565c733659f87535a8ef9fccc9b1215d405908734caa100f291ceb56b
        B/table-images/TABLE-2-page-8-1.png: e0228e6d7ea98c2566a5e3a486936e0004f63545015dde3cc4f1d7bd7832a067
        B/table-images/page-7.png: ae2b402a2e74fe06600665a915f05b5f0ed84048b6627a73fc8ed48e7a2bfc75
        B/table-images/TABLE-4-page-11-1.png: 53ccf3e0cf28ce6b40d3f83aa161bdebd443130f99c6245ca6db13bbe84c0072
        B/table-images/page-9.png: cae024a094da4cecfa7d1d582da4db1483bd09b7b21c79694a3a1968e3b16646
        B/table-images/page-8.png: 26668b9d21a3c29dba81116e35d85ad1b48518e06f5e8109d2d0b7e5f0d123fb
        B/table-images/manifest.json: e0706c79c30da47ef5ee1604161df11e371291930f3c4167a67c357c647bc9ac
        B/table-images/TABLE-6-page-13-1.png: c0b6f76c124d70fd184c9f28d2c6fe28aa625d2cc3bc8cd1e99d801439a2c91d
        B/table-images/TABLE-5-page-12-1.png: 5d26122cfca4c972664f8a89b41455ff1ec7a3cd694de8cbdf76f8a0ed2d3cdd
        B/clauses/window-11/raw.json: f3f0af05889dad2482047cb1e162d7d533a9c3f9c2b4062df0a4a81da83a26f0
        B/clauses/window-11/prompt.txt: 90f6db8bd5580941e39b369119401ab772033dc3682f726a84c8f83591e20abc
        B/clauses/window-11/meta.json: faadbb787bd89ae654d85d972929db69392fbf929b7c3955e57060d1b43118be
        B/clauses/window-10/raw.json: 312ddb4343671918e1e241adae93001d2e6389bab34b46640e422be5990d92ef
        B/clauses/window-10/prompt.txt: 08855200def221488adb1263577f84b36aa03f106b193a8f444c60239486ed76
        B/clauses/window-10/meta.json: db1008590130f42de9a886bdb4aa066000926280e7ec90641451e4ffe904adb5
        B/clauses/window-03/raw.json: 0f941a59a2615bde6c168af5e7e39cceb839c0d417ba452b38f3d2d491b1d9e9
        B/clauses/window-03/prompt.txt: 36af5a70af7044a51a9921b143e1ec5f89f3d03278f75f2546a9d6a5653f3e7a
        B/clauses/window-03/meta.json: fe6849b25a9b5df51d4279553b68917a4cd404cc72f6d3d44341fceabfc5eb94
        B/clauses/window-04/raw.json: 19d9bdc6789af7725ef07edd853fe24a8375314fb1d8de8a6248e52b56377883
        B/clauses/window-04/prompt.txt: 2a8e27e2d4cb19b62432675f111a4d88da5751c11a2ddedd43ec5c195066a099
        B/clauses/window-04/meta.json: d144b5bf8fc4096c0c44358ba3d72af687c3c247d2595e613fc89532af4553b9
        B/clauses/window-05/raw.json: ed02f07011b1691a31fcbc00f806ecdac441c43c607cb4d434a082da3077f343
        B/clauses/window-05/prompt.txt: 3002458982c18ae4dfef19d0b879dd83b1564ca07ea81269cbd28a67b890d25e
        B/clauses/window-05/meta.json: 37372484c9d28d94a1eada333bd3a3a75a116877c60c29a8c3b8c45dd7bcbb76
        B/clauses/window-02/raw.json: 5f1ee3a10a90dec527303bcd50ca24fa8574aa97a3f08797b606e47d9ef205d9
        B/clauses/window-02/prompt.txt: e45f5793099bd1801cd67e191045e3e41a6a89dac73158af9d9b605c3fa46b28
        B/clauses/window-02/meta.json: b214666e6c18dcbaed33dc9fe17c2a8bfbd6b8d3be104103d1be30756cfba303
        B/clauses/window-12/raw.json: 20b5adc0107bbf595b135703a90876513d3e5f1ddedde15da5ca757efe37b8bf
        B/clauses/window-12/prompt.txt: 18ae09b3085476ee52f7ecb198af87ff2f00460f34379c88cdc4131c0c08c813
        B/clauses/window-12/meta.json: 72332cf3511d60bbb9943b563936d156da2337abadd9e2991829fcbf5052dd3d
        B/clauses/window-13/raw.json: e4fee8522ec4bf82a1649bd805f62c7bb99ff0e97e3e98a5bd0f6f69f0643ae2
        B/clauses/window-13/prompt.txt: 049dea359c382bff351cc0df363bde772c6d9085e151e3e9286294855bca5f66
        B/clauses/window-13/meta.json: ec1229c165f6e1fc9c67d58ff18b873434d01ef325675d965871606b865b3057
        B/clauses/window-14/raw.json: 9558bc44d22fd8713eafa084ac10862615308bf75720c1d208555120d8e9e5d8
        B/clauses/window-14/prompt.txt: a8aa3201a398c6ec66f8e8ea991f4c960f690d31a542df93f219bb73fd580963
        B/clauses/window-14/meta.json: ab43995957aeaf65e24cec72a2f0b0b95847ea2408f511d0a55053de54f9b1fe
        B/clauses/window-09/raw.json: 04a47c2ffedce748cf77f241c84af00343150d241f25aff2f4cfe625f3ad8d98
        B/clauses/window-09/prompt.txt: 106e431a1ae43b3f1c6df88b2d306368330bf8a7273684b3b87ffc7703a56497
        B/clauses/window-09/meta.json: a35db03bb685bda774512409920066223cd63085001a3242b578d7ff9ec94d14
        B/clauses/window-07/raw.json: 134c65e2c9c414afd4908f775a5b24ebcd1585401bab786b41bb5f173c33b467
        B/clauses/window-07/prompt.txt: f8f29a9cae82184fd2e8a1f68e76e9cbb59e2c4df05bb0122c9578a6f722b3cf
        B/clauses/window-07/meta.json: 5a52c51e1ed1859b282bdc23d15a1e29ec158d36d443707c713ef37e5e9abfdb
        B/clauses/window-01/raw.json: cb0a7d9a053cb19c0546423b3ef47a94fc97eaea5b298052efcd33e13fa06dfb
        B/clauses/window-01/prompt.txt: 292ed45907c76d07c93fd676fc3f3e31f9771b7d14be3faf75a0ca143ad4cca6
        B/clauses/window-01/meta.json: 192bea6c8461ad63a260338f73fabdd5bf467d43e460cad3539c73814fdc3fc1
        B/clauses/window-06/raw.json: 4be84a3a93d3a8db16981bee14afaf20168e55e67b65cc1b209e45bfff4f4627
        B/clauses/window-06/prompt.txt: bcad3eb7bf47d9f8f55f15c2ee75a9f10f0ea6afd63e5f90e903cdf1cddf040a
        B/clauses/window-06/meta.json: a233c1fab540f8ea94142fea7a9b6e1252c938eeb26e52dba2c87491de8d78db
        B/clauses/window-08/raw.json: ca2260d77954b44a3d034f1246adc09882e2831bde27ebc759299df3ac2a49a0
        B/clauses/window-08/prompt.txt: 6bb0da02bb62d4288a32fa651c4e0800a3d581926f3c01e46583fd7ed3dccf44
        B/clauses/window-08/meta.json: 197125daed2ecc1d0112d586144acb91f1018f0bdcd1fee67a24b92a181c0597
        B/tables/TABLE-4-page-11-5/raw.json: 36d2c8fa82a2ba7767745f03ecd1125ce47cc3809340fe28d21ab2fff0e42a6e
        B/tables/TABLE-4-page-11-5/prompt.txt: 8a75668847caa213b28eae120a01f888aff8db45f19b137fff7d4aae45c2ae69
        B/tables/TABLE-4-page-11-5/meta.json: 167dc86ba0879a521a059ff53cef1195153f2369bab4ba8e438c2144f2aaf069
        B/tables/TABLE-2-page-8-2/raw.json: d6ad61956a031af2f8a7ca377f01b100311bd7407ec4011a5306228c7b4932e3
        B/tables/TABLE-2-page-8-2/prompt.txt: 091356fc22ae9e0370cbd52686734d8dc0e32c03da87d3bdb0115fdccb8fdcd9
        B/tables/TABLE-2-page-8-2/meta.json: 8f4b559e19e5e2cfe93481e9e8b5b688bdac490b50980df9b27c90cd55eb9b4c
        B/tables/TABLE-1-page-7-1/raw.json: 1ed6c4edebab55bfecaad8b95c38121fb69f05fc45d438f4a89efb6953906d67
        B/tables/TABLE-1-page-7-1/prompt.txt: 9f0e13c2a881dd3fcfada4c0bd4d799f2b207291ef410e549f95374131edb264
        B/tables/TABLE-1-page-7-1/meta.json: 704025b697356d3c2a37d9d8ad8372b15100bd83ea280b08fab6b2bb758b347c
        B/tables/TABLE-3-page-10-4/raw.json: 4b06ab257a6a260515910e5c116fcb7c89bda59dd15e26150728f20c0effda22
        B/tables/TABLE-3-page-10-4/prompt.txt: 01a3921c74398973d277da9f9135f8201bf1de9387d4c47fc65503ecdfc3e781
        B/tables/TABLE-3-page-10-4/meta.json: 83f49bdb58bb384e335e011cb4433a1b2027967e249bbedbe8cb247f829f7f7f
        B/tables/TABLE-5-page-12-6/raw.json: ad5cbb07a13758d5d6b9381bb54381dcd29eb9f3762b3bbfa6ab8909d3dd54aa
        B/tables/TABLE-5-page-12-6/prompt.txt: bdaea8a58c102f7f127aaa132ac0fc686e758d8d9aaefb807680f8863368f88e
        B/tables/TABLE-5-page-12-6/meta.json: dbee58aca577f47010dcf9d913564f2b750e962451d4bea15043132f1fcb12ae
        B/tables/TABLE-3-page-9-3/raw.json: ac3fe265df0185203c40cfb8fe6e79d6cf5ca1c41b60b720010d374cd93bf35e
        B/tables/TABLE-3-page-9-3/prompt.txt: da39bd76d29180b79e92f9700cfdc4318cdb088f5b1269db0993db22391245c4
        B/tables/TABLE-3-page-9-3/meta.json: 641b3c38c91ec1fe3f3fda0b2af277219190286fc7823641af56b392955e7658
        B/tables/TABLE-6-page-13-7/raw.json: b88fa5afdd62d87320fa33b956a8a2e2edaa58293b7e187fd3eed78cfb40278e
        B/tables/TABLE-6-page-13-7/prompt.txt: 12b4e490f255f0913be2a274040b007b4a3cabaf9b1c9ad6352bd35fb1711fe2
        B/tables/TABLE-6-page-13-7/meta.json: 023ebd24c693432e9f28dd12f270793ca3856efc4024fcfbdfbeb3fa81fb3a27
      code:
        relationship_review.py: 6d0359072ca11a7569362fe49703755a98b4207ba814fcd311161c48936053ed
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
      pdf_sha256: c8562d7b60d51b5ec07c8d06adda9523b0af176ca21610d4d53af3f26f94ec8a
      source_review: _compare/relationships-2026-11-16/review-current/Efstratiadou2018
      source_status_sha256: 0058c33ec42a27f561ff06fa2e3be620acb330938e57076aa55d21496f4b405b
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R005
    exposure:
      text: semantic feature analysis (SFA)
    outcome:
      text: naming of trained items
    analysis_label: SFA efficacy by aphasia type (trained items)
    relation: treatment_effect
    evidence_ids:
    - P10-S2-C7
    - P10-S2-C8
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
      pdf_sha256: c8562d7b60d51b5ec07c8d06adda9523b0af176ca21610d4d53af3f26f94ec8a
      source_review: _compare/relationships-2026-11-16/review-current/Efstratiadou2018
      source_status_sha256: 0058c33ec42a27f561ff06fa2e3be620acb330938e57076aa55d21496f4b405b
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P1-S1-C7
      - Result passage disposed without unit P4-S2-C11
      - Result passage disposed without unit P4-S3-C3
      - Result passage disposed without unit P6-S1-C13
      - Result passage disposed without unit P6-S1-C14
      - Result passage disposed without unit P6-S2-C11
      - Result passage disposed without unit P6-S2-C12
      - Result passage disposed without unit P6-S2-C9
      - Result passage disposed without unit P6-S2-C13
      - Result passage disposed without unit P6-S3-C5
      - Result passage disposed without unit P6-S3-C7
      - Result passage disposed without unit P6-S3-C9
      - Accounting without a linked unit P10-S1-C7
      - Accounting without a linked unit P10-S1-C8
      - Accounting without a linked unit P10-S1-C9
      - Unaccounted source passage P10-S1-C9
      - Unaccounted source passage P10-S1-C7
      - Unaccounted source passage P10-S1-C8
      - Result passage disposed without unit P10-S1-C10
      - Result passage disposed without unit P10-S2-C4
      - Accounting without a linked unit P10-S2-C5
      - Accounting without a linked unit P10-S2-C7
      - Accounting without a linked unit P10-S2-C8
      - Unaccounted source passage P10-S2-C8
      - Unaccounted source passage P10-S2-C7
      - Unaccounted source passage P10-S2-C5
      - Accounting without a linked unit P12-S1-C2
      - Accounting without a linked unit P12-S1-C5
      - Accounting without a linked unit P12-S1-C6
      - Unaccounted source passage P12-S1-C2
      - Unaccounted source passage P12-S1-C6
      - Unaccounted source passage P12-S1-C5
      - Result passage disposed without unit P12-S1-C14
      - Accounting without a linked unit P12-S2-C2
      - Accounting without a linked unit P12-S2-C3
      - Unaccounted source passage P12-S2-C3
      - Unaccounted source passage P12-S2-C2
      - Accounting without a linked unit P12-S2-C5
      - Accounting without a linked unit P12-S2-C6
      - Accounting without a linked unit P12-S2-C7
      - Unaccounted source passage P12-S2-C6
      - Unaccounted source passage P12-S2-C5
      - Unaccounted source passage P12-S2-C7
      - Result passage disposed without unit P14-S1-C3
      - Result passage disposed without unit P14-S1-C4
      - Result passage disposed without unit P14-S1-C5
      - Result passage disposed without unit P15-S1-C4
      - Result passage disposed without unit P15-S1-C5
      - Result passage disposed without unit P15-S1-C6
      - 'window 33: invalid/duplicate disposition P15-S1-C9'
      - Result passage disposed without unit P15-S1-C9
      unattached_null_or_qualifier_ids:
      - P6-S2-C9
      - P6-S2-C12
      - P12-S1-C5
      suppressed_nonrepresented_units: 22
      default_disposition_count_requires_completeness_check: 308
      unselected_timing_passages:
      - P12-S1-C4
      - P12-S1-C5
      - P12-S1-C6
      - P12-S1-C7
      - P12-S1-C8
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P1-S1-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S2-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S2-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S2-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S1-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P14-S1-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P14-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P14-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P14-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P15-S1-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P15-S1-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P5-S1-C6
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: tested_personal_effects
        source_id: P14-S3-C8
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P14-S3-C9
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P15-S1-C7
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: analysed_sample
        source_ids:
        - P1-S1-C6
        - P2-S2-C11
        - P3-S1-C7
        - P3-S1-C11
        - P4-S2-C9
        - P4-S3-C6
        - P6-S1-C13
        - P7-S1-C10
        - P7-S1-C11
        - P7-S1-C12
        - P7-S1-C13
        - P7-S1-C15
        - P7-S1-C16
        - P7-S1-C17
        - P7-S1-C18
        - P14-S1-C1
        - P15-S1-C9
        - P15-S1-C11
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: recruited_sample
        source_ids:
        - P1-S1-C6
        - P2-S2-C11
        - P3-S1-C7
        - P3-S1-C11
        - P4-S1-C16
        - P5-S2-C7
        - P6-S3-C4
        - P7-S1-C10
        - P7-S1-C11
        - P7-S1-C12
        - P7-S1-C13
        - P7-S1-C15
        - P7-S1-C16
        - P7-S1-C17
        - P7-S1-C18
        - P9-S1-C5
        - P10-S1-C11
        - P10-S1-C12
        - P10-S1-C13
        - P10-S1-C14
        - P10-S1-C15
        - P10-S1-C16
        - P10-S1-C17
        - P14-S1-C1
        - P15-S1-C9
        - P15-S1-C11
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: eligibility
        source_ids:
        - P4-S1-C1
        - P4-S1-C13
        - P4-S1-C14
        - P4-S2-C2
        - P4-S2-C3
        - P4-S2-C4
        - P4-S2-C6
        - P4-S2-C8
        - P7-S1-C10
        - P7-S1-C11
        - P7-S1-C12
        - P7-S1-C13
        - P7-S1-C15
        - P7-S1-C16
        - P7-S1-C17
        - P7-S1-C18
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: outcome_timing
        source_ids:
        - P10-S2-C3
        - P10-S2-C7
        - P10-S2-C9
        - P10-S2-C10
        - P12-S1-C3
        - P12-S1-C5
        - P12-S1-C6
        - P12-S1-C7
        - P12-S1-C8
        - P14-S1-C8
        - P14-S1-C10
        - P14-S1-C12
        - P14-S1-C13
        - P15-S1-C10
        - P15-S1-C11
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: outcome_definition
        source_ids:
        - P1-S1-C5
        - P1-S1-C9
        - P3-S1-C7
        - P3-S1-C9
        - P3-S1-C15
        - P3-S2-C9
        - P6-S1-C3
        - P6-S1-C5
        - P10-S1-C13
        - P10-S2-C6
        - P12-S1-C9
        - P14-S1-C3
        - P14-S1-C4
        - P14-S1-C5
        - P14-S1-C6
        - P15-S1-C10
        - P15-S1-C11
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: descriptive_personal_factors
        source_ids:
        - P1-S1-C6
        - P2-S2-C11
        - P3-S1-C8
        - P3-S1-C12
        - P3-S2-C4
        - P3-S2-C8
        - P5-S2-C1
        - P5-S2-C2
        - P5-S2-C3
        - P5-S2-C4
        - P5-S2-C5
        - P6-S3-C3
        - P6-S3-C4
        - P6-S3-C5
        - P6-S3-C6
        - P6-S3-C7
        - P6-S3-C8
        - P6-S3-C9
        - P9-S1-C6
        - P9-S1-C7
        - P9-S1-C8
        - P9-S1-C9
        - P10-S1-C6
        - P10-S1-C7
        - P10-S1-C8
        - P10-S1-C9
        - P10-S1-C10
        - P10-S1-C11
        - P10-S1-C12
        - P10-S1-C15
        - P10-S1-C16
        - P10-S1-C17
        - P10-S2-C13
        - P10-S2-C14
        - P10-S2-C15
        - P14-S2-C10
        - P14-S3-C3
        - P14-S3-C4
        - P14-S3-C5
        - P15-S1-C9
        - P15-S1-C11
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - analysed_sample
      - recruited_sample
      - eligibility
      - imaging_provenance
      - imaging_timing
      - outcome_timing
      - outcome_definition
      - validation
      - personal_factors
      - tested_personal_effects
      - adjustment_roles
      - explicitly_not_adjusted
      - descriptive_personal_factors
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-7-1
      - TABLE-2-page-8-2
      - TABLE-3-page-10-4
      - TABLE-3-page-9-3
      - TABLE-4-page-11-5
      - TABLE-5-page-12-6
      - TABLE-6-page-13-7
      unlinked_tables:
      - TABLE-2-page-8-2
      - TABLE-4-page-11-5
      - TABLE-6-page-13-7
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P2-S3
        - P3-S2
        - P4-S2
        - P4-S3
        - P5-S2
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: c8562d7b60d51b5ec07c8d06adda9523b0af176ca21610d4d53af3f26f94ec8a
      source_review: _compare/relationships-2026-11-16/review-current/Efstratiadou2018
      source_status_sha256: 0058c33ec42a27f561ff06fa2e3be620acb330938e57076aa55d21496f4b405b
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the number of studies and participants reviewed.
    - source_id: P1-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the types of studies included.
    - source_id: P1-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports the average quality score of included studies.
    - source_id: P1-S1-C9
      disposition: represented
      result_indexes:
      - 0
      reason: Reports improvement in naming of trained items.
    - source_id: P1-S1-C10
      disposition: represented
      result_indexes:
      - 1
      reason: Reports small treatment effect size.
    - source_id: P4-S1-C16
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the study selection process.
    - source_id: P4-S1-C18
      disposition: background_or_descriptive
      result_indexes: []
      reason: Lists excluded studies.
    - source_id: P4-S2-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Lists excluded studies.
    - source_id: P4-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Lists excluded studies.
    - source_id: P4-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Lists excluded studies.
    - source_id: P4-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Lists excluded studies.
    - source_id: P4-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Lists excluded studies.
    - source_id: P4-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Lists excluded studies.
    - source_id: P4-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: States the number of included articles.
    - source_id: P4-S2-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the areas covered by the studies.
    - source_id: P4-S3-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the areas covered by the studies.
    - source_id: P4-S3-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: States that all studies were single case studies.
    - source_id: P5-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports intrarater reliability of the SCED Scale.
    - source_id: P6-S1-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: States the number of included studies.
    - source_id: P6-S1-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the research areas covered.
    - source_id: P6-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports SCED Scale scores.
    - source_id: P6-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Assigns level of evidence to studies.
    - source_id: P6-S2-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Categorizes studies by treatment phase.
    - source_id: P6-S2-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Categorizes studies by treatment phase.
    - source_id: P6-S2-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Categorizes studies by treatment phase.
    - source_id: P6-S3-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: States total number of participants.
    - source_id: P6-S3-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports range and mean of total treatment amount.
    - source_id: P6-S3-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes noun SFA studies.
    - source_id: P6-S3-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes noun SFA treatment duration and dosage.
    - source_id: P6-S3-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes verb SFA studies.
    - source_id: P6-S3-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes verb SFA treatment duration and dosage.
    - source_id: P10-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes studies comparing SFA to PCA.
    - source_id: P10-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes participant heterogeneity.
    - source_id: P10-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports age range and mean.
    - source_id: P10-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports time post onset range and mean.
    - source_id: P10-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports gender distribution.
    - source_id: P10-S1-C19
      disposition: represented
      result_indexes:
      - 0
      reason: Reports improvement in naming of trained items.
    - source_id: P10-S2-C3
      disposition: represented
      result_indexes:
      - 2
      reason: Reports maintenance of naming of trained items.
    - source_id: P10-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes range of generalization effects.
    - source_id: P10-S2-C5
      disposition: represented
      result_indexes:
      - 3
      reason: Reports percentage of generalization to untrained items.
    - source_id: P10-S2-C7
      disposition: represented
      result_indexes:
      - 4
      reason: Reports improvement on trained items by aphasia type.
    - source_id: P10-S2-C8
      disposition: represented
      result_indexes:
      - 4
      reason: Reports negative outcomes for global and mixed aphasia.
    - source_id: P10-S2-C9
      disposition: represented
      result_indexes:
      - 5
      reason: Reports maintenance effects by aphasia type.
    - source_id: P10-S2-C10
      disposition: represented
      result_indexes:
      - 6
      reason: Reports generalization gains for Broca's aphasia.
    - source_id: P10-S2-C11
      disposition: represented
      result_indexes:
      - 6
      reason: Reports minimal generalization gains for other aphasia types.
    - source_id: P11-S1-C26
      disposition: represented
      result_indexes:
      - 0
      - 2
      - 3
      reason: Summary table of treatment outcomes (improvement, maintenance, generalization).
    - source_id: P12-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Restatement of generalization results.
    - source_id: P12-S1-C2
      disposition: represented
      result_indexes:
      - 6
      reason: Reports generalization gains by aphasia type.
    - source_id: P12-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes number of studies assessing maintenance.
    - source_id: P12-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes timing of maintenance assessments.
    - source_id: P12-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes timing of maintenance assessments.
    - source_id: P12-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes timing of maintenance assessments.
    - source_id: P12-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Lists studies reporting effect sizes.
    - source_id: P12-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Lists studies where effect size could not be calculated.
    - source_id: P12-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes how effect sizes were calculated by the author.
    - source_id: P12-S1-C14
      disposition: represented
      result_indexes:
      - 10
      reason: Introduces effect size results.
    - source_id: P12-S2-C2
      disposition: represented
      result_indexes:
      - 10
      reason: Reports number of participants with large effect sizes.
    - source_id: P12-S2-C3
      disposition: represented
      result_indexes:
      - 10
      reason: Reports number of participants with medium effect sizes.
    - source_id: P12-S2-C4
      disposition: represented
      result_indexes:
      - 10
      reason: Reports number of participants with small effect sizes.
    - source_id: P12-S2-C5
      disposition: represented
      result_indexes:
      - 10
      reason: Reports number of participants with negligible or no change in effect
        size.
    - source_id: P12-S2-C7
      disposition: represented
      result_indexes:
      - 11
      reason: Reports PND calculation for specific participants.
    - source_id: P12-S2-C8
      disposition: represented
      result_indexes:
      - 11
      reason: Reports magnitude of PND effect.
    - source_id: P12-S2-C9
      disposition: represented
      result_indexes:
      - 11
      reason: Reports overall clinical efficacy using PND.
    - source_id: P12-S2-C10
      disposition: represented
      result_indexes:
      - 11
      reason: Reports absence of ineffective treatment PND scores.
    - source_id: P14-S1-C3
      disposition: represented
      result_indexes:
      - 0
      reason: Restatement that SFA improved treated items.
    - source_id: P14-S1-C4
      disposition: represented
      result_indexes:
      - 1
      reason: Reports proportion of participants with small or less-than-small effect
        sizes.
    - source_id: P14-S1-C5
      disposition: represented
      result_indexes:
      - 3
      reason: Reports limited generalization to untrained items.
    - source_id: P14-S1-C6
      disposition: represented
      result_indexes:
      - 2
      reason: Reports maintenance of trained items.
    - source_id: P14-S1-C15
      disposition: represented
      result_indexes:
      - 3
      reason: Reports positive generalization outcomes for 40% of participants.
    - source_id: P15-S1-C10
      disposition: represented
      result_indexes:
      - 12
      reason: Reports outcomes for participants with low amount of treatment.
    - source_id: P15-S1-C11
      disposition: represented
      result_indexes:
      - 12
      reason: Reports outcomes for participants with high overall treatment amount.
    unresolved_coverage:
    - source_id: P15-S1-C10
      disposition: unresolved
      reason: Unknown result index; not accepted as coverage
    - source_id: P15-S1-C11
      disposition: unresolved
      reason: Unknown result index; not accepted as coverage
    - source_id: P12-S2-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S2-C12
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P14-S1-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P14-S1-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P14-S1-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P14-S1-C12
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P14-S3-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P14-S3-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P14-S3-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P15-S1-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P15-S1-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P15-S1-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P15-S1-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P15-S1-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P15-S1-C13
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C6
    - P1-S1-C7
    - P1-S1-C8
    - P4-S1-C16
    - P4-S1-C18
    - P4-S2-C1
    - P4-S2-C2
    - P4-S2-C5
    - P4-S2-C6
    - P4-S2-C7
    - P4-S2-C8
    - P4-S2-C9
    - P4-S2-C11
    - P4-S3-C3
    - P4-S3-C6
    - P5-S1-C7
    - P6-S1-C13
    - P6-S1-C14
    - P6-S2-C7
    - P6-S2-C9
    - P6-S2-C11
    - P6-S2-C12
    - P6-S2-C13
    - P6-S3-C4
    - P6-S3-C5
    - P6-S3-C6
    - P6-S3-C7
    - P6-S3-C8
    - P6-S3-C9
    - P10-S1-C1
    - P10-S1-C7
    - P10-S1-C8
    - P10-S1-C9
    - P10-S1-C10
    - P10-S2-C4
    - P12-S1-C1
    - P12-S1-C5
    - P12-S1-C6
    - P12-S1-C7
    - P12-S1-C8
    - P12-S1-C9
    - P12-S1-C10
    - P12-S1-C11
    - P12-S1-C14
    - P12-S2-C6
    - P12-S2-C7
    - P12-S2-C12
    - P14-S1-C8
    - P14-S1-C10
    - P14-S1-C11
    - P14-S1-C12
    - P14-S3-C4
    - P14-S3-C5
    - P15-S1-C4
    - P15-S1-C5
    - P15-S1-C6
    - P15-S1-C8
    - P15-S1-C9
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-7-1
    - TABLE-2-page-8-2
    - TABLE-3-page-10-4
    - TABLE-3-page-9-3
    - TABLE-4-page-11-5
    - TABLE-5-page-12-6
    - TABLE-6-page-13-7
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample: []
      recruited_sample: []
      eligibility: []
      imaging_provenance: []
      imaging_timing: []
      outcome_timing: []
      outcome_definition: []
      validation: []
      analysis_restrictions:
      - P3-S1-C10
      dependent_variable_statement:
      - P1-S1-C5
      - P3-S1-C7
      - P3-S1-C13
      - P3-S2-C9
      limitations:
      - P3-S1-C15
      - P14-S1-C13
      - P14-S2-C7
      - P14-S2-C14
      - P14-S4-C2
      - P15-S1-C2
      - P15-S1-C14
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles: []
      explicitly_not_adjusted: []
      descriptive_personal_factors: []
    outcome_type: both_reported
    imaging_vs_outcome: not_stated
    validation_type: mixed
    window_merge: Union of selected IDs; differing window enums retained conservatively
      as both/mixed. Not verified study-level facts.
    held_selections:
    - slot: dependent_variable_statement
      source_id: P1-S1-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S2-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S2-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S2-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S1-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P14-S1-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P14-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P14-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P14-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P15-S1-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P15-S1-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P5-S1-C6
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: tested_personal_effects
      source_id: P14-S3-C8
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P14-S3-C9
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P15-S1-C7
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: analysed_sample
      source_ids:
      - P1-S1-C6
      - P2-S2-C11
      - P3-S1-C7
      - P3-S1-C11
      - P4-S2-C9
      - P4-S3-C6
      - P6-S1-C13
      - P7-S1-C10
      - P7-S1-C11
      - P7-S1-C12
      - P7-S1-C13
      - P7-S1-C15
      - P7-S1-C16
      - P7-S1-C17
      - P7-S1-C18
      - P14-S1-C1
      - P15-S1-C9
      - P15-S1-C11
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: recruited_sample
      source_ids:
      - P1-S1-C6
      - P2-S2-C11
      - P3-S1-C7
      - P3-S1-C11
      - P4-S1-C16
      - P5-S2-C7
      - P6-S3-C4
      - P7-S1-C10
      - P7-S1-C11
      - P7-S1-C12
      - P7-S1-C13
      - P7-S1-C15
      - P7-S1-C16
      - P7-S1-C17
      - P7-S1-C18
      - P9-S1-C5
      - P10-S1-C11
      - P10-S1-C12
      - P10-S1-C13
      - P10-S1-C14
      - P10-S1-C15
      - P10-S1-C16
      - P10-S1-C17
      - P14-S1-C1
      - P15-S1-C9
      - P15-S1-C11
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: eligibility
      source_ids:
      - P4-S1-C1
      - P4-S1-C13
      - P4-S1-C14
      - P4-S2-C2
      - P4-S2-C3
      - P4-S2-C4
      - P4-S2-C6
      - P4-S2-C8
      - P7-S1-C10
      - P7-S1-C11
      - P7-S1-C12
      - P7-S1-C13
      - P7-S1-C15
      - P7-S1-C16
      - P7-S1-C17
      - P7-S1-C18
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: outcome_timing
      source_ids:
      - P10-S2-C3
      - P10-S2-C7
      - P10-S2-C9
      - P10-S2-C10
      - P12-S1-C3
      - P12-S1-C5
      - P12-S1-C6
      - P12-S1-C7
      - P12-S1-C8
      - P14-S1-C8
      - P14-S1-C10
      - P14-S1-C12
      - P14-S1-C13
      - P15-S1-C10
      - P15-S1-C11
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: outcome_definition
      source_ids:
      - P1-S1-C5
      - P1-S1-C9
      - P3-S1-C7
      - P3-S1-C9
      - P3-S1-C15
      - P3-S2-C9
      - P6-S1-C3
      - P6-S1-C5
      - P10-S1-C13
      - P10-S2-C6
      - P12-S1-C9
      - P14-S1-C3
      - P14-S1-C4
      - P14-S1-C5
      - P14-S1-C6
      - P15-S1-C10
      - P15-S1-C11
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: descriptive_personal_factors
      source_ids:
      - P1-S1-C6
      - P2-S2-C11
      - P3-S1-C8
      - P3-S1-C12
      - P3-S2-C4
      - P3-S2-C8
      - P5-S2-C1
      - P5-S2-C2
      - P5-S2-C3
      - P5-S2-C4
      - P5-S2-C5
      - P6-S3-C3
      - P6-S3-C4
      - P6-S3-C5
      - P6-S3-C6
      - P6-S3-C7
      - P6-S3-C8
      - P6-S3-C9
      - P9-S1-C6
      - P9-S1-C7
      - P9-S1-C8
      - P9-S1-C9
      - P10-S1-C6
      - P10-S1-C7
      - P10-S1-C8
      - P10-S1-C9
      - P10-S1-C10
      - P10-S1-C11
      - P10-S1-C12
      - P10-S1-C15
      - P10-S1-C16
      - P10-S1-C17
      - P10-S2-C13
      - P10-S2-C14
      - P10-S2-C15
      - P14-S2-C10
      - P14-S3-C3
      - P14-S3-C4
      - P14-S3-C5
      - P15-S1-C9
      - P15-S1-C11
      reason: Runaway selection (>8 passages); entire slot requires source review
    policy: All slots and enums remain unverified. Held selections are not evidence
      of absence. Original responses are preserved in frame/chunk-*/attempt-*/raw.json.
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
      pdf_sha256: c8562d7b60d51b5ec07c8d06adda9523b0af176ca21610d4d53af3f26f94ec8a
      review_sha256: 71453e86d91903d06b2957c7e7f267f13b820fc57127950d0f32df0aeb2c5e77
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
      - P10-S2-C8
      source_result: 'The source reports that improvement in naming of trained items
        was observed in the majority of participants across specific aphasia types:
        12/14 (85.71%) with Broca''s, 13/16 (81.25%) with anomic, 4/5 (80%) with Wernicke''s,
        9/9 (100%) with conduction, and 3/3 (100%) with transcortical motor aphasia.
        Conversely, negative outcomes were found for the two participants with global
        and mixed aphasia.'
      result_status: detected
      patient_measurement: non_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis (R005) and the proposed core both refer to
            the efficacy of SFA on trained items stratified by aphasia type. The source
            passages P10-S2-C7 and P10-S2-C8 explicitly provide these stratified results.
          source_ids:
          - P10-S2-C7
          - P10-S2-C8
        direction:
          answer: fits
          reason: The claim correctly identifies 'improvement' (positive effect) for
            the majority of aphasia types and 'negative outcomes' for global/mixed
            aphasia, matching the source text exactly.
          source_ids:
          - P10-S2-C7
          - P10-S2-C8
        construct:
          answer: fits
          reason: The exposure is SFA, the outcome is naming of trained items, and
            the population is persons with aphasia. The measurement is behavioral
            (naming performance), correctly classified as non_imaging.
          source_ids:
          - P10-S2-C7
          - P10-S2-C8
          - P2-S3-C9
        qualifications:
          answer: fits
          reason: The draft includes the critical qualification that the effect is
            specific to 'trained items' and notes the inclusion of both fluent and
            nonfluent types, which aligns with the source data.
          source_ids:
          - P10-S2-C7
          - P10-S2-C8
          - P10-S1-C11
        missing_material_caveat:
          answer: fits
          reason: The draft includes limitations regarding protocol heterogeneity
            and lack of standardization, which are material caveats found in the source
            (P14-S3-C11, P15-S1-C2). No material caveat changing the interpretation
            of the specific result is omitted.
          source_ids:
          - P14-S3-C11
          - P15-S1-C2
      optional_pending:
      - 'sample.population: source confirmation required; original proposed wording
        remains in the audit.'
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - 'sample.population: source confirmation required; original proposed wording
      remains in the audit.'
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - 'sample.population: source confirmation required; original proposed wording
      remains in the audit.'
    normalizations:
    - field: sample.population
      original: persons with aphasia (51 stroke, 4 TBI) with varying severity (mostly
        mild to moderate) and types
      action: not_transcribed
      reason: 'Numbers not grounded in usable selected source readings: 4'
    analysis_identity:
      id: R005
      exposure:
        text: semantic feature analysis (SFA)
      outcome:
        text: naming of trained items
      analysis_label: SFA efficacy by aphasia type (trained items)
      relation: treatment_effect
      evidence_ids:
      - P10-S2-C7
      - P10-S2-C8
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
        pdf_sha256: c8562d7b60d51b5ec07c8d06adda9523b0af176ca21610d4d53af3f26f94ec8a
        source_review: _compare/relationships-2026-11-16/review-current/Efstratiadou2018
        source_status_sha256: 0058c33ec42a27f561ff06fa2e3be620acb330938e57076aa55d21496f4b405b
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P6-S3-C4:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: c8562d7b60d51b5ec07c8d06adda9523b0af176ca21610d4d53af3f26f94ec8a
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: b3992147762dc9374cf3d262d74526b5adb6e9eeac366e18d4d84709c0037e0d
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P6-S3-C4
          page: 6
          text_layer_sha256: b3992147762dc9374cf3d262d74526b5adb6e9eeac366e18d4d84709c0037e0d
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'A to-

          tal of 55 participants have been treated in the included

          studies.'
        anchor_text: 'A to-

          tal of 55 participants have been treated in the included

          studies.'
        excluded_fragments: []
        image_sha256: 1019556ee2fd5e487c3d7f26b66acb279c64e11d2018c7f55bf5927fe5cf41fc
        transcription: . A total of 55 participants have been treated in the included
          studies
      P10-S1-C12:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: c8562d7b60d51b5ec07c8d06adda9523b0af176ca21610d4d53af3f26f94ec8a
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 4c0646a9973f707239e4279608d37cdc87b71bd6260b61fc407c2336bdc175e9
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P10-S1-C12
          page: 10
          text_layer_sha256: 4c0646a9973f707239e4279608d37cdc87b71bd6260b61fc407c2336bdc175e9
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Apha-

          sia was due to a stroke in 51 individuals and to traumatic

          brain injury in four individuals (neuropathology for three

          individuals was not reported).'
        anchor_text: 'Apha-

          sia was due to a stroke in 51 individuals and to traumatic

          brain injury in four individuals (neuropathology for three

          individuals was not reported).'
        excluded_fragments: []
        image_sha256: ecbaca70a02046afea201bd2b1524d76cb398e018f03b9fb1ff0040612d0d32f
        transcription: '. Apha-

          sia was due to a stroke in 51 individuals and to traumatic

          brain injury in four individuals (neuropathology for three

          individuals was not reported)'
      P4-S3-C6:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: c8562d7b60d51b5ec07c8d06adda9523b0af176ca21610d4d53af3f26f94ec8a
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 40672d84c04667aefa21b84f7ec8180dec7c51fd6147fc1b751df0cbc47c16f8
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P4-S3-C6
          page: 4
          text_layer_sha256: 40672d84c04667aefa21b84f7ec8180dec7c51fd6147fc1b751df0cbc47c16f8
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'All studies were single case

          studies (N = 21).'
        anchor_text: 'All studies were single case

          studies (N = 21).'
        excluded_fragments: []
        image_sha256: a507ead2a66bb8f94d0f7fb8188854850a425d93817a02e598bbc83922eda817
        transcription: '. All studies were single case

          studies (N = 21)'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 10
  quote: 'Twelve of the 14 (85.71%) participants with Broca’s

    aphasia, 13 of the 16 anomic participants (81.25%), four

    of the five (80%) individuals with Wernicke’s aphasia, and

    all nine with conduction aphasia and three with transcor-

    tical motor aphasia (100%) showed improvement on nam-

    ing of trained items.'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-23'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
