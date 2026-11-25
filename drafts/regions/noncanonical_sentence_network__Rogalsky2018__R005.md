---
id: noncanonical_sentence_network
name: noncanonical sentence comprehension cluster
kind: network
findings:
- id: f1
  outcome_measurement:
    status: identified
    instruments:
    - name: Sentence-picture matching task
    - name: Plausibility judgment task
    note: Canonical/noncanonical sentence contrasts, response-bias metrics and mixed stroke/lobectomy population
      remain in the source record.
  target_audit:
    status: behaviour_label_present
    category: behaviour_or_language_construct
    original_target: noncanonical_sentence_performance
    reason: Label names a behaviour or language construct; its exact operational definition and measurement
      still need source review.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  target: noncanonical_sentence_performance
  target_kind: impairment
  claim: Lower performance on noncanonical sentences (after regressing out variance
    due to canonical sentence performance) is associated with damage to a large left
    superior temporal-inferior parietal network, but not Broca's area.
  direction: likely
  relationship: correlational
  method: VLSM
  sample:
    n: not_reported
    population: Left-hemisphere patients with chronic focal cerebral damage (including
      stroke and unilateral left temporal lobectomy)
    phase: not_reported
    time_post_onset: Chronic phase (6 months or more post-onset for stroke patients)
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Temporal lobectomy patients may have experienced functional neural reorganization
    due to epilepsy or surgery
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Patient lesion overlap with a left superior temporal-inferior
    parietal network (including Heschl''s gyrus, STG, middle temporal gyrus, and supramarginal
    gyrus) as identified by VLSM for noncanonical sentence performance with canonical
    performance as a covariate. Analysis used a covariate approach to regress out
    variance due to canonical sentence performance; Findings were consistent across
    both the sentence-picture matching and plausibility judgment tasks. Additional
    metadata has not been transcribed; review the pending-field flags before approval.
    PDF image reading (P5-S1-C1, two-model agreement, human verification pending):
    chronic focal (6 months or more postonset) lesion due to

    a stroke in the left hemisphere (n = 48; 17 women, mean

    age = 62 years, range = 31–84 years) or a unilateral left tem-

    poral lobectomy (n = 18; 10 women, mean age = 46 years,

    range = 29–62 years),² (ii) no significant anatomical abnor-

    malities other than the signature lesion of their vascular

    event (or evidence of surgery for the seizure participants)

    nor signs of multiple strokes, and (iii) were administered

    both of the comprehension tasks of interest Original text-layer quotation is preserved
    below.'
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
    - not_transcribed:sample.n
    - proposed_concept:noncanonical_sentence_performance
  citation: '@Rogalsky2018'
  source_passages:
  - section: Original source P1-S1-C12
    page: 1
    quote: 'Using

      voxel-based lesion–symptom mapping, we find that lower per-

      formances on canonical and noncanonical sentences in each

      task are both associated with damage to a large left superior

      temporal–inferior parietal network including portions of the

      ATL, but not Broca’s area.'
    supports: claim
  - section: Original source P12-S1-C5
    page: 12
    quote: 'VLSM Results: Agrammatic Comprehension

      For both tasks, the VLSMs for performance on the non-

      canonical (OR and passive) sentences with canonical (SR

      and active) sentence performance as a covariate identi-

      fied large clusters of voxels spanning the left superior

      temporal lobe and, to a lesser extent, the inferior parietal

      lobe: Implicated regions include Heschl’s gyrus, STG,

      middle temporal gyrus, supramarginal gyrus, and under-

      lying white matter (for sentence–picture matching peak t

      at Talairach coordinates −35 −52 14 in the white matter

      underlying the posterior STG and number of voxels =

      19,650, for plausibility judgments peak t at Talairach

      coordinates −54 −26 5 and number of voxels = 13,109,

      p < .001, corrected; Figure 5).'
    supports: claim
  - section: Original source P16-S2-C4
    page: 16
    quote: 'VLSM of Noncanonical Sentence Comprehension

      The VLSMs investigating brain regions implicated in non-

      canonical sentence comprehension with canonical sen-

      tence comprehension performance as a covariate also

      identified superior temporal and inferior parietal regions

      in both tasks (Figure 5) consistent with the agrammatic

      comprehension lesion overlap findings (Figure 4).'
    supports: claim
  - section: Original source P5-S1-C1
    page: 5
    quote: '

      chronic focal (6 months or more postonset) lesion due to

      a stroke in the left hemisphere (n = 48; 17 women, mean

      age = 62 years, range = 31–84 years) or a unilateral left tem-

      poral lobectomy (n = 18; 10 women, mean age = 46 years,

      range = 29–62 years),2 (ii) no significant anatomical abnor-

      malities other than the signature lesion of their vascular

      event (or evidence of surgery for the seizure participants)

      nor signs of multiple strokes, and (iii) were administered

      both of the comprehension tasks of interest.'
    supports: sample
  - section: Original source P9-S2-C3
    page: 9
    quote: 'For each

      task, a VLSM was calculated for performance on the

      noncanonical sentences (object-relative and passive sen-

      tences), with performance on the canonical (subject-

      relative and active) sentences as a covariate.'
    supports: method
  - section: Original source P16-S2-C10
    page: 16
    quote: 'To summarize, our VLSMs of noncanonial sentence

      comprehension primarily implicate posterior temporal

      and inferior parietal regions with only partial extension

      into ATL regions previously implicated in sentence pro-

      cessing and no evidence of Broca’s area involvement.

      '
    supports: claim
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-25'
relationship_review:
  paper: Rogalsky2018
  proposal_id: R005
  review_status_sha256: 5c3d62d4c0072faaae65f9512bd50e2fc678ee126634127f5fceb18fb432270c
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: a58a5b9ea30eebd639e26d9c87b6e18640880907f66e87ba64024e442ba702b4
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: a58a5b9ea30eebd639e26d9c87b6e18640880907f66e87ba64024e442ba702b4
        A/passages.json: e6adde89dc789aab5279f2166f3c2e713cdc8eea67eeabf2953c2302d4eb19c1
        A/raw.json: 844de3a39780949cedbaf3d79d4a98dbab5a034b6476e1bad3c50da5cf39530a
        A/source-units.json: 28e3240c5d8e4f0ccf0ecf8bf46aa249f9787cdef2ec2956906e9452d5c8fc3d
        A/full-source-units.json: da7e50289e6929a62a0888cc4c5f5ef6bb50825e8033de28025ea0929ede949c
        A/meta.json: ff5cf54bdfb2be8cd06002931eaaad9e844fa793d01307a9f4e9873fed76901a
        A/table-images/TABLE-1-page-5-1.png: 7860a06eeb9516f7d99dff3d87334fb493345f088aa90d51b84ddd768eff9ad9
        A/table-images/TABLE-1-page-5-2.png: 9f048e6214ec6d261cec5f9692c1d1b30838ef69388f877c3f4f8981376790b7
        A/table-images/page-6.png: e977542b95ca428be2e8fe382c092f623666d97d4fd5c93ef7a82544062ec45f
        A/table-images/TABLE-3-page-8-1.png: 7e1b21cd3afdaaf1778185fcb8b6397dc0526df6147bd1988486665dd21227b7
        A/table-images/page-7.png: 7ef56e9a87e14d10e50a6e00252bbd176f2e682ec3fb12e95ce983909d722ecd
        A/table-images/page-5.png: 5723533e39e91b9ac343b861f3c501bfb1e3b8fde20c3e79c78d21154a060760
        A/table-images/TABLE-3-page-8-2.png: bc8629a5d005ea9576eca350466c26af69d6686b35515bbb690660cdab293ee1
        A/table-images/page-8.png: 99f4fadee855260bc500cfea051964cefbea4222a625876434da68bc0eb0a95d
        A/table-images/TABLE-2-page-6-1.png: ea39131c869819a05490e0e4883d6fef24170e824e3bbfb051c05d58c47bd465
        A/table-images/manifest.json: 2042fbacaca5b6709feb1520e719a0842418d61e33e76ef6dee0fc676608c29e
        A/table-images/TABLE-3-page-7-2.png: 352ff11181c983583e22f3081b71c743d3e485965cddaf8a2dae408111932ea5
        A/table-images/TABLE-3-page-7-1.png: 8c6d6d932a4d10715e694be6d1cdcb31a5b3f5f4e853443068109884e6135f2d
        A/table-images/TABLE-4-page-18-1.png: 4b03bb2033e8ad1f280d5ba92ba9742f64de887859de01610b39f7d12613b858
        A/table-images/page-18.png: b5143e1cfc347287212e0e1bc986b8c98a695938a1c2194cff62d11dc0b4981e
        A/clauses/window-11/raw.json: 8bc8c2f112eb81b9757611d083815482ad8af3255d350c342340533b9592064d
        A/clauses/window-11/prompt.txt: 02de844e5f606a87584f6d3380808932cce3bfc879366b5f67dcdd832c1903db
        A/clauses/window-11/meta.json: 758c14840c203bb5f1eaec8145d50e8fc5502f16de07d7371e44b3e71f703877
        A/clauses/window-16/raw.json: d2abe1c9c8e3650dc00e55a400c7f5c3b950ca06c0853e4d6c21c8accd917b6e
        A/clauses/window-16/prompt.txt: 2e037bb2a3edf201e8d9b236cec5646d17908322a692e191437d298238022f72
        A/clauses/window-16/meta.json: 0d84347813297a936979f78060e41cb98957972f66e9cf5e5397dbdd5b60195e
        A/clauses/window-10/raw.json: d77da7130260d7f833cb2ad23d7e1444c65399a5e761d5246f6c3c324e3f1c22
        A/clauses/window-10/prompt.txt: e0c3489c4996ffcad440ce89d7c7e1529d2ba52470558a55658662e484db5d87
        A/clauses/window-10/meta.json: 68a23621a016b10b77acf225bcd42efc1feb3583aa14b6e5e76b1532f0bc60aa
        A/clauses/window-03/raw.json: a3db383be7e4e977810fca3dc61202e76e99a0230b12edeea947f1ffc14242b3
        A/clauses/window-03/prompt.txt: d47d3cf96239d8b94c0ae02fe5be9aa817522ca81c99136ff3aa2cbda0473023
        A/clauses/window-03/meta.json: 630a0dedd813837f8127e28277283ee37dd1c6c7723e601f8521fdf51bc94fc6
        A/clauses/window-04/raw.json: 54ee6f2dcbfbb446f17ca234841b3aaf3a9c540be0cc2e37ebaced7ccb696778
        A/clauses/window-04/prompt.txt: 609d1373fbfaa1e33f1f108b939a8f43731f80fe86c1ec3be37169bba09a25fb
        A/clauses/window-04/meta.json: f4fca1939a92ad6a87ba56b580620ba72d4bcfff744b046d405556c6429c127c
        A/clauses/window-05/raw.json: 8cdffa985fbabe1c0df57f6a2dd1348097cf7c7d1a367e871856c6cbe9f7dae6
        A/clauses/window-05/prompt.txt: 53499c6831ed56a0f869ed35f7cb059a11d837b138a40c7ed7a8519b9054550d
        A/clauses/window-05/meta.json: d4678281e291c5965cbce047506712add3430ea7d6c18257dc4f160c0dbd02e6
        A/clauses/window-02/raw.json: f9efe920e493492b46c3c660b977e0964b52d0e29148e4d62c2fa902163d0506
        A/clauses/window-02/prompt.txt: e224210af1b6952e85bbe5a519fd3f1bb80cae3e5579512be94f66e5486b25c3
        A/clauses/window-02/meta.json: 46aeed4f0c2a924a1094492af35403ae12d1654f7d5f512c0a7998ea23cc94c0
        A/clauses/window-15/raw.json: 5b1346546e2be8389373b438b472507e314837b7bf1895ff949d29529e9bd2b3
        A/clauses/window-15/prompt.txt: a88075992a87efe9ea429568d49c7127f00fe73cdcb56239a7fb5e875e463183
        A/clauses/window-15/meta.json: 5469de5ba2023f673ab504a6bd7c770d53337141b1391209e54cc8c18ddd0f83
        A/clauses/window-12/raw.json: cd8140e237d095fb759fd697d6bbd405b48fff37766bc624daa3fa1d089b3066
        A/clauses/window-12/prompt.txt: 39397a27b4f35ead0e870b1935982437b0af72010e4abef1c44b46438028b2a4
        A/clauses/window-12/meta.json: c7f64b2e9974df3c4e9ade11e6c7808df52578f8bade1f1ee6a3c19c5ff26ead
        A/clauses/window-13/raw.json: 96e333a19375e6b77e722b545a3b23cb65801b52eaa47672af4d5f6de306d98b
        A/clauses/window-13/prompt.txt: 8575b0e8ba0ca18ff9edb53038cd95c4bce6d017402bf69b6319e091b932c54e
        A/clauses/window-13/meta.json: 8fc171bb4cad971bf4f09f8d015c4563285a059bd9ceab7158333febeb8a5c90
        A/clauses/window-14/raw.json: 5857c2f929367da7b8d39640628145323f6f3474be21e15f0832424e5e9a7b4f
        A/clauses/window-14/prompt.txt: ad2b47d237ba4c19902de8f0475f19d7c16d81933b03af74f978e3e14b48412d
        A/clauses/window-14/meta.json: 517ea81ad22d590c25340e0a8d42a87a0d013c22d6e7a2dc40bb96ada7593da8
        A/clauses/window-09/raw.json: 74093a92bbac5507d0f9ccee6cfe1bc9ea6571f92d385be5c1ae92e21b74fd97
        A/clauses/window-09/prompt.txt: 6c0676994845a49d1b917205f497d39fdf21f230f5061dee64a1eb77a3fa9a75
        A/clauses/window-09/meta.json: 572544476f1866c89d6179d187e93b5bdb09f290348de45f7475486c7f6f5683
        A/clauses/window-07/raw.json: b63bb52ad6fb6dcd8b9d84d0f328226da0fcad7add2d84bbc14ac0e37d1d32e4
        A/clauses/window-07/prompt.txt: bbc946ac1148f185d170a706fd2ea5f7da9f7755b4cf91ec71d34ccb2b3a8186
        A/clauses/window-07/meta.json: fcaf3727caf59bad3ba4489662301e6f5afbbe598a88a8cdd6d5e009d7bce674
        A/clauses/window-01/raw.json: be83b5cd796d23b188f6a94debea0985c1867e133a03842b1a972f6e970187bf
        A/clauses/window-01/prompt.txt: db76b3f0f4eadf088e788d7e159ea4bc14f2420bef8762b1f846207a239686c1
        A/clauses/window-01/meta.json: ed5bf754713b775f3898fc24902b8975b71e4e7f6a498784adb7407b225d5a96
        A/clauses/window-06/raw.json: 59b4f41d8c5bb30537072be2f3ab8b352292917d52762d3d09c49c32b4b5d130
        A/clauses/window-06/prompt.txt: e0f076e3ff535f42599c767b9e21e725ca132a9728a4fee1ecd1d35f7dd5fefa
        A/clauses/window-06/meta.json: 8a3f1b5116f9000dc73040b0bb10a32194637c6c1a61a3f879761ecec253df8c
        A/clauses/window-08/raw.json: e37ced19658b2bf444ec683c1c08696ce866f9bc2a5810aefbf7dd1910b97f2a
        A/clauses/window-08/prompt.txt: 0f9ac158a406ace68c66ef3fdde5cfcd6eb87d97d8acee553b638df10aa040b7
        A/clauses/window-08/meta.json: 707737d87d54c84448a6da39ea827b4546845e1313539b81298541fe2f2bee20
        A/tables/TABLE-1-page-5-1/raw.json: 13523c93b024287f2194a0296cb094e0d140d2e7153292bc447c531b6ba55443
        A/tables/TABLE-1-page-5-1/prompt.txt: 4923ed4c87de8e2fd36b885d7fe7ffd42853387a0926b6d9df7188bb666d6dca
        A/tables/TABLE-1-page-5-1/meta.json: 5a03449b343e8eb104937780298319711a512b65d277fe5e3fffacebaa4d671d
        A/tables/TABLE-2-page-6-3/raw.json: b7ae566e3719ac044b540f28d3828e0bb28eae66f7acc0e6b9e905a3fa02c8e6
        A/tables/TABLE-2-page-6-3/prompt.txt: 74cc6f1e12d9556df8a72a843305e27658cb45282950d9947242dee680e5b79f
        A/tables/TABLE-2-page-6-3/meta.json: 408b34d26e092afd37b987c2c7a482c1edc93fa7dffce49e99623f26cb2bc823
        A/tables/TABLE-1-page-5-2/raw.json: 5fb5f92c728f7c216889af910aa4a481aebbd97c364e5637d5e89e17b8aa18ce
        A/tables/TABLE-1-page-5-2/prompt.txt: 438f5813109ab5637c49d1ee8118821f32c70634ece20b72c5626a0bbc7499b3
        A/tables/TABLE-1-page-5-2/meta.json: 4a414dc128bd562971c741060465d72a59848ec214f68d7dc07660af33a36479
        A/tables/TABLE-3-page-7-4/raw.json: 73e32dac99a48aae10fe55e05fca0e02c41e707819e1c8af521ddaf3172f9561
        A/tables/TABLE-3-page-7-4/prompt.txt: 36b90f911351d1e22c3fa5c06d2817fbfc7daf41a06e232beb6e9f11440e0422
        A/tables/TABLE-3-page-7-4/meta.json: d833b7a2d9bdff47124b88f5392ae9aeab3edebacdd6eeaaeab33b6902a97bbb
        A/tables/TABLE-3-page-7-5/raw.json: 1d96a57a38abf7563c3a574a5259955e242b5727ce423bd4eeaca4042f2d79a9
        A/tables/TABLE-3-page-7-5/prompt.txt: 40adb341ecbf0ec6605467e85bfbf7ceb86a046fdba15aa4ca9c634e0cb8fe40
        A/tables/TABLE-3-page-7-5/meta.json: 77a596d3ddef514facb14e8c9b018d6e50e7d98329be80fe0d235932345877a4
        A/tables/TABLE-4-page-18-8/raw.json: 780e5eb3f5481281f87cf036284f1286678b12afa983c73c9b7c0493e8469f9a
        A/tables/TABLE-4-page-18-8/prompt.txt: 112d4c5567e64d241e483b4f55f07f004ad052e7dfde36f0277b2d6686b3c513
        A/tables/TABLE-4-page-18-8/meta.json: 955b7d104259aac9fdce4e3a95ad2138774cc10e37074f1a15b34229d6fe29bb
        A/tables/TABLE-3-page-8-6/raw.json: 51ba961f26f1100bcddd4ab9132bcf3006c7aacd310bddb4570f03e3620936a0
        A/tables/TABLE-3-page-8-6/prompt.txt: c559fc8e5b70f57b93dbb77474168434f95fc9fa99eaec4e710ce8d9f844b009
        A/tables/TABLE-3-page-8-6/meta.json: 0bcdfca3caa123e0de4bad8c23cc9110104a1c90e9a476f5eeda412dbba1a97b
        A/tables/TABLE-3-page-8-7/raw.json: e6654a608f0ac93135d85e85af3ad28f67476494435cb26a949ac11d34168aed
        A/tables/TABLE-3-page-8-7/prompt.txt: 667d134f54ac1e7c00fd273036c93c51420e263205c147a5c913fa6238539aa5
        A/tables/TABLE-3-page-8-7/meta.json: 24b462723624377dc3ed407ce766ac90a892f189a5e183f593cec8f13e9d6cd2
        B/passages.json: e6adde89dc789aab5279f2166f3c2e713cdc8eea67eeabf2953c2302d4eb19c1
        B/raw.json: 580a285abc1c899e4e664d09daae603317012386f634932aa81f24f2c4e3b0cf
        B/source-units.json: 28e3240c5d8e4f0ccf0ecf8bf46aa249f9787cdef2ec2956906e9452d5c8fc3d
        B/full-source-units.json: da7e50289e6929a62a0888cc4c5f5ef6bb50825e8033de28025ea0929ede949c
        B/meta.json: dec94fc2d1ef068fb67c92097f6a6d997fb15358381a67814ccae25dfe93d019
        B/table-images/TABLE-1-page-5-1.png: 7860a06eeb9516f7d99dff3d87334fb493345f088aa90d51b84ddd768eff9ad9
        B/table-images/TABLE-1-page-5-2.png: 9f048e6214ec6d261cec5f9692c1d1b30838ef69388f877c3f4f8981376790b7
        B/table-images/page-6.png: e977542b95ca428be2e8fe382c092f623666d97d4fd5c93ef7a82544062ec45f
        B/table-images/TABLE-3-page-8-1.png: 7e1b21cd3afdaaf1778185fcb8b6397dc0526df6147bd1988486665dd21227b7
        B/table-images/page-7.png: 7ef56e9a87e14d10e50a6e00252bbd176f2e682ec3fb12e95ce983909d722ecd
        B/table-images/page-5.png: 5723533e39e91b9ac343b861f3c501bfb1e3b8fde20c3e79c78d21154a060760
        B/table-images/TABLE-3-page-8-2.png: bc8629a5d005ea9576eca350466c26af69d6686b35515bbb690660cdab293ee1
        B/table-images/page-8.png: 99f4fadee855260bc500cfea051964cefbea4222a625876434da68bc0eb0a95d
        B/table-images/TABLE-2-page-6-1.png: ea39131c869819a05490e0e4883d6fef24170e824e3bbfb051c05d58c47bd465
        B/table-images/manifest.json: 40db755da72fc16c371158ab02ac76ac5fc9933c31e8492c433acdab73bc0c7b
        B/table-images/TABLE-3-page-7-2.png: 352ff11181c983583e22f3081b71c743d3e485965cddaf8a2dae408111932ea5
        B/table-images/TABLE-3-page-7-1.png: 8c6d6d932a4d10715e694be6d1cdcb31a5b3f5f4e853443068109884e6135f2d
        B/table-images/TABLE-4-page-18-1.png: 4b03bb2033e8ad1f280d5ba92ba9742f64de887859de01610b39f7d12613b858
        B/table-images/page-18.png: b5143e1cfc347287212e0e1bc986b8c98a695938a1c2194cff62d11dc0b4981e
        B/clauses/window-11/raw.json: 3ef8053455173a5822c762c1df101a9b77a41f75c8cc120f6a78dafe0f8717bd
        B/clauses/window-11/prompt.txt: 02de844e5f606a87584f6d3380808932cce3bfc879366b5f67dcdd832c1903db
        B/clauses/window-11/meta.json: 576ff3f0cb0f2b698986250c0bc918775c6abdfe87b8ea79827f595c1a28f239
        B/clauses/window-16/raw.json: d2832a16a9288e909545999d9138afbcb9f8e06260968d4c9eb42dbcd661b950
        B/clauses/window-16/prompt.txt: 2e037bb2a3edf201e8d9b236cec5646d17908322a692e191437d298238022f72
        B/clauses/window-16/meta.json: 22a6048e9dc2d044a2b593d29a5b420d053d626ab4b1f2c206d5fee6b0cc8d24
        B/clauses/window-10/raw.json: 9d4aedb3587670cf5f3e6ffcedd1359e0cbc661764c446f49ee78510602f3243
        B/clauses/window-10/prompt.txt: e0c3489c4996ffcad440ce89d7c7e1529d2ba52470558a55658662e484db5d87
        B/clauses/window-10/meta.json: 007649f5cc90b9db125da43e296dad9019249a8df59f2d8d57ccc96ce4b51887
        B/clauses/window-03/raw.json: 197e5fb8551ce928221ee2b1cb232dbd1351b7d3d7d4417abeb0245993c54b36
        B/clauses/window-03/prompt.txt: d47d3cf96239d8b94c0ae02fe5be9aa817522ca81c99136ff3aa2cbda0473023
        B/clauses/window-03/meta.json: 4dd234d628411833958221a79d9a82f4ac3d62dfde91b0976526ff6e78057e37
        B/clauses/window-04/raw.json: 4b95690428e25d7ad33bef8f581ee3133fbc787af76ed6f45dc85737f0d59d52
        B/clauses/window-04/prompt.txt: 609d1373fbfaa1e33f1f108b939a8f43731f80fe86c1ec3be37169bba09a25fb
        B/clauses/window-04/meta.json: 20e4a463637a96f4590b3396f886ce644088f9ea26053da50e709c0b4287b795
        B/clauses/window-05/raw.json: 405cc4ded1ee8f92d0f419f76c51c8f826e931a5df98fea990842a6927f822f2
        B/clauses/window-05/prompt.txt: 53499c6831ed56a0f869ed35f7cb059a11d837b138a40c7ed7a8519b9054550d
        B/clauses/window-05/meta.json: ed126b613afacc143d0d482561af05278d9405b5d61b682e7e2c967b24d33a90
        B/clauses/window-02/raw.json: 33cd7060eaca89feb3a560ab8d47f44907cc97b3d85155cbe111e5c75cb59ad1
        B/clauses/window-02/prompt.txt: e224210af1b6952e85bbe5a519fd3f1bb80cae3e5579512be94f66e5486b25c3
        B/clauses/window-02/meta.json: 0d7a8b5116cfe995a02f02d20bd0cf7061fd1adea83d1dd1e39d2e4e34d97d95
        B/clauses/window-15/raw.json: 7abbddd6923a9cdb7b63c91286322da771d3bb2da7046a2b297455853bbf9cff
        B/clauses/window-15/prompt.txt: a88075992a87efe9ea429568d49c7127f00fe73cdcb56239a7fb5e875e463183
        B/clauses/window-15/meta.json: 8fc60df013c7ef315f630b02edd673cc4d8c1d2a6b77032222d524bc3e43ebe4
        B/clauses/window-12/raw.json: fa54bea00252c570f13560faff6522ce35eda358c12c879e5a4aa3115cb681d5
        B/clauses/window-12/prompt.txt: 39397a27b4f35ead0e870b1935982437b0af72010e4abef1c44b46438028b2a4
        B/clauses/window-12/meta.json: b28b0105925689820e98d203454e16195d86df478e85bcc7e8c88e8546558092
        B/clauses/window-13/raw.json: 6c44e9f71a251ffb82fdf423c7504fb370530b6a76f060398814fe8e06a14ac3
        B/clauses/window-13/prompt.txt: 8575b0e8ba0ca18ff9edb53038cd95c4bce6d017402bf69b6319e091b932c54e
        B/clauses/window-13/meta.json: 117e065f5154cd9c4076ecfaf8e8b37e75f1d56664c63c6927d1479e7cc1dc23
        B/clauses/window-14/raw.json: 98c9ed7cdcb2c9ca2a20b99ebb7a5bdc80e3086bd3155e0a50aa592b25657bc0
        B/clauses/window-14/prompt.txt: ad2b47d237ba4c19902de8f0475f19d7c16d81933b03af74f978e3e14b48412d
        B/clauses/window-14/meta.json: ef49bf1567e155e2589ed5f3eef813a2b1bdddbbf6262947664862a9261519b9
        B/clauses/window-09/raw.json: 06802d7d460edf2a8644d7e7c863aa94bcbe8eef2ea0102a2d2617b6ee3b060d
        B/clauses/window-09/prompt.txt: 6c0676994845a49d1b917205f497d39fdf21f230f5061dee64a1eb77a3fa9a75
        B/clauses/window-09/meta.json: 9cc108f86be8a1eed9d76acaf6b1c6e3ed37819043b1aa8cf510ff1fdc06ded7
        B/clauses/window-07/raw.json: 90f4e5585460aaaf3c61946508bdf3e60a67e291cf6a81be7d71c4fa79f730f1
        B/clauses/window-07/prompt.txt: bbc946ac1148f185d170a706fd2ea5f7da9f7755b4cf91ec71d34ccb2b3a8186
        B/clauses/window-07/meta.json: 564b1d42364d4de6d8aab0ea6ac5c8fe2bf589829a6ce30538156d7e97da761b
        B/clauses/window-01/raw.json: 6c81a5338efd8489d0ee407aa52e945d0da6e8c948a1bfdd480a29df188fb11e
        B/clauses/window-01/prompt.txt: db76b3f0f4eadf088e788d7e159ea4bc14f2420bef8762b1f846207a239686c1
        B/clauses/window-01/meta.json: 82f8168392a0fd4df3fb6ffee12911e30941d33f0368aa565eaaaee2c9779e4c
        B/clauses/window-06/raw.json: 59b4f41d8c5bb30537072be2f3ab8b352292917d52762d3d09c49c32b4b5d130
        B/clauses/window-06/prompt.txt: e0f076e3ff535f42599c767b9e21e725ca132a9728a4fee1ecd1d35f7dd5fefa
        B/clauses/window-06/meta.json: 56ba6998027e9102f5ba9be7453d3b6ce9f4dfa16c2262c39d96af6021f4436b
        B/clauses/window-08/raw.json: a8ae22632c73c3c8e2d15c866364803e37a3070b9fc2f1d2123837c56de4f987
        B/clauses/window-08/prompt.txt: 0f9ac158a406ace68c66ef3fdde5cfcd6eb87d97d8acee553b638df10aa040b7
        B/clauses/window-08/meta.json: d2855c86bfc2bd63ab10a687cec6c7654022bbeb6f60c43ec3df8fb542fb51df
        B/tables/TABLE-1-page-5-1/raw.json: 142ad8df002009f0612f8dc61f35555868462cb26562c51a1f6fb6423ba847a7
        B/tables/TABLE-1-page-5-1/prompt.txt: 4923ed4c87de8e2fd36b885d7fe7ffd42853387a0926b6d9df7188bb666d6dca
        B/tables/TABLE-1-page-5-1/meta.json: 9cf492f356f15ca115452249938c168049d58e18eb714615701c6d34932c0f25
        B/tables/TABLE-2-page-6-3/raw.json: 8fc4069d8cc9173d943358e5b9a77a1da72ee167efd010ca70b7ce2097cb5e7d
        B/tables/TABLE-2-page-6-3/prompt.txt: 74cc6f1e12d9556df8a72a843305e27658cb45282950d9947242dee680e5b79f
        B/tables/TABLE-2-page-6-3/meta.json: a6df65c930157c2dfde8040086d5319c79e983f253e0dc16ba25fea24e54f342
        B/tables/TABLE-1-page-5-2/raw.json: 82c21bbd3e05488f249e479b56f10c0cd2f9fa85a11afb644d7d257d08cc0397
        B/tables/TABLE-1-page-5-2/prompt.txt: 438f5813109ab5637c49d1ee8118821f32c70634ece20b72c5626a0bbc7499b3
        B/tables/TABLE-1-page-5-2/meta.json: 2b88a4e6e0844a8d1e16a47e39d777b94e6be2adf078beaaf8218427487581a7
        B/tables/TABLE-3-page-7-4/raw.json: 41390a74bd5c4285288a6a2ef6c52d6215c322956a34899a67edbb6bcd2e6deb
        B/tables/TABLE-3-page-7-4/prompt.txt: 36b90f911351d1e22c3fa5c06d2817fbfc7daf41a06e232beb6e9f11440e0422
        B/tables/TABLE-3-page-7-4/meta.json: 5865a6c910fe5b717052bc014f4dc87d28a5759a72ab7df684248107a5d1cbb1
        B/tables/TABLE-3-page-7-5/raw.json: 3a8c1b9314ebf70c85c56b63e36e3a22f10f5010a92409128d3341fa80619f95
        B/tables/TABLE-3-page-7-5/prompt.txt: 40adb341ecbf0ec6605467e85bfbf7ceb86a046fdba15aa4ca9c634e0cb8fe40
        B/tables/TABLE-3-page-7-5/meta.json: 2489f6814589739f9d46bc23826a8bd37ce298ff74bce1275c2adf6fc9805c33
        B/tables/TABLE-4-page-18-8/raw.json: de18824deb7637e2c845d9a9fb2e5e56b91feac7dd1483395b74b5a19e6a6522
        B/tables/TABLE-4-page-18-8/prompt.txt: 112d4c5567e64d241e483b4f55f07f004ad052e7dfde36f0277b2d6686b3c513
        B/tables/TABLE-4-page-18-8/meta.json: 558729a62e4b268af0640096f0ebd4d274bb256e056e90836d719ad03edfcc5b
        B/tables/TABLE-3-page-8-6/raw.json: 82437e9debb0f8ccc2e78d8e45a9e64714d531a5060db86bdc5e689464a17c02
        B/tables/TABLE-3-page-8-6/prompt.txt: c559fc8e5b70f57b93dbb77474168434f95fc9fa99eaec4e710ce8d9f844b009
        B/tables/TABLE-3-page-8-6/meta.json: 3ddb794d62a48bf4462d524f28f028f8d2eadde4b36d952334dacb7600236131
        B/tables/TABLE-3-page-8-7/raw.json: 54d8555f68e683c81d4de738d1033d4df8cc2c9755e4a6cc98f141b30db64ed7
        B/tables/TABLE-3-page-8-7/prompt.txt: 667d134f54ac1e7c00fd273036c93c51420e263205c147a5c913fa6238539aa5
        B/tables/TABLE-3-page-8-7/meta.json: 9bd1de39fc0d4c25d7e6f7f056bf4eb50c95a23ca464491227b379c156624c47
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
      pdf_sha256: a58a5b9ea30eebd639e26d9c87b6e18640880907f66e87ba64024e442ba702b4
      source_review: _compare/relationships-2026-11-16/review-current/Rogalsky2018
      source_status_sha256: ce35ce23bb9573393d4a40e5d5dcc78d3cfe86988c682f2fceddf1ff57548e00
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R005
    exposure:
      text: Noncanonical sentence performance (controlling for canonical performance)
    outcome:
      text: Brain region association
    analysis_label: Voxel-based Lesion-Symptom Mapping (Covariate Approach)
    relation: association
    evidence_ids:
    - P1-S1-C12
    - P12-S1-C5
    - P16-S2-C4
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
      pdf_sha256: a58a5b9ea30eebd639e26d9c87b6e18640880907f66e87ba64024e442ba702b4
      source_review: _compare/relationships-2026-11-16/review-current/Rogalsky2018
      source_status_sha256: ce35ce23bb9573393d4a40e5d5dcc78d3cfe86988c682f2fceddf1ff57548e00
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P1-S1-C10
      - Result passage disposed without unit P1-S1-C11
      - Accounting without a linked unit P1-S1-C12
      - Accounting without a linked unit P1-S1-C13
      - Accounting without a linked unit P1-S2-C1
      - Unaccounted source passage P1-S1-C13
      - Unaccounted source passage P1-S2-C1
      - Unaccounted source passage P1-S1-C12
      - Result passage disposed without unit P4-S3-C7
      - Accounting without a linked unit P6-S2-C7
      - Unaccounted source passage P6-S2-C7
      - Accounting without a linked unit P10-S2-C3
      - Result passage disposed without unit P10-S2-C4
      - Accounting without a linked unit P10-S2-C7
      - Unaccounted source passage P10-S2-C7
      - Unaccounted source passage P10-S2-C3
      - Result passage disposed without unit P11-S1-C4
      - Result passage disposed without unit P11-S1-C6
      - Accounting without a linked unit P11-S1-C8
      - Accounting without a linked unit P11-S2-C2
      - Accounting without a linked unit P12-S1-C1
      - Accounting without a linked unit P12-S1-C2
      - Result passage disposed without unit P12-S1-C3
      - Unaccounted source passage P11-S2-C2
      - Unaccounted source passage P11-S1-C8
      - Unaccounted source passage P12-S1-C2
      - Unaccounted source passage P12-S1-C1
      - Result passage disposed without unit P14-S1-C1
      - Result passage disposed without unit P14-S1-C4
      - Accounting without a linked unit P14-S1-C6
      - Result passage disposed without unit P14-S1-C7
      - Accounting without a linked unit P15-S1-C2
      - Unaccounted source passage P14-S1-C6
      - Unaccounted source passage P15-S1-C2
      - Accounting without a linked unit P15-S1-C4
      - Accounting without a linked unit P15-S1-C5
      - Accounting without a linked unit P16-S1-C1
      - Accounting without a linked unit P16-S1-C5
      - Accounting without a linked unit P16-S1-C6
      - Accounting without a linked unit P16-S1-C7
      - Accounting without a linked unit P16-S1-C8
      - Unaccounted source passage P15-S1-C5
      - Unaccounted source passage P16-S1-C5
      - Unaccounted source passage P16-S1-C1
      - Unaccounted source passage P16-S1-C8
      - Unaccounted source passage P16-S1-C6
      - Unaccounted source passage P16-S1-C7
      - Unaccounted source passage P15-S1-C4
      - Result passage disposed without unit P16-S3-C3
      - Result passage disposed without unit P16-S3-C6
      - Accounting without a linked unit P16-S3-C7
      - Accounting without a linked unit P17-S1-C1
      - Accounting without a linked unit P17-S1-C2
      - Result passage disposed without unit P17-S1-C3
      - Unaccounted source passage P17-S1-C1
      - Unaccounted source passage P17-S1-C2
      - Unaccounted source passage P16-S3-C7
      - Result passage disposed without unit P18-S1-C11
      - Unresolved source passage P18-S1-C12
      - Unresolved source passage P18-S2-C1
      - Accounting without a linked unit P18-S2-C3
      - Accounting without a linked unit P18-S2-C4
      - Accounting without a linked unit P18-S2-C5
      - Accounting without a linked unit P18-S2-C6
      - Unaccounted source passage P18-S2-C5
      - Unaccounted source passage P18-S2-C3
      - Unaccounted source passage P18-S2-C4
      - Unaccounted source passage P18-S2-C6
      - Result passage disposed without unit P19-S1-C8
      unattached_null_or_qualifier_ids:
      - P1-S1-C10
      - P6-S1-C7
      - P10-S2-C3
      - P11-S1-C4
      - P11-S2-C2
      - P12-S1-C2
      - P14-S1-C7
      - P15-S1-C4
      - P16-S1-C5
      suppressed_nonrepresented_units: 21
      default_disposition_count_requires_completeness_check: 307
      unselected_timing_passages:
      - P1-S1-C7
      - P2-S3-C2
      - P2-S3-C5
      - P3-S1-C1
      - P5-S1-C1
      - P14-S1-C9
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P12-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S2-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S1-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P14-S1-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P14-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P9-S2-C9
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P10-S1-C1
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P10-S1-C3
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: imaging_provenance
        source_ids:
        - P6-S3-C2
        - P6-S3-C4
        - P6-S3-C8
        - P9-S2-C2
        - P9-S2-C11
        - P9-S2-C12
        - P9-S2-C13
        - P10-S1-C1
        - P10-S1-C13
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - imaging_provenance
      - validation
      - personal_factors
      - tested_personal_effects
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-5-1
      - TABLE-1-page-5-2
      - TABLE-2-page-6-3
      - TABLE-3-page-7-4
      - TABLE-3-page-7-5
      - TABLE-3-page-8-6
      - TABLE-3-page-8-7
      - TABLE-4-page-18-8
      unlinked_tables:
      - TABLE-1-page-5-1
      - TABLE-1-page-5-2
      - TABLE-2-page-6-3
      - TABLE-3-page-7-4
      - TABLE-3-page-7-5
      - TABLE-3-page-8-6
      - TABLE-3-page-8-7
      - TABLE-4-page-18-8
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P8-S1
        - P9-S2
        - P10-S2
        - P11-S1
        - P11-S2
        - P12-S1
        - P12-S2
        - P13-S1
        - P14-S1
        - P15-S1
        - P16-S2
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: a58a5b9ea30eebd639e26d9c87b6e18640880907f66e87ba64024e442ba702b4
      source_review: _compare/relationships-2026-11-16/review-current/Rogalsky2018
      source_status_sha256: ce35ce23bb9573393d4a40e5d5dcc78d3cfe86988c682f2fceddf1ff57548e00
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C9
      disposition: represented
      result_indexes:
      - 0
      reason: Reports Broca's group performance on noncanonical sentences.
    - source_id: P1-S1-C10
      disposition: represented
      result_indexes:
      - 1
      reason: Reports ATL group performance on agrammatic patterns.
    - source_id: P1-S1-C11
      disposition: represented
      result_indexes:
      - 2
      reason: Identifies overlap in posterior superior temporal and inferior parietal
        regions for agrammatic patterns.
    - source_id: P1-S1-C12
      disposition: represented
      result_indexes:
      - 4
      reason: VLSM associating noncanonical performance with superior temporal-inferior
        parietal network.
    - source_id: P1-S1-C13
      disposition: represented
      result_indexes:
      - 7
      reason: Associates response bias with inferior frontal cortex/Broca's area.
    - source_id: P1-S2-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Introductory text regarding Broca's area.
    - source_id: P4-S3-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement of hypothesis failure.
    - source_id: P4-S3-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: General summary of data trends.
    - source_id: P6-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Demographic/clinical subtype description.
    - source_id: P6-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Demographic description of non-impaired patients.
    - source_id: P6-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of task stimuli.
    - source_id: P10-S1-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Section header.
    - source_id: P10-S2-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Introduction to behavioral results.
    - source_id: P10-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Main effect of sentence type in SOAP task.
    - source_id: P10-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Lack of main effect of group.
    - source_id: P10-S2-C7
      disposition: represented
      result_indexes:
      - 0
      reason: Null result for Broca's group in SOAP task.
    - source_id: P10-S2-C8
      disposition: represented
      result_indexes:
      - 1
      reason: Significant difference for ATL group in SOAP task.
    - source_id: P10-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Main effect of sentence type in plausibility task.
    - source_id: P10-S3-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Main effect of sentence type in plausibility task.
    - source_id: P10-S3-C3
      disposition: represented
      result_indexes:
      - 0
      reason: Null result for Broca's group in plausibility task.
    - source_id: P10-S3-C4
      disposition: represented
      result_indexes:
      - 1
      reason: Non-significant difference for ATL group in plausibility task.
    - source_id: P10-S3-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Descriptive mean performance scores.
    - source_id: P11-S1-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to Figure 3.
    - source_id: P11-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Count of patients with agrammatic patterns.
    - source_id: P11-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Count of patients with agrammatic patterns.
    - source_id: P11-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Null result for Liebermeister tests.
    - source_id: P11-S1-C8
      disposition: represented
      result_indexes:
      - 2
      reason: Maximum overlap for agrammatic group in SOAP task.
    - source_id: P12-S1-C1
      disposition: represented
      result_indexes:
      - 3
      reason: Overlap for agrammatic group in plausibility task.
    - source_id: P12-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Overlap for non-agrammatic group.
    - source_id: P12-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Summary statement of ROI/overlap results.
    - source_id: P12-S1-C5
      disposition: represented
      result_indexes:
      - 4
      reason: VLSM results for noncanonical performance.
    - source_id: P12-S1-C7
      disposition: repeated
      result_indexes:
      - 4
      reason: Restatement of VLSM findings.
    - source_id: P12-S2-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of VLSM approach.
    - source_id: P13-S1-C1
      disposition: represented
      result_indexes:
      - 5
      reason: VLSM for overall performance.
    - source_id: P13-S1-C3
      disposition: represented
      result_indexes:
      - 5
      reason: Identifies ATL involvement in overall performance.
    - source_id: P13-S1-C4
      disposition: represented
      result_indexes:
      - 6
      reason: VLSM for specific sentence types.
    - source_id: P14-S1-C1
      disposition: represented
      result_indexes:
      - 6
      reason: Null result for frontal regions in sentence type VLSM.
    - source_id: P14-S1-C6
      disposition: represented
      result_indexes:
      - 7
      reason: VLSM identifying inferior frontal gyrus for response bias.
    - source_id: P15-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement of similar behavioral performance.
    - source_id: P15-S1-C3
      disposition: represented
      result_indexes:
      - 0
      reason: Restatement of null result for Broca's group.
    - source_id: P15-S1-C4
      disposition: represented
      result_indexes:
      - 1
      reason: Restatement of ATL group results.
    - source_id: P16-S1-C5
      disposition: represented
      result_indexes:
      - 2
      - 3
      reason: Summary of agrammatic overlap results.
    - source_id: P16-S1-C6
      disposition: represented
      result_indexes:
      - 2
      reason: Identifies posterior STG as maximum overlap.
    - source_id: P16-S2-C4
      disposition: represented
      result_indexes:
      - 4
      reason: Restatement of noncanonical VLSM results.
    - source_id: P16-S3-C7
      disposition: represented
      result_indexes:
      - 5
      - 6
      reason: Summary of overall and sentence-type VLSM results.
    - source_id: P17-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: General summary of Broca's area null results.
    - source_id: P18-S2-C3
      disposition: repeated
      result_indexes:
      - 0
      - 1
      reason: Conclusion restating ROI results.
    - source_id: P18-S2-C4
      disposition: repeated
      result_indexes:
      - 2
      - 3
      reason: Conclusion restating overlap results.
    - source_id: P18-S2-C5
      disposition: repeated
      result_indexes:
      - 4
      reason: Conclusion restating noncanonical VLSM results.
    - source_id: P18-S2-C6
      disposition: repeated
      result_indexes:
      - 5
      - 6
      reason: Conclusion restating whole-sample VLSM results.
    unresolved_coverage:
    - source_id: P12-S2-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P11-S2-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S1-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S2-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S1-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P14-S1-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P14-S1-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P15-S1-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P16-S1-C1
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P16-S1-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P16-S1-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P16-S1-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P16-S2-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P16-S2-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P16-S2-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P16-S2-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P16-S2-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P16-S2-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P16-S3-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P16-S3-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P16-S3-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P17-S1-C1
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P17-S1-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P17-S1-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P17-S1-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P17-S1-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P17-S1-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P17-S2-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P18-S1-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P18-S1-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P18-S2-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P19-S1-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S2-C1
    - P4-S3-C7
    - P4-S3-C8
    - P6-S1-C6
    - P6-S1-C7
    - P6-S2-C7
    - P10-S1-C14
    - P10-S2-C1
    - P10-S2-C3
    - P10-S2-C4
    - P10-S2-C9
    - P10-S3-C1
    - P10-S3-C3
    - P10-S3-C4
    - P10-S3-C5
    - P11-S1-C1
    - P11-S1-C3
    - P11-S1-C4
    - P11-S1-C6
    - P11-S2-C2
    - P12-S1-C2
    - P12-S1-C3
    - P12-S1-C6
    - P12-S1-C7
    - P12-S2-C2
    - P13-S1-C2
    - P14-S1-C4
    - P14-S1-C7
    - P15-S1-C2
    - P15-S1-C5
    - P16-S1-C1
    - P16-S1-C7
    - P16-S1-C8
    - P16-S1-C9
    - P16-S2-C5
    - P16-S2-C6
    - P16-S2-C7
    - P16-S2-C8
    - P16-S2-C9
    - P16-S2-C10
    - P16-S3-C3
    - P16-S3-C6
    - P16-S3-C8
    - P17-S1-C1
    - P17-S1-C2
    - P17-S1-C3
    - P17-S1-C5
    - P17-S1-C6
    - P17-S1-C7
    - P17-S1-C8
    - P17-S2-C9
    - P18-S1-C4
    - P18-S1-C11
    - P18-S2-C3
    - P18-S2-C4
    - P18-S2-C5
    - P18-S2-C6
    - P18-S2-C7
    - P19-S1-C8
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-5-1
    - TABLE-1-page-5-2
    - TABLE-2-page-6-3
    - TABLE-3-page-7-4
    - TABLE-3-page-7-5
    - TABLE-3-page-8-6
    - TABLE-3-page-8-7
    - TABLE-4-page-18-8
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P4-S3-C10
      - P5-S1-C1
      recruited_sample:
      - P4-S3-C9
      - P5-S1-C1
      eligibility:
      - P5-S1-C1
      - P6-S1-C3
      - P6-S1-C4
      imaging_provenance: []
      imaging_timing:
      - P3-S1-C8
      - P18-S1-C7
      - P18-S1-C8
      outcome_timing:
      - P3-S1-C8
      - P18-S1-C7
      - P18-S1-C8
      outcome_definition:
      - P4-S2-C8
      - P4-S2-C10
      - P9-S1-C10
      - P11-S1-C3
      validation: []
      analysis_restrictions:
      - P9-S2-C3
      - P9-S2-C4
      - P10-S1-C5
      dependent_variable_statement:
      - P6-S2-C14
      - P8-S1-C8
      - P9-S1-C2
      - P10-S2-C2
      limitations:
      - P4-S1-C10
      - P4-S1-C11
      - P16-S1-C4
      - P16-S3-C4
      - P19-S1-C5
      - P19-S1-C6
      - P19-S1-C7
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P4-S3-C5
      - P9-S2-C3
      - P9-S2-C4
      - P10-S1-C5
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P5-S1-C1
      - P5-S1-C4
      - P6-S1-C4
      - P6-S1-C6
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P12-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S2-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S1-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P14-S1-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P14-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P9-S2-C9
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P10-S1-C1
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P10-S1-C3
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: imaging_provenance
      source_ids:
      - P6-S3-C2
      - P6-S3-C4
      - P6-S3-C8
      - P9-S2-C2
      - P9-S2-C11
      - P9-S2-C12
      - P9-S2-C13
      - P10-S1-C1
      - P10-S1-C13
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
      pdf_sha256: a58a5b9ea30eebd639e26d9c87b6e18640880907f66e87ba64024e442ba702b4
      review_sha256: 5c3d62d4c0072faaae65f9512bd50e2fc678ee126634127f5fceb18fb432270c
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
      - P1-S1-C12
      - P12-S1-C5
      - P16-S2-C4
      source_result: Voxel-based lesion-symptom mapping (VLSM) using a covariate approach
        (regressing out canonical sentence performance) identified significant associations
        between lower performance on noncanonical sentences and damage to a large
        left superior temporal-inferior parietal network (including Heschl's gyrus,
        STG, middle temporal gyrus, and supramarginal gyrus) in both the sentence-picture
        matching and plausibility judgment tasks. No significant association was found
        for Broca's area.
      result_status: detected
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The draft correctly identifies the analysis as VLSM with a covariate
            approach for noncanonical sentence performance, matching the source description
            in P9-S2-C3 and P12-S1-C5.
          source_ids:
          - P9-S2-C3
          - P12-S1-C5
          - P16-S2-C4
        direction:
          answer: fits
          reason: The draft correctly states that lower performance is associated
            with damage to the temporal-parietal network and explicitly notes the
            lack of association with Broca's area, consistent with P1-S1-C12 and P16-S2-C9.
          source_ids:
          - P1-S1-C12
          - P16-S2-C9
        construct:
          answer: fits
          reason: The exposure (noncanonical performance controlling for canonical)
            and outcome (brain region association via lesion overlap) are correctly
            described. The patient measurement is correctly identified as template
            lesion overlap (VLSM), not patient diffusion or functional imaging.
          source_ids:
          - P1-S1-C12
          - P12-S1-C5
          - P6-S3-C4
        qualifications:
          answer: fits
          reason: The draft includes the key qualification that canonical performance
            was regressed out (covariate approach) and that findings were consistent
            across tasks. It also notes the limitation regarding neural reorganization
            in the temporal lobectomy group, which is relevant to the ATL findings
            discussed in P16-S1-C4.
          source_ids:
          - P9-S2-C3
          - P16-S1-C4
          - P16-S2-C4
        missing_material_caveat:
          answer: fits
          reason: No material caveats are missing. The draft correctly reflects the
            null finding for Broca's area and the positive finding for the temporal-parietal
            network. The limitation regarding neural reorganization is included. The
            sample size is noted as pending, which is appropriate for a qualitative
            draft.
          source_ids:
          - P16-S3-C3
          - P16-S3-C4
          - P16-S3-C5
      optional_pending:
      - Sample size (n=66) is mentioned in source but not transcribed in draft fields
      - Specific Talairach coordinates and voxel counts are not transcribed
      - Exact p-values and cluster thresholds are not transcribed
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Sample size requires source confirmation; it has not been transcribed.
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Sample size (n=66) is mentioned in source but not transcribed in draft fields
    - Specific Talairach coordinates and voxel counts are not transcribed
    - Exact p-values and cluster thresholds are not transcribed
    normalizations:
    - field: sample.n
      original: 66
      action: not_transcribed
      reason: Not supported by selected quotations
    analysis_identity:
      id: R005
      exposure:
        text: Noncanonical sentence performance (controlling for canonical performance)
      outcome:
        text: Brain region association
      analysis_label: Voxel-based Lesion-Symptom Mapping (Covariate Approach)
      relation: association
      evidence_ids:
      - P1-S1-C12
      - P12-S1-C5
      - P16-S2-C4
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
        pdf_sha256: a58a5b9ea30eebd639e26d9c87b6e18640880907f66e87ba64024e442ba702b4
        source_review: _compare/relationships-2026-11-16/review-current/Rogalsky2018
        source_status_sha256: ce35ce23bb9573393d4a40e5d5dcc78d3cfe86988c682f2fceddf1ff57548e00
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P5-S1-C1:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: a58a5b9ea30eebd639e26d9c87b6e18640880907f66e87ba64024e442ba702b4
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 652483db501e7f826d900ebdcbb797a0f7cbbf742db2dc369128acfe38e60a42
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P5-S1-C1
          page: 5
          text_layer_sha256: a32bd944e0e475df6f3fe9e7ef517e64554a5b31f3ccd0a0018ebcc97dd287b9
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: '

          chronic focal (6 months or more postonset) lesion due to

          a stroke in the left hemisphere (n = 48; 17 women, mean

          age = 62 years, range = 31–84 years) or a unilateral left tem-

          poral lobectomy (n = 18; 10 women, mean age = 46 years,

          range = 29–62 years),2 (ii) no significant anatomical abnor-

          malities other than the signature lesion of their vascular

          event (or evidence of surgery for the seizure participants)

          nor signs of multiple strokes, and (iii) were administered

          both of the comprehension tasks of interest.'
        anchor_text: 'chronic focal (6 months or more postonset) lesion due to

          a stroke in the left hemisphere (n = 48; 17 women, mean

          age = 62 years, range = 31–84 years) or a unilateral left tem-

          poral lobectomy (n = 18; 10 women, mean age = 46 years,

          range = 29–62 years),2 (ii) no significant anatomical abnor-

          malities other than the signature lesion of their vascular

          event (or evidence of surgery for the seizure participants)

          nor signs of multiple strokes, and (iii) were administered

          both of the comprehension tasks of interest.'
        excluded_fragments: []
        image_sha256: 9823204a98c76e4372b195163abff335b9b16c831aec08aea5bff77897e82e66
        transcription: 'chronic focal (6 months or more postonset) lesion due to

          a stroke in the left hemisphere (n = 48; 17 women, mean

          age = 62 years, range = 31–84 years) or a unilateral left tem-

          poral lobectomy (n = 18; 10 women, mean age = 46 years,

          range = 29–62 years),² (ii) no significant anatomical abnor-

          malities other than the signature lesion of their vascular

          event (or evidence of surgery for the seizure participants)

          nor signs of multiple strokes, and (iii) were administered

          both of the comprehension tasks of interest'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 1
  quote: 'Using

    voxel-based lesion–symptom mapping, we find that lower per-

    formances on canonical and noncanonical sentences in each

    task are both associated with damage to a large left superior

    temporal–inferior parietal network including portions of the

    ATL, but not Broca’s area.'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-25'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
